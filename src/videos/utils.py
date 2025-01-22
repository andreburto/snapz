import boto3
import json
import os
import requests

from datetime import datetime

OPENAI_MODEL = "gpt-4-turbo"
OPENAI_PROMPT = """
Describe the image.
Create a three sentence description. 
Include a list of ten tags.
Present this information in JSON format using description and tag as elements."
""".replace("\n", " ").replace("\r", "").strip()


def generate_description(image_path):
    # Make file name
    bucket_name = os.getenv("BUCKET_NAME")
    object_name = f"{datetime.now().strftime('%Y%m%d%H%I%S')}.png"

    # Upload file to S3
    client_s3 = boto3.client(
      's3',
      aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
      aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
    client_s3.upload_file(image_path, bucket_name, object_name)

    headers = {
      "Content-Type": "application/json",
      "Authorization": f'Bearer {os.getenv("OPENAI_KEY")}'
    }

    payload = {
      "model": OPENAI_MODEL,
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": OPENAI_PROMPT
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"http://{bucket_name}.s3.amazonaws.com/{object_name}"
              }
            }
          ]
        }
      ],
      "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    client_s3.delete_object(Bucket=bucket_name, Key=object_name)
    json_response = response.json().get("choices")[0].get("message").get("content")
    openai_response_json = json.loads(json_response.replace("```", "")[4:].strip())

    if "description" not in openai_response_json:
        raise ValueError("Description not found in OpenAI response.")

    if not isinstance(openai_response_json["tags"], list):
        raise ValueError("Tag not found in OpenAI response.")

    return openai_response_json

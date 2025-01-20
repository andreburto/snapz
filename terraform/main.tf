terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    encrypt = true
    bucket = "mothersect-tf-state"
    dynamodb_table = "mothersect-tf-state-lock"
    key    = "describer"
    region = "us-east-1"
  }
}

locals {
  index_file = "index.html"
}

# Configure the AWS Provider
provider "aws" {
  region = var.aws_region
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}

resource "aws_s3_bucket" "describer" {
  bucket = var.bucket_name

  tags = {
    Name        = var.bucket_name
    Environment = "development"
  }
}

resource "aws_s3_bucket_public_access_block" "describer" {
  bucket = aws_s3_bucket.describer.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
  
}

// create an s3 bucket policy for a static website
resource "aws_s3_bucket_policy" "describer" {
  bucket = aws_s3_bucket.describer.id

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = "*",
        Action = "s3:GetObject",
        Resource = "${aws_s3_bucket.describer.arn}/*",
      },
      {
        Effect = "Allow",
        Principal = {
          "AWS": "arn:aws:iam::${var.aws_account_id}:root"
        },
        Action = ["s3:*"],
        Resource = [
          "${aws_s3_bucket.describer.arn}",
          "${aws_s3_bucket.describer.arn}/*"
        ],
      },
    ],
  })
}

// enable static website hosting
resource "aws_s3_bucket_website_configuration" "describer" {
  bucket = aws_s3_bucket.describer.id

  index_document {
    suffix = "index.html"
  }
}

resource "aws_s3_object" "index" {
  bucket = aws_s3_bucket.describer.bucket
  key    = local.index_file
  source = local.index_file
  content_type = "text/html"
  etag = filemd5(local.index_file)
}

# DNS stuff
resource "aws_route53_record" "describer" {
  zone_id = var.zone_id
  name    = "${var.bucket_name}."
  type    = "A"

  alias {
    name                   = aws_s3_bucket.describer.website_domain
    zone_id                = aws_s3_bucket.describer.hosted_zone_id
    evaluate_target_health = false
  }
}

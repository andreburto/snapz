variable "aws_access_key" {
  type = string
}

variable "aws_secret_key" {
  type = string
}

variable "aws_account_id" {
  type = string
}

variable "aws_region" {
  type = string
  default = "us-east-1"
}

variable "bucket_name" {
  type    = string
  default = "describer.mothersect.info"
}

variable "zone_id" {
  type    = string
  default = "ZMWA8O6ANKCDQ"
}
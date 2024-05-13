terraform {
  backend "s3" {
    region = "us-west-2"
    bucket = "hm-terraform-bucket"
    key    = "development/snowflake/general/terraform.tfstate"
  }
  required_providers {
    # https://registry.terraform.io/providers/Snowflake-Labs/snowflake/latest
    snowflake = {
      source  = "Snowflake-Labs/snowflake"
      version = "0.90.0"
    }
  }
  required_version = ">= 1.8"
}
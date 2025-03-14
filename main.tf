provider "aws" {
  region = "eu-west-2"  # Specify the AWS region (London)
}

resource "aws_s3_bucket" "frontend_bucket" {
  bucket = "sentimentpress-frontend-1"  # Change this to a globally unique bucket name
}

resource "aws_s3_bucket_ownership_controls" "frontend_bucket_ownership" {
  bucket = aws_s3_bucket.frontend_bucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_public_access_block" "frontend_bucket_public_access" {
  bucket = aws_s3_bucket.frontend_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_policy" "frontend_bucket_policy" {
  bucket = aws_s3_bucket.frontend_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "PublicReadGetObject"
        Effect    = "Allow"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource = [
          "${aws_s3_bucket.frontend_bucket.arn}/*"
        ]
      }
    ]
  })

  depends_on = [aws_s3_bucket_public_access_block.frontend_bucket_public_access]
}

resource "aws_s3_bucket_website_configuration" "frontend_bucket_website" {
  bucket = aws_s3_bucket.frontend_bucket.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "index.html"  # Ensures SPA routing works
  }
}

resource "aws_s3_object" "frontend_files" {
  for_each = fileset("sentiment-press-frontend/build", "**/*")
  bucket   = aws_s3_bucket.frontend_bucket.bucket
  key      = each.value
  source   = "sentiment-press-frontend/build/${each.value}"
  etag     = filemd5("sentiment-press-frontend/build/${each.value}")

  content_type = lookup({
    "html" = "text/html",
    "js"   = "application/javascript",
    "css"  = "text/css",
    "json" = "application/json",
    "png"  = "image/png",
    "jpg"  = "image/jpeg",
    "jpeg" = "image/jpeg",
    "gif"  = "image/gif",
    "svg"  = "image/svg+xml",
    "txt"  = "text/plain",
    "ico"  = "image/x-icon"
  }, split(".", each.value)[length(split(".", each.value)) - 1], "application/octet-stream")
}

output "website_url" {
  value = aws_s3_bucket_website_configuration.frontend_bucket_website.website_endpoint
}

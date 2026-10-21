---
url: https://docs.cloud.google.com/storage-transfer/docs/s3-cloudfront/
title: Transfer from S3 via CloudFront \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:46.403102+00:00
---

# Transfer from S3 via CloudFront  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/s3-cloudfront/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Transfer from S3 via CloudFront Stay organized with collections  Save and categorize content based on your preferences. 

Transfers from Amazon S3 can use an [Amazon CloudFront](https://aws.amazon.com/cloudfront/) distribution as an egress path.

Data transfers through CloudFront may benefit from lower AWS egress costs compared to transferring directly from S3. See [CloudFront pricing](https://aws.amazon.com/cloudfront/pricing/) and [S3 egress charges](https://aws.amazon.com/s3/pricing/) for details. 

Using CloudFront as the egress path does not expose your S3 objects to the public. See Does using CloudFront expose my objects to the public?

## Overview

In order to transfer S3 data through CloudFront, you must follow these steps:

  * Configure IAM permissions
  * Configure access to your S3 bucket
  * Create a CloudFront distribution for your S3 bucket
  * Create a transfer job



## Configure IAM permissions

Follow the instructions in [Agentless transfer permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-cloud) to grant the required Google Cloud permissions.

## Configure access to your S3 bucket

Follow the instructions in [Configure access to a source: Amazon S3](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3) to configure access to your data in Amazon S3.

## Create a CloudFront distribution for your S3 bucket

  1. In your AWS account, go to **CloudFront**.
  2. Click **Create a CloudFront distribution**.
  3. Under **Origin domain** select your S3 bucket.
  4. **Origin path** must be left empty.
  5. Accept the auto-filled **Origin name** or specify your own value.
  6. In the **Origin access** section, select _Public_. This does not make your bucket public; instead it indicates to CloudFront that no access mechanism should be configured.
  7. In the **Cache key and origin requests** section: 
     1. For **Cache policy** select _CachingDisabled_. This prevents CloudFront from caching requests and serving them to unauthenticated viewers.
     2. For **Origin request policy** select _AllViewerExceptHostHeader_. This allows CloudFront to forward authentication headers to S3, so that Storage Transfer Service can access your bucket with your secure credentials.
  8. In the **Web Application Firewall (WAF)** section, select _Do not enable_.
  9. Optionally, choose a **Price class**. Storage Transfer Service selects worker pools based on the source bucket's region, so CloudFront pricing is incurred in that region. To obtain the lowest pricing, either ensure that your source bucket is in the US or Europe, or select _Use only North America and Europe_ as the **Price class** in CloudFront. 
  10. Click **Create CloudFront distribution**.

Once successfully created, the CloudFront distribution details page is displayed.

  11. Note the **Distribution domain name**. For example: `https://dy1h2n3l4ob56.cloudfront.net`. If the details page doesn't include the `https://` protocol in front of the distribution domain name, you'll need to add it yourself when creating the transfer job.




## Create a transfer job

Transferring via a CloudFront distribution is supported in the Google Cloud console and the REST API.

Don't include sensitive information such as personally identifiable information (PII) or security data in your transfer job name. Resource names may be propagated to the names of other Google Cloud resources and may be exposed to Google-internal systems outside of your project. 

###  Google Cloud console 

To create a transfer using a the Google Cloud console, follow the instructions to [create a transfer](https://docs.cloud.google.com/storage-transfer/docs/create-transfers?tab=google-cloud-console#create_a_transfer).

When prompted to enter the **CloudFront domain** , enter the distribution domain name you noted in the previous section. You can also find this value listed in the CloudFront section of the Amazon Web Services console. It has the format `https://dy1h2n3l4ob56.cloudfront.net`.

###  REST API 

To create a transfer using the REST API, follow the example on the [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers?tab=rest#s3-to-cloud) page.

Specify the distribution domain name as the value of the `transferSpec.awsS3DataSource.cloudfrontDomain` field:
    
    
    "transferSpec": {
      "awsS3DataSource": {
        "bucketName": "AWS_SOURCE_NAME",
        "cloudfrontDomain": "https://dy1h2n3l4ob56.cloudfront.net",
        "awsAccessKey": {
          "accessKeyId": "AWS_ACCESS_KEY_ID",
          "secretAccessKey": "AWS_SECRET_ACCESS_KEY"
        }
      },
      ...
    }
    

## Troubleshooting

### AuthorizationHeaderMalformed error

If you encounter an `AuthorizationHeaderMalformed` error that specifies a region mismatch (for example, `the region 'Location A' is wrong; expecting 'Location B'`), it is likely due to an unsupported CloudFront configuration.

This error occurs if you use a single CloudFront distribution to front multiple S3 buckets that reside in different AWS regions.

To resolve this issue, ensure that each CloudFront distribution fronts S3 buckets in only a single AWS region. If you have S3 buckets in different regions, create a separate CloudFront distribution for each region.

## Frequently asked questions

### Does using CloudFront expose my objects to the public?

No. If you've followed the configuration steps on this page, your objects are not exposed to the public.

  * Cloudfront does not have direct access to your S3 objects.
  * Users receive a `permission denied` error if they try to access your objects either directly or through CloudFront (if your bucket is private).
  * Storage Transfer Service signs requests to CloudFront using the credentials you provided in the transfer job, which allows us to download your objects securely as if we were downloading directly from S3. This works due to the header forwarding setting `AllViewerExceptHostHeader`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

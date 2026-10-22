---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-api-gateway/
title: Collect AWS API Gateway access logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:41.380527+00:00
---

# Collect AWS API Gateway access logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-api-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS API Gateway access logs

**Parser Version:** 7.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Amazon API Gateway access logs to Google Security Operations using **AWS CloudWatch Logs and Kinesis Data Firehose**. Amazon API Gateway provides REST and HTTP APIs to build and manage APIs at scale. Access logs help monitor API usage and troubleshoot issues. This integration streams these logs into Google SecOps for analysis and monitoring.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to AWS



## Enable Amazon API Gateway Access Logging (to CloudWatch Logs)

  1. Go to **AWS Console > API Gateway**.
  2. For **REST APIs** : 

     * Open your **Stage > Logs/Tracing > enable Access logging**. 
     * **Log format** : Select **JSON**.
           
           {
             "requestId":"$context.requestId",
             "ip":"$context.identity.sourceIp",
             "requestTime":"$context.requestTime",
             "httpMethod":"$context.httpMethod",
             "routeKey":"$context.routeKey",
             "status":"$context.status",
             "protocol":"$context.protocol",
             "responseLength":"$context.responseLength",
             "integrationLatency":"$context.integrationLatency",
             "error":"$context.error.message"
           }
           

     * **CloudWatch Logs log group** : Choose or create a log group (for example, `/aws/apigateway/access`).

  3. For **HTTP APIs** :

     * Select your **API > Monitor > Logging**.
     * Select **Stage > Edit**.
     * Enable **Access logging**.
     * Use the same JSON log format as above.
     * **CloudWatch Logs log group** : Choose or create a log group (for example, `/aws/apigateway/access`).
  4. Click **Save**.




## Configure a Feed in Google SecOps to Ingest Amazon API Gateway logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter `Amazon API Gateway - CloudWatch via Firehose`.
  4. Select **Amazon Data Firehose** as the **Source type**.
  5. Select **Amazon API Gateway** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **Split delimiter** : Optional `n`
     * **Asset namespace** : `aws.api_gateway`
     * **Ingestion labels** : For example, `source=apigw_access`, `aws_region=<your-region>`
  8. Click **Next**.
  9. Review the feed configuration and click **Submit**.
  10. In the feed **Details** , click **Generate Secret Key** and copy the **Secret Key**.
  11. Copy the **Feed HTTPS endpoint URL** from **Endpoint Information**.
  12. Create a **Google Cloud API key** in **APIs & Services > Credentials > Create credentials > API key**, and restrict it to **Chronicle API**. 
  13. Copy and save the API key in a secure location.



## Configure Amazon Kinesis Data Firehose (Direct to Google SecOps)

  1. In the **AWS Console** , go to **Kinesis > Data Firehose > Create delivery stream**.
  2. Provide the following configuration details: 
     * **Source** : Select **Direct PUT or other sources**.
     * **Destination** : Choose **HTTP endpoint**.
     * **HTTP endpoint URL** : Enter `ENDPOINT_URL?key=API_KEY` (use the Feed HTTPS endpoint URL and the API key from the previous step).
     * **HTTP method** : Select **POST**.
     * **Access key** : Paste the Secret Key generated in the feed.
     * **Buffering hints** : Set **Buffer size** = **1 MiB** , **Buffer interval** = **60 seconds**.
     * **Compression** : Select **Disabled**.
     * **S3 backup** : Select **Disabled**.
     * Leave **retry** and **logging** settings as default.
  3. Click **Create delivery stream**. (For example, `cwlogs-to-secops`.)



## Configure IAM Permissions and Subscribe the Log Group

  1. In the **AWS Console** , go to **IAM > Policies > Create policy > JSON**.
  2.      1. In the JSON editor, enter the following policy: 
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "firehose:PutRecord",
            "firehose:PutRecordBatch"
          ],
          "Resource": "arn:aws:firehose:<region>:<account-id>:deliverystream/cwlogs-to-secops"
        }
      ]
    }
    

     * Replace `<region>` and `<account-id>` with your AWS Region and account ID.
  3. Name the policy `CWLtoFirehoseWrite` and click **Create policy**.

  4. Go to **IAM > Roles > Create role**.

  5. Select **Custom trust policy** and enter the following:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Principal": {
                 "Service": "logs.<your-region>.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
             }
           ]
         }
         

  6. Attach the policy `CWLtoFirehoseWrite` to the role.

  7. Name the role `CWLtoFirehoseRole` and click **Create role**.

  8. Go to **CloudWatch > Logs > Log groups**.

  9. Select the **API Gateway** log group you created earlier.

  10. Open the **Subscription filters** tab and click **Create**.

  11. Choose **Create Amazon Kinesis Data Firehose subscription filter**.

  12. Configure the following:

     * **Destination** : Delivery stream `cwlogs-to-secops`.
     * **Grant permission** : Role `CWLtoFirehoseRole`.
     * **Filter name** : Enter `all-events`.
     * **Filter pattern** : Leave empty to send all events.
  13. Click **Start streaming**.




## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-api-gateway-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

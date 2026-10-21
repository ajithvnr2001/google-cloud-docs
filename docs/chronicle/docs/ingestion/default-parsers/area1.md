---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/area1/
title: Collect Area 1 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:04:44.678038+00:00
---

# Collect Area 1 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/area1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Area 1 logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Area 1 Email Security (by Cloudflare) logs to Google Security Operations using AWS S3. The parser processes the logs in JSON format. It extracts relevant fields from the nested JSON structure, maps them to the Unified Data Model (UDM), and enriches the data with geographical information and security details like attachment hashes and disposition.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * A Windows 2016 or later, or a Linux host with `systemd`
  * If running behind a proxy, firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open
  * Privileged access to Area 1 Email Security (by Cloudflare)



## Configure AWS IAM and S3 Bucket

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Sign in to the **AWS Console**.
  3. Go to **S3 > Create bucket**.
  4. Enter a name for the bucket (for example, `area1-security-logs`).
  5. Leave other defaults (or configure encryption and versioning if required).
  6. Click **Create**.
  7. Save the bucket **Name** and **Region** for future reference.
  8. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  9. Select the created **User**.
  10. Select **Security credentials** tab.
  11. Click **Create Access Key** in section **Access Keys**.
  12. Select **Third-party service** as **Use case**.
  13. Click **Next**.
  14. Optional: Add a description tag.
  15. Click **Create access key**.
  16. Click **Download CSV file** and store the **Access Key** and **Secret Access Key** for future reference.
  17. Click **Done**.
  18. Select the **Permissions** tab.
  19. In **Permissions policies** , click **Add permissions**.
  20. Select **Attach policies directly**.
  21. Search for **AmazonS3FullAccess** policy.
  22. Select the policy.
  23. Click **Next**.
  24. Click **Add permissions**.



## Get Area 1 API Credentials

  1. Sign in to the **Area 1 Security (Cloudflare)** dashboard.
  2. Go to **Settings > API Access**.
  3. Generate the **API Key** (Token).
  4. **Copy** and **Save** the Token in a secure place.



## Configure the required Python packages

  1. Sign in to your log collection host (for example, an **AWS VM**) and run the following to configure AWS credentials:
         
         pip install boto3 requests
         aws configure
         




## Create the Area 1 Log Puller script

  1. Create the following file by entering `sudo vi area1_to_s3.py`, and then copy the following code:

     * Adjust the following:
    
    #!/usr/bin/env python3
    import os
    import requests
    import boto3
    import datetime
    import json
    
    # Configuration
    AREA1_API_TOKEN = os.environ.get("AREA1_API_TOKEN")  # Load securely from env
    AWS_PROFILE = os.environ.get("AWS_PROFILE", None)    # Optional, for named profiles
    S3_BUCKET_NAME = "area1-security-logs"
    LOG_TYPE = "events"
    
    # Time range
    end_time = datetime.datetime.utcnow()
    start_time = end_time - datetime.timedelta(days=1)
    
    def fetch_area1_logs():
        url = f"https://api.area1security.com/v1/{LOG_TYPE}"
        headers = {
            "Authorization": f"Bearer {AREA1_API_TOKEN}",
            "Accept": "application/json"
        }
        params = {
            "startDate": start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "endDate": end_time.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def upload_to_s3(data):
        filename = f"area1_{LOG_TYPE}_{start_time.strftime('%Y%m%d')}.json"
    
        session = boto3.Session(profile_name=AWS_PROFILE) if AWS_PROFILE else boto3.Session()
        s3 = session.client("s3")
    
        s3.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=f"logs/{filename}",
            Body=json.dumps(data).encode("utf-8"),
            ContentType="application/json"
        )
        print(f"[✓] Uploaded {filename} to s3://{S3_BUCKET_NAME}/logs/")
    
    if __name__ == "__main__":
        logs = fetch_area1_logs()
        upload_to_s3(logs)
    

  2. Save and exit `vi`: click **`esc`** and then type **`:wq`**.




## Store the environment variables

  1. Create a secure file to store environment variables in `/etc/area1.env` (or `/home/user/.area1.env`)
         
         export AREA1_API_TOKEN="your_actual_area1_api_token"
         export AWS_PROFILE="<your_aws_programmatic_username>"
         

  2. Make sure the file is secure:
         
         chmod 600 /etc/area1.env
         




## Run and test the script

  1. Run the following script:
         
         python3 area1_to_s3.py
         

  2. You should see:
         
         Uploaded area1_events_20250701.json to s3://area1-security-logs/logs/
         




## Automate with Cron

  1. Create Wrapper Script for Cron by running `sudo vi /usr/local/bin/run_area1.sh` and then copy the following code:
         
         #!/usr/bin/env bash
         set -euo pipefail
         
         source /etc/area1.env
         /usr/bin/python3 /opt/scripts/area1_to_s3.py
         

  2. Make the file executable:
         
         chmod +x /usr/local/bin/run_area1.sh
         

  3. Set to run daily at 01:00 UTC:
         
         crontab -e
         0 1 * * * /usr/local/bin/run_area1.sh >> /var/log/area1_to_s3.log 2>&1
         




## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds**
  * **Content Hub > Content Packs**

**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

## Set up feeds from SIEM Settings > Feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Area1 Logs`).
  5. Select **Amazon S3** as the **Source type**.
  6. Select **Area1 Security** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Region** : The region where the Amazon S3 bucket is located.
     * **S3 URI** : The bucket URI (the format should be: `s3://<your-log-bucket-name>`). Replace the following: 
       * `your-log-bucket-name`: the name of the bucket.
     * **URI is a** : Select **Directory which includes subdirectories**.
     * **Source deletion options** : select deletion option according to your preference.
**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
     * **Access Key ID** : the User access key with access to the s3 bucket.
     * **Secret Access Key** : the User secret key with access to the s3 bucket.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Set up feeds from the Content Hub

Specify values for the following fields:

  * **Region** : The region where the Amazon S3 bucket is located.

    * **S3 URI** : The bucket URI (the format should be: `s3://<your-log-bucket-name>`). Replace the following: 
      * `your-log-bucket-name`: the name of the bucket.
    * **URI is a** : Select **Directory which includes subdirectories**.
    * **Source deletion options** : select deletion option according to your preference.
**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
    * **Access Key ID** : the User access key with access to the s3 bucket.
    * **Secret Access Key** : the User secret key with access to the s3 bucket.§



**Advanced options**

  * **Feed Name** : A prepopulated value that identifies the feed.
  * **Source Type** : Method used to collect logs into Google SecOps.
  * **Asset Namespace** : Namespace associated with the feed.
  * **Ingestion Labels** : Labels applied to all events from this feed.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
alert_id | security_result.rule_id | The value is taken from the `alert_id` field.  
alert_reasons | security_result.description | The value is taken from the `alert_reasons` field.  
attachments.att_size | security_result.about.file.size | The value is taken from the `attachments.att_size` field and converted to an unsigned integer.  
attachments.disposition | security_result.about.user.attribute.labels.value | The value is taken from the `attachments.disposition` field.  
attachments.extension | security_result.about.file.mime_type | The value is taken from the `attachments.extension` field.  
attachments.md5 | security_result.about.file.md5 | The value is taken from the `attachments.md5` field.  
attachments.name | security_result.about.file.full_path | The value is taken from the `attachments.name` field.  
attachments.sha1 | security_result.about.file.sha1 | The value is taken from the `attachments.sha1` field.  
attachments.sha256 | security_result.about.file.sha256 | The value is taken from the `attachments.sha256` field.  
attachments.ssdeep | security_result.about.file.ssdeep | The value is taken from the `attachments.ssdeep` field.  
delivery_mode | security_result.detection_fields.value | The value is taken from the `delivery_mode` field.  
envelope_from | principal.user.email_addresses, network.email.from | The value is taken from the `envelope_from` field.  
envelope_to | network.email.to, target.user.email_addresses | The value is taken from the `envelope_to` field.  
final_disposition | security_result.category_details | The value is taken from the `final_disposition` field.  
message_id | metadata.product_log_id | The value is taken from the `message_id` field after removing '<' and '>' characters.  
replyto | network.email.bounce_address | The value is taken from the `replyto` field.  
smtp_helo_server_ip | principal.ip | The value is taken from the `smtp_helo_server_ip` field.  
smtp_helo_server_ip_as_name | principal.location.name | The value is taken from the `smtp_helo_server_ip_as_name` field.  
smtp_helo_server_ip_as_number | principal.asset_id | The value is taken from the `smtp_helo_server_ip_as_number` field and prepended with `asset_id:`.  
smtp_helo_server_ip_geo | principal.location.country_or_region, principal.location.state, principal.location.city | The value is extracted from the `smtp_helo_server_ip_geo` field using a Grok pattern.  
smtp_helo_server_name | principal.administrative_domain | The value is taken from the `smtp_helo_server_name` field.  
source | metadata.vendor_name | The value is taken from the `source` field. If the field is empty, the value is set to `area1security`.  
subject | network.email.subject | The value is taken from the `subject` field.  
time | metadata.event_timestamp | The value is taken from the `time` field and converted to a timestamp.  
| metadata.event_type | The value is set to `EMAIL_TRANSACTION`.  
| metadata.product_name | The value is set to `AREA1`.  
| metadata.log_type | The value is set to `AREA1`.  
| security_result.about.user.attribute.labels.key | The value is set to `disposition`.  
| security_result.category | The value is set to `SOFTWARE_MALICIOUS`.  
| security_result.detection_fields.key | The value is set to `delivery_mode`.  
`envelope_to.0" instead of "replyto` | `network.email.to` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/area1-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

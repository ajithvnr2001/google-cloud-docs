---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-dns/
title: Collect Cisco Umbrella DNS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:59:19.318350+00:00
---

# Collect Cisco Umbrella DNS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Umbrella DNS logs

**Parser Version:** 17.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Umbrella DNS logs to Google Security Operations using Amazon S3. Cisco Umbrella is a cloud-delivered security service that provides DNS-layer protection, secure web gateway, and cloud access security broker (CASB) functionality. Umbrella DNS logs capture DNS query activity across your network, including requested domains, response codes, and security policy actions taken on each request.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance.
  * Privileged access to the **Cisco Umbrella** dashboard with Full Admin or Read-Only Admin role.
  * Privileged access to **AWS** (S3, IAM).



## Configure Cisco Umbrella log export to Amazon S3

Cisco Umbrella natively supports exporting DNS logs to an Amazon S3 bucket that you manage.

  1. Sign in to the **Cisco Umbrella** dashboard at `https://dashboard.umbrella.com`.
  2. Go to **Admin > Log Management**.
  3. Click **Use your company-managed Amazon S3 bucket**.
  4. Provide the following configuration details: 
     * **Bucket Name** : Enter the name of the S3 bucket you will create in the next section (for example, `umbrella-dns-logs`).
     * **Region** : Select the AWS region where your bucket will be created.
  5. Copy the **AWS Account ID** and **External ID** displayed by Umbrella. You will need these to configure the IAM trust policy in AWS.
  6. Click **Save**.

**Note:** Do not click **Verify** yet. You must first create the S3 bucket and IAM role in AWS.

## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `umbrella-dns-logs`).
  3. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**.
  5. Select **Security credentials** tab.
  6. Click **Create Access Key** in section **Access Keys**.
  7. Select **Third-party service** as **Use case**.
  8. Click **Next**.
  9. Optional: Add description tag.
  10. Click **Create access key**.
  11. Click **Download CSV file** to save the **Access Key** and **Secret Access Key** for future reference.
  12. Click **Done**.
  13. Select **Permissions** tab.
  14. Click **Add permissions** in section **Permissions policies**.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**.
  17. Search for **AmazonS3FullAccess** policy.
  18. Select the policy.
  19. Click **Next**.
  20. Click **Add permissions**.



## Configure the IAM policy and role for Cisco Umbrella S3 access

Cisco Umbrella requires a cross-account IAM role to write logs to your S3 bucket.

  1. In the AWS console, go to **IAM > Policies > Create policy > JSON tab**.
  2. Copy and paste the following policy (replace `umbrella-dns-logs` if you entered a different bucket name):
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Sid": "AllowUmbrellaPutObjects",
               "Effect": "Allow",
               "Action": [
                 "s3:PutObject",
                 "s3:GetBucketLocation"
               ],
               "Resource": [
                 "arn:aws:s3:::umbrella-dns-logs",
                 "arn:aws:s3:::umbrella-dns-logs/*"
               ]
             }
           ]
         }
         

  3. Click **Next > Create policy**. Name it `UmbrellaS3WritePolicy`.

  4. Go to **IAM > Roles > Create role > Custom trust policy**.

  5. Paste the following trust policy, replacing `UMBRELLA_AWS_ACCOUNT_ID` and `UMBRELLA_EXTERNAL_ID` with the values copied from the Umbrella dashboard:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Principal": {
                 "AWS": "arn:aws:iam::UMBRELLA_AWS_ACCOUNT_ID:root"
               },
               "Action": "sts:AssumeRole",
               "Condition": {
                 "StringEquals": {
                   "sts:ExternalId": "UMBRELLA_EXTERNAL_ID"
                 }
               }
             }
           ]
         }
         

  6. Click **Next**.

  7. Attach the `UmbrellaS3WritePolicy` policy.

  8. Name the role `UmbrellaS3Role` and click **Create role**.

  9. Copy the **Role ARN** for use in the Umbrella dashboard.




## Verify Cisco Umbrella log export

  1. Return to the **Cisco Umbrella** dashboard.
  2. Go to **Admin > Log Management**.
  3. Enter the **Role ARN** from the IAM role you created.
  4. Click **Verify** to confirm that Umbrella can write to the S3 bucket.
  5. After successful verification, Umbrella will begin exporting DNS logs to the S3 bucket.

**Note:** Umbrella exports DNS logs in CSV format to the S3 bucket in the following path structure: `s3://umbrella-dns-logs/dnslogs/<year>-<month>-<day>/`.

## Configure a feed in Google SecOps to ingest Cisco Umbrella DNS logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `Cisco Umbrella DNS logs`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **Cisco Umbrella DNS** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters:

     * **S3 URI** : `s3://umbrella-dns-logs/dnslogs/`
     * **Source deletion options** : Select deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label applied to the events from this feed.
  8. Click **Next**.

  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`action` | `security_result.action_details` | The value is taken from the `action` field if it exists in the JSON logs, or from `column6` or `column7` in CSV logs, and converted to uppercase (ALLOW or BLOCK).  
`amp.disposition` | `security_result.detection_fields[].key` | Value is `ampDisposition`.  
`amp.disposition` | `security_result.detection_fields[].value` | The value is taken from the `amp.disposition` field.  
`amp.malware` | `security_result.detection_fields[].key` | Value is `ampMalware`.  
`amp.malware` | `security_result.detection_fields[].value` | The value is taken from the `amp.malware` field.  
`amp.score` | `security_result.detection_fields[].key` | Value is `ampScore`.  
`amp.score` | `security_result.detection_fields[].value` | The value is taken from the `amp.score` field.  
`blocked_categories` | `security_result.category_details` | The value is taken from the `blocked_categories` field.  
`blockedfiletype` | `security_result.detection_fields[].key` | Value is `egress type`.  
`blockedfiletype` | `security_result.detection_fields[].value` | The value is taken from the `blockedfiletype` field.  
`bundleid` | `additional.fields[].key` | Value is `bundleid`.  
`bundleid` | `additional.fields[].value.string_value` | The value is taken from the `bundleid` field.  
`categories[]` | `security_result.category_details` | The value is taken from the `categories[].label` field.  
`column1` | `metadata.event_timestamp.seconds` | The value is parsed from the `column1` field as a timestamp. For proxy logs, if `date` and `time` fields exist, they are combined and parsed as a timestamp.  
`column10` | `network.http.user_agent` | The value is taken from the `column10` field.  
`column10` | `additional.fields[].value.string_value` | The value is taken from the `column10` field.  
`column11` | `target.port` | The value is taken from the `column11` field.  
`column12` | `principal.resource.name` | The value is taken from the `column12` field.  
`column13` | `security_result.rule_id` | The value is taken from the `column13` field.  
`column14` | `security_result.action_details` | The value is taken from the `column14` field.  
`column2` | `principal.user.user_display_name` | The value is taken from the `column2` field.  
`column2` | `principal.user.userid` | The value is taken from the `column2` field.  
`column2` | `principal.location.name` | The value is taken from the `column2` field.  
`column3` | `principal.hostname` | The value is taken from the `column3` field.  
`column3` | `principal.user.product_object_id` | The value is taken from the `column3` field.  
`column3` | `principal.location.city` | The value is taken from the `column3` field.  
`column3` | `additional.fields[].value.string_value` | The value is taken from the `column3` field.  
`column4` | `principal.asset.ip` | The value is taken from the `column4` field.  
`column4` | `principal.ip` | The value is taken from the `column4` field.  
`column4` | `principal.port` | The value is taken from the `column4` field.  
`column5` | `principal.asset.ip` | The value is taken from the `column5` field.  
`column5` | `principal.ip` | The value is taken from the `column5` field.  
`column5` | `target.asset.ip` | The value is taken from the `column5` field.  
`column5` | `target.ip` | The value is taken from the `column5` field.  
`column6` | `security_result.action_details` | The value is taken from the `column6` field.  
`column6` | `target.port` | The value is taken from the `column6` field.  
`column7` | `network.received_bytes` | The value is taken from the `column7` field.  
`column7` | `additional.fields[].value.string_value` | The value is taken from the `column7` field.  
`column8` | `principal.asset.ip` | The value is taken from the `column8` field.  
`column8` | `principal.ip` | The value is taken from the `column8` field.  
`column8` | `target.url` | The value is taken from the `column8` field.  
`column9` | `principal.port` | The value is taken from the `column9` field.  
`column9` | `network.http.referral_url` | The value is taken from the `column9` field.  
`data_center_name` | `principal.resource.name` | The value is taken from the `data_center_name` field.  
`datacenter.label` | `security_result.detection_fields[].key` | Value is `datacenter label`.  
`datacenter.label` | `security_result.detection_fields[].value` | The value is taken from the `datacenter.label` field.  
`destinationip` | `target.asset.ip` | The value is taken from the `destinationip` field.  
`destinationip` | `target.ip` | The value is taken from the `destinationip` field.  
`direction` | `network.direction` | The value is taken from the `direction` field and converted to uppercase.  
`domain` | `network.dns.questions[].name` | The value is taken from the `domain` field, with the trailing dot removed if present.  
`dstPort` | `target.port` | The value is taken from the `dstPort` field.  
`dstip` | `target.asset.ip` | The value is taken from the `dstip` field.  
`dstip` | `target.ip` | The value is taken from the `dstip` field.  
`egress.ip` | `security_result.detection_fields[].key` | Value is `egress ip`.  
`egress.ip` | `security_result.detection_fields[].value` | The value is taken from the `egress.ip` field.  
`egress.type` | `security_result.detection_fields[].key` | Value is `egress type`.  
`egress.type` | `security_result.detection_fields[].value` | The value is taken from the `egress.type` field.  
`externalip` | `principal.asset.ip` | The value is taken from the `externalip` field.  
`externalip` | `principal.ip` | The value is taken from the `externalip` field.  
`forwardingmethod` | `additional.fields[].key` | Value is `forwardingmethod`.  
`forwardingmethod` | `additional.fields[].value.string_value` | The value is taken from the `forwardingmethod` field.  
`granular_identity` | `principal.user.user_display_name` | The value is taken from the `granular_identity` field if both `granular_identity` and `most_granular_identity` are present. Otherwise, it's derived from the `_policy_identity` field and further parsed based on `identityType`.  
`granular_identity` | `principal.user.email_addresses` | The value is extracted from the `granular_identity` field using a regular expression.  
`granular_identity` | `principal.user.first_name` | The value is extracted from the `granular_identity` field using a regular expression.  
`granular_identity` | `principal.user.last_name` | The value is extracted from the `granular_identity` field using a regular expression.  
`granular_identity` | `principal.user.userid` | The value is extracted from the `granular_identity` field using a regular expression.  
`granular_identity` | `principal.hostname` | The value is taken from the `granular_identity` field.  
`granular_identity` | `principal.location.name` | The value is taken from the `granular_identity` field.  
`identity_types` | `additional.fields[].value.string_value` | The value is taken from the `identity_types` field.  
`identities[]` | `principal.user.product_object_id` | The value is taken from the `identities[]` field.  
`identities` | `principal.user.product_object_id` | The value is taken from the `identities` field.  
`internalip` | `principal.asset.ip` | The value is taken from the `internalip` field.  
`internalip` | `principal.ip` | The value is taken from the `internalip` field.  
`isolated.fileaction` | `security_result.detection_fields[].key` | Value is `isolated fileaction`.  
`isolated.fileaction` | `security_result.detection_fields[].value` | The value is taken from the `isolated.fileaction` field.  
`isolated.state` | `security_result.detection_fields[].key` | Value is `isolated state`.  
`isolated.state` | `security_result.detection_fields[].value` | The value is taken from the `isolated.state` field.  
`most_granular_identity` | `principal.user.identityType` | The value is taken from the `most_granular_identity` field if both `granular_identity` and `most_granular_identity` are present. Otherwise, it's taken from the `_policy_identity_type` field.  
`nat_destination_ip` | `principal.asset.ip` | The value is taken from the `nat_destination_ip` field.  
`nat_destination_ip` | `principal.ip` | The value is taken from the `nat_destination_ip` field.  
`odns_categories` | `security_result.category_details` | The value is taken from the `odns_categories` field.  
`policy.ruleid` | `security_result.rule_id` | The value is taken from the `policy.ruleid` field.  
`policy.rulesetid` | `security_result.detection_fields[].key` | Value is `rulesetid`.  
`policy.rulesetid` | `security_result.detection_fields[].value` | The value is taken from the `policy.rulesetid` field.  
`policy.timebasedrule` | `security_result.detection_fields[].key` | Value is `timebasedrule`.  
`policy.timebasedrule` | `security_result.detection_fields[].value` | The value is taken from the `policy.timebasedrule` field.  
`port` | `target.port` | The value is taken from the `port` field.  
`query_type_name` | `network.dns.questions[].type` | The numeric part is extracted from the `query_type_name` field using a regular expression and converted to an integer.  
`query_type_name` | `additional.fields[].value.string_value` | The string part within parentheses is extracted from the `query_type_name` field using a regular expression.  
`querytype` | `network.dns.questions[].type` | The value is taken from the `querytype` field and mapped to a numeric value based on the DNS record type.  
`referer` | `network.http.referral_url` | The value is taken from the `referer` field.  
`requestmethod` | `network.http.method` | The value is taken from the `requestmethod` field.  
`requestsize` | `network.sent_bytes` | The value is taken from the `requestsize` field and converted to an unsigned integer.  
`response` | `additional.fields[].value.string_value` | The value is taken from the `response` field.  
`responsecode` | `network.http.response_code` | The value is taken from the `responsecode` field.  
`responsefilename` | `target.file.names` | The value is taken from the `responsefilename` field.  
`responsesize` | `network.received_bytes` | The value is taken from the `responsesize` field and converted to an unsigned integer.  
`returncode` | `network.dns.response_code` | The value is taken from the `returncode` field and converted to an unsigned integer.  
`securityoverridden` | `additional.fields[].key` | Value is `securityoverridden`.  
`securityoverridden` | `additional.fields[].value.string_value` | The value is taken from the `securityoverridden` field.  
`sha256` | `target.file.sha256` | The value is taken from the `sha256` field.  
`source_ip` | `principal.asset.ip` | The value is taken from the `source_ip` field if it exists in the JSON logs, or from `column3` in CSV logs.  
`source_ip` | `principal.ip` | The value is taken from the `source_ip` field if it exists in the JSON logs, or from `column3` in CSV logs.  
`srcPort` | `principal.port` | The value is taken from the `srcPort` field.  
`statuscode` | `network.http.response_code` | The value is taken from the `statuscode` field.  
`tenantcontrols` | `additional.fields[].key` | Value is `tenantcontrols`.  
`tenantcontrols` | `additional.fields[].value.string_value` | The value is taken from the `tenantcontrols` field.  
`timestamp` | `metadata.event_timestamp.seconds` | The value is parsed from the `timestamp` field as a timestamp.  
`tunnel_name` | `additional.fields[].key` | Value is `tunnel_name`.  
`tunnel_name` | `additional.fields[].value.string_value` | The value is taken from the `tunnel_name` field.  
`tunnel_type` | `metadata.product_event_type` | The value is taken from the `tunnel_type` field.  
`type` | `additional.fields[].key` | Value is `type`.  
`type` | `additional.fields[].value.string_value` | The value is taken from the `type` field.  
`url` | `target.url` | The value is taken from the `url` field.  
`useragent` | `network.http.user_agent` | The value is taken from the `useragent` field.  
`verdict` | `security_result.action_details` | The value is taken from the `verdict` field.  
`warnstatus` | `security_result.detection_fields[].key` | Value is `warnstatus`.  
`warnstatus` | `security_result.detection_fields[].value` | The value is taken from the `warnstatus` field. Value is `DNS Lookup Type`. The string part within parentheses is extracted from the `query_type_name` field using a regular expression, or it's an empty string if the field is not present. Value is `DNS request and response were made.` Determined based on the presence of certain fields: NETWORK_DNS if `question.name` is present, NETWORK_CONNECTION if both `principal.ip` and `target.ip` are present, STATUS_UPDATE if only `principal.ip` is present, or GENERIC_EVENT otherwise. Value is `UMBRELLA_DNS`. Value is `Umbrella DNS`. Value is `Cisco`. Value is initially set to `DNS`. If `requestmethod` is a valid HTTP method, it's changed to `HTTP`. The numeric part is extracted from the `query_type_name` field using a regular expression and converted to an integer, or it's derived from the `querytype` field and mapped to a numeric value based on the DNS record type. The value is derived from the `useragent` or `column10` field using the `parseduseragent` filter. The value is taken from the last part of the `column3` field after splitting by commas, or it's an empty string if the field is not present. The value is taken from the first part of the `column3` field after splitting by commas, or it's taken from the `column2` field if `column3` is not present. The value is extracted from the `column2` or `column3` field using a regular expression. The value is extracted from the `column2` or `column3` field using a regular expression. The value is extracted from the `column2` or `column3` field using a regular expression. The value is extracted from the `column2` or `column3` field using a regular expression. The value is derived from the `action`, `column6`, `column7`, or `verdict` field and converted to uppercase (ALLOW or BLOCK). Value is set to `NETWORK_MALICIOUS` if `_categories` contains `Malware`, or `NETWORK_SUSPICIOUS` if `_categories` contains `Potentially Harmful`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-dns-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

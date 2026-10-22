---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dope-swg/
title: Collect Dope Security SWG logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:23.091865+00:00
---

# Collect Dope Security SWG logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dope-swg/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Dope Security SWG logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Dope Security SWG logs into Google Security Operations using Amazon S3.

Dope Security dope.swg is an endpoint-based secure web gateway that provides real-time web filtering, malware protection, and cloud application control. Each dope.endpoint sends web transaction logs to the dope.cloud every 15 minutes, which are then automatically exported to your AWS S3 bucket in compressed GZIP JSONL format for SIEM integration.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Dope Security dope.console**
  * Privileged access to **AWS** (S3, IAM)
  * Your Dope Security tenant must be in the same AWS region as your S3 bucket (verify region in **Settings > SIEM** page)



## Configure Dope Security SIEM integration

To configure Dope Security SIEM integration, do the following:

  1. Sign in to the **dope.console** at https://console.dope.security
  2. Go to **Settings > SIEM > SIEM Integration Settings**.
  3. In the **SIEM Type** list, select **AWS S3**.
  4. Note the **AWS Region** displayed on the right side of the page (for example, **US-EAST-2**).

**Note:** Your AWS S3 bucket must be created in this exact region. The region is determined by your Dope Security tenant's data residency location.
  5. Leave this page open because you will return to complete the configuration after setting up AWS S3.




## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create an **Amazon S3 bucket**. For more information, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. When creating the bucket, ensure that the **Region** matches the region shown in the Dope Security SIEM Integration page (for example, **US East (Ohio) us-east-2**).
  3. Save bucket **Name** for future reference (for example, `chronicle-dope-swg-logs`).

**Note:** Do not enable KMS encryption on this S3 bucket. Dope Security does not support KMS-encrypted buckets at this time.
  4. Create a **User**. For more information, see [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).

  5. Select the **User** you created.

  6. Select **Security credentials** tab.

  7. Click **Create Access Key** in the **Access Keys** section.

  8. Select **Third-party service** as **Use case**.

  9. Click **Next**.

  10. Optional: Add a description tag.

  11. Click **Create access key**.

  12. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.

  13. Click **Done**.

  14. Select **Permissions** tab.

  15. Click **Add permissions** in **Permissions policies** section.

  16. Select **Add permissions**.

  17. Select **Attach policies directly**.

  18. Search for **AmazonS3FullAccess** policy.

  19. Select the policy.

  20. Click **Next**.

  21. Click **Add permissions**.




## Configure Dope Security Amazon S3 connection

  1. Return to the **dope.console** at the **Settings > SIEM > SIEM Integration Settings** page.
  2. In the **S3 Bucket Name** field, enter the name of your S3 bucket (for example, `chronicle-dope-swg-logs`).
  3. In the right pane, you will see a **Bucket Policy** section with a pre-generated JSON policy.
  4. Click **Copy** next to the policy JSON to copy it to your clipboard.
  5. In a new browser tab, go to the **AWS S3 Console**.
  6. Select your S3 bucket (for example, `chronicle-dope-swg-logs`).
  7. Go to **Permissions** tab.
  8. Scroll down to **Bucket policy** section.
  9. Click **Edit**.
  10. Paste the policy JSON that you copied from the dope.console into the **Policy** text area.
  11. Click **Save changes**.
  12. Return to the **dope.console** browser tab.
  13. Click **Sync** at the bottom of the SIEM Integration Settings page.
  14. Wait for the synchronization to complete.
  15. Verify that a green checkmark appears next to the **S3 Bucket Name** field.
  16. Verify that the **Last Synchronization** timestamp appears in the top right corner of the page.

**Note:** If synchronization fails, check for the following common errors: AWS S3 bucket not found, AWS S3 bucket is not in the correct region, AWS S3 access policy is not set, or AWS S3 access policy is incorrect. The SIEM Integration page displays the specific error message.



## Configure a feed in Google SecOps to ingest Dope Security SWG logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name** (for example, `Dope Security SWG Logs`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **DOPE_SWG** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields:

     * **S3 URI** : `s3://chronicle-dope-swg-logs/` (replace with your bucket name)
     * **Source deletion option** : Select the deletion option according to your preference
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Access Key ID** : User access key with access to the S3 bucket (from step 12 of AWS configuration)
     * **Secret Access Key** : User secret key with access to the S3 bucket (from step 12 of AWS configuration)
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
  9. Click **Next** and then click **Submit**.




## Log data format reference

Dope Security exports logs in JSONL (JSON Lines) format with GZIP compression. Each log entry contains the following key fields:

Field | Description  
---|---  
**Timestamp** | ISO 8601 timestamp of when the web transaction was requested  
**Duration** | Connection duration in milliseconds  
**Matched Destination** | Domain that the dope category was matched against  
**Destination IP** | Destination IP address for the requested URL  
**Tenant ID** | Customer's dope.cloud unique tenant ID  
**Agent ID** | Unique agent ID for the dope.endpoint  
**User** | Logged-in user on the dope.endpoint  
**OIDC User** | Email address for authenticated user (when OIDC authentication is enabled)  
**Categories** | Matched dope category numbers (0-88) for the requested URL  
**Verdict** | Policy verdict: Allow (0), Block (1), Warning (2), or Bypass (3)  
**Data Sent** | Amount of data sent in the connection (bytes)  
**Data Received** | Amount of data received in the connection (bytes)  
**Policy Type** | Type of policy applied: Web, Cloud Application Control (CAC), Custom Category, Bypass, or Malware  
**Block Detail** | For block verdicts: dope category, custom category, cloud application, or malware type  
**Filename** | Name of any downloaded file  
**File Hash** | File hash for downloaded files  
**Process Name** | Name of the process making the URL request  
**URL** | Complete requested URL  
**Policy Name** | Name of the policy applied  
**Protocol** | Protocol used (for example, HTTP/2, HTTP/1.1)  
**Hostname** | Device hostname  
**HTTP Request Method** | HTTP request method (for example, GET, POST, PUT)  
**Process Call Tree** | Parent-child relationships from process spawn operations with command arguments  
  
For the complete category and verdict mappings, see the [Dope Security Category & Verdict Mappings](https://inflight.dope.security/dope.console/settings/siem-integration/category-and-verdict-mappings) documentation.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
policy.categories, request.processTree | additional.fields | Merged as list from policy.categories and request.processTree in JSON  
timestamp | metadata.event_timestamp | Parsed as ISO8601 timestamp in both JSON and CSV  
| metadata.event_type | Set to NETWORK_HTTP if has_principal, has_target, has_http in JSON; else NETWORK_CONNECTION if has_principal and has_target; else USER_UNCATEGORIZED if has_user; else STATUS_UPDATE if has_principal; else GENERIC_EVENT; set to NETWORK_HTTP in CSV  
schemaVersion | metadata.product_version | Value copied directly from schemaVersion in JSON  
request.httpVersion | network.http.user_agent | Value copied directly from request.httpVersion in JSON  
bandwidth.dataReceivedInBytes, bytes_received | network.received_bytes | Converted to uinteger from bandwidth.dataReceivedInBytes in JSON or bytes_received in CSV if not empty and not 0  
bandwidth.dataSentInBytes, bytes_sent | network.sent_bytes | Converted to uinteger from bandwidth.dataSentInBytes in JSON or bytes_sent in CSV if not empty and not 0  
request.duration | network.session_duration.seconds | Converted to integer from request.duration in JSON  
endpoint.agentID, endpoint_id | principal.asset.asset_id | Prefixed with DS: from endpoint.agentID in JSON or endpoint_id in CSV  
endpoint.tenantID | principal.asset.attribute.cloud.project.id | Value copied directly from endpoint.tenantID in JSON  
endpoint.deviceName | principal.asset.hostname | Value copied directly from endpoint.deviceName in JSON  
endpoint.deviceName, endpoint_hostname | principal.hostname | Value from endpoint.deviceName in JSON or endpoint_hostname in CSV  
request.processName | principal.process.command_line | Value copied directly from request.processName in JSON  
process_name | principal.process.file.names | Value copied directly from process_name in CSV  
sso_user, user | principal.user.account_type | Set to DOMAIN_ACCOUNT_TYPE if sso_user not empty, else LOCAL_ACCOUNT_TYPE in CSV  
endpoint.oidcUser | principal.user.email_addresses | Merged if endpoint.oidcUser matches email regex in JSON  
endpoint.oidcUser | principal.user.user_display_name | Value copied directly if endpoint.oidcUser does not match email regex in JSON  
endpoint.user, sso_user, user | principal.user.userid | Value from endpoint.user in JSON; from sso_user if not empty else user in CSV  
security_result | security_result | Merged from security_result in JSON  
policy.verdict, verdict | security_result.action | Set to BLOCK if 1, ALLOW if 0, CHALLENGE if 2 from policy.verdict in JSON or verdict in CSV  
categories | security_result.action_details | Value copied directly from categories in CSV  
policy.policyName | security_result.rule_name | Value copied directly from policy.policyName in JSON  
policy.policyType | security_result.rule_type | Value copied directly from policy.policyType in JSON  
file_name | target.file.names | Value copied directly from file_name in CSV  
file_hash | target.file.sha256 | Value copied directly from file_hash in CSV  
destination.matchedDestination, domain | target.hostname | Value from destination.matchedDestination if not IP in JSON; from domain in CSV  
destination.matchedDestination, destination.destinationIP, ip | target.ip | Value from destination.matchedDestination or destination.destinationIP if IP in JSON; from ip in CSV  
destination.url, url | target.url | Value from destination.url in JSON; from url in CSV  
| metadata.product_name | Set to "DOPE_SWG" in JSON; "SWG" in CSV  
| metadata.vendor_name | Set to "DOPE_SWG" in JSON; "Dope Security" in CSV  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dope-swg-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

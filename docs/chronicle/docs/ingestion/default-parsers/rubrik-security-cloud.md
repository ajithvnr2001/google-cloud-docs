---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rubrik-security-cloud/
title: Collect Rubrik Security Cloud logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:28.574888+00:00
---

# Collect Rubrik Security Cloud logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rubrik-security-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Rubrik Security Cloud logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Rubrik Security Cloud logs to Google Security Operations using webhooks. Rubrik Security Cloud (RSC) is a SaaS-based data security platform that provides backup, recovery, anomaly detection, and data governance capabilities across cloud and on-premises environments. RSC generates security events, audit logs, and operational activity logs in PagerDuty Common Event Format (PD-CEF) JSON that can be pushed to Google SecOps for centralized monitoring and analysis.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to Rubrik Security Cloud console with permissions to manage webhooks
  * Network connectivity from Rubrik Security Cloud to the Google SecOps webhook endpoint
  * Access to Google Cloud console for API key creation



## Create a webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Rubrik Security Cloud Events`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Rubrik Security Cloud** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Leave empty as each webhook request contains a single event.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



### Generate and save the secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. Copy and save the secret key securely.

**Important:** The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.

### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. Save this URL for the next steps.
  4. Click **Done**.



## Create a Google Cloud API key

Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud console.

### Create the API key

  1. Go to the [Google Cloud console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Google SecOps instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps Webhook API Key`).
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** drop-down, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Google SecOps API, reducing security risk if the key is compromised.



## Configure a Rubrik Security Cloud webhook

### Construct the webhook URL

  * Combine the Google SecOps endpoint URL, the API key, and the feed secret key. Both credentials are passed as query parameters:
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET>
        

    * **Example:**
          
          https://<REGION>-chronicle.googleapis.com/v1alpha/projects/<PROJECT_NUMBER>/locations/<REGION>/instances/<INSTANCE_ID>/feeds/<FEED_ID>:importPushLogs?key=AIzaSyD...&secret=a1b2c3d4...
          




### Create a webhook in Rubrik Security Cloud

  1. Sign in to **Rubrik Security Cloud** at `https://<account>.my.rubrik.com`.
  2. Click the gear icon in the upper right corner and select **Settings**.
  3. Click **Notifications** and select **Webhooks**.
  4. Click **Add Webhook**.
  5. The Add Webhook wizard appears.
  6. In **Provider** , select **Generic**.

**Note:** The Generic provider type sends event data in PagerDuty Common Event Format (PD-CEF) JSON, which is compatible with Google SecOps.
  7. In **Webhook name** , enter a descriptive name (for example, `Google SecOps Integration`).

  8. In **Endpoint** , paste the complete webhook URL from above, including both the `key` and `secret` query parameters. Authentication is carried by the URL, so the **Authentication** toggle can stay off.

**Note:** If your organization does not allow credentials in URLs, turn on **Authentication** instead, select **Custom** , and add custom headers: `X-Webhook-Access-Key` set to the feed secret key and, if your wizard version allows more than one header, `X-goog-api-key` set to the API key. Remove from the endpoint URL every credential you pass as a header (`&secret=<SECRET>`, and `?key=<API_KEY>` when both headers are used). Earlier versions of this page showed a different custom header name; that name is not accepted by the feed endpoint and produces a 403 `PERMISSION_DENIED` ("No valid secret found") error. If your webhook is configured with it, replace it with `X-Webhook-Access-Key` or switch to the URL parameters above.
  9. Click **Next**.

  10. Click **Test Webhook** to verify that the specified webhook configuration works and click **Next**.

  11. The **Select event and severity** window appears.

  12. Select the events that RSC sends to the configured webhook endpoint:

     1. Under **Events** , select the event types to forward:

        * **Backup**
        * **Recovery**
        * **Anomaly**
        * **Threat Hunt**
        * **Threat Monitoring**
        * **Configuration**
        * **Diagnostic**
        * **Sync**
        * **Maintenance**
        * **System**
**Note:** Include **Threat Hunt** and **Threat Monitoring** : the parser maps these categories to security events, and without them RSC never forwards threat findings to the feed.
     2. Under **Audit** , select the audit types to forward. Authentication audit types feed the parser's login mappings.

     3. Under **Severity** , select the severity levels for triggering alerts:

        * **Critical**
        * **Warning**
        * **Informational**
  13. Click **Next**.

  14. Review the configuration details on the **Confirmation** window and click **Save**.

**Note:** After 3 consecutive failed attempts with exponential backoff (1s, 5s, 10s), the event is removed from the queue. The webhook is auto-disabled after 25 consecutive failures. Monitor webhook status regularly.



### Verify the webhook is working

#### Check the Rubrik Security Cloud webhook status

  1. Sign in to **Rubrik Security Cloud**.
  2. Go to **Settings > Notifications > Webhooks**.
  3. Check the **Status** column for your webhook (should show **Enabled**).
  4. Monitor for any error messages in the webhook details.



#### Check the Google SecOps feed status

  1. Go to **SIEM Settings > Feeds** in Google SecOps.
  2. Check the **Status** column for your webhook feed (should be **Active**).
  3. Check **Events received** count (should be incrementing).

**Note:** The **Last succeeded on** column stays empty for webhook feeds. Push feeds have no schedule, so data arrives when the source sends it and there is no scheduled run to report.



#### Verify logs in Google SecOps

  1. Go to **Search > UDM Search**.
  2. Use the following query:
         
         metadata.vendor_name = "RUBRIK" nocase AND metadata.product_name = "RUBRIK SECURITY CLOUD" nocase
         

  3. Adjust time range to last 1 hour.

  4. Verify events appear in results.




## Webhook payload reference

  * Rubrik Security Cloud sends events in PagerDuty Common Event Format (PD-CEF) by default. The following is an example event payload:
        
        {
          "summary": "Failed backup of vSphere VM 'example-vm'.",
          "source": "Rubrik Security Cloud",
          "severity": "critical",
          "timestamp": "2024-07-18T06:39:40.46Z",
          "class": "Backup",
          "custom_details": {
            "seriesId": "ccd7a8a5-4c58-4c88-bff9-7bdffddb6099",
            "id": "c2b47274-6323-4025-b307-afed1cfb7574",
            "type": "Event",
            "objectId": "83c4a80a-4a57-5699-b399-651089135586",
            "objectName": "example-vm",
            "objectType": "VmwareVm",
            "status": "Failure",
            "clusterId": "6a271636-9392-4cba-90c5-bdbe227854ab",
            "clusterName": "production-cluster",
            "eventName": "Snapshot.BackupFailed",
            "errorId": "Snapshot.VmwareSnapshotError",
            "errorCode": "",
            "errorRemedy": "",
            "errorReason": "",
            "auditUserName": "",
            "auditUserId": "",
            "location": "vcenter.example.com",
            "url": "",
            "customerID": "rubrik-customer",
            "logicalSizeInBytes": "",
            "dataTransferredInBytes": "",
            "effectiveThroughput": ""
          }
        }
        




## Webhook limits and best practices

### Request limits

Limit | Value  
---|---  
**Max single log line** | 1 MB  
**Max QPS (queries per second)** | 15,000  
**Request timeout** | 90 seconds  
**Retry behavior** | Sender-managed. Google SecOps returns HTTP 429 when the burst limit is exceeded; the sending system must buffer and retry.  
  
## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`audit_info_label` | `additional.fields` | Merged  
`effectiveThroughput_label` | `additional.fields` | Merged  
`group_label` | `additional.fields` | Merged  
`isPolarisAudit_label` | `additional.fields` | Merged  
`label_name_label` | `additional.fields` | Merged  
`node_label` | `additional.fields` | Merged  
`orgID_label` | `additional.fields` | Merged  
`snappable_name_label` | `additional.fields` | Merged  
`snappable_type_label` | `additional.fields` | Merged  
`snapshot_date_label` | `additional.fields` | Merged  
`type_label` | `additional.fields` | Merged  
`userNote_label` | `additional.fields` | Merged  
`has_target` | `extensions.auth.type` | Mapped: `true` → `AUTHTYPE_UNSPECIFIED`  
`hunt_date` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `SCAN_HOST`, `true` → `STATUS_UPDATE`  
`has_target` | `metadata.event_type` | Mapped: `true` → `USER_LOGIN`  
`custom_details.eventName` | `metadata.product_event_type` | Directly mapped  
`custom_details.id` | `metadata.product_log_id` | Directly mapped  
`source` | `metadata.product_name` | Directly mapped  
`custom_details.url` | `metadata.url_back_to_product` | Directly mapped  
`custom_details.dataTransferredInBytes` | `network.sent_bytes` | Directly mapped  
`custom_details.customerID` | `principal.administrative_domain` | Directly mapped  
`domain` | `principal.domain.name` | Directly mapped  
`custom_details.ipAddress` | `principal.ip` | Merged  
`ip_address` | `principal.ip` | Merged  
`is_ip_assigned` | `principal.ip` | Mapped: `false` → `ip_address`  
`custom_details.clusterName` | `principal.resource.name` | Directly mapped  
`custom_details.clusterId` | `principal.resource.product_object_id` | Directly mapped  
`user_email` | `principal.user.email_addresses` | Merged  
`custom_details.auditUserName` | `principal.user.user_display_name` | Directly mapped  
`user_name` | `principal.user.user_display_name` | Directly mapped  
`action_name` | `security_result.action` | Merged  
`custom_details.status` | `security_result.action_details` | Directly mapped  
`category_temp` | `security_result.category` | Merged  
`class` | `security_result.category_details` | Merged  
`confidence` | `security_result.confidence_details` | Directly mapped  
`custom_details.errorMessage` | `security_result.description` | Directly mapped  
`access_type_label` | `security_result.detection_fields` | Merged  
`action_date_label` | `security_result.detection_fields` | Merged  
`detection_time_label` | `security_result.detection_fields` | Merged  
`directories_snoozed_label` | `security_result.detection_fields` | Merged  
`directories_unsnoozed_label` | `security_result.detection_fields` | Merged  
`document_count_label` | `security_result.detection_fields` | Merged  
`encryption_level_label` | `security_result.detection_fields` | Merged  
`errorCode_label` | `security_result.detection_fields` | Merged  
`errorId_label` | `security_result.detection_fields` | Merged  
`errorReason_label` | `security_result.detection_fields` | Merged  
`errorRemedy_label` | `security_result.detection_fields` | Merged  
`event_info_label` | `security_result.detection_fields` | Merged  
`failed_document_count_label` | `security_result.detection_fields` | Merged  
`file_matches_label` | `security_result.detection_fields` | Merged  
`files_created_count_label` | `security_result.detection_fields` | Merged  
`files_modified_count_label` | `security_result.detection_fields` | Merged  
`files_removed_count_label` | `security_result.detection_fields` | Merged  
`files_suspicious_count_label` | `security_result.detection_fields` | Merged  
`hash_tf_version_label` | `security_result.detection_fields` | Merged  
`identity_name_label` | `security_result.detection_fields` | Merged  
`num_files_with_matches_label` | `security_result.detection_fields` | Merged  
`num_hash_matches_label` | `security_result.detection_fields` | Merged  
`num_of_violating_identities_label` | `security_result.detection_fields` | Merged  
`num_yara_rule_matches_label` | `security_result.detection_fields` | Merged  
`obj_failed_label` | `security_result.detection_fields` | Merged  
`obj_partially_succeeded_label` | `security_result.detection_fields` | Merged  
`obj_succeeded_label` | `security_result.detection_fields` | Merged  
`object_matches_label` | `security_result.detection_fields` | Merged  
`policy_name_label` | `security_result.detection_fields` | Merged  
`reason_label` | `security_result.detection_fields` | Merged  
`remediation_type_label` | `security_result.detection_fields` | Merged  
`remedy_label` | `security_result.detection_fields` | Merged  
`risk_name_label` | `security_result.detection_fields` | Merged  
`seriesID_label` | `security_result.detection_fields` | Merged  
`seriesId_label` | `security_result.detection_fields` | Merged  
`skipped_document_count_label` | `security_result.detection_fields` | Merged  
`strain_name_label` | `security_result.detection_fields` | Merged  
`successful_document_count_label` | `security_result.detection_fields` | Merged  
`total_accessible_files_at_risk_count_label` | `security_result.detection_fields` | Merged  
`vm_count_label` | `security_result.detection_fields` | Merged  
`yara_tf_version_label` | `security_result.detection_fields` | Merged  
`hunt_name` | `security_result.rule_name` | Directly mapped  
`hunt_type` | `security_result.rule_type` | Directly mapped  
`is_severity_assigned` | `security_result.severity` | Mapped: `false` → `INFORMATIONAL`, `false` → `MEDIUM`  
`severity` | `security_result.severity` | Mapped: `INFO` → `INFORMATIONAL`, `WARNING` → `MEDIUM`  
`severity_name` | `security_result.severity` | Mapped: `INFO` → `INFORMATIONAL`, `WARNING` → `MEDIUM`  
`severity` | `security_result.severity_details` | Directly mapped  
`severity_name` | `security_result.severity_details` | Directly mapped  
`summary` | `security_result.summary` | Directly mapped  
`threat_feed_type` | `security_result.threat_feed_name` | Directly mapped  
`custom_details.logicalSizeInBytes` | `target.file.size` | Directly mapped  
`client_id_label` | `target.labels` | Merged  
`client_name_label` | `target.labels` | Merged  
`custom_details.location` | `target.location.name` | Directly mapped  
`custom_details.objectName` | `target.resource.name` | Directly mapped  
`object_name` | `target.resource.name` | Directly mapped  
`resource_name` | `target.resource.name` | Directly mapped  
`custom_details.objectId` | `target.resource.product_object_id` | Directly mapped  
`component` | `target.resource.resource_subtype` | Directly mapped  
`custom_details.objectType` | `target.resource.resource_subtype` | Directly mapped  
`is_object_type_assigned` | `target.resource.resource_type` | Mapped: `false` → `UNSPECIFIED`  
`class` | `target.user.email_addresses` | Mapped: `Login` → `user_email`  
`user_email` | `target.user.email_addresses` | Merged  
`each_group` | `target.user.group_identifiers` | Merged  
`custom_details.auditUserName` | `target.user.user_display_name` | Directly mapped  
`user_name` | `target.user.user_display_name` | Directly mapped  
`custom_details.auditUserId` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `metadata.product_name` | Constant: `RUBRIK SECURITY CLOUD`  
N/A | `metadata.vendor_name` | Constant: `RUBRIK`  
N/A | `principal.resource.resource_type` | Constant: `CLUSTER`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
N/A | `target.resource.resource_type` | Constant: `UNSPECIFIED`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rubrik-security-cloud-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

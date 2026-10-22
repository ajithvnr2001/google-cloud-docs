---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-virtual-scanner/
title: Collect Qualys Virtual Scanner logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:31.287885+00:00
---

# Collect Qualys Virtual Scanner logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-virtual-scanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Qualys Virtual Scanner logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This parser transforms raw JSON formatted Qualys Virtual Scanner logs into a structured format conforming to the Google Security Operations UDM. It extracts relevant fields like asset information, scan details, and detected vulnerabilities, mapping them to corresponding UDM fields for consistent representation and analysis. 

## Before you begin

Ensure that you have the following prerequisites:

  * Google Security Operations instance.
  * Privileged access to Google Cloud.
  * Privileged access to Qualys.



## Enable Required APIs:

  1. Sign in to the Google Cloud console.
  2. Go to **APIs & Services** > **Library**.
  3. Search for the following APIs and enable them: 
     * Cloud Functions API
     * Cloud Scheduler API
     * Cloud Pub/Sub (required for Cloud Scheduler to invoke functions)



## Create a Google Cloud Storage Bucket

  1. Sign in to the Google Cloud console.
  2. Go to the **Cloud Storage Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  3. Click **Create**.

  4. Configure the bucket:

     * **Name** : enter a unique name that meets the bucket name requirements (for example, **qualys-vscanner-bucket**).
     * **Choose where to store your data** : select a location.
     * **Choose a storage class for your data** : either select a **default storage class** for the bucket, or select **Autoclass** for automatic storage class management.
     * **Choose how to control access to objects** : select **not** to enforce **public access prevention** , and select an **access control model** for your bucket's objects.
**Note:** If public access prevention is already enforced by your project's organization policy, the **Prevent public access** checkbox is locked.
     * **Storage class** : Choose based on your needs (for example, **Standard**).
  5. Click **Create**.


**Note:** Do not set a retention policy, as the last data entry may need to be overwritten in case of a timeout.

## Create a Google Cloud Service Account

  1. Go to to **IAM & Admin** > **Service Accounts**.
  2. Create a new service account. 
  3. Give it a descriptive name (for example, **qualys-user**).
  4. Grant the service account with **Storage Object Admin** role on the Cloud Storage bucket you created in the previous step.
  5. Grant the service account with **Cloud Functions Invoker** role.
  6. Create an [**SSH key**](https://docs.cloud.google.com/iam/docs/keys-create-delete) for the service account.
  7. Download a JSON key file for the service account. Keep this file secure.



## Optional: Create a dedicated API User in Qualys

  1. Sign in to the Qualys console.
  2. Go to **Users**.
  3. Click **New** > **User**.
  4. Enter the **General Information** required for the user.
  5. Select **User Role** tab.
  6. Make sure the role has the **API Access** checkbox selected.
  7. Click **Save**.



## Identify your specific Qualys API URL

### Option 1

Identify your URLs as mentioned in the [platform identification](https://www.qualys.com/platform-identification).

### Option 2

  1. Sign in to the Qualys console.
  2. Go to **Help** > **About**.
  3. Scroll to see this information under Security Operations Center (SOC).
  4. Copy the Qualys API URL.



## Configure the Cloud Function

  1. Go to **Cloud Functions** in the Google Cloud console.
  2. Click **Create Function**.
  3. Configure the Function:

     * **Name** : enter a name for your function (for example, **fetch-qualys-vscanner**).
     * **Region** : select a region close to your Bucket.
     * **Trigger** : choose HTTP trigger if needed or Cloud Pub/Sub for scheduled execution.
     * **Authentication** : secure with authentication.
     * **Write the Code** with an inline editor:
**Note:** Replace the following placeholders with your specific data values: `<bucket-name>`, `<qualys-username>`, `<qualys-password>`, `<qualys_base_url>`.
    
    ```python
    from google.cloud import storage
    import requests
    import base64
    import json
    
    # Google Cloud Storage Configuration
    BUCKET_NAME = "<bucket-name>"
    FILE_NAME = "qualys_virtual_scanners.json"
    
    # Qualys API Credentials
    QUALYS_USERNAME = "qualys-username"
    QUALYS_PASSWORD = "<qualys-password>"
    QUALYS_BASE_URL = "https://<qualys_base_url>"  # for example, https://qualysapi.qualys.com
    
    def fetch_virtual_scanners():
        """Fetch Virtual Scanner details from Qualys."""
        auth = base64.b64encode(f"{QUALYS_USERNAME}:{QUALYS_PASSWORD}".encode()).decode()
        headers = {
            "Authorization": f"Basic {auth}",
            "Content-Type": "application/xml"
        }
        url = f"{QUALYS_BASE_URL}/api/2.0/fo/scanner/"
        payload = {
            "action": "list",
            "scanner_type": "virtual"
        }
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        return response.text  # Qualys API returns XML data
    
    def upload_to_gcs(data):
        """Upload data to Google Cloud Storage."""
        client = storage.Client()
        bucket = client.get_bucket(BUCKET_NAME)
        blob = bucket.blob(FILE_NAME)
        blob.upload_from_string(data, content_type="application/xml")
    
    def main(request):
        """Cloud Function entry point."""
        try:
            scanners = fetch_virtual_scanners()
            upload_to_gcs(scanners)
            return "Qualys Virtual Scanners data uploaded to Cloud Storage successfully!"
        except Exception as e:
            return f"An error occurred: {e}", 500
    ```
    

  4. Click **Deploy** after completing the configuration.




## Configure Cloud Scheduler

  1. Go to **Cloud Scheduler** in the Google Cloud console.
  2. Click **Create Job**.
  3. Configure the job:

     * **Name** : enter a name for your job (for example, **trigger-fetch-qualys-vscanner**).
     * **Frequency** : use **cron** syntax to specify the schedule (for example, 0 0 * * * for daily at midnight).
     * **Time Zone** : set your preferred time zone.
     * **Trigger Type** : Choose **HTTP**.
     * **Trigger URL** : enter the Cloud Function's URL (found in the function details after deployment).
     * **Method** : Choose **POST**.
**Note:** If authentication is enabled for the function, select **Service Account** and ensure the account has the **Cloud Functions Invoker** role.
  4. Create the Job.




## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed; for example, **Qualys Virtual Scanner Logs**.
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Qualys Virtual Scanner** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage Bucket URI** : the Google Cloud storage bucket source URI.
     * **Source deletion option** : select the deletion option according to your preference.
**Note:** If you select the `Delete transferred files` or the `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account. * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
ASSET_ID | entity.entity.asset.asset_id | Direct mapping from `ASSET_ID` field.  
CLOUD_PROVIDER_TAGS.CLOUD_TAG.NAME | entity.relations.entity.resource.attribute.labels.key | Direct mapping from `CLOUD_PROVIDER_TAGS.CLOUD_TAG.NAME` field.  
CLOUD_PROVIDER_TAGS.CLOUD_TAG.VALUE | entity.relations.entity.resource.attribute.labels.value | Direct mapping from `CLOUD_PROVIDER_TAGS.CLOUD_TAG.VALUE` field.  
CLOUD_RESOURCE_ID | entity.relations.entity.resource.id | Direct mapping from `CLOUD_RESOURCE_ID` field.  
DETECTION_LIST.DETECTION.FIRST_FOUND_DATETIME | entity.metadata.threat.first_discovered_time | Direct mapping from `DETECTION_LIST.DETECTION.FIRST_FOUND_DATETIME` field, converted to timestamp.  
DETECTION_LIST.DETECTION.FIRST_REOPENED_DATETIME | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.FIRST_REOPENED_DATETIME` field. The key is hardcoded as "FIRST_REOPENED_DATETIME".  
DETECTION_LIST.DETECTION.IS_DISABLED | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.IS_DISABLED` field. The key is hardcoded as "IS_DISABLED".  
DETECTION_LIST.DETECTION.LAST_FIXED_DATETIME | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.LAST_FIXED_DATETIME` field. The key is hardcoded as "LAST_FIXED_DATETIME".  
DETECTION_LIST.DETECTION.LAST_FOUND_DATETIME | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.LAST_FOUND_DATETIME` field. The key is hardcoded as "LAST_FOUND_DATETIME".  
DETECTION_LIST.DETECTION.LAST_PROCESSED_DATETIME | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.LAST_PROCESSED_DATETIME` field. The key is hardcoded as "LAST_PROCESSED_DATETIME".  
DETECTION_LIST.DETECTION.LAST_REOPENED_DATETIME | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.LAST_REOPENED_DATETIME` field. The key is hardcoded as "LAST_REOPENED_DATETIME".  
DETECTION_LIST.DETECTION.LAST_TEST_DATETIME | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.LAST_TEST_DATETIME` field. The key is hardcoded as "LAST_TEST_DATETIME".  
DETECTION_LIST.DETECTION.LAST_UPDATE_DATETIME | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.LAST_UPDATE_DATETIME` field. The key is hardcoded as "LAST_UPDATE_DATETIME".  
DETECTION_LIST.DETECTION.PORT | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.PORT` field. The key is hardcoded as "PORT".  
DETECTION_LIST.DETECTION.PROTOCOL | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.PROTOCOL` field. The key is hardcoded as "PROTOCOL".  
DETECTION_LIST.DETECTION.QID | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.QID` field. The key is hardcoded as "QID".  
DETECTION_LIST.DETECTION.RESULTS | entity.metadata.threat.summary | Direct mapping from `DETECTION_LIST.DETECTION.RESULTS` field.  
DETECTION_LIST.DETECTION.SEVERITY | entity.metadata.threat.severity_details | Direct mapping from `DETECTION_LIST.DETECTION.SEVERITY` field.  
DETECTION_LIST.DETECTION.SSL | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.SSL` field. The key is hardcoded as "SSL".  
DETECTION_LIST.DETECTION.STATUS | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.STATUS` field. The key is hardcoded as "STATUS".  
DETECTION_LIST.DETECTION.TIMES_FOUND | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.TIMES_FOUND` field. The key is hardcoded as "TIMES_FOUND".  
DETECTION_LIST.DETECTION.TIMES_REOPENED | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.TIMES_REOPENED` field. The key is hardcoded as "TIMES_REOPENED".  
DETECTION_LIST.DETECTION.TYPE | entity.metadata.threat.severity | Mapped from `DETECTION_LIST.DETECTION.TYPE` field. If the value is "info" (case-insensitive), it's mapped to "INFORMATIONAL". Otherwise, it's added as a detection field with key "TYPE".  
DETECTION_LIST.DETECTION.UNIQUE_VULN_ID | entity.metadata.threat.detection_fields.value | Direct mapping from `DETECTION_LIST.DETECTION.UNIQUE_VULN_ID` field. The key is hardcoded as "UNIQUE_VULN_ID".  
DNS | entity.entity.asset.hostname | Mapped from `DNS` field if `DNS_DATA.HOSTNAME` is empty.  
DNS_DATA.HOSTNAME | entity.entity.asset.hostname | Direct mapping from `DNS_DATA.HOSTNAME` field.  
EC2_INSTANCE_ID | entity.relations.entity.resource.product_object_id | Direct mapping from `EC2_INSTANCE_ID` field.  
ID | entity.entity.asset.product_object_id | Direct mapping from `ID` field.  
ID | entity.metadata.product_entity_id | Direct mapping from `ID` field.  
IP | entity.entity.ip | Direct mapping from `IP` field.  
LAST_SCAN_DATETIME | entity.metadata.interval.start_time | Direct mapping from `LAST_SCAN_DATETIME` field, converted to timestamp.  
METADATA.AZURE.ATTRIBUTE.NAME | entity.relations.entity.resource.attribute.labels.key | Direct mapping from `METADATA.AZURE.ATTRIBUTE.NAME` field.  
METADATA.AZURE.ATTRIBUTE.VALUE | entity.relations.entity.resource.attribute.labels.value | Direct mapping from `METADATA.AZURE.ATTRIBUTE.VALUE` field.  
OS | entity.entity.asset.platform_software.platform | Mapped from `OS` field. If the value contains "windows" (case-insensitive), it's mapped to "WINDOWS". If it contains "Linux" (case-insensitive), it's mapped to "LINUX".  
TAGS.TAG.NAME | entity.relations.entity.resource.attribute.labels.key | Direct mapping from `TAGS.TAG.NAME` field.  
TAGS.TAG.TAG_ID | entity.relations.entity.resource.attribute.labels.value | Mapped from `TAGS.TAG.TAG_ID` field. The value is prefixed with "TAG_ID: ".  
| entity.metadata.collected_timestamp | The timestamp of the log entry.  
| entity.metadata.entity_type | Determined based on the presence of `IP` field. If `IP` is present, it's set to "IP_ADDRESS". Otherwise, it's set to "ASSET".  
| entity.metadata.interval.end_time | Hardcoded to a very large timestamp value (253402300799 seconds).  
| entity.metadata.product_name | Hardcoded to "QUALYS_VIRTUAL_SCANNER".  
| entity.metadata.vendor_name | Hardcoded to "QUALYS_VIRTUAL_SCANNER".  
| entity.relations.entity.resource.resource_type | If `CLOUD_SERVICE` is "VM", it's set to "VIRTUAL_MACHINE".  
| entity.relations.entity_type | Hardcoded to "RESOURCE".  
| entity.relations.relationship | Hardcoded to "MEMBER".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/qualys-virtual-scanner-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

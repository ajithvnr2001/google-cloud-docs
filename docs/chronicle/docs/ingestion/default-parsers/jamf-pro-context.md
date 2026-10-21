---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-pro-context/
title: Collect Jamf Pro context logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:23.908003+00:00
---

# Collect Jamf Pro context logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-pro-context/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Jamf Pro context logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Jamf Pro context logs (device & user context) to Google Security Operations using Cloud Storage with Cloud Run functions, Pub/Sub, and Cloud Scheduler. Jamf Pro is a comprehensive management solution for Apple devices, providing device inventory, user context, and configuration management capabilities.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage Cloud Storage buckets
  * Permissions to manage IAM policies on Cloud Storage buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Jamf Pro tenant



## Configure Jamf API Role

  1. Sign in to Jamf web UI.
  2. Go to **Settings > System section > API Roles and Clients**.
  3. Select the **API Roles** tab.
  4. Click **New**.
  5. Enter a display name for the API role (for example, `context_role`).
  6. In the **Jamf Pro API role privileges** , type the name of a privilege, and then select it from the menu:

     * Computer Inventory
     * Mobile Device Inventory
**Note:** You can continue adding more privileges until you are finished.
  7. Click **Save**.




## Configure Jamf API Client

  1. In Jamf Pro, go to **Settings > System section > API roles and clients**.
  2. Select the **API Clients** tab.
  3. Click **New**.
  4. Enter a display name for the API client (for example, `context_client`).
  5. In the **API Roles** field, add the `context_role` role you previously created.
  6. Under **Access Token Lifetime** , enter the time in seconds for the access tokens to be valid.
  7. Click **Save**.
  8. Click **Edit**.
  9. Click **Enable API Client**.
  10. Click **Save**.



## Configure Jamf Client Secret

  1. In Jamf Pro, go to the newly created API client.
  2. Click **Generate Client Secret**.
  3. In a confirmation screen, click **Create Secret**.
  4. Save the following parameters in a secure location: 
     * **Base URL** : `https://<your>.jamfcloud.com`
     * **Client ID** : UUID.
     * **Client Secret** : Value is shown once.



## Create Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `jamfpro`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to Cloud Storage bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `jamf-pro-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Jamf Pro context logs`.
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section, add the following roles: 
     1. Click **Select a role**.
     2. Search for and select **Storage Object Admin**.
     3. Click **\+ Add another role**.
     4. Search for and select **Cloud Run Invoker**.
     5. Click **\+ Add another role**.
     6. Search for and select **Cloud Functions Invoker**.
  6. Click **Continue**.
  7. Click **Done**.



These roles are required for:

  * **Storage Object Admin** : Write logs to Cloud Storage bucket and manage state files
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allow function invocation



### Grant IAM permissions on Cloud Storage bucket

Grant the service account write permissions on the Cloud Storage bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `jamf-pro-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `jamf-pro-context-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Jamf Pro API and write them to Cloud Storage.

  1. In the **console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `jamf-pro-context-collector`  
**Region** | Select region matching your Cloud Storage bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Pub/Sub**.
     3. In**Select a Pub/Sub topic** , choose the Pub/Sub topic (`jamf-pro-context-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check**Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`jamf-pro-collector-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `jamfpro`  
`GCS_PREFIX` | `jamf-pro/context/`  
`JAMF_CLIENT_ID` | Enter Jamf Client ID  
`JAMF_CLIENT_SECRET` | Enter Jamf Client Secret  
`JAMF_BASE_URL` | Enter Jamf URL, replace `<your>` in `https://<your>.jamfcloud.com`  
`PAGE_SIZE` | `200`  
  10. Scroll down in the **Variables & Secrets** tab to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
     * Click **Done**.
  12. Scroll down to **Execution environment** :

     * Select **Default** (recommended).
  13. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  14. Click **Create**.

  15. Wait for the service to be created (1-2 minutes).

  16. After the service is created, the **inline code editor** will open automatically.




### Add function code

  1. Enter **main** in **Function entry point**
  2. In the inline code editor, create two files:

     * First file: **main.py:**
    
    import functions_framework
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import json
    import os
    import urllib3
    from datetime import datetime, timezone
    import gzip
    import io
    import time
    
    # Initialize HTTP client
    http = urllib3.PoolManager()
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    # Configuration
    BASE_URL = os.environ.get("JAMF_BASE_URL", "").rstrip("/")
    CLIENT_ID = os.environ.get("JAMF_CLIENT_ID")
    CLIENT_SECRET = os.environ.get("JAMF_CLIENT_SECRET")
    GCS_BUCKET = os.environ.get("GCS_BUCKET")
    GCS_PREFIX = os.environ.get("GCS_PREFIX", "jamf-pro/context/")
    PAGE_SIZE = int(os.environ.get("PAGE_SIZE", "200"))
    
    SECTIONS = [
        "GENERAL", "HARDWARE", "OPERATING_SYSTEM", "USER_AND_LOCATION",
        "DISK_ENCRYPTION", "SECURITY", "EXTENSION_ATTRIBUTES", "APPLICATIONS",
        "CONFIGURATION_PROFILES", "LOCAL_USER_ACCOUNTS", "CERTIFICATES",
        "SERVICES", "PRINTERS", "SOFTWARE_UPDATES", "GROUP_MEMBERSHIPS",
        "CONTENT_CACHING", "STORAGE", "FONTS", "PACKAGE_RECEIPTS",
        "PLUGINS", "ATTACHMENTS", "LICENSED_SOFTWARE", "IBEACONS", "PURCHASING"
    ]
    
    # Cached access token, refreshed shortly before it expires
    _token_cache = {"value": None, "expires_at": 0.0}
    
    def get_token():
        """OAuth2 client credentials > access_token"""
        url = f"{BASE_URL}/api/oauth/token"
    
        fields = {
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        }
    
        # encode_multipart=False is required. It sends a real
        # application/x-www-form-urlencoded body, which is what the Jamf token
        # endpoint expects. Without it, urllib3 sends a multipart/form-data body
        # and Jamf cannot read grant_type, client_id and client_secret.
        response = http.request(
            'POST',
            url,
            fields=fields,
            encode_multipart=False,
            timeout=30.0
        )
    
        if response.status != 200:
            raise Exception(f"Failed to get token: {response.status} {response.data.decode('utf-8')}")
    
        data = json.loads(response.data.decode('utf-8'))
        return data["access_token"], int(data.get("expires_in", 1200))
    
    def get_valid_token():
        """Return a cached token, refreshing it before it expires."""
        now = time.time()
        if _token_cache["value"] and now < _token_cache["expires_at"] - 60:
            return _token_cache["value"]
    
        token, ttl = get_token()
        _token_cache["value"] = token
        _token_cache["expires_at"] = now + ttl
        return token
    
    def fetch_page(token, page):
        """GET /api/v1/computers-inventory with sections & pagination"""
        url = f"{BASE_URL}/api/v1/computers-inventory"
    
        # Build query parameters
        params = [("page", str(page)), ("page-size", str(PAGE_SIZE))]
        params.extend([("section", s) for s in SECTIONS])
    
        # Encode parameters
        query_string = "&".join([f"{k}={v}" for k, v in params])
        full_url = f"{url}?{query_string}"
    
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json"
        }
    
        response = http.request(
            'GET',
            full_url,
            headers=headers,
            timeout=60.0
        )
    
        if response.status != 200:
            raise Exception(f"Failed to fetch page {page}: {response.status} {response.data.decode('utf-8')}")
    
        return json.loads(response.data.decode('utf-8'))
    
    def write_ndjson_gz(objs, when):
        buf = io.BytesIO()
        with gzip.GzipFile(filename="-", mode="wb", fileobj=buf, mtime=int(time.time())) as gz:
            for obj in objs:
                line = json.dumps(obj, separators=(",", ":")) + "\n"
                gz.write(line.encode("utf-8"))
    
        buf.seek(0)
    
        prefix = GCS_PREFIX.strip("/") + "/" if GCS_PREFIX else ""
        key = f"{prefix}{when:%Y/%m/%d}/jamf_pro_context_{int(when.timestamp())}.ndjson.gz"
    
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
        blob = bucket.blob(key)
        blob.[upload_from_file](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_file)(buf, content_type="application/gzip")
    
        return key
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch Jamf Pro context logs and write to Cloud Storage.
    
        Each computer is written exactly as Jamf returns it: the inventory sections
        (general, hardware, operatingSystem, userAndLocation, and so on) are top-level
        keys on the record. The default parser reads this shape directly, so the records
        are not reshaped here.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        if not all([BASE_URL, CLIENT_ID, CLIENT_SECRET, GCS_BUCKET]):
            print("Error: Missing required environment variables")
            return
    
        try:
            page = 0
            total = 0
            batch = []
            now = datetime.now(timezone.utc)
    
            while True:
                payload = fetch_page(get_valid_token(), page)
                results = payload.get("results") or []
    
                if not results:
                    break
    
                # Write the Jamf records as returned; do not rename or nest fields.
                batch.extend(results)
                total += len(results)
    
                if len(batch) >= 5000:
                    key = write_ndjson_gz(batch, now)
                    print(f"Wrote {len(batch)} records to gs://{GCS_BUCKET}/{key}")
                    batch = []
    
                if len(results) < PAGE_SIZE:
                    break
    
                page += 1
    
            if batch:
                key = write_ndjson_gz(batch, now)
                print(f"Wrote {len(batch)} records to gs://{GCS_BUCKET}/{key}")
    
            print(f"Successfully processed {total} total records")
    
        except Exception as e:
            print(f"Error processing Jamf Pro context logs: {str(e)}")
            raise
    

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).




## Create Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `jamfpro-context-schedule-1h`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`jamf-pro-context-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Test the scheduler job

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > jamf-pro-context-collector > Logs**.
  4. Verify the function executed successfully.
  5. Check the Cloud Storage bucket to confirm logs were written.



## Configure a feed in Google SecOps to ingest Jamf Pro context logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Jamf Pro Context logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Jamf pro context** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email is displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

  11. **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
         
         gs://jamfpro/jamf-pro/context/
         

eplace `jamfpro` with the actual name of the bucket.

**Note:** Always include the trailing slash (/) at the end of the URI.


  * **Source deletion option** : Select the deletion option according to your preference:

    * **Never** : Never deletes any files after transfers (recommended for testing).
    * **Delete transferred files** : Deletes files after successful transfer.
    * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
  * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

  * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

  * **Ingestion labels** : The label to be applied to the events from this feed.



  1. Click **Next**.
  2. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your Cloud Storage bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details:
  6. **Add principals** : Paste the Google SecOps service account email.
  7. **Assign roles** : Select **Storage Object Viewer**.
  8. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-pro-context-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

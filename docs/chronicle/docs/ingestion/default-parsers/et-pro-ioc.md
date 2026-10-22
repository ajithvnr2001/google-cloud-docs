---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/et-pro-ioc/
title: Collect Proofpoint Emerging Threats Pro IOC logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:35.458510+00:00
---

# Collect Proofpoint Emerging Threats Pro IOC logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/et-pro-ioc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Proofpoint Emerging Threats Pro IOC logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Proofpoint Emerging Threats Pro IOC logs to Google Security Operations using Google Cloud Storage. Emerging Threats Intelligence publishes hourly reputation lists for IPs and domains in CSV format with threat intelligence data including categories, scores, and temporal information. The parser code processes CSV formatted ET_PRO threat intelligence data. It extracts IP addresses, domains, categories, scores, and other relevant information, mapping them to both a standardized IOC format and the Chronicle UDM schema for further analysis and use within Google SecOps.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Proofpoint ET Intelligence subscription with access to reputation lists
  * ET Intelligence API key from <https://etadmin.proofpoint.com/api-access>



## Collect Emerging Threats Pro prerequisites

  1. Sign in to the ET Intelligence Admin Portal at <https://etadmin.proofpoint.com>.
  2. Go to **API Access**.
  3. Copy and save your **API Key**.
  4. Contact your Proofpoint representative to obtain: 
     * Detailed IP Reputation List URL
     * Detailed Domain Reputation List URL



ET Intelligence provides separate CSV files for IP and Domain reputation lists, updated hourly. Use the "detailed" format which includes these columns:

  * **Domain list** : Domain Name, Category, Score, First Seen, Last Seen, Ports
  * **IP list** : IP Address, Category, Score, First Seen, Last Seen, Ports



The detailed format URLs typically follow this pattern:

  * IP list: `https://rules.emergingthreatspro.com/[your-code]/reputation/detailed-iprepdata.txt`
  * Domain list: `https://rules.emergingthreatspro.com/[your-code]/reputation/detailed-domainrepdata.txt`



The Authorization header must contain the raw API key value without a Bearer prefix, matching Emerging Threats API expectations.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `et-pro-ioc-bucket`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `et-pro-ioc-fetcher-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Proofpoint ET Pro IOC logs`.
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

  * **Storage Object Admin** : Write logs to GCS bucket and manage state files
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allow function invocation



### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `et-pro-ioc-fetcher-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `et-pro-ioc-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Proofpoint ET Intelligence API and writes them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `et-pro-ioc-fetcher`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `et-pro-ioc-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `et-pro-ioc-fetcher-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `et-pro-ioc-bucket` | GCS bucket name  
`GCS_PREFIX` | `et-pro-ioc` | Prefix for log files  
`STATE_KEY` | `et-pro-ioc/state.json` | State file path  
`ET_API_KEY` | `your-et-api-key` | ET Intelligence API key  
`ET_IP_LIST_URL` | `https://rules.emergingthreatspro.com/[your-code]/reputation/detailed-iprepdata.txt` | Detailed IP Reputation List URL  
`ET_DOMAIN_LIST_URL` | `https://rules.emergingthreatspro.com/[your-code]/reputation/detailed-domainrepdata.txt` | Detailed Domain Reputation List URL  
`TIMEOUT` | `120` | HTTP request timeout in seconds  
  10. Scroll down in the **Variables & Secrets** tab to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
     * Click **Done**.
  12. Scroll to **Execution environment** :

     * Select **Default** (recommended).
  13. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  14. Click **Create**.

  15. Wait for the service to be created (1-2 minutes).

  16. After the service is created, the **inline code editor** opens automatically.




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
    import time
    
    # Initialize HTTP client with timeouts
    http = urllib3.PoolManager(
        timeout=urllib3.Timeout(connect=5.0, read=30.0),
        retries=False,
    )
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch ET Pro IOC reputation lists and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        # Get environment variables
        bucket_name = os.environ.get('GCS_BUCKET')
        prefix = os.environ.get('GCS_PREFIX', 'et-pro-ioc').strip('/')
        state_key = os.environ.get('STATE_KEY', f'{prefix}/state.json')
        et_api_key = os.environ.get('ET_API_KEY')
        et_ip_list_url = os.environ.get('ET_IP_LIST_URL')
        et_domain_list_url = os.environ.get('ET_DOMAIN_LIST_URL')
        timeout = int(os.environ.get('TIMEOUT', '120'))
    
        if not all([bucket_name, et_api_key, et_ip_list_url, et_domain_list_url]):
            print('Error: Missing required environment variables')
            return
    
        try:
            # Get GCS bucket
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
            # Generate timestamp for file naming
            now = datetime.now(timezone.utc)
            timestamp = now.strftime('%Y/%m/%d/%H%M%S')
    
            results = []
            errors = []
    
            # Fetch IP reputation list
            try:
                print('Fetching IP reputation list...')
                ip_data = fetch_with_retry(et_ip_list_url, et_api_key, timeout)
                ip_key = f'{prefix}/ip/{timestamp}.csv'
                save_to_gcs(bucket, ip_key, ip_data)
                results.append({'type': 'ip', 'key': ip_key, 'size': len(ip_data)})
                print(f'Successfully fetched IP list: {len(ip_data)} bytes')
            except Exception as e:
                error_msg = f'Failed to fetch IP list: {str(e)}'
                print(error_msg)
                errors.append(error_msg)
    
            # Fetch Domain reputation list
            try:
                print('Fetching Domain reputation list...')
                domain_data = fetch_with_retry(et_domain_list_url, et_api_key, timeout)
                domain_key = f'{prefix}/domain/{timestamp}.csv'
                save_to_gcs(bucket, domain_key, domain_data)
                results.append({'type': 'domain', 'key': domain_key, 'size': len(domain_data)})
                print(f'Successfully fetched Domain list: {len(domain_data)} bytes')
            except Exception as e:
                error_msg = f'Failed to fetch Domain list: {str(e)}'
                print(error_msg)
                errors.append(error_msg)
    
            # Save state
            state = {
                'last_fetch': now.isoformat(),
                'results': results,
                'errors': errors
            }
            save_state(bucket, state_key, state)
    
            if errors:
                print(f'Completed with {len(errors)} error(s)')
            else:
                print('Successfully completed all fetches')
    
        except Exception as e:
            print(f'Error processing logs: {str(e)}')
            raise
    
    def fetch_with_retry(url, api_key, timeout, max_retries=3):
        """Fetch URL with retry logic for rate limits."""
        if not url.lower().startswith('https://'):
            raise ValueError('Only HTTPS URLs are allowed')
    
        headers = {'Authorization': api_key}
    
        for attempt in range(max_retries):
            try:
                response = http.request('GET', url, headers=headers, timeout=timeout)
    
                if response.status == 200:
                    return response.data
                elif response.status == 429:
                    # Rate limited, wait and retry
                    wait_time = min(30 * (2 ** attempt), 300)
                    print(f'Rate limited, waiting {wait_time}s...')
                    time.sleep(wait_time)
                else:
                    raise Exception(f'HTTP {response.status}: {response.reason}')
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                time.sleep(5 * (attempt + 1))
    
        raise Exception(f'Failed to fetch {url} after {max_retries} attempts')
    
    def save_to_gcs(bucket, key, content):
        """Save content to GCS with appropriate content type."""
        blob = bucket.blob(key)
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(content, content_type='text/csv')
        print(f'Saved {len(content)} bytes to gs://{bucket.name}/{key}')
    
    def save_state(bucket, key, state):
        """Save state to GCS."""
        try:
            blob = bucket.blob(key)
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                json.dumps(state, indent=2),
                content_type='application/json'
            )
        except Exception as e:
            print(f'Warning: Could not save state: {str(e)}')
    

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create Cloud Scheduler job

Cloud Scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `et-pro-ioc-fetcher-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `et-pro-ioc-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

  * Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every hour | `0 * * * *` | Standard (recommended for ET Pro IOC)  
Every 2 hours | `0 */2 * * *` | Lower frequency  
Every 6 hours | `0 */6 * * *` | Minimal updates  
**Note:** ET Intelligence updates reputation lists hourly, so hourly collection is recommended.



### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click the function name (`et-pro-ioc-fetcher`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for the following:
         
         Fetching IP reputation list...
         Successfully fetched IP list: X bytes
         Fetching Domain reputation list...
         Successfully fetched Domain list: X bytes
         Successfully completed all fetches
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folders (`et-pro-ioc/ip/` and `et-pro-ioc/domain/`).

  11. Verify that new `.csv` files were created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check ET_API_KEY in environment variables
  * **HTTP 403** : Verify API key has required permissions
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `ET Pro IOC - IP Reputation`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Emerging Threats Pro** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email is displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Configure feeds in Google SecOps to ingest Proofpoint Emerging Threats Pro IOC logs

You need to create two separate feeds - one for IP reputation and one for Domain reputation.

### Create IP Reputation Feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter `ET Pro IOC - IP Reputation`.
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Emerging Threats Pro** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://et-pro-ioc-bucket/et-pro-ioc/ip/
           

       * Replace `et-pro-ioc-bucket` with your actual GCS bucket name.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




### Create Domain Reputation Feed

Repeat the feed creation process:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter `ET Pro IOC - Domain Reputation`.
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Emerging Threats Pro** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
    
    gs://et-pro-ioc-bucket/et-pro-ioc/domain/
    

Replace `et-pro-ioc-bucket` with your actual GCS bucket name.

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label applied to the events from this feed.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
category | This field is used in the parser logic but not mapped directly to the UDM. | It determines the value of event.ioc.categorization through a lookup table.  
collection_time.nanos | event.idm.entity.metadata.collected_timestamp.nanos | Directly mapped from the raw log.  
collection_time.seconds | event.idm.entity.metadata.collected_timestamp.seconds | Directly mapped from the raw log.  
data | This field is parsed into multiple UDM fields based on its content. |   
first_seen | event.idm.entity.metadata.interval.start_time | Parsed as a date and mapped to the UDM.  
first_seen | event.ioc.active_timerange.start | Parsed as a date and mapped to the UDM.  
ip_or_domain | event.idm.entity.entity.hostname | Mapped to the UDM if the grok pattern extracts a host from the field.  
ip_or_domain | event.idm.entity.entity.ip | Mapped to the UDM if the grok pattern does not extract a host from the field.  
ip_or_domain | event.ioc.domain_and_ports.domain | Mapped to the UDM if the grok pattern extracts a host from the field.  
ip_or_domain | event.ioc.ip_and_ports.ip_address | Mapped to the UDM if the grok pattern does not extract a host from the field.  
last_seen | event.idm.entity.metadata.interval.end_time | Parsed as a date and mapped to the UDM.  
last_seen | event.ioc.active_timerange.end | Parsed as a date and mapped to the UDM.  
ports | event.idm.entity.entity.labels.value | Parsed, joined with comma delimiter, and mapped to the UDM if there are multiple ports.  
ports | event.idm.entity.entity.port | Parsed and mapped to the UDM if there is only one port.  
ports | event.ioc.domain_and_ports.ports | Parsed and mapped to the UDM if the grok pattern extracts a host from the field.  
ports | event.ioc.ip_and_ports.ports | Parsed and mapped to the UDM if the grok pattern does not extract a host from the field.  
score | event.ioc.confidence_score | Directly mapped from the raw log.  
| event.idm.entity.entity.labels.key | Set to "ports" if there are multiple ports.  
| event.idm.entity.metadata.entity_type | Set to "DOMAIN_NAME" if the grok pattern extracts a host from the ip_or_domain field, otherwise set to "IP_ADDRESS".  
| event.idm.entity.metadata.threat.category | Set to "SOFTWARE_MALICIOUS".  
| event.idm.entity.metadata.threat.category_details | Derived from the category field using a lookup table.  
| event.idm.entity.metadata.threat.threat_name | Set to "ET Intelligence Rep List".  
| event.idm.entity.metadata.vendor_name | Set to "ET_PRO_IOC".  
| event.ioc.feed_name | Set to "ET Intelligence Rep List".  
| event.ioc.raw_severity | Set to "Malicious".  
| timestamp.nanos | Copied from collection_time.nanos.  
| timestamp.seconds | Copied from collection_time.seconds.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/et-pro-ioc-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

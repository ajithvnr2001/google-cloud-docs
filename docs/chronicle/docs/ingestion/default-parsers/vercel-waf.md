---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vercel-waf/
title: Collect Vercel WAF logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:30:41.234105+00:00
---

# Collect Vercel WAF logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vercel-waf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Vercel WAF logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest Vercel WAF logs to Google Security Operations using Google Cloud Storage V2.

Vercel WAF is a web application firewall integrated into the Vercel edge network for protecting serverless applications. It inspects incoming HTTP requests at the edge and applies security rules to block malicious traffic before it reaches your application. Because Vercel WAF logs must be exported from the Vercel platform, you must upload those logs to a Google Cloud Storage (GCS) bucket, and then configure a Google SecOps feed to ingest them.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with billing enabled
  * A Vercel account with access to WAF logs (Pro or Enterprise plan)
  * A Vercel API token or Log Drain configured to export WAF logs



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `vercel-waf-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your Google SecOps instance (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.

**Note:** Record the bucket name. You will use it when configuring the Google SecOps feed.



## Export Vercel WAF logs to GCS

Vercel provides WAF logs through Log Drains and the Vercel REST API. Configure log export, then upload to GCS.

### Option A: Configure Vercel Log Drains (Recommended)

Vercel Log Drains stream logs in real-time to an external endpoint.

  1. Sign in to the [Vercel Dashboard](https://vercel.com/dashboard).
  2. Go to your team settings: **Settings > Log Drains**.
  3. Click **Add Log Drain**.
  4. Configure the log drain: 
     * **Delivery Format** : Select **JSON**.
     * **Sources** : Select **Firewall** to include WAF events.
     * **Environments** : Select the environments to monitor (Production, Preview, Development).
     * **Endpoint** : Enter the URL of your intermediate receiver (for example, a Cloud Run function endpoint that writes to GCS).
  5. Click **Add Log Drain**.
  6. Verify that logs are being delivered to your endpoint.

**Note:** Vercel Log Drains require a Pro or Enterprise plan. The intermediate receiver should write incoming log data to GCS.



### Option B: Export via Vercel REST API

  1. Generate a Vercel API token in **Settings > Tokens**.
  2. Use the Vercel REST API to retrieve firewall events:
         
         curl -H "Authorization: Bearer YOUR_VERCEL_TOKEN" \
           "https://api.vercel.com/v1/security/firewall/events?teamId=YOUR_TEAM_ID&projectId=YOUR_PROJECT_ID&limit=100" \
           -o vercel-waf-events.json
         

**Note:** Replace `YOUR_VERCEL_TOKEN`, `YOUR_TEAM_ID`, and `YOUR_PROJECT_ID` with your Vercel credentials.



## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Vercel WAF Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Vercel WAF** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `vercel-waf-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email (for example, `chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of **Storage Object Viewer**.



## Configure the Google SecOps feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Vercel WAF Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Vercel WAF** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI:
           
           gs://vercel-waf-logs/vercel-waf/
           

       * Replace `vercel-waf-logs` with your GCS bucket name.
       * Replace `vercel-waf` with your configured prefix path.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the Google SecOps service account must have **Storage Object Admin** role instead of **Storage Object Viewer**. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
record.requestId, record.proxy.timestamp, record.proxy.region, record.proxy.errorCode, record.proxy.vercelCache, record.proxy.pathType, record.proxy.referer, record.proxy.cacheId, record.proxy.wafAction, record.proxy.scheme, record.proxy.userAgent, record.environment | additional.fields | Additional event metadata  
| metadata.event_type | Type of event  
record.deploymentId | metadata.product_deployment_id | Product-specific deployment ID  
record.id | metadata.product_log_id | Product-specific log ID  
record.proxy.method | network.http.method | HTTP method  
record.statusCode | network.http.response_code | HTTP response code  
record.source | principal.asset.hostname | Hostname of the asset associated with the principal  
record.host | principal.hostname | Hostname of the principal  
record.message | security_result.description | Description of the security result  
record.proxy.wafRule | security_result.rule_name | Name of the rule that triggered the security result  
record.level | security_result.severity | Severity of the security result  
record.proxy.wafRule | security_result.threat_name | Name of the threat  
record.proxy.clientIp | target.asset.ip | IP address of the asset  
record.projectId | target.cloud.project.id | ID of the cloud project  
record.projectName | target.cloud.project.name | Name of the cloud project  
record.proxy.path | target.file.full_path | Full path of the file  
record.proxy.clientIp | target.ip | IP address of the target  
record.executionRegion | target.location.name | Name of the location  
record.proxy.vercelId | target.user.userid | User ID of the target user  
| metadata.product_name | Product name  
| metadata.vendor_name | Vendor name  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fivetran/
title: Collect Fivetran logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:34.065939+00:00
---

# Collect Fivetran logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fivetran/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fivetran logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure Fivetran to push logs to Google Security Operations using webhooks.

Fivetran is a data integration platform that automates data pipelines from various sources to data warehouses. Fivetran generates operational events including connector sync events, transformation events, and connection status changes. These events can be sent to external endpoints via outbound webhooks for monitoring, alerting, and security analysis.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Fivetran account with admin or account-level permissions.
  * Access to the Google Cloud Console (for API key creation).
  * Fivetran account with [REST API access](https://fivetran.com/docs/rest-api/webhooks) enabled.



## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **\+ Add New**.
  3. Select **Configure a single feed**.
  4. In the **Feed name** field, enter a name (for example, `Fivetran Events`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Fivetran** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Leave empty.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.
  10. Review your new feed configuration and click **Submit**.



### Generate and save secret key

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. **Copy and save** the secret key securely.

**Important:** The secret key is displayed only once. If you lose it, you must generate a new one.

### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. Save this URL for the next steps.
  4. Click **Done**.



## Create Google Cloud API key

Google SecOps requires an API key for authentication.

### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project.
  3. Click **Create credentials** > **API key**.
  4. Click **Edit API key** to restrict the key.



### Restrict the API key

  1. In the **API key** settings: 
     * **Name** : Enter a descriptive name (for example, `SecOps Webhook API Key`).
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the dropdown, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. **Copy** the API key value and save it securely.



## Configure Fivetran webhook

### Construct the webhook URL

  * Combine the endpoint URL and API key:
        
        <ENDPOINT_URL>?key=<API_KEY>
        




### Create webhook using Fivetran REST API

#### Get Fivetran API credentials

  1. Sign in to your [Fivetran account](https://fivetran.com/dashboard).
  2. Go to **Account Settings** > **API Config**.
  3. Click **Generate API Key** if you don't have one.
  4. Copy the **API Key** and **API Secret**.



#### Create account-level webhook

Use this method to receive events from all connectors in your account.

  1. Open a terminal and run the following command:
         
         curl -X POST https://api.fivetran.com/v1/webhooks/account \
                 -u "API_KEY:API_SECRET" \
                 -H "Content-Type: application/json" \
                 -H "Accept: application/json" \
                 -d '{
                         "url": "https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=YOUR_CHRONICLE_API_KEY",
                         "events": [
                                 "sync_start",
                                 "sync_end",
                                 "transformation_start",
                                 "transformation_succeeded",
                                 "transformation_failed",
                                 "connection_successful",
                                 "connection_failure",
                                 "create_connector",
                                 "pause_connector",
                                 "resume_connector",
                                 "edit_connector",
                                 "delete_connector",
                                 "force_update_connector",
                                 "resync_connector",
                                 "resync_table"
                         ],
                         "active": true,
                         "secret": "YOUR_CHRONICLE_SECRET_KEY"
                 }'
         

     * Where `{region}` is the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`), and `{parent}` is the resource path in the format `projects/<PROJECT_ID>/locations/<LOCATION>/instances/<INSTANCE_ID>/logTypes/<LOG_TYPE>`.



## Webhook details

### Available webhook events

Event | Description  
---|---  
`sync_start` | Connector sync started  
`sync_end` | Connector sync completed  
`transformation_start` | Transformation started  
`transformation_succeeded` | Transformation completed successfully  
`transformation_failed` | Transformation failed  
`connection_successful` | Connection test succeeded  
`connection_failure` | Connection test failed  
`create_connector` | New connector created  
  
### Webhook retry behavior

Fivetran automatically retries failed webhooks for up to **24 hours** with the following schedule:

Retry | Time After Initial Attempt  
---|---  
1st retry | 6 minutes  
2nd retry | 27 minutes  
3rd retry | 1 hour 45 minutes  
4th retry | 6 hours 25 minutes  
5th retry | 23 hours 13 minutes  
**Note:** Webhooks are automatically deactivated after 3 days of consistent failures.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`jsonPayload.connector_id` | `additional.connector_id` | Value copied directly.  
`jsonPayload.connector_type` | `additional.connector_type` | Value copied directly.  
`jsonPayload.data.query` | `additional.query` | Value copied directly.  
N/A | `metadata.event_type` | Set based on presence of principal and target.  
`jsonPayload.event` | `metadata.product_event_type` | Value copied directly.  
`jsonPayload.sync_id` | `metadata.product_log_id` | Value copied directly.  
`jsonPayload.connector_name` | `principal.hostname` | Value copied directly.  
`resource.labels.email_id` | `principal.user.email_addresses` | Mapped if format is valid email.  
`resource.labels.unique_id` | `principal.user.userid` | Value copied directly.  
`severity` | `security_result.severity` | "INFO" maps to **INFORMATIONAL**.  
`logName` | `target.resource.name` | Value copied directly.  
N/A | `target.resource.type` | Set to **DATABASE**.  
N/A | `metadata.product_name` | Set to **FIVETRAN**.  
N/A | `metadata.vendor_name` | Set to **FIVETRAN**.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fivetran-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 

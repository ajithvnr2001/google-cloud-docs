---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-openpages/
title: Collect IBM OpenPages logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:56:30.700214+00:00
---

# Collect IBM OpenPages logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-openpages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect IBM OpenPages logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure IBM OpenPages to push logs to Google Security Operations using webhooks.

IBM OpenPages is an AI-driven governance, risk, and compliance (GRC) platform that provides a centralized solution for managing risk, regulatory compliance, internal audit, IT governance, and policy management. OpenPages supports webhooks (version 9.1.2 and later) that send real-time event notifications when GRC objects are created, updated, deleted, associated, or disassociated.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * IBM OpenPages supports webhook or HTTP POST for log delivery
  * Access to Google Cloud Console (for API key creation)
  * IBM OpenPages version 9.1.2 or later with administrator access
  * For on-premises and Cloud Pak for Data deployments, RabbitMQ installed and configured with the OpenPages connection to RabbitMQ set up
  * For SaaS deployments, the Google SecOps webhook endpoint domain must be on the approved allowlist



## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `IBM OpenPages Events`).
  5. Select **Webhook** as the **Source type**.
  6. Select **IBM OpenPages** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Enter `\n` to split multi-line events
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



### Generate and save secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. **Copy and save** the secret key securely.

**Important:** The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.

### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is:
         
         https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate
         

or
         
         https://<REGION>-malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate
         

  4. Save this URL for the next steps.

  5. Click **Done**.




## Create Google Cloud API key

Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud Console.

### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Google SecOps instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps Webhook API Key`)
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Google SecOps API, reducing security risk if the key is compromised.

## Configure IBM OpenPages webhook

### Construct the webhook URL

  * Combine the Chronicle endpoint URL and API key:
        
        <ENDPOINT_URL>?key=<API_KEY>
        

**Example** :
        
        https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...
        




### Create webhook in IBM OpenPages

  1. Sign in to the **IBM OpenPages** administration console as an administrator.
  2. Go to **Administration > Integrations > Webhooks**.
  3. Click **Create Webhook**.
  4. Provide the following configuration details:

     * **Endpoint URL** : Paste the complete endpoint URL with API key from above (for example, `https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...`).

**Note:** The endpoint must accept POST requests over HTTPS. Each webhook must use a unique endpoint URL—duplicates are not allowed.
     * **Authentication Method** : Select **Bearer Token**.

     * **Bearer Token** : Paste the secret key generated from the Google SecOps feed creation step.

**Note:** IBM OpenPages supports the following authentication methods for webhooks: **Basic Auth** (username/password), **Bearer Token** , **API Key** (custom header and token prefix), and **OAuth 2.0** (IBM IAM API keys only). For Google SecOps integration, use **Bearer Token** with the Google SecOps secret key, or use **API Key** with the header name `x-chronicle-auth` and the secret key as the token value.
  5. In the **Event Subscriptions** section, select the object types and events to monitor:

     * **Object Types** : Select the GRC object types to monitor (for example, `SOXRisk`, `SOXIssue`, `SOXBusEntity`, `SOXControl`, `SOXProcess`, `SOXTask`).
     * **Event Types** : Select the events to send to Google SecOps: 
       * **create** — published when an object of a subscribed type is created
       * **update** — published when an object of a subscribed type is updated (includes which fields changed)
       * **delete** — published when an object of a subscribed type is deleted
       * **associate** — published when an object is associated with a parent object
       * **disassociate** — published when an object is removed from a parent object



### Test and enable the webhook

**For SaaS deployments:**

  1. Enable the webhook first by toggling the **Enabled** switch to **On**.
  2. Wait approximately 1-2 minutes for the egress connection to open.
  3. Click **Test Connection** to verify the endpoint is reachable.
  4. Verify the test returns a successful response.



**For on-premises deployments:**

  1. Click **Test Connection** to verify the endpoint is reachable.
  2. Verify the test returns a successful response.
  3. Enable the webhook by toggling the **Enabled** switch to **On**.
  4. Wait approximately 5 minutes for the events broker to pick up the configuration.

**Note:** Once the webhook is enabled, wait 5 minutes for the events broker to pick up the configuration. After that, any event matching the subscription will be dispatched to the endpoint. Events in the queue have a default time to live (TTL) of 1 day, after which they are automatically removed.

### Webhook payload format

  * IBM OpenPages sends webhook events as JSON payloads via HTTP POST. The following is an example of a webhook payload for a risk object update:
        
        {
            "action": "update",
            "type": "GRC_OBJECT",
            "objectType": "SOXRisk",
            "message": {
                "event": "update",
                "publishedDate": "2025-09-25 02:14:26.797Z",
                "details": {
                    "object_id": "9032",
                    "object_name": "RB-01-Risk00190",
                    "object_path": "/_op_sox/Project/Default/ICDocumentation/Risks/Global Financial Services/North America/Retail Banking/RB-01-Risk00190.txt",
                    "updated_fields": [
                        "OPSS-Risk-Qual:Inherent Likelihood",
                        "OPSS-Risk-Qual:Inherent Risk Rating",
                        "OPSS-Risk-Quant:Inherent Frequency",
                        "OPSS-Risk-Quant:Inherent Risk Exposure"
                    ],
                    "last_modification": "2025-08-30 08:58:48.000Z"
                },
                "actor": {
                    "iam_id": "user1@ibm.com",
                    "user_id": "2087",
                    "user_name": "user1"
                }
            },
            "version": "9.1.2"
        }
        




### Webhook system constraints

Constraint | Value  
---|---  
**Maximum enabled webhooks** | 50 (default), configurable up to 100 via `/Platform/Messaging/Webhooks Limit` registry setting  
**Unique endpoint URL** | Each webhook must use a unique endpoint URL  
**Event TTL in queue** | 1 day (events not dispatched within this period are removed)  
**Broker pickup delay** | 5 minutes after enabling a webhook  
  
## Authentication methods reference

Google SecOps webhook feeds support multiple authentication methods. Choose the method that your vendor supports.

### Method 1: Custom headers (Recommended)

If your vendor supports custom HTTP headers, use this method for better security.

  * **Request format:**
        
        POST <ENDPOINT_URL> HTTP/1.1
        Content-Type: application/json
        x-goog-chronicle-auth: <API_KEY>
        x-chronicle-auth: <SECRET_KEY>
        
        {
                "event": "data",
                "timestamp": "2025-01-15T10:30:00Z"
        }
        




**Advantages:**

  * API key and secret not visible in URL
  * More secure (headers not logged in web server access logs)
  * Preferred method when vendor supports it



### Method 2: Query parameters

If your vendor does not support custom headers, append credentials to the URL.

  * **URL format:**
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

  * **Example:**
        
        https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...&secret=abcd1234...
        

  * **Request format:**
        
        POST <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY> HTTP/1.1
        Content-Type: application/json
        
        {
                "event": "data",
                "timestamp": "2025-01-15T10:30:00Z"
        }
        




**Disadvantages:**

  * Credentials visible in URL
  * May be logged in web server access logs
  * Less secure than headers



### Method 3: Hybrid (URL + Header)

Some configurations use API key in URL and secret key in header.

  * **Request format:**
        
        POST <ENDPOINT_URL>?key=<API_KEY> HTTP/1.1
        Content-Type: application/json
        x-chronicle-auth: <SECRET_KEY>
        
        {
                "event": "data",
                "timestamp": "2025-01-15T10:30:00Z"
        }
        




### Authentication header names

Google SecOps accepts the following header names for authentication:

**For API key:**

  * `x-goog-chronicle-auth` (recommended)
  * `X-Goog-Chronicle-Auth` (case-insensitive)



**For secret key:**

  * `x-chronicle-auth` (recommended)
  * `X-Chronicle-Auth` (case-insensitive)



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
column5 | metadata.description | Description of the event  
has_principal_user | metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
column1 | metadata.product_event_type | Product-specific event type  
metadata.product_name | metadata.product_name | Product name  
metadata.vendor_name | metadata.vendor_name | Vendor/company name  
column6 | principal.user.userid | User ID of the principal  
is_successful | security_result.action | Action taken  
is_successful | security_result.action_details | Details of the action  
column4 | security_result.detection_fields | Additional detection fields  
column5 | security_result.detection_fields |   
counter | security_result.detection_fields |   
column4 | security_result.description | Description of the security result  
column2 | security_result.summary | Summary of the security result  
column4 | target.user.attribute.roles | Roles associated with the target user  
column4 | target.user.userid | User ID of the target  
`target_user` | `target.user.userid` | Mapped from changelog  
`IBM_OPENPAGES` | `metadata.vendor_name` | Mapped from changelog  
`IBM_OPENPAGES` | `metadata.product_name` | Mapped from changelog  
`OpenPages` | `metadata.product_name` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-openpages-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

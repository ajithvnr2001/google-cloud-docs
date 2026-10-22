---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ionix/
title: Collect IONIX Attack Surface Management logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:04.004269+00:00
---

# Collect IONIX Attack Surface Management logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ionix/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect IONIX Attack Surface Management logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure IONIX Attack Surface Management to push logs to Google Security Operations using webhooks.

IONIX is an External Attack Surface Management (EASM) platform that discovers, assesses, and validates security exposures across your organization's internet-facing assets and digital supply chain. IONIX provides action items for DNS findings, PKI issues, cloud exposures, and vulnerabilities, delivering prioritized remediation workflows.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * IONIX Attack Surface Management supports HTTP POST push for log delivery
  * Access to Google Cloud Console (for API key creation)
  * An active IONIX portal account with administrator access to **Settings > Integrations**



## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `IONIX ASM Logs`).
  5. Select **Webhook** as the **Source type**.
  6. Select **IONIX** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Enter a delimiter to split multi-line events. Common values: 
       * `\n` \- Newline delimiter (most common for NDJSON)
       * Leave empty if each request contains a single event
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
         
         https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import
         

Where `{region}` is the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`), and `{parent}` is the resource path in the format `projects/<PROJECT_ID>/locations/<LOCATION>/instances/<INSTANCE_ID>/logTypes/<LOG_TYPE>`.

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

## Configure IONIX Attack Surface Management webhook

IONIX natively supports pushing security event data to external endpoints via HTTP POST using its integration framework. The integration is configured in the IONIX portal and uses the same mechanism as the Splunk HEC integration, adapted to push data to the Google SecOps webhook endpoint.

### Construct the webhook URL

  * Combine the Google SecOps endpoint URL and API key into a single URL:
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

    * **Example:**
          
          https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...
          




### Configure the integration in the IONIX portal

  1. Sign in to your **IONIX portal** (for example, `https://<your-portal-name>.ionix.com`).
  2. Navigate to **Settings > Integrations**.
  3. Click the **Splunk Integration > Settings**.
  4. Provide the following configuration details:

     * **HEC Token** : Enter the secret key generated from the Google SecOps webhook feed.
     * **Splunk Server** : Enter the full Google SecOps webhook endpoint URL with the API key appended as a query parameter. Use the following format:
           
           https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=<API_KEY>
           

**Note:** IONIX's Splunk integration sends data via HTTP POST to the configured server URL. By providing the Google SecOps webhook endpoint URL in the **Splunk Server** field, IONIX will push JSON event data directly to Google SecOps.
  5. Configure the **push interval** to set how frequently IONIX sends data to the endpoint (for example, every 60 minutes).

  6. Fill out any additional data fields relevant to your environment.

  7. Click **Save**.

  8. Turn on the integration by toggling the integration switch to **Enabled**.

  9. Data will begin appearing in Google SecOps within one push interval cycle. Initial data delivery may take up to one hour.




### Alternative: Use the IONIX REST API with a custom script

If the native Splunk HEC integration does not meet your requirements, you can use the IONIX REST API to pull data and forward it to Google SecOps.

#### Generate an IONIX API key

  1. Sign in to the **IONIX portal**.
  2. Click **API Settings**.
  3. Provide a **name** for the token.
  4. Select the token type: 
     * **Read-only** (recommended for data collection)
     * **Read-write**
  5. Set an **expiry date** for the token.
  6. Click **Create Token**.
  7. Copy the generated token and save it securely.



#### IONIX API endpoints

Use the following API endpoints to retrieve security data from IONIX:

Endpoint | Description  
---|---  
`/api/v1/remediation/action-items/open/` | Open action items (domains, root endpoint)  
`/api/v1/remediation/action-items/all/detailed` | All action items with detailed information  
`/api/v1/discovery/org-assets/export-discovery-evidence` | Asset risk and discovery evidence  
`/api/v1/discovery/org-assets` | Organization assets (includes first_seen date)  
`/api/v1/tests` | Security test results  
  
  * **Example API request**
        
        curl -X GET "https://api.portal.ionix.io/api/v1/remediation/action-items/all/detailed" \
            -H "Authorization: Token <IONIX_API_KEY>" \
            -H "Content-Type: application/json"
        




#### Forward data to Google SecOps

  * After retrieving data from the IONIX API, forward it to the Google SecOps webhook endpoint:
        
        curl -X POST "<ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>" \
            -H "Content-Type: application/json" \
            -d @ionix_events.json
        




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
    
    https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...
    

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

  * **For API key:**

    * `x-goog-chronicle-auth` (recommended)
    * `X-Goog-Chronicle-Auth` (case-insensitive)
  * **For secret key:**

    * `x-chronicle-auth` (recommended)
    * `X-Chronicle-Auth` (case-insensitive)



## UDM mapping table

For information about how IONIX log fields are mapped to Google Security Operations Unified Data Model (UDM) fields, search for the `IONIX` log type in the [supported default parsers](https://docs.cloud.google.com/chronicle/docs/reference/default-parsers) reference.

## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ionix-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

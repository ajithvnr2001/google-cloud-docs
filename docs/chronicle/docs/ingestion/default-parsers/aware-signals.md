---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aware-signals/
title: Collect Aware Signals logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:03.104319+00:00
---

# Collect Aware Signals logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aware-signals/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Aware Signals logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure Aware to push Signal event logs to Google Security Operations using webhooks.

Aware (by Mimecast) is a collaboration security and insider risk platform that monitors content across enterprise communication tools such as Slack, Microsoft Teams, Zoom, Cisco Webex, and Workvivo. The Aware Signal application uses AI models, keyword matching, regular expressions, and sentiment analysis to detect policy violations and generate events. These Signal events can be forwarded to a SIEM destination for centralized security monitoring and correlation.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * An Aware platform subscription with the Signal module enabled
  * An Aware administrator account with access to **System Settings**
  * At least one collaboration platform (Slack, Microsoft Teams, Zoom, Webex, or Workvivo) connected and ingesting content in Aware
  * At least one Signal policy and rule configured to generate events
  * Access to Google Cloud Console (for API key creation)



## Create a webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Aware Signal Events`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Aware Signals** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** : Enter `\n` (newline delimiter for NDJSON payloads)
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



### Generate and save the secret key

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




## Create a Google Cloud API key

Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud Console.

### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Google SecOps instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Chronicle Webhook API Key`)
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Google SecOps API, reducing security risk if the key is compromised.



## Obtain the Aware API key

Aware uses an API key for authenticating external integrations. To obtain the key:

  1. Sign in to **Aware** at <https://aware.work> with an administrator account.
  2. Click **System Settings** in the lower left corner.
  3. Navigate to the **Integrations** tab.
  4. Copy the **API Key** displayed on the page.

**Note:** All Aware API methods are protected by a customer-specific access token provided through the HTTP `X-Aware-Api-Key` header. Only Aware administrators can access the API key from System Settings.
  5. Save the API key securely for use in the next steps.




## Configure Aware Signal webhook forwarding

### Construct the webhook URL

  * Combine the Google SecOps endpoint URL, API key, and secret key:
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

  * **Example:**
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...
        




### Configure event forwarding in Aware

Configure Aware to forward Signal events to the Google SecOps webhook endpoint. The exact steps may vary depending on your Aware platform version.

  1. Sign in to **Aware** at <https://aware.work> with an administrator account.
  2. Click **System Settings** in the lower left corner.
  3. Navigate to the **Integrations** tab.
  4. Configure a new webhook destination with the following details:

     * **Destination URL** : Paste the complete webhook URL with API key and secret key appended as query parameters:
           
           https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=YOUR_API_KEY&secret=YOUR_SECRET_KEY
           

     * **Content Type** : Select `application/json`

     * **Authentication Header** (if supported by your Aware version): Set the header name to `X-Aware-Api-Key` and the value to your Aware API key

  5. Select the event types to forward. For comprehensive security monitoring, enable forwarding of all Signal events:

     * Policy violation events
     * Keyword match events
     * AI/sentiment detection events
     * Toxic behavior detection events
  6. Click **Save** to activate the webhook destination.

**Note:** If webhook-based event forwarding is not available in your Aware platform version, contact your Mimecast account representative to request the feature or explore the alternative approach described in the next section. For more information, see [Aware documentation](https://mimecastsupport.zendesk.com/hc/en-us/sections/34917949065875-Aware).



### Alternative: Forward events using a Cloud Run function

If your Aware version does not support native webhook push for Signal events, you can use a Cloud Run function to poll the Aware API and forward events to the Google SecOps webhook endpoint.

  1. Create a **Cloud Run function** (Python 3.12 or later) with a Pub/Sub trigger.
  2. Configure the function to: 
     1. Authenticate to the Aware API using the `X-Aware-Api-Key` header.
     2. Query Signal events from the Aware API endpoint.
     3. Forward each event as a JSON payload to the Google SecOps webhook endpoint URL.
  3. Use **Cloud Scheduler** to invoke the function at regular intervals (for example, every 5 minutes).

     * **Example request to forward events:**
           
           curl -X POST "https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=YOUR_API_KEY&secret=YOUR_SECRET_KEY" \
             -H "Content-Type: application/json" \
             -d '{"signal_id":"12345","event_type":"policy_violation","timestamp":"2026-01-15T10:30:00Z","user":"user@example.com","platform":"slack","policy":"Data Loss Prevention","rule":"Credit Card Numbers","message_snippet":"detected content"}'
           

**Note:** Contact Aware support for the current API endpoint documentation and available query parameters for retrieving Signal events programmatically. All API methods are subject to rate limits.



### Verify event delivery

  1. In Google SecOps, go to **SIEM Settings > Feeds**.
  2. Click on the **Aware Signal Events** feed.
  3. Go to the **Status** tab.
  4. Verify that events are being received.
  5. Alternatively, trigger a test Signal event in Aware:

     1. In **Aware** , navigate to **Signal > Events**.
     2. Verify that new events are being generated by your policies.
     3. Wait a few minutes for the events to appear in Google SecOps.
**Note:** Events may take a few minutes to appear depending on the delivery method and event volume.



## Aware Signal event types

Aware Signal detects events across connected collaboration platforms using a combination of AI models, keyword matching, regular expressions, and sentiment analysis. The following event categories are commonly generated:

Category | Description | Examples  
---|---|---  
Policy violation | Events triggered by defined policy rules | Keyword detection, regex pattern match, sensitive data  
AI/Sentiment | Events detected by AI and sentiment models | Toxic language, negative sentiment, harassment  
Data loss | Events related to potential data exfiltration | File sharing violations, external sharing, credential exposure  
Insider risk | Events indicating potential insider threats | Unusual behavior patterns, access anomalies, departing employee risk  
Compliance | Events related to regulatory compliance | PII exposure, financial data sharing, HIPAA violations  
  
## Authentication methods reference

Google SecOps webhook feeds support multiple authentication methods. Choose the method that your vendor supports.

### Method 1: Query parameters

Append credentials to the webhook URL.

  * **URL format:**
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

  * **Example:**
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...
        




### Method 2: Custom headers

If your configuration supports custom HTTP headers, use this method for improved security.

  * **Headers:**
        
        x-goog-chronicle-auth: <API_KEY>
        x-chronicle-auth: <SECRET_KEY>
        




**Advantages:**

  * API key and secret not visible in URL
  * More secure (headers not logged in web server access logs)



## Webhook limits and best practices

### Request limits

Limit | Value  
---|---  
**Max request size** | 4 MB  
**Max QPS (queries per second)** | 15,000  
**Request timeout** | 30 seconds  
**Retry behavior** | Automatic with exponential backoff  
  
### Best practices

  * Enable forwarding for all Signal event types to ensure comprehensive security coverage
  * Monitor the webhook delivery status regularly for failures or delays
  * Use the `\n` split delimiter in the Google SecOps feed configuration to handle NDJSON payloads
  * Test the integration with a known policy violation before deploying to production
  * Review Aware Signal policies periodically to ensure relevant events are being captured



## Troubleshooting

### Events not appearing in Google SecOps

**Cause:** Events are being generated in Aware but not ingested

**Solution:**

  1. Go to **SIEM Settings > Feeds** in Google SecOps.
  2. Click on your Aware Signal Events feed.
  3. Go to the **Status** tab.
  4. Check for ingestion errors.
  5. Verify the log type is set to **Aware Signals**.
  6. Verify the API key and secret key in the webhook URL are correct.



### Authentication errors

**Cause:** Invalid API key or secret key

**Solution:**

  1. Verify the Google SecOps API key is valid and has the correct API restriction.
  2. Verify the secret key matches the one generated during feed creation.
  3. Test the endpoint manually:
         
         curl -X POST "https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=YOUR_API_KEY&secret=YOUR_SECRET_KEY" \
             -H "Content-Type: application/json" \
             -d '{"test": "event"}'
         

  4. If the test fails, regenerate the API key or secret key and update the webhook configuration in Aware.




### Payload exceeds maximum size

**Cause:** Event payloads exceed the 4 MB limit

**Solution:**

  1. Reduce the number of event types being forwarded.
  2. Contact Aware support to configure payload size limits.
  3. If using the Cloud Run function approach, implement batching to split large payloads into multiple requests.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`signalEventDetails.eventStatus` | `security_result.action_details` | Directly mapped  
`contentObjectDetails_contentObjectIsChat_label` | `security_result.detection_fields` | Merged  
`contentObjectDetails_contentObjectIsThread_label` | `security_result.detection_fields` | Merged  
`detectionLength_label` | `security_result.detection_fields` | Merged  
`detectionStart_label` | `security_result.detection_fields` | Merged  
`ruleConditionMatches_label` | `security_result.detection_fields` | Merged  
`search_label` | `security_result.detection_fields` | Merged  
`signalEventDetails_createdTime_label` | `security_result.detection_fields` | Merged  
`signalEventDetails_deletedTime_label` | `security_result.detection_fields` | Merged  
`signalEventDetails_inspectionRequestId_label` | `security_result.detection_fields` | Merged  
`signalEventDetails_isQuarantined_label` | `security_result.detection_fields` | Merged  
`signalEventDetails_policyDetails_createdTime_label` | `security_result.detection_fields` | Merged  
`signalEventDetails_policyDetails_policyId_label` | `security_result.detection_fields` | Merged  
`signalEventDetails_policyDetails_policyName_label` | `security_result.detection_fields` | Merged  
`signalEventDetails_ruleBehavior_label` | `security_result.detection_fields` | Merged  
`signalEventDetails_ruleFamilyId_label` | `security_result.detection_fields` | Merged  
`signalEventDetails_tenantId_label` | `security_result.detection_fields` | Merged  
`signalEventId_label` | `security_result.detection_fields` | Merged  
`signal_EventDetails_policyDetails_deletedTime_label` | `security_result.detection_fields` | Merged  
`snippetContent_label` | `security_result.detection_fields` | Merged  
`snippetLength_label` | `security_result.detection_fields` | Merged  
`snippetStart_label` | `security_result.detection_fields` | Merged  
`signalEventDetails_ruleId` | `security_result.rule_id` | Directly mapped  
`signalEventDetails_ruleName` | `security_result.rule_name` | Directly mapped  
`contentGroupDetails.contentGroupScope_label` | `target.group.attribute.labels` | Merged  
`contentObjectDetails_contentGroupDetails_contentGroupTag_label` | `target.group.attribute.labels` | Merged  
`contentGroupDetails_contentGroupName` | `target.group.group_display_name` | Directly mapped  
`contentObjectDetails_contentPlatformId_label` | `target.resource.attribute.labels` | Merged  
`contentObjectDetails_contentTime_label` | `target.resource.attribute.labels` | Merged  
`contentObjectDetails_contentObjectId` | `target.resource.product_object_id` | Directly mapped  
`contentObjectDetails_contentObjectType` | `target.resource.resource_subtype` | Directly mapped  
`contentAuthorDetails_contentAuthorEmail` | `target.user.email_addresses` | Merged  
`contentAuthorDetails_contentAuthorName` | `target.user.user_display_name` | Directly mapped  
`contentAuthorDetails_contentAuthorId` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `NETWORK_CONNECTION`  
N/A | `metadata.product_name` | Constant: `AWARE SIGNALS`  
N/A | `metadata.vendor_name` | Constant: `AWARE SIGNALS`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aware-signals-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 

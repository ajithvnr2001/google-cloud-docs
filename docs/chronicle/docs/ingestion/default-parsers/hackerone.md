---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hackerone/
title: Collect HackerOne logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:23.626853+00:00
---

# Collect HackerOne logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hackerone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect HackerOne logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure HackerOne to push logs to Google Security Operations using webhooks.

HackerOne is a vulnerability coordination and bug bounty platform that connects organizations with security researchers to identify and remediate security vulnerabilities. The platform provides bug bounty programs, vulnerability disclosure programs, pentesting, and continuous security testing across the software development lifecycle.

## Before you begin

  * Ensure that you have the following prerequisites:

  * A Google SecOps instance

  * HackerOne program with Professional or Enterprise tier (webhooks are only available for these tiers)

  * Administrative access to your HackerOne program settings

  * Access to Google Cloud Console (for API key creation)




## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `HackerOne Webhook`).
  5. Select **Webhook** as the **Source type**.
  6. Select **HackerOne** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** : Leave empty. Each webhook request contains a single JSON event.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



### Generate and save secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. **Copy and save** the secret key securely.



**Important** : The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.

### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is:
         
         https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import
         

Where `{region}` is the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`), and `{parent}` is the resource path in the format `projects/<PROJECT_ID>/locations/<LOCATION>/instances/<INSTANCE_ID>/logTypes/<LOG_TYPE>`.

  4. Save this URL for the next steps.

  5. Click **Done**.




## Create Google Cloud API key

Chronicle requires an API key for authentication. Create a restricted API key in the Google Cloud Console.

### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Google SecOps instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Chronicle HackerOne Webhook API Key`).
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Chronicle API, reducing security risk if the key is compromised.



## Configure HackerOne webhook

### Construct the webhook URL

Combine the Google SecOps endpoint URL, API key, and secret key into a single URL. Both the API key and the secret key must be appended as query parameters.

**URL format:**
    
    
    ```none
    <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
    ```
    

**Example:**
    
    
    ```none
    https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...
    ```
    

Replace the following: \- `<ENDPOINT_URL>`: The feed endpoint URL from the **Get the feed endpoint URL** section. \- `<API_KEY>`: The Google Cloud API key from the **Create Google Cloud API key** section. \- `<SECRET_KEY>`: The secret key from the **Generate and save secret key** section.

**Important** : Do not put the Google SecOps secret key in HackerOne's **Secret** field. The HackerOne **Secret** field is used for HMAC payload signature validation (`X-H1-Signature` header), which is a separate mechanism from Google SecOps webhook authentication. Placing the Google SecOps secret in HackerOne's **Secret** field will result in a `403 Forbidden` error because HackerOne does not pass that value as a Google SecOps authentication credential. Instead, append both `key` and `secret` as query parameters in the **Payload URL**.

### Create webhook in HackerOne

  1. Sign in to [HackerOne](https://www.hackerone.com/) and navigate to your program.
  2. Go to **Engagements** , click the kebab menu for the program you want to configure, then click **Settings**.
  3. Go to **Automation > Webhooks**.
  4. Click **New webhook**.
  5. Provide the following configuration details: 
     * **Payload URL** : Paste the complete URL with API key and secret from above. For example, `https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...`.
     * **Secret** : Leave this field **blank**.
  6. Select which events you'd like to trigger the webhook. Choose one of the following: 
     * **Send me everything** : All events will trigger the webhook.
     * **Let me specify individual events** : Select the specific events you'd like to send to Google SecOps.
  7. Click **Add webhook**.

**Note:** HackerOne's **Secret** field generates an HMAC signature (`X-H1-Signature` header) for payload validation. This is separate from Google SecOps authentication. Leave this field blank to avoid authentication conflicts.



### Test the webhook

  1. In the webhook configuration page, click **Test request** to send an example request to the configured Payload URL.
  2. Verify the response is **HTTP 200**.
  3. Click your webhook to view details.
  4. Under the **Recent deliveries** section, verify recent deliveries show successful status (HTTP 200).
  5. Click any delivery to view the POST payload request.



If you receive an error: \- **HTTP 403** : Verify the API key and secret key are correctly appended as query parameters in the Payload URL. Confirm the HackerOne **Secret** field is blank. \- **HTTP 401** : Verify the API key is valid and restricted to the Google SecOps API. \- **HTTP 404** : Verify the endpoint URL is correct and includes the full path (`/v1/{parent}/logs:import`).

### Verify ingestion in Google SecOps

  1. Go to **SIEM Settings > Feeds** in Google SecOps.
  2. Locate your HackerOne webhook feed.
  3. Check the **Status** column (should be **Active**).
  4. Check **Events received** count (should be incrementing).
  5. Check **Last succeeded on** timestamp (should be recent).



## Webhook limits and best practices

### Request limits
    
    
    | Limit | Value |
    |-------|-------|
    | **Max request size** | 4 MB |
    | **Max QPS (queries per second)** | 15,000 |
    | **Request timeout** | 30 seconds |
    | **Retry behavior** | Automatic with exponential backoff |
    

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
attributes.cleared, attributes.rules_of_engagement_signed, attributes.identity_verified, attributes.background_checked, attributes.citizenship_verified, attributes.residency_verified, type, attributes.title, attributes.main_state, attributes.state, relationships.reporter.data.type, relationships.reporter.data.attributes.reputation, relationships.reporter.data.attributes.signal, relationships.reporter.data.attributes.impact, relationships.reporter.data.attributes.disabled, relationships.reporter.data.attributes.profile_picture.62x62, relationships.reporter.data.attributes.profile_picture.82x82, relationships.reporter.data.attributes.profile_picture.110x110, relationships.reporter.data.attributes.profile_picture.260x260, relationships.reporter.data.attributes.hackerone_triager, relationships.program.data.id, relationships.program.data.type, relationships.program.data.attributes.handle, relationships.severity.data.type, relationships.severity.data.attributes.rating, relationships.severity.data.attributes.author_type, relationships.severity.data.attributes.calculation_method, relationships.weakness.data.id, relationships.weakness.data.type, relationships.weakness.data.attributes.name, relationships.weakness.data.attributes.description, relationships.weakness.data.attributes.external_id, relationships.structured_scope.data.id, relationships.structured_scope.data.type, relationships.structured_scope.data.attributes.asset_type, relationships.structured_scope.data.attributes.eligible_for_bounty, relationships.structured_scope.data.attributes.eligible_for_submission, relationships.structured_scope.data.attributes.instruction, relationships.structured_scope.data.attributes.max_severity, relationships.structured_scope.data.attributes.confidentiality_requirement, relationships.structured_scope.data.attributes.integrity_requirement, relationships.structured_scope.data.attributes.availability_requirement, relationships.inboxes.data.id, relationships.inboxes.data.type, relationships.inboxes.data.attributes.name, relationships.inboxes.data.attributes.type | additional.fields | Merged as key-value labels  
timestamp | metadata.event_timestamp | Parsed using date filter with format yyyy-MM-dd'T'HH:mm:ss.SSSZ  
| metadata.event_type | Set to "STATUS_UPDATE" if has_principal true, "USER_UNCATEGORIZED" if has_principal_user_user true, else "GENERIC_EVENT"  
id | metadata.product_log_id | Value copied directly  
relationships.structured_scope.data.attributes.asset_identifier | principal.asset.asset_id | Prefixed with "ASSET:"  
attributes.email_alias | principal.user.email_addresses | Merged  
relationships.reporter.data.id | principal.user.employee_id | Value copied directly  
relationships.reporter.data.attributes.name | principal.user.first_name | Value copied directly  
attributes.username, relationships.reporter.data.attributes.username | principal.user.user_display_name | Value from relationships.reporter.data.attributes.username if not empty, else attributes.username  
relationships.severity.data.attributes.user_id | principal.user.userid | Value copied directly  
relationships.severity.data.id | security_result.rule_id | Value copied directly  
relationships.severity.data.attributes.max_severity | security_result.severity | Converted to uppercase  
attributes.vulnerability_information | security_result.summary | Value copied directly  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hackerone-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

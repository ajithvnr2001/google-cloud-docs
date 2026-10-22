---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gitguardian-enterprise/
title: Collect GitGuardian Enterprise logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:25.896748+00:00
---

# Collect GitGuardian Enterprise logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gitguardian-enterprise/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect GitGuardian Enterprise logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure GitGuardian Enterprise to push logs into Google Security Operations using webhooks.

GitGuardian Enterprise is a secrets detection and remediation platform that monitors source code repositories, CI/CD pipelines, and developer workstations for exposed credentials and sensitive data. It provides real-time alerts when secrets are detected, and helps security teams manage incident remediation workflows.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * GitGuardian Enterprise workspace with Manager access level
  * Access to Google Cloud Console (for API key creation)
  * GitGuardian Business plan or higher (for custom webhook support)



## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `GitGuardian Enterprise Incidents`).
  5. Select **Webhook** as the **Source type**.
  6. Select **GitGuardian Enterprise** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Split delimiter** (optional): Leave empty (each webhook request contains a single event)
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

     * **Name** : Enter a descriptive name (for example, `Google SecOps GitGuardian Webhook API Key`)
  2. Under **API restrictions** :

     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.

  4. **Copy** the API key value from the **API key** field at the top of the page.

  5. Save the API key securely.

**Note:** Restricting the API key ensures that it can only be used with the Chronicle API, reducing security risk if the key is compromised.



## Configure GitGuardian Enterprise webhook

### Construct the webhook URL

  * Combine the Google SecOps endpoint URL and API key:
        
        <ENDPOINT_URL>?key=<API_KEY>
        

**Example:**
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...
        




### Create custom webhook in GitGuardian

#### For personal workspace:

  1. Sign in to the **GitGuardian dashboard**.
  2. Go to **Settings > Workspace > Integrations > Destinations > Custom webhook**.
  3. Click **Add a custom webhook** or **Create new custom webhook**.
  4. Provide the following configuration details:

     * **Name** : Enter a descriptive name (for example, `Google SecOps SIEM Integration`).
     * **URL** : Paste the complete endpoint URL with API key from above.
     * **Signature token** : Paste the secret key from Google SecOps feed creation.
     * **Custom header** (optional): Leave empty unless you need to specify environment or service tags.
  5. In the **Event Subscription** section, select the events you want to send to Google SecOps:

     * **Incidents** : 
       * ☑ **New incident detected**
       * ☑ **New occurrence detected**
       * ☑ **Incident resolved**
       * ☑ **Incident ignored**
       * ☑ **Incident reopened**
       * ☑ **Incident regression**
       * ☑ **Incident assigned**
       * ☑ **Incident reassigned**
       * ☑ **Incident unassigned**
       * ☑ **Incident Severity changed**
       * ☑ **Incident Validity changed**
       * ☑ **Incident access granted**
       * ☑ **Incident access revoked**
       * ☑ **Incident shared publicly**
       * ☑ **Incident unshared publicly**
       * ☑ **Feedback submitted**
       * ☑ **New comment on an incident**
  6. Click **Create** or **Save**.

  7. GitGuardian sends a test message to verify that the webhook is operational.




#### For business workspace:

  1. Sign in to the **GitGuardian dashboard**.
  2. Determine the scope for your webhook:

     * For **all incidents** in the workspace: Navigate to the **All-incidents team**.
     * For **specific team incidents** : Navigate to the desired team.
  3. Go to **Settings > Workspace > Integrations > Destinations > Custom webhook**.

     * Alternatively, from the team page, go to **Integrations > Custom webhook**.
  4. Click **Add a custom webhook** or **Create new custom webhook**.

  5. Provide the following configuration details:

     * **Name** : Enter a descriptive name (for example, `Google SecOps SIEM Integration`).
     * **URL** : Paste the complete endpoint URL with API key from above.
     * **Signature token** : Paste the secret key from Google SecOps feed creation.
     * **Custom header** (optional): Leave empty unless you need to specify environment or service tags.
  6. In the **Event Subscription** section, select the events you want to send to Google SecOps:

     * **Incidents** : 
       * ☑ **New incident detected**
       * ☑ **New occurrence detected**
       * ☑ **Incident resolved**
       * ☑ **Incident ignored**
       * ☑ **Incident reopened**
       * ☑ **Incident regression**
       * ☑ **Incident assigned**
       * ☑ **Incident reassigned**
       * ☑ **Incident unassigned**
       * ☑ **Incident Severity changed**
       * ☑ **Incident Validity changed**
       * ☑ **Incident access granted**
       * ☑ **Incident access revoked**
       * ☑ **Incident shared publicly**
       * ☑ **Incident unshared publicly**
       * ☑ **Feedback submitted**
       * ☑ **New comment on an incident**
  7. Click **Create** or **Save**.

  8. GitGuardian sends a test message to verify that the webhook is operational.




### Verify webhook delivery

  1. In the GitGuardian dashboard, navigate to your custom webhook configuration.
  2. Click **Send test message** or **Test webhook**.
  3. GitGuardian sends a sample payload to Google SecOps.
  4. In the Google SecOps console, go to **SIEM Settings > Feeds**.
  5. Locate your GitGuardian feed and verify that the test event was received.
  6. Check that the **Feed Status** shows **Active** with recent ingestion timestamp.

**Note:** The test message contains sample data with censored secret values. Production webhooks will contain actual incident data.



## Authentication methods reference

Google SecOps webhook feeds support multiple authentication methods. Choose the method that your vendor supports.

### Method 1: Query parameters (Recommended for GitGuardian)

GitGuardian custom webhooks work best with credentials appended to the URL.

  * **URL format:**
        
        <ENDPOINT_URL>?key=<API_KEY>
        

**Example:**
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...
        

**GitGuardian webhook configuration:**

    * **URL** : Full endpoint URL with API key parameter
    * **Signature token** : Google SecOps secret key (for HMAC verification)
  * **Request format:**
        
        POST <ENDPOINT_URL>?key=<API_KEY> HTTP/1.1
        Content-Type: application/json
        Timestamp: 1234567890
        Gitguardian-Signature: sha256=abc123...
        
        {
            "source": "GitGuardian",
            "timestamp": "2025-01-15T10:30:00Z",
            "action": "incident_triggered",
            "incident": {...}
        }
        




### Method 2: Custom headers (Alternative)

If you prefer to keep credentials out of the URL, use custom headers.

  * **Request format:**
        
        POST <ENDPOINT_URL> HTTP/1.1
        Content-Type: application/json
        x-goog-chronicle-auth: <API_KEY>
        Timestamp: 1234567890
        Gitguardian-Signature: sha256=abc123...
        
        {
            "source": "GitGuardian",
            "timestamp": "2025-01-15T10:30:00Z",
            "action": "incident_triggered",
            "incident": {...}
        }
        

**Note:** GitGuardian custom webhooks do not support adding custom headers to outbound requests. Use the query parameter method instead.



## GitGuardian webhook signature verification

GitGuardian signs all webhook payloads using HMAC-SHA256 to ensure authenticity and prevent tampering.

### Signature headers

GitGuardian includes the following headers in webhook requests:

  * **Gitguardian-Signature** : HMAC-SHA256 signature in the format `sha256=<hex_digest>`
  * **Timestamp** : Unix timestamp when the request was sent
  * **X-GitGuardian-Signature** : Deprecated header (still supported for backward compatibility)



### Signature algorithm

  * The signature is computed as follows:
        
        HMAC-SHA256(key=timestamp + signature_token, message=payload)
        

Where:

    * **timestamp** : Value from the `Timestamp` header
    * **signature_token** : The secret key configured in GitGuardian webhook settings
    * **payload** : Raw JSON request body as UTF-8 string



### Verification example (Python)
    
    
    import hmac
    import hashlib
    
    def verify_signature(signature: str, timestamp: str, signature_token: str, payload: str) -> bool:
        if not signature.startswith("sha256="):
            return False
        
        signature = signature.split("sha256=")[-1]
        
        hmac_digest = hmac.new(
            key=bytes(timestamp + signature_token, "utf-8"),
            msg=bytes(payload, "utf-8"),
            digestmod=hashlib.sha256
        ).hexdigest()
        
        return hmac.compare_digest(signature, hmac_digest)
    

### Replay attack protection

  * The `Timestamp` header prevents replay attacks. If the current timestamp differs from the webhook timestamp by more than a few seconds (recommended: 300 seconds), reject the request.

**Note:** Google SecOps automatically handles webhook authentication. You do not need to implement signature verification when using Google SecOps webhook feeds.



## Event types and payload structure

GitGuardian sends different event types based on incident lifecycle changes.

### Incident events

Event Type | Action Value | Description  
---|---|---  
**New incident detected** | `incident_triggered` | A new secret incident has been detected  
**New occurrence detected** | `new_occurrence` | A new occurrence of an existing incident was found  
**Incident resolved** | `incident_resolved` | The incident has been marked as resolved  
**Incident ignored** | `incident_ignored` | The incident has been marked as ignored  
**Incident reopened** | `incident_reopened` | A previously closed incident has been reopened  
**Incident regression** | `incident_regression` | A new regression was found for this incident  
**Incident assigned** | `incident_assigned` | The incident has been assigned to a user  
**Incident reassigned** | `incident_reassigned` | The incident has been reassigned to a different user  
**Incident unassigned** | `incident_unassigned` | A user was unassigned from this incident  
**Severity changed** | `incident_severity_changed` | The severity level has been updated  
**Validity changed** | `incident_validity_changed` | The validity status has been updated  
**Access granted** | `incident_access_granted` | A user has been granted access to this incident  
**Access revoked** | `incident_access_revoked` | Access to this incident has been revoked for a user  
**Shared publicly** | `incident_shared_publicly` | A public sharing link has been generated  
**Unshared publicly** | `incident_unshared_publicly` | The public sharing link has been deactivated  
**Feedback submitted** | `issue_feedback_received` | Feedback has been submitted for this incident  
**New comment** | `incident_note_created` | A new note has been created for this incident  
  
### Sample payload structure

  * All webhook payloads follow this structure:
        
        {
            "source": "GitGuardian",
            "timestamp": "2025-01-15T10:30:00.123456Z",
            "action": "incident_triggered",
            "message": "A new incident has been detected.",
            "target_user": "john.doe@example.com",
            "target_team": "Security Team",
            "custom_webhook_name": "Google SecOps SIEM Integration",
            "incident": {
                "id": 12345,
                "date": "2025-01-15T10:29:58.123456Z",
                "detector": {
                    "name": "aws_iam",
                    "display_name": "AWS Keys",
                    "nature": "specific",
                    "family": "credentials"
                },
                "secret_hash": "abc123...",
                "secret_revoked": false,
                "validity": "valid",
                "occurrence_count": 1,
                "status": "triggered",
                "assignee_email": null,
                "severity": "high",
                "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/incidents/12345"
            }
        }
        




## Webhook limits and best practices

### Request limits

Limit | Value  
---|---  
**Max request size** | 4 MB  
**Max QPS (queries per second)** | 15,000  
**Request timeout** | 30 seconds  
**Retry behavior** | Automatic with exponential backoff  
  
### Best practices

  * **Event selection** : Subscribe only to events relevant to your security operations to reduce noise.
  * **Team scoping** : For business workspaces, create webhooks at the team level to filter incidents by team ownership.
  * **Signature verification** : Store the signature token securely and never commit it to source code.
  * **Monitoring** : Regularly check webhook delivery status in GitGuardian dashboard.
  * **Testing** : Use the test message feature to verify webhook configuration before production use.



### Delivery guarantees

**Important** : Webhook delivery is best effort and not guaranteed. If your Google SecOps endpoint is unreachable or there are network issues, webhook events may not be received. While webhooks are generally reliable, delivery cannot be guaranteed.

For critical use cases, consider supplementing webhooks with periodic API polling to ensure no incidents are missed.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
date | metadata.event_timestamp | Converted using ISO8601 format  
has_user | metadata.event_type | Set to "USER_UNCATEGORIZED" if has_user is true, else "GENERIC_EVENT"  
event_name | metadata.product_event_type | Value copied directly  
id | metadata.product_log_id | Value copied directly  
| metadata.product_name | Set to "GitGuardian Enterprise"  
| metadata.vendor_name | Set to "GitGuardian"  
member_email | principal.user.email_addresses | Merged from member_email  
member_name | principal.user.user_display_name | Value copied directly  
member_id | principal.user.userid | Converted to string  
action_type | security_result.action_details | Value copied directly  
target_ids | target.resource.product_object_id | Value from first element of target_ids  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gitguardian-enterprise-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/keycloak/
title: Collect Keycloak logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:58.681698+00:00
---

# Collect Keycloak logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/keycloak/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Keycloak logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure Keycloak to push logs to Google Security Operations using webhooks.

Keycloak is an open-source identity and access management (IAM) solution that provides single sign-on (SSO), user federation, identity brokering, and social login capabilities. It supports OpenID Connect, OAuth 2.0, and SAML 2.0 protocols and tracks user events (login, logout, registration, password changes) and admin events (user, client, realm, and role management operations) for security auditing.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A running Keycloak instance (version 20 or later recommended)
  * Administrator access to the Keycloak Admin Console
  * Access to the Keycloak server filesystem or container to deploy extensions
  * Access to Google Cloud Console (for API key creation)



## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Keycloak Events`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Keycloak** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Enter `\n` to split multi-line events (each webhook POST contains a single event, so this can be left empty).
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
  2. Select your project (the project associated with your Chronicle instance).
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

**Note:** Restricting the API key ensures it can only be used with the Chronicle API, reducing security risk if the key is compromised.

## Enable event storage in Keycloak

Before configuring the webhook extension, enable event storage in Keycloak so that events are generated and available for forwarding.

### Enable user events

  1. Sign in to the **Keycloak Admin Console**.
  2. Select the **realm** you want to monitor from the realm dropdown in the upper-left corner.
  3. Go to **Realm Settings > Events**.
  4. Select the **User events settings** sub-tab.
  5. Enable the **Save events** toggle.
  6. Set the **Expiration** period (minimum recommended: **7 days**).
  7. Click **Save**.



### Enable admin events

  1. On the same **Events** tab, select the **Admin events settings** sub-tab.
  2. Enable the **Save events** toggle.
  3. Enable the **Include representation** toggle to capture full details of changed objects.
  4. Set the **Expiration** period (minimum recommended: **7 days**).
  5. Click **Save**.



## Install the webhook event listener extension

Keycloak does not include a native webhook event listener. Install the `keycloak-events` extension from Phase Two (p2-inc) to enable webhook delivery.

### Download and deploy the extension

  1. Download the latest release JAR from the [keycloak-events releases page on Maven Central](https://github.com/p2-inc/keycloak-events) or build from source:
         
         git clone https://github.com/p2-inc/keycloak-events.git
         cd keycloak-events
         mvn clean install
         

  2. Copy the resulting fat JAR file into the Keycloak `providers` directory:
         
         cp target/keycloak-events-*.jar /opt/keycloak/providers/
         

  3. Rebuild and restart Keycloak:
         
         /opt/keycloak/bin/kc.sh build
         /opt/keycloak/bin/kc.sh start
         

**Note:** For containerized deployments, add the JAR to the `/opt/keycloak/providers/` directory in your container image and rebuild.



### Enable the webhook event listener

  1. Sign in to the **Keycloak Admin Console**.
  2. Select the target **realm** from the realm dropdown.
  3. Go to **Realm Settings > Events**.
  4. In the **Event listeners** dropdown, select **ext-event-webhook**.
  5. Click **Save**.



## Configure Keycloak webhook

### Construct the webhook URL

  * Combine the Chronicle endpoint URL and API key:
        
        <ENDPOINT_URL>?key=<API_KEY>
        

  * **Example:**
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...
        




### Create webhook subscription via Keycloak REST API

The `keycloak-events` extension provides REST endpoints for managing webhook subscriptions. Use the Keycloak Admin REST API to create a webhook.

#### Step 1: Obtain an access token

  * Request an access token from Keycloak using an admin account:
        
        TOKEN=$(curl -sS -X POST "https://<KEYCLOAK_HOST>/realms/master/protocol/openid-connect/token" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          --data-urlencode "grant_type=password" \
          --data-urlencode "client_id=admin-cli" \
          --data-urlencode "username=<ADMIN_USERNAME>" \
          --data-urlencode "password=<ADMIN_PASSWORD>" \
          | sed -n 's/.*"access_token":"\([^"]*\)".*/\1/p')
        




Replace the following:

  * `<KEYCLOAK_HOST>`: Your Keycloak server hostname and port (for example, `keycloak.example.com:8443`)
  * `<ADMIN_USERNAME>`: Your Keycloak admin username
  * `<ADMIN_PASSWORD>`: Your Keycloak admin password



#### Step 2: Create the webhook

  * Send a POST request to create the webhook subscription for the target realm:
        
        curl -sS -X POST "https://<KEYCLOAK_HOST>/realms/<REALM_NAME>/webhooks" \
          -H "Authorization: Bearer ${TOKEN}" \
          -H "Content-Type: application/json" \
          -d '{
            "enabled": "true",
            "url": "<ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>",
            "secret": "<WEBHOOK_HMAC_SECRET>",
            "eventTypes": ["*"]
          }'
        




Replace the following:

  * `<KEYCLOAK_HOST>`: Your Keycloak server hostname
  * `<REALM_NAME>`: The name of the realm to monitor (for example, `master` or `my-realm`)
  * `<ENDPOINT_URL>`: The Chronicle feed endpoint URL copied earlier
  * `<API_KEY>`: The Google Cloud API key created earlier
  * `<SECRET_KEY>`: The Chronicle webhook secret key generated earlier
  * `<WEBHOOK_HMAC_SECRET>`: An arbitrary secret string for HMAC signing of webhook payloads (for example, `mySecretKey123`)



#### Step 3: Verify the webhook

  * Confirm the webhook was created by listing all webhooks for the realm:
        
        curl -sS -X GET "https://<KEYCLOAK_HOST>/realms/<REALM_NAME>/webhooks" \
          -H "Authorization: Bearer ${TOKEN}" \
          -H "Accept: application/json"
        




The response returns a list of webhook objects. Verify that your webhook appears with `"enabled": "true"` and the correct URL.

### Webhook event types

The `eventTypes` field accepts an array of expressions to filter which events are sent:

  * `*` — Send all events (recommended for SIEM integration)
  * `access.*` — Send all access events
  * `admin.*` — Send all admin events
  * `admin.USER-*` — Send all admin events related to users
  * `admin-USER-CREATE` — Send only user creation admin events



### Webhook payload format

  * The webhook sends events as HTTP POST requests with JSON payloads. Example user event payload:
        
        {
          "id": "987865-1a2b-3c4d-9876-654321abc",
          "time": 1767799710612,
          "type": "LOGIN",
          "realmId": "12345abcde-1a2b-4d3c-9876-abcd456",
          "clientId": "account-console",
          "userId": "abcd456-1234-5678-abc9-987gfed654",
          "sessionId": "efghij-9876-abcd-456-11223344",
          "ipAddress": "203.0.113.45",
          "details": {
            "auth_method": "openid-connect",
            "auth_type": "code",
            "redirect_uri": "https://app.example.com/callback",
            "consent": "no_consent_required",
            "username": "jdoe"
          }
        }
        




### Webhook retry behavior

The extension uses automatic exponential backoff for retries when a non-2xx response is received:

Parameter | Default Value | Description  
---|---|---  
**backoffInitialInterval** | 500 ms | Initial retry interval  
**backoffMaxElapsedTime** | 900000 ms (15 min) | Maximum total retry time  
**backoffMaxInterval** | 180000 ms (3 min) | Maximum interval between retries  
**backoffMultiplier** | 5 | Multiplier for each retry interval  
**backoffRandomizationFactor** | 0.5 | Randomization factor for jitter  
  
## Authentication methods reference

Chronicle webhook feeds support multiple authentication methods. Choose the method that your vendor supports.

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

Chronicle accepts the following header names for authentication:

**For API key:**

  * `x-goog-chronicle-auth` (recommended)
  * `X-Goog-Chronicle-Auth` (case-insensitive)



**For secret key:**

  * `x-chronicle-auth` (recommended)
  * `X-Chronicle-Auth` (case-insensitive)

**Note:** The Keycloak `keycloak-events` webhook extension sends events as HTTP POST with JSON content type. Because the extension does not support custom HTTP headers on outbound requests, use the query parameter method (Method 2) by appending `?key=<API_KEY>&secret=<SECRET_KEY>` to the webhook URL.

## Webhook limits and best practices

### Request limits

Limit | Value  
---|---  
**Max request size** | 4 MB  
**Max QPS (queries per second)** | 15,000  
**Request timeout** | 30 seconds  
**Retry behavior** | Automatic with exponential backoff  
  
## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
payload.client_id | additional.fields | Merged with fields created from payload.client_id, payload.realm_id  
payload.realm_id | additional.fields |   
source_timestamp | metadata.event_timestamp | Parsed using date filter with patterns ISO8601 and yyyy-MM-dd'T'HH:mm:ss.SSSZ  
payload.ip_address | metadata.event_type | Set to "STATUS_UPDATE" if payload.ip_address is not empty, else "USER_UNCATEGORIZED" if uuid is not empty, else "GENERIC_EVENT"  
uuid | metadata.event_type |   
payload.type | metadata.product_event_type | Value copied directly  
payload.session_id | network.session_id | Value copied directly  
payload.ip_address | principal.ip | Value copied directly  
source_metadata.schema | principal.resource.attribute.labels | Merged with labels created from source_metadata.schema, source_metadata.table, source_metadata.is_deleted (converted to string), source_metadata.change_type, source_metadata.tx_id, source_metadata.lsn  
source_metadata.table | principal.resource.attribute.labels |   
source_metadata.is_deleted | principal.resource.attribute.labels |   
source_metadata.change_type | principal.resource.attribute.labels |   
source_metadata.tx_id | principal.resource.attribute.labels |   
source_metadata.lsn | principal.resource.attribute.labels |   
uuid | principal.user.userid | Value copied directly  
object | security_result.detection_fields | Merged with labels created from object, read_method, payload.id  
read_method | security_result.detection_fields |   
payload.id | security_result.detection_fields |   
redirect_uri | target.url | Value copied directly  
username | target.user.userid | Value copied directly  
metadata.product_name | metadata.product_name | Set to "KEYCLOAK"  
metadata.vendor_name | metadata.vendor_name | Set to "KEYCLOAK"  
`username" from "details_json` | `target.user.userid` | Mapped from changelog  
`redirect_uri" from "details_json` | `target.url` | Mapped from changelog  
`realm_id" and "client_id` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/keycloak-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

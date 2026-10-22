---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oort/
title: Collect Cisco Identity Intelligence logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:55.304898+00:00
---

# Collect Cisco Identity Intelligence logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oort/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Identity Intelligence logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to configure Cisco Identity Intelligence to push logs to Google Security Operations using webhooks.

Cisco Identity Intelligence (formerly Oort Security) is an identity threat detection and response platform that continuously monitors user behavior, authentication patterns, device usage, and access privileges across identity providers. It detects identity-based threats, misconfigurations, and compliance violations by analyzing user activity, failed security checks, trust scores, and risky behaviors.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to a Cisco Identity Intelligence tenant
  * Administrative permissions to manage integrations in Cisco Identity Intelligence
  * Access to Google Cloud Console (for API key creation)



## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Cisco Identity Intelligence Events`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Cisco Identity Intelligence** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Enter `\n` to split multi-line events.
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

## Configure Cisco Identity Intelligence webhook

### Construct the webhook URL

  * Combine the Chronicle endpoint URL and API key:
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

    * **Example:**
          
          https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...
          




Replace the following:

  * `<ENDPOINT_URL>`: The Chronicle feed endpoint URL copied earlier
  * `<API_KEY>`: The Google Cloud API key created earlier
  * `<SECRET_KEY>`: The Chronicle webhook secret key generated earlier



### Create webhook notification target in Cisco Identity Intelligence

  1. Sign in to **Cisco Identity Intelligence**.
  2. Go to **Integrations**.
  3. Click **Add Integration**.
  4. Scroll down to the **Webhook** section.
  5. Click **Add Webhook Target**.
  6. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Chronicle SIEM Integration`).
     * **Webhook URL** : Paste the complete endpoint URL with API key and secret key from above.
     * **Authorization Type** : Select **API Key**.
     * **API Key Name** : Enter a key name (for example, `x-goog-chronicle-auth`).
     * **API Key Value** : Enter the Google Cloud API key.
  7. Expand the **Invocation HTTP Parameters** section.
  8. Add the following parameters with the type **Header** : 
     * **Key** : `Content-Type`, **Value** : `application/json`
     * **Key** : `Accept`, **Value** : `application/json`
  9. In the **Use this target for** section, select **Failed Check** to receive notifications when identity checks detect failed results.
  10. Click **Save**.

**Note:** The webhook destination must have a valid public trusted certificate. Certificates from a private PKI are not supported.



### Test the webhook connection

  1. On the **Integrations** page, find the webhook notification target you created.
  2. Click the **three-dot menu** on the right side of the row.
  3. Select **Test Connectivity**.
  4. Verify that the test message is delivered successfully.



### Enable the webhook for identity checks

After creating the webhook notification target, you must enable it for the specific identity checks you want to monitor.

  1. Go to the desired **Check** details page in Cisco Identity Intelligence.
  2. Expand the dropdown on the top-right corner of the page.
  3. Select the checkbox for the webhook notification target you created.
  4. Repeat for each check you want to send to Google SecOps.

**Note:** Nothing will be sent through the webhook until it is enabled for at least one identity check. Once enabled, Cisco Identity Intelligence sends an event to the webhook once a day with a payload including the list of new users failing the enabled check.



For more information, see the [Cisco Identity Intelligence webhook documentation](https://docs.oort.io/integrations/webhooks).

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

**Note:** Cisco Identity Intelligence supports custom HTTP headers through Invocation HTTP Parameters. You can use either the query parameter method (Method 2) by appending credentials to the webhook URL, or configure custom headers (Method 1) through the Invocation HTTP Parameters section. The query parameter method is the simplest approach for this integration.

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
account | account_label.value | Value copied directly  
account | account_label.key | Set to "account"  
account_label | security_result.detection_fields | Merged into detection_fields  
additional_detaildescription.key | additional_detaildescription.key | Set to "detail description"  
detaildescription | additional_detaildescription.value.list_value.values | Merged from detaildescription  
additional_detaildescription | event.idm.read_only_udm.additional.fields | Merged into additional.fields  
additional_recommendedaction.key | additional_recommendedaction.key | Set to "recommended action"  
recommendedAction | additional_recommendedaction.value.list_value.values | Merged from recommendedAction  
additional_recommendedaction | event.idm.read_only_udm.additional.fields | Merged into additional.fields  
data1 | usersFailing_label | Value copied directly  
data.login | login_label | Value copied directly  
detail-type | security_result.summary | Value copied directly  
detail.id | security_result.rule_id | Value copied directly  
detail.title | security_result.rule_name | Value copied directly  
detail.severity | security_result.severity | Value from detail.severity if in [CRITICAL,ERROR,HIGH,INFORMATIONAL,LOW,MEDIUM], else MEDIUM if moderate  
detaildescription | value_array.string_value | Value copied directly  
detailsdata.key | add_label.value, add_label.key | Value from detailsdata.value, key as "loginDetails %{index} details %{detailindex} %{detailsdata.key}" if not failedSigninDetails or ips  
detailsdata.value | add_label.value, add_label.key |   
detailsdata.key | security_result.detection_fields | Merged add_label if conditions met  
detailsdata.value | security_result.detection_fields |   
field_.value | security_result.detection_fields | Merged for various nested fields in json_array (msg, ipInfo, asn, coordinates, first_event, second_event, locations) with keys like "%{index} %{detailindex} %{index1} %{key}" etc., excluding ipAddress, ip, etc.  
field_.key | security_result.detection_fields |   
id | metadata.product_log_id | Value copied directly  
login_label | principal.user.email_addresses | Merged if matches email regex  
msg.ipAddress | principal.ip | Merged if not empty  
msg.first_event.ip_address | principal.ip | Merged if not empty  
msg.second_event.ip_address | principal.ip | Merged if not empty  
msg_travels_first_event_ip_address | principal.ip | Merged if not empty  
msg_travels_second_event_ip_address | principal.ip |   
recommendedAction | value_array.string_value | Value copied directly  
security_result | event.idm.read_only_udm.security_result | Merged into security_result  
source | source_label.value | Value copied directly  
source | source_label.key | Set to "source"  
source_label | event.idm.read_only_udm.src.labels | Merged into src.labels  
time | @timestamp | Parsed using date filter with ISO8601, RFC 3339, yyyy-MM-ddTHH:mm:ss.SSSSSSZ  
usersFailing_label | principal.user.email_addresses | Merged if matches email regex  
version | metadata.product_version | Value copied directly  
has_principal | event.idm.read_only_udm.metadata.event_type | Set to "STATUS_UPDATE" if has_principal true, else "USER_UNCATEGORIZED" if has_user true, else "GENERIC_EVENT"  
has_user | event.idm.read_only_udm.metadata.event_type |   
metadata.product_name | metadata.product_name | Set to "OORT"  
metadata.vendor_name | metadata.vendor_name | Set to "OORT"  
`detail.published` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`detail.login` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`detail.userTrustLevel` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`detail.login` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`detail.checkTopics` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`region` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detail.checkId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detail.checkScope` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detail.frameworks` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detail.explainabilityEventIds` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.value` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oort-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 

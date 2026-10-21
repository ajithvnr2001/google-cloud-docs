---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-reporter-plus/
title: Collect ManageEngine Exchange Reporter Plus logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:32.658798+00:00
---

# Collect ManageEngine Exchange Reporter Plus logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-reporter-plus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ManageEngine Exchange Reporter Plus logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure ManageEngine Exchange Reporter Plus to push logs to Google Security Operations using webhooks.

ManageEngine Exchange Reporter Plus is a web-based reporting, auditing, and monitoring solution for Microsoft Exchange Server and Exchange Online environments. It provides comprehensive reports on mailbox sizes, email traffic, public folders, Exchange ActiveSync logs, and audit logs for administrator activities and configuration changes in hybrid Exchange deployments.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * ManageEngine Exchange Reporter Plus installed and configured to monitor Exchange Server or Exchange Online
  * Administrative access to the ManageEngine Exchange Reporter Plus web console
  * Access to Google Cloud Console (for API key creation)



## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `ManageEngine Exchange Reporter Plus Logs`).
  5. Select **Webhook** as the **Source type**.
  6. Select **ManageEngine Exchange Reporter Plus** as the **Log type**.
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

## Configure ManageEngine Exchange Reporter Plus webhook

### Construct the webhook URL

  * Combine the Chronicle endpoint URL, API key, and secret key:
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

  * **Example:**
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...
        




### Configure log forwarding in Exchange Reporter Plus

  1. Sign in to the **ManageEngine Exchange Reporter Plus** web console as an administrator.
  2. Go to **Settings > Admin > General Settings > Log Forwarder**.
  3. Select the **Enable Log Forwarding** checkbox.
  4. Click the **Webhook** tab.
  5. Provide the following configuration details: 
     * **HTTP Method** : Select **POST**.
     * **HTTP URL** : Paste the complete webhook URL constructed in the previous step (the Chronicle endpoint URL with the API key and secret key appended as query parameters).
  6. In the **Advanced Settings** section: 
     1. Click **HTTP Request Headers**.
     2. Add the following header: 
        * **Key** : `Content-Type`
        * **Value** : `application/json`
  7. Click **Save**.

**Note:** For more details on configuring the Log Forwarder, refer to the [ManageEngine Exchange Reporter Plus Log Forwarder documentation](https://www.manageengine.com/products/exchange-reports/help/admin/log-forwarder.html).



### Verify log forwarding

  1. After saving the configuration, Exchange Reporter Plus will begin forwarding audit logs to Google SecOps through the webhook endpoint.
  2. Sign in to the Google SecOps console and verify that logs appear in the **Search** interface with the ingestion label `MANAGE_ENGINE_REPORTER_PLUS`.



### Firewall configuration

Ensure the following firewall rules are configured.

**Outbound from Exchange Reporter Plus server:**

  * Protocol: HTTPS (TCP 443)
  * Destination: Chronicle regional endpoint (`<region>-chronicle.googleapis.com`)
  * Purpose: Log delivery to Google SecOps via webhook



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
        




**Disadvantages:** \- Credentials visible in URL \- May be logged in web server access logs \- Less secure than headers

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

**Note:** ManageEngine Exchange Reporter Plus Log Forwarder supports custom HTTP request headers through its **Advanced Settings** section. You can use either Method 1 (custom headers) or Method 2 (query parameters) depending on your security requirements. If using custom headers, add `x-goog-chronicle-auth` and `x-chronicle-auth` headers in the **HTTP Request Headers** configuration instead of appending credentials to the URL.

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
msg.OrganizationId | additional.fields | Merged labels with key "OrganizationId" and value from msg.OrganizationId; key "MailboxGuid" and value from msg.MailboxGuid; key "RecordType" and value from msg.RecordType  
msg.MailboxGuid | additional.fields |   
msg.RecordType | additional.fields |   
msg.CreationTime | metadata.event_type | Set to value from event_type if not empty; else "USER_UNCATEGORIZED" if msg.Operation == "Update"; else "USER_CREATION" if msg.Operation == "Create" and msg.MailboxOwnerUPN not empty; else "USER_UNCATEGORIZED" if msg.Operation == "Create"; else "USER_UNCATEGORIZED" if msg.UserId not empty; else "STATUS_UPDATE" if msg.ClientIP not empty; else "GENERIC_EVENT"  
msg.Operation | metadata.product_event_type | Value copied directly  
msg.Id | metadata.product_log_id | Value copied directly  
msg.ClientVersion | metadata.product_version | Value from msg.ClientVersion if not empty, else msg.Version converted to string  
msg.Version | metadata.product_version |   
AffectedItems.0.InternetMessageId | network.email.mail_id | Gsub <  
AffectedItems | network.email.subject | Parsed as JSON, extracted item.Subject, merged if found  
msg.ClientInfoString | network.http.user_agent | Value from msg.ClientInfoString if not empty, else msg.Client  
msg.Client | network.http.user_agent |   
msg.ClientProcessName | principal.application | Value copied directly  
msg.OriginatingServer | principal.hostname | Extracted using grok pattern, if successful, else value copied directly  
clientIP | principal.ip | Extracted from msg.ClientIP using grok  
clientPort | principal.port | Extracted from msg.ClientIP using grok, converted to integer  
msg.UserKey | principal.user.attribute.labels | Set label key to "UserKey", value to msg.UserKey, merged  
msg.UserType | principal.user.attribute.roles | Set roles.name to msg.UserType, merged  
msg.UserId | principal.user.email_addresses | Merged if msg.UserId matches email regex  
msg.UserId | principal.user.userid | Value copied directly  
msg.MailboxOwnerSid | principal.user.windows_sid | Value from msg.MailboxOwnerSid if not empty, else msg.LogonUserSid  
msg.LogonUserSid | principal.user.windows_sid |   
security_result | security_result | Merged from security_result hash  
security_result_action | security_result.action | Merged from security_result_action  
msg.ResultStatus | security_result.action_details | Value copied directly  
msg.RecordType | security_result.detection_fields | Converted to string, set key "RecordType", value to msg.RecordType, merged  
msg.OrganizationName | target.administrative_domain | Value copied directly  
msg.DestFolder | target.file.full_path | Extracted fileId and filePath using grok, gsubs backslashes, concatenated as fileId/filePath  
host | target.hostname | Value copied directly  
msg.Folder | target.process.parent_process.file.full_path | Extracted parentFileId and parentFilePath using grok, gsubs backslashes, concatenated as parentFileId/parentFilePath  
msg.MailboxOwnerUPN | target.user.email_addresses | Merged if matches email regex  
msg.MailboxOwnerUPN | target.user.user_display_name | Set if contains space  
msg.MailboxOwnerUPN | target.user.userid | Set if not email and no space  
metadata.product_name | metadata.product_name | Set to "Manage Engine"  
metadata.vendor_name | metadata.vendor_name | Set to "Manage Engine Reporter Plus"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/manage-engine-reporter-plus-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 

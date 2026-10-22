---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dnsfilter/
title: Collect DNSFilter logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:50.065401+00:00
---

# Collect DNSFilter logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dnsfilter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect DNSFilter logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure DNSFilter to push logs into Google Security Operations using webhooks via the HTTP Event Collector (HEC) protocol.

DNSFilter is an AI-powered DNS security solution that provides threat protection, content filtering, and network visibility. The Data Export feature enables automated export of DNS query log data to SIEM platforms via HTTP Event Collector (HEC) API, supporting real-time security monitoring and compliance reporting.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Access to **DNSFilter dashboard** with administrator permissions or higher
  * **DNSFilter Data Export** add-on feature enabled (available for Basic, Pro, and Enterprise plans as a paid add-on)
  * Access to Google Cloud Console (for API key creation)



## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `DNSFilter HEC Feed`).
  5. Select **Webhook** as the **Source type**.
  6. Select **DNSFILTER** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Leave empty as each HEC request contains properly formatted events
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

  1. In the **API key** settings page: **Name** : Enter a descriptive name (for example, `Google SecOps DNSFilter Webhook API Key`)
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Chronicle API, reducing security risk if the key is compromised.



## Configure DNSFilter Data Export

### Construct the HEC endpoint URL

  * Combine the Google SecOps endpoint URL and API key to create the HEC URL:
        
        <ENDPOINT_URL>?key=<API_KEY>
        

  * Example:
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...
        




### Configure Data Export in DNSFilter

  1. Sign in to the **DNSFilter dashboard**.
  2. Go to **Tools > Data Export**.
  3. In the **Export Destination** section, select **HTTP Event Collector (HEC)**.
  4. In the **HEC Configuration** section, enter the following: 
     * **HTTP Event Collector URL** : Paste the complete endpoint URL with API key from the previous step.
     * **Active Event Collector Token** : Paste the secret key generated during Google SecOps feed creation.
  5. Click **Save Configuration**.
  6. DNSFilter will test the connection and display a success message if the configuration is correct.

**Note:** DNSFilter exports logs in CSV format by default. The Data Export feature automatically exports query log data multiple times per hour to your configured HEC endpoint. Each export includes more than 25 categories of data including domain name, request address, server address, timestamps, policy actions, and threat categories.



## Verify data ingestion

  1. In the **DNSFilter dashboard** , go to **Tools > Data Export**.
  2. Verify the **Status** shows as **Active** or **Connected**.
  3. In the Google SecOps console, go to **SIEM Settings > Feeds**.
  4. Locate your DNSFilter feed and verify the **Status** shows as **Active**.
  5. Click the feed name to view details.
  6. Check the **Logs Ingested** metric to confirm data is flowing.
  7. To search for DNSFilter events, go to **Search** , and run the following query:
         
         metadata.log_type = "DNSFILTER"
         




## Authentication methods reference

Google SecOps webhook feeds support multiple authentication methods. DNSFilter HEC integration uses the hybrid method.

### Method used: Hybrid (URL + Header)

DNSFilter sends the API key in the URL and the secret key (HEC token) in the request header.

  * **Request format:**
        
        POST <ENDPOINT_URL>?key=<API_KEY> HTTP/1.1
        Content-Type: application/json
        Authorization: Splunk <SECRET_KEY>
        
        {
            "event": "data",
            "timestamp": "2025-01-15T10:30:00Z"
        }
        

**Note:** DNSFilter uses the standard Splunk HEC authentication header format `Authorization: Splunk <TOKEN>`, which Google SecOps accepts as equivalent to `x-chronicle-auth: <SECRET_KEY>`.



### Alternative method: Custom headers

If configuring a custom application to send logs to Google SecOps, use this method for better security.

  * **Request format:**
        
        POST <ENDPOINT_URL> HTTP/1.1
        Content-Type: application/json
        x-goog-chronicle-auth: <API_KEY>
        x-chronicle-auth: <SECRET_KEY>
        
        {
            "event": "data",
            "timestamp": "2025-01-15T10:30:00Z"
        }
        

  * **Advantages:**

    * API key and secret not visible in URL
    * More secure (headers not logged in web server access logs)
    * Preferred method when vendor supports it



### Authentication header names

Google SecOps accepts the following header names for authentication:

  * **For API key:**

    * `x-goog-chronicle-auth` (recommended)
    * `X-Goog-Chronicle-Auth` (case-insensitive)
  * **For secret key:**

    * `x-chronicle-auth` (recommended)
    * `X-Chronicle-Auth` (case-insensitive)
    * `Authorization: Splunk <TOKEN>` (HEC compatibility)



## Webhook limits and best practices

### Request limits

Limit | Value  
---|---  
**Max request size** | 4 MB  
**Max QPS (queries per second)** | 15,000  
**Request timeout** | 30 seconds  
**Retry behavior** | Automatic with exponential backoff  
  
### Best practices

  * **Monitor export status** : Regularly check the Data Export status in DNSFilter dashboard to ensure continuous data flow.
  * **API key rotation** : Periodically rotate your Google Cloud API key for security.
  * **Secret key management** : Store the Google SecOps secret key securely and regenerate if compromised.
  * **Data retention** : Configure appropriate data retention policies in both DNSFilter and Google SecOps.
  * **Alert configuration** : Set up alerts in Google SecOps for critical DNS security events.



## Troubleshooting

### Connection test fails

If the DNSFilter Data Export configuration test fails:

  1. Verify the HEC URL is correct and includes the API key parameter.
  2. Verify the secret key (HEC token) is copied correctly without extra spaces.
  3. Check that the Google Cloud API key has Chronicle API access enabled.
  4. Verify the Google SecOps feed is in **Active** status.
  5. Check network connectivity from DNSFilter to Google Cloud endpoints.



### No data appearing in Google SecOps

If the connection succeeds but no data appears:

  1. Verify DNS queries are being generated in your DNSFilter deployment.
  2. Check the DNSFilter Query Log to confirm traffic is being processed.
  3. In Google SecOps, search for `metadata.log_type = "DNSFILTER"` to verify ingestion.
  4. Check the feed **Logs Ingested** metric in Google SecOps.
  5. Review the feed **Error Logs** for any ingestion errors.



### Data Export returns error message

Common error causes:

  * **Invalid credentials** : The API key or secret key is incorrect or expired.
  * **Region mismatch** : The Google SecOps endpoint URL region doesn't match your instance.
  * **Permissions** : The API key doesn't have Chronicle API access enabled.
  * **Network issues** : Firewall or proxy blocking outbound HTTPS connections.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
time | metadata.collected_timestamp | Converted using date format: yyyy-MM-dd HH:mm:ss Z UTC  
| metadata.event_type | Set to "STATUS_UPDATE" if principal_ip_present, principal_hostname_present, or principal_mac_present is true, else "GENERIC_EVENT"  
question_type | network.dns.questions | Converted question_type to question.type using DNS record type mapping, then merged into array  
code | network.dns.response_code | Converted using DNS response code mapping  
protocol | network.ip_protocol | Converted using IP protocol mapping  
client | principal.hostname | Value copied directly  
request_address, ip4, ip6, source_addresses | principal.ip | Merged from request_address (extracted IP), ip4 (extracted IP), ip6 (extracted IP), and IPs extracted from source_addresses array  
region | principal.location.country_or_region | Value copied directly  
clientMac | principal.mac | Value copied directly if matches MAC regex  
clientID | principal.resource.product_object_id | Value copied directly  
username | principal.user.user_display_name | Value copied directly  
user_id | principal.user.userid | Value copied directly  
code, original_code, clientType, collection, network_name, networkID, collectionID, policy, policyID, scheduled_policy, scheduled_policyID, sec_cats, sec_allow_cats, block_cats, block_allow_cats, threat, allowed, method, organization, organizationID, applicationID, application_name, application_categoryID, application_category_name | security_result.detection_fields | Merged labels from various source fields as key-value pairs  
domain | target.administrative_domain | Value copied directly  
fqdn | target.domain.name | Value copied directly  
| metadata.product_name | Set to "DNSFILTER"  
| metadata.vendor_name | Set to "DNSFILTER"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dnsfilter-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

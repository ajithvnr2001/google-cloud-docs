---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/thinkst-canary/
title: Collect Thinkst Canary logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:53.172918+00:00
---

# Collect Thinkst Canary logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/thinkst-canary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Thinkst Canary logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Thinkst Canary logs by setting up a Google Security Operations feed using the Third Party API.

Thinkst Canary provides deception-based threat detection: hardware, virtual and cloud Canaries impersonate real assets, and Canarytokens act as tripwires in files, credentials and URLs. When an attacker touches a Canary or trips a token, the Canary Console records an incident. The feed retrieves those incidents from the Console API.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the Thinkst Canary Console



## Configure the REST API in Thinkst Canary

  1. Sign in to your **Thinkst Canary Console** (`https://<DOMAIN_HASH>.canary.tools`).
  2. Click the **gear icon** in the top right corner and select **Global Settings**.
  3. In the menu, click **API**.
  4. If the API is disabled, click **Enable API**.
  5. Use the existing **Default API Key** , or click **\+ Add new API key** to create a dedicated one:

     * **API key type** : Select **Read-Only**. This is sufficient for log collection.
     * **Note** : Enter a name for the key (for example, `Google SecOps Integration`).
**Note:** The key type is fixed at creation and cannot be changed later.
  6. Copy and save the following in a secure location:

     * **Domain Hash** : The identifier of your Console. Your API hostname is `<DOMAIN_HASH>.canary.tools`.
     * **Auth Token** : The API key used to authenticate requests.



## Configure a feed in Google SecOps to ingest Thinkst Canary logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Thinkst Canary Logs`).
  5. Select **Third Party API** as the **Source type**.
  6. Select **Thinkst Canary** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Authentication HTTP header** : The token generated earlier, in the `auth_token:<TOKEN>` format (for example, `auth_token:AAAABBBBCCCC111122223333`).
     * **API Hostname** : The fully qualified domain name of your Thinkst Canary REST API endpoint, in the `<DOMAIN_HASH>.canary.tools` format (for example, `myinstance.canary.tools`).
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




After setup, the feed begins to retrieve logs from the Thinkst Canary instance in chronological order.

## Incident updates and re-delivery

The Canary Console API returns an incident again whenever the incident is updated, not only when it is created. Canary bundles subsequent similar events from the same source into the existing incident. For example, each brute-force attack attempt becomes an event inside a single incident. Other incident modifications can also trigger re-delivery.

Expect the following behavior in Google SecOps:

  * Incidents that were already delivered reappear in the feed after they are updated.
  * A re-delivered incident can surface with an event timestamp considerably older than the moment it was re-delivered. This is because the parser derives event timestamps from the incident's original creation time and from the bundled events' own occurrence times, not from the update time.



The re-delivery itself is the documented behavior of the incident collection API (it filters on the incident's update counter), not data loss or a parser defect.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`_canary_uptime_label` | `additional.fields` | Merged  
`desc_events_n_func_code_label` | `additional.fields` | Merged  
`desc_events_n_func_name_label` | `additional.fields` | Merged  
`desc_events_n_sfunc_code_label` | `additional.fields` | Merged  
`desc_events_n_sfunc_name_label` | `additional.fields` | Merged  
`desc_events_n_timestamp_std_label` | `additional.fields` | Merged  
`desc_events_n_unit_id_label` | `additional.fields` | Merged  
`description_created_std_label` | `additional.fields` | Merged  
`description_events_list_label` | `additional.fields` | Merged  
`event_data_list` | `additional.fields` | Merged  
`event_descrip_label` | `additional.fields` | Merged  
`events_url_label` | `additional.fields` | Merged  
`local_time_label` | `additional.fields` | Merged  
`locale_label` | `additional.fields` | Merged  
`lt_label` | `additional.fields` | Merged  
`offline_text_label` | `additional.fields` | Merged  
`updated_label` | `additional.fields` | Merged  
`updated_std_label` | `additional.fields` | Merged  
`_auth` | `extensions.auth` | Renamed/mapped  
`_metadata` | `metadata` | Renamed/mapped  
`_event_time` | `metadata.event_timestamp` | Parsed as `UNIX`  
`_metadata_event_timestamp` | `metadata.event_timestamp` | Parsed as `UNIX`  
`description.created_std` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`elem.timestamp_std` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss ZZZ+0000`  
`updated` | `metadata.event_timestamp` | Parsed as `EEE, dd MMM yyyy HH:mm:ss ZZZ`  
`updated_std` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`format` | `metadata.event_type` | Mapped: `grok` → `STATUS_UPDATE`, `grok` → `GENERIC_EVENT`  
`has_principal_hostname` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`_network` | `network` | Renamed/mapped  
`_observer` | `observer` | Renamed/mapped  
`_principal` | `principal` | Renamed/mapped  
`ThinkstCanary_Process` | `principal.application` | Directly mapped  
`ThinkstCanary_Process` | `principal.asset.hostname` | Directly mapped  
`ThinkstCanary_Hostname` | `principal.hostname` | Directly mapped  
`_md_product_event_type` | `security_result` | Mapped values (10 total, e.g. `Shared File Opened` → `_security_result`, `Host Port Scan` → ...  
`_security_result` | `security_result` | Merged  
`format` | `security_result` | Mapped: `kv` → `_security_result`, `json` → `_security_result`  
`_source` | `src` | Renamed/mapped  
`_target` | `target` | Renamed/mapped  
N/A | `metadata.event_type` | Constant: `STATUS_UPDATE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/thinkst-canary-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

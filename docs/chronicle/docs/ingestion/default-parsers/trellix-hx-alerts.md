---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-alerts/
title: Collect Trellix Endpoint Security (HX) alert logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:35.889973+00:00
---

# Collect Trellix Endpoint Security (HX) alert logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trellix Endpoint Security (HX) alert logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Trellix Endpoint Security (HX) alert logs by setting up a Google Security Operations feed using the Third-Party API.

Trellix Endpoint Security (HX) is an endpoint detection and response platform that generates alerts when threats are detected on managed endpoints, including malware detections, exploit attempts, IOC matches, and real-time indicator alerts. Collecting these alerts in Google SecOps provides centralized visibility into endpoint threats for detection, investigation, and response workflows.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the Trellix Endpoint Security (HX) management console
  * Trellix Endpoint Security (HX) with API access enabled
  * One of the following authentication credentials configured (see next section)



## Configure Trellix HX API access

To enable Google SecOps to pull alert data, you need API credentials from your Trellix HX environment. 

  1. Sign in to the Endpoint Security (HX) Web UI as an administrator.
  2. Go to **Admin > Appliance Settings > User Accounts**.
  3. Add a new user account with the `api_analyst` role for use with Google SecOps. Do not reuse the built-in `api_analyst` account.
  4. Copy and save the following values: 
     * **Username** : The local HX account username.
     * **Password** : The local HX account password.



## Configure a feed in Google SecOps to ingest Trellix HX alert logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Trellix HX Alerts`).
  5. Select **Third-Party API** as the **Source type**.
  6. Select **Trellix HX Alerts** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **HX Endpoint URL** : The base URL of your HX appliance (for example, `https://xxxxxxxx-hx-webui-1.hex03.apps.xdr.trellix.com`).
     * **Authentication** : **Trellix Local Auth**

       * **Username** : Enter the local HX account username created for this integration.
       * **Password** : Enter the password for the username.
       * **Token API Endpoint Path** : `/hx/api/v3/token`
       * **Token Header** : `X-FeApi-Token`
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




After setup, the feed begins to retrieve alert logs from the Trellix HX instance in chronological order.

## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`event_at` | `metadata.event_timestamp` | Parsed as `RFC3339`  
`reported_at` | `metadata.event_timestamp` | Parsed as `RFC3339`  
`__event_type` | `metadata.event_type` | Mapped: `fileWriteEvent` → `FILE_MODIFICATION`  
`__reg_key_event_type` | `metadata.event_type` | Mapped: `0/1/5` → `REGISTRY_MODIFICATION`, `2/4` → `REGISTRY_DELETION`, `3` → `REGISTRY_CREA...  
`__source` | `metadata.event_type` | Mapped values (9 total, e.g. `IOC` → `FILE_MODIFICATION`, `IOC` → `REGISTRY_MODIFICATION`, `...  
`event_type` | `metadata.event_type` | Mapped values (8 total, e.g. `regKeyEvent` → `REGISTRY_MODIFICATION`, `regKeyEvent` → `REGIS...  
`__appliance_id` | `metadata.product_deployment_id` | Mapped when `__appliance_id` != ``  
`__event_type` | `metadata.product_event_type` | Mapped when `__event_type` != ``  
`__product_log_id` | `metadata.product_log_id` | Mapped when `__product_log_id` != ``  
`__url` | `metadata.url_back_to_product` | Mapped when `__url` != ``  
`__source` | `network.application_protocol` | Mapped: `IOC` → `DNS`, `IOC` → `HTTP`  
`event_type` | `network.application_protocol` | Mapped: `dnsLookupEvent` → `DNS`, `urlMonitorEvent` → `HTTP`  
`__source` | `network.direction` | Mapped: `IOC` → `UNKNOWN_DIRECTION`  
`event_type` | `network.direction` | Mapped: `ipv4NetworkEvent` → `UNKNOWN_DIRECTION`  
`__dns_lookup_event_question` | `network.dns.questions` | Merged  
`__source` | `network.dns.questions` | Mapped: `IOC` → `__dns_lookup_event_question`  
`event_type` | `network.dns.questions` | Mapped: `dnsLookupEvent` → `__dns_lookup_event_question`  
`event_values.__urlMethod` | `network.http.method` | Mapped when `__source` == `IOC`  
`event_values.__userAgent` | `network.http.user_agent` | Mapped when `__source` == `IOC`  
`event_values.__protocol` | `network.ip_protocol` | Mapped when `__source` == `IOC`  
`__agent_data` | `principal` | Renamed/mapped  
`__source` | `principal.ip` | Mapped: `IOC` → `event_values.__localIP`  
`event_type` | `principal.ip` | Mapped: `ipv4NetworkEvent` → `event_values.__localIP`  
`event_values.__localIP` | `principal.ip` | Merged  
`event_values.__localPort` | `principal.port` | Renamed/mapped  
`__parent_process_path` | `principal.process.file.full_path` | Mapped when `__source` == `IOC`  
`__process_full_path` | `principal.process.file.full_path` | Mapped when `__source` == `IOC`  
`__event_type` | `principal.process.file.names` | Mapped: `fileWriteEvent` → `__process`  
`__process` | `principal.process.file.names` | Merged  
`__source` | `principal.process.file.names` | Mapped: `IOC` → `__process`, `IOC` → `event_values.__parentProcess`  
`event_type` | `principal.process.file.names` | Mapped values (6 total, e.g. `regKeyEvent` → `__process`, `ipv4NetworkEvent` → `__process`, ...  
`event_values.__parentProcess` | `principal.process.file.names` | Merged  
`__parent_process_path` | `principal.process.parent_process.file.full_path` | Mapped when `__source` == `IOC`  
`__event_type` | `principal.process.parent_process.file.names` | Mapped: `fileWriteEvent` → `__parent_process`  
`__parent_process` | `principal.process.parent_process.file.names` | Merged  
`__source` | `principal.process.parent_process.file.names` | Mapped: `IOC` → `__parent_process`  
`__parent_pid` | `principal.process.parent_process.pid` | Mapped when `__source` == `IOC`  
`__parent_pid` | `principal.process.pid` | Mapped when `__source` == `IOC`  
`__pid` | `principal.process.pid` | Mapped when `__source` == `IOC`  
`__domain_user` | `principal.user.userid` | Mapped when `__source` == `IOC`  
`__security_result` | `security_result` | Merged  
`__source` | `security_result` | Mapped: `IOC` → `__security_result`  
`__agent_data` | `target` | Renamed/mapped  
`event_values.__fullPath` | `target.file.full_path` | Mapped when `__source` == `IOC`  
`event_values.__md5` | `target.file.md5` | Mapped when `__source` == `IOC`  
`__event_type` | `target.file.names` | Mapped: `fileWriteEvent` → `event_values.__fileName`  
`__source` | `target.file.names` | Mapped: `IOC` → `event_values.__fileName`  
`event_values.__fileName` | `target.file.names` | Merged  
`event_values.__size` | `target.file.size` | Renamed/mapped  
`event_values.__hostname` | `target.hostname` | Mapped when `__source` == `IOC`  
`__source` | `target.ip` | Mapped: `IOC` → `event_values.__remoteIP`, `IOC` → `event_values.__remoteIpAddress`  
`event_type` | `target.ip` | Mapped: `ipv4NetworkEvent` → `event_values.__remoteIP`, `urlMonitorEvent` → `event _values._ _...  
`event_values.__remoteIP` | `target.ip` | Merged  
`event_values.__remoteIpAddress` | `target.ip` | Merged  
`__event_type` | `target.labels` | Mapped values (9 total, e.g. `fileWriteEvent` → `__file_write_event_label_writes`, `fileWrit...  
`__file_write_event_label_closed` | `target.labels` | Merged  
`__file_write_event_label_data_at_lowest_offset` | `target.labels` | Merged  
`__file_write_event_label_event_reason` | `target.labels` | Merged  
`__file_write_event_label_lowest_file_offset_seen` | `target.labels` | Merged  
`__file_write_event_label_num_bytes_seen_written` | `target.labels` | Merged  
`__file_write_event_label_open_duration` | `target.labels` | Merged  
`__file_write_event_label_open_time` | `target.labels` | Merged  
`__file_write_event_label_text_at_lowest_offset` | `target.labels` | Merged  
`__file_write_event_label_writes` | `target.labels` | Merged  
`__image_load_event_value_device_path_label` | `target.labels` | Merged  
`__reg_key_event_type_label` | `target.labels` | Merged  
`__reg_key_event_value_basesf_label` | `target.labels` | Merged  
`__source` | `target.labels` | Mapped values (13 total, e.g. `IOC` → `__file_write_event_label_writes`, `IOC` → `__file_wri...  
`__url_monitor_event_headers` | `target.labels` | Merged  
`event_type` | `target.labels` | Mapped: `regKeyEvent` → `__reg_key_event_value_basesf_label`, `regKeyEvent` → `__reg_key_eve...  
`event_values.__urlMethod` | `target.network.http.method` | Mapped when `__source` == `IOC`  
`event_values.__userAgent` | `target.network.http.user_agent` | Mapped when `__source` == `IOC`  
`event_values.__remotePort` | `target.port` | Renamed/mapped  
`event_values.__processCmdLine` | `target.process.command_line` | Mapped when `__source` == `IOC`  
`__process_full_path` | `target.process.file.full_path` | Mapped when `__source` == `IOC`  
`event_values.__fullPath` | `target.process.file.full_path` | Mapped when `__source` == `IOC`  
`event_values.__md5` | `target.process.file.md5` | Mapped when `__source` == `IOC`  
`__process` | `target.process.file.names` | Merged  
`__source` | `target.process.file.names` | Mapped: `IOC` → `__process`, `IOC` → `event_values.__fileName`  
`event_type` | `target.process.file.names` | Mapped: `processEvent` → `__process`, `imageLoadEvent` → `event_values.__fileName`  
`event_values.__fileName` | `target.process.file.names` | Merged  
`__parent_process_path` | `target.process.parent_process.file.full_path` | Mapped when `__source` == `IOC`  
`__source` | `target.process.parent_process.file.names` | Mapped: `IOC` → `event_values.__parentProcess`  
`event_type` | `target.process.parent_process.file.names` | Mapped: `processEvent` → `event_values.__parentProcess`  
`event_values.__parentProcess` | `target.process.parent_process.file.names` | Merged  
`__parent_pid` | `target.process.parent_process.pid` | Mapped when `__source` == `IOC`  
`__pid` | `target.process.pid` | Mapped when `__source` == `IOC`  
`__agent_id` | `target.process.product_specific_process_id` | Mapped when `__source` == `IOC`  
`__pid` | `target.process.product_specific_process_id` | Mapped when `__source` == `IOC`  
`event_values.__startTime` | `target.process.product_specific_process_id` | Mapped when `__source` == `IOC`  
`event_values.__path` | `target.registry.registry_key` | Mapped when `__source` == `IOC`  
`event_values.__text` | `target.registry.registry_value_data` | Mapped when `__source` == `IOC`  
`event_values.__value` | `target.registry.registry_value_data` | Mapped when `__source` == `IOC`  
`event_values.__valueName` | `target.registry.registry_value_name` | Mapped when `__source` == `IOC`  
`__reg_value_type` | `target.registry.registry_value_type` | Mapped when `__source` == `IOC`  
`event_values.__requestUrl` | `target.url` | Mapped when `__source` == `IOC`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trellix-hx-alerts-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

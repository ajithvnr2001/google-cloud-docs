---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/chrome-management-changelog/
title: Change log for CHROME_MANAGEMENT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:00:45.957316+00:00
---

# Change log for CHROME_MANAGEMENT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/chrome-management-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CHROME_MANAGEMENT

Date | Changes  
---|---  
2026-09-06 |  \- `target.url_metadata.title`: Newly mapped `TAB_TITLE` parameter raw log field with `target.url_metadata.title` UDM field for events `urlFilteringInterstitialEvent`.   
2026-08-31 |  \- `about.security_result.detection_fields[`referrer_risk`]`: Newly mapped `referrers.risk_level` raw log field with `about.security_result.detection_fields[`referrer_risk`]` UDM field for events `urlFilteringInterstitialEvent`.   
2026-07-20 |  \- Mapped `url_info` object raw log fields for events `sensitiveDataEvent`, `loginEvent`, `unscannedFileEvent`, `badNavigationEvent`.  
\- Mapped `tab_url_info` object raw log fields for events `sensitiveDataEvent`, `unscannedFileEvent`.  
\- Mapped `referrers` object raw log fields for events `sensitiveDataEvent`, `contentTransferEvent`, `dangerousDownloadEvent`, `urlFilteringInterstitialEvent`, `loginEvent`, `unscannedFileEvent`, `badNavigationEvent`.  
\- `security_result.threat_name`: Removed mapping of `url_info.risk_infos.threat_type` for `urlNavigationEvent` and `suspiciousUrlEvent` events in order to introduce a more accurate mapping.  
\- `principal.security_result.threat_name`: Newly mapped `url_info.risk_infos.threat_type` raw log field with `principal.security_result.threat_type` UDM field for events `urlNavigationEvent` and `suspiciousUrlEvent`.   
2026-06-18 |  \- target.resource.attribute.labels[`api_name`]: Newly mapped `telemetry_event_signals.api_name` raw log field with `target.resource.attribute.labels[`api_name`]` UDM field.  
\- target.resource.attribute.labels[`arg_url`]: Newly mapped `telemetry_event_signals.arg_url` raw log field with `target.resource.attribute.labels[`arg_url`]` UDM field.  
\- target.resource.attribute.labels[`args_list`]: Newly mapped `telemetry_event_signals.args_list` raw log field with `target.resource.attribute.labels[`args_list`]` UDM field.  
\- target.resource.attribute.labels[`timestamp_ms`]: Newly mapped `telemetry_event_signals.timestamp_ms` raw log field with `target.resource.attribute.labels[`timestamp_ms`]` UDM field.  
\- target.resource.attribute.labels[`access_type`]: Newly mapped `telemetry_event_signals.access_type` raw log field with `target.resource.attribute.labels[`access_type`]` UDM field.  
\- metadata.event_type: Newly set `event_type` to `USER_RESOURCE_ACCESS` if the `telemetry_event_signals.signal_name` is `DOM_ACCESS_INFO`.   
2026-05-12 |  \- security_result.category: Removed mapping of `security_result.category` for `extensionTelemetryEvent` events for accurate mapping.   
2025-11-11 |  \- target.user.email_addresses: Newly mapped `web_app_signed_in_account` raw log field with `target.user.email_addresses` UDM field for events: contentTransferEvent, sensitiveDataEvent, urlFilteringInterstitialEvent.   
2025-10-10 |  \- additional.fields: Newly mapped `content_transfer_method` raw log field with `additional.fields` UDM field for events: contentTransferEvent, malwareTransferEvent, sensitiveDataTransferEvent, sensitiveDataEvent.  
\- additional.fields: Newly mapped `server_scan_status` raw log field with `additional.fields` UDM field for events: malwareTransferEvent, sensitiveDataTransferEvent, sensitiveDataEvent.  
\- principal.ip: Newly mapped `local_ips` raw log field with `principal.ip` UDM field for events: browserCrashEvent, contentTransferEvent, dataAccessControlEvent, browserExtensionInstallEvent, extensionTelemetryEvent, loginEvent, malwareTransferEvent, passwordBreachEvent, passwordChangedEvent, passwordReuseEvent, sensitiveDataTransferEvent, suspiciousUrlEvent, badNavigationEvent, urlFilteringInterstitialEvent, urlNavigationEvent, sensitiveDataEvent.  
\- target.ip: Newly mapped `remote_ip` raw log field with `target.ip` UDM field for events: browserCrashEvent, dataAccessControlEvent, browserExtensionInstallEvent, extensionTelemetryEvent, loginEvent, malwareTransferEvent, passwordBreachEvent, passwordChangedEvent, passwordReuseEvent, sensitiveDataTransferEvent, badNavigationEvent, sensitiveDataEvent.  
\- about.url: Newly mapped `tab_url` raw log field with `about.url` UDM field for events: malwareTransferEvent, sensitiveDataTransferEvent, sensitiveDataEvent.  
\- about.asset_id: Newly mapped `agents.crowdstrike.agentId` raw log field with `about.asset_id` UDM field.  
\- about.resource.product_object_id: Newly mapped `agents.crowdstrike.customerId` raw log field with `about.resource.product_object_id` UDM field.  
\- Mappings specific to `contentTransferEvent`:  
\- security_result.rule_id: Newly mapped `matched_detectors.detector_id` raw log field with `security_result.rule_id` UDM field.  
\- security_result.rule_name: Newly mapped `matched_detectors.display_name` raw log field with `security_result.rule_name` UDM field.  
\- security_result.detection_fields[`detector_type`]: Newly mapped `matched_detectors.detector_type` raw log field with `security_result.detection_fields[`detector_type`]` UDM field.  
\- security_result.detection_fields[`mask_type`]: Newly mapped `matched_detectors.mask_type` raw log field with `security_result.detection_fields[`mask_type`]` UDM field.  
\- security_result.category: Newly set `security_result.category` to `DATA_EXFILTRATION` for the event `contentTransferEvent` when the `reason` field is `CONTENT_MATCHED_SENSITIVE_DATA_TYPES`.   
2025-08-14 |  \- principal.ip: Newly mapped `local_ips` raw log field with `principal.ip` UDM field for extensionTelemetryEvent event  
\- target.ip: Newly mapped `remote_ip` raw log field with `target.ip` UDM field for extensionTelemetryEvent event  
\- principal.asset.attribute.labels: Newly mapped `device_fqdn` raw log field with `principal.asset.attribute.labels` UDM field for extensionTelemetryEvent event  
\- principal.network.carrier_name: Newly mapped `network_name` raw log field with `principal.network.carrier_name` UDM field for extensionTelemetryEvent event  
\- about.ip: Removed mapping of `remote_ip` from `about.ip` UDM field for dangerousDownloadEvent, contentTransferEvent, urlNavigationEvent, suspiciousUrlEvent and urlFilteringInterstitialEvent event in order to introduce a more accurate mapping.  
\- target.ip: Mapped `remote_ip` raw log field with `target.ip` UDM field for dangerousDownloadEvent, contentTransferEvent, urlNavigationEvent, suspiciousUrlEvent and urlFilteringInterstitialEvent event  
\- about.domain.name: Removed mapping of `device_fqdn` from `about.domain.name` UDM field for urlNavigationEvent, suspiciousUrlEvent and urlFilteringInterstitialEvent event in order to introduce a more accurate mapping.  
\- principal.asset.attribute.labels: Mapped `device_fqdn` raw log field with `principal.asset.attribute.labels` UDM field for urlNavigationEvent, suspiciousUrlEvent and urlFilteringInterstitialEvent event   
2025-07-03 |  \- Mapped `security_result.action` as `ALLOW` if raw log field `event.result` contains `EVENT_RESULT_ALLOWED` and mapped `security_result.action` as `BLOCK` if raw log field `event.result` contains `EVENT_RESULT_BLOCKED`.   
2025-04-18 |  `urlNavigationEvent`,`suspiciousUrlEvent`, and `urlFilteringInterstitialEvent`: Added support for the event `urlNavigationEvent`,`suspiciousUrlEvent`,`urlFilteringInterstitialEvent` and relevant corresponding raw log fields.   
2025-04-04 |  `dangerousDownloadEvent`,`contentTransferEvent`: Added support for the event `dangerousDownloadEvent`,`contentTransferEvent` and relevant corresponding raw log fields.   
2024-10-11 |  \- Updated mappings `PROFILE_USER_NAME` field in Chrome Management to be consistent with Workspace activity `chrome` application logs.  
\- Updated mapping for `event.type`, `event.reason` and `device_user` fields.  
\- Added mapping for `TRIGGER_TYPE` and `VIRTUAL_DEVICE_ID` fields.   
2024-09-20 |  \- Added support of the new event type `extensionTelemetryEvent`.   
2024-03-13 |  \- Added support for the following fields in event `sensitiveDataEvent`: `transfer_method`.   
2024-02-28 |  \- Added support for the following fields in event `browserExtensionInstallEvent`: `extension_action`, `extension_version`, `extension_source`.   
2024-02-14 |  \- Updated event validation check for `USER_LOGIN` and `USER_RESOURCE_UPDATE_CONTENT` event types.   
2023-11-29 |  \- Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.   
2023-09-06 |  \- Updated the mapping of the `device_id` field from `principal.asset.asset_id` to `principal.asset.product_object_id`.   
2023-07-26 |  \- Updated the mapping of the `profile_user` field from `target.user.user_display_name` to `principal.user.email_addresses`.   
2023-07-12 |  \- Added support for the following fields in event `urlFilteringInterstitialEvent`: `clickedThrough`, `event_result`, `threat_type`, `triggered_rule_info.action`, `triggered_rule_info.rule_id`, `triggered_rule_info.rule_name`, and `triggered_rule_info.url_category`.   
2023-06-28 |  \- Promoted `CHROME_MANAGEMENT` parser to default.  
\- For the field mapping reference, see [https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chrome-management>Collect Chrome Management logs](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/<code).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

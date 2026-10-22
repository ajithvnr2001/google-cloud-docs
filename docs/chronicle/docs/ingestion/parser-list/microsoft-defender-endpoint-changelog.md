---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-endpoint-changelog/
title: Change log for MICROSOFT_DEFENDER_ENDPOINT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:37.561733+00:00
---

# Change log for MICROSOFT_DEFENDER_ENDPOINT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-endpoint-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MICROSOFT_DEFENDER_ENDPOINT

Date | Changes  
---|---  
2026-10-05 |  \- principal.asset.attribute.labels: Newly mapped `properties.MachineGroup` raw log field with `principal.asset.attribute.labels` UDM field for `AdvancedHunting-DeviceFileEvents`, `AdvancedHunting-DeviceLogonEvents`, `AdvancedHunting-DeviceNetworkEvents`, and `AdvancedHunting-DeviceProcessEvents` categories.   
2026-09-25 |  \- Added support for `IdentityDirectoryEvents` and `EntraIdSignInEvents` event categories.  
\- Added support for nested raw log fields from the `properties.AdditionalFields` raw log field. For details on the added fields, please refer to the parser documentation: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint#additional-fields-mapping  
\- Enhanced parsing logic and data validation across network, host, and user fields to ensure consistent UDM event normalization.   
2026-09-17 |  \- additional.fields: Newly mapped `properties.InitiatingProcessUniqueId` raw log field with `additional.fields` UDM field for `AdvancedHunting-DeviceEvents`, `AdvancedHunting-DeviceFileEvents`, `AdvancedHunting-DeviceImageLoadEvents`, `AdvancedHunting-DeviceLogonEvents`, `AdvancedHunting-DeviceNetworkEvents`, `AdvancedHunting-DeviceProcessEvents`, and `AdvancedHunting-DeviceRegistryEvents` categories.  
\- additional.fields: Newly mapped `properties.ProcessUniqueId` raw log field with `additional.fields` UDM field for `AdvancedHunting-DeviceEvents`, `AdvancedHunting-DeviceFileEvents`, `AdvancedHunting-DeviceImageLoadEvents`, `AdvancedHunting-DeviceLogonEvents`, `AdvancedHunting-DeviceNetworkEvents`, `AdvancedHunting-DeviceProcessEvents`, and `AdvancedHunting-DeviceRegistryEvents` categories.  
\- principal.asset.attribute.labels: Newly mapped `properties.MachineGroup` raw log field with `principal.asset.attribute.labels` UDM field for `AdvancedHunting-DeviceEvents` category.   
2026-08-07 |  \- Added support for nested raw log fields from `properties.AdditionalFields` raw log field for `AdvancedHunting-DeviceEvents` category and `AdvancedHunting-AlertEvidence` category (for `EntityType` value `Process`).  
\- Please refer to the parser documentation page for information regarding the added nested raw log fields - https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint#additional-fields-mapping   
2026-08-04 |  \- principal.user.email_addresses: Enhanced email address mappings for RawEventData raw log field with standard syntax and length validation  
\- principal.user.attribute.labels: Enhanced mapping for extended or non-standard email addresses to `principal.user.attribute.labels` to preserve telemetry fidelity   
2026-07-29 |  \- security_result.action: Mapped `properties.ActionType` raw log field values (`LogonSuccess`, `LogonFailed`, `LogonAttempted`) to `security_result.action` UDM field (`ALLOW` / `FAIL`) for `AdvancedHunting-DeviceLogonEvents` category.   
2026-06-03 |  \- additional.fields: Newly mapped `properties.EmailDirection` raw log field with `additional.fields` UDM field as a part of fallback logic for `AdvancedHunting-EmailEvents` category  
\- network.email.to: Newly mapped `properties.DistributionList` raw log field with `network.email.to` UDM field for `AdvancedHunting-EmailEvents` category  
\- additional.fields: Newly mapped `properties.DistributionList` raw log field with `additional.fields` UDM field if `properties.DistributionList` is not mapped to `network.email.to` due to any invalid email format (eg: exceeds 255 characters) for `AdvancedHunting-EmailEvents` category.  
\- additional.fields: Newly mapped `properties.IsClickedThrough` raw log field with `additional.fields` UDM field for `AdvancedHunting-UrlClickEvents` category  
\- principal.resource.attribute.labels: Newly mapped `properties.Workload` and ``properties.AppVersion`` raw log field with `principal.resource.attribute.labels` UDM field for `AdvancedHunting-UrlClickEvents` category  
\- principal.application: Newly mapped `properties.AppName` raw log field with `principal.application` UDM field for `AdvancedHunting-UrlClickEvents` category  
\- security_result.category: Newly mapped `properties.ThreatTypes` raw log field with values like `Malware` and `Spam` with `security_result.category` UDM field to add support for `AdvancedHunting-EmailAttachmentInfo`, `AdvancedHunting-EmailEvents` and `AdvancedHunting-EmailPostDeliveryEvents`.   
2026-04-23 |  \- Updated the field mapping for the MICROSOFT_DEFENDER_ENDPOINT parser.  
\- Please refer to the parser documentation page for information regarding the updated UDM mappings - https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint#udm-mapping-delta   
2025-12-05 |  \- Enhanced the parser logic to handle the edge cases of `properties.SenderFromAddress` and `properties.RecipientEmailAddress` raw log fields for events `AdvancedHunting-EmailAttachmentInfo` and `AdvancedHunting-EmailEvents`. When the `properties.SenderFromAddress` and `properties.RecipientEmailAddress` raw log fields exceeds 255 characters, it will now be mapped to `additional.fields` UDM field.   
2025-11-26 |  \- Enhanced the parser logic to handle the edge cases of `properties.OSDistribution` raw field.   
2025-10-31 |  \- Enhanced the parser logic to handle the edge cases of `properties.IsAccountEnabled` raw field.   
2025-08-07 |  Updated following field mappings in `DeviceLogonEvents` Events:  
\- target.ip: Removed mapping of `properties.RemoteIP` from `target.ip` UDM field.  
\- principal.ip: Mapped `properties.RemoteIP` raw log field with `principal.ip` UDM field.  
\- target.hostname: Removed mapping of `properties.RemoteDeviceName` from `target.hostname` UDM field.  
\- principal.hostname: Mapped `properties.RemoteDeviceName` raw log field with `principal.hostname` UDM field.  
\- target.port: Removed mapping of `properties.RemotePort` from `target.port` UDM field.  
\- principal.port: Mapped `properties.RemotePort` raw log field with `principal.port` UDM field.  
\- principal.hostname: Removed mapping of `properties.DeviceName` from `principal.hostname` UDM field.  
\- target.hostname: Mapped `properties.DeviceName` raw log field with `target.hostname` UDM field.  
\- principal.asset_id: Removed mapping of `properties.DeviceId from `principal.asset_id` UDM field.  
\- target.asset_id: Mapped `properties.DeviceId` raw log field with `target.asset_id` UDM field.   
2025-08-06 |   
2025-05-30 |  Added new grok pattern to map the following fields:  
\- principal.ip: Newly mapped `properties.LocalIP` raw log field with `principal.ip` UDM field.  
\- target.ip: Newly mapped `properties.RemoteIP` raw log field with `target.ip` UDM field.   
2025-05-22 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `ForwardTo` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field  
\- `USER_UNCATEGORIZED`: Added support for the event `USER_UNCATEGORIZED` and relevant corresponding raw log fields.   
2025-05-13 |  \- target.process.product_specific_process_id: Removed mapping of `properties.ProcessUniqueId` from `target.process.product_specific_process_id` UDM field.  
\- principal.process.product_specific_process_id: Removed mapping of `properties.InitiatingProcessUniqueId` from `target.process.product_specific_process_id` UDM field.   
2025-03-27 |  \- Promoted the parser to default.  
\- This version includes many changes to improve the parser mappings (parser overhaul) - contact your Google representative to get a detailed list with all changes  
\- This version will have an extended RC period - we encourage you to opt-in and make the required adjustments before it'll be automatically promoted to Default   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

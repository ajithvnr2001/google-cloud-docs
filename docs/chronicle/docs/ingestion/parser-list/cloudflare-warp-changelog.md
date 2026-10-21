---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-warp-changelog/
title: Change log for CLOUDFLARE_WARP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:55:56.552268+00:00
---

# Change log for CLOUDFLARE_WARP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-warp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CLOUDFLARE_WARP

Date | Changes  
---|---  
2026-05-04 |  Enhancement:  
\- `event.idm.read_only_udm.principal.url`: Removed mapping of `URL` from `event.idm.read_only_udm.principal.url`. As it was incorrectly mapped.  
\- `event.idm.read_only_udm.target.url`: Mapped `URL` raw log field with `event.idm.read_only_udm.target.url`.  
\- `event.idm.read_only_udm.target.file.size`: Added a conditional check before already existing mapping of `BlockedFileSize` to `event.idm.read_only_udm.target.file.size`.   
2026-04-08 |  Enhancement:  
\- `event.idm.read_only_udm.target.administrative_domain`: Removed mapping of `HTTPHost` from `event.idm.read_only_udm.target.administrative_domain`. Since this field represents a hostname and not a domain name.  
\- `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname`: Mapped `HTTPHost` raw log field to `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname`.   
2026-03-11 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP` when `HTTPMethod` is not `UNKNOWN`.  
\- `event.idm.read_only_udm.security_result.action`: Mapped `ALLOW` to `event.idm.read_only_udm.security_result when `Action` raw log field is `Bypass`.   
2026-02-16 |  Enhancement:  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `Referer` raw log field to `event.idm.read_only_udm.network.http.referral_url`.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `BlockedFileHash` raw log field to `event.idm.read_only_udm.target.file.sha256`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `Email` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- `event.idm.read_only_udm.principal.file.names`: Newly mapped `BlockedFileName` raw log field to `event.idm.read_only_udm.principal.file.names`.  
\- `event.idm.read_only_udm.target.file.size`: Newly mapped `BlockedFileSize` raw log field to `event.idm.read_only_udm.target.file.size`.  
\- `event.idm.read_only_udm.network.http.referral_url`: Removed mapping of `HTTPHost` from `event.idm.read_only_udm.network.http.referral_url`. Since this field represents a domain name, it is not a valid value for this field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Mapped `HTTPHost` raw log field to `event.idm.read_only_udm.target.administrative_domain`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `BlockedFileType` from `event.idm.read_only_udm.additional.fields`. Since this field has file details, it can be mapped to `event.idm.read_only_udm.target.file.mime_type`.  
\- `event.idm.read_only_udm.target.file.mime_type`: Mapped `BlockedFileType` raw log field to `event.idm.read_only_udm.target.file.mime_type`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `BlockedFileReason` from `event.idm.read_only_udm.additional.fields`. Since this field has event action details, it can be mapped to `event.idm.read_only_udm.security_result.action_details`.  
\- `event.idm.read_only_udm.security_result.action_details`: Mapped `BlockedFileReason` raw log field to `event.idm.read_only_udm.security_result.action_details`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `DownloadMatchedDlpProfiles`, `UploadMatchedDlpProfileEntries`, `DownloadMatchedDlpProfileEntries` and `UploadMatchedDlpProfiles`to `event.idm.read_only_udm.additional.fields`.  
\- Updated mappings for `CategoryIDs` and `CategoryNames` to use indexed keys (e.g., `CategoryIDs_0`, `CategoryNames_0`).   
2026-02-12 |  Enhancement:  
\- Mapped FileInfo.files array directly to the `event.idm.read_only_udm.intermediary` repeated field within a single event to avoid multiple events due to this following fields were removed:  
\- `event.idm.read_only_udm.metadata.event_type`: Removed `event.idm.read_only_udm.metadata.event_type` as we removed multiple events mapping for single log.  
\- `event.idm.read_only_udm.metadata.log_type`: Removed `event.idm.read_only_udm.metadata.log_type` as we removed multiple events mapping for single log.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Removed `event.idm.read_only_udm.metadata.event_timestamp` as we removed multiple events mapping for single log.  
\- `event.idm.read_only_udm.principal.file.sha256`: Removed mapping of `FileInfo.files.file_hash` from `event.idm.read_only_udm.principal.file.sha256` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.principal.file.size`: Removed mapping of `FileInfo.files.file_size` from `event.idm.read_only_udm.principal.file.size` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.principal.file.full_path`: Removed mapping of `FileInfo.files.file_name` from `event.idm.read_only_udm.principal.file.full_path` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.principal.file.mime_type`: Removed mapping of `FileInfo.files.content_type` from `event.idm.read_only_udm.principal.file.mime_type` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `FileInfo.files.direction` from `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.security_result.action_details` and `event.idm.read_only_udm.security_result.action`: Removed mapping of `FileInfo.files.action` from `event.idm.read_only_udm.security_result.action_details` and `event.idm.read_only_udm.security_result.action` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.intermediary.file.sha256`: Newly mapped `FileInfo.files.file_hash` raw log field with `event.idm.read_only_udm.intermediary.file.sha256` UDM field.  
\- `event.idm.read_only_udm.intermediary.file.size`: Newly mapped `FileInfo.files.file_size` raw log field with `event.idm.read_only_udm.intermediary.file.size` UDM field.  
\- `event.idm.read_only_udm.intermediary.file.full_path`: Newly mapped `FileInfo.files.file_name` raw log field with `event.idm.read_only_udm.intermediary.file.full_path` UDM field.  
\- `event.idm.read_only_udm.intermediary.file.mime_type`: Newly mapped `FileInfo.files.content_type` raw log field with `event.idm.read_only_udm.intermediary.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.intermediary.resource.attribute.labels`: Newly mapped `FileInfo.files.direction` raw log field with `event.idm.read_only_udm.intermediary.resource.attribute.labels` UDM field (key: `file direction`).  
\- `event.idm.read_only_udm.intermediary.resource.attribute.labels`: Newly mapped `FileInfo.files.action` raw log field with `event.idm.read_only_udm.intermediary.resource.attribute.labels` UDM field (key: `file action`).  
\- `event.idm.read_only_udm.security_result.action`: Updated condition for raw field Action: Added `allow` to the list of values (now [`allowedByRule`, `authenticate`, `allow`]) that map to `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `RegistrationID`, `DownloadedFileNames`, `UploadedFileNames` raw log fields with event.idm.read_only_udm.additional.fields UDM field.   
2025-10-29 |  Enhancement:  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `HTTPHost` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.src.ip: Newly mapped `SourceInternalIP` raw log field with `event.idm.read_only_udm.src.ip` UDM field.  
\- event.idm.read_only_udm.src.asset.ip: Newly mapped `SourceInternalIP` raw log field with `event.idm.read_only_udm.src.asset.ip` UDM field.  
\- event.idm.read_only_udm.network.dhcp.client_hostname: Newly mapped `VirtualNetworkName` raw log field with `event.idm.read_only_udm.network.dhcp.client_hostname` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `DestinationIPContinentCode` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `SourceIPContinentCode` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ForensicCopyStatus` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `IsIsolated` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Quarantined` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `UntrustedCertificateAction` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `RequestID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.file.sha256: Newly mapped `file_hash` raw log field with `event.idm.read_only_udm.principal.file.sha256` UDM field.  
\- event.idm.read_only_udm.principal.file.size: Newly mapped `file_size` raw log field with `event.idm.read_only_udm.principal.file.size` UDM field.  
\- event.idm.read_only_udm.principal.file.full_path: Newly mapped `file_name` raw log field with `event.idm.read_only_udm.principal.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `file_direction` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.file.mime_type: Newly mapped `file_type` raw log field with `event.idm.read_only_udm.principal.file.mime_type` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `file_action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `file_action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `applicationstatuses` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `applicationids` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `applicationnames` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-02-02 |  Enhancement:  
\- Added support for new set of JSON logs.   
2024-12-18 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

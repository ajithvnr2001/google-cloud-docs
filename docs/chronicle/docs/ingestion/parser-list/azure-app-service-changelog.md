---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-app-service-changelog/
title: Change log for AZURE_APP_SERVICE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:51:18.551694+00:00
---

# Change log for AZURE_APP_SERVICE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-app-service-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_APP_SERVICE

Date | Changes  
---|---  
2026-08-24 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `http_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `request_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `http_version` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `res_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `bytes_sent` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `backend_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `backend_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `http_user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `containerId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `EventOsInstanceId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added uppercase function on `severity` field.   
2024-10-18 |  Enhancement:  
\- Mapped `properties.XForwardedHost` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `properties_category` to `additional.fields`.  
\- Mapped `properties.roleInstance` to `principal.resource.product_object_id`.  
\- Mapped `properties.message` to `security_result.summary`.   
2024-09-30 |  Enhancement:  
\- Added support to parse the new format of unparsed JSON logs.   
2024-06-24 |  Enhancement:  
\- Mapped `metadata.product_name` and `metadata.vendor_name` to `AZURE_APP_SERVICE`.   
2024-06-07 |  Enhancement:  
\- Added support for JSON logs, when they are not in an array format.  
\- Mapped `properties.ScSubStatus` to `additional.fields`.  
\- Mapped `properties.ScWin32Status` to `additional.fields`.   
2024-04-25 |  Enhancement:  
\- Mapped `properties.User` to `principal.user.userid`.  
\- Mapped `properties.UserDisplayName` to `principal.user.user_display_name`.  
\- Mapped `properties.UserAddress` to `principal.ip`.  
\- Mapped `properties.Protocol`, `ClientBrowser`, `ClientModel`, `ClientOS`, `OperationId`, `ParentId`, and `ItemCount` to `additional.fields`.  
\- Mapped `CsUriQuery`, `SDKVersion`, and `Cookie` to `principal.resource.attribute.labels`.  
\- Mapped `SessionId` to `network.session_id`.  
\- Mapped `Message` to `security_result.summary`.  
\- Mapped `SeverityLevel` to `security_result.severity_details`.   
2024-02-20 |  Enhancement:  
\- Mapped `record.AppRoleInstance` to `principal.resource.product_object_id`.  
\- Mapped `record.AppRoleName` to `principal.resource.name`.  
\- Mapped `record.ClientCity` to `principal.location.city`.  
\- Mapped `record.ClientCountryOrRegion` to `principal.location.country_or_region`.  
\- Mapped `record.ClientStateOrProvince` to `principal.location.state`.  
\- Mapped `record.ClientIP` to `principal.ip`.  
\- Mapped `Result` to `security_result.summary`.  
\- Mapped `UserAgent` to `network.http.user_agent`.  
\- Mapped `Referer` to `network.http.referral_url`.  
\- Mapped `record.ResourceGUID` to `target.resource.product_object_id`.  
\- If `record.ResourceGUID` is not present, then mapped `record.resourceId` to `target.resource.product_object_id`.  
\- If `record.ResourceGUID` is present, then mapped `record.resourceId` to `additional.fields`.  
\- Mapped `record.Type` to `additional.fields`.  
\- Mapped `record.ClientType` to `additional.fields`.  
\- Mapped `record.SDKVersion` to `additional.fields`.  
\- Mapped `record.Name` to `additional.fields`.  
\- Mapped `record.Instance` to `additional.fields`.  
\- Mapped `record.TimeTaken` to `additional.fields`.  
\- Mapped `record.Cookie` to `additional.fields`.  
\- Mapped `record.AppVersion` to `principal.resource.attribute.labels`.  
\- Mapped `record.IKey` to `target.resource.attribute.labels`.  
\- Mapped `record.Category` to `metadata.product_event_type`.  
\- Mapped `CsUriStem` to `target.url`.  
\- Changed mapping of `CsBytes` from `network.received_bytes` to `network.sent_bytes`.  
\- Changed mapping of `ScBytes` from `network.sent_bytes` to `network.received_bytes`.   
2023-12-07 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

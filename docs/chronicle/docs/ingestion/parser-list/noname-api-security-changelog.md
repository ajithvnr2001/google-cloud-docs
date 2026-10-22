---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/noname-api-security-changelog/
title: Change log for NONAME_API_SECURITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:37.219048+00:00
---

# Change log for NONAME_API_SECURITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/noname-api-security-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NONAME_API_SECURITY

Date | Changes  
---|---  
2026-05-21 |  \- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `data.date` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.target.user.product_object_id: Newly mapped `data.rowData.user.id` raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped `data.email` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `data.username` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.user.attribute.roles: Newly mapped `data.role` raw log field with `event.idm.read_only_udm.target.user.attribute.roles` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `data.rowData.actionName` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `data.rowData.actionTitle` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `data.eventId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `data.suspiciousValue` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip: Newly mapped `data.ips` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `dst_host` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `data.action`, `data.rowData.user.role`, `data.rowData.user.email`, `data.rowId`, `data.rowData.user.username`, `data.suspiciousValueLocation`, `data.attackType` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` as log contains both `target` data and `principal` or `target` user and machine data.  
\- `event.idm.read_only_udm.extensions.auth.type`: Mapped `event.idm.read_only_udm.extensions.auth.type` to `AUTHTYPE_UNSPECIFIED`, if `rowData_actionName` raw log field contains `login` related data.   
2026-04-23 |  \- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `syslog_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `data.typeId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `data.responseCodes` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `data.countries` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `data.url` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `data.investigate` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.confidence_details`: Newly mapped `data.attackerConfidence` raw log field with `event.idm.read_only_udm.security_result.confidence_details` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `data.remediation` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `data.attackerIdentifier` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields if `data_attackerIdentifier` is a valid IP.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `data.attackerIdentifier` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields if `data_attackerIdentifier` is a valid hostname.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `data.detectionTime` , `data.triggeredOn` ,`data.attackResult` ,`data.vulnerabilityFrameworkTags` ,`data.owaspTags` , and `data.attackerIdentifier` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.last_updated_time`: Newly mapped `data.updatedAt` raw log field with `event.idm.read_only_udm.security_result.last_updated_time` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `data.impact` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `data.title` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: If `severity` is `Info`, updated the value of `event.idm.read_only_udm.security_result.severity` to `LOW`.  
\- `event.idm.read_only_udm.security_result.confidence`: If `data_attackerConfidence` is > 80, updated the value of `event.idm.read_only_udm.security_result.confidence` to `HIGH_CONFIDENCE`.  
\- `event.idm.read_only_udm.security_result.confidence`: If `data_attackerConfidence` is > 50, updated the value of `event.idm.read_only_udm.security_result.confidence` to `MEDIUM_CONFIDENCE`.  
\- `event.idm.read_only_udm.security_result.confidence`: If `data_attackerConfidence` is <= 50, updated the value of `event.idm.read_only_udm.security_result.confidence` to `LOW_CONFIDENCE`.  
\- Added a grok pattern on `data_attackerIdentifier` to extract `data_attackerIdentifier_ip` and `data_attackerIdentifier_host`.   
2025-04-17 |  \- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `APIInformation.accountId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.resource.id`: Newly mapped `attacker.id` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `attacker.identifier` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.type`: Newly mapped `attacker.identifierType` raw log field with `event.idm.read_only_udm.principal.resource.type` UDM field.  
\- `event.idm.read_only_udm.security_result.confidence_details`: Newly mapped `attacker.confidence` raw log field with `event.idm.read_only_udm.security_result.confidence_details` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `attacker.IP` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `attacker.IP` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `createdAt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `link` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `module` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `status` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `type` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `lastActivity` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Newly mapped `APIInformation.apiType` raw log field with `event.idm.read_only_udm.target.resource.resource_type` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped `APIInformation.auth` raw log field with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `APIInformation.internetAccessed` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `APIInformation.internetFacing` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `APIInformation.owner` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `APIInformation.resourceGroupName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `APIInformation.source` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.path`: Newly mapped `path` raw log field with `event.idm.read_only_udm.network.http.path` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `triggeredOn` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `apiAirids` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.destinationIp` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.host` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.method` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.path` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.requestTs` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.statusCode` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestBody.pharmas` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestBody.drugName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestBody.prescriberStates` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestBody.prescriberCities` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestBody.prescriberIds` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestBody.prescriberZips` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestBody.formularies` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestBody.startDate` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestBody.endDate` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestBody.prescriberTaxonomyCodes` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.x-forwarded-for` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.content-length` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.accept` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.host` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.user-agent` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.content-type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.header.typ` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.header.alg` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.header.x5t` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.header.kid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.aud` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.iss` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.iat` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.nbf` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.exp` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.aio` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.appid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.appidacr` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.idp` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.oid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.rh` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.roles` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.sub` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.tid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.uti` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.requestHeaders.authorization.jwt.payload.ver` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.responseBody` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.responseHeaders.x-custom-header` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.responseHeaders.user-agent` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.responseHeaders.host` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.responseHeaders.correlationid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.sample.responseHeaders.content-type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `evidence.sourceIp` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `evidence.sourceIp` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `evidence.statusCode` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2024-06-08 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

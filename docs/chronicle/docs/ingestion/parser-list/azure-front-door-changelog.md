---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-front-door-changelog/
title: Change log for AZURE_FRONT_DOOR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:13:24.111016+00:00
---

# Change log for AZURE_FRONT_DOOR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-front-door-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_FRONT_DOOR

Date | Changes  
---|---  
2026-04-16 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `properties.domain` from `event.idm.read_only_udm.additional.fields` UDM field, when this field contains both domain and port, to allow mapping to more specific UDM fields.  
\- `event.idm.read_only_udm.target.domain.name`: Newly mapped `target_domain` raw log field with `event.idm.read_only_udm.target.domain.name` UDM field, as this represents the correct UDM field for the extracted domain name.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `target_port` raw log field with `event.idm.read_only_udm.target.port` UDM field, as this represents the correct UDM field for the extracted port.  
\- Added a grok pattern on `properties.domain` to extract `target_domain` and `target_port`. This is suitable as `properties.domain` often contains both the domain name and sometimes the port.   
2026-03-31 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname`,`event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `properties.hostName` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field as it represents the destination host.  
\- `event.idm.read_only_udm.target.hostname`,`event.idm.read_only_udm.target.asset.hostname`: Mapped `properties.hostName` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field when `properties.hostName` raw log field is not in ["",n/a,N/A].  
\- `event.idm.read_only_udm.principal.url`: Removed mapping of `properties.requestUri` from `event.idm.read_only_udm.principal.url` UDM field as it represents a resource attribute rather than a primary URL.  
\- `event.idm.read_only_udm.target.url`: Removed mapping of `properties.requestUri` from `event.idm.read_only_udm.target.url` UDM field as it represents a resource attribute rather than a primary URL.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `properties.requestUri` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field when `properties.requestUri` raw log field is not in ["",n/a,N/A].  
\- `event.idm.read_only_udm.target.hostname`,`event.idm.read_only_udm.target.asset.hostname`: Removed mapping of `properties.originName` from `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field when `properties.originName` raw log field as it represents an internal backend server rather than a target hostname.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.originName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when `properties.originName` raw log field is not in ["",n/a,N/A].  
\- `event.idm.read_only_udm.target.url`: Mapped `properties.originUrl` raw log field with `event.idm.read_only_udm.target.url` UDM field when `properties.originUrl` raw log field is not in ["",n/a,N/A].   
2026-02-10 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname`,`event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `properties.hostName` from `event.idm.read_only_udm.principal.hostname`,`event.idm.read_only_udm.principal.asset.hostname` UDM field when `properties.originName` raw-log field is in ["",n/a,N/A] because it represents the destination host when origin details are not present.  
\- `event.idm.read_only_udm.target.hostname`,`event.idm.read_only_udm.target.asset.hostname`: Mapped `properties.hostName` raw log field with `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname` UDM field when `properties.originName` raw-log field is in ["",n/a,N/A].  
\- `event.idm.read_only_udm.target.hostname`,`event.idm.read_only_udm.target.asset.hostname`: Mapped `properties.originName` raw log field with `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname` UDM field when `properties.originName` raw-log field is not in ["",n/a,N/A].  
\- `event.idm.read_only_udm.principal.hostname`,`event.idm.read_only_udm.principal.asset.hostname`: Mapped `properties.hostName` raw log field with `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` UDM field when `properties.originName` raw-log field is not in ["",n/a,N/A].  
\- `event.idm.read_only_udm.principal.url`: Removed mapping of `properties.requestUri` raw log field with `event.idm.read_only_udm.principal.url` UDM field when `properties.originUrl` raw-log field is in ["",n/a,N/A] because it represents the destination URL when origin details are not present.  
\- `event.idm.read_only_udm.target.url`: Mapped `properties.requestUri` raw log field with `event.idm.read_only_udm.target.url` UDM field when `properties.originUrl` raw-log field is in ["",n/a,N/A].  
\- `event.idm.read_only_udm.target.url`: Mapped `properties.originUrl` raw log field with `event.idm.read_only_udm.target.url` UDM field when `properties.originUrl` raw-log field is not in ["",n/a,N/A].  
\- `event.idm.read_only_udm.principal.url`: Mapped `properties.requestUri` raw log field with `event.idm.read_only_udm.principal.url` UDM field when `properties.originUrl` raw-log field is not in ["",n/a,N/A].   
2026-01-07 |  Enhancement:  
\- `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `properties.socketIp`,`properties.socketIP` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field since SocketIp in Azure Front Door logs represents the IP address of the device or service, such as a proxy or load balancer, that is connected directly to the Azure edge, not necessarily the original client IP.  
\- `event.idm.read_only_udm.observer.ip`, `event.idm.read_only_udm.observer.asset.ip`: Mapped `properties.socketIp`,`properties.socketIP` raw log field with `event.idm.read_only_udm.observer.ip` and `event.idm.read_only_udm.observer.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `properties.httpStatusDetails`,`properties.originCryptProtocol`,`properties.originCryptCipher`, raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a conditional check so that the `properties.originName` raw log field is mapped to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` only if its value is not `n/a`, `N/A`, or an empty string.  
\- Added a conditional check so that the `properties.originUrl` raw log field is mapped to `event.idm.read_only_udm.target.url` only if its value is not `n/a`, `N/A`, or an empty string.   
2026-01-01 |  Enhancement:  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Removed mapping of `properties.host` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field because it is the destination of the web request, not the source.  
\- event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname: Mapped `properties.host` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `properties.ruleName` raw log field(s) with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Tag`, `onbehalfServiceId` raw log field(s) with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `onBehalfFields`, `priority`, `primaryPartitionField`, `containerSuffix`, `validJsonColumns`, `excludeFields` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- A key-value filter was added to parse the onbehalfAnnotations field, extracting nested fields for further processing.   
2025-08-06 |  Enhancement:  
event.idm.read_only_udm.principal.ip: Removed mapping of origin_ip from event.idm.read_only_udm.principal.ip UDM field which is the IP address of the entity that is the target of the action or event.  
event.idm.read_only_udm.target.ip: Mapped origin_ip raw log field to event.idm.read_only_udm.target.ip UDM field.  
event.idm.read_only_udm.principal.asset.ip: Removed mapping of origin_ip from event.idm.read_only_udm.principal.asset.ip UDM field which is the IP address of the entity that is the target of the action or event.  
event.idm.read_only_udm.target.asset.ip: Mapped origin_ip raw log field to event.idm.read_only_udm.target.asset.ip UDM field.  
event.idm.read_only_udm.target.url: Removed mapping of properties.requestUri from event.idm.read_only_udm.target.url UDM field because requestUri should be associated with the principal that made the request.  
event.idm.read_only_udm.principal.url: Mapped properties.requestUri raw log field to event.idm.read_only_udm.principal.url UDM field.  
event.idm.read_only_udm.target.resource.product_object_id: Removed mapping of resourceId from event.idm.read_only_udm.target.resource.product_object_id UDM field because this field is for a vendor-specific identifier for the target resource. It is not for a generic ID.  
event.idm.read_only_udm.target.resource.id: Mapped resourceId raw log field to event.idm.read_only_udm.target.resource.id UDM field.  
event.idm.read_only_udm.additional.fields: Removed mapping of operationName from event.idm.read_only_udm.additional.fields UDM field because operationName is a string that represents a specific operation or action that occurred on the Azure Front Door.  
event.idm.read_only_udm.metadata.description: Mapped operationName raw log field to event.idm.read_only_udm.metadata.description UDM field.  
event.idm.read_only_udm.metadata.vendor_name: Newly mapped `Microsoft` static value to event.idm.read_only_udm.metadata.vendor_name UDM field.  
event.idm.read_only_udm.metadata.product_name: Newly mapped `Azure Front Door` static value to event.idm.read_only_udm.metadata.product_name UDM field.  
event.idm.read_only_udm.metadata.product_log_id: Newly mapped properties.trackingReference raw log field to event.idm.read_only_udm.metadata.product_log_id UDM field.  
event.idm.read_only_udm.network.application_protocol: Newly mapped properties.requestProtocol raw log field to event.idm.read_only_udm.network.application_protocol UDM field.  
event.idm.read_only_udm.network.http.method: Newly mapped properties.httpMethod raw log field to event.idm.read_only_udm.network.http.method UDM field.  
event.idm.read_only_udm.network.http.response_code: Newly mapped properties.httpStatusCode raw log field to event.idm.read_only_udm.network.http.response_code UDM field.  
event.idm.read_only_udm.network.received_bytes: Newly mapped properties.responseBytes raw log field to event.idm.read_only_udm.network.received_bytes UDM field.  
event.idm.read_only_udm.network.sent_bytes: Newly mapped properties.requestBytes raw log field to event.idm.read_only_udm.network.sent_bytes UDM field.  
event.idm.read_only_udm.network.tls.version_protocol: Newly mapped properties.securityProtocol raw log field to event.idm.read_only_udm.network.tls.version_protocol UDM field.  
event.idm.read_only_udm.principal.location.country_or_region: Newly mapped properties.clientCountry raw log field to event.idm.read_only_udm.principal.location.country_or_region UDM field.  
event.idm.read_only_udm.principal.hostname: Newly mapped properties.hostName raw log field to event.idm.read_only_udm.principal.hostname UDM field.  
event.idm.read_only_udm.principal.asset.hostname: Newly mapped properties.hostName raw log field to event.idm.read_only_udm.principal.asset.hostname UDM field.  
event.idm.read_only_udm.security_result.action_details: Newly mapped properties.ErrorInfo raw log field to event.idm.read_only_udm.security_result.action_details UDM field.  
event.idm.read_only_udm.security_result.rule_name: Newly mapped properties.routingRuleName raw log field to event.idm.read_only_udm.security_result.rule_name UDM field.  
event.idm.read_only_udm.target.hostname: Newly mapped properties.originName raw log field to event.idm.read_only_udm.target.hostname UDM field.  
event.idm.read_only_udm.target.asset.hostname: Newly mapped properties.originName raw log field to event.idm.read_only_udm.target.asset.hostname UDM field.  
event.idm.read_only_udm.target.url: Newly mapped properties.originUrl raw log field to event.idm.read_only_udm.target.url UDM field.  
event.idm.read_only_udm.security_result.action: Newly mapped sec_result_action raw log field to event.idm.read_only_udm.security_result.action UDM field.  
event.idm.read_only_udm.network.application_protocol_version: Newly mapped properties.httpVersion raw log field to event.idm.read_only_udm.network.application_protocol_version UDM field.  
event.idm.read_only_udm.network.tls.client.server_name: Newly mapped properties.sni raw log field to event.idm.read_only_udm.network.tls.client.server_name UDM field.  
event.idm.read_only_udm.network.http.user_agent: Newly mapped properties.userAgent raw log field to event.idm.read_only_udm.network.http.user_agent UDM field.  
event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped properties.userAgent raw log field to event.idm.read_only_udm.network.http.parsed_user_agent UDM field.  
event.idm.read_only_udm.network.http.referral_url: Newly mapped properties.referer raw log field to event.idm.read_only_udm.network.http.referral_url UDM field.  
event.idm.read_only_udm.network.tls.cipher: Newly mapped properties.securityCipher raw log field to event.idm.read_only_udm.network.tls.cipher UDM field.  
event.idm.read_only_udm.network.tls.curve: Newly mapped properties.securityCurves raw log field to event.idm.read_only_udm.network.tls.curve UDM field.  
event.idm.read_only_udm.intermediary.hostname: Newly mapped properties.endpoint raw log field to event.idm.read_only_udm.intermediary.hostname UDM field.  
event.idm.read_only_udm.additional.fields: Newly mapped properties.cacheStatus, properties.domain, properties.timeToFirstByte, properties.timeTaken, properties.edgeActionsStatusCode, and properties.pop raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
event.idm.read_only_udm.security_result.detection_fields: Newly mapped properties.result and properties.clientJA4FingerPrint raw log fields with event.idm.read_only_udm.security_result.detection_fields UDM field.   
2024-12-13 |  Created new parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

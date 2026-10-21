---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-apigee-changelog/
title: Change log for GCP_APIGEE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:47:27.738028+00:00
---

# Change log for GCP_APIGEE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-apigee-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_APIGEE

Date | Changes  
---|---  
2026-09-30 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `jsonPayload.client_ip` and `jsonPayload.true_client_ip` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields  
\- event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname: Newly mapped `jsonPayload.host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` and `receiveTimestamp` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `jsonPayload.status` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `jsonPayload.response_bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `jsonPayload.env` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `insertId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `jsonPayload.country` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field  
\- event.idm.read_only_udm.target.url: Newly mapped `jsonPayload.path` raw log field with `event.idm.read_only_udm.target.url` UDM field  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `jsonPayload.target` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field  
\- event.idm.read_only_udm.intermediary.resource.name: Newly mapped `jsonPayload.proxy` raw log field with `event.idm.read_only_udm.intermediary.resource.name` UDM field  
\- event.idm.read_only_udm.intermediary.administrative_domain: Newly mapped `jsonPayload.org` raw log field with `event.idm.read_only_udm.intermediary.administrative_domain` UDM field  
\- event.idm.read_only_udm.network.http.method: Newly mapped `jsonPayload.method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `jsonPayload.user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `jsonPayload.referer_origin` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field  
\- event.idm.read_only_udm.network.session_id: Newly mapped `jsonPayload.request_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field  
\- event.idm.read_only_udm.target.resource.attribute.cloud.project.id: Newly mapped `resource.labels.project_id` raw log field with `event.idm.read_only_udm.target.resource.attribute.cloud.project.id` UDM field  
\- event.idm.read_only_udm.additional.fields: Newly mapped `logName`, `resource.type`, `jsonPayload.backend`, `jsonPayload.cf_ray`, `jsonPayload.channel`, `jsonPayload.fault`, `jsonPayload.path_template`, `jsonPayload.proxy_revision`, `jsonPayload.referer_path`, `jsonPayload.response_class`, `jsonPayload.target_latency_ms`, and `jsonPayload.total_latency_ms` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field   
2025-10-23 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src_ip`, `clientIp` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `src_ip`, `clientIp` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `vhost` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.principal.nat_ip: Newly mapped `xff` raw log field with `event.idm.read_only_udm.principal.nat_ip` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `userAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `clientId`, `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `appName` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `app` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly mapped `appId` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `developerMail` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `requestVerb`, `requests.requestVerb` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `targetUrl`, `target_metadata.targetUri` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `targetName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `statusCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `requestId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `apiTraceId`, `messageId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.intermediary: Newly mapped `intermediary` raw log field with `event.idm.read_only_udm.intermediary` UDM field.  
\- event.idm.read_only_udm.intermediary.resource.name: Newly mapped `apiProxyName` raw log field with `event.idm.read_only_udm.intermediary.resource.name` UDM field.  
\- event.idm.read_only_udm.intermediary.administrative_domain: Newly mapped `organizationName` raw log field with `event.idm.read_only_udm.intermediary.administrative_domain` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `requests.requestHost`, `requests.requestIp` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `requests.requestHost`, `requests.requestIp` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `apiStatistics.apmNumber`, `responseStatusCode`,`alertInstanceId`, `alertInstanceTime`,`failOverDeveloperApp`,`flowName`,`requestUri`, `responseCode`, `applog`, `activity`, `parameters`, `message_data`, `traceId`, `developerApp`, `authStatus`, `latencyTotal`, `envStatus`, `failover_enabled`, `active_active_enabled`, `reference_id`, `duration`, `requests.requestScheme`, `requests.requestReceivedStartTimestamp`, `requests.requestReceivedEndTimestamp`, `requests.requestSentStartTimestamp`, `requests.requestSentEndTimestamp`, `requests.requestPayload`, `response.responsePayload`, `apiStatistics.organization`, `apiStatistics.environment`, `apiStatistics.flow_name`, `requestHeaders`, `responseHeaders`, `environmentName`, `environment`, `targetVerb`, `clientReceivedStartTimestamp`, `clientReceivedEndTimestamp`, `targetSentStartTimestamp`, `targetSentEndTimestamp`, `targetReceivedStartTimestamp`, `targetReceivedEndTimestamp`, `clientSentStartTimestamp`, `clientSentEndTimestamp`, `responseDesc`, `apikey`, `gatewayAuthId`, `gatewayAuthId2`, `gatewayAuthLevel`, `latencyRequestTotal`, `isErrorCodeCategorized`, `request.header.Timestamp`, `request.header.Message-Signature`, `target_metadata.targetVerb` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `environmentName`, `environment`, `targetVerb`, `latencyHeader`, `clientReceivedStartTimestamp`, `clientReceivedEndTimestamp`, `targetSentStartTimestamp`, `targetSentEndTimestamp`, `targetReceivedStartTimestamp`, `targetReceivedEndTimestamp`, `clientSentStartTimestamp`, `clientSentEndTimestamp`, `responseDesc`, `apikey`, `gatewayAuthId`, `gatewayAuthId2`, `gatewayAuthLevel`, `latencyRequestTotal`, `latencyTarget`, `latencyProxy`, `isErrorCodeCategorized`, `request.header.Timestamp`, `request.header.Message-Signature`, `target_metadata.targetVerb` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result: Newly mapped `security_result` raw log field with `event.idm.read_only_udm.security_result` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `hmac.computed`, `honeyPot`, `honeyPotMerchant` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `statusReason` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `security_result_action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `signature` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If has_principal_user is true, updated to USER_UNCATEGORIZED.  
\- event.idm.read_only_udm.metadata.event_type: If has_principal_ip is true and has_target is true, updated to NETWORK_CONNECTION.  
\- event.idm.read_only_udm.metadata.event_type: If has_principal_ip is true and has_target is false, updated to STATUS_UPDATE.  
\- event.idm.read_only_udm.metadata.event_type: Otherwise, updated to GENERIC_EVENT.  
\- Added gsub function to replace `message` with `message_data` in json_data.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

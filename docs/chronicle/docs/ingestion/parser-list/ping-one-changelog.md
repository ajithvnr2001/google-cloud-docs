---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ping-one-changelog/
title: Change log for PING_ONE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:42.714816+00:00
---

# Change log for PING_ONE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ping-one-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PING_ONE

Date | Changes  
---|---  
2026-09-10 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `record._embedded.metadata.type`, `record._embedded.metadata.provider`, `record._embedded.metadata.id`, `record._embedded.metadata.data.overallWeightedScore`, `record._embedded.metadata.data.overallConfidenceScore`, `record._embedded.metadata.data.detailedResults.birth_date.rawScore`, `record._embedded.metadata.data.detailedResults.birth_date.confidence`, `record._embedded.metadata.data.detailedResults.name.rawScore`, `record._embedded.metadata.data.detailedResults.name.confidence`, `record._embedded.metadata.data.detailedResults.given_name.rawScore`, `record._embedded.metadata.data.detailedResults.given_name.confidence`, `record._embedded.metadata.data.detailedResults.family_name.rawScore`, `record._embedded.metadata.data.detailedResults.family_name.confidence`, `record._embedded.metadata.data.veriffVerification.vendorData`, `record._embedded.metadata.data.veriffVerification.status`, `record._embedded.metadata.data.veriffVerification.id`, `record._embedded.metadata.data.veriffVerification.code`, `record._embedded.metadata.data.veriffVerification.decisionTime`, `record._embedded.metadata.transaction.id`, `record._embedded.metadata.data.veriffVerification.acceptanceTime`, `matchResult.match` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `pingRequestDomain` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `actor.ip.address` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `record._embedded.metadata.status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.   
2026-01-29 |  Enhancement:  
\- `event.idm.read_only_udm.sec_result.detection_fields`: Newly mapped `outcomeDescription`, `outcomeStatusDetail`, `nodeTitle`, `nodeId`, `outcomeType`, `outcomeStatus`, `err_code` raw log fields with `event.idm.read_only_udm.sec_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `transactionId_flow` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `flowName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `companyId`, `eventMessage`, `connectorId`, `usageTransactionType` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `correlationId_flow`, `flowInteractionEvent_id`, `interactionId`, `originalCapabilityName`, `flow_success`, `identity`, `connectionId`, `err_msg`, `flowVersionId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `err_httpResponseCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `flow_userAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.metadata.ingested_timestamp`: Newly mapped `collectionDate` raw log field with `event.idm.read_only_udm.metadata.ingested_timestamp` UDM field.   
2025-11-06 |  Enhancement:  
\- Added support to new format of json logs.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `clientType` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.principal.user.title: Newly mapped `user_type` raw log field with `event.idm.read_only_udm.principal.user.title` UDM Field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `user_href` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `population_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.principal.asset_id: Newly mapped `user_environment_id` raw log field with `event.idm.read_only_udm.principal.asset_id` UDM Field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `actor_username` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM Field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `actor_userid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM Field.  
\- event.idm.read_only_udm.principal.cloud.project.id: Newly mapped `actor_clientId` raw log field with `event.idm.read_only_udm.principal.cloud.project.id` UDM Field.  
\- event.idm.read_only_udm.principal.cloud.project.name: Newly mapped `client_name` raw log field with `event.idm.read_only_udm.principal.cloud.project.name` UDM Field.  
\- event.idm.read_only_udm.principal.cloud.vpc.id: Newly mapped `environment_id` raw log field with `event.idm.read_only_udm.principal.cloud.vpc.id` UDM Field.  
\- event.idm.read_only_udm.principal.url: Newly mapped `client_href` raw log field with `event.idm.read_only_udm.principal.url` UDM Field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `result_description` raw log field with `event.idm.read_only_udm.security_result.summary` UDM Field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `result_status` raw log field with `event.idm.read_only_udm.security_result.action` UDM Field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `result_status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM Field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `record_transactionId` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `record_correlationId` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `action_type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `record_recordedAt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM Field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `record_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM Field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `source_ipaddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM Field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `source_ipaddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM Field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `source_userAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM Field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `source_userAgent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM Field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `action_description` raw log field with `event.idm.read_only_udm.security_result.description` UDM Field.  
\- event.idm.read_only_udm.target.url: Newly mapped `resource_url` raw log field with `event.idm.read_only_udm.target.url` UDM Field.  
\- event.idm.read_only_udm.target.user.attribute.labels: Newly mapped `resource_pop_id` raw log field with `event.idm.read_only_udm.target.user.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.target.cloud.project.id: Newly mapped `resource_env_id` raw log field with `event.idm.read_only_udm.target.cloud.project.id` UDM Field.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped `resource_email` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM Field.  
\- event.idm.read_only_udm.target.user.user_display_name: Newly mapped `resource_name` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM Field.  
\- event.idm.read_only_udm.target.resource.id: Newly mapped `resource_id` raw log field with `event.idm.read_only_udm.target.resource.id` UDM Field.  
\- event.idm.read_only_udm.target.resource.resource_subtype: Newly mapped `resource_type` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM Field.   
2024-12-05 |  Enhancement:  
\- Mapped `event.browser.userAgent` to `network.http.user_agent`.  
\- Mapped `source.userAgent` to `additional.fields`.   
2024-11-12 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

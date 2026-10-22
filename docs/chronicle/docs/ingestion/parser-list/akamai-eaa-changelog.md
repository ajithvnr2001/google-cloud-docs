---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-eaa-changelog/
title: Change log for AKAMAI_EAA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:54.908174+00:00
---

# Change log for AKAMAI_EAA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-eaa-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AKAMAI_EAA

Date | Changes  
---|---  
2025-07-15 |  Enhancement:  
\- event.idm.read_only_udm.metadata.id: Newly mapped `eventId` raw log field to event.idm.read_only_udm.metadata.id.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `eventTime` raw log field to event.idm.read_only_udm.metadata.event_timestamp.  
\- event.idm.read_only_udm.principal.user.company_name: Newly mapped `ACCOUNT_NAME` raw log field to event.idm.read_only_udm.principal.user.company_name.  
\- event.idm.read_only_udm.target.application: Newly mapped `APPLICATION` and `method` raw log fields to event.idm.read_only_udm.target.application.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `ACCOUNT_STATUS` and `PROPERTY_VERSION` raw log fields to event.idm.read_only_udm.target.resource.attribute.labels.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `USERNAME` raw log field to event.idm.read_only_udm.principal.user.userid.  
\- event.idm.read_only_udm.target.asset.asset_id: Newly mapped `ASSET_ID` raw log field to event.idm.read_only_udm.target.asset.asset_id.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `PROPERTY_NAME` raw log field to event.idm.read_only_udm.target.resource.name.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `pulsar_host` raw log field to event.idm.read_only_udm.intermediary.ip.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `pulsar_host` raw log field to event.idm.read_only_udm.intermediary.hostname.  
\- event.idm.read_only_udm.extensions.auth.auth_details: Newly mapped `authenticationMethod` raw log field to event.idm.read_only_udm.extensions.auth.auth_details.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `domain` raw log field to event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname.  
\- event.idm.read_only_udm.security_result.last_discovered_time: Newly mapped `notOnOrAfter` raw log field to event.idm.read_only_udm.security_result.last_discovered_time.  
\- event.idm.read_only_udm.security_result.about.labels: Newly mapped `entityId` raw log field to event.idm.read_only_udm.security_result.about.labels.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `eventType.eventDefinition.eventDescription` raw log fields to event.idm.read_only_udm.metadata.description.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `details` raw log field to event.idm.read_only_udm.security_result.description.  
\- event.idm.read_only_udm.security_result.first_discovered_time: Newly mapped `notBefore` raw log field to event.idm.read_only_udm.security_result.first_discovered_time.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `arrivalDate` raw log field to event.idm.read_only_udm.metadata.collected_timestamp.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `eventType.eventTypeId` raw log field to event.idm.read_only_udm.metadata.product_log_id.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `eventType.eventTypeName` raw log field to event.idm.read_only_udm.metadata.product_event_type.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `username` raw log field to event.idm.read_only_udm.principal.user.email_addresses.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `IS_INTERNAL_USER`, `IS_ON_HOME_ACCOUNT`, `CONTRACT_TYPE_ID`, `requestId`, `eventType.eventDefinition.eventDefinitionId`, `eventType.eventDefinition.eventName` and `impersonator` raw log fields to event.idm.read_only_udm.additional.fields.   
2025-01-09 |  Enhancement:  
\- Converted `error_code` to `string`.   
2023-11-14 |  Enhancement:  
\- Mapped `username`, `client_ip`, `device_type`, `cloud_zone`, `client_version`, `geo_city`, `geo_state`, `geo_country`, `resource`, `groups`, and `event` to `principal.user.user_display_name`, `principal.ip`, `principal.platform_version`, `principal.cloud.availability_zone`, `metadata.product_version`, `principal.location.city`, `principal.location.state`, `principal.location.country_or_region`, `principal.resource.attribute.labels`, `principal.user.group_identifiers` and `metadata.description` respectively.  
\- Mapped `http_method`, `protocol`, `app_version`, `referer`, `status_code`, `user_agent`, `session_id`, `bytes_out`, and `bytes_in` to `network.http_method`, `network.application_protocol`, `network.application_protocol_version`, `network.referral_url`, `network.http.response_code`, `network.http.user_agent`, `network.session_id`, `network.sent_bytes`, and `network.recieved_bytes` respectively.  
\- Mapped `resource`, `url_path`, and `apphost` to `target.resource.id`, `target.url`, and `target.hostname` respectively.  
\- Mapped `resp_time`, `conn_resp_time`, and `origin_resp_time` to `security_result.detection_fields`.  
\- Mapped `con_ip`, `con_srcport`, `deny_reason`, and `con_uuid` to `intermediary.ip`, `intermediary.port`, `security_result.summary`, and `intermediary.resource.product_object_id` respectively.  
\- Mapped `error_code`, `idpinfo`, `origin_host`, `content_type`, `internal_host`, `session_info`, and `client_id` to `additional.fields`.   
2023-08-31 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

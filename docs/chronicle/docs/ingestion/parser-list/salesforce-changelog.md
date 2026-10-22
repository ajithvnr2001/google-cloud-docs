---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/salesforce-changelog/
title: Change log for SALESFORCE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:31.465761+00:00
---

# Change log for SALESFORCE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/salesforce-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SALESFORCE

Date | Changes  
---|---  
2026-09-30 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping of `column4` from `event.idm.read_only_udm.principal.user.userid` UDM field when `event_id` is `LoginAs` and it contains target administrative domain data.  
\- `event.idm.read_only_udm.target.administrative_domain`: Mapped `column4` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field when `event_id` is `LoginAs`.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Removed mapping of `column5` from `event.idm.read_only_udm.principal.resource.product_object_id` UDM field when `event_id` is `LoginAs` and it contains principal user ID related data.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `column5` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field when `event_id` is `LoginAs`.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Removed mapping of `column11` from `event.idm.read_only_udm.principal.user.email_addresses` UDM field when `event_id` is `LoginAs` and it contains target user email related data.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Mapped `column11` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field when `event_id` is `LoginAs`.   
2026-08-26 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `column6` raw log field to `event.idm.read_only_udm.target.user.user_display_name` UDM field when `event_id` is `SalesforceLoginAs`.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `column5` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field when `event_id` is `SalesforceLoginAs`.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` : Newly mapped `column7` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when `event_id` is `SalesforceLoginAs`.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `column9` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field when `event_id` is `SalesforceLoginAs`.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `column8` raw log field to `event.idm.read_only_udm.network.session_id` UDM field when `event_id` is `SalesforceLoginAs`.   
2026-08-12 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping of `column4` from `event.idm.read_only_udm.principal.user.userid` UDM field for LightningInteraction, LightningPerformance, URI, and the new formats of LightningPageView (when `column52` is a valid IP), ApexExecution (when `column23` is a valid IP or `column22` is not empty), ApexTrigger (when `column24` is a valid IP), RestApi and ApexRestApi (when `column31` is a valid IP), and ApexCallout events (when `column24` is a valid IP or `column23` is not empty), as it contains Salesforce Organization ID.  
\- `event.idm.read_only_udm.target.administrative_domain`: Mapped `column4` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field for LightningInteraction, LightningPerformance, URI, LightningPageView (when `column52` is a valid IP), ApexExecution (when `column23` is a valid IP or `column22` is not empty), ApexTrigger (when `column24` is a valid IP), RestApi and ApexRestApi (when `column31` is a valid IP), and ApexCallout events (when `column24` is a valid IP or `column23` is not empty).  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `column30` (as `user_id_derived_data`) from `event.idm.read_only_udm.additional.fields` UDM field for RestApi and ApexRestApi events when `column31` is a valid IP address, as it contains actual user ID related data.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `column30` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field for RestApi and ApexRestApi events when `column31` is a valid IP address.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `column45`, `column32`, `column18`, `column56` (as `USER_ID_DERIVED`) from `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field for LightningInteraction, LightningPerformance, URI, and UiTelemetryResourceTiming events, as it contains actual user ID related data.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `column45`, `column32`, `column18`, `column56` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field for LightningInteraction, LightningPerformance, URI, and UiTelemetryResourceTiming events.  
\- `event.idm.read_only_udm.principal.resource.type`: Removed mapping of principal resource type from `event.idm.read_only_udm.principal.resource.type` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.principal.resource.resource_subtype`: Mapped principal resource type with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.resource.type`: Removed mapping of target resource type from `event.idm.read_only_udm.target.resource.type` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Mapped target resource type with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.resource.id`: Removed mapping of ID from `event.idm.read_only_udm.target.resource.id` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Mapped `ID` with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `ID` with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field when product object id is already present.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `column51` (for LightningPageView when `column52` is a valid IP), `column22` (for ApexExecution when `column23` is a valid IP or `column22` is not empty), and `column23` (for ApexTrigger when `column24` is a valid IP, and ApexCallout when `column24` is a valid IP or `column23` is not empty) raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `column23` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field for ApexExecution event when `column23` is a valid IP address or `column22` is not empty.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `column24` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field for ApexCallout (when `column24` is a valid IP address or `column23` is not empty) and ApexTrigger events (when `column24` is a valid IP address).  
\- `event.idm.read_only_udm.target.url`: Mapped `column18` raw log field with `event.idm.read_only_udm.target.url` UDM field for ApexCallout events when `column24` is a valid IP address or `column23` is not empty, and it has 25 columns.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `column14` (as `trigger_id`), `column17` (as `Trigger Event`), and `column15` (as `trigger_name`) raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field for ApexTrigger events.  
\- `event.idm.read_only_udm.network.received_bytes`, `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `column15` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field, and `column16` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field for ApexCallout events.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `column17` raw log field (as `Time Stamp`) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field for ApexCallout events.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column11` raw log field (as `api_type`) and `column16` raw log field (as `quiddity`) with `event.idm.read_only_udm.additional.fields` UDM field for ApexCallout and ApexExecution events respectively.   
2026-07-16 |  Enhancement:  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `referring_url` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `Salesforce_User_ID` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `Salesforce_Record` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `URL` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `response_size` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `target_user_id_details` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `record_id` and `rows_processed_data` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `derived_time`, `salesforce_number_fields`, `page_rendering_time_ms`, `client_request_id`, `network_rtt_ms`, `lightning_page_template`, `ui_context`, `lightning_component`, `salesforce_user_id_alt`, `ObjectType`, `sfdc_console_type`, `app`, `api_category`, `transaction_status`, `db_blocks_data`, `request_size_data`, `number_of_records`, `qp_total_time`, `user_id_derived_data` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-06-02 |  Enhancement:  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `HTTP_REFERER` (from `column22`) raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field for `Login` event_type logs and when `column33` is equal to `LOGIN_NO_ERROR`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `AUTHENTICATION_CONTEXT_CLASS_REFERENCE` (from `column28`), `OLE_object_id` (from `column27`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field for `Login` event_type logs and when `column33` is equal to `LOGIN_NO_ERROR`.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `target_usr_product_object_id` (from `column30`) raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field for `Login` event_type logs and when `column33` is equal to `LOGIN_NO_ERROR`.  
\- `event.idm.read_only_udm.security_result.first_discovered_time`: Newly mapped `column22` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field for `ApiTotalUsage` event_type logs.   
2026-05-12 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Removed mapping of `column17` from `event.idm.read_only_udm.principal.user.user_display_name` UDM field, as it contains principal email related data for `ApiTotalUsage` event_type logs.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Mapped `column17` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field for the `ApiTotalUsage` event_type logs.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Removed mapping of `column5` from `event.idm.read_only_udm.principal.resource.product_object_id` UDM field, as it contains principal user related data for `ApiTotalUsage` event_type logs.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `column5` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field for the `ApiTotalUsage` event_type logs.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Removed mapping of `user_type` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field, as it contains principal resource related data.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `user_type` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Removed mapping of `USER_ID_DERIVED` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field, as it contains principal resource related data.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `USER_ID_DERIVED` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `ApiVersion` from `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field, as it contains target resource related data.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `ApiVersion` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Removed mapping of `column9` from `event.idm.read_only_udm.metadata.product_log_id` UDM field, as it contains principal resource related data and network user_agent related data for `Login`, `Logout`, or `ApiTotalUsage` event_type logs.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `column9` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field for `ApiTotalUsage` event_type logs.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `column9` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field for `Logout` event_type logs.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `column9` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field for `Logout` event_type logs.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `column4` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field for `ApiTotalUsage` event_type logs.   
2026-04-24 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid`: Removed mapping of `column18` from `event.idm.read_only_udm.target.user.userid` UDM field, as it contains principal email related data for `Login` event_type logs.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `column18` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping of `column4` from `event.idm.read_only_udm.principal.user.userid` UDM field, as it contains target administrative domain information for `Logout` event_type logs.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `column4` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `column5` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field for `Logout` event_type logs.  
\- `event.idm.read_only_udm.target.resource.id`: Removed mapping of `request_id` from `event.idm.read_only_udm.target.resource.id` UDM field, as it contains target resource product specific information.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Mapped `request_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `column13`, `column18` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field for `ApiTotalUsage` event_type logs.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `column20`, `column8` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field for `Logout` event_type logs.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `column7`, `column16`, `login_subtype` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-03-30 |  Enhancement:  
\- Added a Grok pattern to extract target user details from the raw log.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `UserID` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.user.user_display_name: Mapped `target_user_name` log field to `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- Added support for a new pattern of CSV logs. Due to this, the following UDM fields are now being mapped correctly:  
\- `event.idm.read_only_udm.additional.fields`  
\- `event.idm.read_only_udm.principal.user.user_display_name`  
\- `event.idm.read_only_udm.security_result.description`  
\- `event.idm.read_only_udm.target.administrative_domain`  
2026-03-06 |  Enhancement:  
\- Added conditional check for `column21` to determine if it contains an IP address.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `column17` raw log field to `event.idm.read_only_udm.network.sent_bytes` UDM field.   
2026-02-06 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: Removed mapping of `column9` from `event.idm.read_only_udm.principal.user.userid` UDM field and mapped `column13` instead for `UiTelemetryResourceTiming` events as it is a more appropriate value for the specified UDM field.  
\- event.idm.read_only_udm.network.session_id: Removed mapping of `column9` from `event.idm.read_only_udm.network.session_id` UDM field and mapped `column12` instead for `UiTelemetryResourceTiming` events as it is a more appropriate value for the specified UDM field.  
\- Modified grok pattern for `device_platform` to extract `device`.  
\- Refactored parser logic for handling `DB_BLOCKS` and `DeviceSessionId` mappings.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `column5` raw log field to `event.idm.read_only_udm.target.user.userid` for `URI`, `UiTelemetryResourceTiming`, `LightningInteraction`, and `LightningPerformance` events.  
\- event.idm.read_only_udm.target.resource.attribute.labels: For URI events, newly mapped `DB_BLOCKS` (from `column14`), `USER_ID_DERIVED` (from `column18`) raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: For `UiTelemetryResourceTiming` events, newly mapped `USER_ID_DERIVED` (from `column56`) raw log field to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: For `LightningInteraction` events, newly mapped `PAGE_START_TIME` (from `column28`), `USER_ID_DERIVED` (from `column45`) raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: For `LightningPerformance` events, newly mapped `PAGE_START_TIME` (from `column28`), `USER_ID_DERIVED` (from `column32`) raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- event.idm.read_only_udm.target.administrative_domain: Newly mapped `column4` raw log field to `event.idm.read_only_udm.target.administrative_domain` for `UiTelemetryResourceTiming` events.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `column14` raw log field to `event.idm.read_only_udm.principal.location.country_or_region` for `UiTelemetryResourceTiming` events.  
\- event.idm.read_only_udm.principal.application: Newly mapped `column16` raw log field to `event.idm.read_only_udm.principal.application` for `UiTelemetryResourceTiming` events.  
\- event.idm.read_only_udm.principal.resource.name: Newly mapped `column21` raw log field to `event.idm.read_only_udm.principal.resource.name` for `UiTelemetryResourceTiming` events.  
\- event.idm.read_only_udm.principal.platform: Newly mapped `column23` raw log field to `event.idm.read_only_udm.principal.platform` for `UiTelemetryResourceTiming` events.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped `column24` raw log field to `event.idm.read_only_udm.principal.platform_version` for `UiTelemetryResourceTiming` events.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `column52` raw log field to `event.idm.read_only_udm.network.http.response_code` for `UiTelemetryResourceTiming` events.  
\- event.idm.read_only_udm.additional.fields: For `UiTelemetryResourceTiming` events, newly mapped `device`, `device_session_id` (from `column6`), `UI_EVENT_TIMESTAMP` (from `column7`), `UI_ROOT_ACTIVITY_ID` (from `column9`), `CONNECTION_TYPE` (from `column15`), `BROWSER_VERSION` (from `column22`), `PAGE_ENTITY_TYPE` (from `column26`), `PAGE_CONTEXT` (from `column27`), `PAGE_ENTITY_ID` (from `column28`), `INITIATOR_TYPE` (from `column33`), `NEXT_HOP_PROTOCOL` (from `column34`), `RENDER_BLOCKING_STATUS` (from `column35`), `WORKER_START` (from `column36`), `REDIRECT_START` (from `column37`), `REQUEST_START` (from `column45`), `RESPONSE_START` (from `column46`), `RESPONSE_END` (from `column48`), `TRANSFER_SIZE` (from `column49`), `ENCODED_BODY_SIZE` (from `column50`), `DECODED_BODY_SIZE` (from `column51`), `SERVER_REQUEST_ID` (from `column53`), `UI_THREAD_RESPONSE_DELAY` (from `column54`) raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.additional.fields: For `LightningInteraction` events, newly mapped device, `BROWSER_VERSION` (from `column17`), `UI_EVENT_ID` (from `column24`), `UI_EVENT_TYPE` (from `column25`), `UI_EVENT_SOURCE` (from `column26`), `UI_EVENT_TIMESTAMP` (from `column27`), `device_session_id` (from `column30`), `UI_EVENT_SEQUENCE_NUM` (from `column31`), `PAGE_ENTITY_ID` (from `column32`), `PAGE_ENTITY_TYPE` (from `column33`), `PAGE_CONTEXT` (from `column34`), `PAGE_APP_NAME` (from `column36`), `TARGET_UI_ELEMENT` (from `column37`), `PARENT_UI_ELEMENT` (from `column38`) raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.additional.fields: For `LightningPerformance` events, newly mapped `device`, `BROWSER_VERSION` (from `column17`), `UI_EVENT_ID` (from `column24`), `UI_EVENT_TYPE` (from `column25`), `UI_EVENT_SOURCE` (from `column26`), `UI_EVENT_TIMESTAMP` (from `column27`), `device_session_id` (from `column30`) raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `column16` raw log field to `event.idm.read_only_udm.network.http.referral_url` for `URI` events.  
\- Enhanced `SourceIp` parsing to distinguish between IP addresses and hostnames, mapping to `event.idm.read_only_udm.principal.ip` & `event.idm.read_only_udm.principal.asset.ip` or `event.idm.read_only_udm.principal.hostname` & `event.idm.read_only_udm.principal.asset.hostname` accordingly. This fixes the log failure issue for cases where invalid values were being assigned to `hostname` fields. This is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.event_timestamp.nanos`  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.ingestion_labels.key`  
\- `event.idm.read_only_udm.metadata.ingestion_labels.value`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.principal.user.userid`  
\- `event.idm.read_only_udm.target.url`  
\- `event.idm.read_only_udm.target.resource.id`  
\- `event.idm.read_only_udm.target.resource.attribute.labels.key`  
\- `event.idm.read_only_udm.target.resource.attribute.labels.value`  
\- `event.idm.read_only_udm.network.session_id`  
\- `event.idm.read_only_udm.network.http.method`  
\- `event.idm.read_only_udm.network.http.user_agent`  
\- `event.idm.read_only_udm.network.http.response_code`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.family`  
\- `event.idm.read_only_udm.security_result.rule_id`  
\- `event.idm.read_only_udm.additional.fields.key`  
\- `event.idm.read_only_udm.additional.fields.value.string_value`  
2026-02-02 |  Enhancement:  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `column27` raw log field to `event.idm.read_only_udm.target.user.userid`.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `column5` raw log field to `event.idm.read_only_udm.principal.user.product_object_id`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `column11`, `column20` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `column15` raw log field to `event.idm.read_only_udm.metadata.product_version`.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `column17` raw log field to `event.idm.read_only_udm.network.http.method`.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `column21` raw log field to `event.idm.read_only_udm.network.received_bytes`.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `column22` raw log field to `event.idm.read_only_udm.network.sent_bytes`.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `column28` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `column26` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `column16` raw log field to `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field`.   
2026-01-27 |  Enhancement:  
\- event.idm.read_only_udm.principal.nat_ip: Newly mapped `source_ip` raw log field(s) with `event.idm.read_only_udm.principal.nat_ip` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `x_forwarded_for_ip` raw log field(s) with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.   
2025-12-31 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `login_key` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `client_ip_1` field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `client_ip_1` field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `client_ip_1` field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `client_ip_1` field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.administrative_domain: Newly mapped `organization_id` field with `event.idm.read_only_udm.target.administrative_domain` UDM field if `event_id` is `AuraRequest`.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `column2` field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field if `event_id` is `AuraRequest`.  
\- event.idm.read_only_udm.principal.user.userid: Changed mapping for `event.idm.read_only_udm.principal.user.userid` from `column4` to `column5` UDM field if `event_id` is `AuraRequest`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `user_type` field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field if `event_id` is `AuraRequest`.   
2025-12-13 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `LoginTime` raw log field to event.idm.read_only_udm.metadata.event_timestamp.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `User.LastLoginDate` raw log field to event.idm.read_only_udm.metadata.collected_timestamp.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `ClientVersion` raw log field to event.idm.read_only_udm.metadata.product_version.  
\- event.idm.read_only_udm.principal.resource.type: Newly mapped `User.attributes.type` raw log field to event.idm.read_only_udm.principal.resource.type.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `User.Username`, `User.Email` raw log field to event.idm.read_only_udm.principal.user.email_addresses.  
\- event.idm.read_only_udm.principal.user.attribute.roles: Newly mapped `User.UserType` raw log field to event.idm.read_only_udm.principal.user.attribute.roles.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `User.Name` raw log field to event.idm.read_only_udm.principal.user.user_display_name.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `User.Id` raw log field to event.idm.read_only_udm.principal.user.product_object_id.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `User.attributes.url`, `User.NumberOfFailedLogins` raw log field to event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Id`, `LoginSubType`, `OptionsIsGet`, `OptionsIsPost`, `User.IsActive`, `User.ReceivesAdminInfoEmails`, `User.ReceivesInfoEmails`, `User.IsPortalEnabled` raw log field to event.idm.read_only_udm.additional.fields.   
2025-12-12 |  Enhancement:  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `column13` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `column14` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- Added `BulkApi2` in the conditional check for `event_id` field.   
2025-12-08 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Conditionally mapped the raw field `column16` to a new key-value pair within `event.idm.read_only_udm.security_result.detection_fields`. The key is `ActionMessage`. This mapping is applied only if the raw field `column20` is not empty and can be parsed as an IP or Hostname, AND the raw field `column16` is not empty.  
\- event.idm.read_only_udm.principal.ip: Conditionally mapped from the raw field `column20` if `column20` is not empty and can be parsed as an IP or Hostname.   
2025-11-11 |  Enhancement:  
\- Added support for new csv pattern of logs.  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Removed mapping of `column26` raw log field with event.idm.read_only_udm.principal.hostname UDM field and event.idm.read_only_udm.principal.asset.hostname UDM field in order to introduce a more accurate mapping for the raw log fields.  
\- event.idm.read_only_udm.security_result.description: Removed mapping of `column28` raw log field with event.idm.read_only_udm.security_result.description UDM field when log has `34 columns` in order to introduce a more accurate mapping for the raw log fields.  
\- event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname: Newly mapped `target_host` raw log field with event.idm.read_only_udm.target.hostname UDM field and event.idm.read_only_udm.target.asset.hostname UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `api_token`,`api_type`,`loginkey` raw log field with event.idm.read_only_udm.additional.fields UDM field.   
2025-10-27 |  Enhancement:  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `QUERY_IDENTIFIER` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `QUERY_TYPE` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `SQL_ID` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `LOGIN_KEY` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- Updated conditional check for `REQUEST_SIZE` to exclude values of `-1`.   
2025-10-01 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `properties.Description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.location.city`: Newly mapped `properties.City` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `properties.AppName` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `properties.OrgId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `properties.OrgName` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.namespace`: Newly mapped `namespace` raw log field with `event.idm.read_only_udm.principal.namespace` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `properties.LoginUrl, properties.PageUrl` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `properties.Application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `recordDate` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `name` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `properties.Username` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `properties.UserId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.role_name`: Newly mapped `properties.UserType` raw log field with `event.idm.read_only_udm.principal.user.role_name` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `properties.Country` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `properties.SourceIp` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `properties.SourceIp` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `properties.SourceIp (if not a valid IP), properties.OsName (if not Windows, Linux, or Mac), properties.DisplayedFieldEntities` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `properties.TlsProtocol` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `properties.CipherSuite` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `properties.EventDate, startTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `properties.EventIdentifier` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `properties.HttpMethod` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `properties.HttpMethod` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_latitude`: Newly mapped `properties.LoginLatitude` raw log field with `event.idm.read_only_udm.principal.location.region_latitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_longitude`: Newly mapped `properties.LoginLongitude` raw log field with `event.idm.read_only_udm.principal.location.region_longitude` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: Newly mapped `properties.OsName, properties.Platform` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `properties.OsVersion` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.target.resource.id`: Newly mapped `properties.RecordId` raw log field with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `properties.SessionKey` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `properties.UserAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `properties.UserAgent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `properties.PageStartTime, properties.PreviousPageUrl, properties.Description, properties.ReportId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `properties.Name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped properties.Records.datacells, finishDate, mrId, properties.CountryIso, properties.CreatedById, properties.Subdivision, properties.Browser, properties.EvaluationTime, properties.LoginGeoId, properties.LoginHistoryId, properties.LoginKey, properties.LoginSubType, properties.NetworkId, spanId, startDate, _region, endTime, device, properties.DeviceSessionId, properties.Duration, properties.EffectivePageTime, properties.ConnectionType, properties.EffectivePageTimeDeviationErrorType, properties.EffectivePageTimeDeviationReason, properties.HasEffectivePageTimeDeviation, properties.DeviceId, properties.DeviceModel, properties.Operation, properties.PreviousPageAppName, properties.PreviousPageEntityId, properties.PreviousPageEntityType, properties.QueriedEntities, properties.RelatedEventIdentifier, properties.Sandbox, properties.SdkAppType, properties.SdkAppVersion, properties.SdkVersion, properties.SessionLevel, properties.UserType, properties.CreatedDate, properties.AdditionalInfo, properties.ApiType, properties.ApiVersion, properties.AuthMethodReference, properties.AuthServiceId, properties.PostalCode, properties.PolicyOutcome, properties.LoginType, properties.ForwardedForIp, properties.ClientVersion, properties.RowsProcessed, properties.ExecutionIdentifier, properties.IsScheduled, properties.EventSource, properties.ColumnHeaders, properties.DashboardId, properties.DashboardName, properties.ExportFileFormat, properties.Format, properties.GroupedColumnHeaders, properties.NumberOfColumns, properties.RowsReturned, properties.Scope, properties.Sequence` and `properties.OwnerId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-09-26 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped column12 raw log fields with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped column14 raw log fields with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped column10 raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped column15, column11 raw log fields with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped principal_ip, column15 raw log fields with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped intermediary_ip raw log fields with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.target.resource.id`: Newly mapped column8 raw log fields with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped column12 raw log fields with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped column15 raw log fields with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped column3 raw log fields with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped column5 raw log fields with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped column14 raw log fields with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped column14 raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped column17 for LoginAs event type raw log fields with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped column13 for ApiTotalUsage event type raw log fields with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped column8 for the Search event type has been added to `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped column5 to column4 raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.   
2025-08-26 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `profile_name` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `src_app_name` raw log field to `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `STATUS_CODE` raw log field to `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `CLIENT_IP` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `method` raw log field to `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `resource_name` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `ApiVersion` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `app_name` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly mapped `column13` raw log field to `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `ENTITY_NAME`, `COUNTS_AGAINST_API_LIMIT` and `column14` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2025-01-30 |  Enhancement:  
\- Mapped `region` to `principal.location.country_or_region`.  
\- Mapped `account` to `principal.user.userid`.  
\- Mapped `detail.payload.ConnectedAppId` to `additional.fields`.  
\- Mapped `detail.payload.Platform` to `additional.fields`.  
\- Mapped `detail.payload.Query` to `additional.fields`.  
\- Mapped `detail.payload.EvaluationTime` to `additional.fields`.  
\- Mapped `detail.payload.Operation` to `additional.fields`.  
\- Mapped `detail.payload.LoginHistoryId` to `additional.fields`.  
\- Mapped `detail.payload.CreatedById` to `additional.fields`.  
\- Mapped `detail.payload.SessionKey` to `additional.fields`.  
\- Mapped `detail.payload.ApiType` to `additional.fields`.  
\- Mapped `detail.payload.UserAgent` to `network.http.user_agent`.  
\- Mapped `detail.payload.Client` to `principal.asset.hostname`.  
\- Mapped `detail.payload.PolicyOutcome` to `security_result.detection_fields`.  
\- Mapped `detail.payload.EventIdentifier` to `additional.fields`.  
\- Mapped `detail.payload.RequestIdentifier` to `additional.fields`.  
\- Mapped `detail.payload.ApiVersion` to `additional.fields`.  
\- Mapped `detail.payload.RelatedEventIdentifier` to `additional.fields`.  
\- Mapped `detail.payload.Username` to `target.user.email_addresses`.  
\- Mapped `detail.payload.RowsProcessed` to `additional.fields`.  
\- Mapped `detail.payload.RowsReturned` to `additional.fields`.  
\- Mapped `detail.payload.SourceIp` to `principal.ip`.  
\- Mapped `detail.payload.UserId` to `target.user.userid`.  
\- Mapped `totalSize` to `additional.fields`.  
\- Mapped `done` to `additional.fields`.  
\- Mapped `detail.payload.CreatedDate` to `additional.fields`.  
\- Mapped `detail.payload.LoginKey` to `additional.fields`.  
\- Mapped `detail.payload.Application` to `additional.fields`.  
\- Mapped `detail.payload.PolicyId` to `additional.fields`.  
\- Mapped `detail.payload.QueriedEntities` to `additional.fields`.  
\- Mapped `detail.payload.SessionLevel` to `additional.fields`.  
\- Mapped `detail.schemaId` to `additional.fields`.  
\- Mapped `detail.id` to `target.resource.id`.  
\- Mapped `records_index.attributes.type` to `security_result.detection_fields`.   
2025-01-21 |  Enhancement:  
\- Mapped `column25` to `network.http.user_agent`.  
\- Mapped `column28` to `principal.ip` and `principal.asset.ip`.  
\- If `column24` contain `User-Agent`, then mapped `column24` to `network.http.user_agent`. Otherwise, mapped `column24` to `network.http.method`.   
2025-01-15 |  Enhancement:  
\- Mapped `Name` to `principal.user.user_display_name`.  
\- Mapped `Email` to `principal.user.email_addresses`.  
\- Mapped `FederationIdentifier` to `additional.fields`.  
\- Mapped `CreatedBy.Email` to `principal.user.email_addresses`.  
\- Mapped `CreatedBy.Name` to `principal.user.user_display_name`.  
\- Mapped `CreatedBy.FederationIdentifier` to `additional.fields`.  
\- Mapped `Section` to `additional.fields`.  
\- Mapped `DelegateUser` to `additional.fields`.  
\- Mapped `ResponsibleNamespacePrefix` to `additional.fields`.  
\- Mapped `CreatedByContext` to `additional.fields`.  
\- Mapped `CreatedByIssuer` to `additional.fields`.  
\- Mapped `Browser` to `additional.fields`.  
\- When `Platform` is nearly equal to `Windows`, then mapped `principal.platform` to `WINDOWS`.  
\- When `Platform` is nearly equal to `Linux`, then mapped `principal.platform` to `LINUX`.  
\- When `Platform` is nearly equal to `Mac`, then mapped `principal.platform` to `MAC`.  
\- Mapped `Status` to `security_result.action_details`.  
\- Mapped `CountryIso` to `additional.fields`.   
2025-01-10 |  Enhancement:  
\- Added support for new pattern of `Login` and `LoginAs` logs.   
2025-01-09 |  Enhancement:  
\- Mapped `payload.PreviousPageUrl` to `metadata.url_back_to_product`.  
\- Mapped `payload.OsVersion` to `principal.platform_version`.  
\- Mapped `payload.PreviousPageEntityId`, `payload.SdkVersion`, `payload.Operation`, `payload.PageUrl`, `HasEffectivePageTimeDeviation_label`, `payload.EffectivePageTime`, `payload.EffectivePageTimeDeviationReason`, `payload.DeviceSessionId`, `payload.PreviousPageAppName`, and `payload.PreviousPageEntityType` to `additional.fields`.  
\- Mapped `payload.SessionKey` to `network.session_id`.  
\- Mapped `payload.UserAgent` to `network.http.user_agent`.  
\- Mapped `payload.RecordId` to `target.resource.id`.  
\- Mapped `payload.EventIdentifier` to `metadata.product_log_id`.  
\- Mapped `payload.OsName` to `principal.platform`.   
2024-12-10 |  Enhancement:  
\- Mapped `user_permission` to `principal.user.attribute.labels`.   
2024-12-03 |  Enhancement:  
\- Added support for new pattern of `Login` logs.   
2024-11-29 |  Enhancement:  
\- Added support for a new format of JSON logs.   
2024-10-07 |  Enhancement:  
\- Added `deactivateduser`, `PermSetUnassign`, and `PermSetAssign` as conditional check.   
2024-09-20 |  Enhancement:  
\- Mapped `column9` to `metadata.product_log_id`.  
\- Mapped `column5` to `security_result.rule_author`.  
\- Mapped `column10` to `security_result.summary`.  
\- Mapped `column4` to `security_result.rule_name`.   
2024-09-16 |  Enhancement:  
\- Mapped `description` to `security_result.description`.  
\- Mapped `client_ip` to `principal.ip` and `principal.asset.ip`.  
\- Fixed mapping of `target_username` and `tls_protocol`.   
2024-07-08 |  Enhancement:  
\- Mapped `domain` to `target.administrative_domain`.  
\- Mapped `user_display` to `principal.user.userid`.  
\- Mapped `section` to `additional.fields`.  
\- Fixed the mapping to parse all fields.   
2024-06-04 |  Enhancement:  
\- Added support for newly ingested logs.   
2024-03-06 |  Enhancement:  
\- Changed mapping of the field `Id` from `metadata.product_log_id` to `principal.user.userid`.  
\- Changed mapping of the field `CreatedById` from `principal.user.userid` to `principal.resource.attribute.labels`.  
\- Mapped `IsDeleted` to `principal.resource.attribute.labels`.  
\- Mapped `LogFileLength` to `principal.resource.attribute.labels`.  
\- Mapped `LogFileContentType` to `principal.resource.attribute.labels`.  
\- Mapped `ApiVersion` to `principal.resource.attribute.labels`.  
\- Mapped `LogFile` to `principal.resource.attribute.labels`.   
2023-02-24 |  Enhancement-  
\- `security_result.action` mapped to ALLOW instead of BLOCK if the action is `LOGIN_NO_ERROR`.  
\- For `Login` events :  
\- `action` mapped to `security_result.action`.  
\- `target_user_name` mapped to `target.user.userid`.  
\- `tls_protocol` mapped to `network.tls.version_protocol`.  
\- `cipher_suite` mapped to `network.tls.cipher`.  
\- Added `on_error` check for `OsVersion` and `date` block.   
2022-12-13 |  Enhancement-  
-Mapped `LoginType` to `security_result.description`.  
-Mapped `LoginUrl` to `principal.url`.  
-Added empty check for `ApiType` and `LoginGeo.City`.   
2022-09-02 |  Enhancement-  
Migrated the custom parsers into default parser.   
2022-07-04 |  Enhancement-  
\- Enhanced the parser to parse the logs having event_type `LoginHistory`.  
\- Added condition to parse different formats of timestamp.  
\- Added condition for event_type `USER_UNCATEGORIZED` where `user_id` or `UserId` or `target_user_name` is not null.  
\- Added validation for parsing src_ip.   
2022-04-18 |  Enhancement-Modified mapping for DOWNLOAD_FORMAT from `metadata.ingestion_labels` to `target.resource.attribute.labels`.   
2022-03-30 |  Enhancement-Changed event_type for `LoginEventStream` to USER_LOGIN.  
Corrected mapping for the fields DOWNLOAD_FORMAT and ConnectedAppId.  
Added mappings for certain fields when log is of type LoginEventStream, WaveDownload, ApiEventStream.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workspace-activity-changelog/
title: Change log for WORKSPACE_ACTIVITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:39:19.837216+00:00
---

# Change log for WORKSPACE_ACTIVITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workspace-activity-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WORKSPACE_ACTIVITY

Date | Changes  
---|---  
2026-09-21 |  \- `target.url_metadata.title`: Newly mapped `TAB_TITLE` parameter raw log field with `target.url_metadata.title` UDM field for `chrome` application events.   
2026-08-18 |  \- security_result.action_details: Removed mapping of `events.status.eventStatus` from `security_result.action_details` UDM field to ensure accurate identification of the event status.  
\- security_result.action: Removed static mapping of `events.status.eventStatus` from `security_result.action` UDM field to ensure accurate identification of the event status.  
\- additional.fields[event_status]: Mapped `events.status.eventStatus` raw log field with `additional.fields[event_status]` UDM field.  
\- security_result.action: Mapped `BYPASSED` and `WARNED` values of `EVENT_RESULT` raw log field to `security_result.action` UDM field as `ALLOW` for the `chrome` application.   
2026-07-10 |  \- Provided support for the following applications: `vault`, `classroom`, `assignments`, `cloud_search`, `tasks`, `data_migration`, `meet_hardware`, `directory_sync`, `ldap`, `profile`, `access_evaluation`, `admin_data_action`, `contacts`, `takeout`, `graduation`.   
2026-06-30 |  \- Updated the field mapping for the Workspace Activity parser. Please refer to the parser documentation page for information regarding the updated UDM mappings - https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workspace-activity#udm_mapping_delta  
\- Enhanced support for applications `calendar`, `chat`, `chrome`, `data_studio`, `drive`, `gmail`, `groups`, `groups_enterprise`, `login`, `meet`, `gemini_in_workspace_apps`, and `token` through the addition of new events as part of Workspace Activity Refresher.   
2026-05-14 |  \- target.resource.attribute.labels[device_compromised_state]: Newly mapped `events.parameters[device_compromised_state]` raw log field with `target.resource.attribute.labels[device_compromised_state]` UDM field.   
2025-12-24 |  \- Added `google_chat` as an application name alongside `chat`.   
2025-12-12 |  Updated the mapping as below to accurately map the following fields for the `gmail` application and the `delivery` event name.  
\- principal.network.email.to: Removed mapping of `actor.email` from `principal.network.email.to` UDM field.  
\- network.email.to: Removed mapping of `actor.email` from `network.email.to` UDM field.  
\- principal.user.email_addresses: Removed mapping of `events.parameters[delivery].msgValue[message_info].parameter.msgValue[source].parameter.value[address]` from `principal.user.email_addresses` UDM field.  
\- principal.network.email.from: Removed mapping of `events.parameters[delivery].msgValue[message_info].parameter.msgValue[source].parameter.value[from_header_address]` from `principal.network.email.from` UDM field.  
\- network.smtp.mail_from: Mapped `events.parameters[delivery].msgValue[message_info].parameter.msgValue[source].parameter.value[address]` raw log field with `network.smtp.mail_from` UDM field.   
2025-12-09 |  \- Enhanced the parser with the changes mentioned in the schema for admin audit logs. The changes are as follows:  
\- `DISALLOW_SERVICE_FOR_OAUTH2_ACCESS` event type is renamed to `CHANGE_API_ACCESS`  
\- `ADD_TO_BLOCKED_OAUTH2_APPS` event type is renamed to `CHANGE_API_ACCESS`  
\- `ADD_TO_TRUSTED_OAUTH2_APPS` event type is renamed to `CHANGE_API_ACCESS`  
\- `USER_DEFINED_SETTING_NAME` (param) is moved to `SETTING_METADATA.USER_DEFINED_NAME`  
\- `CHANGE_EMAIL_SETTING` event type is renamed to `CHANGE_APPLICATION_SETTING`  
\- `CHANGE_GMAIL_SETTING` event type is renamed to `CHANGE_APPLICATION_SETTING`  
\- `DELETE_GMAIL_SETTING` event type is renamed to `DELETE_APPLICATION_SETTING`  
\- `CREATE_GMAIL_SETTING` event type is renamed to `CREATE_APPLICATION_SETTING`  
\- For `CHANGE_APPLICATION_SETTING` event type, `SETTING_METADATA` param is newly introduced and it has following sub-fields:  
\- `USER_DEFINED_NAME, DESCRIPTION, rule_key, rule_type`  
\- For some event types, the values of the different parameters have been changed in which development is not required.   
2025-11-13 |  \- principal.ip: Newly mapped LOCAL_IP values from `events.parameters` raw log field with `principal.ip` UDM field for applicationName `chrome`.  
\- target.ip: Newly mapped REMOTE_IP values from `events.parameters` raw log field with `target.ip` UDM field for applicationName `chrome`.   
2025-11-07 |  \- Updated the parser to map the fields `actor.applicationInfo.oauthClientId`, `actor.applicationInfo.impersonation`, and `actor.applicationInfo.applicationName`.  
\- `principal.asset.attribute.labels[device_type]` : Newly mapped `userDeviceInfo.deviceType` raw log field with `principal.asset.attribute.labels[device_type]` UDM field.   
2025-09-02 |  \- `principal.ip_geo_artifact.network.asn` : Newly mapped `networkInfo.ipAsn` raw log field with `principal.ip_geo_artifact.network.asn` UDM field  
\- `principal.location.country_or_region` : Newly mapped `networkInfo.regionCode` raw log field with `principal.location.country_or_region` UDM field  
\- `principal.location.state` : Newly mapped `networkInfo.subdivisionCode` raw log field with `principal.location.state` UDM field  
\- `principal.application` : Newly mapped `actor.applicationInfo.applicationName` raw log field with `principal.application` UDM field  
\- `additional.fields[oauth_client_id]` : Newly mapped `actor.applicationInfo.oauthClientId` raw log field with `additional.fields[oauth_client_id]` UDM field  
\- `additional.fields[impersonation]` : Newly mapped `actor.applicationInfo.impersonation` raw log field with `additional.fields[impersonation]` UDM field  
\- `principal.platform` : Newly mapped `userDeviceInfo.deviceType` raw log field with `principal.platform` UDM field  
\- `principal.platform_version` : Newly mapped `userDeviceInfo.deviceOsVersion` raw log field with `principal.platform_version` UDM field  
\- `principal.asset.asset_id` : Newly mapped `userDeviceInfo.deviceId` raw log field with `principal.asset.asset_id` UDM field  
\- `network.http.response_code` : Newly mapped `events.status.httpStatusCode` raw log field with `network.http.response_code` UDM field  
\- `security_result.action_details` : Newly mapped `events.status.eventStatus` raw log field with `security_result.action_details` UDM field  
\- `security_result.detection_fields[error_code]` : Newly mapped `events.status.errorCode` raw log field with `security_result.detection_fields[error_code]` UDM field  
\- `security_result.description` : Newly mapped `events.status.errorMessage` raw log field with `security_result.description` UDM field  
\- Added constraint on email addresses to be less than 256 characters.   
2025-07-16 |  \- about.resource.attribute.labels[applied_labels_field_values_selection_value_display_name]: Newly mapped `resourceDetails.appliedLabels.fieldValues.selectionValue.displayName` raw log field with `about.resource.attribute.labels[applied_labels_field_values_selection_value_display_name]` UDM field.  
\- about.resource.attribute.labels[applied_labels_field_values_selection_value_id]: Newly mapped `resourceDetails.appliedLabels.fieldValues.selectionValue.id` raw log field with `about.resource.attribute.labels[applied_labels_field_values_selection_value_id]` UDM field.  
\- about.resource.attribute.labels[applied_labels_field_values_selection_value_badged]: Newly mapped `resourceDetails.appliedLabels.fieldValues.selectionValue.badged` raw log field with `about.resource.attribute.labels[applied_labels_field_values_selection_value_badged]` UDM field.   
2025-07-07 |  \- about.resource.attribute.labels[applied_labels_field_values_selection_value_display_name]: Newly mapped `resourceDetails.appliedLabels.fieldValues.selectionValue.displayName` raw log field with `about.resource.attribute.labels[applied_labels_field_values_selection_value_display_name]` UDM field.  
\- about.resource.attribute.labels[applied_labels_field_values_selection_value_id]: Newly mapped `resourceDetails.appliedLabels.fieldValues.selectionValue.id` raw log field with `about.resource.attribute.labels[applied_labels_field_values_selection_value_id]` UDM field.   
2025-06-23 |  This version adds support for the `resourceDetails` object within the Workspace Activity logs by adding a new set of mappings as listed below:  
\- about.resource.attribute.labels[resource_id]: Newly mapped `events.resourceIds` raw log field with `about.resource.attribute.labels[resource_id]` UDM field.  
\- about.resource.product_object_id: Newly mapped `resourceDetails.id` raw log field with `about.resource.product_object_id` UDM field.  
\- about.resource.name: Newly mapped `resourceDetails.title` raw log field with `about.resource.name` UDM field.  
\- about.resource.resource_subtype: Newly mapped `resourceDetails.type` raw log field with `about.resource.resource_subtype` UDM field.  
\- about.resource.attribute.labels[application_id]: Newly mapped `resourceDetails.applicationId` raw log field with `about.resource.attribute.labels[application_id]` UDM field.  
\- about.resource.attribute.labels[relation]: Newly mapped `resourceDetails.relation` raw log field with `about.resource.attribute.labels[relation]` UDM field.  
\- about.resource.attribute.labels[owner_email]: Newly mapped `resourceDetails.ownerEmail` raw log field with `about.resource.attribute.labels[owner_email]` UDM field.  
\- about.resource.attribute.labels[applied_labels_id]: Newly mapped `resourceDetails.appliedLabels.id` raw log field with `about.resource.attribute.labels[applied_labels_id]` UDM field.  
\- about.resource.attribute.labels[applied_labels_title]: Newly mapped `resourceDetails.appliedLabels.title` raw log field with `about.resource.attribute.labels[applied_labels_title]` UDM field.  
\- about.resource.attribute.labels[applied_labels_reason]: Newly mapped `resourceDetails.appliedLabels.reason` raw log field with `about.resource.attribute.labels[applied_labels_reason]` UDM field.  
\- about.resource.attribute.labels[applied_labels_field_values_reason]: Newly mapped `resourceDetails.appliedLabels.fieldValues.reason` raw log field with `about.resource.attribute.labels[applied_labels_field_values_reason]` UDM field.  
\- about.resource.attribute.labels[applied_labels_field_values_id]: Newly mapped `resourceDetails.appliedLabels.fieldValues.id` raw log field with `about.resource.attribute.labels[applied_labels_field_values_id]` UDM field.  
\- about.resource.attribute.labels[applied_labels_field_values_display_name]: Newly mapped `resourceDetails.appliedLabels.fieldValues.displayName` raw log field with `about.resource.attribute.labels[applied_labels_field_values_display_name]` UDM field.  
\- about.resource.attribute.labels[applied_labels_field_values_type]: Newly mapped `resourceDetails.appliedLabels.fieldValues.type` raw log field with `about.resource.attribute.labels[applied_labels_field_values_type]` UDM field.  
\- about.resource.attribute.labels[applied_labels_field_values_date_value_year]: Newly mapped `resourceDetails.appliedLabels.fieldValues.dateValue.year` raw log field with `about.resource.attribute.labels[applied_labels_field_values_date_value_year]` UDM field.  
\- about.resource.attribute.labels[applied_labels_field_values_date_value_month]: Newly mapped `resourceDetails.appliedLabels.fieldValues.dateValue.month` raw log field with `about.resource.attribute.labels[applied_labels_field_values_date_value_month]` UDM field.  
\- about.resource.attribute.labels[applied_labels_field_values_date_value_day]: Newly mapped `resourceDetails.appliedLabels.fieldValues.dateValue.day` raw log field with `about.resource.attribute.labels[applied_labels_field_values_date_value_day]` UDM field.  
\- about.resource.attribute.labels[applied_labels_field_values_selection_list_value_id]: Newly mapped `resourceDetails.appliedLabels.fieldValues.selectionListValue.values.id` raw log field with `about.resource.attribute.labels[applied_labels_field_values_selection_list_value_id]` UDM field.  
\- about.resource.attribute.labels[applied_labels_field_values_selection_list_value_display_name]: Newly mapped `resourceDetails.appliedLabels.fieldValues.selectionListValue.values.displayName` raw log field with `about.resource.attribute.labels[applied_labels_field_values_selection_list_value_display_name]` UDM field.  
\- about.resource.attribute.labels[applied_labels_field_values_text_list_value_values]: Newly mapped `resourceDetails.appliedLabels.fieldValues.textListValue.values` raw log field with `about.resource.attribute.labels[applied_labels_field_values_text_list_value_values]` UDM field.  
\- about.resource.attribute.labels[applied_labels_field_values_user_list_value_values_email]: Newly mapped `resourceDetails.appliedLabels.fieldValues.userListValue.values.email` raw log field with `about.resource.attribute.labels[applied_labels_field_values_user_list_value_values_email]` UDM field.   
2025-05-09 |  \- event.idm.read_only_udm.principal.hostname : Newly Mapped `DEVICE_NAME` to `event.idm.read_only_udm.principal.hostname` UDM field.  
\- Added Support to handle the Action Details properly.  
\- Aded Support to handle the `GENERIC_EVENT` events.   
2025-04-16 |  \- security_result.action: Newly mapped `security_result.action` UDM field for `id.applicationName`=`saml`  
2024-11-22 |  \- Mapped `from_header_address` raw log field to `network.email.from` UDM field.  
\- Mapped `actor.email` raw log field to `network.email.to` UDM field   
2024-10-18 |  \- Mapped `message_info.post_delivery_info.action_type` raw log field to `about.labels[post_delivery_action_type]` UDM field.  
\- Mapped `message_info.post_delivery_info.interaction.link_url` raw log field to `about.url` UDM field   
2024-09-17 |  \- Mapped each email address of the raw log field `resource_recipients` separately to `principal.user.email_addresses` UDM field.   
2024-09-09 |  \- Updated mapping of field `from_header_address` to `principal.network.email.from`.   
2024-07-26 |  \- Added support to parse the logs having `events` marked as hidden and the logs that are out of scope parsed as GENERIC_EVENT.   
2024-06-05 |  \- Added support for `access_url`, `access_item_content`, and `sheets_import_url` events.   
2024-05-15 |  \- Added additional mapping for `target_user` field.  
\- Added support for `team_drive_settings_change`, `presentation_stopped`, and `content_unmatched` events.  
\- Added support for `BLOCKED_API_ACCESS` and `MONITOR_MODE_ACCESS_DENY_EVENT` events.  
\- Added support of field `TAB_URL` for event `MALWARE_TRANSFER`.   
2024-05-09 |  \- Added support for logs of applicationName `google_meet`.   
2024-05-08 |  \- Added support for `team_drive_membership_change`, `change_owner_hierarchy_reconciled`, and `publish_new_version` events.  
\- Added support of field `file_name` for Gmail logs.   
2024-03-06 |  \- Added support for `call_ended`, `presentation_started`, and `invitation_sent` events.  
\- Mapped `login_challenge_method` count to `security_result.detection_fields`.  
\- Handled different timestamp format.  
\- Update mapping of actor.profileId field to noun.user.product_object_id.  
\- Added support of new events `DELETE_GROUP`, `SECURITY_CENTER_RULE_THRESHOLD_TRIGGER`, `RELEASE_FROM_QUARANTINE` and `deny`.   
2023-12-13 |  Added support for `ADD_TO_BLOCKED_OAUTH2_APPS`, `ADD_TO_TRUSTED_OAUTH2_APPS`,  
`UPDATE_ACCESS_LEVEL_V2`, `sharing_blocked`, `UPDATE_AUTO_PROVISIONED_USER`,  
`SECURITY_INVESTIGATION_EXPORT_QUERY`, and `SECURITY_INVESTIGATION_ACTION_CANCELLATION` events.   
2023-11-29 |  \- Added support for `email_collaborators`, `message_deleted` and `unsubscribe_via_mail` events.  
\- Added additional mappings for deprecated labels.   
2023-11-01 |  1\. Added support for `download_forms_response`, `ACTION_REQUESTED`, `change_email_subscription_type`, and `reaction_added` events.  
2\. Updated mapping of field `target` for `applicationName`=`drive` to `target.user.email_addresses`.  
3\. Enhancement to use `base64` hex decode function to parse IP addresses.   
2023-10-04 |  Added support for `invitation_sent`, `SECURITY_INVESTIGATION_ACTION_COMPLETION`,  
`CREATE_GMAIL_SETTING`, `CHANGE_GMAIL_SETTING` and `DELETE_GMAIL_SETTING` events.   
2023-09-20 |  Added logic to map `actor.key` to `noun.user.userid` where `actor.callType` is `KEY`.   
2023-09-06 |  Added support for new events.   
2023-08-24 |  Modified the logic to parse `TARGET_USER_EMAIL` field for events.name `CHANGE_USER_ACCESS`.   
2023-08-23 |  Modified logic for `events.name=CHROME_OS_LOGIN_EVENT`.   
2023-08-09 |  1\. Added support for GMAIL_LOGS.  
2\. Added support for events `CHANGE_EMAIL_SETTING`,  
`SECURITY_INVESTIGATION_ACTION`,  
`SECURITY_INVESTIGATION_OBJECT_CREATE_DRAFT_INVESTIGATION`,  
`REMOVE_GROUP_MEMBER`,  
`UPDATE_GROUP_MEMBER_DELIVERY_SETTINGS`, `UPDATE_GROUP_MEMBER`,  
and `SECURITY_CHART_DRILLDOWN`.   
2023-07-26 |  Added support for events `label_applied`, `risky_sensitive_action_blocked`,  
`ALERT_CENTER_LIST_FEEDBACK`, `ALERT_CENTER_GET_SIT_LINK`,  
`ALERT_CENTER_LIST_CHANGE`, `ALERT_CENTER_LIST_RELATED_ALERTS`,  
`EMAIL_LOG_SEARCH`, `SECURITY_INVESTIGATION_QUERY`, `CHANGE_GROUP_SETTING`,  
`ADD_GROUP_MEMBER`, `CREATE_GROUP`, `USER_LICENSE_ASSIGNMENT`,  
`USER_LICENSE_REVOKE`, and `blocked_sender`.   
2023-07-12 |  \- Added support of event `label_field_value_changed` for `applicationName=rules`.   
2023-06-14 |  1\. Additional mapping of `actor.email` field with `security_result.about.email` UDM field.  
2\. Updated the parser to include `parse_network_http_user_agent` to use `Parsed User Agent` and `User Agent`.   
2023-05-31 |  1\. Added support of events `ASSIGN_ROLE`, `CREATE_ROLE` for `applicationName=admin` and `events.type = DELEGATED_ADMIN_SETTINGS`.  
2\. Added support of events `AUTHORIZE_API_CLIENT_ACCESS` for `applicationName=admin` and `events.type = DOMAIN_SETTINGS`.  
3\. Added support of events `ALERT_CENTER_VIEW` for `applicationName=admin` and `events.type = ALERT_CENTER`.  
4\. Added support of events `risky_sensitive_action_allowed` for `applicationName=login` and `events.type = login`.  
5\. Modified logic for `USER_LOGIN` events.   
2023-05-29 |  Update mapping of `actor` field for `USER_LOGIN` and `USER_LOGOUT` events.   
2023-04-12 |  Promoted WORKSPACE_ACTIVITY parser to default.  
For the field mapping reference, see [https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workspace-activity#field-mapping>Collect Google Workspace logs](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/<code).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

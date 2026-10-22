---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sailpoint-iam-changelog/
title: Change log for SAILPOINT_IAM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:27.038288+00:00
---

# Change log for SAILPOINT_IAM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sailpoint-iam-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SAILPOINT_IAM

Date | Changes  
---|---  
2026-09-18 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `source` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `clientHost` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `string1`, `string2`, `string3`, and `string4` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `attributeName`, `attributeValue`, `autoCreated`, `dirty`, `disabled`, `immutable`, `locked`, `nameUnique`, `persisted`, `pseudoCreated`, `refreshedExistingLock`, and `xml` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-07-27 |  Enhancement:  
\- Added support for syslog format.  
\- Added a grok pattern on message to extract `syslog_pri`, `syslog_version`, `timestamp`, `hostname`, `appname`, `description`.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.   
2025-08-29 |  Enhancement:  
\- event.idm.entity.entity.user.first_name: Newly mapped firstName raw log field to event.idm.entity.entity.user.first_name UDM field.  
\- event.idm.entity.entity.user.last_name: Newly mapped lastName raw log field to event.idm.entity.entity.user.last_name UDM field.  
\- event.idm.entity.entity.user.user_display_name: Newly mapped displayName raw log field to event.idm.entity.entity.user.user_display_name UDM field.  
\- event.idm.entity.metadata.product_entity_id: Newly mapped id raw log field to event.idm.entity.metadata.product_entity_id UDM field.  
\- event.idm.entity.entity.user.managers: Newly mapped manager.displayName raw log field to user_display_name subfield within the merged event.idm.entity.entity.user.managers UDM field.  
\- event.idm.entity.entity.user.managers: Newly mapped manager.id raw log field to userid subfield within the merged event.idm.entity.entity.user.managers UDM field.  
\- event.idm.entity.entity.user.managers.attribute.labels: Newly added key manager_name with value from manager.name raw log field to event.idm.entity.entity.user.managers.attribute.labels UDM field.  
\- event.idm.entity.entity.user.employee_id: Newly mapped employeeNumber raw log field to event.idm.entity.entity.user.employee_id UDM field.  
\- event.idm.entity.entity.user.office_address.country_or_region: Newly mapped attributes.country raw log field to event.idm.entity.entity.user.office_address.country_or_region UDM field.  
\- event.idm.entity.entity.user.office_address.city: Newly mapped attributes.city raw log field to event.idm.entity.entity.user.office_address.city UDM field.  
\- event.idm.entity.entity.user.office_address.name: Newly mapped attributes.location raw log field to event.idm.entity.entity.user.office_address.name UDM field.  
\- event.idm.entity.entity.user.personal_address.name: Newly mapped attributes.streetAddress raw log field to event.idm.entity.entity.user.personal_address.name UDM field.  
\- event.idm.entity.entity.user.phone_numbers: Newly merged values from attributes.workPhone raw log field to event.idm.entity.entity.user.phone_numbers UDM field.  
\- event.idm.entity.entity.user.company_name: Newly mapped attributes.companyName raw log field to event.idm.entity.entity.user.company_name UDM field.  
\- event.idm.entity.entity.user.title: Newly mapped attributes.title raw log field to event.idm.entity.entity.user.title UDM field.  
\- event.idm.entity.entity.user.userid: Newly mapped attributes.userid raw log field to event.idm.entity.entity.user.userid UDM field.  
\- event.idm.entity.entity.user.department: Newly merged values from attributes.department raw log field to event.idm.entity.entity.user.department UDM field.  
\- event.idm.entity.entity.labels: Newly added key-value pairs from `accessdata.id`, `accessdata.name`, `accessdata.displayName`, `accessdata.type`, `accessdata.description`, `accessdata.source.id`, `accessdata.source.name`, `accessdata.privileged`, `accessdata.attribute`, `accessdata.value`, `accessdata.standalone`, `accountdata.id`, `accountdata.name`, `accountdata.accountId`, `accountdata.source.id`, `accountdata.source.name`, `accountdata.source.type`, `accountdata.disabled`, `accountdata.locked`, `accountdata.privileged`, `accountdata.manuallyCorrelated`, `accountdata.created`, `visibleSegment`, `accessCount`, `entitlementCount`, `roleCount`, `accessProfileCount`, `ownsCount`, `tagsCount`, `visibleSegmentCount`, `accountCount`, `sourceCount`, `appCount`, `inactive`, `attributes.active`, `attributes.cloudStatus`, `protected`, `status`, `attributes.managedcompany`, `attributes.futureAction`, `attributes.iscLicense`, `attributes.identityState`, `attributes.internalCloudStatus`, `attributes.cloudLifecycleState`, `pod`, `org`, `modified`, `synced`, `_type`, `source_id`, `_version`, `type`, `attributes.visibleSegments`, `source.name` raw log fields to event.idm.entity.entity.labels.  
\- event.idm.entity.entity.user.attribute.labels: Newly added `isManager`, `employeeType`, `deactivationdate`, `companyPrefix`, `postalCode`, `uid`, `futureDate`, `cloudAuthoritativeSource`, `addressLine1`, `activationdate`, `companyEmaildomain`, `costCenter`, `identificationNumber`, `startDate`, `identityProfile.id`, `identityProfile.name`, `name` raw log fields to event.idm.entity.entity.user.attribute.labels.  
\- Consolidated all mapping for event.idm.read_only_udm.additional.fields, event.idm.read_only_udm.principal.resource.attribute.labels.   
2025-06-23 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Removed mapping of `actor.name` raw log field from `event.idm.read_only_udm.principal.user.user_display_name` UDM field. The field `actor.name` is not suitable for `event.idm.read_only_udm.principal.user.user_display_name` and it should be mapped to `event.idm.read_only_udm.principal.user.userid` instead.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `actor.name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping of `target.name` raw log field from `event.idm.read_only_udm.principal.user.userid` UDM field. `target.name` represents the target of the action, so it should be mapped to `event.idm.read_only_udm.target.user.userid`.  
\- `event.idm.read_only_udm.target.user.userid`: Mapped `target.name` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Mapped `attributes.hostName` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields if `attributes.hostName` is a valid IP else mapped with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`.  
\- Added `has_principal_user` flag check to be true while mapping `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_UPDATE_CONTENT`.   
2025-06-03 |  Enhancement:  
\- Added support to handle new pattern of `event.idm.read_only_udm.metadata.event_timestamp`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `attributes.info`, `synced`, `objects`, `details` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2024-09-13 |  Bug-Fix:  
\- Mapped `attributes.attributeValue` to `target.group.attribute.labels`.  
\- Mapped `attributes.accountName` to `principal.user.attribute.labels`.   
2024-05-03 |  Bug-Fix:  
\- Mapped `created` to `metadata.event_timestamp`.  
\- Mapped `auditClassName` to `metadata.product_event_type`.  
\- Mapped `interface`, `referenceClass`, `referenceId`, `sailPointObjectName`, and `target` to `additional.fields`.  
\- Mapped `serverHost` and `server` to `principal.hostname`, and `principal.asset.hostname`.   
2024-02-21 |  Enhancement:  
\- Aligned `principal.ip to `principal.asset.ip".  
\- Aligned `principal.hostname` to `principal.asset.hostname`.  
\- Aligned `target.ip` to `target.asset.ip`.  
\- Aligned `target.hostname` to `target.asset.hostname`.  
\- Mapped `operation` to `target.attribute.labels`.  
\- When `technicalName` in `PASSWORD_CHANGE_STARTED`, `PASSWORD_ACTION_CHANGE_PASSED`, `PASSWORD_CHANGE_FAILED` or `USER_PASSWORD_UPDATE_PASSED` and `action` in `PasswordChange`, `PasswordChangeSuccess`, `PasswordChangeFailure` or `USER_PASSWORD_UPDATE_PASSED`, then mapped `metadata.event_type` to `USER_CHANGE_PASSWORD`.  
\- When `technicalName` in `IDENTITY_ACCOUNT_REMOVE_PASSED`, `IDENTITY_DELETE_PASSED`, `WORKFLOW_DELETE_PASSED` or `ACCOUNT_DISABLE_PASSED` and `action` in USER_REMOVE_ACCOUNT`, `delete`, `WORKFLOW_DELETED` or `DisableAccount`, then mapped `metadata.event_type` to `USER_DELETION".  
\- When `technicalName` in `PERSONAL_ACCESS_TOKEN_USE_PASSED`, `SAML_ASSERTION_RECEIVE_PASSED`, `SAML_REQUEST_SEND_PASSED`, `SOURCE_ACCOUNT_AGGREGATE_STARTED`, `IDENTITY_PROCESSING_MANUAL_PASSED`, `SOURCE_ENTITLEMENT_AGGREGATE_PASSED` or `MFA_REGISTRATION_REGISTER_PASSED` and `action` in `PERSONAL_ACCESS_TOKEN_USED`, `SAML2-142`, `SAML2-31`, `SOURCE_ACCOUNT_AGGREGATION_STARTED`, `IDENTITY_PROCESSING`, `SOURCE_ENTITLEMENT_AGGREGATION` or `MFA_REGISTRATION_REGISTERED`, then mapped `metadata.event_type` to `USER_RESOURCE_ACCESS`.  
\- When `technicalName` in `AUTHENTICATION_REQUEST_PASSED`, `ACCESS_REQUEST_PROCESSED`, `ACCESS_REQUEST_APPROVED`, `ACCESS_APPROVAL_CREATE_STARTED`, `ACCESS_REQUEST_STARTED` or `SUBSCRIPTION_EXECUTE_STARTED` and `action` in `AUTHENTICATION-105`, `AccessRequestProcessed`, `AccessRequestApproved`, `ACCESS_APPROVAL_STARTED`, `AccessRequestRequested` or `SUBSCRIPTION_EXECUTE_STARTED`, then mapped `metadata.event_type` to `USER_LOGIN`.  
\- When `technicalName` is `CERTIFICATION_ITEM_REMEDIATE_PASSED` and `action` is `remediate`, then mapped `metadata.event_type` to `USER_RESOURCE_UPDATE_PERMISSIONS`.  
\- When `technicalName` in `SOURCE_ACCOUNT_AGGREGATE_PASSED`, `SOURCE_ENTITLEMENT_AGGREGATE_STARTED` or `BRANDING_UPDATE_PASSED` and `action` in `SOURCE_ACCOUNT_AGGREGATION_PASSED`, `SOURCE_ENTITLEMENT_AGGREGATION_STARTED` or `BRANDING_UPDATE`, then mapped `metadata.event_type` to `USER_RESOURCE_UPDATE_CONTENT`.  
\- When `technicalName` in `SUPPORT_LOGIN_TOKEN_AUTHENTICATE_PASSED`, `USER_AUTHENTICATION_STEP_UP_SETUP_PASSED`, `IDENTITY_PROCESSING_SCHEDULED_PASSED`, `MFA_VERIFICATION_FAILED`, `CERTIFICATION_REASSIGN_PASSED`, `WORKITEM_COMPLETE_COMMENTS_ADD_PASSED`, `ACCESS_REQUEST_REJECTED` or `CERTIFICATION_CAMPAIGN_ACTIVATE_PASSED` and `action` in `SUPPORT_LOGIN_AUTHENTICATE`, `USER_STEP_UP_AUTH`, `IDENTITY_PROCESSING`, `MFA_VERIFICATION_FAILED`, `reassign`, `Comment`, `AccessRequestRejected` or `CertificationCampaignActivate`, then mapped `metadata.event_type` to `USER_LOGIN`.  
\- When `technicalName` is `USER_LOGOUT_PASSED` or `CERTIFICATION_SIGNOFF_PASSED` and `action` is `AUTHENTICATION-303` or `signoff`, then mapped `metadata.event_type` to `USER_LOGOUT`.  
\- When `technicalName` in `IDENTITY_PROCESSING_SCHEDULED_STARTED`, `USER_ACTIVATE_PASSED`, `USER_EMAIL_UPDATE_PASSED`, `USER_PHONE_UPDATE_PASSED`, `CERTIFICATION_CAMPAIGN_CREATE_PASSED`, `ACCESS_REQUEST_CANCELLED`, `ACCESS_PROFILE_CREATE_PASSED`, `WORKFLOW_CREATE_PASSED`, `ACCOUNT_ENABLE_PASSED`, `ENTITLEMENT_SET_PASSED` or `ACCOUNT_CREATE_PASSED` and `action` in `IDENTITY_PROCESSING`, `USER_ACTIVATE`, `USER_EMAIL_UPDATE`, `USER_PHONE_UPDATE`, `CertificationCampaignCreate`, `AccessRequestCancelled`, `create`, `WORKFLOW_CREATED`, `EnableAccount`, `SetEntitlement` or `CreateAccount`, then mapped `metadata.event_type` to `USER_CREATION`.  
\- When `technicalName` in `USER_UNLOCK_PASSED`, `SOURCE_ACCOUNT_AGGREGATE_FAILED`, `SAML_ASSERTION_RECEIVE_FAILED`, `IDENTITY_LIFECYCLE_CHANGE_PASSED`, `IDENTITY_STATE_CHANGE_PASSED`, `APP_CREATE_PASSED`, `USER_ROLE_ADMIN_REVOKE_PASSED`, `USER_ROLE_ADMIN_GRANT_PASSED`, `USER_AUTHENTICATION_STEP_UP_SETUP_FAILED`, `ACCESS_PROFILE_UPDATE_PASSED`, `SOURCE_ENTITLEMENT_AGGREGATE_FAILED`, `IAI_ADMIN_CONFIG_UPDATE_PASSED`, `IDENTITY_ATTRIBUTE_VALUE_UPDATE_PASSED` or `APP_UPDATE_PASSED` and `action` in `USER_UNLOCK`, `SOURCE_ACCOUNT_AGGREGATION_FAILED`, `SAML2-166`, `identityLifecycleEvent`, `IdentityStateChange`, `APP_CREATE`, `USER_ADMIN_REVOKE`, `USER_ADMIN_GRANT`, `USER_STEP_UP_AUTH_FAILURE`, `update`, `SOURCE_ENTITLEMENT_AGGREGATION_FAILED`, `IAI_ADMIN_CONFIG_UPDATE_EVENT`, `IdentityAttributeUpdate` or `APP_UPDATE`, then mapped `metadata.event_type` to `USER_CHANGE_PERMISSIONS`.  
\- When `technicalName` is `ROLE_ADD_PASSED` and `action` is `RoleAdd`, then mapped `metadata.event_type` to `USER_RESOURCE_CREATION`.  
\- When `technicalName` in `ACCOUNT_MODIFY_FAILED`, `ACCOUNT_UNLOCK_PASSED`, `ENTITLEMENT_ADD_PASSED`, `ENTITLEMENT_REMOVE_FAILED`, `ACCOUNT_MODIFY_PASSED`, `ENTITLEMENT_REMOVE_PASSED`, `ENTITLEMENT_ADD_FAILED` or `TASK_RESULT_DELETE_PASSED` and `action` in `ModifyAccountFailure`, `UnlockAccount`, `AddEntitlement`, `RemoveEntitlementFailure`, `ModifyAccount`, `RemoveEntitlement`, `AddEntitlementFailure` or `taskResultsPruned`, then mapped `metadata.event_type` to `USER_CHANGE_PERMISSIONS`.  
\- When `technicalName` is `EMAIL_SEND_PASSED` and `action` is `emailSent`, then mapped `metadata.event_type` to `EMAIL_TRANSACTION`.   
2023-12-03 |  Enhancement:  
\- Mapped `org` to `principal.administrative_domain`.  
\- Mapped `pod` to `principal.location.name`.  
\- Mapped `id` to `metadata.product_log_id`.  
\- Mapped `type` to `metadata.product_event_type`.  
\- Mapped `action` to `metadata.description`.  
\- Mapped `actor.name` to `principal.user.user_display_name`.  
\- Mapped `attributes.accountName` to `principal.user.group_identifiers`.  
\- Mapped `target.name` to `principal.user.userid`.  
\- Mapped `stack`, `attributes.interface`, `trackingNumber`, `attributes.accountUuid`, `attributes.previousValue`, `attributes.attributeName`, and `attributes.attributeValue` to `additional.fields`.  
\- Mapped `attributes.sourceId` and `attributes.sourceName` to `principal.labels`.  
\- Mapped `attributes.cloudAppName` to `target.application`.  
\- Mapped `attributes.appId` to `target.asset_id`.  
\- Mapped `attributes.provisioningResult` to `security_result.detection_fields`.  
\- Mapped `attributes.operation` to `security_result.action_details`.  
\- Mapped `technicalName` to `security_result.summary`.  
\- Mapped `name` to `security_result.description`.  
\- Mapped '_version` to `metadata.product_version".  
\- Mapped `status` to `security_result.severity_details`.  
\- Added condition check and on_error for `instant.epochSecond` before mapping.  
\- If `principal.user` and `target.application` are present, then set `metadata.event_type` to `USER_LOGIN` and `extensions.auth_type` to `AUTHTYPE_UNSPECIFIED`.  
\- If `principal.user` is present and `target.application` is not present, then set `metadata.event_type` to `USER_UNCATEGORIZED` and `extensions.auth_type` to `AUTHTYPE_UNSPECIFIED`.   
2022-07-08 |  Enhancement:  
\- Modified mapping for `iiq_target_user_role` from `target.user.role_name` to `target.user.attribute.roles`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

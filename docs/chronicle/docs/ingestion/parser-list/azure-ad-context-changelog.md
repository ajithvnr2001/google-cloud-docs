---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-context-changelog/
title: Change log for AZURE_AD_CONTEXT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:58.238063+00:00
---

# Change log for AZURE_AD_CONTEXT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-context-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_AD_CONTEXT

Date | Changes  
---|---  
2026-08-31 |  Enhancement:  
\- `event.idm.entity.entity.user.attribute.labels` : Removed mapping of `assignedLicense.disabledPlans`, `assignedPlans.capabilityStatus`, `assignedPlans.service`, `assignedPlans.servicePlanId`, `provisionedPlans.service`, `provisionedPlans.provisioningStatus`, `empmanager-src.provisionedPlans.service`, `empmanager-src.provisionedPlans.provisioningStatus`, `empmanager-src.provisionedPlans.capabilityStatus`, `provisionedPlans.capabilityStatus`, `empmanager-src.assignedPlans.servicePlanId`, `empmanager-src.assignedPlans.service`, `empmanager-src.assignedPlans.capabilityStatus`, `empmanager-src.assignedPlans.assignedDateTime` and `assignedPlans.assignedDateTime` raw log fields from the `event.idm.entity.entity.user.attribute.labels` UDM field since it was causing regression issues.   
2026-08-24 |  Enhancement:  
\- `event.idm.entity.entity.user.managers.phone_numbers`: Newly mapped `mobilePhone` raw log field with `event.idm.entity.entity.user.managers.phone_numbers` UDM field.  
\- `event.idm.entity.entity.user.managers.attribute.creation_time`: Newly mapped `createdDateTime` raw log field with `event.idm.entity.entity.user.managers.attribute.creation_time` UDM field.  
\- `event.idm.entity.entity.user.managers.attribute.labels`: Newly mapped `faxNumber`, `onPremisesObjectIdentifier`, and `showInAddressList` raw log fields with `event.idm.entity.entity.user.managers.attribute.labels` UDM field.  
\- `event.idm.entity.relations.entity.asset.attribute.labels`: Newly mapped `accountEnabled`, `odata_type`, `extensionAttributes`, `alternativeSecurityIds.key`, `alternativeSecurityIds.type`, `hostnames`, `physicalIds`, `alternativeNames`, `systemLabels`, `deviceOwnership`, `deviceVersion`, `enrollmentType`, `isCompliant`, `isManaged`, `isManagementRestricted`, `managementType`, `mdmAppId`, `onPremisesLastSyncDateTime`, `onPremisesSyncEnabled`, `profileType`, `registrationDateTime`, and `trustType` raw log fields with `event.idm.entity.relations.entity.asset.attribute.labels` UDM field.   
2026-07-30 |  Enhancement:  
\- `event.idm.entity.entity.user.attribute.labels`: Newly mapped `isLicenseReconciliationNeeded` , `passwordProfile.forceChangePasswordNextSignIn` , `passwordProfile.forceChangePasswordNextSignInWithMfa` , `cloudRealtimeCommunicationInfo.isSipEnabled` , `onPremisesLastSyncDateTime` , `onPremisesObjectIdentifier` , `onPremisesSipInfo.isSipEnabled` , `onPremisesSyncEnabled` , `securityIdentifier` , `signInSessionsValidFromDateTime` , `assignedPlan.assignedDateTime` , `assignedPlan.capabilityStatus` , `assignedPlan.service` , `assignedPlan.servicePlanId` , `provisionedPlan.capabilityStatus` , `provisionedPlan.provisioningStatus` , `provisionedPlan.service`, `showInAddressList`, `preferredDataLocation`, `postalCode`, `identity.issuer` and `identity.issuerAssignedId` raw log fields with `event.idm.entity.entity.user.attribute.labels` UDM field.  
\- `event.idm.entity.entity.user.email_addresses`: Newly mapped `onPremisesSipInfo.sipPrimaryAddress` , `onPremisesUserPrincipalName` and `imAddresses` raw log fields with `event.idm.entity.entity.user.email_addresses` UDM field.   
2026-07-13 |  Enhancement:  
\- `event.idm.entity.entity.user.managers.user_authentication_status`: When `manager.accountEnabled` is true, updated the value of `event.idm.entity.entity.user.managers.user_authentication_status` to ACTIVE.  
\- `event.idm.entity.entity.user.attribute.labels`: Newly mapped `manager.employeeType`, `manager.officeLocation`, `manager.onPremisesImmutableId`, `manager.onPremisesLastSyncDateTime`, `manager.onPremisesSamAccountName`, `manager.onPremisesSyncEnabled`, `manager.passwordPolicies`, `manager.postalCode`, `manager.securityIdentifier`, `manager.signInSessionsValidFromDateTime`, `manager.onPremisesUserPrincipalName`, `businessPhones`, `assignedPlans.servicePlanId`, `assignedPlans.service`, `assignedPlans.capabilityStatus`, `assignedPlans.assignedDateTime`, `disabledPlans`, `assignedLicenses.skuId`, `imAddresses`, `manager.onPremisesExtensionAttributes`, `provisionedPlans.service`, `provisionedPlans.provisioningStatus`, and `provisionedPlans.capabilityStatus` raw log fields with `event.idm.entity.entity.user.attribute.labels` UDM field.  
\- `event.idm.entity.entity.user.managers.attribute.labels`: Newly mapped `manager.odata_type`, `identity.issuerAssignedId`, `identity.issuer`, and `manager.accountEnabled` raw log fields with `event.idm.entity.entity.user.managers.attribute.labels` UDM field.  
\- `event.idm.entity.entity.user.attribute.creation_time`: Newly mapped `manager.createdDateTime` raw log field with `event.idm.entity.entity.user.attribute.creation_time` UDM field.   
2026-05-18 |  Enhancement:  
\- Updated the conditional logic for populating the `accountEnabled` key in `entity.user.attribute.labels` based on the string value of the `accountEnabled` raw field.  
\- `event.idm.entity.entity.user.phone_numbers`: Newly mapped `mobilePhone` raw log field with `event.idm.entity.entity.user.phone_numbers` UDM field.  
\- `event.idm.entity.relations.entity.asset.attribute.labels`: Newly mapped `gopher-device-item.approximateLastSignInDateTime`, `gopher-device-item.id`, raw log fields with `event.idm.entity.relations.entity.asset.attribute.labels` UDM field.  
\- `event.idm.entity.entity.user.user_authentication_status`: If `accountEnabled` is `true`, updated the value of entity.user.user_authentication_status to `ACTIVE`.   
2025-10-03 |  Enhancement:  
\- `event.idm.read_only_udm.entity.user.attribute.labels` : Removed mapping of assignedLicense.disabledPlans, assignedPlans.capabilityStatus, assignedPlans.service, assignedPlans.servicePlanId, and assignedPlans.assignedDateTime raw log fields from the event.idm.read_only_udm.entity.user.attribute.labels UDM field since it was causing regression issues in other parsers.   
2025-07-31 |  Enhancement:  
\- `event.idm.entity.entity.user.attribute.labels` : Newly mapped Added support for parsing the `assignedLicenses.skuId`, `assignedLicenses.disabledPlans`, `assignedPlans.capabilityStatus`, `assignedPlan.service`, `assignedPlan.servicePlanId`, `assignedPlan.assignedDateTime` and externalUserState raw log fields with `event.idm.entity.entity.user.attribute.labels` UDM field.   
2025-05-16 |  Enhancement:  
\- event.idm.entity.metadata.event_metadata.log_type : Newly Mapped `AZURE_AD_CONTEXT` value to `event.idm.entity.metadata.event_metadata.log_type` UDM Field.   
2025-04-10 |  Enhancement:  
\- relation_entity.entity.hostname: Newly mapped `gopher-device.displayName` raw log field with `relation_entity.entity.hostname` and `relation_entity.entity.asset.hostname` UDM field.   
2025-02-14 |  Enhancement:  
-Mapping `IsOnCloudAccount` to `user.attribute.labels`.   
2024-11-13 |  Enhancement:  
\- Mapped `manager.accountEnabled` to `entity.user.managers.attribute.labels` and `entity.user.managers.user_authentication_status`.   
2024-05-02 |  Bug-fix:  
\- Added checks for `accountEnabled` field to parse correct value to `entity.user.attribute.labels.value` field.   
2024-04-29 |  Enhancement:  
\- Mapped `officeLocation` to `entity.location.name`.  
\- Mapped `extension_wfc_groupDescription`, `extension_wfc_execDescription`, `extension_wfc_orgDescription`, `extension_wfc_AccountingUnitName`, and `extension_wfc_AccountType` to `entity.labels`.   
2024-03-14 |  Enhancement:  
\- Mapped `onPremisesImmutableId` to `entity.user.attribute.labels`.  
\- Mapped `gopher-manager.onPremisesImmutableId` to `entity.user.attribute.labels`.   
2024-01-12 |  Bug-Fix:  
\- Changed `empmanager-src.usageLocation` mapping from `entity.user.personal_address.country_or_region` to `entity.user.attribute.labels`.   
2023-11-24 |  Enchancement  
\- Mapped `employeeType` attribute to `entity.user.attribute.labels`.  
\- Dropped malformed JSON logs with tag `TAG_MALFORMED_MESSAGE`.   
2023-10-25 |  Bug-Fix  
\- Added null checks and an `on_error` check for absent values.   
2023-09-25 |  Enhancement  
\- Added rename function, instead of replace, to map `group.displayName` to `relation_entity.entity.group.group_display_name`.  
\- Mapped `country` to `user.personal_address.country_or_region`. If `country` not present, mapped `usageLocation` to `user.personal_address.country_or_region`.   
2023-02-09 |  Enhancement  
\- Added null check before mapping data for field `onPremisesDistinguishedName`.  
\- Added gsub to extract email address from field `proxyAddresses`.   
2023-01-23 |  Enhancement:  
\- Mapped `onPremisesExtensionAttributes.extensionAttribute4` to `entity.entity.user.attribute.labels` if `onPremisesExtensionAttributes.extensionAttribute4` is `Employee`.  
\- Added gsub for `onPremisesDistinguishedName` to remove extra backslashes.   
2022-12-15 |  Bug-Fix:  
\- Mapped `mailNickname` to `entity.user.attribute.labels`.  
\- Mapped only `country_n_code` to `user.manager.personal_address.country_or_region` if `empmanager-src.usageLocation` is null.   
2022-09-19 |  Bug-Fix:  
\- Mapped `entity.user.attribute.roles` to `ADMINISTRATOR` where OU includes `Admin`  
2022-08-11 |  Enhancement:  
\- Mapped `accountEnabled` to `user.attribute.labels`  
2022-05-16 |  Enhancement: Added mappings for following fields:  
\- `createdDateTime` mapped to `entity.user.attribute.creation_time`  
\- `accountEnabled` mapped to `entity.user.user_authentication_status`  
2022-05-09 |  Enhancement- Mapped fields starting with extension_GUID_sbuxXXXXXXX to user.attribute.labels or manager.attribute.labels, depending on its occurrence in the log.   
2022-03-24 |  Enhancement-Added few missing fields  
onPremisesSamAccountName, onPremisesDomainName, onPremisesDistinguishedName mapped to entity.user.attribute.labels.  
For signInType, userPrincipalName mapped to entity.user.attribute.labels.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

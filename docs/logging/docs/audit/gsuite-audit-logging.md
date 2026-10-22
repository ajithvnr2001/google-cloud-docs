---
url: https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging/
title: Audit logs for Google Workspace \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:04.252499+00:00
---

# Audit logs for Google Workspace  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Audit logs for Google Workspace Stay organized with collections  Save and categorize content based on your preferences. 

Google Workspace audit logs in Cloud Audit Logs let you track administrative and user actions across your organization to help you answer "Who did what, where, and when?". You can share your Google Workspace audit logs with Google Cloud to store, analyze, monitor, and alert on your Google Workspace data.

For instructions on viewing and managing your Google Workspace audit logs, see [View and manage audit logs for Google Workspace](https://docs.cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs).

## Overview

Audit logs for Google Workspace are available for Cloud Identity, Cloud Identity Premium, and all Google Workspace customers.

If you've [enabled Google Workspace data sharing](https://docs.cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs) with Google Cloud, then audit logs are always enabled for Google Workspace.

Disabling Google Workspace data sharing stops new Google Workspace audit log events from being sent to Google Cloud. Any existing logs remain through their [default retention periods](https://docs.cloud.google.com/logging/quotas#logs_retention_periods), unless you have configured [custom retention](https://docs.cloud.google.com/logging/docs/buckets#custom-retention) to retain your logs for a longer period.

If you don't enable Google Workspace data sharing with Google Cloud, then you can't see audit logs for Google Workspace in Google Cloud.

**Note:** Some Enterprise Groups Audit membership changes automatically populate the `principalEmail` field in the audit log with `cloud-support@google.com`. For example, an audit log might show `cloud-support@google.com` as the principal removing a user from the group, when the removal of the user is automatic due to the expiration of a user's membership.

## Types of audit logs

[Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) contain log entries for API calls or other actions that modify the configuration or metadata of resources. For example, these logs record when users create VM instances or change Identity and Access Management (IAM) permissions.

[Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access) contain API calls that read the configuration or metadata of resources, as well as user-driven API calls that create, modify, or read user-provided resource data. Data Access audit logs don't record the data-access operations on resources that are publicly shared (available to All Users or All Authenticated Users) or that can be accessed without logging into Google Cloud, Google Workspace, Cloud Identity, or Drive Enterprise account.

## Google Workspace services forwarding audit logs to Google Cloud

Google Workspace provides the following audit logs at the Google Cloud organization level:

  * [**Access Transparency**](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/understanding-workspace-logs): Access Transparency logs provide a record of actions when Google personnel access customer content in your Google Workspace resources. In contrast to Access Transparency, Cloud Audit Logs record the actions that members of your Google Cloud organization have taken in your Google Cloud resources.

For more information about the structure of Access Transparency logs and the types of accesses that are logged, see [Log field descriptions](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs#axt-log-entry-sample).

  * [**Google Workspace Admin Audit**](https://developers.google.com/admin-sdk/reports/v1/reference/activity-ref-appendix-a/admin-event-names): Admin Audit logs provide a record of actions performed in your Google Admin console. For example, you can see when an administrator added a user or turned on a Google Workspace service.

Admin Audit writes Admin Activity audit logs only.

**Note:** Unless you use the Google Admin console, changes to Group settings are captured in the Google Workspace Enterprise Groups Audit logs. When you use the Google Admin console, changes to Group settings are captured in the Google Workspace Admin Audit logs. For example, if you changed a Group email address in groups.google.com, then those changes are captured in Google Workspace Enterprise Groups Audit logs.
  * [**Google Workspace Enterprise Groups Audit**](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/groups-enterprise): Enterprise Groups Audit logs provide a record of actions performed on groups and group memberships. For example, you can see when an administrator added a user or when a group owner deleted their group.

Enterprise Groups Audit writes Admin Activity audit logs only.

  * [**Google Workspace Login Audit**](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/login): Login Audit logs track user sign-ins to your domain. These logs only record the login event. They don't record which system was used to perform the login action.

Login Audit writes Data Access audit logs only.

  * [**Google Workspace OAuth Token Audit**](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/token): OAuth Token Audit logs track which users are using which third-party mobile or web applications in your domain. For example, when a user opens a Google Workspace Marketplace app, the log records the name of the app and the person using it. The log also records each time a third-party application is authorized to access Google Account data, such as Google Contacts, Calendar, and Drive files (Google Workspace only).

OAuth Token Audit writes both Admin Activity and Data Access audit logs.

  * [**Google Workspace SAML Audit**](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/saml): SAML Audit logs track users' successful and failed sign-ins to SAML applications. Entries usually appear within an hour of the user action.

SAML Audit writes Data Access audit logs only.




## Service-specific information

Details for each Google Workspace service's audit logs are as follows:

### Google Workspace Admin Audit

Google Workspace Admin Audit audit logs use the resource type `audited_resource` for all audit logs.

Google Workspace Admin Audit audit logs use the service name `admin.googleapis.com`.

Google Workspace Admin Audit writes Admin Activity audit logs only. The following are the audited operations:

Activity type | `AuditLog.method_name`  
---|---  
AI_CLASSIFICATION_SETTINGS | `google.admin.AdminService.aiClassificationInsufficientTrainingExamples`  
`google.admin.AdminService.aiClassificationModelLowScore`  
`google.admin.AdminService.aiClassificationNewModelReady`  
  
[ALERT_CENTER](https://developers.google.com/admin-sdk/alertcenter/reference/rest/v1beta1/alerts) | `google.admin.AdminService.alertCenterBatchDeleteAlerts`  
`google.admin.AdminService.alertCenterBatchUndeleteAlerts`  
`google.admin.AdminService.alertCenterCreateAlert`  
`google.admin.AdminService.alertCenterCreateFeedback`  
`google.admin.AdminService.alertCenterDeleteAlert`  
`google.admin.AdminService.alertCenterGetAlertMetadata`  
`google.admin.AdminService.alertCenterGetCustomerSettings`  
`google.admin.AdminService.alertCenterGetSitLink`  
`google.admin.AdminService.alertCenterListChange`  
`google.admin.AdminService.alertCenterListFeedback`  
`google.admin.AdminService.alertCenterListRelatedAlerts`  
`google.admin.AdminService.alertCenterUndeleteAlert`  
`google.admin.AdminService.alertCenterUpdateAlert`  
`google.admin.AdminService.alertCenterUpdateAlertMetadata`  
`google.admin.AdminService.alertCenterUpdateCustomerSettings`  
`google.admin.AdminService.alertCenterView`  
  
[APPLICATION_SETTINGS](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-application-settings) | `google.admin.AdminService.changeApplicationSetting`  
`google.admin.AdminService.createApplicationSetting`  
`google.admin.AdminService.deleteApplicationSetting`  
`google.admin.AdminService.reorderGroupBasedPoliciesEvent`  
`google.admin.AdminService.gplusPremiumFeatures`  
`google.admin.AdminService.createManagedConfiguration`  
`google.admin.AdminService.deleteManagedConfiguration`  
`google.admin.AdminService.updateManagedConfiguration`  
`google.admin.AdminService.flashlightEduNonFeaturedServicesSelected`  
  
[CALENDAR_SETTINGS](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-calendar-settings) | `google.admin.AdminService.createBuilding`  
`google.admin.AdminService.deleteBuilding`  
`google.admin.AdminService.updateBuilding`  
`google.admin.AdminService.createCalendarResource`  
`google.admin.AdminService.deleteCalendarResource`  
`google.admin.AdminService.createCalendarResourceFeature`  
`google.admin.AdminService.deleteCalendarResourceFeature`  
`google.admin.AdminService.updateCalendarResourceFeature`  
`google.admin.AdminService.renameCalendarResource`  
`google.admin.AdminService.updateCalendarResource`  
`google.admin.AdminService.changeCalendarSetting`  
`google.admin.AdminService.cancelCalendarEvents`  
`google.admin.AdminService.releaseCalendarResources`  
  
[CHAT_SETTINGS](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-chat-settings) | `google.admin.AdminService.meetInteropCreateGateway`  
`google.admin.AdminService.meetInteropDeleteGateway`  
`google.admin.AdminService.meetInteropModifyGateway`  
`google.admin.AdminService.changeChatSetting`  
  
[CHROME_OS_SETTINGS](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-chrome-os-settings) | `google.admin.AdminService.changeChromeOsAndroidApplicationSetting`  
`google.admin.AdminService.changeChromeOsApplicationSetting`  
`google.admin.AdminService.sendChromeOsDeviceCommand`  
`google.admin.AdminService.changeChromeOsDeviceAnnotation`  
`google.admin.AdminService.changeChromeOsDeviceSetting`  
`google.admin.AdminService.changeChromeOsDeviceState`  
`google.admin.AdminService.changeChromeOsPublicSessionSetting`  
`google.admin.AdminService.insertChromeOsPrinter`  
`google.admin.AdminService.deleteChromeOsPrinter`  
`google.admin.AdminService.updateChromeOsPrinter`  
`google.admin.AdminService.changeChromeOsSetting`  
`google.admin.AdminService.changeChromeOsUserSetting`  
`google.admin.AdminService.removeChromeOsApplicationSettings`  
  
[CONTACTS_SETTINGS](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-contacts-settings) | `google.admin.AdminService.changeContactsSetting`  
[DELEGATED_ADMIN_SETTINGS](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-delegated-admin-settings) | `google.admin.AdminService.assignRole`  
`google.admin.AdminService.createRole`  
`google.admin.AdminService.deleteRole`  
`google.admin.AdminService.addPrivilege`  
`google.admin.AdminService.removePrivilege`  
`google.admin.AdminService.renameRole`  
`google.admin.AdminService.updateRole`  
`google.admin.AdminService.unassignRole`  
  
DEVICE_SETTINGS | `google.admin.AdminService.deleteDevice`  
`google.admin.AdminService.moveDeviceToOrgUnit`  
[DOCS_SETTINGS](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-docs-settings) | `google.admin.AdminService.transferDocumentOwnership`  
`google.admin.AdminService.driveDataRestore`  
`google.admin.AdminService.changeDocsSetting`  
  
[DOMAIN_SETTINGS](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-domain-settings) | `google.admin.AdminService.changeAccountAutoRenewal`  
`google.admin.AdminService.addApplication`  
`google.admin.AdminService.addApplicationToWhitelist`  
`google.admin.AdminService.changeAdvertisementOption`  
`google.admin.AdminService.createAlert`  
`google.admin.AdminService.changeAlertCriteria`  
`google.admin.AdminService.deleteAlert`  
`google.admin.AdminService.alertReceiversChanged`  
`google.admin.AdminService.renameAlert`  
`google.admin.AdminService.alertStatusChanged`  
`google.admin.AdminService.addDomainAlias`  
`google.admin.AdminService.removeDomainAlias`  
`google.admin.AdminService.skipDomainAliasMx`  
`google.admin.AdminService.verifyDomainAliasMx`  
`google.admin.AdminService.verifyDomainAlias`  
`google.admin.AdminService.toggleOauthAccessToAllApis`  
`google.admin.AdminService.toggleAllowAdminPasswordReset`  
`google.admin.AdminService.enableApiAccess`  
`google.admin.AdminService.authorizeApiClientAccess`  
`google.admin.AdminService.removeApiClientAccess`  
`google.admin.AdminService.chromeLicensesRedeemed`  
`google.admin.AdminService.toggleAutoAddNewService`  
`google.admin.AdminService.changePrimaryDomain`  
`google.admin.AdminService.changeWhitelistSetting`  
`google.admin.AdminService.communicationPreferencesSettingChange`  
`google.admin.AdminService.changeConflictAccountAction`  
`google.admin.AdminService.enableFeedbackSolicitation`  
`google.admin.AdminService.toggleContactSharing`  
`google.admin.AdminService.createPlayForWorkToken`  
`google.admin.AdminService.toggleUseCustomLogo`  
`google.admin.AdminService.changeCustomLogo`  
`google.admin.AdminService.changeDataLocalizationForRussia`  
`google.admin.AdminService.changeDataLocalizationSetting`  
`google.admin.AdminService.changeDataProtectionOfficerContactInfo`  
`google.admin.AdminService.deletePlayForWorkToken`  
`google.admin.AdminService.viewDnsLoginDetails`  
`google.admin.AdminService.changeDomainDefaultLocale`  
`google.admin.AdminService.changeDomainDefaultTimezone`  
`google.admin.AdminService.changeDomainName`  
`google.admin.AdminService.toggleEnablePreReleaseFeatures`  
`google.admin.AdminService.changeDomainSupportMessage`  
`google.admin.AdminService.addTrustedDomains`  
`google.admin.AdminService.removeTrustedDomains`  
`google.admin.AdminService.changeEduType`  
`google.admin.AdminService.toggleEnableOauthConsumerKey`  
`google.admin.AdminService.toggleSsoEnabled`  
`google.admin.AdminService.toggleSsl`  
`google.admin.AdminService.changeEuRepresentativeContactInfo`  
`google.admin.AdminService.generateTransferToken`  
`google.admin.AdminService.changeLoginBackgroundColor`  
`google.admin.AdminService.changeLoginBorderColor`  
`google.admin.AdminService.changeLoginActivityTrace`  
`google.admin.AdminService.playForWorkEnroll`  
`google.admin.AdminService.playForWorkUnenroll`  
`google.admin.AdminService.mxRecordVerificationClaim`  
`google.admin.AdminService.toggleNewAppFeatures`  
`google.admin.AdminService.toggleUseNextGenControlPanel`  
`google.admin.AdminService.uploadOauthCertificate`  
`google.admin.AdminService.regenerateOauthConsumerSecret`  
`google.admin.AdminService.toggleOpenIdEnabled`  
`google.admin.AdminService.changeOrganizationName`  
`google.admin.AdminService.toggleOutboundRelay`  
`google.admin.AdminService.changePasswordMaxLength`  
`google.admin.AdminService.changePasswordMinLength`  
`google.admin.AdminService.updateDomainPrimaryAdminEmail`  
`google.admin.AdminService.enableServiceOrFeatureNotifications`  
`google.admin.AdminService.removeApplication`  
`google.admin.AdminService.removeApplicationFromWhitelist`  
`google.admin.AdminService.changeRenewDomainRegistration`  
`google.admin.AdminService.changeResellerAccess`  
`google.admin.AdminService.ruleActionsChanged`  
`google.admin.AdminService.createRule`  
`google.admin.AdminService.changeRuleCriteria`  
`google.admin.AdminService.deleteRule`  
`google.admin.AdminService.renameRule`  
`google.admin.AdminService.ruleStatusChanged`  
`google.admin.AdminService.addSecondaryDomain`  
`google.admin.AdminService.removeSecondaryDomain`  
`google.admin.AdminService.skipSecondaryDomainMx`  
`google.admin.AdminService.verifySecondaryDomainMx`  
`google.admin.AdminService.verifySecondaryDomain`  
`google.admin.AdminService.updateDomainSecondaryEmail`  
`google.admin.AdminService.changeSsoSettings`  
`google.admin.AdminService.generatePin`  
`google.admin.AdminService.updateRule`  
  
[EMAIL_SETTINGS](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-gmail-settings) | `google.admin.AdminService.dropFromQuarantine`  
`google.admin.AdminService.emailLogSearch`  
`google.admin.AdminService.emailUndelete`  
`google.admin.AdminService.changeEmailSetting`  
`google.admin.AdminService.changeGmailSetting`  
`google.admin.AdminService.createGmailSetting`  
`google.admin.AdminService.deleteGmailSetting`  
`google.admin.AdminService.rejectFromQuarantine`  
`google.admin.AdminService.releaseFromQuarantine`  
  
[GROUP_SETTINGS](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-group-settings) | `google.admin.AdminService.createGroup`  
`google.admin.AdminService.deleteGroup`  
`google.admin.AdminService.changeGroupDescription`  
`google.admin.AdminService.groupListDownload`  
`google.admin.AdminService.addGroupMember`  
`google.admin.AdminService.removeGroupMember`  
`google.admin.AdminService.updateGroupMember`  
`google.admin.AdminService.updateGroupMemberDeliverySettings`  
`google.admin.AdminService.updateGroupMemberDeliverySettingsCanEmailOverride`  
`google.admin.AdminService.groupMemberBulkUpload`  
`google.admin.AdminService.groupMembersDownload`  
`google.admin.AdminService.changeGroupEmail`  
`google.admin.AdminService.changeGroupName`  
`google.admin.AdminService.changeGroupSetting`  
`google.admin.AdminService.whitelistedGroupsUpdated`  
  
LABELS | `google.admin.AdminService.labelDeleted`  
`google.admin.AdminService.labelDisabled`  
`google.admin.AdminService.labelReenabled`  
`google.admin.AdminService.labelPermissionUpdated`  
`google.admin.AdminService.labelPermissionDeleted`  
`google.admin.AdminService.labelPublished`  
`google.admin.AdminService.labelCreated`  
`google.admin.AdminService.labelUpdated`  
  
[LICENSES_SETTINGS](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-licenses-settings) | `google.admin.AdminService.orgUsersLicenseAssignment`  
`google.admin.AdminService.orgAllUsersLicenseAssignment`  
`google.admin.AdminService.userLicenseAssignment`  
`google.admin.AdminService.changeLicenseAutoAssign`  
`google.admin.AdminService.userLicenseReassignment`  
`google.admin.AdminService.orgLicenseRevoke`  
`google.admin.AdminService.userLicenseRevoke`  
`google.admin.AdminService.updateDynamicLicense`  
`google.admin.AdminService.licenseUsageUpdate`  
  
[MOBILE_SETTINGS](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-mobile-settings) | `google.admin.AdminService.actionCancelled`  
`google.admin.AdminService.actionRequested`  
`google.admin.AdminService.addMobileCertificate`  
`google.admin.AdminService.companyDevicesBulkCreation`  
`google.admin.AdminService.companyOwnedDeviceBlocked`  
`google.admin.AdminService.companyDeviceDeletion`  
`google.admin.AdminService.companyOwnedDeviceUnblocked`  
`google.admin.AdminService.companyOwnedDeviceWiped`  
`google.admin.AdminService.changeMobileApplicationPermissionGrant`  
`google.admin.AdminService.changeMobileApplicationPriorityOrder`  
`google.admin.AdminService.removeMobileApplicationFromWhitelist`  
`google.admin.AdminService.changeMobileApplicationSettings`  
`google.admin.AdminService.addMobileApplicationToWhitelist`  
`google.admin.AdminService.mobileDeviceApprove`  
`google.admin.AdminService.mobileDeviceBlock`  
`google.admin.AdminService.mobileDeviceDelete`  
`google.admin.AdminService.mobileDeviceWipe`  
`google.admin.AdminService.changeMobileSetting`  
`google.admin.AdminService.changeAdminRestrictionsPin`  
`google.admin.AdminService.changeMobileWirelessNetwork`  
`google.admin.AdminService.addMobileWirelessNetwork`  
`google.admin.AdminService.removeMobileWirelessNetwork`  
`google.admin.AdminService.changeMobileWirelessNetworkPassword`  
`google.admin.AdminService.removeMobileCertificate`  
`google.admin.AdminService.enrollForGoogleDeviceManagement`  
`google.admin.AdminService.useGoogleMobileManagement`  
`google.admin.AdminService.useGoogleMobileManagementForNonIos`  
`google.admin.AdminService.useGoogleMobileManagementForIos`  
`google.admin.AdminService.mobileAccountWipe`  
`google.admin.AdminService.mobileDeviceCancelWipeThenApprove`  
`google.admin.AdminService.mobileDeviceCancelWipeThenBlock`  
  
[ORG_SETTINGS](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-org-settings) | `google.admin.AdminService.chromeLicensesEnabled`  
`google.admin.AdminService.chromeApplicationLicenseReservationCreated`  
`google.admin.AdminService.chromeApplicationLicenseReservationDeleted`  
`google.admin.AdminService.chromeApplicationLicenseReservationUpdated`  
`google.admin.AdminService.assignCustomLogo`  
`google.admin.AdminService.unassignCustomLogo`  
`google.admin.AdminService.createEnrollmentToken`  
`google.admin.AdminService.revokeEnrollmentToken`  
`google.admin.AdminService.chromeLicensesAllowed`  
`google.admin.AdminService.createOrgUnit`  
`google.admin.AdminService.removeOrgUnit`  
`google.admin.AdminService.editOrgUnitDescription`  
`google.admin.AdminService.moveOrgUnit`  
`google.admin.AdminService.editOrgUnitName`  
`google.admin.AdminService.toggleServiceEnabled`  
  
[SECURITY_INVESTIGATION](https://support.google.com/a/answer/7575955) | `google.admin.AdminService.securityInvestigationAction`  
`google.admin.AdminService.securityInvestigationActionCancellation`  
`google.admin.AdminService.securityInvestigationActionCompletion`  
`google.admin.AdminService.securityInvestigationActionRetry`  
`google.admin.AdminService.securityInvestigationActionVerificationConfirmation`  
`google.admin.AdminService.securityInvestigationActionVerificationRequest`  
`google.admin.AdminService.securityInvestigationActionVerificationRequestExpiration`  
`google.admin.AdminService.securityInvestigationChartCreate`  
`google.admin.AdminService.securityInvestigationContentAccess`  
`google.admin.AdminService.securityInvestigationDownloadAttachment`  
`google.admin.AdminService.securityInvestigationExportActionResults`  
`google.admin.AdminService.securityInvestigationExportQuery`  
`google.admin.AdminService.securityInvestigationObjectCreateDraftInvestigation`  
`google.admin.AdminService.securityInvestigationObjectDeleteInvestigation`  
`google.admin.AdminService.securityInvestigationObjectDuplicateInvestigation`  
`google.admin.AdminService.securityInvestigationObjectOwnershipTransfer`  
`google.admin.AdminService.securityInvestigationObjectSaveInvestigation`  
`google.admin.AdminService.securityInvestigationObjectUpdateDirectSharing`  
`google.admin.AdminService.securityInvestigationObjectUpdateLinkSharing`  
`google.admin.AdminService.securityInvestigationQuery`  
`google.admin.AdminService.securityInvestigationSettingUpdate`  
  
SECURITY_SETTINGS | `google.admin.AdminService.addToTrustedOauth2Apps`  
`google.admin.AdminService.allowAspWithout2Sv`  
`google.admin.AdminService.allowServiceForOauth2Access`  
`google.admin.AdminService.allowStrongAuthentication`  
`google.admin.AdminService.blockOnDeviceAccess`  
`google.admin.AdminService.changeAllowedTwoStepVerificationMethods`  
`google.admin.AdminService.changeAppAccessSettingsCollectionId`  
`google.admin.AdminService.changeCaaAppAssignments`  
`google.admin.AdminService.changeCaaDefaultAssignments`  
`google.admin.AdminService.changeCaaErrorMessage`  
`google.admin.AdminService.changeSessionLength`  
`google.admin.AdminService.changeTwoStepVerificationEnrollmentPeriodDuration`  
`google.admin.AdminService.changeTwoStepVerificationFrequency`  
`google.admin.AdminService.changeTwoStepVerificationGracePeriodDuration`  
`google.admin.AdminService.changeTwoStepVerificationStartDate`  
`google.admin.AdminService.disallowServiceForOauth2Access`  
`google.admin.AdminService.enableNonAdminUserPasswordRecovery`  
`google.admin.AdminService.enforceStrongAuthentication`  
`google.admin.AdminService.removeFromTrustedOauth2Apps`  
`google.admin.AdminService.sessionControlSettingsChange`  
`google.admin.AdminService.toggleCaaEnablement`  
`google.admin.AdminService.trustDomainOwnedOauth2Apps`  
`google.admin.AdminService.unblockOnDeviceAccess`  
`google.admin.AdminService.untrustDomainOwnedOauth2Apps`  
`google.admin.AdminService.updateErrorMsgForRestrictedOauth2Apps`  
`google.admin.AdminService.weakProgrammaticLoginSettingsChanged`  
  
[SITES_SETTINGS](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-sites-settings) | `google.admin.AdminService.addWebAddress`  
`google.admin.AdminService.deleteWebAddress`  
`google.admin.AdminService.changeSitesSetting`  
`google.admin.AdminService.changeSitesWebAddressMappingUpdates`  
`google.admin.AdminService.viewSiteDetails`  
  
[USER_SETTINGS](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-user-settings) | `google.admin.AdminService.delete2SvScratchCodes`  
`google.admin.AdminService.generate2SvScratchCodes`  
`google.admin.AdminService.revoke3LoDeviceTokens`  
`google.admin.AdminService.revoke3LoToken`  
`google.admin.AdminService.addRecoveryEmail`  
`google.admin.AdminService.addRecoveryPhone`  
`google.admin.AdminService.grantAdminPrivilege`  
`google.admin.AdminService.revokeAdminPrivilege`  
`google.admin.AdminService.revokeAsp`  
`google.admin.AdminService.toggleAutomaticContactSharing`  
`google.admin.AdminService.bulkUpload`  
`google.admin.AdminService.bulkUploadNotificationSent`  
`google.admin.AdminService.cancelUserInvite`  
`google.admin.AdminService.changeUserCustomField`  
`google.admin.AdminService.changeUserExternalId`  
`google.admin.AdminService.changeUserGender`  
`google.admin.AdminService.changeUserIm`  
`google.admin.AdminService.enableUserIpWhitelist`  
`google.admin.AdminService.changeUserKeyword`  
`google.admin.AdminService.changeUserLanguage`  
`google.admin.AdminService.changeUserLocation`  
`google.admin.AdminService.changeUserOrganization`  
`google.admin.AdminService.changeUserPhoneNumber`  
`google.admin.AdminService.changeRecoveryEmail`  
`google.admin.AdminService.changeRecoveryPhone`  
`google.admin.AdminService.changeUserRelation`  
`google.admin.AdminService.changeUserAddress`  
`google.admin.AdminService.createEmailMonitor`  
`google.admin.AdminService.createDataTransferRequest`  
`google.admin.AdminService.grantDelegatedAdminPrivileges`  
`google.admin.AdminService.deleteAccountInfoDump`  
`google.admin.AdminService.deleteEmailMonitor`  
`google.admin.AdminService.deleteMailboxDump`  
`google.admin.AdminService.changeFirstName`  
`google.admin.AdminService.gmailResetUser`  
`google.admin.AdminService.changeLastName`  
`google.admin.AdminService.mailRoutingDestinationAdded`  
`google.admin.AdminService.mailRoutingDestinationRemoved`  
`google.admin.AdminService.addNickname`  
`google.admin.AdminService.removeNickname`  
`google.admin.AdminService.changePassword`  
`google.admin.AdminService.changePasswordOnNextLogin`  
`google.admin.AdminService.downloadPendingInvitesList`  
`google.admin.AdminService.removeRecoveryEmail`  
`google.admin.AdminService.removeRecoveryPhone`  
`google.admin.AdminService.requestAccountInfo`  
`google.admin.AdminService.requestMailboxDump`  
`google.admin.AdminService.resendUserInvite`  
`google.admin.AdminService.resetSigninCookies`  
`google.admin.AdminService.securityKeyRegisteredForUser`  
`google.admin.AdminService.revokeSecurityKey`  
`google.admin.AdminService.userInvite`  
`google.admin.AdminService.viewTempPassword`  
`google.admin.AdminService.turnOff2StepVerification`  
`google.admin.AdminService.unblockUserSession`  
`google.admin.AdminService.unenrollUserFromTitanium`  
`google.admin.AdminService.archiveUser`  
`google.admin.AdminService.updateBirthdate`  
`google.admin.AdminService.createUser`  
`google.admin.AdminService.deleteUser`  
`google.admin.AdminService.downgradeUserFromGplus`  
`google.admin.AdminService.userEnrolledInTwoStepVerification`  
`google.admin.AdminService.downloadUserlistCsv`  
`google.admin.AdminService.moveUserToOrgUnit`  
`google.admin.AdminService.userPutInTwoStepVerificationGracePeriod`  
`google.admin.AdminService.renameUser`  
`google.admin.AdminService.unenrollUserFromStrongAuth`  
`google.admin.AdminService.suspendUser`  
`google.admin.AdminService.unarchiveUser`  
`google.admin.AdminService.undeleteUser`  
`google.admin.AdminService.unsuspendUser`  
`google.admin.AdminService.upgradeUserToGplus`  
`google.admin.AdminService.usersBulkUpload`  
`google.admin.AdminService.usersBulkUploadNotificationSent`  
  
### Google Workspace Enterprise Groups Audit

Google Workspace Enterprise Groups Audit audit logs use the resource type `audited_resource` for all audit logs.

Google Workspace Enterprise Groups Audit audit logs use the service name `cloudidentity.googleapis.com`.

Google Workspace Enterprise Groups Audit writes Admin Activity audit logs only. The following are the audited operations:

Audit logs category  |  `AuditLog.method_name`  
---|---  
Admin Activity audit logs  | `google.apps.cloudidentity.groups.v1.GroupsService.UpdateGroup`  
`google.apps.cloudidentity.groups.v1.MembershipsService.UpdateMembership`  
  
### Google Workspace Login Audit

All Google Workspace Login Audit audit logs use the resource type `audited_resource`.

Google Workspace Login Audit audit logs use the service name `login.googleapis.com`.

Google Workspace Login Audit writes Data Access audit logs only. The following are the audited operations; [log samples](https://docs.cloud.google.com/logging/docs/audit/gsuite-login-samples) for each operation are available.

Audit logs category | `AuditLog.method_name`  
---|---  
Data Access audit logs  | `google.login.LoginService.2svDisable`   
`google.login.LoginService.2svEnroll`   
`google.login.LoginService.accountDisabledPasswordLeak`   
`google.login.LoginService.accountDisabledGeneric`   
`google.login.LoginService.accountDisabledSpammingThroughRelay`   
`google.login.LoginService.accountDisabledSpamming`   
`google.login.LoginService.accountDisabledHijacked`   
`google.login.LoginService.emailForwardingOutOfDomain`   
`google.login.LoginService.govAttackWarning`   
`google.login.LoginService.loginChallenge`   
`google.login.LoginService.loginFailure`   
`google.login.LoginService.loginVerification`   
`google.login.LoginService.logout`   
`google.login.LoginService.loginSuccess`   
`google.login.LoginService.passkeyEnrolled`   
`google.login.LoginService.passkeyRemoved`   
`google.login.LoginService.passwordEdit`   
`google.login.LoginService.recoveryEmailEdit`   
`google.login.LoginService.recoveryPhoneEdit`   
`google.login.LoginService.recoverySecretQaEdit`   
`google.login.LoginService.riskySensitiveActionAllowed`   
`google.login.LoginService.riskySensitiveActionBlocked`   
`google.login.LoginService.suspiciousLogin`   
`google.login.LoginService.suspiciousLoginLessSecureApp`   
`google.login.LoginService.suspiciousProgrammaticLogin`   
`google.login.LoginService.titaniumEnroll`   
`google.login.LoginService.titaniumUnenroll`   
  
  
### Google Workspace OAuth Token Audit

Google Workspace OAuth Token Audit audit logs use the resource type `audited_resource` for all audit logs.

Google Workspace OAuth Token Audit audit logs use the service name `oauth2.googleapis.com`.

Google Workspace OAuth Token Audit writes both Admin Activity and Data Access audit logs. The following are the audited operations:

Audit logs category  |  `AuditLog.method_name`  
---|---  
Admin Activity audit logs  | `google.identity.oauth2.Deny`  
`google.identity.oauth2.GetToken`  
`google.identity.oauth2.Request`  
`google.identity.oauth2.RevokeToken`  
  
Data Access audit logs | `google.identity.oauth2.GetTokenInfo`   
  
  
### Google Workspace SAML Audit

Google Workspace SAML Audit audit logs use the resource type `audited_resource` for all audit logs.

Google Workspace SAML Audit audit logs use the service name `login.googleapis.com`.

Google Workspace SAML Audit writes Data Access audit logs only. The following are the audited operations:

Audit logs category  |  `AuditLog.method_name`  
---|---  
Data Access audit logs | `google.apps.login.v1.SamlLoginFailed`   
  
| `google.apps.login.v1.SamlLoginSucceeded`  
  
  
## Audit log permissions

IAM permissions and roles determine your ability to access audit logs data in the [Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest), the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), and the [Google Cloud CLI](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging).

For detailed information about the organization-level IAM permissions and roles you might need, see the [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

## Audit log format

Google Workspace audit log entries include the following objects:

  * The log entry itself, which is an object of type [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry). When examining audit logging data, you might find the following useful:

    * `logName` contains the organization ID and audit log type.
    * `resource` contains the target of the audited operation.
    * `timeStamp` contains the time of the audited operation.
    * `protoPayload` contains the Google Workspace audit log in its `metadata` field.



The `protoPayload.metadata` field holds the audited Google Workspace information. The following is an example of a Login Audit log:
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.net"
        },
        "requestMetadata": {
          "callerIp": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.loginFailure",
        "resourceName": "organizations/123",
        "metadata": {
          "event": [
            {
              "eventName": "login_failure",
              "eventType": "login",
              "parameter": [
                {
                  "value": "google_password",
                  "type": "TYPE_STRING",
                  "name": "login_type",
                },
                {
                  "name": "login_challenge_method",
                  "type": "TYPE_STRING",
                  "label": "LABEL_REPEATED",
                  "multiStrValue": [
                    "password",
                    "idv_preregistered_phone",
                    "idv_preregistered_phone"
                  ]
                },
              ]
            }
          ],
          "activityId": {
            "uniqQualifier": "358068855354",
            "timeUsec": "1632500217183212"
          },
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto"
        }
      },
      "insertId": "-nahbepd4l1x",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "method": "google.login.LoginService.loginFailure",
          "service": "login.googleapis.com"
        }
      },
      "timestamp": "2021-09-24T16:16:57.183212Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-09-24T17:51:25.034361197Z"
    }

For information about service-specific audit logging fields, and how to interpret them, select from the services listed in [Available audit logs](https://support.google.com/a/answer/9725452).

## View logs

For information on viewing your Google Workspace audit logs, see [View and manage audit logs for Google Workspace](https://docs.cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs).

## Route audit logs

You can route Google Workspace audit logs from Cloud Logging to supported destinations, including other Logging buckets.

Here are some applications for routing audit logs:

  * To use more powerful search capabilities, you can route copies of your audit logs to Cloud Storage, BigQuery, or Pub/Sub. Using Pub/Sub, you can route to other applications, other repositories, and to third parties.

  * To manage your audit logs across an entire organization, you can create [aggregated sinks](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks) that combine and route logs from all the Google Cloud projects, billing accounts, and folders contained by your organization. For instance, you might aggregate and route audit log entries from an organization's folders to a Cloud Storage bucket.




For instructions on routing logs, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

## Regionalization

You can't choose a region where your Google Workspace logs are stored. Google Workspace logs aren't covered by the [Google Workspace Data Region Policy](https://support.google.com/a/answer/9223653).

## Retention periods

The following retention periods apply to your audit logs data:

  * [Data retention policy in Google Workspace](https://support.google.com/a/answer/7061566?hl=en).

  * [Data retention policy in Google Cloud Cloud Logging](https://docs.cloud.google.com/logging/quotas#logs_retention_periods).




For each organization, Cloud Logging automatically stores logs in two buckets: a `_Default` bucket and a `_Required` bucket. The `_Required` bucket holds Admin Activity audit logs, System Event audit logs, and [Access Transparency logs](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/understanding-workspace-logs). The `_Default` bucket holds all other log entries that aren't stored in the `_Required` bucket. For more information on Logging buckets, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview).

You can configure Cloud Logging to retain the logs in the `_Default` logs bucket for a period ranging from 1 day to 3650 days.

To update the retention period for the `_Default` logs bucket, see [Custom retention](https://docs.cloud.google.com/logging/docs/buckets#custom-retention).

You can't change the retention period on the `_Required` bucket.

## Quotas and limits

The same quotas apply to audit logs for Google Workspace and Cloud Audit Logs.

For details about these usage limits, including the maximum sizes of audit logs, see [Quotas and limits](https://docs.cloud.google.com/logging/quotas).

## Pricing

For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).

## What's next

  * Learn how to [configure and manage Google Workspace audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs).
  * Review [best practices](https://docs.cloud.google.com/logging/docs/audit/best-practices) for Cloud Audit Logs.
  * Learn how to [view and understand Access Transparency logs for Google Workspace](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/understanding-workspace-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 

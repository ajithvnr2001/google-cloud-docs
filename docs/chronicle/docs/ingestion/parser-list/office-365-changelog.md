---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/office-365-changelog/
title: Change log for OFFICE_365 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:38.581293+00:00
---

# Change log for OFFICE_365  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/office-365-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OFFICE_365

Date | Changes  
---|---  
2026-09-25 |  \- `target.user.group_identifiers`: Newly mapped `ChatThreadId` raw log field with `target.user.group_identifiers` UDM field.  
\- `target.group.product_object_id`: Newly mapped `ChatThreadId` raw log field with `target.group.product_object_id` UDM field.   
2026-09-22 |  \- Handled edge case scenarios for the `OperationCount` raw log field.   
2026-09-07 |  \- `principal.user.product_object_id`: Newly mapped `AppAccessContext.UserObjectId` raw log field with `principal.user.product_object_id` UDM field when workload is `OneDrive` and operation is `ManagedSyncClientAllowed`.  
\- `target.resource.product_object_id`: Newly mapped `Site` raw log field with `target.resource.product_object_id` UDM field when workload is `OneDrive` and operation is `ManagedSyncClientAllowed`.  
\- `about.resource.product_object_id`: Newly mapped `WebId` raw log field with `about.resource.product_object_id` UDM field when workload is `OneDrive` and operation is `ManagedSyncClientAllowed`.  
\- `network.session_id`: Newly mapped `CallId` raw log field with `network.session_id` UDM field when workload is `MicrosoftTeams` and operation is applicable.  
\- `principal.asset.attribute.labels`: Newly mapped `DeviceInformation` raw log field with `principal.asset.attribute.labels` UDM field when workload is `MicrosoftTeams` and operation is applicable.  
\- `additional.fields`: Newly mapped `JoinTime` raw log field with `additional.fields` UDM field when workload is `MicrosoftTeams` and operation is applicable.  
\- `additional.fields`: Newly mapped `LeaveTime` raw log field with `additional.fields` UDM field when workload is `MicrosoftTeams` and operation is applicable.  
\- `target.user.product_object_id`: Newly mapped `Target.1.ID` raw log field with `target.user.product_object_id` UDM field when workload is `AzureActiveDirectory` and operation is `Add user.`, `Delete user.`, `Update user.`, or `Enable account.`.  
\- `target.resource.attribute.labels`: Newly mapped `Item.ImmutableId` raw log field with `target.resource.attribute.labels` UDM field when workload is `Exchange` and operation is `Update`.  
\- `about.resource.product_object_id`: Newly mapped `ObjectId` raw log field with `about.resource.product_object_id` UDM field when workload is `Yammer` or `PowerBI` and operation is applicable.  
\- `target.resource.product_object_id`: Newly mapped `ThreadId` raw log field with `target.resource.product_object_id` UDM field when workload is `Yammer` and operation is applicable.  
\- `about.resource.attribute.labels`: Newly mapped `ObjectType` raw log field with `about.resource.attribute.labels` UDM field when workload is `PowerBI`.  
\- `target.resource.attribute.labels`: Newly mapped `WorkspaceName` raw log field with `target.resource.attribute.labels` UDM field when workload is `PowerBI`.  
\- `additional.fields`: Removed mapping of `Item.Id` from `additional.fields` UDM field to better identify the target resource for Exchange Update operations when workload is `Exchange` and operation is `Update`.  
\- `target.resource.product_object_id`: Mapped `Item.Id` raw log field with `target.resource.product_object_id` UDM field when workload is `Exchange` and operation is `Update`.  
\- `target.resource.product_object_id`: Added fallback mapping for `WorkspaceId` to `target.resource.product_object_id` in `PowerBI` workload if the primary identifier is missing.  
\- `target.user.email_addresses`: Added email regex check for `parameter.Value` in `Remove-MigrationUser` operation.   
2026-09-01 |  \- `about.user.userid`: Newly mapped `member.UPN` raw log fields with `about.user.userid` UDM field.  
\- Added an overwrite for the `member.UPN` raw field to facilitate email extraction.   
2026-08-17 |  \- `additional.fields`: Removed mapping of `EvidenceFile.FullUrl` and `EvidenceFile.StorageName` from `additional.fields` UDM field for `FileRead` and `FileUploadedToCloud` operations to remove duplicate mappings.   
2026-08-11 |  \- `principal.user.userid`: Removed mapping of `MailboxOwnerUPN` from `principal.user.userid` UDM field for `Send` operation as MailboxOwnerUPN states the mailbox where the action happened.  
\- `principal.user.email_addresses`: Removed mapping of `MailboxOwnerUPN` from `principal.user.email_addresses` UDM field for `Send` operation as MailboxOwnerUPN states the mailbox where the action happened.  
\- `target.user.userid`: Mapped `MailboxOwnerUPN` raw log field with `target.user.userid` UDM field for `Send` operation.  
\- `target.user.email_addresses`: Mapped `MailboxOwnerUPN` raw log field with `target.user.email_addresses` UDM field for `Send` operation.  
\- `network.email.from`: Removed mapping of `UserId` from `network.email.from` UDM field for `Send` operation as UserId states the user who initiated the action.  
\- `target.user.userid`: Removed mapping of `SendAsUserSmtp` from `target.user.userid` UDM field for both `Send` and `SendAs` operation as SendAsUserSmtp states the `From` email address the recipient actually sees.  
\- `target.user.email_addresses`: Removed mapping of `SendAsUserSmtp` from `target.user.email_addresses` UDM field for both `Send` and `SendAs` operation as SendAsUserSmtp states the `From` email address the recipient actually sees.  
\- `network.email.from`: Newly mapped `SendAsUserSmtp` raw log field with `network.email.from` UDM field for both `Send` and `SendAs` operation.  
\- `target.user.email_addresses`: Newly mapped `Recipient.Address` raw log field with `target.user.email_addresses` UDM field for `SendAs` operation.  
\- `target.user.userid`: Newly mapped `Recipient.Name` raw log field with `target.user.userid` UDM field for `SendAs` operation.  
\- `network.email.to`: Newly mapped `Recipient.Address` raw log field with `network.email.to` UDM field for `SendAs` operation.   
2026-07-10 |  \- Improved parser stability and error handling: Updated condition checks to check field presence and use specific fallback on error labels across multiple operations to prevent parser errors on missing fields or unmapped values.  
\- Improved merge stability: Updated the mapping logic for some UDM fields across multiple operations to ensure intermediate variables and temporary structures are non-empty before replacing or merging into UDM objects.   
2026-07-01 |   
2026-06-30 |  \- `about.file.names` : Enhanced the mapping logic for `Item.Attachments` field to remove leading and trailing space from `about.file.names` UDM field for `Update`, `SendOnBehalf`, `SendAs`, `Send`, `Create`, `UpdateInboxRules`, `FolderBind` operations.  
\- `about.file.names` : Enhanced the mapping logic for `AffectedItems.Attachments` field to remove leading and trailing space from `about.file.names` UDM field.   
2026-06-24 |  \- `additional.fields`: Updated the key and value mapping for UDM field `additional.fields` for raw log fields `PolicyDetails.Rules.ConditionsMatched.DocumentProperties` and `PolicyDetails.Rules.ConditionsMatched.OtherConditions` from nested map syntax (keys prefixed with `DocumentProperties_` or `OtherConditions_`) to array-indexed Name-Value pairs (keys formatted as `_`).  
\- Improved parser stability and error handling: Updated condition checks on multiple `ModifiedProperties` and `Parameters` raw log fields (such as `NewValue`, `OldValue`, and `Value`) to use temporary variables with safe fallback configuration to prevent parser errors on missing fields.  
\- Improved merge stability: Updated the `about` and `about.resource.attribute.labels` mapping logic to utilize temporary variables to prevent incorrect merge/overwrites to the target UDM object.   
2026-06-19 |  \- `additional.fields`: Removed mapping of `AttachmentDetails.Name` from `additional.fields` UDM field  
\- `target.file.names`: Mapped `AttachmentDetails.Name` raw log field with `target.file.names` UDM field  
\- `additional.fields`: Removed mapping of `EndpointMetaData.EnforcementMode` from `additional.fields` UDM field  
\- `security_result.action_details`: Mapped `EndpointMetaData.EnforcementMode` raw log field with `security_result.action_details` UDM field  
\- `additional.fields`: Removed mapping of `EndpointMetaData.FileSize` from `additional.fields` UDM field  
\- `target.file.size`: Mapped `EndpointMetaData.FileSize` raw log field with `target.file.size` UDM field  
\- `additional.fields`: Removed mapping of `EndpointMetaData.FileType` from `additional.fields` UDM field  
\- `target.file.file_type`: Mapped `EndpointMetaData.FileType` raw log field with `target.file.file_type` UDM field  
\- `additional.fields`: Newly mapped `EvidenceFile.StorageName` raw log field with `additional.fields` UDM field  
\- `DlpRuleMatch` Operation with Workload `Endpoint`: Added support for the event `DlpRuleMatch` with Workload `Endpoint`  
\- `RecipientChange`: Added support for the operation `RecipientChange` and relevant corresponding raw log fields  
\- `IDCRLBlockedDueToSoftEnforcement`: Added support for the operation `IDCRLBlockedDueToSoftEnforcement` and relevant corresponding raw log fields  
\- `additional.fields`: Newly mapped `IsManagedDevice` raw log field with `additional.fields` UDM field  
\- `additional.fields`: Newly mapped `PolicyChangeType` raw log field with `additional.fields` UDM field  
\- `FileVersionDeleted`: Added support for the operation `FileVersionDeleted` and relevant corresponding raw log fields  
\- `FilePreserved`: Added support for the operation `FilePreserved` and relevant corresponding raw log fields  
\- `DLPRuleMatch`: Added support for the operation `DLPRuleMatch` and relevant corresponding raw log fields  
\- `additional.fields`: Mapped `UserType` raw log field with `additional.fields` UDM field for Operation `FolderRecycled`  
\- `target.file.names`: Mapped `SourceFileName` raw log field with `target.file.names` UDM field for Operation `FolderRecycled`  
2026-06-04 |  \- `target.user.userid`: Removed mapping of `MailboxOwnerUPN` from `target.user.userid` UDM field for `Send` operation.  
\- `principal.user.userid`: Mapped `MailboxOwnerUPN` raw log field with `principal.user.userid` UDM field for `Send` Operation.  
\- `target.user.email_addresses`: Removed mapping of `MailboxOwnerUPN` from `target.user.email_addresses` UDM field for `Send` operation.  
\- `principal.user.email_addresses`: Mapped `MailboxOwnerUPN` raw log field with `principal.user.email_addresses` UDM field for `Send` Operation.  
\- `principal.user.userid`: Removed mapping of `UserId` from `principal.user.userid` UDM field for `Send` operation.  
\- `principal.user.email_addresses`: Removed mapping of `UserId` from `principal.user.email_addresses` UDM field for `Send` operation.  
\- `network.email.from`: Mapped `UserId` raw log field with `network.email.from` UDM field for `Send` Operation.  
\- `target.user.email_addresses`: Newly mapped `Recipient.Address` raw log field with `target.user.email_addresses` UDM field for `Send` operation.  
\- `target.user.userid`: Newly mapped `Recipient.Name` raw log field with `target.user.userid` UDM field for `Send` operation.  
\- `network.email.to`: Newly mapped `Recipient.Address` raw log field with `network.email.to` UDM field for `Send` operation.   
2026-06-03 |  \- `additional.fields`: Newly mapped `Recipients` raw log field with `additional.fields` UDM field for the operation `UpdateInboxRules`.  
\- `security_result.action_details`: Newly mapped `ActionType` raw log field with `security_result.action_details` UDM field for the operation `UpdateInboxRules`.   
2026-05-26 |  \- `GroupMemberRoleAdded`: Added support for the operation `GroupMemberRoleAdded`.   
2026-04-30 |  \- `UnifiedSimulationRuleMatch`: Added support for the operation `UnifiedSimulationRuleMatch`.   
2026-04-07 |  \- Updated the field mapping for the Office 365 parser. For the configuration details along with the list mapping which were changed in comparison to the existing default parser, please check the parser documentation page: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365#udm_mapping_delta.   
2026-03-18 |  \- Updated below mapping for the operation `MailItemsAccessed` to ensure accurate mapping:  
\- additional.fields: Removed mapping of `Folders.FolderItems.Subject` from `additional.fields` UDM field.  
\- network.email.subject: Newly mapped `Folders.FolderItems.Subject` raw log field with `network.email.subject` UDM field.   
2026-03-12 |  \- `additional.fields`: Newly mapped `Workload` raw log field with the UDM field `additional.fields` if the `Operation` raw log field has the value `CopilotInteraction`.   
2026-01-22 |  \- additional.fields: Newly mapped key-value pairs from the `Data` raw log field with the `additional.fields` UDM field for the operation `AlertEntityGenerated`, `AlertTriggered`, and `AlertUpdated`.   
2026-01-12 |  \- Added support for multiple new fields as part of the Office 365 parser update.   
2025-12-26 |  \- security_result.detection_fields[sensitive_info_detection_is_included]: Newly mapped `SensitiveInfoDetectionIsIncluded` raw log field with `security_result.detection_fields[sensitive_info_detection_is_included]` UDM field.   
2025-12-16 |  Implemented a conditional multi-strategy grok approach to parse `ActorInfoString`  
\- Case 1: Extracts content from `ActorInfoString` using the grok pattern UserAgent=(?[^;]+).  
\- network.http.user_agent: Removed mapping of `ClientInfoString` from `network.http.user_agent` UDM field and mapped `temp_agent` extracted user agent value using above grok pattern.  
\- If `temp_agent` contains `NoUserAgent`, it attempts to re-parse `ActorInfoString` to find an agent between the last semicolon and `[AppId=` using Client=.*;(?[^;]+).*\\\\[AppId= from `ClientInfoString`.  
\- network.http.user_agent: Removed mapping of `ClientInfoString` from `network.http.user_agent` UDM field and mapped `agent` extracted user agent value using above grok pattern instead.  
Else if the above grok pattern fails, user agent is treated as empty  
\- network.http.user_agent: Removed mapping of `ClientInfoString` from `network.http.user_agent` UDM field.  
\- Case 2: If `ActorInfoString` contains `Client=`, extract the agent between the last semicolon and `[AppId=` using `Client=.*;(?[^;]+).*\\[AppId=`.  
\- network.http.user_agent: Removed mapping of `ClientInfoString` from `network.http.user_agent` UDM field and mapped `temp_agent` extracted user agent value using above grok pattern instead.  
\- Case 3: If above cases fail, then map entire `ActorInfoString`.  
\- network.http.user_agent: Removed mapping of `ClientInfoString` from `network.http.user_agent` UDM field and mapped `ActorInfoString` instead.   
2025-12-09 |  Updated the following field mapping in the parser as the product's document has been updated.  
\- additional.fields[FileData_DocumentId]: Removed mapping of `FileData.DocumentId` from `additional.fields[FileData_DocumentId]` UDM field.  
\- target.resource.product_object_id: Mapped `FileData.DocumentId` raw log field with `target.resource.product_object_id` UDM field.  
\- additional.fields[FileData_FileName]: Removed mapping of `FileData.FileName` from `additional.fields[FileData_FileName]` UDM field.  
\- target.file.full_path: Mapped `FileData.FileName` raw log field with `target.file.full_path` UDM field.  
\- additional.fields[FileData_FilePath]: Removed mapping of `FileData.FilePath` from `additional.fields[FileData_FilePath]` UDM field.  
\- target.url: Mapped `FileData.FilePath` raw log field with `target.url` UDM field.  
\- additional.fields[FileData_FileSize]: Removed mapping of `FileData.FileSize` from `additional.fields[FileData_FileSize]` UDM field.  
\- target.file.size: Mapped `FileData.FileSize` raw log field with `target.file.size` UDM field.  
\- additional.fields[FileData_FileVerdict]: Removed mapping of `FileData.FileVerdict` from `additional.fields[FileData_FileVerdict]` UDM field.  
\- security_result.detection_fields[file_verdict]: Mapped `FileData.FileVerdict` raw log field with `security_result.detection_fields[file_verdict]` UDM field.  
\- security_result.category: Newly mapped the value `SOFTWARE_MALICIOUS` with `security_result.category` UDM field if `FileData.FileVerdict` raw log field is not empty.  
\- additional.fields[FileData_MalwareFamily]: Removed mapping of `FileData.MalwareFamily` from `additional.fields[FileData_MalwareFamily]` UDM field.  
\- security_result.threat_name: Mapped `FileData.MalwareFamily` raw log field with `security_result.threat_name` UDM field  
\- additional.fields[FileData_SHA256]: Removed mapping of `FileData.SHA256` from `additional.fields[FileData_SHA256]` UDM field.  
\- target.file.sha256: Mapped `FileData.SHA256` raw log field with `target.file.sha256` UDM field  
\- target.resource.attribute.labels[last_modified_date]: Removed mapping of `LastModifiedBy` from `target.resource.attribute.labels[last_modified_date]` UDM field.  
\- target.resource.attribute.labels[last_modified_by]: Mapped `LastModifiedBy` raw log field with `target.resource.attribute.labels[last_modified_by]` UDM field.  
\- `Set-TransportRule`: Added support for the operation `Set-TransportRule` and relevant corresponding raw log fields.  
\- `AtpDetection`: Added support for the operation `AtpDetection` and relevant corresponding raw log fields.  
\- principal.resource.attribute.labels[external_access]: Newly mapped `ExternalAccess` raw log field with `principal.resource.attribute.labels[external_access]` UDM field for the operation `New-InboxRule`.  
\- security_result.rule_name: Newly mapped `Parameters.Name` raw log field with `security_result.rule_name` UDM field for the operation `New-InboxRule`.  
\- additional.fields: Newly mapped key-value pairs from the `Parameters` raw log field with the `additional.fields` UDM field for the operation `New-InboxRule`.  
\- security_result.action: Newly mapped the value `ALLOW` with `security_result.action` UDM field if `ResultStatus` raw log field has the value `True` for the operation `New-InboxRule`.  
\- security_result.action: Newly mapped the value `BLOCK` with `security_result.action` UDM field if `ResultStatus` raw log field has the value `False` for the operation `New-InboxRule`.  
\- principal.resource.attribute.labels[external_access]: Newly mapped `ExternalAccess` raw log field with `principal.resource.attribute.labels[external_access]` UDM field for the operation `Set-InboxRule`.  
\- security_result.rule_name: Newly mapped `Parameters.Name` raw log field with `security_result.rule_name` UDM field for the operation `Set-InboxRule`.  
\- security_result.detection_fields[parameters_identity]: Newly mapped `Parameters.Identity` raw log field with `security_result.detection_fields[parameters_identity]` UDM field for the operation `Set-InboxRule`.  
\- additional.fields: Newly mapped key-value pairs from the `Parameters` raw log field with the `additional.fields` UDM field for the operation `Set-InboxRule`.  
\- security_result.action: Newly mapped the value `ALLOW` with `security_result.action` UDM field if `ResultStatus` raw log field has the value `True` for the operation `Set-InboxRule`.  
\- security_result.action: Newly mapped the value `BLOCK` with `security_result.action` UDM field if `ResultStatus` raw log field has the value `False` for the operation `Set-InboxRule`.   
2025-12-03 |  \- `Set-OrganizationConfig`: Added support for the operation `Set-OrganizationConfig`.   
2025-12-01 |  \- additional.fields: Newly mapped `ExchangeMetaData.AttachmentDetails.Name`, `ExchangeMetaData.AttachmentDetails.Size`, and iterated over `ExchangeMetaData.AttachmentDetails.Labels` to map child raw log fields with `additional.fields` UDM field.   
2025-11-11 |  \- network.email.subject: Newly mapped `ExchangeMetaData.Subject` raw log field with `network.email.subject` UDM field.   
2025-10-27 |  Updated mapping for ExtendedProperties.RequestType raw log field.  
\- extensions.auth.type: Removed mapping of the value `MACHINE` from `extensions.auth.type` UDM field and mapped the value `SSO` instead.  
\- extensions.auth.mechanism: Removed mapping of the value `REMOTE` from `extensions.auth.mechanism` UDM field and mapped the value `INTERACTIVE` instead.   
2025-10-13 |  \- Improved error handling to cover various edge cases across multiple scenarios.  
\- metadata.log_type: Newly mapped `OFFICE_365` value with `metadata.log_type` UDM field.   
2025-09-15 |  Updated mapping for Data.trc field and Data.imsgid field.  
\- principal.user.email_address: Removed mapping of `Data.trc` from `principal.user.email_address` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- target.user.email_address: Mapped `Data.trc` raw log field with `target.user.email_address` UDM field.  
\- principal.user.email_address: Removed mapping of `Data.imsgid` from `principal.user.email_address` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- network.email.mail_id: Mapped `Data.imsgid` raw log field with `network.email.mail_id` UDM field.   
2025-08-11 |  \- Added support for multiple new fields across various events as part of the Office 365 parser update.   
2025-08-05 |  \- security_result.description: Newly mapped `UserClaims` raw log field with `security_result.description` UDM field.   
2025-06-04 |  \- additional.fields[internet_message_id]: Newly mapped `InternetMessageId` raw log field with `additional.fields[internet_message_id]` UDM field.   
2025-05-29 |  \- target.file.md5: Newly mapped `MD5Hash` raw log field with `target.file.md5` UDM field for `FileMalwareDetected` logs.  
\- target.file.sha256: Newly mapped `SHA256Hash` raw log field with `target.file.sha256` UDM field for `FileMalwareDetected` logs.  
\- Added an index to the key within `additional.fields` for the `ExtendedProperties` log field to ensure key uniqueness.   
2025-05-13 |  \- `target.file.full_path`: Added the mapping of `ObjectId` raw log field to `target.file.full_path` UDM field if the value of the field `Workload` is `Endpoint` for `MipLabel`, `DlpRuleMatch`,`DLPRuleMatch`,`DlpRuleUndo`, `DLPRuleUndo` and `DlpInfo` operations.   
2025-04-03 |  \- additional.fields[mailbox_owner_upn]: Newly mapped `MailboxOwnerUPN` raw log field with `additional.fields[mailbox_owner_upn]` UDM field.   
2025-03-05 |  \- Added support for the `EndpointMetaData.FileExtension` `EndpointMetaData.FileSize` `EndpointMetaData.EnforcementMode` `EndpointMetaData.EndpointOperation` `ExchangeMetaData.FileSize` `ExchangeMetaData.FileType` dynamically mapped to `additional.fields` UDM field respectively.   
2025-02-25 |  \- Added support for the `SystemOverrides.Details`, `SystemOverrides.FinalOverride` , `SystemOverrides.Result`, `SystemOverrides.Source` raw log field operation and dynamically mapped to `target.resource.attribute.label.SystemOverrides_key` UDM field respectively.   
2025-01-21 |  \- Added replace block and on_error check for `field.OldValue` field in `ModifiedProperties` raw log field in `TeamsAdminAction` operation.   
2025-01-20 |  \- Added support for the raw log field `Id`, mapping it to `principal.asset_id` UDM field for the `UserLoggedIn` operation.  
\- Added support for the raw log field `BrowserType`, mapping it to `principal.asset.software.name` UDM field for the `UserLoggedIn` operation.  
\- Added support for the raw log fields `TrustType`, `IsCompliant` and `IsCompliantAndManaged`, mapping them to `additional.fields` for the `UserLoggedIn` operation.   
2025-01-05 |  \- Added support for the `Parameters` raw log field object in `Set-MailboxAutoReplyConfiguration` operation and dynamically mapped to `security_result.detection_fields` UDM field.   
2024-11-11 |  \- Updated logic for AppAccessContext.AADSessionId field to map it to network.session_id   
2024-10-11 |  \- Added support for CopilotEventData.AccessedResources field for CopilotInteraction operations.   
2024-09-13 |  \- Added support for Parameters field for New-TransportRule operations.  
\- Added support for Actions field for AirInvestigationData operations.   
2024-09-06 |  \- Added support for FileSizeBytes field for various file related operations.   
2024-08-23 |  \- Added support for the field ParticipantInfo and its sub-field for the Operation MemberAdded.  
\- Added support for the field QueryText for the Operation SearchCreated, SearchUpdated, SearchStarted and map it to security_result.detection_fields[QueryText]  
\- Added support for the field ObjectId for the Operation SearchCreated, SearchUpdated, SearchStarted and map it to additional.fields[ObjectId]  
\- Added support for the Operation TeamsAdminAction for the field ModifiedProperties to security.detection_field.  
\- Added support for the AlertEntityId to target.url when the log with `EntityType`:`MaliciousUrl`.   
2024-08-09 |  \- Added support for Attachments[].AffectedItems and mapped the first file name and size of the file to about.file.size and about.file.full_path.  
\- Added support for Attachments[].AffectedItems and mapped the field to additional.fields[Attachments_AffectedItems].   
2024-07-10 |  \- Added support for PreExecutionMessage , PostExecutionMessage iterated over the fields and mapped the key value to security_result.detection_fields.   
2024-06-12 |  \- Added support for `target.user.userid` in UDM, which is mapped to `Data:` -> `userPrincipalName`.  
\- Added support for `security_result.url_back_to_product` in UDM, which is mapped to `AlertLinks:` -> `AlertLinkHref`.  
\- Added support for UserId, which is mapped to `additional.fields` as UserId does not provide the true user.userid  
\- Added support for `target.user.product_object_id` in UDM, which is mapped to `Data:` -> `riskyUserId`  
\- Added support for ModifiedProperties and field.Name = IPAddressAllowList under the additional fields with `NewIPAddressAllowList` and `OldIPAddressAllowList`.   
2024-05-22 |  \- Added support for `ObjectId` field to additional field for `Add member to role.`, and `Add user.` operations.   
2024-05-15 |  \- Added support for `ItemName` and `ParticipantInfo.HasForeignTenantUsers` fields to `additional` field for `ChatCreated` operations.   
2024-05-08 |  \- Added support of the `StrongAuthenticationMethod` and `StrongAuthenticationUserDetails` values of the `ModifiedProperties.Name` raw log field.  
\- Added support for `ObjectId` field to the additional field `FileUploadedToCloud` operations.   
2024-04-24 |  \- Added UDM mapping of the field `ResultStatusDetail`.  
\- Added support for `Parameters` field for `Add-RecipientPermission` operations.  
\- Updated UDM mapping of ModifiedProperties raw log field.   
2024-03-27 |  \- Added support for `ObjectId` field from `FilePrinted` and `FileUploadedToCloud` operations.  
\- Added support for `SearchQueryText` field for `SearchQueryPerformed` operations.  
\- Added mapping of `InternetMessageId` to `network.email.mail_id` UDM fields for `UserSubmission`, `UserSubmissionTriage` operation.  
\- Added mapping of `FileSizeBytes` for `FileModifiedExtended` operations.   
2024-03-13 |  \- Added support for `GetRefreshablesForCapacityAsAdmin` new operations.  
\- Added support for `AppRole.Value` field from `ModifiedProperties`.  
\- Added mapping of `SensitivityLabelEventData.JustificationText` field to `security_result.detection_fields` UDM field.  
\- Added mapping of `UrlClickAction` field to `security_result.detection_fields` UDM field.   
2024-02-28 |  \- Added support for new operations.   
2024-02-14 |  \- Added support for `QuarantineApproveReleaseMessage`, `QuarantineDenyReleaseMessage`, `FileSensitivityLabelApplied`, `Update policy.`, `SharingLinkUsed`, `AddedToSharingLink`, `Authorize`, `SharingLinkUpdated`, `SubTaskUpdated`, `TaskRead`, and `SubTaskCreated` new operations.   
2024-01-31 |  \- Added support for `SharingLinkCreated`, `TimesheetSaved`, `ResourceCheckedOut`, `GetGroupUsers`, `SensitivityLabelUpdated`, `ListItemRecycled` and `TimesheetAccessed` operations.   
2024-01-17 |  \- Added support for `SensitivityLabelApplied` operation.   
2024-01-03 |  \- Added support for `Add-MailboxLocation` and `Release-QuarantineMessage` operations.   
2023-11-29 |  \- Added support for `Set-DlpCompliancePolicy` and `Remove-DlpCompliancePolicy` operations.  
\- Added additional mapping of `RequestType` field from `ExtendedProperties` to `about.labels` in `UserLoggedIn` and `UserLoginFailed` operations.  
\- Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.  
\- Added support for additional fields for `noun.labels`.   
2023-11-01 |  \- Added support for `QuarantineReleaseMessage`, `WorkspaceStatusReceived`,`LinkedEntityUpdated`, `ViewResponse`, `O365SyncAdminUserPromotion`, `FileCopiedToClipboard`, and `FileTranscriptContentAccessed` operations.   
2023-10-18 |  \- Added support for `TaskModified` and `DeleteTile` operations.   
2023-10-04 |  \- Added support for `SensitivityLabeledFileOpened`,`SensitivityLabeledFileRenamed` and `Validate` operations.  
\- Added support for `Modified Properties` fields in the `Update user` operation.   
2023-09-20 |  \- Added support for `PutConnection`,`PutConnectionPermission` `AdminSubmissionTablAllow`, `Add contact.` and `WorkspacePortalUrlReceived` operations.   
2023-09-06 |  \- Added mapping of `ObjectId` for `Add-MailboxPermission` Operation.   
2023-08-23 |  \- Added support for `TaskListRead` operation.   
2023-08-09 |  \- Added support for `GetWorkspaces`, `TeamsUserSignedOut` and `ConnectFromExternalApplication` operation.   
2023-07-26 |  \- Added support for `SensitiveInfoTypeData` fields in DLP logs.  
\- Updated mapping of `metadata.event_type` for `UserLoginFailed` operation.   
2023-06-28 |  \- Updated mapping of `metadata.event_type` for `UserLoggedIn` operation.   
2023-06-14 |  \- Added support for `ListViewUpdated` operation.  
\- Updated the parser to include `parse_network_http_user_agent` to use `Parsed User Agent` and `User Agent`.   
2023-05-31 |  \- Added support for `FileUploadedToCloud`, `GenerateDataflowSasToken`, `GenerateScreenshot`, `MDCAssessments`, `RemovableMediaMount`, `SignInEvent`, `ApprovedRequest`, `CreateForm`, `ListForms`, `MDCRegulatoryComplianceAssessments`, `PreviewForm`, `ViewedApprovalRequest`, `ListCreated` and `SiteColumnCreated` operations.  
\- Added mapping for the recipient of the email for TIMailData.   
2023-05-02 |  \- Added mapping of attachment data for operation `TIMailData`.  
\- Added mapping of `Result Status` log field for operation `SoftDelete`.  
\- Updated mapping of event type of `Update Service Principal`.  
\- Added mapping of `Result Status` with `security_result.action` for all operations.  
\- Added mapping of `ErrorNumber` log field for operations `UserLoggedIn` and `UserLoginFailed`.  
\- Added support for `New-DlpCompliancePolicy`, `New-DlpComplianceRule`, `Get-InsiderRiskPolicy`, `Enable Strong Authentication.`, `ReactedToMessage`, `RemovableMediaUnmount` and `Set-HostedContentFilterPolicy` operations.   
2023-04-12 |  \- Added mapping of fields present in the `Data` field for operations `AirInvestigation`, `AlertUpdated`, `AlertEntityGenerated`, `AlertTriggered`.  
\- Added support for operation `DeleteDatasetRows`.  
\- Added mapping of `ApplicationId` log field and updated mapping for the `ApplicationDisplayName`, `appId` and `RequestType` log fields.   
2023-03-29 |  \- Added support for IPv6 dual address.  
\- Added support for operation `LaunchPowerApp`.   
2023-03-15 |  \- Added mapping of `Role.TemplateId` field for operation `Add member to role.`.  
\- Updated mapping of `Role.DisplayName` field for operation `Add member to role.`.   
2023-03-01 |  \- Added support for operation `FileSensitivityLabelChanged`.  
\- Added support for operation `FileRead`.  
\- Added support for operation `MessageReadReceiptReceived`.  
\- Added support for operation `Search`.  
\- Added support for operation `TaskDeleted`.  
\- Added support for operation `TaskUpdated`.  
\- Added support for operation `TaskCreation`.  
\- Added regular expression for `email` field for operation `AirInvestigationData'.  
\- Added size validation for `principal.user.userid` and `target.user.userid`.  
\- Modified validations for setting `metadata.event_type`.  
\- Removed unwanted invalid JSON format logs.   
2023-02-01 |  \- Added support for operation `SecurityGroupModified`.  
\- Added mapping of principal.user.userid and target.user.userid.   
2023-01-18 |  \- Added mapping for field `Is Hard Deleted` and mapped it with security_result.detection_fields.key/value.  
\- Added mapping for field `GivenName` and mapped it with target.user.attribute.labels.key/value.  
\- Added mapping for field `RequiredResourceAccess` and mapped it with target.resource.attribute.labels.key/value.  
\- Added mapping for field `DelegatedPermissionGrant.Scope` and mapped it with target.resource.attribute.labels.key/value.   
2023-01-11 |  \- Removed gsub filter to remove leading zeros.  
\- Added validation logic to check if IP is valid or not.  
\- Handled the ObjectId field to remove unnecessary angular brackets.  
\- Added support for RecipientCount, Sent, SensitiveInformationDetailedClassificationAttributes.Confidence, SensitiveInformationDetailedClassificationAttributes.Count, SensitiveInfoTypeData.Confidence, SensitiveInfoTypeData.Count fields.   
2023-01-04 |  Promoting parser to default.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

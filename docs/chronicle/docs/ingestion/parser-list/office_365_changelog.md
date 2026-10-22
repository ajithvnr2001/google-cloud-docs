---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/office_365_changelog/
title: Change log for OFFICE_365 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:47:10.579122+00:00
---

# Change log for OFFICE_365  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/office_365_changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OFFICE_365 

Date | Changes | 2022-04-17 | Enhancement-Added mappings for new fields   
TargetUserOrGroupName & TargetUserOrGroupType fields parsed for the following Office 365 Event Types:   
"AccessRequestUpdated","SharingInvitationCreated","SharingInvitationAccepted".   
  
---|---  
2022-04-12 | Enhancement-Added mappings for new fields.   
Added following new event "TIUrlClickData".   
Url mapped to target.url.   
Based on UrlClickAction value security_result.action_details and security_result_description has been mapped.   
UserIp mapped to principal.ip.   
Added new event "InsightGenerated".   
Description mapped to metadata.description.   
For existing Operation/Event "DLPRuleMatch" mapped following fields:   
\- PolicyId, PolicyName, Actions, RuleId, RuleMode, RuleName, Severity, SensitiveInformationTypeName, SharePointMetaData.FileID, SharePointMetaData.FileName, SharePointMetaData.FilePathUrl, SharePointMetaData.FileSize.   
For existing Operation/Event "FileModifiedExtended", mapped following fields:   
\- CorrelationId mapped to network.sessionId.   
\- ApplicationDisplayName,ApplicationId mapped to target.labels,   
\- FileSizeBytes mapped to target.file.size.   
For existing Operation/Event "AddedToSecureLink" mapped following fields:   
\- TargetUserOrGroupName mapped to target.group.name if this is group, else mapped to target.user.userid.   
\- TargetUserOrGroupType mapped to target.user.attribute.roles if TargetUserOrGroupType is not Group.   
For existing Operation/Event "Add registered users to device." mapped following fields:   
\- ResultStatus mapped to securityResult.actionDetails.   
\- Based on ResultStatus enum value securityResult.action is mapped.   
\- AzureActiveDirectoryEventType mapped to security_result.summary. If AzureActiveDirectoryEventType = 0 then "AccountLogon" else if AzureActiveDirectoryEventType = 1 then "AzureApplicationAuditEvent".   
\- ModifiedProperties.[n].NewValue mapped to securityResult.description.   
\- target.[n].ID mapped to target.user.productObjectId if target.[n].type is 3, else mapped to target.user.userid target.[n].type is 4 or 5.   
For existing Operation/Event "Add registered users to device." mapped following fields:   
\- ModifiedProperties.[n].NewValue mapped to target.asset.asset_id if it is TargetId.DeviceId , else mapped to target.asset.platform_software.platform if it is TargetId.DeviceOSType, else mapped to target_software.version if it is DeviceOSVersion.   
\- ModifiedProperties.[n].NewValue mapped to target.labels based on ModifiedProperties.[n].Name values.   
For existing Operation/Event "Add member to group." mapped following fields:   
\- actor.[n].ID mapped to principal.user.productObjectId if actor.[n].Type is 3.   
For existing Operation/Event "MemberRemoved" mapped following fields:   
\- Currently UserId always goes to principal.user.userid, but now mapped based on UserType values.   
\- Members.[0].displayName mapped to target.user.displayName.   
\- Members.[0].Role mapped to target.user.attribute.roles.   
For existing Operation/Event "AddFolderPermissions" mapped following fields:   
\- LogonType mapped to extensions.auth.authDetails.   
\- Item.Id mapped to target.resource.id.   
\- Item.ParentFolder.MemberSid mapped to target.user.productObjectId.   
\- Item.ParentFolder.MemberUpn mapped to target.user.emailAddresses.   
  
2022-03-28 | Enhancement-Added mappings for new fields   
Added following new events "AddedToSecureLink", "AccessRequestCreated", "AccessRequestApproved", "SiteCollectionAdminRemoved", "UserExpirationChanged".   
TargetUserOrGroupName and TargetUserOrGroupType mapped for the following events: "AddedToSecureLink", "AddedToGroup", "AccessRequestCreated", "AccessRequestApproved", "SharingSet", "SharingRevoked", "SiteCollectionAdminAdded", "SiteCollectionAdminRemoved", "UserExpirationChanged"   
TargetUserOrGroupName mapped to target.user.email_addresses if this is an email, else mapped to target.user.userid   
TargetUserOrGroupType mapped to target.user.attribute.roles   
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

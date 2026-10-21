---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/atlassian-jira-changelog/
title: Change log for ATLASSIAN_JIRA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:05:21.068389+00:00
---

# Change log for ATLASSIAN_JIRA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/atlassian-jira-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ATLASSIAN_JIRA

Date | Changes  
---|---  
2026-07-31 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `webhookEvent` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user.accountId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `user.displayName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `user.self` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `issue.id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `issue.key` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `issue.self` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `issue.fields.assignee.displayName` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `issue.fields.priority.name` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `user.timeZone`, `user.accountType`, `user.active`, `user.avatarUrls.size_16x16`, `user.avatarUrls.size_24x24`, `user.avatarUrls.size_32x32`, `user.avatarUrls.size_48x48` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `issue.fields.assignee.accountType`, `issue.fields.creator.accountId`, `issue.fields.creator.displayName`, `issue.fields.creator.self` raw log fields with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `issue_event_type_name`, `changelog.id`, `issue.fields.watches.self`, `issue.fields.watches.watchCount`, `issue.fields.watches.isWatching`, `issue.fields.customfield_10054.errorMessage`, `issue.fields.customfield_10054.i18nErrorMessage.i18nKey`, `issue.fields.worklog.maxResults`, `changelog.items`, `issue.fields.issuelinks`, `issue.fields.customfield_10020`, `issue.fields.customfield_10019`, `issue.fields.resolution.name`, `issue.fields.resolution.description`, `issue.fields.lastViewed`, `issue.fields.status.description`, `issue.fields.priority.self`, `issue.fields.issuetype.hierarchyLevel` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `issue.fields.issuetype.id`, `issue.fields.priority.id`, `issue.fields.issuetype.subtask`, `issue.fields.project.simplified`, `issue.fields.summary`, `issue.fields.description`, `issue.fields.statuscategorychangedate`, `issue.fields.issuetype.name`, `issue.fields.project.id`, `issue.fields.project.key`, `issue.fields.project.name`, `issue.fields.status.name`, `issue.fields.status.id`, `issue.fields.issuetype.description`, `issue.fields.created`, `issue.fields.updated`, `issue.fields.statusCategory.name`, `issue.fields.statusCategory.self`, `issue.fields.statusCategory.id`, `issue.fields.statusCategory.key`, `issue.fields.statusCategory.colorName`, `issue.fields.project.projectTypeKey`, `issue.fields.project.projectCategory.name`, `issue.fields.issuetype.entityId`, `issue.fields.status.iconUrl`, `issue.fields.project.self`, `Issue_Type_iconUrl` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting the value of `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` when user related data is present and target resource data is present.   
2023-12-12 |  Bug-Fix:  
\- Added support for mapping multiple IP addresses from `source` to `principal.ip`.   
2023-11-10 |  Enhancement:  
\- Added a new Grok pattern to parse failing JSON logs.  
\- Mapped `affectedObjects` to `target.resource.attribute.labels`.  
\- Mapped `changedValues` to `security_result.about.resource.attribute.labels`.  
\- Mapped `extraAttributes` to `principal.resource.attribute.labels`.  
\- Mapped `source` to `principal.ip`.  
\- Mapped `author.id`, `author.name`, `author.uri`, `author.type`, `auditType.area`, `auditType.category`, and `auditType.action` to `principal.user.userid`, `principal.user.user_display_name`, `principal.url`, `principal.resource.attribute.labels`, `metadata.product_event_type`, `security_result.category_details`, and `security_result.summary` respectively.   
2023-02-09 |  Enhancement -  
\- Added a `json` block to retrieve the JSON data.   
2023-01-10 |  Enhancement - Added support for JSON format logs.  
\- Mapped `authorAccountId` to `principal.user.userid`.  
\- Mapped `id` to `metadata.product_log_id`.  
\- Mapped `remoteAddress` to `principal.ip`.  
\- Mapped `summary` to `metadata.description`.  
\- Mapped `category` to `metadata.product_event_type`.  
\- Mapped `authorKey` to `target.resource.attribute.labels`.  
\- Mapped `objectItem.id`, `objectItem.name`, `objectItem.typeName` to `security_result.detection_fields`.  
\- Mapped `associatedItems.0.id` to `target.user.userid` when `associatedItems.0.typeName` is `USER`.  
\- Mapped `associatedItems.0.name` to `target.user.user_display_name` when `associatedItems.0.typeName` is `USER`.  
\- Mapped `associatedItems.0.parentId` to `target.process.parent_process.pid` when `associatedItems.0.typeName` is `USER`.  
\- Mapped `associatedItems.0.parentName` to `target.resource.parent` when `associatedItems.0.typeName` is `USER`.  
\- Mapped `associatedItems.0.id` and `associatedItems.0.name` to `security_result.detection_fields` when `associatedItems.0.typeName` is not `USER`.  
\- Mapped `associatedItems.0.typeName` to `security_result.detection_fields`.  
\- Mapped `changedValues.fieldName`, `changedValues.changedFrom`, "`changedValues.changedTo` to `security_result.about.resource.attribute.labels`.  
\- Mapped `STATUS_UPDATE` to `metadata.event_type` if `remoteAddress` is present.  
\- Mapped `USER_UNCATEGORIZED` to `metadata.event_type` if `authorAccountId` is present or `associatedItems.0.typeName is `USER` and `associatedItems.0.id" is present.   
2022-05-31 |  Bug-fix - Added condition to check the incorrect mapping for principal.url if url value in the logs has `/status`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

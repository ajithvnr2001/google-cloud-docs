---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-devops-changelog/
title: Change log for AZURE_DEVOPS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:56.360160+00:00
---

# Change log for AZURE_DEVOPS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-devops-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_DEVOPS

Date | Changes  
---|---  
2025-03-10 |  Enhancement:  
\- Mapped `area` to `target.application`.  
\- Mapped `categoryDisplayName` to `security_result.action_details`.  
\- Mapped `details` to `metadata.description`.  
\- Mapped `actionId` to `metadata.product_event_type`.  
\- Mapped `timestamp` to `metadata.event_timestamp`.  
\- Mapped `actorUserId` to `principal.user.userid`.  
\- Mapped `actorDisplayName` to `principal.user.user_display_name`.  
\- Mapped `actorCUID` to `principal.user.product_object_id`.  
\- Mapped `actorUPN` to `principal.user.email_addresses`.  
\- Mapped `scopeId` to `target.resource_ancestors_scope.product_object_id`.  
\- Mapped `scopeName` to `target.resource_ancestors_scope.name`.  
\- Mapped `userAgent` to `network.http.user_agent` and `network.http.parsed_user_agent`.  
\- Mapped `projectId` to `target.resource_ancestors_project.product_object_id`.  
\- Mapped `scopeType` to `additional.fields`.  
\- Mapped `projectName` to `target.resource.attribute.labels`.  
\- Mapped `activityId` to `metadata.product_log_id`.   
2024-01-19 |  Enhancement:  
\- Changed `metadata.event_type` value from `SERVICE_*` to `USER_RESOURCE_UPDATE_CONTENT` if principal user data and target resource data are present.  
\- Changed mapping for `IpAddress` from `target.ip` to `principal.ip`.  
\- Changed mapping for `ActorCUID` from `principal.user.product_object_id` to `additional.fields`.  
\- Changed mapping for `ScopeId` from `principal.asset_id` to `resource_ancestors.product_object_id`.  
\- Changed mapping for `_Internal_WorkspaceResourceId` from `target.resource.product_object_id` to `additional.fields`.  
\- Changed mapping for `ProjectId` from `target.resource.attribute.labels` to `target.resource_ancestors.product_object_id`.  
\- Changed mapping for `AuthenticationMechanism` from `security_result.summary` to `extensions.auth.auth_details`.  
\- Changed mapping for `CorrelationId` from `network.session_id` to `additional.fields`.  
\- Changed mapping for `ScopeDisplayName` from `additional.fields` to `target.resource_ancestors.name`.  
\- Changed mapping for `PipelineId` from `additional.fields` to `target.resource.product_object_id`.  
\- Changed mapping for `PipelineName` from `additional.fields` to `target.resource.name`.  
\- Changed mapping for `PipelineScope` from `additional.fields` to `target.resource.attribute.labels`.  
\- Changed mapping for `PipelineRevision` from `additional.fields` to `target.resource.attribute.labels`.  
\- Changed mapping for `ProjectId` from `target.resource.resource.attribute.labels` to `target.resource_ancestors.product_object_id`.  
\- Changed mapping for `Area` from `additional.fields` to `target.application`.  
\- Mapped `MICROSOFT_AZURE` value to `target.asset.attribute.cloud.environment`.  
\- When `AuthenticationMechanism` is having `ServicePrincipal` value, then set `SERVICE_ACCOUNT_TYPE` to `principal.user.account_type`, else set `CLOUD_ACCOUNT_TYPE` to `principal.user.account_type`.  
\- Mapped `Category` to `security_result.action_details`.  
\- Mapped `ALLOW` or `BLOCK` to `security_result.action` based on `Details` field.  
\- Mapped `ActivityId` to `additional.fields`.   
2024-01-09 |  Enhancement:  
\- Added Grok and gsub to parse the unparsed JSON logs.  
\- Mapped `rec.correlationId`, `properties.currentHealthStatus`, `properties.previousHealthStatus`, `properties.type`, `properties.cause`, `properties.title`, `properties.details`, `properties.recommendationType`, `properties.recommendationCategory`, `properties.recommendationImpact`, `properties.recommendationName`, `properties.recommendationResourceLink`, `properties.recommendationSchemaVersion`, `properties.eventCategory`, `properties.hierarchy`, `properties.message`, `properties.entity`, `identity.claims.xms.tcdt`, `identity.claims.aio`, `identity.claims.appid`, `identity.claims.appidacr`, `identity.claims.aud`, `identity.claims.exp`, `identity.claims.iat`, `identity.claims.idtyp`, `identity.claims.iss`, `identity.claims.uti`, `identity.claims.rh`, `identity.claims.ver`, `identity.claims.nbf`, `identity.authorization.evidence.roleAssignmentId`, `identity.authorization.evidence.principalType`, `identity.authorization.evidence.principalId`, `identity.authorization.evidence.roleAssignmentScope`, `identity.authorization.evidence.roleDefinitionId` to `security_result.detection_fields`.  
\- Mapped `resultSignature.label`, `rec.resultType`, `Visibility`, `Humidity`, `Precipitation`,`MoonPhase`, `Moonrise`, `Moonset`, `Pressure`, `WindSpeed`, `UVIndex`, `DewPoint`, WindDirection`, `Sunrise`, `Sunset`, `Temperature`, `Icon`, `Conditions` to `additional.fields".  
\- Mapped `level` to `security_result.severity`.  
\- Mapped `appname` to `target.application`.  
\- Mapped `category.details` to `security.result.category.details`.  
\- Mapped `rec.resourceId` to `target.resource.id`.  
\- Mapped `res.extensionResourceName` to `principal.hostname`.   
2023-11-23 |  Enhancement:  
\- Added support for a new pattern of JSON logs.  
\- Mapped `data.TimeGenerated` to `metadata.event_timestamp`.  
\- When `_Internal_WorkspaceResourceId` is missing, then mapped `topic` to `target.resource.product_object_id`.  
\- Mapped `data.Data.ConnectionId` to `additional.fields`.  
\- Mapped `data.Data.ownerDetails` to `additional.fields`.  
\- Mapped `data.Data.DeploymentResult` to `additional.fields`.  
\- Mapped `data.Data.EnvironmentName` to `additional.fields`.  
\- Mapped `data.Data.JobName` to `additional.fields`.  
\- Mapped `data.Data.StageName` to `additional.fields`.  
\- Mapped `data.Data.RunName` to `additional.fields`.  
\- Mapped `data.Data.RetentionLeaseId` to `additional.fields`.  
\- Mapped `data.Data.CheckSuiteId` to `additional.fields`.  
\- Mapped `data.Data.CheckSuiteStatus` to `additional.fields`.  
\- Mapped `data.Data.ApprovalRequest` to `additional.fields`.  
\- Mapped `data.Data.ApprovalType` to `additional.fields`.  
\- Mapped `subject` to `additional.fields`.  
\- Mapped `data.ActorUserId` to `principal.user.userid`.  
\- Mapped `data.ActorDisplayName` to `principal.user.user_display_name`.  
\- Mapped `data.ActorCUID` to `principal.user.product_object_id`.  
\- Mapped `data.ActorUPN` to `principal.user.email_addresses`.  
\- Mapped `data.ScopeId` to `principal.asset_id`.  
\- Mapped `data.CorrelationId` to `network.session_id`.  
\- Mapped `data.UserAgent` to `network.http.user_agent`.  
\- Mapped `data.ProjectId` to `target.resource.attribute.labels`.  
\- Mapped `data.ScopeType` to `additional.fields`.  
\- Mapped `data.ProjectName` to `target.resource.attribute.labels`.  
\- Mapped `data.Details` to `metadata.description`.  
\- Mapped `data.CategoryDisplayName` to `security_result.rule_name`.  
\- Mapped `data.Area` to `additional.fields`.  
\- Mapped `data.Id` to `metadata.product_log_id`.  
\- Mapped `data.ActionId` to `metadata.product_event_type`.  
\- Mapped `data.Timestamp` to `metadata.event_timestamp`.   
2022-06-28 |  Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

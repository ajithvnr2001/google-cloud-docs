---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-keyvault-audit-changelog/
title: Change log for AZURE_KEYVAULT_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:23:22.637355+00:00
---

# Change log for AZURE_KEYVAULT_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-keyvault-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_KEYVAULT_AUDIT

Date | Changes  
---|---  
2026-09-10 |  Enhancement:  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `data.properties.tlsVersion` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `data.identity.claim.oid` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `data.identity.claim.appidacr`, `data.identity.claim.xms_mirid`, `data.properties.algorithm`, `data.properties.appliedAssignmentId`, `data.properties.trustedService` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `data.properties.isRbacAuthorized`, `data.properties.keyProperties.attributes.hsmPlatform`, `data.properties.keyProperties.type` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2026-07-14 |  Enhancement:  
`event.idm.read_only_udm.additional.fields`: Newly mapped `record.time`, `record.category`, `record.operationName` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
`event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `record.operationName` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
`event.idm.read_only_udm.target.resource.name`: Newly mapped `record.properties.ObjectName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
`event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `record.properties.ObjectType` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
`event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `record.resourceId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
`event.idm.read_only_udm.security_result.category_details`: Newly mapped `record.category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `record.resultType`, `record.properties.IsComplianceCheck`, `record.properties.EvaluationDetails.DefinitionId`, `record.properties.EvaluationDetails.Outcome`, `record.properties.EvaluationDetails.DefinitionDisplayName`, `record.properties.EvaluationDetails.AssignmentId`, `record.properties.EvaluationDetails.ExpressionEvaluationDetails.Expression`, `record.properties.EvaluationDetails.ExpressionEvaluationDetails.ExpressionKind`, `record.properties.EvaluationDetails.ExpressionEvaluationDetails.ExpressionValue`, `record.properties.EvaluationDetails.ExpressionEvaluationDetails.Operator`, `record.properties.EvaluationDetails.ExpressionEvaluationDetails.Result`, `record.properties.EvaluationDetails.ExpressionEvaluationDetails.TargetValue` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
`event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `record.properties.EvaluationDetails.AssignmentDisplayName` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
`event.idm.read_only_udm.security_result.rule_id`: Newly mapped `record.properties.EvaluationDetails.AssignmentId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
`event.idm.read_only_udm.security_result.description`: Newly mapped `record.properties.EvaluationDetails.DefinitionDisplayName` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.   
2026-07-03 |  Enhancement:  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `records.category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `records.callerIpAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.network.http.user_agent, event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `records.properties.clientInfo` raw log field with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `records.properties.httpStatusCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `records.properties.id` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `records.properties.requestUri` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `records.resourceId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `records.correlationId`, `records.resultType` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `records.properties.properties.networkAcls.bypass`, `records.properties.properties.networkAcls.defaultAction`, `records.properties.properties.sku.Family`, `records.properties.properties.sku.Name` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `records.operationVersion`, `records.durationMs`, `records.identity.claim.appid`, `records.properties.properties.enablePurgeProtection`, `records.properties.properties.enableRbacAuthorization`, `records.properties.properties.enableSoftDelete`, `records.properties.properties.enabledForDeployment`, `records.properties.properties.enabledForDiskEncryption`, `records.properties.properties.enabledForTemplateDeployment`, `records.properties.properties.tenantId`, `records.resultSignature` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `records.operationName` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `records.time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-07-08 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `loggingSourceName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added support to `has_principal` which is causing the issue to parser error.   
2025-01-30 |  Enhancement:  
\- Added support for the new pattern of JSON logs.   
2024-11-18 |  Enhancement:  
\- Added support for new pattern of JSON logs.   
2024-10-29 |  Enhancement:  
\- Mapped `properties.isAddressAuthorized`, `properties.isAccessPolicyMatch`, and `properties.isRbacAuthorized` to `target.resource.attribute.labels`.  
\- Mapped `properties.subnetId`, and `properties.privateEndpointId` to `additional.fields`.   
2024-09-25 |  \- Modified condition for `USER_UNCATEGORIZED` event_type.   
2024-02-27 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

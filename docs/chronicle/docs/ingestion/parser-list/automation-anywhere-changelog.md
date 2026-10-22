---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/automation-anywhere-changelog/
title: Change log for AUTOMATION_ANYWHERE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:46:15.529679+00:00
---

# Change log for AUTOMATION_ANYWHERE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/automation-anywhere-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AUTOMATION_ANYWHERE

Date | Changes  
---|---  
2026-01-09 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: mentioned `has_user` to `true` when the user details are available to event.idm.read_only_udm.principal.user.userid UDM field.  
\- Mapped the `USER_LOGIN` and `USER_LOGOUT` event_types when the `event_description` contains `User log in successfully` and `User log out successfully` respectively.   
2025-12-19 |  Enhancement:  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.target.asset.hostname`.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `resource_name` raw log field with `event.idm.read_only_udm.target.asset.ip`.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `audit.hostName` raw log field with `event.idm.read_only_udm.principal.hostname`.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `audit.hostName` raw log field with `event.idm.read_only_udm.principal.asset.hostname`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `audit.userName` raw log field with `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `audit.requestId` raw log field with `event.idm.read_only_udm.metadata.product_log_id`.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `audit.createdOn` raw log field with `event.idm.read_only_udm.metadata.event_timestamp`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `auditdetail.newValue`, `auditdetail.oldValue` raw log fields with `event.idm.read_only_udm.security_result.detection_fields`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped the following raw log fields `audit.source`, `audit.auditType`, `audit.createdBy`, `audit.externalSessionId`, `audit.externalReference.id`, `audit.externalReference.displayName`, `audit.externalReference.type`, `audit.id`, `audit.eventDescription`, `audit.environmentName`, `audit.modelInfo.modelName`, `audit.modelInfo.version`, `audit.modelInfo.revision`, `audit.modelInfo.provider`, `audit.modelInfo.deploymentId`, `audit.modelInfo.region`, `audit.modelInfo.displayName`, `audit.modelInfo.isCustom`, `audit.modelInfo.modelType`, `audit.modelInfo.modelConnectionType`, `audit.modelInfo.customModelName`, `audit.modelInfo.groundedSourceId`, `audit.modelInfo.modelConnectionName`, `audit.encryptedPayload.type`, `audit.encryptedPayload.attributes.promptTokens`, `audit.encryptedPayload.attributes.totalTokens`, `audit.encryptedPayload.attributes.completionTokens`, `audit.executionContext.executionId`, `audit.executionContext.automationName`, `audit.executionContext.deviceId`, `audit.executionContext.botId`, `audit.executionContext.workspaceType`, `audit.executionContext.automationType`, `audit.executionContext.folderPath`, `audit.executionContext.deviceName`, `audit.executionContext.activityId`, `audit.executionContext.plannerId`, `audit.executionContext.agentRequestId`, `audit.aiGuardrail.id_`, `audit.aiGuardrail.name_`, `audit.aiGuardrail.toxicityScore_`, `audit.aiGuardrail.toxicityLevel_`, `audit.aiGuardrail.action_`, `audit.aiEvaluation.id_`, `audit.aiEvaluation.name_`, `audit.aiEvaluation.method_`, `audit.aiEvaluation.status_`, `audit.aiEvaluation.type_`, `audit.aiEvaluation.sourceName_`, `audit.aiEvaluation.routeUrl_`, `audit.encryptedPayload.payload`, `audit.encryptedPayload.iv`, `audit.executionContext.toolInfo` with `event.idm.read_only_udm.additional.fields`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

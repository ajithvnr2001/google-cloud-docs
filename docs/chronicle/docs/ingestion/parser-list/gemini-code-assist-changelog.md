---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gemini-code-assist-changelog/
title: Change log for GEMINI_CODE_ASSIST \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:47.866065+00:00
---

# Change log for GEMINI_CODE_ASSIST  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gemini-code-assist-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GEMINI_CODE_ASSIST

Date | Changes  
---|---  
2026-09-09 |  \- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `insertId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `receiveTimestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `labels.method` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `labels.client_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `jsonPayload.message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `labels.user_id`, `jsonPayload.user.email` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `labels.user_id`, `jsonPayload.user.email` raw log fields with `event.idm.read_only_udm.principal.user.email_addresses` UDM field  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `labels.client_name` raw log field with `event.idm.read_only_udm.principal.application` UDM field  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `jsonPayload.host.name` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields  
\- `event.idm.read_only_udm.principal.asset.hardware.cpu_platform`: Newly mapped `jsonPayload.host.arch` raw log field with `event.idm.read_only_udm.principal.asset.hardware.cpu_platform` UDM field  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `jsonPayload.process.pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `jsonPayload.process.command` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `jsonPayload.process.executable.path` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `jsonPayload.process.executable.name` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `jsonPayload.session.id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `logName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `resource.type` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `resource.labels.resource_container`, `resource.labels.project_id` raw log fields with `event.idm.read_only_udm.target.resource.product_object_id` UDM field  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field  
\- `event.idm.read_only_udm.about.file.full_path`: Newly mapped `jsonPayload.codeCompletionRequest.inputDataContext.additionalContext.files.path`, `jsonPayload.taskCompletionRequest.inputDataContext.additionalContext.files.path` raw log fields with `event.idm.read_only_udm.about.file.full_path` UDM field  
\- `event.idm.read_only_udm.about.labels`: Newly mapped `jsonPayload.codeCompletionRequest.inputDataContext.additionalContext.files.language`, `jsonPayload.codeCompletionRequest.inputDataContext.additionalContext.files.states`, `jsonPayload.taskCompletionRequest.inputDataContext.additionalContext.files.language`, `jsonPayload.taskCompletionRequest.inputDataContext.additionalContext.files.states` raw log fields with `event.idm.read_only_udm.about.labels` UDM field  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `jsonPayload.process.command_args`, `jsonPayload.codeCompletionRequest.inputDataContext.additionalContext.files.segments.content`, `jsonPayload.taskCompletionRequest.inputDataContext.additionalContext.files.segments.content`, `jsonPayload.taskCompletionRequest.input.preamble`, `jsonPayload.taskCompletionRequest.input.messages.author`, `jsonPayload.taskCompletionRequest.input.messages.content`, `labels.request_id`, `labels.prompt_id`, `labels.model`, `labels.product`, `labels.is_agentic`, `labels.instrumentation_source`, `labels.service.instance.id`, `jsonPayload.@type`, `jsonPayload.codeCompletionRequest.inputDataContext.additionalContext.@type`, `jsonPayload.taskCompletionRequest.inputDataContext.additionalContext.@type`, `jsonPayload.metadata.totalTokenCount`, `jsonPayload.auth_type`, `jsonPayload.installation.id`, `jsonPayload.interactive`, `jsonPayload.process.owner`, `jsonPayload.process.runtime.description`, `jsonPayload.process.runtime.name`, `jsonPayload.process.runtime.version`, `jsonPayload.service.instance.id`, `jsonPayload.strategy`, `spanId`, `trace`, `traceSampled` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `resource.labels.location`, `resource.labels.instance_id`, `resource.labels.job`, `resource.labels.task_id`, `resource.labels.namespace` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `Google Cloud Platform` value with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `Gemini Code Assist` value with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- When principal data and target resource data is present, Set the value to USER_RESOURCE_ACCESS.  
\- When only principal data is present , Set the value to STATUS_UPDATE.  
\- When principal data is also not present, Set the value to GENERIC_EVENT.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

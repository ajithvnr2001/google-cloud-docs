---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/circleci-changelog/
title: Change log for CIRCLECI \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:53.410208+00:00
---

# Change log for CIRCLECI  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/circleci-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CIRCLECI

Date | Changes  
---|---  
2026-06-15 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `organization.type` raw log field with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `actor.name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `payload.context_id`, `target_json.type` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `payload.context_name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `actor.type` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `payload.environment_variable_titles`, `account.type`, `common_fields.outcome` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `common_fields.status` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Newly mapped `scope.type` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels` UDM field.   
2025-05-15 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `msg.ACCOUNT_ID` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `msg.ACTOR_ID` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `msg.ID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `msg.OCCURRED_DT` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `msg.OCCURRED_AT` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `msg.ORGANIZATION_ID` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `msg.ORGANIZATION_NAME` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `msg.REQUEST_ID` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.id`: Newly mapped `msg.SCOPE_ID` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.type`: Newly mapped `msg.SCOPE_TYPE` raw log field with `event.idm.read_only_udm.principal.resource.type` UDM field.  
\- `event.idm.read_only_udm.target.resource.id`: Newly mapped `msg.TARGET_ID` raw log field with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- `event.idm.read_only_udm.target.resource.type`: Newly mapped `msg.TARGET_TYPE` raw log field with `event.idm.read_only_udm.target.resource.type` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `msg.ACTOR_TYPE` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `msg.ACTION` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `msg.VERSION` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Newly mapped `msg.PAYLOAD.workflow.id`, `PAYLOAD.workflow.name`, `PAYLOAD.job.status` and `PAYLOAD.job.name` raw log fields with `event.idm.read_only_udm.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Newly mapped `msg.PAYLOAD.workflow.name` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `msg.PAYLOAD.workflow.vcs_branch` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `msg.RAW_JSON.actor.name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `msg.SUCCESS` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `pipeline.vcs.origin_repository_url` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read.only_udm.target.url`: Newly mapped `pipeline.vcs.target_repository_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.   
2025-04-11 |  Enhancement:  
\- `JSON`: Added support for JSON format.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly Mapped `ACCOUNT_ID` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly Mapped `ACTOR_ID` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly Mapped `ID` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly Mapped `METADATA` raw log field to `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly Mapped `branch` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly Mapped `OCCURRED_DT` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field using the format `yyyy-MM-dd`.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly Mapped `ORGANIZATION_ID` raw log field to `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly Mapped `ORGANIZATION_NAME` raw log field to `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly Mapped `REQUEST_ID` raw log field to `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.id`: Newly Mapped `SCOPE_ID` raw log field to `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.type`: Newly Mapped `SCOPE_TYPE` raw log field to `event.idm.read_only_udm.principal.resource.type` UDM field.  
\- `event.idm.read_only_udm.target.resource.id`: Newly Mapped `TARGET_ID` raw log field to `event.idm.read_only_udm.target.resource.id` UDM field.  
\- `event.idm.read_only_udm.target.resource.type`: Newly Mapped `TARGET_TYPE` raw log field to `event.idm.read_only_udm.target.resource.type` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly Mapped `config_source` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly Mapped `pipeline_id` raw log field to `event.idm.read_only_udm.target.resource.id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly Mapped `trigger_source` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly Mapped `ACTOR_TYPE` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly Mapped `ACTION` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly Mapped `VERSION` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly Mapped `via` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2024-12-20 |  Enhancement:  
\- Added support for JSON format logs.   
2023-03-09 |  Created new parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/manage-engine-ad360-changelog/
title: Change log for MANAGE_ENGINE_AD360 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:41.090531+00:00
---

# Change log for MANAGE_ENGINE_AD360  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/manage-engine-ad360-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MANAGE_ENGINE_AD360

Date | Changes  
---|---  
2025-08-05 |  \- Added a new grok pattern for `message` data field to add support for the dropped logs.  
\- Newly added JSON filter for `message` data field to add support for the dropped logs.  
\- Newly added gsub for the `message`, `kv_data1` data field to parse the following log fields.  
\- Added a kv filter for `message`,`kv_data1` data field to parse the following log fields.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `appname` raw log field to event.idm.read_only_udm.principal.application.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field to `event.idm.read_only_udm.principal.hostname` UDM field and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `TechnicianName` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `ModuleName` raw log field to `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `Nombre_de_objeto` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `Nombre_de_dominio` raw log field to `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.security_result.summary` : Newly mapped `Estado` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.target.user.phone_numbers`: Newly mapped `telephoneNumber` raw log field to `event.idm.read_only_udm.target.user.phone_numbers` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `facility`, `priority`, `version`, `Tipo de contraseña` (as key password_type), `Nombre de la plantilla` (as key template_name), `mobile` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `userAccountControl` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name` : Newly mapped `ACTION` raw log field to `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type` : Newly mapped `event.idm.read_only_udm.metadata.event_type` as `NETWORK_CONNECTION` if `has_principal` is `true` and `has_target` is `true`,`USER_CHANGE_PERMISSIONS` if `has_principal` is `true` and `has_target_user` is `true`, `STATUS_UPDATE` if `has_principal` is `true` and has_target is `false`, `GENERIC_EVENT` otherwise.   
2022-09-16 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

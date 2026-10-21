---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/beyondtrust-endpoint-changelog/
title: Change log for BEYONDTRUST_ENDPOINT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:10:34.817281+00:00
---

# Change log for BEYONDTRUST_ENDPOINT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/beyondtrust-endpoint-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BEYONDTRUST_ENDPOINT

Date | Changes  
---|---  
2026-01-22 |  Enhancement:  
\- Added a grok pattern on `host.ip` field to validate that the `host.ip` field is a valid IP address before mapping it to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` to parse the raw log.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `user.LocalIdentifier`, `file.code_signature.subject_name`, `file.type`, `file.gid`, `file.group`, `file.Bundle.Name`, `file.uid`, `group.id`, `EPMWinMac.AuthorizationRequest.ControlAuthorization` and `EPMWinMac.Event.Action` raw log field to event.idm.read_only_udm.additional.fields.   
2024-12-12 |  Enhancement:  
\- Added support to handle SYSLOG + KV logs.   
2024-11-21 |  Enhancement:  
\- Mapped `user.DomainIdentifier`, `user.DomainNetBIOSName`, `user.name`, and `user.domain` to `additional.fields`.   
2024-09-05 |  Enhancement:  
\- Added support for a new pattern of SYSLOG logs.   
2024-08-28 |  Enhancement:  
\- Added support for new log pattern.   
2024-06-10 |  Enhancement:  
\- Enhanced the parser to handle the new logs.  
\- Mapped `Processes.process_exec` to `additional.fields`.  
\- Mapped `Processes.action` to `security_result.action`.  
\- Mapped `Processes.description` to `metadata.description`.  
\- Mapped `Processes.dest` to `target.hostname`.  
\- Mapped `Processes.process_id` to `principal.process.pid`.  
\- Mapped `Processes.user` to `principal.user.userid`.  
\- Mapped `Processes.process` to `principal.application`.  
\- Mapped `Processes.user_id` to `principal.user.windows_sid`.  
\- Mapped `Processes.parent_process_id` to `principal.process.parent_process.pid`.  
\- Mapped `Processes.process_hash`, `Processes.process_name`, `Processes.parent_process`, `Processes.parent_process_exec` to `additional.fields`.  
\- Mapped `Processes.process_path` to `principal.process.parent_process.file.full_path`.   
2024-03-20 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

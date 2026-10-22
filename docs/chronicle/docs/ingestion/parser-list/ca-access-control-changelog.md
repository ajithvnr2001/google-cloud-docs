---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ca-access-control-changelog/
title: Change log for CA_ACCESS_CONTROL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:28.870924+00:00
---

# Change log for CA_ACCESS_CONTROL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ca-access-control-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CA_ACCESS_CONTROL

Date | Changes  
---|---  
2023-07-25 |  Bug-Fix -Removed use case-specific information from default parser.   
2022-06-29 |  Enhancement - Modified grok pattern to parse Update Event log types, shutdown logs and start logs.  
Mapped `timestamp` to `event.idm.read_only_udm.metadata.collected_timestamp` for SEAUDIT FORMAT Logs.  
Mapped `Userid` to `event.idm.read_only_udm.target.user.userid` for Update User, Update Group.  
Mapped `event.idm.read_only_udm.metadata.event_type` [User_Uncategorized for Update (User,File,Program,Hnode) and Group_Uncategorized for Update(Group)].  
Mapped `about.labels` for Update Hnode log type with key as `policy_name`.  
Mapped `event.idm.read_only_udm.target.resource.name` for Update Hnode Log Type.  
Mapped `event.idm.read_only_udm.target.process.command_line` for Update Events.  
Mapped `event.idm.read_only_udm.src.user.userid` with the raw field User Name.  
Mapped `event.idm.read_only_udm.security_result.rule_type` with command_type for `Security database administration` event type.   
2022-04-13 |  Enhancement-Mapped the following fields: status, reason, stage, class, resource, access, event header, administrator, command, type, sequence number, daemon.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

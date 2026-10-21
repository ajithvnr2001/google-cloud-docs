---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium_th_changelog/
title: Change log for TANIUM_TH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:46:00.479556+00:00
---

# Change log for TANIUM_TH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium_th_changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TANIUM_TH 

Date | Changes | 2022-03-30 | Enhancement to map following raw logs elements to UDM elements:   
Mapped field "additional.event__TargetSid" and "additional.event__TargetUserSid" to "target.user.windows_sid".   
Mapped field "additional.event__SubjectUserName" to "principal.user.user_display_name".   
Mapped field "additional.event__CallerProcessId" and "additional.event__ClientProcessId" to "principal.process.pid".   
Mapped field "additional.event__CallerProcessName" to "principal.process.file.full_path".   
Mapped filed "additional.event__FQDN" to "principal.hostname".   
Mapped field "additional.event__ParentProcessName" to "principal.process.parent_process.file.full_path".   
Mapped field "additional.event__CommandLine" to "target.process.command_line".   
Mapped field "additional.event__NewProcessId" to "target.process.pid".   
Mapped field "additional.event__NewProcessName" to "target.process.file.full_path".   
Mapped field "additional.event__ParentProcessId" to "principal.process.parent_process.pid".   
Mapped field "additional.event__ObjectServer" to "security_result.category_details".   
Mapped field "additional.event__Service" to "security_result.description".   
Mapped field "additional.event__PrivilegeList" to "principal.user.attribute.permissions".   
Mapped field "additional.event__TransmittedServices", "additional.event__LmPackageName", "additional.event__TokenElevationType", "additional.event__MandatoryLabel", "additional.event__AlgorithmName", "additional.event__KeyName", "additional.event__KeyType", "additional.event__Operation", "additional.event__ProviderName", "additional.event__ReturnCode", "additional.event__RpcCallClientLocality", "additional.event__ClientProcessStartKey", "additional.event__TaskContentNew", "additional.event__TaskName", "additional.event__Status", "additional.event__FailureReason", "additional.event__SubStatus", "additional.event__KeyLength", "additional.event__RestrictedAdminMode", "additional.event__TargetLinkedLogonId", "additional.event__TargetOutboundUserName", "additional.event__TargetOutboundDomainName" to "additional.fields".   
Changed mapping for "additional.event__VirtualAccount", "additional.event__ElevatedToken", "additional.event__ImpersonationLevel", "additional.event__TargetLogonId", "additional.event__SubjectLogonId" from "about.labels" to "additional.fields".   
  
---|---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

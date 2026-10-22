---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workspace-alerts-changelog/
title: Change log for WORKSPACE_ALERTS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:50.413893+00:00
---

# Change log for WORKSPACE_ALERTS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workspace-alerts-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WORKSPACE_ALERTS

Date | Changes  
---|---  
2026-01-27 |  \- security_result.action: Extended support for `data.ruleViolationInfo.triggeredActionTypes` raw log field with `security_result.action` UDM field.   
2025-10-29 |  \- `APNS certificate is expiring soon`: Added support for the alert type `APNS certificate is expiring soon` and relevant corresponding raw log fields.  
\- `APNS certificate has expired`: Added support for the alert type `APNS certificate has expired` and relevant corresponding raw log fields.   
2024-10-08 |  \- Mapped all fields in `message` raw log field to `security_result.detection_fields` with separate `security_result` block for each message.   
2024-07-26 |  \- Updated the field name from `emailaddress` to `emailAddress`  
2023-11-29 |  \- Updated mapping to map the first occurrence of domain values in the recipients array to `target.domain.name` and other occurrences to `additional` UDM field.  
\- Added additional mappings for deprecated labels.   
2023-11-01 |  Enhancement to use `base64` hex decode function to parse IP addresses.   
2023-10-04 |  Added support for new Alert Types for source `Reporting Rule`.   
2023-09-06 |  Added support for new Alert Types for source `UserChanges` and `AppSettingsChanged`.   
2023-04-12 |  Promoted `WORKSPACE_ALERTS` parser to default.  
For the field mapping reference, see [https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workspace-activity#field-mapping>Collect Google Workspace logs](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/<code).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

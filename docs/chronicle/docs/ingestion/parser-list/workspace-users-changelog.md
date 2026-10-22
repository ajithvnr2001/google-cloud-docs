---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workspace-users-changelog/
title: Change log for WORKSPACE_USERS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:49.354442+00:00
---

# Change log for WORKSPACE_USERS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workspace-users-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WORKSPACE_USERS

Date | Changes  
---|---  
2025-08-27 |  \- additional.fields: Newly mapped all key-value pairs from the `customSchemas` object in the raw log to the `additional.fields` UDM field.   
2025-07-16 |  Updated the parser to correctly handle edge cases for the addresses.formatted raw field.   
2024-03-27 |  Removed the mapping of the extracted user ID from the `primaryEmail` raw log field to the `entity.user.userid` UDM field.   
2023-11-29 |  Added additional mappings for deprecated labels.   
2023-09-06 |  Modified logic for relations object to handle missing field `value`.   
2023-07-26 |  Updated mapping of `lastLoginTime` field from `entity.user.attribute.labels` to `entity.user.last_login_time`.   
2023-04-12 |  Promoted `WORKSPACE_USERS` parser to default.  
For the field mapping reference, see [https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workspace-activity#field-mapping>Collect Google Workspace logs](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/<code).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ocsf-changelog/
title: Change log for OCSF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:27:57.603522+00:00
---

# Change log for OCSF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ocsf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OCSF

Date | Changes  
---|---  
2025-11-25 |  Newly mapped key-value pairs from the `raw_data` raw log field. The potentially nested structure within `raw_data` is flattened into the additional.fields array. Each entry in this array has a key field, representing the concatenated path to the value within the original JSON structure (e.g., parentkey_childkey_grandchildkey).  
additional.fields: Newly mapped `raw_data` raw log field with `additional.fields` UDM field   
2025-11-03 |  Added support for the event `Detection Finding` for some of the objects and its corresponding raw log fields into OCSF parser.   
2025-09-05 |  Added support for the event `Detection Finding` and relevant corresponding raw log fields into OCSF parser.   
2025-04-28 |  Handled the index overriding issue in the for loop.   
2025-02-26 |  Added support for the categories of OCSF schema v1.1.0: System Activity (Process Activity), Findings (Security Finding), Identity and Access Management (Authentication, Authorized Session), Network Activity (Network Activity, HTTP Activity, DNS Activity, FTP Activity, Network File Activity), Application Activity (API Activity).   
2025-01-30 |  Handled the error in the convert filter for the field `connection_info.direction_id`.   
2023-10-30 |  Added support for additional two activity types.   
2023-06-28 |  Promoted parser to default.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

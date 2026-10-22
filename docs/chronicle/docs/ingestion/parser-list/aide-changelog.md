---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aide-changelog/
title: Change log for AIDE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:44.015904+00:00
---

# Change log for AIDE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aide-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AIDE

Date | Changes  
---|---  
2025-03-10 |  Enhancement:  
\- Mapped `host` to `principal.hostname`.  
\- Mapped `path` to `principal.file.full_path`.  
\- Mapped `total_files`, `added_files`, `removed_files`, `changed_files`, `old_timestamp`, `old_perms`, `old_sha256`, `old_md5`, and `old_acl` to `principal.asset.attribute.labels`.  
\- Mapped `new_timestamp`, `new_perms`, `new_sha256`, `new_md5`, and `new_acl` to `target.asset.attribute.labels`.  
\- Mapped `old_size` to `principal.file.size`.  
\- Mapped `new_size` to `target.file.size`.   
2024-10-24 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

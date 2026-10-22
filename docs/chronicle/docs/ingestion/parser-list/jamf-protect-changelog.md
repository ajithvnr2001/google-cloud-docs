---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-protect-changelog/
title: Change log for JAMF_PROTECT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:42.578977+00:00
---

# Change log for JAMF_PROTECT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-protect-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for JAMF_PROTECT

Date | Changes  
---|---  
2026-06-30 |  \- `metadata.event_type`: Added event parsing for the event_types `auth-signal`, `auth-setflags`, `mount`, `exec`, `nmap` and `auth-exec`.  
\- `additional.fields`: Newly mapped `input.match.event.cwd` raw log field with `additional.fields` UDM field.  
\- `additional.fields`: Newly mapped `input.match.event.sig` raw log field with `additional.fields` UDM field.  
\- `target.file.full_path`: Newly mapped `input.match.event.targetPath` raw log field with `target.file.full_path` UDM field.  
\- `additional.fields`: Removed mapping of `input.related.files.objectType` to key `input_related_files_objecttype` from `additional.fields` UDM field and mapped to key `input_related_files_objecttype_%{index}` instead to prevents duplicate key collisions when parsing logs containing multiple files.   
2024-10-08 |  Update the gsub filter to support the logs.   
2024-05-01 |  Added additional mappings for deprecated labels.   
2024-02-06 |  Added support for the event `GPScreenshotEvent` and the raw log fields associated with that event.  
\- Mapped the raw log field `input.host.os` with the UDM field `principal.platform_version`  
\- Mapped the raw log field `input.host.protectVersion` with the UDM field `principal.asset.attribute.labels`  
\- Mapped the raw log field `input.match.facts.matchReason` with the UDM field `security_result.detection_fields`  
\- Mapped the raw log field `input.match.version` with the UDM field `additional.fields`  
\- Mapped the raw log field `input.related.files.objectType` with the UDM field `additional.fields`  
2024-01-03 |  \- Updated logic for `file.inode` raw log field.   
2023-11-22 |  \- Updated logic for `file.inode` raw log field.  
\- Align `principal.hostname, target.hostname, `principal.asset.hostname, and target.asset.hostname' mapping.   
2023-06-28 |  Promoted JAMF_PROTECT parser to default.  
For the field mapping reference, see [https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-protect>Collect Jamf Protect logs](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/<code).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

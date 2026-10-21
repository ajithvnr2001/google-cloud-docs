---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-casb-changelog/
title: Change log for ZSCALER_CASB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:16:08.804424+00:00
---

# Change log for ZSCALER_CASB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-casb-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ZSCALER_CASB

Date | Changes  
---|---  
2026-05-06 |  \- Updated the mapping for raw log fields `applicationname` and `appname`, moving them from `principal.application` to `target.application` to ensure more accurate field alignment.   
2026-04-29 |  \- target.file.mime_type: Removed mapping of `filetypename` from `target.file.mime_type` UDM field in order to introduce a more accurate mapping for `File` event.  
\- target.file.file_type: Mapped `filetypename` raw log field with `target.file.file_type` UDM field using conditional logic if the raw log field `filetypename` is not empty and not equal to `None`. This mapping aligns the recognized file types with their corresponding UDM `file_type` ENUM values. File types not explicitly mapped to a UDM ENUM are mapped with`additional.fields[filetypename]` UDM field for `File` event.  
\- target.file.mime_type: Removed mapping of `filetype` from `target.file.mime_type` UDM field in order to introduce a more accurate mapping for `Gen AI` event.  
\- target.file.file_type: Mapped `filetype` raw log field with `target.file.file_type` UDM field using conditional logic if the raw log field `filetype` is not empty and not equal to `None`. This mapping aligns the recognized file types with their corresponding UDM `file_type` ENUM values. File types not explicitly mapped to a UDM ENUM are mapped with`additional.fields[filetype]` UDM field for `Gen AI` event.   
2026-01-06 |  \- Updated the field mapping for the Zscaler CASB parser. Please refer to the parser documentation page for information regarding the updated UDM mappings - https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-casb#udm_mapping_delta   
2025-11-28 |  \- principal.user.department: Newly mapped `departmentname` raw log field with `principal.user.department` UDM field.  
\- target.user.userid: Newly mapped `extusername` raw log field with `target.user.userid` UDM field.  
\- target.file.file_type: Newly mapped `filetype` raw log field with `target.file.file_type` UDM field, if the `filetype` raw log value contains `ppt` or `pdf`.  
\- additional.fields[filetype]: Newly mapped `filetype` raw log field with `additional.fields[filetype]` UDM field, if the `filetype` raw log value does not contain `ppt` or `pdf`.  
\- additional.fields[download_time]: Newly mapped `download_time` raw log field with `additional.fields[download_time]` UDM field.  
\- additional.fields[runid]: Newly mapped `runid` raw log field with `additional.fields[runid]` UDM field.  
\- additional.fields[scan_time]: Newly mapped `scan_time` raw log field with `additional.fields[scan_time]` UDM field.  
\- additional.fields[scanid]: Newly mapped `scanid` raw log field with `additional.fields[scanid]` UDM field.  
\- additional.fields[file_doctype]: Newly mapped `file_doctype` raw log field with `additional.fields[file_doctype]` UDM field.  
\- additional.fields[filesha]: Newly mapped `filesha` raw log field with `additional.fields[filesha]` UDM field.  
\- additional.fields[sender_type]: Newly mapped `sender_type` raw log field with `additional.fields[sender_type]` UDM field.  
\- security_result.detection_fields[last_edit_user]: Newly mapped `last_edit_user` raw log field with `security_result.detection_fields[last_edit_user]` UDM field.  
\- security_result.detection_fields[last_share_user]: Newly mapped `last_share_user` raw log field with `security_result.detection_fields[last_share_user]` UDM field.  
\- security_result.detection_fields[last_shared_on]: Newly mapped `last_shared_on` raw log field with `security_result.detection_fields[last_shared_on]` UDM field.  
\- security_result.detection_fields[botname]: Newly mapped `botname` raw log field with `security_result.detection_fields[botname]` UDM field.  
\- security_result.detection_fields[dlpengnames]: Newly mapped `dlpengnames` raw log field with `security_result.detection_fields[dlpengnames]` UDM field.  
\- security_result.detection_fields[extcollab_groups]: Newly mapped `extcollab_groups` raw log field with `security_result.detection_fields[extcollab_groups]` UDM field.  
\- security_result.detection_fields[intcollab_groups]: Newly mapped `intcollab_groups` raw log field with `security_result.detection_fields[intcollab_groups]` UDM field.  
\- security_result.detection_fields[oextcollab_groups]: Newly mapped `oextcollab_groups` raw log field with `security_result.detection_fields[oextcollab_groups]` UDM field.  
\- security_result.detection_fields[ointcollab_groups]: Newly mapped `ointcollab_groups` raw log field with `security_result.detection_fields[ointcollab_groups]` UDM field.  
\- security_result.detection_fields[dlpdictcnts]: Newly mapped `dlpdictcnts` raw log field with `security_result.detection_fields[dlpdictcnts]` UDM field.   
2025-06-04 |  \- Updated the parser to handle logs where the `RESPCODE` raw field has a `NA` value.   
2025-04-30 |  \- Promoted ZSCALER_CASB Premium parser to default. You can see full details in the parser configuration page - https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-zscaler-logs   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

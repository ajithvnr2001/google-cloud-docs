---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-webproxy-changelog/
title: Change log for ZSCALER_WEBPROXY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:31:09.470931+00:00
---

# Change log for ZSCALER_WEBPROXY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-webproxy-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ZSCALER_WEBPROXY

Date | Changes  
---|---  
2026-06-09 |  Handled edge case for handling `odlpdict` and `b64threatname` log fields.   
2026-05-21 |  Handled edge case for `security_result.detection_fields[obwclassname]` UDM field.   
2026-04-30 |  \- security_result.description: Raw log field `reason` is mapped to `security_result.description` UDM field irrespective of the value of the `action` raw log field. Previously, the `reason` raw log field was mapped to the `security_result.description` UDM field only if `action` raw log field is equal to `Blocked`.   
2026-03-27 |  Refactored the mapping of raw log fields `filetype` and `upload_filetype` to the UDM field `additional.fields[file_type]` from the include file `file_type_enum.include` to the parser config file.   
2026-03-03 |  Handled edge case for `principal.port`UDM field.   
2026-02-20 |  Updated field mapping in the Zscaler Webproxy parser.  
\- target.file.mime_type: Removed mapping of `filetype` from `target.file.mime_type` UDM field in order to introduce a more accurate mapping.  
\- target.file.file_type: Mapped `filetype` raw log field with `target.file.file_type` UDM field using conditional logic if the raw log field `filetype` is not empty and not equal to `None`. This mapping aligns the recognized file types with their corresponding UDM `file_type` ENUM values. File types not explicitly mapped to a UDM ENUM are mapped with`additional.fields[file_type]` UDM field.  
\- target.file.mime_type: Removed mapping of `upload_filetype` from `target.file.mime_type` UDM field in order to introduce a more accurate mapping.  
\- target.file.file_type: Mapped `upload_filetype` raw log field with `target.file.file_type` UDM field using conditional logic if the raw log field `filetype` is empty or equal to `None`. This mapping aligns the recognized file types with their corresponding UDM `file_type` ENUM values. File types not explicitly mapped to a UDM ENUM are mapped with`additional.fields[file_type]` UDM field.  
\- additional.fields: Removed mapping of `contenttype` from `additional.fields[content_type]` UDM field in order to introduce a more accurate mapping.  
\- target.file.mime_type: Mapped `contenttype` raw log field with `target.file.mime_type` UDM field.   
2026-01-12 |  \- Updated the field mapping for the Zscaler Webproxy parser. Please refer to the parser documentation page for information regarding the updated UDM mappings - https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-webproxy#udm_mapping_delta   
2025-11-28 |  \- security_result.rule_name: Newly mapped `ft_rulename` raw log field with `security_result.rule_name` UDM field.  
\- additional.fields[time]: Newly mapped `time` raw log field with `additional.fields[time]` UDM field.  
\- additional.fields[upload_doc_sub_type]: Newly mapped `upload_doc_sub_type` raw log field with `additional.fields[upload_doc_sub_type]` UDM field.  
\- additional.fields[client_tls_keyex_non_pqc_offers]: Newly mapped `client_tls_keyex_non_pqc_offers` raw log field with `additional.fields[client_tls_keyex_non_pqc_offers]` UDM field.   
2025-10-28 |  \- security_result.rule_name: Newly mapped `ssl_rulename` raw log field with `security_result.rule_name` UDM field  
\- additional.fields[client_tls_keyex_pqc_offers]: Newly mapped `client_tls_keyex_pqc_offers` raw log field with `additional.fields[client_tls_keyex_pqc_offers]` UDM field  
\- additional.fields[client_tls_keyex_hybrid_offers]: Newly mapped `client_tls_keyex_hybrid_offers` raw log field with `additional.fields[client_tls_keyex_hybrid_offers]` UDM field  
\- additional.fields[client_tls_keyex_unknown_offers]: Newly mapped `client_tls_keyex_unknown_offers` raw log field with `additional.fields[client_tls_keyex_unknown_offers]` UDM field  
\- additional.fields[client_tls_sig_pqc_offers]: Newly mapped `client_tls_sig_pqc_offers` raw log field with `additional.fields[client_tls_sig_pqc_offers]` UDM field  
\- additional.fields[client_tls_sig_non_pqc_offers]: Newly mapped `client_tls_sig_non_pqc_offers` raw log field with `additional.fields[client_tls_sig_non_pqc_offers]` UDM field  
\- additional.fields[client_tls_sig_hybrid_offers]: Newly mapped `client_tls_sig_hybrid_offers` raw log field with `additional.fields[client_tls_sig_hybrid_offers]` UDM field  
\- additional.fields[client_tls_sig_unknown_offers]: Newly mapped `client_tls_sig_unknown_offers` raw log field with `additional.fields[client_tls_sig_unknown_offers]` UDM field  
\- additional.fields[client_tls_keyex_alg]: Newly mapped `client_tls_keyex_alg` raw log field with `additional.fields[client_tls_keyex_alg]` UDM field  
\- additional.fields[client_tls_sig_alg]: Newly mapped `client_tls_sig_alg` raw log field with `additional.fields[client_tls_sig_alg]` UDM field  
\- additional.fields[server_tls_keyex_alg]: Newly mapped `server_tls_keyex_alg` raw log field with `additional.fields[server_tls_keyex_alg]` UDM field  
\- additional.fields[server_tls_sig_alg]: Newly mapped `server_tls_sig_alg` raw log field with `additional.fields[server_tls_sig_alg]` UDM field   
2025-10-14 |  Added edge-case handling for raw log field `upload_filename_temp`.   
2025-09-15 |  Improved error handling to cover various edge cases across multiple scenarios.   
2025-09-04 |  \- target.file.full_path: Newly mapped `upload_filename` raw log field with `target.file.full_path` UDM field if `filename` raw log field is equal to `None` and the `upload_filename` raw log field is not equal to `None`.  
\- target.resource.attribute.labels[upload_filename]: Newly mapped `upload_filename` raw log field with `target.resource.attribute.labels[upload_filename]` UDM field if `filename` raw log field is not equal to `None` and the `upload_filename` raw log field is not equal to `None`.   
2025-06-13 |  \- Fix the event timestamp format issue for the formats `yyyy-MM-dd HH:mm:ss` and `yyyy-MM-ddTHH:mm:ssZ`.  
\- Improved the parser performance to remove security_result.risk_score if pagerisk contains invalid values, as per the UDM documentation.   
2025-05-30 |  \- Added condition to handle timezone for `America/New York`.   
2025-05-08 |  \- Promoted ZSCALER_WEBPROXY Premium parser to default. You can see full details in the parser configuration page - https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-zscaler-logs   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

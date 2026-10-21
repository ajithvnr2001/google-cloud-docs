---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-zpa-changelog/
title: Change log for ZSCALER_ZPA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:58:24.882163+00:00
---

# Change log for ZSCALER_ZPA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-zpa-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ZSCALER_ZPA

Date | Changes  
---|---  
2026-06-30 |  \- security_result.action: Updated the parser to skip mapping of `security_result.action` UDM field when the `InternalReason` log field is empty.   
2026-05-06 |  \- Enhanced conditional mapping of user information to either map with `principal.user` or `target.user` UDM field based on the `InternalReason` log field.   
2026-01-07 |  \- Updated the field mapping for the Zscaler ZPA parser.  
\- Please refer to the parser documentation page for information regarding the updated UDM mappings - https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-zpa#udm_mapping_delta   
2025-11-28 |  \- additional.fields[protocol_version]: Newly mapped `ProtocolVersion` raw log field with `additional.fields[protocol_version]` UDM field.  
\- principal.user.userid: Newly mapped `UserID` raw log field with `principal.user.userid` UDM field, if the value of `InternalReason` raw log field is not equal to `ZPN_STATUS_AUTHENTICATED` or `ZPN_STATUS_DISCONNECTED`.  
\- principal.user.user_display_name: Newly mapped `UserID` raw log field with `principal.user.user_display_name` UDM field, if the value of `InternalReason` raw log field is not equal to `ZPN_STATUS_AUTHENTICATED` or `ZPN_STATUS_DISCONNECTED`.  
\- principal.user.email_addresses: Newly mapped `UserID` raw log field with `principal.user.email_addresses` UDM field, if the value of `InternalReason` raw log field is not equal to `ZPN_STATUS_AUTHENTICATED` or `ZPN_STATUS_DISCONNECTED`.  
\- target.user.userid: Newly mapped `UserID` raw log field with `target.user.userid` UDM field, if the value of `InternalReason` raw log field is equal to `ZPN_STATUS_AUTHENTICATED` or `ZPN_STATUS_DISCONNECTED`.  
\- target.user.user_display_name: Newly mapped `UserID` raw log field with `target.user.user_display_name` UDM field, if the value of `InternalReason` raw log field is equal to `ZPN_STATUS_AUTHENTICATED` or `ZPN_STATUS_DISCONNECTED`.  
\- target.user.email_addresses: Newly mapped `UserID` raw log field with `target.user.email_addresses` UDM field, if the value of `InternalReason` raw log field is equal to `ZPN_STATUS_AUTHENTICATED` or `ZPN_STATUS_DISCONNECTED`.   
2025-11-14 |  \- target.hostname: Modified mapping for the `Host` raw log field. When the value is an IP address, it is now mapped to `target.ip` and no longer to `target.hostname` and `target.asset.hostname`. When the value is not an IP address, it remains mapped to `target.hostname` and `target.asset.hostname`.   
2025-10-30 |  Modified the value mapping logic for the `security_result.action` UDM field to correct an issue where events were too often marked as `BLOCK`.  
\- security_result.action: Removed the condition that set the value of `security_result.action` UDM field based on the value of `ConnectionStatus` raw log field.  
\- security_result.action: Modified the codition to set the value of `security_result.action` UDM field based on the value of `InternalReason` raw log field. The value of `security_result.action` UDM field set to `BLOCK` only if the value of `InternalReason` raw log field is one of the following: `BRK_MT_SETUP_FAIL_NO_POLICY_FOUND`, `BRK_MT_SETUP_FAIL_REJECTED_BY_POLICY`, or `BRK_MT_SETUP_FAIL_SAML_EXPIRED`. The value of `security_result.action` UDM field set to `ALLOW` for all other values of `InternalReason` raw log field.   
2025-05-08 |  \- Promoted ZSCALER_ZPA Premium parser to default. You can see full details in the parser configuration page - https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-zscaler-logs   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rsa-securid-changelog/
title: Change log for RSA_SECURID \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:28.744913+00:00
---

# Change log for RSA_SECURID  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rsa-securid-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for RSA_SECURID

Date | Changes  
---|---  
2024-12-23 |  Enhancement:  
\- Changed mapping of `column4` from `principal.ip` to `target.ip`.  
\- Changed mapping of `column5` from `target.ip` to `principal.ip`.  
\- If audit_section is equal to `audit.runtime.com.rsa.ims.authn.impl.AuthenticationBrokerImpl`, changed mapping of `hostname` from `principal.hostname` to `target.hostname`.   
2024-06-07 |  Enhancement:  
\- Added support for `audit_section` logs, such as `audit.admin.com.rsa.authmgr.internal.admin.tokenmgt.impl.TokenAdministrationImpl`, `audit.admin.com.rsa.authmgr.internal.admin.attributemgt.impl.AttributeDefinitionAdministrationImpl`, and "`audit.runtime.com.rsa.ims.authn.impl.AuthenticationBrokerImpl`.   
2024-04-23 |  \- Mapped `time` and `column1` to `metadata.event_timestamp`.   
2024-03-17 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-ad-changelog/
title: Change log for WINDOWS_AD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:47:07.254324+00:00
---

# Change log for WINDOWS_AD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-ad-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WINDOWS_AD

Date | Changes  
---|---  
2026-08-26 |  \- `entity.user.email_addresses`: Newly mapped `UserPrincipalName` raw log field with `entity.user.email_addresses` UDM field.   
2025-07-08 |  \- Fixed the flakiness of the parser.   
2025-06-13 |  Enhancement:  
\- `group`: Added support for the entity `group` and relevant corresponding raw log fields.   
2025-04-02 |  Enhancement:  
\- `entity.user.phone_numbers`: Newly mapped `otherMobile` raw log field with `entity.user.phone_numbers` UDM.   
2024-11-06 |  Enhancement:  
\- Mapped `OU` and `DC` to `relations.entity.user.attribute`.   
2024-10-08 |  Enhancement:  
\- `DistinguishedName` and `MemberOf` mapped to `relations.entity`.   
2024-07-10 |  Added support of Byte Order Mark removal from the logs that rendered the logs invalid.   
2024-03-27 |  Added support of winlogbeat logs.   
2024-01-31 |  Added support of `ObjectGUID` raw log field.   
2023-08-09 |  Updated mapping of fields `LastLogonDate`, `PasswordLastSet`,  
`AccountExpirationDate`, `LastBadPasswordAttempt`, and `AccountLockoutTime`.   
2023-08-01 |  Added the `on_error` check wherever the `date` filter is being used.   
2023-07-12 |  Mapped only `hostname`, instead of `FQDN`, to `entity.asset.hostname`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

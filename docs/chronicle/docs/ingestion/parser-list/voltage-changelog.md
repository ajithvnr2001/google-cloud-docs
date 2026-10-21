---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/voltage-changelog/
title: Change log for VOLTAGE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:14:04.006607+00:00
---

# Change log for VOLTAGE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/voltage-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VOLTAGE

Date | Changes  
---|---  
2025-06-11 |  Enhancement:  
\- Added grok pattern to support new format of SYSLOG logs.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `cef_product` raw field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `version` raw field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `event_id` raw field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `severity` raw field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `district` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `identity` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname`: Newly mapped `shost` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `requestClientApplication` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `length` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.mechanism`: Newly mapped `AuthenticationMethod` raw log field with `event.idm.read_only_udm.extensions.auth.mechanism` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `request` raw field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped path `raw` field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.nanos"`: Newly mapped `requestTimeMillis` raw field with `event.idm.read_only_udm.network.session_duration.nanos` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `timeMillis` raw field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.observer.application`: Newly mapped cvProduct raw log field with `event.idm.read_only_udm.observer.application` UDM field.  
\- `event.idm.read_only_udm.observer.labels`: Newly mapped `cvapi`, `cvframework` and `cvdevice` raw log fields with `event.idm.read_only_udm.observer.labels` UDM field.  
\- `event.idm.read_only_udm.observer.platform`: Newly mapped `cvos` raw log field with `event.idm.read_only_udm.observer.platform` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `msg` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `proxyConnectionIp` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped raw fields`: `rollover`, `merchantId`, `keyId`, `phaseBit`, `leadingDigits`, `trailingDigits`, `elapsedTimeMillis`, `authTokens`, `isUserPassSet`, `proxyType`, `attemptedAuthMethods`, `out` and `masked` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped raw fields `cached`,`fullIdentity`, `algorithm`, `returnEncryptedKeyOption`, `authMethodName`, `authType`, `authTimeMillis`, `hsmEnabled`, `wrappedMode`, `format`, `returnFullIdentity`, `acceptBadData` and `CachedAuthentication` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` if `has_principal`and `has_target` or `has_user` is `true` and `prod_event_name` is `authenticated user` or `failed to authenticate user`.  
-event.idm.read_only_udm.security_result.action`: Mapped `event.idm.read_only_udm.security_result.action` to `ALLOW` if `prod_event_name` is `authenticated user` else set it to `BLOCK` if `prod_event_name` is `failed to authenticate user`.   
2024-07-02 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

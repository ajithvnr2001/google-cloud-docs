---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/keycloak-changelog/
title: Change log for KEYCLOAK \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:54:08.863606+00:00
---

# Change log for KEYCLOAK  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/keycloak-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for KEYCLOAK

Date | Changes  
---|---  
2026-01-23 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `typeEv` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `environnement` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `status_code` raw log field to `event.idm.read_only_udm.network.http.response_code` UDM field.   
2026-01-01 |  Enhancement:  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Removed mapping of `ctx.host` raw log field from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field inorder to introduce a more accurate mapping.  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip: Removed mapping of `ctx.ip` raw log field from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field inorder to introduce a more accurate mapping.  
\- event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname: Newly mapped `ctx.host` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `ctx.ip` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` if `payload.type` is `LOGIN` and `has_user` is `true`.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT` if `payload.type` is `LOGOUT` and `has_user` is `true`.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` if `typeEv` is `USER_INFO_REQUEST` and `has_resource` is `true`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `refresh_token_id`, and `token_id` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-30 |  Enhancement:  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `ctx.clientId` raw log field to `event.idm.read_only_udm.principal.application`.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `ctx.host` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `ctx.ip` raw log field to `event.idm.read_only_udm.target.ip`.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `ctx.realmId` raw log field to `event.idm.read_only_udm.target.administrative_domain`.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `ctx.requestId` raw log field to `event.idm.read_only_udm.metadata.product_log_id`.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `ctx.sessionId` raw log field to `event.idm.read_only_udm.network.session_id`.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `ctx.uri` raw log field to `event.idm.read_only_udm.target.url`.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `ctx.userAgent` raw log field to `event.idm.read_only_udm.network.http.user_agent`.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `ctx.userId` raw log field to `event.idm.read_only_udm.principal.user.product_object_id`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `ctx.username` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `env.application` raw log field to `event.idm.read_only_udm.target.application`.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `env.instance` raw log field to `event.idm.read_only_udm.target.resource.name`.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `ctx.referer` raw log field to `event.idm.read_only_udm.network.http.referral_url`.  
\- Added logic to iterate through the `events` array in the raw log and mapped the whole array to `event.idm.read_only_udm.additional.fields`.   
2024-09-17 |  Enhancement:  
\- Mapped `username` from `details_json` to `target.user.userid`.  
\- Mapped `redirect_uri` from `details_json` to `target.url`  
\- Mapped `realm_id` and `client_id` to `additional.fields`  
2024-07-09 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

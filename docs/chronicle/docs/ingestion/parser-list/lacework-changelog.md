---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/lacework-changelog/
title: Change log for LACEWORK \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:43.166561+00:00
---

# Change log for LACEWORK  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/lacework-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for LACEWORK

Date | Changes  
---|---  
2025-06-27 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.summary` : Newly mapped `event_title` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.description` : Newly mapped `event_description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.confidence_details` : Newly mapped `summary_details` raw log field with `event.idm.read_only_udm.security_result.confidence_details` UDM field.  
\- `event.idm.read_only_udm.target.user.userid` : Newly mapped `target_user_id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id` : Newly mapped `resource_product_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field and set `has_target_resource` to `true`.  
\- `event.idm.read_only_udm.target.user.role_name` : Newly mapped `user_role` raw log field with `event.idm.read_only_udm.target.user.role_name` UDM field.  
\- `event.idm.read_only_udm.target.resource.name` : Newly mapped `account_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field and set `has_target_resource` to `true`.  
\- `event.idm.read_only_udm.target.application` : Newly mapped `application` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id` : Newly mapped `event_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type` : Newly mapped `event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details` : Newly mapped `event_severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid` : Newly mapped `lacework_account` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field and set `has_principal_user` to `true`.  
\- `event.idm.read_only_udm.metadata.url_back_to_product` : Newly mapped `event_link` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `starttimevalue` and `endtimevalue` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels` : Newly mapped `intgGuid` and `rec_id` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field and set `has_target_resource` to `true`.  
\- `event.idm.read_only_udm.metadata.product_name` : Newly mapped `event_source` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp` : Newly mapped `event_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type` : Modified mapping of `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` when (`has_principal_user` is `true` and `has_target_resource` are `true`) or `has_prin_resource` is `true`.   
2025-02-24 |  Enhancement:  
\- Mapped `ACCOUNT`, `EVENT_CATEGORY`, `subject.srcEvent.recipientAccountAlias`, `DERIVED_FIELDS.SOURCE`, `subject.srcEvent.event.userIdentity.accessKeyId`, `subject.srcEvent.event.userIdentity.arn`, `subject.srcEvent.event.errorCode`, `subject.srcEvent.event.errorMessage`, `subject.srcEvent.event.eventID`, `subject.srcEvent.event.eventSource`, `subject.srcEvent.event.userIdentity.sessionContext.attributes.mfaAuthenticated`, `subject.srcEvent.username`, `subject.startTime`, `subject.srcEvent.eventName`, `DERIVED_FIELDS.CATEGORY`, `DERIVED_FIELDS.SUBCATEGORY`, `subject.dstEvent.gbm_version`, `subject.dstEvent.is_visible`, `subject.dstEvent.severity`, `subject.dstEvent.recipientAccountAlias`, `subject.srcEvent.api`, `subject.srcEvent.calltype`, `subject.srcEvent.gbm_version`, `subject.srcEvent.is_visible`, and `subject.srcEvent.severity` to `additional.fields`.  
\- Mapped `SUMMARY` to `metadata.description`.  
\- Mapped `EVENT_TYPE` to `metadata.product_event_type`.  
\- Mapped `EVENT_ID` to `metadata.product_log_id`.  
\- Mapped `LINK` to `metadata.url_back_to_product`.  
\- Mapped `subject.srcEvent.event.userAgent`, `subject.srcEvent.source` to `network.http.user_agent`.  
\- Mapped `subject.srcEvent.recipientAccountId` to `principal.user.groupid`.  
\- Mapped `subject.srcEvent.principalId` to `principal.user.userid`.  
\- Mapped `subject.srcEvent.event.awsRegion` to `security_result.about.asset.attribute.cloud.availability_zone`.  
\- Mapped `subject.srcEvent.event.eventCategory` to `security_result.about.asset.category`.  
\- Mapped `EVENT_NAME` to `security_result.category`.  
\- Mapped `EVENT_NAME` to `security_result.summary`.  
\- Mapped `subject.srcType` to `src.resource.resource_subtype`.  
\- Mapped `subject.srcEvent.event.userIdentity.sessionContext.attributes.creationDate` to `metadata.event_timestamp`.  
\- Mapped `subject.srcEvent.accountcaller` to `principal.resource.product_object_id`.  
\- Mapped `subject.dstEvent.region` to `target.asset.location.name`.  
\- Mapped `subject.dstEvent.accountcaller` to `target.resource.product_object_id`.  
\- Mapped `subject.dstType` to `target.resource.resource_subtype`.  
\- Mapped `subject.dstEvent.service` to `target.url`.  
\- Mapped `subject.dstEvent.username` to `target.user.userid`.   
2024-11-15 |  Enhancement:  
\- Added support to handle JSON logs.  
\- Reduced the GENERIC_EVENT percentage.   
2024-09-25 |  Enhancement:  
\- Added support to handle JSON logs.   
2023-11-09 |  \- Newly created pars   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

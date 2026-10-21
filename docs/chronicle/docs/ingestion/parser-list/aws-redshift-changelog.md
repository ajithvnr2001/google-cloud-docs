---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-redshift-changelog/
title: Change log for AWS_REDSHIFT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:40:28.919939+00:00
---

# Change log for AWS_REDSHIFT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-redshift-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_REDSHIFT

Date | Changes  
---|---  
2025-04-16 |  \- `csv_data`: Added support for `csv` format.  
-`event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `column1` raw field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
-`event.idm.read_only_udm.metadata.timestamp`: Newly mapped `column2` raw field to `event.idm.read_only_udm.metadata.timestamp` UDM field.  
-`event.idm.read_only_udm.principal.ip`: Newly mapped `column3` raw field to `event.idm.read_only_udm.principal.ip` UDM field if valid IP.  
-`event.idm.read_only_udm.principal.asset.ip`: Newly mapped `column3` raw field to `event.idm.read_only_udm.principal.asset.ip` UDM field if valid IP.  
-`event.idm.read_only_udm.principal.principal.hostname`: Newly mapped `column3` raw field to `event.idm.read_only_udm.principal.hostname` UDM field if not valid IP.  
-`event.idm.read_only_udm.principal.port`: Newly mapped `column4` raw field to `event.idm.read_only_udm.principal.port` UDM field if valid HOSTPORT.  
-`event.idm.read_only_udm.principal.process.pid`: Newly mapped `column5` raw field to `event.idm.read_only_udm.principal.process.pid` UDM field.  
-`event.idm.read_only_udm.target.resource.name`: Newly mapped `column6` raw field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- Updated `has_target_resource` to `true` if `column6` is not empty.  
-`event.idm.read_only_udm.target.resource.type`: Newly mapped `event.idm.read_only_udm.target.resource.type` UDM field to `DATABASE`.  
-`event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `column7` raw field to `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `column8` raw field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `column9` raw field to `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
-`event.idm.read_only_udm.network.tls.version`: Newly mapped `column10` raw field to `event.idm.read_only_udm.network.tls.version` UDM field.  
-`event.idm.read_only_udm.network.tls.cipher`: Newly mapped `column11` raw field to `event.idm.read_only_udm.network.tls.cipher` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `column12` raw field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `column13` raw field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `column14` raw field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `column15` raw field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.principal.application`: Newly mapped `column16` raw field to `event.idm.read_only_udm.principal.application` UDM field.  
-`event.idm.read_only_udm.principal.platform_version`: Newly mapped `column17` raw field to `event.idm.read_only_udm.principal.platform_version` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `column18` raw field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `column19` raw field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `column20` raw field to `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
-`event.idm.read_only_udm.network.session_id`: Newly mapped `column21` raw field to `event.idm.read_only_udm.network.session_id` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `column22` raw field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-03-06 |  -event.idm.read_only_udm.principal.process.pid: Newly mapped `pid` to `event.idm.read_only_udm.principal.process.pid` UDM field.  
-event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `time_zone` to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
-event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `sql_query` to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
-event.idm.read_only_udm.target.resource.name: Newly mapped `db` to `event.idm.read_only_udm.target.resource.name` UDM field.  
-event.idm.read_only_udm.target.resource.type: Newly mapped `db` to `event.idm.read_only_udm.target.resource.type` UDM field.  
-event.idm.read_only_udm.target.user.user_display_name: Newly mapped `user` to `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
-event.idm.read_only_udm.principal.user.userid: Newly mapped `user_id` to `event.idm.read_only_udm.principal.user.userid` UDM field.  
-event.idm.read_only_udm.network.session_id: Newly mapped `xid` to `event.idm.read_only_udm.network.session_id` UDM field.  
-event.idm.read_only_udm.metadata.event_type: Newly mapped `metadata.event_type` UDM field to `USER_RESOURCE_ACCESS` if `has_target_resource` and `has_user` is `true`.  
-event.idm.read_only_udm.metadata.event_type: Newly mapped `metadata.event_type` UDM field to `STATUS_UPDATE` if `has_principal` is `true`.  
-event.idm.read_only_udm.metadata.event_type: Newly mapped `metadata.event_type` UDM field to `USER_UNCATEGORIZED` if `has_user` is `true`.  
-event.idm.read_only_udm.metadata.event_type: Newly mapped `metadata.event_type` UDM field to `GENERIC_EVENT` if none of the above conditions are `true`.  
-Modified the `message` field by replacing all occurrences of `\\` with `$`  
-Modified the `message` field by replacing all occurrences of `#` with `,`  
-Added support for parsing a JSON array within the `message` field.  
-Added a grok pattern to parse the `record` field.  
-Added a kv filter to parse key-value pairs from the `kv_data` field.   
2025-02-06 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

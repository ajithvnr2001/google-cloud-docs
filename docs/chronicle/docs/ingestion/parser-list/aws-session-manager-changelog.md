---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-session-manager-changelog/
title: Change log for AWS_SESSION_MANAGER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:51:39.291026+00:00
---

# Change log for AWS_SESSION_MANAGER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-session-manager-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_SESSION_MANAGER

Date | Changes  
---|---  
2025-04-30 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped eventVersion raw log field to event.idm.read_only_udm.metadata.product_version UDM field.  
\- event.idm.read_only_udm.principal.cloud.availability_zone: Newly mapped awsRegion raw log field to event.idm.read_only_udm.principal.cloud.availability_zone UDM field.  
\- event.idm.read_only_udm.target.resource.id: Newly mapped target.id raw log field to event.idm.read_only_udm.target.resource.id UDM field. Set event.idm.read_only_udm.target.resource.type to `instance`.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped userIdentity.arn raw log field to event.idm.read_only_udm.principal.user.product_object_id UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped runAsUser raw log field to event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped sessionId raw log field to event.idm.read_only_udm.network.session_id UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped sessionData array to event.idm.read_only_udm.security_result.detection_fields UDM field, using index as key and the value of the array as value.  
\- JSON: Added support for parsing JSON format logs.  
\- Modified the grok patterns in order to parse the logs with json format, including handling of nested objects (target, userIdentity) and arrays (sessionData).   
2023-06-14 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

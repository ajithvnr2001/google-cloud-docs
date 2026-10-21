---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jenkins-changelog/
title: Change log for JENKINS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:40:57.613738+00:00
---

# Change log for JENKINS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jenkins-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for JENKINS

Date | Changes  
---|---  
2026-08-17 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `receiveTimestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `insertId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `logName` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `resource.labels.location` raw log field with `event.idm.read_only_udm.target.location.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `jobname` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `credential_name`, `credential_type`, `job_class`, `resource.labels.cluster_name` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource_ancestors.name`: Newly mapped `resource.labels.project_id` raw log field with `event.idm.read_only_udm.target.resource_ancestors.name` UDM field.  
\- `event.idm.read_only_udm.target.namespace`: Newly mapped `resource.labels.namespace_name` raw log field with `event.idm.read_only_udm.target.namespace` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `resource.labels.container_name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `textPayload` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `resource.labels.pod_name`, `labels.compute.googleapis.com/resource_name`, `resource.type`, `labels.k8s-pod/app`, `labels.k8s-pod/jenkins-cr` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2024-11-19 |  Enhancement:  
\- Added support to check if `action` is `doUninstall` or `uninstall` then only map `target.resource.attribute.labels`.   
2024-10-25 |  Enhancement:  
\- Added support to parse `datio-pipeline-steps` instead of `plugin/datio-pipeline-steps` and `pipeline-model-declarative-agent` instead of `plugin/pipeline-model-declarative-agent` in `metadata.description`.  
\- Mapped `userid` to `principal.user.userid`.  
\- Mapped `ip` to `principal.ip` and `principal.asset.ip`.   
2024-08-14 |  Enhancement:  
\- Modified a Grok pattern to parse timestamp correctly.   
2024-07-18 |  Enhancement:  
\- Added support to handle unparsed syslog logs.   
2024-06-24 |  Enhancement:  
\- Modified the Grok pattern to accurately parse the `userid`.   
2024-06-15 |  Enhancement:  
\- Mapped `object_id` to `target.resource.attribute.labels`.   
2023-11-27 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

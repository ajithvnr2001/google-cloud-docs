---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-compute-changelog/
title: Change log for GCP_COMPUTE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:02.842397+00:00
---

# Change log for GCP_COMPUTE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-compute-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_COMPUTE

Date | Changes  
---|---  
2026-01-16 |  Enhancement:  
\- Updated conditional logic for mapping `jsonPayload.rule_details.direction` to event.idm.read_only_udm.network.direction. The checks for `INGRESS` and `egress` are now case-insensitive, using regex matching (?i)INGRESS and (?i)egress respectively.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `resource.labels.subnetwork_id`, `jsonPayload.remote_location.continent`, `jsonPayload.rule_details.target_tag`, `jsonPayload.vpc.vpc_name` to `event.idm.read_only_udm.target.resource.attribute.labels.value` UDM field.  
\- event.idm.read_only_udm.target.location.city: Newly mapped `jsonPayload.remote_location.city` raw log field to `event.idm.read_only_udm.target.location.city` UDM field.  
\- event.idm.read_only_udm.target.location.country_or_region: Newly mapped `jsonPayload.remote_location.country` raw log field to `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.target.location.name: Newly mapped `jsonPayload.remote_location.region` raw log field to `event.idm.read_only_udm.target.location.name` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `jsonPayload.rule_details.destination_range`, `jsonPayload.rule_details.ip_port_info` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2024-06-18 |  Enhancement:  
-Mapped `file` to `principal.file.names`.  
-Mapped `function` to `principal.resource.attribute.labels`.  
-Mapped `line` to `principal.resource.attribute.labels`.  
-Mapped `timestamp` to `event_timestamp`.   
2023-02-24 |  Bug - Added mapping for `asset_id` to facilitate search in UI:  
`asset:resource.labels.instance_id` is mapped to `principal.asset_id`  
2022-06-16 |  Enhancement - Added mapping for the following new fields:  
jsonPayload.Message as syslog.  
Process Name to principal.application.  
Process ID to principal.process.pid.  
Account Domain to principal.administrative_domain.  
Account Name to principal.user.user_display_name.  
Object Name to target.resource.name.  
Object Type to target.resource.type.  
Security ID to target.user.windows_sid.  
addr to principal.ip.  
auid to network.session_id.  
Mapped `LINUX - %{type}` for linux logs and `WINDOWS event log` for windows log to metadata.product_event_type.  
pid to target.process.pid.  
acct to target.user.userid.  
exe to target.process.command_line.  
file_path to principal.process.file.full_path.  
Changed mapping of desc from metadata.description to security_result.description.   
2022-05-23 |  Enhancement - Added mapping for the following new fields:  
jsonPayload.message as syslog.  
resource.labels.zone to principal.resource.attribute.cloud.availability_zone.  
resource.labels.location to principal.location.name.  
resource.labels.project_id to metadata.product_deployment_id.  
resource.labels.instance_id to principal.resource.product_object_id.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

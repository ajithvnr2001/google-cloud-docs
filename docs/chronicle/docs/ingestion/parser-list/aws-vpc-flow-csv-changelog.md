---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-vpc-flow-csv-changelog/
title: Change log for AWS_VPC_FLOW_CSV \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:59.292672+00:00
---

# Change log for AWS_VPC_FLOW_CSV  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-vpc-flow-csv-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_VPC_FLOW_CSV

Date | Changes  
---|---  
2026-06-05 |  Enhancement:  
\- This is a legacy parser. Please use AWS_VPC_FLOW prebuilt parser instead.   
2025-05-26 |  Enhancement:  
\- Added a convert block to convert the `column10` from `string` to `float`.   
2025-04-22 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp.seconds: Newly mapped `column11` from the CSV logs with `event.idm.read_only_udm.metadata.event_timestamp.seconds` UDM field.   
2025-03-10 |  Enhancement:  
\- Newly created parser.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `column1` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `column2` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`interface_id`]: Newly mapped `column3` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`interface_id`]` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `column4` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `column4` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `column5` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `column5` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `column6` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `column7` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.additional.fields[`protocol`]: Mapped `column8` raw log field with `event.idm.read_only_udm.additional.fields[`protocol`]` UDM field.  
\- event.idm.read_only_udm.network.ip_protocol: Mapped `column8` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field based on the value.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`packets`]: Newly mapped `column9` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`packets`]` UDM field.  
\- event.idm.read_only_udm.target.file.size: Newly mapped `column10` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.  
\- event.idm.read_only_udm.additional.fields[`start`]: Newly mapped `column11` raw log field with `event.idm.read_only_udm.additional.fields[`start`]` UDM field.  
\- event.idm.read_only_udm.additional.fields[`end`]: Newly mapped `column12` raw log field with `event.idm.read_only_udm.additional.fields[`end`]` UDM field.  
\- event.idm.read_only_udm.security_result.action: Mapped `column13` raw log field with `event.idm.read_only_udm.security_result.action` UDM field based on the value.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`log_status`]: Newly mapped `column14` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`log_status`]` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels[`vpc_id`]: Newly mapped `column15` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels[`vpc_id`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`SubnetID`]: Newly mapped `column16` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`SubnetID`]` UDM field.  
\- event.idm.read_only_udm.resource_ancestors.product_object_id: Newly mapped `column17` raw log field with `event.idm.read_only_udm.resource_ancestors.product_object_id` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`tcp_flags`]: Newly mapped `column18` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`tcp_flags`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`type`]: Newly mapped `column19` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`type`]` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `column20` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.ip: Newly mapped `column20` raw log field with `event.idm.read_only_udm.intermediary.asset.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `column21` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.ip: Newly mapped `column21` raw log field with `event.idm.read_only_udm.intermediary.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `column22` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.principal.cloud.availability_zone: Newly mapped `column23` raw log field with `event.idm.read_only_udm.principal.cloud.availability_zone` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`sublocation_type`]: Newly mapped `column24` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`sublocation_type`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`sublocation_id`]: Newly mapped `column25` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`sublocation_id`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`pkt_src_aws_service`]: Newly mapped `column26` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`pkt_src_aws_service`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`pkt_dst_aws_service`]: Newly mapped `column27` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`pkt_dst_aws_service`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`flow_direction`]: Newly mapped `column28` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`flow_direction`]` UDM field.  
\- event.idm.read_only_udm.network.direction: Newly mapped `column28` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`traffic_path`]: Newly mapped `column29` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`traffic_path`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`ecs_cluster_arn`]: Newly mapped `column30` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`ecs_cluster_arn`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`ecs_cluster_name`]: Newly mapped `column31` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`ecs_cluster_name`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`ecs_container_instance_arn`]: Newly mapped `column32` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`ecs_container_instance_arn`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`ecs_container_instance_id`]: Newly mapped `column33` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`ecs_container_instance_id`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`ecs_container_id`]: Newly mapped `column34` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`ecs_container_id`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`ecs_second_container_id`]: Newly mapped `column35` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`ecs_second_container_id`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`ecs_service_name`]: Newly mapped `column36` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`ecs_service_name`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`ecs_task_definition_arn`]: Newly mapped `column37` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`ecs_task_definition_arn`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`ecs_task_arn`]: Newly mapped `column38` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`ecs_task_arn`]` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels[`ecs_task_id`]: Newly mapped `column39` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels[`ecs_task_id`]` UDM field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

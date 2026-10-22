---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-route-53-changelog/
title: Change log for AWS_ROUTE_53 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:45:43.003515+00:00
---

# Change log for AWS_ROUTE_53  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-route-53-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_ROUTE_53

Date | Changes  
---|---  
2025-04-22 |  Enhancement:  
\- Added null checks for `Query.Hostname` when mapping with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.domain.name` UDM fields.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `activity_id` raw log field and `activity_name` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `category_name` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `category_uid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `metadata.product_feature_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.about.labels: Newly mapped `disposition` raw log field with `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `class_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `class_uid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly mapped `cloud.account.uid` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `cloud.provider` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.location.name: Newly mapped `cloud.region` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `connection_info.direction` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `connection_info.protocol_name` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `metadata.profiles` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `observables.name` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `observables.type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `observables.type_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `observables.value` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `query.class` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.dns.questions.class: Newly mapped `query.class` raw log field with `event.idm.read_only_udm.network.dns.questions.class` UDM field.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Newly mapped `src_endpoint.instance_uid` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Newly mapped `query.hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.network.dns.questions.name: Newly mapped `query.hostname` raw log field with `event.idm.read_only_udm.network.dns.questions.name` UDM field.  
\- event.idm.read_only_udm.principal.resource: Newly mapped `src_endpoint.vpc_uid` raw log field with `event.idm.read_only_udm.principal.resource` UDM field.  
\- event.idm.read_only_udm.principal.resource.resource_type: Newly mapped `VPC_NETWORK` value with `event.idm.read_only_udm.principal.resource.resource_type` UDM field.  
\- event.idm.read_only_udm.principal.ip ,event.idm.read_only_udm.principal.asset.ip: Newly mapped `src_endpoint.ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `src_endpoint.port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `severity_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `type_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `type_uid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.security_result.action, event.idm.read_only_udm.security_result.action_details: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field and `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `metadata.product.name` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- event.idm.read_only_udm.metadata.vendor_name: Newly mapped `metadata.product.vendor_name` raw log field with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `metadata.product.version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.ready_only_udm.security_result.detection_fields: Newly mapped `action_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added a conditional check before mapping `event.idm.read_only_udm.network.application_protocol` to `DNS`.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `rcode` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `source` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `connection_info.direction_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `rcode_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-04-10 |  Enhancement:  
\- `event.idm.read_only_udm.network.dns.questions.name`: Newly mapped `Query.Hostname` raw log field with `event.idm.read_only_udm.network.dns.questions.name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `event.idm.read_only_udm.metadata.event_type` UDM field as `NETWORK_DNS` when `Query.Hostname` raw log field is present.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `event.idm.read_only_udm.network.application_protocol` UDM field as `DNS` when `Query.Hostname` raw log field is present.  
\- Changed the logic of mapping `Query.Hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field and `event.idm.read_only_udm.principal.domain.name` UDM field as per the previous parser version.  
\- `event.idm.read_only_udm.principal.domain.name`: Removed mapping of `Query.Hostname` raw log field from `event.idm.read_only_udm.principal.domain.name` UDM field due to logic change.   
2025-03-13 |  Enhancement:  
\- Mapped `Cloud.Region` to `principal.location.name`.  
\- Mapped `Src_endpoint.Vpc_uid` to `principal.resource.name`.  
\- Mapped `Src_endpoint.Ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `Src_endpoint.Port` to `principal.port`.  
\- Mapped `Query.Hostname` to `principal.hostname` and `principal.domain.name`.  
\- Mapped `Query.Type` to `metadata.product_event_type`.  
\- Mapped `Rcode` to `metadata.description` and `network.dns.response_code`.  
\- Mapped `Connection_info.Protocol_name` to `network.ip_protocol`.  
\- Mapped `Src_endpoint.Instance_uid` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `Dst_endpoint.Instance_uid` and `Dst_endpoint.Interface_uid` to `security_result.rule_labels`.  
\- Mapped `Category_uid`, `Class_uid`, `Class_name`, `Cloud.Provider`, `Metadata.Product.Feature.Name`, `Type_name`, `Type_uid`, `Metadata.Profiles` to `additional.fields`.  
\- Mapped `Category_name` to `security_result.category_details`.  
\- Mapped `Firewall_rule.Uid` to `security_result.rule_id`.  
\- Mapped `Metadata.Product.Name` to `metadata.product_name`.  
\- Mapped `Metadata.Product.Vendor_name` to `metadata.vendor_name`.  
\- Mapped `Severity` to `security_result.severity` after uppercasing.  
\- Mapped `Activity_id` and `Activity_name` to `metadata.product_event_type`.  
\- Mapped `Observables.Array` to `security_result.detection_fields`.   
2025-02-06 |  Enhancement:  
\- Added `gsub` to parse new type of logs.  
\- Added JSON filter to parse new type of logs.   
2025-01-28 |  Enhancement:  
\- Mapped `answers.Class`, `answers.Type`, `query_class` to `additional.fields`.   
2024-10-22 |  Enhancement:  
\- Mapped `answers` field to `network.dns.answers`.   
2024-10-17 |  Enhancement:  
\- Added on_error to all fields before mapping to UDM.   
2023-12-20 |  Bug-Fix:  
\- Added gsub to replace `\\` with `#` to convert SYSLOG into JSON.  
\- Added gsub to replace back `#` with `\\`.   
2023-05-08 |  Enhancement:  
\- Modified Grok pattern for the query DNS logs to support a new log format.  
\- Handle JSON logs containing multiple events.   
2022-08-10 |  Removed extra uppercase mutate blocks.   
2022-07-22 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

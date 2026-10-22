---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sysdig-changelog/
title: Change log for SYSDIG \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:06.476422+00:00
---

# Change log for SYSDIG  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sysdig-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SYSDIG

Date | Changes  
---|---  
2026-05-21 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Updated event_type from `PROCESS_UNCATEGORIZED` to `NETWORK_CONNECTION` if log type is `connection`.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped value from `labels.agent_tag_topology_kubernetes_io_region` with `event.idm.read_only_udm.target.location.name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `labels.agent_tag_topology_kubernetes_io_zone` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-05-04 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.url_back_to_product`: Removed mapping from the `event.idm.read_only_udm.metadata.url_back_to_product` UDM field as the mapping is hardcoded with specific value.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `content.fields.ka.uri.param_command` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `labels.cloudProvider.organization` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.cloud.environment`: Mapped `labels.cloudProvider.name` raw log field with `event.idm.read_only_udm.target.resource.attribute.cloud.environment` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `content.fields.ka.target.subresource` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.   
2026-04-06 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `content.fields.ka.user.name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `content.fields.ka.target.name` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.namespace`: Newly mapped `content.fields.ka.target.namespace` raw log field with `event.idm.read_only_udm.target.namespace` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `content.fields.ka.response.code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `content.fields.ka.auth.decision` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `originator`, `rawEventCategory`, `sourceDetails.sourceType`, `sourceDetails.sourceSubType`, `engine`, `content.falsePositive`, `content.matchedOnDefault`, `labels.kubernetes.configmap.name` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the condition to set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when the principal user details are present.   
2026-03-11 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `filename` raw log field from `event.idm.read_only_udm.additional.fields` as it contains target file name.  
\- `event.idm.read_only_udm.target.file.names`: Mapped `filename` raw log field to `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: When `type` is `fileaccess` AND principal machine data AND target file are present, Set `event.idm.read_only_udm.metadata.event_type` to `FILE_READ`.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `labels.host.id` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.   
2026-02-18 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Updated `event.idm.read_only_udm.metadata.event_type` to `FILE_READ` for logs where `type` is `fileaccess` and `directory` field is not empty.  
\- `event.idm.read_only_udm.target.file.full_path` : Added null conditional check before mapping `directory` raw log field to `event.idm.read_only_udm.target.file.full_path` UDM field.   
2026-02-15 |  Enhancement:  
\- `event.idm.read_only_udm.target.file.full_path`: Removed mapping of `container_image_repo` from `event.idm.read_only_udm.target.file.full_path`. As this is a execution path so this mapping is better suited for `event.idm.read_only_udm.target.process.file.full_path`.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Mapped `container_image_repo` raw log field to `event.idm.read_only_udm.target.process.file.full_path`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `pcomm` from `event.idm.read_only_udm.additional.fields`. We have moved this to relevant UDM field `event.idm.read_only_udm.principal.process.parent_process.file.names`.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.names`: Mapped `pcomm` raw log field to `event.idm.read_only_udm.principal.process.parent_process.file.names`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `comm` from `event.idm.read_only_udm.additional.fields`. We have moved this to relevant UDM field `event.idm.read_only_udm.principal.process.file.names`.  
\- `event.idm.read_only_udm.principal.process.file.names`: Mapped `comm` raw log field to `event.idm.read_only_udm.principal.process.file.names`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `userLoginUid`, `labels.agent.tag.department`, `labels.agent.variant`, `labels.agent.version`, `labels.kubernetes.cluster.distribution`, `count` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- Added string conversion for the `tty` field.  
\- Updated the condition to set `event.idm.read_only_udm.metadata.event_type` to `PROCESS_LAUNCH` to also include cases where `type` is `command`.   
2026-02-13 |  Enhancement:  
-`event.idm.read_only_udm.additional.fields`: Removed mapping of `labels.kubernetes.workload.name` raw log field from `event.idm.read_only_udm.additional.fields` to map it to more specific UDM field.  
-`event.idm.read_only_udm.target.resource_ancestors.name`: Mapped `labels.kubernetes.workload.name` raw log field to `event.idm.read_only_udm.target.resource_ancestors.name` UDM field.  
-`event.idm.read_only_udm.additional.fields`: Removed mapping of `labels.kubernetes.workload.type` raw log field from `event.idm.read_only_udm.additional.fields` to map it to more specific UDM field.  
-`event.idm.read_only_udm.target.resource_ancestors.resource_subtype`: Mapped `labels.kubernetes.workload.type` raw log field to `event.idm.read_only_udm.target.resource_ancestors.resource_subtype` UDM field.  
-`event.idm.read_only_udm.additional.fields`: Removed mapping of `labels.kubernetes.pod.name` and `labels.container.label.io.kubernetes.pod.name` raw log fields from `event.idm.read_only_udm.additional.fields` to map them to more specific UDM fields.  
-`event.idm.read_only_udm.target.resource_ancestors.name`: Mapped `labels.kubernetes.pod.name` and `labels.container.label.io.kubernetes.pod.name` raw log fields to `event.idm.read_only_udm.target.resource_ancestors.name` UDM field and set `event.idm.read_only_udm.target.resource_ancestors.type` as static value `POD`.  
-`event.idm.read_only_udm.additional.fields`: Removed mapping of `labels.container.label.io.kubernetes.container.name` raw log field from `event.idm.read_only_udm.additional.fields` to map it to more specific UDM field.  
-`event.idm.read_only_udm.target.resource_ancestors.name`: Mapped `labels.container.label.io.kubernetes.container.name` raw log field to `event.idm.read_only_udm.target.resource_ancestors.name` UDM field and set `event.idm.read_only_udm.target.resource_ancestors.type` as static value `CONTAINER`.  
-`event.idm.read_only_udm.additional.fields`: Removed mapping of `labels.kubernetes.cluster.name` raw log field from `event.idm.read_only_udm.additional.fields` to map it to more specific UDM field.  
-`event.idm.read_only_udm.target.resource_ancestors.name`: Mapped `labels.kubernetes.cluster.name` and `evnt.labels.kubernetes.cluster.name` raw log field to `event.idm.read_only_udm.target.resource_ancestors.name` UDM field and set `event.idm.read_only_udm.target.resource_ancestors.type` as static value `CLUSTER`.  
-`event.idm.read_only_udm.additional.fields`: Removed mapping of `labels.kubernetes.deployment.name` raw log field from `event.idm.read_only_udm.additional.fields` to map it to more specific UDM field.  
-`event.idm.read_only_udm.target.resource_ancestors.name`: Mapped `labels.kubernetes.deployment.name` raw log field to `event.idm.read_only_udm.target.resource_ancestors.name` UDM field and set `event.idm.read_only_udm.target.resource_ancestors.resource_subtype` as static value `DEPLOYMENT`.  
-`event.idm.read_only_udm.additional.fields`: Removed mapping of `labels.kubernetes.service.name` raw log field from `event.idm.read_only_udm.additional.fields` to map it to more specific UDM field.  
-`event.idm.read_only_udm.target.resource.name`: Mapped `labels.kubernetes.service.name` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field and set `event.idm.read_only_udm.target.resource.type` as static value `SERVICE`.  
-`event.idm.read_only_udm.principal.hostname`: Newly mapped `labels.kubernetes.node.name` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
-`event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `labels.kubernetes.node.name` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
-`event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `labels.kubernetes.cluster.distribution` raw log field with key `kubernetes_cluster_distribution` with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
-`event.idm.read_only_udm.additional.fields`: Newly mapped `tty` raw log field with key `tty_value`,`timestampRFC3339Nano` raw log field with key `timestamp RFC3339 Nano` and `count` raw log field with key `Count` with `event.idm.read_only_udm.additional.fields` UDM field.  
-`event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `userLoginUid` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
-`event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `labels.agent.variant` raw log field with key `agent variant` with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
-`event.idm.read_only_udm.metadata.product_version`: Newly mapped `labels.agent.version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
-`event.idm.read_only_udm.target.resource.attribute.cloud.availability_zone`: Newly mapped `labels.cloudProvider.region` and `record.labels.cloudProvider.region` raw log field with `event.idm.read_only_udm.target.resource.attribute.cloud.availability_zone` UDM field.  
-`event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `labels.host.hostName` raw log field from `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field as this is a duplicate mapping.   
2025-08-07 |  Enhancement:  
\- Refactored the code logic to parse json logs as array of json.  
\- Added a `if` condition check that when `not_in_json` is false then parse the logs as a single log entry.  
\- Added a `if` condition check that when `not_in_json` is true then parse the logs as array of json by converting the logs into array format.  
\- event.idm.read_only_udm.metadata.id: Newly mapped `reference`, `record.reference` raw log fields with event.idm.read_only_udm.metadata.id UDM field.  
\- event.idm.read_only_udm.target.cloud.project.id: Newly mapped `labels.aws.accountId`, `record.labels.aws.accountId` raw log fields with event.idm.read_only_udm.target.cloud.project.id UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.cloud.project.id: Newly mapped `labels.cloudProvider.account.id`, `record.labels.cloudProvider.account.id` raw log fields with event.idm.read_only_udm.target.resource.attribute.cloud.project.id UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.cloud.environment: Newly mapped `labels.cloudProvider.name`, `record.labels.cloudProvider.name` raw log fields with event.idm.read_only_udm.target.resource.attribute.cloud.environment UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `labels.orchestrator.type`, `record.labels.orchestrator.type` raw log fields with event.idm.read_only_udm.target.resource.attribute.labels UDM field.  
\- Added gsub to replace `\\r\\n` with "`, `\\\n` with `` and `}{` with `},{` on `record_json_message".  
\- Modified and placed the drop tag after implementing json filter on `record_json_message`.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `record.content.responseStatusCode` raw log field(s) with event.idm.read_only_udm.network.http.response_code UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `record.content.userOriginIP` raw log field(s) with event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip UDM fields.  
\- event.idm.read_only_udm.target.url: Newly mapped `record.content.requestUri` raw log field(s) with event.idm.read_only_udm.target.url UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `record.content.requestMethod` raw log field(s) with event.idm.read_only_udm.network.http.method UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `record.severity` raw log field(s) with event.idm.read_only_udm.security_result.severity_details UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `record.id` raw log field(s) with event.idm.read_only_udm.metadata.product_log_id UDM field.  
\- event.idm.read_only_udm.metadata.product_deployment_id: Newly mapped `record.agentId` raw log field(s) with event.idm.read_only_udm.metadata.product_deployment_id UDM field.  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped `record.cmdline` raw log field(s) with event.idm.read_only_udm.principal.process.command_line UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `record.type` raw log field(s) with event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Newly mapped `record.hostname` raw log field(s) with event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `record.cwd` raw log field(s) with event.idm.read_only_udm.principal.process.file.full_path UDM field.  
\- event.idm.read_only_udm.target.asset.asset_id: Newly mapped `record.containerId` raw log field(s) with event.idm.read_only_udm.target.asset.asset_id UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `record.pid` raw log field(s) with event.idm.read_only_udm.principal.process.pid UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.pid: Newly mapped `record.ppid` raw log field(s) with event.idm.read_only_udm.principal.process.parent_process.pid UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `record.timestamp` raw log field(s) with event.idm.read_only_udm.metadata.event_timestamp UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `record.timestampRFC3339Nano` raw log field(s) with event.idm.read_only_udm.metadata.collected_timestamp UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `record.uid` raw log field(s) with event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `record.username` raw log field(s) with event.idm.read_only_udm.principal.user.user_display_name UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `record.labels.aws.instanceId` raw log field(s) with event.idm.read_only_udm.target.resource.product_object_id UDM field and set `event.idm.read_only_udm.target.resource_type` to `CLOUD_PROJECT`.  
\- event.idm.read_only_udm.target.cloud.project.id : Newly mapped `record.labels.aws.accountId` raw log field(s) with event.idm.read_only_udm.target.cloud.project.id UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.cloud.availability_zone: Newly mapped `record.labels.aws.region` raw log field(s) with event.idm.read_only_udm.target.resource.attribute.cloud.availability_zone UDM field.  
\- Added a grok pattern on `record.labels.host.hostName` to extract IP Addresses in `src_ip` field and if grok matches then map `src_ip` to `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` else map `record.labels.host.hostName` to `event.idm.read_only_udm.principal.hostname`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `record.labels.agent.tag.env`, `record.labels.agent.tag.role`, `record.labels.agent.tag.stage` raw log field(s) with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `record.comm`, `record.pcomm`, `record.count`, `record.loginShellDistance`, `record.loginShellId`, `record.rxTimestamp`, `record.tty`, `record.originator`, `record.source`, `record.rawEventOriginator`, `record.rawEventCategory`, `record.sourceDetails.sourceType`, `record.sourceDetails.sourceSubType`, `record.engine`, `record.content.entityType` raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.   
2025-06-12 |  Enhancement:  
\- Added a gsub to remove `` from raw logs.  
\- event.idm.read_only_udm.principal.platform: Set `event.idm.read_only_udm.principal.platform` UDM field to `LINUX` if `rawEventOriginator` raw log field is `linuxAgent`.  
\- event.idm.read_only_udm.principal.platform: Set `event.idm.read_only_udm.principal.platform` UDM field to `WINDOWS` if `rawEventOriginator` raw log field is `windowsAgent`.  
\- event.idm.read_only_udm.security_result.severity: Removed mapping of `event.severity` and `severity` raw log fields with `security_result.severity` UDM field when `rawEventCategory` raw log field is `auditTrail`.  
\- event.idm.read_only_udm.security_result.severity: Modified conditions to map `event.severity` raw log field with `security_result.severity` UDM field.  
Set `security_result.severity` UDM field to `HIGH` when `event.severity` is 0, 1, 2 or 3 and unset it from `HIGH` when `event.severity` is 7 or 8.  
Set `security_result.severity` UDM field to `MEDIUM` when `event.severity` is 4, 5 and unset it from `MEDIUM` when `event.severity` is 6.  
Set `security_result.severity` UDM field to `LOW` when `event.severity` is 6 and unset it from `LOW` when `event.severity` is 0, 1, 2 or 3.  
Set `security_result.severity` UDM field to `INFORMATIONAL` when `event.severity` is 7.  
Unset `security_result.severity` UDM field from `CRITICAL` when `event.severity` is 9, 10.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` UDM field to `PROCESS_LAUNCH` if `content.fields.evt.type` raw log field is `execve`, `fork`, `clone`, `setuid`, `CreateProcess`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `rawEventOriginator` raw log field with `event.idm.read_only_udm.additional.fields` UDM field if `rawEventOriginator` raw log field is not `linuxAgent` and `windowsAgent`.  
\- Modified a condition check for `labels.container.image.digest` raw log field before mapping it with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-06-11 |  Enhancement:  
\- Added conditional check for `security_result_severity` to populate field `name` with appropriate severity.   
2025-05-19 |  Enhancement:  
\- event.idm.read_only_udm.metadata.url_back_to_product: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `pod_uid` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.security_result.about.resource.name: Newly mapped `pod` raw log field with `event.idm.read_only_udm.security_result.about.resource.name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `container_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `cluster_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.   
2025-05-02 |  Enhancement:  
\- Removed Gsub which was replacing `content\`:{` to `content_info\`:{`.  
\- Added Gsub to replace `proc.ppid.ts` with `proc.ppid_ts`.  
\- Added Gsub to replace `proc.pid.ts` with `proc.pid_ts`.  
\- Added Gsub to replace `` `` with "".  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.hostname`: Newly mapped `Impactscopedetails.EndpointServers.Ips` raw log field with event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip UDM field if Impactscopedetails.EndpointServers.Ips is ip, else it will be mapped with event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname.   
2025-03-19 |  Enhancement:  
\- Mapped `_time`, `time`, `evnt.timestamp`, `evnt.timestampRFC3339Nano`, `evnt.originator`, `evnt.source`, `evnt.rawEventOriginator`, `evnt.rawEventCategory`, `evnt.sourceDetails.sourceType`, `evnt.sourceDetails.sourceSubType`, `evnt.engine`, `evnt.name`, `evnt.containerId`, `evnt.machineId`, `evnt.content.baselineId`, `evnt.content.ruleType`, `evnt.content.ruleTags`, `evnt.content.output`, `evnt.content.fields`, `evnt.content.falsePositive`, `evnt.content.matchedOnDefault`, `evnt.labels.kubernetes.cluster.name`, `evnt.labels.kubernetes.configmap.name`, `evnt.labels.kubernetes.namespace.name`, `index` and `sourcetype` to `additional.fields`.  
\- Mapped `evnt.description` to `security_result.description`.  
\- Mapped `evnt.id` to `metadata.product_log_id`.  
\- Mapped `evnt.type` to `metadata.product_event_type`.  
\- Mapped `evnt.category` to `security_result.category_details`.  
\- Mapped `evnt.content.policyId` to `security_result.rule_id`.  
\- Mapped `evnt.content.ruleName` to `security_result.rule_name`.  
\- Mapped `evnt.content.policyVersion` to `security_result.rule_labels`.  
\- Mapped `evnt.content.policyOrigin` to `security_result.rule_labels`.  
\- Mapped `evnt.severity` to `security_result.severity`.  
\- Mapped `evnt.id` to `metadata.url_back_to_product`.   
2025-01-16 |  Enhancement:  
\- Mapped `content_entityPayload.items.items`, `content_entityPayload.channels`, `content_entityPayload.connectionInfo.chronicleCustomerId`, `content_entityPayload.connectionInfo.region`, `content_entityPayload.customer.accessKey`, `content_entityPayload.products`, and `content_entityPayload_status` to `additional.fields`.  
\- Mapped `content_entityPayload.firstName` to `principal.user.first_name`.  
\- Mapped `content_entityPayload.lastName` to `principal.user.last_name`.  
\- Mapped `teamrole.teamName` to `principal.group.group_display_name`.  
\- Mapped `teamrole.role` to `principal.user.role_name`.  
\- Mapped `teamrole.userName` to `principal.user.user_display_name`.   
2024-12-20 |  Enhancement:  
\- Mapped `content_entityPayload.details.exceptions`, `content_entityPayload.compression`, `content_entityPayload.reportFormat`, `content_entityPayload.reportType`, `content_entityPayload.filters.conditionFilters.vulnName.value`, and `content_entityPayload.notificationChannels` to `additional.fields`.   
2024-11-07 |  Enhancement:  
\- Mapped `content.queryString`, `content.entityType`, `content_entityPayload.id`, `content_entityPayload.name`, `content_entityPayload.version`, `content_entityPayload.details.priority`, and `content_entityPayload.details.ruleType` to `additional.fields`.  
\- Mapped `content_entityPayload.description` to `security_result.summary`.   
2024-10-01 |  Enhancement:  
\- Added support for new pattern of JSON logs.   
2024-07-08 |  Enhancement:  
\- Added conditional check for MAC address.  
\- Added support to handle JSON logs.   
2024-06-12 |  Enhancement:  
\- Added support to handle unparsed JSON logs.   
2024-01-05 |  \- When `severity` is 0, 1, 2, 3, then changed mapping of `security_result.severity` from `LOW` to `HIGH`.  
\- When `severity` is 6, then changed mapping of `security_result.severity` from `HIGH` to `LOW`.  
\- When `severity` is 7, then changed mapping of `security_result.severity` from `HIGH` to `INFORMATIONAL`.  
\- Added `drop` for logs not in JSON format.  
\- Added `on_error` to `timestampRFC3339Nano` date mapping.   
2022-10-07 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

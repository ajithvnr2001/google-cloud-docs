---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mongo-db-changelog/
title: Change log for MONGO_DB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:42.061017+00:00
---

# Change log for MONGO_DB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mongo-db-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MONGO_DB

Date | Changes  
---|---  
2026-05-12 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Removed static mapping of `event.idm.read_only_udm.principal.user.userid` as `unknown` for event_type `USER_UNCATEGORIZED` to avoid invalid event_type setting.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `service.name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `host.name` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `host.name` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.group.product_object_id`: Newly mapped `mongodb.group.id` raw log field with `event.idm.read_only_udm.principal.group.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `mongodb.cluster.name`, `mongodb.customer.cluster.name` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp`, `ts.date` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `uuid.binary` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `users.1.user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `remote.ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `remote.port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `local.ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `local.port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `roles.role` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `param.args.client.application.name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform`: Newly mapped `param.args.client.os.type` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `param.args.client.os.version` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hardware`: Newly mapped `param.args.client.os.architecture` raw log field with `event.idm.read_only_udm.principal.asset.hardware` UDM field as `cpu_platform`.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `atype`, `param.command` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `param.ns` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `result` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `event.idm.read_only_udm.security_result.summary` UDM field based on the value of `result` raw log field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `mongodb.log.type`, `param.args.db`, `uuid.type`, `param.args.clientOperationKey.type`, `param.args.clientOperationKey.binary`, `param.args.aggregate`, `param.args.mayBypassWriteBlocking`, `param.args.configTime.timestamp.t`, `param.args.topologyTime.timestamp.t`, `param.args.audit`, `param.args.cursor.batchSize.numberLong`, `param.args.includeQueryStatsMetrics`, `param.args.fromMongos`, `param.args.readConcern.provenance`, `param.args.readConcern.level`, `param.args.writeConcern.provenance`, `param.args.writeConcern.level`, `param.args.client.platform`, `param.args.client.driver.name`, `param.args.client.driver.version`, `param.args.client.os.name`, `param.args.clusterTime`, `param.args.lsid.id.type`, `param.args.lsid.uid.binary`, `param.args.users.1.db`, `param.args.client.mongos.version`, `param.args.readConcern.provenance`, `param.args.readConcern.level`, `param.args.writeConcern.w`, `param.args.writeConcern.provenance`, `param.args.writeConcern.wtimeout`, `param.args.lsid.uid.type`, `param.args.pipeline.1.match.managedClusterType`, `param.args.pipeline.2.group.n.sum.const`, `param.args.pipeline.2.group._id.const`, `param.args.topologyTime.timestamp.t`, `param.args.client.mongos.client.port` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `param.args.audit.impersonatedRoles` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `param.args.audit.impersonatedUser` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped extracted IP from `param.args.client.mongos.client` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped extracted IP from `param.args.client.mongos.host` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.port`: Newly mapped extracted port from `param.args.client.mongos.host` raw log field with `event.idm.read_only_udm.intermediary.port` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type: Modified the logic for setting `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when the value of `principal_userid` is not empty or `unknown`.   
2025-03-12 |  Enhancement:  
\- Mapped `accessLog.authResult` to `additional.fields`.  
\- Mapped `accessLog.authSource` to `additional.fields`.  
\- Mapped `accessLog.failureReason` to `additional.fields`.  
\- Mapped `accessLog.groupId` to `target.resource.product_object_id`.  
\- Mapped `accessLog.hostname` to `principal.hostname`.  
\- Mapped `accessLog.ipAddress` to `intermediary.ip`.  
\- Mapped `accessLog.logLine.t.$date` to `additional.fields`.  
\- Mapped `accessLog.logLine.s` to `additional.fields`.  
\- Mapped `accessLog.logLine.c` to `additional.fields`.  
\- Mapped `accessLog.logLine.id` to `additional.fields`.  
\- Mapped `accessLog.logLine.ctx` to `additional.fields`.  
\- Mapped `accessLog.logLine.msg` to `additional.fields`.  
\- Mapped `accessLog.logLine.attr.client` to `additional.fields`.  
\- Mapped `accessLog.logLine.attr.isSpeculative` to `additional.fields`.  
\- Mapped `accessLog.logLine.attr.isClusterMember` to `additional.fields`.  
\- Mapped `accessLog.logLine.attr.mechanism` to `additional.fields`.  
\- Mapped `accessLog.logLine.attr.user` to `additional.fields`.  
\- Mapped `accessLog.logLine.attr.db` to `additional.fields`.  
\- Mapped `accessLog.logLine.attr.result` to `additional.fields`.  
\- Mapped `accessLog.logLine.attr.metrics.conversation_duration.micros` to `additional.fields`.  
\- Mapped `accessLog.logLine.attr.metrics.conversation_duration.summary.step` to `additional.fields`.  
\- Mapped `accessLog.logLine.attr.metrics.conversation_duration.summary.step_total` to `additional.fields`.  
\- Mapped `accessLog.logLine.attr.metrics.conversation_duration.summary.duration_micros` to `additional.fields`.  
\- Mapped `accessLog.username` to `target.user.user_display_name`.  
\- Mapped `accessLog.timestamp` to `additional.fields`.   
2024-04-01 |  Enhancement:  
\- Mapped `roles.db` to `principal.user.attribute.roles`.  
\- When `atype` is `updateUser`, `createUser`, `createRole`, `grantRolesToUser`:  
-Mapped `roles.db` to `target.user.attribute.roles`.   
2024-02-23 |  Enhancement: Supported new format of JSON logs.   
2023-05-26 |  Enhancement: Parsed logs having `atype` value as `dropIndex`, `createIndex`, `clientMetadata`, `logout`.  
When the value of `atype` is `clientMetadata` mapped the following fields:  
\- The field `log.param.clientMetadata.os.type` is mapped to `principal.platform`.  
\- The field `log.param.clientMetadata.os.version` is mapped to `principal.platform_version`.  
\- The field `log.param.clientMetadata.os.name` is mapped to `principal.platform_patch_level`.  
\- The field `log.param.clientMetadata.os.architecture` is mapped to `principal.asset.hardware[n].cpu_platform`.  
\- The field `log.param.clientMetadata.driver.name` is mapped to `principal.asset.software[n].name`.  
\- The field `log.param.clientMetadata.driver.version` is mapped to `principal.asset.software[n].version`.  
\- `metadata.event_type` is set to `STATUS_UPDATE`.  
When the value of `atype` is `logout` mapped the following fields:  
\- The field `log.param.reason` is mapped to `security_result.description`.  
\- The field `log.param.initialUsers[0].db` is mapped to `target.resource.name` and `target.administrative_domain`.  
\- The field `log.param.initialUsers[0].user` is mapped to `target.user.userid`.  
\- The field `log.param.initialUsers[1..n].user` is mapped to `about.user.userid`.  
\- `metadata.event_type` is set to `USER_LOGOUT`.  
When the value of `atype` is `createIndex` mapped the following fields:  
\- The field `log.param.ns` is mapped to `target.resource.name`.  
\- The field `log.param.indexBuildState` is mapped to `security_result.description`.  
\- The field `log.param.indexName` is mapped to `target.resource.attribute.labels`.  
\- `metadata.event_type` is set to `RESOURCE_CREATION`.  
When the value of `atype` is `dropIndex` mapped the following fields:  
\- The field `log.param.ns` is mapped to `target.resource.name`.  
\- The field `log.param.indexBuildState` is mapped to `security_result.description`.  
\- The field `log.param.indexName` is mapped to `target.resource.attribute.labels`.  
\- `metadata.event_type` is set to `RESOURCE_DELETION`.   
2022-09-15 |  Enhancement - Migrated to default parser.   
2022-06-28 |  Enhancement: Parsed logs having `category` value as `NETWORK`, `STORAGE`, `ACCESS`, `COMMAND`, `CONNPOOL`, `SHARDING`, `REPL`.  
\- The field `log.t.$date` mapped to `metadata.event_timestamp`.  
\- The field `log.c` mapped to `metadata.product_event_type`.  
\- The field `log.attr.remote` mapped to `principal.ip` and `principal.port` accordingly.  
\- The field `log.attr.doc.application.name` mapped to `target.application`.  
\- The field `log.s` mapped to `security_result.severity`.  
\- The field `log.attr.connectionId` mapped to `additional.fields[n]`.  
\- The field `log.attr.connectionCount` mapped to `additional.fields[n]`.  
\- The field `log.ctx` mapped to `additional.fields`.  
\- The field `log.msg` mapped to `metadata.description`.  
\- The field `log.id` mapped to `metadata.product_log_id`.  
\- When the value of `log.c` is `NETWORK` mapped following fields:  
\- The field `log.attr.doc.os.type` mapped to `principal.platform`.  
\- The field `log.attr.doc.os.version` mapped to `principal.platform_version`.  
\- The field `log.attr.doc.os.name` mapped to `principal.platform_patch_level`.  
\- The field `log.attr.doc.os.architecture` mapped to `principal.asset.hardware[n].cpu_platform`.  
\- The field `log.attr.doc.driver.name` mapped to `principal.asset.software[n].name`.  
\- The field `log.attr.doc.driver.version` mapped to `principal.asset.software[n].version`.  
\- When the value of `log.c` is `STORAGE` mapped following fields:  
\- The field `log.attr.message` to `security_result.summary`.  
\- When the value of `log.c` is `ACCESS` mapped following fields:  
\- The field `log.attr.authenticationDatabase` to `target.resource.name`.  
\- The field `log.attr.error` to `security_result.summary`.  
\- The field `log.attr.principalName` to `target.user.userid`.  
\- The field `log.attr.mechanism` to `extensions.auth.auth_details`.  
\- When the value of `log.c` is `COMMAND` mapped following fields:  
\- The field `log.attr.ns` to `principal.namespace`.  
\- The field `log.attr.command.$db` to `target.resource.name`.  
\- The field `log.attr.planSummary` to `security_result.summary`.  
\- The field `log.attr.command.$readPreference.mode` to `target.resource.attribute.labels[n]`.  
\- The field `log.attr.queryHash` to `target.resource.attribute.labels[n]`.  
\- The field `log.attr.storage.data.bytesRead` to `target.resource.attribute.labels[n]`.  
\- The field `log.attr.storage.data.timeReadingMicros` to `target.resource.attribute.labels[n]`.  
\- The field `log.attr.protocol` to `target.resource.attribute.labels[n]`.  
\- When the value of `log.c` is `CONNPOOL` mapped following fields:  
\- The field `log.attr.hostAndPort` to `principal.hostname` and `principal.port` accordingly.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

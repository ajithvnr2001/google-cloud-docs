---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/observeit-changelog/
title: Change log for OBSERVEIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:21:20.340872+00:00
---

# Change log for OBSERVEIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/observeit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OBSERVEIT

Date | Changes  
---|---  
2025-10-31 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Event.endpoint.id`,`Event.activity.trigger`, `Event.activity.categories`, `Event.activity.signals`, `Event.activity.clumps.primary.item.designations`, `Event.activity.clumps.primary.id`, `Event.rver`, `Event.session.id`, `Event.annotations.workflow.state.disposition.status.id`, `Event.annotations.workflow.state.status`, `Event.ui.layout.h`, `Event.ui.layout.id`, `Event.ui.layout.w`, `Event.ui.layout.displays`, `Event.activity.primaryCategory`, `Event.context`, `Event.Event.occurredAt`, `Event.Event.observedAt`, `Event.Event.timezone.offset`, `Event.Event.kind`, `Event.Event.clock.offset`, `Event.Event.expiresAt`, `Event.Event.observed.offline`, `Event.Event.sequence.id`, `Event.agent.pid`, `Event.agent.kind`, `Event.endpoint.os.name`, `Event.endpoint.os.multiuser`, `Event.endpoint.os.version`, `Event.endpoint.os.kind`, `Event.endpoint.alias`, `Event.endpoint.location.geo.coordinates.lat`, `Event.endpoint.location.geo.coordinates.lon`, `Event.endpoint.location.geo.address.area1.code`, `Event.endpoint.location.geo.address.country.name`, `Event.endpoint.location.geo.address.area2.code`, `Event._sys.processing.catalog.identity.enabled`, `Event.Event.trace.context.transactionId`, `Event.Event.trace.context.correlationId`, `Event.Event.inspectedAt`, `Event.Event.ingestedAt`, `Event.Event.id`, `Event.Event.time.utc.secondOfDay`, `Event.Event.time.local.date`, `Event.Event.time.local.sec`, `Event.Event.time.local.min`, `Event.Event.time.local.dayOfWeek`, `Event.Event.time.local.month`, `Event.Event.time.local.hour`, `Event.Event.time.local.year`, `Event.Event.time.local.dayOfYear`, `Event.Event.time.local.day`, `Event.retention`, `Event.process.uid`, `Event.process.egid`, `Event.process.gid`, `Event.process.isRoot`, `Event.process.euid`, `Event.process.application.description`, `Event.process.application.vendor`, `Event.process.executable.name`, `Event.process.sid`, `Event.sver`, `Event.resources`, `Event.indicators`, `Event.contextId`, `Event.processing.actions`, `Event._sys.processing.actions`, `Event.organization.tenant.pfpt.oit.id`, `Event.organization.tenant.kind`, `Event.organization.tenant.id`, `Event.organization.customer.name`, `Event.organization.customer.alias`, `Event.organization.customer.id`, `Event.organization.customer.details.verticals`, `Event.organization.instances`, `Event._sys.processing.rule.artifacts`, `Event._sys.processing.modules`, `Event._sys.processing.rule.notification`, `Event.incident.severity`, `Event.incident.kind`, `Event.incident.name`, `Event.incident.description`, `Event.incident.id`, `Event.incident.status`, `Event.incident.reasons`, `Event.user.groups`, `Event.user.directory.manager.catalog.id`, `Event.user.directory.manager.email`, `Event.user.directory.ou`, `Event.user.directory.company.name`, `Event.user.directory.department.name`, `Event.user.directory.attributes`, `Event.user.intelligence.risk.overall.level`, `Event.user.intelligence.risk.overall.score`, `Event.user.intelligence.risk.threat.level`, `Event.user.intelligence.risk.threat.score`, `Event.user.intelligence.risk.data.level`, `Event.user.intelligence.risk.data.score`, `Event.user.intelligence.risk.awareness.level`, `Event.user.intelligence.risk.awareness.score`, `Event.user.uid`, `Event.user.netbiosDomain`, `Event.user.intelligence.assessments`, `Event.entity.name`, `Event.entity.suite`, `Event.entity.provider`, `Event.entity.kind`, `Event.entity.vendor`, `Event.user.gid`, `Event.user.aliases`, `Event.user.catalog.id`, `Event.user.catalog.iver`, `Event.user.identifiers`, `Event.site.path`, `Event.site.categorization.match.url.stem`, `Event.site.categorization.details.matchedurl`, `Event.site.categorization.details.categories`, `Event.site.categorization.details.status`, `Event.site.categorization.categories`, `Event.site.reputation.level`, `Event.site.reputation.score`, `Event.site.reputation.details.threatHistory`, `Event.site.reputation.details.country`, `Event.site.reputation.details.matchedurl`, `Event.site.reputation.details.popularity`, `Event.site.reputation.details.age`, `Event.site.reputation.details.url`, `Event.site.reputation.details.status`, `Event.createdBy.principal.id`, `Event.intelligence.findings`, `Event.tags`, `Event.feed.product`, `Event.feed.instance`, `Event.feed.data.realm.id`, `Event.feed.data.source.kind`, `Event.feed.kind`, `Event.feed.vendor`, `Event.feed.channel`, `Event.feed.realm`, `Event.feed.connection.source.geo.coordinates.lat`, `Event.feed.connection.source.geo.coordinates.lon`, `Event.feed.connection.source.geo.address.area1.code`, `Event.feed.connection.source.geo.address.country.name`, `Event.feed.connection.source.geo.address.country.code`, `Event.feed.connection.source.geo.address.area2.code`, `Event.feed.connection.source.ip`, `Event.feed.details.tenant.alias`, `Event.feed.id`, `Event.feed.region`, `Event.feed.tenant`, `Event.components.version`, `Event.activity.policies` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Event.fqid` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `Event.agent.version` raw log field to `event.idm.read_only_udm.metadata.product_version`.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `Event.endpoint.fqdn` raw log field to `event.idm.read_only_udm.target.administrative_domain`.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `Event.endpoint.location.geo.address.country.code` raw log field to `event.idm.read_only_udm.target.location.country_or_region`.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `Event.site.host` raw log field to `event.idm.read_only_udm.target.hostname`.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `Event.site.host` raw log field to `event.idm.read_only_udm.target.asset.hostname`.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `Event.site.port` raw log field to `event.idm.read_only_udm.target.port`.  
\- `event.idm.read_only_udm.target.process.product_specific_process_id`: Newly mapped `Event.process.id` raw log field to `event.idm.read_only_udm.target.process.product_specific_process_id`.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `Event.process.executable.path` raw log field to `event.idm.read_only_udm.target.file.full_path`.  
\- `event.idm.read_only_udm.target.process.parent_process.pid`: Newly mapped `Event.process.ppid` raw log field to `event.idm.read_only_udm.target.process.parent_process.pid`.  
\- `event.idm.read_only_udm.metadata.url_back_to_product`: Newly mapped `Event.esUrl` raw log field to `event.idm.read_only_udm.metadata.url_back_to_product`.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `Event.sessionId` raw log field to `event.idm.read_only_udm.network.session_id`.  
\- `event.idm.read_only_udm.target.nat_ip`: Newly mapped `Event.endpoint.location.ip` raw log field to `event.idm.read_only_udm.target.nat_ip`.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `Event.user.directory.domain` raw log field to `event.idm.read_only_udm.principal.administrative_domain`.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `Event.user.id` raw log field to `event.idm.read_only_udm.principal.user.product_object_id`.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `Event.user.email` raw log field to `event.idm.read_only_udm.principal.user.email_addresses`.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `Event.user.fullname` raw log field to `event.idm.read_only_udm.principal.user.user_display_name`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `Event.user.name` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- `event.idm.read_only_udm.principal.user.title`: Newly mapped `Event.user.directory.title` raw log field to `event.idm.read_only_udm.principal.user.title`.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `Event.endpoint.hostname` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `Event.endpoint.net.interfaces.ip` raw log field to `event.idm.read_only_udm.target.ip`.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `Event.endpoint.net.interfaces.ip` raw log field to `event.idm.read_only_udm.target.asset.ip`.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `Event.process.pid` raw log field to `event.idm.read_only_udm.target.process.pid`.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `Event.process.application.name` raw log field to `event.idm.read_only_udm.principal.application`.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `Event.site.url` raw log field to `event.idm.read_only_udm.target.url`.  
\- `event.idm.read_only_udm.network.dns.answers`: Newly mapped `Event.ttl` raw log field to `event.idm.read_only_udm.network.dns.answers`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `Event.components.id` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `Event.components.kind` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels`.   
2025-07-17 |  Enhancement:  
\- Added a grok pattern to parse the raw log.  
\- Modified gsub on `kv_data` to replace `([a-zA-Z0-9_-]+)=` with `#$1=`  
\- Added a gsub to replace `type` with `Type` , `, ` with ` ` ,  
\- event.idm.read_only_udm.principal.process.file.sha256: Newly mapped `sha256` raw log field to `event.idm.read_only_udm.principal.process.file.sha256`  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `id` raw log field to `event.idm.read_only_udm.target.resource.product_object_id`.  
\- event.idm.read_only_udm.principal.process.file.size: Newly mapped `size` raw log field to `event.idm.read_only_udm.principal.process.file.size`.  
\- event.idm.read_only_udm.principal.file.file_type: Newly mapped `Type` raw log field to `event.idm.read_only_udm.principal.file.file_type`.  
\- event.idm.read_only_udm.security_result.priority_details: Newly mapped `pri` raw log field to `event.idm.read_only_udm.security_result.priority_details`.  
\- Added a grok pattern to extract `tar_host` and `tar_ip` from "relay raw log field.  
\- event.idm.read_only_udm.target.hostname,event.idm.read_only_udm.target.asset.hostname: Newly mapped `tar_host` raw log field to `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname`.  
\- event.idm.read_only_udm.target.ip,event.idm.read_only_udm.target.asset.ip: Newly mapped `tar_ip` raw log field to event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip".  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `stat` raw log field to `event.idm.read_only_udm.security_result.summary`.  
\- Modified already existing mapping of `proto` to map `event.idm.read_only_udm.network.application_protocol` correctly.  
\- Added a regex conditional check before already existing of `to`, `from`,`rcpt`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `corrupted`, `protected`, `duration`, `mailer`, `tls_verify`, and `dsn` raw log fields to event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `m`, `omime`, `oext`, `lang`, `url_count`, `virtual`, `a`, `delay`, and `xdelay` raw log fields to event.idm.read_only_udm.additional.fields.   
2024-12-13 |  Enhancement:  
\- Mapped `_derivatives.direction.source.name` to `target.resource.attribute.labels`.   
2024-12-09 |  Enhancement:  
-Changed mapping of `reason.name` from `security_result.detection_fields` to `security_result.description`.   
2024-11-21 |  Enhancement:  
Mapped `resource.target` to `target.resource.attribute.labels`.  
\- Mapped`resource.classification.labels` to `security_result.detection_fields`  
\- Mapped `partitionKey` to `security_result.detection_fields`  
\- Mapped `fqid` to `security_result.detection_fields`  
\- Mapped `context.contextId` to `principal.labels`  
\- Mapped `context.partitionKey` to `principal.labels`  
\- Mapped `entity` to `security_result.detection_fields`  
\- Mapped `feed.instance` to `principal.asset.product_object_id`  
\- Mapped `incident.reasons` to `security_result.detection_fields`  
\- Mapped `recipient.id` to `target.user.userid`  
\- Mapped `recipient.kind` to `target.user.role_description`  
\- Mapped `recipient.email` to `target.user.email_addresses`  
\- Mapped `esUrl` to `metadata.url_back_to_product`  
\- Mapped `policyRoutes` to `security_result.detection_fields`  
\- Mapped `organization.tenant` to `security_result.detection_fields`  
2024-10-17 |  Enhancement:  
\- Modified the mapping of `additional.fields` for `value.verticals.key`.  
\- Mapped `remote.host.ip.address` to `principal.ip`.   
2023-12-15 |  Enhancement:  
\- Added support for CEF format logs.   
2023-11-03 |  Enhancement:  
\- Mapped the fields in `processing.actions` to `security_result.detection_fields`.  
\- Mapped the fields in `organization.customer` to `additional fields`.  
\- Mapped the fields in `organization.instances` to `target.resource.attribute.labels`.  
\- Mapped the fields in `_sys.processing.modules` to `target.resource.attribute.labels`.  
\- Mapped the fields in `_sys.processing.rule.artifacts` to `target.resource.attribute.labels`.  
\- Mapped the fields in `event` to `additional fields`.  
\- Mapped the fields in `activity` to `additional fields`.  
\- Mapped the fields in `endpoint.os` to `additional fields`.  
\- Mapped the fields in `ui.windows.os` to `target.resource.attribute.labels`.  
\- Mapped the `_sys.operation` to `additional fields`.  
\- Mapped `ttl` to `network.dns.answer`.  
\- Mapped `site.url` to `target.url`.  
\- Mapped `site.port` to `target.port`.  
\- Mapped `site.host` to `target.hostname`.  
\- Mapped `site.scheme` to `network.application_protocol`.  
\- Mapped the fields in `site.resource` to `target.resource.attribute.labels`.  
\- Mapped `activity.primaryCategory` to `metadata.product_event_type`.   
2023-07-28 |  Enhancement:  
\- Mapped `feed.region` to `principal.asset.location.country_or_region` from `entity.asset.location.country_or_region`.  
\- Mapped `feed.connection.source.ip` to `principal.asset.ip` from `entity.asset.ip`.  
\- Mapped `feed.id` to `principal.asset.asset_id` from `entity.asset.hostname`.  
\- Mapped `feed.instance` to `principal.asset.product_object_id` from `entity.asset.product_object_id`.  
\- Mapped `principal.asset.category` to `WORKSTATION` when `feed.realm` contains `WORKSTATION`.  
\- Mapped `principal.asset.type` to `WORKSTATION` when `feed.realm` contains `WORKSTATION`.   
2023-07-21 |  Enhancement:  
\- Modified the logic to fetch the file related information from the JSON array instead of always fetching from the first element of the array.   
2023-05-08 |  Bug-fix:  
\- Mapped `observedAt` to `metadata.event_timestamp`.   
2023-01-21 |  Enhancement:  
\- Mapped `session.id` to `network.session_id`.  
\- Mapped `endpoint.location.geo.coordinates.lon.double` to `target.location.region_longitude`.  
\- Mapped `endpoint.location.geo.coordinates.lat.double` to `target.location.region_latitude`.  
\- Mapped `agent.version` to `metadata.product_version`.  
\- Mapped `agent.kind` to `additional.fields`.  
\- Mapped `context.createdAt` to `metadata.collected_timestamp`.  
\- Mapped `context.sortKey` to `security_result.detection_fields`.  
\- Mapped `user.name` to `principal.user.userid`.  
\- Mapped `resources.0.size.int` to `principal.process.file.size`.  
\- Mapped `host` to `principal.hostname`.  
\- Added conditional check for `time`, `proc`, `device`, and `pid`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

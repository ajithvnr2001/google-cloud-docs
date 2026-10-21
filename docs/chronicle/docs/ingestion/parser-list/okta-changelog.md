---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/okta-changelog/
title: Change log for OKTA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:24:50.535189+00:00
---

# Change log for OKTA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/okta-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OKTA

Date | Changes  
---|---  
2026-09-18 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Removed mapping of `user_email` from `event.idm.read_only_udm.principal.user.email_addresses` UDM field for `system.email.challenge_factor_redeemed` event as it is a email related to network event.  
\- `event.idm.read_only_udm.network.email.from`: Mapped `user_email` raw log field with `event.idm.read_only_udm.network.email.from` UDM field for `system.email.challenge_factor_redeemed` event.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `Anomalous Device` from `event.idm.read_only_udm.security_result.detection_fields` UDM field as it is part of value of reasons.   
2026-07-22 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Set the `event.idm.read_only_udm.metadata.event_type` to `GROUP_UNCATEGORIZED` when `eventType` is `app.office365.api.error.get.object.ids.by.group.id`.   
2026-05-28 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `deviceKey` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field when target does not have `ud_device` details.   
2026-04-02 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Removed mapping of `user_email` from `event.idm.read_only_udm.principal.user.email_addresses` UDM field when `eventType` is `system.email.delivery` or `system.email.account_unlock.sent_message`.  
\- `event.idm.read_only_udm.network.email.from`: Mapped `user_email` raw log field with `event.idm.read_-only_udm.network.email.from` UDM field when `eventType` is `system.email.delivery` or `system.email.account_unlock.sent_message`.   
2026-01-09 |  Enhancement:  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `debugContext.debugData.zoneData.cidr_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `debugContext.debugData.zoneData.cidr_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `debugContext.debugData.zoneData.range`, `debugContext.debugData.zoneData.CIDR` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_type`: For RESOURCE_* events when resource_type is not present then mapped `event.idm.read_only_udm.target.resource.resource_type` with `UNSPECIFIED`.  
\- Changed mapping of `event.idm.read_only_udm.target.resource.type` to `event.idm.read_only_udm.target.resource.resource_type` for all the events as `event.idm.read_only_udm.target.resource.type` is deprecated.   
2025-10-14 |  Enhancement:  
\- Changed the severity level for `severity1` log field from `ERROR` to `HIGH` when `severity1` is `ERROR`.   
2025-08-19 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta .  
\- Support for Okta Scaleft logs has been moved from OKTA parser to OKTA_SCALEFT parser.   
2025-08-14 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `level`, `detectionName`, `issuer`, and `previousLevel` from the `debugContext.debugData.risk` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `reason` from the `debugContext.debugData.risk` raw log field to `event.idm.read_only_udm.security_result.detection_fields` if `no_reason` is `true`.  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Newly mapped `request.ipChain.0.version` raw log field to `event.idm.read_only_udm.principal.asset.attribute.labels`.   
2025-06-17 |  Enhancement:  
\- event.idm.read_only_udm.security_result.action: Newly added `Action1` field when `outcome.result` raw log field is `UNANSWERED` and `ABANDONED` with `QUARANTINE` to `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `version` field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `debugContext.debugData.authenticatorMethodChallengeTime` field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `debugContext.debugData.requestId` and `debugContext.debugData.targetEventHookIds` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-06-12 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `details.type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `details.actor.name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `details.actor.details.full_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.user.first_name: Newly mapped `details.actor.details.first_name` raw log field with `event.idm.read_only_udm.principal.user.first_name` UDM field.  
\- event.idm.read_only_udm.principal.user.last_name: Newly mapped `details.actor.details.last_name` raw log field with `event.idm.read_only_udm.principal.user.last_name` UDM field.  
\- event.idm.read_only_udm.principal.user.employee_id: Newly mapped `details.actor.id` raw log field with `event.idm.read_only_udm.principal.user.employee_id` UDM field.  
\- event.idm.read_only_udm.principal.user.department: `details.actor.team_name` raw log field now merged with `event.idm.read_only_udm.principal.user.department` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `details.client.hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `details.client.hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `details.client.id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `details.client.description` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.platform: Newly mapped `details.client.os` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped `details.client.os` version raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: `details.actor.details.email` raw log field now merged with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.target.resource.id: Newly mapped `details.team_id` raw log field with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `details.team_id` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `details.team_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `details.client.state` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `details.target_server` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `details.via` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `details_session_type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.roles: Newly mapped `details.actor.details.user_type` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `details.trace_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Newly mapped `details.client.encrypted` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `details.client.user_name` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `details.client_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `details.client_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.resource.id: Newly mapped `details.project.id` raw log field with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `details.project.team` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `details.project.create_server_users`, `details.project.force_shared_ssh_users`, `details.project.forward_traffic`, `details.project.rdp_session_recording`, `details.project.require_preauth_for_creds`, `details.project.ssh_certificate_type`, and `details.project.ssh_session_recording` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `details.project.next_unix_gid` and `details.project.next_unix_uid` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `details.server_hostnames` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `details.server_hostnames` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.intermediary.resource.attribute.labels: Newly mapped `server_cloud_provider`, `server_instance_type`, `server_instance_id`, `server_network`, `server_project_id`, `server_zone_id`, `detailsserver_os`, `server_services`, `server_sftd_version`, `server_source`,`details.servers.id`, `details.servers.cloud_provider`,`details.servers.instance_details._type` , `details.servers.instance_details.instance_id`, `details.servers.instance_details.internal_ip`, `details.servers.instance_details.network`, `details.servers.instance_details.project_id`, `details.servers.instance_id`, `details.servers.os`, `details.servers.source`, `details.servers.project_name`, `details.servers.source_details.cloud_account`, `details.servers.source_details.cloud_provider`, `details.servers.source_details.instance_id`, `details.server.id`, `details.server.cloud_provider`,`details.server.instance_details._type` , `details.server.instance_details.instance_id`, `details.server.instance_details.internal_ip`, `details.server.instance_details.network`, `details.server.instance_details.project_id`, `details.server.instance_id`, `details.server.os`, `details.server.source`, `details.server.project_name`, `details.server.source_details.cloud_account`, `details.server.source_details.cloud_provider`, `details.server.source_details.instance_id` and `server_source_details` raw log fields with `event.idm.read_only_udm.intermediary.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.intermediary.user.department: Newly mapped `detailsserver.team_name` raw log field with `event.idm.read_only_udm.intermediary.user.department` UDM field.  
\- event.idm.read_only_udm.target.user.user_display_name: Newly mapped `details.username` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `details.ssh_key_fingerprint` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `details.unix_user_name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped `details.ssh_algorithm` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `details.servers.alt_names` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `details.servers.alt_names` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `details.server.alt_names` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `details.server.alt_names` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `details.servers.access_address` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `details.server.access_address` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `details.servers.external_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `details.server.external_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `details.server.sftd_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `details.servers.sftd_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.intermediary.location.country_or_region: Newly mapped `details.server.instance_details.zone_id` raw log field with `event.idm.read_only_udm.intermediary.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.intermediary.location.country_or_region: Newly mapped `details.servers.instance_details.zone_id` raw log field with `event.idm.read_only_udm.intermediary.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` if both principal user and target user are present.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` if only principal user is present.   
2025-02-25 |  Enhancement:  
\- Mapped `debugContext.debugData.authType` and `debugContext.debugData.factorType` to `additional.fields`.   
2025-02-06 |  Enhancement:  
\- Mapped `risk.level` to `security_result.severity_details`.  
\- Mapped `risk.reasons` to `security_result.description`.   
2025-02-05 |  Enhancement:  
\- Mapped `actor.displayName` and `target.displayName` to `additional.fields`  
2025-01-16 |  Enhancement:  
\- Mapped `anonymous`, `operator`, and `type` to `security_result.detection_fields`.   
2025-01-08 |  Enhancement:  
\- Mapped `tunnels` and `policyRuleFactorMode` to `security_result.detection_fields`.   
2025-01-02 |  Enhancement:  
\- Mapped `authnRequestId`, `traceId`, `debugContext.debugData.tunnels` to additional fields.   
2024-11-14 |  Enhancement:  
\- Added support for a new format of JSON logs.   
2024-09-20 |  Enhancement:  
\- Added a Grok pattern to extract `userid` from `profile.login` and mapped it to `principal.user.userid`.  
\- Mapped `profile.displayName` to `principal.user.user_display_name`.  
\- Mapped `profile.email` to `principal.user.email_addresses`.   
2024-09-12 |  Enhancement:  
\- Added `gsub` to parse the unparsed logs.   
2024-07-23 |  Enhancement:  
\- Removed mapping of `actor.displayname` from `principal.application`.  
\- Added conditional check before setting event_type to `USER_DELETION`.   
2024-06-26 |  Enhancement:  
\- Added support to parse unparsed logs.  
\- Mapped the `securityContext.isProxy` field to `additional.fields`.   
2024-05-16 |  Enhancement:  
If `is_alert` is `true` and `is_significant` is `true`, then set `security_result.alert_state` as `ALERTING`.   
2024-03-05 |  Enhancement:  
\- Updated `security_result.action` field to reflect whether the traffic was allowed or blocked.   
2024-02-16 |  Bug-Fix:  
\- When `target.0.type` is `User` or `AppUser`, then mapped `target.0.alternateId` to `target.user.userid`.  
\- When `target.1.type` is `User` or `AppUser`, then mapped `target.1.alternateId` to `target.user.userid`.   
2023-12-14 |  Enhancement:  
\- Mapped `securityContext.asNumber` to `security_result.detection_fields`.  
\- Mapped `legacyEventType` to `security_result.detection_fields`.  
\- Added `conditional_check` before setting `metadata.event_type`.   
2023-06-28 |  Enhancement:  
\- Mapped complete value of `debugContext.debugData.suspiciousActivityEventType` to `security_result.detection_fields`.  
\- Mapped complete value of `debugContext.debugData.logOnlySecurityData.behaviors.New Device` to `security_result.detection_fields`.   
2023-06-09 |  Enhancement:  
\- The field `debugContext.debugData.deviceFingerprint` is mapped to `target.asset.asset_id`.  
\- Mapped complete value of `debugContext.debugData.risk.reasons` to `security_result.detection_fields`.   
2023-05-17 |  \- The field `authenticationContext.externalSessionId` is mapped to `network.parent_session_id`.  
\- The field `debugContext.debugData.pushOnlyResponseType` is mapped to `security_result.detection_fields.key/value`.  
\- The field `debugContext.debugData.factor` is mapped to `security_result.detection_fields.key/value`.  
\- The field `debugContext.debugData.factorIntent` is mapped to `security_result.detection_fields.key/value`.  
\- The field `debugContext.debugData.pushWithNumberChallengeResponseType` is mapped to `security_result.detection_fields.key/value`.  
\- The field `debugContext.debugData.dtHash` is mapped to `security_result.detection_fields.key/value`.  
\- The field `client.userAgent.rawUserAgent` is mapped to `network.http.user_agent`.  
\- Changed the mapping from `ALLOW_WITH_MODIFICATION` to enum value `CHALLENGE` under `security_result.action`.  
\- For the eventType `system.api_token.create`, changed metadata.event_type from `USER_UNCATEGORIZED` to `RESOURCE_CREATION`.   
2023-04-28 |  Bug-Fix:  
\- Modified mapping for `security_result.threat_status` to `ACTIVE` when `debugContext.debugData.threatSuspected` is `true` else mapped to `FALSE_POSITIVE`.   
2023-04-11 |  Enhancement:  
\- Remapped the fields which are mapped to `http.user_agent` to `http.parsed_user_agent`.  
\- Mapped `target.displayName` to `target.resource_ancestors.name`.  
\- Mapped `targetfield.detailEntry.methodTypeUsed` to `target.resource_ancestors.attribute.labels`.  
\- Mapped `targetfield.detailEntry.methodUsedVerifiedProperties` to `target.resource_ancestors.attribute.labels`.   
2023-03-24 |  Enhancement:  
\- Mapped `logOnlySecurityData` fields to `security_result.detection_fields`.  
\- Additionally, resolved parsing error by adding `DEFERRED` to action list.   
2023-02-20 |  Enhancement:  
\- Changed `metadata.event_type` from `USER_LOGIN` to `STATUS_UPDATE` where `eventType` is `user.authentication.auth_via_AD_agent`  
2022-12-14 |  Enhancement:  
\- Mapped `debugContext.debugData.changedAttributes` to `security_result.detection_fields`.  
\- Added null check for `detail.actor.alternateId`.   
2022-11-17 |  Enhancement:  
\- The field `target[n].alternateId` is mapped to `target.resource.attribute.labels`.  
\- The field `detail.target.0.alternateId` is mapped to `target.resource.attribute.labels`.   
2022-11-08 |  Bug-fix:  
\- Added condition for proper email check for field `user_email`.  
\- Added check for field `Action1` not in `RATE_LIMIT`.  
\- Added null, unknown check for `actor.displayName`.   
2022-11-04 |  Enhancement:  
Added support for logs having multiple events.   
2022-10-15 |  Enhancement:  
\- `signOnModeType` mapped to `security_result.detection_fields`.  
\- `authenticationProvider` mapped to `security_result.detection_fields`.  
\- `credentialProvider` mapped to `security_result.detection_fields`.  
\- `device` mapped to `additional.fields`.  
\- `zone` mapped to `additional.fields`.  
\- `type` mapped to `additional.fields`.   
2022-10-14 |  Bug-fix:  
\- Added conditional check for `principal.user.email_addresses` and `target.user.email_addresses`.  
\- Added grok to check for valid ip_address for the field `request.ipChain.0.ip` mapped to `principal.ip`.  
\- Added on_error condition for the field `debugContext.debugData.url` mapped to `target.url`.   
2022-10-03 |  Enhancement:  
\- Mapped `client.userAgent.os` to `principal.platform`.  
\- Mapped `client.device` to `principal.asset.type`.  
\- Mapped `anonymized IP` (hardcoded string) to security_result.detection_fields.key where `securityContext.isProxy` value to corresponding security_result.detection_fields.value.   
2022-09-16 |  Enhancement:  
\- `securityContext.asOrg` mapped to `security_result.category_details`.  
\- `securityContext.isProxy` mapped to `security_result.detection_fields`.  
\- `securityContext.domain` mapped to `security_result.detection_fields`.  
\- `securityContext.isp` mapped to `security_result.detection_fields`.  
\- `debugContext.debugData.risk.level` mapped to `security_result.severity`.  
\- `debugContext.debugData.risk.reasons` mapped to `security_result.detection_fields`.   
2022-08-12 |  Enhancement: The newly ingested logs have been parsed and mapped to following fields:  
\- `detail.uuid` mapped to `metadata.product_log_id`.  
\- `detail.eventType` mapped to `metadata.product_event_type`  
\- `detail.actor.id` mapped to `principal.user.product_object_id`.  
\- if `detail.actor.alternateId` mapped to `principal.user.userid` else  
`detail.actor.alternateId` mapped to `principal.user.email_addresses`.  
\- `detail.actor.displayName` mapped to `principal.user.user_display_name`.  
\- `detail.actor.type` mapped to `.principal.user.attribute.roles`.  
\- `detail.client.ipChain.0.ip` mapped to `principal.ip`.  
\- `detail.client.ipChain.0.geographicalContext.state` mapped to `principal.location.state`.  
\- `detail.client.ipChain.0.geographicalContext.city` mapped to `principal.location.city`.  
\- `detail.client.ipChain.0.geographicalContext.country` mapped to `principal.location.country_or_region`.  
\- `detail.debugContext.debugData.requestUri` mapped to `target.url`.  
\- `detail.target.0.type` mapped to `target.resource.resource_subtype`.  
\- `detail.target.0.id` mapped to `target.resource.resource.product_object_id`.  
\- `detail.target.0.displayName` mapped to `target.resource.resource_subtype`.  
\- `detail.target.0.detailEntry.policyType` mapped to `target.resource_ancestors.attribute.labels`.  
\- `detail.outcome.reason` mapped to `security_result.category_details`.  
\- `detail.debugContext.debugData.threatSuspected` mapped to `security_result.detection_fields`.  
\- `detail.displayMessage` mapped to `security_result.summary`.  
\- `detail.outcome.result` mapped to `security_result.action`.  
\- `detail.severity` mapped to `security_result.severity`.  
\- `detail.transaction.id` mapped to `network.session_id`.  
\- `detail.debugContext.debugData.requestUri` mapped to `extensions.auth.auth_details`.   
2022-07-08 |  Enhancement:  
\- Modified mapping for `actor.type` from `principal.user.role_name` to `principal.user.attribute.roles`.  
\- Modified mapping for `target.0.type` from `target.user.role_name` to `target.user.attribute.roles`.  
\- Modified mapping for `target.1.type` from `target.user.role_name` to `target.user.attribute.roles`.   
2022-06-15 |  Enhancement-  
\- for `target.0.type` == `Token`.  
\- Mapped `target.0.detailEntry.clientAppId` to `target.asset_id`.  
\- Added conditional check for the field `transaction.id` mapped to the UDM field `network.session_id`.   
2022-06-03 |  Enhancement-  
Mapped debugContext.debugData.privilegeGranted to target.user.attribute.roles.name additionally.  
Mapped debugContext.debugData.requestUri to extensions.auth.auth_details.  
Mapped debugContext.debugData.suspiciousActivityEventId, debugContext.debugData.threatDetections, debugContext.debugData.threatSuspected to security_result.detection_fields.   
2022-03-22 |  Enhancement-  
debugContext.debugData.behaviors mapped to security_result.description.  
debugContext.debugData.threatSuspected mapped to security_result.threat_status.  
debugContext.debugData.risk mapped to security_result.severity.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

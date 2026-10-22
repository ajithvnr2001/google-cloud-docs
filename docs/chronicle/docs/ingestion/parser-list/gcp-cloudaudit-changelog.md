---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloudaudit-changelog/
title: Change log for GCP_CLOUDAUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:43.252721+00:00
---

# Change log for GCP_CLOUDAUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloudaudit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_CLOUDAUDIT

Date | Changes  
---|---  
2026-10-01 |  \- Optimized parser execution performance while preserving full UDM output parity:  
\- Guarded pre-JSON `annotations` regex Grok, secondary JSON parse, and `for data in annotation` loop with `if [message] =~ `annotations``.  
\- Removed 15 empty-string (`""`) pre-initializations of nested `protoPayload.*` paths from the top-level initialization block to avoid creating empty intermediate maps and triggering phantom loop iterations on every log, and added explicit `on_error` temporary extraction guards.  
\- Added subtree existence probes (`mutate { convert => { ... => `string` } on_error => ... }`) across the general `protoPayload` section (`metadata.*`, `serviceData.*`, `request.*`, `response.*`) to skip unpopulated subtrees.  
\- Added subtree existence probes inside the `serviceName == `k8s.io`` section (`webhooks`, `spec.template.spec`, `spec.jobTemplate.spec.template.spec` across `request` and `response`) and inside `containers`, `initContainers`, and `ephemeralContainers` loops (`lifecycle`, `livenessProbe`, `readinessProbe`, `startupProbe`, `securityContext`) to bypass unpopulated Kubernetes extraction blocks.   
2026-08-21 |  \- target.resource.attribute.labels: Newly mapped `protoPayload.request.targetTags` raw log field with `target.resource.attribute.labels[req_target_tags_%{index}]` UDM field.   
2026-08-04 |  \- `target.resource.attribute.labels`: Newly mapped `protoPayload.request.retrohunt.processInterval.endTime` raw log field with `target.resource.attribute.labels` UDM field with key `req_retrohunt_endTime`.  
\- `target.resource.attribute.labels`: Newly mapped `protoPayload.request.retrohunt.processInterval.startTime` raw log field with `target.resource.attribute.labels` UDM field with key `req_retrohunt_startTime`.  
\- `target.resource.attribute.labels`: Newly mapped `protoPayload.request.retrohunt.name` raw log field with `target.resource.attribute.labels` UDM field with key `req_retrohunt_name`.   
2026-07-31 |  \- target.resource.attribute.labels[res_item_ip_cidr]: Newly mapped `protoPayload.response.items` raw log field with `target.resource.attribute.labels[res_item_ip_cidr]` UDM field.   
2026-07-24 |  \- additional.fields[key]: Newly mapped `labels` object raw log fields with `additional.fields[key]` UDM field.   
2026-07-14 |  \- target.resource.attribute.labels: Newly mapped `protoPayload.request.bucket.retentionDays` raw log field with `target.resource.attribute.labels[req_bucket_retention_days]` UDM field.  
\- target.ip: Newly mapped `protoPayload.response.items` raw log field with `target.ip` UDM field.  
\- metadata.event_type: Enhance event validation logic that uses the principal.user.userid UDM field in validation.   
2026-06-30 |  \- Added mappings below for `google.cloud.chronicle.v1alpha.RuleService.ModifyRules` MethodName:  
\- security_result.detection_fields[req_requests_%{index}_update_mask]: Newly mapped `protoPayload.request.requests.updateMask` raw log field with `security_result.detection_fields[req_requests_%{index}_update_mask]` UDM field.  
\- security_result.rule_labels[req_requests_%{index}_rule_live_mode_enabled]: Newly mapped `protoPayload.request.requests.rule.liveModeEnabled` raw log field with `security_result.rule_labels[req_requests_%{index}_rule_live_mode_enabled]` UDM field.  
\- security_result.rule_name: Newly mapped `protoPayload.request.requests.rule.name` raw log field with `security_result.rule_name` UDM field.   
2026-06-05 |  \- target.resource.attribute.labels[`req_rule_text`]: Newly mapped `protoPayload.request.rule.text` raw log field with `target.resource.attribute.labels[`req_rule_text`]` UDM field.  
\- target.resource.attribute.labels[`res_text`]: Newly mapped `protoPayload.response.text` raw log field with `target.resource.attribute.labels[`res_text`]` UDM field.   
2026-05-14 |  \- Added mappings below for `google.cloud.chronicle.v1alpha.RuleService.UpdateRuleDeployment` MethodName:  
\- target.resource.attribute.labels[`req_rule_deployment_name`]: Newly mapped `protoPayload.request.ruleDeployment.name` raw log field with `target.resource.attribute.labels[`req_rule_deployment_name`]` UDM field.  
\- target.resource.attribute.labels[`req_rule_deployment_alerting`]: Newly mapped `protoPayload.request.ruleDeployment.alerting` raw log field with `target.resource.attribute.labels[`req_rule_deployment_alerting`]` UDM field.  
\- target.resource.attribute.labels[`res_last_alert_status_change_time`]: Newly mapped `protoPayload.response.lastAlertStatusChangeTime` raw log field with `target.resource.attribute.labels[`res_last_alert_status_change_time`]` UDM field.  
\- target.resource.attribute.labels[`res_enabled`]: Newly mapped `protoPayload.response.enabled` raw log field with `target.resource.attribute.labels[`res_enabled`]` UDM field.  
\- target.resource.attribute.labels[`res_execution_state`]: Newly mapped `protoPayload.response.executionState` raw log field with `target.resource.attribute.labels[`res_execution_state`]` UDM field.  
\- target.resource.attribute.labels[`res_archive_time`]: Newly mapped `protoPayload.response.archiveTime` raw log field with `target.resource.attribute.labels[`res_archive_time`]` UDM field.  
\- target.resource.attribute.labels[`res_archived`]: Newly mapped `protoPayload.response.archived` raw log field with `target.resource.attribute.labels[`res_archived`]` UDM field.  
\- Added mappings below for `google.cloud.resourcemanager.v3.TagBindings.CreateTagBinding` MethodName:  
\- target.resource.attribute.labels[`res_tag_value_namespaced_name`]: Newly mapped `protoPayload.response.tagValueNamespacedName` raw log field with `target.resource.attribute.labels[`res_tag_value_namespaced_name`]` UDM field.   
2026-04-02 |  \- Added mappings below for `google.cloud.chronicle.v1alpha.CuratedRuleService.BatchUpdateCuratedRuleSetDeployments` MethodName:  
\- `target.resource.attribute.labels`: Newly mapped `protoPayload.request.requests.curatedRuleSetDeployment.enabled` raw log field with `target.resource.attribute.labels` UDM field.  
\- `target.resource.attribute.labels`: Newly mapped `protoPayload.request.requests.curatedRuleSetDeployment.precision` raw log field with `target.resource.attribute.labels` UDM field.  
\- `target.resource.attribute.labels`: Newly mapped `protoPayload.request.requests.curatedRuleSetDeployment.name` raw log field with `target.resource.attribute.labels` UDM field.  
\- `target.resource.attribute.labels`: Newly mapped `protoPayload.request.requests.curatedRuleSetDeployment.alerting` raw log field with `target.resource.attribute.labels` UDM field.  
\- Added mappings below for `beta.compute.instances.insert` MethodName:  
\- `target.resource.attribute.labels`: Newly mapped `protoPayload.request.networkInterfaces.nicType` raw log field with `target.resource.attribute.labels` UDM field.  
\- `target.resource.attribute.labels`: Newly mapped `protoPayload.request.networkInterfaces.network` raw log field with `target.resource.attribute.labels` UDM field.  
\- `target.ip`: Newly mapped `protoPayload.request.networkInterfaces.networkIP` raw log field with `target.ip` UDM field.  
\- `target.resource.attribute.labels`: Newly mapped `protoPayload.request.networkInterfaces.networkAttachment` raw log field with `target.resource.attribute.labels` UDM field.   
2026-01-22 |  \- Optimize the mapping pattern to reduce the configuration file size.  
\- `target.resource.attribute.labels`: Updated key from `oauth_client_id` to `metadata_oauth_client_id` for raw log field `protoPayload.metadata.oauth_client_id`.  
\- `target.resource.attribute.labels`: Updated key from `req_spec_username` to `request_spec_user` for raw log field `protoPayload.request.spec.user`.  
\- `target.resource.attribute.labels`: Updated key from `request_constraint` to `request_policy_boolean_policy_constraint` for raw log field `protoPayload.request.policy.booleanPolicy.enforced`.  
\- `target.resource.attribute.labels`: Updated key from `cls_name` to `resource_labels_cluster_name` for raw log field `resource.labels.cluster_name`.  
\- `target.resource.attribute.labels`: Updated key from `email_id` to `resource_email_id` for raw log field `resource.email_id`.  
\- `target.resource.attribute.labels`: Updated key from `email_id` to `resource_labels_email_id` for raw log field `resource.labels.email_id`.  
\- `target.resource.attribute.labels`: Updated key from `imagepolicywebhook.image-policy.k8s.io/dry-run` to `imagepolicywebhook_image_policy_k8s_io_dry_run` for raw log field `labels.imagepolicywebhook.image-policy.k8s.io/dry-run`.  
\- `target.resource.attribute.labels`: Updated key from `request.metadata.name` to `request_metadata_name` for raw log field `protoPayload.request.metadata.name`.  
\- `target.resource.attribute.labels`: Updated key from `Denied Protocol` to `Denied_Protocol` for raw log field `protoPayload.request.denieds.0.IPProtocol`.  
\- `target.resource.attribute.labels`: Updated key from `Request Priority` to `Request_Priority` for raw log field `protoPayload.request.priority`.  
\- `target.resource.attribute.labels`: Updated key from `request apiVersion` to `request_apiVersion` for raw log field `protoPayload.request.apiVersion`.  
\- `target.resource.attribute.labels`: Updated key from `Request Network` to `Request_Network` for raw log field `protoPayload.request.network`.  
\- `additional.fields`: Updated key from `req_page_size` to `request_page_size` for raw log field `request.pagesize`.  
\- `target.resource.attribute.labels`: Removed duplicate key mappings within the labels block to improve parser efficiency and maintainability.   
2025-12-15 |  \- principal.ip: Removed mapping of `httpRequest.serverIp` from `principal.ip` UDM field and mapped `httpRequest.remoteIp` instead.  
\- principal.asset.ip: Removed mapping of `httpRequest.serverIp` from `principal.asset.ip` UDM field and mapped `httpRequest.remoteIp` instead.  
\- target.ip: Removed mapping of `httpRequest.remoteIp` from `target.ip` UDM field and mapped `httpRequest.serverIp` instead.  
\- target.asset.ip: Removed mapping of `httpRequest.remoteIp` from `target.asset.ip` UDM field and mapped `httpRequest.serverIp` instead.   
2025-11-05 |  Added support for kubernetes API resources as part of Cloud Audit Logs parser update.   
2025-09-05 |  principal.namespace: Removed mapping of `protoPayload.request.metadata.namespace` from `principal.namespace` UDM field and mapped to `security_result.about.namespace` in order to prevent the feed namespace from being overwritten by the prebuilt parser.   
2025-08-28 |  Handled edge case for raw log field `protoPayload.request.disks[].mode` for event `v1.compute.instances.startWithEncryptionKey`.   
2025-07-29 |  Improve validation logic to handle `protoPayload.request.cluster` when it appears as either an object or a string.   
2025-05-05 |  Renamed incorrectly labeled variable used for populating `about.resource.name`.   
2025-04-28 |  \- target.resource_ancestors.attribute.labels: Newly mapped `protoPayload.response.spec.template.spec.containers.securityContext.runAsUser` raw log field with `target.resource_ancestors.attribute.labels` UDM field   
2025-04-11 |  \- target.resource.attribute.labels: Newly mapped `protoPayload.request.metadata.generateName` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.metadata.annotations` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.metadata.labels` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.rules.host` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.rules.http.paths.path` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.rules.http.paths.pathType` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.rules.http.paths.backend.service.name` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.rules.http.paths.backend.service.port.name` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.rules.http.paths.backend.service.port.number` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.rules.http.paths.backend.resource.kind` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.rules.http.paths.backend.resource.name` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.rules.http.paths.backend.resource.apiGroup` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.rules.http.paths.backend.serviceName` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.rules.http.paths.backend.servicePort` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.status.loadBalancer.ingress.hostname` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.status.loadBalancer.ingress.ports.port` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.status.loadBalancer.ingress.ports.protocol` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.status.loadBalancer.ingress.ports.error` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.backend.serviceName` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.backend.servicePort` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.defaultBackend.service.name` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.defaultBackend.service.port.name` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.defaultBackend.service.port.number` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.defaultBackend.resource.kind` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.defaultBackend.resource.name` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.defaultBackend.resource.apiGroup` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.ingressClassName` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.tls.hosts` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.metadata.generateName` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.metadata.annotations` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.metadata.labels` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.rules.host` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.rules.http.paths.path` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.rules.http.paths.pathType` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.rules.http.paths.backend.service.name` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.rules.http.paths.backend.service.port.name` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.rules.http.paths.backend.service.port.number` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.rules.http.paths.backend.resource.kind` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.rules.http.paths.backend.resource.name` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.rules.http.paths.backend.resource.apiGroup` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.rules.http.paths.backend.serviceName` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.rules.http.paths.backend.servicePort` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.status.loadBalancer.ingress.hostname` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.status.loadBalancer.ingress.ports.port` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.status.loadBalancer.ingress.ports.protocol` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.status.loadBalancer.ingress.ports.error` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.backend.serviceName` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.backend.servicePort` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.defaultBackend.service.name` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.defaultBackend.service.port.name` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.defaultBackend.service.port.number` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.defaultBackend.resource.kind` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.defaultBackend.resource.name` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.defaultBackend.resource.apiGroup` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.ingressClassName` raw log field with `target.resource.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.tls.hosts` raw log field with `target.resource.attribute.labels` UDM field.  
\- security_result.detection_fields: Newly mapped `protoPayload.request.spec.tls.secretName` raw log field with `security_result.detection_fields` UDM field.  
\- security_result.detection_fields: Newly mapped `protoPayload.request.data.tls.crt` raw log field with `security_result.detection_fields` UDM field.  
\- security_result.detection_fields: Newly mapped `protoPayload.request.data.tls.key` raw log field with `security_result.detection_fields` UDM field.  
\- security_result.detection_fields: Newly mapped `protoPayload.response.spec.tls.secretName` raw log field with `security_result.detection_fields` UDM field.  
\- security_result.detection_fields: Newly mapped `protoPayload.response.data.tls.crt` raw log field with `security_result.detection_fields` UDM field.  
\- security_result.detection_fields: Newly mapped `protoPayload.response.data.tls.key` raw log field with `security_result.detection_fields` UDM field.  
\- target.ip: Newly mapped `protoPayload.request.status.loadBalancer.ingress.ip` raw log field with `target.ip` UDM field.  
\- target.ip: Newly mapped `protoPayload.response.status.loadBalancer.ingress.ip` raw log field with `target.ip` UDM field.  
\- target.resource_ancestors.name: Newly mapped `protoPayload.request.spec.containers.name` raw log field with `target.resource_ancestors.name` UDM field.  
\- target.resource_ancestors.name: Newly mapped `protoPayload.response.spec.containers.name` raw log field with `target.resource_ancestors.name` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.containers.image` raw log field with `target.resource_ancestors.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.containers.image` raw log field with `target.resource_ancestors.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.request.spec.containers.ports.containerPort` raw log field with `target.resource_ancestors.attribute.labels` UDM field.  
\- target.resource.attribute.labels: Newly mapped `protoPayload.response.spec.containers.ports.containerPort` raw log field with `target.resource_ancestors.attribute.labels` UDM field.   
2025-03-11 |  \- `additional.fields[validate_only]`: Newly mapped `protoPayload.request.validateOnly` raw log field with `additional.fields[validate_only]` UDM field.   
2025-01-27 |  \- Added mapping for the raw log field `protoPayload.request.spec.template.spec.containers.securityContext.runAsUser` to target.resource.attribute.labels[req_spec_template_spec_containers_securitycontext_run_as_user] UDM field.   
2024-12-16 |  \- Added mapping for the raw log fields `protoPayload.request.serialConsoleOptions`, `protoPayload.request.username` and `protoPayload.response.duration`  
2024-12-13 |  \- Removed mapping of `callerIp` raw log field from `principal.hostname` and `principal.asset.hostname` UDM field.   
2024-10-15 |  \- Added mapping for these fields: `protoPayload.metadata.jobInsertion.reason`, `protoPayload.metadata.jobInsertion.job.jobConfig.queryConfig.statementType` and `protoPayload.metadata.jobInsertion.job.jobStatus.jobState`  
\- Added support for the raw log fields `protoPayload.response.state` and `protoPayload.request.metadata.state`.   
2024-10-11 |  \- Added support for the raw log fields under `protoPayload.metadata.jobChange` and `protoPayload.metadata.jobInsertion` objects.   
2024-10-01 |  \- Set `metadata.event_type` UDM field as `USER_LOGIN` if the value of `protoPayload.request.cmd` raw field is `connect`.   
2024-09-17 |  \- Updated mapping of metadata.event_type UDM field.   
2024-09-13 |  \- Updated the GCP_CLOUDAUDIT Gold parser to update mandatory UDM field for event_type `USER_UNCATEGORIZED`.   
2024-09-03 |  \- Added mapping for `protoPayload.request.spec.template.spec.shareProcessNamespace` log field.  
\- Added mapping for `protoPayload.response.spec.type` log field.  
\- Updated the logic of `target.resource.resource_type` UDM field.  
\- Extracted and mapped organization ids.  
\- Added mapping for `protoPayload.metadata.event.parameter.boolValue` log field.  
\- Added mapping for `protoPayload.response.vulnerability.shortDescription`, `protoPayload.response.vulnerability.effectiveSeverity` and `protoPayload.response.resourceUri` log fields.   
2024-08-30 |  \- Added mapping for protoPayload.request.permissions raw log field.   
2024-08-14 |  \- Added mapping for protoPayload.response.roleRef.name raw log field.  
\- Added mapping for protoPayload.authorizationInfo.permissionType raw log field.  
\- Set the security_result.action as BLOCK for every error blob.  
\- Added mapping for protoPayload.metadata.instanceMetadataDelta.addedMetadataKeys raw log field.  
\- Added mapping for protoPayload.authenticationInfo.serviceAccountDelegationInfo.firstPartyPrincipal.principalEmail raw log field.   
2024-07-19 |  \- Updated mapping for `security_result.action` based on the `protoPayload.response.status` log field.  
\- Added mapping for `protoPayload.response.reason` log field.  
\- Update mapping for `protoPayload.response.code` log field.  
\- Removed mapping of `protoPayload.metadata.event` raw log field form `target.resource_ancestors`.  
\- Updated mapping for `metadata.description` based on the `protoPayload.status.message` log field.  
\- Updated mapping for `protoPayload.request.policy.bindings.members` raw log field.   
2024-07-03 |  \- Mapped `protoPayload.response.bindings` to `additional.fields`.  
\- Mapped `protoPayload.request.bindings` to `additional.fields`.   
2024-06-20 |  \- Added mappings for the following fields:  
\- `protoPayload.request.projection`  
\- `protoPayload.response.items.metageneration`  
\- `protoPayload.response.items.labels.created_date`  
\- `protoPayload.response.items.labels.team_email`  
\- `protoPayload.response.items.labels.team_name`  
\- `protoPayload.response.items.labels.office_number`  
\- `protoPayload.response.items.labels.department`  
\- `protoPayload.response.items.labels.business_project_number`  
\- `protoPayload.response.items.labels.owner_email`  
\- `protoPayload.response.items.labels.purchase_order_number`  
\- `protoPayload.response.items.labels.office_name`  
\- `protoPayload.response.items.labels.environment`  
\- `protoPayload.response.items.labels.created_by`  
\- `protoPayload.response.items.labels.project_name`  
\- `protoPayload.response.items.labels.finops_tag`  
\- `protoPayload.response.items.labels.owner_role`  
\- `protoPayload.response.items.versioning.enabled`  
\- `protoPayload.response.items.iamConfiguration.publicAccessPrevention`  
\- `protoPayload.response.items.iamConfiguration.uniformBucketLevelAccess.lockedTime`  
\- `protoPayload.response.items.iamConfiguration.uniformBucketLevelAccess.enabled`  
\- `protoPayload.response.items.id`  
\- `protoPayload.response.items.updated`  
\- `protoPayload.response.items.storageClass`  
\- `protoPayload.response.items.timeCreated`  
\- `protoPayload.response.items.location`  
\- `protoPayload.response.items.locationType`  
\- `protoPayload.response.items.projectNumber`  
\- `protoPayload.response.items.name`  
\- `protoPayload.response.items.softDeletePolicy.effectiveTime`  
\- `protoPayload.response.items.softDeletePolicy.retentionDurationSeconds`  
\- `protoPayload.response.items.etag`  
2024-06-19 |  \- Added mappings for the following raw log fields: `protoPayload.response.displayName`, `protoPayload.request.referenceList.displayName`.  
\- Extracted values from the following raw log fields: `protoPayload.authenticationInfo.principalSubject`, `protoPayload.resourceName`.   
2024-05-29 |  \- Removed mapping of the `protoPayload.authenticationInfo.principalEmail` raw log field from the `target.user.userid` UDM field.  
\- Updated the Grok pattern to support multiple values of the `protoPayload.metadata.membershipDelta.member` raw log field.  
\- Added mappings of the `protoPayload.metadata.updatedGrant.state`, `protoPayload.metadata.updatedGrant.privilegedAccess.gcpIamAccess.resource`,  
`protoPayload.metadata.updatedGrant.privilegedAccess.gcpIamAccess.resourceType`, `protoPayload.metadata.updatedGrant.privilegedAccess.gcpIamAccess.roleBindings.role`,  
`protoPayload.metadata.updatedGrant.justification.unstructuredJustification`, `protoPayload.metadata.updatedGrant.requestedDuration`,  
`protoPayload.metadata.updatedGrant.requester`, `protoPayload.metadata.jobInsertion.job.jobConfig.labels.looker_studio_report_id`,  
`protoPayload.metadata.jobInsertion.job.jobConfig.labels.requestor` and protoPayload.metadata.jobInsertion.job.jobConfig.labels.looker_studio_datasource_id" raw log fields.   
2024-05-22 |  \- Added mappings for the following fields: `protoPayload.metadata.tableChange.table.policy.bindings.members, protoPayload.metadata.datasetChange.dataset.acl.policy.bindings.members, protoPayload.request.bindings.members, protoPayload.metadata.tableChange.bindingDeltas.member`  
2024-05-15 |  \- Added mapping for fields: `protoPayload.metadata.jobChange.job.jobConfig.labels.looker_studio_report_id, protoPayload.metadata.jobChange.job.jobConfig.labels.requestor and protoPayload.metadata.jobChange.job.jobConfig.labels.looker_studio_datasource_id`  
2024-05-01 |  \- Added a mapping for the `protoPayload.response.serviceConfig.timeoutSeconds` raw log field.   
2024-04-24 |  \- Added mapping for fields: `protoPayload.serviceData.jobCompletedEvent.job.jobConfiguration.labels.requestor`, `protoPayload.serviceData.jobCompletedEvent.job.jobConfiguration.labels.looker_studio_datasource_id`, `protoPayload.serviceData.jobCompletedEvent.job.jobConfiguration.labels.looker_studio_report_id` and `protoPayload.metadata.jobChange.job.jobConfig.queryConfig.query`.  
\- Added support for `protoPayload.response.overrideValue` and `protoPayload.request.override.overrideValue` log fields.   
2024-04-17 |  \- Add mapping for protoPayload.request.timestampRange,  
protoPayload.request.regexSearch, protoPayload.request.productSources,  
protoPayload.request.query, protoPayload.request.caseSensitive raw log fields.   
2024-03-27 |  \- Handled the jumpcloud function audit logs in the parser.   
2024-03-06 |  \- Added mapping of `protoPayload.request.New Data` and `protoPayload.request.Original Data` raw log fields.  
\- Added mapping for fields of `protoPayload.request.service.metadata.annotations` and `protoPayload.request.service.spec.template.metadata.annotations` object.  
\- Added mapping for fields of `protoPayload.response.spec.template` object.   
2024-02-28 |  \- Added mapping of `protoPayload.request.metadata.resourceVersion` raw log field.  
\- Change mapping of `protoPayload.metadata.projectMetadataDelta` and `protoPayload.request.action` raw log field.   
2024-01-31 |  \- Added additional field mapping for `GroupsService.UpdateGroup` MethodName.   
2024-01-17 |  \- Added mapping of `protoPayload.metadata.datasetChange.bindingDeltas` raw log field block.  
\- Added additional field mapping of `io.k8s.certificates.v1.certificatesigningrequest`, `UpdateCryptoKeyVersion`, `google.cloud.orgpolicy.v2.OrgPolicy.DeletePolicy`, `UpdateEventThreatDetectionSettings`, `SetIamPolicy` and `beta.compute.images.setIamPolicy` MethodName.  
\- Removed duplicate mapping of `security_result.action` UDM field.   
2023-12-13 |  \- Changed mapping of `target.application` UDM field for Kubernetes Engine events.   
2023-11-29 |  \- Added mapping of `securityContext.capabilities.add`, `securityContext.seccompProfile.type` and `spec.Containers.shareProcessNamespace` raw log fields.  
\- Added mapping of `membershipDelta` raw log block.  
\- Added support of `SelfSubjectAccessReviews` MethodName.  
\- Added mappings of the raw log fields which were mapped to the deprecated field `noun.labels`.   
2023-11-09 |  \- Added mapping of `request.roleRef.name` log field.  
\- Added support for the `clusterroles.create` MethodName.  
\- Added support for the `daemonsets.create` MethodName.  
\- Align `principal/target.hostname` and `principal/target.asset.hostname` mapping.   
2023-10-18 |  \- Added mapping of `labels.imagepolicywebhook.image-policy.k8s.io/dry-run` log field.   
2023-08-28 |  \- Updated `metadata.event_type` for `DisableServiceAccount` and `EnableServiceAccount` MethodName.   
2023-07-26 |  \- Updated `metadata.event_type` for `v1.compute.disks.insert` MethodName.  
\- Updated mapping of `protoPayload.status.code` log field.   
2023-07-12 |  Added support for the `io.k8s.batch.v1.jobs.create` MethodName.   
2023-06-14 |  Updated the parser to include `parse_network_http_user_agent` to use `Parsed User Agent` and `User Agent`.   
2023-05-02 |  Added mapping for `protoPayload.request.action` log field of  
methodName `v1.compute.securityPolicies.patchRule` and set value of  
`security_result.action` UDM field based on the `protoPayload.request.action`  
log field.   
2023-04-12 |  Promoted GCP_CLOUDAUDIT parser to default.  
For the field mapping reference, see https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudaudit#field-mapping.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

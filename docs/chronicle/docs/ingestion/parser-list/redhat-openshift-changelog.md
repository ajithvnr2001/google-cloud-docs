---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/redhat-openshift-changelog/
title: Change log for REDHAT_OPENSHIFT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:28.692545+00:00
---

# Change log for REDHAT_OPENSHIFT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/redhat-openshift-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for REDHAT_OPENSHIFT

Date | Changes  
---|---  
2026-09-28 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `requestObject.userName` and `annotations.authentication.openshift.io/username` raw log fields to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `responseObject.userName` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field when `requestObject.userName` is not present.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `annotations.authentication.openshift.io/decision` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `requestObject.clientName` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `responseObject.clientName` raw log field to `event.idm.read_only_udm.target.application` UDM field when `requestObject.clientName` is empty.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `requestObject.redirectURI` raw log field to `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `responseObject.redirectURI` raw log field to `event.idm.read_only_udm.network.http.referral_url` UDM field when `requestObject.redirectURI` is empty.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `requestObject.userUID` raw log field to `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `responseObject.userUID` raw log field to `event.idm.read_only_udm.target.user.product_object_id` UDM field when `requestObject.userUID` is empty.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `requestObject.expiresIn` raw log field to `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `responseObject.expiresIn` raw log field to `event.idm.read_only_udm.network.session_duration.seconds` UDM field when `requestObject.expiresIn` is empty.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `requestObject.scopes` raw log field to `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `responseObject.scopes` and `user.extra.authentication.kubernetes.io/node-uid` raw log field to `event.idm.read_only_udm.target.user.attribute.labels` UDM field when `requestObject.scopes` is empty.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `responseStatus.message`, `requestObject.codeChallenge`, `responseObject.codeChallenge`, `requestObject.codeChallengeMethod`, `responseObject.metadata.uid`, `responseObject.metadata.creationTimestamp` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2026-04-30 |  Enhancement:  
\- Modified grok patterns to parse `syslog_priority` raw log field.  
\- Added a grok pattern on `msg` to extract `prod_log_id`, `prog_id`.  
\- `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `inter_hostname` raw log field with `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.observer.asset.hostname`: Newly mapped `observer_hostname` and `app_name` raw log field with `event.idm.read_only_udm.observer.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `arch` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `syscall` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `SYSCALL` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.pid`: Newly mapped `ppid` raw log field with `event.idm.read_only_udm.principal.process.parent_process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `uid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.group.product_object_id`: Newly mapped `gid` raw log field with `event.idm.read_only_udm.principal.group.product_object_id` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `ses` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `comm` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `exe` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `UID` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.group.group_display_name`: Newly mapped `GID` raw log field with `event.idm.read_only_udm.principal.group.group_display_name` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `euid` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `EUID` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.group.product_object_id`: Newly mapped `egid` raw log field with `event.idm.read_only_udm.target.group.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `prod_log_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Mapped `res`, `success` raw log fields with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` if user data is present.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `subcomponent` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `a0`, `a1`, `a2`, `a3`, `items`, `suid`, `auid`, `fsuid`, `sgid`, `fsgid`, `subj`, `key`, `exit`, `tty`, `ARCH`, `AUID`, `SUID`, `FSUID`, `EGID`, `SGID`, `FSGID`, `prog_id`, `op`, `syslog_priority` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-03-12 |  Enhancement:  
\- Added a grok pattern to support syslog+json format logs.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `message_id` raw log field to `event.idm.read_only_udm.metadata.product_log_id`.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `pod_name` raw log field to `event.idm.read_only_udm.principal.resource.name`.  
\- `event.idm.read_only_udm.network.application_protocol`: If `proto` contains `HTTP`, updated the value of `event.idm.read_only_udm.network.application_protocol` to `HTTP`.  
\- `event.idm.read_only_udm.network.http.application_protocol_version`: If `proto` contains version, updated the version value to `event.idm.read_only_udm.network.http.application_protocol_version`.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `remoteAddress` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `statusCode` raw log field to `event.idm.read_only_udm.network.http.response_code`.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `url` raw log field to `event.idm.read_only_udm.target.url`.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `username` raw log field to `event.idm.read_only_udm.principal.user.user_display_name`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `contentLength`, `container_name`, `namespace_name`, and `component` raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_ver`, `container_type`, `pos`, `proto`, `thread_id`, `datetime`, and `line_number` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `file` raw log field to `event.idm.read_only_udm.principal.process.file.full_path`.   
2026-02-23 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `hostname` value extracted from syslog header with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_hostname` raw log extracted from syslog header with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `log_type` (key: `log_type`), `requestObject.apiVersion` (key: `requestObject_apiVersion`), `requestObject.kind` (key: `requestObject_kind`), `requestObject.propagationPolicy` (key: `requestObject_propagationPolicy`), `responseObject.apiVersion` (key: `responseObject_apiVersion`), `responseObject.kind` (key: `responseObject_kind`), `responseObject.metadata.resourceVersion` (key: `responseObject_metadata_resourceVersion`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `user.extra.authentication.kubernetes.io/credential-id` (key: `credential_id_%{index}`) and `user.extra.authentication.kubernetes.io/node-name` (key: `node_name_%{index}`) raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- Modified a grok pattern to parse the raw log fields.   
2025-12-22 |  Enhancement:  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field to `event.idm.read_only_udm.principal.process.pid`.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `kubernetes.container_image` raw log field to event.idm.read_only_udm.target.file.full_path.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `kubernetes.container_name` raw log field to `event.idm.read_only_udm.target.application`.  
\- `event.idm.read_only_udm.target.namespace`: Newly mapped `kubernetes.namespace_name` raw log field to `event.idm.read_only_udm.target.namespace`.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `kubernetes.pod_ip` raw log field to `event.idm.read_only_udm.target.ip`.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `kubernetes.pod_ip` raw log field to `event.idm.read_only_udm.target.asset.ip`.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `kubernetes.pod_name` raw log field to `event.idm.read_only_udm.target.resource.name`.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `kubernetes.pod_id` raw log field to `event.idm.read_only_udm.target.resource.product_object_id`.  
\- `event.idm.read_only_udm.observer.process.pid`: Newly mapped `systemd.t.PID` raw log field to `event.idm.read_only_udm.observer.process.pid`.  
\- `event.idm.read_only_udm.observer.process.file.full_path`: Newly mapped `systemd.t.EXE` raw log field to `event.idm.read_only_udm.observer.process.file.full_path`.  
\- `event.idm.read_only_udm.observer.process.command_line`: Newly mapped `systemd.t.CMDLINE` raw log field to `event.idm.read_only_udm.observer.process.command_line`.  
\- `event.idm.read_only_udm.observer.user.userid`: Newly mapped `systemd.t.UID` raw log field to `event.idm.read_only_udm.observer.user.userid`.  
\- `event.idm.read_only_udm.observer.group.product_object_id`: Newly mapped `systemd.t.GID` raw log field to `event.idm.read_only_udm.observer.group.product_object_id`.  
\- `event.idm.read_only_udm.observer.asset.asset_id`: Newly mapped `systemd.t.MACHINE_ID` raw log field to `event.idm.read_only_udm.observer.asset.asset_id`.  
\- `event.idm.read_only_udm.observer.application`: Newly mapped `systemd.t.SYSTEMD_UNIT` raw log field to `event.idm.read_only_udm.observer.application`.  
\- `event.idm.read_only_udm.observer.application`: Newly mapped `systemd.u.SYSLOG_IDENTIFIER` raw log field to `event.idm.read_only_udm.observer.application`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `name`, `interface`, `default`, `kubernetes.labels.app`, `kubernetes.labels.pod-template-hash`, `kubernetes.labels.svcname`, `kubernetes.namespace_labels.kubernetes_io_metadata_name`, `kubernetes.namespace_labels.pod-security_kubernetes_io_audit`, `kubernetes.namespace_labels.pod-security_kubernetes_io_audit-version`, `kubernetes.namespace_labels.pod-security_kubernetes_io_warn`, `kubernetes.namespace_labels.pod-security_kubernetes_io_warn-version`, `kubernetes.namespace_labels.storage_openshift_io_fsgroup-change-policy`, `systemd.t.COMM`, `crio_message_timestamp`, `kubernetes.annotations.k8s.v1.cni.cncf.io/network-status`, `openshift_audit_level`, `requestReceivedTimestamp`, `stageTimestamp`, `kubernetes.container_id`, `kubernetes.container_iostream`, `kubernetes.namespace_id`, `kubernetes.pod_owner`, `tag`, `systemd.t.BOOT_ID`, `systemd.t.CAP_EFFECTIVE`, `systemd.t.SELINUX_CONTEXT`, `systemd.t.STREAM_ID`, `systemd.t.SYSTEMD_CGROUP`, `systemd.t.SYSTEMD_INVOCATION_ID`, `systemd.t.SYSTEMD_SLICE`, `systemd.t.TRANSPORT`, `systemd.u.SYSLOG_FACILITY`, `default.ip_address`, `default.gateway_ip`, `default.mac_address`, `default.role`, `routedst.dest` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- Adjusted positions of grok pattern so that specific grok can be prioritized over generic grok.   
2025-08-13 |  Enhancement:  
\- Modified Grok pattern to extract observer_hostname.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped observer_hostname raw log field with event.idm.read_only_udm.observer.hostname UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped requestReceivedTimestamp raw log field with event.idm.read_only_udm.metadata.collected_timestamp UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped user.extra.authentication.kubernetes.io/pod-name, user.extra.authentication.kubernetes.io/pod-uid raw log field(s) with event.idm.read_only_udm.target.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped openshift.sequence raw log field with event.idm.read_only_udm.additional.fields UDM field.   
2025-06-17 |  Enhancement:  
\- event.idm.read_only_udm.observer.hostname: Newly mapped `app_name` raw log field to `event.idm.read_only_udm.observer.hostname` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `facility` raw log field to `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.observer.resource.name: Newly mapped `log_source` raw log field to `event.idm.read_only_udm.observer.resource.name` UDM Field.   
2025-03-03 |  Enhancement:  
\- Added support for a new log format.   
2024-12-12 |  Enhancement:  
\- Added support to handle JSON logs.   
2022-08-17 |  Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

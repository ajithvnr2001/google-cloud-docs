---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hashicorp-changelog/
title: Change log for HASHICORP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:27.149247+00:00
---

# Change log for HASHICORP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hashicorp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for HASHICORP

Date | Changes  
---|---  
2025-12-11 |  Enhancement:  
\- Added gsub function on `message` field to replace `message` field with `message_data`.  
\- Added grok pattern on `message_data` field.  
\- event.idm.read_only_udm.intermediary: Newly mapped `intermediary` field with `event.idm.read_only_udm.intermediary` UDM field.  
\- event.idm.read_only_udm.intermediary.application: Newly mapped `intermediary_application` field with `event.idm.read_only_udm.intermediary.application` UDM field.  
\- event.idm.read_only_udm.intermediary.user.userid: Newly mapped `intermediary_user` field with `event.idm.read_only_udm.intermediary.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `principal_user` with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `target_resource` field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `response.auth.metadata.username` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `appname` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.security_result.priority_details: Newly mapped `priority` raw log field with `event.idm.read_only_udm.security_result.priority_details` UDM field.  
\- event.idm.read_only_udm.observer.process.pid: Newly mapped `proc_id` raw log field with `event.idm.read_only_udm.observer.process.pid` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `security_result_action` field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `auth.policies`, `auth.token_policies` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `request.policy_override`, `response.data.admin_password`, `response.data.admin_token`, `response.data.admin_user`, `response.data.certificate`, `response.data.check_url`, `response.data.keystore`, `response.data.keystore_password`, `response.data.private_key` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `type`, `auth.identity_policies`, `request.data`, `facility`, `task` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If `event.idm.read_only_udm.principal.user.userid` is `true` and task is `Password Fetched`, updated to `USER_RESOURCE_ACCESS`.  
\- event.idm.read_only_udm.metadata.event_type: If `event.idm.read_only_udm.principal.user.userid` is `true` and task is `Entry Created`, updated to `USER_RESOURCE_CREATION`.   
2025-01-23 |  Enhancement:  
\- Added support for JSON format logs.   
2025-01-22 |  Enhancement:  
\- Modified mapping for additional fields.   
2024-11-14 |  Enhancement:  
\- Mapped `jsonPayload.auth.policy_results.granting_policies.type`, `jsonPayload.auth.policy_results.granting_policies.name`, and `jsonPayload.auth.policy_results.granting_policies.namespace_id` to `additional.fields`.  
\- Mapped `jsonPayload.request.namespace.id` to `target.namespace`.   
2024-10-15 |  Enhancement:  
\- Added support to handle JSON logs.   
2024-08-28 |  Enhancement:  
\- Added a Grok pattern to retrieve `secretname`.  
\- Mapped `jsonPayload.cos.googleapis.com/container_id`, `jsonPayload.cos.googleapis.com/container_name`, `jsonPayload.cos.googleapis.com/stream` to `additional.fields`.  
\- Mapped `resource.labels.instance_id` to `principal.resource.product_object_id`.  
\- Mapped `principal.resource.attribute.cloud.availability_zone` to `resource.labels.zone`.  
\- Mapped `logName` to `security_result.category_details`.   
2023-10-26 |  Enhancement:  
\- Added a Grok pattern to handle SYSLOG+JSON logs.   
2023-09-22 |  Enhancement:  
\- Modified mapping for `request.remote_port` from `target.port` to `principal.port`.  
\- Modified mapping for `request.remote_address` from `target.ip` to `principal.ip`.  
\- Mapped `error` to `security_result.description`.  
\- Mapped `resource.labels.namespace_name` to `target.namespace`.  
\- Mapped `resource.labels.pod_name`, `resource.labels.container_name` to `additional.fields`.  
\- Mapped `resource.labels.project_id` to `target.cloud.project.name`.  
\- Mapped `resource.labels.location` to `target.location.name`.  
\- Mapped `insertId` to `metadata.product_log_id`.  
\- Mapped `labels.k8s-pod/app_kubernetes_io/instance`, `labels.k8s-pod/app_kubernetes_io/name`, `labels.k8s-pod/component`, `labels.k8s-pod/helm_sh/chart`, `labels.k8s-pod/controller-revision-hash`, `labels.k8s-pod/vault-initialized`, `labels.k8s-pod/vault-version`, `labels.k8s-pod/vault-sealed`, `labels.k8s-pod/vault-perf-standby`, and `labels.k8s-pod/vault-active` to `target.resource.attribute.labels`.  
\- Mapped `labels.compute.googleapis.com/resource_name` to `target.resource.name`.   
2023-04-26 |  Enhancement:  
\- Added a Grok pattern to handle syslog logs.  
\- Mapped `status` to `network.http.response_code`.  
\- Mapped `runner` to `principal.user.userid`  
\- Mapped `job_id`, `job_status` to `additional.fields`.   
2023-03-24 |  Enhancement:  
\- Mapped `host` to `observer.hostname`.  
\- Mapped `cluster` to `observer.resource.name`.  
\- If log contains cluster, then mapped `cluster` to `observer.resource.resource_type`.  
\- Added JSON block to retrieve data from `_raw` field.  
\- `httpStatus` mapped to `network.http.response_code`.  
\- `httpUrl` mapped to `target.url`.  
\- `pid` mapped to `target.process.pid`.  
\- `msg` mapped to `metadata.description`.  
\- `url` mapped to `principal.url`.  
\- `hostname` mapped to `observer.hostname`.  
\- `streamingID`, `requestId`, `httpHeaders.cf-cache-status`, `httpHeaders.cf-ray`, `httpHeaders.gitlab-lb`, `httpHeaders.gitlab-sv`, `httpHeaders.x-request-id`, `httpHeaders.x-content-type-options`, `httpHeaders.x-frame-options`, `httpHeaders.ratelimit-limit`, `httpHeaders.ratelimit-observed`, `httpHeaders.ratelimit-remaining`, `httpHeaders.ratelimit-reset`, `httpHeaders.ratelimit-resettime`, `httpHeaders.server`, `httpHeaders.referrer-policy` mapped to `target.resource.attribute.labels`.  
\- `method` mapped to `network.application_protocol`.  
\- `headers.user-agent` mapped to `network.http.parsed_user_agent`.  
\- `httpHeaders.cache-control` mapped to `additional.fields`.  
\- `httpHeaders.content-type`, `httpHeaders.content-length`, `maskedToken`, `headers.accept` mapped to `security_result.about.resource.attribute.labels`.  
\- `headers.x-real-ip` mapped to `principal.ip`.  
\- `headers.x-forwarded-host` mapped to `principal.hostname`.  
\- `headers.x-forwarded-port` mapped to `principal.port`.  
\- `headers.snyk-acting-org-public-id`, `headers.snyk-flow-name`, `headers.snyk-request-id` mapped to `principal.resource.attribute.labels`.   
2023-02-09 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

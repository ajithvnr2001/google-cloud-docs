---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/falco-ids-changelog/
title: Change log for FALCO_IDS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:44.517196+00:00
---

# Change log for FALCO_IDS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/falco-ids-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FALCO_IDS

Date | Changes  
---|---  
2024-03-06 |  Bug-Fix:  
\- Changed the name of the label for `output_fields.tags` from `tags` to `tags_label`.   
2023-05-23 |  Extracted and mapped `host-IP` and `host-name` field from `output` field.  
Changed event_type from `GENERIC_EVENT` to related `metadata.event_type` wherever possible.   
2022-08-26 |  Mapped `priority` to `resource.attribute.labels` and key is priority.  
Added Condition to check whether output_fields.email is in the form of email or not before mapping it to target.email.   
2022-08-01 |  Mapped `output` to `metadata.description`  
Mapped `priority` to `security_result.priority` and `security_result.severity`  
Mapped `rule` to `security_result.rule_name`  
Mapped `time` to `date`  
Mapped `output_fields.bl-ssr` to `target.resource.name`  
Mapped `output_fields.cloud-project-id` to `observer.cloud.project.id`  
Mapped `output_fields.cloud-provider` to `target.resource.attribute.cloud.environment`  
Mapped `output_fields.container.id` to `target.asset.asset_id`  
Mapped `output_fields.container.image.repository` to `target.file.full_path`  
Mapped `output_fields.email` to `target.email`  
Mapped `output_fields.evt.arg.fd` to `resource.attribute.labels` and key is `evt_arg_fd`  
Mapped `output_fields.evt.arg.filename` to `resource.attribute.labels` and `evt_arg_filename`  
Mapped `output_fields.evt.arg.mode` to `resource.attribute.labels` and `evt_arg_mode`  
Mapped `output_fields.fd.name` to `resource.attribute.labels` and `fd_name`  
Mapped `output_fields.host-ip` to `target.ip`  
Mapped `output_fields.host-name` to `target.hostname`  
Mapped `output_fields.k8s.ns.name` to `additional.fields` and key is `k8s_ns_name`  
Mapped `output_fields.k8s.pod.name` to `additional.fields` and key is `k8s_pod_name`  
Mapped `output_fields.ol-env` to `resource.attribute.labels` and key is `ol-env`  
Mapped `output_fields.pod-ip` to `observer.ip`  
Mapped `output_fields.pod-name` to `observer.hostname`  
Mapped `output_fields.proc.cmdline` to `target.resource.attribute.labels` and key is `proc_cmdline`  
Mapped `output_fields.user.loginuid` to `target.user.userid`  
Mapped `output_fields.user.name` to `principal.user.user_display_name`  
Mapped `output_fields.ebpf_enabled` to `target.resource.attribute.labels` and key is `ebpf_enabled`  
Mapped `output_fields.falco.contact` to `principal.user.email_addresses`  
Mapped `output_fields.falco.host.ip` to `principal.ip`  
Mapped `output_fields.falco.host.name` to `principal.hostname`  
Mapped `output_fields.falco.pod.ip` to `observer.ip`  
Mapped `output_fields.falco.pod.name` to `observer.hostname`  
Mapped `output_fields.falco.ssrid` to `resource.product_object_id`  
Mapped `output_fields.tags` to `target.labels` and key is `tags`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

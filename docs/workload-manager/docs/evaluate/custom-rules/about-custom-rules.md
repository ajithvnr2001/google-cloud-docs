---
url: https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/about-custom-rules/
title: About custom rules in Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:05.003731+00:00
---

# About custom rules in Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/about-custom-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  About custom rules in Workload Manager Stay organized with collections  Save and categorize content based on your preferences. 

Workload Manager supports using customized rules that help you validate your workloads against best practices recommended by your organization.

For example, to ensure that the virtual machines (VMs) in your deployment don't use the Compute Engine default service account, you can create a custom rule. After you create the rule, create and run an evaluation in Workload Manager to validate your workloads against the rule. You can then review the evaluation results and take remediation steps for any violation of these rules. This helps improve the quality, reliability, and performance of your deployments.

## How it works

To evaluate workloads using custom rules, do the following:

  1. Identify the best practices relevant to your deployments from [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework).
  2. [Create custom rules using Rego](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/rego-custom-rules).
  3. [Create and schedule evaluations for your workloads](https://docs.cloud.google.com/workload-manager/docs/create-evaluation).
  4. Optional: Export evaluation results to BigQuery and set up notifications.



The following figure summarizes the process of using custom rules in Workload Manager:

![How custom rules work in Workload Manager](https://docs.cloud.google.com/static/workload-manager/docs/evaluate/images/wlm-custom-rules.png)

## Limitations

The following limitations apply to custom rules in Workload Manager:

  * You can include a maximum of 300 rules per evaluation in Workload Manager. More number of rules can slow down the evaluation process. We recommend that you split your rules across multiple evaluations.
  * Workload Manager does not support exporting evaluation results to multi-regional BigQuery datasets. You can export evaluation results to regional BigQuery datasets.



## Supported data sources

Workload Manager uses data from the following services to scan the resources that you specified for evaluation:

  * Cloud Asset Inventory: For a complete list of supported resource types in Cloud Asset Inventory, see [Supported asset types](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types)
  * Cloud Monitoring metrics. See Supported metrics for Compute Engine.



### Supported metrics for Compute Engine

The following table lists the metrics supported for Compute Engine. For more information about these metrics, see [Cloud Monitoring metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute).

The "Metric type" strings in this table must be prefixed with `compute.googleapis.com`. That prefix has been omitted from the entries in the table.

Display name  
`(Metric type)` | Description  
Labels | ASSET_TYPE  
(rule metadata)  
---|---|---  
**CPU utilization**   
`instance/cpu/utilization` | Fractional utilization of allocated CPU on a VM instance.   
`instance_name`: The name of the VM instance. | `Instance_CPUUtil_Last1H`   
`Instance_CPUUtil_Last6H`   
`Instance_CPUUtil_Last12H`   
`Instance_CPUUtil_Last1D`  
**Disk average latency**   
`instance/disk/average_io_latency` | Disk's average io latency in the last 60s.   
`device_name`: The name of the disk device.   
`storage_type`: Storage type, one of [pd-standard, pd-balanced, pd-ssd, pd-extreme, hyperdisk-extreme, hyperdisk-throughput]. | `Instance_DiskIO_Last1H`   
`Instance_DiskIO_Last6H`   
`Instance_DiskIO_Last12H`   
`Instance_DiskIO_Last1D`  
**VM Memory Used**   
`instance/memory/balloon/ram_used` | Memory currently used in the VM.   
`instance_name`: The name of the VM instance. | `Instance_MemoryUtil_Last1H`   
`Instance_MemoryUtil_Last6H`   
`Instance_MemoryUtil_Last12H`   
`Instance_MemoryUtil_Last1D`  
  
## Pricing

For pricing information, see [Workload Manager Pricing](https://cloud.google.com/workload-manager/pricing).

## What's next

  * [Write custom rules using Rego](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/rego-custom-rules)
  * [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/create-evaluation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

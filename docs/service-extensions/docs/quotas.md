---
url: https://docs.cloud.google.com/service-extensions/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:23.294154+00:00
---

# Quotas and limits  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Resources ](https://docs.cloud.google.com/service-extensions/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Service Extensions.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



## Quotas

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

The following quotas apply to Service Extensions. They can be increased on request.

Quotas |  | Value  
---|---|---  
Number of global authorization extensions in a project  |  | 10  
Number of global edge extensions in a project  |  | 100  
Number of global route extensions in a project  |  | 100  
Number of global traffic extensions in a project  |  | 100  
Number of authorization extensions per region in a project  |  | 10  
Number of route extensions per region in a project  |  | 100  
Number of traffic extensions per region in a project  |  | 100  
Number of plugins per project per location |  | 100  
Cloud Load Balancing only: Number of plugins attached to Application Load Balancers through edge extensions per project |  | 5 at any given point in time  
Cloud Load Balancing only: Number of plugins attached to Application Load Balancers through route extensions per project, per location, and per load balancing scheme |  | 5 at any given point in time  
Cloud Load Balancing only: Number of plugins attached to Application Load Balancers through traffic extensions per project, per location, and per load balancing scheme |  | 5 at any given point in time  
Media CDN only: Number of plugin resources attached to Media CDN services through `WasmAction` resources per project |  | 5 at any given point in time  
  
## Limits

The following sections describe the resource, configuration, and execution limits that apply to Service Extensions.

### Resource and configuration limits

There are also _system limits_ on Service Extensions resources. System limits can't be changed. 

Service Extensions enforces the following resource and configuration limits:

Limit |  | Value  
---|---|---  
Number of extension chains per attachment point  |  | 5  
Number of plugins in an edge extension chain  |  | 1  
Number of plugins or callouts in a route extension chain  |  | 1  
Number of plugins or callouts in a traffic extension chain  |  | 3  
Size of a compiled plugin along with the plugin configuration data  |  | 5 MiB  
Size of the plugin [configuration data](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#config-file) when provided directly (by using file upload in the Google Cloud console, the `--plugin-config` or `--plugin-config-file` option with the Cloud SDK, or the `WasmPluginVersion.plugin_config_data` field with the REST API) and not by using Artifact Registry  |  | 900 KiB  
Number of versions per plugin |  | 100  
  
### Plugin usage and execution limits

Service Extensions enforces the following plugin usage and execution limits:

Usage limit |  | Value  
---|---|---  
Execution duration per request The duration is the sum of the durations of all Proxy-Wasm callbacks associated with the request. Plugins that exceed the limit are terminated, which causes the associated request to return an HTTP `500` status code. |  | 1 msec  
CPU used per request Maximum [normalized vCPU](https://docs.cloud.google.com/service-extensions/docs/plugins-overview#resource-limitations) used per plugin invocation. Plugins that exceed this limit are terminated, which causes the associated request to return an HTTP `500` status code. |  | 1 msec  
Memory used by a plugin Maximum [allocated memory](https://docs.cloud.google.com/service-extensions/docs/plugins-overview#resource-limitations) held by a plugin instance. Plugins that exceed this limit are terminated, which causes the associated request to return an HTTP `500` status code. |  | 16 MiB  
Size of the log content emitted by a plugin per invocation When the limit is exceeded, further logs are dropped. |  | 16 KiB  
Number of log entries emitted by a plugin per invocation When the limit is exceeded, further logs are dropped. |  | 16  
Queries per second (QPS) per region for plugins If you plan to exceed this limit, then [contact support](https://cloud.google.com/support-hub/). |  | 100k  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

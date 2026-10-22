---
url: https://docs.cloud.google.com/build/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:54.155061+00:00
---

# Quotas and limits  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Resources ](https://docs.cloud.google.com/build/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Cloud Build.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

There are also _system limits_ on Cloud Build resources. System limits can't be changed. 

## Quotas

Cloud Build enforces quotas on running builds for various reasons. For example, quotas help to protect the community of Google Cloud users by preventing unforeseen spikes in usage.

Google Cloud also offers [free trial quotas](https://cloud.google.com/free/docs/free-trial-quotas) that provide limited access for projects to help you explore Google Cloud on a free trial basis. 

By default, the following Cloud Build quotas apply to each Google Cloud project. However, per-project quotas depend on usage and may vary over time.

Worker pool | Resource | Description | Default Limit | Can be increased | Scope  
---|---|---|---|---|---  
Private pool | C3 CPU | Number of concurrent C3 CPUs | 0* \- 300 | Yes. When this quota is filled, requests for additional CPUs are queued and processed serially. | Per region  
Private pool | E2 CPU | Number of concurrent E2 CPUs | 0* \- 2400 | Yes. When this quota is filled, requests for additional CPUs are queued and processed serially. | Per region  
Private pool | N2D CPU | Number of concurrent N2D CPUs | 0* \- 2400 | Yes. When this quota is filled, requests for additional CPUs are queued and processed serially. | Per region  
Default pool | E2 CPU | Number of concurrent E2 CPUs | 5 - 100 | No. If you require more than 100 concurrent CPUs, then use [private pools](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools). | Per region  
Default pool | Build | Number of concurrent builds | 10 - 30 | No. If you want to run more than 30 concurrent builds, then consider moving to a different region. | Global region  
  
* Depending on your project and usage, you may not have quotas to use [private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview). If this is the case, you can use [default pools](https://docs.cloud.google.com/build/docs/build-push-docker-image).

### API rate limits

API rate limits affect the rate at which you can call the Cloud Build API. You can view and edit the API rate limits by going to the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page.

## Resource limits

Cloud Build enforces the following limits on resources:

Limits |   
---|---  
[`args`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#buildstep) values per build step | 100  
[Build steps](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#buildstep) per build | 300  
Built [images](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#builtimage) per build | 700  
[`env`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#buildstep) values per build step | 100  
Length of the `arg` value | 10000 characters  
Length of the build step [name](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#buildstep) | 1000 characters  
Length of the [`dir`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#buildstep) value | 1000 characters  
Length of the `env` value | 65536 characters  
Length of the [list of tags](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#resource:-build) per build | 64  
Number of [artifact paths](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#Build.ArtifactObjects) per build | 100  
Number of [build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers) | 600  
Number of parameters for a [substitution](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_user-defined_substitutions) | 200  
Size of a [`secret`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#Build.Secret) | 65536 characters  
Unique [`secretEnv`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#secret) values per build | 100  
  
## Increasing quota

  1. Open the **Cloud Build Quotas** page.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?service=cloudbuild.googleapis.com)

  2. Select the quota(s) you want to modify and click **Edit quotas**.

  3. Enter the new quota limit for the quota you selected.

  4. Click **Submit request**.


**Important:** Don't change the `build_origin` value from `default` unless you've been provided a different value by another Google Cloud document or Google Cloud support.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

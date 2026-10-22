---
url: https://docs.cloud.google.com/artifact-registry/quotas/
title: Quotas and limits \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:43.049094+00:00
---

# Quotas and limits  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Resources ](https://docs.cloud.google.com/artifact-registry/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Artifact Registry.

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

There are also _system limits_ on Artifact Registry resources. System limits can't be changed. 

Artifact Registry limits the maximum rate of incoming requests and enforces quotas on a per-project and per-user basis.

For more information about quota policies, viewing your quotas, and managing your quotas, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/overview).

Go to the [API dashboard](https://console.cloud.google.com/apis/dashboard) for your current API activity.

## Quotas

Artifact Registry enforces the following quotas.

### Per-project request quota

Quota | Value | Additional information  
---|---|---  
Requests per minute in each region or multi-region | 60,000 |   
Write requests per minute in each region or multi-region | 18,000 | In most cases, a single HTTP request or API call counts as a single request. However, some operations count as multiple requests. For example, a batch request like `ImportAptArtifacts` might charge quota for each item in the batch. A Docker pull or push usually makes multiple HTTP requests, so quota is charged for each request.  
Delete requests per minute in each region or multi-region | 18,000 | Deletions requested by [cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy) count towards the delete requests quota and deletions per day, per repository limit.  
  
### Per-user request quota

By default, projects have unlimited per-user quotas. You can optionally [cap](https://docs.cloud.google.com/docs/quotas/view-manage#capping_usage) these per-user quotas within a project. A per-user quota applies per authenticated user or per client IP address for unauthenticated requests to a public repository.

### Cloud KMS quotas and Artifact Registry

When you use CMEK in Artifact Registry, your projects can consume Cloud KMS cryptographic requests quotas. For example, CMEK-encrypted repositories can consume these quotas for each upload or download. Encryption and decryption operations using CMEK keys affect Cloud KMS quotas only if you use hardware (Cloud HSM) or external (Cloud EKM) keys. Confirm that you have enough quota to enable application-layer secrets encryption for your applications and workflows. For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).

## Artifact Analysis quotas

See [Artifact Analysis quotas and limits](https://docs.cloud.google.com/artifact-analysis/quotas) for information on scanning usage policies.

## Public upstream quotas

If you use remote repositories to cache public upstream repositories, you might be subject to the upstream repositories' read and write quotas.

## Usage Limits

Artifact Registry enforces the following usage limits.

Usage limit | Value  
---|---  
Cleanup policy deletions per repository, per day | 300,000  
Cleanup policies per repository | 10  
Max data retrieval from upstream of remote repository per request | 9.9 GB  
Max upstream policies for virtual repositories | 30  
Max number of total upstream resolutions per request for virtual repositories | 250  
Max number of remote repository upstream resolutions per request for virtual repositories | 30  
Repository creation and deletion operations, per region, per minute | 30  
Note: Deletions requested by cleanup policies count towards the deletions limit as well as the delete request quota. 

### Remote Repository Limits

When you request an artifact from your remote repository, and the artifact hasn't already been cached in your remote, the artifact is requested from the upstream repository, and then stored in your remote repository. Requests to upstream hosts count against your organization's upstream host read request limit, and caching the artifact in your remote repository uses your project's write and request quotas. Once the artifact has been cached to your remote, requests for that artifact only count against your project's request quota.

Artifact Registry enforces the following usage limits for remote repositories.

Limit | Public upstream | Value  
---|---|---  
Public upstream host reads per organization, per region, per minute | Default | 600  
Docker Hub | 600  
proxy.golang.org | 600  
Maven Central | 3000  
NpmJS | 1800  
PyPI | 1200  
Go Module Proxy | 10000  
  
### Limit for listing artifacts in a repository

Format-specific API requests to all formats are limited to 10,000. For example, the Docker Registry API method to [list container images](https://docs.docker.com/registry/spec/api/#listing-image-tags) returns an incomplete list if a repository has more than 10,000 images or tags.

The limitation does not apply to the [gcloud artifacts docker images list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list) command or Artifact Registry API requests.

## Request a quota increase

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

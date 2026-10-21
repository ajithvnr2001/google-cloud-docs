---
url: https://docs.cloud.google.com/infrastructure-manager/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:45:46.724904+00:00
---

# Quotas and limits  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/infrastructure-manager/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Infrastructure Manager.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Infra Manager is subject to the [Cloud Build quotas and limits](https://docs.cloud.google.com/build/quotas) and to the [Cloud Storage quotas and limits](https://docs.cloud.google.com/storage/quotas). 

For information about quota validation for resources provisioned using Infra Manager, see quota validation of provisioned resources.

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Infra Manager resources. System limits can't be changed. 

## Allocation quotas

The following quotas don't reset over time and instead are released when you release the resource:

Quotas | Value  
---|---  
Deployments per project per location (region or multi-region) | 1,000  
Previews per project per location (region or multi-region) | 1,000  
**Note:** Multi-regional locations (such as `us`) have their own separate quota allocations distinct from individual regions.

## Rate quotas

The following quotas apply to Infra Manager requests:

Quota | Value  
---|---  
Mutating requests per minute per project per location (region or multi-region) | 20  
Number of API requests per minute per project per location (region or multi-region) | 1,200  
  
## Usage limits

Infra Manager enforces the following usage limits:

Usage limit | Value  
---|---  
Number of Terraform input variables | 150  
Number of resources returned when listing resources | 500  
Length of identifiers in characters | 40  
Size of the API payload in bytes | 950,000  
Number of the historical revisions | 100  
**Caution:** The API payload limit is inclusive of metadata associated with your API payload. To avoid exceeding your API payload limits, ensure that the size of your payload is less than 950,000 bytes.

## Request a quota increase

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

## Quota validation of provisioned resources

Infra Manager provisions Google Cloud resources. These resources have their own quotas and limitations. For example, Virtual Private Cloud has its own [quotas and limitations](https://docs.cloud.google.com/vpc/docs/quota).

You can enable quota validation when using Infra Manager to create or update a deployment to ensure that the infrastructure outlined using your Terraform configuration doesn't exceed your quota values.

Infra Manager uses the `quota-validation` flag to determine whether to validate the resources outlined in your Terraform configuration as part of the `gcloud infra-manager deployments apply` command. When the `quota-validation` flag is in use, Infra Manager either logs when a deployment exceeds quota values (`ENABLED`), or prevents the deployment altogether (`ENFORCED`).

Infra Manager quota values are assessed for only the following Google Cloud resource types:

  * `google_compute_network`
  * `google_compute_disk`
  * `google_compute_instance`



For more information about how to use quota validation with Infra Manager, see [deploy resources](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources), or [update a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment).

## Cloud Build quotas and limits implications

Infra Manager uses Cloud Build to create and update deployments. As part of the deployment and update process, Infra Manager checks the status of the deployments using Cloud Build approximately 12 times per minute.

Cloud Build API rate limits affect the rate at which you can call the Cloud Build API. If you are running several deployments concurrently (for example, across multiple regions or environments), check the Cloud Build API rate limits for your organization to ensure that the number of your Cloud Build operation requests are within your API rate limits. You can view and edit your API rate limits by going to the [Quotas](https://console.cloud.google.com/iam-admin/quotas?service=cloudbuild.googleapis.com) console page.

**Caution:** You may experience deployment errors if the number of deployments you are running concurrently exceeds the API rate limits for your organization. To workaround Infra Manager deployment errors with your API rate limits, you should serialize your deployments or logically separate deployments into separate projects.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

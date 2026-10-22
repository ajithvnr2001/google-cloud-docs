---
url: https://docs.cloud.google.com/docs/quotas/terminology/
title: Quota and system limit terminology \u00a0|\u00a0 Cloud Quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:02.386442+00:00
---

# Quota and system limit terminology  |  Cloud Quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/terminology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Guides ](https://docs.cloud.google.com/docs/quotas/overview)



Send feedback 

#  Quota and system limit terminology Stay organized with collections  Save and categorize content based on your preferences. 

Quotas and system limits restrict your use of Google Cloud resources to support resource availability for all Google Cloud users. Quotas have default values, and can typically be adjusted. System limits are fixed values that cannot be changed. 

The following table lists additional quota terminology and definitions.

Term | Description  
---|---  
Dimension | A dimension is an attribute that represents a region or a zone, or a service-specific dimension, such as `gpu_family` or `network_id`. The Cloud Quotas API represents dimensions as key-value pairs, where the key is the dimension name, and the value is the value of the named dimension—for example, {"`key" : "region", "value" : "us-central1`"}.  
Quota | Usually, _quota_ refers to a Google Cloud resource and its unit of measurement. For example, the quota `CPUS-PER-VM-FAMILY-per-project-region` defines the number of Compute Engine virtual CPUs (vCPUs) available to your project for a specific VM family in a particular region. Occasionally, Google Cloud documentation uses the word _quota_ in its more general sense, meaning a limited allowance.  
Quota adjustment | A request to increase or decrease a quota value. Quota adjustment requests are subject to review by Google Cloud.   
Quota adjuster settings ([Preview](https://cloud.google.com/products#product-launch-stages)) |  This resource represents your quota adjuster settings for a particular project. When enabled, the quota adjuster monitors your usage for the specified resources and issues quota adjustment requests when resource usage approaches its quota value.  
Quota info | `QuotaInfo` is a read-only resource that provides metadata and quota value information about a particular quota for a given project, folder or organization. The `QuotaInfo` resource contains:
* Metadata such as name and dimension.
* Quota values for different quota dimensions.
Cloud Quotas obtains information from the quotas defined by Google Cloud services and any fulfilled quota adjustments that you initiate. **Note** : Because `QuotaInfo` is constructed by incorporating information from different sources, a default quota configuration exists even if you have not created a `QuotaPreference` resource. Until you express a preferred state through `quotaPreference.create` or `quotaPreference.update`, `QuotaInfo` relies on the default quota information available to determine what quota value to enforce.  
Quota preference | A `QuotaPreference` resource represents your quota preferences for a particular dimension combination. You can use this resource to make quota adjustments requests and specify behavior for adjustment requests. You can set quota preferences by using the Google Cloud console, the Cloud Quotas API, or the Google Cloud CLI.  
Quota value | The maximum for a given quota. This value can be adjusted for most quotas.  
System limit | A fixed value; typically, an architectural constraint. System limits cannot be adjusted.  
  
## What's next

  * [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview)
  * [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage)
  * [Cloud Quotas API overview](https://docs.cloud.google.com/docs/quotas/api-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/compute/docs/instances/idle-vm-recommendations-overview/
title: Idle VM recommendations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:35.803339+00:00
---

# Idle VM recommendations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/idle-vm-recommendations-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Idle VM recommendations Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine provides idle VM recommendations to help you identify virtual machine (VM) instances that have not been used over the previous 1 to 14 days. You can use idle VM recommendations to find and stop idle VM instances to reduce wasting resources and reduce your compute bill.

Compute Engine generates recommendations automatically based on system metrics gathered by the Cloud Monitoring service. You can configure idle VM recommendations to receive more or fewer recommendations.

This page provides conceptual information on how Compute Engine generates idle VM recommendations and on the parameters you can use to configure them.

  * For more information on how to identify idle VMs and take action, see [View and apply idle VM recommendations](https://docs.cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations).
  * For more information on how to configure idle VM recommendations, see [Configure idle VM recommendations](https://docs.cloud.google.com/compute/docs/instances/configuring-idle-vm-recommendations).



## Pricing

Idle VM recommendations are available free of charge. Using recommendations to reduce your resource usage can result in cost savings.

## Limitations

For standalone VMs, idle VM recommendations are not available in following cases:

  * Instances with local SSDs
  * Instances with GPU/TPUs
  * App Engine flex resources
  * Dataflow resources
  * Google Kubernetes Engine resources



## How detection of idle VM instances works

Compute Engine generates recommendations about idle VM instances based on historical usage metrics. By default, the historical observation period is 14 days, or, for new VMs, starting one day after VM creation. By changing the default observation period, you can customize the recommendations that you receive.

To generate recommendations, the algorithm considers the CPU and network usage in the last observation period. If CPU and network usage are below predefined thresholds, the Recommender classifies the VM as idle.

**Note:** Google designs the default thresholds so that if monitoring agents generate the majority of CPU and network usage, then your VM is classified as idle. The default threshold values that are currently used to classify a VM as idle might change in the future.

### Frequency of recommendations

After a VM is created and running for at least one day during the observation period, Compute Engine begins generating idle VM recommendations for it. New recommendations are generated once per day.

### Relation with machine type sizing recommendations

[Machine type sizing recommendations](https://docs.cloud.google.com/compute/docs/instances/apply-sizing-recommendations-for-instances) recommend the optimal size for a VM. You might receive a machine type recommendation to downsize an idle VM.

If you must keep an idle VM running despite its low utilization, you can use machine type recommendations to help you choose the optimal size for underutilized VMs.

## Customize recommendations

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Compute Engine lets you customize the recommendations you receive for your project by changing the configuration used by the recommendation algorithm. In particular, by changing the default observation period, you can receive recommendations that better fit your workloads, applications, and infrastructure needs.

To learn how to modify the configuration for your project, see [Configure idle VM recommendations](https://docs.cloud.google.com/compute/docs/instances/configuring-idle-vm-recommendations).

## Choose the right configuration

This section describes the values that you can set for the configuration. Changing these values affects the recommendations that you receive.

### The observation period

Set the observation period to modify the duration of the window used to calculate the recommendations.

You can set the observation period to a value between 1 day and 14 days, using a string with the total number of seconds, followed by the letter `s`.

  * For an observation period of 1 day, use `"86400s"`.
  * For an observation period of 14 days, use `"1209600s"`.



By default, the observation period is 14 days.

  * Use a shorter observation period if you want to receive recommendations based on short-term changes in your workload.
  * Use a longer observation period if you want to receive recommendations that are not affected by short-term fluctuations in your workload.



## What's next

  * Learn how to [view and apply idle VM recommendations](https://docs.cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations).
  * Learn how to [configure idle VM recommendations](https://docs.cloud.google.com/compute/docs/instances/configuring-idle-vm-recommendations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

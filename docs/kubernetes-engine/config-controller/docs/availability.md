---
url: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/availability/
title: Configure Config Controller for high-availability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:08.607153+00:00
---

# Configure Config Controller for high-availability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Controller ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/overview)



Send feedback 

#  Configure Config Controller for high-availability Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how best to use Config Controller when operating highly-available services or managing resources in multiple Google Cloud regions.

This page is for Admins and architects and Operators who manage the lifecycle of the underlying tech infrastructure and plan capacity and infrastructure needs. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Config Controller runs in a single region, so it can tolerate the failure of an availability zone, but if an entire region fails, Config Controller loses availability. There are two different strategies to deal with regional failure, and your choice depends on what you would do if a region fails:

  * If you would make configuration changes in response to a regional failure, create a second Config Controller instance.

  * If you would not make configuration changes, use a single Config Controller instance.


**Note:** While planning for failure is important, [regions offer sufficient availability for many applications](https://docs.cloud.google.com/compute/docs/regions-zones).

## Understand failure scenarios

Config Controller uses a [regional GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters). Although the regional cluster can tolerate the failure of a single zone in a region, the cluster becomes unavailable if multiple zones in the region fail.

If your Config Controller instance fails, your existing Google Cloud resources remain in their current state. However, even if your applications are still running, you cannot change their configuration when Config Controller is unavailable. This applies to resources in the same region and to resources in other regions that you are managing from the Config Controller in the unavailable region.

Because you can't reconfigure resources in the same region, if a regional failure _does_ affect existing Google Cloud resources in the Config Controller region, you cannot repair those resources.

Because you also can't reconfigure resources in other regions, a failure in one region has now affected your ability to make changes in another region.

Other failure scenarios are also possible. For example, if you configure Config Sync to pull from an external Git provider, you should consider the failure modes of that Git provider. You might not be able to make configuration changes because you cannot push changes to that Git provider. Or if Config Sync cannot read from Git, then any Git changes aren't applied to the cluster, and so Config Connector does not apply them. However, regional failure is often the most important failure scenario, because other failure scenarios are typically uncorrelated with Config Controller failure.

## Use a single cluster for regional availability

In many scenarios, you would not perform any reconfiguration if a region fails. In that case, you might choose to accept that a regional failure causes your configuration control-plane to become unavailable.

For example, if you only operate in a single region, there might not be any useful reconfiguration you can do if that region fails. Similarly, if you have a single point of failure database in a single region, you might not be able to recover until that region recovers. For applications that do not need the absolute highest availability, this situation can be a reasonable trade-off against cost and complexity.

Locating the Config Controller instance in the same region gives you a shared fate: Config Controller is available as long as your primary region is available. Locating the Config Controller instance in a _different_ region can also be a good choice; although you now have to think about potential failures in two regions, you avoid the correlated-failure of your configuration control-plane with the failure of your primary region.

Alternatively, if you have a multi-regional redundant configuration, your system might automatically steer away from failed regions. Here too, you might not want to do reconfiguration if a region fails. In this case, you might choose a single Config Controller instance.

## Manually failover to a second Config Controller instance

You might want to do some reconfiguration if a region fails so that you can remedy the failure. You might also want to continue configuring resources in other regions, even if your Config Controller instance is located in a failed region. In this case, we recommend using a second Config Controller instance in a second region.

Though it is not recommended, two Config Controller instances can run with identical configurations. Both instances race to read from the same Git repository and apply the same changes to Google Cloud. However, numerous edge-cases make this configuration unreliable. The two Config Controller instances observe the Git repository at slightly different times; they might attempt to apply slightly different versions of your Google Cloud configuration. Multiple active writers to Google Cloud make it more likely that you encounter quotas or rate limits. A small number of Config Connector resources are also [not idempotent](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#resources_with_restrictions_around_acquisition), and need extra care as discussed in the rest of this section. We therefore recommend against having two Config Controller clusters both actively reconciling.

We recommend instead that if the region running your Config Controller fails, then you run another Config Controller in a second region. The new Config Controller instance should be configured identically to the first one, reading from the same Git repository. Pre-preparing a script to bring up and configure your Config Controller instance might be useful in this scenario. When you create your new Config Controller instance, Config Sync reads and applies the desired state from Git to Kubernetes; Config Connector synchronizes the desired state to Google Cloud.

There are two things to be careful of in this situation:

  * If the first Config Controller cluster is still running, or starts running when the first region recovers, then it might attempt to apply the old state to Google Cloud. If you can stop the Config Controller cluster in the first region before starting a second Config Controller cluster, you can avoid this potential conflict.

  * Not all Config Connector resources can be seamlessly reapplied from Git. For the list of resources that need special care, see [resources with restrictions around acquisition](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#resources_with_restrictions_around_acquisition). In particular, we recommend being careful around `Folder` resources, and avoiding `IAMServiceAccountKey` resources (for example, using GKE Workload Identity Federation for GKE instead).


**Note:** If you need to reconfigure resources when a region fails, you should consider running Config Controller in a _different_ region from your primary Google Cloud services. This configuration helps you avoid a single regional failure affecting your Config Controller instance at the exact time you need it.

## One Config Controller instance per region

If you want to avoid a Config Controller instance in one region affecting another region, you might also consider running a Config Controller instance per region, where each Config Controller instance manages resources in that region.

This configuration is workable, but it isn't one of our recommended options for the following reasons:

  * Some resources span multiple regions (such as Cloud DNS), which makes this strategy limited.

  * Generally, having a Config Controller cluster in the same region encounters the correlated-failure problem: you want to reconfigure resources exactly when a regional failure affects the Config Controller in that region.

  * You have to split up your Config Connector resources by region.

  * Config Controller is not currently available in all regions.




## Directly configuring Google Cloud resources

In exceptional circumstances, you might make changes directly to the underlying Google Cloud resources, without going through Git or Config Connector. Config Connector tries to remediate any "drift", so if your Config Controller instance is still running, Config Connector considers any changes you make manually to be "drift" and tries to revert them.

However, if you stop your Config Controller instance, or if the region is offline, this can be a useful stop-gap measure.

When your Config Controller instance recovers, Config Connector will likely try to revert your manual changes. To avoid this situation, you can make corresponding changes in Git for any changes you make manually.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

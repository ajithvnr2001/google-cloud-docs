---
url: https://docs.cloud.google.com/compute/docs/instance-groups/overview-add-vms-all-at-once-in-mig/
title: Overview of adding instances all at once in a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:08.533643+00:00
---

# Overview of adding instances all at once in a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/overview-add-vms-all-at-once-in-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Overview of adding instances all at once in a MIG Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the different methods that you can use to create all of the virtual machine (VM) instances that you require in a managed instance group (MIG) at the same time. By default, a MIG creates each instance individually. If you have specific workloads that requires all instances to be available before the job starts, then the individual instances creation can lead to partial provisioning. You can choose to create instances _all at once_ so that the MIG creates the requested number of instances only when the resources become available. This approach also helps you avoid charges for partial capacity.

You can use one of the following capabilities in a MIG to add instances all at once:

  * **Bulk mode** : You set the MIG's target size and the MIG creates those instances all at once when the capacity becomes available. In the bulk mode, the MIG stays at zero instances until it is able to obtain the full capacity.

  * **Resize requests** : You create a resize request in a MIG by specifying the number of instances that you need. The MIG creates the requested instances all at once and increases the target size by the number of instances created. You can create more than one resize request in a MIG.




The following sections help you to determine which method is suitable for your workload to create your instances all at once.

To learn about other ways to add or remove instances in your MIG, see [Add and remove VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig).

## Comparison of bulk mode and resize request

The following table outlines the differences between using bulk mode or creating a resize requests. In most cases, we recommend that you choose bulk mode, unless you need to manage multiple parallel requests to create instances all at once or resize a MIG that already contains instances.

Feature | Bulk mode | Resize request  
---|---|---  
**Workloads** | Suitable for workloads that require a specific number of instances. | Suitable for capacity pool orchestration that requires the ability to make multiple requests to create instances all at once.  
**Benefits** | 

  * Ease of use
  * Terraform compatible
  * Observability at MIG level

| Ability to make multiple independent requests to add instances to a MIG of any size.  
**All at once instance creation** | On MIG creation or when resizing an existing MIG from zero instances. | Only in an existing MIG of any size.  
**Configuration** | Set the target size mode to `BULK` and then set the target size to the required number of instances. | Create a resize request in which you specify the number of instances.  
**Concurrent requests** | Concurrent requests are not possible as you specify the number of instances by setting the target size. | Concurrent requests are possible by creating different resize requests in a MIG.  
**Observability** | View the bulk operation details in the MIG details. | View the details of a specific resize request or list all resize requests in a MIG.  
  
## What's next

  * [Learn more about bulk mode](https://docs.cloud.google.com/compute/docs/instance-groups/about-bulk-mode)
  * [Learn more about resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

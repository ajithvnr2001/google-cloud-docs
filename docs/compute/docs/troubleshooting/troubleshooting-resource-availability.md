---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability/
title: Troubleshooting resource availability errors \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:13.750624+00:00
---

# Troubleshooting resource availability errors  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting resource availability errors Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to resolve resource availability errors that might occur when you try to request new Compute Engine resources or create reservations of Compute Engine resources. Resource errors occur when you try to request resources in a zone that can't accommodate your request due to the current unavailability of a Compute Engine resource, such as GPUs or vCPUs.

Resource errors aren't related to your Compute Engine quota. These errors only apply to the resources that you specified in your request when you sent it; they don't apply to all resources in a zone.

## Common error messages

The following are examples of common resource errors that you might encounter when you request new Compute Engine resources or create new reservations:
    
    
    ZONE_RESOURCE_POOL_EXHAUSTED
    
    
    
    ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS
    
    
    
    The zone 'projects/PROJECT_ID/zones/ZONE' does not have enough resources available to fulfill the request.
    Try a different zone, or try again later.
    
    
    
    A VM_TYPE_AND_SIZE VM instance with RESOURCE_ATTACHMENT is currently unavailable in the ZONE zone.
    
    Capacity changes frequently, so try your request in a different zone, with a different VM hardware
    configuration, or at a later time. For more options, see troubleshooting documentation.
    
    
    
    A VM_TYPE_AND_SIZE VM instance with RESOURCE_ATTACHMENT is currently unavailable in the ZONE zone, because of  REASON.
    
    Consider trying your request in the ZONE zone(s), which currently has capacity to accommodate your request.
    
    If you cannot move your VM to ZONE, review the REASON failure resolution instructions available in troubleshooting documentation, then try your request again.
    If your workload can't accommodate the suggested resolution, try your request with a different VM hardware configuration or at a later time.
    

Some error messages include a `reason` field that details which specific resources Compute Engine couldn't provide. For more information, see the Resource error reasons and recommendations in this document.

## How to resolve resource errors

If the error message that you encountered includes a `reason` field, then, to see specific guidance to resolve the error, see Resource error reasons and recommendations in this document. Otherwise, the best approach for resolving a resource availability error involves trying one or more of the following. The following approaches are ordered from the least to the most disruptive for your workload.

  1. **Retry your request at a different time**. Resource availability can be transient, and you can resolve this error by requesting resources at a later time.

  2. **Retry your request in a different region or zone**. Try requesting resources in a different region or zone.

  3. **Use a different machine configuration**. You can change one or more of the following properties when you request resources:

     * Request a smaller number of compute instances.

     * Request a different machine series or machine type.

     * Request a different number of Local SSD disks or GPUs.

  4. **Use a different provisioning model**. If you can't create standard compute instances, then try creating Flex-start VMs or Spot VMs. Different provisioning models have different capacity pools and availability characteristics. For more information, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).




Additionally, if you're trying to create a regional managed instance group (MIG), you can try the following:

  * Configure instance flexibility so the MIG can automatically select from multiple compatible machine types based on real-time availability. For more information, see [About instance flexibility in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility).

  * Change the distribution shape of the MIG to `ANY`, `ANY_SINGLE_ZONE`, or `BALANCED`. For more information about distribution shapes, see [Regional MIG target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape).


**Tip:** To help prevent resource availability errors in the future, we recommend that you [reserve Compute Engine resources](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type) ahead of time. Reservations help ensure that resources are available when you need them. 

### Resource error reasons and recommendations

The following table provides information about the `reason` field present in some resource error messages, as well as recommendations about resolution strategies for each `reason`.

Error `reason` | Description | Recommendation  
---|---|---  
`resource_availability` | The type and size of compute instance that you requested is currently unavailable in the zone that you requested it in. | Try one of the following:

  * Request the compute instance in another zone.
  * If you get a resource availability error while requesting an `a3-highgpu-1g`, `a3-highgpu-2g`, or `a3-highgpu-4g` machine type, then ensure that you are provisioning the compute instance using one of [these supported methods](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-high-vms).

  
`cpu_availability` | A compute instance with the amount of CPU that you requested is currently unavailable in the zone that you requested it in. | Try one of the following:

  * If you're requesting a single compute instance, then request the compute instance in another zone.
  * If you're requesting multiple compute instances, then try one or more of the following:
    * Request the compute instances in another zone.
    * Divide the total amount of vCPU across smaller compute instances. For example, if you requested 80 compute instances with 224 vCPUs, try requesting 160 compute instances with 128 vCPUs each.

  
`memory_availability` | A compute instance with the amount of memory that you requested is currently unavailable in the zone that you requested it in. | Try one of the following:

  * If you're requesting a single compute instance, request the compute instance in another zone.
  * If you're requesting multiple compute instances, then try one or more of the following:
    * Request the compute instances in another zone.
    * Split your memory request into multiple compute instances. For example, if you requested three compute instances with 1.88 TB of memory each, divide the request into several compute instances that have a total combined memory of 1.88 TB.

  
`local_ssd_availability` | A compute instance with the amount of local SSD that you requested is currently unavailable in the zone that you requested it in. | Try one of the following:

  * If you're requesting a single compute instance, then request the compute instance in another zone.
  * If you're requesting multiple compute instances, then try one or more of the following:
    * Request the compute instances in another zone.
    * If your workload permits, then request a zonal or regional SSD persistent disk instead of local SSD.
    * Split your local SSD request into multiple compute instances. For example, if you requested one compute instance with 600 GB of local SSD, divide the request into several compute instances that have a total combined local SSD of 600 GB.

  
`gpu_availability` | A compute instance with the GPU that you requested is currently unavailable in the zone you requested it in. | Try requesting the compute instance in another zone.  
`configuration_availability` | A compute instance with the configuration that you requested isn't supported in the zone that you requested it in. | Retry your request in a zone that supports the machine type and configuration you require. To learn more about which machine types are supported in each region and zone, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). To learn more about the configurations that each machine type supports, see [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-types#machine_type_comparison).  
  
If you're unable to resolve the error by using any of the preceding resolution recommendations, then [contact support](https://docs.cloud.google.com/compute/docs/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

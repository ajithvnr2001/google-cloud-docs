---
url: https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation/
title: About bulk creation of VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:06.480280+00:00
---

# About bulk creation of VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About bulk creation of VMs Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Bulk creation of virtual machine (VM) instances lets you create a large number of VMs that are identical and independent from each other. When you create VMs in bulk, you can do the following:

  * **Minimize consumption of API rate limits.** Requests for creating VMs in bulk consume [API rate limits](https://docs.cloud.google.com/compute/docs/api-rate-limits) as if you were creating a single VM.

  * **Distribute VM creation across multiple zones in a region.** For regional requests, Compute Engine determines the zone to create the VMs in based on the zones that have available hardware, taking into consideration the available capacity in each zone, as well as any of your [reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).




Compute Engine doesn't manage VMs that you create in bulk. To create a group of managed VMs, use [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups).

## Creating VMs in bulk versus batching API requests

Creating VMs in bulk is different from [batching API requests](https://docs.cloud.google.com/compute/docs/api/how-tos/batch) with the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). The following table compares these two ways of creating multiple VMs:

Functionality | Batching API requests | Creating VMs in bulk  
---|---|---  
**Zone selection**  
Automatically selected based on considerations such as resource availability and quota  | Manual | Automatic when using the regional endpoint  
**Upfront validation**  
Request fails immediately if it is not feasible  | No | With capacity and quota  
**VM name generation**  
Automatically generated based on a specified name pattern  | Manual | Optionally generated automatically  
**Automatic rollback**  
Request automatically rolled back if Compute Engine cannot create the target number of VMs  | No | Optionally enabled  
**API rate limit**  
How requests affect the API rate limit  | One request for each VM | One request for each bulk operation  
  
## Limitations

The following list describes the limitations that apply when creating VMs in bulk:

  * **Customer supplied encryption keys.** You can't create VMs that have disks that are protected by customer-supplied encryption keys (CSEKs) ([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations)). The disks must use Google-owned and managed keys or customer-managed encryption keys.

  * **Boot disks from snapshots.** You can't use a snapshot to create the boot disks for the VMs. Instead, use [a custom image](https://docs.cloud.google.com/compute/docs/images/create-custom#create_image) when you create VMs in bulk.

  * **Global DNS.** If you are using global DNS, there might be name conflicts because the fully qualified domain name (FQDN) doesn't contain the zone. To avoid this, use zonal DNS. If you cannot switch to zonal DNS, avoid using the same name pattern across different regions. For more information, see [Types of internal DNS names](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names).

  * **Machine images.** You cannot create VMs from [machine images](https://docs.cloud.google.com/compute/docs/machine-images).

  * **Number of VMs.** You can create up to 5,000 VMs with each call. Also, you can create a maximum of 8,000 instances simultaneously at any time. This simultaneous operation limit is shared between [`instances.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) and [`instances.bulkInsert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert).

  * **Sole-tenant nodes.** You cannot create VMs that use [sole-tenant node affinity labels](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_affinity_and_anti-affinity).

  * **VM properties.** All [VM properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties), except their names and custom hostnames, must be identical. You cannot use VM properties that are mutually exclusive between VMs, which include but are not limited to static external IP addresses and static internal IP addresses.




## Audit logs

Compute Engine logs information about the bulk VM creation to the [Admin Activity audit log](https://docs.cloud.google.com/logging/docs/audit#admin-activity) when you make the API call and when the API call completes.

Compute Engine also creates separate audit logs for each VM. You can find the audit log for a single VM by matching the value of `protoPayload.resourceName` with the VM name generated by the naming pattern that you specify with the request.

## Pricing

There are no additional charges for using bulk VM creation. As with creating single VMs, billing begins when you create the VMs.

You are not billed for any VMs that Compute Engine fails to create.

## What's next

  * [Create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/vmware-engine/docs/best-practices-compute/
title: Compute best practices \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:22.870690+00:00
---

# Compute best practices  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/best-practices-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Compute best practices

This page presents compute best practices for Google Cloud VMware Engine.

## Select the best region for your application

To pick the best region for your applications, consider the following factors:

  * To minimize network latency and improve the customer experience, select a location that's closest to your users. The Google Cloud console provides a [real-time performance dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloud-latency) that can help you visualize the latency both between regions and between internet users and a Google Cloud region.
  * To maintain application performance, optimize the connectivity to on-premises facilities by selecting the closest Google Cloud region. For multicloud deployments, consider the proximity to the regions of other cloud vendors.
  * To ensure that your applications maintain compliance with regulations, such as [Payment Card Industry (PCI) compliance policies](https://www.pcicomplianceguide.org/faq/) or the [European General Data Protection Regulation (GDPR)](https://gdpr.eu/), select a region that supports those requirements.
  * Costs and pricing vary per region. Ensure that you account for these regional differences when planning your deployment.
  * When selecting a location, some SKUs might be available only in some regions and not in others.



## Decide when to choose a multi-region design

In the following situations, you might want to deploy to multiple VMware Engine private clouds across regions for the same workload or project scope:

  * Disaster recovery implementations that use [Site Recovery Manager (SRM)](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-srm) or [Zerto](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-zerto).
  * Applications that require global availability or low latency to their user base.
  * Capacity planning requirements that are region specific.



## Design for zone resilience

VMware Engine provides zone redundancy in specific regions. In these regions, for increased fault tolerance, you can also deploy private clouds as a [stretched cluster](https://docs.cloud.google.com/vmware-engine/docs/concepts-stretched-private-cloud). For information about these regions, see the [VMware Engine release notes](https://docs.cloud.google.com/vmware-engine/docs/release-notes).

When deployed as a stretch cluster, your private cloud has nodes in two independent zones. You must have an equal number of nodes in each zone to support this design. Such a design ensures application availability through zone resilience and [VMware vSphere High Availability](https://www.vmware.com/products/vsphere/high-availability.html).

When provisioning a stretched private cloud, VMs might run on both sides of a stretched private cloud. Use [affinity rules](https://docs.vmware.com/en/VMware-vSphere/8.0/vsphere-resource-management/GUID-793013E2-0976-43B7-9A00-340FA76859D0.html) to control the placement of workload VMs on hosts within a cluster by grouping them and pinning them to a site. Such a design assures zone resilience through application high availability (HA).

## Segregate environments across several private clouds

A private cloud is an independent VMware Cloud Foundation stack managed by a vCenter Server.

You can segregate your VMware Engine footprint across multiple private clouds. For example, use a dedicated vCenter Server in the following cases:

  * For a specific workload type, such as [Virtual Desktop Infrastructure (VDI)](https://www.vmware.com/products/horizon.html)
  * When the [limits of a private cloud](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components#vsphere-limits) are inadequate
  * For licensing and software management
  * For cost transparency and simplicity
  * For monitoring
  * For compliance with regulatory requirements
  * For multi-tenancy at all layers, including management components and infrastructure



To avoid the unnecessary proliferation of management endpoints, use only the required number of private clouds.

## Optimize the core count

VMware Engine lets you reduce the number of effective CPU cores that are exposed to the ESXi hypervisor. This might be desirable, or required, under some software license agreements.

Reducing the core count of the first cluster is not recommended because it hosts key components, such as vCenter and NSX Manager.

Reducing the number of effective cores in a cluster does not change the cost of running the cluster, specifically for Oracle workloads. For more information, see the guidance regarding [support and licensing](https://docs.cloud.google.com/vmware-engine/docs/concepts-third-party-solutions).

For more information, see [Custom core count limitations](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud#custom-core-count-limits).

## Add spare nodes for resilience

VMware Engine clusters should be sized to have at least one spare node for resilience. This spare node is available to the cluster and can provide additional capacity and resources during times of high load or contention. These spare nodes are billed as part of the existing private cloud.

If higher reliability is required, consider adding more spare nodes to the cluster to be available during maintenance windows. Scheduling workloads to run on these spare nodes helps optimize the use of the clusters in private clouds.

## Define the number of failures to tolerate

For [VMware vSAN](https://docs.vmware.com/en/VMware-vSAN/index.html), use the Failures to tolerate (FTT) attribute in [vSAN storage policies](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components#vsan_storage_policies) to define the number of failures that a cluster can tolerate without affecting its data integrity or VM availability.

The higher the FTT value, the more the capacity hosts that are required.

## What's next

  * Read about best practices for [networking](https://docs.cloud.google.com/vmware-engine/docs/best-practices-networking), [security](https://docs.cloud.google.com/vmware-engine/docs/best-practices-security), [storage](https://docs.cloud.google.com/vmware-engine/docs/best-practices-storage), [migration](https://docs.cloud.google.com/vmware-engine/docs/best-practices-migration), and [costs](https://docs.cloud.google.com/vmware-engine/docs/best-practices-costs).
  * Read about [Private cloud VMware Engine components](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components).
  * Try out VMware Engine. Visit [features, benefits, and use cases](https://docs.cloud.google.com/vmware-engine/docs/overview) for more information.
  * Explore reference architectures, diagrams, tutorials, and best practices about Google Cloud. Visit [Cloud Architecture Center](https://docs.cloud.google.com/architecture) for more information.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

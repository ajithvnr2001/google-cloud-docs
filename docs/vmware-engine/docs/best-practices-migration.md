---
url: https://docs.cloud.google.com/vmware-engine/docs/best-practices-migration/
title: Migration best practices \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:24.109379+00:00
---

# Migration best practices  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/best-practices-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migration best practices

This page presents some best practices for migrating VMware virtual machine (VM) instances to your private cloud by using Google Cloud VMware Engine.

## Plan the migration project

Before migrating VMware VMs to your private cloud, plan the migration as follows:

  * Identify the personnel, including the following:

    * Customer stakeholders
    * Program sponsor and owner
    * The technical team responsible for the migration
    * The stakeholders for in-scope systems and applications
    * The relevant Google Technical Account Manager (TAM), Partner Engineering Manager (PEM), or Customer Engineer (CE)
  * Assess the [source environment](https://docs.cloud.google.com/vmware-engine/docs/workloads/classic-console/howto-migrate-workloads#assess_the_source_environment).

  * Create a plan that defines the following:

    * the migration strategy
    * the architecture of the new environment
    * the goals and success criteria, including the UAT and QA scripts
    * the roles and responsibilities
    * the communication model, including daily standups, status reporting, escalation paths, chat rooms
    * the data that cannot be migrated and related strategies
    * milestones and timings
  * Ensure alignment with all stakeholders.




## Evaluate migration options

To evaluate the different migration options for VMware Engine, consider the following options:

  * Consider planning the migration in waves.

    * Factor in application dependencies and mappings.
    * Group VMs based on their maintenance schedule.
    * To avoid multiple power cycles, identify the VMs with pending system updates and align the schedule with the migration switchover reboots.
  * Establish a backup and DR strategy for VMs. Consider using [Google Cloud Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs) and [VMware Engine Protected](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-engine-protected).

  * Ensure that vSphere, vCenter, HCX, and, if applicable, NSX-T on-premises meet the minimum versioning compatibility with [VMware Engine component versions](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components#vmware_component_versions).

  * Identify VMs with memory, CPU, or storage requirements that exceed the specification of the current node type or that might cause contention if combined with other large VMs.

For example, database servers might require large amounts of memory or file storage servers might require large datastores.

  * Develop pre- and post-migration strategies for content that cannot be migrated due to persistent hardware or tagging, such as mounted ISOs, NSX-T tags, passthrough devices that use [DirectPath I/O](https://docs.vmware.com/en/VMware-vSphere/8.0/vsphere-networking/GUID-BF2770C3-39ED-4BC5-A8EF-77D55EFE924C.html), [multi-writer disks](https://core.vmware.com/blog/migrating-vms-shared-or-multi-writer-disks), and physical RDMs. An example strategy might be to consider converting physical RDMs to [virtual compatibility mode](https://knowledge.broadcom.com/external/article?legacyId=1006599).

  * Assess and evaluate [migration methods](https://docs.vmware.com/en/VMware-HCX/4.9/hcx-user-guide/GUID-8A31731C-AA28-4714-9C23-D9E924DBB666.html).

Prefer [bulk migration](https://docs.vmware.com/en/VMware-HCX/4.9/hcx-user-guide/GUID-20EA2946-57CD-4A87-AE25-866E5336AEA9.html#GUID-20EA2946-57CD-4A87-AE25-866E5336AEA9). Consider the related requirements and restrictions.




## Use VMware HCX for migrations

When using [HCX for migration](https://docs.cloud.google.com/vmware-engine/docs/workloads/howto-migrate-vms-using-hcx), consider the following recommendations:

  * Although a flat network topology is supported for HCX Connector and HCX Service Mesh deployments, to avoid routing problems and connectivity errors, set up HCX Management and the HCX Uplink [network profiles](https://docs.vmware.com/en/VMware-HCX/4.9/hcx-getting-started/GUID-AB56D9A9-7E2C-436F-9E20-445E447E300F.html) on separate networks and VLANs.

  * Ensure that your VMware environment has the latest HCX versions. For more information, see [HCX Service Update Procedures](https://docs.vmware.com/en/VMware-HCX/4.9/hcx-user-guide/GUID-77111C61-EC4C-4C8C-8340-5828CC4D489D.html).

  * Be sure to configure [HCX backups and restore operations](https://docs.vmware.com/en/VMware-HCX/4.9/hcx-user-guide/GUID-50C416BC-5415-42AB-AA7A-3A5CB46A60C7.html), as required.

The SRE team manages HCX Manager backups, but not HCX Connector backups.

HCX service appliances, including HCX-IX and HCX-NE, don't require individual backups. A restored HCX Manager reconnects to existing service appliances that were created within the backup duration. If the service appliances are no longer functional, the HCX Manager deploys new appliance VMs based on the backed-up configuration.

  * When stretching a Layer 2 network by using HCX network extensions, enable TCP Flow Conditioning. For related information, see [Traffic engineering features provided in HCX](https://blogs.vmware.com/cloud/2020/01/16/traffic-engineering-hcx-enterprise/).

  * For VMs that communicate to or from a private cloud over an HCX L2 extension, configure the best MTU setting based on VPN endpoint configurations. This is especially important in cases where an application isn't able to control the maximum payload size.

Google recommends an MTU setting of 1350 bytes to 1390 bytes or lower for VM interfaces that allow data transfer in the following ways:

    * From an on-premises endpoint to a private cloud and conversely
    * From a VM in one private cloud to a VM in another private cloud over an L2 extension

For additional guidance on calculating encapsulation overhead, see [MTU considerations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/mtu-considerations) and [VMware NSX-T VPNs](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.0/administration/GUID-A8B113EC-3D53-41A5-919E-78F1A3705F58.html).




## What's next

  * Read about best practices for [compute](https://docs.cloud.google.com/vmware-engine/docs/best-practices-compute), [networking](https://docs.cloud.google.com/vmware-engine/docs/best-practices-networking), [security](https://docs.cloud.google.com/vmware-engine/docs/best-practices-security), [storage](https://docs.cloud.google.com/vmware-engine/docs/best-practices-storage), and [costs](https://docs.cloud.google.com/vmware-engine/docs/best-practices-costs).
  * Try out VMware Engine. Visit [features, benefits, and use cases](https://docs.cloud.google.com/vmware-engine/docs/overview) for more information.
  * Explore reference architectures, diagrams, tutorials, and best practices about Google Cloud. Visit [Cloud Architecture Center](https://docs.cloud.google.com/architecture) for more information.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

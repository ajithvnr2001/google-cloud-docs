---
url: https://docs.cloud.google.com/sap/docs/checklist-sap/
title: General checklist for SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:14:31.007409+00:00
---

# General checklist for SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/checklist-sap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  General checklist for SAP on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This checklist will help you to improve the design, migration, implementation, and maintenance of your SAP systems on Google Cloud.

As you go through the checklist, take into account your own business needs. If you make choices that differ from what we've recommended, keep track of those differences for later tasks in the checklist.

**Note:** This checklist contains general recommendations and doesn't cover all aspects of your SAP on Google Cloud landscape. 

****

###  Plan and design your needs for compute, networking, and storage

  * Compute
  * Networking
  * Storage



#### Compute

  * To verify if the machine types and software that you plan to use for your migration are certified by SAP, see [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).
  * Try to avoid running multiple applications on the same VM instance. However, if you choose to run more than one application on a single VM: 
    * Make sure the applications don't compete with each other for resources and bandwidth. Otherwise, move the applications to separate VMs.
    * We recommend using [Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) to resolve the static IP addresses rather than using a local resolver.
  * Make sure you estimate sizing for your planned SAP workloads and allow for future growth.

    * To evaluate your sizing options based on the implementation type, see [Benchmark | Sizing](https://www.sap.com/about/benchmark/sizing.html) (SAP) and [Sizing](https://docs.cloud.google.com/sap/docs/architectures/sap-s4hana-on-gcp#sizing) (Google Cloud).
    * To reserve excess capacity based on growth requirements or failover needs, see [Reserving Resources](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources).

    * To optimize cost and efficiency, review the benefits of [sustained use discounts](https://docs.cloud.google.com/compute/vm-instance-pricing#sustained_use) and [committed use discounts](https://docs.cloud.google.com/compute/vm-instance-pricing#committed_use). These tools help you take advantage of the flexibility of cloud resources, and help you use only the resources that you need.




#### Networking

  * To design your Virtual Private Cloud (VPC) network for optimal performance, see the [Best Practices VPC Design](https://docs.cloud.google.com/solutions/best-practices-vpc-design) guide. We recommend the following design choices:

    * Use the Premium network service tier. For information, see [Network Service Tiers](https://cloud.google.com/network-tiers).
    * Choose IP address ranges that do not conflict with each other, and include any existing on-premises IP address ranges into your planning and design.
    * Decide on your network design and configuration before deploying resources for the following reasons: 
      * You cannot add network interfaces or change the assigned cloud network once a VM is deployed.
      * If you need to make changes, you'll need to redeploy instances. Such changes could impact the availability of your landscape and applications.
  * To learn about the benefits of a shared VPC, see the [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc) guide. In general:

    * Shared VPC limits network administration access to the host project. This feature segregates network configuration access, which can be useful in delegated access scenarios. For example, you can allow developers to deploy VM instances in a test project, but prevent them from changing the network configuration.
    * Shared VPC also imposes limits. For example, if Service Accounts in a service project need to make route updates in a high-availability (HA) scenario, you can use [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) and [conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to restrict access to very specific resources.
    * If you select Shared VPC for your landscape, create the Shared VPC before deploying VMs to your projects. This practice prevents you from having to redeploy instances and redo the network configuration if you choose to move to a Shared VPC at a later time.
  * To provide connectivity from your on-premises environment to your Google Cloud project, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product). We recommend the following:

    * Do not create an external IP address for systems that do not require external access. This practice secures your system by limiting outside access.
    * For internal communication, use [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) to limit access to the protocols and port numbers that your landscape actually uses.
    * For access to your Google Cloud environment, see the [Cloud NAT overview](https://docs.cloud.google.com/nat/docs/overview) for details about outbound access and [Using IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) for inbound, administrative access.
    * If you are considering using third-party network appliances (such as proxies, firewalls, packet inspectors, load balancers, and web application firewalls), ensure that these services do not limit bandwidth or cause interruption to your VPC. Please work with your provider to ensure the solution is appropriate for SAP systems, and have them apply the necessary exclusions to limit impact.



#### Storage

  * When you save backups to a persistent disk: 
    * Ensure that you offload the backup files to a secondary location for redundancy. You can accomplish this by creating a snapshot of this volume once the backup completes.
    * Select a storage location that is redundant for the particular risk that you wish to mitigate (such as logical corruption, zonal outage, or regional outage). Using a second region as the secondary location is often a good choice.



###  Review recommendations for migration

  * When upgrading any SAP components, consider the following: 
    * To change your backend database, review the SAP Database Migration Option (DMO) for Software Update Manager (SUM) guides for suggestions on how to combine an upgrade with the migration. See [DMO of SUM 1.0](https://help.sap.com/viewer/c4ebc2b5d928446180d9ad2667f11faa/1.0/en-US/8b1d697dac2c4e92a62e8dd492f49ccc.html) and [DMO of SUM 2.0](https://help.sap.com/viewer/c4ebc2b5d928446180d9ad2667f11faa/1.0/en-US/404d4617367948f0be1c41ec2254ae37.html).
    * To ensure an easier migration, review your current source system data. We recommend that you archive historical business data and delete temporary data before the migration. Doing so reduces your data footprint and the migration time.
  * To implement a lift-and-shift migration, you can use a variety of tools based on your migration needs. Here are some examples of commonly used tools: 
    * [Database Migration Option (DMO)](https://blogs.sap.com/2013/11/29/database-migration-option-dmo-of-sum-introduction/)
    * [Near-Zero Downtime Tool (NZDT)](https://launchpad.support.sap.com/#/notes/693168)
    * [Zero Downtime Option (ZDO)](https://launchpad.support.sap.com/#/notes/2163060)
  * For more information about migration strategies, see [Migration to Google Cloud: Getting started](https://docs.cloud.google.com/solutions/migration-to-gcp-getting-started).



###  Plan and implement security

  * To define security requirements for workloads on Google Cloud, see the [Cloud Security Best Practices](https://cloud.google.com/security/best-practices) guide. We recommend the following: 
    * Always follow the least privilege principle, but make sure that team members have enough access privileges to allow them control and flexibility when carrying out their duties.
    * Use anti-virus and anti-malware applications with care, especially with performance-sensitive applications (such as database servers).
    * Apply appropriate restrictions on files to support your security posture (such as access to database storage).



###  Know how to get support if you need it

  * To view the conditions required by SAP to provide support for your SAP on Google Cloud landscape, see [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406).

Notably, this includes the requirement of installing the [Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning) on your Compute Engine VMs or Bare Metal Solution servers, regardless of the SAP product that you run on them. For more information, see the documentation for your deployment scenario.

  * For more information about getting support from Google Cloud and SAP, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

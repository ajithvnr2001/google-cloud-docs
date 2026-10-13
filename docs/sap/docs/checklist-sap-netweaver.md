---
url: https://docs.cloud.google.com/sap/docs/checklist-sap-netweaver/
title: Checklist for SAP NetWeaver on Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:04.045587+00:00
---

# Checklist for SAP NetWeaver on Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/checklist-sap-netweaver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Checklist for SAP NetWeaver on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This checklist will help you to improve the design, migration, implementation, and maintenance of your SAP NetWeaver landscapes on Google Cloud.

As you go through the checklist, take into account your own business needs. If you make choices that differ from what we've recommended, keep track of those differences for later tasks in the checklist.

**Note:** This checklist contains general recommendations and doesn't cover all aspects of your SAP on Google Cloud landscape. 

****

###  Plan your SAP NetWeaver landscape

  * To scale your SAP NetWeaver landscape and increase redundancy, run SAP central services, each SAP application server, and each database server in its own separate Compute Engine VM instance.
  * Follow these guidelines to ensure the correct sizing for your VM instances: 
    * Before you move your existing systems from on-premises or other cloud environments, use your current workload statistics and utilization as a baseline for sizing when migrating to Google Cloud.
    * If you don't size the VMs correctly for the load, when you combine multiple SAP System IDs with other business solutions, your applications might become resource constrained and run poorly.
    * To learn more about sizing for SAP solutions on Google Cloud, see [What is sizing?](https://www.sap.com/about/benchmark/sizing.html) and the[ SAP Quick Sizer](https://www.sap.com/about/benchmark/sizing.quick-sizer.html).

**Note:** Quick Sizer is intended for new systems. Use your existing workload statistics to determine your application's requirements. Migration offers an opportunity to provide resource constrained systems with additional capacity, or allows the reduction of resources to be more cost effective while still maintaining nominal performance.

  * If you choose to run more than one SAP application instance on the same VM or run multiple application servers from the same SID on the same VM, you should install them with different hostnames to allow you to relocate such instances if they outgrow a single VM. 
    * SAP profiles contain the instance hostname in both the file name and in SAP variables like SAPLOCALHOST and SAPGLOBALHOST. Because of this property, we recommend that you configure alias IPs and alias hostnames for those instances from the start.
    * To maintain mappings of the alias IPs and hostnames for the entire project, configure [Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) in Google Cloud as a central resolver rather than using a local DNS resolver.
  * To adjust your workloads dynamically as application demand rises and falls, consider implementing SAP application auto-scaling mechanisms: 
    * In most large SAP environments, application server workloads have daily, predictable variations. Because the timing and rate of these workload changes are generally consistent and rarely change, these servers are great candidates to benefit from the elastic nature of cloud infrastructure.
    * To benefit from auto-scaling options for your SAP workloads, see [Best practices for SAP app server autoscaling](https://cloud.google.com/blog/products/sap-google-cloud/best-practices-for-sap-app-server-autoscaling-on-google-cloud).
  * For more information about SAP configuration standards and supportability, see the [SAP Support Portal Home](https://support.sap.com/en/index.html) and [SAP on Google Cloud solutions](https://docs.cloud.google.com/solutions/sap).



###  Select regions and zones for SAP NetWeaver

  * To learn which regions and zones support specific Compute Engine VMs, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). Keep in mind that SAP NetWeaver-certified Compute Engine VMs might not be available in all locations.
  * Choose your regions and zones for an SAP NetWeaver deployment based on your business locations. SAP NetWeaver instances must be placed in the same region, and the high-availability components (such as SAP central services) should be deployed in different zones within the region for maximum redundancy.
  * To select the best regions for your SAP NetWeaver deployment, see [Best practices for Compute Engine region selection](https://docs.cloud.google.com/solutions/best-practices-compute-engine-region-selection).
  * To select a network design that can withstand different types of system failure, see [Designing robust systems](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems).



###  Choose a deployment model for SAP NetWeaver

  * To deploy infrastructure for SAP NetWeaver, you can Terraform configurations provided by Google Cloud. Terraform is a popular industry application for building, changing, and versioning infrastructure safely and efficiently. To use Terraform and find the appropriate configuration files for your SAP solutions, see [Automating SAP deployments on Google Cloud with Terraform](https://docs.cloud.google.com/sap/docs/tf-for-sap).

  * If your SAP NetWeaver deployment and installation requires a custom procedure (such as a manual installation, third-party tool, or provider), see the following deployment guides for manual setup and installation of SAP workloads:

    * [Manual VM deployment for SAP NetWeaver on Linux](https://docs.cloud.google.com/sap/docs/netweaver-deployment-linux-manual)
    * [Manual VM deployment for SAP NetWeaver on Windows](https://docs.cloud.google.com/sap/docs/netweaver-deployment-windows-manual)
    * [HA cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel)
    * [HA cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles)
    * [IBM DB2 for SAP deployment guide](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide)



###  Pick appropriate machine types and operating systems for SAP NetWeaver

  * To select a machine type for your SAP NetWeaver deployment, see [Certified machine types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms).
  * To select an operating system and view available OS images, see [OS support for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-os-support) and the [Quick reference table](https://docs.cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table).

  * If you run SAP NetWeaver on the same host as SAP HANA in a two-tier architecture, the SAP HANA machine requirements apply. To see the SAP HANA certified machine types, see [Certifications for SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-hana).

  * For OS image licensing, you can bring your own license provided by your OS vendor. If the guest OS image release you want isn't available in Google Cloud, you can import it as a [custom image](https://docs.cloud.google.com/compute/docs/images#custom_images).

  * For more information about supported machine types, operating systems, and applications, see [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).




###  Select a database for SAP NetWeaver

  * For information from SAP about supported database types, vendors, and assigned SAP Application Performance Standard (SAPS), see [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).



###  Add a file system and shared storage for SAP NetWeaver

  * To learn about NFS and other file storage systems available for SAP NetWeaver Google Cloud, see [Storage options for HA SAP systems on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-ha-planning-guide#ha-storage-options).

  * The Compute Engine high-availability shared storage solutions for SAP NetWeaver include [Filestore Enterprise](https://cloud.google.com/filestore), [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview), and [NetApp Cloud Volumes ONTAP](https://docs.netapp.com/us-en/storage-management-cloud-volumes-ontap/index.html).




###  Have a backup and restore strategy for SAP NetWeaver

  * To learn how to backup the database and the file system for SAP NetWeaver, see [AS Java Backup and Restore](https://help.sap.com/viewer/5bdacafd0bbd41648f4b80093a1bf9d6/7.5.19/en-US/aba24c409cef4f4fa21f9777ce360b06.html?q=backup%20and%20restore%20netweaver) and [Backing Up and Restoring your SAP System on UNIX](https://help.sap.com/viewer/ff18034f08af4d7bb33894c2047c3b71/7.5.14/en-US/d3c0da3ccbb04d35b186041ba6ac301f.html?q=backup%20and%20restore%20netweaver).

  * To secure the backup archives, you must store the backup files in a separate secure location. Here are some common choices:

    * You can store the backups in [Google Cloud Storage](https://docs.cloud.google.com/storage).
    * You can store the archives on a drive in a custom or third-party location (for example, on-premises).
    * You can also store the backups in Google Cloud by using [Filestore](https://docs.cloud.google.com/filestore) or the [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview).
    * Store multiple copies in multiple locations on different media types to assure recoverability.
  * Define the backup frequency and retention period for your file system data and database files based on your business needs for the recovery point objective (RPO) and the recovery time objective (RTO).




###  Best practices for high-availability configurations for SAP NetWeaver

For a checklist of best practices for high-availability configurations for SAP NetWeaver on Google Cloud, see [High availability for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/checklist-sap-high-availability).

###  Build in disaster recovery for SAP NetWeaver

  * To learn about the ways to provide disaster recovery for SAP NetWeaver, see the [Disaster recovery planning guide for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-dr-on-gcp).



###  Use monitoring and alerting for SAP NetWeaver

  * For integrated monitoring of the SAP NetWeaver infrastructure in Google Cloud, use Google Cloud's Agent for SAP. 
    * To set up the monitoring agent, see [Google Cloud's Agent for SAP planning guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning) and [ SAP Note 2469354 - Key Monitoring Metrics for SAP on IaaS Infrastructure](https://launchpad.support.sap.com/#/notes/2469354).
  * Ensure that you implement a robust monitoring strategy for your application using SAP-native systems such as [Solution Manager](https://support.sap.com/en/alm/solution-manager.html) or [Focused Run](https://support.sap.com/en/alm/sap-focused-run.html), or appropriate third-party monitoring applications. Supplement this with [Google Cloud Monitoring](https://docs.cloud.google.com/monitoring), which offers extensive cloud and operating system monitors with the ability to create custom metrics and alerts.



###  Automate validation checks for SAP NetWeaver workloads

To automate continuous validation checks for your SAP NetWeaver workloads that run on Google Cloud, use [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview). Workload Manager allows you to automatically scan and evaluate your SAP NetWeaver workloads against best practices to improve their quality, performance, and reliability. 

###  Enable integration interfaces for SAP NetWeaver

  * In addition to accessing SAP NetWeaver through a web interface or the SAP GUI, you might also need to establish inbound and outbound communication with other SAP solutions or third-party systems. Typical examples of this include IDOC interfaces, process integration with external business partners, and SAP Landscape Transformation Replication with on-premises reporting systems. To enable inbound and outbound interfaces, use the following resources to set up routing and firewall rules in your VPC network:

    * [VPC routes overview](https://docs.cloud.google.com/vpc/docs/routes)

    * [VPC firewall rules overview](https://docs.cloud.google.com/vpc/docs/firewalls)

    * [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc)




###  Add load balancing and scaling for SAP NetWeaver

  * SAP NetWeaver software supports a distributed architecture that allows the distribution of system instances over multiple virtual machines. This architecture provides benefits of both scale and redundancy.
  * The distributed nature of SAP NetWeaver requires load balancing for end-user requests. On Google Cloud you can use native SAP software load balancing in combination with Google-native L4 or L7 load balancers, or choose to set up third-party load balancers from the Google Cloud Marketplace. 
    * To explore options for a load-balancing strategy that considers the geographical location of users and the system landscape setup, see [How to run SAP on Google Cloud if high availability is a high priority](https://cloud.google.com/blog/products/sap-google-cloud/how-to-run-sap-on-google-cloud-if-high-availability-is-high-priority).
    * To explore more ways to provide load-based system flexibility, see [Best practices for SAP app server autoscaling on Google Cloud](https://cloud.google.com/blog/products/sap-google-cloud/best-practices-for-sap-app-server-autoscaling-on-google-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

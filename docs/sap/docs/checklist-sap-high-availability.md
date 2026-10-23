---
url: https://docs.cloud.google.com/sap/docs/checklist-sap-high-availability/
title: High availability for SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:35.343472+00:00
---

# High availability for SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/checklist-sap-high-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  High availability for SAP on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This checklist will help you to improve the design, migration, implementation, and maintenance of high availability for SAP HANA and SAP NetWeaver landscapes on Google Cloud.

As you go through the checklist, take into account your own business needs. If you make choices that differ from what we've recommended, keep track of those differences for later tasks in the checklist.

**Note:** This checklist contains general recommendations and doesn't cover all aspects of your SAP on Google Cloud landscape. 

****

###  Best practices for high-availability configurations for SAP HANA

  * To understand how to implement or maintain a high-availability SAP HANA system on Google Cloud, see the [SAP HANA high-availability planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide).
  * To provide protection against unplanned outages (such as hardware failure), we strongly recommend that you use OS-based software clustering.
  * To allow quick restart of your SAP HANA 2.0 SP04 or later system in case of a process failure or for software maintenance that doesn't require a VM reboot, enable the SAP HANA Fast Restart option. We strongly recommend that you enable the Fast Restart option for Compute Engine memory-optimized machines types, such as the M1, M2, or M3 machine types. For more information from SAP about SAP HANA Fast Restart, see [SAP HANA Fast Restart option](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/ce158d28135147f099b761f8b1ee43fc.html).

For more information about how to enable Fast Restart, see the configuration guide for your Linux distribution:

    * [RHEL: Enable SAP HANA Fast Restart](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#enable_sap_hana_fast_restart)
    * [SLES: Enable SAP HANA Fast Restart](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#enable_sap_hana_fast_restart)
  * To allow SAP HANA to send out notifications for certain events and improve failure detection, enable the SAP HANA HA/DR provider hook.

For more information about how to enable SAP HANA HA/DR provider hook, see the configuration guide for your Linux distribution:

    * [RHEL: Enable the SAP HANA HA/DR provider hook](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#enable-hana-hadr-provider-hook)
    * [SLES: Enable the SAP HANA HA/DR provider hook](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#enable-hana-hadr-provider-hook)
  * If you do not use a cluster automation solution (such as Pacemaker), define and test your recovery procedures and playbook.

  * When using Pacemaker:

    * In the `totem` section of the `corosync.conf` configuration file, use the parameter values that Google Cloud recommends. If you are configuring a new high-availability cluster, you need to change some default values. For more information about recommended values of Corosync configuration parameters, see [Corosync configuration parameter values](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#corosync_configuration_parameter_values).

For more information about how to modify the default values in `corosync.conf` configuration file, see the configuration guide for your Linux distribution:

      * [RHEL: Update the corosync configuration files](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#edit_the_corosyncconf_default_settings)
      * [SLES: Create the corosync configuration files](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#create_the_corosync_configuration_files)
    * When you configure the cluster resource for your fencing device, be sure to set the timeout and monitoring intervals and a restart delay for Corosync as recommended by Google Cloud. For more information about how to set up fencing, see the configuration guide for your Linux distribution:

      * [RHEL: Set up fencing](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#set_up_fencing)
      * [SLES: Set up fencing](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#set_up_fencing)
    * Define a virtual IP address (VIP) that uses an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview). If you do not use the automation provided by Google Cloud to set up this configuration, ensure that you reserve this VIP address to avoid it from being reused accidentally.

    * Create a configuration that follows the standard guidelines for [RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel) and [SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles).

    * For testing purposes, create a non-production HA system that is equivalent to your production environment.




###  Best practices for high-availability configurations for SAP NetWeaver

  * To view the supported SAP configurations for high availability, see [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).
  * On SUSE Linux Enterprise Server (SLES) or Red Hat Enterprise Linux (RHEL), the Pacemaker cluster application provides you with the resources to configure your SAP applications in a high-availability configuration. When using Pacemaker:

    * In the `totem` section of the `corosync.conf` configuration file, use the parameter values that Google Cloud recommends. If you are configuring a new high-availability cluster, you need to change some default values.

For more information about how to modify the default values in `corosync.conf` configuration file, see the configuration guide for your Linux distribution:

      * [RHEL: Update the corosync configuration files](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel#update_the_corosync_configuration_files)
      * [SLES: Create the corosync configuration files](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles#create_the_corosync_configuration_files)
    * When you configure the cluster resource for your fencing device, be sure to set the timeout and monitoring intervals and a restart delay for Corosync as recommended by Google Cloud. For more information on how to set up fencing, see the configuration guide for your Linux distribution:

      * [RHEL: Set up fencing](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel#set_up_fencing)
      * [SLES: Set up fencing](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles#set_up_fencing)
    * For the RHEL and SLES operating systems, use an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview) to manage the virtual IP (VIP) address. The Load Balancer provides a highly available service and creates a floating VIP that can direct traffic between VMs in a cluster.

    * Create a configuration that follows the standard guidelines for [RHEL](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel) and [SLES](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles).

  * For Windows-based environments, the Windows native failover cluster feature provides high availability. For more information, see the following Windows OS resources:

    * [Configuring SQL Server AlwaysOn Availability Groups](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability)

    * [Running Windows Server Failover Clustering](https://docs.cloud.google.com/compute/docs/tutorials/running-windows-server-failover-clustering)

    * [SAP Note 112266 - SAP and Microsoft Failover Cluster: Frequently asked questions and tips](https://launchpad.support.sap.com/#/notes/112266)

  * If your landscape has VM instances that host multiple SAP systems with different system IDs, follow these high availability (HA) recommendations:

    * To provide high availability for SAP central services and database systems, configure high-availability mode by using one of Google Cloud's supported HA methods. See the [High-availability planning guide for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-ha-planning-guide) or the [SAP HANA high-availability planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide).

    * To provide high availability for an IBM Db2 high-availability cluster in an SAP NetWeaver system, see the [IBM Db2 high-availability cluster for SAP deployment guide](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-ha-deployment-guide).

    * To avoid associated complexities, do not run multiple software solutions in the same HA cluster. Instead, deploy software in the HA cluster (for example, SAP central services) on separate VMs that you've sized properly.

      * Do not use different types of clustering software to manage resources on the same VM. The two cluster solutions might conflict with each other and could result in unexpected behavior.
      * If you set up multiple services from different SAP system IDs on the same high-availability VM cluster: 
        * The increased complexity hampers troubleshooting and recovery significantly.
        * If a failure occurs, multiple systems can be impacted. Distributing resources reduces the extent of this impact.
  * If you choose a third-party failover solution for your SAP central services, document the setup and test it thoroughly.

  * For testing and rollout purposes, we recommend that you create a non-production HA system that is equivalent to your production environment.

    * Although this might not be required by the business, you can use this test HA system to validate failover and maintenance procedures, perform extensive testing, and document the system for operational reference.
  * If you implement a standalone instance of SAP central services without high availability, make sure you document your manual procedure for the restore process and test it thoroughly.

    * Note: SAP NetWeaver systems lacking high availability often result in longer service restoration times and unpredictable outages.



###  General best practices for high-availability configurations

  * Live migration and high-availability clusters: 
    * Enable Compute Engine Live Migration[ instance policies](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options) on your VM instances.
    * [Simulate a Live Migration maintenance event](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/simulate-maintenance-event) to assess the impact of Live Migration to your active workloads and high availability configuration.
    * For more information about Live Migration, see [Live Migration](https://docs.cloud.google.com/compute/docs/instances/live-migration).
  * Enable Compute Engine automatic restart [ instance policies](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options) on your VM instances.
  * To ensure you've configured adequate cluster failover thresholds, see [Testing your availability policies](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#testingpolicies).



###  Automate validation checks for high-availability configurations

To automate continuous validation checks for your high-availability configurations on Google Cloud, use [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview). Workload Manager allows you to automatically scan and evaluate your SAP workloads against best practices to improve their quality, performance, and reliability. Workload Manager includes best practices related to high availability, which can evaluate if your configurations are aligned with the best practices from SAP, Google Cloud, and OS vendors. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

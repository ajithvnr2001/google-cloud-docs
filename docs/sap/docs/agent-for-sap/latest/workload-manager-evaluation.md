---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/workload-manager-evaluation/
title: Workload Manager evaluation using Google Cloud's Agent for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:06.250413+00:00
---

# Workload Manager evaluation using Google Cloud's Agent for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/workload-manager-evaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Workload Manager evaluation using Google Cloud's Agent for SAP Stay organized with collections  Save and categorize content based on your preferences. 

This planning guide focuses solely on the _Workload Manager evaluation metrics collection_ feature of Google Cloud's Agent for SAP. For information about the agent and all its features, see [Google Cloud's Agent for SAP planning guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning).

On Linux, Google Cloud's Agent for SAP can help you in evaluating your SAP workloads that run on Google Cloud. This is delivered through the collection of [Workload Manager evaluation metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#wlm_evaluation_metrics) which is enabled by default for new agent installations as of version 3.2 on your Compute Engine instances or Bare Metal Solution servers.

**Note:** The collection of Workload Manager metrics is supported only on Linux. It is not supported on Windows.

Once you enable the collection of the Workload Manager evaluation metrics, you can enable [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview) services for your SAP workloads. The information collected in the Workload Manager evaluation metrics help you check the configuration and settings of your SAP applications, databases, and high-availability configurations. For information about the best practices that Workload Manager supports for evaluating SAP workloads, see [Workload Manager best practices for SAP](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices).

For information about how to configure Google Cloud's Agent for SAP to collect the Workload Manager evaluation metrics, see [Configure Workload Manager evaluation metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-workload-manager-evaluation).

## Pricing

From version 3.2, you don't incur any additional cost for using Google Cloud's Agent for SAP to collect the Workload Manager evaluation metrics, or store these metrics in Workload Manager.

## Workload Manager evaluation metrics

The following table describes the categories of Workload Manager evaluation metrics collected by Google Cloud's Agent for SAP. The metric strings in this table must be prefixed with `workload.googleapis.com/`. This prefix has been omitted from the entries in the following table.

Category | **Metric** | **Description**  
---|---|---  
System | `sap/validation/system` | OS and guest level information about the compute instance.  


  * Instance name
  * OS name and version
  * Agent version

  
Corosync | `sap/validation/corosync` | Information about the Corosync configuration for an HA cluster.  


  * Configuration set in `/etc/corosync/corosync.conf`.
  * Runtime configuration retrieved using `corosync-cmapctl`.

  
Pacemaker | `sap/validation/pacemaker` | Information about the Pacemaker configuration for an HA cluster.  


  * Configuration set in the Pacemaker XML config.
  * The `maintenance_mode` setting for the Pacemaker cluster.

  
SAP HANA | `sap/validation/hana` | Information about the configuration of the SAP HANA system.  


  * Configuration set in the `global.ini` file for the SAP HANA system.
  * Information about the disks hosting the SAP HANA data and log volumes.

  
SAP HANA insights and security | `sap/validation/hanasecurity` | Settings and configuration of the SAP HANA database.  


  * Best practice recommendations for database password settings.
  * Best practice recommendations for data and log backups.
  * Best practice recommendations for scale-out and high-availability cluster settings.

To enable the collection of this metric, you must allow access to the SAP HANA database, for which you need to configure additional parameters in the `workload_validation_db_metrics_config` section. For more information, see [Configure Workload Manager evaluation metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-workload-manager-evaluation).   
SAP NetWeaver | `sap/validation/netweaver` | Information about the configuration of the SAP NetWeaver system.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

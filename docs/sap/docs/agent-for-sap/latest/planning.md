---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning/
title: Google Cloud's Agent for SAP planning guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:48.174386+00:00
---

# Google Cloud's Agent for SAP planning guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Google Cloud's Agent for SAP planning guide Stay organized with collections  Save and categorize content based on your preferences. 

For support and monitoring, Google Cloud provides the _Agent for SAP_ , for SAP workloads running on Compute Engine instances and Bare Metal Solution servers.

As mandated by SAP, to get support from SAP and to enable SAP to meet its service-level agreements (SLAs), you must install Google Cloud's Agent for SAP on all Compute Engine instances and Bare Metal Solution servers that run any SAP system. For more information on the support prerequisites, see [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406).

**Version 3.15 (latest)** of Google Cloud's Agent for SAP is the successor of Google Cloud's monitoring agent for SAP NetWeaver version 2, monitoring agent for SAP HANA version 2, and the Cloud Storage Backint agent for SAP HANA. Therefore, in addition to the collection of metrics, version 3.15 (latest) of Google Cloud's Agent for SAP includes the optional feature: _Backint based backup and recovery for SAP HANA_.

You can opt in to these features that enable products and services such as [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview) for your SAP workloads.

For SAP systems running on a Bare Metal Solution server, Google Cloud's Agent for SAP is required when you run SAP NetWeaver connected to any of the following databases:

  * SAP Adaptive Server Enterprise (ASE)
  * SAP MaxDB
  * IBM Db2

**Note:** Oracle databases are not supported with Google Cloud's Agent for SAP on Bare Metal Solution servers. **Note:** SAP Host Agent, with the `saposcol program`, is required on any host that is running an SAP system. SAP Host Agent is installed automatically during the installation of new SAP system instances with SAP kernel 7.20 or higher. For more information, see [SAP Host Agent](https://help.sap.com/docs/SAP%20Host%20Agent/8661d17ee5c047a887f686b33e990ede/e817cfb89dbc4d799825c94da59c7867.html).

You install Google Cloud's Agent for SAP on the host alongside the SAP system. For instructions about how to install and configure the agent, validate your installation, and verify that the agent is running as expected, see: 

  * [Install and configure the agent on a Compute Engine instance](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm)
  * [Install and configure the agent on a Bare Metal Solution server](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-bms)



If you use the following RHEL or SLES "for SAP" OS images that Google Cloud provides, then Google Cloud's Agent for SAP is packaged with the OS images:

  * RHEL: all "for SAP" images
  * SLES: SLES 15 SP4 for SAP and later versions



## Supported features

Version 3.15 (latest) of Google Cloud's Agent for SAP supports the following features:

  * SAP Host Agent metrics collection
  * SAP system discovery
  * Agent health metrics collection
  * Process Monitoring metrics collection
  * Workload Manager evaluation metrics collection
  * SAP HANA monitoring metrics collection
  * Backint based backup and recovery for SAP HANA
  * Disk snapshot based backup and recovery for SAP HANA
  * Workload performance diagnostics



### SAP Host Agent metrics collection

The SAP Host Agent metrics collection is enabled by default for agent instances installed on Compute Engine instances or Bare Metal Solution servers. Google Cloud's Agent for SAP collects and sends all the required information that SAP mandates to the SAP Host Agent, including metrics about the following:

  * CPUs, for example, CPU utilization.
  * Persistent disk storage, for example, disk throughput and latency.
  * Memory, for example, memory consumption.
  * Networks, for example, network bandwidth.
  * Configuration, including information about the host machine and its environment.



The metrics collected by Google Cloud's Agent for SAP are determined by SAP. For a description of metrics that the agent collects, see [ SAP Note 2469354 - Key Monitoring Metrics for SAP on IaaS Infrastructure](https://launchpad.support.sap.com/#/notes/2469354).

This feature requires the following IAM permissions:

  * `compute.instances.get`
  * `compute.instances.list`
  * `monitoring.metricDescriptors.get`
  * `monitoring.metricDescriptors.list`



### SAP system discovery

This feature is at the core of the agent. It collects information related to your SAP system and the Google Cloud resources it uses, which includes:

  * The Google Cloud resources such as compute instances, disks, networks, load balancers from Cloud Load Balancing, and Filestore instances. For example, in the context of a compute instance, the agent collects information such as the instance name and the region where it's deployed.
  * Information about the connections between the applications and databases in your SAP system.
  * Optionally, the names and versions of the SAP products used in your SAP system.



The collected information is provided to mandatory agent features such as SAP Host Agent metrics collection, other agent features that you enable, and Google Cloud services that you choose to use, such as Workload Manager evaluation. Consequently, this feature is always enabled and can't be turned off.

The following are the configurations that are supported for this feature:

  * The `enable_workload_discovery` boolean parameter determines whether or not the agent collects the names and versions of the SAP products running in your system. By default, this parameter is set to `true`.
  * The `enable_discovery` boolean parameter determines whether or not the collected information is sent to Cloud Logging. It's also sent to Workload Manager if you've enabled the [Workload Manager API](https://console.cloud.google.com/apis/library/workloadmanager.googleapis.com) in your Google Cloud project. By default, this parameter is set to `true`.

The information sent to Workload Manager lets you set up observability for your SAP workload. You don't incur any cost when the agent sends the collected information to Workload Manager. However, there are costs associated with the sending of data to Cloud Monitoring and Cloud Logging, which is required for enabling observability. For information about Workload Manager's observability service for SAP, including pricing, see [SAP observability overview](https://docs.cloud.google.com/workload-manager/docs/observe/sap/overview).




This feature requires the following IAM permissions:

  * `compute.addresses.get`
  * `compute.addresses.list`
  * `compute.disks.get`
  * `compute.forwardingRules.get`
  * `compute.forwardingRules.list`
  * `compute.globalAddresses.get`
  * `compute.globalAddresses.list`
  * `compute.healthChecks.get`
  * `compute.instanceGroups.get`
  * `compute.instances.get`
  * `compute.instances.list`
  * `compute.regionBackendServices.get`
  * `file.instances.get`
  * `file.instances.list`
  * `workloadmanager.insights.write`



### Agent health metrics collection

On Linux, Google Cloud's Agent for SAP can collect metrics that indicate the health of its daemon process on your host. This is an optional feature that you can enable after installing the agent.

This feature is not supported on Windows.

For instructions to enable the collection of the health metrics, and configure the collection frequency, see [Configure agent health metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-agent-health-metrics).

The following table describes the health metrics that the agent collects. The metric strings in this table must be prefixed with `workload.googleapis.com/`. This prefix has been omitted from the entries in the following table.

**Metric** | **Category** | **Description**  
---|---|---  
`sap/agent/health` | Agent for SAP metrics | Indicates if the agent is actively running or not: 

  * The value `true` indicates that the agent is active and running.
  * The value `false` indicates that the agent is not running.

  
`sap/agent/cpu/utilization` | Agent for SAP metrics | CPU utilization by the agent's daemon process.   
`sap/agent/memory/utilization` | Agent for SAP metrics | Memory utilization by the agent's daemon process.  
  
### Process Monitoring metrics collection

On Linux, Google Cloud's Agent for SAP can collect Process Monitoring metrics for your SAP applications and their runtime states. This is an optional feature that you can enable after installing Google Cloud's Agent for SAP.

This feature is not supported on Windows.

The information collected in the Process Monitoring metrics helps you troubleshoot the issues related to your SAP system. In case of issues, with the help of Process Monitoring metrics, Cloud Customer Care can help you reach a resolution more efficiently. The data collected using Process Monitoring metrics provide observability for your SAP HANA high-availability cluster configurations.

Overall, Process Monitoring metrics are fast-changing metrics. For more information about this feature, see [Process monitoring using Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring).

### Workload Manager evaluation metrics collection

On Linux, Google Cloud's Agent for SAP can collect Workload Manager evaluation metrics, which enable you to use [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview#evaluation) to evaluate your SAP workloads against best practices.

From agent version 3.2, this feature is enabled by default for new installations.

This feature is not supported on Windows.

The information collected in the Workload Manager evaluation metrics help you check the configuration and settings of your SAP applications, databases, and high-availability configurations.

Workload Manager evaluation metrics are slow-changing metrics that are collected every 5 minutes by default. From agent version 3.2, you don't incur any additional cost for using the agent to collect the Workload Manager evaluation metrics.

For more information about this feature, see [Workload Manager evaluation using Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/workload-manager-evaluation).

### SAP HANA monitoring metrics collection

On Linux, Google Cloud's Agent for SAP can collect metrics from your SAP HANA instances and send them to [Cloud Monitoring](https://cloud.google.com/monitoring). This optional feature of Google Cloud's Agent for SAP is the successor to using Google Cloud's monitoring agent for SAP HANA version 2.

This feature is not supported on Windows.

The SAP HANA monitoring metrics provide you visibility into the performance, availability, and health of your SAP HANA instances and the underlying infrastructure. The following are examples on how you can use these metrics:

  * You can use the memory utilization related metrics for capacity planning, or to help manage memory-based SAP HANA licensing.
  * By co-relating the SAP HANA monitoring metrics with the Compute Engine metrics, you can identify usage and performance trends.
  * By defining custom queries that collect custom metrics, you can gain deeper insights about your SAP HANA instances.
  * In Cloud Monitoring, you can create dashboards to visualize the SAP HANA monitoring metrics and set up alerts based on metric thresholds.



SAP HANA monitoring metrics are slow-changing metrics that, once enabled, are collected every 5 minutes by default.

For more information about this feature, see [Monitoring SAP HANA using Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana).

### Backint based backup and recovery for SAP HANA

This feature of Google Cloud's Agent for SAP lets you back up and recover SAP HANA systems running on Google Cloud, on Bare Metal Solution, on premises, or on other cloud providers.

This feature of the agent is integrated with SAP HANA so that you can store and retrieve backups directly from Cloud Storage by using SAP-native backup and recovery functions.

For more information about this feature, see [Backup and recovery for SAP HANA by using Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery).

### Disk snapshot based backup and recovery for SAP HANA

This feature of Google Cloud's Agent for SAP lets you back up and recover SAP HANA systems running on Compute Engine instances by using disk snapshots.

The availability of this feature varies based on the architecture and disk configuration of your SAP HANA deployment:

  * For SAP HANA scale-up systems that use a single disk to host the `/hana/data` volume, this feature is generally available (GA).
  * For SAP HANA scale-up systems that use _striped disks_ to host the `/hana/data` volume, and SAP HANA scale-out systems that don't use the host auto-failover solution, this feature is available as a [Preview](https://cloud.google.com/products#product-launch-stages) offering. For more information, [contact Customer Care](https://docs.cloud.google.com/sap/docs/getting-support).



For more information about this feature, see [Backup and recovery for SAP HANA by using disk snapshots](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery).

### Workload performance diagnostics

To help Customer Care troubleshoot performance issues with your SAP workloads that run on Google Cloud, Google Cloud's Agent for SAP contains a built-in performance diagnostics tool. This feature is available from version 3.4 of the agent.

You can use this tool to run the following diagnostics. On-demand diagnostics need to be invoked, whereas default ones such as the guest OS diagnostics are run at all times. You can also have the tool run all these diagnostics in a single execution.

Diagnostic type | Execution mode | Description  
---|---|---  
**Input/output diagnostics** | On-demand |  This is done by using the Flexible I/O tester (FIO) tool, which can stress-test the I/O capabilities of storage systems, and also simulate workloads to assess performance of the underlying infrastructure such as disks and network file system. For more information about FIO, see [ Flexible I/O tester (FIO)](https://fio.readthedocs.io/en/latest/fio_doc.html).   
**Backup diagnostics** | On-demand |  This tests the performance of the Backint based backup and recovery operations for SAP HANA workloads. It includes testing your network connection and access to the Cloud Storage bucket that you've configured for use with the agent's Backint feature. For more information, see [self diagnostic](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#self_diagnostics). It also runs the [`gsutil perfdiag` diagnostic](https://docs.cloud.google.com/storage/docs/gsutil/commands/perfdiag).   
**Guest OS diagnostics** | Default |  For workloads running on Compute Engine bare metal instances, the tool checks whether the guest OS is configured for the optimal running of SAP workloads. This is done by running the `configureinstance -check` command. For more information, see [Configure guest OS on bare metal instances](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-bare-metal-instances).   
  
The output of this tool is a ZIP file that contains the diagnostic information that you specify the tool to gather.

For information about how to use this tool to gather diagnostic information for sharing with Customer Care, see [Gather diagnostic information about SAP workload performance](https://docs.cloud.google.com/sap/docs/getting-support-diag-info-performance).

## Pricing

Google Cloud's Agent for SAP is free to install and run. However, you are responsible for the charges that result from reading and writing metric data to Cloud Monitoring.

For pricing information related to the Backint feature of the agent, see [Monthly cost estimate](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#monthly_cost_estimate).

For the metrics collected by the agent, Monitoring charges according to the following:

  * Monitoring API read calls that exceed the free monthly API allotment.
  * Metrics measured by bytes ingested, when the ingested metric data exceeds the free monthly metric allotment.



In Monitoring, _ingestion_ refers to the process of writing time series to Monitoring. Each time series includes some number of data points; those data points are the basis for ingestion charges. For the pricing information, see [Monitoring Pricing](https://docs.cloud.google.com/monitoring#pricing).

For information about the general concepts in Monitoring, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

## Monthly cost estimates

This section illustrates how to estimate monthly costs for collecting metric data for metrics charged by API read calls and bytes ingested. For estimating the cost of using the Backint feature of Google Cloud's Agent for SAP to perform backup and recovery operations for SAP HANA, see [Monthly cost estimate](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#monthly_cost_estimate).

The examples in this section are based on Monitoring pricing as of December, 2022. These examples are intended to illustrate calculations; for comprehensive estimates, use the [Pricing Calculator](https://cloud.google.com/products/calculator).

The following table summarizes monthly cost estimates for some required and optional features of the agent. For the detailed steps for cost estimation, see SAP Host Agent metrics, Process Monitoring metrics, and SAP HANA monitoring metrics.

**Note:** From agent version 3.2, you don't incur any additional cost for using the agent to collect the Workload Manager evaluation metrics.Feature | Type | Number of Compute Engine instances | Cost ($)  
---|---|---|---  
SAP Host Agent metrics collection | Required | 100 | $209  
Process Monitoring metrics collection | Optional | 100 | $202.70  
SAP HANA monitoring metrics collection | Optional | 500 | $280.30  
  
### Pricing example for metrics charged by API read calls

The following example illustrates how to get an estimate of costs for collecting metric data for metrics charged by API read calls, such as SAP Host Agent metrics.

#### SAP Host Agent metrics

Consider a scenario where you have some number of Compute Engine instances that make some number of API read calls each month. The variables in the scenario include the following:

  * The rate at which a compute instance makes API read calls.
  * The number of compute instances.



For this cost estimation, consider there are roughly 43,800 minutes in a month.

60 * 730 hours (365 days / 12 months * 24 hours)

Assume that a compute instance makes API read calls at the rate of **5 calls per minute**.

For one compute instance, total API read calls at the rate of **5 calls per minute** for one month: 219,000 (43,800 * 5)

Consider that you have **100** compute instances.

  * Total number of API read calls per month: 21,900,000 

(219,000 * 100)

  * Number of API read calls per month after free allotment: 20,900,000 

(21,900,000 - 1,000,000 = 20,900,000)

  * Approximate cost per month for **100** compute instances: **$209**

(20,900,000 / 1000) * 0.01


| No. of reads | Rate ($/1000 reads) | Cost ($)  
---|---|---|---  
Free allotment/month | 1,000,000 | 0.00 | $0.00  
Chargeable | 20,900,000 | 0.01 | $209  
Total | 21,900,000 |  | $209  
  
### Pricing example for metrics charged by bytes ingested

The following examples illustrate how to get a cost estimate for collecting metric data for the metrics charged by bytes ingested, such as Process Monitoring metrics and SAP HANA monitoring metrics.

#### Process Monitoring metrics

Consider a scenario where you have some number of Compute Engine instances that are writing data from some number of metrics each month. The variables in the scenario include the following:

  * The rate at which the metric data is written.
  * The number of metrics.
  * The number of Compute Engine instances.



For this cost estimation, consider that there are roughly 44 Process Monitoring metrics being collected, of which 40 are [slow-changing metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring#pm_metric_types) and 4 are _fast-changing_ metrics. Also, consider that there are roughly 43,800 minutes in a month.

60 * 730 hours (365 days / 12 months * 24 hours)

For one fast-changing metric, writing data at the rate of **1 data point per 30 seconds** , that is, **2 data points per minute** for one month:

For one slow-changing metric, writing data at the rate of **1 data point per 120 seconds** , that is, **0.5 data points per minute** for one month:

  * Total fast-changing metrics data points is: 87,600 (43,800 minutes * 2 data points)
  * Total slow-changing metrics data points is: 21,900 (43,800 minutes * 0.5 data points)
  * Total volume ingested for each fast-changing metric is: 
    * 700,800 bytes (87,600 data points * 8 bytes)
    * This is 0.66833496 MiB (700,800 bytes / 1,048,576 bytes/MiB)
  * Total volume ingested for each slow-changing metric is: 
    * 175,200 bytes (87,600 data points * 8 bytes)
    * This is 0.16708374 MiB (175,200 / 1,048,576 bytes/MiB)



Consider that you have **100** compute instances, each writing 44 metrics.

  * Total monthly ingestion for fast-changing metrics: 267.3339844 MiB 

0.66833496 for one fast-changing metric * 400 (100 compute instances * 4 metrics)

  * Total monthly ingestion for slow-changing metrics: 668.3349609 MiB 

0.16708374 MiB for one slow-changing metric * 4000 (100 compute instances * 40 metrics)

  * Total monthly ingestion: 935.6689453 MiB 

Total monthly ingestion for fast-changing metrics + Total monthly ingestion for slow-changing metrics

  * Approximate cost per month for **100** compute instances: **$202.70**

(935.6689453 - 150) * 0.258


|  **MiB ingested** |  **Rate ($/MiB)** |  **Cost ($)**  
---|---|---|---  
Free allotment/month | 150 | 0.00 | $0.00  
Chargeable | 785.6689453 | 0.258 | $202.70  
Total | 935.6689453 | N/A | $202.70  
  
#### SAP HANA monitoring metrics

Consider a scenario where you have some number of Compute Engine instances that are writing data from querying SAP HANA databases each month. The variables in the scenario include the following:

  * The rate at which the metric data is written.
  * The number of queries.
  * The number of metrics collected for each query.
  * The number of Compute Engine instances deployed.
  * The number of SAP HANA database deployments per compute instance.



By default, Google Cloud's Agent for SAP has 12 built-in queries as part of its SAP HANA monitoring feature. The agent runs these queries once every 300 seconds (the default sample interval) on each SAP HANA database instance. These 12 queries generate a total of 37 metrics. Assume that each compute instance hosts only one SAP HANA database. Therefore, each compute instance writes a total of 37 metrics every 300 seconds.

For this cost estimation, consider that there are roughly 43,800 minutes in a month.

60 * 730 hours (365 days / 12 months * 24 hours)

For one metric, writing data at the rate of **1 data point per 300 seconds** , that is, **0.2 data points per minute** for one month:

  * Total data points is: 8,760 (43,800 minutes * 0.2 data points)
  * Total volume ingested is: 
    * 70,080 bytes (8,760 data points * 8 bytes)
    * This is 0.0668335 MiB (70,080 bytes / 1,048,576 bytes/MiB)



Consider that you have **500** compute instances, each writing **37** metrics.

  * Total monthly ingestion: 1236.419678 MiB 

0.0668335 MiB for one metric * 18,500 (500 compute instances * 37 metrics)

  * Approximate cost per month 500 compute instances: $280.30 

(1236.419678 - 150) * 0.258


| MiB ingested | Rate ($/MiB) | Cost ($)  
---|---|---|---  
Free allotment/month | 150 | 0.00 | $0.00  
Chargeable | 1,086.419678 | 0.258 | $280.30  
Total | 1,236.419678 |  | $280.30  
  
## Resources consumed by the agent

To help you evaluate the resources that Google Cloud's Agent for SAP consumes for collecting metrics, this section shows sample usages of the agent and the resources that they consumed in Google Cloud's test system with the following specifications:

  * Machine type: `n2-highmem-64`
  * Type of persistent storage disk attached to the Compute Engine instance: SSD Persistent Disk (`pd-ssd`)
  * SAP systems running on the compute instance: One instance of SAP HANA and two instances of SAP NetWeaver.



Note that the information in the following table is indicative and that the resources consumed by your agent instances can vary.

| Example 1 | Example 2 | Example 3 | Example 4  
---|---|---|---|---  
**Compute instance runtime** | 24 hours | 24 hours | 24 hours | 24 hours  
**Is SAP Host Agent metrics collection enabled?** | Yes | Yes | No* | No*  
**Is Process Monitoring metrics collection enabled?** | Yes, at the default interval of 30 seconds for fast-changing metrics and 120 seconds for slow-changing metrics | Yes, at the default interval of 30 seconds for fast-changing metrics and 120 seconds for slow-changing metrics | No | No  
**Is Workload Manager evaluation metrics collection enabled?** | Yes | Yes | Yes | No  
**Is SAP HANA monitoring metrics collection enabled?** | Yes | No | No | Yes, at the default interval of 300 seconds  
**CPU usage** | Less than 520 milliseconds per minute of a vCPU. This stays constant even as more vCPUs are added. | Less than 500 milliseconds per minute of a vCPU. This stays constant even as more vCPUs are added. | Less than 30 milliseconds per minute of a vCPU. This stays constant even as more vCPUs are added. | Less than 20 milliseconds per minute of a vCPU core. This stays constant even as more vCPUs are added.  
**Memory usage** | Less than 40 MB | Less than 50 MB | Less than 40 MB | Less than 29 MB  
**Disk writes** | Less than 70 KB per minute† | Less than 70 KB per minute† | Less than 6 KB per minute† | Less than 5 KB per minute†  
**Disk reads** | Zero | Zero | Zero | Zero  
**Network usage (steady state)** | Less than 2 MB per minute | Less than 2 MB per minute | Less than 600 bytes per minute | Less than 1 MB per minute  
  
*SAP Host Agent metrics collection is disabled only to test the consumption of resources. You must not disable the collection of SAP Host Agent metrics because it is mandated by SAP. 

† Agent logs set at the `INFO` level. 

## Supported operating systems

Google Cloud's Agent for SAP supports all operating systems that are supported by SAP NetWeaver and SAP HANA. For details, see the [list of supported operating systems for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table) and [list of supported operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-os-support).

## Authentication and access

Google Cloud's Agent for SAP requires an Identity and Access Management (IAM) [service account](https://docs.cloud.google.com/iam/docs/service-accounts) for authentication with Google Cloud and for permission to access Google Cloud resources.

IAM [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) that are assigned to the service account determine which Google Cloud resources the agent has permission to interact with.

Unless you use an existing or default service account, you need to create the service account in your Google Cloud project and assign one or more roles to the service account.

### Specify a service account

If the agent is running on a Compute Engine instance, then the agent uses the service account of the host compute instance by default. The host compute instance's service account is usually a service account with limited roles that you or one of your colleagues create, but it can instead be the Compute Engine default service account, which has broad permissions by default.

If the agent is not running on a Compute Engine instance, then you need to create a service account with a JSON service account key. For information, see [Set up a service account](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-bms#set_up_service_account).

For more information about service accounts, roles, and permissions, see:

  * [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts)
  * [Compute Engine Access control overview](https://docs.cloud.google.com/compute/docs/access)
  * [Monitoring IAM overview](https://docs.cloud.google.com/monitoring/access-control#overview)



### Required IAM roles

Whether you use a new, existing, or default service account, the service account must include roles that grant the required permissions to the agent.

Feature | Required IAM roles  
---|---  
Collection of SAP Host Agent metrics |  For collecting SAP Host Agent metrics on Compute Engine instances, the following predefined IAM roles are required:

  * [Compute Viewer (`roles/compute.viewer`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.viewer): grants permission to get and list Compute Engine resources, without being able to read the data stored on them.
  * [Monitoring Viewer (`roles/monitoring.viewer`)](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc): grants permission to view Cloud Monitoring data.

For collecting SAP Host Agent metrics on a Bare Metal Solution server, the agent does not access the Google Cloud APIs, and so it does not require an IAM service account or permissions.  
Collection of Workload Manager evaluation metrics |  The following predefined IAM roles are required:

  * [Workload Manager Insights Writer (`roles/workloadmanager.insightWriter`)](https://docs.cloud.google.com/workload-manager/docs/access-control#workloadmanager.insightWriter). This role grants permission to update workloads.
  * If you use Secret Manager to store credentials such as the password for the SAP HANA database user, then you also need the role [ Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`)](https://docs.cloud.google.com/secret-manager/docs/access-control#secretmanager.secretAccessor). This role grants permission to access secrets that are stored in Secret Manager.

**Warning:** Giving Secret Manager access to the [ Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) increases the security risk. Instead, we recommend that you create a [ single-purpose service account](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#single-purpose) with necessary permissions and [limit user's shell access to compute instances](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#shell-access).  
Collection of Process Monitoring metrics or the SAP HANA monitoring metrics |  The following predefined IAM roles are required:

  * [Compute Viewer (`roles/compute.viewer`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.viewer): grants permission to get and list Compute Engine resources, without being able to read the data stored on them.
  * [Monitoring Viewer (`roles/monitoring.viewer`)](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc): grants permission to view Cloud Monitoring data.
  * [Monitoring Metric Writer (`roles/monitoring.metricWriter`)](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc): grants permission to write metrics to Cloud Monitoring.
  * If you use Secret Manager to store credentials such as the password for the SAP HANA database user, then for collecting the Process Monitoring metrics for SAP HANA, or the SAP HANA monitoring metrics, you also need the role [ Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`)](https://docs.cloud.google.com/secret-manager/docs/access-control#secretmanager.secretAccessor). This role grants permission to access secrets that are stored in Secret Manager.

**Warning:** Giving Secret Manager access to the [ Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) increases the security risk. Instead, we recommend that you create a [ single-purpose service account](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#single-purpose) with necessary permissions and [limit user's shell access to compute instances](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#shell-access).  
Backint based backup and recovery for SAP HANA | 

  * [Storage Object Admin (`roles/storage.objectAdmin`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles): grants list, get, create, and delete permissions for objects in Cloud Storage buckets. For information about controlling access to Cloud Storage buckets, managed folders, and objects, see [Use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).
  * [Cloud KMS CryptoKey Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter), if you have used a customer-managed encryption key to encrypt your SAP HANA backups in Cloud Storage. For information about this feature, see [Encryption options for backups](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#encryption_options_for_backups). 

  
  
### Access to Google Cloud APIs

Compute Engine recommends configuring your instances to allow full access to all Cloud APIs and using only the IAM permissions of the instance service account to restrict access to Google Cloud resources. For more information, see [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

If you limit access to the Cloud APIs on a compute instance, then:

  * For the collection of SAP Host Agent metrics, Google Cloud's Agent for SAP requires the following minimum Google Cloud API access scopes on the host compute instance: 
    * **Compute Engine** : **Read Only**
    * **Stackdriver Monitoring API** : **Read Only**
  * For the collection of Workload Manager evaluation metrics, or retrieval of credentials from Secret Manager, the **Cloud Platform** access scope must be enabled.
  * For collecting the Process Monitoring metrics or the SAP HANA monitoring metrics, the access scopes of the host compute instance must have the write access to publish metric data to your Google Cloud projects. When you create a new Compute Engine instance, it is automatically configured with the write access scope, `https://www.googleapis.com/auth/monitoring.write`.
  * For information about the Cloud APIs that you need to access for using the agent to perform backup and recovery operations for SAP HANA, see [Enable access to Cloud APIs and metadata servers](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery#enable_api_ip_access).



If the agent is not running on a Compute Engine instance, then you need to establish connection to Google Cloud APIs. See [Configuring Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid) for details.

## Metrics in Monitoring

For the Process Monitoring metrics and the SAP HANA monitoring metrics, Google Cloud's Agent for SAP sends the data that it retrieves from your SAP systems to Monitoring as custom metric data. To send the data, the agent uses the Monitoring API, which is enabled by default when you create a Google Cloud project.

For an overview of Monitoring, see [Introduction to Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).

### Find the metrics data in Monitoring

The metrics data from Google Cloud's Agent for SAP is available to view as soon as Monitoring receives it. To find and visualize the collected data, you can use Metrics Explorer. For more information about finding the metrics data in Monitoring, see [Google Cloud's Agent for SAP Operations guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-verify-metrics).

For more information about visualizing the collected data in Monitoring, see:

  * [Using dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards)
  * [Filter charted data](https://docs.cloud.google.com/monitoring/charts/selecting-aggregating-metrics#filter-option)
  * [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer)
  * [Monitoring in the Google Cloud console](https://docs.cloud.google.com/monitoring)



### Dashboard definitions on GitHub

On GitHub, you can find the definitions for custom dashboards that help you visualize the metrics collected by Google Cloud's Agent for SAP in Cloud Monitoring. For more information, see:

  * For visualizing the Process Monitoring metrics, see [View the collected metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-process-monitoring#agent4sap_metrics_dashboards).
  * For visualizing the SAP HANA monitoring metrics, see [View the collected metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-sap-hana-monitoring#agent4sap_metrics_dashboards).



### Alert notifications

To alert you when a metric reaches a threshold that you define, you can configure alert notifications in Monitoring.

For more information, see [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts).

## Automatic installation

When you use the [Terraform](https://docs.cloud.google.com/sap/docs/tf-for-sap) configuration files that Google Cloud provides for automating the deployment of your Google Cloud infrastructure, Google Cloud's Agent for SAP is automatically installed as part of the deployment process. This is done to satisfy the SAP mandate of collecting the SAP Host Agent metrics.

For instructions for manually installing and configuring Google Cloud's Agent for SAP, see:

  * [Install and configure Agent for SAP on a single compute instance](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm)
  * [Install and manage Agent for SAP on a fleet of VMs](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-manage-on-vm-fleet)
  * [ Install and configure Agent for SAP on a Bare Metal Solution server](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-bms)



## Google Cloud's Agent for SAP codebase on GitHub

For security requirements of your enterprise, if required, you can review the source code of Google Cloud's Agent for SAP. The codebase of the agent is available in a read-only GitHub repository, `google-cloud-sap-agent` under [GoogleCloudPlatform/sapagent](https://github.com/GoogleCloudPlatform/sapagent).

## Support

For issues with Google Cloud infrastructure or services, contact Customer Care. You can find the contact information on the [Support Overview page](https://console.cloud.google.com/support) in the Google Cloud console. If Customer Care determines that a problem resides in your SAP systems, then you are referred to SAP Support.

For SAP product-related issues, log your support request with [SAP support](https://support.sap.com/support-programs-services/about/getting-started.html). SAP evaluates the support ticket and, if it appears to be a Google Cloud infrastructure issue, then SAP transfers that ticket to the appropriate Google Cloud component in its system: `BC-OP-LNX-GOOGLE` or `BC-OP-NT-GOOGLE`.

### Support requirements

Before you can receive support for SAP systems and the Google Cloud infrastructure and services that they use, you must meet the minimum support plan requirements.

For more information about the minimum support requirements for SAP on Google Cloud, see:

  * [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support)
  * [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406) (An SAP user account is required)



### Gather diagnostic information

Before contacting Customer Care for assistance in resolving issues related to Google Cloud's Agent for SAP, we recommend that you gather all relevant diagnostic information, notably the agent's [support bundle](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/getting-support-diag-info#support_bundle).

For more information about gathering diagnostic information for the agent, see [Google Cloud's Agent for SAP diagnostic information](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/getting-support-diag-info). 

## What's next

  * Read Google Cloud's Agent for SAP installation and configuration guides: 
    * [Install and configure Google Cloud's Agent for SAP on a compute instance](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm)
    * [Install and manage Agent for SAP on a fleet of VMs](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-manage-on-vm-fleet)
    * [Install and configure Google Cloud's Agent for SAP on a Bare Metal Solution server](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-bms)
  * Read [Google Cloud's Agent for SAP operations guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations)
  * [Learn more about Monitoring](https://docs.cloud.google.com/monitoring/docs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

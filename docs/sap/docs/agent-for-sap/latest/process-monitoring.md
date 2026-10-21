---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring/
title: Process monitoring using Google Cloud's Agent for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:49.439038+00:00
---

# Process monitoring using Google Cloud's Agent for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Process monitoring using Google Cloud's Agent for SAP Stay organized with collections  Save and categorize content based on your preferences. 

This planning guide focuses solely on the _Process Monitoring metrics collection_ feature of Google Cloud's Agent for SAP. For information about the agent and all its features, see [Google Cloud's Agent for SAP planning guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning).

On Linux, Google Cloud's Agent for SAP can help you monitor the processes in your SAP applications and their runtime states. This is delivered through the collection of [Process Monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#process_monitoring_metrics), which you can enable after installing the agent on your Compute Engine instances or Bare Metal Solution servers.

**Note:** The collection of Process Monitoring metrics is supported only on Linux. It is not supported on Windows.

The information collected in the Process Monitoring metrics helps you troubleshoot the issues related to your SAP system. In case of issues, with the help of Process Monitoring metrics, Cloud Customer Care can help you reach a resolution more efficiently. The data collected using Process Monitoring metrics provide observability for your SAP HANA high-availability cluster configurations.

For information about how to configure Google Cloud's Agent for SAP to collect the Process Monitoring metrics, see [Configure Process Monitoring metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-process-monitoring).

## Types of Process Monitoring metrics

From version 2.6 of Google Cloud's Agent for SAP, the Process Monitoring metrics collected by the agent are referred to as follows:

  * _Fast-changing_ metrics: This includes `/sap/hana/availability`, `/sap/hana/ha/availability`, `/sap/hana/ha/replication` and `/sap/nw/availability`. These metrics are collected at a default frequency of 30 seconds. This collection frequency can be updated using the configuration parameter `process_metrics_frequency`.
  * _Slow-changing_ metrics: Process Monitoring metrics other than the fast-changing ones are referred to as slow-changing. These metrics are collected at a default frequency of 120 seconds. This collection frequency can updated using the configuration parameter `slow_process_metrics_frequency`.



## Cloud Monitoring pricing

The Process monitoring metrics that Google Cloud's Agent for SAP collects and sends to Monitoring are classified by Monitoring as [_chargeable metrics_](https://cloud.google.com/stackdriver/pricing#metrics-chargeable) and priced by ingested volume.

The frequency at which the agent queries your SAP systems to collect the Process Monitoring metrics affects the volume of metrics that get sent to Monitoring.

Process Monitoring metrics are fast-changing metrics that are collected every 5 seconds by default.

For more information about Monitoring pricing, see [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing#monitoring-costs).

### Sample cost estimate

To see a sample cost estimate for the collection of the Process Monitoring metrics using Google Cloud's Agent for SAP, see [Pricing example for metrics charged by bytes ingested](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#pricing_example_for_metrics_charged_by_bytes_ingested).

## Process Monitoring metrics

The following table describes the Process Monitoring metrics collected by Google Cloud's Agent for SAP. The metric strings in this table must be prefixed with `workload.googleapis.com`. This prefix has been omitted from the entries in the following table.

**Metric** | **Category** | **Description**  
---|---|---  
`/sap/hana/service` | SAP HANA | Numeric response code for SAP HANA service availability. 

  * `0`: Service is not running
  * `1`: Service is running

  
`/sap/hana/ha/replication` | SAP HANA | Numeric response code for SAP HANA system replication, based on SAP System ID, SAP Instance Number, and SAP Service Name. 

  * `0`: Error occurred.
  * `10`: No system replication (standalone mode).
  * `11`: Error occurred on the connection.
  * `12`: The secondary system did not connect to the primary system since last restart of the primary system.
  * `13`: Initial data transfer is in progress. In this state, the secondary system is not usable at all.
  * `14`: The secondary system is syncing again. For example, after a temporary connection loss or restart of the secondary system.
  * `15`: Initialization or sync with the primary system is complete and the secondary system is continuously replicating. No data loss occurs in the `SYNC` mode.

  
`/sap/hana/availability` | SAP HANA | Numeric response code for SAP HANA system availability, based on SAP System ID and SAP Instance Number. 

  * `0`: One or more processes are not active
  * `1`: All processes are active

  
`/sap/hana/ha/availability` | SAP HANA | Numeric response code for SAP HANA system high availability state, based on SAP system ID and SAP Instance Number. 

  * `0`: Unknown state
  * `1`: Current node is secondary
  * `2`: Primary node has error
  * `3`: Primary node is online but replication is not fully functional
  * `4`: Primary node is online with replication running

  
`/sap/hana/query/state` | SAP HANA | Numeric response code that represents the health check of SAP HANA based on the query `select * from dummy`. The value 0 indicates success. Any other value indicates failures.  
`/sap/hana/query/overalltime` | SAP HANA | Reported only if `query/state` is `0`. This is the overall time taken by the query, including client side time and server side time, in microseconds.  
`/sap/hana/query/servertime` | SAP HANA | Reported only if `query/state` is `0`. This is the time taken by the server to process the query, in microseconds.  
`/sap/hana/log/utilisationkb` | SAP HANA | Specifies the disk space (KB) that the SAP HANA log volume is using. This metric is supported from version 3.8 of the agent.  
`/sap/cluster/failcounts` | SAP HANA | The failcount value of the Linux HA resources. If the resource is not present, then there is no failcount registered. Otherwise, the cluster monitoring `crm_mon` reports the number of failed actions.  
`/sap/cluster/nodes` | Pacemaker Cluster | Numeric response code that indicates the state of the Linux HA cluster state. 

  * `-10`: Unknown
  * `-1`: Unclean state
  * `0`: Shutdown
  * `1`: Standby
  * `2`: Online

  
`/sap/cluster/resources` | Pacemaker Cluster | Numeric response code that indicates if the Linux HA cluster resource is up and running. 

  * `-10`: Unknown
  * `0`: Failed
  * `1`: Stopped
  * `2`: Starting
  * `3`: Resource is in one of the following steady states: `Master`, `Slave`, or `Started`

  
`/sap/nw/availability` | SAP NetWeaver | Numeric response code for SAP NetWeaver system availability, based on SAP System ID, SAP Instance Number, and SAP Service Name. 

  * `0`: Unknown state
  * `1`: Current node is active or up

  
`/sap/nw/service` | SAP NetWeaver | Numeric response code for SAP NetWeaver service availability, based on SAP System ID, SAP Instance Number, and SAP Service Name. 

  * `0`: Service is not running
  * `1`: Service is running

  
`/sap/nw/icm/rcode` | SAP NetWeaver | Response code based on the HTTP 1.1 protocol of a non-authenticated ICM URL resource (local call).  
`/sap/nw/icm/rtime` | SAP NetWeaver | Response time in milliseconds of a non-authenticated ICM URL resource (local call).  
`/sap/nw/ms/rcode` | SAP NetWeaver | Response code based on the HTTP 1.1 protocol of a non-authenticated Message Server URL resource (local call).  
`/sap/nw/ms/rtime` | SAP NetWeaver | Response time in milliseconds of a non-authenticated Message Server URL resource (local call).  
`/sap/nw/ms/wp` | SAP NetWeaver | Number of the ABAP work processes (NW ABAP) or Java server nodes (NW Java) reported by the Message Server information page.  
`/sap/nw/abap/proc/busy` | SAP NetWeaver | Number of the busy ABAP work processes by type, such as DIA, ICM, and DISP.  
`/sap/nw/abap/proc/count` | SAP NetWeaver | Number of the all ABAP work processes by type, such as DIA, ICM, and DISP.  
`/sap/nw/abap/queue/current` | SAP NetWeaver | The current number of ABAP queues used by the ABAP work processes, grouped by the work process types such as `DIA`, `ICM`, and `DISP`.  
`/sap/nw/abap/queue/peak` | SAP NetWeaver | The peak number of ABAP queues used by the ABAP work processes, grouped by the work process types such as `DIA`, `ICM`, and `DISP`.  
`/sap/nw/abap/sessions` | SAP NetWeaver | Number of the ABAP sessions by session type.  
`/sap/nw/abap/rfc` | SAP NetWeaver | Number of the ABAP RFC connections by session type.  
`/sap/nw/enq/locks/usercountowner` | SAP NetWeaver | Number of enqueue locks in SAP NetWeaver systems. If your system has a lot of open lock entries, then it can lead to performance issues for your users.  
`/sap/mntmode` | Additional SAP metrics | Maintenance mode of the corresponding SAP System ID (SID) that has been set manually to indicate that the system is intentionally down (`maintenancemode = TRUE`). The value of this metric is used to suppress the alerts for the systems that are unavailable during planned maintenance. To notify the agent if a particular SID is undergoing planned maintenance, run the following command:
    
    
    google_cloud_sap_agent maintenance \
        --enable=TRUE or FALSE \
        --sid=SID  
  
`/sap/service/_failed` | Additional SAP metrics | Indicates if the OS services related to SAP and cluster services failed. The exit code `0` represents a failure.  
`/sap/service/is_disabled` | Additional SAP metrics | This metric is populated when the `pacemaker`, `corosync`, `sapconf`, `saptune`, and `sapinit` services are not enabled.  
`/sap/hana/cpu/utilization` | Additional SAP metrics | Per-process CPU utilization (%) of SAP HANA processes.  
`/sap/nw/cpu/utilization` | Additional SAP metrics | Per-process CPU utilization (%) of SAP NetWeaver processes.  
`/sap/control/cpu/utilization` | Additional SAP metrics | Per-process CPU utilization (%) of SAP Control processes.  
`/sap/hana/memory/utilization` | Additional SAP metrics | Per-process memory utilization (MB) of the HANA processes.  
`/sap/nw/memory/utilization` | Additional SAP metrics | Per-process memory utilization (MB) of the NetWeaver processes.  
`/sap/control/memory/utilization` | Additional SAP metrics | Per-process memory utilization (MB) of the SAP Control processes.  
`/sap/hana/iops/reads` | Additional SAP metrics | Per-process read IOPS for SAP HANA processes.  
`/sap/hana/iops/writes` | Additional SAP metrics | Per-process write IOPS for SAP HANA processes.  
`/sap/nw/iops/reads` | Additional SAP metrics | Per-process read IOPS for SAP NetWeaver processes.  
`/sap/nw/iops/writes` | Additional SAP metrics | Per-process write IOPS for SAP NetWeaver processes.  
`/sap/infra/migration` | Google Cloud infrastructure metrics | Indicates if a Compute Engine instance is undergoing a [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).   
`/sap/pacemaker` | Additional SAP metrics | Numeric response code that conveys if the host includes a Pacemaker configuration. 

  * `0`: No Pacemaker configuration found
  * `1`: Pacemaker configuration found

This metric is supported from version 3.2 of the agent.  
`/sap/hana/volumes` | Additional SAP metrics |  Exposes the following information about the mounted SAP HANA volumes: total size of the volume, used storage, available storage, and storage usage percentage. This metric is supported from version 3.2 of the agent.  
`/sap/networkstats/rtt` | Additional SAP metrics | The average round trip time, in milliseconds. This metric contains TCP connection information related to your SAP HANA system. This metric is collected for sockets of SAP HANA `hdbnameserver` process using the `ss` utility.  
`/sap/networkstats/rcv_rtt` | Additional SAP Metrics | The time taken by the remote client to exhaust the current advertized remote receive window (RWIN) if no userspace consumption of that data has occurred. It is based on the observed bandwidth of the connection and returns a non-zero value. This metric contains TCP connection information related to your SAP HANA system. This metric is collected for sockets of SAP HANA `hdbnameserver` process using the `ss` utility.  
`/sap/networkstats/rto` | Additional SAP Metrics | The TCP re-transmission timeout, in milliseconds. This metric contains TCP connection information related to your SAP HANA system. This metric is collected for sockets of SAP HANA `hdbnameserver` process using the `ss` utility.  
`/sap/networkstats/bytes_acked` | Additional SAP Metrics | The number of bytes acknowledged. This metric contains TCP connection information related to your SAP HANA system. This metric is collected for sockets of SAP HANA `hdbnameserver` process using the `ss` utility.  
`/sap/networkstats/bytes_received` | Additional SAP Metrics | The number of bytes received. This metric contains TCP connection information related to your SAP HANA system. This metric is collected for sockets of SAP HANA `hdbnameserver` process using the `ss` utility.  
`/sap/networkstats/lastsnd` | Additional SAP Metrics | The time, in milliseconds, since the last packet was sent. This metric contains TCP connection information related to your SAP HANA system. This metric is collected for sockets of SAP HANA `hdbnameserver` process using the `ss` utility.  
`/sap/networkstats/lastrcv` | Additional SAP Metrics | The time, in milliseconds, since the last packet was received. This metric contains TCP connection information related to your SAP HANA system. This metric is collected for sockets of SAP HANA `hdbnameserver` process using the `ss` utility.  
`/sap/compute/os/memory/mem_free_kb` | Compute resources | The amount of memory (KB) that is left unused on the compute instance. This doesn't include buffer or cache memory.  
`/sap/compute/os/memory/mem_available_kb` | Compute resources | An estimate of the memory (KB) that is available on the compute instance for starting new applications, without swapping.  
`/sap/compute/os/memory/mem_total_kb` | Compute resources | The total usable memory (KB) that is available on the compute instance.  
`/sap/compute/os/memory/buffers_kb` | Compute resources | The amount of memory (KB) used by kernel buffers.  
`/sap/compute/os/memory/cached_kb` | Compute resources | The amount of memory (KB) used by the page cache and slabs.  
`/sap/compute/os/memory/swap_cached_kb` | Compute resources | The amount of memory (KB) used by the swap space as cache.  
`/sap/compute/os/memory/commit_kb` | Compute resources | The amount of memory (KB) that is committed to the processes of your SAP system.  
`/sap/compute/os/memory/commit_percent` | Compute resources | The percentage of the memory that is committed to the processes of your SAP system.  
`/sap/compute/os/memory/active_kb` | Compute resources | The amount of memory (KB) that has been used more recently and is usually not reclaimed unless required.  
`/sap/compute/os/memory/inactive_kb` | Compute resources | The amount of memory (KB) that has been used more recently and is more eligible to be reclaimed for other purpose.  
`/sap/compute/os/memory/dirty_kb` | Compute resources | The amount of memory (KB) that is waiting to be written back to disk.  
`/sap/compute/os/memory/shmem_kb` | Compute resources | The amount of memory (KB) that is consumed in `tmpfs` filesystems.  
`/sap/compute/os/memory/freemem_total` | Compute resources | The amount of memory (KB) provisioned on the compute instance and usable by the OS.  
`/sap/compute/os/memory/freemem_used` | Compute resources | The amount of memory (KB) being actively used by the kernel and running SAP applications.  
`/sap/compute/os/memory/freemem_free` | Compute resources | The amount of memory (KB) that is unused and readily available.  
`/sap/compute/os/memory/freemem_shared` | Compute resources | The amount of memory (KB) that is shared between the processes running on the compute instance.  
`/sap/compute/os/memory/freemem_buff/cache` | Compute resources | The amount of memory (KB) that is used by the kernel for buffers and page cache.  
`/sap/compute/os/memory/freemem_available` | Compute resources | The amount of memory (KB) that is available for starting new applications without causing the system to swap.  
`/sap/compute/os/memory/freeswap_total` | Compute resources | The amount of swap space (KB) that is configured on your compute instance.  
`/sap/compute/os/memory/freeswap_used` | Compute resources | The amount of swap space (KB) that is being used.  
`/sap/compute/os/memory/freeswap_free` | Compute resources | The amount of swap space (KB) that is unused and available.  
  
## Viewing metrics in Monitoring

Google Cloud provides custom dashboards that help you visualize the Process Monitoring metrics collected by Google Cloud's Agent for SAP. See the `dashboards/google-cloud-agent-for-sap` directory in the [GoogleCloudPlatform/monitoring-dashboard-samples](https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples/tree/master/dashboards/google-cloud-agent-for-sap) repository on GitHub.

For information about these dashboards, including installation instructions, see [View the collected metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-process-monitoring#agent4sap_metrics_dashboards).

For information about finding metrics data in Monitoring and configuring alert notifications, see [Metrics in Monitoring](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#metrics_monitoring).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/sap/docs/known-issues/
title: Known issues \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:33.340122+00:00
---

# Known issues  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Resources ](https://docs.cloud.google.com/sap/docs/resources)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

This page describes known issues that you might experience while running SAP systems on Google Cloud. Understanding these issues, the underlying causes, and their resolutions, lets you troubleshoot problems and helps in ensuring the reliability of your SAP system.

The page includes only those issues that have come to the attention of the SAP specialists on the Cloud Customer Care team. Other issues that can impact your SAP systems might be listed in the documentation of the underlying Google Cloud products and services. For example, issues that are related to Compute Engine instances, Hyperdisk or Persistent Disk volumes, or OS images, are listed on the [Compute Engine known issues page](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues).

This page is intended for cloud architects, network engineers, and developers who help you run and manage SAP solutions.

## Changes to the default fencing method can cause fencing timeout in RHEL 8.4

If you are using RHEL 8.4 with the fence agent `fence-agents-gce` versions `4.2.1-65` to `4.2.1-69`, then a fencing timeout might occur.

The fence agent `fence-agents-gce` versions `4.2.1-65` to `4.2.1-69`, do not define the default fencing method `cycle`. As a result, the default fencing method falls back to the `onoff` method. This causes the fencing agent to make a `stop` API call and a `start` API call instead of a single `reset` API call. So, the fencing process takes longer to access the APIs, which can lead to a fencing timeout.

### Resolution

To resolve this issue, try the following options:

  * Change the default fencing method to `cycle` using the following command:
        
        pcs resource update <STONITH_device_name> method=cycle
        

  * Check your `fence-agents-gce` version and make sure that you are using the version `4.2.1-70` or later:

    * To check your fence agent version, run the following command:
    
    yum info fence-agents-gce
    

    * To update your fence agent, run the following command:
    
    yum --releasever=8.6 update fence-agents-gce
    




## SAP HANA scale-out deployment fails due to a Python error

If you are installing SAP HANA 2.0 SPS 5 Revision 56 or later for an SAP HANA scale-out system with host auto-failover, the SAP HANA scale-out with host auto-failover deployment fails due to a Python error in the storage manager for SAP HANA. The SAP HANA trace log files show the following Python error for this failure: `failed with python error: _sap_hana_forbid() got an unexpected keyword argument 'stdout'`.

### Resolution

Use version 2.2 or later of the storage manager for SAP HANA. Version 2.2 adds support for SAP HANA 2.0 SPS 5 Revision 56 and later. For more information about the storage manager for SAP HANA, see [SAP HANA host auto-failover on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#host_auto_failover).

## High-availability cluster failover issue due to a Corosync communication delay

For your high-availability (HA) cluster for SAP HANA on Google Cloud, failover can be incorrectly triggered due to a temporary delay in the transmission of Corosync messages between the cluster nodes.

This issue occurs on both SUSE and Red Hat high-availability Linux distributions.

This issue is not specific to Google Cloud, but is described here because it has impacted SAP on Google Cloud users.

### Resolution

The resolution of the issue is different depending on your operating system.

#### SUSE

SUSE provided a Corosync maintenance update that solves the problem. To apply the fix, update your Corosync software to one of the versions that are listed in the following table.

**Note:** The information in the following table is provided for your convenience. For the authoritative information, see the [SUSE knowledge base article](https://www.suse.com/support/kb/doc/?id=000020407).SUSE version | Corosync version  
---|---  
SLES 12 - all SP releases | `corosync-2.3.6-9.19.1`  
SLES 15 | `corosync-2.4.5-5.13.1`  
SLES 15 SP1 | `corosync-2.4.5-9.16.1`  
SLES 15 SP2 | `corosync-2.4.5-10.14.6.1`  
SLES 15 SP3 | `corosync-2.4.5-12.3.1`  
SLES 15 SP4 | `corosync-2.4.5-12.7.1`  
  
#### Red Hat

Red Hat provided a Corosync maintenance update that solves the problem. To apply the fix, update your Corosync software to one of the versions that are listed in the following table.

**Note:** The information in the following table is provided for your convenience. For the authoritative information, see the [Red Hat knowledge base article](https://access.redhat.com/solutions/6310541).Red Hat version | Corosync version  
---|---  
RHEL 7 | `corosync-2.4.5-7.el7_9.2`  
RHEL 8 | `corosync-3.1.5-2.el8`  
  
## gVNIC reset on RHEL causes failover in HA configuration

If you are using the gVNIC network driver in combination with versions of RHEL prior to 8.7, then you might experience a gVNIC reset causing the concerned VM to lose network connectivity for a couple of seconds, which might result in undesired failovers in your HA cluster.

You might observe a kernel call stack being generated in the messages log file of the OS, for example:
    
    
      Feb  4 06:58:33  kernel: ------------[ cut here ]------------
      Feb  4 06:58:33  kernel: NETDEV WATCHDOG: eth0 (gvnic): transmit queue 0 timed out
      Feb  4 06:58:33  kernel: WARNING: CPU: 51 PID: 0 at net/sched/sch_generic.c:447 dev_watchdog+0x272/0x280
      Feb  4 06:58:33  kernel: Modules linked in: falcon_lsm_serviceable(PE) falcon_nf_netcontain(PE) falcon_kal(E) falcon_lsm_pinned_16206(E) binfmt_misc nft_fib_inet nft_fib_ipv4 nft_fib_ipv6 nft_fib nft_reject_inet nf_reject_ipv4 nf_reject_ipv6 nft_reject nft_ct nf_tables_set nft_chain_nat nf_nat nf_conntrack nf_defrag_ipv6 nf_defrag_ipv4 ip_set falcon_lsm_pinned_16108(E) nf_tables nfnetlink intel_rapl_msr intel_rapl_common nfit libnvdimm vfat fat dm_mod gve crct10dif_pclmul crc32_pclmul i2c_piix4 ghash_clmulni_intel rapl pcspkr auth_rpcgss sunrpc xfs libcrc32c crc32c_intel serio_raw nvme nvme_core t10_pi [last unloaded: falcon_kal]
      Feb  4 06:58:33  kernel: CPU: 51 PID: 0 Comm: swapper/51 Kdump: loaded Tainted: P            E    --------- -  - 4.18.0-305.82.1.el8_4.x86_64 #1
      Feb  4 06:58:33  kernel: Hardware name: Google Google Compute Engine/Google Compute Engine, BIOS Google 12/13/2023
      Feb  4 06:58:33  kernel: RIP: 0010:dev_watchdog+0x272/0x280
      ...
      Feb  4 06:58:33  kernel: ---[ end trace d6c7c7cb653cce9a ]---
      Feb  4 06:58:33  kernel: gvnic 0000:00:03.0: Performing reset
    

### Cause

The cause of this issue is that RHEL versions prior to 8.7 contain an earlier build of the gVNIC driver that doesn't have the required enhancements and stability patches.

### Resolution

Use an SAP-certified version of RHEL that is later than 8.7, in combination with the gVNIC driver. Doing so is particularly important if you're using a third generation machine from Compute Engine, such as [M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_series), because they don't support using the VirtIO driver, thus requiring you to use the gVNIC driver. For the full list of machine types that default to gVNIC, see the [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) table.

## Reduced replication performance for SAP HANA on X4 due to sub-optimal TCP congestion control settings

SAP HANA systems running on Compute Engine X4 instances experience reduced performance during system replication.

### Cause

This issue is caused by sub-optimal configuration of the TCP congestion control settings. Your configuration must include the TCP congestion control algorithm BBR to take full advantage of the bandwidth available to X4 instances.

### Resolution

To resolve this issue, complete the following steps:

  1. Establish a connection to your X4 instance by using SSH.

  2. View the instance's TCP congestion control settings:
         
         sysctl -a | grep tcp.*congestion
         

The output is similar to the following:
         
         net.ipv4.tcp_allowed_congestion_control = reno cubic
         net.ipv4.tcp_available_congestion_control = reno cubic
         net.ipv4.tcp_congestion_control = cubic
         

  3. Include the TCP congestion control algorithm BBR by updating Google Cloud's Agent for SAP to version 3.15 (latest) and running the `configureinstance` command:

### RHEL
         
         sudo yum check-update google-cloud-sap-agent
          sudo /usr/bin/google_cloud_sap_agent configureinstance -apply

### SLES
         
         sudo zypper list-updates -r google-cloud-sap-agent
          sudo /usr/bin/google_cloud_sap_agent configureinstance -apply

For more information about updating the agent and configuring the guest OS for optimal running of SAP HANA on X4 instances, see:

     * [Update Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-update)
     * [Configure guest OS on Compute Engine bare metal instances](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-bare-metal-instances)
  4. Verify that the updated TCP congestion control settings includes BBR:
         
         sysctl -a | grep tcp.*congestion
         

The output is similar to the following:
         
         net.ipv4.tcp_allowed_congestion_control = reno cubic **bbr**
         net.ipv4.tcp_available_congestion_control = reno cubic **bbr**
         net.ipv4.tcp_congestion_control = **bbr**




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

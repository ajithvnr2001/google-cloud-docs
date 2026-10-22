---
url: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/application-resilience/
title: Application resilience considerations \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:59.135458+00:00
---

# Application resilience considerations  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/application-resilience/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Application resilience considerations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes application resilience for Google Cloud NetApp Volumes and how NFS, SMB, and iSCSI clients handle I/O pauses. Although NetApp Volumes is highly available, I/O operations can briefly pause during planned maintenance or unplanned service events. This page also recommends timeout settings to help ensure smooth application operation, especially when you use cluster software such as [Pacemaker](https://clusterlabs.org/pacemaker/).

## Application resilience considerations

Although NetApp Volumes is highly available, planned maintenance events such as platform updates, service upgrades, software upgrades, or unplanned component failures in the service can lead to brief pauses in input and output (I/O) operations.

For more information about planned maintenance events and unplanned service outages, see [Monitor and plan for a maintenance event](https://docs.cloud.google.com/netapp/volumes/docs/monitor/maintenance-events).

For more information about how these maintenance events affect storage pool states, see [Storage pool states](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/overview#storage_pool_states).

## I/O pauses

Network File System (NFS), Server Message Block (SMB), and iSCSI client software inside your operating system handles short I/O pauses. The client waits and retries the I/O operations without bringing the issue up to the application. Such short pauses are considered non-disruptive because while the application's users might see longer response times, the application doesn't report I/O errors.

For longer I/O pauses, the behavior depends on your operating system's NFS, SMB, or iSCSI client and potential timeouts configured in the application. The following sections discuss protocol-specific details for I/O pauses.

### NFS I/O pauses

All calls to an unavailable, hard-mounted NFS share are blocked in the NFS client and wait indefinitely until the NFS server responds again. While your NFS client waits, messages appear in your client logs that indicate the NFS server isn't responding.

From an application perspective, I/O operations such as read or write are blocked and remain outstanding until the NFS share returns successfully. During I/O pauses, no I/O operation is ever lost and NetApp Volumes ensures data consistency, unless you forcefully stop outstanding I/O operations on the client side.

#### Use cluster software applications to automate failovers

If you use cluster software applications such as [Pacemaker](https://clusterlabs.org/pacemaker/) on the client VMs to automate failover of your application, configure your timeouts for NFS shares to withstand NetApp Volumes maintenance events. Such failovers abort outstanding I/O operations on the client and can lead to lost transactions. We recommend the following timeouts:

Protocol type | Recommended timeout | Notes  
---|---|---  
NFSv3 shares | 60 seconds (for Standard, Premium, Extreme, and Flex Unified service levels)   
  
120 seconds (for Flex File service level)  | We recommend that you use a fencing method, which uses the `nolock` mount option instead of relying on NFS locks.  
NFSv4.1 | 105 seconds (for Standard, Premium, Extreme, and Flex Unified service levels)   
  
165 seconds (for Flex File service level)  | The NFSv4.1 protocol automatically adds reliable locking over NFSv3 ([NFSv4.x RFC](https://datatracker.ietf.org/doc/rfc7530/), section 9.6.2), which you can use as a fencing mechanism. Lock state recovery adds an additional 45 seconds.  
  
### SMB share I/O pauses

Unlike NFS, SMB sessions use a connection that can time out. NetApp Volumes typically avoids timeouts.

#### Session timeouts

The session timeout is defined at the client. The default timeout for Windows clients is 60 seconds. You can run the `Get-SmbClientConfiguration/Set-SmbClientConfiguration` command using the `SessionTimeout` parameter to read or change the session timeout.

If a session timeout occurs, the SMB session breaks and an I/O error is reported to the application doing the I/O. File Explorer or Microsoft 365 applications usually reconnect as soon as the user accesses the SMB share again. When running into I/O errors, some applications attempt to reconnect and retry the failed I/O operation, while others don't. Refer to your application vendor's documentation to understand how the application handles SMB timeouts and operates resiliently on SMB shares.

Continuously available (CA) shares are an SMB3.x feature that improves failover resilience for database-like applications. NetApp Volumes supports continuously available shares for Microsoft SQL Server and FSLogix.

Failure recovery improves with every new SMB version. NetApp Volumes supports SMB 2.1, 3.0, and 3.1.1. If possible, use the latest supported SMB version. Windows 10/Server 2016 and later support the latest SMB version 3.1.1.

#### SMB application-based precautions

Certain SMB-based applications require SMB Transparent Failover. SMB Transparent Failover enables maintenance operations on SMB volumes within NetApp Volumes without interrupting connectivity to server applications that store and access data. NetApp Volumes supports the SMB continuously available shares option to make sure specific applications support SMB Transparent Failover. Using SMB continuously available shares supports only the following workloads:

  * FSLogix user profile containers

  * Microsoft SQL Server (not Linux SQL Server)




SMB continuously available shares doesn't support custom applications.

### iSCSI I/O pauses

In both Linux and Windows environments, iSCSI clients (initiators) handle I/O pauses by retrying commands until the target (NetApp Volumes) becomes available. During short maintenance events, the iSCSI initiator attempts to reconnect and resume outstanding I/O operations, which helps maintain application resilience.

#### iSCSI timeouts

Proper configuration of iSCSI timeouts is essential to maintain application resilience during maintenance events or unexpected service interruptions.

For Linux systems, NetApp Volumes uses the default iSCSI initiator settings. These settings include NetApp-specific configurations within the default Linux Device Mapper Multipath, which automatically manages timeout requirements during NetApp Volumes maintenance events.

However, for Windows systems, modify the Windows MPIO settings using the following command to handle the NetApp Volumes maintenance events.
    
    
     Set-MPIOSetting -NewPathVerificationState Enabled `
     -NewPDORemovePeriod 130 `
     -NewRetryCount 6 `
     -CustomPathRecovery Enabled `
     -NewPathRecoveryInterval 30 `
    

During I/O pauses, the iSCSI initiator retries commands and maintains outstanding I/O for the duration of the timeout. If the timeout is exceeded, the operating system might report I/O errors to the application, which can result in lost transactions or require application-level recovery.

#### Application and cluster considerations

If you use clustering software or applications that automate failover, configure your iSCSI timeouts to accommodate NetApp Volumes maintenance events. Premature failover can abort outstanding I/O operations, and might result in data or transaction loss. Always refer to your application and operating system documentation for best practices on iSCSI timeout settings.

### Maintenance event-related application disruptions

Planned maintenance events, like for platform upgrades and service software upgrades, might occur occasionally. Maintenance events are considered non-disruptive from a file protocol (NFS or SMB) perspective as long as the application can handle the I/O pauses that might occur during these events.

For the Standard, Premium, and Extreme service levels, the I/O pauses are typically short and range from a few seconds up to 30 seconds.

For the Flex service level, the I/O pauses are up to 70 seconds.

For more information about how these maintenance events affect storage pool states, see [Storage pool states](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/overview#storage_pool_states).

## What's next

Read about Google Cloud NetApp Volumes [security considerations](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

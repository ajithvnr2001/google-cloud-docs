---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability-groups-shared/overview/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:24.046430+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability-groups-shared/overview/




Stay organized with collections  Save and categorize content based on your preferences. 

Microsoft SQL Server [Always On availability groups](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver15) (AG) let you replicate databases across multiple SQL Server Enterprise instances.

Similar to [SQL Server Failover Cluster Instances](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance), Always On availability groups use Windows Server Failover Clustering (WSFC) to implement high availability. But the two features differ in multiple ways, including:

| Always On availability groups | Failover cluster instances  
---|---|---  
Scope of fail-over | Group of databases | Instance  
Storage | Not shared | Shared  
  
For a more detailed comparison, see [Comparison of Failover Cluster Instances and Availability Groups](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/failover-clustering-and-always-on-availability-groups-sql-server?view=sql-server-ver15#comparison-of-failover-cluster-instances-and-availability-groups).

Always On availability groups support [multiple availability modes](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/availability-modes-always-on-availability-groups?view=sql-server-ver15#SupportedAvModes). This tutorial shows how you can deploy Always On availability groups in _synchronous commit mode_ to implement high availability for one or more databases.

In the setup, you will create three VM instances. Two VM instances, `node-1` and `node-2`, serve as cluster nodes and run SQL Server. A third VM instance, `witness`, is used to achieve a quorum in a failover scenario. The three VM instances are distributed over three zones and share a common subnet.

Using a SQL Server Always On availability group, an example database, `bookshelf`, is synchronously replicated across the two SQL Server instances.

In an on-premises Windows Server Failover Clustering environment, [ARP announcements](https://en.wikipedia.org/wiki/Address_Resolution_Protocol#ARP_announcements) trigger [IP address failover](https://learn.microsoft.com/en-us/troubleshoot/windows-server/virtualization/mac-address-changes-for-virtual-server). Google Cloud, however, disregards ARP announcements. Consequently, you must implement one of the following two options: using an internal load balancer and a distributed network name (DNN). The article assumes that you have already deployed Active Directory on Google Cloud and that you have basic knowledge of SQL Server, Active Directory, and Compute Engine. For more information about Active Directory on Google Cloud, see the Begin Section

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/compatible-components/
title: Review compatible OS, workloads, and Kubernetes versions \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:25.229222+00:00
---

# Review compatible OS, workloads, and Kubernetes versions  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/compatible-components/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Review compatible OS, workloads, and Kubernetes versions

This document lists operating systems, supported workloads, and Kubernetes versions that have been tested with Migrate to Containers CLI.

To learn how to determine a virtual machine (VM) instance workload's fit for migration to a container, see [Offline assessment overview](https://docs.cloud.google.com/migrate/containers/docs/offline-assessment-overview).

## Supported workloads

Migrate to Containers CLI supports modernization of workloads listed in the following table:

Workload| Type (if applicable)| Supported versions  
---|---|---  
Linux VM container| | VMs running 64-bit Linux-based operating systems  
Linux-based workloads| Tomcat| Apache Tomcat version 8.5 - 10.0  
Apache| Apache HTTP Server version 2.4  
JBoss| 

  * WildFly (formerly known as JBoss Application Server) version 8.1.0 - 26.1.1
  * JBoss Enterprise Application Platform version 7.0 - 7.4

  
WebSphere| 

  * WebSphere Application Server traditional version 8.55 and 9.05
  * All versions of WebSphere Application Server Liberty

  
WordPress sites| WordPress version 4.0 or later running on Apache HTTP Server version 2.4  
Windows IIS application| | Microsoft Internet Information Services version 7 or later  
**Note:** For workloads that use a Java-based plugin, Migrate to Containers CLI only supports Java SE version 8 or later. If your workload relies on an earlier version of Java, then you need to [create a custom Docker image](https://docs.docker.com/build/building/base-images/) to execute the migration.

## Source VM operating systems

### Linux VM container

Migrate to Containers CLI supports migrations of VMs to containers on Google Kubernetes Engine on the 64-bit Linux operating systems listed in the following table:

OS | Compute Engine | VMware  
---|---|---  
CentOS | 

  * 6.0
  * 7.0
  * 7.0 UEFI
  * 8.0

| 

  * 6.7
  * 6.9
  * 7.6

  
Debian | 

  * 7.0
  * 8.0
  * 9.0
  * 10.0

| 

  * 9.4
  * 9.6

  
RHEL | 

  * 6.0
  * 7.0
  * 7.0 UEFI
  * 7.4 SAP
  * 7.6 SAP
  * 8.0

| 

  * 6.5
  * 7.5
  * 7.6
  * 8.3

  
SUSE | 

  * 12
  * 12 SP3 SAP
  * 12 SP4 SAP
  * 15
  * 15 SAP
  * 15 SP1 SAP

| 

  * 12 SP2
  * 12 SP3
  * 12 SP4
  * 15

  
Ubuntu | 

  * 12 LTS
  * 14 LTS
  * 16 LTS
  * 16 LTS minimal
  * 18 LTS
  * 18 LTS minimal
  * 18 LTS UEFI
  * 19.04
  * 19.04 minimal

| 

  * 12.04.5 LTS
  * 14.04 LTS
  * 16.04 LTS
  * 18.04.10 LTS

  
  
### Linux-based workloads

For Linux-based workloads, Migrate to Containers CLI supports all Linux-based operating systems.

### Windows IIS application

Migrate to Containers CLI supports the Windows operating systems listed in the following table:

OS | Compute Engine  
---|---  
Windows | 

  * Microsoft Windows Server 2008R2 or later
  * ASP.NET and .NET Framework version 3.5 or later

  
**Warning:** Dynamic disks have been [deprecated](https://learn.microsoft.com/en-us/windows/win32/fileio/basic-and-dynamic-disks#dynamic-disks) by Microsoft, and have severe limitations with snapshots. Use caution when using these, especially in tandem with using snapshots for backup purposes.

## Local machine operating system

### Linux local machine

Migrate to Containers CLI supports migrations using local machines with all 64-bit Linux operating systems.

### Windows local machine

Migrate to Containers CLI supports migrations using local machines with 64-bit Windows Server 2019 LTSC operating systems.

## Local machine storage

The local machine must have several GB of free storage available to create a copy of the source machine file system. The free storage required on you local machine depends on the size of the source machine file system that you want to copy and on the filters that you apply.

**Note:** It is recommended to avoid running the Migrate to Containers CLI in Cloud Shell where the provisioned disk has only 5 GB of storage.

## Workload cluster operating systems

### Linux VM container

For Linux VM containers, Migrate to Containers CLI supports all versions of Ubuntu-based nodes.

### Linux-based workloads

For Linux-based workloads, Migrate to Containers CLI supports all versions of Linux-based nodes.

### Windows IIS application

For Windows IIS applications, Migrate to Containers CLI supports all versions of Windows-based nodes.

**Note:** If you build the container image locally, then the resulting container runs only on nodes with the same operating system as the machine where you build the container image. However, if you're using Cloud Build to build the container image, then the resulting container runs on any Windows-based node.

## What's next

  * Learn how to [discover, collect, and assess VMware VMs for migration](https://docs.cloud.google.com/migrate/containers/docs/mcdc-vmware-quickstart).
  * Learn how to [migrate a VM](https://docs.cloud.google.com/migrate/containers/docs/migrate-vm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

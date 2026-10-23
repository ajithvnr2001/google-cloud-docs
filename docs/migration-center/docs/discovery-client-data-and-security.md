---
url: https://docs.cloud.google.com/migration-center/docs/discovery-client-data-and-security/
title: Discovery client data collection and security \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:37.603974+00:00
---

# Discovery client data collection and security  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/discovery-client-data-and-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Resources ](https://docs.cloud.google.com/migration-center/docs/release-notes)



Send feedback 

#  Discovery client data collection and security Stay organized with collections  Save and categorize content based on your preferences. 

This document addresses concerns and questions about installing the Migration Center discovery client in data centers. It emphasizes the importance of security, compliance, and performance when discovering and collecting data from customer IT assets in highly regulated environments.

## How data collection is performed

The discovery client uses several methods to collect data from target machines. The data collected varies depending on the method. At guest level, data is collected using the collection scripts; at the hypervisor level, data is collected using the underlying platform APIs.

### Discovery client service and process

The discovery client runs as a service called `GoogleMCDC` under a process called `mcdc_service.exe`.

### Collection scripts

All the guest-level collection methods used by the discovery client run collection scripts on the target machines. You can review the actual scripts used for collection at the following links:

  * Linux 
    * [Full collection](https://storage.googleapis.com/mc-release/mcdc/current/mcdc-linux-collect.sh)
    * [Performance collection](https://storage.googleapis.com/mc-release/mcdc/current/mcdc-linux-collect-performnace.sh)
  * Windows 
    * [Full collection](https://storage.googleapis.com/mc-release/mcdc/current/mcdc-windows-collect.ps1)
    * [Performance collection](https://storage.googleapis.com/mc-release/mcdc/current/mcdc-windows-collect-performance.ps1)



The collection scripts store the results in an archive file (zip or tar) which the discovery client then retrieves.

### Collection mechanisms

The discovery client may use one or more of the collection mechanisms described in the following sections to collect data from the target machines.

#### SSH (Linux)

During SSH collection, the following process occurs:

  1. An SSH session is initiated between the collector machine and the target server.
  2. A temporary directory is created under `~/.mcdc-temp/`.
  3. The collection script is copied to that directory.
  4. The collection script is executed.
  5. The result archive is fetched using SCP.
  6. The temporary directory is cleaned up.



#### WMI (Windows)

By default, discovery client uses remote WMI calls to collect data from target Windows machines. Alternatively, if you enable script-based collection, the discovery client copies and executes a script on the target machine.

During script-based WMI collection, the following process occurs:

  1. A WMI connection is initiated to the target machine.
  2. A temporary (volatile) registry key is created on the target machine under `HKLM:\SOFTWARE\Google\Collector\data`.
  3. The collection script is copied to the registry key.
  4. A temporary directory is created under `C:\temp`.
  5. The collection script is written to the temporary directory.
  6. The collection script is executed.
  7. The result of the collection is written to the volatile registry key.
  8. The result is copied to the collector machine.



#### VMware Guest Tools (Linux and Windows)

During VMware collection for both Linux and Windows, the following process occurs:

  1. A temporary directory is created using VMware guest tools.
  2. The collection script is copied to that directory.
  3. The collection script is executed.
  4. The result archive is fetched using VMware guest tools.
  5. The temporary directory is cleaned up.



### Periodic data collection

The discovery client collects data from all configured servers in a periodic manner. There are two types of collection:

  * **Full collection:** Runs once a day for each server. This collection executes the full collection script that collects various information on the VM such as the hardware, environment, installed software, running processes, and more.
  * **Performance collection:** Runs every 10 minutes on each server. This collection executes the performance collection script that collects data on the CPU, memory, network and disk utilization.



## What data is collected

The collection scripts collect data about target VMs to understand how they are configured and what resources they use. This helps in assessing and planning their migration to the cloud.

The following list describes the data that is collected:

  * **System information** : The basic information that is crucial for determining the VM's size, performance requirements, and dependencies on specific hardware or drivers. It includes: 
    * Operating system (version and release)
    * Hardware (CPU, memory, BIOS details)
    * Network configuration (network interfaces, IP addresses, routing tables)
    * Storage (disk drives, partitions, mount points)
  * **Installed software and services** : The scripts collect a list of installed packages and running services to understand the VM's software stack and its role. It includes: 
    * Web servers (Apache, Tomcat, JBoss)
    * Databases (evidence of SQL Server is collected in the Windows script)
    * Other applications that might require specific configurations during migration.
  * **Application configurations** : The scripts also gather configuration files for web servers (IIS, Apache, Tomcat, JBoss, Wordpress). This helps in understanding the specific settings and dependencies of these applications, which is vital for ensuring a smooth transition to the cloud environment.
  * **VMWare and cloud environment detection** : Both the Linux and Windows scripts attempt to detect if the VM is already running in a cloud environment (AWS or Google Cloud), or in a VCenter cluster. They do this by making requests to the metadata servers of these cloud providers. If the VM is already in the cloud, the scripts collect relevant metadata such as instance ID, instance type, and other details.
  * **Performance metrics:** The performance collection scripts measure resource utilization. This includes the following: 
    * CPU
    * Memory
    * I/O operations
    * Networking
  * **Network connections:** The scripts collect open connections to help create a picture of the different dependencies on network resources.



## Performance impact on target machines

### Resource utilization assessment

The resource utilization of the collection scripts on the target machine depends on parameters such as the number of processes running, the number of applications deployed, the number of active network connections, and others.

On Windows, the collection script runs using the lowest priority available through the Threading API. On Linux, a `nice` value of 5 is used to minimize interference with production workloads, and ensure that they have higher priority over the collection script.

A typical collection might take 5-20 seconds of high single-core CPU usage on an unloaded machine. It might take longer if other workloads are present, because these workloads have higher priority.

### Mitigation strategies

The discovery client provides a mechanism to prevent collection of specific servers during specific hours. This feature can be used to prevent the collection from servers running critical workloads during peak hours.

## Security considerations

### Authentication and authorization

#### Communication with target machines

  * The discovery client uses secure channels to authenticate and communicate with target machines. This includes SSH, WMI, VMware tools, and VCenter connections. The discovery client uses the built-in security measures as part of these protocols.
  * In SSH, the discovery client allows both username-password and key-based authentication. For a full list of the supported types of key pairs, see [Target asset requirements](https://docs.cloud.google.com/migration-center/docs/target-assets-requirements?version=v6#linux_machines).



#### Communication with Google Cloud

  * Registered discovery clients communicate with Google Cloud Migration Center during their normal operation. The communication happens through a service account with the `roles/migrationcenter.discoveryClient` role binding. The service account is either created automatically, or provided by the user during the registration process.
  * The service account private key is encrypted on the discovery client machine using the encryption mechanism described in the following section.
  * All communication to Google Cloud is authenticated using this service account, and encrypted using SSL/TLS.



### Data encryption

  * **In transit:** all discovery client communication channels use encryption to protect data in transit. This includes communication with the target machines using the different protocols (SSH/WMI), and communication with Google Cloud using HTTPS.
  * **At rest:** the discovery client PII, SPII and secrets are all encrypted at rest using the `AES128_GCM` algorithm and using the Windows DPAPI to securely store the encryption keys.



### Intrusion detection and prevention

As discovery client is used to connect and run scripts on many VMs in your organization, it may trigger EDR or xDR alerts. This is highly dependent on the way your security tools are configured and the specific tools you are using. Be aware and consider creating exemptions for the specific alerts and devices.

## Logging and supportability

The discovery client collects logs during its operation to allow for debugging and support. The discovery client logs are collected using two mechanisms:

  * **Local logs:** The logs are written to file under `C:\ProgramData\Google\mcdc\logs`. The log files are rotated and compressed.
  * **Cloud logs:** Registered clients also send the logs to Google Cloud so they can be used by the Google Cloud support team when customer issues are reported.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/ip-network-ports/
title: Configure IP network ports \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:54.034800+00:00
---

# Configure IP network ports  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/ip-network-ports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  Configure IP network ports Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the IP network ports that Transfer Appliance uses during transfers. Work with your network administrator to verify that all required ports are configured appropriately for a successful transfer.

## Required ports for attestation service

After you receive your appliance, you must run the attestation service to ensure that the appliance hasn't been tampered with during shipping. The following table describes the IP network port that is used to run the attestation application.

Service | IP Ports | IP Protocol | Notes  
---|---|---|---  
Attestation service | 8081 | TCP | Run the Transfer Appliance attestation application after you receive the appliance to ensure it hasn't been tampered with during shipping. For more information on how to validate your appliance, refer to the [ Receive your Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/receive-appliance#validate) page.  
  
## Required ports for NFS

Transfer Appliance supports NFS for transfers originating from Linux and Apple macOS workstations. The following table describes the IP network ports that must be enabled on your network to use NFS with Transfer Appliance:

Service | IP Ports | IP Protocol  
---|---|---  
rcpbind | 111 | TCP and UDP  
NFS | 2049 | TCP and UDP  
statd | 32765–32766 | TCP  
mountd | 32757 | TCP  
nlockmgr | 32764,32768 | UDP  
  
## Required ports for SSH or SCP

Transfer Appliance supports SSH or SCP for transfers originating from Microsoft Windows, Linux, and Apple macOS workstations. The following table describes the IP network port that must be enabled on your network to use SSH or SCP with Transfer Appliance:

Service | IP Ports | IP Protocol | Notes  
---|---|---|---  
SSH | 22 | TCP | You can connect to Transfer Appliance using SSH while connected to the management port. The management port is typically used to validate the appliance. For more information, refer to [Validating the appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/installation-guide#validate).   
  
## Optional ports

Transfer Appliance can use DHCP, but it isn't required to use Transfer Appliance. The following table describes the optional IP network port for Transfer Appliance:

Service | IP Ports | IP Protocol | Notes  
---|---|---|---  
DHCP | 68 | UDP | This port is optional if you use static IP assignments on your network. For more information on configuring Transfer Appliance to use a static IP address, refer to [Configuring appliance software](https://docs.cloud.google.com/transfer-appliance/docs/4.0/installation-guide#configure-appliance).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

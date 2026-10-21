---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-dhcp-dns/
title: Setting up DNS and DHCP using NSX \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:59.368563+00:00
---

# Setting up DNS and DHCP using NSX  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-dhcp-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Setting up DNS and DHCP using NSX

Applications and workloads running in a private cloud environment require name resolution and DHCP services for lookup and IP address assignment. A proper DHCP and DNS infrastructure is required to provide these services. You can configure your private cloud NSX to provide DHCP and DNS service or set up a virtual machine (VM) to provide these services in your private cloud.

To set up DNS and DHCP services using NSX:

  * [Set up DHCP](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.0/administration/GUID-1409548E-C26E-4AAE-9B6F-CFDCC6798175.html) using NSX.
  * [Set up IPAM](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.0/administration/GUID-A27DF20A-5162-40F5-B7D5-2DF8B6AE5DBE.html) using NSX



## Before you begin

  * Set up connectivity to your on-premises network by using [private services access](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-setup-private-service-access) or set up [internet access for workload VMs](https://docs.cloud.google.com/vmware-engine/docs/networking/workload-internet-access) to use internet-based DNS servers.

  * Use a virtual machine template or ISO to create a VM.




## Linux-based DNS server setup

Linux offers various packages for setting up DNS servers. For information about setting up an open-source BIND DNS server, see [How To Configure BIND as a Private Network DNS Server on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-configure-bind-as-a-private-network-dns-server-on-centos-7).

## Windows-based setup

For information about DNS and DHCP in the Windows Server environment, see the following pages:

  * [Dynamic Host Configuration Protocol (DHCP)](https://docs.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top)
  * [Domain Name System (DNS)](https://docs.microsoft.com/en-us/windows-server/networking/dns/dns-top)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

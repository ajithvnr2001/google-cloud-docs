---
url: https://docs.cloud.google.com/migration-center/docs/collection-methods/
title: Review data collection methods \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:49.786751+00:00
---

# Review data collection methods  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/collection-methods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Review data collection methods Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the collection methods available in discovery client, and the types of data that discovery client collects from your infrastructure.

## Collection methods

The discovery client provides you with two types of data collection:

  * Operating system collection
  * Inventory discovery using the vSphere API



### Operating system collection

The operating system collection lets you gather data from your Linux and Windows servers. The collected data includes CPU, memory, disk space, and performance data of the machine.

### VMware vCenter collection

The discovery client lets you perform inventory discovery and guest discovery on your vCenter VMs.

  * **Inventory discovery** lets you scan and list all the virtual machine (VM) instances in your infrastructure. By using inventory discovery, you can determine the characteristics of the VMs, such as operating system type, storage, number of cores, and other basic information. Inventory discovery also lets you collect the performance data.

  * **Guest discovery** lets you collect guest-level data, including system data, performance data, and network data, using the VMware guest tools. It uses the VMs' credentials to authenticate to the VMs and provides additional data with respect to inventory discovery.




You can provide the guest credentials for Linux and Windows to automatically assign them to newly discovered servers in a vCenter scan. Alternatively, you can assign guest credentials later to individual servers, or to groups of servers. If you don't provide guest credentials at all, the discovery client performs only an inventory discovery. By default, guest discovery is performed using VMware Tools, if it is installed on servers, otherwise using SSH or WMI.

## What's next

  * Learn how to [create and manage credentials in discovery client](https://docs.cloud.google.com/migration-center/docs/create-and-manage-credentials).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

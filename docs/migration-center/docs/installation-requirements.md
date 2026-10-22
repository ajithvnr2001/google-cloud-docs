---
url: https://docs.cloud.google.com/migration-center/docs/installation-requirements/
title: Review installation requirements \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:50.453714+00:00
---

# Review installation requirements  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/installation-requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Review installation requirements Stay organized with collections  Save and categorize content based on your preferences. 

Discovery client is an executable program that you can install on a single machine.

This page describes the hardware and software requirements for installing discovery client. To learn how to download and install the discovery client, see the [installation process](https://docs.cloud.google.com/migration-center/docs/installation-process).

## Hardware requirements

For optimal performance, the physical or virtual machine on which you install discovery client must meet the following specifications, which depend on the number of servers in your infrastructure:

  * Up to 10,000 servers: 2 CPU core, 12 GB RAM, 30 GB free space.



The specifications of the machine where you install the discovery client and the total number of servers in your infrastructure determine the collection frequency of the scanning cycles. Using a less powerful machine than required might result in reduced performance and capabilities.

## Operating system requirements

To install discovery client, your machine must run one of the following operating systems:

  * Windows Server 2016 or higher
  * Windows Desktop client version 10 or higher (64-bit)



## Software requirements

Discovery client requires one of the following browsers installed:

  * Google Chrome: 2 latest versions
  * Microsoft Edge: 2 latest major versions



## Connectivity requirements

For successful data collection, the discovery client must be able to access the target servers from the machine where it is installed.

If you want to upload the collected data to Migration Center, the discovery client must have access to the following URLs:

  * `https://accounts.google.com`
  * `https://console.cloud.google.com/`
  * `https://www.googleapis.com`
  * `https://cloudresourcemanager.googleapis.com`
  * `https://migrationcenter.googleapis.com`
  * `https://iam.googleapis.com`
  * `https://oauth2.googleapis.com`
  * `https://www.gstatic.com`
  * `https://fonts.gstatic.com`



Additional requirements might apply depending on your infrastructure configuration, as follows:

  * If you have multiple non-routable security zones, install the discovery client within each zone, domain, or VLAN to avoid firewall configuration changes.
  * If you have multiple non-routable security zones, and want to access assets across such zones using a single data collector, use the following firewall exclusions for communication between the IP of the discovery client (source) and the target assets: 
    * Linux SSH: Allow TCP inbound port 22.
    * Windows WMI: Allow TCP inbound port 135 and TCP inbound dynamic ports 49152-65535 for Windows Server 2008 and later.
    * For the bulk scan option, you need to allow ICMP echo requests.
  * If you require access through a proxy server to connect to the internet, [set up a proxy connection](https://docs.cloud.google.com/migration-center/docs/manage-discovery-client#set_up_a_proxy_connection).



## What's next

  * Learn more about [discovery client installation process](https://docs.cloud.google.com/migration-center/docs/installation-process).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

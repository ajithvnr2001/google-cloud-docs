---
url: https://docs.cloud.google.com/migration-center/docs/discovery-client-overview/
title: Migration Center discovery client overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:50.564469+00:00
---

# Migration Center discovery client overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/discovery-client-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Migration Center discovery client overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the discovery client for data discovery in your infrastructure, its benefits, and its limitations. Use this page to get started with the discovery client.

## Benefits of data discovery with the discovery client

The discovery client is an application that automatically discovers your physical servers and virtual machines (VMs) in your infrastructure. After you install the discovery client inside your infrastructure, it collects all the required metrics for a successful migration to Google Cloud.

If you decide to connect the discovery client with Migration Center, the client automatically sends the collected data to Migration Center, where you can review it and perform an assessment.

A thorough data discovery can reveal underutilized resources, uncovers potential risks, and ensures a smooth migration. The agentless design of the discovery client, based on open and readable scripts, offers transparency and flexibility, and can serve the various needs of your organization.

## Key features of the discovery client

The discovery client offers the following key features:

  * **Agentless:** the discovery client doesn't require any software agents, and is based on open and readable scripts. As an alternative to the installed version, the discovery client is available in a [CLI version](https://docs.cloud.google.com/migration-center/docs/discovery-client-cli-overview) that you can use for direct and script-based discovery and collection.
  * **Built for sensitive environments:** the discovery client has minimal system load, with the option to review all the data shared with Google Cloud.
  * **Local offline assessment:** For environments with strict data privacy needs, you can keep your data entirely on-premises and perform both discovery and assessment offline.



## Limitations

The following limitations apply to the discovery client:

  * The discovery client can only be installed on Windows machines. To run a discovery from a Linux machine, use the [Migration Center discovery client CLI](https://docs.cloud.google.com/migration-center/docs/discovery-client-cli-overview).
  * The discovery client can only scan devices running a Windows or Linux OS. AIX, Solaris, FreeBSD, and other UNIX-like systems are not supported.
  * The discovery client doesn't support discovery and collection of database assets.



## How data collection works

Data collection with the discovery client follows these steps:

  1. Download and install the discovery client on a machine that can access all the assets in your infrastructure.
  2. Create the credentials required to access the other machines.
  3. Provide a list of IP addresses that the discovery client will use to authenticate to, and collect data from.
  4. Let the discovery client run on your infrastructure for some days to get a complete picture of your infrastructure.
  5. Review the collected data in Migration Center, where you can continue your assessment journey with total cost of ownership (TCO) and other reports.



## How to use the discovery client: a step-by-step process

This section provides you with the list of tasks you perform to successfully install and run the discovery client in your infrastructure. Follow the steps and read through the linked content in the following pages.

  1. **Before you start, create a Google Cloud project and activate Migration Center.** If you're planning to use the discovery client for offline discovery and assessment only, you can skip this step.

     * For more details, see [Get started with Migration Center](https://docs.cloud.google.com/migration-center/docs/get-started-with-migration-center).
  2. **Review the requirements for the target machines.**

     * [Requirements for Windows machines](https://docs.cloud.google.com/migration-center/docs/target-assets-requirements#windows_machines).
     * [Requirements for Linux machines](https://docs.cloud.google.com/migration-center/docs/target-assets-requirements#linux_machines).
     * [Requirements for vCenter VMs](https://docs.cloud.google.com/migration-center/docs/target-assets-requirements#vcenter).
  3. **Review the installation requirements.**

     * For more details, see [Installation requirements](https://docs.cloud.google.com/migration-center/docs/installation-requirements).
  4. **Install and configure the discovery client.**

     1. [Download and install the discovery client](https://docs.cloud.google.com/migration-center/docs/installation-process?version=v6#download-and-install-discovery-client).
     2. [Choose to work in online or offline mode](https://docs.cloud.google.com/migration-center/docs/installation-process?version=v6#upload-data-to-migration-center).
     3. [Manage users access to the discovery client](https://docs.cloud.google.com/migration-center/docs/installation-process?version=v6#grant_access_to_other_users).
  5. **Start a data discovery.**

     1. [Review the available collection methods](https://docs.cloud.google.com/migration-center/docs/collection-methods).
     2. [Add credentials for servers](https://docs.cloud.google.com/migration-center/docs/create-and-manage-credentials?version=v6#add_credentials_for_servers).
     3. [Add credentials for vCenter](https://docs.cloud.google.com/migration-center/docs/create-and-manage-credentials?version=v6#add_vcenter_credentials).
     4. [Add servers to the credentials](https://docs.cloud.google.com/migration-center/docs/add-servers).



## What's next

  * Learn more about [the requirements for machines and databases](https://docs.cloud.google.com/migration-center/docs/target-assets-requirements) from which you want to collect data.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

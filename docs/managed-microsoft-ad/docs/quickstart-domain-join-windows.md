---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-windows/
title: Quickstart: Join a Windows VM manually to a domain \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:34.659536+00:00
---

# Quickstart: Join a Windows VM manually to a domain  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Join a Windows VM manually to a domain

This document explains how to join a Windows VM to a Managed Microsoft AD domain.

## Before you begin

Before you begin, complete the following tasks:

  * [Create a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-create-domain).

  * [Create a Windows VM](https://docs.cloud.google.com/compute/docs/create-windows-server-vm-instance#create_a_virtual_machine_instance). When you create the VM, make sure that you complete the following tasks:

    * Create the VM with a [Windows version that Managed Microsoft AD supports](https://docs.cloud.google.com/managed-microsoft-ad/docs/os-versions#windows-domain-join).
    * Create the VM in the project that hosts your Managed Microsoft AD domain. If your Managed Microsoft AD domain has [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) as an authorized network, you can alternatively create the VM in any of the Shared VPC service projects.
    * Create the VM on a VPC network that you have peered with the Managed Microsoft AD domain.



## Join the Windows VM

Before you join the Windows VM to the domain, [connect to the Windows VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

To join the VM to the domain, you need the following information:

  * The [domain name](https://docs.cloud.google.com/managed-microsoft-ad/docs/list-describe-delete-domains#getting_domain_info) of your Managed Microsoft AD domain.

  * The username and password of an account that has permissions to join a VM to the domain. By default, members of the `Cloud Service Domain Join Accounts` group have these permissions. For more information about the default groups that Managed Microsoft AD creates, see [Groups](https://docs.cloud.google.com/managed-microsoft-ad/docs/objects#groups).




You can join the Windows VM to the Managed Microsoft AD domain either using the [Windows GUI](https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/join-a-computer-to-a-domain) or [PowerShell](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/add-computer?view=powershell-5.1).

For information about common issues that you can encounter while joining a VM manually to a domain, see [Unable to join a VM manually to a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/troubleshooting#manual-domain-join).

## What's next

  * [Join a Windows VM automatically to a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce).

  * [Manage Active Directory objects](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-active-directory-objects) in your Managed Microsoft AD domain.

  * [Connect to a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/connect-to-active-directory-domain).

  * Learn about the [delegated administrator account](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-delegated-admin).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

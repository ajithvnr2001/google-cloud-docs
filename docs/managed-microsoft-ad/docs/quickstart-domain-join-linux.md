---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-linux/
title: Quickstart: Join a Linux VM to a domain \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:00.212946+00:00
---

# Quickstart: Join a Linux VM to a domain  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-linux/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Join a Linux VM to a domain

This page shows you how to join a Linux VM, running [supported Linux distributions](https://docs.cloud.google.com/managed-microsoft-ad/docs/os-versions#linux-domain-join), to a domain in Managed Service for Microsoft Active Directory using the System Security Services Daemon (SSSD).

Managed Microsoft AD interoperability works for many Linux distributions and other connectivity tools. Learn about [these open source connectivity tools](https://docs.cloud.google.com/managed-microsoft-ad/docs/connect-to-active-directory-domain#connecting_to_a_domain-joined_linux_vm).

## Before you begin

  * Verify that you have the permissions required to complete this guide.

  * [Create a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-create-domain).

  * [Create a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance#create_a_virtual_machine_instance). When you create the VM, make sure that you complete the following tasks:

    * On the **Public images** tab, select the appropriate distribution. For example, **Ubuntu 22.04 LTS** or **Red Hat Enterprise Linux 8**.
    * Select a [Linux version that Managed Microsoft AD supports](https://docs.cloud.google.com/managed-microsoft-ad/docs/os-versions#linux-domain-join).
    * Create the VM in the project that hosts your Managed Microsoft AD domain. If your Managed Microsoft AD domain has a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) as an authorized network, you can also create the VM in any of the Shared VPC service projects.
    * Create the VM on a VPC network that you have peered with the Managed Microsoft AD domain.
  * Install `realmd` on the VM. Learn about [`realm`](https://www.systutorials.com/docs/linux/man/8-realm/).

See [Ubuntu](https://ubuntu.com/server/docs/service-sssd-ad#software-installation-3) and [Red Hat](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/windows_integration_guide/realmd-prepreqs) documentation for instructions.

The following are some sample commands:

###  Ubuntu 22.04 LTS or later 
        
        apt-get update
        apt-get install realmd sssd packagekit
        

###  RHEL 8 or later 
        
        sudo yum install realmd oddjob oddjob-mkhomedir
        sssd adcli
        




## Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

  * [Google Cloud Managed Identities Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities#managedidentities.admin) (`roles/managedidentities.admin`)
  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Account Token Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Join a Linux VM to a domain

To join a Linux VM to a domain, you need the following information:

  * The domain name of your Managed Microsoft AD domain. For example, `mydomain.example.com`.

  * The username and password of an account that has permissions to join a VM to the domain. By default, members of the `Cloud Service Domain Join Accounts` group have these permissions. For more information about the default groups that Managed Microsoft AD creates, see [Groups](https://docs.cloud.google.com/managed-microsoft-ad/docs/objects#groups).

    * The username must be in the following format: USERNAME@DOMAIN_NAME. The domain name part of the username must be in uppercase. For example, `user@MYDOMAIN.EXAMPLE.COM`.



You can join the Linux VM to the Managed Microsoft AD domain using the [`realm join`](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/windows_integration_guide/realmd-domain#realm-join) command. The following is a sample command:
    
    
    realm join DOMAIN_NAME -U 'USERNAME@DOMAIN_NAME'
    

For verbose output, add the `-v` flag at the end of the command.

### Specify account location with `realm join`

By default, the `realm join` command creates a machine account that is located at:
    
    
    CN=ACCOUNT_NAME,OU=Computers,OU=Cloud,DC=MACHINE,DC=MID_LEVEL,DC=EXTENSION
    

To specify where to create the account, use the `--computer-ou` flag to provide the path for the `realm join` command. The following example shows how to specify the path:
    
    
    --computer-ou="OU=CUSTOM_OU,DC=MACHINE,DC=MID_LEVEL,DC=EXTENSION"
    

The user must have the permissions that are required to create accounts in the specified OU.

## Remove a Linux VM from a domain

To remove a Linux VM from a domain, you need the domain name of your Managed Microsoft AD domain and the username of your user account.

You can remove a Linux VM from the Managed Microsoft AD domain using the [`realm leave`](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/windows_integration_guide/realmd-ad-unenroll) command. The following is a sample command:
    
    
    realm leave DOMAIN_NAME -U 'USERNAME@DOMAIN_NAME'
    

## What's next

  * [Connect to a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/connect-to-active-directory-domain).
  * Learn about the [delegated administrator account](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-delegated-admin).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

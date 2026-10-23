---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/create-ad-policy/
title: Create an Active Directory policy \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:58.025669+00:00
---

# Create an Active Directory policy  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/create-ad-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create an Active Directory policy Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create an [Active Directory policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad).

## Before you begin

  * Make sure the Active Directory service is reachable, see [Active Directory domain controllers](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad#active_directory_domain_controller_topologies) and [Firewall rules for Active Directory access](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#firewall_rules_for_active_directory_access).

  * Configure Cloud DNS to forward DNS requests for your Windows domain to your Windows DNS servers to enable your Google Cloud Compute Engine virtual machines to resolve Active Directory hostnames, like the Netbios name used by Google Cloud NetApp Volumes. For more information, see [Best practices for using Cloud DNS private forwarding zones](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices#use_cloud_dns_private_forwarding_zones). This is required for on-premises Active Directory as well as Active Directory built on Compute Engine.

  * Active Directory finds domain controllers by looking up DNS Service (SRV) records. If you use Active Directory integrated DNS, domain controllers automatically create and update these records. If you use a third-party DNS server, such as Infoblox, for your domain, make sure that the server contains the [required SRV records](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/7fcdce70-5205-44d6-9c3a-260e616a2f04).

  * When creating SMB volumes, NetApp Volumes uses secure dynamic DNS updates to register its hostname. This process works well when you use Active Directory DNS. If you are using a third-party DNS service to host the zone for your Windows domain, make sure it's configured to support secure DDNS updates. Otherwise, the volume creation for Flex File service level fails. If you use Infoblox, verify the secure DDNS configuration and related DNS record updates carefully, as misconfigurations often cause provisioning failures.




Active Directory policy settings don't apply until you create the first volume that requires Active Directory in the specified region. During that volume creation, incorrect settings can cause volume creation failures. For more information, see [How Active Directory policies join the domain](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad#how_active_directory_policies_join_the_domain).

Flex Unified storage pools in ONTAP-mode don't use Active Directory policies. For more information about instructions, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/create-ad-policy#ontap-mode) tab in the following section.

## Create an Active Directory policy

Use the following instructions to create an Active Directory policy using the Google Cloud console or Google Cloud CLI or ONTAP-mode.

### Console

Use the following instructions to create an Active Directory policy in the Google Cloud console:

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Select **Active Directory policies**.

  3. Click **Create**.

  4. In the **Create Active Directory Policy** dialog, fill out the fields shown in the following table.

Required fields are marked with an asterisk (*).

Field | Description | Applies to NFS | Applies to SMB | Applies to dual protocol  
---|---|---|---|---  
**Active Directory policy name*** | The unique identifier name for the policy | check | check | check  
**Description** | Optional: you can enter a description for the policy | check | check | check  
Region  
**Region*** | Associates the Active Directory to all volumes in the specified region. | check | check | check  
Active Directory connection details  
**Domain name*** | Fully qualified domain name for the Active Directory domain. | check | check | check  
**DNS Servers*** | Comma-separated list of a maximum of three DNS server IP addresses used for [DNS-based domain controller discovery](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad#active_directory_domain_controllers). | check | check | check  
**Site** | Specifies an Active Directory site to manage domain controller selection.   
  
Use when Active Directory domain controllers in multiple regions are configured. Defaults to **Default-First-Site-Name** if left empty. | check | check | check  
**Organizational Unit** | Name of the Organizational Unit where you intend to create the computer account for NetApp Volumes.   
  
Defaults to **CN=Computers** if left empty. | check | check | check  
**NetBIOS Name Prefix*** | NetBIOS name prefix of the server to be created.   
  
A five-character random ID is generated automatically, for example, `-6f9a`, and appended to the prefix. The full UNC share path has the following format:   
  
`\\<NetBIOS_PREFIX>-<4-random-hexletters>.<DOMAIN_NAME>\<SHARE_NAME>`.  | check | check | check  
**Enable AES Encryption for Active Directory authentication** | Enables AES-128 and AES-256 encryption for Kerberos-based communication with Active Directory | check | check | check  
Active Directory credentials  
**Username* and Password*** | Credentials for the Active Directory account with permissions to create the compute account within the specified organizational unit.   
  
The username requires the Security Account Manager (SAM) account name, which supports a maximum of 20 characters.  | check | check | check  
SMB settings  
**Administrators** | Domain user accounts to be added to the local Administrators group of the SMB service.   
  
Provide a comma-separated list of domain users or groups. The Domain Admin group is automatically added when the service joins your domain as a hidden group.   
  
Administrators only use the Security Account Manager (SAM) Account name. The SAM Account name supports a maximum of 20 characters for your username and 64 characters for your group name.   
  
|  | check | check  
**Backup Operators** | Domain user accounts to be added to the Backup Operators group of the SMB service. The Backup Operators group allows members to backup and restore files regardless of whether they have read or write access to the files.   
  
Provide a comma-separated list of domain users or groups.   
  
Backup Operators only use the Security Account Manager (SAM) Account name. The SAM Account name supports a maximum of 20 characters for your username and 64 characters for your group name. |  | check | check  
**Security Privilege Users** | Domain accounts that require elevated privileges such as `SeSecurityPrivilege` to manage security logs.   
  
Provide a list separated by commas of domain users or groups. This is specifically needed for the installation of a SQL Server where binaries and system databases are stored on an SMB share. This option isn't required if you use an administrator user during installation. |  | check | check  
NFS settings  
**Kerberos Key Distribution Hostname** | Hostname of the Active Directory server used as Kerberos Key Distribution Center | NFSv4.1 with Kerberos |  | SMB and NFSv4.1 with Kerberos  
**KDC IP** | IP address of the Active Directory server used as Kerberos Key Distribution Center | NFSv4.1 with Kerberos |  | SMB and NFSv4.1 with Kerberos  
**Allow local NFS users with LDAP** | Local UNIX users on clients without valid user information in Active Directory are blocked from access to [LDAP enabled volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad#use_cases_for_active_directory).   
  
This option can be used to temporarily switch such volumes to `AUTH_SYS` authentication (user ID + 1-16 groups). | check |  | check  
Labels  
**Labels** | Optional: add relevant labels | check | check | check  
  5. Click **Create**. For the Flex Unified, Standard, Premium, and Extreme service levels: after creating an Active Directory policy and attaching it with a storage pool, you should [test the connection to the Active Directory service](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/test-ad-policy-connection).




### gcloud

Create an Active Directory policy:
    
    
      gcloud netapp active-directories create CONFIG_NAME \
        --project=PROJECT_ID \
        --location=LOCATION \
        --dns=DNS_LIST \
        --domain=DOMAIN_NAME \
        --net-bios-prefix=NetBIOS_PREFIX \
        --username=USERNAME \
        --password=PASSWORD \
        --enable-aes=true
      

Replace the following information:

  * `CONFIG_NAME`: the name of the config you want to create. The config name must be unique per region.

  * `PROJECT_ID`: project ID you are creating the Active Directory policy in.

  * `LOCATION`: the region of you want to create the config in. Google Cloud NetApp Volumes only supports one config per region.

  * `DNS_LIST`: a list separated by commas of up to three IPv4 addresses of Active Directory DNS servers.

  * `DOMAIN_NAME`: the fully qualified domain name of the Active Directory.

  * `NetBIOS_PREFIX`: NetBIOS name prefix of the server you want to create. A five-character random ID generates automatically, such as `-6f9a`, and appends to the prefix.

The full UNC share path has the following format:
        
        \\<NetBIOS_PREFIX>-<4-random-hexletters>.<DOMAIN_NAME>\<SHARE_NAME>.

  * `USERNAME`: The name of a domain user with permission to join the domain.

  * `PASSWORD`: Password for the username.




For more information about the individual parameters, see the instructions in the **Console** tab.

For more information about additional optional flags, see [Google Cloud SDK documentation on Active Directory creation](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/active-directories).

### ONTAP-mode

Flex Unified storage pools in ONTAP-mode don't use Active Directory policies. To use Active Directory with SMB volumes, join the pool's ONTAP storage virtual machine (SVM) to your Windows domain by creating a CIFS server on the SVM.

Before joining the domain, make sure that the pool can connect to Active Directory DNS servers and domain controllers. For an integration overview, prerequisites, and firewall rules, see [Google Cloud NetApp Volumes Active Directory integration](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad).

For instructions about ONTAP CLI commands, the Python join script, and removing a CIFS server, see [Join an ONTAP-mode pool to Active Directory](https://docs.cloud.google.com/netapp/volumes/docs/ontap/join-ontap-mode-pool-to-ad).

## What's next

[Test the Active Directory policy connection](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/test-ad-policy-connection).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

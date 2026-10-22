---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/objects/
title: Default Active Directory objects in Managed Microsoft AD \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:34.591383+00:00
---

# Default Active Directory objects in Managed Microsoft AD  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Default Active Directory objects in Managed Microsoft AD Stay organized with collections  Save and categorize content based on your preferences. 

When you create a new domain with Managed Service for Microsoft Active Directory, some Active Directory objects are automatically created for you. These help you administer your AD domain, and make it easier to manage AD tasks typically delegated to other users or groups.

The following diagram provides an overview. Refer to the tables below for a complete list and description of each object.

![AD groups](https://docs.cloud.google.com/static/managed-microsoft-ad/img/groups.svg)

## Organizational units

Table 1 shows the organizational units (OU) created for you.

**Table 1.** Organizational units Name | Description  
---|---  
`Cloud` | Hosts all your AD objects. You have full control inside this OU.  
`Cloud Service Objects` |  Hosts AD objects created and managed by Managed Microsoft AD. Only Google Cloud can create objects under this OU, though you can update some attributes on the pre-created objects.   
  
## Groups

The following groups are created under the `Cloud Service Objects` OU.

**Table 2.** Groups in `Cloud Service Objects` OU Name | Type | Description |   
---|---|---|---  
`Cloud Service Administrators` | Global |  Members are administrators of the Managed Microsoft AD cloud service.   
`Cloud Service All Administrators` | Domain Local |  Members are administrators of the Managed Microsoft AD cloud service. This can include members from trusted domains.   
`Cloud Service Computer Administrators` | Domain Local | Members are administrators on machines joined to the domain.  
`Cloud Service DNS Administrators` | Domain Local |  Members can add, remove, and modify DNS entries inside the Active Directory-integrated DNS zones.   
`Cloud Service Managed Service Account Administrators` | Domain Local | Members can administer Managed Service Accounts.  
`Cloud Service Computer Remote Desktop Users` | Domain Local | Members have remote desktop rights on machines joined to the domain.  
`Cloud Service Site Administrators` | Domain Local | Members can rename Active Directory sites.  
`Cloud Service Protected Users` | Global | Protections from the [Protected Users](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group) group are applied to members.  
`Cloud Service Group Policy Creator Owners` | Domain Local |  Members can create Group Policy Objects (GPOs). GPOs can only be linked on `Cloud` OU and objects inside it. However, only the creator of these GPOs can edit them. For more information, see [How can I manage group policy objects (GPO)?](https://docs.cloud.google.com/managed-microsoft-ad/docs/faq#group-policy-objects).   
`Cloud Service Domain Join Accounts` | Domain Local | Members can join computers to the domain.  
`Cloud Service Fine Grained Password Policy Administrators` | Domain Local | Members can modify and assign password policies to users and groups.  
  
Managed Microsoft AD doesn't support providing time-limited group memberships to users by using [Privileged Access Management for Active Directory Domain Services](https://learn.microsoft.com/en-us/microsoft-identity-manager/pam/privileged-identity-management-for-active-directory-domain-services).

## Group Policy Objects

Managed Microsoft AD automatically creates some Group Policy Objects (GPO) to support certain Group Policy features.

**Table 3.** Group policy objects Name | Description  
---|---  
`Cloud Service Default Computer Policy` |  Linked to the `Cloud` OU. Grants `Cloud Service Computer Administrators` local administrator rights and `Cloud Service Computer Remote Desktop Users` Remote Desktop (RDP) privileges on `Cloud` OU.   
  
You can [create custom GPOs](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/create-a-group-policy-object) and link them to the `Cloud` OU or to any of the child OUs within the `Cloud` OU. For information about linking a GPO to an OU, see [Link the GPO to the Domain](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/link-the-gpo-to-the-domain).

## Password Settings Objects

Managed Microsoft AD automatically creates ten password settings objects (PSO). You cannot change the name or precedence of these PSOs. Table 4 shows the names and precedences of these PSOs.

**Table 4.** Policy settings objects Name | Precedence  
---|---  
PSO-10 | 10  
PSO-20 | 20  
PSO-30 | 30  
PSO-40 | 40  
PSO-50 | 50  
PSO-60 | 60  
PSO-70 | 70  
PSO-80 | 80  
PSO-90 | 90  
PSO-100 | 100  
  
Default values are assigned to the password policy settings for each PSO. You can change these values. Table 5 shows these default settings.

**Table 5.** Default PSO settings Policy | Setting  
---|---  
Complexity enabled | True  
Lockout duration | 30 minutes  
Lockout observation window | 30 minutes  
Lockout threshold | 0  
Maximum password age | 42 days  
Minimum password age | 1 day  
Minimum password length | 7  
Password history count | 24  
Reversible encryption enabled | False  
  
## Users

Managed Microsoft AD automatically creates the users shown in table 6.

**Table 6.** Users Name | Description  
---|---  
`setupadmin` (default) |  Delegated administrator account for you to manage your domain. The name defaults to `setupadmin`; you can specify a different name during domain creation. [Resetting the password](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-delegated-admin#reset-password) for a domain sets the password for this account.  
`cloudsvcadmin` |  Service account used by Managed Microsoft AD to manage the domain. This account is intended for use by the system and should not be directly used, modified, or deleted.   
  
## Delegated administrator

Table 7 shows the Active Directory rights that are automatically granted to the delegated administrator account when you provision the domain. These rights are granted by the account's group memberships, so if you remove the account from one of those groups, that may affect its rights and available actions. This account has the default name `setupadmin`. If you changed the account name but do not remember the value, you can [retrieve it](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-delegated-admin#get-name). For more information, see [Use delegated administrator account](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-delegated-admin).

The delegated administrator account doesn't have the `Domain Admins`, `Enterprise Admins`, and `BUILTIN\Administrators` permissions because Managed Microsoft AD is a managed service and Google reserves the right to use these permissions. So you can't use Active Directory features that require these permissions in Managed Microsoft AD, such as [Distributed File System (DFS)](https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview), [DHCP](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top), configuring GPOs at the domain level, replicating directory changes, raising forest functional levels, and other forest-wide changes.

**Table 7.** Delegated administrator account rights Active Directory object | Distinguished name | Delegated administrator account actions permitted on object  
---|---|---  
Cloud |  `OU=Cloud,DC=<domain-name>` |  Can perform CRUD operations for any object type under the `Cloud` OU Can link GPO's to this OU and its sub-OU's Cannot delete or rename the OU  
Managed Service Account container |  `CN=Managed Service Accounts, DC=<domain-name>` | Can create, update, and delete group Managed Service Accounts and all related management  
MicrosoftDNS container |  `CN=MicrosoftDNS,CN=System, DC=<domain-name>` | Can connect to AD-integrated DNS Server by using DNS manager.  
DomainDNSZones folder | `CN=MicrosoftDNS, DC=DomainDNSZones,DC=<domain-name>` | Can create conditional forwarders, A records, CNAME records, DNS delegation, forward lookup zones, and reverse lookup zones  
ForestDNSZones folder | `CN=MicrosoftDNS, DC=ForestDNSZones,DC=<domain-name>` | Can create conditional forwarders, A records, CNAME records, DNS delegation, forward lookup zones, and reverse lookup zones  
Delegated administrator account (default name: `setupadmin`) |  `CN=<delegated-admin-name>, OU=Cloud Service Objects,DC=<domain-name>` |  Can change the password of the delegated administrator account that is automatically created during domain provisioning Learn more about [getting this account's name](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-delegated-admin#get-name) and [resetting its password](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-delegated-admin#reset-password).  
Cloud Service Administrators  |  `CN=Cloud Service Administrators, OU=Cloud Service Objects, DC=<domain-name>` |  Can add or remove AD objects to `Cloud Service Administrators` managed group Any accounts added to this group are granted the same set of permissions that are granted to the delegated administrator account.  
All sites |  All sites under: `CN=Sites,CN=Configuration, DC=<domain-name>` | Can change the Active Directory site name  
All managed groups  |  All Cloud managed groups under: `OU=Cloud Service Objects, DC=<domain-name>` |  Can add and remove AD objects from the pre-created Cloud managed groups Does not apply to the built-in Active Directory groups that are created during AD installation  
Policies Container  |  `CN=Policies, CN=System,DC=<domain-name>` |  Can create, update, and delete Group Policy Objects Cannot edit or delete Default Domain Controller or Default Domain Policy GPOs  
Partition Container (UPN suffixes)  |  `CN=Partitions,CN=Configuration, DC=<domain-name>` | Can change UPN suffixes  
Terminal Services License Server |  `CN=Terminal Server License Servers,CN=Builtin, DC=<domain-name>` | Can add Windows Servers with Terminal License Server role to the Terminal Service License Server built-in group  
  
## What's next

  * [Manage Active Directory objects](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-active-directory-objects)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

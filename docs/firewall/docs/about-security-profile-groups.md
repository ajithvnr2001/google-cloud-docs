---
url: https://docs.cloud.google.com/firewall/docs/about-security-profile-groups/
title: Security profile group overview \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:13.150134+00:00
---

# Security profile group overview  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/about-security-profile-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Security profile group overview Stay organized with collections  Save and categorize content based on your preferences. 

A security profile group is a container for security profiles. Your firewall policy rules reference a security profile group to enable Layer 7 inspection, such as [intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention), [Advanced malware sandbox (WildFire)](https://docs.cloud.google.com/firewall/docs/about-wildfire) ([Preview](https://cloud.google.com/products#product-launch-stages)), and [URL filtering service](https://docs.cloud.google.com/firewall/docs/about-url-filtering) on your network.

This document provides a detailed overview of security profile groups and their capabilities.

## Specifications

  * A security profile group is a resource that you can configure at the organization level or the project level.

    * **Organization-level security profile group** : use this to group organization-level security profiles across your organization.

    * **Project-level security profile group:** use this to group project-level security profiles within your project.

  * The name of a security profile group is configured in the following URL identifier format:

    * **Organization-level** :
          
          organizations/ORGANIZATION_ID/locations/global/securityProfileGroups/NAME
          

    * **Project-level** :
          
          projects/PROJECT_ID/locations/global/securityProfileGroups/NAME
          

The `NAME` of the security profile group must meet the following requirements:

    * A string 1 to 63 characters long
    * Contains only lowercase alphanumeric characters or hyphens (-)
    * Starts with a letter

Examples:

    * **Organization-level security profile group** :
          
          organizations/2345678432/locations/global/securityProfileGroups/example-security-profile-group
          

    * **Project-level security profile group** :
          
          projects/my-project-123/locations/global/securityProfileGroups/example-security-profile-group
          

If you use the unique URL identifier for the security profile group name, the URL includes the organization or project, and the location. If you specify only the name, you must provide the organization ID or the project ID and the location separately when you use `gcloud` commands.

  * In a security profile group, you can add [security profiles](https://docs.cloud.google.com/firewall/docs/about-security-profiles) of types `THREAT_PREVENTION`, `WILDFIRE_ANALYSIS`, or `URL_FILTERING` in any order.

  * A security profile group can contain only one security profile of each type. To add multiple profiles, ensure they are of different types. For example, if you add a security profile of the `URL_FILTERING` type, you can add a second profile of type `THREAT_PREVENTION` to scan traffic and filter it. If you add a `WILDFIRE_ANALYSIS` profile to scan for unknown file-based malware, you must also include a mandatory `THREAT_PREVENTION` profile in the security profile group.




## Integration with firewall policy rules

Security profile groups apply to firewall policies only when you add a firewall policy rule with the action `apply_security_profile_group`. You can configure security profile groups in the following firewall policy rules:

  * **[Hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#rule_tasks)** : managed at the organization or folder-level, these policies can reference only organization-level security profile groups.

  * **[Global network firewall policies](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#add_rules)** : managed at the project-level, these policies can reference organization-level security profile groups and project-level security profile groups from any project.




To perform Layer 7 inspection of the network traffic, a firewall policy rule must contain the name of the security profile group to be used by the firewall endpoint.

## Traffic inspection and processing

The firewall policy rule applies to incoming and outgoing traffic of the Virtual Private Cloud (VPC) network. Matched traffic is redirected to the firewall endpoint along with the configured security profile group name.

The firewall endpoint uses the security profiles specified in the security profile group to do the following:

  * Inspect domain and server name indication (SNI) information
  * Scan packets for threats and unknown file-based malware
  * Apply configured actions



### Inspection sequence

The firewall endpoint generally processes security profiles in the following order:

  1. **URL filtering:** The endpoint executes the `URL_FILTERING` security profile.
  2. **Threat prevention and malware analysis:** The endpoint runs the `THREAT_PREVENTION` security profile. When Advanced malware sandbox is enabled, a `WILDFIRE_ANALYSIS` security profile also runs alongside the threat prevention profile.

**Note:** If the endpoint detects a possible threat in the HTTP(S) message header, it can use intrusion detection and prevention service first to evaluate and block the traffic. The traffic that is evaluated and not blocked by intrusion detection and prevention service is then processed by the URL filtering service.

### Threat scanning logic

During threat scanning, Advanced malware sandbox uses a combination of on-box and cloud-based analysis engines. It provides the following types of protection:

  * **Real-time protection:** checks against known malware signatures and uses on-box machine learning (ML) models to dynamically analyze and block unknown threats.
  * **Inline cloud analysis:** evaluates files in the cloud before they reach the network.
  * **Asynchronous deep sandboxing:** if unknown files pass the real-time checks, the firewall extracts and uploads them to the Advanced malware sandbox cloud for analysis based on your configured submission rules.



To learn more about configuration, see the following documents:

  * [Configure the URL filtering service](https://docs.cloud.google.com/firewall/docs/configure-url-filtering)
  * [Configure intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/configure-intrusion-prevention)
  * [Create and manage Advanced malware sandbox security profiles](https://docs.cloud.google.com/firewall/docs/configure-wildfire-security-profiles)



## Resource association

Each security profile group must have an associated project ID. The associated project is used for quotas and access restrictions on security profile group resources.

If you authenticate your service account by using the [`gcloud auth activate-service-account` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account), you can associate your service account with the security profile group.

To learn more, see [Create a security profile group](https://docs.cloud.google.com/firewall/docs/configure-security-profile-groups#create-security-profile-group).

## Differences between organization-level and project-level security profile groups

The following points summarize the differences between organization-level and project-level security profile groups :

  * Organization-level security profile groups apply to both organization-level and project-level endpoints.
  * Project-level security profile groups apply to project-level firewall endpoints that are in the same project as the security profile group. They can't be applied to organization-level firewall endpoints.
  * An organization-level security profile group can contain only organization-level security profiles.
  * A project-level security profile group can contain only project-level security profiles that exist in the same project.



## Identity and Access Management roles

Identity and Access Management (IAM) roles govern the following security profile group actions:

  * Creating a security profile group in an organization or a project
  * Modifying or deleting a security profile group in an organization or a project
  * Viewing details of a security profile group in an organization or a project
  * Viewing a list of security profile groups in an organization or a project
  * Using a security profile group in a firewall policy rule



The following table describes the roles that are necessary for each step.

Ability | Necessary role  
---|---  
Create a security profile group | Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Security Profile Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profile groups, and at either the project level or the organization level for project-level security profile groups 

  
Modify a security profile group | Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Security Profile Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profile groups, and at either the project level or the organization level for project-level security profile groups 

  
Delete a security profile group | Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Security Profile Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profile groups, and at either the project level or the organization level for project-level security profile groups 

  
View details about the security profile group in an organization and a project | Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Security Profile Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profile groups, and at either the project level or the organization level for project-level security profile groups 
  * [Compute Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)
  * [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)

  
View all of the security profile groups in an organization and a project | Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Security Profile Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profile groups, and at either the project level or the organization level for project-level security profile groups 
  * [Compute Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)
  * [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)

  
Use a security profile group in a firewall policy rule | Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Security Profile Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profile groups, and at either the project level or the organization level for project-level security profile groups 
  * [Compute Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)

  
  
## What's next

  * [Configure the URL filtering service](https://docs.cloud.google.com/firewall/docs/configure-url-filtering)
  * [Configure intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/configure-intrusion-prevention)
  * [Configure Advanced malware sandbox service](https://docs.cloud.google.com/firewall/docs/configure-wildfire)
  * [Create security profile groups](https://docs.cloud.google.com/firewall/docs/configure-security-profile-groups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/firewall/docs/about-security-profiles/
title: Security profile overview \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:33.509133+00:00
---

# Security profile overview  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/about-security-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Security profile overview Stay organized with collections  Save and categorize content based on your preferences. 

Security profiles help you define Layer 7 inspection policy for your Google Cloud resources. They are generic policy structures that firewall endpoints use to scan intercepted traffic and provide application layer services, such as the intrusion detection and prevention service, Advanced malware sandbox (WildFire) ([Preview](https://cloud.google.com/products#product-launch-stages)), and URL filtering service.

This document provides a detailed overview of security profiles and their capabilities.

## Specifications

  * Cloud Next Generation Firewall (Cloud NGFW) supports the following types of security profiles:

    * `THREAT_PREVENTION`
    * `WILDFIRE_ANALYSIS` ([Preview](https://cloud.google.com/products#product-launch-stages))
    * `URL_FILTERING`
  * A security profile is a resource that you can configure at the organization level or the project level.

    * **Organization-level security profile** : use this profile to create and manage organization-level and project-level firewall endpoints.

    * **Project-level security profile:** use this profile to create and manage project-level firewall endpoints in the same project.

  * The name of a security profile is configured in the following URL identifier format:

    * **Organization-level** :
          
          organizations/ORGANIZATION_ID/locations/global/securityProfiles/NAME
          

    * **Project-level** :
          
          projects/PROJECT_ID/locations/global/securityProfiles/NAME
          

The `NAME` of the security profile must meet the following requirements:

    * A string 1 to 63 characters long
    * Contains only lowercase alphanumeric characters or hyphens (-)
    * Starts with a letter

Examples:

    * **Organization-level security profile** :
          
          organizations/2345678432/locations/global/securityProfiles/example-security-profile
          

    * **Project-level security profile** :
          
          projects/my-project-123/locations/global/securityProfiles/example-security-profile
          

If you use the unique URL identifier for the security profile name, the URL includes the organization or project, and the location. If you specify only the name, you must provide the organization ID or the project ID and the location separately when you use `gcloud` commands.

  * After you create a security profile, manually attach it to a [security profile group](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups). This security profile group is referenced by the firewall policy of the Virtual Private Cloud (VPC) network where you want to enforce Layer 7 inspection.

  * Each security profile must have an associated project ID. The associated project is used for quotas and access restrictions on security profile resources. If you authenticate your service account by using the [`gcloud auth activate-service-account` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account), you can associate your service account with the security profile. To learn more about how to create a security profile, see [Create a threat prevention security profile](https://docs.cloud.google.com/firewall/docs/configure-security-profiles#create-tp-security-profile), [Create an Advanced malware sandbox security profile](https://docs.cloud.google.com/firewall/docs/configure-wildfire-security-profiles#create-wildfire-security-profile), and [Create a URL filtering security profile](https://docs.cloud.google.com/firewall/docs/configure-urlf-security-profiles#create-urlf-security-profile).

  * When you add security profiles to a [security profile group](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups), the following constraints apply:

    * An organization-level security profile group can reference only organization-level security profiles.
    * A project-level security profile group can reference project-level security profiles in the same project.



## Threat prevention security profile

Cloud NGFW uses threat prevention security profiles to provide [intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention).

When you create a security profile of type `THREAT_PREVENTION`, the following [default threat signatures](https://docs.cloud.google.com/firewall/docs/about-threats#default_signature_set) with default severity and associated actions are added to the profile:

  * Vulnerability detection signatures
  * Anti-spyware signatures
  * Antivirus signatures
  * DNS signatures



You can add severity overrides to your threat prevention security profiles. Each default signature has a [threat severity level](https://docs.cloud.google.com/firewall/docs/about-threats#threat-severity-level). The severity level indicates the risk of the detected threat. Each severity level also has an associated default action. The default action specifies the measures Cloud NGFW takes to handle threats with a specific severity level. Use threat prevention security profiles to override the default action for a severity level.

The following actions are supported:

  * **Default** : performs the default action associated with the threat.
  * **Deny** : logs the threat and drops the packet.
  * **Alert** : logs the threat and allows the session.
  * **Allow** : ignores the threat, if detected.



When you create a threat prevention security profile, the default override action for all severity levels is set to `Default`.

You can also add signature overrides to your threat prevention security profiles. Each threat signature has an associated default action. Use threat prevention security profiles to override these default actions by using the preceding actions. Signature overrides take precedence over severity overrides.

**Note:** If you override the default threat signature action or modify the default severity level action in a threat prevention security profile, it might take up to 15 minutes for these changes to take effect.

To learn more about how to configure threat prevention, see [Configure intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/configure-intrusion-prevention).

## Advanced malware sandbox security profile

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud NGFW uses an Advanced malware sandbox security profile to define the security policies and behaviors for malware analysis. Use the `WILDFIRE_ANALYSIS` security profile type to configure how the firewall detects and responds to potential threats.

For more information, see [Advanced malware sandbox overview](https://docs.cloud.google.com/firewall/docs/about-wildfire).

Use the following parameters, which are part of the Advanced malware sandbox configuration and can be configured using `gcloud beta network-security security-profiles wildfire-analysis` command:

  * **Submission rules** : define the files that Cloud NGFW Enterprise uploads to Advanced malware sandbox for asynchronous analysis. Configure these rules using the `add-submission-rule` command.

    * To specify the file types to submit, choose `ANY_FILE` using the `--file-types` flag.
    * Specify the traffic direction, such as upload, download, or both, using the `--direction` flag.
  * **Inline cloud analysis rules** : use these rules to configure real-time protection. Configure these rules using the `add-inline-cloud-analysis-rule` command.

    * Specify file types (restricted to `ANY_FILE` or `PE` files) using the `--file-types` flag.
    * Specify the traffic direction using the `--direction` flag.
    * Define the action to take upon threat detection (`ALLOW`, `DENY`, or `ALERT`) using the `--action` flag.
  * **Inline ML configuration** : enable or disable machine learning (ML) engines to dynamically detect malicious content for specific file types, such as `WINDOWS_EXECUTABLE`, `POWERSHELL_SCRIPT`, `ELF`, and `MS_OFFICE`. Configure these engines using the `update` command with the following flags:

    * `--[no-]analyze-windows-executables`
    * `--[no-]analyze-powershell-script-1`
    * `--[no-]analyze-powershell-script-2`
    * `--[no-]analyze-elf`
    * `--[no-]analyze-ms-office`
    * `--[no-]analyze-shell`
    * `--[no-]analyze-ooxml`
    * `--[no-]analyze-macho`
  * **Inline ML exceptions** : create rules to bypass the inline ML engine for specific files. Configure exceptions using the `add-inline-ml-exception` command.

    * Specify the file's partial hash using the `--partial-hash` flag.
    * Specify the filename using the `--filename` flag.
  * **Real-time lookup** : determine whether Cloud NGFW holds a file transfer while performing a real-time signature lookup against the Advanced malware sandbox cloud to prevent the initial transfer of known malware. This is enabled by default. Configure this setting using the `update` command with the `--[no-]wildfire-realtime-lookup` flag.

  * **Threat and protocol overrides** : override the default action when a Advanced malware sandbox signature is matched. Configure overrides using the `add-override` command. You can override the following actions:

    * **Protocol overrides** : apply a specific action, such as `DENY`, to all Advanced malware sandbox or inline ML threats that occur over designated protocols such as `HTTP`, `SMTP`, or `FTP`. Configure these using the `--wildfire` or `--wildfire-inline-ml` flag and the `--action` flag.

    * **Threat ID overrides** : add signature exceptions by specifying an exact vendor-specified threat ID. This often involves changing the action to `ALLOW` to suppress false-positive alerts. Configure these using the `--threat-ids` flag and the `--action` flag.




Associate the Advanced malware sandbox security profile with a security profile group to apply these rules to your network traffic. Also include a threat prevention security profile in the same group. To create an Advanced malware sandbox security profile, see [Create an Advanced malware sandbox security profile](https://docs.cloud.google.com/firewall/docs/configure-wildfire-security-profiles#create-wildfire-security-profile).

## URL filtering security profile

Cloud NGFW uses a URL filtering security profile to configure the [URL filtering service](https://docs.cloud.google.com/firewall/docs/about-url-filtering).

A URL filtering security profile is a type of security profile that uses one or more URL filters to define security policies for the firewall endpoints. A URL filter is a list of matcher strings with a unique priority and an action. Matcher strings contain domain names that Cloud NGFW matches against the HTTP message being evaluated. For encrypted messages, Cloud NGFW checks the matcher strings against the SNI sent during TLS negotiation. If you enable TLS inspection, Cloud NGFW decrypts the message header and also evaluates the host header. For unencrypted traffic, Cloud NGFW always compares the matcher strings against the host header of the HTTP message.

The priority of a URL filter is determined by the unique value that you specify using the `priority` field. The priority value of a URL filter can range from `0` to `2147483647`. Cloud NGFW processes the lowest numeric value (representing the highest priority) first, followed by the next higher numeric value until it finds a match. Cloud NGFW doesn't evaluate the individual domains within a URL filtering list in priority order.

**Note:** If you modify a URL filtering security profile, it might take up to 15 minutes for the changes to take effect.

To learn more about creating and managing URL filtering security profiles, see [Create and manage URL filtering security profiles](https://docs.cloud.google.com/firewall/docs/configure-urlf-security-profiles).

To learn more about how to configure URL filtering, see [Configure the URL filtering service](https://docs.cloud.google.com/firewall/docs/configure-url-filtering).

## Identity and Access Management roles

Identity and Access Management (IAM) roles govern the following security profile actions:

  * Creating a security profile in an organization or a project
  * Modifying or deleting a security profile in an organization or a project
  * Viewing details of a security profile in an organization or a project
  * Viewing a list of security profiles in an organization or a project
  * Using a security profile in a security profile group



The following table describes the roles that are necessary for each step.

Ability | Necessary role  
---|---  
Create a security profile  |  Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Security Profile Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profiles, and at either the project level or the organization level for project-level security profiles 

  
Modify a security profile  |  Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Security Profile Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profiles, and at either the project level or the organization level for project-level security profiles 

  
Delete a security profile  |  Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Security Profile Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profiles, and at either the project level or the organization level for project-level security profiles 

  
View details about a security profile  |  Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Security Profile Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profiles, and at either the project level or the organization level for project-level security profiles 
  * [Compute Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)
  * [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)

  
View all of the security profiles in an organization  |  Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Security Profile Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profiles, and at either the project level or the organization level for project-level security profiles 
  * [Compute Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)
  * [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)

  
Use a security profile in a security profile group  |  Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Security Profile Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profiles, and at either the project level or the organization level for project-level security profiles 
  * [Compute Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)

  
  
## Quotas

To view quotas associated with security profiles, see [Quotas and limits](https://docs.cloud.google.com/firewall/docs/quotas).

## What's next

  * [Configure the URL filtering service](https://docs.cloud.google.com/firewall/docs/configure-url-filtering)
  * [Configure intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/configure-intrusion-prevention)
  * [Configure Advanced malware sandbox service](https://docs.cloud.google.com/firewall/docs/configure-wildfire)
  * [Create and manage URL filtering security profiles](https://docs.cloud.google.com/firewall/docs/configure-urlf-security-profiles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

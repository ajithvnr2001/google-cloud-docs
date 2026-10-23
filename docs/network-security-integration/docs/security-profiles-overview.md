---
url: https://docs.cloud.google.com/network-security-integration/docs/security-profiles-overview/
title: Security profiles overview \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:01.709233+00:00
---

# Security profiles overview  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/security-profiles-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Security profiles overview Stay organized with collections  Save and categorize content based on your preferences. 

Security profiles are policy containers used by multiple network security products. The security profile defines the scope of network traffic to monitor and analyze within the Network Security Integration service.

## Why you use security profiles

You use a security profile to specify the action for a matched mirroring rule. Without a security profile attached to the mirroring rule, the integration service doesn't know where to send the mirrored traffic for inspection.

## How security profiles work

The security profile works by attaching your network resources to a [mirroring firewall rule](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/firewall-policies-overview#mirroring-rules). When you attach a security profile to a mirroring firewall rule, the profile performs two key functions:

  * **Route traffic** : the security profile identifies the [endpoint group](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/endpoint-groups-overview) associated with your Virtual Private Cloud (VPC) network. The endpoint group points to a producer's [deployment group](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/deployment-groups-overview). This producer's deployment group organizes your network resources, such as virtual machines (VMs), and defines the traffic scope the integration service can monitor.

  * **Attach the profile** : the mirrored packets carry the [security profile group](https://docs.cloud.google.com/network-security-integration/docs/security-profile-groups-overview) [`data_path_id`](https://docs.cloud.google.com/network-security-integration/docs/understand-geneve#profile_id), which can be used for policy enforcement on the collector. A collector is a user-managed destination in the [producer network](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview#producer-components). A collector receives mirrored traffic from the [consumer network](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview#consumer-components) for inspection.




This document provides an overview of security profiles and their specific configuration capabilities.

## Specifications

  * Network Security Integration supports security profiles of type `CUSTOM_MIRRORING`.

  * The name of a security profile is configured in the following URL identifier format:

    * **Organization-level** : `organizations/ORGANIZATION_ID/locations/global/securityProfiles/NAME`

    * **Project-level** : `projects/PROJECT_ID/locations/global/securityProfiles/NAME`

The `NAME` of the security profile must meet the following requirements:

    * A string 1-63 characters long
    * Contains only lowercase alphanumeric characters or hyphens (-)
    * Starts with a letter

Examples:

    * **Organization-level security profile** : `organizations/2345678432/locations/global/securityProfiles/example-security-profile`.
    * **Project-level security profile** : `projects/my-project-123/locations/global/securityProfiles/example-security-profile`.

If you use the unique URL identifier for the security profile name, the URL already includes the organization or project, and the location. If you specify only the short name, you must provide the organization ID or the project ID and the location separately when you use `gcloud` commands.

  * After you create a security profile, you have the option to attach it to a [security profile group](https://docs.cloud.google.com/network-security-integration/docs/security-profile-groups-overview). This security profile group is referenced by the network firewall policy of the VPC network where you want to process your network traffic within Network Security Integration.

  * Traffic that matches the network firewall policy rule is sent to the [endpoint group](https://docs.cloud.google.com/network-security-integration/docs/endpoint-groups-overview) referenced by the security profile.

  * Each security profile must have an associated project ID. The associated project is used for quotas and access restrictions on security profile resources. If you authenticate your service account by using the [`gcloud auth activate-service-account` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account), you can associate your service account with the security profile. For more information, see [Create and manage custom security profiles](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-custom-security-profiles).




## Identity and Access Management roles

The following table describes the Identity and Access Management (IAM) roles required for managing the security profiles:

Ability | Necessary role  
---|---  
Create a custom security profile  | [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) on the organization or the project where you want to create a custom security profile.  
Modify a custom security profile  | [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) on the organization or the project where the custom security profile exists.  
View details about the custom security profile in an organization or a project  | Any of the following roles on the organization or the project where the custom security profile exists: 

  * [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`)
  * [Compute Network User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`compute.networkUser`)
  * [Compute Network Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`compute.networkViewer`)

  
View all custom security profiles in an organization or a project  | Any of the following roles on the organization or the project where the custom security profile exists: 

  * [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`)
  * [Compute Network User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`compute.networkUser`)
  * [Compute Network Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`compute.networkViewer`)

  
Use a custom security profile in a security profile group  | Any of the following roles on the organization or the project where the custom security profile exists: 

  * [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`)
  * [Compute Network User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`compute.networkUser`)

  
  
If you don't have the [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`), you can create and manage a custom security profile with the following permissions:

  * `networksecurity.securityProfiles.create`
  * `networksecurity.securityProfiles.delete`
  * `networksecurity.securityProfiles.get`
  * `networksecurity.securityProfiles.list`
  * `networksecurity.securityProfiles.update`
  * `networksecurity.securityProfiles.use`



For more information about the IAM permissions and the predefined roles, see [IAM permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference).

## Quotas

To view quotas associated with custom security profiles, see [Quotas and limits](https://docs.cloud.google.com/network-security-integration/docs/quotas).

## What's next

  * [Create and manage security profile groups](https://docs.cloud.google.com/network-security-integration/docs/configure-security-profile-groups)
  * [Create and manage custom mirroring security profiles](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-custom-security-profiles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

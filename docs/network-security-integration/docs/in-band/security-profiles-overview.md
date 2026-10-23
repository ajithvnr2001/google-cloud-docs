---
url: https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profiles-overview/
title: Security profiles overview \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:18.062587+00:00
---

# Security profiles overview  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profiles-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Security profiles overview Stay organized with collections  Save and categorize content based on your preferences. 

A _security profile_ is a custom global policy that the intercept firewall rules apply to the intercepted traffic.

Security profiles define how the Network Security Integration service handles your network traffic. You use security profiles to associate an endpoint group with the Virtual Private Cloud (VPC) network. When used with a firewall rule, a security profile directs the network traffic to the intercept endpoint group.

This page provides a detailed overview of security profiles and their capabilities.

## Specifications

Security profiles have the following specifications:

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

  * After you create a security profile, attach it to a [security profile group](https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profile-groups-overview). This network firewall policy of the VPC network references the security profile to process your network traffic within Network Security Integration.

  * Traffic that matches the network firewall policy rule is sent to the [endpoint group](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-groups-overview) referenced by the security profile.

  * Associate each security profile with a project ID. The associated project is used for quotas on security profile resources. If you authenticate your service account by using the [`gcloud auth activate-service-account` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account), you can associate your service account with the security profile. To learn more about how to create a security profile, see [Create and manage custom security profiles](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-security-profiles).




## Identity and Access Management roles

The following table describes the Identity and Access Management (IAM) roles required for managing the security profiles:

Ability | Necessary role  
---|---  
Create a custom intercept security profile  | [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) on the organization or the project where you want to create a custom security profile.  
Modify a custom intercept security profile  | [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) on the organization or the project where the custom security profile exists.  
View details about the custom intercept security profile in an organization or a project  | [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) on the organization or the project where the custom security profile exists.  
View all custom intercept security profiles in an organization or a project  | [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) on the organization or the project where the custom security profile exists.  
Use a custom intercept security profile in a security profile group  | [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) on the organization or the project where the custom security profile exists.  
  
If you don't have the [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`), you can create a custom intercept security profile with the following permissions:

  * `networksecurity.securityProfiles.create`
  * `networksecurity.securityProfiles.delete`
  * `networksecurity.securityProfiles.get`
  * `networksecurity.securityProfiles.list`
  * `networksecurity.securityProfiles.update`
  * `networksecurity.securityProfiles.use`



For more information about the IAM permissions and the predefined roles, see [IAM permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference).

## Quotas

To view quotas associated with custom intercept security profiles, see [Quotas and limits](https://docs.cloud.google.com/network-security-integration/docs/quotas).

## What's next

  * [Create and manage security profile groups](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-security-profile-groups)
  * [Create and manage custom intercept security profiles](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-security-profiles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

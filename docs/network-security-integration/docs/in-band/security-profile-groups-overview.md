---
url: https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profile-groups-overview/
title: Security profile groups overview \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:24.920833+00:00
---

# Security profile groups overview  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profile-groups-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Security profile groups overview Stay organized with collections  Save and categorize content based on your preferences. 

A security profile group is a container for custom intercept security profiles. An intercept rule references a security profile group to enable the processing of network traffic within Network Security Integration.

This page provides a detailed overview of security profile groups and their capabilities.

## Specifications

Security profile groups have the following specifications:

  * A security profile group is a global organizational-level or a project-level resource.

  * The name of a security profile group is configured in the following URL identifier format:

    * **Organization-level** : `organizations/ORGANIZATION_ID/locations/global/securityProfileGroups/NAME`

    * **Project-level** : `projects/PROJECT_ID/locations/global/securityProfileGroups/NAME`

The `NAME` of the security profile group must meet the following requirements:

    * A string 1-63 characters long
    * Contains only lowercase alphanumeric characters or hyphens (-)
    * Starts with a letter

Examples:

    * **Organization-level security profile group** : `organizations/2345678432/locations/global/securityProfileGroups/example-security-profile-group`.
    * **Project-level security profile group** : `projects/my-project-123/locations/global/securityProfileGroups/example-security-profile-group`.

If you use the unique URL identifier for the security profile group name, the URL already includes the organization or project, and the location. If you specify only the short name, you must provide the organization ID or the project ID and the location separately when you use `gcloud` commands.

  * You can add only one [security profile](https://docs.cloud.google.com/network-security-integration/docs/security-profiles-overview) to a security profile group.

  * A firewall rule must contain the name of the security profile group to be used by the intercept endpoints.

  * Security profile groups apply to in-band integration firewall policies only when you add a firewall rule with the action `APPLY_SECURITY_PROFILE_GROUP`. You can configure security profile groups in [hierarchical firewall policy rules](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#create-rules) and [global network firewall policy rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#create-rules).

  * Depending on the firewall rule's flag direction, the rule can affect both incoming and outgoing traffic within the Virtual Private Cloud (VPC) network. The intercepted traffic is then sent to the intercept endpoint group defined in the security profile referenced by the configured security profile group. Subsequently, the intercept endpoint group redirects the intercepted traffic to the producer deployment group attached by network deployments.

  * Each security profile group must have an associated project ID. The associated project is used for quotas. If you authenticate your service account by using the [`gcloud auth activate-service-account` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account), you can associate your service account with the security profile group. To learn more about how to create a security profile group, see [Create and manage security profile groups](https://docs.cloud.google.com/network-security-integration/docs/configure-security-profile-groups).

  * When you add security profiles to a security profile group, the following constraints apply:

    * An organization-level security profile group can reference only organization-level security profiles.
    * A project-level security profile group can reference only project-level security profiles in the same project.



## Identity and Access Management roles

The following table describes the Identity and Access Management (IAM) roles required for managing the security profile groups:

Ability | Necessary role  
---|---  
Create a security profile group  | [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) on the organization or the project where you want to create a security profile group.  
Modify a security profile group  | [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) on the organization or the project where the security profile group exists.  
View details about the security profile group in an organization or a project  | [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) on the organization or the project where the security profile group exists.  
View all security profile groups in an organization or a project  | [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) on the organization or the project where the security profile group exists.  
Use a security profile group in an in-band integration policy rule in an organization or a project  | [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) on the organization or the project where the security profile group exists.  
  
If you don't have the [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`), you can create security profile groups with the following permissions:

  * `networksecurity.securityProfileGroups.create`
  * `networksecurity.securityProfileGroups.delete`
  * `networksecurity.securityProfileGroups.get`
  * `networksecurity.securityProfileGroups.list`
  * `networksecurity.securityProfileGroups.update`
  * `networksecurity.securityProfileGroups.use`



For more information about IAM permissions and predefined roles, see [IAM permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference).

## Quotas

To view quotas associated with security profile groups, see [Quotas and limits](https://docs.cloud.google.com/network-security-integration/docs/quotas).

## What's next

  * [Create and manage security profile groups](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-security-profile-groups)
  * [Create and manage custom intercept security profiles](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-security-profiles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

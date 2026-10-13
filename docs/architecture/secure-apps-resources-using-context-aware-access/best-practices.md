---
url: https://docs.cloud.google.com/architecture/secure-apps-resources-using-context-aware-access/best-practices/
title: Best practices for securing apps and resources by using context-aware access \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:07:27.921144+00:00
---

# Best practices for securing apps and resources by using context-aware access  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/secure-apps-resources-using-context-aware-access/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Best practices for securing apps and resources by using context-aware access Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-07-22 UTC

This document describes recommended best practices for using context-aware access to help protect your Google Cloud resources effectively. Context-aware access is a security approach where you control users' access based on their authentication strength, device posture, network location, geographic location, or other attributes. This approach goes beyond using basic user identities for security access, and it can help you implement a [zero-trust](https://cloud.google.com/learn/what-is-zero-trust) security model to enhance your overall security posture. For details about how to implement context-aware access for different types of apps and resources, see [Secure apps and resources by using context-aware access](https://docs.cloud.google.com/architecture/secure-apps-resources-using-context-aware-access).

To help secure your apps and Google Cloud resources, you can define granular access control, based on a variety and combination of contextual factors. You can use Access Context Manager to define access policies, which contain _access levels_ and service parameters.

This document is intended for any security professional who's responsible for Identity and Access Management (IAM) and the security of Google Cloud resources and apps. This document assumes that you're already familiar with Access Context Manager, Google Cloud, and IAM management.

## Context-aware access approaches

When you set up context-aware access in your organization, you must decide whether you want to apply context-aware access controls to apps, resources, or both. To make that decision, it's useful to distinguish between the following different types of apps and services:

  * **Administrative apps** : These apps let users manage or interact with Google Cloud resources such as VM instances, BigQuery datasets, or Cloud Storage buckets. Examples of administrative apps include the Google Cloud console, Google Cloud CLI, Terraform, and [IAP Desktop](https://googlecloudplatform.github.io/iap-desktop/).
  * **Line-of-business apps** : These apps include web apps that run on Google Cloud and use SAML or Identity-Aware Proxy (IAP) for authentication and authorization. These apps are sometimes called _internal apps_. Examples of line-of-business apps include CRM systems, dashboards, and other custom apps.
  * **Google Workspace and other Google services** : These services are provided by Google, but they aren't related to Google Cloud.



You can further distinguish line-of-business apps based on how they handle authentication and authorization:

  * **SAML** : Apps that use Google Workspace SAML for authentication. SaaS apps often fall into this category.
  * **IAP** : Custom web apps that you've deployed behind IAP.
  * **OAuth** : Custom web or desktop apps that use OAuth 2.0 and use one or more [Google Cloud OAuth scopes](https://docs.cloud.google.com/storage/docs/oauth-scopes).



The following flow diagram shows the most suitable context-aware access approach for each type of app:

![Decision tree for context-aware access approaches for each type of app.](https://docs.cloud.google.com/static/architecture/images/context-aware-access-best-practices-diagram.svg)

The diagram shows the following types of apps:

  * **Administrative apps** : Generally, it's more important to protect the Google Cloud resources that the administrative app facilitates access to, rather than the app itself. Consider the following scenarios:

    * A user can't access any of the resources. In this scenario, it's likely that having access to an administrative app is not as valuable to the user.
    * A user has access to a resource, but can't access an administrative app. In this scenario, they might be able to find a different administrative app that isn't blocked and lets them access the resource.

Therefore, for administrative apps, take a resource-centric approach. For the most effective way to apply the right context-aware access controls to resources, use Virtual Private Cloud (VPC) service perimeters with the appropriate ingress rules. You can complement the VPC service perimeters with access bindings.

  * **Line-of-business apps that use OAuth** : For these apps, it's important to protect access to the apps themselves, as well as the resources that the apps might use. To protect the apps by using context-aware access, use access bindings.

  * **Line-of-business apps that use IAP** : Although IAP uses OAuth, you can't use access bindings to protect apps that use IAP to authenticate users. Instead, protect these apps by using IAM conditions.

  * **Line-of-business apps that use SAML** : Similar to line-of-business apps that use OAuth, it's important to protect access to the apps themselves, as well as the resources that the apps might use. To protect these apps, use Google Workspace context-aware access.

  * **Google Workspace and other Google services** : For these apps, it's important to protect access to the apps themselves, as well as the resources that the apps might use. To protect these apps, use Google Workspace context-aware access.




## Access level management

The following sections describe the recommended practices to use when you manage access levels.

### Create reusable access levels

Access levels are a global resource and are intended to be used across resources in your Google Cloud organization. Therefore, it's best to limit the overall number of access levels, and make them meaningful and applicable across multiple resources. Consider the following:

  * Avoid embedding the names of specific resources or apps in the name of an access level.
  * Avoid encoding any resource-specific or app-specific requirements in an access level.
  * Use names that assert a certain user or device posture, such as `Fully Trusted Device`.



### Use composite access levels

To help reduce the maintenance overhead and ensure consistency when the subnetworks or regions change, don't repeat the same requirements in multiple access levels. Instead, let access levels [depend on each other](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#access-level-dependency).

For example, don't list the same trusted [regions](https://docs.cloud.google.com/docs/geography-and-regions) or IP subnetworks in multiple access levels, but instead create an additional access level called `Trusted location`. This `Trusted location` level can serve as a dependency for the other access levels.

### Exempt emergency access users in access levels

To prevent an accidental lockout, it's best to exclude at least one emergency access user from all of the access levels. To ensure that the exemption applies to all of the apps and resources that you apply the access level to, configure the exemption in the access level itself:

  * Add one condition that defines your regular requirements.
  * Add another condition with a [`members` requirement](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#condition) that lists one or more of your emergency access users.
  * Set the combining function to an `OR`condition so that users only need to meet one of the two conditions.



For example, the following access level restricts access to three regions, but the user `emergencyaccess@example.net` is exempt from this requirement:
    
    
    {
      "name": "accessPolicies/…",
      "title": "Example access level",
      "basic": {
        "conditions": [
          {
            "members": [
              "user:emergencyaccess@example.net"
            ]
          },
          {
            "regions": [
              "DE",
              "AU",
              "SG"
            ]
          }
        ],
        "combiningFunction": "OR"
      }
    }
    

### Configure a remediation message

Users in your organization might not be aware that their location, device, and other factors can impact whether they're allowed to access certain apps or not. To keep users informed, and to help reduce support requests, configure a custom [remediation message](https://support.google.com/a/answer/11560430) that gives users the steps to take to regain access.

## Access bindings management

Access bindings let you configure context-aware access for OAuth apps that use one or more Google Cloud scopes. Access bindings are also an effective way to enforce context-aware access for line-of-business apps.

The following sections describe recommended practices to use when you use access bindings.

### Use a single access binding with scoped settings

When you use access bindings, you must consider the following constraints:

  * Each Cloud Identity group can have a maximum of one access binding.
  * If more than one access binding applies to a user, the less restrictive access binding takes precedence.



To accommodate these two constraints, use a single access binding that applies to all of your users:

  1. [Create a group that automatically contains all of the users](https://support.google.com/a/answer/9689259) of your Cloud Identity or Google Workspace account.
  2. Create or use an access binding that associates a default access level with the group. The default access level should be appropriate for most users, devices, and apps.
  3. If necessary, use [scoped access settings (`scopedAccessSettings`)](https://docs.cloud.google.com/chrome-enterprise-premium/docs/apply-policies-to-user-groups#define_configurations_for_specific_applications) to assign weaker access levels to selected apps.



### Use a strict default access level

If an access binding specifies both a scoped access setting and a default access level, then the two access levels are combined by using `OR` semantics. This behavior has the following implications:

  * A user needs to meet only one of the access levels to access the OAuth app.
  * When you add a scoped access setting for an OAuth app, you can _lower_ the effective access requirements.
  * A scoped access setting has no effect if it uses an access level that is more strict than the access binding's default access level.



When you select a default access level for an access binding, we recommend that you do the following:

  * Use a strict access level as the default access level.
  * Apply lower access levels to individual OAuth apps by using scoped access settings.



Consider adding some or all of the following restrictions to the default access level:

  * **Browser and device restrictions** : Require that your users access apps by using a managed Chrome browser and an administrator-approved device.
  * **Geographic restrictions** : If your organization operates exclusively in certain regions, use [region restrictions](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#regions) to include only those regions in the allowlist. Otherwise, you can use region restrictions to restrict access to geographies that have sanctions against them or that aren't relevant for other reasons.
  * **IP network restrictions** : If users in your organization access Google Cloud exclusively from certain networks, or if your organization uses a common egress proxy, you can include IP network restrictions.



Don't use access levels that require certificate-based authentication as a default access level. Certificate-based authentication is best suited for VPC service perimeter ingress rules.

### Manage exceptions by app

To manage exceptions to the default access level, add exceptions for individual apps, instead of exceptions for users or groups.

A strict default access level might be appropriate for most apps, but not for all of your apps:

  * Some apps might be less sensitive, and you need to make them accessible to users that don't meet the default access level. Examples might include apps that must be accessible to partners, guests, or alumni.
  * Some apps might be technically incompatible with one of the restrictions that are enforced by the default access level.



To exempt individual apps from the default access level, use scoped access settings. For each affected app, add a scoped setting and assign an access level that's more appropriate for the individual app.

Don't create additional access bindings to manage exceptions by user or group. Additional access bindings can cause the following issues:

  * You might inadvertently create overlapping access bindings.
  * It might become difficult to determine which context-aware access requirements are being enforced effectively for individual apps.



### Avoid overlapping access bindings

Access bindings are associated with groups. If a user is a member of multiple groups, multiple access bindings could apply to them. In this case, the context-aware access requirements of these access bindings are combined by using `OR` semantics.

This behavior can cause unintended effects. For example, when users are allowed to join additional groups, the protection of certain apps might be undermined.

To help prevent such situations, we recommend that you avoid overlapping access bindings:

  * Minimize the number of access bindings, ideally to one.
  * If you need multiple access bindings, assign them to groups that are mutually exclusive.



### Protect groups from unauthorized modification

By default, Cloud Identity allows group members to leave a group. This behavior is appropriate for [access groups](https://docs.cloud.google.com/iam/docs/groups-best-practices#access), but it's problematic for groups with associated access bindings. If a user leaves a group that has an associated access binding, they're no longer subject to the context-aware access requirements that are imposed by the access bindings. Therefore, users can circumvent context-aware access requirements by leaving a group.

Always use [enforcement groups](https://docs.cloud.google.com/iam/docs/groups-best-practices#enforcement) and don't allow users to leave an enforcement group when you configure access bindings. Alternatively, [create a group that automatically contains all of the users](https://support.google.com/a/answer/9689259) of your Cloud Identity or Google Workspace account.

### Don't allow external user access when you use access bindings

Access bindings only affect users of the Cloud Identity or Google Workspace account that your Google Cloud organization belongs to. These users are still subject to the access bindings in _your_ Google Cloud organization if they attempt to access resources in _other_ Google Cloud organizations. This application of access bindings on users is different from behavior in other contexts with Cloud Identity.

If you allow users from external Cloud Identity or Google Workspace accounts to access resources in your Google Cloud organizations, your access bindings have no effect on those users.

To help ensure that your access bindings are effective, don't grant external users access to any apps or resources in your Google Cloud organization. Also, don't add external users to groups in your Cloud Identity or Google Workspace account.

### Use separate access bindings for session length control

In addition to context-aware access control, you can also use access bindings to manage the length of browser sessions and OAuth tokens.

When you use access bindings to control context-aware access, it's best to avoid overlapping access bindings.

When you use access bindings to control session length, don't create overlapping access bindings. If more than one such access binding applies to a user, only the last-updated access binding takes effect, which can lead to unintended results.

To help prevent such unintended results, use a separate access binding to control session length.

### Don't allow users to act as a service account

Access bindings apply to Cloud Identity and Google Workspace users, but access bindings don't affect service accounts. If you allow users to authenticate and act as a service account, they might be able to undermine your context-aware access controls.

Other risks are involved when users are able to act as a service account. If you want to let users temporarily elevate their privileges, we recommend that you use [Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-overview). Don't use service account impersonation, except for development purposes.

For more information about how to secure service accounts and service account keys, see [Best practices for using service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts) and [Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

## Ingress rules for VPC service perimeters

Ingress rules let you grant context-aware access from outside the service perimeter to resources inside the perimeter. VPC service perimeters and ingress rules protect Google Cloud resources, not individual apps. Therefore, a service perimeter with ingress rules is ideal to enforce context-aware access for administrative tools such as the Google Cloud console and the gcloud CLI.

For more information and best practices about VPC service perimeters, see [Best practices for enabling VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/enable).

The following sections describe recommended practices for when you use ingress rules to enforce context-aware access.

### Include IAP TCP forwarding as a restricted service

It can be risky to allow users to connect to VM instances in your service perimeter by using SSH or RDP for the following reasons:

  * Your ingress rules don't apply to the connections because SSH and RDP usage doesn't involve any Google API access.
  * After users establish an SSH or RDP session, any API access that's initiated from within that session is considered to have originated from within the service perimeter. Therefore, your ingress rules don't apply to any API access initiated from within that session.



To mitigate these risks, allow [SSH and RDP access to VMs](https://docs.cloud.google.com/architecture/secure-apps-resources-using-context-aware-access#ssh_and_rdp_access_to_vms) only through IAP TCP forwarding:

  * Include the [`iaptunnel.googleapis.com` service](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_iap_tcp) as a restricted service.
  * Configure [firewall rules](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#create-firewall-rule) that restrict access to SSH and RDP ports through IAP TCP forwarding.



Use IAP TCP forwarding to help ensure that the configuration of your VPC service perimeter's ingress rules apply to every SSH and RDP access attempt.

### Use certificate-based access for sensitive service perimeters

By default, Google access tokens and refresh tokens aren't bound to a device and they can be vulnerable to theft or replay attacks. To help mitigate these risks, you can use [certificate-based access (CBA)](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-resources-with-certificate-based-access), which restricts access to devices that possess a trusted X.509 certificate.

CBA helps you to strengthen security, but this approach also adds additional infrastructure requirements:

  * A user's device must have an X.509 certificate that's issued by an internal certificate authority.
  * The key associated with the certificate must be stored in a way that prevents unauthorized export.
  * Client apps must use mutual TLS (mTLS) authentication to connect to Google Cloud APIs.



Use CBA to protect access to your most sensitive VPC service perimeters. This approach lets you balance security strength with minimal infrastructure requirements and overall impact.

## Contributors

Author: [Johannes Passing](https://www.linkedin.com/in/johannespassing) | Cloud Solutions Architect

Other contributor: [Ido Flatow](https://www.linkedin.com/in/idoflatow) | Cloud Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/architecture/secure-apps-resources-using-context-aware-access/
title: Secure apps and resources by using context-aware access \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:15.388800+00:00
---

# Secure apps and resources by using context-aware access  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/secure-apps-resources-using-context-aware-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Secure apps and resources by using context-aware access Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-07-22 UTC

This document describes how you can use context-aware access to secure different types of apps and resources. Context-aware access is a security approach where you control users' access based on their authentication strength, device posture, network location, geographic location, or other attributes. This approach goes beyond using basic user identities for security access, and it can help you implement a [zero-trust](https://cloud.google.com/learn/what-is-zero-trust) security model to enhance your overall security posture. For details about best practices, see [Best practices for securing apps and resources by using context-aware access](https://docs.cloud.google.com/architecture/secure-apps-resources-using-context-aware-access/best-practices).

To help secure your apps and Google Cloud resources, you can define granular access controls based on a variety and combination of contextual factors. You can use Access Context Manager to define access policies, which contain _access levels_ and service parameters.

This document is intended for any security professional who's responsible for Identity and Access Management (IAM) and the security of Google Cloud resources and apps. This document assumes that you're already familiar with Access Context Manager, Google Cloud, and IAM management.

## Access levels

Access levels let you define a set of requirements that users and their devices must satisfy to meet a certain level of trust.

For example, you can use [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) to configure the following access levels for your organization:

  * **Basic** : A basic set of requirements that you consider to be the minimum level.
  * **Medium** : A more stringent set of requirements that you expect employees and corporate devices to meet. This access level might exclude extended workforce users and non-corporate devices.
  * **High** : Strict requirements that only certain employees and devices meet.



An access level by itself doesn't have any immediate effect on users or devices. The access level specifies requirements, but it doesn't define the users, apps, or resources that those requirements should be enforced upon. An access level is like a reusable piece of configuration that you can refer to when you configure access to specific apps or resources.

Google Cloud lets you use access levels for several different types of apps or resources, including the following, which are described in this document:

  * Google Workspace and other apps and services outside of Google Cloud
  * The Google Cloud console and Google Cloud APIs
  * Virtual Private Cloud (VPC) service perimeters
  * Identity-Aware Proxy (IAP) for SSH and RDP access
  * IAP for web apps



## Apps and resources

The following sections describe how you can apply access levels to the different types of apps and resources and how the processes differ across the different types.

### Google Workspace and other apps and services outside of Google Cloud

Apps and services outside of Google Cloud that support context-aware access include the following:

  * Google Admin console
  * Google Workspace apps such as Gmail, Google Meet, and Google Calendar
  * Other Google apps such as Gemini or Data Studio
  * [Custom SAML apps](https://support.google.com/a/answer/6087519)



To restrict access to Google Workspace and apps and services outside of Google Cloud, [configure context-aware access](https://support.google.com/a/answer/9261439) for each service or app individually in the Admin console. In the Admin console, you do the following:

  * Define the scope for which you want to apply an access level. A scope is a combination of the following:

    * A specific service or SAML app to protect.
    * An organizational unit (OU) or a group that contains relevant users.
  * Select the access level to apply to the selected scope.




When you assign an access level, you can also change that access level's settings. You can specify that the access level only applies when users access the web app directly. Or, you can specify that the level also applies when mobile apps and other apps access the API. For details, see [App behavior based on access level settings](https://support.google.com/a/answer/9261439#zippy=%2Capp-behavior-based-on-access-level-settings) in "Assign Context-Aware access levels to apps".

There could be more than one assignment that applies to a particular user and app. For example, a user might be a member of the _Employees_ OU and a member of the _all-apac_ team. The respective OU and group might have different access levels assigned to them. In this case, Cloud Identity and Google Workspace apply only one of the assignments, which is [the one with the highest priority](https://support.google.com/a/answer/9668676):

  * Group-based assignments have a higher priority than OU-based assignments.
  * Within groups, you can customize their relative priority.
  * Within OUs, the root OU has the lowest relative priority.



Cloud Identity and Google Workspace let you review and analyze context-aware access events in the [Context Aware Access log](https://support.google.com/a/answer/9394107#zippy=%2Caudit-and-investigation-tool).

### The Google Cloud console and Google Cloud APIs

You can configure context-aware access to the Google Cloud console and Google Cloud APIs by using [access bindings](https://docs.cloud.google.com/chrome-enterprise-premium/docs/manage-access-bindings).

Google Cloud APIs use OAuth 2.0 for authentication. To use a Google Cloud API, users need a valid, Google-issued OAuth access token, and the token must be issued for one of the [Google Cloud OAuth scopes](https://docs.cloud.google.com/storage/docs/oauth-scopes). Access bindings restrict users' ability to acquire such access tokens. As a result, access bindings limit access to the Google Cloud console and to all OAuth apps that use Google Cloud OAuth scopes, like the following:

  * The gcloud CLI
  * Third-party tools such as Terraform
  * [OAuth apps that you created yourself](https://developers.google.com/workspace/guides/configure-oauth-consent) and that use a Google Cloud OAuth scope



An access binding links a group to an access level. Each group can have only one access binding. Each access binding can define the following [configurations](https://docs.cloud.google.com/chrome-enterprise-premium/docs/apply-policies-to-user-groups#define_configurations_for_specific_applications):

  * A `scopedAccessSettings` list that assigns access levels to individual OAuth apps.
  * A default access level.



If an access binding specifies both a scoped access setting and a default access level, then the two access levels are combined by using `OR` semantics. Then, a user needs to meet only one of the access levels to access the OAuth app.

An access binding applies to both direct and indirect members of the group. If a user is a member of multiple groups, multiple access bindings could apply to them, which could result in multiple access levels. In this case, the access levels are also combined by using `OR` semantics, which means that the user needs to meet only one of the access levels.

**Note:** In this context, the evaluation of access levels and access bindings is different from how they're evaluated in other contexts. For Cloud Identity and Google Workspace, only the access level with the highest priority is applied. For [session length controls](https://docs.cloud.google.com/chrome-enterprise-premium/docs/session-controls-for-reauthentication#define_session_length_and_re-authentication_methods), only the most recently created access binding is applied.

### VPC service perimeters

When you [create a VPC service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters), you specify a list of restricted services. Restricted services can be accessed from within the service perimeter, but by default they can't be accessed from outside the service perimeter.

To allow access from outside the service perimeter, you use [ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference). Ingress rules let you specify the conditions under which you want to allow external access. You can use access levels to let an ingress rule enforce context-aware access.

A VPC service perimeter can have multiple ingress rules. As a result, more than one ingress rule might apply to a particular user and app, and these ingress rules might require different access levels. In this case, the access levels are evaluated using `OR` semantics and the user needs to meet only one of the access levels.

**Note:** In this context, the evaluation of access levels is similar to how access bindings are combined by using `OR` semantics for the Google Cloud console and Google Cloud APIs. However, this behavior is different from how Cloud Identity and Google Workspace apply only the access level with the highest priority.

You can combine access bindings with VPC service perimeter ingress rules. If the access bindings and ingress rules specify different access levels for a particular user and app, then the levels are combined by using `AND` semantics. In that case, the user must meet both access levels.

To review and analyze the attempts to access resources in a VPC service perimeter, you can use the [VPC Service Controls audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging) or [VPC Service Controls violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer).

### SSH and RDP access to VMs

You can configure context-aware access for SSH and RDP access to VMs by using IAP TCP forwarding.

IAP TCP forwarding supports access bindings and VPC service perimeter ingress rules. Your access bindings for the Google Cloud console and Cloud APIs automatically apply to IAP TCP forwarding.

If your service perimeter includes the [`iaptunnel.googleapis.com` service](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_iap_tcp) as a restricted service, then your ingress rules automatically apply to IAP TCP forwarding. For details about best practices, see [Include IAP TCP forwarding as a restricted service](https://docs.cloud.google.com/architecture/secure-apps-resources-using-context-aware-access/best-practices#include-iap-tcp-forwarding-as-a-restricted-service).

You can also configure context-aware access by using IAM conditions. You can use IAM conditions as an alternative to access bindings and VPC service perimeter ingress rules, or use all of them together.

  * Grant a user or group the IAP-secured Tunnel User role (`roles/iap.tunnelResourceAccessor`). Then, in the role binding, add an [IAM condition expression](https://docs.cloud.google.com/iam/docs/conditions-overview#example-access-level) that requires the user to meet a certain access level. For example, the expression could look similar to the following:
        
        "accessPolicies/123/accessLevels/fully-trusted" in request.auth.access_levels
        

  * Optionally, you can customize the IAM condition to require multiple access levels or to include other checks.




A particular user and app can be subject to an access binding, an ingress rule, and an IAM condition when the user and app access IAP TCP forwarding. In this scenario, access levels are combined by using `AND` semantics and the user must meet all of the access levels.

To review and analyze the attempts to access IAP TCP forwarding, you must [enable data access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) for IAP.

### Web apps

You can configure context-aware access for web apps [by using IAP](https://docs.cloud.google.com/iap/docs/concepts-overview).

IAP for web apps differs from its IAP TCP forwarding counterpart:

  * Access bindings don't apply to web apps that are configured with IAP because the OAuth app that IAP uses doesn't use any Google Cloud OAuth scopes.
  * VPC service perimeter ingress rules don't apply to web apps that are configured with IAP because IAP isn't a Google Cloud API and it can't be configured as a restricted service.



To configure context-aware access for web apps by using IAP, you must use IAM conditions:

  * Grant a user or group the IAP-secured Web App User role (`roles/iap.httpsResourceAccessor`). Then, in the role binding, add an [IAM condition expression](https://docs.cloud.google.com/iam/docs/conditions-overview#example-access-level) that requires the user to meet a certain access level. For example, the expression could look similar to the following:
        
        "accessPolicies/123/accessLevels/fully-trusted" in request.auth.access_levels
        

  * Optionally, you can customize the IAM condition to require multiple access levels or to include other checks.




To review and analyze the attempts to access web apps that are configured with IAP, you must [enable data access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) for IAP.

**Note:** You can't use context-aware access for [instances that use external identities](https://docs.cloud.google.com/iap/docs/enable-external-identities).

## What's Next?

  * [Best practices for securing apps and resources by using context-aware access](https://docs.cloud.google.com/architecture/secure-apps-resources-using-context-aware-access/best-practices).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Johannes Passing](https://www.linkedin.com/in/johannespassing) | Cloud Solutions Architect

Other contributor: [Ido Flatow](https://www.linkedin.com/in/idoflatow) | Cloud Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 

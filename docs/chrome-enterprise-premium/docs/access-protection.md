---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-protection/
title: Chrome Enterprise Premium access protection overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:21.531026+00:00
---

# Chrome Enterprise Premium access protection overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback 

#  Chrome Enterprise Premium access protection overview Stay organized with collections  Save and categorize content based on your preferences. 

Based on the [BeyondCorp](https://docs.cloud.google.com/beyondcorp) security model, Chrome Enterprise Premium is an approach that utilizes a variety of Google Cloud offerings to enforce granular access control based on a user's identity and context of the request.

For example, depending on the policy configuration, your sensitive app or resource can:

  * Grant access to all employees if they're using a trusted corporate device from your corporate network.
  * Grant access to employees in the Remote Access group if they're using a trusted corporate device with a secure password and up-to-date patch level, from any network.
  * Grant administrators access to the Google Cloud console (via UI or API) only if they are coming from a corporate network.
  * Grant developers SSH access to virtual machines.



## When to use Chrome Enterprise Premium

Use Chrome Enterprise Premium when you want to establish fine-grained access control based on a wide range of attributes and conditions including what device is being used and from what IP address. Making your corporate resources context-aware improves your security posture.

You can also apply Chrome Enterprise Premium to Google Workspace apps. For more information about implementing Chrome Enterprise Premium with Google Workspace, see the [Google Workspace overview](https://support.google.com/a/answer/9275380).

## How Chrome Enterprise Premium works

Implementing Chrome Enterprise Premium enacts a zero trust model. No one can access your resources unless they meet all the rules and conditions. Instead of securing your resources at the network-level, access controls are instead put on individual devices and users.

IAP is the base of Chrome Enterprise Premium, letting you grant access to your HTTPS apps and resources. Once you've secured your apps and resources behind IAP, your organization can gradually extend Chrome Enterprise Premium as richer rules are needed. Extended Chrome Enterprise Premium resources can limit access based on properties like user device attributes, time of day, and request path.

Chrome Enterprise Premium works by leveraging four Google Cloud offerings:

  * **[Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview)** : A service that enables employees to access corporate apps and resources from untrusted networks without the use of a VPN.

  * **[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview)** : The identity management and authorization service for Google Cloud.

  * **[Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview)** : A rules engine that enables fine-grained access control.

  * **[Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/overview)** : A Google Chrome extension that collects user device details.




![Chrome Enterprise Premium flow](https://docs.cloud.google.com/chrome-enterprise-premium/images/access-protection-flow.png)

### Gathering device information

[Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/overview) gathers employee device information including encryption status, OS, and user details. Once enabled through the Google Admin console, you can deploy the Endpoint Verification Chrome extension to corporate devices. Employees can also install it on their managed, personal devices. This extension gathers and reports device information, constantly syncing with Google Workspace. The end result is an inventory of all the corporate and personal devices accessing your corporate resources.

### Limiting access

Through Access Context Manager, [access levels](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) are created to define access rules. Access levels applied on your resources with IAM Conditions enforce fine-grained access control based on a variety of attributes.

Access levels restrict access based on the following attributes:

  * [IP subnetworks](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#ip-subnetworks)
  * [Regions](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#regions)
  * [Principals](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#members)
  * [Device policy](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#device-policy)



When you create a device-based access level, Access Context Manager references the inventory of devices created by Endpoint Verification. For example, an access level can restrict access to only employees who are using encrypted devices. Coupled with [IAM conditions](https://cloud.google.com/iam/docs/conditions-overview), you could make this access level more granular by also restricting access to the time between 9am and 5pm.

### Securing resources with IAP

[IAP](https://docs.cloud.google.com/iap/docs/concepts-overview) ties everything together by letting you apply IAM conditions on Google Cloud resources. IAP lets you establish a central authorization layer for your Google Cloud resources accessed by HTTPS and SSH/TCP traffic. With IAP, you can establish a resource-level access control model instead of relying on network-level firewalls. Once secured, your resources are accessible to any employee, from any device, on any network, that meets the access rules and conditions.

### Applying IAM conditions

[IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview#syntax_overview) allow you to define and enforce conditional, attribute-based access control for Google Cloud resources.

With IAM Conditions, you can choose to grant permissions to principals only if configured conditions are met. IAM Conditions can limit access with a variety of attributes, including access levels.

Conditions are specified in the IAP role bindings of a resource's IAM policy. When a condition exists, the role is only granted if the condition expression evaluates to true. Each condition expression is defined as a set of logic statements allowing you to specify one or many attributes to check.

## What's next

  * Get started with Chrome Enterprise Premium using the [quickstart](https://docs.cloud.google.com/chrome-enterprise-premium/docs/apply-resources).
  * Learn more about: 
    * [Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/overview)
    * [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview)
    * [IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview)
    * [IAP](https://docs.cloud.google.com/iap/docs/concepts-overview)
  * [Secure your Google Workspace apps](https://support.google.com/a/answer/9275380) with Chrome Enterprise Premium.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

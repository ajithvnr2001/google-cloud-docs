---
url: https://docs.cloud.google.com/access-context-manager/docs/create-credential-strength-policy/
title: Configuring a credential strength policy \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:39:16.984866+00:00
---

# Configuring a credential strength policy  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/create-credential-strength-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Configuring a credential strength policy Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Credential strength policy**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A key principle of Chrome Enterprise Premium is "Access to services is granted based on what we know about you and your device." The level of access given to a single user or a single device is dynamically inferred by interrogating multiple data sources. This level of trust can then be used as part of the decision process.

A key element to the trust evaluation process is the strength of the user's login credentials, where access to specific types of applications is determined by how the user authenticated to the system. For example, users logged in with just a password can only access applications that do not contain any sensitive information, whereas a user logged in with a hardware security key as a second factor can access the most sensitive enterprise applications.

Credential strength based policies is a feature that allows an enterprise to enable access controls based on the strength of the credential used during the authentication process. By leveraging credential strength as another condition in access control policies, enterprises can enforce access controls based on the usage of hardware security keys, 2-step verification or other forms of strong credentials.

**Note:** To use the credential strength feature, you must be a Chrome Enterprise Premium Enterprise (managed) user.

## Credential strength policy overview

Access Context Manager allows Google Cloud organization administrators to define fine-grained, attribute based access control for projects and resources in Google Cloud.

Access levels are used for permitting access to resources based on contextual information about the request. Using access levels, you can start to organize tiers of trust. For example, you might create an access level called High_Level that will permit requests from a small group of highly-privileged individuals. You might also identify a more general group to trust, such as an IP range that you want to permit requests from. In that case, you might create an access level called Medium_Level to permit those requests.

Access Context Manager provides two ways to define access levels: basic and custom. The credential strength check currently utilizes custom access levels. The information about the credential strength used during user authentication is captured during the Google login process. That information is captured and stored in Google's sessions storage service.

Credential strength check is currently supported for Identity-Aware Proxy, Identity-Aware Proxy for TCP, and Google Workspace.

## Configuring credential strength policy

You can use an Access Context Manager [custom access level](https://cloud.google.com/access-context-manager/docs/custom-access-level-spec) definition to set the appropriate policies. Custom access levels use boolean expressions written in a subset of [Common Expression Language](https://opensource.google.com/projects/cel) (CEL) to test the attributes of a client making a request.

In the Google Cloud console, you can configure custom access levels in the **Advanced Mode** when creating an access level. To create a custom access level, complete the following steps:

  1. In the Google Cloud console, [open the Access Context Manager page](https://console.cloud.google.com/security/access-level).
  2. If you are prompted, select your organization.
  3. At the top of the Access Context Manager page, click **New**.
  4. In the **New Access Level** pane, complete the following steps: 
     1. In the **Access level title** box, enter a title for the access level. The title must be at most 50 characters, start with a letter, and can contain only numbers, letters, underscores, and spaces.
     2. For **Create Conditions in** , select **Advanced Mode**.
     3. In the **Conditions section** , enter the expressions for your custom access level.The condition must resolve to a single boolean value. For examples and more information about Common Expression Language (CEL) support and custom access levels, see the [Custom access level specification](https://cloud.google.com/access-context-manager/docs/custom-access-level-spec).
     4. Click **Save**.



## Supported credential strength values

Value | Google Definition | Example Custom Access Level  
---|---|---  
`pwd` | User authenticated with a password. | `request.auth.claims.crd_str.pwd == true `  
`push` | User authenticated with a push notification to the mobile device. | `request.auth.claims.crd_str.push == true`  
`sms` | User authenticated using a code sent to SMS or via a phone call. | `request.auth.claims.crd_str.sms == true`  
`swk` | 2SV used a software key, such as a phone, as security key. | `request.auth.claims.crd_str.swk == true`  
`hwk` | 2SV used a hardware key, such as Google Titan Key. | `request.auth.claims.crd_str.hwk == true`  
`otp` | User authenticated with one time password methods (Google Authenticator and Backup Codes). | `request.auth.claims.crd_str.otp == true`  
`mfa` | User authenticated with any of the methods in this table except `pwd`. | `request.auth.claims.crd_str.mfa == true`  
  
## Additional information about 2-step verification

Google 2-Step Verification has a feature that allows users to mark their device as trusted and avoid the need for additional 2-step challenges when signing in again on the same device. When this feature is enabled, a user who signs out and signs back in does not receive a 2-step challenge on the second sign-in, and Google would correctly report the credential strength for the second sign-in as password-only, and not Multi-Factor Authentication, since a 2-step challenge was not used on the second sign-in.

If you have applications or workflows that depend on requiring the user to always use strong credentials, you might want to disable the trusted device feature. For information about enabling or disabling the trusted device feature, see [Add or remove trusted computers](https://support.google.com/accounts/answer/2544838?co=GENIE.Platform%3DDesktop&). Note that disabling the feature will require users to present their second factors every time they sign in, even on frequently used devices. Users might have to sign out and sign back in for their most recent sign-in to have Multi-Factor Authentication assertions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

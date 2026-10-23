---
url: https://docs.cloud.google.com/looker/docs/looker-core-user-authentication/
title: User authentication methods for Looker (Google Cloud core) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:24.237081+00:00
---

# User authentication methods for Looker (Google Cloud core)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-user-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  User authentication methods for Looker (Google Cloud core) Stay organized with collections  Save and categorize content based on your preferences. 

To securely control access to your Looker (Google Cloud core) instance and its data, you can authenticate users through various identity providers. These methods help you integrate Looker (Google Cloud core) into your existing identity management systems, ensuring that authorized users can access Looker (Google Cloud core).

## Primary authentication methods

**Note:** The integration between Looker (Google Cloud core) and Workforce Identity Federation is in [preview](https://cloud.google.com/products#product-launch-stages). During the preview, the integration is supported only for Looker (Google Cloud core) instances that use [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections).

When you create a Looker (Google Cloud core) instance, you select one of the following **primary authentication methods** :

  * **[Google OAuth](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication) (default):** Authenticates users by using Google Accounts (such as Google Workspace or Cloud Identity).
  * **[Workforce Identity Federation](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity):** Authenticates users by using an external enterprise identity provider (IdP), such as Microsoft Entra ID, Okta, or PingIdentity, without requiring you to manage Google Accounts for each user.



### Why you select a primary authentication method during instance creation

Unlike in-app authentication methods such as SAML or OpenID Connect, Google OAuth and Workforce Identity Federation integrate directly with Identity and Access Management (IAM) at the Google Cloud infrastructure level.

Selecting a primary authentication method during instance creation is required for the following reasons:

  * **IAM access control:** Google Cloud provisions dedicated authentication credentials for the instance and verifies that users have required IAM permissions (such as `roles/looker.instanceUser`) before allowing them to access the instance.
  * **Initial administrator access (bootstrapping):** When a new instance is created, no users or third-party IdP settings exist within the application. The primary authentication method allows an administrator to sign in for the first time to set up the instance and configure permissions.
  * **Backup access (break-glass):** If you later configure in-app SAML or OpenID Connect and that configuration encounters an issue (such as an expired certificate or network misconfiguration), the primary authentication method provides a secure backup so administrators can still sign in and fix the issue.



## In-app authentication methods

After you create a Looker (Google Cloud core) instance, you can optionally configure in-app authentication from within the Looker Admin settings. However, to use an in-app authentication method, you must choose Google OAuth as the primary authentication method for the instance. The following in-app authentication methods are available:

  * [SAML](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml)
  * [OpenID Connect (OIDC)](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-openid-connect)

**Note:** If you use third-party identity providers, your organization is responsible for managing access and permissions for your Looker instance users. Google's [Our shared security partnership](https://cloud.google.com/looker/product/security) page outlines this responsibility. In-app SAML and OIDC handle authentication entirely within the Looker application and don't enforce IAM permissions at the Google Cloud project level.

## What's next

  * [Manage users within Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-management)
  * [Looker (Google Cloud core) access control with IAM](https://docs.cloud.google.com/looker/docs/looker-core-access-control)
  * [Looker (Google Cloud core) admin settings](https://docs.cloud.google.com/looker/docs/looker-core-admin-looker)
  * [Administer a Looker (Google Cloud core) instance from the Google Cloud console](https://docs.cloud.google.com/looker/docs/looker-core-admin-console)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

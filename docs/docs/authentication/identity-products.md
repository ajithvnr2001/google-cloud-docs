---
url: https://docs.cloud.google.com/docs/authentication/identity-products/
title: Identity management products and features \u00a0|\u00a0 Authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:41:24.741114+00:00
---

# Identity management products and features  |  Authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/authentication/identity-products/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Authentication ](https://docs.cloud.google.com/docs/authentication)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Identity management products and features Stay organized with collections  Save and categorize content based on your preferences. 

Google has various products and technologies that provide identity and access management capabilities. This page lists some of these products, to help you understand what these products offer and how they differ from one another.

If you need help with understanding a specific authentication use case, see [Authentication and authorization use cases](https://docs.cloud.google.com/docs/authentication/use-cases).

## Product list

  * Chrome Enterprise Premium
  * Cloud Identity
  * Firebase Authentication
  * Google Identity Services
  * Google Workspace
  * Identity and Access Management (IAM)
  * Identity-Aware Proxy (IAP)
  * Identity Platform
  * Workforce Identity Federation
  * Workload Identity Federation for GKE
  * Workload Identity Federation



### Chrome Enterprise Premium

[Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/docs) is a zero-trust solution that lets you provide secure access with integrated threat and data protection. You can provide an organization's workforce access to web applications securely from anywhere, without the need for a VPN. Chrome Enterprise Premium includes IAP, Endpoint Verification, and Chrome Enterprise.

For more information about Chrome Enterprise Premium, see the [Chrome Enterprise Premium overview](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview).

### Cloud Identity

[Cloud Identity](https://docs.cloud.google.com/identity) is an Identity as a Service (IDaaS) solution that centrally manages users and groups. It's built in to both Google Cloud and Google Workspace. If you are not adopting Google Workspace, Cloud Identity is available as a standalone product.

For information about Cloud Identity, see [Overview of Cloud Identity](https://docs.cloud.google.com/identity/docs/overview).

Cloud Identity is not related to Identity Platform.

### Firebase Authentication

[Firebase Authentication](https://firebase.google.com/docs/auth) is the authentication solution provided by Firebase, a backend platform for building Web, Android, and iOS applications. Firebase Authentication includes authentication support for a wide array of user account types. 

Firebase Authentication uses Identity Platform as its backend but serves a different audience: 

  * Firebase Authentication is aimed at consumer applications, and offers a subset of features compared to Identity Platform. 
  * Identity Platform is intended for building enterprise-focused SaaS applications. It lets you integrate with enterprise IdPs using inbound OIDC or SAML. 



For more information about the differences between these products, see [ Differences between Identity Platform and Firebase Authentication](https://docs.cloud.google.com/identity-platform/docs/product-comparison). 

For information about Firebase Authentication, see [Where do I start with Firebase Authentication?](https://firebase.google.com/docs/auth/where-to-start)

For a comparison between end-user authentication options, see [Authenticate application users](https://docs.cloud.google.com/docs/authentication/use-cases#app-users). 

### Google Identity Services

[Google Identity Services](https://developers.google.com/identity) is a suite of identity products that support user authentication using Google Accounts, for mobile apps and web platforms. Google Identity Services include the [Sign In With Google](https://developers.google.com/identity/one-tap/android) button, the One Tap sign-in module, and authentication libraries you can use to implement OAuth 2.0 flows in your application.

If you're creating applications that use Google Cloud APIs and resources exclusively, consider using Identity Platform, which is based on Google Identity Services, instead.

For a comparison between end-user authentication options, see [Authenticate application users](https://docs.cloud.google.com/docs/authentication/use-cases#app-users). 

### Google Workspace

[Google Workspace](https://workspace.google.com/) is a suite of business productivity and collaboration tools based on Google identities (Google Accounts). Google Workspace includes the functionality provided by Cloud Identity for user management. [Google Accounts](https://www.google.com/account/about/) provide access to Google's products and services, including Google Cloud.

### Identity and Access Management (IAM)

[IAM](https://docs.cloud.google.com/iam) provides fine-grained access control for Google Cloud resources.

For information, see the [IAM overview](https://docs.cloud.google.com/iam/docs/overview).

### Identity-Aware Proxy (IAP)

[Identity-Aware Proxy](https://docs.cloud.google.com/iap) provides a centralized way to support authentication and authorization for your applications and virtual machines (VMs). IAP can be used for applications running in Google Cloud or on-premises.

For information, see [Identity-Aware Proxy overview](https://docs.cloud.google.com/iap/docs/concepts-overview).

For a comparison between end-user authentication options, see [Authenticate application users](https://docs.cloud.google.com/docs/authentication/use-cases#app-users). 

### Identity Platform

[Identity Platform](https://docs.cloud.google.com/identity-platform) is a customer identity and access management (CIAM) platform that lets users sign in to your applications and services. Identity Platform supports a variety of ways to sign in, including email and password, Google, Facebook, and Apple. Identity Platform also supports SMS-based multi-factor authentication (MFA).

For information about authentication using Identity Platform, see [Authentication](https://docs.cloud.google.com/identity-platform/docs/concepts-authentication).

Identity Platform is not related to Cloud Identity or Identity-Aware Proxy.

Firebase Authentication uses Identity Platform as its backend but serves a different audience: 

  * Firebase Authentication is aimed at consumer applications, and offers a subset of features compared to Identity Platform. 
  * Identity Platform is intended for building enterprise-focused SaaS applications. It lets you integrate with enterprise IdPs using inbound OIDC or SAML. 



For more information about the differences between these products, see [ Differences between Identity Platform and Firebase Authentication](https://docs.cloud.google.com/identity-platform/docs/product-comparison). 

For a comparison between end-user authentication options, see [Authenticate application users](https://docs.cloud.google.com/docs/authentication/use-cases#app-users). 

### Workforce Identity Federation

[Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) is an IAM feature that lets you configure and secure granular access for your workforce—employees and partners—by federating identities from an external identity provider (IdP).

Workforce Identity Federation is not the same as Workload Identity Federation. Workforce Identity Federation and Workload Identity Federation both aggregate identities; Workforce Identity Federation aggregates human users, whereas Workload Identity Federation aggregates machine workloads.

### Workload Identity Federation for GKE

[Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) lets a Kubernetes service account in your GKE cluster act as an IAM service account. Workload Identity Federation for GKE is the recommended way for your workloads running on GKE to access Google Cloud services in a secure and manageable way.

Workload Identity Federation for GKE is not related to Workload Identity Federation.

### Workload Identity Federation

[Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) lets you grant on-premises or multicloud workloads access to Google Cloud resources. It does so by federating identities from an external IdP, without requiring a service account key.

Workload Identity Federation is not related to Workload Identity Federation for GKE.

Workload Identity Federation is not the same as Workforce Identity Federation. Workload Identity Federation and Workforce Identity Federation both aggregate identities; Workload Identity Federation aggregates machine workloads, while Workforce Identity Federation aggregates human users.

## What's next

  * Review a list of [authentication and authorization use cases](https://docs.cloud.google.com/docs/authentication/use-cases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

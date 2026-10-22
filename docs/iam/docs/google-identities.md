---
url: https://docs.cloud.google.com/iam/docs/google-identities/
title: Identity management for Google Cloud \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:53.146718+00:00
---

# Identity management for Google Cloud  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/google-identities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Identity management for Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

To use Google Cloud, users, workloads, and agents need an identity that Google Cloud can recognize.

This page outlines the methods that you can use to configure identities for users, workloads, and agents.

## User identities

There are several ways to configure user identities so that Google Cloud can recognize them:

  * **Create Cloud Identity or Google Workspace accounts** : Users with Cloud Identity or Google Workspace accounts can authenticate to Google Cloud and be authorized to use Google Cloud resources. Cloud Identity and Google Workspace accounts are user accounts that are managed by your organization.

**Note:** Google Workspace accounts may have one or more _[alternate email addresses (email alias)](https://support.google.com/a/answer/33327)_. If you grant a role to a principal's _email alias_ , the role is granted to the _primary email_ instead. It's not possible to grant a role to only the _email alias_.**Warning:** Granting a role to a principal's _email alias_ reveals the _primary email_.

  * **Set up one of the following federated identity strategies** :

    * **Federation using Cloud Identity or Google Workspace** : Sync external identities with corresponding Cloud Identity or Google Workspace accounts so that users can sign in to Google services with their external credentials. With this method, users need two accounts: an external account, and a Cloud Identity or Google Workspace account. You can keep these accounts synchronized using a tool like [Google Cloud Directory Sync (GCDS)](https://tools.google.com/dlpage/dirsync/).
    * **Workforce Identity Federation** : Use your external identity provider (IdP) to sign in your users to Google Cloud and let them access Google Cloud resources and products. With Workforce Identity Federation, users need only one account: their external account. This type of user identity is sometimes referred to as a _federated identity_.



To learn more about these methods for setting up user identities, see [User identities overview](https://docs.cloud.google.com/iam/docs/user-identities).

## Workload identities

Google Cloud provides the following types of identity services for workloads:

  * [**Workload Identity Federation**](https://docs.cloud.google.com/iam/docs/workload-identity-federation) lets your workloads access most Google Cloud services by using an identity that is provided by an IdP. Workloads that use Workload Identity Federation can run on Google Cloud, Google Kubernetes Engine (GKE), or other platforms, such as AWS, Azure, and GitHub.

  * [**Google Cloud service accounts**](https://docs.cloud.google.com/iam/docs/service-account-overview) can act as identities for workloads. Instead of granting access to a workload directly, you grant access to a service account, then let the workload use the service account as its identity.

  * [**Managed workload identities**](https://docs.cloud.google.com/iam/docs/managed-workload-identity) let you bind strongly attested identities to your Compute Engine workloads. You can use managed workload identities to authenticate your workloads to other workloads using [mutual TLS (mTLS)](https://en.wikipedia.org/wiki/Mutual_authentication), but they cannot be used for authenticating to Google Cloud APIs.




The methods that you can use depend on where your workloads are running.

If you're running workloads on Google Cloud, you can use the following methods to configure workload identities:

  * **Workload Identity Federation for GKE** : Grant Identity and Access Management (IAM) access to GKE clusters and Kubernetes service accounts. Doing so lets the clusters' workloads access most Google Cloud services directly, without using IAM service account impersonation.

  * **Attached service accounts** : Attach a service account to a resource so that the service account acts as the resource's default identity. Any workloads running on the resource use the service account's identity when accessing Google Cloud services.

  * **Short-lived service account credentials** : Generate and use short-lived service account credentials whenever your resources need to access Google Cloud services. The most common types of credentials are OAuth 2.0 access tokens and OpenID Connect (OIDC) ID tokens.




If you're running workloads outside of Google Cloud, you can use the following methods to configure workload identities:

  * **Workload Identity Federation** : Use credentials from external identity providers to generate short-lived credentials, which workloads can use to temporarily impersonate service accounts. Workloads can then access Google Cloud resources, using the service account as their identity.
  * **Service account keys** : Use the private portion of a service account's public/private RSA key pair to authenticate as the service account.

**Important:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 




To learn more about these methods for setting up workload identities, see [Workload identities overview](https://docs.cloud.google.com/iam/docs/workload-identities).

## Agent identities

Google Cloud provides [**agent identities**](https://docs.cloud.google.com/iam/docs/agent-identity-overview) for generative AI agents. An agent identity is a SPIFFE-based identity that is tied to an agent's lifecycle and mapped directly to the resource URI where the agent is hosted. The agent uses this identity to authenticate to Google Cloud services or retrieve external credentials from the Agent Identity auth manager.

To learn more about setting up agent identities, see [Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

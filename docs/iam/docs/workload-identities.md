---
url: https://docs.cloud.google.com/iam/docs/workload-identities/
title: Identities for workloads \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:33.293664+00:00
---

# Identities for workloads  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/workload-identities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Identities for workloads Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the identity types that you can use to configure your workloads' access to Google Cloud resources.

Google Cloud provides the following types of identities for workloads:

  * [**Workload Identity Federation**](https://docs.cloud.google.com/iam/docs/workload-identity-federation) and [**Workload Identity Federation for GKE**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) let your workloads access most Google Cloud services by using federated identities that are authenticated through an external identity provider (IdP). After Google Cloud authenticates the identity as a principal, the principal can access resources by using IAM roles that you grant.

  * [**Google Cloud service accounts**](https://docs.cloud.google.com/iam/docs/service-account-overview) can act as identities for workloads in production environments. Instead of granting access to a workload directly, you grant access to a service account, then have the workload use the service account as its identity.

  * [**Managed workload identities**](https://docs.cloud.google.com/iam/docs/managed-workload-identity) let you bind strongly attested identities to your Compute Engine and GKE workloads.

  * **Agent identities** are Google-managed identities for agentic workloads. Agent identities are attested and tied to the lifecycle of the agents. This provides a more secure way to manage agent access to Google Cloud resources than using service accounts.




The types of identities that you can use for workloads and the way that you configure them depends on where your workloads are running.

## Configure workloads on Google Cloud

If you're running workloads on Google Cloud, you can use the following methods to configure identities for your workloads:

  * Attached service accounts
  * Workload Identity Federation for GKE (for workloads running on Google Kubernetes Engine only)
  * Managed workload identities (for workloads that run on Compute Engine and GKE only)
  * Service account keys



### Attached service accounts

For some Google Cloud resources, you can specify a user-managed service account that the resource uses as its default identity. This process is known as _attaching_ the service account to the resource, or _associating_ the service account with the resource. When code running on the resource accesses Google Cloud services and resources, it uses the service account attached to the resource as its identity. For example, if you [attach a service account to a Compute Engine instance](https://docs.cloud.google.com/compute/docs/access/service-accounts#associating_a_service_account_to_an_instance), and the applications on the instance use a [client library](https://docs.cloud.google.com/apis/docs/client-libraries-explained) to call Google Cloud APIs, those applications automatically use the attached service account for authentication and authorization. 

In most cases, you must attach a service account to a resource when you create that resource. After the resource is created, you cannot change which service account is attached to the resource. Compute Engine instances are an exception to this rule; you can change which service account is attached to an instance as needed.

To learn more, see [Attach a service account to a resource](https://docs.cloud.google.com/iam/docs/attach-service-accounts).

### Workload Identity Federation for GKE

For workloads that run on GKE, Workload Identity Federation for GKE lets you grant IAM roles to distinct, fine-grained sets of principals, for each application in your cluster. Workload Identity Federation for GKE lets Kubernetes service accounts in your GKE cluster access Google Cloud resources directly, by using Workload Identity Federation, or indirectly, by using IAM service account impersonation.

By using direct resource access, you can grant IAM roles to the Kubernetes service account identity directly on the Google Cloud service's resources. Most Google Cloud APIs support direct resource access. However, when using identity federation, certain API methods might have limitations. For a list of these limitations, see [Supported products and limitations](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services).

As an alternative, workloads can also use service account impersonation, where the configured Kubernetes ServiceAccount is bound to an IAM service account, which serves as the identity when accessing Google Cloud APIs.

To learn more about GKE Workload Identity Federation for GKE, see [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity).

### Managed workload identities

Managed workload identities let you bind strongly attested identities to your Compute Engine and GKE workloads. You can use managed workload identities to authenticate your workloads to other workloads using [mTLS](https://en.wikipedia.org/wiki/Mutual_authentication).

To learn more about managed workload identities, see [Managed workload identities overview](https://docs.cloud.google.com/iam/docs/managed-workload-identity).

### Agent identities

An agent identity is a Google-managed identity for agentic workloads. An agent identity is attested and tied to the lifecycle of the agent, which provides a more secure way to manage agent access to Google Cloud resources than using service accounts.

Existing access management controls through IAM support agent identity to enable strong governance.

To learn more about agent identities and how to use them, see [Use agent identity with Vertex AI Agent Engine](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity).

## Configure external workloads

If you're running workloads outside of Google Cloud, you can use the following methods to configure identities for your workloads:

  * Workload Identity Federation
  * Service account keys



### Workload Identity Federation

You can use Workload Identity Federation with workloads on Google Cloud or external workloads that run on platforms such as AWS, Azure, GitHub, and GitLab.

Workload Identity Federation lets you use credentials from external identity providers like [AWS, Azure](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds), and [Active Directory](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-active-directory) to generate short-lived credentials, which workloads can use to temporarily impersonate service accounts. Workloads can then access Google Cloud resources, using the service account as their identity.

Workload Identity Federation is the preferred way to configure identities for external workloads.

To learn more about Workload Identity Federation, see [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).

### Service account keys

A service account key lets a workload authenticate as a service account, then use the service account's identity for authorization.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

## Local development

If you're developing in a local environment, you can configure workloads to use either your user credentials or a service account for authentication and authorization. For more information, see [Local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the authentication documentation.

## What's next

  * Learn how to [set up authentication by using service accounts](https://docs.cloud.google.com/docs/authentication#service-accounts).
  * Learn how to [set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
  * Learn how to [grant service accounts access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

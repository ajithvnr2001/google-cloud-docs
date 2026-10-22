---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/permissions/
title: Design permissioning setup \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:02.958918+00:00
---

# Design permissioning setup  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Design permissioning setup Stay organized with collections  Save and categorize content based on your preferences. 

This document outlines best practices for permissioning design in a Google Distributed Cloud (GDC) air-gapped universe. The following topics are covered:

  * Identity providers (IdP) per organization
  * Multi-factor authentication for IdPs
  * Managed and marketplace services
  * Cluster kubeconfig management
  * Kubernetes service accounts
  * Principle of least privilege
  * Regular audits for excess privilege



Although the following designs are recommended, it's not required to follow them exactly as prescribed. Each GDC universe has unique requirements and considerations that must be satisfied on a case-by-case basis.

## Configure an identity provider per organization

An operator must configure one or more identity providers per organization. An administrator then [connects to an identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/connect-identity) to manage authentication services for applications in the GDC universe.

You might have a scenario where your company has multiple departments with separate organizations, and each organization connects to the same identity provider for authentication. In that case, it is your responsibility to understand and audit the combination of privileges a user has across organizations. Ensure that a user with privileges in multiple organizations does not violate the requirements for separating workloads into distinct organizations.

Alternatively, you might have a scenario where different sets of users use different identity providers to authenticate within a single organization, such as when multiple vendor teams work together in a single organization. Consider whether consolidating user identities into a single identity provider or maintaining separate identity providers works best with your company's approach to identity management.

## Configure multi-factor authentication for your identity provider

GDC relies on your IAM platform for authentication, including additional security settings such as multi-factor authentication. It is good practice to configure multi-factor authentication with a physical key for any user that might potentially access sensitive resources.

## Restrict managed services and marketplace services

You might prefer to block some projects from certain services, to either limit the potential attack surface in a project or avoid use of unapproved services. By default, managed services like Artificial Intelligence and Machine Learning are available to use in any project. In comparison to managed services, marketplace services must first be enabled for the organization.

To deny service access from projects, apply [Gatekeeper constraints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/org-policy) against the custom resource definition of a service and a list of namespaces. The approach to deny access with Gatekeeper applies to managed and marketplace services.

## Manage kubeconfig files for multiple clusters

Different operational tasks require a connection to different clusters. For example, you perform tasks like binding an IAM role to a project, and tasks like deploying a Kubernetes `Pod` resource on a Kubernetes cluster.

When using the GDC console, you don't need to be aware of which underlying cluster performs a task, as the GDC console abstracts away the low-level operations like connecting to a cluster.

However, when working with the gdcloud CLI or kubectl CLI, you might have multiple kubeconfig files for accomplishing your tasks. Ensure that you [sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) using kubeconfig credentials for the appropriate cluster for your task.

## Best practices for Kubernetes service accounts

For Kubernetes service accounts, authorization is based on a secret token. To mitigate the risk of service account tokens, consider the following best practices:

  * Avoid downloading persistent service account credentials for use outside of GDC.
  * Be aware of [Kubernetes escalation paths](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#privilege-escalation-via-pod-creation) for users or service accounts who have the ability to create and edit pods.
  * Set the `expirationSeconds` field to a short time period for the service account token projection of your workloads.
  * Regularly rotate service account credentials.



## Consider principle of least privilege

Consider the principle of least privilege (PoLP) when granting [role bindings](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings) to users. In accordance with PoLP, consider assigning only privileges required to complete a task.

For example, you grant the IAM Project Admin role within a single project to a user, so that this user delegates authority to grant roles within that project. This user then grants granular roles to other developers in the project based on the specific services they use. The IAM Project Admin role must be restricted to a trusted lead because this role could be used to escalate privilege, granting oneself or others additional roles in the project.

## Audit regularly for excessive privileges

Be sure to review roles granted within your organization and audit against excessive privilege. You must ensure that the roles granted are necessary for an individual user to complete their job, and that combinations of roles across projects don't lead to an escalation or exfiltration risk.

If your company uses multiple organizations, we don't recommend that an individual user has highly privileged roles across multiple organizations, as this might violate the reason for separating organizations in the first place.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 

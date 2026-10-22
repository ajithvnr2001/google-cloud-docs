---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/authorization-access-control/
title: Authorization and access control \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:46.290000+00:00
---

# Authorization and access control  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/authorization-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Authorization and access control Stay organized with collections  Save and categorize content based on your preferences. 

Identity and Access Management (IAM) in Google Distributed Cloud (GDC) air-gapped lets you control who has access to which resources and what actions they can perform on those resources.

Understanding how IAM works in GDC helps you manage access effectively, ensuring members have the permissions they need to perform their roles while maintaining the security of your air-gapped environment.

This document is for audiences within the platform administrator and application operator groups (such as IT administrators, security engineers, or application developers) who want to understand authorization and access control in GDC air-gapped. This document also helps infrastructure operators build a foundational understanding of access control concepts. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## The access control model

GDC structures access around three core components: _members_ (who), _roles_ (what), and _resource scope_ (where).

![The access control model](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/authorization-access-control-model.png)

Access control consists of two distinct stages—proving who you are (authentication) and determining what you can do (authorization):

  * **Authentication:** GDC doesn't store user accounts or passwords. GDC connects to your organization's identity provider (IdP) so you can sign in with your corporate credentials.
  * **Authorization:** after you authenticate, GDC IAM checks your assigned roles to determine which resources you can access and what actions you can perform.



### Members

A member is an identity that you can grant resource access to. GDC groups members into two main categories based on where you manage them: human identities and non-human identities.

#### Human identities

Human identities are the users and groups who sign in to GDC. Rather than storing user accounts or passwords, GDC connects to your organization's existing login systems, or IdPs (such as Active Directory, LDAP, or Okta), using standard identity federation protocols like OpenID Connect (OIDC) or SAML 2.0.

There are two types of human identities:

  * **Users:** individual human users who sign in to the system using their corporate credentials.
  * **Groups:** collections of human users managed within your organization's IdP. Granting a role to a group automatically grants it to all members of that group.



GDC uses IdPs to uniquely identify human identities. Because your environment can connect to multiple IdPs (for example, if different departments use different login systems), GDC distinguishes between the IdPs to ensure you grant access to the correct person.

When managing access, GDC automatically prepends a unique IdP prefix to all external usernames and groups:

  * **Format:** `idpprefix-username@domain.com` (or `idpprefix-group-name` for groups).
  * **Example:** If your organization's IdP is configured with the prefix `agency-a`, and you sign in as `alice@example.com`, GDC IAM recognizes you as `agency-a-alice@example.com`.



#### Non-human identities

Non-human identities are called service identities (or service accounts). You create and manage them directly within GDC (as `ProjectServiceAccount` resources) to let applications, scripts, or automated workloads interact with APIs securely.

Because service accounts are managed internally by GDC, they don't use IdP prefixes. Instead, they are identified by their project and name (for example, `serviceAccount:projectName:serviceAccountName` when using the gdcloud CLI).

For more information, see [Secure service account keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/secure-service-account-keys).

### Permissions and roles

A permission is the authority to perform a specific action on a resource (for example, creating a VM or deleting a database). You don't grant permissions to members directly. Instead, GDC bundles permissions into roles.

GDC offers two types of roles:

  * **Predefined roles:** built-in bundles of permissions created and managed by GDC. GDC provides a comprehensive library of predefined roles tailored to specific job functions and services (ranging from broad roles like Project Viewer to granular service roles like Bucket Project Admin or KMS Viewer).
  * **Custom roles:** user-defined bundles of permissions that you can create when existing predefined roles don't meet your organization's needs.



Permissions granted through IAM roles are purely additive; they grant access, but don't include deny rules. When you grant multiple roles to a member, the member receives the union of all permissions in those roles. To restrict or deny access to specific services across your organization, you can [set up organization policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/org-policy).

**Note:** When granting roles, always apply the principle of least privilege. This means assigning the most restrictive role that allows the member to perform their required tasks. Start with minimum permissions (like viewer roles) and only grant more permissive roles (like admin) when necessary.

### Resource scope

You always grant access at a specific level of the GDC resource hierarchy. The scope determines which resources the member can access. In multi-zone environments, roles assigned at either scope automatically apply across all zones by default.

You can grant roles at the following resource scopes:

  * **Organization:** the top-level container for your environment. Roles granted at the organization level apply across the entire organization, automatically inheriting down to all projects and resources within it.
  * **Project:** a container within the organization used to group resources for specific teams or applications. Projects serve as strict security boundaries—roles granted at the project level apply only to that specific project and its resources (such as virtual machines, databases, and Kubernetes clusters).



For more information, see [Resource hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy) and [Permissions control for a multi-zone universe](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/permissions).

## How access is authorized

GDC manages and authorizes access primarily using a role-based access control (RBAC) model. In an RBAC model, you don't assign permissions directly to individual users or workloads. Instead, you assign roles to members at a specific resource scope to determine access.

GDC implements RBAC using the following Kubernetes custom resources:

  * `IAMRole`: defines a specific bundle of permissions.
  * `IAMRoleBinding`: links a member (a human user, group, or service account) to an `IAMRole` at either an organization or project scope.



To grant access to organization or project resources, you can create an `IAMRoleBinding` using the GDC console, the gdcloud CLI, or by applying custom resource manifests (YAML files) using the kubectl CLI.

For example, to allow a team member to view virtual machines within a project, you can create an `IAMRoleBinding` at that project's scope linking the member's identity to a viewer role. When the member attempts to view a virtual machine, GDC checks their active role bindings, confirms that the assigned role contains the required permission, and authorizes the request.

While the GDC console and gdcloud CLI connect to your resources automatically, direct API access using the kubectl CLI requires authenticating to the specific Kubernetes cluster or API server hosting that resource by generating a kubeconfig file. For details, see [Sign in and generate a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#generate-kubeconfig-file).

For more information about managing role bindings, see [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings).

## How GDC air-gapped IAM differs from Google Cloud

If you have experience managing access in Google Cloud, GDC uses similar concepts but implements them differently to operate within an air-gapped, Kubernetes-based infrastructure.

The following table provides a comparison between IAM in GDC and Google Cloud:

Feature | Description | GDC air-gapped | Google Cloud  
---|---|---|---  
**User identity (authentication)** | Identity system used to authenticate human users. |  Federated with your external IdP using required IdP prefixes (for example, `idpprefix-user@domain.com`).  |  Google Accounts (such as Gmail) or corporate identities federated through Cloud Identity or Google Workspace.   
**Authorization engine** |  The underlying system that evaluates and enforces permissions.  |  Primarily Kubernetes role-based access control (RBAC), where access requests are evaluated locally by the API server against role bindings. You can use organization policies to set resource restrictions.  |  Google's global Cloud IAM service. Evaluates API requests centrally against access policies attached at any level of the resource hierarchy.   
**Role bindings** | How members are mapped to roles on specific resources. |  Individual `IAMRoleBinding` custom resources. Each binding is an object linking members to one role. IAM role permissions are purely additive (deny rules can be configured separately through organization policies).  |  A single IAM access policy attached to each resource, folder, or organization. Contains multiple bindings mapping members to roles, and supports conditional rules or deny rules.   
**Service accounts** |  Non-human identities used by applications and automated workloads.  |  Local service accounts created inside a specific project (`ProjectServiceAccount`). Public keys are stored in the cluster, while private keys are managed and secured locally by the client.  |  Global identities managed centrally by Google. Credentials can be managed automatically by Google or downloaded as key files to authenticate from anywhere.   
**Resource hierarchy** |  Container structure used to organize resources and inherit permissions.  | Two-tier hierarchy: organization > projects | Multi-tier hierarchy: organization > folders > projects  
**Multi-zone permission scope** |  How permissions are evaluated and propagated across availability zones or regions.  |  Uses Kubernetes RBAC managed by a global API server, which coordinates and replicates role bindings across zonal API servers so access applies across all zones by default.  |  Employs a fully managed, global IAM service. Permissions assigned at any resource level are inherently global and apply across all regions and zones automatically.   
**Client tooling** | Primary interfaces, CLI tools, and APIs used to manage access. |  GDC console, gdcloud CLI, and KRM APIs.  |  Google Cloud console, gcloud CLI, and REST or gRPC APIs.   
**Direct API access** |  How tools and scripts authenticate to manage resources directly using APIs.  |  Direct API access using the kubectl CLI requires authenticating to the specific Kubernetes cluster or API server hosting that resource by generating a kubeconfig file. (GDC console and gdcloud CLI connect to resources automatically.)  |  Direct API access using `gcloud` or REST/gRPC endpoints uses centralized credentials (`gcloud auth login`) that apply globally across all services without needing cluster-specific logins.   
  
## What's next

  * To connect your organization's login systems, see [Connect to an identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/connect-identity).
  * To sign in to your environment, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in).
  * To grant permissions and manage role bindings, see [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

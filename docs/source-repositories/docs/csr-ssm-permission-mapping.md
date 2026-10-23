---
url: https://docs.cloud.google.com/source-repositories/docs/csr-ssm-permission-mapping/
title: Translate Cloud Source Repositories roles and permissions to Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:19.627077+00:00
---

# Translate Cloud Source Repositories roles and permissions to Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/csr-ssm-permission-mapping/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Translate Cloud Source Repositories roles and permissions to Secure Source Manager Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows Cloud Source Repositories (CSR) users how its access controls translate to Secure Source Manager (SSM). To follow this guide, you should know IAM and CSR, and have a basic understanding of SSM.

## Resource Models

CSR has one Google Cloud resource that is a child of a project:

  * A repository, `projects/<var>project</var>/repositories/<var>repo</var>`



SSM has two resources that are regionalized children of a project:

  * An instance, `projects/<var>project</var>/locations/<var>location</var>/instances/<var>instance</var>`
  * A repository, which is the most direct equivalent to a CSR repository and must be attached to (but is not a child of) an SSM instance in the same project and location, `projects/<var>project</var>/locations/<var>location</var>/repositories/<var>repo</var>`



SSM has other resources, but they are modeled as children of the repository. This guide considers them part of the repository.

## Roles

CSR has three roles: `roles/source.reader`, `roles/source.writer`, and `roles/source.admin`. You can bind the reader and writer roles to a repository or project. You should only bind the Administrator role to a project because the `source.repos.create` permission applies only at project scope.

SSM has 11 roles for user principals, a significant increase compared to Cloud Source Repositories. You can group these roles into two categories (plus a superuser role).

The superuser role (`roles/securesourcemanager.admin`) grants all SSM permissions. You must bind this role to a project because instance permissions don't apply if you bind them to a repository, and repository permissions don't apply if you bind them to an instance.

### SSM Instance Roles

Instance roles grant permissions to access a Secure Source Manager instance's UI and connect to it using Git. You must grant users at least one instance role to allow them to access repositories on the instance. You can bind these roles to an instance resource or a project.

Role | Permissions  
---|---  
`roles/securesourcemanager.instanceAccessor` | Access an instance and its repositories. Required for repository-level roles to be effective.  
`roles/securesourcemanager.instanceManager` | Manage instance-level configurations.  
`roles/securesourcemanager.instanceOwner` | Full control over instance configurations.  
`roles/securesourcemanager.instanceRepoCreator` | Create repositories on an instance.  
`roles/securesourcemanager.sshKeyUser` | Manage SSH keys for authentication to an instance. Doesn't grant instance access on its own.  
  
### SSM Repository Roles

Repository roles grant permissions on repositories within a Secure Source Manager instance. You can bind these roles to a repository resource or a project, except for `repoCreator`, which you must bind to a project.

Role | Permissions  
---|---  
`roles/securesourcemanager.repoAdmin` | Full control over a repository, including repository settings and user access.  
`roles/securesourcemanager.repoPullRequestApprover` | Approve pull requests in a repository.  
`roles/securesourcemanager.repoReader` | Read repository content and view pull requests and issues.  
`roles/securesourcemanager.repoWriter` | Read and write repository content, and manage pull requests and issues.  
`roles/securesourcemanager.repoCreator` | Create new repositories within a project.  
  
## Mapping CSR roles to SSM

To use SSM effectively, you need at least two roles: one instance role, and one repository role. There is no 1:1 mapping from a CSR role to an SSM role. These recipes provide equivalent access only for source control, not for SSM features such as pull requests, issues, or instance management.

In CSR, you could create repositories across multiple projects. In Secure Source Manager, all repositories on an instance belong to the same project as the instance. If you bind any role at the project level in Secure Source Manager, you grant that role's permissions to **every repository** on that instance. If you need to grant permissions to specific repositories only, use repository-level bindings.

### Mapping source.reader

If you bound this role at the repository level, bind `securesourcemanager.repoReader` on the repository resource and `securesourcemanager.instanceAccessor` on the host instance to recreate the same level of access. If you bound the role at the project level, binding `repoReader` and `instanceAccessor` at the project level grants read access to all repositories on the instance.

### Mapping source.writer

If you bound this role at the repository level, bind `securesourcemanager.repoWriter` on the repository resource and `securesourcemanager.instanceAccessor` on the host instance to recreate the same level of access. If you bound the role at the project level, binding `repoWriter` and `instanceAccessor` at the project level grants write access to all repositories on the instance.

### Mapping source.admin

You only bind this role at the project level. You can recreate it by binding a combination of `securesourcemanager.instanceAccessor`, `securesourcemanager.repoAdmin`, `securesourcemanager.instanceRepoCreator`, and `securesourcemanager.repoCreator` at the project level. This combination of roles grants permission to create repositories on any instance in the project, and grants administrators permissions to all repositories on any instance in the project. To grant all SSM permissions in the same way that `source.admin` granted all CSR permissions, bind the superuser role, `securesourcemanager.admin`, at the project level.

## Differences between SSM and CSR

This section outlines key changes in how Secure Source Manager handles roles and permissions compared to Cloud Source Repositories.

### Implicit role grant

When you create a new repository resource, the calling principal is automatically granted the `repoAdmin` role on the newly created repository resource.

### New resource types

SSM has more features than CSR, and these features are modeled as new resource types. These features include branch protection rules, hooks, issues, and pull requests, in addition to comments on issues and pull requests. These resources are children of the repository resource. Repository roles include permissions for these resources. For example, `repoAdmin` and `repoWriter` provide write access, while `repoReader` grants only read access.

### Fine-grained roles

SSM includes fine-grained roles that provide specific access controls.

  * `roles/securesourcemanager.repoPullRequestApprover` grants only the permission to approve pull requests. Use this role with `repoReader` and `instanceAccessor` to let a user access an instance, browse the repository, and approve pull requests without modifying other data.
  * `roles/securesourcemanager.repoCreator` grants only the permission to create repositories in a project. Because repositories must be attached to an instance, you must also have `roles/securesourcemanager.instanceRepoCreator` to attach a repository to an instance. Use `roles/securesourcemanager.repoCreator` with `instanceRepoCreator` to grant permissions to create repositories and attach them to an instance.



## What's next

  * [Secure Source Manager overview](https://docs.cloud.google.com/secure-source-manager/docs/overview)
  * [Access control with Identity and Access Management](https://docs.cloud.google.com/secure-source-manager/docs/access-control)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/architecture/identity/overview-google-authentication/
title: Overview of Google identity management \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:28.812289+00:00
---

# Overview of Google identity management  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/overview-google-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Overview of Google identity management Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-06-26 UTC

All Google services, including Google Cloud, Google Marketing Platform, and Google Ads, rely on [Google Sign-In](https://account.google.com/) to authenticate users. This document explains the domain model that Google Sign-In relies on for authentication and identity management. The domain model helps you understand how Google Sign-In works in a corporate context, how identities are managed, and how you can facilitate an integration with an external identity provider (IdP). The following diagram shows how these entities interact.

![Overview of the domain model.](https://docs.cloud.google.com/static/architecture/identity/images/domain-model.svg)

As this diagram shows, at the center of the model is the _Google identity_ , which is used by Google Sign-In. The Google identity is related to a number of other entities that are all relevant in the context of managing identities:

  * **Google for consumers** contains the entities that are relevant for consumer-focused usage of Google services such as Gmail.
  * **Google for organizations** contains entities managed by [Cloud Identity](https://docs.cloud.google.com/identity) or [Google Workspace](https://workspace.google.com/). These entities are the most relevant for managing corporate identities.
  * **Google Cloud** contains the entities that are specific to Google Cloud.
  * **External** contains entities that are relevant if you integrate Google with an external IdP.



Solid arrows in the diagram indicate that entities reference each other or contain each other. In contrast, dashed arrows denote a federation relationship.

## Google identities

Identities, users, and user accounts play a crucial role in identity management. The three terms are closely related and sometimes even used interchangeably. However, in the context of identity management, it's worthwhile to differentiate between the concepts:

  * An _identity_ is a name that uniquely identifies the person who is interacting with a Google service. Google uses email addresses for this purpose. A person's email address is considered that person's Google identity.

The process of verifying the association between a person and an identity is called authentication or sign-in, making the person prove that this is indeed _their_ identity.

A person might have multiple email addresses. Because Google services use an email address as identity, such a person would be considered to have multiple identities.

  * A _user account_ is a data structure that keeps track of attributes, activities, and configurations that should be applied whenever a certain identity interacts with a Google service. User accounts are not created on the fly, but need to be provisioned before the first sign-on.

User accounts are identified by an ID that is not exposed externally. User interfaces or APIs therefore require you to reference the user account indirectly by its associated identity, such as `alice@gmail.com`. Despite this indirection, any data and configuration details are associated with the user account, not with the identity.




In most cases, there is a one-to-one relationship between user accounts and identities, which makes them easy to conflate. However, this is not always the case, as the following edge cases illustrate:

  * **The relationship between user accounts and identities is not fixed.** You can change the primary email address of a user account, which associates a different identity with the user.

As a Cloud Identity or Google Workspace administrator, you can even swap the primary email addresses of two users. For example, if you swapped the primary email addresses of Alice (`alice@example.com`) and Bob (`bob@example.com`), then Alice would be using Bob's previous user account and Bob would be using Alice's previous user account. Because data and configuration is associated with the user account and not the identity, Alice would also now use Bob's existing configuration and data (and Bob would now use Alice's configuration and data). The following figure shows this relationship.

![Relationship of identities for Bob and Alice.](https://docs.cloud.google.com/static/architecture/identity/images/bob-alice-identities.svg)

In a non-federated setup, you'd also have to reset passwords in order for Alice and Bob to swap user accounts. In a federated setup where Alice and Bob use an external IdP to authenticate, resetting passwords wouldn't be necessary.

  * **The relationship between identity and users might not be 1:1.** A consumer account [can intentionally be associated with multiple identities](https://support.google.com/accounts/answer/176347), as in the following diagram.

It's also possible that one identity refers to two different user accounts. We recommend that you avoid this situation, but it can arise in the case of a [conflicting user account](https://knowledge.workspace.google.com/p/duplicate-account-errors). In such a case, a user is shown a ballot screen during authentication in which they select the user account to use.

![Alice: user and identity are not always 1:1.](https://docs.cloud.google.com/static/architecture/identity/images/alice-user-identity.svg)




Google differentiates between two types of user accounts, _consumer user accounts_ and _managed user accounts_. The following sections cover both types of user accounts and their related entities in more detail.

## Google for consumers

If you own a Gmail email address like `alice@gmail.com`, then your Gmail account is a _consumer account_. Similarly, if you use the **Create account** link on the Google Sign-In page and during sign-up you provide a custom email address that you own, such as `alice@example.com`, then the resulting account is also a consumer account.

### Consumer account

Consumer accounts are created by self-service and are primarily intended to be used for private purposes. The person who created the consumer account has full control of the account and any data created by using the account. The email address that that person used during sign-up becomes the primary email address of the consumer account and serves as its identity. That person can [add email addresses](https://support.google.com/accounts/answer/176347/) to the consumer account. These email addresses serve as additional identities and can also be used for signing in.

When a consumer account uses a primary email address that corresponds to the primary or secondary domain of a Cloud Identity or Google Workspace account, then the consumer account is also referred to as an _unmanaged personal account_.

A consumer account can be a member of any number of groups.

## Google for organizations

If your organization uses Google services, it's best to use _managed user accounts_. These accounts are called _managed_ because their lifecycle and configuration can be fully controlled by the organization.

Managed user accounts are a feature of Cloud Identity and Google Workspace.

### Cloud Identity or Google Workspace account

A Cloud Identity or Google Workspace account is the top-level container for users, groups, configuration, and data. A Cloud Identity or Google Workspace account is created when a company signs up for Cloud Identity or Google Workspace and corresponds to the notion of a [tenant](https://en.wikipedia.org/wiki/Multitenancy).

Cloud Identity and Google Workspace share a common technical platform. Both products use the same set of APIs and administrative tools and share the notion of an account as a container for users and groups; that container is identified by a domain name. For the purpose of managing users, groups, and authentication, the two products can largely be considered equivalent.

An account contains groups and one or more organizational units.

**Important:** A Cloud Identity or Google Workspace account is not a user account, but a directory of user accounts.

### Organizational unit

An organizational unit (OU) is a sub-container for user accounts that lets you segment the user accounts defined in the Cloud Identity or Google Workspace account into disjoint sets to make them easier to manage.

Organizational units are organized hierarchically. Each Cloud Identity or Google Workspace account has a root OU, under which you can [create more OUs as needed](https://support.google.com/a/answer/4352075). You can also nest your OUs.

Cloud Identity and Google Workspace lets you apply certain configurations by OU, such as [license assignment](https://support.google.com/a/answer/6342682) or [2-step verification](https://support.google.com/a/answer/175197). These settings automatically apply to all users in the OU and are also inherited by child OUs. Organizational units therefore play a key role in managing Cloud Identity and Google Workspace configuration.

A user account cannot belong to more than one OU, which makes OUs different from groups. Although OUs are useful for applying configuration to user accounts, they are not intended to be used for managing access. For managing access, we recommend that you use groups.

Although OUs resemble Google Cloud folders, the two entities serve different purposes and are unrelated to another.

### Managed user account

Managed user accounts work similarly to consumer user accounts, but they can be fully controlled by administrators of the Cloud Identity or Google Workspace account.

The identity of a managed user account is defined by its primary email address. The primary email address has to use a domain that corresponds to one of the primary, secondary, or alias domains added to the Cloud Identity or Google Workspace account. Managed user accounts can have additional [alias email addresses](https://support.google.com/a/answer/33327) and a [recovery email address](https://support.google.com/a/answer/3033063), but these addresses aren't considered identities and cannot be used for signing in. For example, if Alice uses `alice@example.com` as her primary email address and has configured `ally@example.com` as an alias email address and `alice@gmail.com` as a recovery email address, then the only email address Alice can use for signing in is `alice@example.com`.

Managed user accounts are contained by an organizational unit and can be a member of any number of groups.

Managed user accounts are intended to be used by human users rather than machine users. A machine user account is a special kind of account used by an application or a virtual machine (VM) instance, not a person. For machine users, Google Cloud provides service accounts. (Service accounts are discussed in more detail later in this document.)

**Note:** In the context of Google Workspace, Cloud Identity, and Google Cloud, the _managed_ prefix is sometimes left out in other documentation, and managed user accounts are simply referred to as _user accounts_. In contrast, _consumer user accounts_ are always qualified with the _consumer_ prefix.

### Unmanaged user account

When someone uses their corporate email address to create a Google Account, this account is an _unmanaged account_. 

Unlike managed user accounts, these accounts aren't under the administrative control of your organization. 

#### Resolve conflicts and transfer unmanaged accounts

In the context of Cloud Identity and Google Workspace, unmanaged accounts fall into two categories:

  * **Unmanaged personal accounts** : Accounts created by individuals using their corporate email address to access consumer Google services.
  * **Unmanaged work accounts (or unmanaged teams)** : Accounts created by users for business services such as Google Workspace Essentials or Google Cloud.



When an administrator creates a managed account using the same email address as an unmanaged account, it causes an account conflict. To resolve account conflicts and take over unmanaged accounts, an administrator must do the following:

  * [Verify domain ownership](https://knowledge.workspace.google.com/admin/domains/verify-your-domain-for-google-workspace). After your domain is verified, users can no longer use their corporate email address to create unmanaged accounts.
  * [Resolve duplicate account errors](https://knowledge.workspace.google.com/p/duplicate-account-errors)
  * [Transfer unmanaged personal accounts](https://knowledge.workspace.google.com/admin/users/find-and-add-unmanaged-users)
  * [Transfer unmanaged work accounts](https://knowledge.workspace.google.com/p/unmanaged-work-accounts)



### Group

Groups let you bundle multiple users. You can use groups to manage a mailing list or to apply common access control or configuration to multiple users.

Cloud Identity and Google Workspace identify groups by email address—for example, `billing-admins@example.com`. Similar to a user's primary email address, the group email address must use one of the primary, secondary, or alias domains of the Cloud Identity or Google Workspace account. The email address doesn't need to correspond to a mailbox unless the group is used as a mailing list. Authentication still happens using the user's email rather than the group email, so a user can't sign in using a group email address.

A group can have the following entities as members:

  * Users (managed users or consumer accounts)
  * Other groups
  * Service accounts



Unlike an organizational unit, groups don't act as a container:

  * A user or group can be a member of any number of groups, not just one.
  * Deleting a group does not delete any of the member users or groups.



Groups can contain members from any Cloud Identity or Google Workspace account as well as consumer accounts. You can use the [disallow members outside your organization](https://support.google.com/a/answer/9175391) setting to restrict members to user accounts of the same Cloud Identity or Google Workspace account.

## External identities

By federating a Cloud Identity or Google Workspace account with an external IdP, you can enable employees to use their existing identity and credentials to sign in to Google services.

At the most basic level, federation entails [setting up single sign-on by using SAML](https://docs.cloud.google.com/architecture/identity/single-sign-on), which links identities in Cloud Identity or Google Workspace to identities managed by your external IdP. To link an identity like `alice@example.com` and enable it for single sign-on to Google, you must meet two prerequisites:

  * Your external IdP must recognize the identity `alice@example.com` and allow it to be used for single sign-on.
  * Your Cloud Identity or Google Workspace account must contain a user account that uses `alice@example.com` as its identity. This user account must exist before the first single sign-on attempt.



Instead of manually creating and maintaining user accounts in Cloud Identity or Google Workspace, you can automate the process by combining SAML-based single sign-on with automatic user provisioning. The idea of automatic user provisioning is to synchronize all or a subset of the users and groups from an external authoritative source to Cloud Identity or Google Workspace.

Depending on your choice of IdP, SAML-based single sign-on and automatic user provisioning might be handled by the same software component or might require separate components. The domain model therefore distinguishes between a _SAML identity provider_ and an _external authoritative source_.

### External SAML identity provider

The external IdP is the sole system for authentication and provides a single sign-on experience for your employees that spans applications. It is external to Google and therefore referred to as an _external identity provider_.

When you [configure single sign-on](https://docs.cloud.google.com/architecture/identity/single-sign-on), Cloud Identity or Google Workspace relays authentication decisions to a SAML IdP. In SAML terms, [Cloud Identity or Google Workspace acts as a _service provider_](https://support.google.com/a/answer/60224) that trusts the SAML IdP to verify a user's identity on its behalf.

Commonly used external IdPs include Active Directory Federation Services (AD FS), Entra ID, Okta, or Ping Identity.

### External authoritative source

The authoritative source for identities is the sole system that you use to create, manage, and delete identities for your employees. It's external to Google and therefore referred to as an _external authoritative source_.

From the external authoritative source, user accounts and groups can be automatically provisioned to Cloud Identity or Google Workspace. Provisioning might be handled by the authoritative source itself, or by means of provisioning middleware.

For automatic user provisioning to be effective, users have to be provisioned with an identity that your SAML IdP recognizes. If you map between identities (for example, if you map the identity `alice@example.com` in Cloud Identity or Google Workspace to `u12345@corp.example.com` in your SAML IdP), then both the SAML IdP and the provisioning middleware must perform the same mapping.

### External user account

External identity providers are assumed to have the concept of a user account that keeps track of the name, attributes, and configuration.

The authoritative source (or provisioning middleware) is expected to provision all (or a subset of) external user accounts to Cloud Identity or Google Workspace in order to facilitate a sign-on experience. In many cases, it's sufficient to propagate only a subset of the user's attributes (such as email address, first name, and last name) to Cloud Identity or Google Workspace so that you can limit data redundancy.

### External group

If your external IdP supports the notion of a group, then you can optionally map these groups to groups in Cloud Identity or Google Workspace.

Mapping and auto-provisioning groups is optional and not required for single sign-on, but both steps can be useful if you want to reuse existing groups to control access in Google Workspace or Google Cloud.

## Google Cloud

Like other Google services, Google Cloud relies on Google Sign-In to authenticate users. Google Cloud also closely integrates with Google Workspace and Cloud Identity to allow you to manage resources efficiently.

Google Cloud introduces the notion of organization nodes, folders, and projects. These entities are primarily used for managing access and configuration, so they are only tangentially relevant in the context of identity management. However, Google Cloud also includes an additional type of user account: service accounts. Service accounts belong to projects and play a crucial role in identity management.

### Organization node

An [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) is the root node in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) and a container for projects and folders. Organizations let you structure resources hierarchically and are key to managing resources centrally and efficiently.

Each organization belongs to a single Cloud Identity or Google Workspace account. The name of the organization is derived from the primary domain name of the corresponding Cloud Identity or Google Workspace account.

**Note:** Google Cloud organizations are unrelated to [organizations in Google Marketing Platform](https://support.google.com/marketingplatform/answer/9024856).

### Folder

Folders are nodes in the Google Cloud resource hierarchy and can contain projects, other folders, or a combination of both. You use folders to group resources that share common [Identity and Access Management (IAM) policies](https://docs.cloud.google.com/iam/docs/overview#iam_policy) or [organizational policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview). These policies automatically apply to all projects in the folder and are also inherited by child folders.

Folders are similar, but unrelated, to organizational units. Organizational units help you manage users and apply common configuration or policies to users, whereas folders help you manage Google Cloud projects and apply common configuration or policies to projects.

### Project

A project is a [container for resources](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects). Projects play a crucial role for managing APIs, billing, and managing access to resources.

In the context of identity management, projects are relevant because they are the containers for service accounts.

### Service account

A _service account_ (or Google Cloud service account) is a special kind of user account that is intended to be used by applications and other types of machine users.

Each service account [belongs to a Google Cloud project](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts). As is the case with managed user accounts, administrators can fully control the lifecycle and configuration of a service account.

Service accounts also use an email address as their identity, but unlike with managed user accounts, the email address always uses a Google-owned domain such as `developer.gserviceaccount.com`.

Service accounts don't participate in federation and also don't have a password. On Google Cloud, you [use IAM to control](https://docs.cloud.google.com/iam/docs/understanding-service-accounts) the permission that a service account has for a compute resource such as a virtual machine (VM) or Cloud Run function, removing the need to manage credentials. Outside of Google Cloud, you can use [service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) to let an application authenticate by using a service account.

### Kubernetes service account

Kubernetes service accounts are a [concept of Kubernetes](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/#user-accounts-vs-service-accounts) and are relevant when you use [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine). Similar to Google Cloud service accounts, Kubernetes service accounts are meant to be used by applications, not humans.

Kubernetes service accounts can be used to authenticate when an application calls the Kubernetes API of a Kubernetes cluster, but they cannot be used outside of the cluster. They are not recognized by any Google APIs and are therefore not a replacement for a Google Cloud service account.

When you deploy an application as a Kubernetes [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/), you can [associate the Pod with a service account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#use-the-default-service-account-to-access-the-api-server). This association lets the application use the Kubernetes API without having to configure or maintain certificates or other credentials.

By using [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity), you can link a Kubernetes service account to a Google Cloud service account. This link lets an application also authenticate to Google APIs, again without having to maintain certificates or other credentials.

## What's next

  * Review our [reference architectures for identity management](https://docs.cloud.google.com/architecture/identity/reference-architectures).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-06-26 UTC."],[],[]] 

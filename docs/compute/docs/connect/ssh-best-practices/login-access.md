---
url: https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/login-access/
title: Best practices for controlling SSH login access \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:17.953797+00:00
---

# Best practices for controlling SSH login access  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/login-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Best practices for controlling SSH login access Stay organized with collections  Save and categorize content based on your preferences. 

This document describes best practices for controlling SSH login access to Linux virtual machine (VM) instances.

To effectively manage SSH access to VM instances, you must allow users access when they need it, and revoke that access when they don't need it anymore. If your process for revoking access isn't reliable or doesn't cover all resources, then bad actors might be able to hold on to access even after their access should have been revoked.

The following sections contain best practices that help you ensure effective access revocation and protect against persistence threats:

  * Use OS Login to ensure continuous access evaluation against IAM policies
  * Use organizational policies to enforce consistent use of OS Login
  * Grant privileged roles on a per-VM basis
  * Suspend user accounts when users leave the organization
  * Avoid granting SSH access to VMs that have a privileged service account
  * Pre-create POSIX profiles to ensure consistent usernames and UIDs
  * Limit the use of root privileges



The document focuses on practices that are either specific to Google Cloud or of particular relevance when using SSH on Google Cloud. The document doesn't cover best practices for specific SSH client or server implementations.

## Use OS Login to ensure continuous access evaluation against IAM policies

The Compute Engine [public Linux images](https://docs.cloud.google.com/compute/docs/images) are configured to allow SSH public key authentication. To authorize a user's public key and grant them permission to a establish an SSH session, you can use one of the following two mechanisms:

  * **Metadata-based key authorization** : As an administrator, you upload a [user's public key to VM or project metadata](https://docs.cloud.google.com/compute/docs/instances/ssh#metadata) or you let users perform the upload themselves by granting them permission to modify metadata.

A public key uploaded to the metadata of a single VM grants the user root privileges to the VM only; a key uploaded to project metadata grants a user access to all VMs in the project.

  * **[OS Login](https://docs.cloud.google.com/compute/docs/oslogin) key authorization:** As a user, you upload one or more public keys to your OS Login profile, which is part of your Google user account.

As an administrator, you can decide whether to grant a user root privileges or regular user privileges on the VM by granting either the _OS Login Admin User_ IAM role or _OS Login User_ IAM role.

The gcloud CLI, the Google Cloud console in-browser SSH client, and [IAP Desktop](https://github.com/GoogleCloudPlatform/iap-desktop) automatically detect which mechanism you're using and can upload a user's key accordingly.


**Important:** By default, OS Login is disabled and VMs only allow metadata-based key authorization.

A key difference between the two mechanisms is when access is evaluated against IAM policies:

  * With metadata keys, access is evaluated only once, at the time of key upload.

The user's key is tied to the lifecycle of the VM or project and remains valid until you remove the key or delete the VM or project. Suspending or deleting the user account has no effect on the validity of their keys.

  * With OS Login, access is evaluated every time a user attempts to establish an SSH session.

The user's key is tied to the lifecycle of their user account. If you suspend or delete a user in Cloud Identity or Google Workspace, their keys can no longer be used to grant SSH access.




Using metadata-based keys can expose you to persistence threats: Users might retain SSH access for longer than necessary if their public key isn't removed from metadata in a timely manner, and they might even retain access after leaving the organization. Although you can reduce this risk by regularly scouring metadata, doing so can be difficult in larger environments, and it might be insufficient because metadata-based keys grant users root privileges.

To help protect against such persistence threats, don't allow users to use metadata-based keys. Instead, configure your projects to enforce the use of OS Login.

## Use organizational policies to enforce consistent use of OS Login

OS Login is controlled [by the `enable-oslogin` metadata key](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#enable_os_login): Setting `enable-oslogin` to `TRUE` in project or instance metadata enables OS Login, setting it to `FALSE` disables OS Login.

To modify project-level metadata, you need the `compute.projects.setCommonInstanceMetadata` permission on the project. This permission is part of the _Compute Instance Admin_ (`roles/compute.instanceAdmin.v1`) and _Compute Admin_ (`roles/compute.admin`) roles. Similarly, modifying instance-level metadata requires the `compute.instances.setMetadata` permission on the respective VM instance.

Instance-level metadata takes higher precedence than project-level metadata. Setting `enable-oslogin` to `TRUE` in project metadata is therefore insufficient to enforce the use of OS Login throughout the project: Users with _Compute Instance Admin_ or equivalent access to a VM instances in the project can override your setting by adding `enable-oslogin=FALSE` to the VM instance's metadata.

To enforce consistent use of OS Login, don't rely on setting `enable-oslogin` to `TRUE` in project metadata. Instead, apply the [Enable OS Login for an organization using an organization policy](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#set-org-policy) so that any attempts to set `enable-oslogin` to `false` in instance or project metadata are rejected.

## Grant privileged roles on a temporary or per-VM basis

If you have VM instances that run different workloads and are managed by different teams, you can simplify access management by deploying these VMs in different Google Cloud projects, and letting the projects use a shared network. But using separate projects isn't always viable and some of your projects might contain a combination of VM instances, where different VM instances should only be accessible to different users.

Whenever a project contains such a combination of different VM instances, avoid permanently granting users roles such as _Compute Instance Admin_ on the project level. Instead, distinguish between view-only and privileged access:

  * Grant users _Compute Viewer_ or an equivalent view-only role on the project level. This role lets users browse VMs using the Google Cloud console, but doesn't let them publish SSH keys or access the VMs.
  * Grant users Compute _OS Login_ , _Compute Instance Admin_ , or other privileged roles only for individual VMs, or [on a just-in-time basis only](https://docs.cloud.google.com/architecture/manage-just-in-time-privileged-access-to-project).



## Suspend user accounts when users leave the organization

Suspending or deleting a user account in Cloud Identity or Google Workspace automatically revokes the user's IAM permissions. Because OS Login checks a user's IAM permissions before allowing them to establish an SSH session, suspending or deleting a user account also revokes the user's access to VMs that use OS Login.

If you've configured Cloud Identity or Google Workspace to use an external IdP for single sign-on, then employees have a user account in both your external IdP and in Cloud Identity or Google Workspace. Disabling or deleting an employee's user account in your external IdP [revokes their ability to establish new browser sessions to access Google services](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#propagate_suspension_events_to_cloud_identity_or_g_suite), but has no immediate impact on OS Login: As long as the employee's Cloud Identity or Google Workspace user account remains active, OS Login will continue to allow the user to authenticate and establish SSH connections.

To reliably revoke SSH access when a user leaves the organization, make sure to suspend or delete their Cloud Identity or Google Workspace user account. If you use an external IdP, configure it to [propagate user suspension events](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#propagate_suspension_events_to_cloud_identity_or_g_suite) so that OS Login can revoke access.

## Avoid granting SSH access to VMs that have a privileged service account

If a VM instance has an [attached](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts#attaching-to-resources) service account, then applications running on the VM can [request short-lived credentials from the VM's metadata server](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#applications) and use these credentials to [act as the service account](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts).

Having SSH access to a VM grants you similar privileges: Like an application, you can request short-lived credentials from the VM's metadata server and act as the attached service account.

Because having SSH access to a VM with an attached service account lets you act as the service account, OS Login requires you to have the `iam.serviceAccounts.actAs` permission on the service account, and checks for this permission every time you connect to the VM instance. That way, OS Login helps maintain the security of the service account and prevent SSH access from being abused for privilege escalation.

To further mitigate the risks associated with VMs that have privileged service accounts, consider the following alternatives:

  * Don't attach a service account to the VM unless the workload requires access to Google Cloud resources.
  * Use a [single-purpose service account](https://docs.cloud.google.com/iam/docs/best-practices-for-using-and-managing-service-accounts#single-purpose) and only grant it access to the resources that workload needs.
  * Require users to [request a just-in-time access](https://docs.cloud.google.com/architecture/manage-just-in-time-privileged-access-to-project) instead of granting them access to the VM and service account on a permanent basis.



## Limit the use of root privileges

When you use OS Login and grant a user the _OS Login User_ (`roles/compute.osLogin`) role, you're assigning the user limited user privileges on the VM. In contrast, when you grant a user the _OS Login Admin User_ (`roles/compute.osAdminLogin`) role, use metadata-based key authorization instead of OS Login, or allow users to modify VM metadata, you're implicitly granting the user root privileges on the VM.

Granting users root privileges on a VM can expose you to persistence risks: Users might abuse these privileges to create new user accounts or install backdoors to maintain persistent access to the VM.

To help reduce this persistence risk, limit the use of root privileges and only grant the _OS Login User_ (`roles/compute.osLogin`) role when root privileges aren't required.

## Pre-create POSIX profiles to ensure consistent usernames and UIDs

Each Linux VM maintains a local database of users (`/etc/passwd`) and groups (`/etc/groups`). When you first connect to a Linux VM by using SSH, the guest environment automatically creates a Linux user account for you, and assigns it a UID.

When you use metadata-based keys, the guest environment doesn't link the Linux user to your Google user account and might assign you a different UID on each VM you connect to. If you use protocols such as NFS that assume consistent UIDs in an environment that doesn't enforce consistent UIDs across machines, users might – accidentally or, in the case of bad actors, deliberately – be able to perform remote access as a different user.

When you use metadata-based keys, the guest environment also lets you choose the username you want to use. If you choose a username that a coworker used previously, you're logged in with the account that was initially created for your coworker.

You can prevent such UID and username ambiguities by using OS Login: When you first sign in to a Linux VM by using OS Login, the guest environment creates a Linux user based on your Google user account's [POSIX profile](https://docs.cloud.google.com/compute/docs/oslogin#user_account_configuration). The POSIX profile serves as a template for Linux users and defines the following:

  * a Linux username that's unique across all users of the same Cloud Identity or Google Workspace account
  * a UID and GID that unique across all Google Cloud projects
  * a home directory path
  * additional configuration, such as a login shell



If your Google Account doesn't have a POSIX profile when you first sign in, OS Login automatically creates one for you.

The username and UIDs allocated by OS Login are unique within your Google Cloud environment, but might overlap or be inconsistent with usernames and UIDs that you use outside of Google Cloud. If you need OS Login usernames and UIDs to be consistent across other environments, it's best not to rely on automatic profile creation. Instead, use the [Directory API](https://developers.google.com/admin-sdk/reference-overview) to pre-create OS Login POSIX profiles and assign custom usernames, UIDs, and GIDs.

## What's next

  * Continue reading about [best practices for protecting SSH credentials](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/credentials)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

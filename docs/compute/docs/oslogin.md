---
url: https://docs.cloud.google.com/compute/docs/oslogin/
title: About OS Login \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:19.781309+00:00
---

# About OS Login  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About OS Login Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the OS Login service and how it works. To learn how to set up OS Login, see [Set up OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin).

Use OS Login to manage SSH access to your instances using IAM without having to create and manage individual SSH keys. OS Login maintains a consistent Linux user identity across Compute Engine instances and is the recommended way to manage many users across multiple compute instances or projects.

**Note:** When a user connects to a VM, that user can use all of the IAM permissions granted to the service account attached to the VM. 

## Benefits of OS Login

OS Login simplifies SSH access management by linking your Linux user account to your Google identity. Administrators can easily manage access to instances at either an instance or project level by setting IAM permissions.

OS Login provides the following benefits:

  * **Automatic Linux account lifecycle management** \- You can directly tie a Linux user account to a user's Google identity so that the same Linux account information is used across all instances in the same project or organization.

  * **Fine grained authorization using Google IAM** \- Project and instance-level administrators can use IAM to grant SSH access to a user's Google identity without granting a broader set of privileges. For example, you can grant a user permissions to log into the system, but not the ability to run commands such as `sudo`. Google checks these permissions to determine whether a user can log into a compute instance.

  * **Automatic permission updates** \- With OS Login, permissions are updated automatically when an administrator changes IAM permissions. For example, if you remove IAM permissions from a Google identity, then access to compute instances is revoked. Google checks permissions for every login attempt to prevent unwanted access.

  * **Ability to import existing Linux accounts** \- Administrators can choose to optionally synchronize Linux account information from Active Directory (AD) and Lightweight Directory Access Protocol (LDAP) that are set up on-premises. For example, you can ensure that users have the same user ID (UID) in both your Cloud and on-premises environments.

  * **Integration with Google Account two-step verification** \- You can optionally require that OS Login users [validate their identity using 2-step verification (2FA)](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#2fa) when connecting to compute instances. OS Login supports the following challenge types: [Google Authenticator](https://support.google.com/accounts/answer/1066447), text message or phone call verification, [phone prompts](https://support.google.com/accounts/answer/7026266), and [security key one-time password (OTP)](https://gsuiteupdates.googleblog.com/2019/06/security-codes-and-security-keys.html).

  * **Support for certificate-based authentication** \- You can use SSH certificate authentication to connect to compute instances that use OS Login. For more information, see [Require SSH certificates with OS Login](https://docs.cloud.google.com/compute/docs/oslogin/certificates).

  * **Integration with audit logging** \- OS Login provides [audit logging](https://docs.cloud.google.com/compute/docs/oslogin/view-audit-logs) that you can use to monitor connections to compute instances for OS Login users.




## OS Login IAM roles

OS Login uses IAM to authorize login access. You can grant OS Login IAM roles at the instance, folder, or organization level. OS Login provides the following predefined roles:

  * `roles/compute.osLogin`: grants login access without `sudo` access to compute instances.
  * `roles/compute.osAdminLogin`: grants login access with `sudo` access to compute instances.



For guidance on assigning OS Login IAM roles, see [Assign OS Login IAM roles](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#configure_users).

## How OS Login works

When OS Login is enabled, Compute Engine performs configurations on compute instances and the Google accounts of OS Login users.

### Compute instance configuration

When you enable OS Login, the compute instance fetches the SSH keys associated with the Linux user account from the OS Login service to authenticate a login attempt. 

You can configure an `authorized_keys` file to provision access for a local user account even when OS Login is enabled. SSH public keys that are configured in the `authorized_keys` file are used to authenticate user login attempts by the local user. Local user accounts and OS Login users must have different usernames and UIDs.

**Note:** Compute instances that use OS Login can't use metadata-based SSH keys. If you enable OS Login for a compute instance, then the compute instance's guest agent ignores the keys stored in metadata. To learn more about using SSH keys with compute instances, see [Add SSH keys to compute instances](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys).

For more information about the OS Login components, review the [OS Login GitHub page](https://github.com/GoogleCloudPlatform/guest-oslogin#overview).

### User account configuration

OS Login configures your Google account with POSIX information, including a username, when you do any of the following:

  * Connect to an OS Login-enabled compute instance using the Google Cloud console
  * Connect to an OS Login-enabled compute instance using the gcloud CLI
  * Import a public SSH key using the gcloud CLI
  * Import a public SSH key using the OS Login API



OS Login configures POSIX accounts with the following values:

  * **Username:** a username in the format of `USERNAME_DOMAIN_SUFFIX`. If the user is from a different Google Workspace organization than the one hosting their OS Login-enabled compute instances, their username is prefixed with `ext_`. If the user is a service account, its username is prefixed with `sa_`. Usernames cannot exceed 32 characters. Usernames that exceed 32 characters are truncated.

Cloud Identity administrators can [modify usernames](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#modify-users) and Google Workspace super administrators can change the username format to [remove the domain suffix](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#manage-oslogin-api).

  * **UID:** a unique, randomly-generated [POSIX-compliant](https://en.wikipedia.org/wiki/User_identifier) user ID.

  * **GID:** a POSIX-compliant group ID that matches the UID.

  * **Home directory:** the path to the user's home directory.


Organization administrators can configure and update a user's POSIX account information. For more information, see [Modify user accounts using the Directory API](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#modify-users). 

## Limitations

OS Login isn't supported on all compute instance configurations. For more information, see [OS Login limitations](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#limitations).

## What's next

  * For step-by-step instructions, review one of the following: 
    * [Set up OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin).
    * [Set up OS Login with 2FA](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#2fa)
  * Review [Managing OS Login in an organization](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org)
  * [Troubleshoot](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-os-login) OS Login.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

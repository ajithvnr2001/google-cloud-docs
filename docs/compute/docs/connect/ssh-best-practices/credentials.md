---
url: https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/credentials/
title: Best practices for protecting SSH credentials \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:23.262610+00:00
---

# Best practices for protecting SSH credentials  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Best practices for protecting SSH credentials Stay organized with collections  Save and categorize content based on your preferences. 

This document describes best practices for protecting SSH credentials.

By default, Compute Engine uses public key-based SSH authentication: Users are authenticated _by something they have_ , which is an SSH private key. If users' private keys aren't properly secured, they might fall into the hands of bad actors who might use these keys to access your VM instances.

The following sections contain best practices that can help you avoid key leakage and reduce the potential impact of leaked private keys:

  * Treat SSH private keys similar to service account keys
  * Use ephemeral SSH keys for machine users
  * Use IAP to complement SSH public key authentication
  * Use multi-factor authentication
  * Use non-exportable or passphrase-protected private keys
  * Use host keys to authenticate the host
  * Don't leave personal credentials on VMs
  * Don't submit SSH private keys to source code repositories



The document focuses on practices that are either specific to Google Cloud or of particular relevance when using SSH on Google Cloud. The document doesn't cover best practices for specific SSH client or server implementations.

## Treat SSH private keys similar to service account keys

Some of your VM instances may have an [attached](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts#attaching-to-resources) service account. Attaching a service account to a VM lets workloads running on these VMs [request short-lived access tokens from the metadata server](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#applications) so that they can access Google Cloud APIs and resources.

When you connect to a VM with an attached service account by using SSH, you can also [request short-lived access tokens from the metadata server](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#applications). Granting a user SSH access to a VM is therefore similar to granting the user permission to [act as the attached service account](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts). Because of that similarity, treat SSH private keys, especially when they're not passphrase-protected, [like service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys): Both kinds of keys, if leaked, might grant a bad actor access to Google Cloud resources.

## Use ephemeral SSH keys for machine users

Deployment pipelines or automation processes might require SSH access to VM instances to perform deployments or apply configuration changes. Instead of letting these workloads use a long-lived SSH key pair, let them use a new, ephemeral SSH key every time they run.

To use ephemeral SSH keys, let your deployment pipelines or automation processes perform the following steps:

  1. Authenticate as a service account in a way that doesn't involve a key or secret, for example by using an [attached service account](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts#attaching-to-resources) or [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).
  2. Generate a temporary SSH key pair by using a tool such as `ssh-keygen`.
  3. Publish the public key to Google Cloud, specifying a near-future expiry date (such as 1h in the future).

OS Login lets you specify a key expiration date when [you publish a key](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1/users/importSshPublicKey). Similarly, you can [specify an expiry date](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#during-vm-creation) when you publish an SSH public key to project or VM metadata.

  4. Use the private key to establish SSH connections to VM instances.

  5. Optionally, unpublish the public key and delete the private key.




For example:
    
    
    # Generate RSA key pair without passphrase
    ssh-keygen -t rsa -f ephemeral_key -q -N "" -V 30m
    
    # Publish key to the service account's OS Login profile, with 30 min expiry
    gcloud compute os-login ssh-keys add --key-file ephemeral_key.pub --ttl 30m
    
    # Look up the service account's UNIX username
    USERNAME=$(gcloud compute os-login describe-profile --format "value(posixAccounts[0].username)")
    
    # Authenticate using the service account's UNIX user and public key
    ssh $USERNAME@VM whoami
    
    # Remove key
    gcloud compute os-login ssh-keys remove --key-file ephemeral_key.pub
    

While an ephemeral SSH private key might still be leaked, it can only be used for a short time. Using ephemeral SSH keys can therefore reduce your risk of credential leakage, and lets you use Cloud IAM as the primary means of authentication and authorization.

## Use IAP to complement SSH public key authentication

By default, SSH private keys can be used independently of Google credentials: If a user's private SSH key is leaked, a bad actor can use the key to connect and authenticate to any VM instances that the key is authorized to access. It's not necessary for the bad actor to know the user's username or password, or to even possess any Google credential.

Security controls such as [two-step verification](https://support.google.com/accounts/answer/185839?co=GENIE.Platform%3DAndroid) and [limiting the session length for Google Cloud services](https://support.google.com/cloudidentity/answer/9368756?ref_topic=7558427) can be effective ways to reduce the risk of credential theft, but these controls only apply to resources that require Google credentials.

To ensure that SSH keys can't be used without valid Google credentials, use IAP to govern SSH access and [use firewall policies](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/network-access#use-firewall-policies) to enforce that all SSH access is performed through IAP.

IAP acts as a reverse proxy and only permits users to establish SSH connections to VM instances if they successfully authenticated using their Google credentials. Additionally, IAP lets you [restrict which VMs users can connect to](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#grant-permission), and enforce context-aware access.

## Use multi-factor authentication

Using IAP to govern SSH access makes it more difficult for a bad actor to access VM instances using leaked credentials, but doesn't make it impossible: For example, a bad actor might compromise a workstation and find both, a private SSH key and cached gcloud CLI credentials – enough to pass IAP's authentication and authorization checks, and connect to the user's VM instances.

You can reduce the possible impact of such credential theft attacks by configuring Cloud Identity or Google Workspace to require multi-factor authentication (MFA).

If [Cloud Identity or Google Workspace is your primary identity provider](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_google_as_an_idp), do the following to enforce MFA:

  1. Configure Cloud Identity or Google Workspace to [enforce 2-step verification](https://support.google.com/a/answer/175197).
  2. [Limit the session length for Google Cloud services](https://support.google.com/cloudidentity/answer/9368756?ref_topic=7558427) so that cached credentials are automatically invalidated and users have to periodically re-authenticate and perform MFA.



If you [use single sign-on with an external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp), do the following instead:

  1. Configure Cloud Identity or Google Workspace to [limit the session length for Google Cloud services](https://support.google.com/cloudidentity/answer/9368756?ref_topic=7558427) so that cached credentials are automatically invalidated and users have to periodically re-authenticate using the external IdP.
  2. Configure your external IdP to require MFA, and limit its session length so that users have to perform MFA every time their Google Cloud session expires.



To ensure that MFA also applies to SSH access, you must also do at least one of the following:

  1. [Use IAP to control network access](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/network-access#reduce-network-exposure) so that users have to periodically perform MFA to refresh their Google credentials.
  2. [Enable OS Login 2FA](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin) for individual VM instances or entire projects so that users have to perform MFA every time they establish an SSH connection.



Users that have the _Compute Instance Admin_ or an equivalent role for a VM instance or project can disable OS Login 2FA by modifying instance metadata. The effectiveness of OS Login 2FA is therefore limited if you don't also enforce MFA in Cloud Identity or your external IdP.

## Use non-exportable or passphrase-protected private keys

Many SSH clients default to storing SSH private keys as files on disk. For example, `gcloud compute ssh` generates an SSH key pair on first use, and stores it in your home directory. Your operating system might protect your files from being accessed by other users, but if a bad actor can overcome file system permissions (for example, by copying and mounting the disk on another machine), they can copy the key elsewhere, and use it without your knowledge.

Some SSH clients let you avoid using file-based keys and offer alternative options to manage SSH private keys, such as:

  * Using a hardware-backed key: Modern versions of OpenSSH let you use FIDO2 security keys for authentication, and you can [configure OS Login](https://docs.cloud.google.com/compute/docs/oslogin/security-keys) so that it only permits security keys that are enrolled in Cloud Identity or Google Workspace. Using hardware-backed keys helps you avoid storing any private key material on your computer's file system.
  * Using your operating system's key storage facilities: For example, IAP Desktop avoids using file-based keys and instead uses [Windows CNG](https://learn.microsoft.com/en-us/windows/win32/seccng/key-storage-and-retrieval) to protect your SSH keys.



If using hardware-backed or operating system-managed keys isn't an option, you can use a passphrase to protect your SSH private key: To use a passphrase-protected SSH key, a bad actor not only needs a copy of the private key, but also needs to know the key's passphrase.

## Use host keys to authenticate the host

When you create an SSH connection to a VM instance, you identify the VM instance by its name or IP address. Names and IP addresses can be reassigned and reused, and the name that referred to a certain VM instance yesterday might not refer to the same VM instance today. Bad actors might deliberately reassign or reuse names or IP addresses to _spoof_ VM instances and lure users into connecting to a compromised VM.

SSH clients can detect situations where a previously-trusted VM instance was replaced with a different VM instance by using SSH host keys: A VM's SSH host key is generated on first boot and is used to identify the instance. SSH clients typically request and store a VM's host key on the first connection and verify that the VM's host key hasn't changed on subsequent connections.

SSH host keys work based on the [trust on first use](https://en.wikipedia.org/wiki/Trust_on_first_use) scheme. The effectiveness of SSH host keys can be undermined if a bad actor uses a man in the middle (MITM) attack to let a client connect to and trust the wrong VM on first use. A better way to obtain a host key is to obtain it over a trusted side channel before connecting to a VM for the first time.

You can let the gcloud CLI [obtain host keys over a back channel by enabling guest attributes](https://cloud.google.com/solutions/connecting-securely#storing_host_keys_by_enabling_guest_attributes) in your project. The gcloud CLI then reads a VM's host key before you first connect to it, and saves them on your local computer.

## Don't leave personal credentials on VMs

When you [authorize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate), the tool obtains an [OAuth refresh token](https://developers.google.com/identity/protocols/oauth2) and stores it in your local home directory. When you subsequently run a gcloud CLI command, the gcloud CLI uses the refresh token to authenticate you automatically.

Your local computer might be inaccessible to other users, but on a VM instance, your home directory can also be accessed by other users that have sudo privileges on the VM.

If a bad actor manages to obtain sudo privileges on a VM, they might scan for refresh tokens and other credentials in other users' home directories, and [use these credentials to escalate their privileges or extend their access to other resources](https://docs.cloud.google.com/docs/security/bps-for-protecting-developer-credentials) (lateral movement).

When you're connected to a VM instance over SSH, avoid authorizing the gcloud CLI or Application Default Credentials (ADC) with your personal credentials, and let the gcloud CLI use the VM's attached service account instead. Similarly, avoid running other tools that might store personal credentials in your home directory.

You can further reduce risks by [limiting the session length for Google Cloud services](https://docs.cloud.google.com/docs/security/bps-for-protecting-developer-credentials#set-session-length-for-google-cloud-services) so that stored OAuth refresh tokens automatically expire after a certain amount of time.

## Don't submit SSH private keys to source code repositories

Some automation tools like Ansible use SSH to access and manage VM instances. Because such tools might have access to many VM instances (and their attached service accounts), the SSH private keys used by such tools can be particularly sensitive.

If you submit an SSH private key to a source code repository, there is an increased risk that the key becomes accessible to unauthorized users and bad actors:

  * Bad actors might scan the source code of public source repositories for leaked keys.
  * In the future, you might decide to turn a private source repository into a public repository, without checking it for keys first.
  * Other team members might store copies of the source code on their workstation.



To mitigate these risks, store the SSH private key in a secure location that's separate from the source code and use ephemeral SSH keys when possible.

**Important:** If you accidentally submitted an SSH private key to a source code repository, it's insufficient to delete the key from the source code repository because the key might persist in the repository history or other users' local copies. You must also revoke access by removing the corresponding public key from the user's OS Login profile, project and instance metadata, and other applications that you used the key for.

## What's next

  * Continue reading about [best practices for auditing SSH access](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/auditing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org/
title: Manage OS Login in an organization \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:37.651030+00:00
---

# Manage OS Login in an organization  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage OS Login in an organization Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document describes how you can use OS Login to manage access to VM instances across your organization.

Note: To complete any of the tasks detailed in this document, you must be a Google Workspace administrator. 

This topic covers the following tasks:

  * Enable OS Login for an organization using an organization policy: Use an organization policy to ensure that all new VM instances in your organization have OS Login enabled.
  * Grant instance access to users outside of your organization: Allow user accounts outside of your organization to use SSH to connect to your instances.
  * Manage the OS Login API: Allow or deny users access to use the OS Login API. Also enable or disable features of the OS Login API.
  * Audit OS Login events: Track OS Login-related events and activities such as adding, deleting, or updating an SSH key, or deleting POSIX information.
  * Modify user accounts using the Directory API: Update user properties, such as username and POSIX account information, by using the Directory API.
  * Use Linux groups with OS Login (Deprecated): Manage user permissions within VMs by using Linux groups with OS Login.
  * Use OS Login with [workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) ([Preview](https://cloud.google.com/products/#product-launch-stages)): Connect to VMs that have OS Login enabled when your organization uses an external identity provider (IdP).



## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## OS Login organization policy

You can set up an OS Login constraint in your organization to ensure that all new projects, and the VM instances created in these new projects, have OS Login enabled.

When this constraint is set up, the following conditions are applied:

  * `enable-oslogin=true` is included in the project metadata for all new projects.
  * Requests that set `enable-oslogin` to `false` in instance or project metadata are rejected, for new and existing VMs and projects.



### Limitations

OS Login isn't supported in the following products, features, and OS images: 

  * Cloud Data Fusion versions 6.1.4 and earlier.
  * Managed Service for Apache Airflow 1.
  * OS Login profiles with a total size greater than 32 KiB. The OS Login profile includes POSIX account information and SSH public keys.
  * Compute instance that use the following OS images:
    * Windows Server and SQL Server.
    * Fedora CoreOS. To manage instance access to compute instances created using these images, use the [Fedora CoreOS ignition system](https://docs.fedoraproject.org/en-US/fedora-coreos/producing-ign/).
    * SLES 16. To manage instance access to compute instances created by using these images, use the [Metadata-based SSH](https://docs.cloud.google.com/compute/docs/instances/access-overview#ssh-access/).



#### Workarounds for Cloud Data Fusion and Managed Airflow

To use OS Login in organizations that use Cloud Data Fusion and Managed Airflow, you can enable OS Login constraint at the organization level and then selectively disable the constraint on projects or folders for the affected projects.

For more information about editing organization policies, see [creating and editing policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#creating_and_editing_policies). 

### Enable the organization policy

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `resourcemanager.organizationAdmin role`. For more information see, [Access control for organizations using IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-org).
  * To learn more about managing policies at the organization level, see [Add an organization policy administrator](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#add-org-policy-admin).



To enable the OS Login policy, you can set the OS Login constraint on specific projects and folders by using the Google Cloud CLI. You can also set the OS Login constraint on the entire organization by using either the Google Cloud console or the Google Cloud CLI.

###  Console 

To set the OS Login [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#boolean_constraints) from the console, complete the following steps:

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to the Organization policies page](https://console.cloud.google.com/iam-admin/orgpolicies/)

  2. In the policies list, click **Require OS Login** to view the OS Login constraints.
  3. Click **Edit** to edit your existing OS Login constraints.
  4. On the **Edit** page, select **Customize**.
  5. To enable enforcement of this constraint, select **On**.
  6. Click **Save** to apply the constraint settings.



###  gcloud 

To set the OS Login organization policy, use the [`gcloud beta resource-manager org-policies enable-enforce`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/org-policies/enable-enforce) command.

  1. Find your organization ID.
         
         gcloud organizations list

  2. Set the constraint in your organization. Replace `organization-id` with your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
         
         gcloud beta resource-manager org-policies enable-enforce compute.requireOsLogin \
             --organization=organization-id
         




You can also apply the OS Login organization policy to a folder or a project with the `--folder` or the `--project` flags, and the folder ID and project ID, respectively.

For folders, run the following command:
    
    
    gcloud beta resource-manager org-policies enable-enforce compute.requireOsLogin \
        --folder=folder-id
    

For projects, run the following command:
    
    
    gcloud beta resource-manager org-policies enable-enforce compute.requireOsLogin \
        --project=project-id
    

Replace the following:

  * `folder-id`: your [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).
  * `project-id`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).



## Grant instance access to users outside of your organization

**Note:** If your project is part of an [organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization), you can grant instance access to users who are outside of your organization by using `roles/compute.osLoginExternalUser` or by using a [custom role with the `compute.oslogin.updateExternalUser` permission](https://docs.cloud.google.com/compute/docs/access/iam#compute.osLoginExternalUser).

By default, users outside of your organization can't set SSH keys for instances in your organization or be granted access to instances in your organization. In some situations, you might need to grant instance access to users who are part of a different organization or who have a consumer Google `gmail.com` account.

The [`roles/compute.osLoginExternalUser`](https://docs.cloud.google.com/compute/docs/access/iam#compute.osLoginExternalUser) IAM role lets external Google Accounts interact with the other OS Login roles by allowing them to configure POSIX account information.

To grant `roles/compute.osLoginExternalUser` and other necessary OS Login instance access roles to users outside of your organization, complete the following steps:

  1. In the Google Cloud console, go to the **IAM & Admin** page. 

[Go to IAM & Admin](https://console.cloud.google.com/projectselector/iam-admin/iam)

  2. Click the **Select a project** drop-down menu. In the **Select a resource** dialog that appears, select your organization by doing the following: 
     1. Click the organization drop-down menu to view all of your organizations.
     2. Select your organization from the drop-down.
  3. Click **Grant access** to add a new role to a user.
  4. In the **New principals** field, add the email address for the user for whom you want to configure instance access.
  5. From the **Role** drop-down menu, select the **Compute OS Login External User** role.
  6. Click **Save**.
  7. If you have not already done so, [grant the other OS Login instance access roles](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access#configure_users) to the user at the project or organization level.



The user can now [connect to instances](https://docs.cloud.google.com/compute/docs/connect/standard-ssh) in your project that have OS Login enabled.

## Manage the OS Login API

At an organization level, you can restrict access to the OS Login API by setting Google Workspace admin controls. To configure Google Workspace admin controls or view configuration options, see [Control who uses Google Cloud in your organization](https://support.google.com/a/answer/9197205). As a Google Workspace admin, you can also turn on or off certain features of the OS Login API. This includes the following options:

  * Choose whether to include the domain suffix in usernames generated by OS Login API. For example, in the domain `example.com`, the user `user@example.com` will have the username `user` if the setting to include domain suffix is not checked.
  * Decide if members of your organization can manage SSH keys using the OS Login API.
  * Restrict or permit VM access to users outside of your organization.



For more information about turning on or off OS Login API settings, see [Choose settings for Google Cloud Platform](https://support.google.com/a/answer/9197205).

## Audit OS Login events

As a Google Workspace Admin, you can use the Google Workspace Admin SDK to audit actions performed with the OS Login API. By reviewing these events, you can track when a user adds, deletes, or updates an SSH key, or deletes POSIX account information.

You can retrieve OS Login API audit activity events, from the Google Workspace Admin SDK, by calling `Activities.list()` with `applicationName=gcp`. For more information, see [Google Cloud activity events](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/gcp#CLOUD_OSLOGIN) in the Google Workspace Admin SDK Reports API documentation.

## Modify user accounts using the Directory API

**Note:** You can't use the Directory API to modify Google consumer accounts, service accounts, or accounts for users outside your Google Workspace organization.

OS Login uses either your [Cloud Identity](https://docs.cloud.google.com/identity) or [Google Workspace](https://support.google.com/a/topic/14586?hl=en&ref_topic=2425090) user settings when connecting to an instance. If you are a Google Workspace super admin, you can use the Directory API to complete the following tasks for your Google Workspace or Cloud Identity user accounts:

  * Modify instance login settings
  * [Make a user an administrator](https://developers.google.com/admin-sdk/directory/v1/guides/manage-users#make_admin)
  * Modify user properties such as account name and email
  * Add and remove SSH keys for a user
  * Modify POSIX account information
  * Change the username that the users connect to on the instance



The following examples show how to modify or remove user accounts using the Directory API. For more information about the account properties that you can edit, see the [Directory API reference](https://developers.google.com/admin-sdk/directory/v1/reference/).

###  Modify account properties 

To modify a user's POSIX account information or manage the user's SSH keys, issue a `PUT` request to the [`directory.users.update` method](https://developers.google.com/admin-sdk/directory/v1/reference/users/update) and specify one or more properties to change on the user account.

If you modify a user's `posixAccounts` properties, you must specify the current or new `username`, `uid`, and `gid` values in the request.

If you modify the user's `sshPublicKeys` properties, you must specify the `key` value in the request.

**Caution:** Do not update the `systemId` property. OS Login ignores POSIX account information where the `systemId` is not blank.

The following is an example of a `PUT` request:
    
    
    PUT https://admin.googleapis.com/admin/directory/v1/users/USER_KEY
    
    {
     "posixAccounts": [
      {
        "username": "USERNAME",
        "uid": "UID",
        "gid": "GID",
        "homeDirectory": "USER_HOME_PATH",
        "shell": "SHELL_PATH"
       }
      ],
     "sshPublicKeys": [
      {
        "key": "KEY_VALUE",
        "expirationTimeUsec": EXPIRATION_TIME
       }
      ],
    }
    

Replace the following:

  * `USER_KEY`: the user's primary email address, alias email address, or unique user ID.
  * `USERNAME`: the username that Compute Engine adds to the VM for the user. This value must be unique within your organization and must not end in a tilde ("~") or contain a period (".").
  * `UID`: the user ID on the VM for this user. This property must be a value between `1001` and `60000`, or a value between `65535` and `2147483647`. To access a container-optimized OS, the `UID` must have a value between `65536` and `214748646`. The `UID` must be unique within your organization.
  * `GID`: the group ID on the VM that the user belongs to.
  * `USER_HOME_PATH`: (Optional) the home directory on the VM for the user. For example, `/home/example_username`.
  * `SHELL_PATH`: (Optional) the path to the default shell for the user after they connect to the instance. For example, `/bin/bash` or `/bin/sh`.
  * `KEY_VALUE`: the public SSH key value.
  * `EXPIRATION_TIME`: (Optional) the key's expiration time in microseconds since epoch (1 second = 106 microseconds).



###  Remove account properties 

To clear the `posixAccounts` and `sshPublicKeys` data for a user, issue a `PUT` request to the [`directory.users.update` method](https://developers.google.com/admin-sdk/directory/v1/reference/users/update), setting the `posixAccounts` and `sshPublicKeys` fields to `null`:
    
    
    PUT https://admin.googleapis.com/admin/directory/v1/users/USER_KEY
    
    {
     "posixAccounts": null,
     "sshPublicKeys": null
    }
    

Replace `USER_KEY` with the user's primary email address, alias email address, or unique user ID.

## Use Linux groups with OS Login (Deprecated)

**Caution:** OS Login POSIX groups support is [deprecated](https://docs.cloud.google.com/compute/docs/deprecations). As of September 26, 2024, you can no longer use OS Login to link POSIX groups with supplementary Linux groups in your organization's VMs. We recommend that you delete OS Login POSIX group configurations.

Organization admins can use the [Cloud Identity Groups API](https://docs.cloud.google.com/identity/docs/groups) to configure supplementary Linux groups for OS Login users by creating and managing POSIX groups. OS Login links POSIX groups with supplementary Linux groups in your organization's VMs so that you can manage the permissions users have in your VMs.

### Manage user membership in Linux groups

To create a POSIX group, see [Creating and updating POSIX groups](https://docs.cloud.google.com/identity/docs/how-to/create-posix-groups).

To add users to a group, see [Add or invite users to a group](https://support.google.com/cloudidentity/answer/9400087?&ref_topic=7558943).

Membership updates take effect within 10 minutes. Group changes are reflected in all newly created VMs. POSIX group updates may take up to six hours to propagate to all running VMs. Users may have to log out or use the `newgrp` command to observe group changes.

#### Delete POSIX groups configurations

OS Login POSIX group support is deprecated. We recommend that you delete OS Login POSIX groups configurations.

You must be an [organization administrator](https://docs.cloud.google.com/resource-manager/docs/access-control-org#resourcemanager.organizationAdmin) to delete OS Login POSIX group configurations.

**Caution:** Removing OS Login POSIX groups configurations might disrupt users' ability to access resources on Linux VMs. If you use POSIX groups to manage access on your Linux VMs, ensure that you transition to an alternative method of access management before you delete OS Login POSIX group configurations.

  1. If you don't know your organization resource ID, [get your organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
  2. [List all POSIX groups](https://docs.cloud.google.com/identity/docs/how-to/retrieve-list-posix-groups#listing_posix_groups) in your organization. Note the email address of each group.
  3. For each POSIX group in your organization, do the following: 
     1. [Retrieve the group information](https://docs.cloud.google.com/identity/docs/how-to/retrieve-list-posix-groups#retrieving_a_posix_group_by_email). Note the `posixGroups.gid`.
     2. [Delete the POSIX group](https://docs.cloud.google.com/identity/docs/how-to/create-posix-groups#deleting_a_posix_group).
  4. Optionally verify that all groups have been deleted by [listing all POSIX groups](https://docs.cloud.google.com/identity/docs/how-to/retrieve-list-posix-groups#listing_posix_groups) in your organization. If all groups have been successfully deleted, the response is empty.



### Rate limits for Linux groups with OS Login

Linux groups with OS Login use `oslogin.googleapis.com/metadata_server_groups_requests` quota. By default, the quota limit is **60 requests/minute** , per project for a particular region.

If you need a higher rate limit, you can [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase) from the Quotas page in the Google Cloud console.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?service=oslogin.googleapis.com)

## Use workforce identity federation with OS Login

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Organizations that use [workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) can use OS Login to manage access to their VMs. When workforce identity federation is enabled for an organization, OS Login uses certificate-based authentication instead of key-based authentication to verify user identities.

### Before you begin

  * [Create a workforce identity pool](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create).
  * [Set up `google.posix_username` attribute mappings](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings).
  * Configure your VM to use OS Login with workforce identity federation by doing the following:

    1. Confirm that the VM has OpenSSH 7.4 or later installed by running the following command on the VM:
           
           ssh -V
           

    2. [Update the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#update-guest).




### Limitations

  * You can't use workforce identity federation with OS Login two-factor authentication (2FA).
  * The VM you're connecting to must have OpenSSH version 7.4 or later to use workforce identity federation with OS Login.
**Note:** VMs built from SUSE Linux Enterprise Server (SLES) 12 images don't have OpenSSH 7.4 and can't use workforce identity federation with OS Login. 
  * If your organization uses workforce identity federation, you can't access VM's [serial ports](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output).



### Connect to VMs that use OS Login and workforce identity federation

Connect to VMs that use OS Login with workforce identity federation using the Google Cloud console, the gcloud CLI, or other SSH clients.

###  Console 

When you connect to VMs that use OS Login with workforce identity federation using [SSH-in-browser](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#console), Compute Engine configures the SSH certificate on your behalf when you attempt to connect.

To connect to VMs, do the following:

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the list of virtual machine instances, click **SSH** in the row of the instance that you want to connect to. 

![SSH button next to instance name.](https://docs.cloud.google.com/static/docs/images/establish-ssh-connection-1.png)




###  gcloud 

When you connect to VMs that use OS Login with workforce identity federation using the [gcloud CLI](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#gcloud), Compute Engine configures the SSH certificate on your behalf when you attempt to connect.

Connect to a VM using SSH by running the [`gcloud beta compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/ssh):

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the following command:
         
         gcloud beta compute ssh --project=PROJECT_ID --zone=ZONE VM_NAME

Replace the following:

     * `PROJECT_ID`: the ID of the project that contains the VM
     * `ZONE`: the name of the zone that the VM is located in
     * `VM_NAME`: the name of the VM

If you have [set default properties](https://docs.cloud.google.com/compute/docs/gcloud-compute#default-properties) for the Google Cloud CLI, you can omit the `--project` and `--zone` flags from this command. For example:
    
    gcloud compute ssh VM_NAME


**Note:** When you connect to VMs using the gcloud CLI, Compute Engine creates a persistent SSH key for you. For more information about SSH keys, see [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh).

###  IAP Desktop 

When you connect to VMs that use OS Login with workforce identity federation using [IAP Desktop](https://github.com/GoogleCloudPlatform/iap-desktop/), Compute Engine configures the SSH certificate on your behalf when you attempt to connect.

To connect to a VM using IAP Desktop, do the following:

  1. [Install IAP Desktop](https://github.com/GoogleCloudPlatform/iap-desktop/) on your workstation if you haven't already. 

  2. Open IAP Desktop. The **Add projects** window opens. 

  3. When prompted, [ sign in with workforce identity federation](https://googlecloudplatform.github.io/iap-desktop/install/#connect-to-google-cloud). 

  4. In the **Add projects** window, enter the project ID or name of the project that contains the VMs you want to connect to. 

  5. In the **Project Explorer** window, right-click the name of the VM again and select **Connect** to connect to the VM. 




###  SSH client 

To connect to a VM that uses OS Login with workforce identity federation using an SSH client, do the following:

  1. [Create an SSH key](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys) if you don't already have one.
  2. Sign your public SSH key using the [`users.projects.locations.signSshPublicKey` method](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users.projects.locations/signSshPublicKey):
         
         POST https://oslogin.googleapis.com/v1beta/users/USER/projects/PROJECT_ID/locations/LOCATION:signSshPublicKey
         
         {
          "ssh_public_key": "PUBLIC_KEY"
         }
         

Replace the following:

     * `USER`: a single identity in a workforce pool, in the following format: 
           
           principal:%2F%2Fiam.googleapis.com%2Flocations%2Fglobal%2FworkforcePools%2POOL_ID%2Fsubject%2FSUBJECT_ATTRIBUTE_VALUE
           

Replace the following:

       * `POOL_ID`: the workforce pool the user belongs to.
       * `SUBJECT_ATTRIBUTE_VALUE`: the value of the user's [`google.posix_username` attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings).
     * `PROJECT_ID`: the project ID of the project that contains the VM you want to connect to.

     * `LOCATION`: the zone where the VM you want to connect to is located.

     * `PUBLIC_KEY`: the contents of your SSH public key file.

  3. Copy the SSH certificate from the output of the `user.signSshPublicKey` method and save the contents in a new file.

  4. Set permissions on the SSH certificate file, by running the following command:
         
         sudo chmod 600 FILE_NAME
         

Replace `FILE_NAME` with the name of the file.

  5. Connect to the VM using the following command:
         
         ssh -i PATH_TO_PRIVATE_KEY -o CertificateFile=PATH_TO_SSH_CERTIFICATE USERNAME@EXTERNAL_IP
         

Replace the following:

     * `PATH_TO_PRIVATE_KEY`: the path to your private SSH key file.
     * `PATH_TO_SSH_CERTIFICATE`: the path to your SSH certificate file.
     * `USERNAME`: the value of the user's [`google.posix_username` attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings).
     * `EXTERNAL_IP`: the external IP address of the VM.



## What's next

  * Learn how to [set up OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access).
  * Learn how to [set up OS Login with 2-step verification](https://docs.cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication).
  * Read an overview of the [OS Login feature](https://docs.cloud.google.com/compute/docs/oslogin).
  * [Troubleshoot](https://docs.cloud.google.com/compute/docs/oslogin/troubleshoot-os-login) OS Login.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

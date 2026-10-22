---
url: https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin/
title: Set up OS Login \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:16.667857+00:00
---

# Set up OS Login  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Set up OS Login Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up OS Login.

OS Login lets you control access to virtual machine (VM) instances based on IAM permissions. To learn more about OS Login, see [About OS Login](https://docs.cloud.google.com/compute/docs/oslogin).

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

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 




## Limitations

OS Login isn't supported with the following: 

  * OS Login profiles with a total size greater than 32 KiB. The OS Login profile includes POSIX account information and SSH public keys.
  * Compute instance that use the following OS images:
    * Windows Server and SQL Server.
    * Fedora CoreOS. To manage instance access to compute instances created using these images, use the [Fedora CoreOS ignition system](https://docs.fedoraproject.org/en-US/fedora-coreos/producing-ign/).
    * SLES 16. To manage instance access to compute instances created by using these images, use the [Metadata-based SSH](https://docs.cloud.google.com/compute/docs/instances/access-overview#ssh-access/).



To verify OS Login support for specific Linux distributions, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).

## Assign OS Login IAM roles

Assign all of the required IAM roles to users who connect to VMs that have OS Login enabled.

Role | Required users | Grant level  
---|---|---  
`[roles/compute.osLogin](https://docs.cloud.google.com/compute/docs/access/iam#compute.osLogin)` or `[roles/compute.osAdminLogin](https://docs.cloud.google.com/compute/docs/access/iam#compute.osAdminLogin)` | All users | On the [Project](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) or [instance](https://docs.cloud.google.com/compute/docs/access/managing-access-to-resources#bind-member). If a user requires SSH access from Google Cloud console or Google Cloud CLI, you must grant these roles at the project level, or additionally grant a role at the project level that contains the `compute.projects.get` permission.  
`[roles/iap.tunnelResourceAccessor](https://docs.cloud.google.com/compute/docs/access/iam#iap.tunnelresourceaccessor)` | All users who require SSH access by using IAP TCP forwarding | On the [Project](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) or [instance](https://docs.cloud.google.com/compute/docs/access/managing-access-to-resources#bind-member).  
`[roles/iam.serviceAccountUser](https://docs.cloud.google.com/compute/docs/access/iam#iam.serviceAccountUser)` | All users, if the VM has a service account | On the [Service account](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).  
`[roles/compute.osLoginExternalUser](https://docs.cloud.google.com/compute/docs/access/iam#compute.osLoginExternalUser)` | Users from a different organization than the VM they're connecting to | On the [Organization](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#external-user). This role must be granted by an organization administrator.  
  
## Enable OS Login

You can enable OS Login for a single VM, or all VMs in a project, by setting `enable-oslogin` to `TRUE` in [project or instance metadata](https://docs.cloud.google.com/compute/docs/metadata/overview).

When you set OS Login metadata, Compute Engine deletes the VM's `authorized_keys` files and no longer accepts connections from SSH keys that are stored in project or instance metadata.

### Enable OS Login for all VMs in a project

To enable OS Login for all VMs in a project, set the following value in [project metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-projectwide):

  * Key: `enable-oslogin`
  * Value: `TRUE`



### Enable OS Login for a single VM

To enable OS Login for a single VM, set the following value in [instance metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#update_metadata):

  * Key: `enable-oslogin`
  * Value: `TRUE`



### Enable OS Login during VM creation

Enable OS Login while creating a VM using the Google Cloud console or the gcloud CLI.

###  Console 

Create a VM that enables OS Login on startup by [creating a VM from a public image](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#publicimage) and specifying the following configurations:

  1. Expand the **Advanced options** section.
  2. Expand the **Security** section.
  3. Expand the **Manage access** section.
  4. Select **Control VM access through IAM permissions**.
  5. Click **Create** to create and start the VM.



###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Create a VM that enables OS Login on startup by running the following [`gcloud compute instance create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create):
         
         gcloud compute instances create VM_NAME \
            --image-family=IMAGE_FAMILY \
            --image-project=IMAGE_PROJECT \
            --metadata enable-oslogin=TRUE
         

Replace the following:

     * `VM_NAME`: the name of the new VM.
     * `IMAGE_FAMILY`: the image family of a Linux OS. This creates the VM from the most recent non-deprecated OS image. For all public image families, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).
     * `IMAGE_PROJECT`: the image project that contains the image family. Each OS has its own image project. For all public image projects, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).



###  Terraform 

You can apply the metadata values to your projects or VMs by using one of the following options:

  * **Option 1:** Set `enable-oslogin` in project-wide metadata so that it applies to all of the VMs in your project.

Use the [`google_compute_project_metadata`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_project_metadata) Terraform resource and set a metadata value where `oslogin=TRUE`:
        
        resource "google_compute_project_metadata" "default" {
          metadata = {
            enable-oslogin = "TRUE"
          }
        }

Alternatively, you can set `enable-oslogin` to `FALSE` to disable OS Login.

  * **Option 2:** Set `enable-oslogin` in the metadata of a new or an existing VM.

Use the [`google_compute_instance`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance) Terraform resource and set `oslogin=TRUE`. Replace `oslogin_instance_name` with the name of your VM.
        
        resource "google_compute_instance" "oslogin_instance" {
          name         = "oslogin-instance-name"
          machine_type = "f1-micro"
          zone         = "us-central1-c"
          metadata = {
            enable-oslogin : "TRUE"
          }
          boot_disk {
            initialize_params {
              image = "debian-cloud/debian-13"
            }
          }
          network_interface {
            # A default network is created for all GCP projects
            network = "default"
            access_config {
            }
          }
        }

Alternatively, you can set `enable-oslogin` to `FALSE` to exclude your VM from using OS Login.




## Disable OS Login

You can disable OS Login by setting `enable-oslogin` to `FALSE` in [project or instance metadata](https://docs.cloud.google.com/compute/docs/metadata/overview).

When OS Login is disabled, you can connect to your VMs using [SSH keys stored in metadata](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys).

### Disable OS Login for all VMs in a project

To disable OS Login for all VMs in a project, set the following value in [project metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-projectwide):

  * Key: `enable-oslogin`
  * Value: `FALSE`



### Disable OS Login for a single VM

To disable OS Login for a single VM, set the following value in [instance metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#update_metadata):

  * Key: `enable-oslogin`
  * Value: `FALSE`



Setting `enable-oslogin` to `FALSE` in instance metadata disables OS Login for the VM even if `enable-oslogin` is set to `TRUE` in project metadata.

## Connect to VMs that have OS Login enabled

Connect to VMs that have OS Login enabled by using the methods described in [Connect to Linux VMs](https://docs.cloud.google.com/compute/docs/connect/standard-ssh).

When you connect to VMs that have OS Login enabled, Compute Engine uses the [username that your organization administrator configured for you](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#modify-users). If your organization administrator hasn't configured a username for you, Compute Engine generates a username in the format of `USERNAME_DOMAIN_SUFFIX`. For more information about usernames, see [How OS Login works](https://docs.cloud.google.com/compute/docs/oslogin#how_os_login_works). 

## Enable OS Login with 2FA

For additional security, you can require users to use two-factor authentication (2FA) when connecting to VMs that have OS Login enabled. If you plan to use OS Login with two-factor authentication, users must configure 2-Step Verification on their accounts. For information about supported 2FA methods, see [About OS Login](https://docs.cloud.google.com/compute/docs/oslogin).

Before you enable 2FA, ensure that OS Login is enabled as described in Enable OS Login. To enable OS Login 2FA, set the following metadata value in instance or project metadata:

  * Key: `enable-oslogin-2fa`
  * Value: `TRUE`



For OS Login 2FA to be enforced, metadata for both OS Login (`enable-oslogin`) and OS Login 2FA (`enable-oslogin-2fa`) must be set to `TRUE`.

**Note:** When OS Login 2FA is enabled on your VM, you must have 2-step verification set up on your [Google Account](https://support.google.com/accounts/answer/185839) or [domain](https://support.google.com/a/answer/175197?&visit_id=637926366678234132-2638872723&rd=1) to connect. Otherwise, any attempts to access these VMs are denied. 2-step verification is not enforced on service account users.

When you connect to VMs that have OS Login 2FA enabled, you also see a message based on your selected 2-step verification method or challenge type. For the phone prompt method, accept the prompts on your phone or tablet to continue. For other methods, enter your security code or one-time password. 

## Troubleshoot OS Login

To find methods for diagnosing and resolving OS Login errors, see [Troubleshooting OS Login](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-os-login).

## What's next

  * Learn how [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh) work on Compute Engine.
  * Learn how to use [SSH certificates](https://docs.cloud.google.com/compute/docs/oslogin/certificates) (**Preview**) to connect to VMs.
  * Learn how to use [SSH with security keys](https://docs.cloud.google.com/compute/docs/oslogin/security-keys) (**Preview**) to further restrict access to VMs.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/workstations/docs/create-configuration/
title: Create a workstation configuration \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:22.540496+00:00
---

# Create a workstation configuration  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/create-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Create a workstation configuration Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to get started creating a workstation configuration with Cloud Workstations. 

A workstation configuration acts as a template for the creation of consistent workstations for multiple developers, and specifies configuration settings such as machine type, zones, disk size, tools, and preinstalled libraries. Any operations performed on a workstation configuration, such as changing the machine type or container image, reflect on each workstation the next time the workstation starts up.

This section explains the steps of creating a workstation configuration:

  1. Configure basics
  2. Define machine settings
  3. Customize the environment
  4. Add users
  5. Add labels and tags



* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/?journey_id=workstations--set-up--intro&walkthrough_id=workstations--set-up--configure)

* * *

## Before you begin

Before you begin using Cloud Workstations, be sure that you have the [required permissions](https://docs.cloud.google.com/workstations/docs/access-control#enable_required_roles) and that you complete these required setup steps. You can skip this section if you've already completed this setup.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud Workstations API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=workstations.googleapis.com)

  7. Make sure that you have a Cloud Workstations Admin IAM role on the project so that you can create workstation configurations. To check your IAM roles in the Google Cloud console, go to the **IAM** page:

[ Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  8. Cloud Workstations are hosted on VMs booted from Compute Engine's preconfigured public [Container-Optimized OS (COS)](https://docs.cloud.google.com/compute/docs/images/os-details#container-optimized_os_cos) images. If the `constraints/compute.trustedimageProjects` organization policy constraint is enforced, you must [set image access constraints](https://docs.cloud.google.com/compute/docs/images/restricting-image-access#trusted_images) to allow users to create boot disks from `projects/cos-cloud` or all public images. 
  9. Cloud Workstations uses Private Service Connect to connect to Google-managed services. If the `constraints/compute.restrictPrivateServiceConnectProducer` organization policy constraint is enforced in your organization, you must [add Google as an allowed producer](https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-consumers#add-org-policy) (`under:organizations/433637338589`). 
  10. If the `constraints/compute.disablePrivateServiceConnectCreationForConsumers` organization policy constraint is enforced in your organization, you must ensure that Private Service Connect endpoints connecting to Google APIs (`GOOGLE_APIS`) are [allowed](https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-consumers#connection-type). If you configure private clusters, endpoints connecting to published services (`SERVICE_PRODUCERS`) must also be allowed. 
  11. **Optional:** Enable the Container File System API to allow faster workstation startup. 

[Enable the Container File System API](https://console.cloud.google.com/apis/library/containerfilesystem.googleapis.com?q=container%20file%20system)

For more information, see [Reduce workstation startup time with Image streaming](https://docs.cloud.google.com/workstations/docs/architecture#image-streaming). 




## Configure basics

To configure the basics of a workstation configuration, follow these steps: 

  1. In the console, navigate to **Cloud Workstations** > **Workstation configurations**. 

[Go to Workstation configurations](https://console.cloud.google.com/workstations/configurations)

  2. From the **Workstation configurations** page, click add_box**Create**.

![](https://docs.cloud.google.com/static/workstations/images/console-configurations-page-create-button.png)

  3. In the **Name** field, enter `test-configuration` as the name of your configuration.

  4. In the **Region** field, select the region of the workstation cluster that you want to use for this configuration, or select the region where you want to create a cluster.

  5. From the **Clusters** list, select your workstation cluster, and then click **Continue**.

If no workstation cluster is available in the selected region, a cluster is created automatically along with your configuration. The new cluster is created with default settings, and you can adjust them by clicking **Customize cluster settings**. For more information about workstation cluster settings, see [Create a workstation cluster](https://docs.cloud.google.com/workstations/docs/create-cluster#workstation-cluster).

  6. For **Machine preset** , select one of the preconfigured options (for example, **Moderate**), or select **Custom** to customize compute and storage settings.

  7. For **Quick start workstations** , select **Enabled** for faster workstation startup or **Disabled** for lower cost.

This value specifies the number of virtual machines (VMs) kept in a pre-started state, which enables faster workstation start times. However, your project is billed for these VMs.

  8. In the **Code editors** menu, choose the Cloud Workstations **Base Editor (Code OSS for Cloud Workstations)**. If your organization prefers a different IDE, you can also choose from the list of [preconfigured IDEs](https://docs.cloud.google.com/workstations/docs/preconfigured-ides). If you don't want to use a preconfigured image, you can choose a custom image on the **Environment settings** page.

  9. Click **Continue** to progress to the **Machine configuration** page.




## Define machine settings

  1. To use a machine type other than the preset, select a **Machine type** based on your needs. For example, you might choose **e2-standard-4** (4 CPU, 16 GB memory).

  2. Select two **Zones** within the region you selected. Cloud Workstations creates VM resources and stores data in these zones.

The zone selection also affects the type of computing resources that are available. For example, if you select the N1 machine type and want to use GPUs, be sure to select two zones where the chosen GPU type is listed as available in the [GPU availability by region and zone](https://docs.cloud.google.com/workstations/docs/available-gpus#gpu_availability_by_region_and_zone) table.

  3. For **Enable quick start workstations** , choose a pool size based on the number of developers you anticipate, your use cases, and your budget. The default **Quick start pool size** is **1**.

  4. In the **Cost savings** section, set the amount of time to wait before auto-sleep. Leave the **Auto-sleep** field set to **After 2 hours of inactivity (default)** to automatically shut down workstations inactive for more than two hours.

  5. Optional: In the **Advanced options** section, click expand_moreExpand More.

     1. To add network tags, enter text in the **Network tags** field.

Network tags are metadata applied to the underlying Compute Engine VMs that allow you to make firewall rules and routes applicable to specific VM instances. In Cloud Workstations, you can use network tags to make firewall rules or routes applicable to all the workstations under a workstation configuration.

     2. To turn off public IP addresses, select the **Disable public IP addresses** checkbox.

If you disable public IP addresses, you must set up [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) or [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) on your network. If you use Private Google Access and you use `private.googleapis.com` or `restricted.googleapis.com` for Artifact Registry, make sure that you set up DNS records for [domains](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#domain-options) `*.pkg.dev`.

     3. To turn on nested virtualization, select the **Enable nested virtualization** checkbox. Nested virtualization lets you run VM instances inside your workstation.

Before enabling nested virtualization, consider the following important considerations.

Cloud Workstations instances are also subject to the [same restrictions as Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview#restrictions):

        * **Organization policy** : projects, folders, or organizations might be restricted from creating nested VMs if the **Disable VM nested virtualization** constraint is enforced in the organization policy. For more information, see the Compute Engine section, [Check whether nested virtualization is allowed](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/managing-constraint#check_whether_nested_virtualization_is_allowed).

        * **Performance** : nested VMs might experience a 10% or greater decrease in performance for workloads that are CPU-bound and possibly greater than a 10% decrease for workloads that are input or output bound.

        * **Machine Type** : nested virtualization can only be enabled on workstation configurations that specify machine types in the N1 or N2 machine series. 

     4. To encrypt your data while it is being processed on this VM, select the **Confidential VM service** checkbox. For more information, see [Create a Confidential VM instance](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/creating-cvm-instance).

     5. To set Shielded VM settings, select the corresponding feature checkbox. Shielded VM features include trusted UEFI firmware and provides options for boot, vTPM, and integrity monitoring.

     6. By default, Cloud Workstations encrypts resources created with this workstation configuration using a [Google-owned and Google-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/default-keys). To use a [customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) instead, select **Use customer-managed encryption key (CMEK)**.

  6. Click **Continue** to progress to the **Environment settings** page.




## Customize the environment

Customize the Cloud Workstations environment by configuring the workstation container image and persistent storage using these steps:

  1. Configure the container image by choosing whether to use one of the [preconfigured base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) or to provide a reference to a [customized container image](https://docs.cloud.google.com/workstations/docs/customize-container-images) that you've created.

     1. To use a [preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images):

        1. Leave the container type set to **Code editors on base images**.

        2. In the **Code editors** menu, choose the Cloud Workstations **Base Editor (Code OSS for Cloud Workstations)**. If your organization prefers a different IDE, you can also choose from the list of [preconfigured IDEs](https://docs.cloud.google.com/workstations/docs/preconfigured-ides).

        3. Optional: In the **Service account** menu, choose from the list of [service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview).

     2. Optional: To use your own [customized container image](https://docs.cloud.google.com/workstations/docs/customize-container-images) instead of one of the [preconfigured base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images):

        1. Select **Custom container image**.

        2. Specify the **Container image URL**.

        3. Click the **Service account** menu and select the service account to be used on VM instances created under workstation configuration. This service account must have permissions to pull your customized container image (or the image must be publicly accessible). For more information, see the description of `serviceAccount` in [Customize your development environment](https://docs.cloud.google.com/workstations/docs/customize-development-environment#gceinstance).

  2. In the **Storage settings** section, choose preferences for the initial home directory and for disk attributes:

     1. To create an empty home directory, select **Create a blank persistent disk**. To use a disk snapshot for the home directory, choose **Create a persistent disk from a source disk snapshot**.

     2. Set the **Disk type** of your persistent directory to **Balanced** , which has higher performance but is more economical than **SSD**.

     3. Set the **Disk size** of your persistent directory. The default is `200` GB but valid values are `10`, `50`, `100`, `200`, `500`, or `1000` GB. Choose the disk size that best fits your team's needs.

     4. Set the **Reclaim policy** to **Delete** or **Retain**. The default is **Delete**. This policy determines what happens to the persistent disk when a workstation is deleted.

**Notes** : 
        * You can't modify the disk type after creating a workstation. 
        * Choosing **Retain** allows administrators to audit the content of workstation home disks after the workstations are deleted, but administrators are responsible for manually deleting the disk. 
        * If you choose the **Retain** option and then delete your workstation, your persistent disk won't be deleted. However, if you recreate your workstation, a new disk will be attached to the workstation which won't contain the data from the deleted workstation.

To access the data on the disk, you can follow these steps:

        1. [Create a new Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
        2. [Add your persistent disk to the instance](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#create_disk).
        3. [Mount your disk on your VM](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux#mounting). 



You can also customize further by following these optional steps:

  1. Optional: Add **Readiness checks**.

If needed, specify readiness checks to verify that the workstation accepts requests at specific paths and ports when starting workstations that are associated with this workstation configuration.

  2. Optional: Expand **Advanced container options**.

If needed, specify additional parameters for the container image being used. For example, specify a working directory override, user override, command overrides, arguments to pass to the `entrypoint` command, and environment variables.

  3. Click **Continue** to progress to the **Users and permissions** page.




## Add users

To allow multiple users to create workstations, add users to your workstation configuration: 

  1. From the **Users and permissions** page, click the **Users** field and enter the email addresses of one or more users or Google groups to which you want to give access. This sets up a Cloud Workstations Creator IAM policy for these users.

  2. Optional: To add Cloud Workstations policy administrator access, expand **Advanced IAM options**.

To grant the `roles/workstations.policyAdmin` role to workstation creators, select the **Grant Policy Admin role to workstation creators** checkbox. This lets the creator of a workstation update the IAM policy of the workstation, which grants access to the workstation and its individual ports.

For more information about Cloud Workstations port sharing, see the [Grant access to individual Cloud Workstations ports](https://docs.cloud.google.com/workstations/docs/configure-port-access) page.

**Note:** By default, the creator of a workstation gets the `roles/workstations.user` role on the workstation that they create, regardless of the **Grant Policy Admin role to workstation creators** setting.

1\. Click **Continue** to progress to the **Labels and tags** page. 

## Add labels and tags

  1. From the **Labels and tags** page, configure labels and tags:

     1. Optional: Add **Labels** to apply key-value pair labels to the underlying Compute Engine resources.
  2. To create your workstation configuration, click **Create**.

If you chose to create a new cluster, the creation process can take up to 20 minutes.




You've just created your first workstation configuration and added users to it.

To create and launch a workstation based on this configuration, click **Next**.

## Clean up

If you created a new workstation configuration to learn about Cloud Workstations and you no longer need the configuration, you can delete it from the Google Cloud console:

  1. In the Google Cloud console, go to **Cloud Workstations > Workstation configurations**.
  2. Select the checkbox beside the workstation configuration that you want to delete.
  3. Click themore_vert**More** options menu and select **Delete** to delete the selected workstation configuration. 

For more about deleting workstations, workstation clusters, and Google Cloud projects, see [Delete resources](https://docs.cloud.google.com/workstations/docs/delete-resources). 

## What's next

  * [Create a workstation](https://docs.cloud.google.com/workstations/docs/create-workstation) using your newly created workstation configuration.

  * Use the [Cloud Workstations base editor](https://docs.cloud.google.com/workstations/docs/base-editor-overview).

  * Customize your [workstation configuration](https://docs.cloud.google.com/workstations/docs/customize-development-environment) through the API.

  * Create [customized container images](https://docs.cloud.google.com/workstations/docs/customize-container-images) that extend the [preconfigured base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) provided by Cloud Workstations.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

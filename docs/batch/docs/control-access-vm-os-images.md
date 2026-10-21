---
url: https://docs.cloud.google.com/batch/docs/control-access-vm-os-images/
title: Control access to VM OS images for Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:29:24.479034+00:00
---

# Control access to VM OS images for Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/control-access-vm-os-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Control access to VM OS images for Batch Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure the trusted image policy constraint. This lets you control access to the operating system (OS) images that can be used to create the boot disks for any Compute Engine virtual machine (VM) instances.

By default, a user can use any public image or any custom image that is shared with them for the Compute Engine VMs that run their Batch jobs. If the trusted image policy constraint is not enabled and you don't want to restrict VM OS images, you can stop reading this document.

Enable the trusted image policy constraint if you want to require all the users in a project, folder, or organization to create VMs that contain approved software that meets your policy or security requirements. If the trusted image policy constraint is enabled, affected users [can't run Batch jobs](https://docs.cloud.google.com/batch/docs/troubleshooting#constraint-violated-trusted-images) unless the VM OS image for their job is allowed. To create and run jobs when the trusted image policy constraint is enabled, do at least one of the following:

  * Have users [specify a VM OS image](https://docs.cloud.google.com/batch/docs/specify-vm-os-image) that is already allowed.
  * Allow the default VM OS images from Batch, as shown in this document.



To learn more about VM OS images and boot disks, see [VM OS environment overview](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview). To learn about which policy constraints have been enabled for your project, folder, or organization, [view your organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to configure organization policies, ask your administrator to grant you the [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Allow images from Batch

The following steps describe how to modify the trusted image policy constraint to allow all VM OS images from Batch by using the Google Cloud console or Google Cloud CLI.

For more instructions on how to use the trusted image (`compute.trustedImageProjects`) policy constraint, see [Setting up trusted image policies](https://docs.cloud.google.com/compute/docs/images/restricting-image-access) in the Compute Engine documentation.

###  Console 

  1. Go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies/)

  2. From the policies list, click **Define trusted image projects**.

The **Policy details** page opens.

  3. On the **Policy details** page, click edit **Manage Policy**. The **Edit policy** page opens.

  4. On the **Edit policy** page, select **Customize**.

  5. For **Policy enforcement** , select an enforcement option.

  6. Click **Add rule**.

  7. In the **Policy values** list, you can select whether to add a rule that allows access to all unspecified image projects, denies access to all unspecified image projects, or specifies a custom set of projects to allow or deny access to. To allow all images from Batch, do the following:

     1. In the **Policy values** list, select **Custom**. A **Policy type** and **Custom values** field appears.
     2. In the **Policy type** list, select **Allow**.
     3. In the **Custom values** field, enter `projects/batch-custom-image`.
  8. To save the rule, click **Done**.

  9. To save and apply the organization policy, click **Save**.




###  gcloud 

The following example describes how to allow images from Batch for a specific project:

  1. To get the existing policy settings for a project, run the [`resource-manager org-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/describe):
         
         gcloud resource-manager org-policies describe \
            compute.trustedImageProjects --project=PROJECT_ID \
            --effective > policy.yaml
         

Replace PROJECT_ID with the project ID of the project that you want to update.

  2. Open the `policy.yaml` file in a text editor. Then, modify the `compute.trustedImageProjects` constraint by adding `projects/batch-custom-image` to the `allowedValues` field. For example, to allow only VM OS images from Batch set the `compute.trustedImageProjects` constraint to the following:
         
         constraint: constraints/compute.trustedImageProjects
         listPolicy:
          allowedValues:
             - projects//batch-custom-image
         

When you have finished editing the `policy.yaml` file, save your changes.

  3. To apply the `policy.yaml` file to your project, use the [`resource-manager org-policies set-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy):
         
         gcloud resource-manager org-policies set-policy \
            policy.yaml --project=PROJECT_ID
         

Replace PROJECT_ID with the project ID of the project that you want to update.




When you finish updating constraints, testing those constraints is recommended to verify that they are working as intended.

## What's next

  * Create and run jobs, such as the following: 
    * [Create and run a basic job](https://docs.cloud.google.com/batch/docs/create-run-basic-job), which uses a VM OS image from Batch by default.
    * [Create and run a job that uses a specific VM OS image](https://docs.cloud.google.com/batch/docs/specify-vm-os-image).
  * Learn more about [VM OS images and boot disks](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

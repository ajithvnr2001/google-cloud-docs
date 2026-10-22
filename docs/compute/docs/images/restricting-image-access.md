---
url: https://docs.cloud.google.com/compute/docs/images/restricting-image-access/
title: Setting up trusted image policies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:02.412044+00:00
---

# Setting up trusted image policies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/restricting-image-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Setting up trusted image policies Stay organized with collections  Save and categorize content based on your preferences. 

By default, users in your project can create persistent disks or copy images using any of the [public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support) and any images that [principals can access through IAM roles](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects). However, in some situations you might want to restrict principals so that they can create boot disks only from images that contain approved software that meets your policy or security requirements.

Use the Trusted image feature to define an organization policy that allows principals to create persistent disks only from images in specific projects.

To restrict the locations where your images can be used, read [restricting use of your shared images, disks, and snapshots](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects#restrict).

## Before you begin

  * Read the [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints) page to learn about managing policies at organization level.
  * Read the [Understanding hierarchy evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy) page to learn how organization policies propagate.
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




## Limitations

  * Trusted image policies do not restrict access to the following images:

    * [Custom images](https://docs.cloud.google.com/compute/docs/images#custom_images) in your local project.

    * Image files in Cloud Storage buckets.

  * Trusted image policies do not prevent users from creating image resources in their local projects.




## Set image access constraints

Enact an image access policy by setting a `compute.trustedImageProjects` constraint on your project, your folder, or your organization. You must have permission to modify organization policies to set these constraints. For example, [`roles/orgpolicy.policyAdmin`](https://docs.cloud.google.com/resource-manager/docs/access-control-org) has permission to set these constraints. For more information about managing policies at the project, folder, or organization level, see [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints).

You can set constraints on all public images available on Compute Engine. For a list of image project names, see [Operating systems details](https://docs.cloud.google.com/compute/docs/images/os-details). You can also restrict the Machine Learning (ML) images that are available on Compute Engine by using the `ml-images` project. If you are using [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#errors), grant your project permission to use Compute Engine VM images from the `serverless-vpc-access-images` project.

Use the Google Cloud console or Google Cloud CLI to set constraints on image access.

###  Console 

For example, to set a constraint at the project level, do the following:

  1. Go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies/)

  2. From the policies list, click **Define trusted image projects**. The **Policy details** page displays.

  3. On the **Policy details** page, click **Manage Policy**. The **Edit policy** page displays.

  4. On the **Edit policy** page, select **Customize**.

  5. For **Policy enforcement** , select an enforcement option. For information about inheritance and the resource hierarchy, see [Understanding Hierarchy Evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy).

  6. Click **Add rule**.

  7. In the **Policy values** list, you can select whether this organization policy should allow access to all image projects, deny access to all image projects, or you can specify a custom set of projects to allow or deny access to.

To set the policy rule, complete one of the following options:

     * To allow users to create boot disks from all public images, select **Allow All**.
     * To restrict users from creating boot disk from all public images, select **Deny All**.
     * To specify a select set of public images that users can create boot disks from, select **Custom**. A **Policy type** and **Custom values** field displays.

       1. In the **Policy type** list, select **Allow** or **Deny**.
       2. In the **Custom values** field, enter the name of the image project using the `projects/IMAGE_PROJECT` format.

Replace `IMAGE_PROJECT` with the image project you want to set the constraint on.

You can add multiple image projects. For each image project that you want to add, click **Add** and enter the image project name.

  8. To save the rule, click **Done**.

  9. To save and apply the organization policy, click **Save**.




For more information about creating organization policies, see [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

###  gcloud 

For example, to set a constraint at the project level, do the following:

  1. Get the existing policy settings for your project by using the [`resource-manager org-policies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/describe) command.
         
         gcloud resource-manager org-policies describe \
            compute.trustedImageProjects --project=PROJECT_ID \
            --effective > policy.yaml
         

Replace PROJECT_ID with your project ID.

  2. Open the `policy.yaml` file in a text editor and modify the `compute.trustedImageProjects` constraint. Add the restrictions that you need and remove the restrictions that you no longer require. When you have finished editing the file, save your changes. For example, you might set the following constraint entry in your policy file:
         
         constraint: constraints/compute.trustedImageProjects
         listPolicy:
          allowedValues:
             - projects/debian-cloud
             - projects/cos-cloud
          deniedValues:
             - projects/IMAGE_PROJECT
         

Replace IMAGE_PROJECT with the name of the image project that you want to restrict in your project.

Optionally, you might want to deny access to all images outside of the custom images in your project. For that situation, use the following example: 
         
         constraint: constraints/compute.trustedImageProjects
         listPolicy:
          allValues: DENY
         

  3. Apply the `policy.yaml` file to your project. If your [organization or folder has existing constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-policies), those constraints might conflict with project-level constraints that you set. To apply the constraint, use the [`resource-manager org-policies set-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy) command.
         
         gcloud resource-manager org-policies set-policy \
            policy.yaml --project=PROJECT_ID
         

Replace PROJECT_ID with your project ID.




When you have finished configuring the constraints, test those constraints to ensure that they create the restrictions that you need.

## What's next

  * Learn more about the [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).
  * See what [public images](https://docs.cloud.google.com/compute/docs/images) are available for you to use by default.
  * [Share your private image](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects) with other projects.
  * Learn how to [restrict use of your shared images, disks, and snapshots](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects#restrict).
  * Learn how to [start an instance from an image](https://docs.cloud.google.com/compute/docs/instances/creating-and-starting-an-instance#startinginstancwithimage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

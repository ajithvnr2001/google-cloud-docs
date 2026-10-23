---
url: https://docs.cloud.google.com/organization-policy/quickstart/
title: Quickstart: Enforce an organization policy \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:59.769775+00:00
---

# Quickstart: Enforce an organization policy  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Guides ](https://docs.cloud.google.com/organization-policy/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enforce an organization policy

This guide describes how to set an [organization policy](https://docs.cloud.google.com/organization-policy/overview) that includes the [resource locations](https://docs.cloud.google.com/organization-policy/restrict-locations) constraint, and how to test that constraint after it is applied in the [Google Cloud console](https://console.cloud.google.com/).

## Before you begin

### Required roles

To get the permissions that you need to restrict where Compute Engine disks can be created, ask your administrator to grant you the following IAM roles: 

  * To set an organization policy: [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) on your organization 
  * To create a Compute Engine disk: [Compute Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.storageAdmin) (`roles/compute.storageAdmin`) on your project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable the APIs

Enable the Compute Engine and Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,cloudresourcemanager.googleapis.com&redirect=https%3A//console.cloud.google.com)

## Create a project

  1. Ensure that you have the Project Creator IAM role (`roles/resourcemanager.projectCreator`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  2. In the Google Cloud console, go to the project selector page.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Click **Create project**.

  4. Name your project. Make a note of your generated project ID.

  5. Edit the other fields as needed.

  6. Click **Create**.




## Create a Compute Engine disk

To test the functionality of the resource locations constraint, set up a Compute Engine regional persistent disk. When you create a regional persistent disk, you must specify the location where it will reside. For more information about creating Compute Engine regional persistent disks, see [Create and manage regional disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk).

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Select the project that you created.

     1. If you are prompted to link a billing account to your project, do so now. For more information about enabling billing, see [Enable billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project).
  3. Click **Create disk**.

  4. Specify a **Name** for your disk.

  5. For the **Location** , choose **Regional**.

  6. For the **Region** , select `europe-north1 (Finland)`.

  7. For the **Zone** , select `europe-north1-a`.

  8. Select the **Replica zone** in the same region.

  9. Click **Create**.




When the disk is successfully created, a green check mark appears next to the name.

## Set the organization policy

To set an organization policy on the project that you created:

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. Click **Select**.

  3. Select the project that you created.

  4. Click **Google Cloud Platform - Resource Location Restriction** , and then click **Manage policy**.

  5. Under **Policy source** , select **Override parent's policy**.

  6. Under **Policy enforcement** , select **Replace**.

  7. Click **Add rule**.

  8. Under **Policy values** , select **Custom**.

  9. Under **Policy type** , select **Allow**.

  10. In the **Custom values** box, enter `in:asia-locations`.

  11. Click **Done** , and then click **Set policy**. A notification appears to confirm the policy update.




`asia-locations` is a [value group](https://docs.cloud.google.com/organization-policy/restrict-locations#value_groups) that is curated by Google to include every location in a particular geographic region. In this case, every region in Asia is defined as an allowed location for any resources created after this point. Note that the regional persistent disk you created is not affected by this new policy, because the policy is not retroactive.

## Testing the organization policy

Now that the organization policy is in effect, you cannot create resources in regions that were not specified as part of the organization policy. To test this, try to create a regional persistent disk in an invalid location:

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Select the project that you created.

  3. Click **Create Disk**.

  4. Specify a **Name** for your disk.

  5. For the **Location** , choose **Regional**.

  6. For the **Region** , select `europe-north1 (Finland)`.

  7. For the **Zone** , select `europe-north1-a`.

  8. Select the **Replica zone** in the same region.

  9. Click **Create**.




A red exclamation point appears next to the name, and an error notification displays:
    
    
    Location ZONE:europe-north1-a violates constraint
    constraints/gcp.resourceLocations on the resource RESOURCE_ID
    

Where RESOURCE_ID is the full resource path of your project and disk. The disk is not created.

## Create regional persistent disk in valid location

The organization policy constraint blocks the creation of resources unless you specify a valid location:

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Select the project that you created.

  3. Click **Create Disk**.

  4. Specify a **Name** for your disk.

  5. For the **Location** , choose **Regional**.

  6. For the **Region** , select `asia-east2 (Hong Kong)`.

  7. For the **Zone** , select `asia-east2-a`.

  8. Select the **Replica zone** in the same region.

  9. Click **Create**.




The resource is created successfully because all zones under `asia-east2` are within the `asia-locations` value group.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete regional persistent disks

Delete the regional persistent disks you created for this quickstart:

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. In the list that appears, select both of the disks that you created.

  3. Click **Delete**.

  4. In the confirmation dialog that appears, click **Delete**.




A notification dialog appears to confirm the disks were deleted.

### Delete the project

Delete the project that you created for this quickstart:

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to Manage resources](https://console.cloud.google.com/cloud-resource-manager)

  2. In the list of resources that appears, select the project that you created, then click **Delete**.

  3. On the **Shut down project** dialog that appears, enter the project ID, and then click **Shut down anyway**.




## What's next

  * Learn how to [Apply organization policies](https://docs.cloud.google.com/organization-policy/apply-policies).
  * Review the [services that support the resource locations constraint](https://docs.cloud.google.com/organization-policy/reference/restrict-locations-supported-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

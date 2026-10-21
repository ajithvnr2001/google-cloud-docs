---
url: https://docs.cloud.google.com/build/docs/securing-builds/configure-access-to-resources/
title: Configuring access to Cloud Build resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:01.579116+00:00
---

# Configuring access to Cloud Build resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/securing-builds/configure-access-to-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Configuring access to Cloud Build resources Stay organized with collections  Save and categorize content based on your preferences. 

By default, only the creator of a Google Cloud project has access to the project and its resources. To grant other users access, you can grant Identity and Access Management (IAM) roles on the project, or on a specific Cloud Build resource.

This page describes the ways you can set access control for your Cloud Build resources.

## Before you begin

  * Understand the [basic concepts of IAM](https://docs.cloud.google.com/iam/docs/overview).
  * Learn about the [Cloud Build roles and permissions](https://docs.cloud.google.com/build/docs/iam-roles-permissions).



## Granting roles on the project

###  Console 

  1. Open the IAM page in the Google Cloud console:

[Open the IAM page](https://console.cloud.google.com/iam-admin/roles)

  2. Select your project, and click **Continue**.

  3. Click **Grant access**.

  4. Enter the user's or service account's email address.

  5. Select the desired role from the drop-down menu. Cloud Build roles are under **Cloud Build**.

  6. Click **Save**.


**Note:** If you do not see the Cloud Build roles in the drop-down menu, you may need to [enable the Cloud Build API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com&_ga=1.128224844.1904271179.1489680703).

###  gcloud 

To grant a role to a principal, run the `add-iam-policy-binding` command:
    
    
    gcloud group add-iam-policy-binding resource \
        --member=principal --role=role-id
    

Where:

  * group: The gcloud CLI group for the resource you want to update. For example, you can use projects or organizations.

  * resource: The name of the resource.

  * principal: An identifier for the principal, which usually has the following form: principal-type:id. For example, user:my-user@example.com. For a full list of principal, or member, types, see the [Policy Binding reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy#Binding).

  * role-id: The name of the role.




For example, to grant the Cloud Build Viewer role to the user `my-user@example.com` for the project `my-project`:
    
    
    gcloud projects add-iam-policy-binding my-project \
        --member=user:my-user@example.com --role=roles/cloudbuild.builds.viewer
    

## Granting permissions to run gcloud commands

To run [`gcloud builds`](https://docs.cloud.google.com/sdk/gcloud/reference/builds) commands, users with only `cloudbuild.builds.viewer` or `cloudbuild.builds.editor` roles also require the `serviceusage.services.use` permission. To give this permission to the user, grant them the `serviceusage.serviceUsageConsumer` role.

User with roles/editor and roles/owner roles can run [`gcloud builds`](https://docs.cloud.google.com/sdk/gcloud/reference/builds) commands without the additional `serviceusage.services.use` permission.

## Permissions to view build logs

To view build logs, you require additional permissions depending on whether you're storing your build logs in the default Cloud Storage bucket or in a user-specified Cloud Storage bucket. For more information on permissions required to view build logs, see [Viewing build logs](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs#viewing_build_logs).

## Revoking roles on the project

###  Console 

  1. Open the IAM page in the Google Cloud console:

[Open the IAM page](https://console.cloud.google.com/iam-admin/roles)

  2. Select your project, and click **Continue**.

  3. In the permissions table, locate the email ID of the principal and click on the pencil icon.

  4. Delete the role that you want to revoke.

  5. Click **Save**.




###  gcloud 

To revoke a role from a user, run the `remove-iam-policy-binding` command:
    
    
    gcloud group remove-iam-policy-binding resource \
        --member=principal --role=role-id
    

Where:

  * group: The gcloud CLI group for the resource you want to update. For example, you can use projects or organizations.

  * resource: The name of the resource.

  * principal: An identifier for the principal, which usually has the following form: principal-type:id. For example, user:my-user@example.com. For a full list of principal, or member, types, see the [Policy Binding reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy#Binding).

  * role-id: The name of the role.




For example, to revoke the Cloud Build Viewer role from the user `my-user@example.com` for the project `my-project`:
    
    
    gcloud projects remove-iam-policy-binding my-project \
        --member=user:my-user@example.com --role=roles/cloudbuild.builds.viewer
    

## Viewing roles on the project

###  Console 

  1. Open the IAM page in the Google Cloud console:

[Open the IAM page](https://console.cloud.google.com/iam-admin/roles)

  2. Select your project, and click **Continue**.

  3. Under **View by** , click **Roles**.

  4. To view the principals with a particular role, expand the role name.




###  gcloud 

To view all users that are granted a particular role in a Google Cloud project, run the following command:
    
    
    gcloud projects get-iam-policy project-id \
        --flatten="bindings[].members" \
        --format="table(bindings.members)" \
        --filter="bindings.role:role-id"
    

Where:

  * project-id is your project ID.

  * role-id is the name of the role for which you want to view the principals.




For example, to view all principals in a project that are granted the Google Cloud project Viewer role, run the following command:
    
    
    gcloud projects get-iam-policy my-project \
        --flatten="bindings[].members" \
        --format="table(bindings.members)" \
        --filter="bindings.role:roles/cloudbuild.builds.viewer"
    

## Creating IAM custom roles

For users that want to define their own roles containing bundles of permissions that they specify, IAM offers custom roles. For instructions on creating and using IAM custom roles, see [Creating and Managing Custom Roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

**Note:** You must include the `serviceusage.services.use` permission in each Cloud Build custom role you create.

## What's next

  * Learn about [Default Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account).
  * Learn how to [configure access to Cloud Build service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account).
  * Learn about [the permissions required to view build logs](https://docs.cloud.google.com/build/docs/securing-builds/store-view-build-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

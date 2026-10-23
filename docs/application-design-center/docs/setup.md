---
url: https://docs.cloud.google.com/application-design-center/docs/setup/
title: Set up Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:56.488500+00:00
---

# Set up Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Application Design Center

This document guides administrators through the initial setup for Application Design Center, which lets you design, share, and manage cloud infrastructure using an application-centric model. The setup process configures the following:

  * Application management, which lets you define the [boundary](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-mgmt-boundary) for your application and manage its lifecycle.
  * An initial space where your team can collaborate.
  * A default catalog to store templates.
  * A Google-managed catalog with templates based on best practices.
  * One of the following Cloud Storage buckets for Terraform storage: 
    * A new storage bucket that is automatically created.
    * Your own existing storage bucket.



## Before you begin

### Choose a storage bucket option

When you create templates and applications, App Design Center stores Terraform code in a Cloud Storage bucket. Choose one of the following storage bucket options:

  * _Automatically create a new bucket_ : Perform the setup in the console.
  * _Use an existing storage bucket_ : Complete the setup using the App Design Center API.



You might use your own bucket if you have organization policies that prevent you from creating new buckets, or if you have established business practices that dictate bucket creation.

#### Verify existing storage bucket access

To complete the setup and use your own bucket, verify the following:

  1. You have access to use APIs. For more information, see [Set up API access](https://docs.cloud.google.com/docs/get-started/access-apis).

  2. Your bucket is in the same management project where you want to set up App Design Center.

  3. You have the following [permissions](https://docs.cloud.google.com/storage/docs/access-control/iam-permissions) on the bucket:

     * `storage.buckets.get`
     * `storage.objects.create`



### Choose your application management boundary

An [application management boundary](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-mgmt-boundary) is a centralized place for application management tasks, including API enablement, access control, billing, and quotas. Within the boundary, you can monitor, troubleshoot, optimize costs, and manage your Google Cloud resources in the context of your application.

Choose the boundary model that fits your organization:

  * _Single-project boundary_ ([Preview](https://docs.cloud.google.com/products#product-launch-stages)): Best for new users or small organizations where all resources reside in one project.
  * _Folder-level boundary_ : Best for large organizations that manage resources across multiple projects and subfolders.



The following table compares the features of each boundary model:

Feature | Single-project boundary ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) | Folder-level boundary  
---|---|---  
Flexibility | Complete the setup using default settings. | 

  * Specify a name for your space.
  * Select whether to disable Google-provided templates.
  * Post-setup, you can create additional spaces in the application management boundary.

  
Integrated products | 

  * App Design Center
  * [App Hub](https://docs.cloud.google.com/app-hub/docs/overview)
  * [Application Monitoring](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring)

| 

  * App Design Center
  * [App Hub](https://docs.cloud.google.com/app-hub/docs/overview)
  * [Cloud Hub](https://docs.cloud.google.com/hub/docs/overview)
  * [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview)
  * [Application Monitoring](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring)

  
  
### Enable application management

When you enable application management, the system does one of the following to help you manage quotas and billing for your application:

  * _Single-project_ ([Preview](https://docs.cloud.google.com/products#product-launch-stages)): The system configures your project as a [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project).
  * _Folder-level_ : The system creates a new management project in the folder.



To enable application management, do the following:

### Single-project (Preview)

  1. Make sure that your project has a [linked billing account](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  2. Make sure that you have the required roles to enable application management and complete the setup, which creates your space.

  3. Application management is automatically enabled on your project when you complete the setup using the console. Alternatively, to perform the setup using the App Design Center API, [enable application management](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-single-project#set-up) on your project.




### Folder-level

  1. Make sure that you have an [organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization).

  2. Make sure that you have the [required roles](https://docs.cloud.google.com/resource-manager/docs/manage-applications#roles) to enable application management.

  3. [Configure a folder for application management](https://docs.cloud.google.com/resource-manager/docs/manage-applications#configure-folder-app-management).

  4. [Link a billing account to the management project](https://docs.cloud.google.com/resource-manager/docs/manage-applications#billing).

  5. [Configure the observability scope](https://docs.cloud.google.com/resource-manager/docs/manage-applications#configure-observability-scope) for the management project.

  6. Make sure that you have the required roles to complete the setup and create your space.




### Verify required IAM roles

To perform the setup, ask your administrator to grant you the necessary roles on your project or [boundary](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-mgmt-boundary) folder, as listed in the following table:

Task | Required roles  
---|---  
Perform single-project initial setup | Project Owner (`roles/owner`), or both of the following:  
Application Design Center Admin (`roles/designcenter.admin`) and  
Service Usage Admin (`roles/serviceusage.serviceUsageAdmin`)  
Perform folder-level initial setup | Both of the following:  
Application Design Center Admin (`roles/designcenter.admin`) and  
Application Admin (`roles/designcenter.applicationAdmin`)  
  
For more information about roles, see [Access control with IAM](https://docs.cloud.google.com/application-design-center/docs/access-control).

## Set up App Design Center and create a new storage bucket

The setup process in the console creates a new Cloud Storage bucket to store application information. To use an existing bucket, see Set up App Design Center and use your own storage bucket.

### Single-project (Preview)

To enable application management on a single project and set up App Design Center, do the following:

  1. Go to the **Application Design Center Overview** page.

[Go to Overview](https://console.cloud.google.com/products/design-center/overview)

  2. From the project picker, select the project where you want to configure application management.

  3. Click **Go to Setup**.

  4. In the **Setup your project for application management** pane, review the list of APIs that will be enabled.

  5. Click **Enable**. The system enables the APIs, and creates the storage bucket and **default-space** space.

  6. To store the Google Cloud resources that you deploy with App Design Center, create standard projects in your organization.




### Folder-level

To set up App Design Center on your [app-enabled folder](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-enabled-folder), do the following:

  1. Go to the **Application Design Center Overview** page.

[Go to Overview](https://console.cloud.google.com/products/design-center/overview)

  2. Click **Select folder** and select your app-enabled folder.

  3. Click **Set up ADC**.

  4. In the **My space name** field, enter a name for your space. You can't edit this name later.

  5. By default, the space contains [components](https://docs.cloud.google.com/application-design-center/docs/supported-resources) and [application templates](https://docs.cloud.google.com/application-design-center/docs/build-on-google-templates) that are created by Google. To remove Google components and application templates from the space, clear the **Enable Google opinionated templates** checkbox.

If you remove Google opinionated templates, space users can only use the [components that you import](https://docs.cloud.google.com/application-design-center/docs/import-components) and the [application templates that you create](https://docs.cloud.google.com/application-design-center/docs/design-application-templates).

  6. Click **Complete setup**. The system enables the APIs, and creates the storage bucket and space.

  7. To store the Google Cloud resources that you deploy with App Design Center, create standard projects in your [app-enabled folder](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-enabled-folder).




## Set up App Design Center and use your own storage bucket

When you set up App Design Center, you can use your own Cloud Storage bucket to store Terraform code. For example, you might use an existing bucket if your organization policies prevent you from creating new buckets.

To set up Application Design Center and use your own Cloud Storage bucket, you must use the App Design Center API. Do the following:

  1. Identify the bucket name.

  2. Create your API call using the [`projects.locations.spaces`](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces) resource. The API request path takes the format `projects/<var>PROJECT_ID</var>/locations/<var>LOCATION</var>`, where `<var>PROJECT_ID</var>` is one of the following:

     * For a single-project [boundary](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-mgmt-boundary), use your project ID.
     * For a folder-level boundary, use the ID of the management project that you created during the application management setup.

Perform the following configuration in your API call:

     1. Specify your bucket name in the `gcs_bucket` field. For example, if the bucket URI is `gs://my-bucket`, the bucket name is `my-bucket`.

     2. Use the [`projects.locations.spaces.create`](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/create) method to create the space.

Running this method creates your space, sets your bucket as the storage location for application information, enables the required APIs, and completes the setup process.




## What's next

  * Deploy your first application from a Google template by following [Quickstart: Customize and deploy a Google template](https://docs.cloud.google.com/application-design-center/docs/quickstart-deploy-google-template).
  * Manage team permissions by [providing access to space users](https://docs.cloud.google.com/application-design-center/docs/manage-spaces#manage_space_users).
  * Share templates by [creating additional spaces](https://docs.cloud.google.com/application-design-center/docs/manage-spaces#create-spaces-share-catalogs).
  * Review core concepts and benefits with the [App Design Center overview](https://docs.cloud.google.com/application-design-center/docs/overview).
  * Publish templates by [managing template catalogs](https://docs.cloud.google.com/application-design-center/docs/manage-catalogs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

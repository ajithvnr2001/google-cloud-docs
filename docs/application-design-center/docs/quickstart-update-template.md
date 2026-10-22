---
url: https://docs.cloud.google.com/application-design-center/docs/quickstart-update-template/
title: Quickstart: Update an application template and redeploy \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:43.817319+00:00
---

# Quickstart: Update an application template and redeploy  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/quickstart-update-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update an application template and redeploy

This quickstart helps you modify the [three-tier web application](https://docs.cloud.google.com/application-design-center/docs/quickstart-create-template) by connecting a Memorystore for Redis component. You update an existing template and redeploy the application to verify your change. This application update helps you cache data and improve performance.

![A three-tier web application in the design canvas with a Memorystore for Redis
component. The application includes frontend, backend, database, and cache
components.](https://docs.cloud.google.com/static/application-design-center/images/three-tier-application-cache.png)

You update the template by doing one of the following:

  * Add and connect a component on the design canvas in Application Design Center.
  * Use natural language prompts in Gemini Cloud Assist.



The changes you make are reflected in the application's Terraform code, which you can review before you deploy. For more information, see [Overview of Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform/terraform-overview).

After you update the template, deploy your application to verify your changes.

## Before you begin

Complete the [Create and verify a template](https://docs.cloud.google.com/application-design-center/docs/quickstart-create-template) quickstart.

## Add a component to the template

Use the App Design Center design canvas or Gemini Cloud Assist to modify your template.

### Design canvas

  1. In the Google Cloud console, go to the **Templates** page.

[Go to Templates](https://console.cloud.google.com/products/design-center/templates)

  2. Click the **quickstart-three-tier-web-app** template.

  3. In the design canvas, from the **cloud-run-2** component, click add **Add** and select **Memorystore for Redis**.




###  Gemini Cloud Assist

  1. In the Google Cloud console, go to the **Templates** page.

[Go to Templates](https://console.cloud.google.com/products/design-center/templates)

  2. Click the **quickstart-three-tier-web-app** template.

  3. In the Google Cloud console toolbar, click spark **Open or close Gemini Cloud Assist chat**.

The **Cloud Assist** panel opens.

  4. In Gemini Cloud Assist chat, enter the following prompt:
         
         Update this template to include a backend cache.
         

  5. In the design canvas, review the updated design and click **Accept suggestion**.




Your template now contains four components. Lines are displayed between components to represent connections.

## Update the application draft

  1. From the design canvas, click **Configure an app**.

  2. Click **Quickstart three-tier test**.

  3. Click **Save**.




The application draft is updated with the new template.

## Configure the new component

  1. In the design canvas, click **memorystore-1** and do the following in the **Configuration** area:

     1. From the **Project ID** list, select the deployment project you created in [Create and verify a template](https://docs.cloud.google.com/application-design-center/docs/quickstart-create-template).

     2. From the **Zone** list, select `us-central1-a`.

     3. In the **Name** field, enter `cache-redis`.

     4. Click **Save**.




Green check marks are displayed in each component to convey that you have specified the required parameters. The application draft is ready to be redeployed to the TEST environment for verification.

## Redeploy the application

  1. Click **Deploy**.

  2. In the **Select a service account** area, do the following:

     1. Click **Create a new service account**.

     2. Click **Proceed**.

  3. To review the Terraform plan for your application, do the following:

     1. Click **Preview**. A Terraform plan is generated after a few minutes.

     2. Review the Terraform plan for your application.

     3. Click **Copy and close**.

     4. Paste the copied Terraform in a document.

  4. Click **Deploy**.




The application is deployed after a few minutes and resources are created in your project. The following details are displayed:

  * A link to App Hub, where you can view deployed resource details, including links to monitoring dashboards.
  * Links to Cloud Build logs, which you can use to troubleshoot deployment errors.
  * Outputs like service URIs are displayed, which you can use to interact with deployed resources.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the deployed application

  1. From the navigation menu, click **Applications**.

[Go to Applications](https://console.cloud.google.com/products/design-center/applications)

  2. From the table, click **Quickstart three-tier web app**.

  3. Click more_vert **Actions** and select **Delete Application**.

  4. In the **Delete** field, enter `Quickstart three-tier web app`.

  5. Click **Delete**.




The application is deleted, including the following:

  * The application details are removed from Application Design Center.
  * The underlying App Hub application is deleted.
  * The underlying resources are deleted.



### Optional: Delete the project

To delete the deployment project you created in the [Create and verify a template](https://docs.cloud.google.com/application-design-center/docs/quickstart-create-template) quickstart, do the following:

**Caution:** If you delete a project, all resources in the project are permanently deleted.

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. At the prompt, type the project ID, and then click **Shut down**. 



## What's next

  * Review core concepts and benefits with the [App Design Center overview](https://docs.cloud.google.com/application-design-center/docs/overview).
  * Learn how to duplicate and customize a Google-provided template in [Quickstart: Customize and deploy a Google template](https://docs.cloud.google.com/application-design-center/docs/quickstart-deploy-google-template).
  * Define your own configurations by [designing application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

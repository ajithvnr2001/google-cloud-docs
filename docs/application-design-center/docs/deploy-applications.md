---
url: https://docs.cloud.google.com/application-design-center/docs/deploy-applications/
title: Deploy applications \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:34.048822+00:00
---

# Deploy applications  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/deploy-applications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Deploy applications Stay organized with collections  Save and categorize content based on your preferences. 

After you create an application draft from a template, you can deploy the application. When you deploy an application using App Design Center, your application is automatically registered in App Hub. The deployment process lets you do the following:

  * Preview changes that Terraform plans to make to your infrastructure.
  * Enable Google Cloud resource APIs that are required for your application.
  * Investigate deployment issues.
  * Assess your design against organization policies.
  * Use telemetry data to analyze resource performance.
  * Identify and apply template revisions to your application.



This document helps you deploy, manage, and apply a template revision to your application.

## Before you begin

To perform the tasks in this document, ask your administrator to grant you the necessary roles on the [app-enabled folder](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-enabled-folder) or [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project), as listed in the following table:

Task | Required roles  
---|---  
Deploy an application and apply template revisions | Application Admin (`roles/designcenter.applicationAdmin`), or  
Application Operator (`roles/designcenter.applicationOperator`)  
Automatically create a service account during deployment | Project IAM Admin (`roles/resourcemanager.projectIamAdmin`)  
  
To deploy the application using an existing service account, see [Grant roles to your service account](https://docs.cloud.google.com/application-design-center/docs/grant-roles-service-account).

For more information about roles, see [Access control with IAM](https://docs.cloud.google.com/application-design-center/docs/access-control).

## Deploy your application

Select a service account option and deploy your application. When you deploy an application, Google Cloud resources are created, and you begin to incur charges associated with those resources.

### Design canvas

  1. From the navigation menu, click **Applications**.

[Go to Applications](https://console.cloud.google.com/products/design-center/applications)

  2. From the table, click the **Application name**.

  3. From the **Application details** page, review the details and click **Edit** to make changes.

**Note:** If you plan to deploy and later delete this application, deploy to the `TEST`, `DEVELOPMENT`, or `STAGING` **Environment**.
  4. Click **Deploy**.

  5. Select one of the following service accounts to deploy your application:

     * **Select a service account** : In the **Service account** field, enter the name of an existing service account. To configure the service account, see [Grant roles to your service account](https://docs.cloud.google.com/application-design-center/docs/grant-roles-service-account).

     * **Create a new service account** : You must have the [Project IAM Admin](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) role, which is used to assign the required deployment roles to the service account.

  6. Click **Proceed**.

  7. To preview the changes that Terraform plans to make to your infrastructure, do the following:

     1. Click **Preview**.

     2. Review the changes and click **Copy and close**. The preview is copied to your clipboard.

     3. To save the preview, paste and save in a document of your choice. 

  8. In the **Review APIs** area, review the list of APIs that are required for your application. The APIs are automatically enabled when you deploy.

  9. Click **Deploy**. The application details and deployment status are displayed as the deployment completes.

  10. If there are issues with your deployment, do the following:

     1. In the **Application details** panel, click **Deployments**.

     2. Review the error messages.

     3. Click **View logs** to view detailed build information.

     4. To view suggestions to fix deployment errors, click **Troubleshoot Deployment** ([Preview](https://cloud.google.com/products#product-launch-stages)).

For more information, see Troubleshoot and fix deployment issues.

**Tip:** To view a list of applications with deployment issues in Cloud Hub, see [View deployments](https://docs.cloud.google.com/hub/docs/deployments).
  11. To manage your deployed application, see View application details.




###  gcloud CLI 

  1. Preview the application to view the Terraform code before you deploy. This operation might require several minutes to complete. Do one of the following:

     * To automatically create a service account, use the following command:
           
           gcloud design-center spaces applications preview APPLICATION \
           --project=PROJECT \
           --location=LOCATION \
           --space=SPACE \
           --create-sa \
           --service-account=SERVICE_ACCOUNT
           

     * To use your own service account, use the following command:
           
           gcloud design-center spaces applications preview APPLICATION \
           --project=PROJECT \
           --location=LOCATION \
           --space=SPACE \
           --service-account=SERVICE_ACCOUNT
           

Replace the following:

     * `APPLICATION`: The application ID.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application region.
     * `SPACE`: Your space ID.
     * `SERVICE_ACCOUNT`: Do one of the following: 
       * To create a new service account, provide a name for the service account. 
       * To use your own service account, provide the full resource name in the format `projects/PROJECT/serviceAccounts/EMAIL_ADDRESS`.

For more information, see [gcloud design-center spaces applications preview](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/preview).

  2. Deploy the application asynchronously and copy the full operation name. Do one of the following:

**Note:** To update an existing application, add the `--replace` flag to the following deploy commands.
     * To automatically create a service account, use the following command:
           
           gcloud design-center spaces applications deploy APPLICATION \
            --project=PROJECT \
            --location=LOCATION \
            --space=SPACE \
            --create-sa \
            --service-account=SERVICE_ACCOUNT \
            --async
           

     * To use your own service account, use the following command:
           
           gcloud design-center spaces applications deploy APPLICATION \
            --project=PROJECT \
            --location=LOCATION \
            --space=SPACE \
            --service-account=SERVICE_ACCOUNT \
            --async
           

Replace the following:

     * `APPLICATION`: The application ID.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application region.
     * `SPACE`: Your space ID.
     * `SERVICE_ACCOUNT`: Do one of the following: 
       * To create a new service account, provide a name for the service account. 
       * To use your own service account, provide the full resource name in the format `projects/PROJECT/serviceAccounts/EMAIL_ADDRESS`.

For more information, see [gcloud design-center spaces applications deploy](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/deploy).

  3. The deployment requires a few minutes to complete. Track the deployment status.
         
         gcloud design-center operations describe OPERATION\
         --project=PROJECT \
         --location=LOCATION
         

Replace the following:

     * `OPERATION`: The full operation name copied from the `deploy` command output in the format `projects/PROJECT/locations/LOCATION/operations/operation-<var>OPERATION_ID</var>`.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application region.

For more information, see [gcloud design-center operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/operations/describe).




## Troubleshoot and fix deployment issues

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If your application deployment fails, you can view a summary of errors, get a detailed analysis, identify steps to resolve, and automatically fix some issues.

To troubleshoot and fix errors, do the following:

  1. In the **Application details** panel, click **Deployments**.

  2. To analyze errors and suggest fixes, click **Troubleshoot Deployment**.

The **Troubleshooting details** panel displays documentation suggestions, configuration changes, and other information that can help you resolve deployment errors.

  3. Review the deployment errors and recommendations:

     1. If the analysis results in component configurations recommendations, review the suggested changes and click **Update Application** to apply the changes.

     2. If the analysis results in other recommendations, the system displays gcloud CLI commands you can execute to resolve the errors. To run the gcloud CLI commands in Cloud Shell, click **Run command**.




## View application details

When your application deployment finishes, you can examine its related information. For example, you might view the following:

  * Details such as last update time, revision date, and region.
  * Outputs such as service URI.
  * Deployment status, error information, and links to logs.



To view application details, do the following:

### Design canvas

  1. From the navigation menu, click **Applications**.

[Go to Applications](https://console.cloud.google.com/products/design-center/applications)

  2. From the table, click the **Application name**. The **Application details** panel displays the following:

     * **View app in App Hub** : Investigate your application in App Hub. You can view deployed resources and examine telemetry data to diagnose issues and analyze performance. For more information, see [Monitor App Hub applications](https://docs.cloud.google.com/app-hub/docs/monitor-applications).

     * **App Details** : View information like the last updated date, source template, region, and service account.

     * **Outputs** : Identify service URIs, which you can use to interact with your application frontend or backend.

     * **Deployments** : Examine the deployment status, deployment errors, and links to logs to troubleshoot errors.




###  gcloud CLI 
    
    
    gcloud design-center spaces applications describe APPLICATION \
    --project=PROJECT \
    --location=LOCATION \
    --space=SPACE
    

Replace the following:

  * `APPLICATION`: The application ID.
  * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
  * `LOCATION`: The application region.
  * `SPACE`: Your space ID.



For more information, see [gcloud design-center spaces applications describe](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/describe).

## Modify deployed applications

If you want to modify a deployed application, do one of the following to make sure that your changes are retained when you redeploy the application:

  * [Revise the template](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#revise_and_reshare_your_template) and then Apply the template revision
  * [Revise the application](https://docs.cloud.google.com/application-design-center/docs/manage-applications#create-application-revision)



### Apply template revisions

If your application was previously deployed using App Design Center, and an administrator has shared a template revision with you, you can apply the template changes to your application. When you update your application, an application revision is created. You can configure components that were modified or added to the revised template.

You can view available template revisions for your applications using Cloud Hub. For more information, see [View deployments](https://docs.cloud.google.com/hub/docs/deployments).

To apply template revisions to your application, do the following:

**Caution:** If you modified an application's components outside of App Design Center, those changes are not retained when you redeploy. To retain changes, see Modify deployed applications.

### Design canvas

  1. From the navigation menu, click **Templates**.

[Go to Templates](https://console.cloud.google.com/products/design-center/templates)

  2. Click the **Template ID** that contains the revision you want to apply.

  3. From the **Configure an app** list, select the application that you want to update.

  4. Edit the application details and click **Save**.

  5. Click each component in the design canvas, and modify component configurations.

  6. Click **Deploy**. For deployment steps, see Deploy your application.




###  gcloud CLI 

  1. Identify the application template revision URI for the latest revision.
         
         gcloud design-center spaces application-templates describe APPLICATION_TEMPLATE \
          --project=PROJECT \
          --location=LOCATION \
          --space=SPACE \
          --format='yaml(name,latestRevision)'
         

Replace the following:

     * `APPLICATION_TEMPLATE`: The application template ID that is the basis of your application.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application template region.
     * `SPACE`: Your space ID.

For more information, see [gcloud design-center spaces application-templates describe](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/describe).

  2. Copy the `latestRevision` output.

  3. Update the application to use the application template revision.
         
         gcloud design-center spaces applications update APPLICATION \
          --project=PROJECT \
          --location=LOCATION \
          --space=SPACE \
          --source-application-template-revision=SOURCE_APPLICATION_TEMPLATE_REVISION
         

Replace the following:

     * `APPLICATION`: The application ID.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application region.
     * `SPACE`: Your space ID.
     * `SOURCE_APPLICATION_TEMPLATE_REVISION`: Your application template URI. For example, `projects/PROJECT/locations/LOCATION/spaces/SPACE/applicationTemplates/APPLICATION_TEMPLATE/revisions/REVISION`

For more information, see [gcloud design-center spaces applications update](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/update).

  4. To configure new or updated components in the application, see [Configure components and connections](https://docs.cloud.google.com/application-design-center/docs/manage-applications#configure-components-connections).

  5. When you deploy the application, use the `--replace` flag. For deployment steps, see Deploy your application.




## What's next

  * Track your workloads by [monitoring application health and performance](https://docs.cloud.google.com/application-design-center/docs/monitor-applications).
  * Get started with preconfigured architectures by [building on Google templates](https://docs.cloud.google.com/application-design-center/docs/build-on-google-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

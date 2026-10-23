---
url: https://docs.cloud.google.com/application-design-center/docs/manage-applications/
title: Manage applications \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:38.757128+00:00
---

# Manage applications  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/manage-applications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Manage applications Stay organized with collections  Save and categorize content based on your preferences. 

Create an application when you want to customize and deploy from a template. For example, you might create an application that you plan to deploy for testing purposes. You might create another application for production use.

When you create an application, you specify information that helps you categorize it based on the application's intended usage. This information helps you filter and find a specific application. You can also configure components and connection details.

This document shows you how to manage the lifecycle of an application. You'll learn how to create an application draft from a template, configure its components, edit its underlying Terraform code, create a new revision, and finally, delete the application when it's no longer needed.

## Before you begin

To perform the tasks in this document, ask your administrator to grant you the necessary roles on the [app-enabled folder](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-enabled-folder) or [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project), as listed in the following table:

Task | Required roles  
---|---  
Create, configure, edit, and version application drafts | Application Design Center Admin (`roles/designcenter.admin`), or  
Application Admin (`roles/designcenter.applicationAdmin`), or  
Application Editor (`roles/designcenter.applicationEditor`)  
Delete an application | Application Design Center Admin (`roles/designcenter.admin`), or  
Application Admin (`roles/designcenter.applicationAdmin`)  
  
For more information about roles, see [Access control with IAM](https://docs.cloud.google.com/application-design-center/docs/access-control).

## Create an application draft

Create an application draft from a template by specifying details and optionally overriding component configurations. You can then deploy the draft to create an application.

### Design canvas

  1. From the navigation menu, do one of the following:

     * To view templates created in your space, click **Templates**.

[Go to Templates](https://console.cloud.google.com/products/design-center/templates)

     * To view templates shared from another space, click **Shared templates**.

[Go to Shared templates](https://console.cloud.google.com/products/design-center/shared-catalog)

  2. Click the **Template ID** that you want to use.

  3. From the design canvas, click **Configure an app**. Then click **Create new application**.

  4. In the **Application name area** , do the following to name and describe your application:

     1. In the **Name** field, enter a unique identifier in this space. For example, use a unique name and environment combination like `web-app-staging`. This is a required field.

You can use up to 63 characters, including lowercase letters, numbers, and hyphens. The name must start with a lowercase letter and can't end with a hyphen. Names can't be changed.

     2. In the **Display name** field, enter a name to display in the Google Cloud console.

     3. In the **Description** field, enter the purpose of this application.

  5. To set a default project for any components with an empty **Project ID** field, select a project from the **Deployment project** list. In a folder-level boundary, the project must have the following qualifications:

     * The project must be inside the selected [app-enabled folder](https://docs.cloud.google.com/resource-manager/docs/manage-applications#configure-folder-app-management).
     * The project must not be a [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project).

If a component already has a project specified in its **Project ID** field, that project is used instead of this setting.

  6. From the **Region** list, select the region where components are deployed. The component region is applied based on the following:

     * If the application scope is **Global** (default), the region is applied to components that don't already have a configured region.

     * If the application scope is **Regional** , the region is applied to all components.

  7. From the **Environment** list, select the environment where you want to deploy this application. For example, you might want to verify that your deployment works as expected in `TEST`.

**Note:** If you plan to deploy and later delete this application, deploy to `TEST`, `DEVELOPMENT`, or `STAGING`.
  8. From the **Criticality** list, select the degree of impact on your business. For example, `LOW` or `HIGH`.

  9. To specify owners, in the **Owners** area, click **Add owner** and enter a **Display name** and **email** for the following:

     * In the **Business owners** area, enter an owner who is responsible for quality and user expectations.

     * In the **Developer owners** area, enter an owner who is responsible for development and coding.

     * In the **Operator owners** area, enter an owner who is responsible for operating the application.

  10. From the **Scope** list, select one of the following:

     * **Global** (default): The application contains a global resource, or resources are in multiple regions.

     * **Regional** : All resources are in a single region.

This is a required field. For more information, see [Compare global and regional applications](https://docs.cloud.google.com/app-hub/docs/global-regional-applications#compare-global-regional).

  11. Click **Create Application**. The application details are displayed.




###  gcloud CLI 

  1. Identify the application template revision URI for the template that you want to use to create the application.
         
         gcloud design-center spaces application-templates describe APPLICATION_TEMPLATE \
          --project=PROJECT \
          --location=LOCATION \
          --space=SPACE \
          --format='yaml(name,latestRevision)'
         

Replace the following:

     * `APPLICATION_TEMPLATE`: The template ID for the application template that you want to use as the basis for your application.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application template region.
     * `SPACE`: Your space ID.

For more information, see [gcloud design-center spaces application-templates describe](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/describe).

  2. Copy the `latestRevision` output. 

  3. Create an application draft based on your template.
         
         gcloud design-center spaces applications create APPLICATION \
           --project=PROJECT \
           --location=LOCATION \
           --space=SPACE \
           --source-application-template-revision=SOURCE_APPLICATION_TEMPLATE_REVISION \
           --scope-type=SCOPE_TYPE
         

Replace the following:

     * `APPLICATION`: The application ID for the application draft that you want to create.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application region.
     * `SPACE`: Your space ID.
     * `SOURCE_APPLICATION_TEMPLATE_REVISION`: Your application template URI. For example, `projects/PROJECT/locations/LOCATION/spaces/SPACE/applicationTemplates/APPLICATION_TEMPLATE/revisions/REVISION`
     * `SCOPE_TYPE`: The scope for your application. One of `regional` or `global`. If the application scope is 'global`, the region is applied to components that don't already have a configured region. If the application scope is`regional`, the region is applied to all components.

For more information, see [gcloud design-center spaces applications create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/create).




### Configure components and connections

For each component in the application, you can specify configuration details such as the project where the resource is created, and the location where it's deployed.

You can also modify connection details if the default configuration doesn't meet your requirements. For example, you might modify environment variable key names, change connection ports, or add additional roles to service accounts.

You must configure the required details for each [supported resource](https://docs.cloud.google.com/application-design-center/docs/supported-resources).

To configure components and connections, do the following:

### Design canvas

  1. From the design canvas, click a component.

  2. In the **Configuration** area, from the **Project ID** list, select the project where you want to deploy the resource. Select a project with the following qualifications:

     * The project must be inside the selected [app-enabled folder](https://docs.cloud.google.com/resource-manager/docs/manage-applications#configure-folder-app-management).

     * The project must not be a [management project](https://docs.cloud.google.com/resource-manager/docs/manage-applications#management-project).

  3. Configure additional settings for the resource. For example, for Cloud SQL, you might configure the following:

     * Region
     * Backup configuration
     * Database flags
     * IP configuration

For links to configuration documentation for each component, see [Supported resources](https://docs.cloud.google.com/application-design-center/docs/supported-resources).

  4. When you connect components on the design canvas, default configuration values are used to create the connection. To add or modify connection details, do the following.

     1. In the design canvas, click the connection between two components. The **Connection** panel opens and displays connection parameters.

     2. Do one of the following:

        * To modify an existing connection parameter, click **Edit**.

        * To add a new connection parameter, click **Add parameter**.

     3. Update the **Key** and **Value** fields. For example, you might want to modify the following details:

        * The environment variable key names to align with your application requirements.
        * The connection port value.
        * The roles added to a service account.
  5. Click **Save**.




###  gcloud CLI 

  1. Describe the application to view component parameters, and identify required parameters for your application.
         
         gcloud design-center spaces applications describe APPLICATION \
          --project=PROJECT \
          --location=LOCATION \
          --space=SPACE \
          --format='yaml(name,componentParameters)'
         

Replace the following:

     * `APPLICATION`: The application ID.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application region.
     * `SPACE`: Your space ID.

For more information, see [gcloud design-center spaces applications describe](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/describe).

  2. For each component that you want to modify, in your home directory, create a JSON file that contains parameter values.

For example, you might create the following file for a Cloud Run component:
         
         {
             "component": "projects/PROJECT/locations/us-central1/spaces/SPACE/applicationTemplates/APPLICATION_TEMPLATE/components/COMPONENT",
             "parameters": [
                {
                   "key": "service_name",
                   "value": "frontend-service"
                },
                {
                   "key": "project_id",
                   "value": "DEPLOYMENT_PROJECT"
                }
             ]
           }
         

  3. Update the application to configure the required parameters.
         
         gcloud design-center spaces applications update APPLICATION \
          --project=PROJECT \
          --location=LOCATION \
          --space=SPACE \
          --component-parameters=COMPONENT_FILE_PATH_1
         

Replace the following:

     * `APPLICATION`: The application ID.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application region.
     * `SPACE`: Your space ID.
     * `COMPONENT_FILE_PATH_1`: A JSON file that includes component parameters. For each additional JSON file, add another `--component-parameter` argument and value.

For more information, see [gcloud design-center spaces applications update](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/update).




For deployment steps, see [Deploy applications](https://docs.cloud.google.com/application-design-center/docs/deploy-applications).

### Verify security compliance

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can perform a security assessment of your application to validate your configuration against [Security Command Center frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework). This comprehensive assessment evaluates the following:

  * **Component configuration values** : The configuration settings that were automatically inherited from the template, or settings that you modified for this application.
  * **Application parameters** : The instance-specific details provided for your application, such as the deployment region or environment.
  * **Allowed components** : The services and workloads in the current application that are allowed for use by your organization.



Applications inherit [Security Command Center frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework) from their template. First, your administrator must [attach a security framework to your application template](https://docs.cloud.google.com/application-design-center/docs/enforce-security-policies). Then, do the following to assess security compliance from your application:

###  gcloud CLI 
    
    
      gcloud alpha design-center spaces applications preview APPLICATION \
      --project=PROJECT \
      --location=LOCATION \
      --space=SPACE \
      --generate-assessment-report=true
    

Replace the following:

  * `APPLICATION`: The application ID for the application that you want to assess.
  * `PROJECT`: Your management project ID.
  * `LOCATION`: The application region.
  * `SPACE`: Your space ID.



The output displays an assessment report for your application based on the template's attached frameworks.

## Edit Terraform code

Your application generates Terraform code to reflect design and configuration details. You can edit the Terraform to specify component configuration details.

The system generates the following Terraform files:

  * `main.tf`: Infrastructure code that includes a module for each component in the template.
  * `outputs.tf`: Exposes information about infrastructure components that are deployed.
  * `variables.tf`: Declares name, type, and description for variables used in the `main.tf` file.
  * `input.tfvars`: Defines values for variables used in the `main.tf` file.
  * [`providers.tf`](https://docs.cloud.google.com/docs/terraform/terraform-overview#providers): Defines labels that help Terraform interact with Google Cloud APIs and resources.



For background information, see [Overview of Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform/terraform-overview).

To edit the Terraform code, do the following:

  1. From the design canvas, click **Code**. The system displays the generated Terraform files.

  2. Click **main.tf**. The system displays the Terraform module for each component.

  3. Edit configuration details. For more information, see the configuration documentation for each [supported resource](https://docs.cloud.google.com/application-design-center/docs/supported-resources).

The system automatically validates your edits, and displays errors if your edits are invalid.

  4. To highlight and compare your edits, do the following:

     1. Click **View diff**.

     2. To revert a change, in the margin, click **Click to revert change**.

     3. Click **View diff** to close the comparison view.

  5. To save your edits, click **Save code changes**.

  6. To verify your changes, do the following.

     1. Click **Design**.
     2. Click a component and review its configuration details.



## Create an application revision

Create an application revision to modify details or components. If you modify application components outside of App Design Center, those changes are not retained when you redeploy.

To create an application revision:

### Design canvas

  1. From the navigation menu, click **Applications**.

[Go to Applications](https://console.cloud.google.com/products/design-center/applications)

  2. From the table, click the **Application name** that you want to revise.

  3. To modify application details, do the following:

  4. Click **Edit** and modify the details.

  5. Click **Save** to save your changes.

  6. To modify a component in this application, do the following:

     1. Click the component in the design canvas and edit the details in the **Configuration** area.

     2. Click **Save** to save your changes.




###  gcloud CLI 

See Configure components and connections.

For deployment steps, see [Deploy applications](https://docs.cloud.google.com/application-design-center/docs/deploy-applications).

## Delete an application

If you no longer need an application, you can delete it. For example, you might deploy an application to verify your template in the `TEST` environment, and then delete the application.

You can delete the following applications:

  * An application that has not been deployed. On the **Applications** page, the **Status** is listed as **Draft**.
  * An application that was deployed to the `TEST`, `DEVELOPMENT`, or `STAGING` **Environment**.



When you delete an application, the following occurs:

  * The application details are removed from Application Design Center.
  * The underlying App Hub application is deleted.
  * If you deployed, resources are deleted.



To delete an application:

### Design canvas

  1. From the navigation menu, click **Applications**.

[Go to Applications](https://console.cloud.google.com/products/design-center/applications)

  2. From the table, click the **Application name**.

  3. Click more_vert **Actions** and select **Delete Application**.

  4. In the **Delete** field, enter the application name.

  5. Click **Delete**.




###  gcloud CLI 

Delete an application.
    
    
        gcloud design-center spaces applications delete APPLICATION \
        --project=PROJECT \
        --location=LOCATION \
        --space=SPACE
    

Replace the following:

  * `APPLICATION`: The application ID for the application that you want to delete.
  * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
  * `LOCATION`: The application region.
  * `SPACE`: Your space ID.

For more information, see [gcloud design-center spaces applications delete](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/delete).




## What's next

  * Provision your infrastructure with the console or the command line by [deploying applications](https://docs.cloud.google.com/application-design-center/docs/deploy-applications).
  * Export Terraform configurations to your local machine or repository by [downloading and deploying Terraform](https://docs.cloud.google.com/application-design-center/docs/download-and-deploy). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/application-design-center/docs/design-composite-templates/
title: Design composite templates \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:33.173686+00:00
---

# Design composite templates  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/design-composite-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Design composite templates Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When you want to build complex applications from smaller, reusable building blocks, create composite templates. For example, you might create a composite template that includes several connected application templates.

You can also create composite templates to model and package units of deployment for a SaaS offering that you deploy with App Lifecycle Manager. For more information, see [Model and package units of deployment](https://docs.cloud.google.com/saas-runtime/docs/model-saas-offering).

Design composite templates by adding and connecting standard application templates and individual components. This modular approach lets you do the following:

  * _Accelerate development_ : Assemble complex apps from smaller building blocks. You can reuse each standard application template in multiple composite templates.
  * _Enable parallel development_ : Enable modular teams to specialize in specific building blocks. For example, a database team can address data storage and analysis with minimal reliance on the application logic team.
  * _Reduce vulnerability impacts_ : Developers can update or fix a building block without redeploying the entire application.
  * _Improve security posture_ : Restrict access by creating distinct service accounts to deploy each building block. Ensure that each team only has permissions for the building blocks that they configure.



This document shows you how to design, verify, and share a composite template.

## Before you begin

To perform the tasks in this document, ask your administrator to grant you the necessary roles on the [app-enabled folder](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-enabled-folder) or [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project), as listed in the following table:

Task | Required roles  
---|---  
Create, design, and edit composite templates | Application Design Center Admin (`roles/designcenter.admin`), or  
Application Design Center User (`roles/designcenter.user`)  
Publish or share composite templates to a catalog | Application Design Center Admin (`roles/designcenter.admin`)  
  
For more information about roles, see [Access control with IAM](https://docs.cloud.google.com/application-design-center/docs/access-control).

To use your own standard application templates as building blocks, set input and output variables to establish configurable variables, and create connections between your application templates. For details, see the following:

  * [Design standard application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates)
  * [Share a template to a catalog](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#share-template-to-catalog)



## Create a composite application template

Create composite templates when you want to design and share complex applications. You can add and connect the following in your template design:

  * _Standard application templates_ : Select from the following existing templates:

    * [Templates designed by Google](https://docs.cloud.google.com/application-design-center/docs/build-on-google-templates), incorporating Google Cloud best practices and default security configurations.
    * Templates that you [previously created](https://docs.cloud.google.com/application-design-center/docs/design-application-templates) and added to your space's catalog.
  * _Components_ : Select from the following Google Cloud resources:

    * [Components designed by Google](https://docs.cloud.google.com/application-design-center/docs/supported-resources), incorporating Google Cloud best practices and default security configurations.
    * Your own [components that you import](https://docs.cloud.google.com/application-design-center/docs/import-components), based on your own Terraform modules.



### Specify template details

Template details help you categorize your template and help developers decide whether to use your template.

To enter details for your template, do the following:

### Design canvas

  1. From the navigation menu, click **Templates**.

[Go to Templates](https://console.cloud.google.com/products/design-center/templates)

  2. From the **Region** list, select the location for the template. If you plan to create a scaled deployment in App Lifecycle Manager, select **global**.

  3. From the **Create Template** list, select **Composite template**.

  4. The **Template ID** field is automatically populated. Alternatively, enter a unique identifier for the template. This field is required.

  5. In the **Template Name** field, enter a human-readable identifier to display in the Google Cloud console.

If you don't provide a name, the Template ID is copied to this field.

  6. In the **Description** field, enter a brief explanation of the application's purpose.

  7. Click **Create template**. The design canvas is displayed.




###  gcloud CLI 

Create a new composite application template.
    
    
    gcloud design-center spaces application-templates create APPLICATION_TEMPLATE \
    --project=PROJECT \
    --location=LOCATION \
    --space=SPACE \
    --display-name=DISPLAY_NAME \
    --description=DESCRIPTION \
    --composition-type=COMPOSITE
    

Replace the following:

  * `APPLICATION_TEMPLATE`: The template ID for the application template that you want to create.
  * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
  * `LOCATION`: The application template region. If you plan to create a scaled deployment in App Lifecycle Manager, use **global**.
  * `SPACE`: Your space ID.
  * `DISPLAY_NAME`: A name to display in the Google Cloud console.
  * `DESCRIPTION`: A brief description.



For more information, see [gcloud design-center spaces application-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/create).

### Design your template

Design your composite template by adding and connecting standard application templates and components to the following starting points:

  * A blank canvas.
  * A [Google-provided template](https://docs.cloud.google.com/application-design-center/docs/build-on-google-templates).
  * A template that you generate with [Gemini assistance](https://docs.cloud.google.com/cloud-assist/design-application).



As you design your template, App Design Center generates Terraform code to reflect the design and configuration details.

To design your template, do the following:

### Design canvas

  1. From the design canvas, select **Design** to view the canvas.

  2. Do one of the following to get started:

     * To start from a Google-provided template, in the **Get Started** area on the canvas, click the template name.

     * To start from a blank canvas, continue to the next step.

  3. To add a standard application template to the canvas, do the following:

     1. In the **Components** area, click **Embed templates**.

     2. To add an existing template, click a template in one of the following lists:

        * **Templates** : standard application templates that are in your space's catalog, or have been shared with your space.
        * **Google templates** : standard application templates created by Google and added to the Google catalog.
     3. To add the selected template to the canvas, click **Select**.

  4. To create a new standard application template, click **Create a new template**. The **Create new template** page opens.

For more information, see [Design standard application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates).

  5. To add a component to the canvas, from the **Components** area, click a component.

  6. To create a communication channel between templates and components, do one of the following:

     * Drag from a blue dot on one building block to a blue dot on another building block.

     * To add a connected component to an existing component, click add **Add** and select the component to add.

For connection details, see the configuration documentation for each [supported resource](https://docs.cloud.google.com/application-design-center/docs/supported-resources).

  7. To remove a building block or connection, do the following:

     1. In the canvas, click the building block or connection.

     2. In the **Configuration** area, click **Delete**.

     3. In the field, enter **delete**.

     4. Click **Delete**.




###  gcloud CLI 

  1. Identify the template revision URIs for the building blocks in your space's catalog.
         
         gcloud design-center spaces shared-templates list \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE
         

Replace the following:

     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application template region.
     * `SPACE`: Your space ID.

For more information, see [gcloud design-center spaces shared-templates list](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/shared-templates/list).

  2. Identify the template revision URIs for the Google catalog building blocks that you want to add to the template.
         
         gcloud design-center spaces shared-templates list \
         --google-catalog \
         --location=us-central1
         

For more information, see [gcloud design-center spaces shared-templates list](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/shared-templates/list).

  3. Add a standard application template or component to your composite template.
         
         gcloud design-center spaces application-templates components create COMPONENT \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE \
         --application-template=APPLICATION_TEMPLATE \
         --shared-template-revision-uri=SHARED_TEMPLATE_URI
         

Replace the following:

     * `COMPONENT`: The ID for the standard application template or component that you want to add to the template.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application template region.
     * `SPACE`: Your space ID.
     * `APPLICATION_TEMPLATE`: The template ID for the composite application template where you're adding the standard application template or component.
     * `SHARED_TEMPLATE_URI`: The standard application template or component shared template URI. For example, `projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1`.

For more information, see [gcloud design-center spaces application-templates components create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/create).

  4. Add a second standard application template or component to your template.
         
         gcloud design-center spaces application-templates components create COMPONENT_2 \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE \
         --application-template=APPLICATION_TEMPLATE \
         --shared-template-revision-uri=SHARED_TEMPLATE_URI_2
         

Replace the following:

     * `COMPONENT_2`: The ID for the second standard application template or component that you want to add to the template.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application template region.
     * `SPACE`: Your space ID.
     * `APPLICATION_TEMPLATE`: The template ID for the composite template where you're adding the standard application template or component.
     * `SHARED_TEMPLATE_URI_2`: The second standard application template or component shared template URI. For example, `projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1`.

For more information, see [gcloud design-center spaces application-templates components create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/create).

  5. Create a connection between the standard application templates or components.
         
         gcloud design-center spaces application-templates components connections create CONNECTION \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE \
         --application-template=APPLICATION_TEMPLATE \
         --component=COMPONENT \
         --destination-component-uri=COMPONENT_2
         

Replace the following:

     * `CONNECTION`: The connection ID for the connection that you want to add to the template.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application template region.
     * `SPACE`: Your space ID.
     * `APPLICATION_TEMPLATE`: The template ID for the application template where you're adding the connection.
     * `COMPONENT`: The source standard application template or component ID.
     * `COMPONENT_2`: The destination standard application template or component ID.

For more information, see [gcloud design-center spaces application-templates components connections create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/connections/create).




### Configure default values for components

For each component you add to a template, you can specify default configuration details, such as the resource's project and deployment location. Application Design Center applies these defaults when an application is created from this template.

Application developers can also modify connection details if the default configuration doesn't meet their requirements. For example, you might modify environment variable key names, change connection ports, or add additional roles to service accounts when you create an application.

Before developers deploy an application, they can view and modify the default values you configured in the template. Developers must configure the required details for each [supported resource](https://docs.cloud.google.com/application-design-center/docs/supported-resources).

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

  1. Describe each component in the application template to view component parameters.
         
         gcloud design-center spaces application-templates components describe COMPONENT \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE \
         --application-template=APPLICATION_TEMPLATE
         

Replace the following:

     * `COMPONENT`: The component ID for the component that you want to describe.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application template region.
     * `SPACE`: Your space ID.
     * `APPLICATION_TEMPLATE`: The template ID for the application template.

For more information, see [gcloud design-center spaces application-templates components describe](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/describe).

  2. For each component you want to modify, create a JSON file in your home directory containing the parameter values.

For example, you might create the following file for a Cloud Run component:
         
         [
               {
                 "key": "service_name",
                 "value": "frontend-service"
               },
               {
                 "key": "project_id",
                 "value": "DEPLOYMENT_PROJECT"
               }
           ]
         

  3. Update each component in the application template to configure the required parameters.
         
         gcloud design-center spaces application-templates components update COMPONENT \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE \
         --parameters=PARAMETERS_FILE_PATH \
         --application-template=APPLICATION_TEMPLATE
         

Replace the following:

     * `COMPONENT`: The component ID for the component that you want to update.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application template region.
     * `SPACE`: Your space ID.
     * `PARAMETERS_FILE_PATH`: A JSON file that includes component parameters.
     * `APPLICATION_TEMPLATE`: The template ID for the application template.

For more information, see [gcloud design-center spaces application-templates components update](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/update).

  4. Describe the component connections.
         
         gcloud design-center spaces application-templates components connections describe CONNECTION \
         --component=COMPONENT \
         --application-template=APPLICATION_TEMPLATE \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE
         

Replace the following:

     * `CONNECTION`: The connection ID.
     * `COMPONENT`: The component ID.
     * `APPLICATION_TEMPLATE`: The template ID.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application template region.
     * `SPACE`: Your space ID.

For more information, see [gcloud design-center spaces application-templates components connections describe](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/connections/describe).

  5. Edit component connection parameters.
         
         gcloud design-center spaces application-templates components connections update CONNECTION \
         --component=COMPONENT \
         --application-template=APPLICATION_TEMPLATE \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE \
         --source-component-parameters='[{"key": SOURCE_KEY, "value": SOURCE_VALUE}]'
         

Replace the following:

     * `CONNECTION`: The connection ID.
     * `COMPONENT`: The component ID.
     * `APPLICATION_TEMPLATE`: The template ID.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application template region.
     * `SPACE`: Your space ID.
     * `SOURCE_KEY`: The new parameter key.
     * `SOURCE_VALUE`: The new parameter value.

For more information, see [gcloud design-center spaces application-templates components connections update](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/connections/update).




### Configure standard application templates

When developers deploy your composite template as an application, an application is created for each of the following:

  * Each group of standard application templates.
  * Each group of components. 



You can provide default values for each group. For example, you might include the deployment project, region, and owners. When developers deploy the application in App Design Center, they can use the default values, or specify their own details for each application.

To provide default application details for each group, do the following:

### Design canvas

  1. From the design canvas, click a standard application template.

The **Embedded Template** panel opens.

  2. In the **Configuration** area, enter the application details.

For more information, see [Create an application draft](https://docs.cloud.google.com/application-design-center/docs/manage-applications#create_an_application_draft).




###  gcloud CLI 

For more information, see [Design your template](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#design-template).

## Verify your template

Before you share your composite template with developers, deploy and verify your template in App Design Center. This step helps you verify functionality before a scaled deployment on multiple machines.

To verify your template, do the following:

  1. From the design canvas, click **Continue** and select **Create application to deploy**.

The **Create an application** panel opens.

  2. In the **Composite application details** area, enter the application details.

For more information, see [Create an application draft](https://docs.cloud.google.com/application-design-center/docs/manage-applications#create_an_application_draft).

  3. Click **Next**.

  4. For each building block you added to the composite template, an application will be created when you deploy. Configure each application and click **Next**.

For more information, see [Create an application draft](https://docs.cloud.google.com/application-design-center/docs/manage-applications#create_an_application_draft).

  5. Test your deployed application to make sure that it meets your requirements.

  6. To avoid recurring costs, delete the test deployment.




## Create a scaled deployment

To deploy and manage multiple instances of your composite template, use App Lifecycle Manager.

  1. Verify your template in App Design Center.

  2. From the design canvas, click **Continue** and select **Deploy at scale with App Lifecycle Manager**.

The **App Lifecycle Manager Units** page opens.

  3. For steps to deploy, see [Deploy a SaaS offering](https://docs.cloud.google.com/saas-runtime/docs/deploy-saas-offering).




## Share your template

To make your template available to developers, you can add it to a catalog and share. When you add a template to a catalog the template is available as an application source in spaces where the catalog is shared.

To share the template, do the following:

  1. From the design canvas, click **Add to Catalog**.

  2. To manage spaces where the catalog is shared, see [Manage catalogs](https://docs.cloud.google.com/application-design-center/docs/manage-catalogs).




## Revise and reshare your template

As you gain experience with your application and your business needs evolve, you might want to update your template. For example, you might decide to improve performance for a backend service by adding a Memorystore service for caching.

When you modify a template, you create a template revision. To apply your changes to existing applications, developers must deploy applications using the revision.

App Design Center doesn't automatically publish template revisions to catalogs. To share the latest revision, publish the template to the catalog again.

To create a new revision, do the following:

  1. From the navigation menu, click **Templates**.

[Go to Templates](https://console.cloud.google.com/products/design-center/templates)

  2. Select the application template that you want to revise. The canvas opens.

  3. Modify the template to fit your new requirements. For example, add and configure a new component.

  4. To share the latest revision with other spaces, add the template to your catalog again. 




## Delete a template

If you no longer need a template, you can delete it.

### Design canvas

  1. From the design canvas, click more_vert **Actions**.
  2. Click **Delete**.



###  gcloud CLI 

Delete an application template.
    
    
    ```sh
    gcloud design-center spaces application-templates delete APPLICATION_TEMPLATE \
    --project=PROJECT \
    --location=LOCATION \
    --space=SPACE
    ```
    

Replace the following:

  * `APPLICATION_TEMPLATE`: The template ID for the application template that you want to delete.
  * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
  * `LOCATION`: The application template region.
  * `SPACE`: Your space ID.



For more information, see [gcloud design-center spaces application-templates delete](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/delete).

## What's next

  * Deploy your composite template with App Lifecycle Manager by [deploying a SaaS offering](https://docs.cloud.google.com/saas-runtime/docs/deploy-saas-offering).
  * Share your templates with other spaces by [managing template catalogs](https://docs.cloud.google.com/application-design-center/docs/manage-catalogs).
  * Use your own Terraform modules in your template designs by [importing components](https://docs.cloud.google.com/application-design-center/docs/import-components).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

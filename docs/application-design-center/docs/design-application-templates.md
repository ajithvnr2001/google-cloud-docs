---
url: https://docs.cloud.google.com/application-design-center/docs/design-application-templates/
title: Design standard application templates \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:56.774733+00:00
---

# Design standard application templates  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/design-application-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Design standard application templates Stay organized with collections  Save and categorize content based on your preferences. 

Administrators create standard application templates to help ensure that their preferred architecture is used by each development team. This lets you govern the resources and configurations that developers use in their application deployments. Once you create a standard template, others in your space can access it. You can also add a template to a catalog to share with other spaces.

Developers can use your template to create and deploy an application, or you can embed your template as part of a larger [composite template](https://docs.cloud.google.com/application-design-center/docs/design-composite-templates). When developers create an application, they can configure each component from the template, but they can't add or remove any components. The template generates Terraform code, which developers can download or deploy from App Design Center.

This document helps you design, configure, and share a standard application template using App Design Center.

**Tip:** To use natural language assistance to design and refine your application template, see [Design and deploy an application with Gemini assistance](https://docs.cloud.google.com/cloud-assist/design-application).

## Before you begin

To perform the tasks in this document, ask your administrator to grant you the necessary roles on the [app-enabled folder](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-enabled-folder) or [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project), as listed in the following table:

Task | Required roles  
---|---  
Create, design, and edit standard application templates | Application Design Center Admin (`roles/designcenter.admin`), or  
Application Design Center User (`roles/designcenter.user`)  
Publish or share standard templates to a catalog | Application Design Center Admin (`roles/designcenter.admin`)  
  
For more information about roles, see [Access control with IAM](https://docs.cloud.google.com/application-design-center/docs/access-control).

## Create a standard application template

Create standard application templates to share your architecture design with development teams. You can add the following components to your template design:

  * **Assets** : High-level resources that help you control other resources, such as service accounts.

  * **Services** : Network or API interfaces that are consumed over the network, such as Cloud Storage and Vertex AI.

  * **Workloads** : Binary deployments that perform business functions, such as Cloud Run and Compute Engine.




You can select from the following components:

  * [Components designed by Google](https://docs.cloud.google.com/application-design-center/docs/supported-resources), incorporating Google Cloud best practices and default security configurations.
  * Your own [components that you import](https://docs.cloud.google.com/application-design-center/docs/import-components), based on your own Terraform modules.



As you design your template, App Design Center generates Terraform code to reflect the design and configuration details.

### Specify template details

Template details help you categorize your template and help developers decide whether to use your template.

To enter details for your template, do the following:

### Design canvas

  1. From the navigation menu, click **Templates**.

[Go to Templates](https://console.cloud.google.com/products/design-center/templates)

  2. Click **Create Template**.

  3. The **Template ID** field is automatically populated. Alternatively, enter a unique identifier for the template. This field is required.

  4. In the **Template Name** field, enter a human-readable identifier to display in the Google Cloud console.

If you don't provide a name, the Template ID is copied to this field.

  5. In the **Description** field, enter a brief explanation of the application's purpose.

  6. Click **Create template**. The design canvas is displayed.




###  gcloud CLI 

Create a new application template.
    
    
    gcloud design-center spaces application-templates create APPLICATION_TEMPLATE \
    --project=PROJECT \
    --location=LOCATION \
    --space=SPACE \
    --display-name=DISPLAY_NAME \
    --description=DESCRIPTION
    

Replace the following:

  * `APPLICATION_TEMPLATE`: The template ID for the application template that you want to create.
  * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
  * `LOCATION`: The application template region.
  * `SPACE`: Your space ID.
  * `DISPLAY_NAME`: A name to display in the Google Cloud console.
  * `DESCRIPTION`: A brief description.



For more information, see [gcloud design-center spaces application-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/create).

### Design your template

Design your template by adding and connecting components. The following example includes three connected components on the design canvas.

![A three-tier web application in the design canvas. The application includes frontend, backend, and database components.](https://docs.cloud.google.com/static/application-design-center/images/three-tier-application.png)

You can design your template by adding components to the following starting points:

  * A blank canvas.
  * A [Google-provided template](https://docs.cloud.google.com/application-design-center/docs/build-on-google-templates).
  * A template that you generate with [Gemini assistance](https://docs.cloud.google.com/cloud-assist/design-application).



To help developers configure an application based on your template, designate specific input and output variables. Variables help you define the following:

  * Specific inputs that developers must provide when they create an application based on your template. For example, you can provide distinct variable values for each environment when you deploy an application to development, production, and test environments. These variables are automatically exposed in the generated Terraform `variables.tf` and `outputs.tf` files.

  * Connections between two standard application templates that are embedded in a [composite template](https://docs.cloud.google.com/application-design-center/docs/design-composite-templates). For example, to create a connection in a composite template, a database template might output a database name variable that is used as input for an application logic template.




To design your template, do the following:

### Design canvas

  1. From the design canvas, select **Design** to view the canvas.

  2. Do one of the following to get started:

     * To start from scratch, from the **Components** area, click a component to add it to the canvas area.

     * To start from a Google-provided template, in the **Get Started** area on the canvas, click the template name.

     * To use natural language chat to generate a template, click **Custom Application with Gemini**.

  3. To create a communication channel between components, do one of the following:

     * To connect two components on the canvas, drag from a blue dot on a component to a blue dot on another component.

     * To add to an existing component, click add **Add** and select the component to add.

For connection details, see the configuration documentation for each [supported resource](https://docs.cloud.google.com/application-design-center/docs/supported-resources).

  4. To remove a component or connection, do the following:

     1. In the canvas, click the component or connection.

     2. In the **Configuration** area, click **Delete**.

     3. In the field, enter **delete**.

     4. Click **Delete**.

  5. To specify input and output variables for your template, do the following:

     1. Click **Template details**.

     2. In the **Template details** panel, click the **Variables** tab.

     3. In the **Edit Variable** area, do the following.

        1. From the **Component** list, select the component that is the basis of your variable.

        2. From the **Variable type** list, select one of the following:

           * **Output** : The component outputs a value that might be required for a connection. For example, a Cloud Run service might output an IP address.

           * **Input** : The component requires input from the developer or from another standard application template. For example, a data processing template might require a database name from a data storage template.

        3. To create another variable, click **Add variable** and repeat these steps.




###  gcloud CLI 

  1. Identify the template revision URIs for the Google catalog components that you want to add to the template.
         
         gcloud design-center spaces shared-templates list \
         --google-catalog \
         --location=us-central1
         

For more information, see [gcloud design-center spaces shared-templates list](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/shared-templates/list).

  2. Add a component to your application template.
         
         gcloud design-center spaces application-templates components create COMPONENT \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE \
         --application-template=APPLICATION_TEMPLATE \
         --shared-template-revision-uri=SHARED_TEMPLATE_URI
         

Replace the following:

     * `COMPONENT`: The component ID for the component that you want to add to the template.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application template region.
     * `SPACE`: Your space ID.
     * `APPLICATION_TEMPLATE`: The template ID for the application template where you're adding the component.
     * `SHARED_TEMPLATE_URI`: The component shared template URI. For example, `projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1`.

For more information, see [gcloud design-center spaces application-templates components create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/create).

  3. Add a second component to your template.
         
         gcloud design-center spaces application-templates components create COMPONENT_2 \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE \
         --application-template=APPLICATION_TEMPLATE \
         --shared-template-revision-uri=SHARED_TEMPLATE_URI_2
         

Replace the following:

     * `COMPONENT_2`: The component ID for the second component that you want to add to the template.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application template region.
     * `SPACE`: Your space ID.
     * `APPLICATION_TEMPLATE`: The template ID for the application template where you're adding the component.
     * `SHARED_TEMPLATE_URI_2`: The second component shared template URI. For example, `projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1`.

For more information, see [gcloud design-center spaces application-templates components create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/create).

  4. Create a connection between the two components.
         
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
     * `COMPONENT`: The source component ID.
     * `COMPONENT_2`: The destination component ID.

For more information, see [gcloud design-center spaces application-templates components connections create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/connections/create).

  5. Add input and output variables to require developer input, or to connect to other components in composite templates.
         
         gcloud design-center spaces application-templates update APPLICATION_TEMPLATE \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE \
         --add-root-input-variables=componentUri=COMPONENT_URI,variable=VARIABLE \
         --add-root-output-variables=componentUri=COMPONENT_URI,variable=VARIABLE
         

Replace the following:

     * `APPLICATION_TEMPLATE`: The template ID for the application template where you're adding variables.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application template region.
     * `SPACE`: Your space ID.
     * `COMPONENT_URI`: The URI for the component that is the basis of your variable.
     * `VARIABLE`: The component variable that you want to input or output. For example, a database component might have a `database_name` variable that you might want to output or require input from developers.

For more information, see [gcloud design-center spaces application-templates update](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/update).




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




### Verify compliance with security frameworks

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can apply a consistent set of policies to any application that is deployed from a template to enforce specific security requirements from your organization before deployment. Running assessments at the template design phase is optional, but resolving misconfigurations early is highly recommended because assessments are enforced during the application pre-deployment phase.

If you have the Standard tier of [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/service-tiers), your templates are validated against the Google Cloud [Security Essentials](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#security-essentials) framework. If you have the Premium or Enterprise tier, you can [create additional frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework) and attach them directly to your application template within a folder-level boundary or a single-project boundary.

For more information on how to attach security frameworks to your template, see [Enforce security policies](https://docs.cloud.google.com/application-design-center/docs/enforce-security-policies).

### Edit Terraform code

As you design your application template, App Design Center generates Terraform code to reflect the design and configuration details. You can edit the Terraform to specify component configuration details.

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



## Verify your template

Before you share your template with developers, make sure that it functions as you intended. To verify your template, do the following:

  1. Create an [application](https://docs.cloud.google.com/application-design-center/docs/manage-applications) with the following settings: 
     1. From the **Environment** list, select **TEST**.
     2. From the **Criticality** list, select **LOW**.
  2. [Deploy the application](https://docs.cloud.google.com/application-design-center/docs/deploy-applications).
  3. Test your infrastructure to make sure that it meets your requirements.
  4. To avoid recurring costs, delete the test deployment.



## Share a template to a catalog

Once you have verified your template, you can publish the template to a catalog. The template can be used by application developers who have access to a space where the catalog is shared.

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

  * Share your templates with other spaces by [managing template catalogs](https://docs.cloud.google.com/application-design-center/docs/manage-catalogs).
  * Use your own Terraform modules in your template designs by [importing components](https://docs.cloud.google.com/application-design-center/docs/import-components).
  * Learn how to update, scale, and delete your resources by [managing applications](https://docs.cloud.google.com/application-design-center/docs/manage-applications).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

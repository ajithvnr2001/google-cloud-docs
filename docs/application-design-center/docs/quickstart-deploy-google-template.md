---
url: https://docs.cloud.google.com/application-design-center/docs/quickstart-deploy-google-template/
title: Quickstart: Customize and deploy a Google template \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:41.082657+00:00
---

# Quickstart: Customize and deploy a Google template  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/quickstart-deploy-google-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Customize and deploy a Google template

This quickstart helps you copy a [Google-provided template](https://docs.cloud.google.com/application-design-center/docs/build-on-google-templates), customize its components, and deploy a test application. You'll use the [Generative AI RAG with Cloud SQL](https://docs.cloud.google.com/application-design-center/docs/gen-ai-rag-with-sql) template in this quickstart, but you can apply the procedures in this document to any template. 

The following image shows the components and connections of the Generative AI RAG with Cloud SQL template in the design canvas:

![A Generative AI RAG application in the design canvas.](https://docs.cloud.google.com/static/application-design-center/images/google-gen-ai-rag-no-lb.png)

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. [Set up App Design Center](https://docs.cloud.google.com/application-design-center/docs/setup) in your project.



### Required roles

Ask your administrator to grant you the roles listed in the following table:

Task | Required roles  
---|---  
Copy, design, and edit templates | Application Design Center Admin (`roles/designcenter.admin`), or  
Application Design Center User (`roles/designcenter.user`)  
Deploy applications and configurations | Application Admin (`roles/designcenter.applicationAdmin`), or  
Application Editor (`roles/designcenter.applicationEditor`)  
Create service accounts during deployment | Create service accounts (`roles/iam.serviceAccountCreator`) on the project  
Grant service account access to your project | Project IAM Admin (`roles/resourcemanager.projectIamAdmin`) on the project  
  
For more information about roles, see [Access control with IAM](https://docs.cloud.google.com/application-design-center/docs/access-control).

### Prepare the environment

You can use one of the following to complete this quickstart.

  * Use the design canvas in the Google Cloud console.



  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  * [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  * If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  * To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
        
        gcloud init

  * [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  * If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  * To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
        
        gcloud init




## Copy the template and create an application draft

Copy the Google template and configure an application draft.

### Design canvas

  1. In the Google Cloud console, go to the **Google templates** page.

[Go to Google templates](https://console.cloud.google.com/products/design-center/google-catalog)

  2. Click **Preview and customize** on the **Generative AI RAG with Cloud SQL** template card.

The template opens in the design canvas.

  3. Click **Duplicate and customize**.

  4. In the **Create a new template** dialog, enter the following details:

     1. In the **Template ID** field, enter `quickstart-custom-gen-ai-rag`.

     2. In the **Template Name** field, enter `Quickstart custom Generative AI RAG`.

     3. In the **Description** field, enter `A custom template copied from the Generative AI RAG with Cloud SQL template.`

     4. Click **Create template**.

The template is copied to your space and displayed in the design canvas.

  5. From the design canvas, click **Configure an app**.

  6. Click **Create new application** and enter the following details:

     1. In the **Name** field, enter `quickstart-custom-gen-ai-rag-test`.

     2. In the **Display Name** field, enter `Quickstart custom Generative AI RAG test`.

     3. From the **Region** list, select `us-central1 (Iowa)`.

     4. From the **Environment** list, select `Test`.

     5. From the **Criticality** list, select `Low`.

  7. Click **Create Application**.

The system creates the application draft.




###  gcloud CLI 

  1. Filter the shared templates in the Google catalog to find the revision URI for the `gen-ai-rag-with-sql` template.
         
         gcloud design-center spaces shared-templates list \
           --google-catalog \
           --location=LOCATION \
           --filter="displayName:gen-ai-rag-cloud-sql"
         

Replace the following:

     * `LOCATION`: Your space location. For example, `us-central1`.

Identify the revision URI from the output.

  2. Create an application draft from that template revision.
         
         gcloud design-center spaces applications create quickstart-custom-gen-ai-rag-test \
           --space=SPACE \
           --location=LOCATION \
           --project=PROJECT \
           --source-shared-template-revision-uri=SHARED_TEMPLATE_REVISION_URI \
           --display-name="Quickstart custom Generative AI RAG test" \
           --environment-type=test \
           --criticality-type=low \
           --scope-type=regional \
           --deployment-region=LOCATION
         

Replace the following:

     * `SPACE`: Your space ID. For example, `default-space`.
     * `PROJECT`: Your project ID.
     * `SHARED_TEMPLATE_REVISION_URI`: The revision URI of the template. For example, `projects/gcpdesigncenter/locations/us-central1/spaces/googlespace/sharedTemplates/f8ddfbd3-6393-4a1e-942c-aaa7292fa30c/revisions/r-28`.



## Configure components

Configure required component parameters in your application draft. For more information about component parameters, see [Supported resources](https://docs.cloud.google.com/application-design-center/docs/supported-resources).

### Design canvas

  1. In the design canvas, click **frontend-service** and do the following in the **Configuration** area:

     1. In the **Service Name** field, enter `custom-rag-frontend`.

     2. Click **Save**.

  2. In the design canvas, click **retrieval-service** and do the following in the **Configuration** area:

     1. In the **Service Name** field, enter `custom-retrieval-service`.

     2. Click **Save**.

  3. In the design canvas, click **database-postgresql** and do the following in the **Configuration** area:

     1. In the **Name** field, enter `custom-rag-database`.

     2. Click **Save**.

  4. In the design canvas, click **vertex-ai** and do the following in the **Configuration** area:

     1. From the **Project ID** list, make sure your project is selected.

     2. Click **Save**.

  5. In the design canvas, click **secret-manager** and do the following in the **Configuration** area:

     1. In the **Name** field, enter `db-ai-secret`.

     2. Click **Save**.




The canvas displays a green check mark in each component to convey that all required parameters are configured.

###  gcloud CLI 

  1. Describe the application to identify component parameters.
         
         gcloud design-center spaces applications describe quickstart-custom-gen-ai-rag-test \
           --space=SPACE \
           --location=LOCATION \
           --project=PROJECT \
           --format='yaml(name,componentParameters)'
         

The output displays parameters for each component.

  2. Get a list of component URIs.
         
         gcloud design-center spaces applications describe quickstart-custom-gen-ai-rag-test \
           --space=SPACE \
           --location=LOCATION \
           --project=PROJECT \
           --format='value(serializedApplicationTemplate.components.uri)'
         

  3. Create configuration JSON files in your working directory.

     1. Create `custom-frontend.json`.
            
            {
               "component": "FRONTEND_COMPONENT_URI",
               "parameters": [
                  {
                     "key": "service_name",
                     "value": "custom-rag-frontend"
                  },
                  {
                     "key": "PROJECT",
                     "value": "PROJECT"
                  },
                  {
                     "key": "location",
                     "value": "LOCATION"
                  }
               ]
            }
            

     2. Create `custom-retrieval.json`.
            
            {
               "component": "RETRIEVAL_COMPONENT_URI",
               "parameters": [
                  {
                     "key": "service_name",
                     "value": "custom-retrieval-service"
                  },
                  {
                     "key": "project_id",
                     "value": "PROJECT"
                  },
                  {
                     "key": "location",
                     "value": "LOCATION"
                  }
               ]
            }
            

     3. Create `custom-database.json`.
            
            {
               "component": "DATABASE_COMPONENT_URI",
               "parameters": [
                  {
                     "key": "name",
                     "value": "custom-rag-database"
                  },
                  {
                     "key": "project_id",
                     "value": "PROJECT"
                  },
                  {
                     "key": "database_version",
                     "value": "POSTGRES_15"
                  },
                  {
                     "key": "region",
                     "value": "us-central1"
                  },
                  {
                     "key": "zone",
                     "value": "us-central1-a"
                  }
               ]
            }
            

     4. Create `custom-secmanager.json`.
            
            {
            "component": "SECRET_MANAGER_COMPONENT_URI",
            "parameters": [
               {
                  "key": "name",
                  "value": "db-ai-secret"
               },
               {
                  "key": "project_id",
                  "value": "PROJECT"
               }
            ]
            }
            

     5. Create `custom-vertex.json`.
            
            {
            "component": "VERTEX_AI_COMPONENT_URI",
            "parameters": [
               {
                  "key": "project_id",
                  "value": "PROJECT"
               }
            ]
            }
            

Replace the following:

     * `FRONTEND_COMPONENT_URI`: The frontend component URI. For example, `projects/gcpdesigncenter/locations/us-central1/spaces/googlespace/applicationTemplates/gen-ai-rag-cloud-sql/components/frontend-service`.
     * `RETRIEVAL_COMPONENT_URI`: The retrieval component URI. For example, `projects/gcpdesigncenter/locations/us-central1/spaces/googlespace/applicationTemplates/gen-ai-rag-cloud-sql/components/retrieval-service`.
     * `DATABASE_COMPONENT_URI`: The database component URI. For example, `projects/gcpdesigncenter/locations/us-central1/spaces/googlespace/applicationTemplates/gen-ai-rag-cloud-sql/components/database-postgresql`
     * `SECRET_MANAGER_COMPONENT_URI`: The Secret Manager component URI. For example, `projects/gcpdesigncenter/locations/us-central1/spaces/googlespace/applicationTemplates/gen-ai-rag-cloud-sql/components/secret-manager`.
     * `VERTEX_AI_COMPONENT_URI`: The Vertex AI component URI. For example, `projects/gcpdesigncenter/locations/us-central1/spaces/googlespace/applicationTemplates/gen-ai-rag-cloud-sql/components/vertex-ai`.
     * `PROJECT`: Your project ID.
  4. Update the application configuration with the JSON parameter files.
         
         gcloud design-center spaces applications update quickstart-custom-gen-ai-rag-test \
           --space=SPACE \
           --location=LOCATION \
           --project=PROJECT \
           --component-parameters=./custom-frontend.json \
           --component-parameters=./custom-retrieval.json \
           --component-parameters=./custom-database.json \
           --component-parameters=./custom-secmanager.json \
           --component-parameters=./custom-vertex.json
         




## Deploy the application

Deploy the configured application.

### Design canvas

  1. Click **Deploy**.

  2. In the **Select service account** area, do the following:

     1. Select **Create a new service account**.

     2. Click **Proceed**.

  3. Click **Deploy**.

After a few minutes, the application is deployed and resources are created.




###  gcloud CLI 

  1. Preview the deployment and automatically create a preview service account.
         
         gcloud design-center spaces applications preview quickstart-custom-gen-ai-rag-test \
           --space=SPACE \
           --location=LOCATION \
           --project=PROJECT \
           --create-sa
         

  2. Deploy the application and automatically create a deployment service account.
         
         gcloud design-center spaces applications deploy quickstart-custom-gen-ai-rag-test \
           --space=SPACE \
           --location=LOCATION \
           --project=PROJECT \
           --create-sa \
           --async
         

Copy the operation ID.

  3. Track the deployment status.
         
         gcloud design-center operations describe operation-OPERATION_ID \
           --space=SPACE \
           --location=LOCATION \
           --project=PROJECT
         

Replace the following:

     * `OPERATION_ID`: The operation ID.



## Optional: Monitor your deployment

After you deploy your application, you can view telemetry and monitor performance:

  1. In the Google Cloud console, go to the **Application monitoring** page: 

[Go to **Application monitoring**](https://console.cloud.google.com/monitoring/applications)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the **Name** column, click the application you deployed. 

The page displays monitoring information for the application and its services and workloads. 

  3. Review predefined dashboards. For more information, see [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring).




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

### Delete the deployed application

### Design canvas

  1. From the navigation menu, click **Applications**.

[Go to Applications](https://console.cloud.google.com/products/design-center/applications)

  2. Click **Quickstart custom Generative AI RAG test**.

  3. Click more_vert **Actions** and select **Delete application**.

  4. In the **Delete** field, enter `quickstart-custom-gen-ai-rag-test`.

  5. Click **Delete**.




###  gcloud CLI 

  1. Delete the application using the CLI.
         
         gcloud design-center spaces applications delete quickstart-custom-gen-ai-rag-test \
           --space=SPACE \
           --location=LOCATION \
           --project=PROJECT
         




### Optional: Delete the project

**Caution:** If you delete a project, all resources in the project are permanently deleted.

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. At the prompt, type the project ID, and then click **Shut down**. 



## What's next

  * Review core concepts and benefits with the [App Design Center overview](https://docs.cloud.google.com/application-design-center/docs/overview).
  * Get started with preconfigured architectures by [building on Google templates](https://docs.cloud.google.com/application-design-center/docs/build-on-google-templates).
  * Define your own configurations by [designing application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/application-design-center/docs/quickstart-create-template/
title: Create and verify a template \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:37.587027+00:00
---

# Create and verify a template  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/quickstart-create-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and verify a template

This quickstart helps you create and deploy a three-tier web application template that includes frontend, backend, and database components. The following image shows the design canvas, which includes the application components and connections.

![A three-tier web application in the design canvas. The application includes frontend, backend, and database components.](https://docs.cloud.google.com/static/application-design-center/images/three-tier-application.png)

You design the template using one of the following:

  * The design canvas in Application Design Center.
  * Natural language prompts in [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview).
  * App Design Center [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/design-center).



After you complete the design, verify the template by deploying a test application in App Design Center.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=application-design-center--quickstart-create-template)

* * *

## Before you begin

  1. [Set up App Design Center](https://docs.cloud.google.com/application-design-center/docs/setup).

  2. [Create a deployment project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) in your [app-enabled folder](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-enabled-folder).

You'll deploy Google Cloud resources to this project when you deploy your application.

  3. [Make sure that billing is enabled](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project) for your deployment project.




### Set up tools

You can use one of the following to complete this quickstart.

  * Use the design canvas in the Google Cloud console.

  * To use Gemini Cloud Assist to create your design, see [Set up Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/set-up-gemini).




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




## Make sure you have required roles

Before starting the quickstart, ask your administrator to grant you the necessary roles required to design, build, and deploy, as listed in the following table:

Task | Required roles  
---|---  
Create, design, and edit standard templates | Application Design Center Admin (`roles/designcenter.admin`), or  
Application Design Center User (`roles/designcenter.user`)  
Deploy applications and configurations | Application Admin (`roles/designcenter.applicationAdmin`), or  
Application Editor (`roles/designcenter.applicationEditor`)  
Create service accounts during deployment | Create service accounts (`roles/iam.serviceAccountCreator`) on the management project  
Grant service account access to a deployment project | Project IAM Admin (`roles/resourcemanager.projectIamAdmin`) on the deployment project  
  
For more information about roles, see [Access control with IAM](https://docs.cloud.google.com/application-design-center/docs/access-control).

## Create a new template and add details

### Design canvas

  1. In the Google Cloud console, go to the **Templates** page.

[Go to Templates](https://console.cloud.google.com/products/design-center/templates)

  2. Click **Create Template** and enter the following details:

     1. In the **Template ID** field, enter `quickstart-three-tier-web-app`.

     2. In the **Template Name** field, enter `Quickstart three-tier web app` .

     3. In the **Description** field, enter `A template to generate a three-tier web application`.

     4. Click **Create template**.

The template is created and the design canvas is displayed.

  3. In the **Components** area, click the following components to add them to the design canvas:

     * **Cloud Run** (add two components)
     * **Cloud SQL (PostgreSQL)**
  4. To create connections between components, do the following:

     1. From the blue dot at the bottom of **cloud-run-1** , drag to the blue dot at the top of **cloud-run-2**.

     2. From the blue dot at the bottom of **cloud-run-2** , drag to the blue dot at the top of **sql-postgresql-1**.

Your template contains three components. The canvas displays between components to represent connections.




###  Gemini Cloud Assist 

  1. In the Google Cloud console toolbar, click spark **Open or close Gemini Cloud Assist chat**.

The **Cloud Assist** panel opens.

  2. In Gemini Cloud Assist chat, enter the following prompt:
         
         I want to create a three-tier web application.
         

Gemini Cloud Assist generates a basic design for a three-tier web application.

  3. To remove the load balancers and Secret Manager components, enter the following prompt:
         
         I don't need load balancers or Secret Manager.
         

Gemini Cloud Assist updates the design to remove the components.

  4. Review the updated design that includes the following components:

     * Cloud Run (two components)
     * Cloud SQL for PostgreSQL
  5. Click **Edit app design**.

The **Create a new template** page is displayed.

  6. Enter the following template details:

     1. In the **Template ID** field, enter `quickstart-three-tier-web-app`.

     2. In the **Template Name** field, enter `Quickstart three-tier web app` .

     3. In the **Description** field, enter `A template to generate a three-tier web application`.

  7. Click **Create template**.

The system creates a new template and displays the design canvas.




###  gcloud CLI 

  1. Create an application template.
         
         gcloud design-center spaces application-templates create quickstart-three-tier-web-app \
         --display-name="Quickstart three-tier web app" \
         --description="A template to generate a three-tier web application" \
         --space=SPACE \
         --location=us-central1 \
         --project=MANAGEMENT_PROJECT_ID
         

  2. List the shared templates in the Google catalog.
         
         gcloud design-center spaces shared-templates list \
         --google-catalog \
         --location=us-central1
         

     1. Identify the shared template IDs for Cloud Run and Cloud SQL.
  3. Add a Cloud Run component to use as the frontend.
         
         gcloud design-center spaces application-templates components create cloud-run-1 \
         --application-template=quickstart-three-tier-web-app \
         --shared-template-revision-uri=google/1b5e09c8-780f-484e-b8ed-c7178f4e4342 \
         --space=SPACE \
         --location=us-central1 \
         --project=MANAGEMENT_PROJECT_ID
         

  4. Add a second Cloud Run component to use as the backend.
         
         gcloud design-center spaces application-templates components create cloud-run-2 \
         --application-template=quickstart-three-tier-web-app \
         --shared-template-revision-uri=google/1b5e09c8-780f-484e-b8ed-c7178f4e4342 \
         --space=SPACE \
         --location=us-central1 \
         --project=MANAGEMENT_PROJECT_ID
         

  5. Add a Cloud SQL component.
         
         gcloud design-center spaces application-templates components create sql-postgresql-1 \
         --application-template=quickstart-three-tier-web-app \
         --shared-template-revision-uri=google/45be1bc2-89bc-477b-9b5d-64c41ff3b146 \
         --space=SPACE \
         --location=us-central1 \
         --project=MANAGEMENT_PROJECT_ID
         

  6. Connect cloud-run-1 to cloud-run-2.
         
         gcloud design-center spaces application-templates components connections create frontend-to-backend \
          --application-template=quickstart-three-tier-web-app \
          --component=cloud-run-1 \
          --destination-component-uri=cloud-run-2 \
          --space=SPACE \
          --location=us-central1 \
          --project=MANAGEMENT_PROJECT_ID
         

  7. Connect cloud-run-2 to sql-postgresql-1.
         
         gcloud design-center spaces application-templates components connections create backend-to-database \
          --application-template=quickstart-three-tier-web-app \
          --component=cloud-run-2 \
          --destination-component-uri=sql-postgresql-1 \
          --space=SPACE \
          --location=us-central1 \
          --project=MANAGEMENT_PROJECT_ID
         

  8. Commit your changes to create an application template revision.
         
         gcloud design-center spaces application-templates commit quickstart-three-tier-web-app \
          --space=SPACE \
          --location=us-central1 \
          --project=MANAGEMENT_PROJECT_ID
         




## Create an application draft

### Design canvas

  1. From the design canvas, click **Configure an app**.

  2. Click **Create new application** and do the following:

     1. In the **Name** field, enter `quickstart-three-tier-test`.

     2. In the **Display Name** field, enter `Quickstart three-tier test`.

     3. From the **Region** list, select `us-central1 (Iowa)`.

     4. From the **Environment** list, select `Test`.

     5. From the **Criticality** list, select `Low`.

     6. In the **Scope** area, from the **Application scope** list, select `Regional`.

  3. Click **Create Application**.

The system creates the application draft.




###  gcloud CLI 

  1. Identify your application template latest revision URI.
         
         gcloud design-center spaces application-templates describe quickstart-three-tier-web-app \
          --space=SPACE \
          --location=us-central1 \
          --project=MANAGEMENT_PROJECT_ID \
          --format='yaml(name,latestRevision)'
         

  2. Create an application draft based on your template.
         
         gcloud design-center spaces applications create quickstart-three-tier-test \
            --space=SPACE \
            --location=us-central1 \
            --project=MANAGEMENT_PROJECT_ID \
            --source-application-template-revision=projects/MANAGEMENT_PROJECT_ID/locations/us-central1/spaces/SPACE/applicationTemplates/quickstart-three-tier-web-app/revisions/TEMPLATE_REVISION \
            --display-name="Quickstart three-tier test" \
            --environment-type=test \
            --criticality-type=low \
            --scope-type=regional \
            --deployment-region=us-central1
         




## Configure components

### Design canvas

  1. In the design canvas, click **cloud-run-1** and do the following in the **Configuration** area:

     1. From the **Project ID** list, select the deployment project you created in Before you begin. The resource will be deployed to this project.

     2. In the **Service Name** field, enter `frontend-service`.

     3. Click **Save**.

  2. In the design canvas, click **cloud-run-2** and do the following in the **Configuration** area:

     1. From the **Project ID** list, select the deployment project you created in Before you begin. The resource will be deployed to this project.

     2. In the **Service Name** field, enter `backend-service`.

     3. Click **Save**.

  3. In the design canvas, click **sql-postgresql-1** and do the following in the **Configuration** area:

     1. From the **Project ID** list, select the deployment project you created in Before you begin. The resource will be deployed to this project.

     2. In the **Name** field, enter `database-postgresql`.

     3. From the **Database Version** list, select `POSTGRES_15`.

     4. From the **Zone** drop-down list, select `us-central1-a`.

     5. Click **Save**.

The canvas displays a green check mark in each component to convey that you have specified the required parameters. You can now deploy the application draft to the `Test` environment for verification.




###  gcloud CLI 

  1. Describe the application to identify the required configuration parameters.
         
         gcloud design-center spaces applications describe quickstart-three-tier-test \
          --space=SPACE \
          --location=us-central1 \
          --project=MANAGEMENT_PROJECT_ID \
          --format='yaml(name,componentParameters)'
         

  2. For each component, in your home directory, create a JSON file that contains required parameter values.

     1. Create `frontend-service.json`.
            
            {
               "component": "projects/MANAGEMENT_PROJECT_ID/locations/us-central1/spaces/SPACE/applicationTemplates/quickstart-three-tier-web-app/components/cloud-run-1",
               "parameters": [
                  {
                     "key": "service_name",
                     "value": "frontend-service"
                  },
                  {
                     "key": "project_id",
                     "value": "DEPLOYMENT_PROJECT_ID"
                  }
               ]
             }
            

     2. Create `backend-service.json`.
            
            {
               "component": "projects/MANAGEMENT_PROJECT_ID/locations/us-central1/spaces/SPACE/applicationTemplates/quickstart-three-tier-web-app/components/cloud-run-2",
               "parameters": [
                  {
                     "key": "service_name",
                     "value": "backend-service"
                  },
                  {
                     "key": "project_id",
                     "value": "DEPLOYMENT_PROJECT_ID"
                  }
               ]
             }
            

     3. Create `database-postgresql.json`.
            
            {
               "component": "projects/MANAGEMENT_PROJECT_ID/locations/us-central1/spaces/SPACE/applicationTemplates/quickstart-three-tier-web-app/components/sql-postgresql-1",
               "parameters": [
                  {
                     "key": "name",
                     "value": "database-postgresql"
                  },
                  {
                     "key": "project_id",
                     "value": "DEPLOYMENT_PROJECT_ID"
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
            

  3. Update the application to configure the required parameters.
         
         gcloud design-center spaces applications update quickstart-three-tier-test \
          --space=SPACE \
          --location=us-central1 \
          --project=MANAGEMENT_PROJECT_ID \
          --component-parameters=./frontend-service.json \
          --component-parameters=./backend-service.json \
          --component-parameters=./database-postgresql.json
         




## Deploy the application

### Design canvas

  1. Click **Deploy**.

  2. In the **Select a service account** area, do the following:

     1. Click **Create a new service account**.

     2. Click **Proceed**.

  3. Click **Deploy**.

After a few minutes, the system deploys the application and creates resources in your project. The system displays the following details:

     * A link to App Hub, where you can view deployed resource details, including links to monitoring dashboards.
     * Links to Cloud Build logs, which you can use to troubleshoot deployment errors.
     * Outputs like service URIs are displayed, which you can use to interact with deployed resources.
  4. To build on this quickstart, see [Update an application template and redeploy](https://docs.cloud.google.com/application-design-center/docs/quickstart-update-template).




###  gcloud CLI 

  1. Describe the application to identify required IAM roles for your deployment service account.
         
         gcloud design-center spaces applications describe quickstart-three-tier-test \
          --space=SPACE \
          --location=us-central1 \
          --project=MANAGEMENT_PROJECT_ID \
          --format='yaml(name,projectParameters)'
         

  2. Create a new service account to deploy the application.
         
         gcloud iam service-accounts create quickstart-service-account \
          --project=MANAGEMENT_PROJECT_ID \
          --display-name="Quickstart service account" \
          --description="A service account to deploy the ADC quickstart"
         

  3. Add the required deployment project roles to the service account.
         
         #!/bin/bash
         
         PROJECT_ID="DEPLOYMENT_PROJECT_ID"
         SERVICE_ACCOUNT="quickstart-service-account@MANAGEMENT_PROJECT_ID.iam.gserviceaccount.com"
         
         ROLES=(
         "roles/iap.admin"
         "roles/compute.networkAdmin"
         "roles/compute.viewer"
         "roles/run.admin"
         "roles/iam.serviceAccountAdmin"
         "roles/serviceusage.serviceUsageAdmin"
         "roles/cloudkms.admin"
         "roles/logging.logWriter"
         "roles/iam.serviceAccountUser"
         "roles/cloudsql.admin"
         "roles/cloudkms.autokeyAdmin"
         "roles/storage.admin"
         "roles/serviceusage.serviceUsageViewer"
         "roles/resourcemanager.projectIamAdmin"
         "roles/cloudkms.cryptoKeyEncrypterDecrypter"
         )
         
         for role in "${ROLES[@]}"; do
         echo "Adding role: ${role}"
         gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
            --member="serviceAccount:${SERVICE_ACCOUNT}" \
            --role="${role}"
         echo "---"
         done
         
         echo "Finished adding roles."
         

  4. Add the required [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) roles to the service account.
         
         #!/bin/bash
         
         PROJECT_ID="MANAGEMENT_PROJECT_ID"
         SERVICE_ACCOUNT="quickstart-service-account@MANAGEMENT_PROJECT_ID.iam.gserviceaccount.com"
         
         ROLES=(
         "roles/config.agent"
         "roles/apphub.editor"
         )
         
         for role in "${ROLES[@]}"; do
         echo "Adding role: ${role}"
         gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
            --member="serviceAccount:${SERVICE_ACCOUNT}" \
            --role="${role}"
         echo "---"
         done
         
         echo "Finished adding roles."
         

  5. Identify your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) number.
         
         gcloud projects describe MANAGEMENT_PROJECT_ID \
         --format="value(projectNumber)"
         

  6. Add an IAM policy binding for the `roles/iam.serviceAccountUser` role on your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project).
         
         gcloud iam service-accounts add-iam-policy-binding projects/MANAGEMENT_PROJECT_ID/serviceAccounts/quickstart-service-account@MANAGEMENT_PROJECT_ID.iam.gserviceaccount.com \
         --project=MANAGEMENT_PROJECT_ID \
         --member="serviceAccount:service-MANAGEMENT_PROJECT_NUMBER@gcp-sa-designcenter.iam.gserviceaccount.com" \
         --role="roles/iam.serviceAccountUser"
         

  7. Update the application to use your service account.
         
         gcloud design-center spaces applications update quickstart-three-tier-test \
         --space=SPACE \
         --location=us-central1 \
         --project=MANAGEMENT_PROJECT_ID \
         --service-account=projects/MANAGEMENT_PROJECT_ID/serviceAccounts/quickstart-service-account@MANAGEMENT_PROJECT_ID.iam.gserviceaccount.com
         

  8. Give your user actAs permission on your service account.
         
         gcloud iam service-accounts add-iam-policy-binding quickstart-service-account@MANAGEMENT_PROJECT_ID.iam.gserviceaccount.com \
         --project=MANAGEMENT_PROJECT_ID \
         --member="user:USER" \
         --role="roles/iam.serviceAccountUser"
         

USER is your Google Cloud user. For example, `dana@example.com`.

  9. Preview the application:

The preview takes a few minutes to generate.
         
         gcloud design-center spaces applications preview quickstart-three-tier-test \
         --location=us-central1 \
         --space=SPACE \
         --project=MANAGEMENT_PROJECT_ID
         

  10. Deploy the application.
         
         gcloud design-center spaces applications deploy quickstart-three-tier-test \
         --space=SPACE \
         --location=us-central1 \
         --project=MANAGEMENT_PROJECT_ID \
         --async
         

  11. Identify the operation ID.

  12. The deployment requires a few minutes to complete. Track the deployment status.
         
         gcloud design-center operations describe operation-OPERATION_ID \
         --space=SPACE \
         --location=us-central1 \
         --project=MANAGEMENT_PROJECT_ID
         

  13. When the deployment completes, identify the application output parameters.
         
         gcloud design-center spaces applications describe quickstart-three-tier-test \
          --space=SPACE \
          --location=us-central1 \
          --project=MANAGEMENT_PROJECT_ID \
          --format='yaml(name,appParameters,componentParameters,deploymentMetadata,deploymentRevision,previewReference)'
         




### Optional: Monitor your deployment

After you deploy an application, you can use [Application Monitoring](https://docs.cloud.google.com/stackdriver/docs/observability/about-application-monitoring) to view application telemetry and monitor health and performance:

  1. In the Google Cloud console, go to the **Application monitoring** page: 

[Go to **Application monitoring**](https://console.cloud.google.com/monitoring/applications)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. From the project picker of the Google Cloud console, select the management project.

  3. For detailed instructions on how to use the predefined dashboards and explore your telemetry data, see [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring).




You can also get additional health and performance information in [Cloud Hub](https://docs.cloud.google.com/hub/docs/overview), including deployment failures and deployments that can be updated, information about Google Cloud incidents that impact your applications, and services that are near their quota limits. 

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

### Delete the deployed application

  1. From the navigation menu, click **Applications**.

[Go to Applications](https://console.cloud.google.com/products/design-center/applications)

  2. From the table, click **Quickstart three-tier web app**.

  3. Click more_vert **Actions** and select **Delete application**.

  4. In the **Delete** field, enter `Quickstart three-tier web app`.

  5. Click **Delete**.




The system deletes the application, including the following:

  * The application details are removed from App Design Center.
  * The underlying App Hub application is deleted.
  * The underlying resources are deleted.



### Optional: Delete the project

To delete the deployment project you created in Before you begin, do the following:

**Caution:** If you delete a project, all resources in the project are permanently deleted.

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. At the prompt, type the project ID, and then click **Shut down**. 



## What's next

  * Learn how to modify your architecture by [updating a template and redeploying](https://docs.cloud.google.com/application-design-center/docs/quickstart-update-template).
  * Review core concepts and benefits with the [App Design Center overview](https://docs.cloud.google.com/application-design-center/docs/overview).
  * Build your templates using natural language with [Gemini assistance](https://docs.cloud.google.com/cloud-assist/design-application).
  * Duplicate and customize template architectures in [Quickstart: Customize and deploy a Google template](https://docs.cloud.google.com/application-design-center/docs/quickstart-deploy-google-template).
  * Define your own configurations by [designing application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

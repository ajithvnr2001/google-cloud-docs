---
url: https://docs.cloud.google.com/application-design-center/docs/import-terraform/
title: Import existing Terraform \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:17.552543+00:00
---

# Import existing Terraform  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/import-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Import existing Terraform Stay organized with collections  Save and categorize content based on your preferences. 

Application Design Center lets you import your existing multi-product Google Cloud Terraform configurations into an application template as is, without restructuring your code into individual component modules or publishing it to a catalog first.

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Unlike single-product Terraform modules that you import as catalog components and connect on the design canvas, a multi-product Terraform configuration is a root module that provisions resources across several Google Cloud products. To import single-product modules as components, see [Import components](https://docs.cloud.google.com/application-design-center/docs/import-components).

Importing existing Terraform configurations into App Design Center helps you do the following:

  * Bring existing Terraform configurations under App Design Center application lifecycle management and automatically register deployed resources in App Hub.
  * Version your Terraform configurations by creating immutable application template revisions.
  * Preview and deploy applications using Infrastructure Manager, or export the Terraform files to Cloud Storage.



After you create a template revision, you can use it in either of the following ways:

  * **Deploy directly** : Create an application from the revision, preview it to get an assessment report, and deploy it. You don't need to publish the template to a catalog, share it, or find a shared template first.
  * **Reuse through your catalog** : Publish the revision to your catalog, add it as a component to a composite application template, and export the composite template's Terraform. For more information, see [Publish an application template to a catalog](https://docs.cloud.google.com/application-design-center/docs/manage-catalogs#publish-an-application-template-to-a-catalog).



## Before you begin

To perform the tasks in this document, ask your administrator to grant you the necessary roles on the [app-enabled folder](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-enabled-folder) or [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project), as listed in the following table:

Task | Required roles  
---|---  
Create, import, snapshot, and export application templates and template revisions | Application Design Center Admin (`roles/designcenter.admin`), or  
Application Design Center User (`roles/designcenter.user`)  
Create, deploy, and export applications | Application Admin (`roles/designcenter.applicationAdmin`), or  
Application Editor (`roles/designcenter.applicationEditor`)  
  
For more information about roles, see [Access control with Identity and Access Management](https://docs.cloud.google.com/application-design-center/docs/access-control).

Store your Terraform root module (`.tf` files and any supporting files, such as `.json` files) in one of the following sources:

  * A Cloud Storage bucket.
  * A Developer Connect repository.
  * A public Git repository.
  * A local YAML or JSON file that contains the files.



## Import Terraform into an application template

Complete the following steps using Google Cloud CLI to create an application template, import your existing Terraform configuration, and create an immutable template revision.

  1. Create an application template in your space.
         
         gcloud design-center spaces application-templates create APPLICATION_TEMPLATE \
             --project=PROJECT \
             --location=LOCATION \
             --space=SPACE \
             --display-name=DISPLAY_NAME
         

Replace the following:

     * `APPLICATION_TEMPLATE`: The ID for the application template that you want to create.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
     * `SPACE`: Your space ID.
     * `DISPLAY_NAME`: A display name for the application template.

For more information, see [gcloud design-center spaces application-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/create).

  2. Import your Terraform configuration into the application template from one of the following sources:

     * To import from a Cloud Storage bucket, run the following command:
           
           gcloud design-center spaces application-templates ingest-iac APPLICATION_TEMPLATE \
               --project=PROJECT \
               --location=LOCATION \
               --space=SPACE \
               --gcs-uri=GCS_URI \
               --raw-terraform-import-enabled
           

     * To import from a Developer Connect repository, run the following command:
           
           gcloud design-center spaces application-templates ingest-iac APPLICATION_TEMPLATE \
               --project=PROJECT \
               --location=LOCATION \
               --space=SPACE \
               --developer-connect-repo-uri=DEVELOPER_CONNECT_REPO_URI \
               --developer-connect-branch=DEVELOPER_CONNECT_BRANCH \
               --developer-connect-dir=DEVELOPER_CONNECT_DIR \
               --raw-terraform-import-enabled
           

     * To import from a public Git repository, run the following command:
           
           gcloud design-center spaces application-templates ingest-iac APPLICATION_TEMPLATE \
               --project=PROJECT \
               --location=LOCATION \
               --space=SPACE \
               --git-source-repo=GIT_SOURCE_REPO \
               --git-source-ref-tag=GIT_SOURCE_REF_TAG \
               --git-source-dir=GIT_SOURCE_DIR \
               --raw-terraform-import-enabled
           

     * To import from a local YAML or JSON file containing an `IaCModule` payload, run the following command:
           
           gcloud design-center spaces application-templates ingest-iac APPLICATION_TEMPLATE \
               --project=PROJECT \
               --location=LOCATION \
               --space=SPACE \
               --iac-module-from-file=IAC_MODULE_FILE \
               --raw-terraform-import-enabled
           

Replace the following:

     * `APPLICATION_TEMPLATE`: The application template ID.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
     * `SPACE`: Your space ID.
     * `GCS_URI`: The Cloud Storage URI containing your Terraform files, in the format `gs://BUCKET_NAME/FOLDER_PATH`.
     * `DEVELOPER_CONNECT_REPO_URI`: The Developer Connect repository link URI, in the format `projects/PROJECT/locations/LOCATION/connections/CONNECTION/gitRepositoryLinks/REPO_LINK`.
     * `DEVELOPER_CONNECT_BRANCH`: The branch name in your Developer Connect repository. Alternatively, specify `--developer-connect-ref-tag` or `--developer-connect-commit-sha`.
     * `DEVELOPER_CONNECT_DIR`: The directory path in your Developer Connect repository.
     * `GIT_SOURCE_REPO`: The HTTPS URL of the public Git repository.
     * `GIT_SOURCE_REF_TAG`: The Git reference or tag in the public Git repository.
     * `GIT_SOURCE_DIR`: The directory path in the public Git repository.
     * `IAC_MODULE_FILE`: The path to a local YAML or JSON file containing your Terraform files.
  3. Create a snapshot of the application template to generate an immutable application template revision that you can use to create and deploy applications.
         
         gcloud design-center spaces application-templates snapshot APPLICATION_TEMPLATE \
             --project=PROJECT \
             --location=LOCATION \
             --space=SPACE
         

Replace the following:

     * `APPLICATION_TEMPLATE`: The application template ID.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
     * `SPACE`: Your space ID.

The output includes the created application template revision URI in the format `projects/PROJECT/locations/LOCATION/spaces/SPACE/applicationTemplates/APPLICATION_TEMPLATE/revisions/REVISION`.




## Create and deploy an application from the template

After you create a snapshot revision of your imported Terraform template, you can create an application draft, supply input variable values, and deploy the application.

  1. Create an application draft from the application template revision.
         
         gcloud design-center spaces applications create APPLICATION \
             --project=PROJECT \
             --location=LOCATION \
             --space=SPACE \
             --source-application-template-revision=SOURCE_APPLICATION_TEMPLATE_REVISION \
             --deployment-project=DEPLOYMENT_PROJECT \
             --deployment-region=DEPLOYMENT_REGION \
             --app-parameters=APP_PARAMETERS \
             --scope-type=SCOPE_TYPE
         

Replace the following:

     * `APPLICATION`: The ID for the application that you want to create.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
     * `SPACE`: Your space ID.
     * `SOURCE_APPLICATION_TEMPLATE_REVISION`: The application template revision URI returned by the `snapshot` command.
     * `DEPLOYMENT_PROJECT`: The target project ID where your Terraform resources are deployed.
     * `DEPLOYMENT_REGION`: The target region where your Terraform resources are deployed.
     * `APP_PARAMETERS`: Optional. Input variable key-value pairs for your Terraform root module (for example, `key=KEY,value=VALUE`), or the path to a YAML or JSON file containing your application parameters.
     * `SCOPE_TYPE`: The scope for your application, either `regional` or `global`.

For more information about managing applications, see [Manage applications](https://docs.cloud.google.com/application-design-center/docs/manage-applications).

  2. Preview and deploy your application. For step-by-step instructions, see [Deploy applications](https://docs.cloud.google.com/application-design-center/docs/deploy-applications).




## Export Terraform code to Cloud Storage

You can export the Terraform files from an application template, an application template revision, or an application to a Cloud Storage bucket. Export when you want to run the Terraform with your own CI/CD tools or keep a copy in version control.

  * To export Terraform files from an application template draft, run the following command:
        
        gcloud design-center spaces application-templates export APPLICATION_TEMPLATE \
            --project=PROJECT \
            --location=LOCATION \
            --space=SPACE \
            --artifact-location-gcs-uri=ARTIFACT_LOCATION_GCS_URI
        

  * To export Terraform files from an application template revision, run the following command:
        
        gcloud design-center spaces application-templates revisions export REVISION \
            --application-template=APPLICATION_TEMPLATE \
            --project=PROJECT \
            --location=LOCATION \
            --space=SPACE \
            --artifact-location-gcs-uri=ARTIFACT_LOCATION_GCS_URI
        

  * To export Terraform files from an application (including `zz_adc_inputs.auto.tfvars.json` populated with your configured application parameters), run the following command:
        
        gcloud design-center spaces applications export APPLICATION \
            --project=PROJECT \
            --location=LOCATION \
            --space=SPACE \
            --artifact-location-gcs-uri=ARTIFACT_LOCATION_GCS_URI
        




Replace the following:

  * `APPLICATION_TEMPLATE`: The application template ID.
  * `REVISION`: The application template revision ID.
  * `APPLICATION`: The application ID.
  * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
  * `LOCATION`: Your location ID.
  * `SPACE`: Your space ID.
  * `ARTIFACT_LOCATION_GCS_URI`: The destination Cloud Storage URI in the format `gs://BUCKET_NAME/EXPORT_FOLDER`.



## What's next

  * [Manage applications](https://docs.cloud.google.com/application-design-center/docs/manage-applications).
  * [Deploy applications](https://docs.cloud.google.com/application-design-center/docs/deploy-applications).
  * [Download and deploy Terraform](https://docs.cloud.google.com/application-design-center/docs/download-and-deploy).
  * [Export Terraform code from the Google Cloud console](https://docs.cloud.google.com/application-design-center/docs/download-and-deploy#export_terraform_code).
  * [Publish an application template to a catalog](https://docs.cloud.google.com/application-design-center/docs/manage-catalogs#publish-an-application-template-to-a-catalog).
  * [Import components](https://docs.cloud.google.com/application-design-center/docs/import-components).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/application-design-center/docs/import-components/
title: Import components \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:55.963897+00:00
---

# Import components  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/import-components/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Import components Stay organized with collections  Save and categorize content based on your preferences. 

Application Design Center supports several Google Cloud products that you can add as components to your application. To use your own version of these components, or add other components, import your Terraform modules to App Design Center.

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Terraform modules are reusable configurations for Google Cloud products. Importing Terraform modules helps you do the following:

  * Accelerate and govern application development.
  * Reuse your existing design decisions in App Design Center.
  * Help application developers adhere to your established design policies.



When you import a Terraform module, App Design Center creates a corresponding component template in your space's catalog. You can then use the template as a component in your application template design.

To learn about Terraform on Google Cloud, see the following:

  * [Terraform overview](https://docs.cloud.google.com/docs/terraform/terraform-overview).
  * [Best practices for general style and structure](https://docs.cloud.google.com/docs/terraform/best-practices/general-style-structure).
  * [Best practices for reusable modules](https://docs.cloud.google.com/docs/terraform/best-practices/reusable-modules).



## Before you begin

To perform the tasks in this document, ask your administrator to grant you the necessary roles on the [app-enabled folder](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-enabled-folder) or [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project), as listed in the following table:

Task | Required roles  
---|---  
Import Terraform modules as custom components | Application Design Center Admin (`roles/designcenter.admin`), or  
Application Design Center User (`roles/designcenter.user`)  
  
For more information about roles, see [Access control with IAM](https://docs.cloud.google.com/application-design-center/docs/access-control).

## Configure and import your modules

Complete the following steps to connect to GitHub, create a metadata file, and import a Terraform module.

### Connect to your repository using Developer Connect

Create a Developer Connect connection to the GitHub repository where you store your Google Cloud Terraform modules. You'll use this connection when you import.

  1. Create a Developer Connect connection.

For steps, see [Connect to GitHub](https://docs.cloud.google.com/developer-connect/docs/connect-github-repo).

  2. Create a Developer Connect repository link.

For steps, see [Add repository links to existing connections](https://docs.cloud.google.com/developer-connect/docs/connect-github-repo#link-repos).




### Optional: Prepare your Terraform module metadata

When you import your Terraform module, you can supply your own metadata, or let App Design Center create a metadata file for you.

For example, the following is a `metadata.yaml` file that you might create for a service account:
    
    
      spec:
        info:
          actuationTool:
            flavor: Terraform
            version: ">= 1.3"
        interfaces: # Optional
          variables:
            - name: service_account
              connections:
                - source:
                    source: github.com/terraform-google/terraform-google-service-accounts
                    version: ">= 4.4"
                  spec:
                    outputExpr: email
        requirements:
          roles: # Optional after IAM integrations
            - level: Project
              roles:
                - roles/iam.serviceAccountUser
                - roles/iap.admin
                - roles/run.admin
                - roles/iam.serviceAccountAdmin
          providerVersions:
            - source: hashicorp/google
              version: ">= 6, < 7"
            - source: hashicorp/google-beta
              version: ">= 6, < 7"
        ui: # Optional
          input:
            variables:
              ca_root_module:
                name: ca_root_module
                title: CA Root Module
              service_account:
                name: service_account
                title: Service Account
    

### Import from your repository

You can create an App Design Center component by importing a Terraform module that is based on a single Google Cloud product. If you make changes to your Terraform module in your repository, repeat these steps to import your changes.

To import your Terraform module, do the following:

  1. Identify the catalog where you want to create your component.
         
         gcloud design-center spaces catalogs list \
           --project=PROJECT \
           --location=LOCATION \
           --space=SPACE
         

Replace the following:

     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
     * `SPACE`: Your space ID.

For more information, see [gcloud design-center spaces catalogs list](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/catalogs/list).

  2. Create a catalog template in your space's private catalog.
         
         gcloud design-center spaces catalogs templates create COMPONENT_TEMPLATE \
           --project=PROJECT \
           --catalog=CATALOG \
           --location=LOCATION \
           --space=SPACE \
           --template-category=component-template
         

Replace the following:

     * `COMPONENT_TEMPLATE`: The template ID for the component template that you want to create.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `CATALOG`: Your catalog ID.
     * `LOCATION`: Your location ID.
     * `SPACE`: Your space ID.

For more information, see [gcloud design-center spaces catalogs templates create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/catalogs/templates/create).

  3. Create a catalog template revision based on the Terraform module in your repository.
         
         gcloud design-center spaces catalogs templates revisions create REVISION \
           --project=PROJECT \
           --catalog=CATALOG \
           --location=LOCATION \
           --space=SPACE \
           --template=COMPONENT_TEMPLATE \
           --developer-connect-repo=DEVELOPER_CONNECT_REPO \
           --developer-connect-repo-ref=DEVELOPER_CONNECT_REPO_REF \
           --developer-connect-repo-dir=DEVELOPER_CONNECT_REPO_DIR \
           --metadata=METADATA
         
         

Replace the following:

     * `REVISION`: The revision ID for the revision that you want to create.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `CATALOG`: Your catalog ID.
     * `LOCATION`: Your location ID.
     * `SPACE`: Your space ID.
     * `COMPONENT_TEMPLATE`: The template ID that you created in the previous step.
     * `DEVELOPER_CONNECT_REPO`: The Developer Connect repository to use as a source. For example, `projects/my-project/locations/us-central1/connections/my-connection/gitRepositoryLinks/my-repo`.
     * `DEVELOPER_CONNECT_REPO_REF`: The Git branch or tag in the repository. For example, `refs/tags/v1.0.0` or `refs/heads/main`.
     * `DEVELOPER_CONNECT_REPO_DIR`: The directory in the repository. For example, `modules/my-product`.
     * To specify the Terraform module metadata, do one of the following: 
       * To use your own metadata file, replace `METADATA` with your `metadata.yaml` file.
       * To automatically use metadata files located in your repository, leave the --metadata flag unspecified.

For more information, see [gcloud design-center spaces catalogs templates revisions create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/catalogs/templates/revisions/create).

  4. Share your catalog with other spaces.
         
         gcloud design-center spaces catalogs shares create SHARE \
           --project=PROJECT \
           --catalog=CATALOG \
           --location=LOCATION \
           --space=SPACE \
           --destination-space=DESTINATION_SPACE
         

Replace the following:

     * `SHARE`: The share ID for the share that you want to create.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `CATALOG`: Your catalog ID.
     * `LOCATION`: Your location ID.
     * `SPACE`: Your space ID.
     * `DESTINATION_SPACE`: The destination space ID.

For more information, see [gcloud design-center spaces catalogs shares create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/catalogs/shares/create).




## Create an application template using imported components

Create an application template using your imported components and Google-provided components.

  1. Create a new application template.
         
         gcloud design-center spaces application-templates create APPLICATION_TEMPLATE \
           --project=PROJECT \
           --location=LOCATION \
           --space=SPACE
         

Replace the following:

     * `APPLICATION_TEMPLATE`: The template ID for the application template that you want to create.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
     * `SPACE`: Your space ID.

For more information, see [gcloud design-center spaces application-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/create).

  2. Identify the template revision URIs for the components that you want to add to the template.
         
         gcloud design-center spaces shared-templates list \
           --project=PROJECT \
           --location=LOCATION \
           --space=SPACE \
           --uri
         

Replace the following:

     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
     * `SPACE`: Your space ID.

For more information, see [gcloud design-center spaces shared-templates list](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/shared-templates/list).

  3. Add a component to your application template.
         
         gcloud design-center spaces application-templates components create COMPONENT \
           --project=PROJECT \
           --location=LOCATION \
           --space=SPACE \
           --application-template=APPLICATION_TEMPLATE \
           --shared-template-revision-uri=SHARED_TEMPLATE_URI
         

Replace the following:

     * `COMPONENT`: The component ID for the component that you want to add to the template.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
     * `SPACE`: Your space ID.
     * `APPLICATION_TEMPLATE`: The template ID for the application template where you are adding the component.
     * `SHARED_TEMPLATE_URI`: The component shared template URI. For example, `projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1`.

For more information, see [gcloud design-center spaces application-templates components create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/create).

  4. Add a second component to your template.
         
         gcloud design-center spaces application-templates components create COMPONENT_2 \
           --project=PROJECT \
           --location=LOCATION \
           --space=SPACE \
           --application-template=APPLICATION_TEMPLATE \
           --shared-template-revision-uri=SHARED_TEMPLATE_URI_2
         

Replace the following:

     * `COMPONENT_2`: The component ID for the second component that you want to add to the template.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
     * `SPACE`: Your space ID.
     * `APPLICATION_TEMPLATE`: The template ID for the application template where you are adding the component.
     * `SHARED_TEMPLATE_URI_2`: The second component shared template URI. For example, `projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1`.

For more information, see [gcloud design-center spaces application-templates components create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/create).

  5. Create a connection between the two components.
         
         gcloud design-center spaces application-templates components connections create CONNECTION \
           --project=PROJECT \
           --location=LOCATION \
           --space=SPACE \
           --application-template=APPLICATION_TEMPLATE \
           --component=COMPONENT \
           --destination-component-uri=SHARED_TEMPLATE_URI_2
         

Replace the following:

     * `CONNECTION`: The connection ID for the connection that you want to add to the template.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
     * `SPACE`: Your space ID.
     * `APPLICATION_TEMPLATE`: The template ID for the application template where you are adding the component.
     * `SHARED_TEMPLATE_URI_2`: The second component shared template URI. For example, `projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1`.

For more information, see [gcloud design-center spaces application-templates components connections create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/connections/create).




## What's next

  * Before you deploy, [create an application](https://docs.cloud.google.com/application-design-center/docs/manage-applications).
  * [Deploy applications](https://docs.cloud.google.com/application-design-center/docs/deploy-applications).
  * [Export](https://docs.cloud.google.com/application-design-center/docs/download-and-deploy) your Terraform code.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

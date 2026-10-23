---
url: https://docs.cloud.google.com/application-design-center/docs/download-and-deploy/
title: Download and deploy Terraform \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:31.770452+00:00
---

# Download and deploy Terraform  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/download-and-deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Download and deploy Terraform Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to download Terraform for a template or application you designed in Application Design Center. Use this option when you want to deploy the application with your own CI/CD tools.

If you download and deploy this code using your own tools, the exported Terraform files contain the logic to automatically register your application in App Hub. This capability enables runtime monitoring in [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview).

However, because you deploy the application externally, the application is treated as an unmanaged application. As a result, you cannot use [Application-centric Google Cloud](https://docs.cloud.google.com/application-design-center/docs/application-centric-google-cloud) features exclusive to managed applications, such as [design-time security assessments](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#verify-compliance) and [tracing security findings to their source](https://docs.cloud.google.com/application-design-center/docs/monitor-applications#monitor_security_compliance) for root-cause resolution.

If you want to take full advantage of application lifecycle management in App Design Center and use all Application-centric Google Cloud features, [deploy an application using App Design Center](https://docs.cloud.google.com/application-design-center/docs/deploy-applications).

The system generates the following Terraform files:

  * `main.tf`: Infrastructure code that includes a module for each component in the template.
  * `outputs.tf`: Exposes information about infrastructure components that are deployed.
  * `variables.tf`: Declares name, type, and description for variables used in the `main.tf` file.
  * `input.tfvars`: Defines values for variables used in the `main.tf` file.
  * [`providers.tf`](https://docs.cloud.google.com/docs/terraform/terraform-overview#providers): Defines labels that help Terraform interact with Google Cloud APIs and resources.



For background information, see [Overview of Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform/terraform-overview).

## Before you begin

To perform the tasks in this document, ask your administrator to grant you the necessary roles on the [app-enabled folder](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-enabled-folder) or [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project), as listed in the following table:

Task | Required roles  
---|---  
Export generated Terraform code locally or to a source control repository | Application Admin (`roles/designcenter.applicationAdmin`), or  
Application Editor (`roles/designcenter.applicationEditor`)  
  
For more information about roles, see [Access control with IAM](https://docs.cloud.google.com/application-design-center/docs/access-control).

## Export Terraform code

If you want to maintain your templates and applications outside of Google Cloud, you can generate Terraform and export to your local machine or to your code repository.

### Export locally

You can export Terraform code generated from a template or from an application.

### Template

  1. In the Google Cloud console, go to the **Templates** page.

[Go to Templates](https://console.cloud.google.com/products/design-center/templates)

  2. Click the **Template ID** that you want to export.

  3. Click **Get Code**.

The system downloads a zip file to your local computer. You can deploy the application using your own deployment tools and workflows.




### Application

  1. In the Google Cloud console, go to the **Applications** page.

[Go to Applications](https://console.cloud.google.com/products/design-center/applications)

  2. Click the **Application name** that you want to export.

  3. Click **Get Code**.

The system downloads a zip file to your local computer. You can deploy the application using your own deployment tools and workflows.




### Export to your repository

To maintain your templates through your source code management repository, you can export templates and applications to GitHub. You can then use your existing version control workflows, and trigger builds, tests, and deployments using your own CI/CD pipeline.

#### Connect to your repository

To create a Developer Connect connection between your GitHub repository and your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project), do the following:

  1. Change your organization policy to add the following services to your allowlist:

     1. `developerconnect.googleapis.com`.
     2. `secretmanager.googleapis.com`.

For steps to change your organization policy, see [Using the restrict resource service usage constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources#using_the_restrict_resource_service_usage_constraint).

  2. Create a Developer Connect connection to your GitHub repository, including the following:

     1. Select **Enable data residency**.
     2. Link the repository where you want to export your application.

For steps to create a connection and link a repository, see [Connect GitHub](https://docs.cloud.google.com/developer-connect/docs/connect-github-repo).

  3. To copy the repository URI, do the following:

     1. Open the **Developer Connect Git repositories** page.
     2. In the **Repositories** table, click **More Options** and select **Copy resource path**.



#### Generate and export

To generate Terraform code and export to your GitHub repository, do the following:

### Template

  1. Identify your space ID.
         
         gcloud design-center spaces list \
             --project=PROJECT \
             --location=LOCATION
         

Replace the following:

     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
  2. Identify the template ID for the template that you want to export.
         
         gcloud design-center spaces application-templates list \
             --space=SPACE \
             --project=PROJECT \
             --location=LOCATION
         

Replace the following:

     * `SPACE`: Your space ID.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
  3. Generate your template's Terraform code, and export to GitHub.
         
         gcloud design-center spaces application-templates generate APPLICATION_TEMPLATE \
             --space=SPACE \
             --project=PROJECT \
             --location=LOCATION \
             --developer-connect-export-config-repo-uri=DEVELOPER_CONNECT_EXPORT_CONFIG_REPO_URI \
             --developer-connect-export-config-dir=DEVELOPER_CONNECT_EXPORT_CONFIG_DIR \
             --developer-connect-export-config-branch=DEVELOPER_CONNECT_EXPORT_CONFIG_BRANCH
         

Replace the following:

     * `APPLICATION_TEMPLATE`: The template ID of the template that you want to export.
     * `SPACE`: Your space ID.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
     * `DEVELOPER_CONNECT_EXPORT_CONFIG_DIR`: The directory relative to your GitHub repository.
     * `DEVELOPER_CONNECT_EXPORT_CONFIG_BRANCH`: The branch in your GitHub repository.

For more information, see [gcloud design-center spaces application-templates generate](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/generate)

  4. View your repository to verify that the template was exported successfully.




### Application

  1. Identify your space ID.
         
         gcloud design-center spaces list \
             --project=PROJECT \
             --location=LOCATION
         

Replace the following:

     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
  2. Identify the application ID for the application that you want to export.
         
         gcloud design-center spaces applications list \
             --space=SPACE \
             --project=PROJECT \
             --location=LOCATION
         

Replace the following:

     * `SPACE`: Your space ID.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
  3. Generate your application's Terraform code, and export to GitHub.
         
         gcloud design-center spaces applications generate APPLICATION \
             --space=SPACE \
             --project=PROJECT \
             --location=LOCATION \
             --developer-connect-export-config-repo-uri=DEVELOPER_CONNECT_EXPORT_CONFIG_REPO_URI \
             --developer-connect-export-config-dir=DEVELOPER_CONNECT_EXPORT_CONFIG_DIR \
             --developer-connect-export-config-branch=DEVELOPER_CONNECT_EXPORT_CONFIG_BRANCH
         

Replace the following:

     * `APPLICATION`: The application ID of the application that you want to export.
     * `SPACE`: Your space ID.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: Your location ID.
     * `DEVELOPER_CONNECT_EXPORT_CONFIG_DIR`: The directory relative to your GitHub repository.
     * `DEVELOPER_CONNECT_EXPORT_CONFIG_BRANCH`: The branch in your GitHub repository.

For more information, see [gcloud design-center spaces applications generate](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/generate)

  4. View your repository to verify that the application was exported successfully.




## What's next

  * Get started with preconfigured architectures by [building on Google templates](https://docs.cloud.google.com/application-design-center/docs/build-on-google-templates).
  * Define your own configurations by [designing application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates).
  * Explore how to use Terraform on Google Cloud with the [Terraform on Google Cloud overview](https://docs.cloud.google.com/docs/terraform/terraform-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

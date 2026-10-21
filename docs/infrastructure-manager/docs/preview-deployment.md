---
url: https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment/
title: Preview a deployment \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:45:43.827546+00:00
---

# Preview a deployment  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Preview a deployment Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Infrastructure Manager to preview the deployment of resources defined in a Terraform configuration.

A preview describes the actions to actuate a specific Terraform configuration. Before you create a new deployment or update a deployment, you can preview the deployment to verify the resources that are planned to be provisioned.

A preview executes the `Terraform plan` command. This page assumes you are familiar with Terraform. For details, see [Terraform and Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform).

To create a preview, the Terraform configuration needs to be compatible with one of the supported [Terraform versions](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform_versions).

## Before you begin

  1. [Enable Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/enable-service).
  2. Ensure that you have the Identity and Access Management permissions needed to create previews: `roles/config.admin`.
  3. Ensure you have a service account with the needed permissions. For details, see [Configure the service account](https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account).
  4. Identify the Terraform configuration to preview. Ensure this Terraform configuration complies with the [constraints](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#constraints), including that the configuration does not contain sensitive data.
  5. If you want to store the Terraform configuration in a storage bucket, ensure the Terraform configuration is uploaded to a Cloud Storage bucket. See [Upload a configuration to a storage bucket](https://docs.cloud.google.com/infrastructure-manager/docs/upload-terraform-configuration) for more details.

A storage bucket lets you control access to the configuration. You can also deploy a Terraform configuration that is stored in a Git repository, or stored on your local machine.




## Preview a new deployment

The Terraform configuration that you preview can be in a storage bucket or in a Git repository.

### Preview using a Terraform configuration stored in a Cloud Storage bucket

  1. Ensure that the Terraform configuration is uploaded to a Cloud Storage bucket. See [Upload a configuration to a storage bucket](https://docs.cloud.google.com/infrastructure-manager/docs/upload-terraform-configuration) for more details.

A storage bucket lets you control access to the configuration. You can also deploy a Terraform configuration that is stored in a Git repository, or stored on your local machine.

  2. To preview the update:
         
         
         
         gcloud infra-manager previews create projects/PROJECT_ID/locations/LOCATION/previews/PREVIEW_ID \
         --service-account projects/SERVICE_ACCOUNT_PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT \
         --gcs-source gs://BUCKET_NAME/OBJECT_NAME \
         --input-values=INPUT_1_NAME=VALUE,INPUT_2_NAME=VALUE \
         --tf-version-constraint=TERRAFORM_VERSION \
         --annotations="ANNOTATION_KEY=ANNOTATION_VALUE" \
         --provider-source=SERVICE_MAINTAINED

`

Replace:

     * PROJECT_ID is the project ID where Infrastructure Manager runs.
     * LOCATION is the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
     * PREVIEW_ID is the preview identifier that you specify. See [Preview name](https://docs.cloud.google.com/infrastructure-manager/docs/deployments-revisions#preview_name) for details about constraints on the preview identifier.
     * SERVICE_ACCOUNT is the name of the service account you use to call Infra Manager.
     * SERVICE_ACCOUNT_PROJECT_ID is the project ID of the service account. It's common for this to be the same project where Infra Manager runs.
     * BUCKET_NAME is the name of the storage bucket where the configuration is stored.
     * OBJECT_NAME is the object name of configuration file. This object can be a directory or a zip file, but not a Terraform file. If you are using object versioning, you can also specify the object's generation number. For more details, see [Use versioned objects](https://docs.cloud.google.com/storage/docs/object-versioning).

If the storage bucket is the root path of the Terraform configuration, then OBJECT_NAME is optional.

     * INPUT_1_NAME=VALUE and INPUT_2_NAME=VALUE: any input values in the Terraform configuration, including ones that are not defined by default. For example, you could specify the project where you deploy the resources as `project_id=my-project`.

If all input values are defined by default in the configuration, then this flag is optional.

     * Optional: TERRAFORM_VERSION: the version of Terraform for Infra Manager to use to create the deployment. See [supported Terraform version](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform_versions) for the list of supported versions. If you remove this optional flag, the latest supported version of Terraform is used.

     * Optional: ANNOTATION_KEY and ANNOTATION_VALUE represent a key-value pair of free-form text that can be attached to your Infra Manager deployments. For more information about the use and constraints of annotations and labels, see [Annotations and labels](https://docs.cloud.google.com/infrastructure-manager/docs/annotations).

     * Optional: PROVIDER_SOURCE: Determines which Terraform provider for Google Cloud the deployment uses. Set to `SERVICE_MAINTAINED` to use the Infra Manager maintained Terraform provider. Omit this field to use the HashiCorp-maintained Terraform provider. For more information, see [Use the Terraform provider for Google Cloud](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform-provider).

Fields from the deployment like the Terraform configuration, variables, and service account are automatically merged into preview unless you specify new values in the preview command.




Now that you have created a preview, you can [export and view the results](https://docs.cloud.google.com/infrastructure-manager/docs/export-view-preview-results) to review the plan for the deployment.

### Preview using a Terraform configuration stored in a Git repository

When you update a deployment, some of the existing resources might not change. Previewing an update shows you what resources are planned to be provisioned or deleted and what resources are not planned to be modified.

To update a deployment stored in a Git repository:

  1. If you are using a private Git repository, ensure that you have connected to [your GitHub host](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github?generation=2nd-gen#gcloud) and [GitHub repository](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github?generation=2nd-gen#connecting_a_github_repository_2) using Cloud Build to provide Infra Manager access to your repository.

  2. To preview the deployment:
         
         
         
         gcloud infra-manager previews create projects/PROJECT_ID/locations/LOCATION/previews/PREVIEW_ID \
         --service-account projects/SERVICE_ACCOUNT_PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT \
         --git-source-repo="GIT_REPO" \
         --git-source-directory="DIRECTORY" \
         --git-source-ref="REF" \
         --input-values=INPUT_1_NAME=VALUE,INPUT_2_NAME=VALUE \
         --tf-version-constraint=TERRAFORM_VERSION \
         --annotations="ANNOTATION_KEY=ANNOTATION_VALUE" \
         --provider-source=SERVICE_MAINTAINED

`




Replace:

  * PROJECT_ID is the project ID where Infrastructure Manager runs.
  * LOCATION is the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * PREVIEW_ID is the preview identifier that you specify. See [Preview name](https://docs.cloud.google.com/infrastructure-manager/docs/deployments-revisions#preview_name) for details about constraints on the preview identifier.
  * SERVICE_ACCOUNT is the name of the service account you use to call Infra Manager.
  * SERVICE_ACCOUNT_PROJECT_ID is the project ID of the service account. It's common for this to be the same project where Infra Manager runs.
  * GIT_REPO: the Git repository.
  * DIRECTORY: the directory that has the Terraform configuration.
  * REF: the Git reference of the configuration. The reference is optional. If you don't specify the reference, the Git repository's default configured branch is used.
  * INPUT_1_NAME=VALUE and INPUT_2_NAME=VALUE: any input values in the Terraform configuration, including ones that are not defined by default. For example, you could specify the project where you deploy the resources as `project_id=my-project`.

If all input values are defined by default in the configuration, then this flag is optional.

  * Optional: TERRAFORM_VERSION: the version of Terraform for Infra Manager to use to create the deployment. See [supported Terraform version](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform_versions) for the list of supported versions. If you remove this optional flag, the latest supported version of Terraform is used.

  * Optional: ANNOTATION_KEY and ANNOTATION_VALUE represent a key-value pair of free-form text that can be attached to your Infra Manager deployments. For more information about the use and constraints of annotations and labels, see [Annotations and labels](https://docs.cloud.google.com/infrastructure-manager/docs/annotations).

  * Optional: PROVIDER_SOURCE: Determines which Terraform provider for Google Cloud the deployment uses. Set to `SERVICE_MAINTAINED` to use the Infra Manager maintained Terraform provider. Omit this field to use the HashiCorp-maintained Terraform provider. For more information, see [Use the Terraform provider for Google Cloud](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform-provider).



Fields from the deployment like the Terraform configuration, variables, and service account are automatically merged into preview unless you specify new values in the preview command.

Now that you have created a preview, you can [export and view the results](https://docs.cloud.google.com/infrastructure-manager/docs/export-view-preview-results) to review the plan for the deployment.

After preview a deployment, you can create the deployment to provision the resources. For details, see [deploy resources](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources).

## What's next

  * [Export and view preview results](https://docs.cloud.google.com/infrastructure-manager/docs/export-view-preview-results)
  * Use Infra Manager to [deploy resources](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources).
  * [Automate deployments](https://docs.cloud.google.com/infrastructure-manager/docs/automate-git).
  * Learn more about [Terraform with Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

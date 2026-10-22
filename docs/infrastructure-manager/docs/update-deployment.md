---
url: https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment/
title: Update a deployment \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:33.514366+00:00
---

# Update a deployment  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Update a deployment Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Infrastructure Manager to update a deployment. Cases where you may update a deployment include:

  * To return your infrastructure to a chosen state.

When you create a deployment, after some time resources may have changed. For example, some of the resources may have been modified by someone working in the console. You can update the deployment using the original Terraform configuration to return it to the chosen state.

  * To implement changes to the infrastructure.

After you create a deployment, you may want to modify the infrastructure. For example, adding new resources or changing some of the configuration. You can update the deployment using a Terraform configuration that describes the new infrastructure.




This page assumes you are familiar with Terraform. For details, see [Terraform and Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform).

## Before you begin

  1. Ensure [Infra Manager is enabled](https://docs.cloud.google.com/infrastructure-manager/docs/enable-service).
  2. Ensure that you have the IAM permissions needed to create deployments: `roles/config.admin`
  3. Ensure you have a service account with the needed permissions. For details, see [Configure the service account](https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account).
  4. Identify the Infra Manager deployment to update.
  5. Identify the Terraform configuration to deploy for the update. Any configuration can be used for a revision. This configuration is often an identical or updated version of the configuration already deployed.

Ensure this Terraform configuration complies with the [constraints](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#constraints), including that the configuration does not contain sensitive data.

  6. Confirm your organization's quota for products associated with your intended infrastructure. You may face deployment errors if your intended infrastructure exceeds your organization's quota for the products your deployment uses. See [quotas and limits](https://docs.cloud.google.com/infrastructure-manager/docs/quotas) for more information.

  7. Take any necessary steps for data migration or service continuity for the resources that you are modifying.

  8. If you want to preview the update before configuring resources, then see [Preview an update to a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment-update).




## Grant permissions specific to the configuration

To deploy Google Cloud resources that are specified in the Terraform configuration, the service account that you use to call Infra Manager needs permissions that are specific to:

  * Google Cloud resources defined in the configuration that you are using for the revision.

  * If the configuration you're using for the revision defines different resources than the configuration used for the deployment, then you need permissions for the resources defined in both configurations.




The permissions specific to the resources defined in the configuration are in addition to the permissions that the service account needs to use the Infra Manager service.

For details about granting permissions for the Google Cloud resources and ensuring you have access to the needed projects, see [Configure the service account](https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account).

### Connect your private Git repository and host to Cloud Build

If you are deploying a Terraform configuration from a _private Git repository_ , you need to connect your Git host and repository to Cloud Build.

#### GitHub

  * [Connect to your GitHub host using Cloud Build](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github?generation=2nd-gen#connecting_a_github_host).
  * [Connect to your GitHub repository using Cloud Build](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github?generation=2nd-gen#connecting_a_github_repository_2).



#### GitHub Enterprise

  * [Connect to your GitHub Enterprise host using Cloud Build](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-host-github-enterprise?generation=2nd-gen).
  * [Connect to your GitHub Enterprise repository using Cloud Build](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github-enterprise?generation=2nd-gen).



#### GitLab

  * [Connect to your GitLab host using Cloud Build](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab).
  * [Connect to your GitLab repository using Cloud Build](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-repo-gitlab).



#### GitLab Enterprise

  * [Connect to your GitLab Enterprise host using Cloud Build](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab-enterprise-edition).
  * [Connect to your GitLab Enterprise repository using Cloud Build](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-repo-gitlab-enterprise-edition).



#### Developer Connect

  * [Configure and use Developer Connect Git proxy](https://docs.cloud.google.com/developer-connect/docs/configure-git-proxy).



## Update a deployment

To update a deployment, you deploy a configuration using the same deployment name, and this creates a revision. For more details, see [Deployments and revisions overview](https://docs.cloud.google.com/infrastructure-manager/docs/deployments-revisions).

If you don't have an existing deployment, see [Deploy infrastructure using Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources).

To preview an update without provisioning resources, see [Preview a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment).

**Caution:** Infra Manager does not perform data migration or ensure service continuity. For example, if the revision deletes or replaces a database, it is your responsibility to manage data migration. Creating a revision can cause unrecoverable data loss. Re-applying the previous revision won't restore the data.

Select the tab with your chosen workflow for more information about how to update a deployment.

### Console

This section describes updating a Terraform configuration using Infra Manager in Google Cloud console.

Deploy the configuration and create a revision:

  1. In Google Cloud console, go to the **Infra Manager** page. 

[Go to Infra Manager](https://console.cloud.google.com/infra-manager)

  2. On the **Deployments** page, look in the **ID** column and click the deployment you want to update.
  3. On the page titled with your deployment ID, click **Edit**.
  4. On the **Deployment details** page, you can modify the **Terraform version** , **Service account** ,**** and the **Source of Terraform configuration** fields. If you provide a private Git repository, ensure that you have connected your host and repository to Cloud Build.

Click **Continue**.

**Note:** You can't modify the **Deployment ID** or **Location** parameters of a deployment after it has been created.
  5. On the **Terraform details** page, you can modify **Input values** for the Terraform configuration. Click **Continue**.
  6. On the **Advanced details** page, you can modify the **Labels and annotations** ,**Worker pools** , and **Artifact Cloud Storage bucket** fields.
  7. Click **Update** once you're satisfied with the changes you've made to your deployment to start the update process.



For more information about deployment parameters and their formats, see [Deploy resources](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources) documentation. 

### gcloud CLI

This section describes deploying a Terraform configuration that is stored in a Cloud Storage bucket. A storage bucket lets you control access to the configuration.

  1. Ensure the Terraform configuration is in a Cloud Storage bucket. See [Upload a configuration to a storage bucket](https://docs.cloud.google.com/infrastructure-manager/docs/upload-terraform-configuration) for more details.
  2. If the storage bucket is in a different project from the project where you are running Infra Manager, then you need to ensure that Infra Manager's service account has read permission for the bucket. See [Configure the service account](https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account) for more details.

If the storage bucket is in the same project as Infra Manager, read permission to the bucket is already enabled.

  3. Deploy the configuration and create a revision:
         
         gcloud infra-manager deployments apply projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID \
         --service-account projects/SERVICE_ACCOUNT_PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT \
         --gcs-source gs://BUCKET_NAME/OBJECT_NAME \
         --quota-validation=QUOTA_VALIDATION \
         --input-values=INPUT_1_NAME=VALUE,INPUT_2_NAME=VALUE \
         --tf-version-constraint=TERRAFORM_VERSION \
         --annotations="ANNOTATION_KEY=ANNOTATION_VALUE" \
         --provider-source=SERVICE_MAINTAINED


Replace: 
  * PROJECT_ID: the project ID where Infra Manager runs.
  * LOCATION: the location where Infra Manager runs. See [Infra Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * DEPLOYMENT_ID: the deployment identifier that you specify. See [Deployment name](https://docs.cloud.google.com/infrastructure-manager/docs/deployments-revisions#deployment_name) for details about constraints on the deployment identifier.
  * SERVICE_ACCOUNT_PROJECT_ID is the project ID of the service account. It's common for this to be the same project where Infra Manager runs.
  * SERVICE_ACCOUNT: the name of the service account you use to call Infra Manager.
  * BUCKET_NAME: the name of the storage bucket where the configuration is stored.
  * OBJECT_NAME: the object name of the configuration file. This object can be a directory or a zip file, but not a Terraform file. If you are using object versioning, you can also specify the object's generation number. For more details, see [Use versioned objects](https://docs.cloud.google.com/storage/docs/object-versioning). 

If the storage bucket is the root path of the Terraform configuration, then OBJECT_NAME is optional.

  * Optional: QUOTA_VALIDATION: the value that determines whether quota validation for resources in your Terraform configuration files is enabled or enforced when you create a deployment. Possible values include: 
    * `ENABLED`: Enable computing quota validation for resources in Terraform configuration files. Provides visibility on resources with insufficient quotas.
    * `ENFORCED`: Enforce quota validation so that your deployment will fail if there isn't sufficient quota available for the infrastructure defined in your Terraform configuration file.

If QUOTA_VALIDATION is not defined, quota validation on Terraform configuration files will be disabled. This is the default value. Quota validation applies on limited Google Cloud resources. For more information, see [Quotas and limits](https://docs.cloud.google.com/infrastructure-manager/docs/quotas#quota_validation).

  * INPUT_1_NAME and INPUT_2_NAME: any input values in the Terraform configuration, including ones that are not defined by default. For example, you could specify the project where you deploy the resources as `project_id=my-project`.

If all input values are defined by default in the configuration, then this flag is optional.

  * Optional:TERRAFORM_VERSION: the version of Terraform for Infra Manager to use to create the deployment. See [supported Terraform version](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform_versions) for the list of supported versions. If you remove this optional flag, the latest supported version of Terraform is used.
  * Optional: ANNOTATION_KEY and ANNOTATION_VALUE represent a key-value pair of free-form text that can be attached to your Infra Manager deployments. For more information about the use and constraints of annotations and labels, see [Annotations and labels](https://docs.cloud.google.com/infrastructure-manager/docs/annotations).

  * Optional: PROVIDER_SOURCE: Determines which Terraform provider for Google Cloud the deployment uses. Set to `SERVICE_MAINTAINED` to use the Infra Manager maintained Terraform provider. Omit this field to use the HashiCorp-maintained Terraform provider. For more information, see [Use the Terraform provider for Google Cloud](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform-provider).



### gcloud CLI

This section describes how to work with a Terraform configuration that is stored in a Git repository.

  1. Ensure that you have installed Git.
  2. If your Terraform configuration is stored in a private Git repository, ensure your Git host and repository are connected to Cloud Build.
  3. Deploy the configuration and create a revision:
         
         gcloud infra-manager deployments apply projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID \
         --service-account projects/SERVICE_ACCOUNT_PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT \
         --git-source-repo="GIT_REPO" \
         --git-source-directory="DIRECTORY" \
         --git-source-ref="REF" \
         --quota-validation=QUOTA_VALIDATION \
         --input-values=INPUT_1_NAME=VALUE,INPUT_2_NAME=VALUE \
         --tf-version-constraint=TERRAFORM_VERSION \
         --annotations="ANNOTATION_KEY=ANNOTATION_VALUE" \
         --provider-source=SERVICE_MAINTAINED


Replace: 
  * PROJECT_ID: the project ID where Infra Manager runs.
  * LOCATION: the location where Infra Manager runs. See [Infra Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * DEPLOYMENT_ID: the deployment identifier that you specify. See [Deployment name](https://docs.cloud.google.com/infrastructure-manager/docs/deployments-revisions#deployment_name) for details about constraints on the deployment identifier.
  * SERVICE_ACCOUNT_PROJECT_ID is the project ID of the service account. It's common for this to be the same project where Infra Manager runs.
  * SERVICE_ACCOUNT: the name of the service account you use to call Infra Manager.
  * GIT_REPO: the Git repository.
  * DIRECTORY: the directory that has the Terraform configuration.
  * Optional: REF: the Git reference of the configuration. The reference is optional. If you don't specify the reference, the Git repository's default configured branch is used.
  * Optional: QUOTA_VALIDATION: the value that determines whether quota validation for resources in your Terraform configuration files is enabled or enforced when you create a deployment. Possible values include: 
    * `ENABLED`: Enable computing quota validation for resources in Terraform configuration files. Provides visibility on resources with insufficient quotas.
    * `ENFORCED`: Enforce quota validation so that your deployment will fail if there isn't sufficient quota available for the infrastructure defined in your Terraform configuration file.

If QUOTA_VALIDATION is not defined, quota validation on Terraform configuration files will be disabled. This is the default value. Quota validation applies on limited Google Cloud resources. For more information, see [Quotas and limits](https://docs.cloud.google.com/infrastructure-manager/docs/quotas#quota_validation).

  * INPUT_1_NAME and INPUT_2_NAME: any input values in the Terraform configuration, including ones that are not defined by default. For example, you could specify the project where you deploy the resources as `project_id=my-project`.

If all input values are defined by default in the configuration, then this flag is optional.

  * Optional:TERRAFORM_VERSION: the version of Terraform for Infra Manager to use to create the deployment. See [supported Terraform version](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform_versions) for the list of supported versions. If you remove this optional flag, the latest supported version of Terraform is used.
  * Optional: ANNOTATION_KEY and ANNOTATION_VALUE represent a key-value pair of free-form text that can be attached to your Infra Manager deployments. For more information about the use and constraints of annotations and labels, see [Annotations and labels](https://docs.cloud.google.com/infrastructure-manager/docs/annotations).

  * Optional: PROVIDER_SOURCE: Determines which Terraform provider for Google Cloud the deployment uses. Set to `SERVICE_MAINTAINED` to use the Infra Manager maintained Terraform provider. Omit this field to use the HashiCorp-maintained Terraform provider. For more information, see [Use the Terraform provider for Google Cloud](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform-provider).



### gcloud CLI

This section describes how to work with a Terraform configuration that is stored on your local machine.

  1. If you use Cloud Shell, then you need to upload the configuration to Cloud Shell. For details, see [Manage files with Cloud Shell](https://docs.cloud.google.com/shell/docs/uploading-and-downloading-files).
  2. Deploy the configuration and create a revision:
         
         gcloud infra-manager deployments apply projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID \
         --service-account projects/SERVICE_ACCOUNT_PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT \
         --local-source="LOCAL_DIRECTORY" \
         --quota-validation=QUOTA_VALIDATION \
         --input-values=INPUT_1_NAME=VALUE,INPUT_2_NAME=VALUE \
         --tf-version-constraint=TERRAFORM_VERSION \
         --annotations="ANNOTATION_KEY=ANNOTATION_VALUE" \
         --provider-source=SERVICE_MAINTAINED


Replace: 
  * PROJECT_ID: the project ID where Infra Manager runs.
  * LOCATION: the location where Infra Manager runs. See [Infra Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * DEPLOYMENT_ID: the deployment identifier that you specify. See [Deployment name](https://docs.cloud.google.com/infrastructure-manager/docs/deployments-revisions#deployment_name) for details about constraints on the deployment identifier.
  * SERVICE_ACCOUNT_PROJECT_ID is the project ID of the service account. It's common for this to be the same project where Infra Manager runs.
  * SERVICE_ACCOUNT: the name of the service account you use to call Infra Manager.
  * LOCAL_DIRECTORY: the local directory storing the Terraform configuration. If you are using Cloud Shell, this is the directory in Cloud Shell where the configuration is stored.
  * Optional: QUOTA_VALIDATION: the value that determines whether quota validation for resources in your Terraform configuration files is enabled or enforced when you create a deployment. Possible values include: 
    * `ENABLED`: Enable computing quota validation for resources in Terraform configuration files. Provides visibility on resources with insufficient quotas.
    * `ENFORCED`: Enforce quota validation so that your deployment will fail if there isn't sufficient quota available for the infrastructure defined in your Terraform configuration file.

If QUOTA_VALIDATION is not defined, quota validation on Terraform configuration files will be disabled. This is the default value. Quota validation applies on limited Google Cloud resources. For more information, see [Quotas and limits](https://docs.cloud.google.com/infrastructure-manager/docs/quotas#quota_validation).

  * INPUT_1_NAME and INPUT_2_NAME: any input values in the Terraform configuration, including ones that are not defined by default. For example, you could specify the project where you deploy the resources as `project_id=my-project`.

If all input values are defined by default in the configuration, then this flag is optional.

  * Optional:TERRAFORM_VERSION: the version of Terraform for Infra Manager to use to create the deployment. See [supported Terraform version](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform_versions) for the list of supported versions. If you remove this optional flag, the latest supported version of Terraform is used.
  * Optional: ANNOTATION_KEY and ANNOTATION_VALUE represent a key-value pair of free-form text that can be attached to your Infra Manager deployments. For more information about the use and constraints of annotations and labels, see [Annotations and labels](https://docs.cloud.google.com/infrastructure-manager/docs/annotations).

  * Optional: PROVIDER_SOURCE: Determines which Terraform provider for Google Cloud the deployment uses. Set to `SERVICE_MAINTAINED` to use the Infra Manager maintained Terraform provider. Omit this field to use the HashiCorp-maintained Terraform provider. For more information, see [Use the Terraform provider for Google Cloud](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform-provider).



## What's next

  * Learn more about [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).
  * [Automate deployments](https://docs.cloud.google.com/infrastructure-manager/docs/automate-git).
  * [View the state of a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments).
  * [View resources deployed](https://docs.cloud.google.com/infrastructure-manager/docs/view-resources).
  * [Delete a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/delete-deployments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account/
title: Configure the service account \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:45:46.035763+00:00
---

# Configure the service account  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Configure the service account Stay organized with collections  Save and categorize content based on your preferences. 

To use Infrastructure Manager to create, update, or delete a deployment, you must use a service account. Infra Manager executes Terraform using the identity of this service account.

You do not need a service account to view information about Infra Manager deployments.

This page explains how to configure a service account so that you can deploy resources with Infrastructure Manager.

## Before you begin

  1. [Enable the Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/enable-service) service.
  2. [Create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) or identify an existing service account to use with Infra Manager.



## Grant access to the service account

To use Infrastructure Manager to create, update, or delete a deployment, an individual user needs access to the service account.

Grant the user the [Service Account User (`roles/iam.serviceAccountUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) IAM role for the service account.

## Grant permissions for Infra Manager

To work with Infra Manager, the service account needs the [Infra Manager Agent (`roles/config.agent`) role](https://docs.cloud.google.com/infrastructure-manager/docs/access-control). This grants permissions for Infra Manager to create, update, and delete resources:
    
    
       gcloud projects add-iam-policy-binding INFRA_MANAGER_PROJECT_ID \
          --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
          --role="roles/config.agent"
    

Replace:

  * INFRA_MANAGER_PROJECT_ID: The project ID of the project where you're creating deployments.

  * SERVICE_ACCOUNT_EMAIL: The email of the service account.




For details about how to grant permissions to service accounts, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

## Grant read permission for the storage bucket

You can use a storage bucket to store the Terraform configurations that are deployed by Infra Manager.

If you use a storage bucket for the configurations, and this storage bucket is in a different project from the project where you are running Infra Manager, then you need to ensure that the service account that you use to call Infra Manager has read permission for the bucket. For details about Cloud Storage permissions, see [IAM permissions for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-permissions).

If the storage bucket is in the same project as Infra Manager, and you have granted `roles/config.agent` to the service account, then read permission to the bucket is already enabled.

For details about uploading a configuration to a storage bucket, see [Upload a Terraform configuration](https://docs.cloud.google.com/infrastructure-manager/docs/upload-terraform-configuration).

## Grant permissions for resources defined in the configuration

To create and manage Google Cloud resources that are defined in the Terraform configuration, the service account needs permissions specific to these resources.

  * Permissions specific to the Google Cloud resources that are defined in the Terraform configuration you are deploying. For example, the permission for creating a Compute Engine VM instance is `compute.instances.create`.

  * Permissions specific to the Google Cloud resources that are defined in the Terraform configuration of the deployment that you are updating.

For example, let's say your deployment provisions a Compute Engine VM and then you update the deployment using a configuration that does not include a Compute Engine VM. In this case, when you update the revision, the service account needs:

    * Permissions for the resources defined in the new configuration.

    * Permissions for the resources being deleted, such as the Compute Engine VM in this example.




For help identifying the permissions needed for the resources in the Terraform configurations, see [Choose predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).

For details about how to grant permissions to service accounts, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

## Grant access across multiple projects

Additional permissions are required if the given service account is in a different project than the project where the Infra Manager service is run.

To grant these additional permissions:

  1. Ensure that the service account has the [Infra Manager Agent (`roles/config.agent`) role](https://docs.cloud.google.com/infrastructure-manager/docs/access-control) in the project running Infra Manager. See Grant permissions for Infra Manager for instructions on granting permissions.

  2. Optional: If you are using [Developer Connect](https://docs.cloud.google.com/developer-connect/docs/overview) to deploy a Terraform configuration, grant the `roles/iam.serviceAccountTokenCreator` role to the service account.

  3. In the project that has the service account, ensure that the `iam.disableCrossProjectServiceAccountUsage` organization policy constraint is not enforced. This constraint is enforced by default.

To disable this organization policy constraint, run:
         
         gcloud resource-manager org-policies disable-enforce iam.disableCrossProjectServiceAccountUsage
                --project=SERVICE_ACCOUNT_PROJECT_ID
         

Replace SERVICE_ACCOUNT_PROJECT_ID with the ID of the project that contains the service account.

  4. In the project that has the service account, grant the `roles/iam.serviceAccountUser` role for the Infra Manager service agent of the project where you're creating deployments:
         
         gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
            --member="serviceAccount:service-INFRA_MANAGER_PROJECT_NUMBER@gcp-sa-config.iam.gserviceaccount.com" \
            --role="roles/iam.serviceAccountUser"
         

Replace:

     * SERVICE_ACCOUNT_PROJECT_ID: The project ID of the project that contains the service account.
     * INFRA_MANAGER_PROJECT_NUMBER: The project number of the project where you're creating deployments. This forms the email ID of the service agent: `service-INFRA_MANAGER_PROJECT_NUMBER@gcp-sa-config.iam.gserviceaccount.com`
  5. Grant the [Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`)](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) role to the Cloud Build service agent in the project where you're creating deployments. To allow Infra Manager to execute Terraform using Cloud Build, the Cloud Build service agent in the project containing the service account needs additional permissions as part of the [cross-project set up](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts#cross-project_set_up):
         
         gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
             --member="serviceAccount:service-INFRA_MANAGER_PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com" \
              --role="roles/iam.serviceAccountTokenCreator"
         




## What's next

  * Learn about [IAM](https://docs.cloud.google.com/iam/docs).
  * Learn more about [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).
  * [Deploy infrastructure using Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources).
  * [Update a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment).
  * [View the state of a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

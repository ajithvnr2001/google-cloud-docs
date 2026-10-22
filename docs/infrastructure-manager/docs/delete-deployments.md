---
url: https://docs.cloud.google.com/infrastructure-manager/docs/delete-deployments/
title: Delete a deployment \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:18.851868+00:00
---

# Delete a deployment  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/delete-deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Delete a deployment Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete an Infrastructure Manager deployment.

This page assumes you are familiar with Terraform. For details, see [Terraform and Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform).

## Before you begin

  1. Ensure [Infra Manager is enabled](https://docs.cloud.google.com/infrastructure-manager/docs/enable-service).
  2. Ensure that you have the IAM permissions needed to create deployments: `roles/config.admin`.
  3. Ensure the service account that was last used to create or update the deployment is still valid. Infra Manager uses this service account to delete the deployment. 
     * For details about configuring the service account, including setting up required permissions, see [Configure the service account](https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account).
     * To determine the service account that was last used for the deployment, see [View the state of a revision](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments#revision-details).
  4. Ensure the Terraform configuration that Infra Manager used to create or update the deployment is still valid. Infra Manager uses this configuration to delete the deployment.
  5. Identify the Infra Manager deployment to delete.
  6. Ensure that the service account has the IAM permissions needed to delete resources in the specified projects and locations.



## Grant permissions specific to the configuration

To delete Google Cloud resources in a specific deployment, the service account that you use to call Infra Manager needs permissions that are specific to what you are deleting.

These permissions are in addition to the permissions needed to use the Infra Manager service.

For details about granting permissions for the Google Cloud resources and ensuring you have access to the needed projects, see [Configure the service account](https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account).

## Delete a deployment

When an Infra Manager deployment is created, Infra Manager stores metadata about the deployment, the Terraform configuration that is deployed, and the state file.

When you delete a deployment, you delete this metadata and files. You can also delete the resources provisioned by the deployment, or keep these resources.

### Delete provisioned resources

**Caution:** Deleting Google Cloud resources can cause unrecoverable data loss. Re-deploying the configuration won't restore data.

To delete the deployment metadata and delete the provisioned resources:

  1. Optionally, list the resources provisioned by the deployment:
         
         gcloud infra-manager resources list --revision=projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID/revisions/REVISION_ID
         

Replace the following:

     * PROJECT_ID: the project ID where Infrastructure Manager runs.
     * LOCATION: the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
     * DEPLOYMENT_ID: the deployment identifier that you specify. See [Deployment name](https://docs.cloud.google.com/infrastructure-manager/docs/overview#deployments) for details about constraints on the deployment identifier.
     * REVISION_ID: the revision ID representing a specific revision of a deployment. See [Deployment name](https://docs.cloud.google.com/infrastructure-manager/docs/overview#deployments) for details about constraints on the revision identifier.
  2. Preview the deletion of the resources. For details, see [Preview a deletion of a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment-deletion).

  3. Delete the deployment and provisioned resources:
         
         gcloud infra-manager deployments delete projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID
         

Replace the following:

     * PROJECT_ID: the project ID where Infrastructure Manager runs.
     * LOCATION: the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
     * DEPLOYMENT_ID: the deployment identifier that you specify. See [Deployment name](https://docs.cloud.google.com/infrastructure-manager/docs/overview#deployments) for details about constraints on the deployment identifier.



### Keep provisioned resources

You may want to delete the deployment and keep the Google Cloud resources that were provisioned by the deployment.

For example, you deploy a configuration from the [Terraform blueprints and modules for Google Cloud](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints). Once it's deployed, you want to manage the resources through the console, and not use Infrastructure as Code (IaC). In this case, you may want to delete the deployment as you don't have use for the deployment's metadata.

**Note:** After you delete the deployment, Infra Manager is not able to identify or manage the Google Cloud resources that are kept.

To delete the deployment metadata and keep the provisioned resources:
    
    
    gcloud infra-manager deployments delete projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID \
        --delete-policy=abandon
    

Replace the following:

  * PROJECT_ID: the project ID where Infrastructure Manager runs.
  * LOCATION: the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * DEPLOYMENT_ID: the deployment identifier that you specify. See [Deployment name](https://docs.cloud.google.com/infrastructure-manager/docs/overview#deployments) for details about constraints on the deployment identifier.



## What's next

  * Learn more about [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).
  * [View the state of a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments).
  * [View resources deployed](https://docs.cloud.google.com/infrastructure-manager/docs/view-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

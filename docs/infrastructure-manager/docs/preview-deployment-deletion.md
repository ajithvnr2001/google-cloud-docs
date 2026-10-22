---
url: https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment-deletion/
title: Preview a deletion of a deployment \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:02.609250+00:00
---

# Preview a deletion of a deployment  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment-deletion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Preview a deletion of a deployment Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Infrastructure Manager to preview the deletion of an existing deployment.

A preview describes the actions to actuate a specific Terraform configuration. Before you delete a deployment, you can use a preview to verify the resources that are planned to be deleted.

A preview does not delete any provisioned resources. To delete a deployment, including deleting provisioned resources, see [Delete deployments](https://docs.cloud.google.com/infrastructure-manager/docs/delete-deployments).

A preview executes the `Terraform plan` command. This page assumes you are familiar with Terraform. For details, see [Terraform and Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform).

## Before you begin

  1. [Enable Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/enable-service).
  2. Ensure that you have the IAM permissions needed to create previews: `roles/config.admin`.
  3. Ensure you have a service account with the needed permissions. For details, see [Configure the service account](https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account).
  4. Identify the Terraform configuration to preview. Ensure this Terraform configuration complies with the [constraints](https://docs.cloud.google.com/infrastructure-manager/docs/terraform#constraints), including that the configuration does not contain sensitive data.
  5. If you want to store the Terraform configuration in a storage bucket, ensure the Terraform configuration is uploaded to a Cloud Storage bucket. See [Upload a configuration to a storage bucket](https://docs.cloud.google.com/infrastructure-manager/docs/upload-terraform-configuration) for more details.

A storage bucket lets you control access to the configuration. You can also deploy a Terraform configuration that is stored in a public Git repository, or stored on your local machine.




## Preview the deletion of a deployment

Before you delete a deployment, you can preview and review the deletion.

To preview the deletion of a deployment:
    
    
    gcloud infra-manager previews create --preview-mode DELETE --deployment=projects/PROJECT_ID/locations/LOCATION/previews/DEPLOYMENT_ID \
        --service-account projects/SERVICE_ACCOUNT_PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT \
    

Replace:

  * PROJECT_ID is the project ID where Infrastructure Manager runs.
  * LOCATION is the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * PREVIEW_ID is the preview identifier that you specify. See [Preview name](https://docs.cloud.google.com/infrastructure-manager/docs/deployments-revisions#preview_name) for details about constraints on the preview identifier.
  * SERVICE_ACCOUNT is the name of the service account you use to call Infra Manager.
  * SERVICE_ACCOUNT_PROJECT_ID is the project ID of the service account. It's common for this to be the same project where Infra Manager runs.
  * DEPLOYMENT_ID is the deployment identifier of the deployment you want to update.



Now that you have created a preview, you can [export and view the results](https://docs.cloud.google.com/infrastructure-manager/docs/export-view-preview-results) to review the plan for the deployment.

For more information about deleting deployments, see [Delete a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/delete-deployments).

## What's next

  * [Export and view preview results](https://docs.cloud.google.com/infrastructure-manager/docs/export-view-preview-results)
  * [Delete a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/delete-deployments).
  * [Create a new preview](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment).
  * [Automate deployments](https://docs.cloud.google.com/infrastructure-manager/docs/automate-git).
  * Learn more about [Terraform with Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

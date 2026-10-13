---
url: https://docs.cloud.google.com/infrastructure-manager/docs/export-view-preview-results/
title: Export and view preview results \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:44.946931+00:00
---

# Export and view preview results  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/export-view-preview-results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Export and view preview results Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to export and review the results of a preview. A preview describes the actions to actuate a specific Terraform configuration. Before you create a new deployment or update a deployment, you can preview the deployment to verify what is planned to change.

If you have not yet created the preview that you want to view, see [Preview a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment).

This page assumes you are familiar with Terraform. For details, see [Terraform and Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform).

## Before you begin

  1. [Enable Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/enable-service).
  2. Ensure that you have the IAM permissions needed to export previews: `roles/config.admin`.
  3. Create a [preview deployment](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment).



## Export the results of the preview

To review the results of a preview, first export the results. Then, view the exported results using an appropriate tool.

To export a preview, its state must be `SUCCEEDED` or `STALE`. You can view the current state of a preview using the [describe or list commands](https://docs.cloud.google.com/infrastructure-manager/docs/list-preview).

Export the results of a preview and save it locally using the following command:
    
    
    gcloud infra-manager previews export projects/PROJECT_ID/locations/LOCATION/previews/PREVIEW_ID
    

Replace:

  * PROJECT_ID: the project ID where Infrastructure Manager runs.
  * LOCATION: the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * PREVIEW_ID: the preview identifier that you specify. See [Preview name](https://docs.cloud.google.com/infrastructure-manager/docs/deployments-revisions#preview_name) for details about constraints on the preview identifier.



## View the results of the preview

The results are exported in two formats: the _binary plan file_ , and the _JSON representation_. You can use either format to review the results. To view the results, use an appropriate tool for the format.

**Note:** If you export the results of a preview in the binary plan file format, you need to have your Terraform configuration stored locally, and run `terraform init` on the configuration before you can view the results.

### Review the binary plan file

To view the binary plan file:

  1. Verify that you have the [Terraform CLI](https://developer.hashicorp.com/terraform/cli) installed.

  2. Verify that the Terraform configuration that you used to create the preview is present locally and initialized with `terraform init`.

  3. Print the proposed plan using [`terraform show`](https://developer.hashicorp.com/terraform/cli/commands/show).




### Review the JSON representation

To view the JSON representation, you can use your IDE or tools like [jq](https://jqlang.github.io/jq/).

To enforce policy constraints you can use JSON representation with tools like [Terraform vet](https://cloud.google.com/docs/terraform/policy-validation/quickstart).

## View resource change and drift details

You can use previews to view resource drift for your deployment. Viewing resource drift for your deployments is useful to verify that changes to your configurations are intended, and to summarize _how your deployment will change_ when your deployment is updated with a particular preview.

When you create a preview, you use the Infra Manager API to view changes to your resources as you update your deployments.

### View resource drift

To view a list of resource drifts of a preview deployment:
    
    
    gcloud infra-manager resource-drifts list --preview=projects/PROJECT_ID/locations/LOCATION/previews/PREVIEW_ID
    

Replace:

  * PROJECT_ID: The identifier of the Google Cloud project where your preview deployment is located.
  * LOCATION: The region or zone of your preview deployment.
  * PREVIEW_ID: The identifier of your preview deployment.

**Note:** Infra Manager resource drifts are structured versions of `resource_drift` in the [`terraform plan` representation](https://developer.hashicorp.com/terraform/internals/json-format#plan-representation).

### View details of a drift

To view details of a resource drift from a preview deployment:
    
    
    gcloud infra-manager resource-drifts describe projects/PROJECT_ID/locations/LOCATION/previews/PREVIEW_ID/resourceDrifts/RESOURCE_DRIFT_ID
    

Replace:

  * PROJECT_ID: The identifier of the Google Cloud project where your preview deployment is located.
  * LOCATION: The region or zone of your preview deployment.
  * PREVIEW_ID: The identifier of your preview deployment.
  * RESOURCE_DRIFT_ID: The identifier of your drift.



## Preview resource changes

You can use previews to check how your resources will change if you update a deployment from your preview.

### View resource changes

To view a list of resource changes of a preview deployment:
    
    
    gcloud infra-manager resource-changes list --preview=projects/PROJECT_ID/locations/LOCATION/previews/PREVIEW_ID
    

Replace:

  * PROJECT_ID: The identifier of the Google Cloud project where your preview deployment is located.
  * LOCATION: The region or zone of your preview deployment.
  * PREVIEW_ID: The identifier of your preview deployment.

**Note:** Infra Manager resource changes are structured versions of `resource_changes` in the [`terraform plan` representation](https://developer.hashicorp.com/terraform/internals/json-format#plan-representation).

### View details of a resource change

To view details of a resource change from a preview deployment:
    
    
    gcloud infra-manager resource-changes describe projects/PROJECT_ID/locations/LOCATION/previews/PREVIEW_ID/resourceChanges/RESOURCE_CHANGE_ID
    

Replace:

  * PROJECT_ID: The identifier of the Google Cloud project where your preview deployment is located.
  * LOCATION: The region or zone of your preview deployment.
  * PREVIEW_ID: The identifier of your preview deployment.
  * RESOURCE_CHANGE_ID: The identifier of your resource change.



## What's next

  * [View and list previews](https://docs.cloud.google.com/infrastructure-manager/docs/list-preview).
  * [Deploy resources](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources).
  * Learn more about [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).
  * [Update a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment).
  * [View the state of a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments).
  * [View resources deployed](https://docs.cloud.google.com/infrastructure-manager/docs/view-resources).
  * [Delete a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/delete-deployments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

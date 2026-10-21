---
url: https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments/
title: View deployments \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:45:45.000884+00:00
---

# View deployments  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  View deployments Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view information about deployments, including:

  * Listing deployments in a project.
  * Viewing details of a deployment, including the following: 
    * The state of the deployment.
    * The version of Terraform used to create the deployment.
  * Listing revisions in a deployment.
  * Viewing details of a revision, including the following: 
    * The state of the revision.
    * The version of Terraform used to create the revision.



## Before you begin

  1. Ensure [Infra Manager is enabled](https://docs.cloud.google.com/infrastructure-manager/docs/enable-service).
  2. Ensure that you have the IAM permissions needed to view deployments: 
     * `roles/config.admin` or `roles/config.viewer`.



## List deployments in a project

Deployments are specific to a project and [location](https://docs.cloud.google.com/infrastructure-manager/docs/locations). You can list the deployments if you want to assess which deployments exist.

To list the deployments in a project and location, use the following command:
    
    
    gcloud infra-manager deployments list --project PROJECT_ID --location "LOCATION"
    

Replace the following:

  * PROJECT_ID: the project ID where Infrastructure Manager runs.
  * LOCATION with the location where the deployments exist. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.



## View details of a deployment

After you create a deployment, you might want to view details about the deployment, including the following:

  * The state of the deployment. View the state to verify if the deployment was successful, failed, or had any issues such as a partial deployment.
  * The version of Terraform that Infra Manager used to create the deployment.



To view details of a deployment, use the following command:
    
    
    gcloud infra-manager deployments describe projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID
    

Replace the following:

  * PROJECT_ID: the project ID where Infrastructure Manager runs.
  * LOCATION: the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * DEPLOYMENT_ID: the deployment identifier of the deployment you're viewing.



For the list of possible states and details about each state, see [State](https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.deployments#State) in the REST API reference.

The version of Terraform used to create the deployment is listed in the output next to `tfVersion`. For more information, see [Supported Terraform versions](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform_versions).

To troubleshoot failed deployments, see [Troubleshoot deployment errors](https://docs.cloud.google.com/infrastructure-manager/docs/troubleshoot-deployments).

## List revisions in a deployment

You might want to see the list of the different revisions that a deployment has gone through.

To list the revisions in a deployment, use the following command:
    
    
    gcloud infra-manager revisions list --deployment=projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID
    

Replace the following:

  * PROJECT_ID: the project ID where Infrastructure Manager runs.
  * LOCATION: the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * DEPLOYMENT_ID: the deployment identifier of the deployment you're viewing.



## View details of a revision

To view details of a specific revision, use the following command:
    
    
    gcloud infra-manager revisions describe projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID/revisions/REVISION_ID
    

Replace the following:

  * PROJECT_ID: the project ID where Infrastructure Manager runs.
  * LOCATION: the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * DEPLOYMENT_ID: the deployment identifier of the deployment you're viewing.
  * REVISION_ID: the revision identifier of the revision you're viewing.



For the list of possible states and details about each state, see [State](https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.deployments.revisions#state) in the REST API reference.

The version of Terraform used to create the revision is listed in the output next to `tfVersion`. For more details, see [Supported Terraform versions](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform_versions).

To troubleshoot failed deployments, which includes failed revisions, see [Troubleshoot deployment errors](https://docs.cloud.google.com/infrastructure-manager/docs/troubleshoot-deployments).

## What's next

  * Learn more about [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).
  * [Automate deployments](https://docs.cloud.google.com/infrastructure-manager/docs/automate-git).
  * [Update a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment).
  * [View resources deployed](https://docs.cloud.google.com/infrastructure-manager/docs/view-resources).
  * [Delete a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/delete-deployments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/infrastructure-manager/docs/deployments-revisions/
title: Deployments, revisions, and previews overview \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:43.922685+00:00
---

# Deployments, revisions, and previews overview  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/deployments-revisions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Deployments, revisions, and previews overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes deployments and revisions, including the following:

  * List of metadata stored for each deployment.
  * The format of the deployment name and revision name.



## Deployments

Infra Manager provisions resources onto Google Cloud as a deployment.

A deployment can provision Google Cloud resources to multiple locations and to multiple projects. Note that:

  * The specific resources need to be available in the locations. For example, see [Cloud Run locations](https://docs.cloud.google.com/run/docs/locations) for the list of locations where Cloud Run is available.
  * The service account must have the permissions that are required to deploy to the specified projects. For details, see [Configure the service account](https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account).



### Deployment metadata

Infra Manager creates a storage bucket in the project and location where Infra Manager is run. After the deployment is created, the Infrastructure Manager artifacts are in this storage bucket which has the name: `gs://PROJECT_NUMBER-LOCATION-blueprint-config`.

For deployments created in a multi-region, this storage bucket is created with multi-regional redundancy. For example, if a deployment is created in the `us` multi-region, then the storage bucket is created across data centers in the United States.

Infra Manager uses the term _blueprint_ to refer to a Terraform configuration.

Where you replace the following:

  * PROJECT_ID: the project ID where Infra Manager is run.
  * LOCATION: the location where Infra Manager is run. 



The deployment artifacts in the storage bucket include:

  * Cloud Build logs.
  * Terraform logs.
  * A copy of the Terraform configuration.



Infra Manager also stores a copy of the Terraform state file. For details about the state file, including accessing the file, see [Manage the Terraform state file](https://docs.cloud.google.com/infrastructure-manager/docs/state-file).

Revisions are versions of a deployment, so Infra Manager stores this deployment metadata for each revision.

### Deployment ID

The deployment ID is the user-specified identifier for a deployment resource. Use the deployment ID to refer to a deployment using the format:
    
    
    projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID
    

Replace the following:

  * PROJECT_ID is the project ID where Infra Manager runs.
  * LOCATION is the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * DEPLOYMENT_ID is the deployment ID, which is a user-specified name. This ID must: 
    * Contain only lowercase letters, numbers, or hyphens.
    * Start with a lowercase letter.
    * End with a number or lowercase letter
    * Cannot be the string `archived-deployments` or `archived-previews`
    * Must be unique within the project and location where Infra Manager is run.



For example:
    
    
    projects/my-project/locations/us-central1/deployments/my-deployment
    

## Revisions

Revisions are versions of a deployment. When you initially create a deployment, this deployment is also a revisions and has the revision ID `r-0`.

### Revision name

When you create an Infra Manager deployment, it is automatically given the revision identifier `r-0`. If you update the deployment, then Infrastructure Manager creates a new revision with identifier `r-1`. For every new revision, the identifier increases by one. The revision identifier can only be set by Infrastructure Manager.

For example, a revision name could be:
    
    
    projects/my-project/locations/us-central1/deployments/my-deployment/revisions/r-1
    

## Previews

A preview describes the actions to actuate a specific Terraform configuration. Before you create a new deployment or update a deployment, you can preview the deployment to verify the resources that are planned to be provisioned.

### Preview metadata

Infra Manager creates a storage bucket in the project and location where Infra Manager is run. After the preview is created, the Infra Manager artifacts are in this storage bucket which has the name: `gs://PROJECT_NUMBER-LOCATION-blueprint-config`.

For a preview of a new deployment, the metadata is organized with a `new-previews` prefix, for example: `gs://PROJECT_NUMBER-LOCATION-blueprint-config/new-previews/preview-name`

You can also preview an update to an existing deployment. For these previews targeting an existing deployment, the artifacts are stored in the same storage bucket as the deployment artifacts. The storage bucket which has the name: `gs://PROJECT_ID-LOCATION-blueprint-config/deployment-ID/previews/preview-ID`.

Infrastructure Manager uses the term _blueprint_ to refer to a Terraform configuration.

Replace the following:

  * PROJECT_ID: the project ID where Infra Manager is run.
  * LOCATION: the location where Infra Manager is run.



The preview artifacts in the storage bucket include:

  * Cloud Build logs.
  * Terraform logs.
  * A copy of the Terraform configuration.



### Preview name

The format of the preview name is:
    
    
    projects/PROJECT_ID/locations/LOCATION/previews/PREVIEW_ID
    

Where:

  * PROJECT_ID is the project ID where Infra Manager runs.
  * LOCATION is the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * PREVIEW_ID is the preview identifier, and is a user-specified name. This name must: 
    * Contain only lowercase letters, numbers, or hyphens.
    * Start with a lowercase letter.
    * End with a number or lowercase letter
    * Cannot be the string `archived-deployments` or `archived-previews`
    * Must be unique within the project and location where Infra Manager is run.



For example:
    
    
    projects/my-project/locations/us-central1/previews/my-preview
    

## What's next

  * Learn more about [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).
  * [Create a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources).
  * [Update a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment).
  * [View the state of a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments).
  * [Delete a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/delete-deployments). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

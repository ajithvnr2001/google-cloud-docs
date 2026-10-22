---
url: https://docs.cloud.google.com/infrastructure-manager/docs/troubleshoot-deployments/
title: Troubleshoot deployment errors \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:43.199568+00:00
---

# Troubleshoot deployment errors  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/troubleshoot-deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Troubleshoot deployment errors Stay organized with collections  Save and categorize content based on your preferences. 

This page describes:

  * How to inspect details and logs for deployments and individual revisions.

  * Troubleshooting strategies for common errors that you might see when deploying a Terraform configuration.




## Inspect deployment details and logs

You can inspect details and logs for both deployment and individual revisions.

### Inspect the state of the deployment

Each deployment has information about its current state, error code, and details about failure causes.

For any errors, start by [viewing the state of a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments#deployment-details).

### Inspect the state of a revision

If a deployment fails with error code `REVISION_FAILED`, you can [view the state of a revision](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments#revision-details).

In the output of the revision's state, look at the `stateDetail` and `errorCode` fields.

The state of the revision includes the same information as for a deployment. In addition, it includes the build ID.

### Inspect the Cloud Build logs

[View the state of a revision](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments#revision-details) and get the build ID of the Cloud Build used by the revision.

Use the build ID to inspect the Cloud Build logs. See [View build results](https://docs.cloud.google.com/build/docs/view-build-results) for details about inspecting build results.

## Common errors

This section describes common errors you might see when deploying a Terraform configuration with Infra Manager.

### Failed deployment

If the deployment state is `FAILED` the deployment has encountered an unexpected error.

[View the state of the deployment](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments#deployment-details) and inspect the `stateDetail` and `errorCode` fields for more information.

If a deployment fails with error code `REVISION_FAILED`, you can inspect the state of the revision.

### Configuration errors

If the deployment's state is `FAILED`, it might have failed because of configuration errors with the Terraform configuration.

If the deployment error is related to your configuration, `tfErrors` and `errorLogs` fields are included in the output of the [state of the deployment](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments#deployment-details). Examples of configuration errors include an invalid configuration or missing permissions.

View the errors from Terraform. In the output of the state of the deployment:

  * `tfErrors` is a summary of the errors encountered by Terraform (limited by Infra Manager to 10 errors in this list).
  * `errorLogs` point to a Cloud Storage object in your artifacts bucket. This bucket contains all `tfErrors` in new line delimited JSON format.



Each `tfError` has a resource address and human readable error description in the `errorDescription` field. If the resource fails due an HTTP error code returned from a Google Cloud API, the `httpResponseCode` field is also populated. Any additional API failure information is recorded in the error field.

### Service account missing permissions to fetch configuration

You see the following error:
    
    
      error downloading 'GCS_LOCATION': googleapi: Error 403: SA_EMAIL does
      not have storage.objects.list access to the Google Cloud Storage bucket.
    

You see this error because Infra Manager doesn't have permission to get the Terraform configuration from Cloud Storage bucket.

To address the issue, grant the `storage.objectViewer` role to the service account. For details about granting permissions to the service account, see [Configure the service account](https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account).

### Incorrect location to fetch configuration

You see the following error:
    
    
      `blueprint fetch failed: invalid path`
    

You see this error when an invalid location is specified to fetch the Terraform configuration. Infra Manager uses the term _blueprint_ to refer to a Terraform configuration.

To address this error, verify the location of the Terraform configuration, and ensure that the location is formatted correctly in your command.

### Incorrect permission to actuate resources

Errors are usually under `tfErrors` with the `403` response code for the resources that couldn't be deployed.

You see this error when the service account doesn't have enough permission to create, read, update, or delete resources defined in the Terraform configuration.

To address this error, see [Grant the service account IAM permissions](https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account#grant_the_service_account_permissions).

### Configuration with backend

You see the following error:
    
    
      `blueprint invalid: found backend config in file.tf`
    

You see this error when the Terraform configuration has a [backend block](https://developer.hashicorp.com/terraform/language/settings/backends/configuration). Infrastructure Manager manages the backend, so a backend block cannot be defined in the Terraform configuration.

To address this error, remove the backend block from the configuration.

### Validate Cloud Build repository configuration

If Infra Manager cannot access your Git repository (using a private Git repository or Cloud Build automated workflow), you may need to validate that your Cloud Build repository has been configured correctly.

To validate that the Cloud Build repository has been configured to provide access to the private repository, see [Connect to a GitHub repository](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github?generation=2nd-gen).

Infra Manager uses the first connection where the Cloud Build repository URL matches the Terraform configuration (referenced in `--git-source-repo`), and where it is able to generate a read-only token. The repository connection is validated directly by a call to the [accessReadToken API](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories/accessReadToken) on the selected Cloud Build repository.

Run this command using the Infra Manager service account to verify that the permissions are correct:
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token \
    --impersonate-service-account=SERVICE_ACCOUNT)" \
    "https://cloudbuild.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/connections/CB_CONNECTION/repositories/CB_REPO:accessReadToken"
    

## What's next

  * Learn more about [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).
  * [Update a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment).
  * [View the state of a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments).
  * [View resources deployed](https://docs.cloud.google.com/infrastructure-manager/docs/view-resources).
  * [Delete a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/delete-deployments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

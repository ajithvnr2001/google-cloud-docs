---
url: https://docs.cloud.google.com/appengine/docs/standard/troubleshooter/deployment/
title: Troubleshoot deployment issues in App Engine \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:38:37.652692+00:00
---

# Troubleshoot deployment issues in App Engine  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/troubleshooter/deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Troubleshoot deployment issues in App Engine Stay organized with collections  Save and categorize content based on your preferences. 

Several factors can cause deployment errors in App Engine, including missing permissions, changes to organization policies, and issues in your app configuration.

This page describes the following common deployment errors in App Engine and methods to troubleshoot them:

  * Permission errors
  * Common deployment errors



## Permission errors

This section describes errors that might occur when you deploy your app due to missing account permissions or changes to organization policies.

To identify the active account you use to access Google Cloud CLI and other tools in the Google Cloud Platform, do one of the following:

  * If you used the Google Cloud CLI to deploy, run the [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list) command.

  * If you deployed from an IDE, view the settings for the Cloud Tools plugin.




To learn why assigning only the App Engine Deployer (`roles/appengine.deployer`) role might not be sufficient in some cases, see [App Engine roles](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer).

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Deployment fails for new projects

You might see the following error when you deploy your app for the first time in a new project:
    
    
    ERROR: (gcloud.app.deploy) Error Response: [13] Failed to create cloud build: com.google.net.rpc3.client.RpcClientException:..........invalid bucket "staging.PROJECT_ID.appspot.com"; service account PROJECT_ID@appspot.gserviceaccount.com does not have access to the bucket
    

To resolve this issue, grant the [Storage Admin (`roles/storage.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) role to the default service account. For more information, see [Store build logs in a user-created bucket](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs#store-custom-bucket).

If you have already granted the Storage Admin role, along with the other required roles based on different permission errors you encounter during deployment, and are still unable to deploy your app, it might be due to the following changes to organization policies:

  * As of May 2024, Google Cloud enforces [secure-by-default organization policies](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations) for all organization resources. This policy prevents App Engine from granting the `Editor` role to the App Engine default service accounts.

  * In June 2024, Cloud Build changed the default behavior for how Cloud Build uses service accounts in new projects. This is detailed in [Cloud Build service account change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates). As a result of this change, new projects deploying versions for the first time might be using the default App Engine service account with [insufficient permissions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants%22) for deploying versions.




To resolve this issue, do the following:

  * Grant the [`Editor`](https://docs.cloud.google.com/appengine/docs/standard/roles) role to the App Engine default service account (_`PROJECT_ID @appspot.gserviceaccount.com`_).

  * Review the Cloud Build guidance on changes to the default service account and [opt out of the default changes in new projects](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates#what_do_you_need_to_do).




### The caller doesn't have permission to access project

The following error occurs if the service account doesn't have permission to deploy apps in the current project:
    
    
    User EMAIL_ADDRESS does not have permission to access project PROJECT_ID (or it may not exist).
    
    

To resolve this issue, grant the [App Engine Deployer (`roles/appengine.deployer`) role](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer) to the service account.

### Failed to fetch metadata from the registry

The following error occurs if you use the `gcloud app deploy` command from a service account that doesn't have the [Storage Admin (`roles/storage.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) role:
    
    
    Failed to fetch metadata from the registry, with reason: generic::permission_denied
    

To resolve this issue, grant the Storage Admin role to the service account.

### Service accounts must have permissions on the image

The following error occurs when you deploy your app:
    
    
    The App Engine appspot and App Engine flexible environment service accounts must
    have permissions on the image IMAGE_NAME
    

This error occurs due to one of the following reasons:

  * The default App Engine service account doesn't have the [Storage Object Viewer (`roles/storage.objectViewer`) role](https://docs.cloud.google.com/iam/docs/roles-permissions/storage).

To resolve this issue, grant the [Storage Object Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/storage) to the service account.

  * Your project has a [VPC Service Controls service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) that limits access to the Cloud Storage API using access levels.

To resolve this issue, add the service account you use to deploy your app to the corresponding VPC Service Controls service perimeter [accessPolicies](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#members-example).

  * After May 15, 2024, Artifact Registry hosts images for the `gcr.io` domain in Google Cloud projects without previous Container Registry usage. If you deploy an existing application in a new project created after this date, the service account might not have the required permissions to deploy the app. To grant the required permissions, see [Deploying to App Engine](https://docs.cloud.google.com/artifact-registry/docs/integrate-app-engine#permissions).




### Failed to create Cloud Build

The following error occurs if you use the `gcloud app deploy` command from a service account that doesn't have the Cloud Build Editor (`roles/cloudbuild.builds.editor`) role.
    
    
    Failed to create cloud build: Permission denied
    

To resolve this issue, grant the [Cloud Build Editor role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild) to the service account.

### Error fetching application

The following error occurs when the service account that you used to deploy your app doesn't have the [App Engine Deployer role](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer).
    
    
    Permissions error fetching application apps/app_name. Please make sure you are using the correct project ID and that you have permission to view applications on the project.
    
    If you are running Google Cloud CLI version 328 or later, the following error occurs
    when you deploy your app:
    
    make sure that you have permission to view applications on the project and that
    SERVICE_ACCOUNT has the App Engine Deployer (roles/appengine.deployer) role.
    

To resolve this issue, grant the App Engine Deployer role to the service account that you used to deploy your app.

### Error when deploying a service with a Serverless VPC Access connector

The following error occurs when the user or service account that is trying to deploy the app with a Serverless VPC Access connector doesn't have the required permissions:
    
    
    Please ensure you have [compute.globalOperations.get] on the service project
    

To resolve this issue, ensure that the user or service account used for deployment has the [Serverless VPC Access User](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#curated_iam_roles) and [Compute Viewer IAM](https://docs.cloud.google.com/compute/docs/access/iam#compute.viewer) roles.

## Common deployment errors

This section describes troubleshooting strategies for configuration errors in your app or project.

### Invalid value error when deploying in a Shared VPC setup

The following error shows in Cloud Logging for flexible VM instances when you deploy your app:
    
    
    Invalid value for field 'resource.tags.items[1]': 'aef-instance'. Duplicate
    tags are not allowed: aef-instance on compute.instances.insert
    

This is a known issue where setting the `instance_tag` in your `app.yaml` file results in errors when creating instances.

To resolve the issue, remove the [`instance_tag`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#network_settings) field from your `app.yaml` file and redeploy.

### Exceed the limit on maximum instances

The following error occurs when you deploy your app:
    
    
    You may not have more than 'xx' total max instances in your project.
    

There is a [limit](https://docs.cloud.google.com/appengine/docs/standard/quotas#services,-versions,-and-instances) for the maximum number of instances you can create per project. Requests to create additional instances fail if you exceed this limit.

To resolve this issue, set the value of [`max_instances`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#scaling_elements) in your `app.yaml` file to a value less than this limit or delete some services or versions to bring the sum of `max_instances` within the limit.

### Build during deployment fails without errors in logs

The following error occurs when you deploy your app:
    
    
    ERROR: (gcloud.app.deploy) Cloud build failed. Check logs at https://console.cloud.google.com/cloud-build/builds/BUILD_ID?project=PROJECT_NUMBER Failure status: UNKNOWN: Error Response: [2] Build failed; check build logs for details
    

If you click the link in the error message and find that all build steps were successful, but the app still failed to build, it might be due to either of the following reasons:

  * You use [customer-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek) (CMEK).
  * You set up a [data retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock) for your `staging.PROJECT_ID.appspot.com` bucket.



To resolve this issue, change the following settings for your bucket:

  * Set encryption to [Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/default-keys).
  * Remove the [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock).



### Build fails when running a Node.js application

Build failures might occur when you deploy a Node.js application.

By default, the Node.js runtime will execute `npm run build` if a build script is detected in the `package.json` file. This might cause unexpected behaviors like long-running builds, or out of memory errors.

To resolve this issue, specify `NODE_ENV=development` in your `app.yaml` file to ensure the execution has all the required dependencies.

Despite the error, you can force production by specifying `NODE_ENV: 'production'` under [`build-env-variables`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#build_env_variables) in your `app.yaml` file:
    
    
      build_env_variables:
        NODE_ENV: 'production'
    

For more information see [Executing custom build steps during deployment](https://docs.cloud.google.com/docs/buildpacks/nodejs#executing_custom_build_steps_during_deployment).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

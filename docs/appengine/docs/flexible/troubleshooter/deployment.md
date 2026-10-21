---
url: https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/deployment/
title: Troubleshoot deployment issues in App Engine \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:36:53.348191+00:00
---

# Troubleshoot deployment issues in App Engine  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
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

### Timed out waiting for the app infrastructure to become healthy

The following error occurs when you deploy your app:
    
    
    Timed out waiting for the app infrastructure to become flex_await_healthy
    

Various factors can cause this error, such as missing permissions, code errors, insufficient CPU or memory, or failed health checks.

To resolve this issue, rule out the following potential causes:

  1. Check whether the organization policy for your project restricts access to external IP addresses. For more information, see [App Engine flexible environment known issues](https://docs.cloud.google.com/appengine/docs/flexible/known-issues).

  2. Verify that you have granted the following roles to the service account that you use to run your application (usually the default service account, `app-id@appspot.gserviceaccount.com`):

     * [Editor (`roles/editor`)](https://docs.cloud.google.com/iam/docs/roles-overview#basic)

     * [Storage Object Viewer (`roles/storage.objectViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/storage)

     * [Logs Writer (`roles/logging.logWriter`)](https://docs.cloud.google.com/iam/docs/roles-permissions/logging)

  3. [Grant](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) the remaining roles based on your deployment errors, if the service account doesn't have them.

  4. If you deploy in a Shared VPC setup and configure an `instance_tag` in your `app.yaml` file, see Invalid value error when deploying in a Shared VPC setup to fix the issue.




### Error when restarting instances under running versions

The following error occurs when you deploy your app:
    
    
    error when restarting the instance under the running versions
    

As of May 2024, Google Cloud enforces the [secure-by-default](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations) organization policies for all new organizations. This policy requires all VM instances created in new projects to enable VM Manager. For new and existing projects, this constraint prevents metadata updates that disable VM Manager at the project or instance level.

To resolve this issue, you must [disable](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#boolean_constraints) the organization policy constraint Require OS Config ([`constraints/compute.requireOsConfig`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services)).

If this issue continues to persist, you must also disable the following organization policies that might have been enabled at the project or the organization level:

  * Define allowed external IPs for VM instances ([`constraints/compute.vmExternalIpAccess`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services)). If your application is setup to only use [private networking](https://docs.cloud.google.com/appengine/docs/flexible/disable-external-ip), you don't have to disable this constraint.

  * Disable Guest Attributes of Compute Engine metadata ([`constraints/compute.disableGuestAttributesAccess`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services))




### Required `compute.firewalls.list` permission

The following error occurs when you deploy your app [on a Shared VPC network](https://docs.cloud.google.com/appengine/docs/flexible/using-shared-vpc):
    
    
    Request to https://compute.googleapis.com/compute/v1/projects/projects/PROJECT_ID/global/firewalls?key failed, details: Required 'compute.firewalls.list' permission for 'projects/PROJECT_ID'
    

This error occurs if the following service accounts for the [host project](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_host_project_and_service_project_associations) don't have the Compute Network User (`roles/compute.networkUser`) role:

  * [Google APIs Service Agent](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed)
  * [App Engine flexible environment Service Agent](https://docs.cloud.google.com/appengine/docs/flexible/service-agent)

**Note:** The _host project_ is the Google Cloud project that contains your Shared VPC, not the _service project_ from which you deploy your App Engine app.

To resolve this issue, grant the [Compute Network User role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) to the Google APIs Service Agent and App Engine flexible environment Service Agent service accounts for the host project.

### Deployment fails due to an organization policy constraint

The following error occurs when you deploy an app:
    
    
    ERROR: (gcloud.app.deploy) Error Response: [13] An internal error occurred while processing task /app-engine-flex/....: Request to https://compute.googleapis.com/compute/VERSION/projects/PROJECT_ID/... failed, details: Constraint constraints/compute.disableGuestAttributesAccess violated for project PROJECT_ID.
    

This might be due to the enforcement of the [`constraints/compute.disableGuestAttributesAccess`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services) constraint when deploying your app. All apps in the App Engine flexible environment enforce this organization policy by default.

To resolve this issue, you must [disable](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#boolean_constraints) the `constraints/compute.disableGuestAttributesAccess` constraint.

## Common deployment errors

This section describes troubleshooting strategies for configuration errors in your app or project.

### Invalid value error when deploying in a Shared VPC setup

The following error shows in Cloud Logging for flexible VM instances when you deploy your app:
    
    
    Invalid value for field 'resource.tags.items[1]': 'aef-instance'. Duplicate
    tags are not allowed: aef-instance on compute.instances.insert
    

This is a known issue where setting the `instance_tag` in your `app.yaml` file results in errors when creating instances.

To resolve the issue, remove the [`instance_tag`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#network_settings) field from your `app.yaml` file and redeploy.

### Exceed the limit on maximum instances

The following error occurs when you deploy your app:
    
    
    You may not have more than 'xx' total max instances in your project.
    

There is a [limit](https://docs.cloud.google.com/appengine/docs/flexible/quotas#services,-versions,-and-instances) for the maximum number of instances you can create per project. Requests to create additional instances fail if you exceed this limit.

To resolve this issue, set the value of [`max_instances`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#scaling_elements) in your `app.yaml` file to a value less than this limit or delete some services or versions to bring the sum of `max_instances` within the limit.

### Build during deployment fails without errors in logs

The following error occurs when you deploy your app:
    
    
    ERROR: (gcloud.app.deploy) Cloud build failed. Check logs at https://console.cloud.google.com/cloud-build/builds/BUILD_ID?project=PROJECT_NUMBER Failure status: UNKNOWN: Error Response: [2] Build failed; check build logs for details
    

If you click the link in the error message and find that all build steps were successful, but the app still failed to build, it might be due to either of the following reasons:

  * You use [customer-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek) (CMEK).
  * You set up a [data retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock) for your `staging.PROJECT_ID.appspot.com` bucket.



To resolve this issue, change the following settings for your bucket:

  * Set encryption to [Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/default-keys).
  * Remove the [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock).



### Errors when deploying to an existing App Engine version

The following error might occur when deploying to an existing version in the App Engine flexible environment:
    
    
    ERROR: (gcloud.app.deploy) Error Response: [9] An internal error occurred while
    processing task /app-engine-flex/flex_await_healthy/flex_await_healthy
    

This error indicates that updating an unhealthy deployment with a working Docker image doesn't always result in a healthy deployment. The outcome depends on the state of instances from the unhealthy deployment. Despite the error, if you provide a good Docker image, the deployment might eventually become healthy. Updating an existing version with a new Docker image, though allowed, is not a good practice. There is no rollback in case of version failure.

### Internal IP error when deploying in a Shared VPC setup

The following error might occur when deploying to a Shared VPC network setup in a service project where the default private IP address setting (`private-ranges-only`) is used.
    
    
    ERROR: (gcloud.app.deploy) Error Response: [13] An internal error occurred.
    

This error might indicate that the App Engine flexible environment Service Agent in the host project of the Shared VPC is not available. Either the App Engine flexible environment Service Agent is removed or the App Engine API is not enabled in the host project.

To resolve this issue:

  1. Enable the App Engine API in the host project of the Shared VPC network.
  2. If the App Engine API is enabled, the App Engine flexible environment Service Agent doesn't exist in the project. Refer to [Restore required role for the service agent](https://docs.cloud.google.com/appengine/docs/flexible/service-agent#restore_required_role_for_the_service_agent).



### Deployment failure due to lack of connectivity to Google APIs

The following error occurs when you deploy your app:
    
    
    Your deployment has failed to become healthy in the allotted time and therefore was rolled back. If you believe this was an error, try adjusting the app_start_timeout_sec setting in the readiness_check section.
    

To resolve this issue, ensure that the VPC associated with your application has a [local static route with the `0.0.0.0/0` destination and a default internet gateway next hop](https://docs.cloud.google.com/vpc/docs/routes#routingpacketsinternet). If you use [private internal-only services](https://docs.cloud.google.com/appengine/docs/flexible/disable-external-ip#limitations), then enable PGA on the selected subnet.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/functions/docs/troubleshooting/
title: Troubleshoot Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:46.830402+00:00
---

# Troubleshoot Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/troubleshooting/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Resources ](https://docs.cloud.google.com/functions/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot Cloud Run functions

This document shows you how to troubleshoot error messages and resolve issues when using Cloud Run functions. If you created or deployed a function using Cloud Run, see [Troubleshoot Cloud Run issues](https://docs.cloud.google.com/run/docs/troubleshooting).

## Deployment

This section lists issues that you might encounter with deployment and provides suggestions for how to fix each of them. Many of the issues you might encounter during deployment are related to [roles and permissions](https://docs.cloud.google.com/functions/docs/reference/iam/roles) or incorrect configuration.

You use [Identity and Access Management](https://docs.cloud.google.com/iam) to authorize identities to perform administrative actions on functions created using the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/apis)—for example, using `gcloud functions`, the REST API, or Terraform. Administration actions include creating, updating, and deleting functions. For more information, see [Authorize access with IAM](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam).

### User missing permissions on runtime service account while deploying a function

Every function is associated with a service account that serves as its identity when the function accesses other resources. This [runtime service](https://docs.cloud.google.com/functions/docs/securing/function-identity#runtime-sa) account can be the default service account or a user-managed service account. In environments where multiple functions are accessing different resources, it's a common practice to use [per-function identities](https://docs.cloud.google.com/functions/docs/securing/function-identity#per-function_identity) with named runtime service accounts rather than the default runtime service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`).

To use a runtime service account, the deployer must have the `iam.serviceAccounts.actAs` permission on that service account. A user who creates a non-default runtime service account is automatically granted this permission, but other deployers must have this permission granted by a user.

Assign the `iam.serviceAccounts.actAs` permission on the runtime service account for the user with the Project Viewer, Cloud Functions Developer, or Cloud Functions Admin role.

**The error message**

###  Console 
    
    
      You must have the iam.serviceAccounts.actAs permission on the selected service account. To obtain this permission, you can grant a role that includes it like the Service Account User role, on the project.
    

###  gcloud 

Default service account:
    
    
    ERROR: (gcloud.functions.deploy) ResponseError: status=[403], code=[Ok], message=[Caller is missing permission 'iam.serviceaccounts.actAs' on service account projects/-/serviceAccounts/PROJECT_NUMBER-compute@developer.gserviceaccount.com.Grant the role 'roles/iam.serviceAccountUser' to the caller on the service account projects/-/serviceAccounts/PROJECT_NUMBER-compute@developer.gserviceaccount.com.You can do that by running 'gcloud iam service-accounts add-iam-policy-binding projects/-/serviceAccounts/PROJECT_NUMBER-compute@developer.gserviceaccount.com --member MEMBER --role roles/iam.serviceAccountUser'where MEMBER has a prefix like 'user:' or 'serviceAccount:'
    

Non-default service account:
    
    
    ERROR: (gcloud.functions.deploy) ResponseError: status=[403], code=[Ok], message=[Caller is missing permission 'iam.serviceaccounts.actAs' on service account projects/-/serviceAccounts/
    SERVICE_ACCOUNT_NAME@PROJECT_ID
    .iam.gserviceaccount.com.Grant the role 'roles/iam.serviceAccountUser' to the caller on the service account projects/-/serviceAccounts/
    SERVICE_ACCOUNT_NAME@PROJECT_ID
    .iam.gserviceaccount.com.You can do that by running 'gcloud iam service-accounts add-iam-policy-binding projects/-/serviceAccounts/
    SERVICE_ACCOUNT_NAME@PROJECT_ID
    .iam.gserviceaccount.com --member MEMBER --role roles/iam.serviceAccountUser'where MEMBER has a prefix like 'user:' or 'serviceAccount:'
    

**Note:** `PROJECT_NUMBER-compute@developer.gserviceaccount.com` is the default service account for Cloud Functions. When you use a non-default service account, Cloud Functions replaces the default service account with the user-managed service account `SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com` in the error message.

**The solution**

[Assign the user](https://docs.cloud.google.com/functions/docs/reference/iam/roles#additional-configuration), the Service Account User role (`roles/iam.serviceAccountUser`) on the default or the non-default runtime service account. This role includes the `iam.serviceAccounts.actAs` permission.

### Deployment service account missing Pub/Sub permissions when deploying an event-driven function

The Cloud Functions service uses the Cloud Functions Service Agent service account (`service-PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com`) when performing administrative actions. By default this account is assigned the Cloud Functions `cloudfunctions.serviceAgent` role. To deploy [event-driven functions](https://docs.cloud.google.com/functions/docs/writing#types_of_cloud_functions), the Cloud Functions service must [access Pub/Sub](https://docs.cloud.google.com/functions/docs/concepts/iam#cloud_functions_service_account) to configure topics and subscriptions. If you change the role assigned to the service account without granting the appropriate permissions, the Cloud Functions service cannot access Pub/Sub and the deployment fails.

**The error message**

###  Console 
    
    
    Validation failed for trigger projects/PROJECT_ID/locations/LOCATION/triggers/FUNCTION_NAME-EVENTARC_ID: Permission "iam.serviceAccounts.ActAs" denied on "EndUserCredentials to PROJECT_NUMBER-compute@developer.gserviceaccount.com"
    

###  gcloud 
    
    
    ERROR: (gcloud.functions.deploy) ResponseError: status=[403], code=[Ok], message=[Validation failed for trigger projects/test-project-356312/locations/LOCATION/triggers/FUNCTION_NAME-EVENTARC_ID: Permission "iam.serviceAccounts.ActAs" denied on "EndUserCredentials to PROJECT_NUMBER-compute@developer.gserviceaccount.com"]
    

**The solution**

You can [reset your service account](https://docs.cloud.google.com/functions/docs/concepts/iam#google_cloud_functions_service_agent_service_account) to the default **cloudfunctions.serviceAgent** role.

### Default runtime service account doesn't exist

When you don't specify a [user-managed runtime service account](https://docs.cloud.google.com/functions/docs/securing/function-identity#individual), Cloud Functions uses the [default compute service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) as the runtime service account. Deployments fail if you delete the default account without specifying a user-managed account.

**The error message**

###  gcloud 
    
    
    ERROR: (gcloud.functions.deploy) ResponseError: status=[404], code=[Ok], message=[Service account projects/-/serviceAccounts/PROJECT_NUMBER-compute@developer.gserviceaccount.com was not found.]
    

**The solution**

To resolve this issue, follow any of these solutions:

  * Specify a [user managed runtime service account](https://docs.cloud.google.com/functions/docs/securing/function-identity#individual) before deploying your function.

  * [Undelete the service account by numeric ID](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#undeleting) of the default service account.




### Cloud Functions Service Agent service account missing project bucket permissions while deploying a function

Cloud Run functions can only be [triggered by events](https://docs.cloud.google.com/functions/docs/calling/storage) from Cloud Storage buckets in the same Google Cloud Platform project. In addition, the Cloud Functions Service Agent service account (`service-PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com`) needs a `cloudfunctions.serviceAgent` role on your project.

**The error message**

###  Console 
    
    
    ERROR: (gcloud.functions.deploy) ResponseError: status=[403], code=[Ok], message=[Validation failed for trigger projects/PROJECT_ID/locations/LOCATION/triggers/FUNCTION_NAME-EVENTARC_ID: Permission "iam.serviceAccounts.ActAs" denied on "EndUserCredentials to PROJECT_NUMBER-compute@developer.gserviceaccount.com"]
    

###  gcloud 
    
    
    ERROR: (gcloud.functions.deploy) ResponseError: status=[403], code=[Ok], message=[Validation failed for trigger projects/<project-id>/locations/LOCATION/triggers/FUNCTION_NAME-EVENTARC_ID: Permission "iam.serviceAccounts.ActAs" denied on "EndUserCredentials to PROJECT_NUMBER-compute@developer.gserviceaccount.com"]
    

**The solution**

To resolve this issue, [reset this service account](https://docs.cloud.google.com/functions/docs/concepts/iam#runtime_service_accounts) to the default role.

### User with Project Editor role can't make a function public

The Project Editor role has broad permissions to manage resources within a project, but it doesn't inherently grant the ability to make Cloud Functions public. The user or the service deploying the function would require the `run.services.setIamPolicy` permission.

**The error message**

###  gcloud 
    
    
    ERROR: (gcloud.run.services.add-iam-policy-binding) PERMISSION_DENIED: Permission 'run.services.setIamPolicy' denied on resource 'projects/PROJECT_ID/locations/LOCATION/functions/FUNCTION_NAME' (or resource may not exist).
    

**The solution**

You can :

  * Assign the deployer either the [Project Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) or the [Cloud Functions Admin](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.admin) role.

  * Grant the permission manually by creating a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

  * Check if [domain restricted sharing](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam#domain_restricted_sharing) is enforced on the project.




### Function deployment fails when using Resource Location Restriction organization policy

If your organization uses a [resource location constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) policy, it restricts function deployment in the regions restricted by the policy. In the Google Cloud console, the restricted region won't be available from the region drop-down while deploying a function.

**The error message**

###  gcloud 
    
    
    ResponseError: status=[400], code=[Ok], message=["LOCATION" violates constraint "constraints/gcp.resourceLocations" on the resource "projects/PROJECT_ID/locations/LOCATION/functions/FUNCTION_NAME".]
    

**The solution**

You can add or remove locations from the `allowed_values` or `denied_values` lists of a resource locations constraint to suit successful deployment.

### Function deployment fails while executing function's global scope

This error indicates that there was a problem with your code. The deployment pipeline finished deploying the function, but failed at the last step - sending a health check to the function. This health check is meant to execute a function's [global scope](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#scope), which could be throwing an exception, crashing, or timing out. The global scope is where you commonly load in libraries and initialize clients.

**The error message**

In Cloud Logging logs:
    
    
    Could not create or update Cloud Run service FUNCTION_NAME, Container Healthcheck failed. Revision REVISION_NAMEE is not ready and cannot serve traffic. The user-provided container failed to start and listen on the port defined provided by the PORT=8080 environment variable. Logs for this revision might contain more information.
    

**The solution**

To resolve this issue, follow any of these solutions:

  * For a more detailed error message, review your function's [build logs](https://docs.cloud.google.com/functions/docs/building#accessing_your_build_image_logs).

  * If it is unclear why your function failed to execute its global scope, consider temporarily moving the code into the request invocation, using [lazy initialization of the global variables](https://docs.cloud.google.com/functions/docs/bestpractices/tips#do_lazy_initialization_of_global_variables). This lets you add extra log statements around your client libraries, which could be timing out on their instantiation (especially if they are calling other services), crashing, or throwing exceptions altogether.

  * Additionally, try increasing the function timeout. Longer timeout limits in Cloud Run functions provides more breathing room for initialization and it offers more scalable resource allocation in a Cloud Run environment, potentially mitigating this issue if caused by resource exhaustion.

  * The source code must contain an entry point function that has been correctly specified in the deployment, either through the [console](https://docs.cloud.google.com/functions/docs/deploying/console) or [gcloud](https://docs.cloud.google.com/functions/docs/deploying/filesystem).




### User with Viewer role cannot deploy a function

Users with either the Project Viewer or Cloud Functions Viewer role have **read-only** access to functions and function details, and can't deploy new functions. The **Create function** feature is grayed out in the Google Cloud console with the following error:

**The error message**

###  gcloud 
    
    
    ERROR: (gcloud.functions.deploy) ResponseError: status=[403], code=[Ok], message=[Permission 'cloudfunctions.functions.generateUploadUrl' denied on 'projects/PROJECT_ID/locations/LOCATION/functions']
    

**The solution**

Assign the user [Cloud Functions Developer](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.developer) role.

### Build service account missing permissions

**The error message**

In the function deploy error or in the build logs, you may see one of the following errors:
    
    
    The service account running this build does not have permission to write logs. To fix this, grant the Logs Writer (roles/logging.logWriter) role to the service account.
    
    
    
    Step #0 - "fetch": failed to Fetch: failed to download archive gs://gcf-v2-sources-PROJECT_NUMBER-LOCATION/FUNCTION_NAME/version-VERSION_NUMBER/function-source.zip: Access to bucket gcf-v2-sources-PROJECT_NUMBER-LOCATION denied. You must grant Storage Object Viewer permission to PROJECT_NUMBER-compute@developer.gserviceaccount.com.
    
    
    
    Step #2 - "build": ERROR: failed to create image cache: accessing cache image "LOCATION-docker.pkg.dev/PROJECT/gcf-artifacts/FUNCTION_NAME/cache:latest": connect to repo store "LOCATION-docker.pkg.dev/PROJECT/gcf-artifacts/FUNCTION_NAME/cache:latest": GET https://LOCATION-docker.pkg.dev/v2/token?scope=repository%3APROJECT%2Fgcf-artifacts%2FFUNCTION_NAME%2Fcache%3Apull&service=: DENIED: Permission "artifactregistry.repositories.downloadArtifacts" denied on resource "projects/PROJECT/locations/LOCATION/repositories/gcf-artifacts" (or it may not exist)
    
    
    
    Could not build the function due to a missing permission on the build service account. If  you didn't revoke that permission explicitly, this could be caused by a change in the organization policies.

**The solution**

The build service account needs permission to read from the source bucket and read and write permissions for the Artifact Deployment repository. You may encounter this error due to a change in the default behavior for how Cloud Build uses service accounts, detailed in [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).

To resolve this issue, use any of these solutions:

  * Create a [custom build service account](https://docs.cloud.google.com/functions/docs/securing/build-custom-sa#grant_permissions) for function deployments.
  * Add the [Cloud Build Service Account role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`) to the default Compute Service Account.
  * Review the Cloud Build guidance on changes to the default service account and [opt out of these changes](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates#what_do_you_need_to_do).



### Build service account disabled

**The error message**
    
    
    Could not build the function due to disabled service account used by Cloud Build. Please make sure that the service account is active.
    

**The solution**

The build service account needs to be enabled in order to deploy a function. You may encounter this error due to a change in the default behavior for how Cloud Build uses service accounts, detailed in [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).

To resolve this issue, use any of these solutions:

  * Create a [custom build service account](https://docs.cloud.google.com/functions/docs/securing/build-custom-sa#grant_permissions) for function deployments.
  * Enable the default Compute Service Account.
  * Review the Cloud Build guidance on changes to the default service account and [opt out of these changes](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates#what_do_you_need_to_do).



## Serving

This section lists serving issues that you might encounter, and provides suggestions for how to fix each of them.

### Serving permission error due to the function requiring authentication

HTTP functions without **Allow unauthenticated invocations** enabled, restrict access to end users and service accounts that don't have appropriate [permissions](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam#gcloud_4). This error message indicates that the caller does not have permission to invoke the function.

**Note:** Visiting the Cloud Run functions URL in a browser does not add an authentication header automatically.

**The error message**

HTTP Error Response code: 403 Forbidden

HTTP Error Response body:
    
    
    Error: Forbidden Your client does not have permission
    to get URL /FUNCTION_NAME from this server.
    

**The solution**

To resolve this issue, follow any of these solutions:

  * Assign the user the [Cloud Run Invoker Cloud IAM](https://docs.cloud.google.com/run/docs/reference/iam/roles) role for the specific function.

  * Redeploy your function [to allow public access](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam#allowing_unauthenticated_http_function_invocation) if this is supported by your organization. This is useful for testing.




### Serving error due to `allow internal traffic only` configuration

[Ingress settings](https://docs.cloud.google.com/run/docs/securing/ingress) restrict whether an HTTP function can be invoked by resources outside of your Google Cloud project or VPC Service Controls service perimeter. When you configure **allow internal traffic only** setting for ingress networking, this error message indicates that only requests from VPC networks in the same project or VPC Service Controls perimeter are allowed. This can also be a 404 error for default `functions.net` URL.

**The error message**

HTTP Error Response code: 404 NOT FOUND

**The solution**

To resolve this error, follow any of these solutions:

  * Ensure that the request is coming from your Google Cloud project or VPC Service Controls service perimeter.

  * Change the ingress settings to [allow all traffic](https://docs.cloud.google.com/run/docs/securing/ingress) for the function.

  * Cloud Run functions source code can also result in a 404 due to incorrect function url, http methods, logic errors etc.




### Function invocation lacks valid authentication credentials

Invoking a Cloud Run functions function that has been set up with [restricted access](https://docs.cloud.google.com/run/docs/authenticating/service-to-service#acquire-token) requires an [ID token](https://developers.google.com/identity/protocols/oauth2/openid-connect#obtainuserinfo). [Access tokens](https://developers.google.com/identity/protocols/oauth2?_ga=2.163318204.1401894525.1612199962-958658716.1595873194#2.-obtain-an-access-token-from-the-google-authorization-server.) or [refresh tokens](https://developers.google.com/identity/protocols/oauth2?_ga=2.163318204.1401894525.1612199962-958658716.1595873194#5.-refresh-the-access-token,-if-necessary.) don't work.

**The error message**

HTTP Error Response code: 401 Unauthorized

HTTP Error Response body:
    
    
    Your client does not have permission to the requested URL 'FUNCTION_NAME'
    

**The solution**

To resolve this error, follow either of these solutions:

  * Make sure that your requests include an [`Authorization: Bearer ID_TOKEN` header](https://docs.cloud.google.com/run/docs/authenticating/service-to-service#acquire-token), and that the token is an ID token, not an access or refresh token. If you generate this token manually with a service account's private key, you must exchange the self-signed JWT token for a Google-signed Identity token.

Invoke your HTTP function using authentication credentials in your request header. For example, you can get an identity token using `gcloud` as follows:
        
        curl  -H "Authorization: Bearer $(gcloud auth print-identity-token)"   
            https://REGION-PROJECT_ID.cloudfunctions.net/FUNCTION_NAME
          

  * Redeploy your function to allow unauthenticated invocations if this is supported by your organization. This is useful for testing.

  * Make sure that the `audience (aud)` field in the JSON Web Token (JWT) is an exact match to the function's URL as displayed in the Google Cloud console. Any discrepancies, including an additional relative path, causes an authentication failure and a 401 response.




### Function stops mid-execution, or continues running after your code finishes

Some Cloud Run functions runtimes allow users to run asynchronous tasks. If your function creates such tasks, it must also explicitly wait for these tasks to complete. Failure to do so might cause your function to stop executing at the wrong time.

**The error behavior**

Your function exhibits one of the following behaviors:

  * Your function terminates while asynchronous tasks are still running, but before the specified timeout period has elapsed.
  * Your function _doesn't_ stop running when these tasks finish, and continues to run until the timeout period has elapsed.



**The solution**

If your function terminates early, you should make sure all your function's asynchronous tasks are complete before your function performs any of the following actions:

  * Returning a value
  * Resolving or rejecting a returned `Promise` object (Node.js functions only)
  * Throwing uncaught exceptions or errors
  * Sending an HTTP response
  * Calling a callback function



If your function fails to terminate after completing asynchronous tasks, you should verify that your function is correctly signaling Cloud Run functions after it has completed. In particular, make sure that you perform one of the operations listed earlier as soon as your function has finished its asynchronous tasks.

### Runtime error when accessing resources protected by VPC Service Controls

By default, Cloud Run functions uses public IP addresses to make outbound requests to other services. If your functions are not inside a VPC Service Controls perimeter, this might cause them to receive HTTP 403 responses when attempting to access Google Cloud services protected by VPC Service Controls, due to service perimeter denials.

**The error message**

In Audited Resources logs, an entry like the following:
    
    
    "protoPayload": {
      "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
      "status": {
        "code": 7,
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.PreconditionFailure",
            "violations": [
              {
                "type": "VPC_SERVICE_CONTROLS",
      ...
      "authenticationInfo": {
        "principalEmail": "CLOUD_FUNCTION_RUNTIME_SERVICE_ACCOUNT",
      ...
      "metadata": {
        "violationReason": "NO_MATCHING_ACCESS_LEVEL",
        "securityPolicyInfo": {
          "organizationId": "ORGANIZATION_ID",
          "servicePerimeterName": "accessPolicies/NUMBER/servicePerimeters/SERVICE_PERIMETER_NAME"
      ...
    

**The solution**

To resolve this error, follow either of these solutions:

  * The function should route all outgoing traffic through the VPC network. See [Deploy functions compliant with VPC Service Controls](https://docs.cloud.google.com/functions/docs/securing/using-vpc-service-controls#deploy-compliant-functions) section for more information.

  * Alternatively, grant the function's [runtime service account](https://docs.cloud.google.com/functions/docs/concepts/iam#runtime_service_accounts) access to the perimeter. You can do this either by [creating an access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#members-example) and [adding the access level to the service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#add-access-level), or by [creating an ingress policy](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) on the perimeter. See [Use VPC Service Controls](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls) for more information.




## Scalability

This section lists scalability issues and provides suggestions for how to fix each of them.

### Cloud Logging errors related to pending queue request aborts

Scaling failures can occur from the following scenarios:

  * A huge sudden increase in traffic.
  * Long [cold start time](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#cold-starts).
  * Long request processing time.
  * High function error rate.
  * Reaching the [maximum instance limit](https://docs.cloud.google.com/functions/docs/configuring/max-instances) and preventing the system from scaling.
  * Transient factors attributed to the Cloud Run functions service.



In each case Cloud Run functions might not scale up fast enough to manage the traffic.

**The error message**

  * `The request was aborted because there was no available instance`
    * `severity=WARNING` ( Response code: 429 ) Cloud Run functions cannot scale due to the [`max-instances`](https://docs.cloud.google.com/functions/docs/configuring/max-instances) limit you set during configuration.
    * `severity=ERROR` ( Response code: 500 ) Cloud Run functions intrinsically cannot manage the rate of traffic.



**The solution**

  * To resolve this issue, address the previously listed causes.

  * For HTTP trigger-based functions, have the client implement exponential backoff and retries for requests that must not be dropped. If you are [triggering Cloud Run functions from Workflows](https://docs.cloud.google.com/workflows/docs/calling-run-functions), you can use the [`try/retry` syntax](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying) to achieve this.

  * For background or event-driven functions, Cloud Run functions supports [at-least-once delivery](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#execution-guarantees). Even without explicitly enabling retry, the event is automatically re-delivered and the function execution will be retried. See [Retrying Event-Driven Functions](https://docs.cloud.google.com/functions/docs/bestpractices/retries) for more information.

  * When the root cause of the issue is a period of heightened transient errors attributed solely to Cloud Run functions or if you need assistance with your issue, contact [support](https://docs.cloud.google.com/functions/docs/getting-support).

  * For issues pertaining to cold starts, configure [minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances) to reduce the amount of cold starts with a higher billing implication.




## Logging

The following section covers issues with logging and how to fix them.

### Logs entries have none or incorrect log severity levels

Cloud Run functions includes runtime logging by default. Logs written to `stdout` or `stderr` appear automatically in the [Cloud Logging](https://console.cloud.google.com/project/_/logs?service=cloudfunctions.googleapis.com). But these log entries by default, contain only string messages.

**The error message**

No or incorrect severity levels in logs.

**The solution**

To include log severities, you must send a structured log entry.

**Note:** As of September 2020, _every_ newly released runtime will use the default severity log level behavior as defined by the runtime library itself. For example, Python 3.8 sets the default severity log level at `WARNING` or higher. If you want to capture events with `DEBUG` or `INFO` severity using Python 3.8, you must also programmatically set your log level to include those levels.

### Handle or log exceptions differently in the event of a crash

You might want to customize how you manage and log crash information.

**The solution**

Wrap your function in a `try` block to customize handling exceptions and logging stack traces.

**Note:** Adding a `try` block can result in an unintended side effect in event-driven functions with the `retry on failure` configuration. Retrying failed events might itself fail.

**Example**
    
    
    import logging
    import traceback
    def try_catch_log(wrapped_func):
      def wrapper(*args, **kwargs):
        try:
          response = wrapped_func(*args, **kwargs)
        except Exception:
          # Replace new lines with spaces so as to prevent several entries which
          # would trigger several errors.
          error_message = traceback.format_exc().replace('\n', '  ')
          logging.error(error_message)
          return 'Error';
        return response;
      return wrapper;
    
    #Example hello world function
    @try_catch_log
    def python_hello_world(request):
      request_args = request.args
    
      if request_args and 'name' in request_args:
        1 + 's'
      return 'Hello World!'
    

### Logs too large in Node.js 10+, Python 3.8, Go 1.13, and Java 11

The maximum size for a regular log entry in these runtimes is 105 KiB.

**The solution**

Send log entries smaller than this limit.

### Missing logs despite Cloud Run functions returning errors

Cloud Run functions streams Cloud Run function logs to a default bucket. When you create a project, Cloud Run functions creates and enables the default bucket. If the default bucket is disabled or if Cloud Run function logs are in the exclusion filter, the logs won't appear in Logs Explorer.

**The solution**

Enable default logs.

**Note:** Enabling Cloud Logging might incur charges.

### Cloud Run functions logs aren't appearing in Logs Explorer

Some Cloud Logging client libraries use an asynchronous process to write log entries. If a function crashes, or otherwise terminates, it is possible that some log entries haven't been written yet, and might appear later. Some logs may be lost and can't be seen in the Logs Explorer.

**The solution**

Use the client library interface to flush buffered log entries before exiting the function, or use the library to write log entries synchronously. You can also synchronously write logs directly to `stdout` or `stderr`.

### Missing Cloud Run functions logs when using Log Router sink

Log Router sinks [route](https://docs.cloud.google.com/logging/docs/routing/overview) log entries to various destinations.

![Screenshot of Console Log Router with View sink details highlighted](https://docs.cloud.google.com/static/functions/img/logs-router-gen2.png)

The **Exclusion filters** define entries that you can discard.

**The solution**

Remove exclusion filter set for `resource.type = "cloud_run_revision"`.

## Database connections

There are a number of issues that can arise when connecting to a database, many associated with exceeding connection limits or timing out. If you see a Cloud SQL warning in your logs, for example, `Context deadline exceeded`, you might need to adjust your connection configuration. For more information, see [Cloud SQL best practices](https://docs.cloud.google.com/sql/docs/mysql/connect-functions#best-practices).

## Networking

This section lists networking issues and provides suggestions for how to fix each of them.

### Network connectivity

If all outbound requests from a Cloud Run function fail even after you configure egress settings, you can run Connectivity Tests to identify any underlying network connectivity issues. For more information, see [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests).

### Serverless VPC Access connector is not ready or does not exist

If a Serverless VPC Access connector fails, it might not be using a `/28` subnet mask dedicated to the connector as [required](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors).

**The error message**
    
    
    Problem connecting to VPC Connector projects/xxxxx/locations/REGION/connectors/xxxx: Serverless VPC Access is not found.
    

When Cloud Run functions is deployed with a connector in a bad state due to missing permission on the [Google APIs Service Agent service account](https://docs.cloud.google.com/iam/docs/service-agents#google-apis-service-agent) `PROJECT_NUMBER@cloudservices.gserviceaccount.com`, it results in the following error:

**The error message**
    
    
    Failed to prepare VPC connector. Please try again later.
    

**The solution**

[List your subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#listing_existing_subnets) to check whether your connector uses a `/28` subnet mask. If your connector doesn't use the `/28` subnet mask, [recreate or create a new connector](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors).

To resolve this issue, follow any of these solutions:

  * If you recreate the connector, you don't need to redeploy other functions. You might experience a network interruption as the connector is recreated.

  * If you create a new alternate connector, redeploy your functions to use the new connector and then delete the original connector. This method avoids network interruption.

  * Ensure the Cloud Run functions and its associated connector are deployed in the same region.

  * For the Shared VPC configuration:

    * Ensure that the service accounts `SERVICE_PROJECT_NUMBER@cloudservices.gserviceaccount.com` and `service-SERVICE_PROJECT_NUMBER@gcp-sa-vpcaccess.iam.gserviceaccount.com` used by VPC Connector to provision resources in the project are not missing permissions. These service accounts should have the `roles/compute.networkUser` role in the host project of Shared VPC configuration when the connector is in the service project.

    * If the connector is created in the host project, ensure that the `Serverless VPC Access User` role is [granted](https://docs.cloud.google.com/run/docs/configuring/shared-vpc-service-projects#grant-permissions) on [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#google-cloud-run-service-agent) in your host project.

  * If the connector status shows `Connector is in a bad state, manual deletion recommended` error and the [Google APIs Service Agent](https://docs.cloud.google.com/compute/docs/access/service-accounts#google_apis_service_agent) is missing the required permissions to provision compute resources in the connector's project, grant `roles/compute.admin` to the `PROJECT_NUMBER@cloudservices.gserviceaccount.com` service account. In some cases the connector may need to be recreated after adding these permissions.




### SMTP traffic to external destination IP addresses using TCP port 25 is blocked

For added security, Google Cloud blocks connections to TCP destination port `25` when sending emails from functions.

**The solution**

To unblock these connections, follow any of these solutions:

  * Connect to your SMTP server on a different port, such as TCP port `587` or `465`.

  * [Use a third-party email service](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail#choosing_a_third-party_email_service_to_use).




### 404 error for default `functions.net` URL

Disabling the `run.app` URL in Cloud Run also prevents access to the default `cloudfunctions.net` URL for Cloud Run functions (2nd gen). This error can also be caused by a Serving error due to allow internal traffic only configuration.

**The error message**

HTTP Error Response code: 404 NOT FOUND

**The solution**

To re-enable the default `cloudfunctions.net` URL for Cloud Run functions (2nd gen), you must [re-enable the `run.app` URL in Cloud Run](https://docs.cloud.google.com/run/docs/securing/ingress#yaml_1) by replacing the `service.yaml` file with a new configuration where `annotations:run.googleapis.com/default-url-disabled: false`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

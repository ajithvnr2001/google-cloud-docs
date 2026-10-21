---
url: https://docs.cloud.google.com/functions/1stgendocs/troubleshooting/
title: Troubleshoot Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:43.429888+00:00
---

# Troubleshoot Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/troubleshooting/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot Cloud Run functions (1st gen)

This document shows you how to troubleshoot error messages and resolve issues when using Cloud Run functions (1st gen).

## Deployment

This section lists issues that you might encounter with deployment and provides suggestions for how to fix each of them. Many of the issues you might encounter during deployment are related to [roles and permissions](https://docs.cloud.google.com/functions/docs/reference/iam/roles) or incorrect configuration.

### Deployment service account missing Pub/Sub permissions when deploying an event-driven function

The Cloud Functions service uses the Cloud Functions service agent service account (`service-PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com`) for performing administrative actions. By default, this account is assigned the Cloud Functions `cloudfunctions.serviceAgent` role. To deploy [event-driven functions](https://docs.cloud.google.com/functions/docs/writing#types_of_cloud_functions), the Cloud Functions service must [access Pub/Sub](https://docs.cloud.google.com/functions/docs/concepts/iam#cloud_functions_service_account) to configure topics and subscriptions. If the role assigned to the service account changes and the appropriate permissions aren't updated, the Cloud Functions service can't access Pub/Sub and the deployment fails.

**The error message**

###  Console 
    
    
    Failed to configure trigger PubSub projects/PROJECT_ID/topics/FUNCTION_NAME
    

###  gcloud 
    
    
    ERROR: (gcloud.functions.deploy) OperationError: code=13, message=Failed to configure trigger PubSub projects/PROJECT_ID/topics/FUNCTION_NAME
    

**The solution**

You can [reset your service account](https://docs.cloud.google.com/functions/docs/concepts/iam#google_cloud_functions_service_agent_service_account) to the default `cloudfunctions.serviceAgent` role.

### Default runtime service account does not exist

When a [user-managed service account](https://docs.cloud.google.com/functions/docs/securing/function-identity#individual) is not specified, Cloud Run functions (1st gen) uses the [App Engine service account](https://docs.cloud.google.com/functions/docs/securing/function-identity#runtime_service_account) by default. Deployments fail if you delete the default account without specifying a user-managed service account.

**The error message**

###  gcloud 
    
    
    ERROR: (gcloud.functions.deploy) ResponseError: status=[400], code=[Ok], message=[Default service account 'test-project-356312@appspot.gserviceaccount.com' doesn't exist. Please recreate this account or specify a different account. Please visit https://cloud.google.com/functions/docs/troubleshooting for in-depth troubleshooting documentation.]
    

**The solution**

To resolve this issue, follow any of these solutions:

  * Specify a [user-managed runtime service account](https://docs.cloud.google.com/functions/docs/securing/function-identity#individual) when deploying your function.

  * [Recreate the default service account](https://docs.cloud.google.com/appengine/docs/legacy/standard/python/service-account#repair-service-account) PROJECT_ID@appspot.gserviceaccount.com for your project.

  * [Undelete](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#undeleting-numeric-id) the default service account.




### User missing permissions for runtime service account while deploying a function

Every function is associated with a service account that serves as its identity when the function accesses other resources. This [runtime service account](https://docs.cloud.google.com/functions/docs/securing/function-identity#runtime-sa) can be the default service account or a user-managed service account. For Cloud Functions to use a runtime service account, the deployer must have the `iam.serviceAccounts.actAs` permission on that service account. A user who creates a non-default runtime service account is automatically granted this permission, but other deployers must have this permission granted by a user with the correct permissions.

A user who has been assigned the Project Viewer, Cloud Functions Developer, or Cloud Functions Admin role must additionally be assigned the `iam.serviceAccounts.actAs` permission on the runtime service account.

**The error message**

###  Console
    
    
    You must have the iam.serviceAccounts.actAs permission on the selected service account. To obtain this permission, you can grant a role that includes it like the Service Account User role, on the project.
    

###  gcloud 

The following error occurs for the default service account:
    
    
    ERROR: (gcloud.functions.deploy) ResponseError: status=[403], code=[Ok], message=[Caller USER is missing permission 'iam.serviceaccounts.actAs' on service account PROJECT_ID@appspot.gserviceaccount.com. Grant the role 'roles/iam.serviceAccountUser' to the caller on the service account PROJECT_ID@appspot.gserviceaccount.com. You can do that by running 'gcloud iam service-accounts add-iam-policy-binding
    PROJECT_ID@appspot.gserviceaccount.com --member MEMBER --role roles/iam.serviceAccountUser' where MEMBER has a prefix like 'user:' or 'serviceAccount:'.
    

The following error occurs for the non-default service account:
    
    
    ERROR: (gcloud.functions.deploy) ResponseError: status=[403], code=[Ok], message=[Caller USER is missing permission 'iam.serviceaccounts.actAs' on service account SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com. Grant the role 'roles/iam.serviceAccountUser' to the caller on the service account SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com. You can do that by running 'gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com --member MEMBER --role roles/iam.serviceAccountUser' where MEMBER has a prefix like 'user:' or 'serviceAccount:'.
    

**Note:** `PROJECT_ID@appspot.gserviceaccount.com` is the default runtime service account for Cloud Run functions(1st gen). This is replaced by the user-managed service account `SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com` in the error message when you use a non-default service account.

**The solution**

[Assign the user](https://docs.cloud.google.com/functions/docs/reference/iam/roles#additional-configuration) `roles/iam.serviceAccountUser` role on the default or user-managed service account. This role includes the `iam.serviceAccounts.actAs` permission.

### Cloud Run functions Service Agent service account missing project bucket permissions while deploying a function

Cloud Run functions can only be [triggered by events](https://docs.cloud.google.com/functions/docs/calling/storage) from Cloud Storage buckets in the same Google Cloud Project. In addition, the Cloud Functions Service Agent service account (`service-PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com`) needs the `cloudfunctions.serviceAgent` role on your project.

**The error message**

###  Console 
    
    
    Deployment failure: Insufficient permissions to (re)configure a trigger
    (permission denied for bucket BUCKET_ID). Please, give owner permissions
    to the editor role of the bucket and try again.
    

###  gcloud 
    
    
    ERROR: (gcloud.functions.deploy) OperationError: code=7, message=Insufficient
    permissions to (re)configure a trigger (permission denied for bucket BUCKET_ID).
    Please, give owner permissions to the editor role of the bucket and try again.
    

**The solution**

To resolve this error, [reset the Service Agent service account](https://docs.cloud.google.com/functions/docs/concepts/iam#google_cloud_functions_service_agent_service_account) to the default role.

### User with Project Editor role can't make a function public

The Project Editor role has broad permissions to manage resources within a project, but it doesn't inherently grant the ability to make Cloud Run functions public. You must grant the `cloudfunctions.functions.setIamPolicy` permission to the user or the service deploying the function.

**The error message**

###  gcloud 
    
    
     ERROR: (gcloud.functions.add-iam-policy-binding) ResponseError: status=[403], code=[Forbidden], message=[Permission 'cloudfunctions.functions.setIamPolicy' denied on resource 'projects/PROJECT_ID/locations/LOCATION/functions/FUNCTION_NAME (or resource may not exist).]
    

**The solution**

To resolve this error, follow any of these solutions:

  * Assign the deployer either the [Project Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) or the [Cloud Functions Admin](https://docs.cloud.google.com/functions/docs/reference/iam/roles) role, both of which contain the `cloudfunctions.functions.setIamPolicy` permission.

  * Grant the permission manually by creating a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

  * Check if [domain restricted sharing](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam#domain_restricted_sharing) is enforced on the project.




### Function deployment fails when using Resource Location Restriction organization policy

If your organization uses a [Resource Location Restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) policy, it will restrict function deployment in the regions restricted by the policy. In the Google Cloud console, the restricted region won't be available from the region drop-down while deploying a function.

**The error message**

###  gcloud 
    
    
      ERROR: (gcloud.functions.deploy) ResponseError: status=[400], code=[Ok], message=[The request has violated one or more Org Policies. Please refer to the respective violations for more information. violations {
        type: "constraints/gcp.resourceLocations"
        subject: "orgpolicy:projects/PROJECT_ID"
        description: "Constraint constraints/gcp.resourceLocations violated for projects/PROJECT_ID attempting GenerateUploadUrlActionV1 with location set to RESTRICTED_LOCATION. See https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints for more information."
      }
    

**The solution**

Add or remove locations from the `allowed_values` or `denied_values` lists of the resource locations constraint for successful deployment.

### Function deployment fails while executing function's global scope

This error indicates that there was a problem with your code. The deployment pipeline finished deploying the function, but failed at the last step - sending a health check to the function. This health check is meant to execute a function's [global scope](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#scope), which could be throwing an exception, crashing, or timing out. The global scope is where you commonly load in libraries and initialize clients.

**The error message**

###  Console 
    
    
    Deployment failure: Function failed on loading user code. This is likely due to a bug in the user code.
    

###  gcloud 
    
    
    ERROR: (gcloud.functions.deploy) OperationError: code=3, message=Function
    failed on loading user code. This is likely due to a bug in the user code.
    

In Cloud Logging logs:
    
    
      "Function failed on loading user code. This is likely due to a bug in the user code."
    

**The solution**

To resolve this issue, follow any of these solutions:

  * For a more detailed error message, review your function's [build logs](https://docs.cloud.google.com/functions/docs/building#view_your_build_image_logs).

  * If it is unclear why your function failed to execute its global scope, consider temporarily moving the code into the request invocation, using [lazy initialization of the global variables](https://docs.cloud.google.com/functions/docs/bestpractices/tips#do_lazy_initialization_of_global_variables). This lets you add extra log statements around your client libraries, which could be timing out on their instantiation (especially if they are calling other services), or crashing or throwing exceptions altogether.

  * Increase the function timeout.

  * The source code must contain an entry point function that has been correctly specified in the deployment, either through the [console](https://docs.cloud.google.com/functions/docs/deploying/console) or [gcloud](https://docs.cloud.google.com/functions/docs/deploying/filesystem).




### User with Viewer role cannot deploy a function

Users with either the Project Viewer or Cloud Functions Viewer role have _read-only_ access to functions and function details, and can't deploy new functions. The **Create function** feature is grayed out in the Google Cloud console with the following error:

**The error message**

###  gcloud 
    
    
    ERROR: (gcloud.functions.deploy) PERMISSION_DENIED: Permission
    'cloudfunctions.functions.sourceCodeSet' denied on resource
    'projects/PROJECT_ID/locations/LOCATION` (or resource may not exist)
    

**The solution**

Assign the user [Cloud Functions Developer](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.developer) role.

### Build service account missing permissions

**The error message**

In the function deploy error or in the build logs, you may see one of the following errors:
    
    
    The service account running this build does not have permission to write logs.
    To fix this, grant the Logs Writer (roles/logging.logWriter) role to the service
    account.
    
    
    
    Step #0 - "fetch": failed to Fetch: failed to download archive gs://gcf-sources-PROJECT_NUMBER-LOCATION/FUNCTION_NAME/version-VERSION_NUMBER/function-source.zip: Access to bucket gcf-sources-PROJECT_NUMBER-LOCATION denied. You must grant Storage Object Viewer permission to PROJECT_NUMBER-compute@developer.gserviceaccount.com.
    
    
    
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

HTTP functions without **Allow unauthenticated invocations** enabled restrict access to end users and service accounts that don't have appropriate [permissions](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam#gcloud_4).

Visiting the Cloud Run functions URL in a browser doesn't add an authentication header automatically.

**The error message**

HTTP Error Response code: 403 Forbidden

HTTP Error Response body:
    
    
    Error: Forbidden Your client does not have permission
    to get URL /FUNCTION_NAME from this server.
    

**The solution**

To resolve this error, follow either of these solutions:

  * Assign the user the [Cloud Run functions Invoker](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.invoker) role.

  * Redeploy your function [to allow unauthenticated invocations](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam#gcloud_4) if this is supported by your organization. This can be useful for testing purposes.




### Serving permission error due to `allow internal traffic only` configuration

Ingress settings restrict whether an HTTP function can be invoked by resources outside of your Google Cloud project or VPC Service Controls service perimeter. When you configure **allow internal traffic only** setting for ingress networking, this error message indicates that only requests from VPC networks in the same project or VPC Service Controls perimeter are allowed.

**Note:** Visiting the Cloud Run functions URL in a browser does not add an authentication header automatically.

**The error message**

HTTP Error Response code: 404 NOT FOUND

HTTP Error Response body:
    
    
    404 Page not found
    

**The solution**

To resolve this error, follow either of these solutions:

  * Ensure that the request is coming from your Google Cloud project or VPC Service Controls service perimeter.

  * Change the ingress settings to [allow all traffic](https://docs.cloud.google.com/functions/docs/networking/network-settings#ingress_settings) for the function.

  * Cloud Run functions source code can result in a 404 error due to incorrect function URL, HTTP methods, or logic errors.




### Function invocation lacks valid authentication credentials

Functions configured with [restricted access](https://docs.cloud.google.com/functions/docs/securing) require an [ID token](https://developers.google.com/identity/protocols/oauth2/openid-connect#obtainuserinfo). Function invocation fails if you use [access tokens](https://developers.google.com/identity/protocols/oauth2?_ga=2.163318204.1401894525.1612199962-958658716.1595873194#2.-obtain-an-access-token-from-the-google-authorization-server.) or [refresh tokens](https://developers.google.com/identity/protocols/oauth2?_ga=2.163318204.1401894525.1612199962-958658716.1595873194#5.-refresh-the-access-token,-if-necessary.).

**The error message**

HTTP Error Response code: 401 Unauthorized

HTTP Error Response body:
    
    
    Your client does not have permission to the requested URL </FUNCTION_NAME>
    

**The solution**

To resolve this error, follow either of these solutions:

  * Make sure that your requests include an [`Authorization: Bearer ID_TOKEN` header](https://docs.cloud.google.com/functions/docs/securing/authenticating), and that the token is an ID token, not an access or refresh token. If you generate this token manually with a service account's private key, you must exchange the self-signed JWT token for a Google-signed identity token. For more information, see [Authenticate for invocation](https://docs.cloud.google.com/functions/docs/securing/authenticating#generating_tokens_manually).

  * Invoke your HTTP function using authentication credentials in your request header. For example, you can get an identity token using gcloud as follows:
        
        curl  -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
          https://REGION-PROJECT_ID.cloudfunctions.net/FUNCTION_NAME

For more information, see [Authenticating for invocation ](https://docs.cloud.google.com/functions/docs/securing/authenticating#authenticating_function_to_function_calls).




### Function stops mid-execution, or continues running after your code finishes

Some Cloud Run functions runtimes allow users to run asynchronous tasks. If your function creates such tasks, it must also explicitly wait for these tasks to complete. Failure to do so might cause your function to stop executing at the wrong time.

**The error behavior**

Your function exhibits one of the following behaviors:

  * Your function terminates while asynchronous tasks are still running, but before the specified timeout period has elapsed.
  * Your function doesn't stop running when these tasks finish, and continues to run until the timeout period has elapsed.



**The solution**

If your function terminates early, you should make sure all your function's asynchronous tasks are complete before your function performs any of the following actions:

  * Returning a value
  * Resolving or rejecting a returned `Promise` object (Node.js functions only)
  * Throwing uncaught exceptions and errors
  * Sending an HTTP response
  * Calling a callback function



If your function fails to terminate after completing asynchronous tasks, you should verify that your function is correctly signaling Cloud Run functions after it has completed. In particular, make sure that you perform one of the operations listed in the preceding list as soon as your function has finished its asynchronous tasks.

### Runtime error when accessing resources protected by VPC Service Controls

By default, Cloud Run functions uses public IP addresses to make outbound requests to other services. Functions that are not within the VPC Service Controls perimeter might receive HTTP `403` responses when attempting to access Google Cloud services protected by VPC Service Controls, due to service perimeter denials.

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

  * Alternatively grant the function's [runtime service account](https://docs.cloud.google.com/functions/docs/concepts/iam#runtime_service_accounts) access to the perimeter. You can do this either by [creating an access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#members-example) and [adding the access level to the service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#add-access-level), or by [creating an ingress policy](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) on the perimeter. See [Using VPC Service Controls with functions outside a perimeter](https://docs.cloud.google.com/functions/docs/securing/using-vpc-service-controls#functions-outside-perimeter) for more information.




## Scalability

This section lists scalability issues and provides suggestions for how to fix each of them.

### Cloud Logging errors related to pending queue request aborts

The following conditions can be associated with scaling failures.

  * A huge sudden increase in traffic.
  * Long [cold start time](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#cold-starts).
  * Long request processing time.
  * High function error rate.
  * Reaching the [maximum instance limit](https://docs.cloud.google.com/functions/docs/configuring/max-instances).
  * Transient factors attributed to the Cloud Run functions service.



In each case Cloud Run functions might not scale up fast enough to manage the traffic.

**The error message**
    
    
     The request was aborted because there was no available instance.
    

Cloud Run functions has the following severity levels:
    
    
    * `severity=WARNING` ( Response code: 429 ) Cloud Run functions cannot scale due
      to the [`max-instances`](/functions/docs/configuring/max-instances) limit you set
      during configuration.
    * `severity=ERROR` ( Response code: 500 ) Cloud Run functions intrinsically
      cannot manage the rate of traffic.
    

**The solution**

  * For HTTP trigger-based functions, implement exponential backoff and retries for requests that must not be dropped. If you are [triggering Cloud Run functions from Workflows](https://docs.cloud.google.com/workflows/docs/calling-run-functions), you can use the [`try/retry` syntax](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying) to achieve this.
  * For background or event-driven functions, Cloud Run functions supports [at-least-once delivery](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#execution-guarantees). Even without explicitly enabling retry, the event is automatically re-delivered and the function execution will be retried. For more information, see [Enable event-driven function retries](https://docs.cloud.google.com/functions/docs/bestpractices/retries).
  * When the root cause of the issue is a period of heightened transient errors attributed solely to Cloud Run functions or if you need assistance with your issue, contact [Cloud Customer Care](https://docs.cloud.google.com/functions/docs/getting-support).



## Logging

The following section covers issues with logging and how to fix them.

### Logs entries have none or incorrect log severity levels

Cloud Run functions includes runtime logging by default. Logs written to `stdout` or `stderr` appear automatically in the [Google Cloud console](https://console.cloud.google.com/project/_/logs?service=cloudfunctions.googleapis.com). But these log entries by default, contain only string messages.

**The solution**

To include log severities, you must send a structured log entry.

**Note:** As of September 2020, **every** newly released runtime will use the default severity log level behavior as defined by the runtime library itself. For example, Python 3.8 sets the default severity log level at `WARNING` or higher. If you want to capture events with `DEBUG` or `INFO` severity using Python 3.8, you must also programmatically set your log level to include those levels.

### Handle or log exceptions differently in the event of a crash

You might want to customize how you manage and log crash information.

**The solution**

Wrap your function in a `try` block to customize handling exceptions and logging stack traces.

Adding a `try` block can result in an unintended side effect in event-driven functions with the `retry on failure` configuration. Retrying failed events might itself fail.

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

Cloud Run functions streams Cloud Run function logs to a default bucket. When you create a project, Cloud Run functions creates and enables the default bucket. If the default bucket is disabled or if Cloud Run function logs are in the exclusion filter, the logs won't appear in the Logs Explorer.

**The solution**

Enable default logs and ensure no exclusion filter is set.

**Note:** Enabling Cloud Logging might incur charges.

### Cloud Run functions logs are not appearing in Logs Explorer

Some Cloud Logging client libraries use an asynchronous process to write log entries. If a function crashes, or otherwise terminates, it is possible that some log entries have not been written yet and might appear later. It is also possible that some logs will be lost and cannot be seen in Logs Explorer.

**The solution**

Use the client library interface to flush buffered log entries before exiting the function or use the library to write log entries synchronously. You can also synchronously write logs directly to `stdout` or `stderr`.

### Cloud Run functions logs are not appearing using Log Router sink

Log Router sinks [route](https://docs.cloud.google.com/logging/docs/routing/overview) log entries to various destinations.

![Screenshot of Console Log Router with View sink details highlighted](https://docs.cloud.google.com/static/functions/img/logs-router.png)

Included in the settings are **Exclusion filters** , which define entries that can be discarded.

![Screenshot of Console Log Router Sink Details dialog showing exclusion filter](https://docs.cloud.google.com/static/functions/img/sink-details.png)

**The solution**

Remove exclusion filter set for `resource.type="cloud_functions"`.

## Database connections

Many database errors are associated with exceeding connection limits or timing out. If you see a Cloud SQL warning in your logs, for example, `Context deadline exceeded`, you might need to adjust your connection configuration. For more information, see [Cloud SQL best practices](https://docs.cloud.google.com/sql/docs/mysql/connect-functions#best-practices).

## Networking

This section lists networking issues and provides suggestions for how to fix each of them.

### Network connectivity

If all outbound requests from a Cloud Run function fail even after you configure [egress settings](https://docs.cloud.google.com/functions/docs/networking/network-settings#egress_settings), you can run Connectivity Tests to identify any underlying network connectivity issues. For more information, see [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests).

### Serverless VPC Access connector is not ready or does not exist

If a Serverless VPC Access connector fails, it might not be using a `/28` subnet mask dedicated to the connector as [required](https://docs.cloud.google.com/functions/docs/networking/connecting-vpc#create-connector).

**The error message**
    
    
    VPC connector projects/xxxxx/locations/REGION/connectors/xxxx
    is not ready yet or does not exist.
    

When Cloud Run functions is deployed with a connector in a bad state due to missing permission on the [Google APIs Service Agent service account](https://docs.cloud.google.com/iam/docs/service-agents#google-apis-service-agent) `PROJECT_NUMBER@cloudservices.gserviceaccount.com`, it results in the following error:

**The error message**
    
    
    Failed to prepare VPC connector. Please try again later.
    

**The solution**

[List your subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#listing_existing_subnets) to check whether your connector uses a `/28` subnet mask. If your connector doesn't use the `/28` subnet mask, [recreate or create a new connector](https://docs.cloud.google.com/functions/docs/networking/connecting-vpc#create-connector).

To resolve this issue, follow any of these solutions:

  * If you recreate the connector, you don't need to redeploy other functions. You might experience a network interruption as the connector is recreated.

  * If you create a new alternate connector, redeploy your functions to use the new connector, and then delete the original connector. This method avoids network interruption.

  * Ensure the Cloud Run functions and its associated connector are deployed in the same region.

  * For the Shared VPC configuration :

    * Ensure that the service accounts `SERVICE_PROJECT_NUMBER@cloudservices.gserviceaccount.com` and `service-SERVICE_PROJECT_NUMBER@gcp-sa-vpcaccess.iam.gserviceaccount.com` used by VPC Connector to provision resources in the project are not missing permissions. These service accounts should have the `roles/compute.networkUser` role in the host project of Shared VPC configuration when the connector is in the service project. Otherwise, `roles/compute.networkAdmin` is required.

    * If the connector is created in the host project, ensure that the `Serverless VPC Access User` role is [granted](https://docs.cloud.google.com/functions/docs/networking/shared-vpc-host-project#provide_access_to_the_connector) on `Cloud Run functions Service Agent` in your host project.

    * If the connector status shows `Connector is in a bad state, manual deletion recommended` error, and the [Google APIs Service Agent](https://docs.cloud.google.com/compute/docs/access/service-accounts#google_apis_service_agent) is missing the required permissions to provision compute resources in the connector's project, grant `roles/compute.admin` to the `PROJECT_NUMBER@cloudservices.gserviceaccount.com` service account. In some cases you may need to recreate the connector after updating permissions.




### SMTP traffic to external destination IP addresses using TCP port 25 is blocked

For added security, Google Cloud blocks connections to TCP destination port `25` when sending emails from Cloud Run functions.

**The solution**

To unblock these connections, choose one of the following options:

  * Connect to your SMTP server on a different port, such as TCP port `587` or `465`.

  * [Use a third-party email service](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail#choosing_a_third-party_email_service_to_use).




## Other

This section outlines any additional issues that don't fit into other categories and offers solutions for each one.

### VPC Service Controls error on method `google.storage.buckets.testIamPermissions` in Cloud Audit Logs

When you open the **Function details** page in the Google Cloud console, Cloud Run functions checks whether you can modify the container image's storage repository and access it publicly. To verify, Cloud Run functions sends a request to the Container Registry bucket using the `google.storage.buckets.testIamPermissions` method with the following format: `[REGION].artifacts.[PROJECT_ID].appspot.com`. The only difference between the checks is that one runs with authentication to verify user permissions to modify the bucket, while the other check runs without authentication to verify whether the bucket is publicly accessible.

If the VPC Service Controls perimeter restricts the `storage.googleapis.com` API, the Google Cloud console shows an error on the `google.storage.buckets.testIamPermissions` method in Cloud Audit Logs.

**The error message**

For public access check with no authentication info, the **VPC SC Denial Policy** audit logs shows an entry similar to the following:
    
    
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
      "authenticationInfo": {},
      "requestMetadata": {
        "callerIp": "END_USER_IP"
      },
      "serviceName": "storage.googleapis.com",
      "methodName": "google.storage.buckets.testIamPermissions",
      "resourceName": "projects/PROJECT_NUMBER",
      "metadata": {
        "ingressViolations": [
          {
            "servicePerimeter": "accessPolicies/ACCESS_POLICY_ID/servicePerimeters/VPC_SC_PERIMETER_NAME",
            "targetResource": "projects/PROJECT_NUMBER"
          }
        ],
        "resourceNames": [
          "projects/_/buckets/REGION.artifacts.PROJECT_ID.appspot.com"
        ],
        "securityPolicyInfo": {
          "servicePerimeterName": "accessPolicies/ACCESS_POLICY_ID/servicePerimeters/VPC_SC_PERIMETER_NAME",
          "organizationId": "ORG_ID"
        },
        "violationReason": "NO_MATCHING_ACCESS_LEVEL",
      ...
    

For public access check with authentication info, the **VPC SC Denial Policy** audit logs shows an entry that allows the user to modify bucket settings similar to the following example:
    
    
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
        "principalEmail": "END_USER_EMAIL"
      },
      "requestMetadata": {
        "callerIp": "END_USER_IP",
        "requestAttributes": {},
        "destinationAttributes": {}
      },
      "serviceName": "storage.googleapis.com",
      "methodName": "google.storage.buckets.testIamPermissions",
      "resourceName": "projects/PROJECT_NUMBER",
      "metadata": {
        "ingressViolations": [
          {
            "servicePerimeter": "accessPolicies/ACCESS_POLICY_ID/servicePerimeters/VPC_SC_PERIMETER_NAME",
            "targetResource": "projects/PROJECT_NUMBER"
          }
        ],
        "resourceNames": [
          "projects/_/buckets/REGION.artifacts.PROJECT_ID.appspot.com"
        ],
        "securityPolicyInfo": {
          "servicePerimeterName": "accessPolicies/ACCESS_POLICY_ID/servicePerimeters/VPC_SC_PERIMETER_NAME",
          "organizationId": "ORG_ID"
        },
        "violationReason": "NO_MATCHING_ACCESS_LEVEL",
      ...
    

**The solution**

If the Container Registry bucket is not publicly accessible, you can ignore the VPC Service Controls errors.

Alternatively, you can add a VPC Service Controls [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules) to allow the `google.storage.buckets.testIamPermissions` method, as shown in the following example:
    
    
    ingress_from {
      sources {
        access_level: "*"
      }
      identity_type: ANY_IDENTITY
    }
    ingress_to {
      operations {
        service_name: "storage.googleapis.com"
        method_selectors {
          method: "google.storage.buckets.testIamPermissions"
        }
      }
      resources: "projects/PROJECT_NUMBER"
    }
    

Where possible, you can further refine the ingress rule by defining the access level with user IP addresses.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

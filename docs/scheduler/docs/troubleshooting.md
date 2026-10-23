---
url: https://docs.cloud.google.com/scheduler/docs/troubleshooting/
title: Troubleshoot Cloud Scheduler issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:43:08.568523+00:00
---

# Troubleshoot Cloud Scheduler issues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/scheduler/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Scheduler ](https://docs.cloud.google.com/scheduler/docs)
  * [ Guides ](https://docs.cloud.google.com/scheduler/docs/overview)



Send feedback 

#  Troubleshoot Cloud Scheduler issues Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Cloud Scheduler.

Cloud Scheduler publishes logs at the start of each job execution and at the end of each job execution. You can retrieve, view, and analyze the logs for a specific job, including the audit logs that are available for Cloud Scheduler. For more information, see [View logs](https://docs.cloud.google.com/scheduler/docs/viewing-logs).

By default, when a Cloud Scheduler job doesn't receive an acknowledgment from its target service—the job request handler—the job is considered to have failed. Cloud Scheduler will [retry](https://docs.cloud.google.com/scheduler/docs/configuring/retry-jobs) the job according to the exponential backoff you have configured.

For information about incidents affecting Google Cloud services, refer to the [Google Cloud Service Health Dashboard](https://status.cloud.google.com/summary) and [All incidents reported for Cloud Scheduler](https://status.cloud.google.com/products/Y9fKAQ6BVTQUYomrNN9A/history).

## Job fails due to a downstream service issue

A job failure might be due to an issue in a downstream service that Cloud Scheduler is targeting—for example, Cloud Run—rather than Cloud Scheduler itself. You can suspect a downstream service issue when the following conditions apply:

  * Permissions for Cloud Scheduler are correctly set up.
  * Cloud Scheduler can successfully reach the target service.
  * Error messages in the Cloud Scheduler execution logs originate from the downstream service.



To resolve this issue, complete the following steps:

  1. **Invoke the downstream service directly** : Verify that the downstream service can be successfully invoked without Cloud Scheduler. A successful invocation indicates that Cloud Scheduler is likely causing the issue; if unsuccessful, the downstream service requires further debugging.
  2. **Examine the destination service logs** : Examine the logs for the destination service, determine the errors being output, and triage them accordingly.
  3. **Look for long-running operations** : When Cloud Scheduler returns an HTTP `504` error for long-running operations (more than 30 minutes), check the destination service logs to see whether the execution succeeded or failed, as the destination service might have a longer request timeout. In such a scenario, Cloud Scheduler times out but the destination service doesn't.



## Job fails with a permission error

Permissions control which principals can access resources and what operations are allowed. Misconfigured permissions can disrupt job executions, and can lead to permission denied errors. [Audit logs](https://docs.cloud.google.com/scheduler/docs/audit-logging) provide a detailed record of all permission changes, allowing you to identify the source of these issues.

When your Cloud Scheduler job fails with a permission error, the execution logs might display a message similar to `"debugInfo":"URL_ERROR-ERROR_OTHER. Original HTTP response code number = 403"`.

To resolve this issue, complete one or more of the following verifications:

  * **Verify the IAM roles granted to the service agent** : The Cloud Scheduler service agent requires the [Cloud Scheduler Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudscheduler#cloudscheduler.serviceAgent) (`roles/cloudscheduler.serviceAgent`) role. Without this role, Cloud Scheduler jobs fail. You can manually grant the role to your Cloud Scheduler service agent. A manual grant is required **only** if you enabled the Cloud Scheduler API prior to March 19, 2019; or you removed the Cloud Scheduler Service Agent role. For more information, see [Grant the Cloud Scheduler Service Agent role](https://docs.cloud.google.com/scheduler/docs/http-target-auth#add).

  * **Verify your service account permissions** : Make sure that the [service account](https://docs.cloud.google.com/iam/docs/service-accounts) attached to your job has the correct permissions and scope to invoke the destination service. This includes scenarios where the target is in another project, or is the final target of an intermediary service. When your target is within Google Cloud, confirm that you have [granted the necessary roles](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts) to your service account. Each service within Google Cloud requires a specific role, and the receiving service automatically verifies the generated token. For example, for Cloud Run and Cloud Run functions, you must grant the `Cloud Run Invoker` role. When your target is outside of Google Cloud, the receiving service must [manually verify the token](https://developers.google.com/identity/sign-in/web/backend-auth#verify-the-integrity-of-the-id-token). For more information, see [Authenticate to Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/authentication) and [Use authentication with HTTP targets](https://docs.cloud.google.com/scheduler/docs/http-target-auth).

  * **Verify any VPC Service Controls violations** : [VPC Service Controls](https://docs.cloud.google.com/scheduler/docs/secure-with-vpcsc) is a Google Cloud feature that lets you set up a secure perimeter to guard against data exfiltration. To determine if an error is related to VPC Service Controls, check whether you have enabled VPC Service Controls and applied it to the projects and services you are attempting to use. To verify whether the projects and services are protected by VPC Service Controls, check the VPC Service Controls policy at that level of resource hierarchy.

To understand the scope of an issue, you can [retrieve VPC Service Controls errors from audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/retrieve-troubleshoot-errors).

    1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

    2. Query the audit logs for the following criteria:
           
           severity="ERROR" AND protoPayload.status.details.violations.type="VPC_SERVICE_CONTROLS"

Specifically, error messages might include the following text:

       * `Request is prohibited by organization's policy`
       * `Request violates VPC Service Controls`

For more information about issues that you might encounter when configuring VPC Service Controls, see [Troubleshoot common issues](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting).

  * **Verify any private endpoints** : Cloud Scheduler can only invoke certain private endpoints like Cloud Run, Cloud Run functions, and Google Cloud APIs within a VPC Service Controls perimeter. Check the ingress settings for your destination service—for example, see [Restrict network ingress for Cloud Run](https://docs.cloud.google.com/run/docs/securing/ingress)—and the permissions of the attached service account. You might receive an `URL_ERROR-ERROR_DNS` error message. For more information, in this document, see Job fails due to unreachable destination target.




## Job fails due to unreachable destination target

This issue occurs when your Cloud Scheduler job fails because the destination target is unreachable. The execution logs display errors starting with `URL_ERROR` or `URL_UNREACHABLE`.

To resolve this issue, depending on the error message received, complete one of the following checks:

  * **`URL_ERROR-ERROR_AUTHENTICATION`** : An HTTP `401 (Unauthorized)` or HTTP `407 (Proxy Authentication Required)` error is returned. The destination target requires authentication; however, the Cloud Scheduler request doesn't include a valid authentication token—for example, the request is missing an authorization header or the credentials are invalid. Check your job's authentication settings. For more information, see [Authenticate to Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/authentication) and [Use authentication with HTTP targets](https://docs.cloud.google.com/scheduler/docs/http-target-auth).

  * **`URL_ERROR-ERROR_DNS`** : Indicates that a URL fetch failed because the hostname couldn't be resolved using the Domain Name System (DNS)—for example, the hostname doesn't exist or has no associated IP address. The error message might include the text `Original HTTP response code number = 0`. Check the validity of the hostname and, when invoking a private endpoint, make sure that it is supported by Cloud Scheduler, and check its ingress settings.

  * **`URL_ERROR-ERROR_NOT_FOUND`** : The web server returns an HTTP `404 Not Found` error. Check if the target URL is correct and the resource exists.

  * **`URL_ERROR-ERROR_OTHER`** : This refers to a generic HTTP `4xx` error not previously detailed. Check the logs to retrieve the original HTTP response code. If you receive an HTTP `403` error, in this document, refer to Job fails with a permission error.

  * **`URL_UNREACHABLE-UNREACHABLE_5xx`** : The destination target returns an HTTP `5xx` or `429` error. This might be a transient condition—for example, an overloaded server. Check the logs of the destination target to debug the issue.

  * **`URL_UNREACHABLE-UNREACHABLE_CONNECTION_RESET`** : The connection was reset by the peer. Check for an issue on the external server side.

  * **`URL_UNREACHABLE-UNREACHABLE_ERROR`** : This indicates a network error. Check if the target URL is correct and if there are any firewall rules blocking access.




## Unsupported target when using a secure perimeter

When Cloud Scheduler is a restricted service in a VPC Service Controls perimeter, any attempt to create or update a job with an unsupported target will fail with a `TARGET_TYPE_NOT_PERMITTED_FOR_VPC` error code. For more information, see [Secure cron jobs with VPC Service Controls](https://docs.cloud.google.com/scheduler/docs/secure-with-vpcsc).

## Job execution issues

Cloud Scheduler jobs execute at defined times or regular intervals. The following issues might occur while a job is executing.

### A job that previously worked stops executing

This issue occurs when a Cloud Scheduler job that previously ran successfully stops executing because the Cloud Scheduler API is disabled. You can confirm the time the API was disabled by querying the audit logs for the following criteria:
    
    
    resource.type="audited_resource" AND
    protoPayload.serviceName="cloudscheduler.googleapis.com" AND
    operation.producer="serviceusage.googleapis.com" AND
    protoPayload.authorizationInfo.permission="serviceusage.services.disable"

To resolve this issue, [enable the Cloud Scheduler API](https://docs.cloud.google.com/scheduler/docs/setup#enable-api).

### Subsequent job executions aren't starting

This issue occurs when a job is still running or waiting for a response from its target. Other scheduled runs of the job are skipped until the current run finishes or times out.

In the logging entries, find the latest `type.googleapis.com/google.cloud.scheduler.logging.AttemptStarted` entry and its corresponding `type.googleapis.com/google.cloud.scheduler.logging.AttemptFinished` entry. If the `AttemptFinished` entry is missing or appears after the job's next scheduled run, other pending executions are blocked and won't start. Depending on the job's schedule, this can prevent multiple job executions from starting. To investigate further, verify the timeout on your job's destination target, and if this target has run into any issues.

Note that only a single instance of a job should be run at any time. In rare circumstances, it's possible for multiple instances of the same job to be requested. As a result, your request handler should be [idempotent](https://wikipedia.org/wiki/Idempotence), and your code should ensure that there are no harmful side effects if this occurs.

### A job's execution becomes irregular due to daylight saving time

When creating a Cloud Scheduler job using the Google Cloud console, you must specify a time zone. When using Google Cloud CLI, you can optionally specify a time zone using the `--time-zone` flag; otherwise, the default time zone used is Coordinated Universal Time or `UTC`.

This issue occurs when a job is configured with a non-UTC time zone and its execution becomes irregular due to daylight saving time (DST) changes. This is expected behavior.

If your job requires a very exact cadence, then you should choose a time zone that does not observe DST. Specifically, to avoid the problem altogether, configure your job schedule to use the UTC time zone.

For more information, see [Cron job format and time zone](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules).

## What's next

If you can't find a solution to your problem in the Cloud Scheduler documentation, then consider the following options:

  * Get support from the community by [asking questions on Stack Overflow](https://stackoverflow.com/questions/ask/advice?tags=google-cloud-scheduler), or [search for similar issues](https://stackoverflow.com/questions/tagged/google-cloud-scheduler) using the `google-cloud-scheduler` tag.
  * Open a support case by contacting [Google Cloud Customer Care](https://cloud.google.com/support-hub).
  * Open a bug or feature request by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



For more information, see [Cloud Scheduler support](https://docs.cloud.google.com/scheduler/docs/support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

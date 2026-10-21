---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/tasks/queues/update/
title: gcloud alpha tasks queues update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:09:31.569878+00:00
---

# gcloud alpha tasks queues update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/tasks/queues/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha tasks queues update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha tasks queues update - update a Cloud Tasks queue 
SYNOPSIS
    

`gcloud alpha tasks queues update` `QUEUE` [`--location`=`LOCATION`] [`--clear-http-header-override` | `--http-header-override`=`HEADER_FIELD`: `HEADER_VALUE`] [`--clear-http-method-override` | `--http-method-override`=`HTTP_METHOD_OVERRIDE`] [`--clear-http-oauth-service-account-email-override` | `--http-oauth-service-account-email-override`=`HTTP_OAUTH_SERVICE_ACCOUNT_EMAIL_OVERRIDE`] [`--clear-http-oauth-token-scope-override` | `--http-oauth-token-scope-override`=`HTTP_OAUTH_TOKEN_SCOPE_OVERRIDE`] [`--clear-http-oidc-service-account-email-override` | `--http-oidc-service-account-email-override`=`HTTP_OIDC_SERVICE_ACCOUNT_EMAIL_OVERRIDE`] [`--clear-http-oidc-token-audience-override` | `--http-oidc-token-audience-override`=`HTTP_OIDC_TOKEN_AUDIENCE_OVERRIDE`] [`--clear-http-uri-override` | `--http-uri-override`=`KEY`:`VALUE`,[`KEY`:`VALUE`,…]] [`--clear-max-attempts` | `--max-attempts`=`MAX_ATTEMPTS`] [`--clear-max-backoff` | `--max-backoff`=`MAX_BACKOFF`] [`--clear-max-concurrent-tasks` | `--max-concurrent-tasks`=`MAX_CONCURRENT_TASKS`] [`--clear-max-doublings` | `--max-doublings`=`MAX_DOUBLINGS`] [`--clear-max-retry-duration` | `--max-retry-duration`=`MAX_RETRY_DURATION`] [`--clear-max-tasks-dispatched-per-second` | `--max-tasks-dispatched-per-second`=`MAX_TASKS_DISPATCHED_PER_SECOND`] [`--clear-min-backoff` | `--min-backoff`=`MIN_BACKOFF`] [`--clear-routing-override` | `--routing-override`=`KEY`:`VALUE`,[…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The flags available to this command represent the fields of a queue that are mutable. Attempting to use this command on a different type of queue will result in an error. 
EXAMPLES
     To update a Cloud Tasks queue: 
    
    
    gcloud alpha tasks queues update my-queue --clear-max-attempts --clear-max-retry-duration --clear-max-doublings --clear-min-backoff --clear-max-backoff --clear-max-tasks-dispatched-per-second --clear-max-concurrent-tasks --clear-routing-override

POSITIONAL ARGUMENTS
    

`QUEUE`
     The queue to update. 
FLAGS
    

`--location`=`LOCATION`
     The location where we want to manage the queue or task. If not specified, uses the location of the current project's App Engine app if there is an associated app. 
At most one of these can be specified: 

`--clear-http-header-override`
     Clear the field corresponding to `--http-header-override`. 
`--http-header-override`=`HEADER_FIELD`: `HEADER_VALUE`
     If provided, the specified HTTP headers override the existing headers for all tasks in the queue. If a task has a header with the same Key as a queue-level header override, then the value of the task header will be overriden with the value of the queue-level header. Otherwise, the queue-level header will be added to the task headers. Header values can contain commas. This flag can be repeated. Repeated header fields will have their values overridden. 
At most one of these can be specified: 

`--clear-http-method-override`
     Clear the field corresponding to `--http-method-override`. 
`--http-method-override`=`HTTP_METHOD_OVERRIDE`
     If provided, the specified HTTP method type override is used for all tasks in the queue, no matter what is set at the task-level. 
At most one of these can be specified: 

`--clear-http-oauth-service-account-email-override`
     Clear the field corresponding to `--http-oauth-service-account-email-override`. 
`--http-oauth-service-account-email-override`=`HTTP_OAUTH_SERVICE_ACCOUNT_EMAIL_OVERRIDE`
     The service account email to be used for generating an OAuth2 access token to be included in the request sent to the target when executing the task. The service account must be within the same project as the queue. The caller must have 'iam.serviceAccounts.actAs' permission for the service account. 
At most one of these can be specified: 

`--clear-http-oauth-token-scope-override`
     Clear the field corresponding to `--http-oauth-token-scope-override`. 
`--http-oauth-token-scope-override`=`HTTP_OAUTH_TOKEN_SCOPE_OVERRIDE`
     The scope to be used when generating an OAuth2 access token to be included in the request sent to the target when executing the task. If not specified, 'https://www.googleapis.com/auth/cloud-platform' will be used. 
At most one of these can be specified: 

`--clear-http-oidc-service-account-email-override`
     Clear the field corresponding to `--http-oidc-service-account-email-override`. 
`--http-oidc-service-account-email-override`=`HTTP_OIDC_SERVICE_ACCOUNT_EMAIL_OVERRIDE`
     The service account email to be used for generating an OpenID Connect token to be included in the request sent to the target when executing the task. The service account must be within the same project as the queue. The caller must have 'iam.serviceAccounts.actAs' permission for the service account. 
At most one of these can be specified: 

`--clear-http-oidc-token-audience-override`
     Clear the field corresponding to `--http-oidc-token-audience-override`. 
`--http-oidc-token-audience-override`=`HTTP_OIDC_TOKEN_AUDIENCE_OVERRIDE`
     The audience to be used when generating an OpenID Connect token to be included in the request sent to the target when executing the task. If not specified, the URI specified in the target will be used. 
At most one of these can be specified: 

`--clear-http-uri-override`
     Clear the field corresponding to `--http-uri-override`. 
`--http-uri-override`=`KEY`:`VALUE`,[`KEY`:`VALUE`,…]
     If provided, the specified HTTP target URI override is used for all tasks in the queue depending on what is set as the mode. Allowed values for mode are: ALWAYS, IF_NOT_EXISTS. If not set, mode defaults to ALWAYS. 

KEY must be at least one of: [scheme, host, port, path, query, mode]. Any missing keys will use the default. 

At most one of these can be specified: 

`--clear-max-attempts`
     Clear the field corresponding to `--max-attempts`. 
`--max-attempts`=`MAX_ATTEMPTS`
     The maximum number of attempts per task in the queue. 
At most one of these can be specified: 

`--clear-max-backoff`
     Clear the field corresponding to `--max-backoff`. 
`--max-backoff`=`MAX_BACKOFF`
     The maximum amount of time to wait before retrying a task after it fails. Must be a string that ends in 's', such as "5s". 
At most one of these can be specified: 

`--clear-max-concurrent-tasks`
     Clear the field corresponding to `--max-concurrent-tasks`. 
`--max-concurrent-tasks`=`MAX_CONCURRENT_TASKS`
     The maximum number of concurrent tasks that Cloud Tasks allows to be dispatched for this queue. After this threshold has been reached, Cloud Tasks stops dispatching tasks until the number of outstanding requests decreases. 
At most one of these can be specified: 

`--clear-max-doublings`
     Clear the field corresponding to `--max-doublings`. 
`--max-doublings`=`MAX_DOUBLINGS`
     The time between retries will double maxDoublings times. 

A tasks retry interval starts at minBackoff, then doubles maxDoublings times, then increases linearly, and finally retries retries at intervals of maxBackoff up to maxAttempts times. 

For example, if minBackoff is 10s, maxBackoff is 300s, and maxDoublings is 3, then the a task will first be retried in 10s. The retry interval will double three times, and then increase linearly by 2^3 * 10s. Finally, the task will retry at intervals of maxBackoff until the task has been attempted maxAttempts times. Thus, the requests will retry at 10s, 20s, 40s, 80s, 160s, 240s, 300s, 300s. 

At most one of these can be specified: 

`--clear-max-retry-duration`
     Clear the field corresponding to `--max-retry-duration`. 
`--max-retry-duration`=`MAX_RETRY_DURATION`
     The time limit for retrying a failed task, measured from when the task was first run. Once the `--max-retry-duration` time has passed and the task has been attempted --max-attempts times, no further attempts will be made and the task will be deleted. 

Must be a string that ends in 's', such as "5s". 

At most one of these can be specified: 

`--clear-max-tasks-dispatched-per-second`
     Clear the field corresponding to `--max-tasks-dispatched-per-second`. 
`--max-tasks-dispatched-per-second`=`MAX_TASKS_DISPATCHED_PER_SECOND`
     The maximum rate at which tasks are dispatched from this queue. 
At most one of these can be specified: 

`--clear-min-backoff`
     Clear the field corresponding to `--min-backoff`. 
`--min-backoff`=`MIN_BACKOFF`
     The minimum amount of time to wait before retrying a task after it fails. Must be a string that ends in 's', such as "5s". 
At most one of these can be specified: 

`--clear-routing-override`
     Clear the field corresponding to `--routing-override`. 
`--routing-override`=`KEY`:`VALUE`,[…]
     If provided, the specified App Engine route is used for all tasks in the queue, no matter what is set is at the task-level. 

KEY must be at least one of: [service, version, instance]. Any missing keys will use the default. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud tasks queues update](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/update)
    
    
    [gcloud beta tasks queues update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/tasks/queues/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/sdk/gcloud/reference/tasks/create-http-task/
title: gcloud tasks create-http-task \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:45:03.848846+00:00
---

# gcloud tasks create-http-task  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/tasks/create-http-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud tasks create-http-task Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud tasks create-http-task - create and add a task that targets a HTTP endpoint 
SYNOPSIS
    

`gcloud tasks create-http-task` [`TASK_ID`] `--queue`=`QUEUE` `--url`=`URL` [`--header`=`HEADER_FIELD`: `HEADER_VALUE`] [`--location`=`LOCATION`] [`--method`=`METHOD`] [`--schedule-time`=`SCHEDULE_TIME`] [`--body-content`=`BODY_CONTENT` | `--body-file`=`BODY_FILE`] [[`--oauth-service-account-email`=`OAUTH_SERVICE_ACCOUNT_EMAIL` : `--oauth-token-scope`=`OAUTH_TOKEN_SCOPE`] | [`--oidc-service-account-email`=`OIDC_SERVICE_ACCOUNT_EMAIL` : `--oidc-token-audience`=`OIDC_TOKEN_AUDIENCE`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create and add a task that targets a HTTP endpoint. 
EXAMPLES
     To create a task: 
    
    
    gcloud tasks create-http-task --queue=my-queue --url=http://example.com/handler-path my-task

POSITIONAL ARGUMENTS
    

[`TASK_ID`]
     The task to create. 

If not specified then the system will generate a random unique task ID. Explicitly specifying a task ID enables task de-duplication. If a task's ID is identical to that of an existing task or a task that was deleted or completed recently then the call will fail. 

Because there is an extra lookup cost to identify duplicate task names, tasks created with IDs have significantly increased latency. Using hashed strings for the task ID or for the prefix of the task ID is recommended. 

REQUIRED FLAGS
    

`--queue`=`QUEUE`
     The queue the task belongs to. 
`--url`=`URL`
     The full URL path that the request will be sent to. This string must begin with either "http://" or "https://". 
OPTIONAL FLAGS
    

`--header`=`HEADER_FIELD`: `HEADER_VALUE`
     An HTTP request header. Header values can contain commas. This flag can be repeated. Repeated header fields will have their values overridden. 
`--location`=`LOCATION`
     The location where we want to manage the queue or task. If not specified, uses the location of the current project's App Engine app if there is an associated app. 
`--method`=`METHOD`
     The HTTP method to use for the request. If not specified, "POST" will be used. 
`--schedule-time`=`SCHEDULE_TIME`
     The time when the task is scheduled to be first attempted. Defaults to "now" if not specified. 
At most one of these can be specified: 

`--body-content`=`BODY_CONTENT`
     HTTP Body data sent to the task worker processing the task. 
`--body-file`=`BODY_FILE`
     File containing HTTP body data sent to the task worker processing the task. 
How the request sent to the target when executing the task should be authenticated. At most one of these can be specified: 

OAuth2 
`--oauth-service-account-email`=`OAUTH_SERVICE_ACCOUNT_EMAIL`
     The service account email to be used for generating an OAuth2 access token to be included in the request sent to the target when executing the task. The service account must be within the same project as the queue. The caller must have 'iam.serviceAccounts.actAs' permission for the service account. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--oauth-token-scope`=`OAUTH_TOKEN_SCOPE`
     The scope to be used when generating an OAuth2 access token to be included in the request sent to the target when executing the task. If not specified, 'https://www.googleapis.com/auth/cloud-platform' will be used. 
OpenId Connect 
`--oidc-service-account-email`=`OIDC_SERVICE_ACCOUNT_EMAIL`
     The service account email to be used for generating an OpenID Connect token to be included in the request sent to the target when executing the task. The service account must be within the same project as the queue. The caller must have 'iam.serviceAccounts.actAs' permission for the service account. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--oidc-token-audience`=`OIDC_TOKEN_AUDIENCE`
     The audience to be used when generating an OpenID Connect token to be included in the request sent to the target when executing the task. If not specified, the URI specified in the target will be used. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha tasks create-http-task](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/tasks/create-http-task)
    
    
    [gcloud beta tasks create-http-task](https://docs.cloud.google.com/sdk/gcloud/reference/beta/tasks/create-http-task)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/tasks/queues/add-iam-policy-binding/
title: gcloud beta tasks queues add-iam-policy-binding \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:40.558268+00:00
---

# gcloud beta tasks queues add-iam-policy-binding  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/tasks/queues/add-iam-policy-binding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta tasks queues add-iam-policy-binding Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta tasks queues add-iam-policy-binding - add IAM policy binding for a tasks queue 
SYNOPSIS
    

`gcloud beta tasks queues add-iam-policy-binding` (`QUEUE` : `--location`=`LOCATION`) `--member`=`PRINCIPAL` `--role`=`ROLE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Add an IAM policy binding to a tasks queue's access policy. 
EXAMPLES
     To add an IAM policy binding for the role of 'roles/editor' for the user 'test-user@gmail.com' with queue 'my-queue' and location='my-location', run: 
    
    
    gcloud beta tasks queues add-iam-policy-binding my-queue --location='my-location' --member='user:test-user@gmail.com' --role='roles/editor'

See <https://cloud.google.com/iam/docs/managing-policies> for details of policy role and member types. 

POSITIONAL ARGUMENTS
    

Queue resource - The task queue for which to add IAM policy binding to. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `queue` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`QUEUE`
     ID of the queue or fully qualified identifier for the queue. 

To set the `queue` attribute: 

  * provide the argument `queue` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location name. 

To set the `location` attribute: 

  * provide the argument `queue` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--member`=`PRINCIPAL`
     The principal to add the binding for. Should be of the form `user|group|serviceAccount:email` or `domain:domain`. 

Examples: `user:test-user@gmail.com`, `group:admins@example.com`, `serviceAccount:test123@example.domain.com`, or `domain:example.domain.com`. 

Some resources also accept the following special values: 

  * `allUsers` \- Special identifier that represents anyone who is on the internet, with or without a Google account. 
  * `allAuthenticatedUsers` \- Special identifier that represents anyone who is authenticated with a Google account or a service account. 


`--role`=`ROLE`
     Role name to assign to the principal. The role name is the complete path of a predefined role, such as `roles/logging.viewer`, or the role ID for a custom role, such as `organizations/{ORGANIZATION_ID}/roles/logging.viewer`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudtasks/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/tasks/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud tasks queues add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/add-iam-policy-binding)
    
    
    [gcloud alpha tasks queues add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/tasks/queues/add-iam-policy-binding)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

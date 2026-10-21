---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/source-manager/hooks/create/
title: gcloud alpha source-manager hooks create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:27:50.390298+00:00
---

# gcloud alpha source-manager hooks create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/source-manager/hooks/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha source-manager hooks create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha source-manager hooks create - create a Secure Source Manager hook 
SYNOPSIS
    

`gcloud alpha source-manager hooks create` (`HOOK` : `--region`=`REGION` `--repository`=`REPOSITORY`) `--target-uri`=`TARGET_URI` [`--async`] [`--disabled`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--events`=[`EVENT`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Secure Source Manager hook. 
EXAMPLES
     To create a hook ``my-hook`` in repository ``my-repo`` in location ``us-central1`` targeting ``https://example.com/webhook``, run the following command: 
    
    
    gcloud alpha source-manager hooks create my-hook --repository=my-repo --region=us-central1 --target-uri=https://example.com/webhook --events=PUSH,PULL_REQUEST

POSITIONAL ARGUMENTS
    

Hook resource - The Secure Source Manager hook to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `hook` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`HOOK`
     ID of the hook or fully qualified identifier for the hook. 

To set the `hook` attribute: 

  * provide the argument `hook` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Secure Source Manager location. 

To set the `region` attribute: 

  * provide the argument `hook` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


`--repository`=`REPOSITORY`
     Secure Source Manager repository. 

To set the `repository` attribute: 

  * provide the argument `hook` on the command line with a fully specified name; 
  * provide the argument `--repository` on the command line. 


REQUIRED FLAGS
    

`--target-uri`=`TARGET_URI`
     The target URI to which the payloads will be delivered. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--disabled`
     Determines if the hook is disabled. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--events`=[`EVENT`,…]
     The events that trigger hook on. Can be PUSH, PULL_REQUEST, or PULL_REQUEST_COMMENT. `EVENT` must be one of: 

`PULL_REQUEST`
     Pull request events are triggered when a pull request is opened, closed, reopened, or edited. 
`PULL_REQUEST_COMMENT`
     Triggers when a general comment is added, edited, or deleted on a pull request. 
`PUSH`
     Push events are triggered when pushing to the repository. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

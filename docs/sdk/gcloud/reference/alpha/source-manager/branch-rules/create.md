---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/source-manager/branch-rules/create/
title: gcloud alpha source-manager branch-rules create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:27:51.106291+00:00
---

# gcloud alpha source-manager branch-rules create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/source-manager/branch-rules/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha source-manager branch-rules create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha source-manager branch-rules create - create a Secure Source Manager branch rule 
SYNOPSIS
    

`gcloud alpha source-manager branch-rules create` (`BRANCH_RULE` : `--region`=`REGION` `--repository`=`REPOSITORY`) `--include-pattern`=`INCLUDE_PATTERN` [`--allow-stale-reviews`] [`--async`] [`--disabled`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--minimum-approvals-count`=`MINIMUM_APPROVALS_COUNT`] [`--minimum-reviews-count`=`MINIMUM_REVIEWS_COUNT`] [`--require-code-owner-approval`] [`--require-comments-resolved`] [`--require-linear-history`] [`--require-pull-request`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Secure Source Manager branch rule. 
EXAMPLES
     To create a branch rule called ``my-rule`` in repository ``my-repo`` in location ``us-central1`` protecting the main branch with pull request requirement, run the following command: 
    
    
    gcloud alpha source-manager branch-rules create my-rule --repository=my-repo --region=us-central1 --include-pattern=main --require-pull-request

POSITIONAL ARGUMENTS
    

Branch rule resource - The Secure Source Manager branch rule to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `branch_rule` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BRANCH_RULE`
     ID of the branch_rule or fully qualified identifier for the branch_rule. 

To set the `branch_rule` attribute: 

  * provide the argument `branch_rule` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Secure Source Manager location. 

To set the `region` attribute: 

  * provide the argument `branch_rule` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


`--repository`=`REPOSITORY`
     Secure Source Manager repository. 

To set the `repository` attribute: 

  * provide the argument `branch_rule` on the command line with a fully specified name; 
  * provide the argument `--repository` on the command line. 


REQUIRED FLAGS
    

`--include-pattern`=`INCLUDE_PATTERN`
     The pattern of the branch that can match to this branch rule. 
OPTIONAL FLAGS
    

`--allow-stale-reviews`
     Allows stale reviews or approvals. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--disabled`
     Determines if the branch rule is disabled. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--minimum-approvals-count`=`MINIMUM_APPROVALS_COUNT`
     The minimum number of approvals required. 
`--minimum-reviews-count`=`MINIMUM_REVIEWS_COUNT`
     The minimum number of reviews required. 
`--require-code-owner-approval`
     Determines if code owners must approve. 
`--require-comments-resolved`
     Determines if comments must be resolved. 
`--require-linear-history`
     Requires linear history. 
`--require-pull-request`
     Determines if a pull request is required. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

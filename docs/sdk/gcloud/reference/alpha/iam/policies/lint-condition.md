---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/policies/lint-condition/
title: gcloud alpha iam policies lint-condition \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:57.919916+00:00
---

# gcloud alpha iam policies lint-condition  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/policies/lint-condition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha iam policies lint-condition Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha iam policies lint-condition - lint an IAM condition 
SYNOPSIS
    

`gcloud alpha iam policies lint-condition` (`--condition-from-file`=`CONDITION_FROM_FILE` | [`--expression`=`EXPRESSION` `--title`=`TITLE` : `--description`=`DESCRIPTION`]) [`--resource-name`=`RESOURCE_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Lint an IAM condition. The problems found by linter will not be fixed. Instead, it will show the problems. 
EXAMPLES
     To lint an IAM condition of resource `//cloudresourcemanager.googleapis.com/v1/projects/example-project`, and the condtion to lint is expression='true', title='title', description='description', run: 
    
    
    gcloud alpha iam policies lint-condition --resource-name='//cloudresourcemanager.googleapis.com/v1/projects/example-project' --expression='true' --title='title' --description='description'

To lint an IAM condition of resource `//cloudresourcemanager.googleapis.com/v1/projects/example-project`, and the condition is read from a local YAML file `condition.yaml`, run: 
    
    
    gcloud alpha iam policies lint-condition --resource-name='//cloudresourcemanager.googleapis.com/v1/projects/example-project' --condition-from-file='condition.yaml'

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--condition-from-file`=`CONDITION_FROM_FILE`
     The path to a JSON or YAML file containing the condition. See <https://cloud.google.com/iam/docs/conditions-overview> for schema of the condition. 
Or at least one of these can be specified: 

The condition to lint. It must have an `expression` property and a `title` property. The `description` property is optional. 
`--expression`=`EXPRESSION`
     The expression of the condition which evaluates to True or False. This uses a subset of Common Expression Language syntax. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--title`=`TITLE`
     A title for the expression, i.e. a short string describing its purpose. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--description`=`DESCRIPTION`
     A description of the expression. This is a longer text which describes the expression. 
OPTIONAL FLAGS
    

`--resource-name`=`RESOURCE_NAME`
     The full resource name of the policy containing the condition to lint. See <https://cloud.google.com/apis/design/resource_names> for details. 

To get a URI from most list commands in gcloud, pass the --uri flag. For example: 
    
    
    [gcloud compute instances list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list) --project prj --uri
    
    
    <https://www.googleapis.com/compute/v1/projects/prj/zones/us-east1-c/instances/i1>
    <https://www.googleapis.com/compute/v1/projects/prj/zones/us-east1-d/instances/i2>

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iam/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

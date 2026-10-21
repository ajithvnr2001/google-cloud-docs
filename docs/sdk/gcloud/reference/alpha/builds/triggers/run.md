---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/run/
title: gcloud alpha builds triggers run \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:59:48.746396+00:00
---

# gcloud alpha builds triggers run  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha builds triggers run Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha builds triggers run - run a build trigger 
SYNOPSIS
    

`gcloud alpha builds triggers run` (`TRIGGER` : `--region`=`REGION`) [`--substitutions`=[`KEY`=`VALUE`,…]] [`--branch`=`BRANCH` | `--sha`=`SHA` | `--tag`=`TAG`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Run a build trigger. 
EXAMPLES
     To run a build trigger, run: 
    
    
    gcloud alpha builds triggers run MY-TRIGGER --branch=master

POSITIONAL ARGUMENTS
    

Trigger resource - Build Trigger. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `TRIGGER` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TRIGGER`
     ID of the trigger or fully qualified identifier for the trigger. 

To set the `trigger` attribute: 

  * provide the argument `TRIGGER` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The Cloud location for the trigger. 

To set the `region` attribute: 

  * provide the argument `TRIGGER` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `builds/region`. 


FLAGS
    

`--substitutions`=[`KEY`=`VALUE`,…]
     Parameters to be substituted in the build specification. For example: 
    
    
    gcloud alpha builds triggers run … --substitutions _FAVORITE_COLOR=blue,_NUM_CANDIES=10

This will result in a build where every occurrence of `${_FAVORITE_COLOR}` in certain fields is replaced by "blue", and similarly for `${_NUM_CANDIES}` and "10". 

Substitutions can be applied to user-defined variables (starting with an underscore) and to the following built-in variables: REPO_NAME, BRANCH_NAME, TAG_NAME, REVISION_ID, COMMIT_SHA, SHORT_SHA. 

For more details, see: <https://cloud.google.com/build/docs/configuring-builds/substitute-variable-values>

At most one of these can be specified: 

`--branch`=`BRANCH`
     Branch to run. 
`--sha`=`SHA`
     SHA to run. 
`--tag`=`TAG`
     Tag to run. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud builds triggers run](https://docs.cloud.google.com/sdk/gcloud/reference/builds/triggers/run)
    
    
    [gcloud beta builds triggers run](https://docs.cloud.google.com/sdk/gcloud/reference/beta/builds/triggers/run)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

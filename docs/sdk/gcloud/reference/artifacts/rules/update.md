---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/rules/update/
title: gcloud artifacts rules update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:14.508646+00:00
---

# gcloud artifacts rules update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/rules/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts rules update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts rules update - update an Artifact Registry rule 
SYNOPSIS
    

`gcloud artifacts rules update` (`RULE` : `--location`=`LOCATION` `--repository`=`REPOSITORY`) [`--action`=`ACTION`] [`--condition`=`CONDITION`] [`--operation`=`OPERATION`] [`--package`=`PACKAGE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update an Artifact Registry rule. 

This command can fail for the following reasons: 

  * The rule does not exist. 
  * A rule with the same name already exists. 
  * The active account does not have permission to create repositories. 
  * A rule with given package already exists. 


EXAMPLES
     To create a rule with the name `my-rule` for package `my-pkg` with action deny under the current project, repository, run: 
    
    
    gcloud artifacts rules update my-rule --package=my-pkg --action=deny

POSITIONAL ARGUMENTS
    

Rule resource - The Artifact Registry rule to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `rule` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`RULE`
     ID of the rule or fully qualified identifier for the rule. 

To set the `rule` attribute: 

  * provide the argument `rule` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the rule. Overrides the default artifacts/location property value for this command invocation. To configure the default location, use the command: gcloud config set artifacts/location. To set the `location` attribute: 

  * provide the argument `rule` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `artifacts/location`. 


`--repository`=`REPOSITORY`
     The repository associated with the rule. Overrides the default artifacts/repository property value for this command invocation. To configure the default repository, use the command: gcloud config set artifacts/repository. To set the `repository` attribute: 

  * provide the argument `rule` on the command line with a fully specified name; 
  * provide the argument `--repository` on the command line; 
  * set the property `artifacts/repository`. 


FLAGS
    

`--action`=`ACTION`
     The action the rule would make, can only be DENY or ALLOW. `ACTION` must be one of: `allow`, `deny`. 
`--condition`=`CONDITION`
     The CEL expression for the rule. 
`--operation`=`OPERATION`
     The operation the rule applies to. `OPERATION` must be (only one value is supported): `download`. 
`--package`=`PACKAGE`
     The package the rule applies to. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `artifactregistry/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/artifacts/docs/>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/colab/runtime-templates/set-iam-policy/
title: gcloud beta colab runtime-templates set-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:32.528715+00:00
---

# gcloud beta colab runtime-templates set-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/colab/runtime-templates/set-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta colab runtime-templates set-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta colab runtime-templates set-iam-policy - set IAM policy for a Colab Enterprise runtime template as defined in a JSON or YAML file 
SYNOPSIS
    

`gcloud beta colab runtime-templates set-iam-policy` (`RUNTIME_TEMPLATE` : `--region`=`REGION`) `POLICY_FILE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Set the IAM policy for a Colab Enterprise runtime template as defined in a JSON or YAML file. 

See <https://cloud.google.com/iam/docs/managing-policies> for details of the policy file format and contents. 

EXAMPLES
     To set the IAM policy for a runtime template with id `my-runtime-template` in region `us-central1` to the policy defined in `policy.json`, run: 
    
    
    gcloud beta colab runtime-templates set-iam-policy my-runtime-template policy.json --region=us-central1

POSITIONAL ARGUMENTS
    

Runtime template resource - Unique name of the runtime template to set IAM policy for. This was optionally provided by setting --runtime-template-id in the create runtime-template command, or was system-generated if unspecified. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `runtime_template` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`RUNTIME_TEMPLATE`
     ID of the runtime template or fully qualified identifier for the runtime template. 

To set the `name` attribute: 

  * provide the argument `runtime_template` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Cloud region for the runtime template. 

To set the `region` attribute: 

  * provide the argument `runtime_template` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `colab/region`. 


`POLICY_FILE`
     Path to a local JSON or YAML formatted file containing a valid policy. 

The output of the `get-iam-policy` command is a valid file, as is any JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud colab runtime-templates set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/set-iam-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

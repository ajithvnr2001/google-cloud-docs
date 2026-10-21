---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/models/set-iam-policy/
title: gcloud beta ai-platform models set-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:25:44.226409+00:00
---

# gcloud beta ai-platform models set-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/models/set-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ai-platform models set-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ai-platform models set-iam-policy - set the IAM policy for a model 
SYNOPSIS
    

`gcloud beta ai-platform models set-iam-policy` `MODEL` `POLICY_FILE` [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Sets the IAM policy for the given model as defined in a JSON or YAML file. 

See <https://cloud.google.com/iam/docs/managing-policies> for details of the policy file format and contents. 

EXAMPLES
     The following command will read am IAM policy defined in a JSON file 'policy.json' and set it for the model `my_model`: 
    
    
    gcloud beta ai-platform models set-iam-policy my_model policy.json

POSITIONAL ARGUMENTS
    

Model resource - The AI Platform model to set IAM policy for. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `model` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MODEL`
     ID of the model or fully qualified identifier for the model. 

To set the `name` attribute: 

  * provide the argument `model` on the command line. 


`POLICY_FILE`
     Path to a local JSON or YAML formatted file containing a valid policy. 

The output of the `get-iam-policy` command is a valid file, as is any JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy). 

FLAGS
    

`--region`=`REGION`
     Google Cloud region of the regional endpoint to use for this command. For the global endpoint, the region needs to be specified as `global`. 

Learn more about regional endpoints and see a list of available regions: <https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints>

`REGION` must be one of: `global`, `asia-east1`, `asia-northeast1`, `asia-southeast1`, `australia-southeast1`, `europe-west1`, `europe-west2`, `europe-west3`, `europe-west4`, `northamerica-northeast1`, `us-central1`, `us-east1`, `us-east4`, `us-west1`. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud ai-platform models set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform/models/set-iam-policy)
    
    
    [gcloud alpha ai-platform models set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/models/set-iam-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

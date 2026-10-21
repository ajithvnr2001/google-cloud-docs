---
url: https://docs.cloud.google.com/sdk/gcloud/reference/scc/iac-validation-reports/create/
title: gcloud scc iac-validation-reports create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:01.259984+00:00
---

# gcloud scc iac-validation-reports create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/scc/iac-validation-reports/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud scc iac-validation-reports create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud scc iac-validation-reports create - create a Cloud Security Command Center IaC Validation Report 
SYNOPSIS
    

`gcloud scc iac-validation-reports create` `PARENT` `--tf-plan-file`=`PATH_TO_FILE` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Cloud Security Command Center (SCC) IaC Validation Report. First argument is the parent of the IaC defined in the plan file. It is followed by path of the terraform plan file in JSON format. 

LRO operation ID is returned as the response of the command. 

EXAMPLES
     Create an Iac Validation report on parent `organizations/123/locations/global`: 
    
    
    gcloud scc iac-validation-reports create organizations/123/locations/global --tf-plan-file=planFile.json

POSITIONAL ARGUMENTS
    

`PARENT`
     Name of the organization where IaC Validation Report is to be created. Format: organizations/<organizationID>/locations/<location>
REQUIRED FLAGS
    

`--tf-plan-file`=`PATH_TO_FILE`
     Path to a JSON file containing the IaC plan to be validated. Use a full or relative path to a local file containing the value of tf_plan_file. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `securityposture/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha scc iac-validation-reports create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/iac-validation-reports/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

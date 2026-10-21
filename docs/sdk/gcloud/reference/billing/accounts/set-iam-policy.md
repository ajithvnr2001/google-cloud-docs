---
url: https://docs.cloud.google.com/sdk/gcloud/reference/billing/accounts/set-iam-policy/
title: gcloud billing accounts set-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:37:39.827617+00:00
---

# gcloud billing accounts set-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/billing/accounts/set-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud billing accounts set-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud billing accounts set-iam-policy - set the IAM policy for a Cloud Billing account 
SYNOPSIS
    

`gcloud billing accounts set-iam-policy` `ACCOUNT` `POLICY_FILE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud billing accounts set-iam-policy` sets the IAM policy for a Cloud Billing account given an account ID and a JSON or YAML file that describes the IAM policy. 

Note: Setting the IAM policy for a Cloud Billing account replaces existing IAM bindings for that account. 

EXAMPLES
     The following command reads an IAM policy defined in the JSON file `policy.json` and sets it for a Billing account ID `123456-789876-543210`: 
    
    
    gcloud billing accounts set-iam-policy 123456-789876-543210 policy.json

See <https://cloud.google.com/iam/docs/managing-policies> for policy file format and content details. 

POSITIONAL ARGUMENTS
    

Account resource - The Cloud Billing account for which to display the IAM policy. This represents a Cloud resource. 

This must be specified. 

`ACCOUNT`
     ID of the account or fully qualified identifier for the account. 

To set the `account` attribute: 

  * provide the argument `account` on the command line. 


`POLICY_FILE`
     Path to a local JSON or YAML formatted file containing a valid policy. 

The output of the `get-iam-policy` command is a valid file, as is any JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudbilling/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/billing/docs/apis>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha billing accounts set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing/accounts/set-iam-policy)
    
    
    [gcloud beta billing accounts set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/billing/accounts/set-iam-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

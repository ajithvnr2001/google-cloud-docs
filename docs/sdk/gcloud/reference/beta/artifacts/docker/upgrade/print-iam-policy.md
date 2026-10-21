---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/upgrade/print-iam-policy/
title: gcloud beta artifacts docker upgrade print-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:29:02.297517+00:00
---

# gcloud beta artifacts docker upgrade print-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/upgrade/print-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta artifacts docker upgrade print-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta artifacts docker upgrade print-iam-policy - print an Artifact Registry IAM policy for Container Registry to Artifact Registry upgrade 
SYNOPSIS
    

`gcloud beta artifacts docker upgrade print-iam-policy` `DOMAIN` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Print an Artifact Registry IAM policy that is equivalent to the IAM policy applied to the storage bucket for the specified Container Registry hostname. Apply the returned policy to the Artifact Registry repository that will replace the specified host. If the project has an organization, this command analyzes IAM policies at the organization level. Otherwise, this command analyzes IAM policies at the project level. See required permissions at <https://cloud.google.com/policy-intelligence/docs/analyze-iam-policies#required-permissions>. 
EXAMPLES
     To print an equivalent Artifact Registry IAM policy for 'gcr.io/my-project': 
    
    
    gcloud beta artifacts docker upgrade print-iam-policy upgrade print-iam-policy gcr.io --project=my-project

POSITIONAL ARGUMENTS
    

`DOMAIN`
     A Container Registry domain. Valid values are: [gcr.io, asia.gcr.io, eu.gcr.io, us.gcr.io] 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

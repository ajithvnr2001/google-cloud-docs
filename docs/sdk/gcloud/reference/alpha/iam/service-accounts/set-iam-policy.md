---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/set-iam-policy/
title: gcloud alpha iam service-accounts set-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:03.069933+00:00
---

# gcloud alpha iam service-accounts set-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/service-accounts/set-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha iam service-accounts set-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha iam service-accounts set-iam-policy - set IAM policy for a service account 
SYNOPSIS
    

`gcloud alpha iam service-accounts set-iam-policy` `SERVICE_ACCOUNT` `POLICY_FILE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command replaces the existing IAM policy for a service account, given an IAM_ACCOUNT and a file encoded in JSON or YAML that contains the IAM policy. If the given policy file specifies an "etag" value, then the replacement will succeed only if the policy already in place matches that etag. (An etag obtained via $ [gcloud iam service-accounts get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/get-iam-policy) will prevent the replacement if the policy for the service account has been subsequently updated.) A policy file that does not contain an etag value will replace any existing policy for the service account. 

If the service account does not exist, this command returns a `PERMISSION_DENIED` error. 

When managing IAM roles, you can treat a service account either as a resource or as an identity. This command is to set the iam policy of a service account resource. There are other gcloud commands to manage IAM policies for other types of resources. For example, to manage IAM policies on a project, use the `$ [gcloud projects](https://docs.cloud.google.com/sdk/gcloud/reference/projects)` commands. 

EXAMPLES
     The following command will read an IAM policy from 'policy.json' and set it for a service account with 'my-iam-account@my-project.iam.gserviceaccount.com' as the identifier: 
    
    
    gcloud alpha iam service-accounts set-iam-policy my-iam-account@my-project.iam.gserviceaccount.com policy.json

See <https://cloud.google.com/iam/docs/managing-policies> for details of the policy file format and contents. 
POSITIONAL ARGUMENTS
    

`SERVICE_ACCOUNT`
     The service account whose policy to set. The account should be formatted either as a numeric service account ID or as an email, like this: 123456789876543212345 or my-iam-account@somedomain.com. 
`POLICY_FILE`
     Path to a local JSON or YAML formatted file containing a valid policy. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud iam service-accounts set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/set-iam-policy)
    
    
    [gcloud beta iam service-accounts set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/set-iam-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

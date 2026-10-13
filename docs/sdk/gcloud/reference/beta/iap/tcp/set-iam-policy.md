---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/tcp/set-iam-policy/
title: gcloud beta iap tcp set-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:37.559737+00:00
---

# gcloud beta iap tcp set-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/tcp/set-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta iap tcp set-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta iap tcp set-iam-policy - set the IAM policy for an IAP TCP IAM resource 
SYNOPSIS
    

`gcloud beta iap tcp set-iam-policy` `POLICY_FILE` [`--region`=`REGION` `--resource-type`=`RESOURCE_TYPE` `--instance`=`INSTANCE` | `--service`=`SERVICE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command replaces the existing IAM policy for an IAP TCP IAM resource, given a file encoded in JSON or YAML that contains the IAM policy. If the given policy file specifies an "etag" value, then the replacement will succeed only if the policy already in place matches that etag. (An etag obtained via $ [gcloud beta iap tcp get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/tcp/get-iam-policy) will prevent the replacement if the policy for the resource has been subsequently updated.) A policy file that does not contain an etag value will replace any existing policy for the resource. 
EXAMPLES
     To set the IAM policy for the TCP accesses to all the Cloud Run services within the active project, run: 
    
    
    gcloud beta iap tcp set-iam-policy POLICY_FILE --resource-type=cloud-run

To set the IAM policy for the TCP accesses to all the Cloud Run services in specific region, run: 
    
    
    gcloud beta iap tcp set-iam-policy POLICY_FILE --resource-type=cloud-run --region=REGION

To set the IAM policy for the TCP accesses to a specific Cloud Run service in specific region, run: 
    
    
    gcloud beta iap tcp set-iam-policy POLICY_FILE --resource-type=cloud-run --service=SERVICE_ID --region=REGION

POSITIONAL ARGUMENTS
    

`POLICY_FILE`
     JSON or YAML file containing the IAM policy. 
FLAGS
    

`--region`=`REGION`
     Region name. Required when `--service` or `--instance` is specified for `resource-type=cloud-run`. 
`--resource-type`=`RESOURCE_TYPE`
     Resource type of the IAP resource. `RESOURCE_TYPE` must be (only one value is supported): `cloud-run`. 
At most one of these can be specified: 

`--instance`=`INSTANCE`
     Instance ID. 
`--service`=`SERVICE`
     Service name. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha iap tcp set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/tcp/set-iam-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/ssl-policies/delete/
title: gcloud beta compute ssl-policies delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:52:36.734573+00:00
---

# gcloud beta compute ssl-policies delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/ssl-policies/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute ssl-policies delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute ssl-policies delete - delete Compute Engine SSL policies 
SYNOPSIS
    

`gcloud beta compute ssl-policies delete` `SSL_POLICY` [`SSL_POLICY` …] [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute ssl-policies delete` is used to delete one or more Compute Engine SSL policies. SSL policies can only be deleted when no other resources (e.g., Target HTTPS proxies, Target SSL proxies) refer to them. 

An SSL policy specifies the server-side support for SSL features. An SSL policy can be attached to a TargetHttpsProxy or a TargetSslProxy. This affects connections between clients and the load balancer. SSL policies do not affect the connection between the load balancers and the backends. SSL policies are used by Application Load Balancers and proxy Network Load Balancers. 

POSITIONAL ARGUMENTS
    

`SSL_POLICY` [`SSL_POLICY` …]
     Names of the SSL policies to delete. 
FLAGS
    

At most one of these can be specified: 

`--global`
     If set, the SSL policies are global. 
`--region`=`REGION`
     Region of the SSL policies to delete. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute ssl-policies delete](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/delete)
    
    
    [gcloud alpha compute ssl-policies delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/ssl-policies/delete)
    
    
    [gcloud preview compute ssl-policies delete](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/ssl-policies/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

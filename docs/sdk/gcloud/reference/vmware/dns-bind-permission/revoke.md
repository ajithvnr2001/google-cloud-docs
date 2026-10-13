---
url: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/dns-bind-permission/revoke/
title: gcloud vmware dns-bind-permission revoke \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:09.244316+00:00
---

# gcloud vmware dns-bind-permission revoke  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/dns-bind-permission/revoke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud vmware dns-bind-permission revoke Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud vmware dns-bind-permission revoke - revokes a DNS Bind Permission 
SYNOPSIS
    

`gcloud vmware dns-bind-permission revoke` (`--service-account`=`SERVICE_ACCOUNT` | `--user`=`USER`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Revokes the bind permission from the customer provided user/service account on the intranet VPC associated with the consumer project. 
EXAMPLES
     To revoke the bind permission to the customer provided user `user@abc.com` on the intranet VPC associated with the consumer project `my-project`, run: 
    
    
    gcloud vmware dns-bind-permission revoke --user=user@abc.com --project=my-project

Or: 
    
    
    gcloud vmware dns-bind-permission revoke --user=user@abc.com

In the second example, the project is taken from gcloud properties core/project. 

To revoke the bind permission to the customer provided service account `service-account@gserviceaccount.com` on the intranet VPC associated with the consumer project `my-project`, run: 
    
    
    gcloud vmware dns-bind-permission revoke --service-account=service-account@gserviceaccount.com --project=my-project

Or: 
    
    
    gcloud vmware dns-bind-permission revoke --service-account=service-account@gserviceaccount.com

In the second example, the project is taken from gcloud properties core/project. 

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--service-account`=`SERVICE_ACCOUNT`
     The consumer provided service account whose permission needs to be revoked on the intranet VPC corresponding to the consumer project. If this field is not provided then the user should be provided. 
`--user`=`USER`
     The consumer provided user whose permission needs to be revoked on the intranet VPC corresponding to the consumer project. If this field is not provided then the service-account should be provided. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

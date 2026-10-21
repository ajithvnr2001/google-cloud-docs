---
url: https://docs.cloud.google.com/sdk/gcloud/reference/billing/budgets/describe/
title: gcloud billing budgets describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:57:15.400289+00:00
---

# gcloud billing budgets describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/billing/budgets/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud billing budgets describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud billing budgets describe - describe a budget 
SYNOPSIS
    

`gcloud billing budgets describe` (`BUDGET` : `--billing-account`=`BILLING_ACCOUNT`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe a budget. 
EXAMPLES
     To describe the budget 'abc' in account '123', run: 
    
    
    gcloud billing budgets describe "billingAccounts/123/budgets/abc"

Alternatively, you can run: 
    
    
    gcloud billing budgets describe abc --billing-account=123

POSITIONAL ARGUMENTS
    

Budget resource - Billing budget to describe. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`BUDGET`
     ID of the budget or fully qualified identifier for the budget. 

To set the `budget` attribute: 

  * provide the argument `budget` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--billing-account`=`BILLING_ACCOUNT`
     The billing account. To set the `billing-account` attribute: 

  * provide the argument `budget` on the command line with a fully specified name; 
  * provide the argument `--billing-account` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `billingbudgets/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/billing/docs/how-to/budget-api-overview>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha billing budgets describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing/budgets/describe)
    
    
    [gcloud beta billing budgets describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/billing/budgets/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects/link/
title: gcloud billing projects link \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:37:40.195493+00:00
---

# gcloud billing projects link  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects/link/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud billing projects link Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud billing projects link - link a project with a billing account 
SYNOPSIS
    

`gcloud billing projects link` `PROJECT_ID` `--billing-account`=`ACCOUNT_ID` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command sets or updates the billing account associated with a project. 

Billing is enabled on a project when the project is linked to a valid, active Cloud Billing account. The billing account accrues charges for the usage of resources in all of the linked projects. If the project is already linked to a billing account, this command moves the project to the billing account you specify, updating the billing account that is linked to the project. 

Note that associating a project with a closed billing account has the same effect as disabling billing on the project: any paid resources in use by the project are shut down, and your application stops functioning. Unless you want to disable billing, you should always specify a valid, active Cloud Billing account when you run this command. Learn how to confirm the status of a Cloud Billing account at <https://cloud.google.com/billing/docs/how-to/verify-billing-enabled#billing_account_status>

EXAMPLES
     To link a billing account `0X0X0X-0X0X0X-0X0X0X` with a project `my-project`, run: 
    
    
    gcloud billing projects link my-project --billing-account=0X0X0X-0X0X0X-0X0X0X

POSITIONAL ARGUMENTS
    

`PROJECT_ID`
     Specify a project id. 
REQUIRED FLAGS
    

`--billing-account`=`ACCOUNT_ID`
     Specify a billing account ID. Billing account IDs are of the form `0X0X0X-0X0X0X-0X0X0X`. To see available IDs, run `$ [gcloud billing accounts list](https://docs.cloud.google.com/sdk/gcloud/reference/billing/accounts/list)`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudbilling/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/billing/v1/getting-started>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha billing projects link](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/link)
    
    
    [gcloud beta billing projects link](https://docs.cloud.google.com/sdk/gcloud/reference/beta/billing/projects/link)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

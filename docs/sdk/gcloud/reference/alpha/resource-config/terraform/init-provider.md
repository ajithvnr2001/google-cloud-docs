---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-config/terraform/init-provider/
title: gcloud alpha resource-config terraform init-provider \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:07:45.532841+00:00
---

# gcloud alpha resource-config terraform init-provider  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-config/terraform/init-provider/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha resource-config terraform init-provider Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha resource-config terraform init-provider - generate main.tf file to configure Google Cloud Terraform Provider 
SYNOPSIS
    

`gcloud alpha resource-config terraform init-provider` [`--region`=`REGION`] [`--zone`=`ZONE`] [`--use-gcloud-billing-project` | [`--tf-user-project-override` : `--tf-billing-project`=`TF_BILLING_PROJECT`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Generate main.tf file to configure Google Cloud Terraform Provider. 
    
    
    This command supports Google Terraform Provider version v3.90.0+ and Terraform Provider Schema 0.2

EXAMPLES
     To generate a `main.tf` file in the current directory using the gcloud default values for `zone`, `region` and `project` run: 
    
    
    gcloud alpha resource-config terraform init-provider

To generate a `main.tf` file in the current directory using the user suppplied values for `zone`, `region` and `project` run: 
    
    
    gcloud alpha resource-config terraform init-provider --project="my-project-id" --region="us-central1" --zone="us-central1-c

To generate a `main.tf` file in the current directory using the gcloud default `billing_project` run: 
    
    
    gcloud alpha resource-config terraform init-provider --use-gcloud-billing-project

To generate a `main.tf` file in the current directory using user specified `billing_project` value run: 
    
    
    gcloud alpha resource-config terraform init-provider --tf-user-project-override --tf-billing-project="my-other-project-id"

FLAGS
    

`--region`=`REGION`
     Default Google Cloud Region for Regional Resources. If not specified the current `compute/region` property will be used. 
`--zone`=`ZONE`
     Default Google Cloud Zone for Zonal Resources. If not specified the current `compute/zone` property will be used. 
The below flags specify how the optional `user_project_override` and `billing_project` settings are configured for the Google Terraform Provider. See the [Google Terraform Provider Config Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference#user_project_override) for more details. 

At most one of these can be specified: 

`--use-gcloud-billing-project`
     If specified, will set `user_project_override` value in the Terrafom provider config to `true` and set `billing_project` to the current gcloud `billing/quota_project` property. 
Or at least one of these can be specified: 

Account Override Flags. 
`--tf-user-project-override`
     If specified, sets the `user_project_override` value in the Terraform provider config to `true`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--tf-billing-project`=`TF_BILLING_PROJECT`
     If specified, sets the `billing_project` value in the Terraform provider config. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/workforce-pools/create-login-config/
title: gcloud beta iam workforce-pools create-login-config \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:50.123333+00:00
---

# gcloud beta iam workforce-pools create-login-config  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/workforce-pools/create-login-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta iam workforce-pools create-login-config Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta iam workforce-pools create-login-config - create a login configuration file to enable sign-in via a web-based authorization flow using Workforce Identity Federation 
SYNOPSIS
    

`gcloud beta iam workforce-pools create-login-config` `AUDIENCE` `--output-file`=`OUTPUT_FILE` [`--activate`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command creates a configuration file to enable browser based third-party sign in with Workforce Identity Federation through `gcloud auth login --login-config=/path/to/config.json`. 
EXAMPLES
     To create a login configuration by using the short-format audience, run: 
    
    
    gcloud beta iam workforce-pools create-login-config $WORKFORCE_POOL_ID/$PROVIDER_ID --output-file=login-config.json

To create a login configuration by using the full resource name audience, run: 
    
    
    gcloud beta iam workforce-pools create-login-config locations/global/workforcePools/$WORKFORCE_POOL_ID/providers/$PROVIDER_ID --output-file=login-config.json

POSITIONAL ARGUMENTS
    

`AUDIENCE`
     The workforce pool provider resource name in the format "<pool>/<provider>" or "locations/<location>/workforcePools/<pool>/providers/<provider>". 
REQUIRED FLAGS
    

`--output-file`=`OUTPUT_FILE`
     Location to store the generated login configuration file. 
OPTIONAL FLAGS
    

`--activate`
     Sets the property `auth/login_config_file` to the created login configuration file. Calling `[gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login)` will automatically use this login configuration unless it is explicitly unset. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud iam workforce-pools create-login-config](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-login-config)
    
    
    [gcloud alpha iam workforce-pools create-login-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/workforce-pools/create-login-config)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 

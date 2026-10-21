---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/project-feature-settings/update/
title: gcloud compute os-config project-feature-settings update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:01:24.257635+00:00
---

# gcloud compute os-config project-feature-settings update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/project-feature-settings/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute os-config project-feature-settings update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute os-config project-feature-settings update - update VM Manager project feature settings 
SYNOPSIS
    

`gcloud compute os-config project-feature-settings update` `--patch-and-config-feature-set`=`PATCH_AND_CONFIG_FEATURE_SET` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update VM Manager project feature settings. 
EXAMPLES
     To update project feature settings for project `my-project`: 
    
    
    gcloud compute os-config project-feature-settings update --project=my-project --patch-and-config-feature-set=full

REQUIRED FLAGS
    

`--patch-and-config-feature-set`=`PATCH_AND_CONFIG_FEATURE_SET`
     Specifies the feature set for VM Manager. `PATCH_AND_CONFIG_FEATURE_SET` must be one of: 

`full`
     Full set of VM Manager functionality (alias for osconfig-c). 
`limited`
     Limited feature set. Enables only the basic set of features (alias for osconfig-b). 
`osconfig-b`
     Limited feature set. Enables only the basic set of features. 
`osconfig-c`
     Full set of VM Manager functionality. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `osconfig/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/compute/docs/osconfig/rest>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/oauth-clients/delete/
title: gcloud beta iap oauth-clients delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:40:55.359682+00:00
---

# gcloud beta iap oauth-clients delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/oauth-clients/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta iap oauth-clients delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta iap oauth-clients delete - delete a Cloud IAP OAuth client 
SYNOPSIS
    

`gcloud beta iap oauth-clients delete` (`NAME` : `--brand`=`BRAND`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `(DEPRECATED)` This command is deprecated and will be non-functional after the IAP OAuth Admin APIs are turned down. Jan 19, 2026: Google will discontinue support for the IAP OAuth Admin APIs. New projects will not be able to use these APIs. March 19, 2026: The IAP OAuth Admin APIs will be permanently shut down. Access to this feature will no longer be available. 

`gcloud beta iap oauth-clients delete` is used to delete a Cloud IAP OAuth client. Note this command cannot be used to delete any other type of OAuth client in your project. 

EXAMPLES
     To delete a Cloud IAP OAuth client named CLIENT for the current project and brand BRAND, run: 
    
    
    gcloud beta iap oauth-clients delete CLIENT --brand=BRAND

To delete a Cloud IAP OAuth client named CLIENT for a specific project PROJECT_ID and brand BRAND, run: 
    
    
    gcloud beta iap oauth-clients delete CLIENT --brand=BRAND --project=PROJECT_ID

POSITIONAL ARGUMENTS
    

Proxy client resource - Name of the Cloud IAP OAuth client to delete. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `name` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`NAME`
     ID of the proxy client or fully qualified identifier for the proxy client. 

To set the `identity_aware_proxy_clients` attribute: 

  * provide the argument `name` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--brand`=`BRAND`
     The name of the OAuth brand. 

To set the `brand` attribute: 

  * provide the argument `name` on the command line with a fully specified name; 
  * provide the argument `--brand` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iap/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/iap>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud iap oauth-clients delete](https://docs.cloud.google.com/sdk/gcloud/reference/iap/oauth-clients/delete)
    
    
    [gcloud alpha iap oauth-clients delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/oauth-clients/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

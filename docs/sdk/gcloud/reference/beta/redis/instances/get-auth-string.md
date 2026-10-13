---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/redis/instances/get-auth-string/
title: gcloud beta redis instances get-auth-string \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:13.596241+00:00
---

# gcloud beta redis instances get-auth-string  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/redis/instances/get-auth-string/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta redis instances get-auth-string Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta redis instances get-auth-string - show AUTH string for a Memorystore Redis instance 
SYNOPSIS
    

`gcloud beta redis instances get-auth-string` (`INSTANCE` : `--region`=`REGION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Show AUTH string for a Memorystore Redis instance. 

Result is empty if AUTH is disabled for the instance. 

This command can fail for the following reasons: 

  * The instance specified does not exist. 
  * The active account does not have permission to view the AUTH string 


EXAMPLES
     To display the AUTH string for an instance with the name `my-redis-instance` in the default region, run: 
    
    
    gcloud beta redis instances get-auth-string my-redis-instance

POSITIONAL ARGUMENTS
    

Instance resource - Arguments and flags that specify the Memorystore Redis instance you want to view the AUTH string for. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSTANCE`
     ID of the instance or fully qualified identifier for the instance. 

To set the `instance` attribute: 

  * provide the argument `instance` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The name of the Redis region of the instance. Overrides the default redis/region property value for this command invocation. To set the `region` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `redis/region`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `redis/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/memorystore/docs/redis/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud redis instances get-auth-string](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/get-auth-string)
    
    
    [gcloud alpha redis instances get-auth-string](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/redis/instances/get-auth-string)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

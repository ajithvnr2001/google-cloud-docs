---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/memcache/instances/upgrade/
title: gcloud alpha memcache instances upgrade \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:29:48.242710+00:00
---

# gcloud alpha memcache instances upgrade  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/memcache/instances/upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha memcache instances upgrade Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha memcache instances upgrade - upgrade memcache instance to a newer memcached version 
SYNOPSIS
    

`gcloud alpha memcache instances upgrade` (`INSTANCE` : `--region`=`REGION`) `--memcached-version`=`MEMCACHED_VERSION` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Upgrade memcahce instance to a newer memcached version. 
EXAMPLES
     To upgrade memcache version of an instance with the name 'my-memcache-instance' in region 'us-central-1' to MEMCACHE_1_6_15 
    
    
    gcloud alpha memcache instances upgrade my-memcache-instance --region=us-central1 --memcached-version="1.6.15"

POSITIONAL ARGUMENTS
    

Instance resource - Arguments and flags that specify the Memorystore for Memcached instance you want to upgrade. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
     The name of the Memcached region of the instance. Overrides the default memcache/region property value for this command invocation. To set the `region` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `memcache/region`. 


REQUIRED FLAGS
    

`--memcached-version`=`MEMCACHED_VERSION`
     Memcached engine version to which instance should be upgraded to. `MEMCACHED_VERSION` must be (only one value is supported): 

`1.6.15`
     Memcached engine version 1.6.15 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `memcache/v1beta2` API. The full documentation for this API can be found at: <https://cloud.google.com/memorystore/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud memcache instances upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/memcache/instances/upgrade)
    
    
    [gcloud beta memcache instances upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/beta/memcache/instances/upgrade)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

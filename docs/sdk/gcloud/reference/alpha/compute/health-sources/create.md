---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/health-sources/create/
title: gcloud alpha compute health-sources create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:45.035569+00:00
---

# gcloud alpha compute health-sources create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/health-sources/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute health-sources create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute health-sources create - create a health source 
SYNOPSIS
    

`gcloud alpha compute health-sources create` (`HEALTH_SOURCE` : `--region`=`REGION`) `--health-aggregation-policy`=`HEALTH_AGGREGATION_POLICY` `--sources`=`SOURCES`,[`SOURCES`,…] [`--async`] [`--description`=`DESCRIPTION`] [`--source-type`=`SOURCE_TYPE`; default="backend-service"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a health source. 
EXAMPLES
     The following command creates a new health source: 
    
    
    gcloud alpha compute health-sources create <HEALTH_SOURCE_NAME> --region=<REGION> --source-type=BACKEND_SERVICE --sources=my-backend-service --health-aggregation-policy=my-health-aggregation-policy

POSITIONAL ARGUMENTS
    

Health source resource - The name of the health source you want to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `health_source` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`HEALTH_SOURCE`
     ID of the health source or fully qualified identifier for the health source. 

To set the `health_source` attribute: 

  * provide the argument `health_source` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The name of the Google Compute Engine region. 

To set the `region` attribute: 

  * provide the argument `health_source` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `compute/region`. 


REQUIRED FLAGS
    

`--health-aggregation-policy`=`HEALTH_AGGREGATION_POLICY`
     URL to the health aggregation policy resource. Must be set. Must be regional and in the same region as the HealthSource. Can be mutated. 
`--sources`=`SOURCES`,[`SOURCES`,…]
     URLs to the source resources. Must be size 1. Must be a BackendService if the sourceType is BACKEND_SERVICE. The BackendService must have load balancing scheme INTERNAL or INTERNAL_MANAGED and must be regional and in the same region as the HealthSource (cross-region deployment for INTERNAL_MANAGED is not supported). The BackendService may use only IGs, MIGs, or NEGs of type GCE_VM_IP or GCE_VM_IP_PORT. The BackendService may not use haPolicy. Can be mutated. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     A textual description of the HealthSource. 
`--source-type`=`SOURCE_TYPE`; default="backend-service"
     Specifies the type of the HealthSource. The only allowed value is BACKEND_SERVICE. Must be specified when the HealthSource is created, and cannot be mutated. `SOURCE_TYPE` must be (only one value is supported): `backend-service`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `compute/alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/compute/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute health-sources create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-sources/create)
    
    
    [gcloud beta compute health-sources create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/health-sources/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-instances/
title: gcloud compute target-pools remove-instances \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:50:13.266312+00:00
---

# gcloud compute target-pools remove-instances  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute target-pools remove-instances Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute target-pools remove-instances - remove instances from a target pool 
SYNOPSIS
    

`gcloud compute target-pools remove-instances` `NAME` `--instances`=`INSTANCE`,[`INSTANCE`,…] [`--instances-zone`=`INSTANCES_ZONE`] [`--region`=`REGION`] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute target-pools remove-instances` is used to remove one or more instances from a target pool. For more information on health checks and load balancing, see <https://cloud.google.com/compute/docs/load-balancing-and-autoscaling/>
POSITIONAL ARGUMENTS
    

`NAME`
     The name of the target pool from which to remove the instances. 
REQUIRED FLAGS
    

`--instances`=`INSTANCE`,[`INSTANCE`,…]
     Specifies a list of instances to remove from the target pool. 
OPTIONAL FLAGS
    

`--instances-zone`=`INSTANCES_ZONE`
     Zone of the instances to remove from the target pool. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

`--region`=`REGION`
     Region of the target pool to operate on. If not specified, it will be set to the region of the instances. Overrides the default `compute/region` property value for this command invocation. 
`--zone`=`ZONE`
     Zone of the instances to remove from the target pool. DEPRECATED, use \--instances-zone. If not specified, you will be prompted to select a zone. Overrides the default `compute/zone` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute target-pools remove-instances](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-pools/remove-instances)
    
    
    [gcloud beta compute target-pools remove-instances](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/target-pools/remove-instances)
    
    
    [gcloud preview compute target-pools remove-instances](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-pools/remove-instances)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

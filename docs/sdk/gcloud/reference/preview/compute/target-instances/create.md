---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-instances/create/
title: gcloud preview compute target-instances create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:05:20.643071+00:00
---

# gcloud preview compute target-instances create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-instances/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute target-instances create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute target-instances create - create a target instance for handling traffic from a forwarding rule 
SYNOPSIS
    

`gcloud preview compute target-instances create` `NAME` `--instance`=`INSTANCE` [`--description`=`DESCRIPTION`] [`--instance-zone`=`INSTANCE_ZONE`] [`--network`=`NETWORK`] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute target-instances create` is used to create a target instance for handling traffic from one or more forwarding rules. Target instances are ideal for traffic that should be managed by a single source. For more information on target instances, see <https://cloud.google.com/compute/docs/protocol-forwarding/#targetinstances>
POSITIONAL ARGUMENTS
    

`NAME`
     Name of the target instance to operate on. 
REQUIRED FLAGS
    

`--instance`=`INSTANCE`
     The name of the virtual machine instance that will handle the traffic. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description of the target instance. 
`--instance-zone`=`INSTANCE_ZONE`
     Zone of the instance to operate on. If not specified, it will be set to the same as zone. Overrides the default `compute/zone` property value for this command invocation. 
`--network`=`NETWORK`
     Network that this target instance applies to. This is only necessary if the corresponding instance has multiple network interfaces. If not specified, the default network interface will be used. 
`--zone`=`ZONE`
     Zone of the target instance to operate on. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute target-instances create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-instances/create)
    
    
    [gcloud alpha compute target-instances create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-instances/create)
    
    
    [gcloud beta compute target-instances create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/target-instances/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

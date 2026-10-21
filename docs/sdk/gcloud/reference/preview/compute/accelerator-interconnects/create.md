---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/accelerator-interconnects/create/
title: gcloud preview compute accelerator-interconnects create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:34.917850+00:00
---

# gcloud preview compute accelerator-interconnects create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/accelerator-interconnects/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute accelerator-interconnects create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute accelerator-interconnects create - create a Compute Engine accelerator interconnect 
SYNOPSIS
    

`gcloud preview compute accelerator-interconnects create` `NAME` [`--accelerator-topology`=`ACCELERATOR_TOPOLOGY`] [`--async`] [`--description`=`DESCRIPTION`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--labels`=[`KEY`=`VALUE`,…]] [`--reactivation-mode`=`REACTIVATION_MODE`] [`--zone`=`ZONE`] [`--capacity-pool`=[`RESOURCE_URI`,…] | `--partition-ids`=[`PARTITION_ID`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute accelerator-interconnects create` creates a Compute Engine accelerator interconnect resource representing a dynamic accelerator slice. 
EXAMPLES
     To create an accelerator interconnect named `my-interconnect` in zone `us-central1-a` with a `2x2x4` topology: 
    
    
    gcloud preview compute accelerator-interconnects create my-interconnect --zone=us-central1-a --accelerator-topology=2x2x4 --partition-ids=partition-1

To create an accelerator interconnect using specific instance capacity: 
    
    
    gcloud preview compute accelerator-interconnects create my-interconnect --zone=us-central1-a --accelerator-topology=2x2x4 --capacity-pool=projects/my-proj/zones/us-central1-a/instances/vm-1,projects/my-proj/zones/us-central1-a/instances/vm-2

POSITIONAL ARGUMENTS
    

`NAME`
     The name of the accelerator interconnect to create. 
FLAGS
    

`--accelerator-topology`=`ACCELERATOR_TOPOLOGY`
     Target accelerator topology shape (e.g., "2x2x4", "4x4x8", "4x4x16"). 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     An optional textual description of the accelerator interconnect. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--reactivation-mode`=`REACTIVATION_MODE`
     Reactivation mode for the accelerator interconnect. `REACTIVATION_MODE` must be (only one value is supported): 

`manual`
     The accelerator interconnect must be manually reactivated or recreated upon capacity repair. 
`--zone`=`ZONE`
     Zone of the accelerator interconnect to create. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

At most one of these can be specified: 

`--capacity-pool`=[`RESOURCE_URI`,…]
     List of fully-qualified or relative URIs of resources (instances, MIGs, reservation subblocks) forming the capacity pool. 
`--partition-ids`=[`PARTITION_ID`,…]
     List of physical topology block identifiers (e.g. partition IDs) to form the capacity pool. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

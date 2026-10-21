---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/wire-groups/create/
title: gcloud preview compute interconnects wire-groups create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:53:59.460669+00:00
---

# gcloud preview compute interconnects wire-groups create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/wire-groups/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute interconnects wire-groups create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute interconnects wire-groups create - create a Compute Engine wire group 
SYNOPSIS
    

`gcloud preview compute interconnects wire-groups create` `NAME` `--bandwidth-allocation`=`BANDWIDTH_ALLOCATION` `--bandwidth-unmetered`=`BANDWIDTH_UNMETERED` `--cross-site-network`=`CROSS_SITE_NETWORK` [`--admin-enabled`] [`--description`=`DESCRIPTION`] [`--fault-response`=`FAULT_RESPONSE`] [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute interconnects wire-groups create` is used to create wire groups. A wire group represents a group of redundant wires between interconnects in two different metros. Each WireGroup belongs to a CrossSiteNetwork. 

For an example, refer to the `EXAMPLES` section below. 

EXAMPLES
     To create a wire group, run: 
    
    
    gcloud preview compute interconnects wire-groups create example-wg --cross-site-network=example-csn --bandwidth-unmetered=1

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the wire group to create. 
REQUIRED FLAGS
    

`--bandwidth-allocation`=`BANDWIDTH_ALLOCATION`
     The bandwidth allocation for the wire group. `BANDWIDTH_ALLOCATION` must be one of: 

`ALLOCATE_PER_WIRE`
     Configures a separate unmetered bandwidth allocation (and associated charges) for each wire in the group. 
`SHARED_WITH_WIRE_GROUP`
     Configures one unmetered bandwidth allocation for the wire group. The unmetered bandwidth is divided equally across each wire in the group, but dynamic throttling reallocates unused unmetered bandwidth from unused or underused wires to other wires in the group. 
`--bandwidth-unmetered`=`BANDWIDTH_UNMETERED`
     The amount of unmetered bandwidth to assign to the wire group. 
`--cross-site-network`=`CROSS_SITE_NETWORK`
     Name of the crossSiteNetwork to operate on. 
OPTIONAL FLAGS
    

`--admin-enabled`
     Administrative status of the wire group. If not provided on creation, defaults to enabled. When this is enabled, the wire group is operational and will carry traffic. Use --no-admin-enabled to disable it. 
`--description`=`DESCRIPTION`
     An optional, textual description for the wire group. 
`--fault-response`=`FAULT_RESPONSE`
     The fault response for the wire group. `FAULT_RESPONSE` must be one of: 

`DISABLE_PORT`
     Disable port 
`NONE`
     None 
`--validate-only`
     Validate the new configuration, but don't update it. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute interconnects wire-groups create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/create)
    
    
    [gcloud alpha compute interconnects wire-groups create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/wire-groups/create)
    
    
    [gcloud beta compute interconnects wire-groups create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/wire-groups/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

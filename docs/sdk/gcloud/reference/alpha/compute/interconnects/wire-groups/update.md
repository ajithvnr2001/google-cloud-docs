---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/wire-groups/update/
title: gcloud alpha compute interconnects wire-groups update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:52:40.513447+00:00
---

# gcloud alpha compute interconnects wire-groups update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/wire-groups/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute interconnects wire-groups update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute interconnects wire-groups update - update a Compute Engine wire group 
SYNOPSIS
    

`gcloud alpha compute interconnects wire-groups update` `NAME` `--cross-site-network`=`CROSS_SITE_NETWORK` [`--admin-enabled`] [`--bandwidth-allocation`=`BANDWIDTH_ALLOCATION`] [`--bandwidth-metered`=`BANDWIDTH_METERED`] [`--bandwidth-unmetered`=`BANDWIDTH_UNMETERED`] [`--description`=`DESCRIPTION`] [`--fault-response`=`FAULT_RESPONSE`] [`--flow-management`=`FLOW_MANAGEMENT`] [`--network-service-class`=`NETWORK_SERVICE_CLASS`] [`--type`=`TYPE`] [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute interconnects wire-groups update` is used to update wire groups. 

For an example, refer to the `EXAMPLES` section below. 

EXAMPLES
     To disable a wire group, run: 
    
    
    gcloud alpha compute interconnects wire-groups update example-wg --cross-site-network=example-csn --no-admin-enabled

To change a wire group's unmetered bandwidth, run: 
    
    
    gcloud alpha compute interconnects wire-groups update example-wg --cross-site-network=example-csn --bandwidth-unmetered=5

To enable automatic failure detection for a wire group, run: 
    
    
    gcloud alpha compute interconnects wire-groups update example-wg --cross-site-network=example-csn --fault-response=DISABLE_PORT

To enable bandwidth sharing for a wire group, run: 
    
    
    gcloud alpha compute interconnects wire-groups update example-wg --cross-site-network=example-csn --bandwidth-allocation=SHARED_WITH_WIRE_GROUP

To update a wire group's description, run: 
    
    
    gcloud alpha compute interconnects wire-groups update example-wg --cross-site-network=example-csn --description="new description"

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the wire group to update. 
REQUIRED FLAGS
    

`--cross-site-network`=`CROSS_SITE_NETWORK`
     Name of the crossSiteNetwork to operate on. 
OPTIONAL FLAGS
    

`--admin-enabled`
     Administrative status of the wire group. When this is enabled, the wire group is operational and will carry traffic. Use --no-admin-enabled to disable it. 
`--bandwidth-allocation`=`BANDWIDTH_ALLOCATION`
     The bandwidth allocation for the wire group. `BANDWIDTH_ALLOCATION` must be one of: 

`ALLOCATE_PER_WIRE`
     Configures a separate unmetered bandwidth allocation (and associated charges) for each wire in the group. 
`SHARED_WITH_WIRE_GROUP`
     Configures one unmetered bandwidth allocation for the wire group. The unmetered bandwidth is divided equally across each wire in the group, but dynamic throttling reallocates unused unmetered bandwidth from unused or underused wires to other wires in the group. 
`--bandwidth-metered`=`BANDWIDTH_METERED`
     The amount of metered bandwidth to assign to the wire group. 
`--bandwidth-unmetered`=`BANDWIDTH_UNMETERED`
     The amount of unmetered bandwidth to assign to the wire group. 
`--description`=`DESCRIPTION`
     An optional, textual description for the wire group. 
`--fault-response`=`FAULT_RESPONSE`
     The fault response for the wire group. `FAULT_RESPONSE` must be one of: 

`DISABLE_PORT`
     Disable port 
`NONE`
     None 
`--flow-management`=`FLOW_MANAGEMENT`
     The flow management configuration for the wire group. `FLOW_MANAGEMENT` must be one of: 

`DYNAMIC_PATH`
     The wire uses dynamic paths. 
`FIXED_PATH`
     The wire uses fixed paths. 
`--network-service-class`=`NETWORK_SERVICE_CLASS`
     The network service class for the wire group. `NETWORK_SERVICE_CLASS` must be one of: 

`BRONZE`
     The lowest service class. 
`GOLD`
     The highest service class. 
`--type`=`TYPE`
     The type for the wire group. `TYPE` must be one of: 

`BOX_AND_CROSS`
     Box and cross type wire groups must have two VLAN tags. The first is for the same-zone pseudowire, and the second is for the cross-zone pseudowire. 
`REDUNDANT`
     Redundant type wire groups must have only one VLAN tag. 
`WIRE`
     Single wire type wire groups must have only one VLAN tag. 
`--validate-only`
     Validate the new configuration, but don't update it. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute interconnects wire-groups update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/update)
    
    
    [gcloud beta compute interconnects wire-groups update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/wire-groups/update)
    
    
    [gcloud preview compute interconnects wire-groups update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/wire-groups/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 

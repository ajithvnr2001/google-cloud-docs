---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/groups/create-members/
title: gcloud beta compute interconnects groups create-members \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:22:43.188737+00:00
---

# gcloud beta compute interconnects groups create-members  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/groups/create-members/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute interconnects groups create-members Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute interconnects groups create-members - create new member interconnects in a Compute Engine interconnect group 
SYNOPSIS
    

`gcloud beta compute interconnects groups create-members` `NAME` `--interconnect`=[`INTERCONNECT`,…] [`--admin-enabled`] [`--customer-name`=`CUSTOMER_NAME`] [`--description`=`DESCRIPTION`] [`--facility`=`FACILITY`] [`--intent-mismatch-behavior`=`INTENT_MISMATCH_BEHAVIOR`] [`--interconnect-type`=`INTERCONNECT_TYPE`] [`--link-type`=`LINK_TYPE`] [`--noc-contact-email`=`NOC_CONTACT_EMAIL`] [`--remote-location`=`REMOTE_LOCATION`] [`--requested-features`=[`FEATURES`,…]] [`--requested-link-count`=`REQUESTED_LINK_COUNT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute interconnects groups create-members` is used to create new member interconnects in an interconnect group. 

For an example, refer to the `EXAMPLES` section below. 

EXAMPLES
     To create interconnects interconnect1 and interconnect2 in interconnect group example-interconnect-group, run: 
    
    
    gcloud beta compute interconnects groups create-members example-interconnect-group --interconnect-type=DEDICATED --link-type=LINK_TYPE_ETHERNET_10G_LR --requested-link-count=1 --facility=iad-1 --interconnect="name=interconnect1" --interconnect="name=interconnect2,facility=iad-5467"

Note that facility is required for each member interconnect. interconnect1's facility is set to the default value iad-1 and interconnect2's facility is overridden to iad-5467 in the `--interconnect` flag. 

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the interconnect group to create members. 
REQUIRED FLAGS
    

`--interconnect`=[`INTERCONNECT`,…]
     New member interconnects to create in the interconnect group. To create multiple interconnects, this flag should be specified multiple times. 

Each interconnect takes in the same set of flags as the `gcloud compute interconnects create` command, except instead of a location, a facility must be specified. These flags are defined as a comma separated list of flag=value pairs. 

Example: 
    
    
    --interconnect name=interconnect1,facility=iad-1,description="my interconnect",link-type=LINK_TYPE_ETHERNET_10G_LR,requested-link-count=1,interconnect-type=DEDICATED,admin-enabled,noc-contact-email=noc@google.com,customer-name=customer-name,requested-features=MACSEC:CROSS_SITE_NETWORK

Note that for multiple requested-features, use a colon (:) as the delimiter, as the comma is used to separate the flags. Similarly, if you need to use a comma in another flag value, you should set an alternative delimiter for the \--interconnect flag. Run `[gcloud topic escaping](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping)` for more information. 

OPTIONAL FLAGS
    

`--admin-enabled`
     Administrative status of the interconnect. If not provided on creation, defaults to enabled. When this is enabled, the interconnect is operational and will carry traffic across any functioning linked interconnect attachments. Use \--no-admin-enabled to disable it. 
`--customer-name`=`CUSTOMER_NAME`
     Customer name to put in the Letter of Authorization as the party authorized to request an interconnect. This field is required for most interconnects, however it is prohibited when creating a Cross-Cloud Interconnect. 
`--description`=`DESCRIPTION`
     An optional, textual description for the interconnect. 
`--facility`=`FACILITY`
     The facility (zone free location) to create the interconnect in. 
`--intent-mismatch-behavior`=`INTENT_MISMATCH_BEHAVIOR`
     The behavior when the intent of the interconnect group does not match the topology capability of the member interconnects. `INTENT_MISMATCH_BEHAVIOR` must be one of: `REJECT`, `CREATE`. 
`--interconnect-type`=`INTERCONNECT_TYPE`
     Type of the interconnect. `INTERCONNECT_TYPE` must be one of: 

`DEDICATED`
     Dedicated private interconnect. 
`PARTNER`
     Partner interconnect. Only available to approved partners. 
`--link-type`=`LINK_TYPE`
     Type of the link for the interconnect. `LINK_TYPE` must be one of: 

`LINK_TYPE_ETHERNET_100G_LR`
     100Gbps Ethernet, LR Optics. 
`LINK_TYPE_ETHERNET_10G_LR`
     10Gbps Ethernet, LR Optics. 
`LINK_TYPE_ETHERNET_400G_LR4`
     400Gbps Ethernet, LR4 Optics. 
`--noc-contact-email`=`NOC_CONTACT_EMAIL`
     Email address to contact the customer NOC for operations and maintenance notifications regarding this interconnect. 
`--remote-location`=`REMOTE_LOCATION`
     The location of the interconnect for Cross-Cloud Interconnect. 
`--requested-features`=[`FEATURES`,…]
     List of features requested for this interconnect. `FEATURES` must be one of: 

`CROSS_SITE_NETWORK`
     If specified then the interconnect is created on Cross-Site Network capable hardware ports. This parameter can only be provided during interconnect INSERT and cannot be changed using interconnect PATCH. 
`L2_FORWARDING`
     If specified then the interconnect is created on L2 forwarding capable hardware ports. This parameter can only be provided during interconnect INSERT and cannot be changed using interconnect PATCH. 
`MACSEC`
     If specified then the interconnect is created on MACsec capable hardware ports. If not specified, the interconnect is created on non-MACsec capable ports first, if available. This parameter can only be provided during interconnect INSERT and cannot be changed using interconnect PATCH. 
`--requested-link-count`=`REQUESTED_LINK_COUNT`
     Target number of physical links in the link bundle. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

DEFAULTABLE PER-INTERCONNECT FLAGS
     All flags except `--intent-mismatch-behavior` in the `OPTIONAL FLAGS` section are defaultable per-interconnect. This means that you can set a default value by using these flags, or you can override the value for each interconnect by using the `--interconnect` flag. 

Furthermore, if the default values for the following flags are not specified, then they must be specified per-interconnect in the `--interconnect` flag: 

  * `--facility`
  * `--interconnect-type`
  * `--link-type`
  * `--requested-link-count`


NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute interconnects groups create-members](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups/create-members)
    
    
    [gcloud alpha compute interconnects groups create-members](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members)
    
    
    [gcloud preview compute interconnects groups create-members](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/groups/create-members)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

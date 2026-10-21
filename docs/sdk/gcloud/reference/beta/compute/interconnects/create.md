---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/create/
title: gcloud beta compute interconnects create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:11:44.114792+00:00
---

# gcloud beta compute interconnects create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute interconnects create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute interconnects create - create a Compute Engine interconnect 
SYNOPSIS
    

`gcloud beta compute interconnects create` `NAME` `--interconnect-type`=`INTERCONNECT_TYPE` `--link-type`=`LINK_TYPE` `--location`=`LOCATION` `--requested-link-count`=`REQUESTED_LINK_COUNT` [`--admin-enabled`] [`--customer-name`=`CUSTOMER_NAME`] [`--description`=`DESCRIPTION`] [`--noc-contact-email`=`NOC_CONTACT_EMAIL`] [`--remote-location`=`REMOTE_LOCATION`] [`--requested-features`=[`FEATURES`,…]] [`--resource-manager-tags`=[`KEY`=`VALUE`,…]] [`--subzone`=`SUBZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute interconnects create` is used to create interconnects. An interconnect represents a single specific connection between Google and the customer. 

For an example, refer to the `EXAMPLES` section below. 

EXAMPLES
     To create an interconnect of type DEDICATED, run: 
    
    
    gcloud beta compute interconnects create example-interconnect --customer-name="Example Customer Name" --interconnect-type=DEDICATED --link-type=LINK_TYPE_ETHERNET_10G_LR --location=example-zone1-1 --requested-link-count=1 --noc-contact-email=noc@example.com --description="Example interconnect"

To create a Cross-Cloud Interconnect, run: 
    
    
    gcloud beta compute interconnects create example-cc-interconnect --interconnect-type=DEDICATED --link-type=LINK_TYPE_ETHERNET_10G_LR --location=example-zone1-1 --requested-link-count=1 --remote-location=example-remote-location --noc-contact-email=noc@example.com --description="Example Cross-Cloud Interconnect"

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the interconnect to create. 
REQUIRED FLAGS
    

`--interconnect-type`=`INTERCONNECT_TYPE`
     Type of the interconnect. `INTERCONNECT_TYPE` must be one of: 

`DEDICATED`
     Dedicated private interconnect. 
`IT_PRIVATE`
     Dedicated private interconnect. (Warning: IT_PRIVATE is deprecated, use DEDICATED instead.) 
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
`--location`=`LOCATION`
     The location for the interconnect. The locations can be listed by using the `[gcloud beta compute interconnects locations list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/locations/list)` command to find the appropriate location to use when creating an interconnect. 
`--requested-link-count`=`REQUESTED_LINK_COUNT`
     Target number of physical links in the link bundle. 
OPTIONAL FLAGS
    

`--admin-enabled`
     Administrative status of the interconnect. If not provided on creation, defaults to enabled. When this is enabled, the interconnect is operational and will carry traffic across any functioning linked interconnect attachments. Use \--no-admin-enabled to disable it. 
`--customer-name`=`CUSTOMER_NAME`
     Customer name to put in the Letter of Authorization as the party authorized to request an interconnect. This field is required for most interconnects, however it is prohibited when creating a Cross-Cloud Interconnect. 
`--description`=`DESCRIPTION`
     An optional, textual description for the interconnect. 
`--noc-contact-email`=`NOC_CONTACT_EMAIL`
     Email address to contact the customer NOC for operations and maintenance notifications regarding this interconnect. 
`--remote-location`=`REMOTE_LOCATION`
     The remote location for a Cross-Cloud Interconnect. The remote locations can be listed by using the `[gcloud beta compute interconnects remote-locations list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/remote-locations/list)` command to find the appropriate remote location to use when creating a Cross-Cloud Interconnect. 
`--requested-features`=[`FEATURES`,…]
     List of features requested for this interconnect. `FEATURES` must be one of: 

`CROSS_SITE_NETWORK`
     If specified then the interconnect is created on Cross-Site Network capable hardware ports. This parameter can only be provided during interconnect INSERT and cannot be changed using interconnect PATCH. 
`L2_FORWARDING`
     If specified then the interconnect is created on L2 forwarding capable hardware ports. This parameter can only be provided during interconnect INSERT and cannot be changed using interconnect PATCH. 
`MACSEC`
     If specified then the interconnect is created on MACsec capable hardware ports. If not specified, the interconnect is created on non-MACsec capable ports first, if available. This parameter can only be provided during interconnect INSERT and cannot be changed using interconnect PATCH. 
`--resource-manager-tags`=[`KEY`=`VALUE`,…]
     A comma-separated list of Resource Manager tags to apply to the interconnect. 
`--subzone`=`SUBZONE`
     (DEPRECATED) Subzone in the LOCATION specified by the --location flag. 

The --subzone flag is deprecated and will be removed in a future release. `SUBZONE` must be one of: 

`a`
     Subzone a. 
`b`
     Subzone b. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute interconnects create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/create)
    
    
    [gcloud alpha compute interconnects create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/create)
    
    
    [gcloud preview compute interconnects create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

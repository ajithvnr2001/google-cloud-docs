---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/spokes/linked-vpn-tunnels/create/
title: gcloud beta network-connectivity spokes linked-vpn-tunnels create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:48.099278+00:00
---

# gcloud beta network-connectivity spokes linked-vpn-tunnels create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/spokes/linked-vpn-tunnels/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-connectivity spokes linked-vpn-tunnels create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-connectivity spokes linked-vpn-tunnels create - create a new VPN spoke 
SYNOPSIS
    

`gcloud beta network-connectivity spokes linked-vpn-tunnels create` (`SPOKE` : `--region`=`REGION`) `--hub`=`HUB` `--vpn-tunnels`=[`VPN_TUNNELS`,…] [`--async`] [`--description`=`DESCRIPTION`] [`--exclude-export-ranges`=[`EXCLUDE_EXPORT_RANGES`,…]] [`--exclude-import-ranges`=[`EXCLUDE_IMPORT_RANGES`,…]] [`--group`=`GROUP`] [`--include-export-ranges`=[`INCLUDE_EXPORT_RANGES`,…]] [`--include-import-ranges`=[`INCLUDE_IMPORT_RANGES`,…]] [`--labels`=[`KEY`=`VALUE`,…]] [`--site-to-site-data-transfer`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new [VPN spoke](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpn-spoke). 
EXAMPLES
     To create a VPN spoke in region ``us-central1`` that uses data transfer and has two tunnels, run: 
    
    
    [gcloud beta network-connectivity spokes linked-vpn-tunnels](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/spokes/linked-vpn-tunnels) create my-spoke --hub="<https://www.googleapis.com/networkconnectivity/v1beta/pro\>
    jects/my-project/locations/global/hubs/my-hub" \
        --region=us-central1 \
        --vpn-tunnels=https://www.googleapis.com/compute/v1/projects/\
    my-project/regions/us-central1/vpnTunnels/vpn-tunnel1,[https://\](https://\\)
    www.googleapis.com/compute/v1/projects/my-project/regions/\
    us-central1/vpnTunnels/vpn-tunnel2 --site-to-site-data-transfer

POSITIONAL ARGUMENTS
    

Spoke resource - Name of the spoke to be created. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `spoke` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SPOKE`
     ID of the spoke or fully qualified identifier for the spoke. 

To set the `spoke` attribute: 

  * provide the argument `spoke` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The location Id. To set the `region` attribute: 

  * provide the argument `spoke` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


REQUIRED FLAGS
    

`--hub`=`HUB`
     Hub that the spoke will attach to. The hub must already exist. 
`--vpn-tunnels`=[`VPN_TUNNELS`,…]
     HA VPN tunnels that the spoke provides connectivity to. The resources must already exist. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Description of the spoke to create. 
`--exclude-export-ranges`=[`EXCLUDE_EXPORT_RANGES`,…]
     Dynamic routes overlapped/encompassed by exclude export ranges are excluded during export to hub. 
`--exclude-import-ranges`=[`EXCLUDE_IMPORT_RANGES`,…]
     Hub routes overlapped/encompassed by exclude import ranges are excluded during import from hub. 
`--group`=`GROUP`
     The group that the spoke will be added to. The group must already exist. If unset, the spoke will be added to the ``default`` group. 
`--include-export-ranges`=[`INCLUDE_EXPORT_RANGES`,…]
     Dynamic routes fully encompassed by include export ranges are included during export to hub. If it's empty, the spoke exports all dynamic routes to the hub. 
`--include-import-ranges`=[`INCLUDE_IMPORT_RANGES`,…]
     Hub routes fully encompassed by include import ranges are included during import from hub. If it's empty, the spoke does not import any subnets from the hub. If it's empty and site-to-site-data-transfer is true, the spoke imports all IPv4 site-to-site dynamic routes from the hub. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--site-to-site-data-transfer`
     Whether to enable site-to-site data transfer for this spoke. Data transfer is available only in [supported locations](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkconnectivity/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud network-connectivity spokes linked-vpn-tunnels create](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-vpn-tunnels/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

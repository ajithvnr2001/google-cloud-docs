---
url: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create/
title: gcloud vmware network-peerings create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:48.627115+00:00
---

# gcloud vmware network-peerings create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud vmware network-peerings create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud vmware network-peerings create - create a VMware Engine VPC network peering 
SYNOPSIS
    

`gcloud vmware network-peerings create` (`NETWORK_PEERING` : `--location`=`LOCATION`) `--peer-network`=`PEER_NETWORK` `--peer-network-type`=`PEER_NETWORK_TYPE` `--vmware-engine-network`=`VMWARE_ENGINE_NETWORK` [`--async`] [`--description`=`DESCRIPTION`] [`--no-exchange-subnet-routes`] [`--no-export-custom-routes`] [`--no-export-custom-routes-with-public-ip`] [`--no-import-custom-routes`] [`--no-import-custom-routes-with-public-ip`] [`--peer-mtu`=`PEER_MTU`] [`--peer-project`=`PEER_PROJECT`] [`--vmware-engine-network-project`=`VMWARE_ENGINE_NETWORK_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a VMware Engine VPC network peering. VPC network peering creation is considered finished when the network peering is in ACTIVE state. Check the progress of a VPC network peering using `[gcloud vmware network-peerings list](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/list)`. 
EXAMPLES
     To create a VPC network peering called `new-peering` that connects the VMware Engine network `my-vmware-engine-network` with another VMware Engine network `another-vmware-engine-network` from project `another-project`, run: 
    
    
    gcloud vmware network-peerings create new-peering --vmware-engine-network=my-vmware-engine-network --peer-network=another-vmware-engine-network --peer-network-type=VMWARE_ENGINE_NETWORK --peer-project=another-project

In this example, the project is taken from gcloud properties core/project and location is taken as `global`. 

POSITIONAL ARGUMENTS
    

VMware Engine VPC network peering resource - network_peering. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `network_peering` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`NETWORK_PEERING`
     ID of the VMware Engine VPC network peering or fully qualified identifier for the VMware Engine VPC network peering. 

To set the `network-peering` attribute: 

  * provide the argument `network_peering` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The resource name of the location. 

To set the `location` attribute: 

  * provide the argument `network_peering` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set location as 'global' (default). 


REQUIRED FLAGS
    

`--peer-network`=`PEER_NETWORK`
     ID of the network to peer with the VMware Engine network. The peer network can be a consumer VPC network or another VMware Engine network. 
`--peer-network-type`=`PEER_NETWORK_TYPE`
     Type of the VPC network to peer with the VMware Engine network. PEER_NETWORK_TYPE must be one of the following: 

  * STANDARD: Peering connection used for connecting to another VPC network established by the same user. For example, a peering connection to another VPC network in the same project or to an on-premises network. 
  * VMWARE_ENGINE_NETWORK: Peering connection used for connecting to another VMware Engine network. 
  * PRIVATE_SERVICES_ACCESS: Peering connection used for establishing private services access. 
  * NETAPP_CLOUD_VOLUMES: Peering connection used for connecting to NetApp Cloud Volumes. 
  * THIRD_PARTY_SERVICE: Peering connection used for connecting to third-party services. Most third-party services require manual setup of reverse peering on the VPC network associated with the third-party service. 
  * DELL_POWERSCALE: Peering connection used for connecting to Dell PowerScale Filers. 
  * GOOGLE_CLOUD_NETAPP_VOLUMES: Peering connection used for connecting to Google Cloud NetApp Volumes. `PEER_NETWORK_TYPE` must be one of: `PEER_NETWORK_TYPE_UNSPECIFIED`, `STANDARD`, `VMWARE_ENGINE_NETWORK`, `PRIVATE_SERVICES_ACCESS`, `NETAPP_CLOUD_VOLUMES`, `THIRD_PARTY_SERVICE`, `DELL_POWERSCALE`, `GOOGLE_CLOUD_NETAPP_VOLUMES`. 


`--vmware-engine-network`=`VMWARE_ENGINE_NETWORK`
     ID of the VMware Engine network to attach the new peering to. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--description`=`DESCRIPTION`
     User-provided description of the VPC network peering. 
`--exchange-subnet-routes`
     True if full-mesh connectivity is created and managed automatically between peered VPC networks; false otherwise. This field is always true because Google Compute Engine automatically creates and manages subnetwork routes between two VPC networks when the peering state is ACTIVE. Enabled by default, use `--no-exchange-subnet-routes` to disable. 
`--export-custom-routes`
     True if custom routes are exported to the peered VPC network; false otherwise. The default value is true. Enabled by default, use `--no-export-custom-routes` to disable. 
`--export-custom-routes-with-public-ip`
     True if all subnet routes with public IP address range are exported; false otherwise. The default value is true. Enabled by default, use `--no-export-custom-routes-with-public-ip` to disable. 
`--import-custom-routes`
     True if custom routes are imported to the peered VPC network; false otherwise. The default value is true. Enabled by default, use `--no-import-custom-routes` to disable. 
`--import-custom-routes-with-public-ip`
     True if all subnet routes with public IP address range are imported; false otherwise. The default value is true. Enabled by default, use `--no-import-custom-routes-with-public-ip` to disable. 
`--peer-mtu`=`PEER_MTU`
     Maximum transmission unit (MTU) in bytes. 
`--peer-project`=`PEER_PROJECT`
     Project ID or project number of the peer network. Use this flag when the peer network is in another project. 
`--vmware-engine-network-project`=`VMWARE_ENGINE_NETWORK_PROJECT`
     Project of the VMware Engine network to attach the new peering to. Use this flag when the VMware Engine network is in another project. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

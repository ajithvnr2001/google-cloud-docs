---
url: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-connections/create/
title: gcloud vmware private-connections create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:49.825414+00:00
---

# gcloud vmware private-connections create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-connections/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud vmware private-connections create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud vmware private-connections create - create a Google Cloud Private Connection 
SYNOPSIS
    

`gcloud vmware private-connections create` (`PRIVATE_CONNECTION` : `--location`=`LOCATION`) `--service-project`=`SERVICE_PROJECT` `--type`=`TYPE` `--vmware-engine-network`=`VMWARE_ENGINE_NETWORK` [`--async`] [`--description`=`DESCRIPTION`] [`--routing-mode`=`ROUTING_MODE`] [`--service-network`=`SERVICE_NETWORK`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Creates a new private connection to connect VMware Engine Network to the specified VPC network. This establishes private IP connectivity between the VPC network and all the VMware Private Clouds attached to the VMware Engine Network. Private connection creation is considered finished when the connection is in ACTIVE state. Check the progress of the private connection using `[gcloud vmware private-connections list](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-connections/list)`. 
EXAMPLES
     To create a Private Connection of type PRIVATE_SERVICE_ACCESS, first obtain the service-project by listing vpc-peerings, run: 
    
    
    [gcloud compute networks peerings list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/list) --network=my-vpc --project=my-project

where my-vpc is the VPC on which a private service access connection is created and project is the one in which the private connection will be created. 

The response will be of this format: 

NAME NETWORK PEER_PROJECT 

servicenetworking-googleapis-com my-vpc td096d594ece09650-tp 

The PEER_PROJECT field in the output of the command will provide the value for the service-project required for creating the private connection. 

To create a Private Connection called `my-private-connection` of type `PRIVATE_SERVICE_ACCESS` in project `my-project` and region `us-west1` with routing_mode `REGIONAL` to connect service networking VPC from project `td096d594ece09650-tp` to legacy VMware Engine Network `us-west1-default`, run: 
    
    
    gcloud vmware private-connections create my-private-connection --location=us-west1 --project=my-project --vmware-engine-network=us-west1-default --description="A short description for the new private connection" --routing-mode=REGIONAL --service-project=td096d594ece09650-tp --type=PRIVATE_SERVICE_ACCESS

Or: 
    
    
    gcloud vmware private-connections create my-private-connection --vmware-engine-network=us-west1-default --description="A short description for the new private connection" --routing-mode=REGIONAL --service-project=td096d594ece09650-tp --type=PRIVATE_SERVICE_ACCESS
    
    
    In the second example, the project and location are taken from gcloud properties core/project and compute/region, respectively.

To create a Private Connection called `my-private-connection` of type `THIRD_PARTY_SERVICE` in project `my-project` and region `us-west1` to connect VPC `my-service-network` from project `td096d594ece09650-tp` to legacy VMware Engine Network `us-west1-default`, run: 
    
    
    gcloud vmware private-connections create my-private-connection --location=us-west1 --project=my-project --vmware-engine-network=us-west1-default --description="A short description for the new private connection" --service-network=my-service-network --service-project=td096d594ece09650-tp --type=THIRD_PARTY_SERVICE

Or: 
    
    
    gcloud vmware private-connections create my-private-connection --vmware-engine-network=us-west1-default --description="A short description for the new private connection" --service-network=my-service-network --service-project=td096d594ece09650-tp --type=THIRD_PARTY_SERVICE
    
    
    In the above example, the project and location are taken from gcloud properties core/project and compute/region, respectively.

If you try to create a private connection of type=THIRD_PARTY_SERVICE, and do not provide the service-network field, an error will be thrown with the message: 

Missing required argument [--service-network]: For private connection of type THIRD_PARTY_SERVICE, service-network field is required 

POSITIONAL ARGUMENTS
    

Private Connection resource - private_connection. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `private_connection` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`PRIVATE_CONNECTION`
     ID of the Private Connection or fully qualified identifier for the Private Connection. 

To set the `private-connection` attribute: 

  * provide the argument `private_connection` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The resource name of the location. 

To set the `location` attribute: 

  * provide the argument `private_connection` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `compute/region`. 


REQUIRED FLAGS
    

`--service-project`=`SERVICE_PROJECT`
     Project ID or project number of the service network. 
`--type`=`TYPE`
     Type of private connection. `TYPE` must be one of: 

`DELL_POWERSCALE`
     Peering connection used for connecting to Dell PowerScale. 
`NETAPP_CLOUD_VOLUMES`
     Peering connection used for connecting to NetApp Cloud Volumes. 
`PRIVATE_SERVICE_ACCESS`
     Peering connection used for establishing [private services access](https://cloud.google.com/vpc/docs/private-services-access). 
`THIRD_PARTY_SERVICE`
     Peering connection used for connecting to third-party services. Most third-party services require manual setup of reverse peering on the VPC network associated with the third-party service. 
`--vmware-engine-network`=`VMWARE_ENGINE_NETWORK`
     Resource ID of the legacy VMware Engine network. Provide the {vmware_engine_network_id}, which will be in the form of {location}-default. The {location} is the same as the location specified in the private connection resource. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--description`=`DESCRIPTION`
     Text describing the private connection. 
`--routing-mode`=`ROUTING_MODE`
     Type of the routing mode. Default value is set to GLOBAL. For type=PRIVATE_SERVICE_ACCESS, this field can be set to GLOBAL or REGIONAL, for other types only GLOBAL is supported. `ROUTING_MODE` must be one of: `GLOBAL`, `REGIONAL`. 
`--service-network`=`SERVICE_NETWORK`
     Resource ID of the service network to connect with the VMware Engine network to create a private connection. 

  * For type=PRIVATE_SERVICE_ACCESS, this field represents service networking VPC. In this case the field value will be automatically set to `servicenetworking` and cannot be changed. 
  * For type=NETAPP_CLOUD_VOLUME, this field represents NetApp service VPC. In this case the field value will be automatically set to `netapp-tenant-vpc` and cannot be changed. 
  * For type=DELL_POWERSCALE, this field represents Dell service VPC. In this case the field value will be automatically set to `dell-tenant-vpc` and cannot be changed. 
  * For type=THIRD_PARTY_SERVICE, this field could represent a consumer VPC or any other producer VPC to which the VMware Engine Network needs to be connected. service-network field is required for this type. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

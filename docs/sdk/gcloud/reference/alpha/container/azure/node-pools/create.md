---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/azure/node-pools/create/
title: gcloud alpha container azure node-pools create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:23.072164+00:00
---

# gcloud alpha container azure node-pools create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/azure/node-pools/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container azure node-pools create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container azure node-pools create - create a node pool in an Anthos cluster on Azure 
SYNOPSIS
    

`gcloud alpha container azure node-pools create` (`NODE_POOL` : `--cluster`=`CLUSTER` `--location`=`LOCATION`) `--max-pods-per-node`=`MAX_PODS_PER_NODE` `--node-version`=`NODE_VERSION` `--ssh-public-key`=`SSH_PUBLIC_KEY` `--subnet-id`=`SUBNET_ID` (`--max-nodes`=`MAX_NODES` `--min-nodes`=`MIN_NODES`) [`--annotations`=`ANNOTATION`,[`ANNOTATION`,…]] [`--async`] [`--azure-availability-zone`=`AZURE_AVAILABILITY_ZONE`] [`--config-encryption-key-id`=`CONFIG_ENCRYPTION_KEY_ID`] [`--config-encryption-public-key`=`CONFIG_ENCRYPTION_PUBLIC_KEY`] [`--enable-autorepair`] [`--image-type`=`IMAGE_TYPE`] [`--node-labels`=`NODE_LABEL`,[`NODE_LABEL`,…]] [`--node-taints`=`NODE_TAINT`,[`NODE_TAINT`,…]] [`--root-volume-size`=`ROOT_VOLUME_SIZE`] [`--tags`=`TAG`,[`TAG`,…]] [`--validate-only`] [`--vm-size`=`VM_SIZE`] [`--proxy-resource-group-id`=`PROXY_RESOURCE_GROUP_ID` `--proxy-secret-id`=`PROXY_SECRET_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `(DEPRECATED)` Create a node pool in an Anthos cluster on Azure. 

This command is deprecated. See <https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement> for more details. 

EXAMPLES
     To create a node pool named ``my-node-pool`` in a cluster named ``my-cluster`` managed in location ``us-west1``, run: 
    
    
    gcloud alpha container azure node-pools create my-node-pool --cluster=my-cluster --location=us-west1 --node-version=NODE_VERSION --ssh-public-key=SSH_PUBLIC_KEY --subnet-id=SUBNET_ID

POSITIONAL ARGUMENTS
    

Nodepool resource - node pool to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `node_pool` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`NODE_POOL`
     ID of the nodepool or fully qualified identifier for the nodepool. 

To set the `nodepool` attribute: 

  * provide the argument `node_pool` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--cluster`=`CLUSTER`
     cluster of the nodepool. 

To set the `cluster` attribute: 

  * provide the argument `node_pool` on the command line with a fully specified name; 
  * provide the argument `--cluster` on the command line. 


`--location`=`LOCATION`
     Google Cloud location for the nodepool. 

To set the `location` attribute: 

  * provide the argument `node_pool` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `container_azure/location`. 


REQUIRED FLAGS
    

`--max-pods-per-node`=`MAX_PODS_PER_NODE`
     Maximum number of pods per node. 
`--node-version`=`NODE_VERSION`
     Kubernetes version to use for the node pool. 
`--ssh-public-key`=`SSH_PUBLIC_KEY`
     SSH public key to use for authentication. 
`--subnet-id`=`SUBNET_ID`
     Subnet ID of an existing VNET to use for the node pool. 
Node pool autoscaling 

This must be specified. 

`--max-nodes`=`MAX_NODES`
     Maximum number of nodes in the node pool. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--min-nodes`=`MIN_NODES`
     Minimum number of nodes in the node pool. 

This flag argument must be specified if any of the other arguments in this group are specified. 

OPTIONAL FLAGS
    

`--annotations`=`ANNOTATION`,[`ANNOTATION`,…]
     Annotations for the node pool. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--azure-availability-zone`=`AZURE_AVAILABILITY_ZONE`
     Azure availability zone where the node pool will be created. 
`--config-encryption-key-id`=`CONFIG_ENCRYPTION_KEY_ID`
     URL the of the Azure Key Vault key (with its version) to use to encrypt / decrypt config data. 
`--config-encryption-public-key`=`CONFIG_ENCRYPTION_PUBLIC_KEY`
     RSA key of the Azure Key Vault public key to use for encrypting config data. 
`--enable-autorepair`
     Enable node autorepair feature for a node pool. Use --no-enable-autorepair to disable. 
    
    
    gcloud alpha container azure node-pools create --enable-autorepair

Node autorepair is disabled by default. 

`--image-type`=`IMAGE_TYPE`
     Set the OS image type to use on node pool instances. 

Examples: 
    
    
    gcloud alpha container azure node-pools create --image-type=windows
    gcloud alpha container azure node-pools create --image-type=ubuntu

`--node-labels`=`NODE_LABEL`,[`NODE_LABEL`,…]
     Labels assigned to the node pool's nodes. 
`--node-taints`=`NODE_TAINT`,[`NODE_TAINT`,…]
     Taints assigned to nodes of the node pool. Node taint is of format key=value:effect. Effect must be one of: NoExecute, NoSchedule, PreferNoSchedule. 
`--root-volume-size`=`ROOT_VOLUME_SIZE`
     Size of the root volume. The value must be a whole number followed by a size unit of `GB` for gigabyte, or `TB` for terabyte. If no size unit is specified, GB is assumed. 
`--tags`=`TAG`,[`TAG`,…]
     Applies the given tags (comma separated) on the node pool. Example: 
    
    
    gcloud alpha container azure node-pools create EXAMPLE_NODE_POOL --tags=tag1=one,tag2=two

`--validate-only`
     Validate the creation of the node pool, but don't actually perform it. 
`--vm-size`=`VM_SIZE`
     Azure Virtual Machine Size (e.g. Standard_DS1_v). 
Proxy config 
`--proxy-resource-group-id`=`PROXY_RESOURCE_GROUP_ID`
     The ARM ID the of the resource group containing proxy keyvault. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--proxy-secret-id`=`PROXY_SECRET_ID`
     The URL the of the proxy setting secret with its version. 

This flag argument must be specified if any of the other arguments in this group are specified. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud container azure node-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

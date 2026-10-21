---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/vmware/node-pools/update/
title: gcloud beta container vmware node-pools update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:05:47.204867+00:00
---

# gcloud beta container vmware node-pools update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/vmware/node-pools/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container vmware node-pools update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container vmware node-pools update - update a node pool in an Anthos cluster on VMware 
SYNOPSIS
    

`gcloud beta container vmware node-pools update` (`NODE_POOL` : `--cluster`=`CLUSTER` `--location`=`LOCATION`) [`--async`] [`--display-name`=`DISPLAY_NAME`] [`--validate-only`] [`--boot-disk-size`=`BOOT_DISK_SIZE` `--cpus`=`CPUS` `--image`=`IMAGE` `--image-type`=`IMAGE_TYPE` `--memory`=`MEMORY` `--node-labels`=[`KEY`=`VALUE`,…] `--node-taints`=[`KEY`=`VALUE`:`EFFECT`,…] `--replicas`=`REPLICAS` `--disable-load-balancer` | `--enable-load-balancer`] [`--max-replicas`=`MAX_REPLICAS` `--min-replicas`=`MIN_REPLICAS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a node pool in an Anthos cluster on VMware. 
EXAMPLES
     To update a node pool named ``my-node-pool`` in a cluster named ``my-cluster`` managed in location ``us-west1``, run: 
    
    
    gcloud beta container vmware node-pools update my-node-pool --cluster=my-cluster --location=us-west1

POSITIONAL ARGUMENTS
    

Node pool resource - node pool to update The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `node_pool` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`NODE_POOL`
     ID of the node_pool or fully qualified identifier for the node_pool. 

To set the `node_pool` attribute: 

  * provide the argument `node_pool` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--cluster`=`CLUSTER`
     cluster of the node_pool. 

To set the `cluster` attribute: 

  * provide the argument `node_pool` on the command line with a fully specified name; 
  * provide the argument `--cluster` on the command line. 


`--location`=`LOCATION`
     Google Cloud location for the node_pool. 

To set the `location` attribute: 

  * provide the argument `node_pool` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `container_vmware/location`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--display-name`=`DISPLAY_NAME`
     Display name for the resource. 
`--validate-only`
     If set, only validate the request, but do not actually perform the operation. 
Configuration of the node pool 
`--boot-disk-size`=`BOOT_DISK_SIZE`
     Size of VMware disk to be used during creation in GB. 
`--cpus`=`CPUS`
     Number of CPUs for each node in the node pool. 
`--image`=`IMAGE`
     OS image name in vCenter. 
`--image-type`=`IMAGE_TYPE`
     OS image type to use on node pool instances. 
`--memory`=`MEMORY`
     Size of memory for each node in the node pool in MB. 
`--node-labels`=[`KEY`=`VALUE`,…]
     Kubernetes labels (key/value pairs) to be applied to each node. 
`--node-taints`=[`KEY`=`VALUE`:`EFFECT`,…]
     Applies the given kubernetes taints on all nodes in the new node pool, which can be used with tolerations for pod scheduling. 

Taint effect must be one of the following: `NoSchedule`, `PreferNoSchedule`, or `NoExecute`. 

Examples: 
    
    
    gcloud beta container vmware node-pools update node-pool-1 --cluster=example-cluster --node-taints=key1=val1:NoSchedule,key2=val2:PreferNoSchedule

`--replicas`=`REPLICAS`
     Number of replicas to use on node pool instances. 
At most one of these can be specified: 

`--disable-load-balancer`
     If set, disable the use of load balancer on the node pool instances. 
`--enable-load-balancer`
     If set, enable the use of load balancer on the node pool instances. 
Node pool autoscaling 
`--max-replicas`=`MAX_REPLICAS`
     Maximum number of replicas in the node pool. 
`--min-replicas`=`MIN_REPLICAS`
     Minimum number of replicas in the node pool. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container vmware node-pools update](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/node-pools/update)
    
    
    [gcloud alpha container vmware node-pools update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/vmware/node-pools/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

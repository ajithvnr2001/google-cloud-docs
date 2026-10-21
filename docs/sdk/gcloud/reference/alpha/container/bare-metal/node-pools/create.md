---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/bare-metal/node-pools/create/
title: gcloud alpha container bare-metal node-pools create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:37.732293+00:00
---

# gcloud alpha container bare-metal node-pools create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/bare-metal/node-pools/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container bare-metal node-pools create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container bare-metal node-pools create - create a node pool in an Anthos cluster on bare metal 
SYNOPSIS
    

`gcloud alpha container bare-metal node-pools create` (`NODE_POOL` : `--cluster`=`CLUSTER` `--location`=`LOCATION`) (`--node-configs`=[`labels`=`LABELS`],[`node-ip`=`NODE-IP`] : `--node-labels`=[`KEY`=`VALUE`,…] `--node-taints`=[`KEY`=`VALUE`:`EFFECT`,…] `--disable-serialize-image-pulls` `--registry-burst`=`REGISTRY_BURST` `--registry-pull-qps`=`REGISTRY_PULL_QPS`) [`--annotations`=[`KEY`=`VALUE`,…]] [`--async`] [`--display-name`=`DISPLAY_NAME`] [`--validate-only`] [`--version`=`VERSION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a node pool in an Anthos cluster on bare metal. 
EXAMPLES
     To create a node pool named ``my-node-pool`` in a cluster named ``my-cluster`` managed in location ``us-west1``, run: 
    
    
    gcloud alpha container bare-metal node-pools create my-node-pool --cluster=my-cluster --location=us-west1

POSITIONAL ARGUMENTS
    

Node pool resource - node pool to create The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
  * set the property `container_bare_metal/location`. 


REQUIRED FLAGS
    

Anthos on bare metal node pool configuration. 

This must be specified. 

Populate Bare Metal Node Pool node config. 

Exactly one of these must be specified: 

`--node-configs`=[`labels`=`LABELS`],[`node-ip`=`NODE-IP`]
     Bare Metal Node Pool node configuration. 
`--node-labels`=[`KEY`=`VALUE`,…]
     Labels assigned to nodes of a node pool. 
`--node-taints`=[`KEY`=`VALUE`:`EFFECT`,…]
     Node taint applied to every Kubernetes node in a node pool. 
Modifiable kubelet configurations for bare metal machines. 
`--disable-serialize-image-pulls`
     If set, prevent the Kubelet from pulling multiple images at a time. 
`--registry-burst`=`REGISTRY_BURST`
     Maximum size of bursty pulls, temporarily allow pulls to burst to this number, while still not exceeding registry_pull_qps. 
`--registry-pull-qps`=`REGISTRY_PULL_QPS`
     Limit of registry pulls per second. 
OPTIONAL FLAGS
    

`--annotations`=[`KEY`=`VALUE`,…]
     Annotations on the node pool. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--display-name`=`DISPLAY_NAME`
     Display name for the resource. 
`--validate-only`
     If set, only validate the request, but do not actually perform the operation. 
`--version`=`VERSION`
     Anthos version for the node pool. Defaults to the user cluster version. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud container bare-metal node-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/create)
    
    
    [gcloud beta container bare-metal node-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/bare-metal/node-pools/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

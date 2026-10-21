---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/bare-metal/admin-clusters/update/
title: gcloud beta container bare-metal admin-clusters update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:38:20.752005+00:00
---

# gcloud beta container bare-metal admin-clusters update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/bare-metal/admin-clusters/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container bare-metal admin-clusters update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container bare-metal admin-clusters update - update an Anthos on bare metal admin cluster 
SYNOPSIS
    

`gcloud beta container bare-metal admin-clusters update` (`ADMIN_CLUSTER` : `--location`=`LOCATION`) [`--async`] [`--binauthz-evaluation-mode`=`BINAUTHZ_EVALUATION_MODE`] [`--description`=`DESCRIPTION`] [`--enable-application-logs`] [`--island-mode-service-address-cidr-blocks`=`SERVICE_ADDRESS`,[…]] [`--login-user`=`LOGIN_USER`] [`--maintenance-address-cidr-blocks`=[`MAINTENANCE_ADDRESS_CIDR_BLOCKS`,…]] [`--max-pods-per-node`=`MAX_PODS_PER_NODE`] [`--validate-only`] [`--version`=`VERSION`] [`--api-server-args`=[`KEY`=`VALUE`,…] `--control-plane-node-configs`=[`labels`=`LABELS`],[`node-ip`=`NODE-IP`] `--control-plane-node-labels`=[`KEY`=`VALUE`,…] `--control-plane-node-taints`=[`KEY`=`VALUE`:`EFFECT`,…]] [`--no-proxy`=[`NO_PROXY`,…] `--uri`=`URI`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update an Anthos on bare metal admin cluster. 
EXAMPLES
     To update a cluster named ``my-cluster`` managed in location ``us-west1``, run: 
    
    
    gcloud beta container bare-metal admin-clusters update my-cluster --location=us-west1

POSITIONAL ARGUMENTS
    

Admin cluster resource - admin cluster to update The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `admin_cluster` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ADMIN_CLUSTER`
     ID of the admin_cluster or fully qualified identifier for the admin_cluster. 

To set the `admin_cluster` attribute: 

  * provide the argument `admin_cluster` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Google Cloud location for the admin_cluster. 

To set the `location` attribute: 

  * provide the argument `admin_cluster` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `container_bare_metal/location`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--binauthz-evaluation-mode`=`BINAUTHZ_EVALUATION_MODE`
     Set Binary Authorization evaluation mode for this cluster. `BINAUTHZ_EVALUATION_MODE` must be one of: `DISABLED`, `PROJECT_SINGLETON_POLICY_ENFORCE`. 
`--description`=`DESCRIPTION`
     Description for the resource. 
Anthos on bare metal cluster operations configuration. 
`--enable-application-logs`
     Whether collection of application logs/metrics should be enabled (in addition to system logs/metrics). 
Populate one of the network configs. 
Island mode CIDR network configuration. 
`--island-mode-service-address-cidr-blocks`=`SERVICE_ADDRESS`,[…]
     IPv4 address range for all services in the cluster. 
Anthos on bare metal node access related settings for the admin cluster. 
`--login-user`=`LOGIN_USER`
     User name used to access node machines. 
Anthos on bare metal cluster maintenance configuration. 
`--maintenance-address-cidr-blocks`=[`MAINTENANCE_ADDRESS_CIDR_BLOCKS`,…]
     IPv4 addresses to be placed into maintenance mode. 
Anthos on bare metal admin cluster workload node configuration. 
`--max-pods-per-node`=`MAX_PODS_PER_NODE`
     Maximum number of pods a node can run. 
`--validate-only`
     If set, only validate the request, but do not actually perform the operation. 
`--version`=`VERSION`
     Anthos cluster on bare metal version for the admin cluster resource. 
Anthos on bare metal cluster control plane configuration. 
`--api-server-args`=[`KEY`=`VALUE`,…]
     API Server argument configuration. 
Anthos on bare metal cluster control plane node pool configuration. 
Anthos on bare metal node pool configuration for control plane nodes. 
Anthos on bare metal node configuration for control plane nodes. 
Populate control plane node config. 

At most one of these can be specified: 

`--control-plane-node-configs`=[`labels`=`LABELS`],[`node-ip`=`NODE-IP`]
     Control plane node configuration. 
`--control-plane-node-labels`=[`KEY`=`VALUE`,…]
     Labels assigned to nodes of a node pool. 
`--control-plane-node-taints`=[`KEY`=`VALUE`:`EFFECT`,…]
     Node taint applied to every Kubernetes node in a node pool. 
Anthos on bare metal cluster proxy configuration. 
`--no-proxy`=[`NO_PROXY`,…]
     List of IPs, hostnames, and domains that should skip the proxy. 
`--uri`=`URI`
     Address of the proxy server. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container bare-metal admin-clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update)
    
    
    [gcloud alpha container bare-metal admin-clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/bare-metal/admin-clusters/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

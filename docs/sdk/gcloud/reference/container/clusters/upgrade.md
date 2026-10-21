---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade/
title: gcloud container clusters upgrade \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:46.878435+00:00
---

# gcloud container clusters upgrade  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container clusters upgrade Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container clusters upgrade - upgrade the Kubernetes version of an existing container cluster 
SYNOPSIS
    

`gcloud container clusters upgrade` `NAME` [`--async`] [`--cluster-version`=`CLUSTER_VERSION`] [`--control-plane-soak-duration`=`CONTROL_PLANE_SOAK_DURATION`] [`--image`=`IMAGE`] [`--image-project`=`IMAGE_PROJECT`] [`--image-type`=`IMAGE_TYPE`] [`--master`] [`--node-pool`=`NODE_POOL`] [`--location`=`LOCATION` | `--region`=`REGION` | `--zone`=`ZONE`, `-z` `ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Upgrades the Kubernetes version of an existing container cluster. 

This command upgrades the Kubernetes version of the `node pools` or `master` of a cluster. Note that the Kubernetes version of the cluster's `master` is also periodically upgraded automatically as new releases are available. 

If desired cluster version is omitted, `node pool` upgrades default to the current `master` version and `master` upgrades default to the default cluster version, which can be found in the server config. 

`During node pool upgrades, nodes will be deleted and recreated.` While persistent Kubernetes resources, such as Pods backed by replication controllers, will be rescheduled onto new nodes, a small cluster may experience a few minutes where there are insufficient nodes available to run all of the scheduled Kubernetes resources. 

`Please ensure that any data you wish to keep is stored on a persistent` `disk before upgrading the cluster.` Ephemeral Kubernetes resources--in particular, Pods without replication controllers--will be lost, while persistent Kubernetes resources will get rescheduled. 

EXAMPLES
     Upgrade the node pool `pool-1` of `sample-cluster` to the Kubernetes version of the cluster's master. 
    
    
    gcloud container clusters upgrade sample-cluster --node-pool=pool-1

Upgrade the node pool `pool-1` of `sample-cluster` to Kubernetes version 1.14.7-gke.14: 
    
    
    gcloud container clusters upgrade sample-cluster --node-pool=pool-1 --cluster-version="1.14.7-gke.14"

Upgrade the master of `sample-cluster` to the default cluster version: 
    
    
    gcloud container clusters upgrade sample-cluster --master

POSITIONAL ARGUMENTS
    

`NAME`
     The name of the cluster to upgrade. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--cluster-version`=`CLUSTER_VERSION`
     The GKE release version to which to upgrade the cluster's node pools or master. 

If desired cluster version is omitted, `node pool` upgrades default to the current `master` version and `master` upgrades default to the default cluster version, which can be found in the server config. 

You can find the list of allowed versions for upgrades by running: 
    
    
    [gcloud container get-server-config](https://docs.cloud.google.com/sdk/gcloud/reference/container/get-server-config)

`--control-plane-soak-duration`=`CONTROL_PLANE_SOAK_DURATION`
     The soak duration for the rollback-able control plane upgrade. It only applies to minor version upgrades. Setting this flag will trigger a control plane upgrade with emulated version. The cluster is rollback-able during the soak period. The soak period can be set between 6 hours and 7 days. 
`--image`=`IMAGE`
     The Operating System image for the node pool. This is a private feature, please contact your Google account team for allowlisting this feature. 
`--image-project`=`IMAGE_PROJECT`
     The Google Cloud project storing the Operating System image for the node pool. This is a private feature, please contact your Google account team for allowlisting this feature. 
`--image-type`=`IMAGE_TYPE`
     The image type to use for the cluster/node pool. Defaults to server-specified. 

Image Type specifies the base OS that the nodes in the cluster/node pool will run on. If an image type is specified, that will be assigned to the cluster/node pool and all future upgrades will use the specified image type. If it is not specified the server will pick the default image type. 

The default image type and the list of valid image types are available using the following command. 
    
    
    [gcloud container get-server-config](https://docs.cloud.google.com/sdk/gcloud/reference/container/get-server-config)

`--master`
     Upgrade the cluster's master. Node pools cannot be upgraded at the same time as the master. 
`--node-pool`=`NODE_POOL`
     The node pool to upgrade. 
At most one of these can be specified: 

`--location`=`LOCATION`
     Compute zone or region (e.g. us-central1-a or us-central1) for the cluster. Overrides the default compute/region or compute/zone value for this command invocation. Prefer using this flag over the --region or --zone flags. 
`--region`=`REGION`
     Compute region (e.g. us-central1) for a regional cluster. Overrides the default compute/region property value for this command invocation. 
`--zone`=`ZONE`, `-z` `ZONE`
     Compute zone (e.g. us-central1-a) for a zonal cluster. Overrides the default compute/zone property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha container clusters upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/clusters/upgrade)
    
    
    [gcloud beta container clusters upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters/upgrade)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 

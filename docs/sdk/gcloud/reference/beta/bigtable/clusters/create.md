---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/clusters/create/
title: gcloud beta bigtable clusters create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:10:08.443619+00:00
---

# gcloud beta bigtable clusters create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/clusters/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta bigtable clusters create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta bigtable clusters create - create a bigtable cluster 
SYNOPSIS
    

`gcloud beta bigtable clusters create` (`CLUSTER` : `--instance`=`INSTANCE`) `--zone`=`ZONE` [`--async`] [`--node-scaling-factor`=`NODE_SCALING_FACTOR`; default="node-scaling-factor-1x"] [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`] [`--num-nodes`=`NUM_NODES`; default=3 | [`--autoscaling-cpu-target`=`AUTOSCALING_CPU_TARGET` `--autoscaling-max-nodes`=`AUTOSCALING_MAX_NODES` `--autoscaling-min-nodes`=`AUTOSCALING_MIN_NODES` : `--autoscaling-storage-target`=`AUTOSCALING_STORAGE_TARGET`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a bigtable cluster. 
EXAMPLES
     To add a cluster in zone `us-east1-c` to the instance with id `my-instance-id`, run: 
    
    
    gcloud beta bigtable clusters create my-cluster-id --instance=my-instance-id --zone=us-east1-c

To add a cluster with `10` nodes, run: 
    
    
    gcloud beta bigtable clusters create my-cluster-id --instance=my-instance-id --zone=us-east1-c --num-nodes=10

POSITIONAL ARGUMENTS
    

Cluster resource - The cluster to describe. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CLUSTER`
     ID of the cluster or fully qualified identifier for the cluster. 

To set the `cluster` attribute: 

  * provide the argument `cluster` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     Bigtable instance for the cluster. 

To set the `instance` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line. 


REQUIRED FLAGS
    

`--zone`=`ZONE`
     ID of the zone where the cluster is located. Supported zones are listed at <https://cloud.google.com/bigtable/docs/locations>. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--node-scaling-factor`=`NODE_SCALING_FACTOR`; default="node-scaling-factor-1x"
     Node scaling factor for the cluster. `NODE_SCALING_FACTOR` must be one of: `node-scaling-factor-1x`, `node-scaling-factor-2x`. 
Key resource - The Cloud KMS (Key Management Service) cryptokey that will be used to protect the cluster. The arguments in this group can be used to specify the attributes of this resource. 
`--kms-key`=`KMS_KEY`
     ID of the key or fully qualified identifier for the key. 

To set the `kms-key` attribute: 

  * provide the argument `--kms-key` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--kms-keyring`=`KMS_KEYRING`
     The KMS keyring id of the key. 

To set the `kms-keyring` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-keyring` on the command line. 


`--kms-location`=`KMS_LOCATION`
     The Cloud location for the key. 

To set the `kms-location` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-location` on the command line. 


`--kms-project`=`KMS_PROJECT`
     The Cloud project id for the key. 

To set the `kms-project` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-project` on the command line. 


At most one of these can be specified: 

Manual Scaling 
`--num-nodes`=`NUM_NODES`; default=3
     Number of nodes to serve. 
Autoscaling 
`--autoscaling-cpu-target`=`AUTOSCALING_CPU_TARGET`
     The target CPU utilization percentage for autoscaling. Accepted values are from 10 to 80. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--autoscaling-max-nodes`=`AUTOSCALING_MAX_NODES`
     The maximum number of nodes for autoscaling. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--autoscaling-min-nodes`=`AUTOSCALING_MIN_NODES`
     The minimum number of nodes for autoscaling. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--autoscaling-storage-target`=`AUTOSCALING_STORAGE_TARGET`
     The target storage utilization gibibytes per node for autoscaling. Accepted values are from 2560 to 5120 for SSD clusters and 8192 to 16384 for HDD clusters. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud bigtable clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create)
    
    
    [gcloud alpha bigtable clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/clusters/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

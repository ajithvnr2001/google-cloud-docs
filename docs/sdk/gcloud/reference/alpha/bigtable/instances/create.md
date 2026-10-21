---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/instances/create/
title: gcloud alpha bigtable instances create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:00.506302+00:00
---

# gcloud alpha bigtable instances create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/instances/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha bigtable instances create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha bigtable instances create - create a new Bigtable instance 
SYNOPSIS
    

`gcloud alpha bigtable instances create` `INSTANCE` `--display-name`=`DISPLAY_NAME` [`--async`] [`--cluster`=`CLUSTER`] [`--cluster-config`=[`id`=`ID`,`zone`=`ZONE`,[`nodes`=`NODES`],[`node-scaling-factor`=`NODE_SCALING_FACTOR`],[`kms-key`=`KMS_KEY`],[`autoscaling-min-nodes`=`AUTOSCALING_MIN_NODES`,`autoscaling-max-nodes`=`AUTOSCALING_MAX_NODES`,`autoscaling-cpu-target`=`AUTOSCALING_CPU_TARGET`,`autoscaling-storage-target`=`AUTOSCALING_STORAGE_TARGET`],…]] [`--cluster-num-nodes`=`CLUSTER_NUM_NODES`] [`--cluster-storage-type`=`CLUSTER_STORAGE_TYPE`; default="ssd"] [`--cluster-zone`=`CLUSTER_ZONE`] [`--edition`=`EDITION`] [`--instance-type`=`INSTANCE_TYPE`; default="PRODUCTION"] [`--tags`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new Bigtable instance. 
EXAMPLES
     To create an instance with id `my-instance-id` with a cluster located in `us-east1-c`, run: 
    
    
    gcloud alpha bigtable instances create my-instance-id --display-name="My Instance" --cluster-config=id=my-cluster-id,zone=us-east1-c

To create an instance with multiple clusters, run: 
    
    
    gcloud alpha bigtable instances create my-instance-id --display-name="My Instance" --cluster-config=id=my-cluster-id-1,zone=us-east1-c --cluster-config=id=my-cluster-id-2,zone=us-west1-c,nodes=3

To create an instance with `HDD` storage and `10` nodes, run: 
    
    
    gcloud alpha bigtable instances create my-hdd-instance --display-name="HDD Instance" --cluster-storage-type=HDD --cluster-config=id=my-cluster-id,zone=us-east1-c,nodes=10

To create an instance with edition `ENTERPRISE_PLUS`, run: 
    
    
    gcloud alpha bigtable instances create my-enterprise-plus-instance --display-name="Enterprise Plus Instance" --edition=ENTERPRISE_PLUS --cluster-config=id=my-cluster-id,zone=us-east1-c,nodes=1

POSITIONAL ARGUMENTS
    

Instance resource - The instance to create. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSTANCE`
     ID of the instance or fully qualified identifier for the instance. 

To set the `instance` attribute: 

  * provide the argument `instance` on the command line. 


REQUIRED FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Friendly name of the instance. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--cluster`=`CLUSTER`
     (DEPRECATED) ID of the cluster 

The --cluster argument is deprecated; use --cluster-config instead. 

`--cluster-config`=[`id`=`ID`,`zone`=`ZONE`,[`nodes`=`NODES`],[`node-scaling-factor`=`NODE_SCALING_FACTOR`],[`kms-key`=`KMS_KEY`],[`autoscaling-min-nodes`=`AUTOSCALING_MIN_NODES`,`autoscaling-max-nodes`=`AUTOSCALING_MAX_NODES`,`autoscaling-cpu-target`=`AUTOSCALING_CPU_TARGET`,`autoscaling-storage-target`=`AUTOSCALING_STORAGE_TARGET`],…]
     `Repeatable`. Specify cluster config as a key-value dictionary. 

This is the recommended argument for specifying cluster configurations. 

Keys can be: 
    
    
    *id*: Required. The ID of the cluster.
    
    
    *zone*: Required. ID of the zone where the cluster is located. Supported zones are listed at <https://cloud.google.com/bigtable/docs/locations>.
    
    
    *nodes*: The number of nodes in the cluster. Default=1.
    
    
    *node-scaling-factor*: The node scaling factor for the cluster. Default=node-scaling-factor-1x. NODE_SCALING_FACTOR must be one of: node-scaling-factor-1x, node-scaling-factor-2x.
    
    
    *kms-key*: The Cloud KMS (Key Management Service) cryptokey that will be used to protect the cluster.
    
    
    *autoscaling-min-nodes*: The minimum number of nodes for autoscaling.
    
    
    *autoscaling-max-nodes*: The maximum number of nodes for autoscaling.
    
    
    *autoscaling-cpu-target*: The target CPU utilization percentage for autoscaling. Accepted values are from 10 to 80.
    
    
    *autoscaling-storage-target*: The target storage utilization gibibytes per node for autoscaling. Accepted values are from 2560 to 5120 for SSD clusters and 8192 to 16384 for HDD clusters.

If this argument is specified, the deprecated arguments for configuring a single cluster will be ignored, including `--cluster`, `--cluster-zone`, `--cluster-num-nodes`. 

See `EXAMPLES` section. 

`--cluster-num-nodes`=`CLUSTER_NUM_NODES`
     (DEPRECATED) Number of nodes to serve. 

The --cluster-num-nodes argument is deprecated; use --cluster-config instead. 

`--cluster-storage-type`=`CLUSTER_STORAGE_TYPE`; default="ssd"
     Storage class for the cluster. `CLUSTER_STORAGE_TYPE` must be one of: `hdd`, `ssd`. 
`--cluster-zone`=`CLUSTER_ZONE`
     (DEPRECATED) ID of the zone where the cluster is located. Supported zones are listed at <https://cloud.google.com/bigtable/docs/locations>. 

The --cluster-zone argument is deprecated; use --cluster-config instead. 

`--edition`=`EDITION`
     The edition of the instance. `EDITION` must be one of: `ENTERPRISE`, `ENTERPRISE_PLUS`. 
`--instance-type`=`INSTANCE_TYPE`; default="PRODUCTION"
     (DEPRECATED) The type of instance to create. 

The --instance-type argument is deprecated. DEVELOPMENT instances are no longer offered. All instances are of type PRODUCTION. `INSTANCE_TYPE` must be one of: 

`DEVELOPMENT`
     Development instances are low-cost instances meant for development and testing only. They do not provide high availability and no service level agreement applies. 
`PRODUCTION`
     Production instances provide high availability and are suitable for applications in production. Production instances created with the --instance-type argument have 3 nodes if a value is not provided for --cluster-num-nodes. 
`--tags`=[`KEY`=`VALUE`,…]
     List of tags KEY=VALUE pairs to bind. Each item must be specified in either ID `<tag_key_id>=<tag_value_id>` or namespace format `<tag-key-namespaced-name>=<tag-value-short-name>`. Example: `123/environment=production,123/costCenter=marketing`
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud bigtable instances create](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/create)
    
    
    [gcloud beta bigtable instances create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/instances/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 

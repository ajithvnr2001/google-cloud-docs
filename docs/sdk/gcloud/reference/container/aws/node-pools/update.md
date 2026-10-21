---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update/
title: gcloud container aws node-pools update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:29.938982+00:00
---

# gcloud container aws node-pools update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/node-pools/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container aws node-pools update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container aws node-pools update - update a node pool in an Anthos cluster on AWS 
SYNOPSIS
    

`gcloud container aws node-pools update` (`NODE_POOL` : `--cluster`=`CLUSTER` `--location`=`LOCATION`) [`--async`] [`--config-encryption-kms-key-arn`=`CONFIG_ENCRYPTION_KMS_KEY_ARN`] [`--enable-autorepair`] [`--iam-instance-profile`=`IAM_INSTANCE_PROFILE`] [`--instance-type`=`INSTANCE_TYPE`] [`--max-surge-update`=`MAX_SURGE_UPDATE`] [`--max-unavailable-update`=`MAX_UNAVAILABLE_UPDATE`] [`--node-version`=`NODE_VERSION`] [`--root-volume-iops`=`ROOT_VOLUME_IOPS`] [`--root-volume-kms-key-arn`=`ROOT_VOLUME_KMS_KEY_ARN`] [`--root-volume-size`=`ROOT_VOLUME_SIZE`] [`--root-volume-throughput`=`ROOT_VOLUME_THROUGHPUT`] [`--root-volume-type`=`ROOT_VOLUME_TYPE`] [`--validate-only`] [`--annotations`=`ANNOTATION`,[`ANNOTATION`,…] | `--clear-annotations`] [`--clear-autoscaling-metrics` | `--autoscaling-metrics`=[`AUTOSCALING_METRIC`,…] `--autoscaling-metrics-granularity`=`AUTOSCALING_METRICS_GRANULARITY`] [`--clear-node-labels` | `--node-labels`=`NODE_LABEL`,[`NODE_LABEL`,…]] [`--clear-proxy-config` | `--proxy-secret-arn`=`PROXY_SECRET_ARN` `--proxy-secret-version-id`=`PROXY_SECRET_VERSION_ID`] [`--clear-security-group-ids` | `--security-group-ids`=[`SECURITY_GROUP_ID`,…]] [`--clear-ssh-ec2-key-pair` | `--ssh-ec2-key-pair`=`SSH_EC2_KEY_PAIR`] [`--clear-tags` | `--tags`=`TAG`,[`TAG`,…]] [`--max-nodes`=`MAX_NODES` `--min-nodes`=`MIN_NODES`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(DEPRECATED)` Update a node pool in an Anthos cluster on AWS. 

This command is deprecated. See <https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement> for more details. 

EXAMPLES
     To update a node pool named ``my-node-pool`` in a cluster named ``my-cluster`` managed in location ``us-west1``, run: 
    
    
    gcloud container aws node-pools update my-node-pool --cluster=my-cluster --location=us-west1 --node-version=NODE_VERSION

POSITIONAL ARGUMENTS
    

Node pool resource - node pool to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
  * set the property `container_aws/location`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--config-encryption-kms-key-arn`=`CONFIG_ENCRYPTION_KMS_KEY_ARN`
     Amazon Resource Name (ARN) of the AWS KMS key to encrypt the user data. 
`--enable-autorepair`
     Enable node autorepair feature for a node pool. Use --no-enable-autorepair to disable. 
    
    
    gcloud container aws node-pools update --enable-autorepair

`--iam-instance-profile`=`IAM_INSTANCE_PROFILE`
     Name or ARN of the IAM instance profile associated with the node pool. 
`--instance-type`=`INSTANCE_TYPE`
     AWS EC2 instance type for the node pool's nodes. 
`--max-surge-update`=`MAX_SURGE_UPDATE`
     Maximum number of extra (surge) nodes to be created beyond the current size of the node pool during its update process. Use --max-unavailable-update as well, if needed, to control the overall surge settings. 

To create an extra node each time the node pool is rolling updated, run: 
    
    
    gcloud container aws node-pools update --max-surge-update=1 --max-unavailable-update=0

`--max-unavailable-update`=`MAX_UNAVAILABLE_UPDATE`
     Maximum number of nodes that can be simultaneously unavailable during this node pool's update process. Use --max-surge-update as well, if needed, to control the overall surge settings. 

To modify a node pool with 6 nodes such that, 3 nodes are updated in parallel (1 \+ 2), but keep at least 4 nodes (6 - 2) available each time this node pool is rolling updated, run: 
    
    
    gcloud container aws node-pools update --max-surge-update=1 --max-unavailable-update=2

`--node-version`=`NODE_VERSION`
     Kubernetes version to use for the node pool. 
`--root-volume-iops`=`ROOT_VOLUME_IOPS`
     Number of I/O operations per second (IOPS) to provision for the root volume. 
`--root-volume-kms-key-arn`=`ROOT_VOLUME_KMS_KEY_ARN`
     Amazon Resource Name (ARN) of the AWS KMS key to encrypt the root volume. 
`--root-volume-size`=`ROOT_VOLUME_SIZE`
     Size of the root volume. The value must be a whole number followed by a size unit of `GB` for gigabyte, or `TB` for terabyte. If no size unit is specified, GB is assumed. 
`--root-volume-throughput`=`ROOT_VOLUME_THROUGHPUT`
     Throughput to provision for the root volume, in MiB/s. Only valid if the volume type is GP3. If volume type is GP3 and throughput is not provided, it defaults to 125. 
`--root-volume-type`=`ROOT_VOLUME_TYPE`
     Type of the root volume. `ROOT_VOLUME_TYPE` must be one of: `gp2`, `gp3`. 
`--validate-only`
     Validate the node pool to update, but don't actually perform it. 
Annotations 

At most one of these can be specified: 

`--annotations`=`ANNOTATION`,[`ANNOTATION`,…]
     Annotations for the node pool. 
`--clear-annotations`
     Clear the annotations for the node pool. 
Node pool autoscaling metrics collection 

At most one of these can be specified: 

`--clear-autoscaling-metrics`
     Clear the cloudwatch autoscaling metrics collection associated with the nodepool. 
Or at least one of these can be specified: 

Update existing cloudwatch autoscaling metrics collection parameters 
`--autoscaling-metrics`=[`AUTOSCALING_METRIC`,…]
     Autoscaling metrics to enable. For a list of valid metrics, refer to <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_EnableMetricsCollection.html>. If granularity is specified but not any metrics, all metrics are enabled. 
`--autoscaling-metrics-granularity`=`AUTOSCALING_METRICS_GRANULARITY`
     Frequency at which EC2 Auto Scaling sends aggregated data to AWS CloudWatch. The only valid value is "1Minute". 
Node labels 

At most one of these can be specified: 

`--clear-node-labels`
     Clear the labels assigned to the node pool's nodes. 
`--node-labels`=`NODE_LABEL`,[`NODE_LABEL`,…]
     Labels assigned to the node pool's nodes. 
Proxy config 

At most one of these can be specified: 

`--clear-proxy-config`
     Clear the proxy configuration associated with the node pool. 
Or at least one of these can be specified: 

Update existing proxy config parameters 
`--proxy-secret-arn`=`PROXY_SECRET_ARN`
     ARN of the AWS Secrets Manager secret that contains a proxy configuration. 
`--proxy-secret-version-id`=`PROXY_SECRET_VERSION_ID`
     Version ID string of the AWS Secrets Manager secret that contains a proxy configuration. 
Security groups 

At most one of these can be specified: 

`--clear-security-group-ids`
     Clear any additional security groups associated with the node pool's nodes. This does not remove the default security groups. 
`--security-group-ids`=[`SECURITY_GROUP_ID`,…]
     IDs of additional security groups to add to the node pool's nodes. 
SSH config 

At most one of these can be specified: 

`--clear-ssh-ec2-key-pair`
     Clear the EC2 key pair authorized to login to the node pool's nodes. 
`--ssh-ec2-key-pair`=`SSH_EC2_KEY_PAIR`
     Name of the EC2 key pair authorized to login to the node pool's nodes. 
Tags 

At most one of these can be specified: 

`--clear-tags`
     Clear any tags associated with the node pool's nodes. 
`--tags`=`TAG`,[`TAG`,…]
     Applies the given tags (comma separated) on the node pool. Example: 
    
    
    gcloud container aws node-pools update EXAMPLE_NODE_POOL --tags=tag1=one,tag2=two

Node pool autoscaling 
`--max-nodes`=`MAX_NODES`
     Maximum number of nodes in the node pool. 
`--min-nodes`=`MIN_NODES`
     Minimum number of nodes in the node pool. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha container aws node-pools update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/aws/node-pools/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

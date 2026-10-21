---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/builds/worker-pools/create/
title: gcloud beta builds worker-pools create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:11:49.192897+00:00
---

# gcloud beta builds worker-pools create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/builds/worker-pools/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta builds worker-pools create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta builds worker-pools create - create a worker pool for use by Cloud Build 
SYNOPSIS
    

`gcloud beta builds worker-pools create` `WORKER_POOL` [`--generation`=`GENERATION`; default=1] [`--region`=`REGION`] [`--config-from-file`=`CONFIG_FROM_FILE` | `--disable-public-ip-address` `--network-attachment`=`NETWORK_ATTACHMENT` `--route-all-traffic` | `--peered-network`=`PEERED_NETWORK` `--peered-network-ip-range`=`PEERED_NETWORK_IP_RANGE` `--no-public-egress` `--worker-disk-size`=`WORKER_DISK_SIZE` `--worker-machine-type`=`WORKER_MACHINE_TYPE` `--worker-release`=`WORKER_RELEASE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a worker pool for use by Cloud Build. 
EXAMPLES
     To create a worker pool named `wp1` in region `us-central1`, run: 
    
    
    gcloud beta builds worker-pools create wp1 --region=us-central1

To create a worker pool in project `p1` in region `us-central1` where workers are of machine type `e2-standard-2` and are peered to the VPC network `projects/123/global/networks/default` within the IP range `192.168.0.0/28` and have a disk size of 64GB, run: 
    
    
    gcloud beta builds worker-pools create wp1 --project=p1 --region=us-central1 --peered-network=projects/123/global/networks/default --peered-network-ip-range=192.168.0.0/28 --worker-machine-type=e2-standard-2 --worker-disk-size=64GB

POSITIONAL ARGUMENTS
    

`WORKER_POOL`
     Unique identifier for the worker pool to create. This value should be 1-63 characters, and valid characters are [a-z][0-9]- 
FLAGS
    

`--generation`=`GENERATION`; default=1
     Generation of the worker pool. 
`--region`=`REGION`
     Cloud region where the worker pool is created. See <https://cloud.google.com/build/docs/locations> for available locations. 
At most one of these can be specified: 

`--config-from-file`=`CONFIG_FROM_FILE`
     File that contains the configuration for the worker pool to be created. 

Private pool options: 
    
    
    <https://cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema>

Or at least one of these can be specified: 

Command-line flags to configure the private pool: 
At most one of these can be specified: 

Network configuration for Private Service Connect interface: 
`--disable-public-ip-address`
     If set, workers in the worker pool are created without an external IP address. 

If the worker pool is within a VPC Service Control perimeter, use this flag. 

`--network-attachment`=`NETWORK_ATTACHMENT`
     The network attachment that the worker network interface is peered to. The network attachment is specified in resource URL format projects/{project}/regions/{region}/networkAttachments/{name}. The region of network attachment must be the same as the worker pool. See <https://cloud.google.com/vpc/docs/about-network-attachments> for details. 
`--route-all-traffic`
     Route all traffic through PSC interface. Enable this if you want full control of traffic in the private pool. Configure Cloud NAT for the subnet of network attachment if you need to access public Internet. 

If unset, Only route private IPs, e.g. 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16 through PSC interface. 

Network configuration for Service Networking: 
`--peered-network`=`PEERED_NETWORK`
     Existing network to which workers are peered. The network is specified in resource URL format projects/{network_project}/global/networks/{network_name}. 

If not specified, the workers are not peered to any network. 

`--peered-network-ip-range`=`PEERED_NETWORK_IP_RANGE`
     An IP range for your peered network. Specify the IP range using Classless Inter-Domain Routing (CIDR) notation with a slash and the subnet prefix size, such as `/29`. 

Your subnet prefix size must be between 1 and 29. Optional: you can specify an IP address before the subnet prefix value - for example `192.168.0.0/24`. 

If no IP address is specified, your VPC automatically determines the starting IP for the range. If no IP range is specified, Cloud Build uses `/24` as the default network IP range. 

`--no-public-egress`
     If set, workers in the worker pool are created without an external IP address. 

If the worker pool is within a VPC Service Control perimeter, use this flag. 

Configuration to be used for creating workers in the worker pool: 
`--worker-disk-size`=`WORKER_DISK_SIZE`
     Size of the disk attached to the worker. 

If unspecified, Cloud Build uses a standard disk size. 

`--worker-machine-type`=`WORKER_MACHINE_TYPE`
     Compute Engine machine type for a worker pool. 

If unspecified, Cloud Build uses a standard machine type. 

`--worker-release`=`WORKER_RELEASE`
     Specifies the release channel or version to use for builds in this worker pool. Accepts release channel names (`rapid`, `regular`, `stable`) or specific release versions (for example, `2026.09`, `legacy`). See <https://docs.cloud.google.com/build/docs/release-channels>. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud builds worker-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/builds/worker-pools/create)
    
    
    [gcloud alpha builds worker-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 

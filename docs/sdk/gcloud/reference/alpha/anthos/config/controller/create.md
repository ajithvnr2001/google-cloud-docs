---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/controller/create/
title: gcloud alpha anthos config controller create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:31.770196+00:00
---

# gcloud alpha anthos config controller create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/controller/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha anthos config controller create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha anthos config controller create - create Anthos Config Controller instances 
SYNOPSIS
    

`gcloud alpha anthos config controller create` (`NAME` : `--location`=`LOCATION`) [`--async`] [`--cluster-ipv4-cidr-block`=`CLUSTER_IPV4_CIDR_BLOCK`] [`--cluster-named-range`=`CLUSTER_NAMED_RANGE`] [`--experimental-features`=[`FEATURE`,…]] [`--full-management`] [`--man-block`=`MAN_BLOCK`] [`--man-blocks`=[`BLOCK`,…]] [`--master-ipv4-cidr-block`=`MASTER_IPV4_CIDR_BLOCK`] [`--network`=`NETWORK`] [`--services-ipv4-cidr-block`=`SERVICES_IPV4_CIDR_BLOCK`] [`--services-named-range`=`SERVICES_NAMED_RANGE`] [`--subnet`=`SUBNET`] [`--use-private-endpoint`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create an Anthos Config Controller instance. 
EXAMPLES
     To create an Anthos Config Controller instance with the name ``acc-default``, run: 
    
    
    gcloud alpha anthos config controller create acc-default --location=us-central1

POSITIONAL ARGUMENTS
    

Instance resource - The identifier for a Config Controller instance. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `name` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`NAME`
     ID of the instance or fully qualified identifier for the instance. 

To set the `name` attribute: 

  * provide the argument `name` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The name of the Config Controller instance location. Currently, only ``us-central1``, ``us-east1``, ``us-east4``, ``us-east5``, ``us-west2``, ``northamerica-northeast1``, ``northamerica-northeast2``, ``europe-north1``, ``europe-west1``, ``europe-west3``, ``europe-west6``, ``australia-southeast1``, ``australia-southeast2``, ``asia-northeast1``, ``asia-northeast2`` and ``asia-southeast1`` are supported. 

To set the `location` attribute: 

  * provide the argument `name` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--cluster-ipv4-cidr-block`=`CLUSTER_IPV4_CIDR_BLOCK`
     The IP address range for the cluster pod IPs. Can be specified as a netmask size (e.g. '/14') or as in CIDR notation (e.g. '10.100.0.0/20'). Defaults to '/20' if flag is not provided. 
`--cluster-named-range`=`CLUSTER_NAMED_RANGE`
     The name of the existing secondary range in the clusters subnetwork to use for pod IP addresses. Alternatively, `--cluster_cidr_block` can be used to automatically create a GKE-managed one. 
`--experimental-features`=[`FEATURE`,…]
     Enable experimental features. It can only be enabled in ALPHA version. 
`--full-management`
     Enable full cluster management type. 
`--man-block`=`MAN_BLOCK`
     (DEPRECATED) Master Authorized Network. Allows access to the Kubernetes control plane from this block. Defaults to `0.0.0.0/0` if flag is not provided. 

The --man-block option is deprecated; use --man-blocks instead. 

`--man-blocks`=[`BLOCK`,…]
     Master Authorized Network. Allows users to specify multiple blocks to access the Kubernetescontrol plane from this block. Defaults to `0.0.0.0/0` if flag is not provided. 
`--master-ipv4-cidr-block`=`MASTER_IPV4_CIDR_BLOCK`
     The /28 network that the control plane will use. Defaults to '172.16.0.128/28' if flag is not provided. 
`--network`=`NETWORK`
     Existing VPC Network to put the GKE cluster and nodes in. Defaults to 'default' if flag is not provided. If `--subnet=SUBNET` is also specified, subnet must be a subnetwork of the network specified by this `--network=NETWORK` flag. 
`--services-ipv4-cidr-block`=`SERVICES_IPV4_CIDR_BLOCK`
     The IP address range for the cluster service IPs. Can be specified as a netmask size (e.g. '/14') or as in CIDR notation (e.g. '10.100.0.0/20'). Defaults to '/24' if flag is not provided. 
`--services-named-range`=`SERVICES_NAMED_RANGE`
     The name of the existing secondary range in the clusters subnetwork to use for service ClusterIPs. Alternatively, `--services_cidr_block` can be used to automatically create a GKE-managed one. 
`--subnet`=`SUBNET`
     Specifies the subnet that the VM instances are a part of. `--network=NETWORK` must also be specified, subnet must be a subnetwork of the network specified by the `--network=NETWORK` flag. 
`--use-private-endpoint`
     Only allow access to the master's private endpoint IP. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud anthos config controller create](https://docs.cloud.google.com/sdk/gcloud/reference/anthos/config/controller/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

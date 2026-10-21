---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/azure/clusters/create/
title: gcloud alpha container azure clusters create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:21.501607+00:00
---

# gcloud alpha container azure clusters create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/azure/clusters/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container azure clusters create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container azure clusters create - create an Anthos cluster on Azure 
SYNOPSIS
    

`gcloud alpha container azure clusters create` (`CLUSTER` : `--location`=`LOCATION`) `--azure-region`=`AZURE_REGION` `--cluster-version`=`CLUSTER_VERSION` `--fleet-project`=`FLEET_PROJECT` `--pod-address-cidr-blocks`=`POD_ADDRESS_CIDR_BLOCKS` `--resource-group-id`=`RESOURCE_GROUP_ID` `--service-address-cidr-blocks`=`SERVICE_ADDRESS_CIDR_BLOCKS` `--ssh-public-key`=`SSH_PUBLIC_KEY` `--vnet-id`=`VNET_ID` (`--client`=`CLIENT` | `--azure-application-id`=`AZURE_APPLICATION_ID` `--azure-tenant-id`=`AZURE_TENANT_ID`) [`--admin-groups`=[`GROUP`,…]] [`--admin-users`=`USER`,[`USER`,…]] [`--annotations`=`ANNOTATION`,[`ANNOTATION`,…]] [`--async`] [`--config-encryption-key-id`=`CONFIG_ENCRYPTION_KEY_ID`] [`--config-encryption-public-key`=`CONFIG_ENCRYPTION_PUBLIC_KEY`] [`--database-encryption-key-id`=`DATABASE_ENCRYPTION_KEY_ID`] [`--description`=`DESCRIPTION`] [`--enable-managed-prometheus`] [`--endpoint-subnet-id`=`ENDPOINT_SUBNET_ID`] [`--logging`=`COMPONENT`,[`COMPONENT`,…]] [`--main-volume-size`=`MAIN_VOLUME_SIZE`] [`--replica-placements`=[`REPLICA_PLACEMENT`,…]] [`--root-volume-size`=`ROOT_VOLUME_SIZE`] [`--service-load-balancer-subnet-id`=`SERVICE_LOAD_BALANCER_SUBNET_ID`] [`--subnet-id`=`SUBNET_ID`] [`--tags`=`TAG`,[`TAG`,…]] [`--validate-only`] [`--vm-size`=`VM_SIZE`] [`--proxy-resource-group-id`=`PROXY_RESOURCE_GROUP_ID` `--proxy-secret-id`=`PROXY_SECRET_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `(DEPRECATED)` Create an Anthos cluster on Azure. 

This command is deprecated. See <https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement> for more details. 

EXAMPLES
     To create a cluster named ``my-cluster`` managed in location ``us-west1``, run: 
    
    
    gcloud alpha container azure clusters create my-cluster --location=us-west1 --azure-region=AZURE_REGION --cluster-version=CLUSTER_VERSION --client=CLIENT --pod-address-cidr-blocks=POD_ADDRESS_CIDR_BLOCKS --resource-group-id=RESOURCE_GROUP_ID --ssh-public-key=SSH_PUBLIC_KEY --subnet-id=SUBNET_ID --vnet-id=VNET_ID

POSITIONAL ARGUMENTS
    

Cluster resource - Azure cluster to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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

`--location`=`LOCATION`
     Google Cloud location for the cluster. 

To set the `location` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `container_azure/location`. 


REQUIRED FLAGS
    

`--azure-region`=`AZURE_REGION`
     Azure location to deploy the cluster. Refer to your Azure subscription for available locations. 
`--cluster-version`=`CLUSTER_VERSION`
     Kubernetes version to use for the cluster. 
`--fleet-project`=`FLEET_PROJECT`
     ID or number of the Fleet host project where the cluster is registered. 
`--pod-address-cidr-blocks`=`POD_ADDRESS_CIDR_BLOCKS`
     IP address range for the pods in this cluster in CIDR notation (e.g. 10.0.0.0/8). 
`--resource-group-id`=`RESOURCE_GROUP_ID`
     ID of the Azure Resource Group to associate the cluster with. 
`--service-address-cidr-blocks`=`SERVICE_ADDRESS_CIDR_BLOCKS`
     IP address range for the services IPs in CIDR notation (e.g. 10.0.0.0/8). 
`--ssh-public-key`=`SSH_PUBLIC_KEY`
     SSH public key to use for authentication. 
`--vnet-id`=`VNET_ID`
     ID of the Azure Virtual Network to associate with the cluster. 
Authentication configuration 

Exactly one of these must be specified: 

Client resource - Azure client to use for cluster creation. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--client` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--client` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `container_azure/location`. 


`--client`=`CLIENT`
     ID of the client or fully qualified identifier for the client. 

To set the `client` attribute: 

  * provide the argument `--client` on the command line. 


Azure services authentication 
`--azure-application-id`=`AZURE_APPLICATION_ID`
     ID of the Azure Application to manage Azure resources. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--azure-tenant-id`=`AZURE_TENANT_ID`
     ID of the Azure Tenant to manage Azure resources. 

This flag argument must be specified if any of the other arguments in this group are specified. 

OPTIONAL FLAGS
    

`--admin-groups`=[`GROUP`,…]
     Groups of users that can perform operations as a cluster administrator. 
`--admin-users`=`USER`,[`USER`,…]
     Users that can perform operations as a cluster administrator. If not specified, the value of property core/account is used. 
`--annotations`=`ANNOTATION`,[`ANNOTATION`,…]
     Annotations for the cluster. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--config-encryption-key-id`=`CONFIG_ENCRYPTION_KEY_ID`
     URL the of the Azure Key Vault key (with its version) to use to encrypt / decrypt config data. 
`--config-encryption-public-key`=`CONFIG_ENCRYPTION_PUBLIC_KEY`
     RSA key of the Azure Key Vault public key to use for encrypting config data. 
`--database-encryption-key-id`=`DATABASE_ENCRYPTION_KEY_ID`
     URL the of the Azure Key Vault key (with its version) to use to encrypt / decrypt cluster secrets. 
`--description`=`DESCRIPTION`
     Description for the cluster. 
`--enable-managed-prometheus`
     Enables managed collection for Managed Service for Prometheus in the cluster. 

See <https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke> for more info. 

Managed Prometheus is enabled by default for cluster versions 1.27 or greater, use --no-enable-managed-prometheus to disable. 

`--endpoint-subnet-id`=`ENDPOINT_SUBNET_ID`
     ARM ID of the subnet where the control plane load balancer is deployed. When unspecified, it defaults to the control plane subnet ID. 
`--logging`=`COMPONENT`,[`COMPONENT`,…]
     Set the components that have logging enabled. 

Examples: 
    
    
    gcloud alpha container azure clusters create --logging=SYSTEM
    gcloud alpha container azure clusters create --logging=SYSTEM,WORKLOAD

`COMPONENT` must be one of: `SYSTEM`, `WORKLOAD`. 

`--main-volume-size`=`MAIN_VOLUME_SIZE`
     Size of the main volume. The value must be a whole number followed by a size unit of `GB` for gigabyte, or `TB` for terabyte. If no size unit is specified, GB is assumed. 
`--replica-placements`=[`REPLICA_PLACEMENT`,…]
     Placement info for the control plane replicas. Replica placement is of format subnetid:zone, for example subnetid12345:1 
`--root-volume-size`=`ROOT_VOLUME_SIZE`
     Size of the root volume. The value must be a whole number followed by a size unit of `GB` for gigabyte, or `TB` for terabyte. If no size unit is specified, GB is assumed. 
`--service-load-balancer-subnet-id`=`SERVICE_LOAD_BALANCER_SUBNET_ID`
     ARM ID of the subnet where Kubernetes private service type load balancers are deployed, when the Service lacks a subnet annotation. 
`--subnet-id`=`SUBNET_ID`
     Subnet ID of an existing VNET to use for the cluster control plane. 
`--tags`=`TAG`,[`TAG`,…]
     Applies the given tags (comma separated) on the cluster. Example: 
    
    
    gcloud alpha container azure clusters create EXAMPLE_CLUSTER --tags=tag1=one,tag2=two

`--validate-only`
     Validate the creation of the cluster, but don't actually perform it. 
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
    
    
    [gcloud container azure clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

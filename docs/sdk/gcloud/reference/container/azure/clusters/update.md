---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update/
title: gcloud container azure clusters update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:33.292715+00:00
---

# gcloud container azure clusters update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container azure clusters update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container azure clusters update - update an Anthos cluster on Azure 
SYNOPSIS
    

`gcloud container azure clusters update` (`CLUSTER` : `--location`=`LOCATION`) [`--admin-groups`=[`GROUP`,…]] [`--admin-users`=`USER`,[`USER`,…]] [`--async`] [`--cluster-version`=`CLUSTER_VERSION`] [`--logging`=`COMPONENT`,[`COMPONENT`,…]] [`--ssh-public-key`=`SSH_PUBLIC_KEY`] [`--validate-only`] [`--vm-size`=`VM_SIZE`] [`--annotations`=`ANNOTATION`,[`ANNOTATION`,…] | `--clear-annotations`] [`--clear-description` | `--description`=`DESCRIPTION`] [`--client`=`CLIENT` | `--azure-application-id`=`AZURE_APPLICATION_ID` `--azure-tenant-id`=`AZURE_TENANT_ID` `--clear-client`] [`--disable-managed-prometheus` | `--enable-managed-prometheus`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(DEPRECATED)` Update an Anthos cluster on Azure. 

This command is deprecated. See <https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement> for more details. 

EXAMPLES
     To update a cluster named ``my-cluster`` managed in location ``us-west1``, run: 
    
    
    gcloud container azure clusters update my-cluster --location=us-west1 --cluster-version=CLUSTER_VERSION --client=CLIENT

POSITIONAL ARGUMENTS
    

Cluster resource - Azure cluster to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


FLAGS
    

`--admin-groups`=[`GROUP`,…]
     Groups of users that can perform operations as a cluster administrator. 
`--admin-users`=`USER`,[`USER`,…]
     Users that can perform operations as a cluster administrator. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--cluster-version`=`CLUSTER_VERSION`
     Kubernetes version to use for the cluster. 
`--logging`=`COMPONENT`,[`COMPONENT`,…]
     Set the components that have logging enabled. 

Examples: 
    
    
    gcloud container azure clusters update --logging=SYSTEM
    gcloud container azure clusters update --logging=SYSTEM,WORKLOAD

`COMPONENT` must be one of: `SYSTEM`, `WORKLOAD`. 

`--ssh-public-key`=`SSH_PUBLIC_KEY`
     SSH public key to use for authentication. 
`--validate-only`
     Validate the update of the cluster, but don't actually perform it. 
`--vm-size`=`VM_SIZE`
     Azure Virtual Machine Size (e.g. Standard_DS1_v). 
Annotations 

At most one of these can be specified: 

`--annotations`=`ANNOTATION`,[`ANNOTATION`,…]
     Annotations for the cluster. 
`--clear-annotations`
     Clear the annotations for the cluster. 
Description 

At most one of these can be specified: 

`--clear-description`
     Clear the description for the cluster. 
`--description`=`DESCRIPTION`
     Description for the cluster. 
Authentication configuration 

At most one of these can be specified: 

Client resource - Azure client to use for cluster update. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
`--azure-tenant-id`=`AZURE_TENANT_ID`
     ID of the Azure Tenant to manage Azure resources. 
`--clear-client`
     Clear the Azure client. This flag is required when updating to use Azure workload identity federation from Azure client to manage Azure resources. 
Monitoring Config 

At most one of these can be specified: 

`--disable-managed-prometheus`
     Disable managed collection for Managed Service for Prometheus. 
`--enable-managed-prometheus`
     Enable managed collection for Managed Service for Prometheus. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha container azure clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/azure/clusters/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

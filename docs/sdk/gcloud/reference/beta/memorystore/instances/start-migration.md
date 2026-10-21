---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/memorystore/instances/start-migration/
title: gcloud beta memorystore instances start-migration \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:43.101248+00:00
---

# gcloud beta memorystore instances start-migration  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/memorystore/instances/start-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta memorystore instances start-migration Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta memorystore instances start-migration - start migration for a Memorystore instance 
SYNOPSIS
    

`gcloud beta memorystore instances start-migration` (`INSTANCE` : `--location`=`LOCATION`) `--self-managed-source-ip-address`=`SELF_MANAGED_SOURCE_IP_ADDRESS` `--self-managed-source-network-attachment`=`SELF_MANAGED_SOURCE_NETWORK_ATTACHMENT` `--self-managed-source-port`=`SELF_MANAGED_SOURCE_PORT` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Start migration for a Memorystore instance. 
EXAMPLES
     To start migration of a source instance running at IP address 10.0.0.1 and port 6379 to a Memorystore instance named `my-instance` in region `us-central1`, run: 
    
    
    gcloud beta memorystore instances start-migration my-instance --project=my-project --location=us-central1 --self-managed-source-ip-address=10.0.0.1 --self-managed-source-port=6379 --self-managed-source-network-attachment=projects/my-project/regions/us-central1/networkAttachments/my-network-attachment

POSITIONAL ARGUMENTS
    

Instance resource - The resource name of the instance to start migration on. Format: projects/{project}/locations/{location}/instances/{instance} The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSTANCE`
     ID of the instance or fully qualified identifier for the instance. 

To set the `instance` attribute: 

  * provide the argument `instance` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the instance resource. 

To set the `location` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--self-managed-source-ip-address`=`SELF_MANAGED_SOURCE_IP_ADDRESS`
     The IP address of the source instance. This IP address should be a stable IP address that can be accessed by the Memorystore instance throughout the migration process. 
`--self-managed-source-network-attachment`=`SELF_MANAGED_SOURCE_NETWORK_ATTACHMENT`
     The resource name of the Private Service Connect Network Attachment used to establish connectivity to the source instance. This network attachment has the following requirements: 1. It must be in the same project as the Memorystore instance. 2. It must be in the same region as the Memorystore instance. 3. The subnet attached to the network attachment must be in the same VPC network as the source instance nodes. 

Format: projects/{project}/regions/{region}/networkAttachments/{network_attachment} 

`--self-managed-source-port`=`SELF_MANAGED_SOURCE_PORT`
     The port of the source instance. This port should be a stable port that can be accessed by the Memorystore instance throughout the migration process. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `memorystore/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/memorystore/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud memorystore instances start-migration](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/start-migration)
    
    
    [gcloud alpha memorystore instances start-migration](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/memorystore/instances/start-migration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 

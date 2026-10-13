---
url: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/configure-exascale/
title: gcloud oracle-database cloud-exadata-infrastructures configure-exascale \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:12.849504+00:00
---

# gcloud oracle-database cloud-exadata-infrastructures configure-exascale  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/configure-exascale/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud oracle-database cloud-exadata-infrastructures configure-exascale Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud oracle-database cloud-exadata-infrastructures configure-exascale - configure Exascale Storage for a Cloud Exadata Infrastructure 
SYNOPSIS
    

`gcloud oracle-database cloud-exadata-infrastructures configure-exascale` (`CLOUD_EXADATA_INFRASTRUCTURE` : `--location`=`LOCATION`) `--total-storage-size-gb`=`TOTAL_STORAGE_SIZE_GB` [`--async`] [`--request-id`=`REQUEST_ID`] [`--total-vm-storage-size-gb`=`TOTAL_VM_STORAGE_SIZE_GB`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Configure Exascale Storage for a Cloud Exadata Infrastructure. This operation updates the total storage allocated for Exascale Storage. 
EXAMPLES
     To configure Exascale for a Cloud Exadata Infrastructure with id my-instance in the location us-east4 with 1000 GB of total storage, run: 
    
    
    [gcloud oracle-database cloud-exadata-infrastructures](https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures) configure-exascale my-instance --location=us-east4 --total-storage-size-gb=1000

POSITIONAL ARGUMENTS
    

CloudExadataInfrastructure resource - The name of the Cloud Exadata Infrastructure in the following format: projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `cloud_exadata_infrastructure` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CLOUD_EXADATA_INFRASTRUCTURE`
     ID of the cloudExadataInfrastructure or fully qualified identifier for the cloudExadataInfrastructure. 

To set the `cloud_exadata_infrastructure` attribute: 

  * provide the argument `cloud_exadata_infrastructure` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the cloudExadataInfrastructure resource. 

To set the `location` attribute: 

  * provide the argument `cloud_exadata_infrastructure` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--total-storage-size-gb`=`TOTAL_STORAGE_SIZE_GB`
     The total storage to be allocated to Exascale in GBs. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--request-id`=`REQUEST_ID`
     An optional ID to identify the request. 
`--total-vm-storage-size-gb`=`TOTAL_VM_STORAGE_SIZE_GB`
     Storage size needed for VM storage on Exascale in GBs. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `oracledatabase/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/oracle/database/docs>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 

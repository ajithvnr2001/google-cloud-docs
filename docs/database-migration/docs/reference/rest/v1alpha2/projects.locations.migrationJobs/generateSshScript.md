---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/generateSshScript/
title: Method: projects.locations.migrationJobs.generateSshScript \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:50.823275+00:00
---

# Method: projects.locations.migrationJobs.generateSshScript  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/generateSshScript/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  Method: projects.locations.migrationJobs.generateSshScript Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * VmCreationConfig
    * JSON representation
  * VmSelectionConfig
    * JSON representation
  * Examples
  * Try it!



Generate a SSH configuration script to configure the reverse SSH connectivity.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 asia-southeast3 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west15 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-central2 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8

  
`POST https://datamigration.googleapis.com/v1alpha2/{name}:generateSshScript`

### Path parameters

Parameters  
---  
`name` |  `string` Name of the migration job resource to generate the SSH script. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `datamigration.migrationjobs.generateSshScript`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "vm": string,
      "vmPort": integer,
    
      // Union field vm_config can be only one of the following:
      "vmCreationConfig": {
        object ([VmCreationConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/generateSshScript#VmCreationConfig))
      },
      "vmSelectionConfig": {
        object ([VmSelectionConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/generateSshScript#VmSelectionConfig))
      }
      // End of list of possible types for union field vm_config.
    }  
  
Fields  
---  
`vm` |  `string` Required. Bastion VM Instance name to use or to create.  
`vmPort` |  `integer` The port that will be open on the bastion host  
Union field `vm_config`. The VM configuration `vm_config` can be only one of the following:  
`vmCreationConfig` |  `object (`[VmCreationConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/generateSshScript#VmCreationConfig)`)` The VM creation configuration.  
`vmSelectionConfig` |  `object (`[VmSelectionConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/generateSshScript#VmSelectionConfig)`)` The VM selection configuration.  
  
### Response body

Response message for 'migrationJobs.generateSshScript' request.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "script": string
    }  
  
Fields  
---  
`script` |  `string` The ssh configuration script.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-datamigration `



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## VmCreationConfig

VM creation configuration message.

JSON representation  
---  
      
    
    {
      "vmMachineType": string,
      "vmZone": string,
      "vpc": string,
      "subnet": string
    }  
  
Fields  
---  
`vmMachineType` |  `string` Required. VM instance machine type to create.  
`vmZone` |  `string` The Google Cloud Platform zone to create the VM in.  
`vpc  
**(deprecated)**` |  `string` This item is deprecated!The VPC name the vm needs to be created in.  
`subnet` |  `string` The subnet name the vm needs to be created in.  
  
## VmSelectionConfig

VM selection configuration message

JSON representation  
---  
      
    
    {
      "vmZone": string
    }  
  
Fields  
---  
`vmZone` |  `string` Required. The Google Cloud Platform zone the VM is located.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 

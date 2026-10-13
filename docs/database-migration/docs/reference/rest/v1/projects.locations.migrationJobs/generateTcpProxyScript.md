---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/generateTcpProxyScript/
title: Method: projects.locations.migrationJobs.generateTcpProxyScript \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:36.723094+00:00
---

# Method: projects.locations.migrationJobs.generateTcpProxyScript  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/generateTcpProxyScript/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  Method: projects.locations.migrationJobs.generateTcpProxyScript Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Examples
  * Try it!



Generate a TCP Proxy configuration script to configure a cloud-hosted VM running a TCP Proxy.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 asia-southeast3 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west15 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-central2 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8

  
`POST https://datamigration.googleapis.com/v1/{migrationJob}:generateTcpProxyScript`

### Path parameters

Parameters  
---  
`migrationJob` |  `string` Name of the migration job resource to generate the TCP Proxy script. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `migrationJob`:

  * `datamigration.migrationjobs.generateTcpProxyScript`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "vmName": string,
      "vmMachineType": string,
      "vmZone": string,
      "vmSubnet": string
    }  
  
Fields  
---  
`vmName` |  `string` Required. The name of the Compute instance that will host the proxy.  
`vmMachineType` |  `string` Required. The type of the Compute instance that will host the proxy.  
`vmZone` |  `string` Optional. The Google Cloud Platform zone to create the VM in. The fully qualified name of the zone must be specified, including the region name, for example "us-central1-b". If not specified, uses the "-b" zone of the destination Connection Profile's region.  
`vmSubnet` |  `string` Required. The name of the subnet the Compute instance will use for private connectivity. Must be supplied in the form of projects/{project}/regions/{region}/subnetworks/{subnetwork}. Note: the region for the subnet must match the Compute instance region.  
  
### Response body

Response message for 'migrationJobs.generateTcpProxyScript' request.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "script": string
    }  
  
Fields  
---  
`script` |  `string` The TCP Proxy configuration script.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-datamigration `



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `migrationJob` resource:

  * `datamigration.migrationjobs.generateTcpProxyScript`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 

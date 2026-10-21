---
url: https://docs.cloud.google.com/managed-lustre/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:56.345045+00:00
---

# Access control with IAM  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

You grant access to Google Cloud Managed Lustre operations by granting Identity and Access Management (IAM) roles to users.

IAM permissions only control access to Google Cloud Managed Lustre operations, like creating a Google Cloud Managed Lustre instance. To control access to file system operations on the instance, like reading or writing to a file, use POSIX file permissions.

## Permissions and roles

Managed Lustre uses the following permissions:

Permission | Description  
---|---  
`lustre.instances.create` | Create new instances  
`lustre.instances.delete` | Delete instances  
`lustre.instances.update` | Update instances. Does not allow deletion  
`lustre.instances.get` | Describe instances  
`lustre.instances.list` | List all instances  
`lustre.instances.exportData` | Export data from Managed Lustre to Cloud Storage  
`lustre.instances.importData` | Import data from Cloud Storage to Managed Lustre  
`lustre.locations.get` | Get a location  
`lustre.locations.list` | List all supported locations  
`lustre.operations.list` | List operations  
`lustre.operations.get` | Get an operation  
`lustre.operations.cancel` | Cancel an operation  
`lustre.operations.delete` | Delete an operation  
  
Google Cloud doesn't support granting individual permissions directly; you must grant a role that contains permissions. Managed Lustre's predefined roles are:

  * Managed Lustre Admin (`roles/lustre.admin`)
  * Managed Lustre Viewer (`roles/lustre.viewer`)



The following table lists the permissions granted by the predefined roles for Managed Lustre, as well as the [basic Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic):

Capability | Editor (`roles/editor`) | Managed Lustre (`roles/lustre.*`)   
---|---|---  
`admin` | `viewer`  
Create instances |  |  |   
Delete instances |  |  |   
Update instances |  |  |   
Get instances |  |  |   
List instances |  |  |   
Import/export data from/to Cloud Storage |  |  |   
Get a location |  |  |   
List supported locations |  |  |   
List long-running operations |  |  |   
Get an operation |  |  |   
Cancel an operation |  |  |   
Delete an operation |  |  |   
  
## Custom roles

If the available predefined roles don't meet your organization's access requirements, you can create and apply [custom IAM roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).

When creating custom roles, we recommend using a combination of predefined roles to ensure that the correct permissions are included together.

## Managed Lustre service agent

Managed Lustre uses a [service agent](https://docs.cloud.google.com/iam/docs/service-agents) to access other Google Cloud resources and perform actions on your behalf. A service agent is a Google-managed service account that is automatically created the first time you create a Managed Lustre instance in a project. It can also be manually created.

Granting permissions to the service agent is only required if you use certain optional features. For standard instance creation and file system operations without these features, no service agent configuration is needed.

### Features that require service agent permissions

The following features require granting IAM roles to the service agent:

Feature | Required role | Target resource | Description  
---|---|---|---  
[Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/managed-lustre/docs/cmek) | `roles/cloudkms.cryptoKeyEncrypterDecrypter` | Cloud KMS key | Allows the service agent to encrypt and decrypt data at rest using your key.  
[Transfer data from Cloud Storage](https://docs.cloud.google.com/managed-lustre/docs/transfer-data) | `roles/storage.objectViewer` | Cloud Storage bucket | Allows the service agent to read and import objects from your bucket into the instance.  
[Transfer data to and from Cloud Storage](https://docs.cloud.google.com/managed-lustre/docs/transfer-data) | `roles/storage.objectUser` | Cloud Storage bucket | Allows the service agent to read and write objects during import and export operations.  
  
If you are not using any of these features, you can skip the remaining steps in this section.

### Create or retrieve the service agent identity

To grant permissions to the service agent, you must obtain its identity. The service agent uses the following format:
    
    
    service-PROJECT_NUMBER@gcp-sa-lustre.iam.gserviceaccount.com
    

Use one of the following options to create or determine the service agent identity:

  * **If you have not created a Managed Lustre instance:** Create the service agent manually by running the [`services identity create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/identity/create) command:
        
        gcloud beta services identity create \
          --service=lustre.googleapis.com \
          --project=PROJECT_NUMBER_OR_ID
        

Replace PROJECT_NUMBER_OR_ID with the project number or ID of the project where you want to create the Managed Lustre instance. The command returns output similar to the following:
        
        Service identity created: service-1234567890@gcp-sa-lustre.iam.gserviceaccount.com
        

  * **If you have already created a Managed Lustre instance:** To construct the service agent identity, retrieve your project number using the `gcloud projects describe` command:
        
        gcloud projects describe PROJECT_ID --format="value(projectNumber)"
        

Replace PROJECT_ID with your project ID. Then, substitute PROJECT_NUMBER in the service agent email address:
        
        service-PROJECT_NUMBER@gcp-sa-lustre.iam.gserviceaccount.com
        




### Grant permissions to the service agent

After obtaining your service agent identity, see the following documentation to grant the required role for your feature:

  * [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/managed-lustre/docs/cmek#grant-permissions)
  * [Transfer data to and from Cloud Storage](https://docs.cloud.google.com/managed-lustre/docs/transfer-data#grant-permissions)



## Additional required Google Cloud permissions

In addition to `lustre` permissions, you might require permissions in other Google Cloud services to perform specific tasks:

Task | Permission  
---|---  
Create a VPC network  | See the _Required permissions_ section of [Configure a VPC network](https://docs.cloud.google.com/managed-lustre/docs/vpc#iam)  
Create Compute Engine VMs  | Compute Instance Admin (v1). (`roles/compute.instanceAdmin.v1`) For more information, refer to the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#required-roles).  
Create and manage Google Kubernetes Engine clusters  | Container Admin. (`roles/container.admin`) For more information, refer to the [Google Kubernetes Engine documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam#predefined).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

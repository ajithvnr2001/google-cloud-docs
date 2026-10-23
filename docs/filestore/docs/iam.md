---
url: https://docs.cloud.google.com/filestore/docs/iam/
title: IAM roles and permissions \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:37.711118+00:00
---

# IAM roles and permissions  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  IAM roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

You grant access to Filestore operations by [granting Identity and Access Management (IAM) roles to users](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

IAM permissions only control access to Filestore operations, like creating a Filestore instance. To control access to operations on the file share, like read or execute, use POSIX file permissions.

## Use Filestore roles

To grant Filestore permissions to users, use the Filestore Editor (`roles/file.editor`) and Filestore Viewer (`roles/file.viewer`) roles. If you prefer, you can also use [basic roles](https://docs.cloud.google.com/filestore/docs/access-control#basic-roles) for this purpose.

Use the following table to see the Filestore permissions associated with Filestore roles.

**Permission** | **Action** | **Filestore Editor** | **Filestore Viewer**  
---|---|---|---  
file.locations.get | Get information about a location supported by this service. | ✓ | ✓  
file.locations.list | List information about the supported locations for this service. | ✓ | ✓  
file.instances.create | Create a Filestore instance. | ✓ |   
file.instances.update | Update a Filestore instance. | ✓ |   
file.instances.delete | Delete a Filestore instance. | ✓ |   
file.instances.get | Get details about a specific Filestore instance. | ✓ | ✓  
file.instances.list | List the Filestore instances in the project. | ✓ | ✓  
file.operations.get | Get the status of a Filestore instance operation. | ✓ | ✓  
file.operations.list | List Filestore instance operations. | ✓ | ✓  
file.operations.cancel | Cancel a Filestore instance operation. | ✓ |   
file.operations.delete | Delete a Filestore instance operation. | ✓ |   
file.backups.create | Create a Filestore backup. | ✓ |   
file.backups.update | Update a Filestore backup. | ✓ |   
file.backups.delete | Delete a Filestore backup. | ✓ |   
file.backups.get | Get details about a specific Filestore backup. | ✓ | ✓  
file.backups.list | List the Filestore backups in the project. | ✓ | ✓  
file.snapshots.create | Create a Filestore snapshot. | ✓ |   
file.snapshots.update | Update a Filestore snapshot. | ✓ |   
file.snapshots.delete | Delete a Filestore snapshot. | ✓ |   
file.snapshots.get | Get details about a specific Filestore snapshot. | ✓ | ✓  
file.snapshots.list | List the Filestore snapshot in the project. | ✓ | ✓  
  
## Using basic roles

Filestore permissions are also associated with the IAM [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) of owner, editor, and viewer. To grant Filestore permissions to users, you can use these roles in addition to the Filestore roles.

Use the following table to see the Filestore permissions associated with basic roles.

**Permission** | **Action** | **Project Owner** | **Project Editor** | **Project Viewer**  
---|---|---|---|---  
file.locations.get | Get information about a location supported by this service. | ✓ | ✓ | ✓  
file.locations.list | List information about the supported locations for this service. | ✓ | ✓ | ✓  
file.instances.create | Create a Filestore instance. | ✓ | ✓ |   
file.instances.update | Update a Filestore instance. | ✓ | ✓ |   
file.instances.delete | Delete a Filestore instance. | ✓ | ✓ |   
file.instances.get | Get details about a specific Filestore instance. | ✓ | ✓ | ✓  
file.instances.list | List the Filestore instances in the project. | ✓ | ✓ | ✓  
file.operations.get | Get the status of a Filestore instance operation. | ✓ | ✓ | ✓  
file.operations.list | List Filestore instance operations. | ✓ | ✓ | ✓  
file.operations.cancel | Cancel a Filestore instance operation. | ✓ | ✓ |   
file.operations.delete | Delete a Filestore instance operation. | ✓ | ✓ |   
file.backups.create | Create a Filestore backup. | ✓ | ✓ |   
file.backups.update | Update a Filestore backup. | ✓ | ✓ |  | file.backups.delete | Delete a Filestore backup. | ✓ | ✓ |   
file.backups.get | Get details about a specific Filestore backup. | ✓ | ✓ | ✓  
file.backups.list | List the Filestore backups in the project. | ✓ | ✓ | ✓  
file.snapshots.create | Create a Filestore snapshot. | ✓ | ✓ |  | file.snapshots.update | Update a Filestore snapshot. | ✓ | ✓ |  | file.snapshots.delete | Delete a Filestore snapshot. | ✓ | ✓ |   
file.snapshots.get | Get details about a specific Filestore snapshot. | ✓ | ✓ | ✓  
file.snapshots.list | List the Filestore snapshot in the project. | ✓ | ✓ | ✓  
  
## Custom roles

If the predefined IAM roles don't meet your needs, you can define a custom role with permissions that you specify using IAM's [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles). When you create custom roles for Filestore, make sure that you include both `resourcemanager.projects.get` and `resourcemanager.projects.list` so that the role has permission to query project resources.

## Related roles

Other roles may be required for access to other Google Cloud services. For example, if you want to view or monitor metrics related to Filestore instance performance, you'll need access to the following roles:

  * Monitoring Viewer
  * Monitoring Editor



To see how to grant access to these roles and others, see [Grant access to Cloud Monitoring](https://docs.cloud.google.com/monitoring/access-control#grant-monitoring-access).

## Next steps

  * Try one of the Filestore quickstarts:

    * Using the [Google Cloud console](https://docs.cloud.google.com/filestore/docs/quickstart-console)
    * Using the [Google Cloud CLI](https://docs.cloud.google.com/filestore/docs/quickstart-gcloud)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

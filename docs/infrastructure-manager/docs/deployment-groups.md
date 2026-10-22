---
url: https://docs.cloud.google.com/infrastructure-manager/docs/deployment-groups/
title: Manage deployment groups \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:44.250411+00:00
---

# Manage deployment groups  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/deployment-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Manage deployment groups Stay organized with collections  Save and categorize content based on your preferences. 

This guide helps you understand how to create, manage, and delete deployment groups.

A deployment group is a collection of deployments arranged in a directed acyclic graph. Use deployment groups to manage related deployments as a single logical resource. You can apply deployments in topological order, or delete them in reverse topological order.

## Before you begin

  1. Ensure [Infra Manager is enabled](https://docs.cloud.google.com/infrastructure-manager/docs/enable-service), and the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) is installed and initialized.
  2. Ensure you have the [Config Admin](https://docs.cloud.google.com/infrastructure-manager/docs/access-control) (`roles/config.admin`) Identity and Access Management role.
  3. Ensure your project has an existing deployment, or create a deployment. To create a test deployment for creating deployment groups, run the following command:
         
         gcloud infra-manager deployments apply projects/PROJECT_ID/locations/LOCATION/deployments/NEW_DEPLOYMENT_ID \
          --service-account=SERVICE_ACCOUNT \
          --git-source-repo="https://github.com/terraform-google-modules/terraform-google-network" \
          --git-source-directory="examples/simple_project_with_regional_network" \
          --git-source-ref="v6.0.1" \
          --input-values=network_name=test-network,project_id=PROJECT_ID \
          --import-existing-resources
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * LOCATION: the Google Cloud location of the deployment you need to create to make a deployment group. For example, `us-central1`.
     * NEW_DEPLOYMENT_ID: the ID of a deployment. You need an existing deployment to create a deployment group. Replace `EXISTING_DEPLOYMENT_ID` with `NEW_DEPLOYMENT_ID` in the following sections.
     * SERVICE_ACCOUNT: the ID of the service account you're using to create the deployment.



## Create a deployment group

A deployment group is a collection of deployments that Infra Manager manages as a single logical unit.

When you create a deployment group, each deployment you add to the group is a _deployment unit_.

You can create deployment groups in individual regions (such as `us-central1`) or in multi-regions (like `us`). All deployment units in a deployment group must reside in the _same project and location_ as the deployment group itself. Cross-region orchestration within a single deployment group isn't supported.

To create a deployment group, use the REST API as follows:

  1. Send a `POST` request to the `deploymentGroups` endpoint:
         
         curl \
             -X POST \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json" \
             "https://config.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/deploymentGroups/?deployment_group_id=DEPLOYMENT_GROUP_ID" \
             --data '{
               "deploymentUnits": [
                 {
                     "id": "DEPLOYMENT_UNIT_ID_1",
                     "deployment": "projects/PROJECT_ID/locations/LOCATION/deployments/EXISTING_DEPLOYMENT_ID"
                 },
                 {
                     "id": "DEPLOYMENT_UNIT_ID_2",
                     "dependencies": ["DEPENDENT_UNIT_ID"]
                 }
               ]
             }'
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * LOCATION: the Google Cloud location of the deployment group. For example, `us-central1`.
     * DEPLOYMENT_GROUP_ID: the ID of the deployment group you want to create.
     * DEPLOYMENT_UNIT_ID_1: the ID of the deployment unit to add to the deployment group.
     * EXISTING_DEPLOYMENT_ID: the ID of an existing deployment you use to create a deployment unit of the deployment group.
     * DEPLOYMENT_UNIT_ID_2: the ID of a second deployment unit to add to the deployment group. You can add definitions for each deployment unit you want to add to your deployment group.
     * Optional: DEPENDENT_UNIT_ID: the ID of the deployment unit that serves as a dependency. This dependency must be provisioned _before_ the defined unit, and deprovisioned _after_ it.
  2. Send a `GET` request to the `deploymentGroup` endpoint:
         
         curl \
             -X GET \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json" \
             "https://config.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/deploymentGroups/DEPLOYMENT_GROUP_ID"
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * LOCATION: the Google Cloud location of the deployment group. For example, `us-central1`.
     * DEPLOYMENT_GROUP_ID: the ID of the new deployment group.



## Provision a deployment group

To apply the deployments referenced in a deployment group, you must provision the group. Provisioning applies the deployments in the order defined by the `deploymentUnits` structure. If you need to create or update a deployment during this process, you can provide its definition in the `deploymentSpecs` object of your provision request.

**Caution:** Deployments that have been removed from the last succeeded revision will be deleted by Infra Manager along with their resources.

To provision a deployment group, use the REST API as follows:

  1. Send a `POST` request to the `provision` endpoint:
         
         curl \
             -X POST \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json" \
             "https://config.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/deploymentGroups/DEPLOYMENT_GROUP_ID:provision" \
             --data '{
               "deploymentSpecs": {
                 "DEPLOYMENT_UNIT_ID_2": {
                     "deploymentId": "DEPLOYMENT_ID_2",
                     "deployment": {
                         "terraformBlueprint": {
                             "gitSource": {
                                 "directory": "examples/simple_project_with_regional_network",
                                 "ref": "v6.0.1",
                                 "repo": "https://github.com/terraform-google-modules/terraform-google-network"
                             },
                             "inputValues": {
                                 "network_name": {
                                     "inputValue": "test-network"
                                 }
                             },
                             "externalValues": {
                                 "project_id": {
                                     "deploymentSource": {
                                         "deployment": "projects/PROJECT_ID/locations/LOCATION/deployments/EXISTING_DEPLOYMENT_ID",
                                         "outputName": "project_id"
                                     }
                                 }
                             }
                         },
                         "serviceAccount": "SERVICE_ACCOUNT",
                         "importExistingResources": true
                     }
                 }
               }
             }'
         

**Note:** A deployment unit can only reference `externalValues` from a source deployment in the _same project and location_.

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * LOCATION: the Google Cloud location of the deployment group. For example, `us-central1`.
     * DEPLOYMENT_GROUP_ID: the ID of the new deployment group.
     * DEPLOYMENT_UNIT_ID_2: the ID of a second deployment unit to add to the deployment group. You can add definitions for each deployment unit you want to add to your deployment group.
     * DEPLOYMENT_ID_2: the string ID of the second deployment unit to add to the deployment group.
     * EXISTING_DEPLOYMENT_ID: the ID of an existing deployment.
     * SERVICE_ACCOUNT: the string ID of the service account you're using to provision the deployment group.
  2. To send a `GET` request to the operations endpoint, use the REST API as follows:
         
         curl \
              -X GET \
              -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
              -H "Content-Type: application/json" \
              "https://config.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID"
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * LOCATION: the Google Cloud location of the deployment group. For example, `us-central1`.
     * OPERATION_ID: the operation ID you want to query. For example, `operation-1000000000000-64d67ecd2868c-caa044f9-6b48677e`
  3. Infra Manager uses a long-running operation (LRO) to show provisioning progress. A successful response indicates that provisioning is complete:
         
         {
           "name": "projects/PROJECT_ID/locations/LOCATION/operations/OP_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.config.v1.OperationMetadata",
             "createTime": "2026-02-24T01:27:57.045161236Z",
             "target": "projects/PROJECT_ID/locations/LOCATION/deploymentGroups/DEPLOYMENT_GROUP_ID",
             "verb": "update",
             "requestedCancellation": false,
             "apiVersion": "v1",
             "provisionDeploymentGroupMetadata": {
               "step": "PROVISIONING_DEPLOYMENT_UNITS",
               "deploymentUnitProgresses": [
                 {
                   "unitId": "DEPLOYMENT_UNIT_ID_1",
                   "deployment": "projects/PROJECT_ID/locations/LOCATION/deployments/EXISTING_DEPLOYMENT_ID",
                   "state": "APPLYING_DEPLOYMENT",
                   "intent": "UPDATE_DEPLOYMENT",
                   "deploymentOperationSummary": {
                     "build": "56c739c7-cf42-457c-a889-0e0c139cf7b3",
                     "logs": "gs://path/to/log",
                     "content": "gs://path/to/content",
                     "artifacts": "gs://path/to/artifacts"
                   }
                 },
                 {
                   "unitId": "DEPLOYMENT_UNIT_ID_2",
                   "state": "QUEUED",
                   "intent": "CREATE_DEPLOYMENT"
                 }
               ]
             }
           }
         }
         

Where:

     * OP_ID: the operation ID. Generated by Infra Manager.
     * EXISTING_DEPLOYMENT_ID: the ID of the deployment that Infra Manager will provision before `DEPLOYMENT_UNIT_ID_1`.



## List revisions of a deployment group

Infra Manager creates a deployment group revision after a `provision` or `deprovision` operation completes.

To list deployment group revisions, use the REST API as follows:

  1. Send a `GET` request to the `revisions` endpoint:
         
         curl \
             -X GET \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json" \
             "https://config.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/deploymentGroups/DEPLOYMENT_GROUP_ID/revisions"
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * LOCATION: the Google Cloud location of the deployment group. For example, `us-central1`.
     * DEPLOYMENT_GROUP_ID: the ID of the deployment group you want to list revisions for.



## Update a deployment group

To update a deployment group, change your deployment group definition. You can optionally provision the updated definition to the deployment group.

To update a deployment group, use the REST API as follows:

  1. Send a `PATCH` request to the `deploymentGroups` endpoint:
         
         curl \
             -X PATCH \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json" \
             "https://config.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/deploymentGroups/DEPLOYMENT_GROUP_ID" \
             --data '{
               "deploymentUnits": [
                 {
                     "id": "DEPLOYMENT_UNIT_ID_3"
                 }
               ]
             }'
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * LOCATION: the Google Cloud location of the deployment group. For example, `us-central1`.
     * DEPLOYMENT_GROUP_ID: the ID of the deployment group you want to update.
     * DEPLOYMENT_UNIT_ID_3: the ID for the deployment to update.
  2. Optional: Provision the updated deployment group. Send a `POST` request to the `provision` endpoint:
         
         curl \
             -X POST \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json" \
             "https://config.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/deploymentGroups/DEPLOYMENT_GROUP_ID:provision" \
             --data '{
               "deploymentSpecs": {
                 "DEPLOYMENT_UNIT_ID_3": {
                     "deploymentId": "EXISTING_DEPLOYMENT_ID",
                     "deployment": {
                         "terraformBlueprint": {
                             "gitSource": {
                                 "directory": "examples/simple_project_with_regional_network",
                                 "ref": "v6.0.1",
                                 "repo": "https://github.com/terraform-google-modules/terraform-google-network"
                             },
                             "inputValues": {
                                 "network_name": {
                                     "inputValue": "test-network"
                                 },
                                 "project_id": {
                                   "inputValue": "PROJECT_ID"
                                 }
                             }
                         },
                         "serviceAccount": "SERVICE_ACCOUNT",
                         "importExistingResources": true
                     }
                 }
               }
             }'
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * LOCATION: the Google Cloud location of the deployment group. For example, `us-central1`.
     * DEPLOYMENT_GROUP_ID: the ID of the deployment group you want to update.
     * DEPLOYMENT_UNIT_ID_3: the ID of a third deployment unit to add to the deployment group.
     * EXISTING_DEPLOYMENT_ID: the ID of an existing deployment.
     * SERVICE_ACCOUNT: the string ID of the service account you're using to update the deployment group.

When you provision a deployment group, changes based on the _last successful revision_ are applied to deployments within the deployment group.

If you remove a deployment from the deployment group definition and then provision, the removed deployment will be deleted along with its resources.

  3. A successful response indicates that provisioning is complete.
         
         {
           "name": "projects/PROJECT_ID/locations/LOCATION/operations/OP_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.config.v1.OperationMetadata",
             "createTime": "2026-02-26T20:03:26.580085899Z",
             "target": "projects/PROJECT_ID/locations/LOCATION/deploymentGroups/DEPLOYMENT_GROUP_ID",
             "verb": "update",
             "requestedCancellation": false,
             "apiVersion": "v1",
             "provisionDeploymentGroupMetadata": {
               "step": "PROVISIONING_DEPLOYMENT_UNITS",
               "deploymentUnitProgresses": [
                 {
                   "unitId": "revisions/REVISION_ID/deploymentUnits/DEPLOYMENT_UNIT_ID_2",
                   "deployment": "projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID_2",
                   "state": "DELETING_DEPLOYMENT",
                   "intent": "CLEAN_UP",
                   "deploymentOperationSummary": {
                     "deploymentStep": "VALIDATING_REPOSITORY"
                   }
                 },
                 {
                   "unitId": "revisions/REVISION_ID/deploymentUnits/DEPLOYMENT_UNIT_ID_1",
                   "deployment": "projects/PROJECT_ID/locations/LOCATION/deployments/NEW_DEPLOYMENT_NAME",
                   "state": "QUEUED",
                   "intent": "CLEAN_UP"
                 },
                 {
                   "unitId": "DEPLOYMENT_UNIT_ID_3",
                   "state": "QUEUED",
                   "intent": "RECREATE_DEPLOYMENT"
                 }
               ]
             }
           },
           "done": false
         }
         

Where:

     * OP_ID: represents the operation ID. Generated by Infra Manager.
     * REVISION_ID: represents the revision ID. Generated by Infra Manager.



## Deprovision a deployment group

Deprovision a deployment group to delete all of its referenced deployments, and any deployments that were part of the last successful revision (but have since been deleted).

To deprovision a deployment group, use the REST API as follows:

  1. Send a `POST` request to the `deprovision` endpoint:
         
         curl \
             -X POST \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json" \
             "https://config.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/deploymentGroups/DEPLOYMENT_GROUP_ID:deprovision" \
             --data '{
               "deletePolicy": "DELETE",
               "force": true
             }'
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * LOCATION: the Google Cloud location of the deployment group. For example, `us-central1`.
     * DEPLOYMENT_GROUP_ID: the ID of the deployment group you want to deprovision.
  2. A successful response indicates that deprovisioning is complete.
         
         {
           "name": "projects/PROJECT_ID/locations/LOCATION/operations/OP_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.config.v1.OperationMetadata",
             "createTime": "2026-02-26T20:12:46.929574561Z",
             "endTime": "2026-02-26T20:14:04.390333218Z",
             "target": "projects/PROJECT_ID/locations/LOCATION/deploymentGroups/DEPLOYMENT_GROUP_ID",
             "verb": "update",
             "requestedCancellation": false,
             "apiVersion": "v1",
             "provisionDeploymentGroupMetadata": {
               "step": "SUCCEEDED",
               "deploymentUnitProgresses": [
                 {
                   "unitId": "DEPLOYMENT_UNIT_ID",
                   "deployment": "projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_NAME_3",
                   "state": "SUCCEEDED",
                   "deploymentOperationSummary": {
                     "deploymentStep": "SUCCEEDED"
                   }
                 }
               ]
             }
           },
           "done": true,
           "response": {
             "@type": "type.googleapis.com/google.cloud.config.v1.DeploymentGroup",
             "name": "projects/PROJECT_ID/locations/LOCATION/deploymentGroups/DEPLOYMENT_GROUP_ID",
             "createTime": "2026-02-24T01:21:14.001716666Z",
             "updateTime": "2026-02-26T20:12:46.931142650Z",
             "state": "ACTIVE",
             "deploymentUnits": [
               {
                 "id": "DEPLOYMENT_UNIT_ID_3"
               }
             ],
             "provisioningState": "DEPROVISIONED"
           }
         }
         




## Delete a deployment group

After you deprovision a deployment group, its metadata remains. To remove the metadata, you must delete the deployment group.

To delete a deployment group, use the REST API as follows:

  1. Send a `DELETE` request to the `deploymentGroups` endpoint. Set `force` to `true` if revisions exist.
         
         curl \
             -X DELETE \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json" \
             "https://config.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/deploymentGroups/DEPLOYMENT_GROUP_ID" \
             --data '{
               "force": true
             }'
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * LOCATION: the Google Cloud location of the deployment group. For example, `us-central1`.
     * DEPLOYMENT_GROUP_ID: the ID of the deployment group you want to delete.



## What's next

  * Learn more about [Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/overview).
  * Refer to the [Infrastructure Manager API reference](https://docs.cloud.google.com/infrastructure-manager/docs/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

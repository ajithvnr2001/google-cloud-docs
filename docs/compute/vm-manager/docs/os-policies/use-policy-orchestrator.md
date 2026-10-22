---
url: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/use-policy-orchestrator/
title: Manage OS policy assignments using policy orchestrator \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:13.387013+00:00
---

# Manage OS policy assignments using policy orchestrator  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/use-policy-orchestrator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Manage OS policy assignments using policy orchestrator Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the policy orchestrator feature in VM Manager to create, update, or delete OS policy resources across different projects and zones in your folders or organization.

## Before you begin

  * Review [OS policy and OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies).
  * Review [OS Config quotas](https://docs.cloud.google.com/compute/vm-manager/docs/os-config-quotas).
  * Ensure that you meet the [prerequisites](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites) for using policy orchestrator.
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Create or update OS policy assignments across projects and zones

You can create policy orchestrators to apply OS policies to selected resources in a project, folder, or organization.

###  Project 

###  Console 

To create a policy orchestrator and to apply OS policy assignments in a project, do the following:

  1. On your local client, create or download an OS policy file. This file must be a JSON or YAML file. For more information about creating OS policies or to view sample OS policies, see [OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy).
  2. In the Google Cloud console, go to the **OS policies** page. 

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  3. Click the **Project Selector** on the Google Cloud console action bar and select the project in which you want to create the policy orchestrator.
  4. Click **Create global**.
  5. Specify a name and description for the policy orchestrator. For more information on naming conventions, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format). VM Manager assigns a unique orchestrator ID to the policy orchestrator. You can edit this ID if required.
  6. In the **OS policies** section, upload the OS policy file.
  7. Optional: In the **State** section, select one of the following options to specify the behavior of the policy orchestrator: 
     * `ACTIVE`: In this state, the policy orchestrator can take actions as soon as it's created.
     * `STOPPED`: A policy orchestrator that's created in this state does not take any actions immediately. You can edit the policy orchestrator later to change its state.
  8. In the **Action** field, select the **UPSERT** action.
  9. In the **Orchestration scope** section, specify the folders and projects in which you want to roll out the OS policies. You must enter only the project numbers and folder numbers in these fields, for example, `123456,7654321`.
  10. Select the zones that contain the VMs that you want to apply the OS policies to. Alternatively, click **Select all** to apply the OS policy changes to resources in all zones.
  11. Optional: In the **Target VM instances** section, specify the target VMs that you want to apply the OS policies to. 
     * Select the OS name and version. For more information, see [OS policy assignments](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy-assignment).
     * You can further filter the VMs by specifying include and exclude labels. 

For example, you can select all the Ubuntu VMs in your test environment, and exclude those that are running Google Kubernetes Engine, by specifying the following: 

       * OS short name: `ubuntu`
       * Include: `env:test`, `env:staging`
       * Exclude: `goog-gke-node`
  12. Specify a rollout plan for the OS policy assignment. 
     * Specify the wave size (also referred to as the disruption budget). For example, 10%.
     * Specify the wait time. For example, 15 minutes.
  13. Click **Create**.



###  gcloud 

To create a policy orchestrator, complete the following steps:

  1. Create or download an OS policy assignment file in JSON or YAML format. For more information about this file and sample policy assignments, see [OS policy assignments](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy-assignment).

  2. Use the [`os-config policy-orchestrators create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create) to create and roll out the OS policy assignment in the specified scope.
         
         gcloud compute os-config policy-orchestrators create ORCHESTRATOR_NAME \
             --policy-type=os_policy_assignment_v1 \
             --policy-file=OS_POLICY_ASSIGNMENT_YAML_FILE \
             --policy-id=POLICY_ID
         

Replace the following:

     * `ORCHESTRATOR_NAME`: name for the policy orchestrator. See [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
     * `OS_POLICY_ASSIGNMENT_FILE`: the absolute path to the OS policy assignment file that you created in the previous step.
     * `POLICY_ID`: a unique ID for the policy orchestrator. If you don't specify a value, policy orchestrator assigns a unique ID for the orchestrator resource.

**Example**
    
    gcloud compute os-config policy-orchestrators create my-os-policy-orchestrator \
          --policy-type=os_policy_assignment_v1 \
          --policy-file=/downloads/assignment-config.yaml \
          --policy-id=policy-123
    




###  REST 

To create a policy orchestrator, complete the following steps:

  1. Create or download an OS policy assignment file. This file must be a JSON file. For more information about creating OS policy assignments or to view sample OS policy assignments, see [OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy-assignment).

  2. Depending on the scope at which you are creating the policy orchestrator, use one of the following methods:

Send a `POST` request to [`projects.locations.global.policyOrchestrators.create` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.global.policyOrchestrators/create).

In the request body, paste the OS policy assignment specifications from the previous step.
         
         POST https://osconfig.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/policyOrchestrators
         
           {
               JSON_OS_POLICY_ORCHESTRATOR
           }
         

Replace the following:

     * `PROJECT_NUMBER`: the numeric ID of the project in which you want to create the policy orchestrator.
     * `JSON_OS_POLICY_ORCHESTRATOR`: the policy orchestrator object in JSON format that defines the orchestrator scope, orchestrated resource, and orchestration state. For more information about the parameters and format, see [`Resource: folders.locations.global.policyOrchestrators`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator).

**Example 1: Create an OS policy assignment that installs a Windows MSI file**

To create an OS policy assignment that installs a Windows MSI downloaded from a Cloud Storage bucket by using the [Sample OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#example-policy-assignment), complete the following steps:

     1. Convert the sample to a JSON file.
     2. Make the following request:
            
            POST https://osconfig.googleapis.com/v2/projects/123456/locations/global/policyOrchestrators
            
            {
            "action": "UPSERT",
            "orchestratedResource": {
              "osPolicyAssignmentV1Payload": {
                "instanceFilter": {
                  "inventories": [
                    {
                      "osShortName": "windows"
                    }
                  ]
                },
                "osPolicies": [
                {
                  "id": "install-msi-policy",
                  "mode": "ENFORCEMENT",
                  "resourceGroups": [
                    {
                      "resources": [
                        {
                          "id": "install-msi",
                          "pkg": {
                            "desiredState": "INSTALLED",
                            "msi": {
                              "source": {
                                "gcs": {
                                  "bucket": "my-bucket",
                                  "generation": "1619136883923956",
                                  "object": "my-app.msi"
                                }
                              }
                            }
                          }
                        }
                      ]
                    }
                  ]
                }
                ],
                "rollout": {
                  "disruptionBudget": {
                    "fixed": 10
                  },
                  "minWaitDuration": "300s"
                }
              }
            },
            "orchestrationScope": {
            "selectors": [
              {
                 "resourceHierarchySelector": {
                    "includedProjects": [
                    "projects/87654321",
                    "projects/4567890"
                    ]
                  }
                }
              ]
            },
            "state": "ACTIVE"
            }
            

**Example 2: Roll out an OS policy assignment to specific projects and zones**

To roll out the OS policy assignment to specific projects and zones, specify `resourceHierarchySelector` and `locationSelector` as separate entries in the `selectors` list:
    
    POST https://osconfig.googleapis.com/v2/projects/123456/locations/global/policyOrchestrators
    
      {
        "action": "UPSERT",
        "orchestratedResource": {
          "osPolicyAssignmentV1Payload": {
            "instanceFilter": {
              "inventories": [
                {
                  "osShortName": "windows"
                }
              ]
            },
            "osPolicies": [
              {
                "id": "install-msi-policy",
                "mode": "ENFORCEMENT",
                "resourceGroups": [
                  {
                    "resources": [
                      {
                        "id": "install-msi",
                        "pkg": {
                          "desiredState": "INSTALLED",
                          "msi": {
                            "source": {
                              "gcs": {
                                "bucket": "my-bucket",
                                "generation": "1619136883923956",
                                "object": "my-app.msi"
                              }
                            }
                          }
                        }
                      }
                    ]
                  }
                ]
              }
            ],
            "rollout": {
              "disruptionBudget": {
                "fixed": 10
              },
              "minWaitDuration": "300s"
            }
          }
        },
        "orchestrationScope": {
          "selectors": [
            {
              "resourceHierarchySelector": {
                "includedProjects": [
                  "projects/87654321",
                  "projects/4567890"
                ]
              }
            },
            {
              "locationSelector": {
                "includedLocations": [
                  "us-central1-a",
                  "us-east1-b"
                ]
              }
            }
          ]
        },
        "state": "ACTIVE"
      }
    




###  Folder 

###  Console 

To create a policy orchestrator and to apply OS policy assignments in a folder, do the following:

  1. On your local client, create or download an OS policy file. This file must be a JSON or YAML file. For more information about creating OS policies or to view sample OS policies, see [OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy).
  2. In the Google Cloud console, go to the **OS policies** page. 

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  3. Click the **Project Selector** on the Google Cloud console action bar and select the folder in which you want to create the policy orchestrator.
  4. Click **Create global**.
  5. Specify a name and description for the policy orchestrator. For more information on naming conventions, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format). VM Manager assigns a unique orchestrator ID to the policy orchestrator. You can edit this ID if required.
  6. In the **OS policies** section, upload the OS policy file.
  7. Optional: In the **State** section, select one of the following options to specify the behavior of the policy orchestrator: 
     * `ACTIVE`: In this state, the policy orchestrator can take actions as soon as it's created.
     * `STOPPED`: A policy orchestrator that's created in this state does not take any actions immediately. You can edit the policy orchestrator later to change its state.
  8. In the **Action** field, select the **UPSERT** action.
  9. In the **Orchestration scope** section, specify the folders and projects in which you want to roll out the OS policies. You must enter only the project numbers and folder numbers in these fields, for example, `123456,7654321`.
  10. Select the zones that contain the VMs that you want to apply the OS policies to. Alternatively, click **Select all** to apply the OS policy changes to resources in all zones.
  11. Optional: In the **Target VM instances** section, specify the target VMs that you want to apply the OS policies to. 
     * Select the OS name and version. For more information, see [OS policy assignments](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy-assignment).
     * You can further filter the VMs by specifying include and exclude labels. 

For example, you can select all the Ubuntu VMs in your test environment, and exclude those that are running Google Kubernetes Engine, by specifying the following: 

       * OS short name: `ubuntu`
       * Include: `env:test`, `env:staging`
       * Exclude: `goog-gke-node`
  12. Specify a rollout plan for the OS policy assignment. 
     * Specify the wave size (also referred to as the disruption budget). For example, 10%.
     * Specify the wait time. For example, 15 minutes.
  13. Click **Create**.



###  gcloud 

To create a policy orchestrator, complete the following steps:

  1. Create or download an OS policy assignment file in JSON or YAML format. For more information about this file and sample policy assignments, see [OS policy assignments](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy-assignment).

  2. Use the [`os-config policy-orchestrators create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create) to create and roll out the OS policy assignment in the specified scope.
         
         gcloud --billing-project=QUOTA_PROJECT_ID compute os-config policy-orchestrators create ORCHESTRATOR_NAME \
             --folder=FOLDER_NUMBER \
             --policy-type=os_policy_assignment_v1 \
             --policy-file=OS_POLICY_ASSIGNMENT_YAML_FILE \
             --policy-id=POLICY_ID \
             --include-projects=PROJECT_NUMBERS
         

Replace the following:

     * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
     * `ORCHESTRATOR_NAME`: name for the policy orchestrator. See [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
     * `FOLDER_NUMBER`: the folder number of the folder in which you want to create the policy orchestrator.
     * `OS_POLICY_ASSIGNMENT_FILE`: the absolute path to the OS policy assignment file that you created in the previous step.
     * `POLICY_ID`: a unique ID for the policy orchestrator. If you don't specify a value, policy orchestrator assigns a unique ID for the orchestrator resource.
     * `PROJECT_NUMBERS`: a list of projects for which you want to apply the OS policy assignments. You must specify the project numbers, the unique numeric ID of the projects.

**Example**
    
    gcloud --billing-project=my-quota-project compute os-config policy-orchestrators create my-os-policy-orchestrator \
          --folder=123456 \
          --policy-type=os_policy_assignment_v1 \
          --policy-file=/downloads/assignment-config.yaml \
          --policy-id=policy-123 \
          --include-projects=87654321,4567890
    




###  REST 

To create a policy orchestrator, complete the following steps:

  1. Create or download an OS policy assignment file. This file must be in JSON format. For more information about creating OS policy assignments or to view sample OS policy assignments, see [OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy-assignment).

  2. Depending on the scope at which you are creating the policy orchestrator, use one of the following methods:

Send a `POST` request to the [`folders.locations.global.policyOrchestrators.create` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/create).

In the request body, paste the OS policy assignment specifications from the previous step.
         
         POST https://osconfig.googleapis.com/v2/folders/FOLDER_NUMBER/locations/global/policyOrchestrators
         -H "x-goog-user-project: QUOTA_PROJECT_ID"
         
         {
           JSON_OS_POLICY_ORCHESTRATOR
         }
         

Replace the following:

     * `QUOTA_PROJECT_ID`: the project ID of [the quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
     * `FOLDER_NUMBER`: the numeric ID of the folder in which you want to create the policy orchestrator.
     * `JSON_OS_POLICY_ORCHESTRATOR`: the policy orchestrator object in JSON format that defines the orchestrator scope, orchestrated resource, and orchestration state. For more information about the parameters and format, see [`Resource: folders.locations.global.policyOrchestrators`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator).

**Example 1: Create an OS policy assignment that installs a Windows MSI file**

To create an OS policy assignment that installs a Windows MSI downloaded from a Cloud Storage bucket by using the [Sample OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#example-policy-assignment), complete the following steps:

     1. Convert the sample to a JSON file.
     2. Make the following request:
            
            POST https://osconfig.googleapis.com/v2/folders/123456/locations/global/policyOrchestrators \
            -H "x-goog-user-project: my-quota-project
            
            {
            "action": "UPSERT",
            "orchestratedResource": {
              "osPolicyAssignmentV1Payload": {
                "instanceFilter": {
                  "inventories": [
                    {
                      "osShortName": "windows"
                    }
                  ]
                },
                "osPolicies": [
                {
                  "id": "install-msi-policy",
                  "mode": "ENFORCEMENT",
                  "resourceGroups": [
                    {
                      "resources": [
                        {
                          "id": "install-msi",
                          "pkg": {
                            "desiredState": "INSTALLED",
                            "msi": {
                              "source": {
                                "gcs": {
                                  "bucket": "my-bucket",
                                  "generation": "1619136883923956",
                                  "object": "my-app.msi"
                                }
                              }
                            }
                          }
                        }
                      ]
                    }
                  ]
                }
                ],
                "rollout": {
                  "disruptionBudget": {
                    "fixed": 10
                  },
                  "minWaitDuration": "300s"
                }
              }
            },
            "orchestrationScope": {
            "selectors": [
              {
                 "resourceHierarchySelector": {
                    "includedProjects": [
                    "projects/87654321",
                    "projects/4567890"
                    ]
                  }
                }
              ]
            },
            "state": "ACTIVE"
            }
            

**Example 2: Roll out an OS policy assignment to specific projects and zones**

Specify `resourceHierarchySelector` and `locationSelector` as separate entries in the `selectors` list:
    
    POST https://osconfig.googleapis.com/v2/folders/123456/locations/global/policyOrchestrators \
      -H "x-goog-user-project: my-quota-project"
    
      {
        "action": "UPSERT",
        "orchestratedResource": {
          "osPolicyAssignmentV1Payload": {
            "instanceFilter": {
              "inventories": [
                {
                  "osShortName": "windows"
                }
              ]
            },
            "osPolicies": [
              {
                "id": "install-msi-policy",
                "mode": "ENFORCEMENT",
                "resourceGroups": [
                  {
                    "resources": [
                      {
                        "id": "install-msi",
                        "pkg": {
                          "desiredState": "INSTALLED",
                          "msi": {
                            "source": {
                              "gcs": {
                                "bucket": "my-bucket",
                                "generation": "1619136883923956",
                                "object": "my-app.msi"
                              }
                            }
                          }
                        }
                      }
                    ]
                  }
                ]
              }
            ],
            "rollout": {
              "disruptionBudget": {
                "fixed": 10
              },
              "minWaitDuration": "300s"
            }
          }
        },
        "orchestrationScope": {
          "selectors": [
            {
              "resourceHierarchySelector": {
                "includedProjects": [
                  "projects/87654321",
                  "projects/4567890"
                ]
              }
            },
            {
              "locationSelector": {
                "includedLocations": [
                  "us-central1-a",
                  "us-east1-b"
                ]
              }
            }
          ]
        },
        "state": "ACTIVE"
      }
    




###  Organization 

###  Console 

To create a policy orchestrator and to apply OS policy assignments in a organization, do the following:

  1. On your local client, create or download an OS policy file. This file must be a JSON or YAML file. For more information about creating OS policies or to view sample OS policies, see [OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy).
  2. In the Google Cloud console, go to the **OS policies** page. 

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  3. Click the **Project Selector** on the Google Cloud console action bar and select the organization in which you want to create the policy orchestrator.
  4. Click **Create global**.
  5. Specify a name and description for the policy orchestrator. For more information on naming conventions, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format). VM Manager assigns a unique orchestrator ID to the policy orchestrator. You can edit this ID if required.
  6. In the **OS policies** section, upload the OS policy file.
  7. Optional: In the **State** section, select one of the following options to specify the behavior of the policy orchestrator: 
     * `ACTIVE`: In this state, the policy orchestrator can take actions as soon as it's created.
     * `STOPPED`: A policy orchestrator that's created in this state does not take any actions immediately. You can edit the policy orchestrator later to change its state.
  8. In the **Action** field, select the **UPSERT** action.
  9. In the **Orchestration scope** section, specify the folders and projects in which you want to roll out the OS policies. You must enter only the project numbers and folder numbers in these fields, for example, `123456,7654321`.
  10. Select the zones that contain the VMs that you want to apply the OS policies to. Alternatively, click **Select all** to apply the OS policy changes to resources in all zones.
  11. Optional: In the **Target VM instances** section, specify the target VMs that you want to apply the OS policies to. 
     * Select the OS name and version. For more information, see [OS policy assignments](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy-assignment).
     * You can further filter the VMs by specifying include and exclude labels. 

For example, you can select all the Ubuntu VMs in your test environment, and exclude those that are running Google Kubernetes Engine, by specifying the following: 

       * OS short name: `ubuntu`
       * Include: `env:test`, `env:staging`
       * Exclude: `goog-gke-node`
  12. Specify a rollout plan for the OS policy assignment. 
     * Specify the wave size (also referred to as the disruption budget). For example, 10%.
     * Specify the wait time. For example, 15 minutes.
  13. Click **Create**.



###  gcloud 

To create a policy orchestrator, complete the following steps:

  1. Create or download an OS policy assignment resource in JSON or YAML format. For more information about this file and sample policy assignments, see [OS policy assignments](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy-assignment).

  2. Use the [`os-config policy-orchestrators create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create) to create and roll out the OS policy assignment in the specified scope.
         
         gcloud --billing-project=QUOTA_PROJECT_ID compute os-config policy-orchestrators create ORCHESTRATOR_NAME \
             --organization=ORGANIZATION_NUMBER \
             --policy-type=os_policy_assignment_v1 \
             --policy-file=OS_POLICY_ASSIGNMENT_YAML_FILE \
             --policy-id=POLICY_ID \
             --include-projects=PROJECT_NUMBERS
         

Replace the following:

     * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
     * `ORCHESTRATOR_NAME`: name for the policy orchestrator. See [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
     * `FOLDER_NUMBER`: the folder number of the folder in which you want to create the policy orchestrator.
     * `OS_POLICY_ASSIGNMENT_FILE`: the absolute path to the OS policy assignment file that you created in the previous step.
     * `POLICY_ID`: a unique ID for the policy orchestrator. If you don't specify a value, policy orchestrator assigns a unique ID for the orchestrator resource.
     * `PROJECT_NUMBERS`: a list of projects for which you want to apply the OS policy assignments. You must specify the project numbers, the unique numeric ID of the projects.

**Example**
    
    gcloud --billing-project=my-quota-project compute os-config policy-orchestrators create my-os-policy-orchestrator \
          --organization=123456 \
          --policy-type=os_policy_assignment_v1 \
          --policy-file=/downloads/assignment-config.yaml \
          --policy-id=policy-123 \
          --include-projects=87654321,4567890
    




###  REST 

To create a policy orchestrator, complete the following steps:

  1. Create or download an OS policy assignment file. This file must be a JSON file. For more information about creating OS policy assignments or to view sample OS policy assignments, see [OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy-assignment).

  2. Depending on the scope at which you are creating the policy orchestrator, use one of the following methods:

Send a `POST` request to the [`organizations.locations.global.policyOrchestrators.create` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/create).

In the request body, paste the OS policy assignment specifications from the previous step.
         
         POST https://osconfig.googleapis.com/v2/organizations/ORGANIZATION_NUMBER/locations/global/policyOrchestrators \
         -H "x-goog-user-project: QUOTA_PROJECT_ID"
         
           {
               JSON_OS_POLICY_ORCHESTRATOR
           }
         

Replace the following:

     * `QUOTA_PROJECT_ID`: the project ID of [the quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
     * `ORGANIZATION_NUMBER`: the numeric ID of the organization in which you want to create the policy orchestrator.
     * `JSON_OS_POLICY_ORCHESTRATOR`: the policy orchestrator object in JSON format that defines the orchestrator scope, orchestrated resource, and orchestration state. For more information about the parameters and format, see [`Resource: organizations.locations.global.policyOrchestrators`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators#PolicyOrchestrator).

**Example 1: Create an OS policy assignment that installs a Windows MSI file**

Convert the [Sample OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#example-policy-assignment) to JSON and send the following request:
    
    POST https://osconfig.googleapis.com/v2/organizations/567890/locations/global/policyOrchestrators   
    
        -H "x-goog-user-project: my-quota-project
        {
        "action": "UPSERT",
        "orchestratedResource": {
          "osPolicyAssignmentV1Payload": {
            "instanceFilter": {
              "inventories": [
                {
                  "osShortName": "windows"
                }
              ]
            },
            "osPolicies": [
            {
              "id": "install-msi-policy",
              "mode": "ENFORCEMENT",
              "resourceGroups": [
                {
                  "resources": [
                    {
                      "id": "install-msi",
                      "pkg": {
                        "desiredState": "INSTALLED",
                        "msi": {
                          "source": {
                            "gcs": {
                              "bucket": "my-bucket",
                              "generation": "1619136883923956",
                              "object": "my-app.msi"
                            }
                          }
                        }
                      }
                    }
                  ]
                }
              ]
            }
            ],
            "rollout": {
              "disruptionBudget": {
                "fixed": 10
              },
              "minWaitDuration": "300s"
            }
          }
      },
      "orchestrationScope": {
        "selectors": [
          {
             "resourceHierarchySelector": {
                "includedProjects": [
                "projects/87654321",
                "projects/4567890"
                ]
              }
            }
          ]
       },
        "state": "ACTIVE"
      }
    

**Example 2: Roll out an OS policy assignment to specific projects and zones**

Specify `resourceHierarchySelector` and `locationSelector` as separate entries in the `selectors` list:
    
    POST https://osconfig.googleapis.com/v2/organizations/567890/locations/global/policyOrchestrators \
      -H "x-goog-user-project: my-quota-project"
    
      {
        "action": "UPSERT",
        "orchestratedResource": {
          "osPolicyAssignmentV1Payload": {
            "instanceFilter": {
              "inventories": [
                {
                  "osShortName": "windows"
                }
              ]
            },
            "osPolicies": [
              {
                "id": "install-msi-policy",
                "mode": "ENFORCEMENT",
                "resourceGroups": [
                  {
                    "resources": [
                      {
                        "id": "install-msi",
                        "pkg": {
                          "desiredState": "INSTALLED",
                          "msi": {
                            "source": {
                              "gcs": {
                                "bucket": "my-bucket",
                                "generation": "1619136883923956",
                                "object": "my-app.msi"
                              }
                            }
                          }
                        }
                      }
                    ]
                  }
                ]
              }
            ],
            "rollout": {
              "disruptionBudget": {
                "fixed": 10
              },
              "minWaitDuration": "300s"
            }
          }
        },
        "orchestrationScope": {
          "selectors": [
            {
              "resourceHierarchySelector": {
                "includedProjects": [
                  "projects/87654321",
                  "projects/4567890"
                ]
              }
            },
            {
              "locationSelector": {
                "includedLocations": [
                  "us-central1-a",
                  "us-east1-b"
                ]
              }
            }
          ]
        },
        "state": "ACTIVE"
      }
    




## Delete OS policy assignments from multiple projects

You can use policy orchestrator to delete OS policies from multiple projects in your folder or organization by specifying the unique policy ID for the OS policy resource.

###  Project 

###  Console 

To delete OS policy assignments in a project, do the following:

  1. On your local client, create or download an OS policy file. This file must be a JSON or YAML file. For more information about creating OS policies or to view sample OS policies, see [ OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy).
  2. In the Google Cloud console, go to the **OS policies** page. 

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  3. Click the **Project Selector** on the Google Cloud console action bar and select the project from which you want to delete OS policy assignments.
  4. Click **Create global**.
  5. Specify a name and description for the policy orchestrator. See [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format). VM Manager assigns a unique orchestrator ID to the policy orchestrator. You can edit this ID if required.
  6. In the **OS policies** section, select and upload the OS policy file that you want to delete.
  7. Optional: In the **State** section, select one of the following options to specify the behavior of the policy orchestrator: 
     * `ACTIVE`: In this state, the policy orchestrator can take actions as soon as it's created.
     * `STOPPED`: A policy orchestrator that's created in this state does not take any actions immediately. You can edit the policy orchestrator later to change its state.
  8. In the **Action** field, select the **DELETE** action.
  9. In the **Orchestration scope** section, specify the folders and projects from which you want to delete the OS policy assignments. You must enter only the project numbers and folder numbers in these fields, for example, `123456,7654321`.
  10. Select the zones that contain the VMs from which you want to delete OS policy assignments.
  11. Optional: In the **Target VM instances** section, specify the target VMs from which you want to delete OS policy assignments. 
     * Select the OS families.
     * You can further filter the VMs by specifying include and exclude labels. 

For example, you can select all the Ubuntu VMs in your test environment, and exclude those that are running Google Kubernetes Engine, by specifying the following: 

       * OS short name: `ubuntu`
       * Include: `env:test`, `env:staging`
       * Exclude: `goog-gke-node`
  12. Specify a rollout plan for deleting the OS policy assignment. 
     * Specify the wave size (also referred to as the disruption budget). For example, 10%.
     * Specify the wait time. For example, 15 minutes.
  13. Click **Create**.



###  gcloud 

To delete OS policies from multiple projects using a policy orchestrator, use the [`os-config policy-orchestrators create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create) and specify the action as `delete` for the `policy-id` associated with the OS policy assignment.
    
    
        gcloud compute os-config policy-orchestrators create ORCHESTRATOR_NAME \
          --policy-type=os_policy_assignment_v1 \
          --policy-file=OS_POLICY_ASSIGNMENT_FILE \
          --policy-id=POLICY_ID \
          --action=delete
    

Replace the following:

  * `ORCHESTRATOR_NAME`: name of the policy orchestrator.
  * `OS_POLICY_ASSIGNMENT_FILE`: the absolute path to the OS policy assignment file.
  * `POLICY_ID`: the policy ID for the OS policy orchestrator resource.



**Example**
    
    
       gcloud compute os-config policy-orchestrators create my-os-policy-orchestrator \
         --policy-type=os_policy_assignment_v1
         --policy-id=my-policy \
         --action=delete
    

###  REST 

To create a policy orchestrator that deletes OS policies from multiple projects, use one of the following methods and specify the action as `DELETE`:

Send a `POST` request to [`projects.locations.global.policyOrchestrators.create` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.global.policyOrchestrators/create).

In the request body, specify the policy ID associated with the OS policy assignment.
    
    
      POST https://osconfig.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/policyOrchestrators
    
        {
            JSON_OS_POLICY_ORCHESTRATOR
        }
      

Replace the following:

  * `PROJECT_NUMBER`: the numeric ID of the project in which you want to create the policy orchestrator.
  * `JSON_OS_POLICY_ORCHESTRATOR`: the policy orchestrator object in JSON format that defines the orchestrator scope, orchestrated resource, and orchestration state. For more information about the parameters and format, see [`Resource: folders.locations.global.policyOrchestrators`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator).

**Example**
        
        POST https://osconfig.googleapis.com/v2/projects/567890/locations/global/policyOrchestrators
        
        {
          "action": "DELETE",
          "orchestratedResource": {
            "id": "my-policy",
            "osPolicyAssignmentV1Payload": {}
          },
          "orchestrationScope": {
            "selectors": [
              {
                "resourceHierarchySelector": {
                  "includedProjects": [
                    "projects/87654321",
                    "projects/4567890"
                  ]
                }
              }
            ]
          },
          "state": "ACTIVE"
        }
        




###  Folder 

###  Console 

To delete OS policy assignments in a folder, do the following:

  1. On your local client, create or download an OS policy file. This file must be a JSON or YAML file. For more information about creating OS policies or to view sample OS policies, see [ OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy).
  2. In the Google Cloud console, go to the **OS policies** page. 

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  3. Click the **Project Selector** on the Google Cloud console action bar and select the folder from which you want to delete OS policy assignments.
  4. Click **Create global**.
  5. Specify a name and description for the policy orchestrator. See [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format). VM Manager assigns a unique orchestrator ID to the policy orchestrator. You can edit this ID if required.
  6. In the **OS policies** section, select and upload the OS policy file that you want to delete.
  7. Optional: In the **State** section, select one of the following options to specify the behavior of the policy orchestrator: 
     * `ACTIVE`: In this state, the policy orchestrator can take actions as soon as it's created.
     * `STOPPED`: A policy orchestrator that's created in this state does not take any actions immediately. You can edit the policy orchestrator later to change its state.
  8. In the **Action** field, select the **DELETE** action.
  9. In the **Orchestration scope** section, specify the folders and projects from which you want to delete the OS policy assignments. You must enter only the project numbers and folder numbers in these fields, for example, `123456,7654321`.
  10. Select the zones that contain the VMs from which you want to delete OS policy assignments.
  11. Optional: In the **Target VM instances** section, specify the target VMs from which you want to delete OS policy assignments. 
     * Select the OS families.
     * You can further filter the VMs by specifying include and exclude labels. 

For example, you can select all the Ubuntu VMs in your test environment, and exclude those that are running Google Kubernetes Engine, by specifying the following: 

       * OS short name: `ubuntu`
       * Include: `env:test`, `env:staging`
       * Exclude: `goog-gke-node`
  12. Specify a rollout plan for deleting the OS policy assignment. 
     * Specify the wave size (also referred to as the disruption budget). For example, 10%.
     * Specify the wait time. For example, 15 minutes.
  13. Click **Create**.



###  gcloud 

To delete OS policies from multiple projects using a policy orchestrator, use the [`os-config policy-orchestrators create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create) and specify the action as `delete` for the `policy-id` associated with the OS policy assignment.
    
    
        gcloud --billing-project=QUOTA_PROJECT_ID compute os-config policy-orchestrators create ORCHESTRATOR_NAME \
          --policy-type=os_policy_assignment_v1 \
          --policy-id=POLICY_ID \
          --action=delete
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of [the quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
  * `ORCHESTRATOR_NAME`: name of the policy orchestrator.
  * `FOLDER_NUMBER`: the numeric ID of the folder from which you want to delete the OS policy resources.
  * `POLICY_ID`: the policy ID for the OS policy orchestrator resource.



**Example**
    
    
      gcloud --billing-project=my-quota-project compute os-config policy-orchestrators create my-os-policy-orchestrator \
        --folder=123456 \
        --policy-type=os_policy_assignment_v1 \
        --policy-id=my-policy \
        --action=delete
    

###  REST 

To create a policy orchestrator that deletes OS policies from multiple projects, use one of the following methods and specify the action as `DELETE`:

Send a `POST` request to the [`folders.locations.global.policyOrchestrators.create` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/create).

In the request body, specify the policy ID associated with the OS policy assignment.
    
    
     POST https://osconfig.googleapis.com/v2/folders/FOLDER_NUMBER/locations/global/policyOrchestrators
    -H "x-goog-user-project: QUOTA_PROJECT_ID"
    
     {
        JSON_OS_POLICY_ORCHESTRATOR
     }
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of [the quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
  * `FOLDER_NUMBER`: the numeric ID of the folder from which you want to delete the OS policy resources.
  * `JSON_OS_POLICY_ORCHESTRATOR`: the policy orchestrator object in JSON format that defines the policy id, orchestrator scope, orchestrated resource, and orchestration state. For more information about the parameters and format, see [`Resource: folders.locations.global.policyOrchestrators`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator).



**Example**

For example, to delete OS policy resources from multiple projects, make the following request:
    
    
       POST https://osconfig.googleapis.com/v2/folders/567890/locations/global/policyOrchestrators
       -H "x-goog-user-project: my-quota-project
    
    
    
    {
          "action": "DELETE",
          "orchestratedResource": {
            "id": "my-policy",
            "osPolicyAssignmentV1Payload": {}
          },
          "orchestrationScope": {
            "selectors": [
              {
                "resourceHierarchySelector": {
                  "includedProjects": [
                    "projects/87654321",
                    "projects/4567890"
                  ]
                }
              }
            ]
          },
          "state": "ACTIVE"
        }
     

###  Organization 

###  Console 

To delete OS policy assignments in a organization, do the following:

  1. On your local client, create or download an OS policy file. This file must be a JSON or YAML file. For more information about creating OS policies or to view sample OS policies, see [ OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy).
  2. In the Google Cloud console, go to the **OS policies** page. 

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  3. Click the **Project Selector** on the Google Cloud console action bar and select the organization from which you want to delete OS policy assignments.
  4. Click **Create global**.
  5. Specify a name and description for the policy orchestrator. See [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format). VM Manager assigns a unique orchestrator ID to the policy orchestrator. You can edit this ID if required.
  6. In the **OS policies** section, select and upload the OS policy file that you want to delete.
  7. Optional: In the **State** section, select one of the following options to specify the behavior of the policy orchestrator: 
     * `ACTIVE`: In this state, the policy orchestrator can take actions as soon as it's created.
     * `STOPPED`: A policy orchestrator that's created in this state does not take any actions immediately. You can edit the policy orchestrator later to change its state.
  8. In the **Action** field, select the **DELETE** action.
  9. In the **Orchestration scope** section, specify the folders and projects from which you want to delete the OS policy assignments. You must enter only the project numbers and folder numbers in these fields, for example, `123456,7654321`.
  10. Select the zones that contain the VMs from which you want to delete OS policy assignments.
  11. Optional: In the **Target VM instances** section, specify the target VMs from which you want to delete OS policy assignments. 
     * Select the OS families.
     * You can further filter the VMs by specifying include and exclude labels. 

For example, you can select all the Ubuntu VMs in your test environment, and exclude those that are running Google Kubernetes Engine, by specifying the following: 

       * OS short name: `ubuntu`
       * Include: `env:test`, `env:staging`
       * Exclude: `goog-gke-node`
  12. Specify a rollout plan for deleting the OS policy assignment. 
     * Specify the wave size (also referred to as the disruption budget). For example, 10%.
     * Specify the wait time. For example, 15 minutes.
  13. Click **Create**.



###  gcloud 

To delete OS policies from multiple projects using a policy orchestrator, use the [`os-config policy-orchestrators create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/create) and specify the action as `delete` for the `policy-id` associated with the OS policy assignment.
    
    
      gcloud --billing-project=QUOTA_PROJECT_ID compute os-config policy-orchestrators create ORCHESTRATOR_NAME \
        --organization=ORGANIZATION_NUMBER \
        --policy-type=os_policy_assignment_v1 \
        --policy-id=POLICY_ID \
        --action=delete
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of [the quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
  * `ORCHESTRATOR_NAME`: name of the policy orchestrator.
  * `ORGANIZATION_NUMBER`: the numeric ID of the organization from which you want to delete the OS policy resources.
  * `POLICY_ID`: the policy ID for the OS policy orchestrator resource.



**Example**
    
    
      gcloud --billing-project=my-quota-project compute os-config policy-orchestrators create my-os-policy-orchestrator \
        --organization=987654321
        --policy-type=os_policy_assignment_v1
        --policy-id=my-policy \
        --action=delete
    

###  REST 

To create a policy orchestrator that deletes OS policies from multiple projects, use one of the following methods and specify the action as `DELETE`:

Send a `POST` request to the [`organizations.locations.global.policyOrchestrators.create` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/create).

In the request body, specify the policy ID associated with the OS policy assignment.
    
    
     POST https://osconfig.googleapis.com/v2/organizations/ORGANIZATION_NUMBER/locations/global/policyOrchestrators
    -H "x-goog-user-project: QUOTA_PROJECT_ID"
    
    {
        JSON_OS_POLICY_ORCHESTRATOR
    }
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of [the quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
  * `ORGANIZATION_NUMBER`: the numeric ID of the organization from which you want to delete the OS policy resources.
  * `JSON_OS_POLICY_ORCHESTRATOR`: the policy orchestrator object in JSON format that defines the policy id, orchestrator scope, orchestrated resource, and orchestration state. For more information about the parameters and format, see [`Resource: organizations.locations.global.policyOrchestrators`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator).



**Example**

For example, to delete OS policy resources from multiple projects, send the following request:
    
    
      POST https://osconfig.googleapis.com/v2/organizations/567890/locations/global/policyOrchestrators
      -H "x-goog-user-project: my-quota-project
    
    
    
    {
          "action": "DELETE",
          "orchestratedResource": {
            "id": "my-policy",
            "osPolicyAssignmentV1Payload": {}
          },
          "orchestrationScope": {
            "selectors": [
              {
                "resourceHierarchySelector": {
                  "includedProjects": [
                    "projects/87654321",
                    "projects/4567890"
                  ]
                }
              }
            ]
          },
          "state": "ACTIVE"
        }
     

## What's next?

  * [Manage OS policy assignments](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/manage-os-policy).
  * [Troubleshoot VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/troubleshooting/troubleshoot-vm-manager)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

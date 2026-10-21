---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-recommender/
title: Integrate Recommender with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:50.918593+00:00
---

# Integrate Recommender with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-recommender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Recommender with Google SecOps

This document explains how to integrate Recommender with Google Security Operations.

## Before you begin

Before you configure the **Recommender** integration in the Google SecOps platform, verify that you have the following:

  * **Custom Identity and Access Management role**: A role containing the specific permissions required to view and update recommendations across projects or organizations.

  * **Authentication method**: Choose between the recommended Workload Identity (keyless) method or a service account JSON key.

  * **API service roots** : Access to the endpoints for the Recommender API and Cloud Resource Manager API.




### Custom IAM role permissions

Create a custom role in the Google Cloud console and assign it the permissions required for the integration to function correctly.

  1. In the Google Cloud console, go to **IAM & Admin > Roles** page.

[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

  2. Click **Create role**.

  3. Enter a **Title** , **Description** , and a unique **ID** for the role.

  4. Set the **Role Launch Stage** to `General Availability`.

  5. Click **Add permissions** and add the following:

     * **Recommender API** :

       * `recommender.iamPolicyInsights.get`
       * `recommender.iamPolicyInsights.list`
       * `recommender.iamPolicyRecommendations.get`
       * `recommender.iamPolicyRecommendations.list`
       * `recommender.iamPolicyRecommendations.update`
     * **Cloud Resource Manager API** :

       * `resourcemanager.projects.get`
       * `resourcemanager.projects.list`
       * `resourcemanager.projects.getIamPolicy`
       * `resourcemanager.projects.setIamPolicy`
     * **Location access** :

       * `recommender.locations.get`
       * `recommender.locations.list`
     * **Additional resource access** :

       * `resourcemanager.folders.get`
       * `resourcemanager.folders.getIamPolicy`
       * `resourcemanager.folders.setIamPolicy`
       * `resourcemanager.organizations.get`
       * `resourcemanager.organizations.getIamPolicy`
       * `resourcemanager.organizations.setIamPolicy`
  6. Click **Create**.




### Authentication configuration

Google SecOps supports two authentication paths. Configure one of the following methods:

  * **Option 1:Workload Identity (recommended)**: This is the recommended method because it provides a superior security posture by eliminating the need to manage and rotate long-lived JSON keys.

  * **Option 2:Service account JSON key**: Uses a standard JSON key file for authentication. Use this method only if Workload Identity is not available in your environment.




#### Authenticate using Workload Identity (recommended)

This method uses service account impersonation to allow the platform to securely access your resources.

##### Create a target service account:

Before the integration can access your Google Cloud resources, you must create a dedicated service account in your project and assign it the necessary permissions.

  1. In the Google Cloud console, go **IAM & Admin > Service Accounts**.
  2. Click **Create service account**.
  3. Provide a name and ID, then click **Create and continue**.
  4. Under **Grant this service account access to project** , select the **Custom IAM role** created in the previous section.
  5. Click **Done**.
  6. Copy the email address of the service account.



##### Identify your Google SecOps instance identity:

To enable secure impersonation, you must first identify the unique service account identity used by your specific Google SecOps instance.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.
  2. Search for and select the Recommender integration.
  3. Paste the target service account email into `Workload Identity Email`.
  4. Click **Save** and then click **Test**. The test is expected to fail. 
  5. Click close_small to the right of **Test** and search the error message for an email address beginning with `gke-init-python@...` or `soar-python@...`. Copy this unique email.



##### Grant impersonation permissions:

The final step is to grant your instance identity the permission to act as your target service account, allowing it to perform actions without requiring a static key file.

  1. Return to the **IAM & Admin > Service Accounts** in the Google Cloud console.
  2. Select the name of the target service account you created.
  3. Navigate to the **Permissions** tab and click **Grant access**.
  4. In the **New principals** field, paste the email address.
  5. In the **Select a role** field, choose **Service account token creator** (`roles/iam.serviceAccountTokenCreator`).
  6. Click **Save**. Note that it may take a few minutes for this permission to propagate before the connection test succeeds.



#### Authenticate using a service account JSON key

Use this method only if Workload Identity isn't available in your environment.

##### Create a service account:

To use key-based authentication, you must first create a service account in your Google Cloud project to act as the identity for the integration.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.
  2. Click **Create service account**.
  3. Provide a name and ID, then click **Create and continue**.
  4. Under **Grant this service account access to project** , select the **Custom IAM role** you created.
  5. Click **Done**.



##### Generate and save a JSON key:

After creating the service account, you must generate a private JSON key file that contains the credentials required for Google SecOps to sign in.

  1. In **IAM & Admin > Service Accounts**, select the service account you created.
  2. Navigate to the **Keys** tab.
  3. Click **Add key > Create new key**.
  4. Select `JSON` as the key type and click **Create**. The JSON file downloads to your computer.
  5. Copy the entire content of this file and paste it into `User's Service Account` during integration configuration.



## Integration parameters

The **Recommender** integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Required. The API root of the Recommender service. The default value is `https://recommender.googleapis.com/v1/`.  
`Resource Manager API Root` | Required. The API root for the Resource Manager service used to manage project and organization resources. The default value is `https://cloudresourcemanager.googleapis.com/v3/`.  
`Organization ID` | Optional. The unique identifier of the Google Cloud organization to use with the integration.  
`Project ID` | Optional. The Google Cloud project ID to use for retrieving recommendations.  
`Quota Project ID` | Optional. The project ID used for billing and quota purposes. If no value is provided, the project associated with the service account credentials is used.  
`Workload Identity Email` | Optional. The client email address of the service account used for Workload Identity impersonation. **Important:** Don't populate this field if you intend to authenticate using a JSON key, as providing both causes authentication conflicts. To prevent "Permission Denied" errors, grant the **Service Account Token Creator** role to the Google SecOps instance service account on the email provided in this field.  
`User's Service Account` | Optional. The full content of the service account JSON key file. **Important:** To authenticate, you must provide either this field or the `Workload Identity Email`. Don't populate this field if you intend to authenticate using a Workload Identity, as providing both causes authentication conflicts.   
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the Recommender server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

**Note:** Some actions work only with specific recommendations.

### Apply IAM recommendations

Apply the IAM recommendations based on the provided input.

This action works only with the `google.iam.policy.Recommender` recommendations.

#### Entities

The action does not run on entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters  
---  
`IAM Recommendations JSON` | Required. The JSON result of the recommendation. JSON result can be provided as a placeholder from the _List recommendations_ or _Get recommendation_ actions.  
  
#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
Entity insight | N/A  
Insight | N/A  
JSON result | Available  
OOTB widget | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    {
      "applied_recommendations": [
        {
          "name": "projects/PROJECT_ID/locations/global/recommenders/google.iam.policy.Recommender/recommendations/217d3019-bae5-4a52-9968-787fdd546a53",
          "description": "Replace the current role with a smaller role to cover the permissions needed.",
          "lastRefreshTime": "2023-07-28T07:00:00Z",
          "primaryImpact": {
            "category": "SECURITY",
            "securityProjection": {
              "details": {
                "revokedIamPermissionsCount": 610
              }
            }
          },
          "content": {
            "operationGroups": [
              {
                "operations": [
                  {
                    "action": "add",
                    "resourceType": "cloudresourcemanager.googleapis.com/Project",
                    "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
                    "path": "/iamPolicy/bindings/*/members/-",
                    "value": "USER_ID@example.com",
                    "pathFilters": {
                      "/iamPolicy/bindings/*/condition/expression": "",
                      "/iamPolicy/bindings/*/role": "roles/compute.instanceAdmin"
                    }
                  },
                  {
                    "action": "remove",
                    "resourceType": "cloudresourcemanager.googleapis.com/Project",
                    "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
                    "path": "/iamPolicy/bindings/*/members/*",
                    "pathFilters": {
                      "/iamPolicy/bindings/*/condition/expression": "",
                      "/iamPolicy/bindings/*/members/*": "USER_ID@example.com",
                      "/iamPolicy/bindings/*/role": "roles/compute.admin"
                    }
                  }
                ]
              }
            ],
            "overview": {
              "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
              "member": "user:USER_ID@example.com",
              "removedRole": "roles/compute.admin",
              "addedRoles": [
                "roles/compute.instanceAdmin"
              ],
              "minimumObservationPeriodInDays": "0"
            }
          },
          "stateInfo": {
            "state": "SUCCEEDED",
            "stateMetadata": {
              "applied_by": "bulk_apply_by_automated_script-2023-08-11"
            }
          },
          "etag": "\"892d57ee41baa03e\"",
          "recommenderSubtype": "REPLACE_ROLE",
          "associatedInsights": [
            {
              "insight": "projects/PROJECT_ID/locations/global/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID"
            }
          ],
          "priority": "P4"
        },
        {
          "name": "projects/PROJECT_ID/locations/global/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID",
          "description": "Replace the current role with a smaller role to cover the permissions needed.",
          "lastRefreshTime": "2023-07-28T07:00:00Z",
          "primaryImpact": {
            "category": "SECURITY",
            "securityProjection": {
              "details": {
                "revokedIamPermissionsCount": 19
              }
            }
          },
          "content": {
            "operationGroups": [
              {
                "operations": [
                  {
                    "action": "add",
                    "resourceType": "cloudresourcemanager.googleapis.com/Project",
                    "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
                    "path": "/iamPolicy/bindings/*/members/-",
                    "value": "user:USER_ID@example.com",
                    "pathFilters": {
                      "/iamPolicy/bindings/*/condition/expression": "",
                      "/iamPolicy/bindings/*/role": "roles/storage.objectAdmin"
                    }
                  },
                  {
                    "action": "remove",
                    "resourceType": "cloudresourcemanager.googleapis.com/Project",
                    "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
                    "path": "/iamPolicy/bindings/*/members/*",
                    "pathFilters": {
                      "/iamPolicy/bindings/*/condition/expression": "",
                      "/iamPolicy/bindings/*/members/*": "user:USER_ID@example.com",
                      "/iamPolicy/bindings/*/role": "roles/storage.admin"
                    }
                  }
                ]
              }
            ],
            "overview": {
              "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
              "member": "user:USER_ID@example.com",
              "removedRole": "roles/storage.admin",
              "addedRoles": [
                "roles/storage.objectAdmin"
              ],
              "minimumObservationPeriodInDays": "0"
            }
          },
          "stateInfo": {
            "state": "SUCCEEDED",
            "stateMetadata": {
              "applied_by": "bulk_apply_by_automated_script-2023-08-11"
            }
          },
          "etag": "\"af7635ffeb512998\"",
          "recommenderSubtype": "REPLACE_ROLE",
          "associatedInsights": [
            {
              "insight": "projects/PROJECT_ID/locations/global/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID"
            }
          ],
          "priority": "P4"
        }
      ],
      "failed_recommendations": []
    }
    

##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully applied provided IAM recommendations.` | The action is successful.  
`Successfully applied provided IAM recommendation, but some of the recommendations were not applied.` | The action is successful.   
`No provided IAM recommendations were applied.` | Recommendation failed.  
`Error executing action ACTION_NAME.` | The action returned an error.  
  
### Get recommendation

Get a specific recommendation from the Recommender service.

#### Entities

The action does not run on entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters |   
---|---  
`Recommendation name` | Required. Specifies the recommendation name to return. The action accepts multiple values as a comma-separated string. Example of the expected input:
    
    
        projects/projectname/locations/global/recommenders/google.iam.policy.Recommender/recommendations/0f262740-bf4a-4c3d-9573-0da3345cf3f7
          
  
#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
Entity insight | N/A  
Insight | N/A  
JSON result | Available  
OOTB widget | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    [
      {
        "name": "name",
        "description": "This role has not been used during the observation window.",
        "lastRefreshTime": "2023-07-28T07:00:00Z",
        "primaryImpact": {
          "category": "SECURITY",
          "securityProjection": {
            "details": {
              "revokedIamPermissionsCount": 68
            }
          }
        },
        "content": {
          "operationGroups": [
            {
              "operations": [
                {
                  "action": "remove",
                  "resourceType": "cloudresourcemanager.googleapis.com/Project",
                  "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
                  "path": "/iamPolicy/bindings/*/members/*",
                  "pathFilters": {
                    "/iamPolicy/bindings/*/condition/expression": "",
                    "/iamPolicy/bindings/*/members/*": "serviceAccount:SERVICE_ACCOUNT_ID.iam.gserviceaccount.com",
                    "/iamPolicy/bindings/*/role": "roles/monitoring.admin"
                  }
                }
              ]
            }
          ],
          "overview": {
            "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
            "member": "serviceAccount:SERVICE_ACCOUNT_ID.iam.gserviceaccount.com",
            "removedRole": "roles/monitoring.admin",
            "minimumObservationPeriodInDays": "0"
          }
        },
        "stateInfo": {
          "state": "ACTIVE"
        },
        "etag": "",
        "recommenderSubtype": "REMOVE_ROLE",
        "associatedInsights": [
          {
            "insight": "projects/PROJECT_ID/locations/global/insightTypes/google.iam.policy.Insight/insights/"
          }
        ],
        "priority": "P4"
      }
    ]
    

##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully found recommendation in the Google Cloud Recommender service.` | The action is successful.  
`No recommendations were found in the Google Cloud Recommender service.` | Data is not available.  
`Error executing action ACTION_NAME`. | The action returned an error.  
  
### List recommendations

List available recommendations in the Recommender service.

**Note:** The action returns insights only from the `google.iam.policy.Recommender` recommender.

#### Entities

The action does not run on entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters  
---  
`Recommendation Filter` | Optional. Specifies the filter to fetch the recommendations. The parameter should be a string in any of the following formats:

  * `PROJECTS_OR_ORGANIZATIONS`/ `PROJECT_OR_ORGANIZATION_NAME_OR_ID`
  * //cloudresourcemanager.googleapis.com/` PROJECTS_OR_ORGANIZATIONS`/ `PROJECT_OR_ORGANIZATION_NAME_OR_ID`

If no value is provided, the action fetches the project ID from the configured service account.  
`Recommendation Location` | Required. Specifies the Google Cloud location to fetch recommendations. Default is `global`.  
`Recommendation State` | Optional. Specifies the recommendation state to return. Default is `Not Specified`. Possible values are:

  * `Not Specified`
  * `Active`
  * `Dismissed`

  
`Recommendation Priority` | Optional. Specifies the priority of a recommendation to return. Multiple values can be specified as a comma-separated string.  
`Recommender Subtype` | Optional. Specifies the returned recommender subtype. Default is `Not Specified`. Possible values are:

  * `Not Specified`
  * `REMOVE_ROLE`
  * `REPLACE_ROLE`

  
`Max Records To Return` | Optional. Specifies how many records to return. If no value is provided, the action returns 50 records by default.  
  
#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | Available  
Enrichment table | N/A  
Entity insight | N/A  
Insight | N/A  
JSON result | Available  
OOTB widget | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    [
      {
        "name": "name",
        "description": "This role has not been used during the observation window.",
        "lastRefreshTime": "2023-07-27T07:00:00Z",
        "primaryImpact": {
          "category": "SECURITY",
          "securityProjection": {
            "details": {
              "revokedIamPermissionsCount": 68
            }
          }
        },
        "content": {
          "operationGroups": [
            {
              "operations": [
                {
                  "action": "remove",
                  "resourceType": "cloudresourcemanager.googleapis.com/Project",
                  "resource": "//cloudresourcemanager.googleapis.com/projects",
                  "path": "/iamPolicy/bindings/*/members/*",
                  "pathFilters": {
                    "/iamPolicy/bindings/*/condition/expression": "",
                    "/iamPolicy/bindings/*/members/*": "serviceAccount:SERVICE_ACCOUNT_ID",
                    "/iamPolicy/bindings/*/role": "roles/monitoring.admin"
                  }
                }
              ]
            }
          ],
          "overview": {
            "resource": "//cloudresourcemanager.googleapis.com/",
            "member": "serviceAccount:SERVICE_ACCOUNT_ID",
            "removedRole": "roles/monitoring.admin",
            "minimumObservationPeriodInDays": "0"
          }
        },
        "stateInfo": {
          "state": "ACTIVE"
        },
        "etag": "",
        "recommenderSubtype": "REMOVE_ROLE",
        "associatedInsights": [
          {
            "insight": "projects/i/locations/global/insightTypes/"
          }
        ],
        "priority": "P4"
      },
      {
        "name": "name",
        "description": "This role has not been used during the observation window.",
        "lastRefreshTime": "2023-07-27T07:00:00Z",
        "primaryImpact": {
          "category": "SECURITY",
          "securityProjection": {
            "details": {
              "revokedIamPermissionsCount": 5
            }
          }
        },
        "content": {
          "operationGroups": [
            {
              "operations": [
                {
                  "action": "remove",
                  "resourceType": "cloudresourcemanager.googleapis.com/Project",
                  "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
                  "path": "/iamPolicy/bindings/*/members/*",
                  "pathFilters": {
                    "/iamPolicy/bindings/*/condition/expression": "",
                    "/iamPolicy/bindings/*/members/*": "user:USER_ID@example.com",
                    "/iamPolicy/bindings/*/role": "roles/chroniclesm.admin"
                  }
                }
              ]
            }
          ],
          "overview": {
            "resource": "//cloudresourcemanager.googleapis.com/projects",
            "member": "user:USER_ID@example.com",
            "removedRole": "roles/chroniclesm.admin",
            "minimumObservationPeriodInDays": "0"
          }
        },
        "stateInfo": {
          "state": "ACTIVE"
        },
        "etag": "",
        "recommenderSubtype": "REMOVE_ROLE",
        "associatedInsights": [
          {
            "insight": "projects"
          }
        ],
        "priority": "P4"
      }
    ]
    

##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully found recommendations for the provided criteria in the Google Cloud Recommender service.` | The action is successful.  
`No recommendations were found for the provided criteria in the Google Cloud Recommender service.` | No data is available.  
`Error executing action ACTION_NAME.` | The action returned an error.  
  
The action provides the following case wall table:

Available Recommendations  
---  
Columns | 

  * Name
  * Description
  * Category
  * Recommendation Subtype
  * Priority
  * State
  * Last Refresh Time

  
  
### Ping

Test connectivity to the Recommender service with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Entities

The action does not run on entities.

#### Action inputs

N/A

#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
Entity insight | N/A  
Insight | N/A  
JSON result | N/A  
OOTB widget | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Google Cloud Recommender service with the provided connection parameters!` | The action is successful.  
`Failed to connect to the Google Cloud Recommender service!` | The action returned an error.  
  
### Update recommendation

Update the recommendation in the Recommender service.

#### Entities

The action does not run on entities.

#### Action inputs

Use the following parameters to configure the action:

Parameters  
---  
`Recommendation name` | Required. Specifies the recommendation name to update. The action accepts multiple values as a comma-separated string. Example of the expected input: `projects/projectname/locations/global/recommenders/google.iam.policy.Recommender/recommendations/0f262740-bf4a-4c3d-9573-0da3345cf3f7`  
`Recommendation State` | Optional. Specifies the state for the recommendation to change to. Default is `Not Specified`. Possible values are:

  * `Not Specified`
  * `Claimed`
  * `Dismissed`

  
`Recommendation Result` | Optional. Specifies the result for the recommendation to change to. Default is `Not Specified`. Possible values are:

  * `Not Specified`
  * `Failed`
  * `Succeeded`

  
  
#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
Entity insight | N/A  
Insight | N/A  
JSON result | Available  
OOTB widget | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    [
      {
        "name": "name",
        "description": "This role has not been used during the observation window.",
        "lastRefreshTime": "2023-07-28T07:00:00Z",
        "primaryImpact": {
          "category": "SECURITY",
          "securityProjection": {
            "details": {
              "revokedIamPermissionsCount": 68
            }
          }
        },
        "content": {
          "operationGroups": [
            {
              "operations": [
                {
                  "action": "remove",
                  "resourceType": "cloudresourcemanager.googleapis.com/Project",
                  "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
                  "path": "/iamPolicy/bindings/*/members/*",
                  "pathFilters": {
                    "/iamPolicy/bindings/*/condition/expression": "",
                    "/iamPolicy/bindings/*/members/*": "serviceAccount:SERVICE_ACCOUNT_ID.iam.gserviceaccount.com",
                    "/iamPolicy/bindings/*/role": "roles/monitoring.admin"
                  }
                }
              ]
            }
          ],
          "overview": {
            "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
            "member": "serviceAccount:SERVICE_ACCOUNT_ID.iam.gserviceaccount.com",
            "removedRole": "roles/monitoring.admin",
            "minimumObservationPeriodInDays": "0"
          }
        },
        "stateInfo": {
          "state": "ACTIVE"
        },
        "etag": "",
        "recommenderSubtype": "REMOVE_ROLE",
        "associatedInsights": [
          {
            "insight": "projects/PROJECT_ID/locations/global/insightTypes/google.iam.policy.Insight/insights/"
          }
        ],
        "priority": "P4"
      }
    ]
    

##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated recommendation in the Google Cloud Recommender service.` | The action is successful.  
`No recommendations were found in the Google Cloud Recommender service.` | Data is not available.  
`Error executing action ACTION_NAME`. | The action returned an error.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 

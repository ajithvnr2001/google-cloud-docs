---
url: https://docs.cloud.google.com/policy-intelligence/docs/review-apply-organization-policy-recommendations/
title: Review and apply organization policy recommendations \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:42.853952+00:00
---

# Review and apply organization policy recommendations  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/review-apply-organization-policy-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Review and apply organization policy recommendations Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to view, understand, and apply organization policy recommendations. Organization policy recommendations help you set the right organization policies without disrupting systems.

## Before you begin

  * Enable the Organization Policy and Recommender APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=orgpolicy.googleapis.com,recommender.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Set up authentication.

Select the tab for how you plan to use the samples on this page:

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

  * Understand [organization policy recommendations](https://docs.cloud.google.com/policy-intelligence/docs/organization-policy-recommendations-overview).




## Required IAM roles

This section describes the IAM roles and permissions that you need in order to work with organization policy recommendations.

To get the permissions that you need to manage organization policy recommendations, ask your administrator to grant you the following IAM roles on the resource that you want to manage recommendations for (project, folder, or organization): 

  * To view organization policy recommendations: [Org Policy Recommender Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.orgPolicyViewer) (`roles/recommender.orgPolicyViewer`) 
  * To apply and dismiss organization policy recommendations: [Org Policy Recommender Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.orgPolicyAdmin) (`roles/recommender.orgPolicyAdmin`) 
  * To manage organization policies: [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage organization policy recommendations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage organization policy recommendations:

  * To view organization policy recommendations: 
    * `recommender.orgPolicyRecommendations.get`
    * `recommender.orgPolicyRecommendations.list`
  * To apply and dismiss organization policy recommendations: 
    * `recommender.orgPolicyRecommendations.get`
    * `recommender.orgPolicyRecommendations.list`
    * `recommender.orgPolicyRecommendations.update`
    *   * To manage organization policies: 
    * `orgpolicy.policy.get`
    * `orgpolicy.policy.set`
    * `orgpolicy.constraints.list`
    * `orgpolicy.policies.create`
    * `orgpolicy.policies.delete`
    * `orgpolicy.policies.list`
    * `orgpolicy.policies.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

The preview of Organization Policy recommender has the following limitations:

  * Insights are only available for projects, folders, and organizations that have recommendations.

  * Recommendations are only made for constraints that are not configured on a given resource or any of its child resources.




### Supported constraints

Recommendations are only available for the following organization policy constraints:

  * [Service account key creation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_creation) (`iam.managed.disableServiceAccountKeyCreation`)

  * [Service account key upload](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_upload) (`iam.managed.disableServiceAccountKeyUpload`)

  * [Protocol forwarding rules](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints#restrict_the_types_of_protocol_forwarding_deployments) (`compute.managed.restrictProtocolForwardingCreationForTypes`)




## Review and apply recommendations

You can review and apply organization policy recommendations with the Google Cloud CLI and the Recommender API.

### gcloud

**Review your recommendations:**

To list your recommendations, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command:
    
    
    gcloud recommender recommendations list \
        --location=global \
        --recommender=google.orgpolicy.policy.Recommender \
        --RESOURCE_TYPE=RESOURCE_ID \
        --filter="recommenderSubtype:RECOMMENDER_SUBTYPE" \
        --format=FORMAT
    

Replace the following values:

  * `RESOURCE_TYPE`: The resource type that you want to list recommendations for. Use the value `project`, `folder`, or `organization`.

  * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to list recommendations for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.

  * `RECOMMENDER_SUBTYPE`: Optional. The ID of the subtype you want to see recommendations for. Valid subtypes include the following:

    * `ADD_POLICY_DISABLE_SERVICE_ACCOUNT_KEY_CREATION` provides recommendations for the `iam.managed.disableServiceAccountKeyCreation` constraint.
    * `ADD_POLICY_DISABLE_SERVICE_ACCOUNT_KEY_UPLOAD` provides recommendations for the `iam.managed.disableServiceAccountKeyUpload` constraint
  * `FORMAT`: The format of the response. Use the value `json` or `yaml`.




The response is similar to the following example. In this example, two resources are analyzed for external service account keys, and no violations are detected. As a result, the recommendation suggests setting the `iam.managed.disableServiceAccountKeyCreation` to prevent future violations.
    
    
    [
      {
        "associatedInsights": [
          {
            "insight": "projects/123456789012/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights/fb927dc1-9695-4436-0000-f0f285007c0f"
          }
        ],
        "content": {
          "operationGroups": [
            {
              "operations": [
                {
                  "action": "add",
                  "path": "/",
                  "resource": "//orgpolicy.googleapis.com/projects/123456789012/policies/iam.managed.disableServiceAccountKeyCreation",
                  "resourceType": "orgpolicy.googleapis.com/Policy",
                  "value": {
                    "etag": "",
                    "name": "projects/123456789012/policies/iam.managed.disableServiceAccountKeyCreation",
                    "spec": {
                      "etag": "",
                      "inheritFromParent": false,
                      "reset": false,
                      "rules": [
                        {
                          "enforce": true
                        }
                      ]
                    }
                  }
                }
              ]
            }
          ],
          "overview": {
            "constraint": {
              "id": "constraints/iam.managed.disableServiceAccountKeyCreation",
              "name": "Disable service account key creation"
            },
            "enforcedResources": [
              {
                "numOfResources": "2",
                "resourceType": "iam.googleapis.com/ServiceAccountKey"
              },
              {
                "numOfResources": "1",
                "resourceType": "cloudresourcemanager.googleapis.com/Project"
              }
            ]
          }
        },
        "description": "After analyzing 3 resources and finding 0 violations, Organization Policy Recommender recommends that you disable the creation of service account external keys on your project by enforcing constraints/iam.managed.disableServiceAccountKeyCreation.",
        "etag": "\"826e992a0f9793ff\"",
        "lastRefreshTime": "2024-12-07T08:00:00Z",
        "name": "projects/123456789012/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f",
        "primaryImpact": {
          "category": "SECURITY"
        },
        "priority": "P1",
        "recommenderSubtype": "ADD_POLICY_DISABLE_SERVICE_ACCOUNT_KEY_CREATION",
        "stateInfo": {
          "state": "ACTIVE",
          "stateMetadata": {
            "reviewedBy": "alice",
            "priority": "high"
          }
        },
        "targetResources": [
          "//cloudresourcemanager.googleapis.com/projects/123456789012"
        ]
      }
    ]
    

To learn more about the components of a recommendation, see Understanding recommendations.

**To apply a recommendation:**

  1. Use the [`gcloud recommender recommendations mark-claimed`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed) command to change the recommendation's state to `CLAIMED`, which prevents the recommendation from changing while you apply it:
         
         gcloud recommender recommendations mark-claimed \
             RECOMMENDATION_ID \
             --location=global \
             --recommender=google.orgpolicy.policy.Recommender \
             --RESOURCE_TYPE=RESOURCE_ID \
             --format=FORMAT \
             --etag=ETAG \
             --state-metadata=STATE_METADATA
         

Replace the following values:

     * `RECOMMENDATION_ID`: The unique identifier for the recommendation. This value appears at the end of the `name` field in the recommendation. In the preceding example, the identifier is `fb927dc1-9695-4436-0000-f0f285007c0f`. 

     * `RESOURCE_TYPE`: The resource type that you want to manage recommendations for. Use the value `project`, `folder`, or `organization`. 

     * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to list recommendations for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 

     * `FORMAT`: The format of the response. Use the value `json` or `yaml`. 

     * `ETAG`: An identifier for a version of the recommendation, such as `"7caf4103d7669e12"`. Note that this value can include quotes. 

     * `STATE_METADATA`: Optional. Comma-separated key-value pairs that contain your choice of metadata about the recommendation. For example, `--state-metadata=reviewedBy=alice,priority=high`. The metadata replaces the `stateInfo.stateMetadata` field in the recommendation. 

If the command succeeds, the response shows the recommendation in a `CLAIMED` state, as shown in the following example. For clarity, the example omits most fields:
    
      {
        "description": "After analyzing 3 resources and finding 0 violations, Organization Policy Recommender recommends that you disable the creation of service account external keys on your project by enforcing constraints/iam.managed.disableServiceAccountKeyCreation.",
        "etag": "\"826e992a0f9793ff\"",
        "lastRefreshTime": "2024-12-07T08:00:00Z",
        "name": "projects/123456789012/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f",
        "primaryImpact": {
          "category": "SECURITY"
        },
        "priority": "P1",
        "recommenderSubtype": "ADD_POLICY_DISABLE_SERVICE_ACCOUNT_KEY_CREATION",
        **"stateInfo" : {
          "state": "CLAIMED",
          "stateMetadata": {\
            "reviewedBy": "alice",
            "priority": "high"
          }
        },**
        "targetResources": [
          "//cloudresourcemanager.googleapis.com/projects/123456789012"
        ]
      }
    

  2. [Update and apply](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#boolean-constraint) the organization policy for the project, folder, or organization specified by the `RESOURCE_TYPE` and `RESOURCE_ID` so that it reflects the recommendation.

  3. Update the recommendation's state to `SUCCEEDED` if you were able to apply the recommendation, or `FAILED` if you couldn't apply the recommendation:
         
         gcloud recommender recommendations COMMAND \
             RECOMMENDATION_ID \
             --location=global \
             --recommender=google.iam.policy.Recommender \
             --RESOURCE_TYPE=RESOURCE_ID \
             --format=FORMAT \
             --etag=ETAG \
             --state-metadata=STATE_METADATA
         

Replace the following values:

     * `COMMAND`: Use `mark-succeeded` if you successfully applied the recommendation, or `mark-failed` if you couldn't apply the recommendation. 

     * `RECOMMENDATION_ID`: The unique identifier for the recommendation. This value appears at the end of the `name` field in the recommendation. In the preceding example, the identifier is `fb927dc1-9695-4436-0000-f0f285007c0f`. 

     * `RESOURCE_TYPE`: The resource type that you want to manage recommendations for. Use the value `project`, `folder`, or `organization`. 

     * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to list recommendations for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 

     * `FORMAT`: The format of the response. Use the value `json` or `yaml`. 

     * `ETAG`: An identifier for a version of the recommendation, such as `"7caf4103d7669e12"`. Note that this value can include quotes. 

     * `STATE_METADATA`: Optional. Comma-separated key-value pairs that contain your choice of metadata about the recommendation. For example, `--state-metadata=reviewedBy=alice,priority=high`. The metadata replaces the `stateInfo.stateMetadata` field in the recommendation. 

For example, if you marked the recommendation as having succeeded, the response shows the recommendation in a `SUCCEEDED` state. For clarity, this example omits most fields:
    
      {
        "description": "After analyzing 3 resources and finding 0 violations, Organization Policy Recommender recommends that you disable the creation of service account external keys on your project by enforcing constraints/iam.managed.disableServiceAccountKeyCreation.",
        "etag": "\"826e992a0f9793ff\"",
        "lastRefreshTime": "2024-12-07T08:00:00Z",
        "name": "projects/123456789012/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f",
        "primaryImpact": {
          "category": "SECURITY"
        },
        "priority": "P1",
        "recommenderSubtype": "ADD_POLICY_DISABLE_SERVICE_ACCOUNT_KEY_CREATION",
        **"stateInfo" : {
          "state": "SUCCEEDED",
          "stateMetadata": {
            "reviewedBy": "alice",
            "priority": "high"
          }
        },**
        "targetResources": [
          "//cloudresourcemanager.googleapis.com/projects/123456789012"
        ]
      }
    

To revert the changes to the organization policy, [set the organization](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#boolean-constraint) policy to its original configuration, which is provided in the `configuredPolicy` field of the associated insight.




### REST

**Review your recommendations:**

To list all available recommendations for your project, folder, or organization, use the Recommender API's `[recommendations.list](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list)` method. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The type of the resource that you want to manage recommendations for. Use the value `projects`, `folders`, or `organizations`.
  * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to manage recommendations for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `PAGE_SIZE`: Optional. The maximum number of results to return from this request. If not specified, the server will determine the number of results to return. If the number of recommendations is greater than the page size, the response contains a pagination token that you can use to retrieve the next page of results. 
  * `PAGE_TOKEN`: Optional. The pagination token returned in an earlier response from this method. If specified, the list of recommendations will start where the previous request ended.
  * `FILTER`: Optional. A filter expression to restrict the recommendations returned. You can filter recommendations based on the `stateInfo.state` field. For example, `stateInfo.state:"DISMISSED"` or `stateInfo.state:"FAILED"`. 
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    GET https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN&filter=FILTER

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN&filter=FILTER"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN&filter=FILTER" | Select-Object -Expand Content

The response is similar to the following example. In this example, two resources are analyzed for external service account keys, and no violations are detected. As a result, the recommendation suggests setting the `iam.managed.disableServiceAccountKeyCreation` to prevent future violations. 
    
    
    [
      {
        "associatedInsights": [
          {
            "insight": "projects/123456789012/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights/66d543f3-845d-49d6-a26b-80d84804d8a8"
          }
        ],
        "content": {
          "operationGroups": [
            {
              "operations": [
                {
                  "action": "add",
                  "path": "/",
                  "resource": "//orgpolicy.googleapis.com/projects/123456789012/policies/iam.managed.disableServiceAccountKeyCreation",
                  "resourceType": "orgpolicy.googleapis.com/Policy",
                  "value": {
                    "etag": "",
                    "name": "projects/123456789012/policies/iam.managed.disableServiceAccountKeyCreation",
                    "spec": {
                      "etag": "",
                      "inheritFromParent": false,
                      "reset": false,
                      "rules": [
                        {
                          "enforce": true
                        }
                      ]
                    }
                  }
                }
              ]
            }
          ],
          "overview": {
            "constraint": {
              "id": "constraints/iam.managed.disableServiceAccountKeyCreation",
              "name": "Disable service account key creation"
            },
            "enforcedResources": [
              {
                "numOfResources": "2",
                "resourceType": "iam.googleapis.com/ServiceAccountKey"
              },
              {
                "numOfResources": "1",
                "resourceType": "cloudresourcemanager.googleapis.com/Project"
              }
            ]
          }
        },
        "description": "After analyzing 3 resources and finding 0 violations, Organization Policy Recommender recommends that you disable the creation of service account external keys on your project by enforcing constraints/iam.managed.disableServiceAccountKeyCreation.",
        "etag": "\"826e992a0f9793ff\"",
        "lastRefreshTime": "2024-12-07T08:00:00Z",
        "name": "projects/123456789012/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f",
        "primaryImpact": {
          "category": "SECURITY"
        },
        "priority": "P1",
        "recommenderSubtype": "ADD_POLICY_DISABLE_SERVICE_ACCOUNT_KEY_CREATION",
        "stateInfo": {
          "state": "ACTIVE",
          "stateMetadata": {
            "reviewedBy": "alice",
            "priority": "high"
          }
        },
        "targetResources": [
          "//cloudresourcemanager.googleapis.com/projects/123456789012"
        ]
      }
    ]
    

To learn more about the components of a recommendation, see Understanding recommendations.

**To apply a recommendation:**

  1. Mark the recommendation as `CLAIMED`:

To mark a recommendation as `CLAIMED`, which prevents the recommendation from changing while you apply it, use the Recommender API's `[recommendations.markClaimed](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/markClaimed)` method. 

Before using any of the request data, make the following replacements: 

     * `RESOURCE_TYPE`: The type of the resource that you want to manage recommendations for. Use the value `projects`, `folders`, or `organizations`.
     * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to manage recommendations for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
     * `RECOMMENDATION_ID`: The unique identifier for the recommendation. This value appears at the end of the `name` field in the recommendation. For example, if the `name` field is `projects/example-project/locations/global/recommenders/google.iam.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f`, the recommendation ID is `fb927dc1-9695-4436-0000-f0f285007c0f`. 
     * `ETAG`: The value of the `etag` field in the recommendation, such as `"dd0686e7136a4cbb"`. Use backslashes to escape quotes, for example, `"\"df7308cca9719dcc\""`. 
     * `STATE_METADATA`: Optional. An object that contains key-value pairs with your choice of metadata about the recommendation. For example, `{"reviewedBy": "alice", "priority": "high"}`. The metadata replaces the `stateInfo.stateMetadata` field in the recommendation. 
     * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.

HTTP method and URL: 
    
    POST https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/RECOMMENDATION_ID:markClaimed

Request JSON body: 
    
    {
      "etag": "ETAG",
      "stateMetadata": {
        "STATE_METADATA"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/RECOMMENDATION_ID:markClaimed"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/RECOMMENDATION_ID:markClaimed" | Select-Object -Expand Content

The response shows the recommendation in a `CLAIMED` state, as shown in the following example. For clarity, this example omits most fields: 
    
    {
      "description": "After analyzing 3 resources and finding 0 violations, Organization Policy Recommender recommends that you disable the creation of service account external keys on your project by enforcing constraints/iam.managed.disableServiceAccountKeyCreation.",
      "etag": "\"826e992a0f9793ff\"",
      "lastRefreshTime": "2024-12-07T08:00:00Z",
      "name": "projects/123456789012/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f",
      "primaryImpact": {
        "category": "SECURITY"
      },
      "priority": "P1",
      "recommenderSubtype": "ADD_POLICY_DISABLE_SERVICE_ACCOUNT_KEY_CREATION",
      **"stateInfo": {
        "state": "CLAIMED",
        "stateMetadata": {
          "reviewedBy": "alice",
          "priority": "high"
        }
      },**
      "targetResources": [
        "//cloudresourcemanager.googleapis.com/projects/123456789012"
      ]
    }
    

  2. [Update the organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#boolean_constraints) for the project, folder, or organization specified by the `RESOURCE_TYPE` and `RESOURCE_ID` so that it reflects the recommendation.

  3. Update the recommendation's state to `SUCCEEDED` if you successfully applied the recommendation, or `FAILED` if you couldn't apply the recommendation:

### `SUCCEEDED`

To mark a recommendation as `SUCCEEDED`, indicating that you were able to apply it, use the Recommender API's `[recommendations.markSucceeded](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/markSucceeded)` method. 

Before using any of the request data, make the following replacements: 

     * `RESOURCE_TYPE`: The type of the resource that you want to manage recommendations for. Use the value `projects`, `folders`, or `organizations`.
     * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to manage recommendations for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
     * `RECOMMENDATION_ID`: The unique identifier for the recommendation. This value appears at the end of the `name` field in the recommendation. For example, if the `name` field is `projects/example-project/locations/global/recommenders/google.iam.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f`, the recommendation ID is `fb927dc1-9695-4436-0000-f0f285007c0f`. 
     * `ETAG`: The value of the `etag` field in the recommendation, such as `"dd0686e7136a4cbb"`. Use backslashes to escape quotes, for example, `"\"df7308cca9719dcc\""`. 
     * `STATE_METADATA`: Optional. An object that contains key-value pairs with your choice of metadata about the recommendation. For example, `{"reviewedBy": "alice", "priority": "high"}`. The metadata replaces the `stateInfo.stateMetadata` field in the recommendation. 
     * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.

HTTP method and URL: 
    
    POST https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/RECOMMENDATION_ID:markSucceeded

Request JSON body: 
    
    {
      "etag": "ETAG",
      "stateMetadata": {
        "STATE_METADATA"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/RECOMMENDATION_ID:markSucceeded"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/RECOMMENDATION_ID:markSucceeded" | Select-Object -Expand Content

The response shows the recommendation in a `SUCCEEDED` state, as shown in the following example. For clarity, this example omits most fields: 
    
    {
      "description": "After analyzing 3 resources and finding 0 violations, Organization Policy Recommender recommends that you disable the creation of service account external keys on your project by enforcing constraints/iam.managed.disableServiceAccountKeyCreation.",
      "etag": "\"826e992a0f9793ff\"",
      "lastRefreshTime": "2024-12-07T08:00:00Z",
      "name": "projects/123456789012/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f",
      "primaryImpact": {
        "category": "SECURITY"
      },
      "priority": "P1",
      "recommenderSubtype": "ADD_POLICY_DISABLE_SERVICE_ACCOUNT_KEY_CREATION",
      **"stateInfo": {
        "state": "SUCCEEDED",
        "stateMetadata": {
          "reviewedBy": "alice",
          "priority": "high"
        }
      },**
      "targetResources": [
        "//cloudresourcemanager.googleapis.com/projects/123456789012"
      ]
    }
    

### `FAILED`

To mark a recommendation as `FAILED`, indicating that you were not able to apply it, use the Recommender API's `[recommendations.markFailed](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/markFailed)` method. 

Before using any of the request data, make the following replacements: 

     * `RESOURCE_TYPE`: The type of the resource that you want to manage recommendations for. Use the value `projects`, `folders`, or `organizations`.
     * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to manage recommendations for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
     * `RECOMMENDATION_ID`: The unique identifier for the recommendation. This value appears at the end of the `name` field in the recommendation. For example, if the `name` field is `projects/example-project/locations/global/recommenders/google.iam.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f`, the recommendation ID is `fb927dc1-9695-4436-0000-f0f285007c0f`. 
     * `ETAG`: The value of the `etag` field in the recommendation, such as `"dd0686e7136a4cbb"`. Use backslashes to escape quotes, for example, `"\"df7308cca9719dcc\""`. 
     * `STATE_METADATA`: Optional. An object that contains key-value pairs with your choice of metadata about the recommendation. For example, `{"reviewedBy": "alice", "priority": "high"}`. The metadata replaces the `stateInfo.stateMetadata` field in the recommendation. 
     * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.

HTTP method and URL: 
    
    POST https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/RECOMMENDATION_ID:markFailed

Request JSON body: 
    
    {
      "etag": "ETAG",
      "stateMetadata": {
        "STATE_METADATA"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/RECOMMENDATION_ID:markFailed"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/RECOMMENDATION_ID:markFailed" | Select-Object -Expand Content

The response shows the recommendation in a `FAILED` state, as shown in the following example. For clarity, this example omits most fields: 
    
    {
      "description": "After analyzing 3 resources and finding 0 violations, Organization Policy Recommender recommends that you disable the creation of service account external keys on your project by enforcing constraints/iam.managed.disableServiceAccountKeyCreation.",
      "etag": "\"826e992a0f9793ff\"",
      "lastRefreshTime": "2024-12-07T08:00:00Z",
      "name": "projects/123456789012/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f",
      "primaryImpact": {
        "category": "SECURITY"
      },
      "priority": "P1",
      "recommenderSubtype": "ADD_POLICY_DISABLE_SERVICE_ACCOUNT_KEY_CREATION",
      **"stateInfo": {
        "state": "FAILED",
        "stateMetadata": {
          "reviewedBy": "alice",
          "priority": "high"
        }
      },**
      "targetResources": [
        "//cloudresourcemanager.googleapis.com/projects/123456789012"
      ]
    }
    




## Understanding recommendations

Each recommendation includes information to help you understand why the recommendation was made, and suggestions for changes to your organization policy configuration. Its core attributes include:

  * `description`: A human-readable summary of the recommendation.

  * `recommenderSubtype`: The identifier for a subtype of recommendations. Each constraint has a unique `recommenderSubtype`.

  * `content`: Contains the recommended changes to your organization policy.

    * `overview`: the condensed overview information about the recommendation.

    * `constraint`: provides information about the constraint.

    * `enforced_resources`: provides information about the resources this organization policy affects if you apply the recommendation.

    * `operationGroups`: a set of one or more operations on the org policy when you apply a recommendation.

  * `associatedInsights`: the resource name of insights that led to this recommendation.




For more information about the attributes of a recommendation, see the [recommendation reference](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations#resource-recommendation).

Insights and recommendations are generated for resources that don't have one of the supported organization policies set on it or any of its child resources. To see the organization policy configuration that this recommendation is based on, view the [organization policy insights](https://docs.cloud.google.com/policy-intelligence/docs/organization-policy-recommendations-overview#how-insights-are-generated) that are associated with the recommendation. These insights are listed in the `associatedInsights` field. To view an organization policy insight that is associated with the recommendation, do the following:

  1. Identify which insights in the `associatedInsights` field are organization policy insights. Organization policy insights have the insight type `google.orgpolicy.policy.Insight`. This type appears after `insightTypes` in the `insight` field.

  2. Copy the organization policy insight's ID. The ID is everything after `insights/` in the `insight` field. For example, if the insight field reads `projects/123456789012/locations/us/insightTypes/google.orgpolicy.policy.Insight/insights/fb927dc1-9695-4436-0000-f0f285007c0f`, then the insight ID is `fb927dc1-9695-4436-0000-f0f285007c0f`.

  3. Follow the instructions to get an [organization policy insight](https://docs.cloud.google.com/policy-intelligence/docs/organization-policy-insights), using the insight ID you copied.




## Export recommendations to BigQuery

To view daily snapshots of all recommendations for your organization, including organization policy recommendations, you can export your recommendations to BigQuery.

To export your recommendations to BigQuery, you need to set up a data transfer using BigQuery Data Transfer Service. To learn how to set up a data transfer, see [Export recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).

## What's next

  * Learn more about [Recommender](https://docs.cloud.google.com/recommender/docs/overview).
  * Learn how to use [organization policy insights](https://docs.cloud.google.com/policy-intelligence/docs/organization-policy-insights).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

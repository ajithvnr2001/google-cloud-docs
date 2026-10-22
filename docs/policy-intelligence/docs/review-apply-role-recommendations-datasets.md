---
url: https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations-datasets/
title: Review and apply role recommendations for BigQuery datasets \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:02.764528+00:00
---

# Review and apply role recommendations for BigQuery datasets  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations-datasets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Review and apply role recommendations for BigQuery datasets Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view, understand, and apply IAM role recommendations for BigQuery datasets. Role recommendations help you enforce the principle of least privilege by ensuring that principals have only the permissions that they actually need.

## Before you begin

  * Enable the IAM and Recommender APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,recommender.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Ensure that you have an organization-level or project-level activation of [the Premium or Enterprise tier of Security Command Center](https://docs.cloud.google.com/security-command-center/pricing#security-command-center-pricing). For more information, see [Billing questions](https://docs.cloud.google.com/policy-intelligence/docs/billing-questions).

  * Understand [role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview).

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




### Required IAM roles

To get the permissions that you need to manage dataset-level role recommendations, ask your administrator to grant you the following IAM roles: 

  * [Role Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.roleViewer) (`roles/iam.roleViewer`) on your project
  * [IAM Recommender Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamAdmin) (`roles/recommender.iamAdmin`) on your project
  * [BigQuery Data Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`) on your dataset



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage dataset-level role recommendations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage dataset-level role recommendations:

  * To view recommendations: 
    * `iam.roles.get` on your project
    * `iam.roles.list` on your project
    * `recommender.iamPolicyRecommendations.get` on your project
    * `recommender.iamPolicyRecommendations.list` on your project
    * `recommender.iamPolicyInsights.get` on your project
    * `recommender.iamPolicyInsights.list` on your project
    * `bigquery.datasets.getIamPolicy` on your dataset
  * To apply and dismiss recommendations: 
    * `recommender.iamPolicyRecommendations.update` on your project
    * `bigquery.datasets.setIamPolicy` on your dataset



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Review and apply recommendations

You can review and apply dataset-level role recommendations with the Google Cloud CLI and the Recommender API.

**Note:** The IAM recommender does not take other forms of access controls into account when making recommendations. If you use access controls that are separate from IAM, such as Cloud Storage [access control lists (ACLs)](https://docs.cloud.google.com/storage/docs/access-control/lists) or Kubernetes [role-based access control (RBAC)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control), ensure that each recommendation will not disrupt those access controls before you apply the recommendation.

### gcloud

**Review your recommendations:**

To list your dataset-level recommendations, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command, filtering for only BigQuery dataset recommendations:
    
    
    gcloud recommender recommendations list \
        --location=LOCATION \
        --recommender=google.iam.policy.Recommender \
        --project=PROJECT_ID \
        --format=json \
        --filter="recommenderSubtype:REMOVE_ROLE_BIGQUERY_DATASET OR recommenderSubtype:REPLACE_ROLE_BIGQUERY_DATASET"
    

Replace the following values:

  * `LOCATION`: The region where your Cloud Storage datasets are located—for example, `us` or `us-central1`.
  * `PROJECT_ID`: The ID of the Google Cloud project that contains your BigQuery datasets. Project IDs are alphanumeric strings, like `my-project`.



The response is similar to the following example. In this example, all users with the Editor role on the project `my-project` (`projectEditor:my-project`) have the BigQuery Data Editor role (`roles/bigquery.dataEditor`) on the dataset `dataset-1`. However, this role hasn't been used in the past 90 days. As a result, the role recommendation suggests that you revoke the role:
    
    
    [
      {
        "associatedInsights": [
          {
            "insight": "projects/1069248613794/locations/us/insightTypes/google.iam.policy.Insight/insights/984eccca-0241-472f-baab-2557dd0d7282"
          }
        ],
        "content": {
          "operationGroups": [
            {
              "operations": [
                **{
                  "action": "remove",
                  "path": "/iamPolicy/bindings/*/members/*",
                  "pathFilters": {
                    "/iamPolicy/bindings/*/condition/expression": "",
                    "/iamPolicy/bindings/*/members/*": "projectEditor:my-project",
                    "/iamPolicy/bindings/*/role": "roles/bigquery.dataEditor"
                  },
                  "resource": "//bigquery.googleapis.com/projects/my-project/datasets/dataset-1",
                  "resourceType": "bigquery.googleapis.com/Dataset"
                }**
              ]
            }
          ],
          "overview": {
            "addedRoles": [],
            "member": "projectEditor:my-project",
            "minimumObservationPeriodInDays": "0",
            "removedRole": "roles/bigquery.dataEditor",
            "resource": "//bigquery.googleapis.com/projects/my-project/datasets/dataset-1"
          }
        },
        **"description" : "This role has not been used during the observation window.",**
        "etag": "\"3b123bc08d028128\"",
        "lastRefreshTime": "2024-02-04T08:00:00Z",
        "name": "projects/1069248613794/locations/us/recommenders/google.iam.policy.Recommender/recommendations/0e9831fe-6810-476b-b14d-2b64bda17288",
        "primaryImpact": {
          "category": "SECURITY",
          "securityProjection": {
            "details": {
              "revokedIamPermissionsCount": 37
            }
          }
        },
        "priority": "P4",
        "recommenderSubtype": "REMOVE_ROLE_BIGQUERY_DATASET",
        "stateInfo": {
          "state": "ACTIVE"
        },
        "targetResources": [
          "//bigquery.googleapis.com/projects/my-project/datasets/dataset-1"
        ]
      },
      {
        "associatedInsights": [
          {
            "insight": "projects/1069248613794/locations/us/insightTypes/google.iam.policy.Insight/insights/9d11057e-9c71-410f-ad55-fc82d87761d0"
          }
        ],
        "content": {
          "operationGroups": [
            {
              "operations": [
                {
                  "action": "remove",
                  "path": "/iamPolicy/bindings/*/members/*",
                  "pathFilters": {
                    "/iamPolicy/bindings/*/condition/expression": "",
                    "/iamPolicy/bindings/*/members/*": "user:alicexz@google.com",
                    "/iamPolicy/bindings/*/role": "roles/bigquery.dataOwner"
                  },
                  "resource": "//bigquery.googleapis.com/projects/my-project/datasets/dataset-1",
                  "resourceType": "bigquery.googleapis.com/Dataset"
                }
              ]
            }
          ],
          "overview": {
            "addedRoles": [],
            "member": "user:alicexz@google.com",
            "minimumObservationPeriodInDays": "0",
            "removedRole": "roles/bigquery.dataOwner",
            "resource": "//bigquery.googleapis.com/projects/my-project/datasets/dataset-1"
          }
        },
        "description": "This role has not been used during the observation window.",
        "etag": "\"1da285f7aa6438f1\"",
        "lastRefreshTime": "2024-02-04T08:00:00Z",
        "name": "projects/1069248613794/locations/us/recommenders/google.iam.policy.Recommender/recommendations/56013294-cf81-402a-8cde-25489545777c",
        "primaryImpact": {
          "category": "SECURITY",
          "securityProjection": {
            "details": {
              "revokedIamPermissionsCount": 64
            }
          }
        },
        "priority": "P4",
        "recommenderSubtype": "REMOVE_ROLE_BIGQUERY_DATASET",
        "stateInfo": {
          "state": "ACTIVE"
        },
        "targetResources": [
          "//bigquery.googleapis.com/projects/my-project/datasets/dataset-1"
        ]
      }
    ]

Review each recommendation carefully and consider when it was last refreshed and how it will change the principal's access to Google Cloud resources. To learn how to review recommendations from the gcloud CLI, see Review recommendations on this page.

**To apply a recommendation:**

  1. Use the [`gcloud recommender recommendations mark-claimed` command](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-claimed) to change the recommendation's state to `CLAIMED,` which prevents the recommendation from changing while you apply it:
         
         gcloud recommender recommendations mark-claimed \
             RECOMMENDATION_ID \
             --location=LOCATION \
             --recommender=google.iam.policy.Recommender \
             --project=PROJECT_ID \
             --format=FORMAT \
             --etag=ETAG \
             --state-metadata=STATE_METADATA
         

Replace the following values:

     * `RECOMMENDATION_ID`: The unique identifier for the recommendation. This value appears at the end of the `name` field in the recommendation. For example, if the `name` field is `projects/example-project/locations/global/recommenders/google.iam.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f`, the recommendation ID is `fb927dc1-9695-4436-0000-f0f285007c0f`. 
     * `LOCATION`: The region where your BigQuery dataset is located—for example, `us` or `us-central1`. 
     * `PROJECT_ID`: The ID of the Google Cloud project that contains your BigQuery datasets. Project IDs are alphanumeric strings, like `my-project`. 
     * `FORMAT`: The format of the response. Use `json` or `yaml`. 
     * `ETAG`: The value of the `etag` field in the recommendation, such as `"dd0686e7136a4cbb"`. Note that this value can include quotes. 
     * `STATE_METADATA`: Optional. Comma-separated key-value pairs that contain your choice of metadata about the recommendation. For example, `--state-metadata=reviewedBy=alice,priority=high`. The metadata replaces the `stateInfo.stateMetadata` field in the recommendation. 

If the command succeeds, the response shows the recommendation in a `CLAIMED` state, as shown in the following example. For clarity, the example omits most fields:
    
    ...
    "priority": "P1",
    "recommenderSubtype": "REMOVE_ROLE_BIGQUERY_DATASET",
    **"stateInfo" : {
      "state": "CLAIMED"
    }**
    ...

  2. [Get the allow policy](https://docs.cloud.google.com/iam/docs/manage-access-other-resources#getting-policy) for the dataset, then [modify and set the allow policy](https://docs.cloud.google.com/iam/docs/manage-access-other-resources#modifying-policy) so that it reflects the recommendation.

  3. Update the recommendation's state to `SUCCEEDED`, if you were able to apply the recommendation, or `FAILED`, if you could not apply the recommendation:
         
         gcloud recommender recommendations COMMAND \
             RECOMMENDATION_ID \
             --location=LOCATION \
             --recommender=google.iam.policy.Recommender \
             --project=PROJECT_ID \
             --format=FORMAT \
             --etag=ETAG \
             --state-metadata=STATE_METADATA
         

Replace the following values:

     * `COMMAND`: Use `mark-succeeded`, if you were able to apply the recommendation, or `mark-failed`, if you could not apply the recommendation. 

     * `RECOMMENDATION_ID`: The unique identifier for the recommendation. This value appears at the end of the `name` field in the recommendation. For example, if the `name` field is `projects/example-project/locations/global/recommenders/google.iam.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f`, the recommendation ID is `fb927dc1-9695-4436-0000-f0f285007c0f`. 
     * `LOCATION`: The region where your BigQuery dataset is located—for example, `us` or `us-central1`. 
     * `PROJECT_ID`: The ID of the Google Cloud project that contains your BigQuery datasets. Project IDs are alphanumeric strings, like `my-project`. 
     * `FORMAT`: The format of the response. Use `json` or `yaml`. 
     * `ETAG`: The value of the `etag` field in the recommendation, such as `"dd0686e7136a4cbb"`. Note that this value can include quotes. 
     * `STATE_METADATA`: Optional. Comma-separated key-value pairs that contain your choice of metadata about the recommendation. For example, `--state-metadata=reviewedBy=alice,priority=high`. The metadata replaces the `stateInfo.stateMetadata` field in the recommendation. 

For example, if you marked the recommendation as having succeeded, the response shows the recommendation in a `SUCCEEDED` state. For clarity, this example omits most fields:
    
    ...
    "priority": "P1",
    "recommenderSubtype": "REMOVE_ROLE_BIGQUERY_DATASET",
    **"stateInfo" : {
      "state": "SUCCEEDED"
    }**
    ...




### REST

**Review your recommendations:**

To list all available recommendations for your BigQuery datasets, use the Recommender API's `[recommendations.list](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list)` method. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: The ID of the Google Cloud project that contains your BigQuery datasets. Project IDs are alphanumeric strings, like `my-project`.
  * `LOCATION`: The region where your BigQuery datasets are located—for example, `us` or `us-central1`.
  * `PAGE_SIZE`: Optional. The maximum number of results to return from this request. If not specified, the server will determine the number of results to return. If the number of recommendations is greater than the page size, the response contains a pagination token that you can use to retrieve the next page of results. 
  * `PAGE_TOKEN`: Optional. The pagination token returned in an earlier response from this method. If specified, the list of recommendations will start where the previous request ended.
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.iam.policy.Recommender/recommendations?filter=recommenderSubtype%20%3D%20REMOVE_ROLE_BIGQUERY_DATASET%20OR%20recommenderSubtype%20%3D%20REPLACE_ROLE_BIGQUERY_DATASET&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.iam.policy.Recommender/recommendations?filter=recommenderSubtype%20%3D%20REMOVE_ROLE_BIGQUERY_DATASET%20OR%20recommenderSubtype%20%3D%20REPLACE_ROLE_BIGQUERY_DATASET&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.iam.policy.Recommender/recommendations?filter=recommenderSubtype%20%3D%20REMOVE_ROLE_BIGQUERY_DATASET%20OR%20recommenderSubtype%20%3D%20REPLACE_ROLE_BIGQUERY_DATASET&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN" | Select-Object -Expand Content

The response is similar to the following example. In this example, all users with the Editor role on the project `my-project` (`projectEditor:my-project`) have the BigQuery Data Editor role (`roles/bigquery.dataEditor`) on the dataset `dataset-1`. However, this role hasn't been used in the past 90 days. As a result, the role recommendation suggests that you revoke the role: 
    
    
    {
      "recommendations": [
        {
          "name": "projects/1069248613794/locations/us/recommenders/google.iam.policy.Recommender/recommendations/0e9831fe-6810-476b-b14d-2b64bda17288",
          "description": "This role has not been used during the observation window.",
          "lastRefreshTime": "2024-02-02T08:00:00Z",
          "primaryImpact": {
            "category": "SECURITY",
            "securityProjection": {
              "details": {
                "revokedIamPermissionsCount": 37
              }
            }
          },
          "content": {
            "operationGroups": [
              {
                "operations": [
                  {
                    "action": "remove",
                    "resourceType": "bigquery.googleapis.com/Dataset",
                    "resource": "//bigquery.googleapis.com/projects/my-project/datasets/dataset-1",
                    "path": "/iamPolicy/bindings/*/members/*",
                    "pathFilters": {
                      "/iamPolicy/bindings/*/condition/expression": "",
                      "/iamPolicy/bindings/*/members/*": "projectEditor:my-project",
                      "/iamPolicy/bindings/*/role": "roles/bigquery.dataEditor"
                    }
                  }
                ]
              }
            ],
            "overview": {
              "resource": "//bigquery.googleapis.com/projects/my-project/datasets/dataset-1",
              "member": "projectEditor:my-project",
              "removedRole": "roles/bigquery.dataEditor",
              "addedRoles": [],
              "minimumObservationPeriodInDays": "0"
            }
          },
          "stateInfo": {
            "state": "ACTIVE"
          },
          "etag": "\"d008ad3780bad5e0\"",
          "recommenderSubtype": "REMOVE_ROLE_BIGQUERY_DATASET",
          "associatedInsights": [
            {
              "insight": "projects/1069248613794/locations/us/insightTypes/google.iam.policy.Insight/insights/984eccca-0241-472f-baab-2557dd0d7282"
            }
          ],
          "priority": "P4",
          "targetResources": [
            "//bigquery.googleapis.com/projects/my-project/datasets/dataset-1"
          ]
        }
      ]
    }
    

Review each recommendation carefully and consider when it was last refreshed and how it will change the principal's access to Google Cloud resources. To learn how to review recommendations from the REST API, see Review recommendations on this page.

**To apply a recommendation:**

  1. Mark the recommendation as `CLAIMED`:

To mark a recommendation as `CLAIMED`, which prevents the recommendation from changing while you apply it, use the Recommender API's `[recommendations.markClaimed](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/markClaimed)` method. 

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: The ID of the Google Cloud project that contains your BigQuery datasets. Project IDs are alphanumeric strings, like `my-project`.
     * `LOCATION`: The region where your BigQuery dataset is located—for example, `us` or `us-central1`.
     * `RECOMMENDATION_ID`: The unique identifier for the recommendation. This value appears at the end of the `name` field in the recommendation. For example, if the `name` field is `projects/example-project/locations/global/recommenders/google.iam.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f`, the recommendation ID is `fb927dc1-9695-4436-0000-f0f285007c0f`. 
     * `ETAG`: The value of the `etag` field in the recommendation, such as `"dd0686e7136a4cbb"`. Use backslashes to escape quotes, for example, `"\"df7308cca9719dcc\""`. 
     * `STATE_METADATA`: Optional. An object that contains key-value pairs with your choice of metadata about the recommendation. For example, `{"reviewedBy": "alice", "priority": "high"}`. The metadata replaces the `stateInfo.stateMetadata` field in the recommendation. 

HTTP method and URL: 
    
    POST https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markClaimed

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
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markClaimed"

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
        -Uri "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markClaimed" | Select-Object -Expand Content

The response shows the recommendation in a `CLAIMED` state, as shown in the following example. For clarity, this example omits most fields: 
    
    ...
    **"stateInfo": {
      "state": "CLAIMED"
    },**
    "etag": "\"7caf4103d7669e12\"",
    "recommenderSubtype": "REMOVE_ROLE_BIGQUERY_DATASET",
    ...
    

  2. [Get the allow policy](https://docs.cloud.google.com/iam/docs/manage-access-other-resources#getting-policy) for the project, then [modify the allow policy](https://docs.cloud.google.com/iam/docs/manage-access-other-resources#modifying-policy) so that it reflects the recommendation.

  3. Update the recommendation's state to `SUCCEEDED`, if you were able to apply the recommendation, or `FAILED`, if you could not apply the recommendation:

### `SUCCEEDED`

To mark a recommendation as `SUCCEEDED`, indicating that you were able to apply it, use the Recommender API's `[recommendations.markSucceeded](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/markSucceeded)` method. 

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: The ID of the Google Cloud project that contains your BigQuery datasets. Project IDs are alphanumeric strings, like `my-project`.
     * `LOCATION`: The region where your BigQuery dataset is located—for example, `us` or `us-central1`.
     * `RECOMMENDATION_ID`: The unique identifier for the recommendation. This value appears at the end of the `name` field in the recommendation. For example, if the `name` field is `projects/example-project/locations/global/recommenders/google.iam.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f`, the recommendation ID is `fb927dc1-9695-4436-0000-f0f285007c0f`. 
     * `ETAG`: The value of the `etag` field in the recommendation, such as `"dd0686e7136a4cbb"`. Use backslashes to escape quotes, for example, `"\"df7308cca9719dcc\""`. 
     * `STATE_METADATA`: Optional. An object that contains key-value pairs with your choice of metadata about the recommendation. For example, `{"reviewedBy": "alice", "priority": "high"}`. The metadata replaces the `stateInfo.stateMetadata` field in the recommendation. 

HTTP method and URL: 
    
    POST https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markSucceeded

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
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markSucceeded"

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
        -Uri "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markSucceeded" | Select-Object -Expand Content

The response shows the recommendation in a `SUCCEEDED` state, as shown in the following example. For clarity, this example omits most fields: 
    
    ...
    **"stateInfo": {
      "state": "SUCCEEDED"
    },**
    "etag": "\"7caf4103d7669e12\"",
    "recommenderSubtype": "REMOVE_ROLE_BIGQUERY_DATASET",
    ...
    

### `FAILED`

To mark a recommendation as `FAILED`, indicating that you were not able to apply it, use the Recommender API's `[recommendations.markFailed](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/markFailed)` method. 

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: The ID of the Google Cloud project that contains your BigQuery datasets. Project IDs are alphanumeric strings, like `my-project`.
     * `LOCATION`: The region where your BigQuery dataset is located—for example, `us` or `us-central1`.
     * `RECOMMENDATION_ID`: The unique identifier for the recommendation. This value appears at the end of the `name` field in the recommendation. For example, if the `name` field is `projects/example-project/locations/global/recommenders/google.iam.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f`, the recommendation ID is `fb927dc1-9695-4436-0000-f0f285007c0f`. 
     * `ETAG`: The value of the `etag` field in the recommendation, such as `"dd0686e7136a4cbb"`. Use backslashes to escape quotes, for example, `"\"df7308cca9719dcc\""`. 
     * `STATE_METADATA`: Optional. An object that contains key-value pairs with your choice of metadata about the recommendation. For example, `{"reviewedBy": "alice", "priority": "high"}`. The metadata replaces the `stateInfo.stateMetadata` field in the recommendation. 

HTTP method and URL: 
    
    POST https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markFailed

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
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markFailed"

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
        -Uri "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.iam.policy.Recommender/recommendations/RECOMMENDATION_ID:markFailed" | Select-Object -Expand Content

The response shows the recommendation in a `FAILED` state, as shown in the following example. For clarity, this example omits most fields: 
    
    ...
    **"stateInfo": {
      "state": "FAILED"
    },**
    "etag": "\"7caf4103d7669e12\"",
    "recommenderSubtype": "REMOVE_ROLE_BIGQUERY_DATASET",
    ...
    




## Understand recommendations

Each recommendation includes information to help you understand why the recommendation was made.

For details on the fields of a recommendation, see the [`Recommendation` reference](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations#resource-recommendation).

To see the permission usage that this recommendation is based on, view the [policy insights](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#how-policy-insights-work) that are associated with the recommendation. These insights are listed in the `associatedInsights` field. To view a policy insight that is associated with the recommendation, do the following:

  1. Copy the associated insight's ID. The ID is everything after `insights/` in the `insight` field. For example, if the `insight` field reads `projects/123456789012/locations/us/insightTypes/google.iam.policy.Insight/insights/7849add9-73c0-419e-b169-42b3671173fb`, the insight ID is `7849add9-73c0-419e-b169-42b3671173fb`.
  2. Follow the instructions to [get a policy insight](https://docs.cloud.google.com/policy-intelligence/docs/policy-insights-datasets#get-insight), using the insight ID you copied.



## What's next

  * Learn more about [Recommender](https://docs.cloud.google.com/recommender/docs/overview).
  * Learn how to use [allow policy insights for BigQuery datasets](https://docs.cloud.google.com/policy-intelligence/docs/policy-insights-datasets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

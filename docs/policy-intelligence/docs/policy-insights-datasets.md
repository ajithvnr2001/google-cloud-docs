---
url: https://docs.cloud.google.com/policy-intelligence/docs/policy-insights-datasets/
title: Review policy insights for BigQuery datasets \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:51.986514+00:00
---

# Review policy insights for BigQuery datasets  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/policy-insights-datasets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Review policy insights for BigQuery datasets Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows how to manage dataset-level policy insights, which are machine learning-based findings about permission usage for your BigQuery datasets. Policy insights can help you identify which principals have permissions that they don't need. 

This page focuses on policy insights for datasets. Recommender also offers policy insights for the following resource types: 

  * [Projects, folders, and organizations](https://docs.cloud.google.com/policy-intelligence/docs/policy-insights)
  * [Cloud Storage buckets](https://docs.cloud.google.com/policy-intelligence/docs/policy-insights-buckets)



Dataset-level policy insights are sometimes linked to [ role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview). Role recommendations suggest actions that you can take to remediate the issues identified by dataset-level policy insights. 

**Note** : Policy insights might not list all of the permissions that a principal needs. For example, policy insights don't list permissions used by non-public, early access features. To safely replace a principal's role, use role recommendations. 

## Before you begin

  * Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Be familiar with [IAM role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview).
  * Ensure that you have an [ organization-level or project-level activation](https://docs.cloud.google.com/security-command-center/pricing#security-command-center-pricing) of the Premium or Enterprise tier of Security Command Center. For more information, see [ Billing questions](https://docs.cloud.google.com/policy-intelligence/docs/billing-questions).
  * Optional: Read about [Recommender insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights).



### Required roles

To get the permissions that you need to manage dataset-level policy insights, ask your administrator to grant you the following IAM roles on your project: 

  * [BigQuery Data Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)
  * [IAM Recommender Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamAdmin) (`roles/recommender.iamAdmin`)
  * Manage dataset-level policy insights with the gcloud CLI or REST API: [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage dataset-level policy insights. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage dataset-level policy insights:

  * View dataset-level policy insights: 
    * `recommender.iamPolicyInsights.get`
    * `recommender.iamPolicyInsights.list`
  * Modify dataset-level policy insights: `recommender.iamPolicyInsights.update`
  * Manage dataset-level policy insights with the gcloud CLI or REST API: `serviceusage.services.use`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List dataset-level policy insights

To list all dataset-level policy insights for your project, use one of the following methods: 

### gcloud

Use the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command to view all dataset-level policy insights for your project. 

Before you run the command, replace the following values: 

  * `PROJECT_ID`: The ID of the project that you want to list insights for. 
  * `LOCATION`: The location of the datasets whose insights you want to list. 


    
    
    gcloud recommender insights list --insight-type=google.iam.policy.Insight \
        --project=PROJECT_ID \
        --location=LOCATION\
        --filter="insightSubtype:PERMISSIONS_USAGE_BIGQUERY_DATASET"

The output lists all of the dataset-level policy insights for your project in the specified location. For example: 
    
    
    INSIGHT_ID                            CATEGORY  INSIGHT_STATE  LAST_REFRESH_TIME     SEVERITY  INSIGHT_SUBTYPE                     DESCRIPTION
    101d03ad-6148-4628-943e-fcf1a3af6b57  SECURITY  ACTIVE         2024-02-02T08:00:00Z  LOW       PERMISSIONS_USAGE_BIGQUERY_DATASET  0 of the permissions in this role binding were used in the past 90 days.
    15133dd9-4cbc-41e9-8990-b189241676d8  SECURITY  ACTIVE         2024-02-02T08:00:00Z  LOW       PERMISSIONS_USAGE_BIGQUERY_DATASET  0 of the permissions in this role binding were used in the past 90 days.
    1590aeae-d5bf-4e3d-b7d5-e230212f5faf  SECURITY  ACTIVE         2024-02-02T08:00:00Z  LOW       PERMISSIONS_USAGE_BIGQUERY_DATASET  4 of the permissions in this role binding were used in the past 90 days.
    280e5a14-4d09-4ac6-8e14-be7407611ad7  SECURITY  ACTIVE         2024-02-02T08:00:00Z  LOW       PERMISSIONS_USAGE_BIGQUERY_DATASET  0 of the permissions in this role binding were used in the past 90 days.
    34102078-085f-45d3-ae72-81da16c75781  SECURITY  ACTIVE         2024-02-02T08:00:00Z  LOW       PERMISSIONS_USAGE_BIGQUERY_DATASET  10 of the permissions in this role binding were used in the past 90 days.

### REST

The Recommender API's `[insights.list](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list)` method lists all dataset-level policy insights for your project. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: The ID of the project that you want to list insights for.
  * `LOCATION`: The location of the datasets whose insights you want to list. 



HTTP method and URL: 
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.iam.policy.Insight/insights?filter=insightSubtype%20%3D%20PERMISSIONS_USAGE_BIGQUERY_DATASET

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.iam.policy.Insight/insights?filter=insightSubtype%20%3D%20PERMISSIONS_USAGE_BIGQUERY_DATASET"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.iam.policy.Insight/insights?filter=insightSubtype%20%3D%20PERMISSIONS_USAGE_BIGQUERY_DATASET" | Select-Object -Expand Content

The response lists all of the dataset-level policy insights for your project in the specified location. For example: 
    
    
    {
      "insights": [
        {
          "name": "projects/1069248613794/locations/us/insightTypes/google.iam.policy.Insight/insights/101d03ad-6148-4628-943e-fcf1a3af6b57",
          "description": "0 of the permissions in this role binding were used in the past 90 days.",
          "content": {
            "role": "roles/bigquery.dataEditor",
            "member": "projectEditor:my-project",
            "condition": {
              "expression": "",
              "title": "",
              "description": "",
              "location": ""
            },
            "exercisedPermissions": [],
            "inferredPermissions": [],
            "currentTotalPermissionsCount": "37"
          },
          "lastRefreshTime": "2024-02-02T08:00:00Z",
          "observationPeriod": "7779600s",
          "stateInfo": {
            "state": "ACTIVE"
          },
          "category": "SECURITY",
          "associatedRecommendations": [
            {
              "recommendation": "projects/1069248613794/locations/us/recommenders/google.iam.policy.Recommender/recommendations/9327f952-1ceb-488e-9e49-f17eb21f6e5e"
            }
          ],
          "targetResources": [
            "//bigquery.googleapis.com/projects/my-project/datasets/dataset-1"
          ],
          "insightSubtype": "PERMISSIONS_USAGE_BIGQUERY_DATASET",
          "etag": "\"35d4af47524d3f0c\"",
          "severity": "LOW"
        },
        {
          "name": "projects/1069248613794/locations/us/insightTypes/google.iam.policy.Insight/insights/15133dd9-4cbc-41e9-8990-b189241676d8",
          "description": "0 of the permissions in this role binding were used in the past 90 days.",
          "content": {
            "role": "roles/bigquery.dataViewer",
            "member": "projectViewer:my-project",
            "condition": {
              "expression": "",
              "title": "",
              "description": "",
              "location": ""
            },
            "exercisedPermissions": [],
            "inferredPermissions": [],
            "currentTotalPermissionsCount": "17"
          },
          "lastRefreshTime": "2024-02-02T08:00:00Z",
          "observationPeriod": "7779600s",
          "stateInfo": {
            "state": "ACTIVE"
          },
          "category": "SECURITY",
          "associatedRecommendations": [
            {
              "recommendation": "projects/1069248613794/locations/us/recommenders/google.iam.policy.Recommender/recommendations/bc9b4c28-cc93-4a91-97ea-ff67e3cef1b4"
            }
          ],
          "targetResources": [
            "//bigquery.googleapis.com/projects/my-project/datasets/dataset-2"
          ],
          "insightSubtype": "PERMISSIONS_USAGE_BIGQUERY_DATASET",
          "etag": "\"eafa79df1b329063\"",
          "severity": "LOW"
        }
      ]
    }

To learn more about the components of an insight, see Review dataset-level policy insights on this page. 

## Get a single dataset-level policy insight

To get more information about a single insight, including the insight's description, status, and any recommendations it's associated with, use one of the following methods: 

### gcloud

Use the [`gcloud recommender insights describe`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/describe) command with your insight ID to view information about a single insight. 

  * `INSIGHT_ID`: The ID of the insight that you want to view. To find the ID, list the insights for your project. 
  * `PROJECT_ID`: The ID of the project that you want to manage insights for.
  * `LOCATION`: The location of the dataset whose insight you want to get. 


    
    
    gcloud recommender insights describe INSIGHT_ID \
        --insight-type=google.iam.policy.Insight \
        --project=PROJECT_ID \
        --location=LOCATION

The output shows the insight in detail. For example, the following insight indicates that all users with the Editor role on the project `my-project` (`projectEditor:my-project`) have the BigQuery Data Editor role (`roles/bigquery.dataEditor`) on the dataset `dataset-1`, but that none of the permissions in that role were used in the past 90 days: 
    
    
    associatedRecommendations:
    - recommendation: projects/1069248613794/locations/us/recommenders/google.iam.policy.Recommender/recommendations/9327f951-1ceb-488e-9e49-f17eb21f6e5e
    category: SECURITY
    content:
      condition:
        description: ''
        expression: ''
        location: ''
        title: ''
      currentTotalPermissionsCount: '37'
      exercisedPermissions: []
      inferredPermissions: []
      member: projectEditor:my-project
      role: roles/bigquery.dataEditor
    description: 0 of the permissions in this role binding were used in the past 90 days.
    etag: '"5f2f352a738f7a24"'
    insightSubtype: PERMISSIONS_USAGE_BIGQUERY_DATASET
    lastRefreshTime: '2024-02-04T08:00:00Z'
    name: projects/1069248613794/locations/us/insightTypes/google.iam.policy.Insight/insights/101d03ad-6148-4628-943e-fcf1a3af6b57
    observationPeriod: 7776000s
    severity: LOW
    stateInfo:
      state: ACTIVE
    targetResources:
    - //bigquery.googleapis.com/projects/my-project/datasets/dataset-1

To learn more about the components of an insight, see Review dataset-level policy insights on this page. 

### REST

The Recommender API's `[insights.get](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/get)` method gets a single insight. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: The ID of the project that you want to manage insights for. 
  * `LOCATION`: The location of the dataset whose insight you want to get. 
  * `INSIGHT_ID`: The ID of the insight that you want to view. If you don't know the insight ID, you can find it by listing the insights in your project. The ID of an insight is everything after `insights/` in the `name` field for the insight. 



HTTP method and URL: 
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID" | Select-Object -Expand Content

The response contains the insight. For example, the following insight indicates that all users with the Editor role on the project `my-project` (`projectEditor:my-project`) have the BigQuery Data Editor role (`roles/bigquery.dataEditor`) on the dataset `dataset-1`, but that none of the permissions in that role were used in the past 90 days: 
    
    
    {
      "name": "projects/1069248613794/locations/us/insightTypes/google.iam.policy.Insight/insights/101d03ad-6148-4628-943e-fcf1a3af6b57",
      "description": "0 of the permissions in this role binding were used in the past 90 days.",
      "content": {
        "role": "roles/bigquery.dataEditor",
        "member": "projectEditor:my-project",
        "condition": {
          "expression": "",
          "title": "",
          "description": "",
          "location": ""
        },
        "exercisedPermissions": [],
        "inferredPermissions": [],
        "currentTotalPermissionsCount": "37"
      },
      "lastRefreshTime": "2024-02-02T08:00:00Z",
      "observationPeriod": "7779600s",
      "stateInfo": {
        "state": "ACTIVE"
      },
      "category": "SECURITY",
      "associatedRecommendations": [
        {
          "recommendation": "projects/1069248613794/locations/us/recommenders/google.iam.policy.Recommender/recommendations/9327f952-1ceb-488e-9e49-f17eb21f6e5e"
        }
      ],
      "targetResources": [
        "//bigquery.googleapis.com/projects/my-project/datasets/dataset-1"
      ],
      "insightSubtype": "PERMISSIONS_USAGE_BIGQUERY_DATASET",
      "etag": "\"35d4af47524d3f0c\"",
      "severity": "LOW"
    }

To learn more about the components of an insight, see Review dataset-level policy insights on this page. 

## Review dataset-level policy insights

After you get a single insight, you can review its contents to understand the pattern of resource usage that it highlights. 

An insight's content is determined by its subtypes. Dataset-level policy insights (`google.iam.policy.Insight`) insights have the `PERMISSIONS_USAGE_BIGQUERY_DATASET` subtype. 

`PERMISSIONS_USAGE_BIGQUERY_DATASET` insights have the following components, not necessarily in this order: 

  * `associatedRecommendations`: The identifiers for any recommendations associated with the insight. If there are no recommendations associated with the insight, this field is empty. 
  * `category`: The category for IAM insights is always `SECURITY`. 
  * `content`: Reports a principal's permission usage for a specific role. This field contains the following components: 

    * `condition`: Any conditions attached to the binding that grants the principal the role. If there are no conditions, this field contains an empty condition.
    * `exercisedPermissions`: The permissions in the role that the principal used during the observation period.
    * `inferredPermissions`: The permissions in the role that Recommender has determined, through [ML](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#ml), that the principal is likely to need based on their exercised permissions.
    * `member`: The principal whose permission usage was analyzed.
    * `role`: The role for which the permission usage was analyzed.
  * `description`: A human-readable summary of the insight. 
  * `etag`: A unique identifier for the current state of an insight. Each time the insight changes, a new `etag` value is assigned. 

To change the state of an insight, you must provide the `etag` of the existing insight. Using the `etag` helps ensure that any operations are performed only if the insight has not changed since you last retrieved it. 

  * `insightSubtype`: The insight subtype. 
  * `lastRefreshTime`: The date when the insight was last refreshed, which indicates the freshness of the data used to generate the insight. 
  * `name`: The name of the insight, in the following format:
        
        projects/PROJECT_ID/locations/LOCATION/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID

The placeholders have the following values:

    * `PROJECT_ID`: The ID of the project where the insight was generated. 
    * `LOCATION`: The location of the dataset that the insight is for. 
    * `INSIGHT_ID`: A unique ID for the insight.
  * `observationPeriod`: The time period leading up to the insight. The source data used to generate the insight ends at `lastRefreshTime` and begins at `lastRefreshTime` minus `observationPeriod`. 
  * `stateInfo`: Insights go through multiple state transitions after they are proposed: 

    * `ACTIVE`: The insight has been generated, but either no actions have been taken, or an action was taken without updating the insight's state. Active insights are updated when the underlying data changes. 
    * `ACCEPTED`: Some action has been taken based on the insight. Insights become accepted when an associated recommendation was marked `CLAIMED`, `SUCCEEDED`, or `FAILED`, or the insight was accepted directly. When an insight is in the `ACCEPTED` state, the content of the insight cannot change. Accepted insights are retained for 90 days after they are accepted. 
  * `targetResources`: The [full resource name ](https://docs.cloud.google.com/iam/docs/full-resource-names) of the dataset that the insight is for. For example, `//bigquery.googleapis.com/projects/my-project/datasets/my-dataset`. 



## Mark a dataset-level policy insight as `ACCEPTED`

If you take action based on an active insight, you can mark that insight as `ACCEPTED`. The `ACCEPTED` state tells the Recommender API that you have taken action based on this insight, which helps refine your recommendations. 

Accepted insights are retained for 90 days after they are marked as `ACCEPTED`. 

### gcloud

Use the [ `gcloud recommender insights mark-accepted`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted) command with your insight ID to mark an insight as `ACCEPTED`. 

  * `INSIGHT_ID`: The ID of the insight that you want to view. To find the ID, list the insights for your project. 
  * `PROJECT_ID`: The ID of the project that you want to manage insights for.
  * `LOCATION`: The location of the dataset whose insight you want to mark as `ACCEPTED`. 
  * `ETAG`: An identifier for a version of the insight. To get the `etag`, do the following: 

    1. Get the insight using the `gcloud recommender insights describe` command. 
    2. Find and copy the `etag` value from the output, including the enclosing quotes. For example, `"d3cdec23cc712bd0"`. 


    
    
    gcloud recommender insights mark-accepted INSIGHT_ID \
        --insight-type=google.iam.policy.Insight \
        --project=PROJECT_ID \
        --location=LOCATION \
        --etag=ETAG

The output shows the insight, now with the state of `ACCEPTED`: 
    
    
    associatedRecommendations:
    - recommendation: projects/1069248613794/locations/us/recommenders/google.iam.policy.Recommender/recommendations/9327f951-1ceb-488e-9e49-f17eb21f6e5e
    category: SECURITY
    content:
      condition:
        description: ''
        expression: ''
        location: ''
        title: ''
      currentTotalPermissionsCount: '37'
      exercisedPermissions: []
      inferredPermissions: []
      member: projectEditor:my-project
      role: roles/bigquery.dataEditor
    description: 0 of the permissions in this role binding were used in the past 90 days.
    etag: '"5f2f352a738f7a24"'
    insightSubtype: PERMISSIONS_USAGE_BIGQUERY_DATASET
    lastRefreshTime: '2024-02-04T08:00:00Z'
    name: projects/1069248613794/locations/us/insightTypes/google.iam.policy.Insight/insights/101d03ad-6148-4628-943e-fcf1a3af6b57
    observationPeriod: 7776000s
    severity: LOW
    **stateInfo :
      state: ACCEPTED**
    targetResources:
    - //bigquery.googleapis.com/projects/my-project/datasets/dataset-1

To learn more about the state info of an insight, see Review dataset-level policy insights on this page. 

### REST

The Recommender API's `[insights.markAccepted](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/markAccepted)` method marks an insight as `ACCEPTED`. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: The ID of the project that you want to manage insights for. 
  * `LOCATION`: The location of the dataset whose insight you want to mark as `ACCEPTED`. 
  * `INSIGHT_ID`: The ID of the insight that you want to view. If you don't know the insight ID, you can find it by listing the insights in your project. The ID of an insight is everything after `insights/` in the `name` field for the insight. 
  * `ETAG`: An identifier for a version of the insight. To get the `etag`, do the following: 
    1. Get the insight using the `insights.get` method.
    2. Find and copy the `etag` value from the response.



HTTP method and URL: 
    
    
    POST https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID:markAccepted

Request JSON body: 
    
    
    {
      "etag": "ETAG"
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
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID:markAccepted"

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
        -Uri "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID:markAccepted" | Select-Object -Expand Content

The response contains the insight, now with the state of `ACCEPTED`: 
    
    
    {
      "name": "projects/1069248613794/locations/us/insightTypes/google.iam.policy.Insight/insights/101d03ad-6148-4628-943e-fcf1a3af6b57",
      "description": "0 of the permissions in this role binding were used in the past 90 days.",
      "content": {
        "role": "roles/bigquery.dataEditor",
        "member": "projectEditor:my-project",
        "condition": {
          "expression": "",
          "title": "",
          "description": "",
          "location": ""
        },
        "exercisedPermissions": [],
        "inferredPermissions": [],
        "currentTotalPermissionsCount": "37"
      },
      "lastRefreshTime": "2024-02-02T08:00:00Z",
      "observationPeriod": "7779600s",
      **"stateInfo": {
        "state": "ACCEPTED"
      },**
      "category": "SECURITY",
      "associatedRecommendations": [
        {
          "recommendation": "projects/1069248613794/locations/us/recommenders/google.iam.policy.Recommender/recommendations/9327f952-1ceb-488e-9e49-f17eb21f6e5e"
        }
      ],
      "targetResources": [
        "//bigquery.googleapis.com/projects/my-project/datasets/dataset-1"
      ],
      "insightSubtype": "PERMISSIONS_USAGE_BIGQUERY_DATASET",
      "etag": "\"35d4af47524d3f0c\"",
      "severity": "LOW"
    }

To learn more about the state info of an insight, see Review dataset-level policy insights on this page. 

## What's next

  * Learn how to [view and apply policy recommendations for BigQuery datasets](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations-datasets).
  * Use the [Active Assist](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems) to view and manage all recommendations for your project, including IAM recommendations.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

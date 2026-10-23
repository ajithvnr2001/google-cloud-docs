---
url: https://docs.cloud.google.com/policy-intelligence/docs/policy-insights-buckets/
title: Review policy insights for Cloud Storage buckets \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:55.763702+00:00
---

# Review policy insights for Cloud Storage buckets  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/policy-insights-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Review policy insights for Cloud Storage buckets Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to manage bucket-level policy insights, which are machine learning-based findings about permission usage for your Cloud Storage buckets. Policy insights can help you identify which principals have permissions that they don't need. 

This page focuses on policy insights for buckets. Recommender also offers policy insights for the following resource types: 

  * [Projects, folders, and organizations](https://docs.cloud.google.com/policy-intelligence/docs/policy-insights)
  * [BigQuery datasets](https://docs.cloud.google.com/policy-intelligence/docs/policy-insights-datasets)



Bucket-level policy insights are sometimes linked to [ role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview). Role recommendations suggest actions that you can take to remediate the issues identified by bucket-level policy insights. 

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

To get the permissions that you need to manage bucket-level policy insights, ask your administrator to grant you the following IAM roles on your project: 

  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * Manage bucket-level policy insights with the gcloud CLI or REST API: [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage bucket-level policy insights. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage bucket-level policy insights:

  * To view bucket-level policy insights: 
    * `recommender.iamPolicyInsights.get`
    * `recommender.iamPolicyInsights.list`
  * To modify bucket-level policy insights: `recommender.iamPolicyInsights.update`
  * To manage bucket-level policy insights in the Google Cloud console: 
    * `resourcemanager.projects.get`
    * `storage.buckets.list`
  * Manage bucket-level policy insights with the gcloud CLI or REST API: `serviceusage.services.use`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List bucket-level policy insights

To list all bucket-level policy insights for your project, use one of the following methods: 

### Console

  1. In the Google Cloud console, go to the **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Find the **Security insights** column in the table. If the **Security insights** column is not visible, click view_column **Column display options** and select **Security insights**. 

This column shows a summary of all policy insights for the bucket. Each summary indicates the total number of excess permissions for all roles granted on that bucket.

  3. Find the bucket whose insights you want to view and click the policy insights summary in that row. This action opens the **Security recommendations** pane, which lists all principals who have a role on the bucket, their roles, and any policy insights associated with those roles. 

In this table, policy insights have the form `EXCESS/TOTAL excess permissions`, where `EXCESS` is the number of permissions in the role that the principal does not need and `TOTAL` is the total number of permissions in the role. 




### gcloud

Use the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command to view all bucket-level policy insights for your project. 

Before you run the command, replace the following values: 

  * `PROJECT_ID`: The ID of the project that you want to list insights for. 
  * `LOCATION`: The location of the buckets whose insights you want to list. 


    
    
    gcloud recommender insights list --insight-type=google.iam.policy.Insight \
        --project=PROJECT_ID \
        --location=LOCATION\
        --filter="insightSubtype:PERMISSIONS_USAGE_STORAGE_BUCKET"

The output lists all of the bucket-level policy insights for your project in the specified location. For example: 
    
    
    INSIGHT_ID                            CATEGORY  INSIGHT_STATE  LAST_REFRESH_TIME     SEVERITY  INSIGHT_SUBTYPE                   DESCRIPTION
    00dd7eb5-15c2-4fb3-a9b2-1a85f842462b  SECURITY  ACTIVE         2022-05-24T07:00:00Z  CRITICAL  PERMISSIONS_USAGE_STORAGE_BUCKET  2 of the permissions in this role binding were used in the past 90 days.
    04307297-f57c-416d-9323-38abac450db0  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       PERMISSIONS_USAGE_STORAGE_BUCKET  2 of the permissions in this role binding were used in the past 90 days.
    04845da5-74ba-46b4-a0f3-47d83095c261  SECURITY  ACTIVE         2022-05-24T07:00:00Z  CRITICAL  PERMISSIONS_USAGE_STORAGE_BUCKET  1 of the permissions in this role binding were used in the past 90 days.
    0a39f643-d7a8-4c11-b490-fecd74290fb5  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       PERMISSIONS_USAGE_STORAGE_BUCKET  2 of the permissions in this role binding were used in the past 90 days.
    0a4cee48-777b-4dea-a2b0-702b70da4b6f  SECURITY  ACTIVE         2022-05-24T07:00:00Z  CRITICAL  PERMISSIONS_USAGE_STORAGE_BUCKET  0 of the permissions in this role binding were used in the past 90 days.
    0b2d147c-b26e-4afe-8fab-449c6e793750  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       PERMISSIONS_USAGE_STORAGE_BUCKET  0 of the permissions in this role binding were used in the past 90 days.
    0b5eacc5-ba9a-45f6-aea2-bcdc33ce2a2d  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       PERMISSIONS_USAGE_STORAGE_BUCKET  1 of the permissions in this role binding were used in the past 90 days.
    0bb3032d-721c-44e8-b464-5293f235281c  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       PERMISSIONS_USAGE_STORAGE_BUCKET  3 of the permissions in this role binding were used in the past 90 days.

### REST

The Recommender API's `[insights.list](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list)` method lists all bucket-level policy insights for your project. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: The ID of the project that you want to list insights for.
  * `LOCATION`: The location of the buckets whose insights you want to list. 



HTTP method and URL: 
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.iam.policy.Insight/insights?filter=insightSubtype%20%3D%20PERMISSIONS_USAGE_STORAGE_BUCKET

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.iam.policy.Insight/insights?filter=insightSubtype%20%3D%20PERMISSIONS_USAGE_STORAGE_BUCKET"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.iam.policy.Insight/insights?filter=insightSubtype%20%3D%20PERMISSIONS_USAGE_STORAGE_BUCKET" | Select-Object -Expand Content

The response lists all of the bucket-level policy insights for your project in the specified location. For example: 
    
    
    {
      "insights": [
        {
          "name": "projects/123456789012/locations/us/insightTypes/google.iam.policy.Insight/insights/00dd7eb5-15c2-4fb3-a9b2-1a85f842462b",
          "description": "2 of the permissions in this role binding were used in the past 90 days.",
          "content": {
            "role": "roles/storage.legacyBucketReader",
            "member": "allUsers",
            "condition": {
              "expression": "",
              "title": "",
              "description": "",
              "location": ""
            },
            "exercisedPermissions": [
              {
                "permission": "storage.buckets.get"
              },
              {
                "permission": "storage.objects.list"
              }
            ],
            "inferredPermissions": [],
            "currentTotalPermissionsCount": "3"
          },
          "lastRefreshTime": "2022-05-24T07:00:00Z",
          "observationPeriod": "7772400s",
          "stateInfo": {
            "state": "ACTIVE"
          },
          "category": "SECURITY",
          "associatedRecommendations": [
            {
              "recommendation": "projects/123456789012/locations/us/recommenders/google.iam.policy.Recommender/recommendations/4a31a9d4-5132-4616-8a1f-fb07fad01883"
            }
          ],
          "targetResources": [
            "//storage.googleapis.com/bucket-1"
          ],
          "insightSubtype": "PERMISSIONS_USAGE_STORAGE_BUCKET",
          "etag": "\"2a8784e529b80aea\"",
          "severity": "CRITICAL"
        },
        {
          "name": "projects/123456789012/locations/us/insightTypes/google.iam.policy.Insight/insights/04307297-f57c-416d-9323-38abac450db0",
          "description": "2 of the permissions in this role binding were used in the past 90 days.",
          "content": {
            "role": "roles/storage.legacyBucketReader",
            "member": "projectViewer:my-project",
            "condition": {
              "expression": "",
              "title": "",
              "description": "",
              "location": ""
            },
            "exercisedPermissions": [
              {
                "permission": "storage.buckets.get"
              },
              {
                "permission": "storage.objects.list"
              }
            ],
            "inferredPermissions": [],
            "currentTotalPermissionsCount": "3"
          },
          "lastRefreshTime": "2022-05-24T07:00:00Z",
          "observationPeriod": "7772400s",
          "stateInfo": {
            "state": "ACTIVE"
          },
          "category": "SECURITY",
          "associatedRecommendations": [
            {
              "recommendation": "projects/123456789012/locations/us/recommenders/google.iam.policy.Recommender/recommendations/f3198e63-7f76-462e-a980-8e6370ff32d6"
            }
          ],
          "targetResources": [
            "//storage.googleapis.com/bucket-2"
          ],
          "insightSubtype": "PERMISSIONS_USAGE_STORAGE_BUCKET",
          "etag": "\"5b60b935f27caf2c\"",
          "severity": "LOW"
        }
      ]
    }

To learn more about the components of an insight, see Review bucket-level policy insights on this page. 

## Get a single bucket-level policy insight

To get more information about a single insight, including the insight's description, status, and any recommendations it's associated with, use one of the following methods: 

### Console

  1. In the Google Cloud console, go to the **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Ensure that the **Security insights** column is visible. 
  3. Find the **Security insights** column in the table. This column shows a summary of all policy insights for the bucket. Each summary indicates the total number of excess permissions for all roles granted on that bucket.

If the **Security insights** column is not visible, click view_column **Column display options** and select **Security insights**. Then, find the column in the table. 

  4. Find the bucket whose insights you want to view and click the policy insights summary in that row. This opens a pane that lists all principals who have a role on the bucket, their roles, and any policy insights associated with those roles. 
  5. In the **Security insights** column, click a policy insight. Policy insights have the form `EXCESS/TOTAL excess permissions`, where `EXCESS` is the number of permissions in the role that the principal does not need and `TOTAL` is the total number of permissions in the role. 



The Google Cloud console opens a pane showing the details of the insight. 

### gcloud

Use the [`gcloud recommender insights describe`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/describe) command with your insight ID to view information about a single insight. 

  * `INSIGHT_ID`: The ID of the insight that you want to view. To find the ID, list the insights for your project. 
  * `PROJECT_ID`: The ID of the project that you want to manage insights for.
  * `LOCATION`: The location of the bucket whose insight you want to get. 


    
    
    gcloud recommender insights describe INSIGHT_ID \
        --insight-type=google.iam.policy.Insight \
        --project=PROJECT_ID \
        --location=LOCATION

The output shows the insight in detail. For example, the following insight indicates that all users (`allUsers`) have the Storage Legacy Bucket Reader role (`roles/storage.legacyBucketReader`) on the bucket `bucket-1`, but that only two permissions in that role were used in the past 90 days: 
    
    
    associatedRecommendations:
    - recommendation: projects/123456789012/locations/us/recommenders/google.iam.policy.Recommender/recommendations/4a31a9d4-5132-4616-8a1f-fb07fad01883
    category: SECURITY
    content:
      condition:
        description: ''
        expression: ''
        location: ''
        title: ''
      currentTotalPermissionsCount: '3'
      exercisedPermissions:
      - permission: storage.buckets.get
      - permission: storage.objects.list
      inferredPermissions: []
      member: allUsers
      role: roles/storage.legacyBucketReader
    description: 2 of the permissions in this role binding were used in the past 90 days.
    etag: '"2a8784e529b80aea"'
    insightSubtype: PERMISSIONS_USAGE_STORAGE_BUCKET
    lastRefreshTime: '2022-05-24T07:00:00Z'
    name: projects/123456789012/locations/us/insightTypes/google.iam.policy.Insight/insights/00dd7eb5-15c2-4fb3-a9b2-1a85f842462b
    observationPeriod: 7772400s
    severity: CRITICAL
    stateInfo:
      state: ACTIVE
    targetResources:
    - //storage.googleapis.com/bucket-1

To learn more about the components of an insight, see Review bucket-level policy insights on this page. 

### REST

The Recommender API's `[insights.get](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/get)` method gets a single insight. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: The ID of the project that you want to manage insights for. 
  * `LOCATION`: The location of the bucket whose insight you want to get. 
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

The response contains the insight. For example, the following insight indicates that all users (`allUsers`) have the Storage Legacy Bucket Reader role (`roles/storage.legacyBucketReader`) on the bucket `bucket-1`, but that only two permissions in that role were used in the past 90 days: 
    
    
    {
      "name": "projects/123456789012/locations/us/insightTypes/google.iam.policy.Insight/insights/00dd7eb5-15c2-4fb3-a9b2-1a85f842462b",
      "description": "2 of the permissions in this role binding were used in the past 90 days.",
      "content": {
        "role": "roles/storage.legacyBucketReader",
        "member": "allUsers",
        "condition": {
          "expression": "",
          "title": "",
          "description": "",
          "location": ""
        },
        "exercisedPermissions": [
          {
            "permission": "storage.buckets.get"
          },
          {
            "permission": "storage.objects.list"
          }
        ],
        "inferredPermissions": [],
        "currentTotalPermissionsCount": "3"
      },
      "lastRefreshTime": "2022-05-24T07:00:00Z",
      "observationPeriod": "7772400s",
      "stateInfo": {
        "state": "ACTIVE"
      },
      "category": "SECURITY",
      "associatedRecommendations": [
        {
          "recommendation": "projects/123456789012/locations/us/recommenders/google.iam.policy.Recommender/recommendations/4a31a9d4-5132-4616-8a1f-fb07fad01883"
        }
      ],
      "targetResources": [
        "//storage.googleapis.com/bucket-1"
      ],
      "insightSubtype": "PERMISSIONS_USAGE_STORAGE_BUCKET",
      "etag": "\"2a8784e529b80aea\"",
      "severity": "CRITICAL"
    }

To learn more about the components of an insight, see Review bucket-level policy insights on this page. 

## Review bucket-level policy insights

After you get a single insight, you can review its contents to understand the pattern of resource usage that it highlights. 

### Console

When you click a policy insight in the Google Cloud console, the Google Cloud console opens a pane showing the details of the insight. The appearance of these details depends on whether the insight is associated with a recommendation. 

**Note:** You can check if an insight is associated with a recommendation by looking for the **Recommendation available** ![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-yes.svg) icon in the **Security insights** column. 

If the insight is associated with a recommendation, the pane shows the [details of the recommendation](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations-buckets#review). 

If the insight is not associated with a recommendation, the pane shows a list of all permissions in the role. The permissions that the principal used appear at the top of the list, followed by the excess permissions. 

![](https://docs.cloud.google.com/static/policy-intelligence/img/storage-bucket-insight.png)![](https://docs.cloud.google.com/static/policy-intelligence/img/storage-bucket-insight.png)

**Note** : If an insight is for a [basic role](https://docs.cloud.google.com/iam/docs/roles-overview#basic), the list of permissions in the Google Cloud console might not include all of the permissions that a principal needs. This is because some services use basic roles to indirectly grant additional roles. The list of permissions might not include permissions from these additional roles, even if a principal used them. Role recommendations automatically account for this discrepancy. 

Indirectly granted roles include roles granted through [Cloud Storage convenience values](https://docs.cloud.google.com/storage/docs/access-control/iam#convenience-values) and [BigQuery special group membership](https://docs.cloud.google.com/bigquery/docs/access-control-basic-roles). 

### gcloud

An insight's content is determined by its subtypes. Bucket-level policy insights (`google.iam.policy.Insight`) insights have the `PERMISSIONS_USAGE_STORAGE_BUCKET` subtype. 

`PERMISSIONS_USAGE_STORAGE_BUCKET` insights have the following components, not necessarily in this order: 

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
    * `LOCATION`: The location of the bucket that the insight is for. 
    * `INSIGHT_ID`: A unique ID for the insight.
  * `observationPeriod`: The time period leading up to the insight. The source data used to generate the insight ends at `lastRefreshTime` and begins at `lastRefreshTime` minus `observationPeriod`. 
  * `stateInfo`: Insights go through multiple state transitions after they are proposed: 

    * `ACTIVE`: The insight has been generated, but either no actions have been taken, or an action was taken without updating the insight's state. Active insights are updated when the underlying data changes. 
    * `ACCEPTED`: Some action has been taken based on the insight. Insights become accepted when an associated recommendation was marked `CLAIMED`, `SUCCEEDED`, or `FAILED`, or the insight was accepted directly. When an insight is in the `ACCEPTED` state, the content of the insight cannot change. Accepted insights are retained for 90 days after they are accepted. 
  * `targetResources`: The [full resource name ](https://docs.cloud.google.com/iam/docs/full-resource-names) of the bucket that the insight is for. For example, `//storage.googleapis.com/my-bucket`. 



### REST

An insight's content is determined by its subtypes. Bucket-level policy insights (`google.iam.policy.Insight`) insights have the `PERMISSIONS_USAGE_STORAGE_BUCKET` subtype. 

`PERMISSIONS_USAGE_STORAGE_BUCKET` insights have the following components, not necessarily in this order: 

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
    * `LOCATION`: The location of the bucket that the insight is for. 
    * `INSIGHT_ID`: A unique ID for the insight.
  * `observationPeriod`: The time period leading up to the insight. The source data used to generate the insight ends at `lastRefreshTime` and begins at `lastRefreshTime` minus `observationPeriod`. 
  * `stateInfo`: Insights go through multiple state transitions after they are proposed: 

    * `ACTIVE`: The insight has been generated, but either no actions have been taken, or an action was taken without updating the insight's state. Active insights are updated when the underlying data changes. 
    * `ACCEPTED`: Some action has been taken based on the insight. Insights become accepted when an associated recommendation was marked `CLAIMED`, `SUCCEEDED`, or `FAILED`, or the insight was accepted directly. When an insight is in the `ACCEPTED` state, the content of the insight cannot change. Accepted insights are retained for 90 days after they are accepted. 
  * `targetResources`: The [full resource name ](https://docs.cloud.google.com/iam/docs/full-resource-names) of the bucket that the insight is for. For example, `//storage.googleapis.com/my-bucket`. 



## Mark a bucket-level policy insight as `ACCEPTED`

If you take action based on an active insight, you can mark that insight as `ACCEPTED`. The `ACCEPTED` state tells the Recommender API that you have taken action based on this insight, which helps refine your recommendations. 

Accepted insights are retained for 90 days after they are marked as `ACCEPTED`. 

### Console

If an insight is associated with a recommendation, [applying the recommendation](https://docs.cloud.google.com/iam/docs/recommender-managing) changes the insight's state to `ACCEPTED`. 

To mark an insight as `ACCEPTED` without applying a recommendation, use the gcloud CLI or REST API. 

### gcloud

Use the [ `gcloud recommender insights mark-accepted`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted) command with your insight ID to mark an insight as `ACCEPTED`. 

  * `INSIGHT_ID`: The ID of the insight that you want to view. To find the ID, list the insights for your project. 
  * `PROJECT_ID`: The ID of the project that you want to manage insights for.
  * `LOCATION`: The location of the bucket whose insight you want to mark as `ACCEPTED`. 
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
    - recommendation: projects/123456789012/locations/us/recommenders/google.iam.policy.Recommender/recommendations/4a31a9d4-5132-4616-8a1f-fb07fad01883
    category: SECURITY
    content:
      condition:
        description: ''
        expression: ''
        location: ''
        title: ''
      currentTotalPermissionsCount: '3'
      exercisedPermissions:
      - permission: storage.buckets.get
      - permission: storage.objects.list
      inferredPermissions: []
      member: allUsers
      role: roles/storage.legacyBucketReader
    description: 2 of the permissions in this role binding were used in the past 90 days.
    etag: '"0187c0362e4bcea7"'
    insightSubtype: PERMISSIONS_USAGE_STORAGE_BUCKET
    lastRefreshTime: '2022-05-24T07:00:00Z'
    name: projects/123456789012/locations/us/insightTypes/google.iam.policy.Insight/insights/00dd7eb5-15c2-4fb3-a9b2-1a85f842462b
    observationPeriod: 7772400s
    severity: CRITICAL
    **stateInfo :
      state: ACCEPTED**
    targetResources:
    - //storage.googleapis.com/bucket-1

To learn more about the state info of an insight, see Review bucket-level policy insights on this page. 

### REST

The Recommender API's `[insights.markAccepted](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/markAccepted)` method marks an insight as `ACCEPTED`. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: The ID of the project that you want to manage insights for. 
  * `LOCATION`: The location of the bucket whose insight you want to mark as `ACCEPTED`. 
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
      "name": "projects/123456789012/locations/us/insightTypes/google.iam.policy.Insight/insights/00dd7eb5-15c2-4fb3-a9b2-1a85f842462b",
      "description": "2 of the permissions in this role binding were used in the past 90 days.",
      "content": {
        "role": "roles/storage.legacyBucketReader",
        "member": "allUsers",
        "condition": {
          "expression": "",
          "title": "",
          "description": "",
          "location": ""
        },
        "exercisedPermissions": [
          {
            "permission": "storage.buckets.get"
          },
          {
            "permission": "storage.objects.list"
          }
        ],
        "inferredPermissions": [],
        "currentTotalPermissionsCount": "3"
      },
      "lastRefreshTime": "2022-05-24T07:00:00Z",
      "observationPeriod": "7772400s",
      **"stateInfo": {
        "state": "ACCEPTED"
      },**
      "category": "SECURITY",
      "associatedRecommendations": [
        {
          "recommendation": "projects/123456789012/locations/us/recommenders/google.iam.policy.Recommender/recommendations/4a31a9d4-5132-4616-8a1f-fb07fad01883"
        }
      ],
      "targetResources": [
        "//storage.googleapis.com/bucket-1"
      ],
      "insightSubtype": "PERMISSIONS_USAGE_STORAGE_BUCKET",
      "etag": "\"9a5485cdc1f05b58\"",
      "severity": "CRITICAL"
    }

To learn more about the state info of an insight, see Review bucket-level policy insights on this page. 

## What's next

  * Learn how to [view and apply policy recommendations for Cloud Storage buckets](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations-buckets).
  * Use the [Active Assist](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems) to view and manage all recommendations for your project, including IAM recommendations.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

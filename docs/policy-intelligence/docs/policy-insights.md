---
url: https://docs.cloud.google.com/policy-intelligence/docs/policy-insights/
title: Review policy insights for projects, folders, and organizations \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:53.105335+00:00
---

# Review policy insights for projects, folders, and organizations  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/policy-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Review policy insights for projects, folders, and organizations Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to manage policy insights, which are machine learning-based findings about permission usage. Policy insights can help you identify which principals have permissions that they don't need. 

This page focuses on policy insights for projects, folders, and organizations. Recommender also offers policy insights for the following resource types: 

  * [Cloud Storage buckets](https://docs.cloud.google.com/policy-intelligence/docs/policy-insights-buckets)
  * [BigQuery datasets](https://docs.cloud.google.com/policy-intelligence/docs/policy-insights-datasets)



Policy insights are sometimes linked to [ role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview). Role recommendations suggest actions that you can take to remediate the issues identified by policy insights. 

**Note** : Policy insights might not list all of the permissions that a principal needs. For example, policy insights don't list permissions used by non-public, early access features. To safely replace a principal's role, use role recommendations. 

## Before you begin

  * Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Be familiar with [IAM role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview).
  * You must have [ Premium or Enterprise](https://docs.cloud.google.com/security-command-center/pricing#security-command-center-pricing) activated at the organization or project level to use policy insights. For more information, see [ Billing questions](https://docs.cloud.google.com/policy-intelligence/docs/billing-questions).
  * Optional: Read about [Recommender insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights).



### Required roles

To get the permissions that you need to manage policy insights, ask your administrator to grant you the following IAM roles on the project, folder, or organization that you want to manage insights for: 

  * To view policy insights: [IAM Recommender Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamViewer) (`roles/recommender.iamViewer`) 
  * To modify policy insights: [IAM Recommender Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamAdmin) (`roles/recommender.iamAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage policy insights. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage policy insights:

  * To view policy insights: 
    * `recommender.iamPolicyInsights.get`
    * `recommender.iamPolicyInsights.list`
  * To modify policy insights: `recommender.iamPolicyInsights.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List policy insights

To list all policy insights for your project, folder, or organization, use one of the following methods: 

### Console

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.



The **Security insights** column shows all security-related insights for your project, including policy insights. Policy insights have the form `EXCESS/TOTAL excess permissions`, where `EXCESS` is the number of permissions in the role that the principal does not need and `TOTAL` is the total number of permissions in the role. 

### gcloud

Use the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command to view all policy insights for your project, folder, or organization. 

Before you run the command, replace the following values: 

  * `RESOURCE_TYPE`: The resource type that you want to list insights for. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to list insights for. 


    
    
    gcloud recommender insights list --insight-type=google.iam.policy.Insight \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=global

The output lists all of the policy insights for your project, folder, or organization. For example: 
    
    
    INSIGHT_ID                            CATEGORY  INSIGHT_STATE  LAST_REFRESH_TIME     SEVERITY  INSIGHT_SUBTYPE    DESCRIPTION
    00133c0b-5431-4b30-9172-7c903aa4af24  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       PERMISSIONS_USAGE  9 of the permissions in this role binding were used in the past 90 days.
    0161f2eb-acb7-4a5e-ad52-50284beaa312  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       PERMISSIONS_USAGE  0 of the permissions in this role binding were used in the past 90 days.
    01ea0d0d-e9a1-4073-9367-5a934a857fb4  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       PERMISSIONS_USAGE  1 of the permissions in this role binding were used in the past 90 days.
    039407bc-a25b-4aeb-b573-5c851f2e9833  SECURITY  ACTIVE         2022-05-24T07:00:00Z  HIGH      PERMISSIONS_USAGE  52 of the permissions in this role binding were used in the past 90 days.
    0541df88-8bc3-44b3-ad5d-9cb372630aeb  SECURITY  ACTIVE         2022-05-24T07:00:00Z  HIGH      PERMISSIONS_USAGE  31 of the permissions in this role binding were used in the past 90 days.
    07841f74-02ce-4de8-bbe6-fc4eabb68568  SECURITY  ACTIVE         2022-05-24T07:00:00Z  HIGH      PERMISSIONS_USAGE  0 of the permissions in this role binding were used in the past 90 days.
    07713094-fdee-4475-9c43-cd53d52c9de1  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       PERMISSIONS_USAGE  2 of the permissions in this role binding were used in the past 90 days.
    0a438d19-9d63-4749-aadd-578aa4e77908  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       PERMISSIONS_USAGE  0 of the permissions in this role binding were used in the past 90 days.
    f4292f55-105b-4744-9dc3-fcacf59685bb  SECURITY  ACTIVE         2022-05-24T07:00:00Z  HIGH      PERMISSIONS_USAGE  4 of the permissions in this role binding were used in the past 90 days.

### REST

The Recommender API's `[insights.list](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list)` method lists all policy insights for your project, folder, or organization. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type that you want to list insights for. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to list insights for. 
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    GET https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.Insight/insights

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.Insight/insights"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.Insight/insights" | Select-Object -Expand Content

The response lists all of the policy insights for your project, folder, or organization. For example: 
    
    
    {
      "insights": [
        {
          "name": "projects/123456789012/locations/global/insightTypes/google.iam.policy.Insight/insights/07841f74-02ce-4de8-bbe6-fc4eabb68568",
          "description": "0 of the permissions in this role binding were used in the past 90 days.",
          "content": {
            "role": "roles/viewer",
            "member": "serviceAccount:my-service-account@my-project.iam.gserviceaccount.com",
            "condition": {
              "expression": "",
              "title": "",
              "description": "",
              "location": ""
            },
            "exercisedPermissions": [],
            "inferredPermissions": []
          },
          "lastRefreshTime": "2022-05-24T07:00:00Z",
          "observationPeriod": "7776000s",
          "stateInfo": {
            "state": "ACTIVE"
          },
          "category": "SECURITY",
          "associatedRecommendations": [
            {
              "recommendation": "projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/recommendations/b1932220-867d-43d1-bd74-fb95876ab656"
            }
          ],
          "targetResources": [
            "//cloudresourcemanager.googleapis.com/projects/123456789012"
          ],
          "insightSubtype": "PERMISSIONS_USAGE",
          "etag": "\"b153ab487e4ae100\"",
          "severity": "HIGH"
        },
        {
          "name": "projects/123456789012/locations/global/insightTypes/google.iam.policy.Insight/insights/f4292f55-105b-4744-9dc3-fcacf59685bb",
          "description": "4 of the permissions in this role binding were used in the past 90 days.",
          "content": {
            "role": "roles/owner",
            "member": "serviceAccount:my-service-account2@my-project.iam.gserviceaccount.com",
            "condition": {
              "expression": "",
              "title": "",
              "description": "",
              "location": ""
            },
            "exercisedPermissions": [
              {
                "permission": "iam.roles.create"
              },
              {
                "permission": "iam.roles.delete"
              },
              {
                "permission": "iam.roles.list"
              },
              {
                "permission": "iam.roles.update"
              }
            ],
            "inferredPermissions": []
          },
          "lastRefreshTime": "2022-05-24T07:00:00Z",
          "observationPeriod": "7776000s",
          "stateInfo": {
            "state": "ACTIVE"
          },
          "category": "SECURITY",
          "associatedRecommendations": [
            {
              "recommendation": "projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/recommendations/6ab16c1d-edce-45e5-8d82-570fdd49892a"
            }
          ],
          "targetResources": [
            "//cloudresourcemanager.googleapis.com/projects/123456789012"
          ],
          "insightSubtype": "PERMISSIONS_USAGE",
          "etag": "\"49bb705553338fc3\"",
          "severity": "HIGH"
        }
      ]
    }

To learn more about the components of an insight, see Review policy insights on this page. 

## Get a single policy insight

To get more information about a single insight, including the insight's description, status, and any recommendations it's associated with, use one of the following methods: 

### Console

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.
  3. In the **Security insights** column, click a policy insight. Policy insights have the form `EXCESS/TOTAL excess permissions`, where `EXCESS` is the number of permissions in the role that the principal does not need and `TOTAL` is the total number of permissions in the role. 




The Google Cloud console opens a pane showing the details of the insight. 

### gcloud

Use the [`gcloud recommender insights describe`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/describe) command with your insight ID to view information about a single insight. 

  * `INSIGHT_ID`: The ID of the insight that you want to view. To find the ID, list the insights for your project, folder, or organization. 
  * `RESOURCE_TYPE`: The resource type that you want to manage insights for. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to manage insights for. 


    
    
    gcloud recommender insights describe INSIGHT_ID \
        --insight-type=google.iam.policy.Insight \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=global

The output shows the insight in detail. For example, the following insight indicates that `my-service-account@my-project.iam.gserviceaccount.com` has used zero permissions from the Viewer role (`roles/viewer`) in the past 90 days: 
    
    
    associatedRecommendations:
    - recommendation: projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/recommendations/0573b702-96a5-4622-a916-c762e7b0731f
    category: SECURITY
    content:
      condition:
        description: ''
        expression: ''
        location: ''
        title: ''
      exercisedPermissions: []
      inferredPermissions: []
      member: serviceAccount:my-service-account@my-project.iam.gserviceaccount.com
      role: roles/viewer
    description: 0 of the permissions in this role binding were used in the past 90 days.
    etag: '"d3cdec23cc712bd0"'
    insightSubtype: PERMISSIONS_USAGE
    lastRefreshTime: '2020-07-11T07:00:00Z'
    name: projects/123456789012/locations/global/insightTypes/google.iam.policy.Insight/insights/0d3ce433-f067-4e78-b6ae-03d7d1f6f040
    observationPeriod: 7776000s
    severity: HIGH
    stateInfo:
      state: ACTIVE
    targetResources:
    - //cloudresourcemanager.googleapis.com/projects/123456789012

To learn more about the components of an insight, see Review policy insights on this page. 

### REST

The Recommender API's `[insights.get](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/get)` method gets a single insight. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type that you want to manage insights for. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to manage insights for. 
  * `INSIGHT_ID`: The ID of the insight that you want to view. If you don't know the insight ID, you can find it by listing the insights in your project, folder, or organization. The ID of an insight is everything after `insights/` in the `name` field for the insight. 
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    GET https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID" | Select-Object -Expand Content

The response contains the insight. For example, the following insight indicates that `my-service-account@my-project.iam.gserviceaccount.com` has used zero permissions from the Viewer role (`roles/viewer`) in the past 90 days: 
    
    
    {
      "name": "projects/123456789012/locations/global/insightTypes/google.iam.policy.Insight/insights/07841f74-02ce-4de8-bbe6-fc4eabb68568",
      "description": "0 of the permissions in this role binding were used in the past 90 days.",
      "content": {
        "role": "roles/viewer",
        "member": "serviceAccount:my-service-account@my-project.iam.gserviceaccount.com",
        "condition": {
          "expression": "",
          "title": "",
          "description": "",
          "location": ""
        },
        "exercisedPermissions": [],
        "inferredPermissions": []
      },
      "lastRefreshTime": "2022-05-24T07:00:00Z",
      "observationPeriod": "7776000s",
      "stateInfo": {
        "state": "ACTIVE"
      },
      "category": "SECURITY",
      "associatedRecommendations": [
        {
          "recommendation": "projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/recommendations/b1932220-867d-43d1-bd74-fb95876ab656"
        }
      ],
      "targetResources": [
        "//cloudresourcemanager.googleapis.com/projects/123456789012"
      ],
      "insightSubtype": "PERMISSIONS_USAGE",
      "etag": "\"d3cdec23cc712bd0\"",
      "severity": "HIGH"
    }

To learn more about the components of an insight, see Review policy insights on this page. 

## Review policy insights

After you get a single insight, you can review its contents to understand the pattern of resource usage that it highlights. 

### Console

When you click a policy insight in the Google Cloud console, the Google Cloud console opens a pane showing the details of the insight. The appearance of these details depends on whether the insight is associated with a recommendation. 

**Note:** You can check if an insight is associated with a recommendation by looking for the **Recommendation available** ![](https://docs.cloud.google.com/static/policy-intelligence/img/recommender-yes.svg) icon in the **Security insights** column. 

If the insight is associated with a recommendation, the pane shows the [details of the recommendation](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations#review). 

If the insight is not associated with a recommendation, the pane shows a list of all permissions in the role. The permissions that the principal used appear at the top of the list, followed by the excess permissions. 

![](https://docs.cloud.google.com/static/policy-intelligence/img/policy-insight-details.png)![](https://docs.cloud.google.com/static/policy-intelligence/img/policy-insight-details.png)

**Note** : If an insight is for a [basic role](https://docs.cloud.google.com/iam/docs/roles-overview#basic), the list of permissions in the Google Cloud console might not include all of the permissions that a principal needs. This is because some services use basic roles to indirectly grant additional roles. The list of permissions might not include permissions from these additional roles, even if a principal used them. Role recommendations automatically account for this discrepancy. 

Indirectly granted roles include roles granted through [Cloud Storage convenience values](https://docs.cloud.google.com/storage/docs/access-control/iam#convenience-values) and [BigQuery special group membership](https://docs.cloud.google.com/bigquery/docs/access-control-basic-roles). 

### gcloud

An insight's content is determined by its subtypes. Policy insights (`google.iam.policy.Insight`) insights have the `PERMISSIONS_USAGE` subtype. 

`PERMISSIONS_USAGE` insights have the following components, not necessarily in this order: 

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
        
        RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID

The placeholders have the following values:

    * `RESOURCE_TYPE`: The resource type that the insight was generated for. 
    * `RESOURCE_ID`: The ID of the project, folder, or organization where the insight was generated. 
    * `INSIGHT_ID`: A unique ID for the insight.
  * `observationPeriod`: The time period leading up to the insight. The source data used to generate the insight ends at `lastRefreshTime` and begins at `lastRefreshTime` minus `observationPeriod`. 
  * `stateInfo`: Insights go through multiple state transitions after they are proposed: 

    * `ACTIVE`: The insight has been generated, but either no actions have been taken, or an action was taken without updating the insight's state. Active insights are updated when the underlying data changes. 
    * `ACCEPTED`: Some action has been taken based on the insight. Insights become accepted when an associated recommendation was marked `CLAIMED`, `SUCCEEDED`, or `FAILED`, or the insight was accepted directly. When an insight is in the `ACCEPTED` state, the content of the insight cannot change. Accepted insights are retained for 90 days after they are accepted. 
  * `targetResources`: The [full resource name ](https://docs.cloud.google.com/iam/docs/full-resource-names) of the project, folder, or organization that the insight is for. For example, `//cloudresourcemanager.googleapis.com/projects/123456789012`. 



### REST

An insight's content is determined by its subtypes. Policy insights (`google.iam.policy.Insight`) insights have the `PERMISSIONS_USAGE` subtype. 

`PERMISSIONS_USAGE` insights have the following components, not necessarily in this order: 

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
        
        RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID

The placeholders have the following values:

    * `RESOURCE_TYPE`: The resource type that the insight was generated for. 
    * `RESOURCE_ID`: The ID of the project, folder, or organization where the insight was generated. 
    * `INSIGHT_ID`: A unique ID for the insight.
  * `observationPeriod`: The time period leading up to the insight. The source data used to generate the insight ends at `lastRefreshTime` and begins at `lastRefreshTime` minus `observationPeriod`. 
  * `stateInfo`: Insights go through multiple state transitions after they are proposed: 

    * `ACTIVE`: The insight has been generated, but either no actions have been taken, or an action was taken without updating the insight's state. Active insights are updated when the underlying data changes. 
    * `ACCEPTED`: Some action has been taken based on the insight. Insights become accepted when an associated recommendation was marked `CLAIMED`, `SUCCEEDED`, or `FAILED`, or the insight was accepted directly. When an insight is in the `ACCEPTED` state, the content of the insight cannot change. Accepted insights are retained for 90 days after they are accepted. 
  * `targetResources`: The [full resource name ](https://docs.cloud.google.com/iam/docs/full-resource-names) of the project, folder, or organization that the insight is for. For example, `//cloudresourcemanager.googleapis.com/projects/123456789012`. 



## Mark a policy insight as `ACCEPTED`

If you take action based on an active insight, you can mark that insight as `ACCEPTED`. The `ACCEPTED` state tells the Recommender API that you have taken action based on this insight, which helps refine your recommendations. 

Accepted insights are retained for 90 days after they are marked as `ACCEPTED`. 

### Console

If an insight is associated with a recommendation, [applying the recommendation](https://docs.cloud.google.com/iam/docs/recommender-managing) changes the insight's state to `ACCEPTED`. 

To mark an insight as `ACCEPTED` without applying a recommendation, use the gcloud CLI or REST API. 

### gcloud

Use the [ `gcloud recommender insights mark-accepted`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted) command with your insight ID to mark an insight as `ACCEPTED`. 

  * `INSIGHT_ID`: The ID of the insight that you want to view. To find the ID, list the insights for your project, folder, or organization. 
  * `RESOURCE_TYPE`: The resource type that you want to manage insights for. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to manage insights for. 
  * `ETAG`: An identifier for a version of the insight. To get the `etag`, do the following: 

    1. Get the insight using the `gcloud recommender insights describe` command. 
    2. Find and copy the `etag` value from the output, including the enclosing quotes. For example, `"d3cdec23cc712bd0"`. 


    
    
    gcloud recommender insights mark-accepted INSIGHT_ID \
        --insight-type=google.iam.policy.Insight \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=global \
        --etag=ETAG

The output shows the insight, now with the state of `ACCEPTED`: 
    
    
    associatedRecommendations:
    - recommendation: projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/recommendations/0573b702-96a5-4622-a916-c762e7b0731f
    category: SECURITY
    content:
      condition:
        description: ''
        expression: ''
        location: ''
        title: ''
      exercisedPermissions: []
      inferredPermissions: []
      member: serviceAccount:my-service-account@my-project.iam.gserviceaccount.com
      role: roles/viewer
    description: 0 of the permissions in this role binding were used in the past 90 days.
    etag: '"b153ab487e4ae100"'
    insightSubtype: PERMISSIONS_USAGE
    lastRefreshTime: '2020-07-11T07:00:00Z'
    name: projects/123456789012/locations/global/insightTypes/google.iam.policy.Insight/insights/0d3ce433-f067-4e78-b6ae-03d7d1f6f040
    observationPeriod: 7776000s
    severity: HIGH
    **stateInfo :
      state: ACCEPTED**
    targetResources:
    - //cloudresourcemanager.googleapis.com/projects/123456789012

To learn more about the state info of an insight, see Review policy insights on this page. 

### REST

The Recommender API's `[insights.markAccepted](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/markAccepted)` method marks an insight as `ACCEPTED`. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type that you want to manage insights for. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to manage insights for. 
  * `INSIGHT_ID`: The ID of the insight that you want to view. If you don't know the insight ID, you can find it by listing the insights in your project, folder, or organization. The ID of an insight is everything after `insights/` in the `name` field for the insight. 
  * `ETAG`: An identifier for a version of the insight. To get the `etag`, do the following: 
    1. Get the insight using the `insights.get` method.
    2. Find and copy the `etag` value from the response.
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    POST https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID:markAccepted

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
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID:markAccepted"

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
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.iam.policy.Insight/insights/INSIGHT_ID:markAccepted" | Select-Object -Expand Content

The response contains the insight, now with the state of `ACCEPTED`: 
    
    
    {
      "name": "projects/1234567890/locations/global/insightTypes/google.iam.policy.Insight/insights/07841f74-02ce-4de8-bbe6-fc4eabb68568",
      "description": "0 of the permissions in this role binding were used in the past 90 days.",
      "content": {
        "role": "roles/viewer",
        "member": "serviceAccount:my-service-account@my-project.iam.gserviceaccount.com",
        "condition": {
          "expression": "",
          "title": "",
          "description": "",
          "location": ""
        },
        "exercisedPermissions": [],
        "inferredPermissions": []
      },
      "lastRefreshTime": "2022-05-24T07:00:00Z",
      "observationPeriod": "7776000s",
      **"stateInfo": {
        "state": "ACCEPTED"
        },**
      "category": "SECURITY",
      "associatedRecommendations": [
        {
          "recommendation": "projects/1234567890/locations/global/recommenders/google.iam.policy.Recommender/recommendations/b1932220-867d-43d1-bd74-fb95876ab656"
        }
      ],
      "targetResources": [
        "//cloudresourcemanager.googleapis.com/projects/123456789012"
      ],
      "insightSubtype": "PERMISSIONS_USAGE",
      "etag": "\"b153ab487e4ae100\"",
      "severity": "HIGH"
    }

To learn more about the state info of an insight, see Review policy insights on this page. 

## What's next

  * Learn how to [view and apply policy recommendations](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations).
  * Use the [Active Assist](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems) to view and manage all recommendations for your project, including IAM recommendations.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

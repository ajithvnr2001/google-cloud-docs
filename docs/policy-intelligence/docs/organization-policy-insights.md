---
url: https://docs.cloud.google.com/policy-intelligence/docs/organization-policy-insights/
title: Review organization policy insights for projects, folders, and organizations \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:08.435201+00:00
---

# Review organization policy insights for projects, folders, and organizations  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/organization-policy-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Review organization policy insights for projects, folders, and organizations Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to manage organization policy insights, which are findings about resource configuration and usage. Organization policy insights can help you identify resources that are not protected by organization policies. 

Organization policy insights are sometimes linked to [ organization policy recommendations](https://docs.cloud.google.com/policy-intelligence/docs/organization-policy-recommendations-overview). Organization policy recommendations suggest actions that you can take to remediate the issues identified by organization policy insights. 

## Before you begin

  * Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Be familiar with [organization policy recommendations](https://docs.cloud.google.com/policy-intelligence/docs/organization-policy-recommendations-overview).
  * Optional: Read about [Recommender insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights).



### Required roles

To get the permissions that you need to view and modify organization policy insights, ask your administrator to grant you the [Org Policy Recommender Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.orgPolicyAdmin) (`roles/recommender.orgPolicyAdmin`) IAM role on the resource that you want to manage insights for (project, folder, or organization). For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view and modify organization policy insights. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view and modify organization policy insights:

  * `recommender.orgPolicyInsights.get`
  * `recommender.orgPolicyInsights.list`
  * `recommender.orgPolicyInsights.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List organization policy insights

To list all organization policy insights for your project, folder, or organization, use one of the following methods: 

### gcloud

Use the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command to view all organization policy insights for your project, folder, or organization. 

Before you run the command, replace the following values: 

  * `RESOURCE_TYPE`: The resource type that you want to list insights for. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to list insights for. 


    
    
    gcloud recommender insights list --insight-type=google.orgpolicy.policy.Insight \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=global

The output lists all of the organization policy insights for your project, folder, or organization. For example: 
    
    
    INSIGHT_ID                            CATEGORY  INSIGHT_STATE  LAST_REFRESH_TIME     SEVERITY  INSIGHT_SUBTYPE                                          DESCRIPTION
    66d543f3-845d-49d6-a26b-80d84804d8a8  SECURITY  ACTIVE         2024-12-10T08:00:00Z  HIGH      RESOURCE_VIOLATION_DISABLE_SERVICE_ACCOUNT_KEY_CREATION  Scanned 3 resources and found 0 violations for constraints/iam.managed.disableServiceAccountKeyCreation.

### REST

The Recommender API's `[insights.list](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list)` method lists all organization policy insights for your project, folder, or organization. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type that you want to list insights for. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to list insights for. 
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    GET https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights" | Select-Object -Expand Content

The response lists all of the organization policy insights for your project, folder, or organization. For example: 
    
    
    [
      {
        "associatedRecommendations": [
          {
            "recommendation": "projects/123456789012/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f"
          }
        ],
        "category": "SECURITY",
        "content": {
          "consolidatedPolicy": {
            "inheritFromParent": false,
            "name": "projects/123456789012/policies/iam.managed.disableServiceAccountKeyCreation",
            "policyRules": {
              "rules": [
                {
                  "enforce": false
                }
              ]
            },
            "reset": false
          },
          "constraint": {
            "id": "constraints/iam.managed.disableServiceAccountKeyCreation",
            "name": "Disable service account key creation"
          },
          "evaluatedResources": [
            {
              "numOfResources": "2",
              "resourceType": "iam.googleapis.com/ServiceAccountKey"
            },
            {
              "numOfResources": "1",
              "resourceType": "cloudresourcemanager.googleapis.com/Project"
            }
          ],
          "violations": [
            {
              "numOfResources": "0",
              "resourceType": "iam.googleapis.com/ServiceAccountKey"
            },
            {
              "numOfResources": "0",
              "resourceType": "cloudresourcemanager.googleapis.com/Project"
            }
          ]
        },
        "description": "Scanned 3 resources and found 0 violations for constraints/iam.managed.disableServiceAccountKeyCreation.",
        "etag": "\"9a1ad019022f9f56\"",
        "insightSubtype": "RESOURCE_VIOLATION_DISABLE_SERVICE_ACCOUNT_KEY_CREATION",
        "lastRefreshTime": "2024-12-07T08:00:00Z",
        "name": "projects/123456789012/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights/66d543f3-845d-49d6-a26b-80d84804d8a8",
        "observationPeriod": "86400s",
        "severity": "HIGH",
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

To learn more about the components of an insight, see Review organization policy insights on this page. 

## Get a single organization policy insight

To get more information about a single insight, including the insight's description, status, and any recommendations it's associated with, use one of the following methods: 

### gcloud

Use the [`gcloud recommender insights describe`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/describe) command with your insight ID to view information about a single insight. 

  * `INSIGHT_ID`: The ID of the insight that you want to view. To find the ID, list the insights for your project, folder, or organization. 
  * `RESOURCE_TYPE`: The resource type that you want to manage insights for. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to manage insights for. 


    
    
    gcloud recommender insights describe INSIGHT_ID \
        --insight-type=google.orgpolicy.policy.Insight \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=global

The output shows the insight in detail. For example, two resources are analyzed for external service account keys, and no violations are detected: 
    
    
    associatedRecommendations:
    - recommendation: projects/123456789012/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f
    category: SECURITY
    content:
      consolidatedPolicy:
        inheritFromParent: false
        name: 'projects/123456789012/policies/iam.managed.disableServiceAccountKeyCreation'
        policyRules:
          rules: [
            "enforce": false
          ]
        reset: false
      constraint: {
        id: constraints/iam.managed.disableServiceAccountKeyCreation
        name: Disable service account key creation
      }
      evaluatedResources:
      - numOfResources: '1'
        resourceType: cloudresourcemanager.googleapis.com/Project
      - numOfResources: '2'
        resourceType: iam.googleapis.com/ServiceAccountKey
      violations:
      - numOfResources: '0'
        resourceType: iam.googleapis.com/ServiceAccountKey
      - numOfResources: '0'
        resourceType: cloudresourcemanager.googleapis.com/Project
    description: Scanned 3 resources and found 0 violations for constraints/iam.managed.disableServiceAccountKeyCreation.
    etag: '"34ddfdcefd214fd7"'
    insightSubtype: RESOURCE_VIOLATION_DISABLE_SERVICE_ACCOUNT_KEY_CREATION
    lastRefreshTime: '2024-12-10T08:00:00Z'
    name: projects/123456789012/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights/66d543f3-845d-49d6-a26b-80d84804d8a8
    observationPeriod: 86400s
    severity: HIGH
    stateInfo:
      state: ACTIVE
    targetResources:
    - //cloudresourcemanager.googleapis.com/projects/123456789012

To learn more about the components of an insight, see Review organization policy insights on this page. 

### REST

The Recommender API's `[insights.get](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/get)` method gets a single insight. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type that you want to manage insights for. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to manage insights for. 
  * `INSIGHT_ID`: The ID of the insight that you want to view. If you don't know the insight ID, you can find it by listing the insights in your project, folder, or organization. The ID of an insight is everything after `insights/` in the `name` field for the insight. 
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    GET https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights/INSIGHT_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights/INSIGHT_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights/INSIGHT_ID" | Select-Object -Expand Content

The response contains the insight. For example, two resources are analyzed for external service account keys, and no violations are detected: 
    
    
    [
      {
        "associatedRecommendations": [
          {
            "recommendation": "projects/123456789012/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f"
          }
        ],
        "category": "SECURITY",
        "content": {
          "consolidatedPolicy": {
            "inheritFromParent": false,
            "name": "projects/123456789012/policies/iam.managed.disableServiceAccountKeyCreation",
            "policyRules": {
              "rules": [
                {
                  "enforce": false
                }
              ]
            },
            "reset": false
          },
          "constraint": {
            "id": "constraints/iam.managed.disableServiceAccountKeyCreation",
            "name": "Disable service account key creation"
          },
          "evaluatedResources": [
            {
              "numOfResources": "1",
              "resourceType": "cloudresourcemanager.googleapis.com/Project"
            },
            {
              "numOfResources": "2",
              "resourceType": "iam.googleapis.com/ServiceAccountKey"
            }
          ],
          "violations": [
            {
              "numOfResources": "0",
              "resourceType": "iam.googleapis.com/ServiceAccountKey"
            },
            {
              "numOfResources": "0",
              "resourceType": "cloudresourcemanager.googleapis.com/Project"
            }
          ]
        },
        "description": "Scanned 2 resources and found 0 violations for constraints/iam.managed.disableServiceAccountKeyCreation.",
        "etag": "\"9a1ad019022f9f56\"",
        "insightSubtype": "RESOURCE_VIOLATION_DISABLE_SERVICE_ACCOUNT_KEY_CREATION",
        "lastRefreshTime": "2024-12-03T08:00:00Z",
        "name": "projects/123456789012/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights/66d543f3-845d-49d6-a26b-80d84804d8a8",
        "observationPeriod": "86400s",
        "severity": "HIGH",
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

To learn more about the components of an insight, see Review organization policy insights on this page. 

## Review organization policy insights

After you get a single insight, you can review its contents to understand the configuration of the organization policy on your resources, including any violations. 

Organization policy insights (`google.orgpolicy.policy.Insight`) insights have the following components, not necessarily in this order: 

  * `associatedRecommendations`: The identifiers for any recommendations associated with the insight. If there are no recommendations associated with the insight, this field is empty. 
  * `category`: The category for organization policy insights is always `SECURITY`. 
  * `content`: Provides details about the resources and the organization policy that were analyzed. This field contains the following components: 
    * `constraint`: The constraint that was analyzed. 
    * `consolidatedPolicy`: The organization policy for the analyzed resource. 
    * `evaluatedResources`: The resources that were evaluated to generate the insight. 
    * `violations`: The number and types of resources that violate the organization policy. 
  * `description`: A human-readable summary of the insight. 
  * `etag`: A unique identifier for the current state of an insight. Each time the insight changes, a new `etag` value is assigned. 

To change the state of an insight, you must provide the `etag` of the existing insight. Using the `etag` helps ensure that any operations are performed only if the insight has not changed since you last retrieved it. 

  * `insightSubtype`: The insight subtype. 
  * `lastRefreshTime`: The date when the insight was last refreshed, which indicates the freshness of the data used to generate the insight. 
  * `name`: The name of the insight, in the following format:
        
        RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights/INSIGHT_ID

The placeholders have the following values:

    * `RESOURCE_TYPE`: The resource type that the insight was generated for. 
    * `RESOURCE_ID`: The ID of the project, folder, or organization where the insight was generated. 
    * `INSIGHT_ID`: A unique ID for the insight.
  * `observationPeriod`: The time period leading up to the insight. The source data used to generate the insight ends at `lastRefreshTime` and begins at `lastRefreshTime` minus `observationPeriod`. 
  * `severity`: The severity of the insight. Insights for organization policies have a severity of `HIGH`. 
  * `stateInfo`: Insights go through multiple state transitions after they are proposed: 

    * `ACTIVE`: The insight has been generated, but either no actions have been taken, or an action was taken without updating the insight's state. Active insights are updated when the underlying data changes. 
    * `ACCEPTED`: Some action has been taken based on the insight. Insights become accepted when an associated recommendation was marked `CLAIMED`, `SUCCEEDED`, or `FAILED`, or the insight was accepted directly. When an insight is in the `ACCEPTED` state, the content of the insight cannot change. Accepted insights are retained for 90 days after they are accepted. 
  * `targetResources`: The [full resource name ](https://docs.cloud.google.com/iam/docs/full-resource-names) of the project, folder, or organization that the insight is for. For example, `//cloudresourcemanager.googleapis.com/projects/1234567890`. 



## Mark a organization policy insight as `ACCEPTED`

If you take action based on an active insight, you can mark that insight as `ACCEPTED`. The `ACCEPTED` state tells the Recommender API that you have taken action based on this insight, which helps refine your recommendations. 

Accepted insights are retained for 90 days after they are marked as `ACCEPTED`. 

### gcloud

Use the [ `gcloud recommender insights mark-accepted`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted) command with your insight ID to mark an insight as `ACCEPTED`. 

  * `INSIGHT_ID`: The ID of the insight that you want to view. To find the ID, list the insights for your project, folder, or organization. 
  * `RESOURCE_TYPE`: The resource type that you want to manage insights for. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: The ID of the project, folder, or organization that you want to manage insights for. 
  * `ETAG`: An identifier for a version of the insight. To get the `etag`, do the following: 

    1. Get the insight using the `gcloud recommender insights describe` command. 
    2. Find and copy the `etag` value from the output, including the enclosing quotes. For example, `"d3cdec23cc712bd0"`. 


    
    
    gcloud recommender insights mark-accepted INSIGHT_ID \
        --insight-type=google.orgpolicy.policy.Insight \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=global \
        --etag=ETAG

The output shows the insight, now with the state of `ACCEPTED`: 
    
    
    associatedRecommendations:
    - recommendation: folders/234567890123/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f
    category: SECURITY
    content:
      consolidatedPolicy:
        inheritFromParent: false
        name: 'projects/123456789012/policies/iam.managed.disableServiceAccountKeyCreation'
        policyRules:
          rules: [
            "enforce": false
          ]
        reset: false
      constraint: {
        id: constraints/iam.managed.disableServiceAccountKeyCreation
        name: Disable service account key creation
      }
      evaluatedResources:
      - numOfResources: '0'
        resourceType: iam.googleapis.com/ServiceAccountKey
      - numOfResources: '1'
        resourceType: cloudresourcemanager.googleapis.com/Folder
      - numOfResources: '1'
        resourceType: cloudresourcemanager.googleapis.com/Project
      violations:
      - numOfResources: '0'
        resourceType: iam.googleapis.com/ServiceAccountKey
      - numOfResources: '0'
        resourceType: cloudresourcemanager.googleapis.com/Folder
      - numOfResources: '0'
        resourceType: cloudresourcemanager.googleapis.com/Project
    description: Scanned 2 resources and found 0 violations for constraints/iam.managed.disableServiceAccountKeyUpload.
    etag: '"2cbb89b22fe2dab7"'
    insightSubtype: RESOURCE_VIOLATION_DISABLE_SERVICE_ACCOUNT_KEY_UPLOAD
    lastRefreshTime: '2024-12-10T08:00:00Z'
    name: folders/234567890123/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights/66d543f3-845d-49d6-a26b-80d84804d8a8
    observationPeriod: 86400s
    severity: HIGH
    stateInfo:
      state: ACCEPTED
    targetResources:
    - //cloudresourcemanager.googleapis.com/folders/234567890123

To learn more about the state info of an insight, see Review organization policy insights on this page. 

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
    
    
    POST https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights/INSIGHT_ID:markAccepted

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
         "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights/INSIGHT_ID:markAccepted"

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
        -Uri "https://recommender.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights/INSIGHT_ID:markAccepted" | Select-Object -Expand Content

The response contains the insight, now with the state of `ACCEPTED`: 
    
    
    [
      {
        "associatedRecommendations": [
          {
            "recommendation": "projects/123456789012/locations/global/recommenders/google.orgpolicy.policy.Recommender/recommendations/fb927dc1-9695-4436-0000-f0f285007c0f"
          }
        ],
        "category": "SECURITY",
        "content": {
          "consolidatedPolicy": {
            "inheritFromParent": false,
            "name": "projects/123456789012/policies/iam.managed.disableServiceAccountKeyCreation",
            "policyRules": {
              "rules": [
                {
                  "enforce": false
                }
              ]
            },
            "reset": false
          },
          "constraint": {
            "id": "constraints/iam.managed.disableServiceAccountKeyCreation",
            "name": "Disable service account key creation"
          },
          "evaluatedResources": [
            {
              "numOfResources": "1",
              "resourceType": "cloudresourcemanager.googleapis.com/Project"
            },
            {
              "numOfResources": "2",
              "resourceType": "iam.googleapis.com/ServiceAccountKey"
            }
          ],
          "violations": [
            {
              "numOfResources": "0",
              "resourceType": "iam.googleapis.com/ServiceAccountKey"
            },
            {
              "numOfResources": "0",
              "resourceType": "cloudresourcemanager.googleapis.com/Project"
            }
          ]
        },
        "description": "Scanned 2 resources and found 0 violations for constraints/iam.managed.disableServiceAccountKeyCreation.",
        "etag": "\"9a1ad019022f9f56\"",
        "insightSubtype": "RESOURCE_VIOLATION_DISABLE_SERVICE_ACCOUNT_KEY_CREATION",
        "lastRefreshTime": "2024-12-03T08:00:00Z",
        "name": "projects/123456789012/locations/global/insightTypes/google.orgpolicy.policy.Insight/insights/66d543f3-845d-49d6-a26b-80d84804d8a8",
        "observationPeriod": "86400s",
        "severity": "HIGH",
        "stateInfo": {
          "state": "ACCEPTED",
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

To learn more about the state info of an insight, see Review organization policy insights on this page. 

## What's next

  * Learn how to [ view and apply organization policy recommendations](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-organization-policy-recommendations).
  * Use the [Active Assist](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems) to view and manage all recommendations for your project, including IAM recommendations.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

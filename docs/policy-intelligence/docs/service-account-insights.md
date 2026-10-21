---
url: https://docs.cloud.google.com/policy-intelligence/docs/service-account-insights/
title: Find unused service accounts \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:04:01.169339+00:00
---

# Find unused service accounts  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/service-account-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Find unused service accounts Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows how to manage service account insights, which are findings about which service accounts in your project haven't authenticated in the past 90 days. We recommend disabling or deleting these unused service accounts and keys because they create an unnecessary security risk. 

Requests authenticated by [API keys bound to service accounts](https://docs.cloud.google.com/docs/authentication/api-keys#api-keys-bound-sa) aren't recorded in [service account usage metrics](https://docs.cloud.google.com/iam/docs/service-account-monitoring). As a result, these service accounts might be reported as unused.

Authentication activities with a Google API outside of Google Cloud, such as [domain-wide delegation](https://docs.cloud.google.com/workspace/cloud-search/docs/guides/delegation) of authority to Google Workspace APIs, aren't tracked by [Activity Analyzer](https://docs.cloud.google.com/policy-intelligence/docs/activity-analyzer-service-account-authentication) or [service account insights](https://docs.cloud.google.com/policy-intelligence/docs/service-account-insights). To track these authentication activities, use Cloud Monitoring [service account usage metrics](https://docs.cloud.google.com/iam/docs/service-account-monitoring). 

We recommend cross referencing service account insights with Cloud Monitoring service account usage metrics before you disable or delete a service account. This approach prevents you from removing service accounts that are in use with Google APIs outside of Google Cloud.

## Before you begin

  * Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Optional: Read about [Recommender insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights).



### Required roles

To get the permissions that you need to manage service account insights, ask your administrator to grant you the following IAM roles on the project that you want to manage insights for: 

  * To view service account insights: [IAM Recommender Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamViewer) (`roles/recommender.iamViewer`) 
  * To modify service account insights: [IAM Recommender Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamAdmin) (`roles/recommender.iamAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage service account insights. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage service account insights:

  * To view service account insights: 
    * `recommender.iamServiceAccountinsights.get`
    * `recommender.iamServiceAccountinsights.list`
  * To modify service account insights: `recommender.iamServiceAccountinsights.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List service account insights

To list all service account insights for your project, use one of the following methods: 

### gcloud

Use the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command to view all service account insights for your project. 

Before you run the command, replace the following values: 

  * `PROJECT_ID`: The ID of the project that you want to list insights for. 


    
    
    gcloud recommender insights list --insight-type=google.iam.serviceAccount.Insight \
        --project=PROJECT_ID \
        --location=global

The output lists all of the service account insights for your project. For example: 
    
    
    INSIGHT_ID                            CATEGORY  INSIGHT_STATE  LAST_REFRESH_TIME     SEVERITY  INSIGHT_SUBTYPE        DESCRIPTION
    446303ba-2a14-49cc-b9fa-e2d2499d4f82  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       SERVICE_ACCOUNT_USAGE  Service account sa-1@my-project.iam.gserviceaccount.com was inactive.
    4cfd82c3-7320-4dc6-9b67-ca0756bbd54c  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       SERVICE_ACCOUNT_USAGE  Service account sa-2@my-project.iam.gserviceaccount.com was inactive.
    a627bed7-c8f4-4611-89c9-2a9a8618ca1b  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       SERVICE_ACCOUNT_USAGE  Service account sa-3@my-project.iam.gserviceaccount.com was inactive.
    a922dd59-df0a-422d-a2a4-096195e1dae5  SECURITY  ACTIVE         2022-05-24T07:00:00Z  LOW       SERVICE_ACCOUNT_USAGE  Service account sa-4@my-project.iam.gserviceaccount.com was inactive.

### REST

The Recommender API's `[insights.list](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list)` method lists all service account insights for your project. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: The ID of the project that you want to list insights for.



HTTP method and URL: 
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights" | Select-Object -Expand Content

The response lists all of the service account insights for your project. For example: 
    
    
    {
      "insights": [
        {
          "name": "projects/123456789012/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights/446303ba-2a14-49cc-b9fa-e2d2499d4f82",
          "description": "Service account sa-1@my-project.iam.gserviceaccount.com was inactive.",
          "content": {
            "serviceAccountId": "103185812403937829397",
            "email": "sa-1@my-project.iam.gserviceaccount.com",
            "lastAuthenticatedTime": "2020-09-11T07:00:00Z"
          },
          "lastRefreshTime": "2022-05-24T07:00:00Z",
          "observationPeriod": "19008000s",
          "stateInfo": {
            "state": "ACTIVE"
          },
          "category": "SECURITY",
          "targetResources": [
            "//cloudresourcemanager.googleapis.com/projects/123456789012"
          ],
          "insightSubtype": "SERVICE_ACCOUNT_USAGE",
          "etag": "\"9d797dd04263c855\"",
          "severity": "LOW"
        },
        {
          "name": "projects/123456789012/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights/4cfd82c3-7320-4dc6-9b67-ca0756bbd54c",
          "description": "Service account sa-2@my-project.iam.gserviceaccount.com was inactive.",
          "content": {
            "serviceAccountId": "105496400997178042131",
            "email": "sa-2@my-project.iam.gserviceaccount.com"
          },
          "lastRefreshTime": "2022-05-24T07:00:00Z",
          "observationPeriod": "16070400s",
          "stateInfo": {
            "state": "ACTIVE"
          },
          "category": "SECURITY",
          "targetResources": [
            "//cloudresourcemanager.googleapis.com/projects/123456789012"
          ],
          "insightSubtype": "SERVICE_ACCOUNT_USAGE",
          "etag": "\"783a32b635d79a4e\"",
          "severity": "LOW"
        }
      ]
    }

To learn more about the components of an insight, see Review service account insights on this page. 

## Get a single service account insight

To get more information about a single insight, including the insight's description, status, and any recommendations it's associated with, use one of the following methods: 

### gcloud

Use the [`gcloud recommender insights describe`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/describe) command with your insight ID to view information about a single insight. 

  * `INSIGHT_ID`: The ID of the insight that you want to view. To find the ID, list the insights for your project. 
  * `PROJECT_ID`: The ID of the project that you want to manage insights for.


    
    
    gcloud recommender insights describe INSIGHT_ID \
        --insight-type=google.iam.serviceAccount.Insight \
        --project=PROJECT_ID \
        --location=global

The output shows the insight in detail. For example,the following insight indicates that the service account `sa-1@my-project.iam.gserviceaccount.com` has not authenticated since October 11, 2020. 
    
    
    category: SECURITY
    content:
      email: sa-1@my-project.iam.gserviceaccount.com
      lastAuthenticatedTime: '2020-10-11T07:00:00Z'
      serviceAccountId: '103185812403937829397'
    description: Service account sa-1@my-project.iam.gserviceaccount.com
      was inactive.
    etag: '"9d797dd04263c855"'
    insightSubtype: SERVICE_ACCOUNT_USAGE
    lastRefreshTime: '2022-05-24T07:00:00Z'
    name: projects/123456789012/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights/446303ba-2a14-49cc-b9fa-e2d2499d4f82
    observationPeriod: 19008000s
    severity: LOW
    stateInfo:
      state: ACTIVE
    targetResources:
    - //cloudresourcemanager.googleapis.com/projects/123456789012

To learn more about the components of an insight, see Review service account insights on this page. 

### REST

The Recommender API's `[insights.get](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/get)` method gets a single insight. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: The ID of the project that you want to manage insights for. 
  * `INSIGHT_ID`: The ID of the insight that you want to view. If you don't know the insight ID, you can find it by listing the insights in your project. The ID of an insight is everything after `insights/` in the `name` field for the insight. 



HTTP method and URL: 
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights/INSIGHT_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights/INSIGHT_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights/INSIGHT_ID" | Select-Object -Expand Content

The response contains the insight. For example,the following insight indicates that the service account `sa-1@my-project.iam.gserviceaccount.com` has not authenticated since October 11, 2020. 
    
    
    {
      "name": "projects/123456789012/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights/446303ba-2a14-49cc-b9fa-e2d2499d4f82",
      "description": "Service account sa-1@my-project.iam.gserviceaccount.com was inactive.",
      "content": {
        "serviceAccountId": "103185812403937829397",
        "email": "sa-1@my-project.iam.gserviceaccount.com",
        "lastAuthenticatedTime": "2020-09-11T07:00:00Z"
      },
      "lastRefreshTime": "2022-05-24T07:00:00Z",
      "observationPeriod": "19008000s",
      "stateInfo": {
        "state": "ACTIVE"
      },
      "category": "SECURITY",
      "targetResources": [
        "//cloudresourcemanager.googleapis.com/projects/123456789012"
      ],
      "insightSubtype": "SERVICE_ACCOUNT_USAGE",
      "etag": "\"9d797dd04263c855\"",
      "severity": "LOW"
    }

To learn more about the components of an insight, see Review service account insights on this page. 

## Review service account insights

After you get a single insight, you can review its contents to understand the pattern of resource usage that it highlights. 

An insight's content is determined by its subtypes. Service account insights (`google.iam.serviceAccount.Insight`) insights have the `SERVICE_ACCOUNT_USAGE` subtype. 

`SERVICE_ACCOUNT_USAGE` insights have the following components, not necessarily in this order: 

  * `associatedRecommendations`: The identifiers for any recommendations associated with the insight. If there are no recommendations associated with the insight, this field is empty. 
  * `category`: The category for IAM insights is always `SECURITY`. 
  * `content`: Reports the last time the service account was authenticated. This field contains the following components: 

    * `email`: The email address of the service account.
    * `lastAuthenticatedTime`: The most recent time that the service account was authenticated. If the service account does not have any recorded authentications, this field is not included.
    * `serviceAccountId`: The unique numeric ID of the service account.
  * `description`: A human-readable summary of the insight. 
  * `etag`: A unique identifier for the current state of an insight. Each time the insight changes, a new `etag` value is assigned. 

To change the state of an insight, you must provide the `etag` of the existing insight. Using the `etag` helps ensure that any operations are performed only if the insight has not changed since you last retrieved it. 

  * `insightSubtype`: The insight subtype. 
  * `lastRefreshTime`: The date when the insight was last refreshed, which indicates the freshness of the data used to generate the insight. 
  * `name`: The name of the insight, in the following format:
        
        projects/PROJECT_ID/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights/INSIGHT_ID

The placeholders have the following values:

    * `PROJECT_ID`: The ID of the project where the insight was generated. 
    * `INSIGHT_ID`: A unique ID for the insight.
  * `observationPeriod`: The time period leading up to the insight. The source data used to generate the insight ends at `lastRefreshTime` and begins at `lastRefreshTime` minus `observationPeriod`. 
  * `stateInfo`: Insights go through multiple state transitions after they are proposed: 

    * `ACTIVE`: The insight has been generated, but either no actions have been taken, or an action was taken without updating the insight's state. Active insights are updated when the underlying data changes. 
    * `ACCEPTED`: Some action has been taken based on the insight. Insights become accepted when an associated recommendation was marked `CLAIMED`, `SUCCEEDED`, or `FAILED`, or the insight was accepted directly. When an insight is in the `ACCEPTED` state, the content of the insight cannot change. Accepted insights are retained for 90 days after they are accepted. 
  * `targetResources`: The [full resource name ](https://docs.cloud.google.com/iam/docs/full-resource-names) of the project that the insight is for. For example, `//cloudresourcemanager.googleapis.com/projects/123456789012`. 



## Mark a service account insight as `ACCEPTED`

If you take action based on an active insight, you can mark that insight as `ACCEPTED`. The `ACCEPTED` state tells the Recommender API that you have taken action based on this insight, which helps refine your recommendations. 

Accepted insights are retained for 90 days after they are marked as `ACCEPTED`. 

### gcloud

Use the [ `gcloud recommender insights mark-accepted`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted) command with your insight ID to mark an insight as `ACCEPTED`. 

  * `INSIGHT_ID`: The ID of the insight that you want to view. To find the ID, list the insights for your project. 
  * `PROJECT_ID`: The ID of the project that you want to manage insights for.
  * `ETAG`: An identifier for a version of the insight. To get the `etag`, do the following: 

    1. Get the insight using the `gcloud recommender insights describe` command. 
    2. Find and copy the `etag` value from the output, including the enclosing quotes. For example, `"d3cdec23cc712bd0"`. 


    
    
    gcloud recommender insights mark-accepted INSIGHT_ID \
        --insight-type=google.iam.serviceAccount.Insight \
        --project=PROJECT_ID \
        --location=global \
        --etag=ETAG

The output shows the insight, now with the state of `ACCEPTED`: 
    
    
    category: SECURITY
    content:
      email: sa-1@my-project.iam.gserviceaccount.com
      lastAuthenticatedTime: '2020-10-11T07:00:00Z'
      serviceAccountId: '103185812403937829397'
    description: Service account sa-1@my-project.iam.gserviceaccount.com
      was inactive.
    etag: '"39c4199dcec92848"'
    insightSubtype: SERVICE_ACCOUNT_USAGE
    lastRefreshTime: '2022-05-24T07:00:00Z'
    name: projects/123456789012/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights/446303ba-2a14-49cc-b9fa-e2d2499d4f82
    observationPeriod: 19008000s
    severity: LOW
    **stateInfo :
      state: ACCEPTED**
    targetResources:
    - //cloudresourcemanager.googleapis.com/projects/123456789012

To learn more about the state info of an insight, see Review service account insights on this page. 

### REST

The Recommender API's `[insights.markAccepted](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/markAccepted)` method marks an insight as `ACCEPTED`. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: The ID of the project that you want to manage insights for. 
  * `INSIGHT_ID`: The ID of the insight that you want to view. If you don't know the insight ID, you can find it by listing the insights in your project. The ID of an insight is everything after `insights/` in the `name` field for the insight. 
  * `ETAG`: An identifier for a version of the insight. To get the `etag`, do the following: 
    1. Get the insight using the `insights.get` method.
    2. Find and copy the `etag` value from the response.



HTTP method and URL: 
    
    
    POST https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights/INSIGHT_ID:markAccepted

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
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights/INSIGHT_ID:markAccepted"

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
        -Uri "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights/INSIGHT_ID:markAccepted" | Select-Object -Expand Content

The response contains the insight, now with the state of `ACCEPTED`: 
    
    
    {
      "name": "projects/123456789012/locations/global/insightTypes/google.iam.serviceAccount.Insight/insights/446303ba-2a14-49cc-b9fa-e2d2499d4f82",
      "description": "Service account sa-1@my-project.iam.gserviceaccount.com was inactive.",
      "content": {
        "serviceAccountId": "103185812403937829397",
        "email": "sa-1@my-project.iam.gserviceaccount.com",
        "lastAuthenticatedTime": "2020-10-11T07:00:00Z"
      },
      "lastRefreshTime": "2022-05-24T07:00:00Z",
      "observationPeriod": "19008000s",
      **"stateInfo": {
        "state": "ACCEPTED"
        },**
      "category": "SECURITY",
      "targetResources": [
        "//cloudresourcemanager.googleapis.com/projects/123456789012"
      ],
      "insightSubtype": "SERVICE_ACCOUNT_USAGE",
      "etag": "\"39c4199dcec92848\"",
      "severity": "LOW"
    }

To learn more about the state info of an insight, see Review service account insights on this page. 

## What's next

  * Review the other available [tools to understand service account usage](https://docs.cloud.google.com/policy-intelligence/docs/service-account-usage-tools).
  * Use the [Active Assist](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems) to view and manage all recommendations for your project, including IAM recommendations.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/contact-center/insights/docs/use-authorized-views/
title: Use authorized views \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:04:13.924432+00:00
---

# Use authorized views  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/insights/docs/use-authorized-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Use authorized views Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use authorized views to retrieve conversation data, perform analysis, or edit feedback labels. You can't use authorized views to edit or import conversation data, train topic models, or create scorecards.

Select an authorized view to access the specific data scope it provides. Each view can define a different scope. You will only see data permitted through the selected view.

Choose **No view** to use your assigned Identity and Access Management (IAM) permissions. This is the default state.

## Required permissions and roles

To use authorized views, you need the following [IAM permissions](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#permissions_and_roles):

### Permissions for project access

Managers and agents require view access on the project `resourcemanager.projects.get` to interact with the console.

Use `roles/browser` to give managers and agents a basic level of access. See the [project level access control documentation](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#access_control_at_the_project_level) for more details.

### Authorized view permissions

Grant the following permissions on specific authorized views with the `SetIamPolicy` methods. See the [authorized view resources](https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-and-manage-authorized-views#modifying_iam_policies_on_an_authorized_view) for more details.

**Warning:** Granting authorized view permissions and roles at the project level, rather than the authorized view level, results in agents having access to all authorized views.

Authorized view users only need the `contactcenterinsights.authorizedViews.get` permission and the corresponding `authorized` permissions for the resources they can access.

#### Permissions for authorized conversations

Permission | Description  
---|---  
`contactcenterinsights.authorizedConversations.get` | Use an authorized view to get a conversation.  
`contactcenterinsights.authorizedConversations.list` | Use an authorized view to list conversations.  
  
#### Permissions for authorized operations

Permission | Description  
---|---  
`contactcenterinsights.authorizedOperations.get` | Use an authorized view to get an operation.  
`contactcenterinsights.authorizedOperations.list` | Use an authorized view to list operations.  
**Warning:** Don't give agents permissions to manage authorized views.

#### Predefined roles

The following predefined IAM roles provide the necessary permissions:

Role | Description  
---|---  
`roles/contactcenterinsights.authorizeEditor` | Provides read/write access to all authorized Customer Experience Insights resources.  
`roles/contactcenterinsights.authorizedViewer` | Provides full access to all Customer Experience Insights authorized resources.  
  
## Search your authorized views

### REST

Retrieve all the authorized views that you have access to.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The location of your Customer Experience Insights data.
  * AUTHORIZED_VIEW_SET_ID: A user-defined identifier for the authorized view set or wildcard `-`.
  * PAGE_SIZE: The maximum number of views to return in the response. If the value is zero, the service will select a default size. A call might return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.
  * PAGE_TOKEN: The value returned by the last `SearchAuthorizedViewsResponse`. This value indicates that this is a continuation of a prior `SearchAuthorizedViews` call and that the system should return the next page of data.
  * FILTER: The filter expression to filter authorized views listed in the response. You can filter on the following fields: `authorized_view_id`, `display_name`, `conversation_filter`, `create_time`, and `update_time`. You can use arbitrary and/or expressions. You can also use regular expressions for string fields.
    * Example: `display_name = "My View"`
    * Example: `conversation_filter =~ ".*agent-1.*"`
    * Example: `create_time > "2022-01-01T00:00:00Z"`
    * Example: `display_name =~ ".*View.*"`
    * Example: `create_time > "2022-01-01T00:00:00Z" AND create_time <= "2022-01-02T00:00:00Z"`
  * ORDER_BY: The order by expression to order authorized views listed in the response.
    * Example: `create_time`
    * Example: `update_time desc`



HTTP method and URL: 
    
    
    GET https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews:search?page_size=PAGE_SIZE&page_token=PAGE_TOKEN&filter=FILTER&order_by=ORDER_BY

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews:search?page_size=PAGE_SIZE&page_token=PAGE_TOKEN&filter=FILTER&order_by=ORDER_BY"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews:search?page_size=PAGE_SIZE&page_token=PAGE_TOKEN&filter=FILTER&order_by=ORDER_BY" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "authorizedViews": [
        {
          "name": "projects/my-project/locations/us-central1/authorizedViewSets/my-view-set/authorizedViews/my-view-1",
          "displayName": "My First View",
          "conversationFilter": "agent_id = \"agent-1\"",
          "createTime": "2022-01-01T00:00:00.000000Z",
          "updateTime": "2022-01-01T00:00:00.000000Z"
        },
        {
          "name": "projects/my-project/locations/us-central1/authorizedViewSets/my-view-set/authorizedViews/my-view-2",
          "displayName": "My Second View",
          "conversationFilter": "agent_id = \"agent-2\"",
          "createTime": "2022-01-01T00:00:00.000000Z",
          "updateTime": "2022-01-01T00:00:00.000000Z"
        }
      ],
      "nextPageToken": "next-page-token"
    }
    

## Authorized conversation

An authorized conversation represents a conversation when accessed using an authorized view.

For a full list of supported methods, see the [authorized conversation methods reference docs](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.authorizedConversation).

### Get an authorized conversation

### REST

Getting an authorized conversation requires the `contactcenterinsights.authorizedConversations.get` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: The location of your project 
  * AUTHORIZED_VIEW_SET_ID: The ID of the authorized view set.
  * AUTHORIZED_VIEW_ID: The ID of the authorized view.
  * CONVERSATION_ID: The ID of the conversation.



HTTP method and URL: 
    
    
    GET https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID/conversations/CONVERSATION_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID/conversations/CONVERSATION_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID/conversations/CONVERSATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION_ID/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID/conversations/CONVERSATION_ID",
      "createTime": "2025-03-03T11:23:17.823813113Z",
      "updateTime": "2025-03-03T11:23:17.987216Z",
      "agentId": "AGENT_ID",
      "callMetadata": {
        "customerChannel": 1,
        "agentChannel": 2
      },
      "medium": "CHAT",
      "duration": "0s",
      "turnCount": 2,
      "languageCode": "en",
      "startTime": "2025-03-03T11:23:16.903361174Z",
      "qualityMetadata": {
        "agentInfo": [
          {
            "agentId": "AGENT_ID",
            "agentType": "HUMAN_AGENT"
          }
        ]
      }
    }
    

### List authorized conversations

### REST

Listing authorized conversations requires the `contactcenterinsights.authorizedConversations.list` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: The location of your project. 
  * AUTHORIZED_VIEW_SET_ID: The ID of the authorized view set.
  * AUTHORIZED_VIEW_ID: The ID of the authorized view.
  * PAGE_SIZE: The number of conversations to return per page.



HTTP method and URL: 
    
    
    GET https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID/conversations?pageSize=PAGE_SIZE

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID/conversations?pageSize=PAGE_SIZE"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID/conversations?pageSize=PAGE_SIZE" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "conversations": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION_ID/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID/conversations/4315d72e3d-c75-94d-2d5-1ae05b4222352",
          "createTime": "2025-03-03T11:23:17.823813113Z",
          "updateTime": "2025-03-03T11:23:17.987216Z",
          "agentId": "AGENT_ID",
          "callMetadata": {
            "customerChannel": 1,
            "agentChannel": 2
          },
          "medium": "CHAT",
          "duration": "0s",
          "turnCount": 2,
          "languageCode": "en",
          "startTime": "2025-03-03T11:23:16.903361174Z",
          "qualityMetadata": {
            "agentInfo": [
              {
                "agentId": "AGENT_ID",
                "agentType": "AUTOMATED_AGENT"
              }
            ]
          }
        },
        {
          "name": "projects/PROJECT_ID/locations/LOCATION_ID/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID/conversations/8d3b61-bd4-f2c-364-b5a794f76",
          "createTime": "2025-03-03T11:19:58.605217527Z",
          "updateTime": "2025-03-03T11:19:58.901962Z",
          "agentId": "AGENT_ID",
          "callMetadata": {
            "customerChannel": 1,
            "agentChannel": 2
          },
          "medium": "CHAT",
          "duration": "0s",
          "turnCount": 2,
          "runtimeAnnotations": [
            {
              "createTime": "2025-03-03T11:19:56.164686195Z",
              "startBoundary": {
                "transcriptIndex": 1
              },
              "endBoundary": {
                "transcriptIndex": 2
              },
              "answerFeedback": {},
             
            }
          ],
          "languageCode": "en",
          "startTime": "2025-03-03T11:19:56.164686195Z",
          "qualityMetadata": {
            "agentInfo": [
              {
                "agentId": "AGENT_ID",
                "agentType": "HUMAN_AGENT"
              }
            ]
          }
        }
      ],
      "nextPageToken": "NEXT_PAGE_TOKEN"
    }
    

## Authorized operations

For a full list of supported methods, see the [authorized operations methods reference docs](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.authorizedOperation)

### Get an authorized operation

### REST

Getting an authorized operation requires the `contactcenterinsights.authorizedOperations.get` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The location of your Customer Experience Insights data.
  * OPERATION_ID: The ID of the conversation you want to analyze. This value was returned when you created the analysis. 



HTTP method and URL: 
    
    
    GET https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/operations/OPERATION_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/operations/OPERATION_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.contactcenterinsights.v1.QueryMetricsMetadata"
      },
      "done": true
    }
    

### List authorized operations

### REST

Listing authorized operations requires the `contactcenterinsights.authorizedOperations.list` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The location of your Customer Experience Insights data.
  * AUTHORIZED_VIEW_SET_ID: The ID of the authorized view set.
  * AUTHORIZED_VIEW_ID: The ID of the authorized view.



HTTP method and URL: 
    
    
    GET https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID/operations/

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID/operations/"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID/operations/" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "operations": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION_ID/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID/operations/OPERATION_ID",
          "metadata": {
            "@type": "type.googleapis.com/google.cloud.contactcenterinsights.v1.QueryMetricsMetadata"
          },
          "done": true
        },
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID/operations/OPERATION_ID_2",
          "metadata": {
            "@type": "type.googleapis.com/google.cloud.contactcenterinsights.v1.QueryMetricsMetadata"
          },
          "done": true
        }
      ]
    }
    

## What's next?

  * [Best practices for authorized views](https://docs.cloud.google.com/gemini-enterprise-cx/insights/best-practices-for-fine-grained-access-control)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

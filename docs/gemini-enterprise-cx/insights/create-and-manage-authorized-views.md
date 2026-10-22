---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-and-manage-authorized-views/
title: Create and manage authorized views \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:57.566550+00:00
---

# Create and manage authorized views  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-and-manage-authorized-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Create and manage authorized views Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can perform the following administrative operations on authorized views and authorized view sets.

## Required permissions and roles

To create and manage authorized view sets and authorized views, you need the following IAM permissions.

Authorized view sets:

Permission | Description  
---|---  
`contactcenterinsights.authorizedViewSet.create` | Create an authorized view set.  
`contactcenterinsights.authorizedViewSet.get` | Get details about an authorized view set.  
`contactcenterinsights.authorizedViewSet.update` | Update an existing authorized view set.  
`contactcenterinsights.authorizedViewSet.delete` | Delete an authorized view set.  
`contactcenterinsights.authorizedViewSet.list` | List authorized view sets in a project.  
  
Authorized views:

Permission | Description  
---|---  
`contactcenterinsights.authorizedView.create` | Create an authorized view.  
`contactcenterinsights.authorizedView.get` | Get details about an authorized view.  
`contactcenterinsights.authorizedView.update` | Update an existing authorized view.  
`contactcenterinsights.authorizedView.delete` | Delete an authorized view.  
  
To grant access to authorized views, you need the following permissions:

Permission | Description  
---|---  
`contactcenterinsights.authorizedView.addIamPolicy` | Add the IAM policy on an authorized view.  
`contactcenterinsights.authorizedView.getIamPolicy` | Get the IAM policy on an authorized view.  
  
### Predefined roles

The following predefined IAM roles provide the necessary permissions:

Role | Description  
---|---  
`roles/contactcenterinsights.editor` | Provides Read and Write access to all Customer Experience Insights resources.  
`roles/contactcenterinsights.admin` | Provides Read and Write access to all Customer Experience Insights resources.  
  
## Authorized view sets

Authorized view sets group and simplify granting permissions to multiple authorized views.

### Create an authorized view set

### REST

To create an authorized view set, you need the `contactcenterinsights.authorizedViewSet.create` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The location of your Customer Experience Insights data.
  * AUTHORIZED_VIEW_SET_ID: An optional user-defined identifier for the authorized view set to create; this value must be 1-63 characters, begin and end with [a-z0-9], and can contain dashes (-) between characters
  * DISPLAY_NAME: A descriptive name for the authorized view set.



HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets?authorized_view_set_id=AUTHORIZED_VIEW_SET_ID

Request JSON body: 
    
    
    {
      "displayName": "DISPLAY_NAME"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets?authorized_view_set_id=AUTHORIZED_VIEW_SET_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets?authorized_view_set_id=AUTHORIZED_VIEW_SET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID",
      "displayName": "DISPLAY_NAME",
      "createTime": "2022-01-01T00:00:00.000000Z",
      "updateTime": "2022-01-01T00:00:00.000000Z"
    }
    

### Read an authorized view set

### REST

Reading an authorized view set requires the `contactcenterinsights.authorizedViewSet.get` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The location of your Customer Experience Insights data.
  * AUTHORIZED_VIEW_SET_ID: The identifier for the authorized view set.



HTTP method and URL: 
    
    
    GET https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID",
      "displayName": "DISPLAY_NAME",
      "createTime": "2022-01-01T00:00:00.000000Z",
      "updateTime": "2022-01-01T00:00:00.000000Z"
    }
    

### Update an authorized view set

### REST

Updating an authorized view set requires the `contactcenterinsights.authorizedViewSet.update` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The location of your Customer Experience Insights data.
  * AUTHORIZED_VIEW_SET_ID: The identifier for the authorized view set.
  * DISPLAY_NAME: A descriptive name for the authorized view set.
  * UPDATE_MASK: The fields to update. This value is a comma-separated list of fields. 
    * `display_name`



HTTP method and URL: 
    
    
    PATCH https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID?update_mask=display_name

Request JSON body: 
    
    
    {
      "displayName": "DISPLAY_NAME"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID?update_mask=display_name"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID?update_mask=display_name" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID",
      "displayName": "DISPLAY_NAME",
      "createTime": "2022-01-01T00:00:00.000000Z",
      "updateTime": "2022-01-01T00:00:00.000000Z"
    }
    

### Delete an authorized view set

### REST

Deleting an authorized view set requires the `contactcenterinsights.authorizedViewSet.delete` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The location of your Customer Experience Insights data.
  * AUTHORIZED_VIEW_SET_ID: The identifier for the authorized view set.



HTTP method and URL: 
    
    
    DELETE https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {}
    

### List authorized view sets

### REST

Listing authorized view sets requires the `contactcenterinsights.authorizedViewSet.list` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The location of your Customer Experience Insights data.
  * PAGE_SIZE: The maximum number of authorized view sets to return in the response. If the value is zero, the service will select a default size. A call might return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.
  * PAGE_TOKEN: The value returned by the last `ListAuthorizedViewSetsResponse`. This value indicates that this is a continuation of a prior `ListAuthorizedViewSets` call and that the system should return the next page of data.
  * FILTER: An expression to filter authorized view sets. For example: 
    * `create_time > "2022-01-01T00:00:00Z"`
    * `update_time < "2022-01-02T00:00:00Z"`
    * `display_name = "My Authorized View Set"`
    * `display_name =~ "My.*"`
    * `create_time > "2022-01-01T00:00:00Z" AND display_name = "My Authorized View Set"`
    * `create_time > "2022-01-01T00:00:00Z" OR display_name = "My Authorized View Set"`
  * ORDER_BY: An expression to order the authorized view sets listed in the response. For example: 
    * `create_time`
    * `create_time desc`
    * `update_time`
    * `update_time desc`
    * `display_name`
    * `display_name desc`



HTTP method and URL: 
    
    
    GET https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets?page_size=PAGE_SIZE&page_token=PAGE_TOKEN&filter=FILTER&order_by=ORDER_BY

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets?page_size=PAGE_SIZE&page_token=PAGE_TOKEN&filter=FILTER&order_by=ORDER_BY"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets?page_size=PAGE_SIZE&page_token=PAGE_TOKEN&filter=FILTER&order_by=ORDER_BY" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "authorizedViewSets": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID",
          "displayName": "My Authorized View Set",
          "createTime": "2022-01-01T00:00:00.000000Z",
          "updateTime": "2022-01-01T00:00:00.000000Z"
        },
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID_2",
          "displayName": "Another Authorized View Set",
          "createTime": "2022-01-02T00:00:00.000000Z",
          "updateTime": "2022-01-02T00:00:00.000000Z"
        },
      ],
      "nextPageToken": "NEXT_PAGE_TOKEN"
    }
    

## Authorized views

Authorized views define restricted number of conversations and an agent's or manager's role for them.

### Create an authorized view

### REST

Creating an authorized view requires the `contactcenterinsights.authorizedView.create` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The location of your Customer Experience Insights data.
  * AUTHORIZED_VIEW_SET_ID: The identifier for the authorized view set this authorized view belongs to.
  * AUTHORIZED_VIEW_ID: An optional user-defined identifier for the authorized view to create; this value must be 1-63 characters, begin and end with [a-z0-9], and can contain dashes (-) between characters.
  * DISPLAY_NAME: A descriptive name for the authorized view set.
  * CONVERSATION_FILTER: The filter to apply to the data. You can use the following fields: `agent_id`. 
    * `agent_id = "agent_123"`
    * `agent_id = "agent_123" OR agent_id = "agent_456"`
    * `quality_metadata.agent_info.agent_id: "agent_456"`
    * `quality_metadata.agent_info.teams: "team_123"`



HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews?authorized_view_id=AUTHORIZED_VIEW_ID

Request JSON body: 
    
    
    {
      "displayName": "DISPLAY_NAME",
      "conversation_filter": "CONVERSATION_FILTER"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews?authorized_view_id=AUTHORIZED_VIEW_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews?authorized_view_id=AUTHORIZED_VIEW_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID",
      "displayName": "DISPLAY_NAME",
      "conversationFilter": "CONVERSATION_FILTER",
      "createTime": "2022-01-01T00:00:00.000000Z",
      "updateTime": "2022-01-01T00:00:00.000000Z"
    }
    

### Read an authorized view

### REST

Reading an authorized view requires the `contactcenterinsights.authorizedView.get` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The location of your Customer Experience Insights data.
  * AUTHORIZED_VIEW_SET_ID: The identifier for the authorized view set.
  * AUTHORIZED_VIEW_ID: The identifier for the authorized view.



HTTP method and URL: 
    
    
    GET https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID",
      "displayName": "DISPLAY_NAME",
      "conversationFilter": "CONVERSATION_FILTER",
      "createTime": "2022-01-01T00:00:00.000000Z",
      "updateTime": "2022-01-01T00:00:00.000000Z"
    }
    

### Update an authorized view

### REST

Updating an authorized view requires the `contactcenterinsights.authorizedView.update` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The location of your Customer Experience Insights data.
  * AUTHORIZED_VIEW_SET_ID: The identifier for the authorized view set this authorized view belongs to.
  * AUTHORIZED_VIEW_ID: The identifier for the authorized view to update.
  * DISPLAY_NAME: A descriptive name for the authorized view set.
  * CONVERSATION_FILTER: The filter to apply to the data. You can use the following fields: `agent_id`. 
    * `agent_id = "agent_123"`
    * `agent_id = "agent_123" OR agent_id = "agent_456"`
    * `quality_metadata.agent_info.agent_id: "agent_456"`
    * `quality_metadata.agent_info.teams: "team_123"`
  * UPDATE_MASK: The fields to update. This value is a comma-separated list of fields. 
    * `display_name`
    * `conversation_filter`



HTTP method and URL: 
    
    
    PATCH https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID?update_mask=display_name,conversation_filter

Request JSON body: 
    
    
    {
      "displayName": "DISPLAY_NAME",
      "conversation_filter": "CONVERSATION_FILTER"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID?update_mask=display_name,conversation_filter"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID?update_mask=display_name,conversation_filter" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID",
      "displayName": "DISPLAY_NAME",
      "conversationFilter": "CONVERSATION_FILTER",
      "createTime": "2022-01-01T00:00:00.000000Z",
      "updateTime": "2022-01-01T00:00:00.000000Z"
    }
    

### Delete an authorized view

### REST

Deleting an authorized view requires the `contactcenterinsights.authorizedView.delete` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The location of your Customer Experience Insights data.
  * AUTHORIZED_VIEW_SET_ID: The identifier for the authorized view set.
  * AUTHORIZED_VIEW_ID: The identifier for the authorized view.



HTTP method and URL: 
    
    
    DELETE https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {}
    

### List authorized views

### REST

Listing authorized view sets requires the `contactcenterinsights.authorizedViews.list` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The location of your Customer Experience Insights data.
  * AUTHORIZED_VIEW_SET_ID: A user-defined identifier for the authorized view set.
  * PAGE_SIZE: The maximum number of views to return in the response. If the value is zero, the service will select a default size. A call might return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.
  * PAGE_TOKEN: The value returned by the last `ListAuthorizedViewsResponse`. This value indicates that this is a continuation of a prior `ListAuthorizedViews` call and that the system should return the next page of data.
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
    
    
    GET https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews?page_size=PAGE_SIZE&page_token=PAGE_TOKEN&filter=FILTER&order_by=ORDER_BY

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews?page_size=PAGE_SIZE&page_token=PAGE_TOKEN&filter=FILTER&order_by=ORDER_BY"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews?page_size=PAGE_SIZE&page_token=PAGE_TOKEN&filter=FILTER&order_by=ORDER_BY" | Select-Object -Expand Content

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
    

### Add IAM policy on an authorized view

### REST

Adding the IAM policy on an authorized view requires the `contactcenterinsights.authorizedView.addIamPolicy` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The location of your Customer Experience Insights data.
  * AUTHORIZED_VIEW_SET_ID: The identifier for the authorized view set.
  * AUTHORIZED_VIEW_ID: The identifier for the authorized view.
  * PRINCIPAL: The principal (user) to whom you want to grant access.
  * ROLE: The role to grant to the user.



HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID:addIamPolicy

Request JSON body: 
    
    
    {
      "policy": {
        "bindings": [
          {
            "role": "roles/ROLE",
            "members": [
              "PRINCIPAL"
            ]
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID:addIamPolicy"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID:addIamPolicy" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "version": 1,
      "etag": "BwW...",
      "bindings": [
        {
          "role": "roles/ROLE",
          "members": [
            "PRINCIPAL"
          ]
        }
      ]
    }
    

### Read IAM policy on an authorized view

### REST

Reading the IAM policy on an authorized view requires the `contactcenterinsights.authorizedView.getIamPolicy` permission.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The location of your Customer Experience Insights data.
  * AUTHORIZED_VIEW_SET_ID: The identifier for the authorized view set.
  * AUTHORIZED_VIEW_ID: The identifier for the authorized view.



HTTP method and URL: 
    
    
    GET https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID:getIamPolicy

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID:getIamPolicy"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/AUTHORIZED_VIEW_SET_ID/authorizedViews/AUTHORIZED_VIEW_ID:getIamPolicy" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "version": 1,
      "etag": "BwW...",
      "bindings": [
        {
          "role": "roles/ROLE",
          "members": [
            "PRINCIPAL"
          ]
        }
      ]
    }
    

## Example organization setup

This example demonstrates how to set up authorized views for a simplified organization. This example uses the [REST API](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest) to create and manage resources in a fictional project named `acme-corp`.

Acme has the following structure:

  * **Alice:** Alice is the administrator of the project. 
    * **Bob:** Bob is the manager.
    * **Carol:** Carol is an agent.
    * **Dave:** Dave is an agent.



Each user has a [principal identifier](https://docs.cloud.google.com/iam/docs/principal-identifiers) associated with their email address.

  * Alice's is `user:admin.alice@acme.com`.
  * Bob's is `user:manager.bob@acme.com`.
  * Carol's is `user:agent.carol@acme.com`.
  * Dave's is `user:agent.dave@acme.com`.



Each agent has an `agent_id` which corresponds to the [Conversation.agent_id](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations#resource:-conversation) field for their conversations.

  * Carol's is `agent-carol`.
  * Dave's is `agent-dave`.



### Requirements

Each user requires the following levels of access:

  * **Administrator Access:** As the administrator, Alice has full access to all data and resources.
  * **Manager Access:** As the manager, Bob can create, edit, and view conversations and analyses for their respective teams.
  * **Agent Access:** As the agents, Carol and Dave can only view conversations and analyses they participated in.



## Step 1: Grant project access

Add all users to the project and grant them `roles/browser`. This role allows them to view the project and its resources.

### Grant project browser to users

The following code illustrates how you could grant the browser role to each member of Acme.
    
    
    gcloud projects add-iam-policy-binding acme-corp \
        --member="user:admin.alice@acme.com" \
        --role="roles/browser"
    
    gcloud projects add-iam-policy-binding acme-corp \
        --member="user:manager.bob@acme.com" \
        --role="roles/browser"
    
    gcloud projects add-iam-policy-binding acme-corp \
        --member="user:agent.carol@acme.com" \
        --role="roles/browser"
    
    gcloud projects add-iam-policy-binding acme-corp \
        --member="user:agent.dave@acme.com" \
        --role="roles/browser"
    

For more information, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

You can also use Google Groups to manage access to your project. Instead of granting permissions to individual users, you can grant `roles/browser` to a group. For example, you could create a group called `project-browsers@acme.com` and add Bob to this group. Then, you could grant `roles/browser` role to this group. For more information, see [Google Groups](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console).

## Step 2: Grant project level permissions to an administrator

Grant your administrator `roles/contactcenterinsights.admin` at the project level. For example, Alice is the administrator at Acme, so she'd gain full access to all the resources with this role.

### Grant the Admin role

The following code illustrates how you could grant Alice the Admin role:
    
    
    gcloud projects add-iam-policy-binding acme-corp \
        --member="user:admin.alice@acme.com" \
        --role="roles/contactcenterinsights.admin"
    

## Step 3: Create authorized view sets

Create two authorized view sets to group the authorized views for managers and agents.

### Create an editor authorized view set

### REST

This example creates an authorized view set named `editor-view-set` to group views that have manager permissions. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets?authorized_view_set_id=editor-view-set

Request JSON body: 
    
    
    {
      "displayName": "Editor View Set"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets?authorized_view_set_id=editor-view-set"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets?authorized_view_set_id=editor-view-set" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/editor-view-set",
      "displayName": "Editor View Set",
      "createTime": "2022-01-01T00:00:00.000000Z",
      "updateTime": "2022-01-01T00:00:00.000000Z"
    }
    

### Create a viewer authorized view set

### REST

This example creates an authorized view set named `viewer-view-set` to group views that have agent permissions. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets?authorized_view_set_id=viewer-view-set

Request JSON body: 
    
    
    {
      "displayName": "Viewer View Set"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets?authorized_view_set_id=viewer-view-set"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets?authorized_view_set_id=viewer-view-set" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/viewer-view-set",
      "displayName": "Viewer View Set",
      "createTime": "2022-01-01T00:00:00.000000Z",
      "updateTime": "2022-01-01T00:00:00.000000Z"
    }
    

## Step 4: Grant project-level permissions to authorized view sets

Authorized views are [resources with built-in identities](https://docs.cloud.google.com/iam/docs/resources-with-built-in-identities) and require permissions to access {product_name} data. To give authorized views the ability to access conversations and operations, grant them the following roles:

  * `roles/contactcenterinsights.editor` for all authorized views in the `editor-view-set`
  * `roles/contactcenterinsights.viewer` for all authorized views in the `viewer-view-set`



For more information, see [grant or revoke a role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role).

### Grant the editor role to `editor-view-set`

This example grants `roles/contactcenterinsights.editor` to `editor-view-set`.

### gcloud
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="principalSet://contactcenterinsights.googleapis.com/projects/PROJECT_NUMBER/type/AuthorizedView/ancestor.name/authorizedViewSets/editor-view-set" \
        --role="roles/contactcenterinsights.editor"
    

### Grant the viewer role to `viewer-view-set`

This example grants the `roles/contactcenterinsights.viewer` role to the `viewer-view-set` authorized view set.

### gcloud
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="principalSet://contactcenterinsights.googleapis.com/projects/PROJECT_NUMBER/type/AuthorizedView/ancestor.name/authorizedViewSets/viewer-view-set" \
        --role="roles/contactcenterinsights.viewer"
    

## Step 5: Create authorized views

Create an authorized view for each manager and agent, and apply the appropriate filters.

### Create a manager's authorized view

### REST

This example creates an authorized view with the ID `bobs-editor-view` that filters conversations on `agent_id = carol OR agent_id = dave`. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViews?authorized_view_id=bobsEditorView

Request JSON body: 
    
    
    {
      "displayName": "Bob's Editor View",
      "value": {
        "filter": "agent_id = \"agent-carol\" OR agent_id = \"agent-dave\""
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViews?authorized_view_id=bobsEditorView"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViews?authorized_view_id=bobsEditorView" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/authorizedViews/bobs-editor-view",
      "displayName": "Bob's Editor View",
      "createTime": "2022-01-01T00:00:00.000000Z",
      "updateTime": "2022-01-01T00:00:00.000000Z",
      "conversationFilter":"agent_id = \"agent-carol\" OR agent_id = \"agent-dave\""
    }
    

### Grant the Authorized Editor role to a manager

### REST

This example grants `roles/contactcenterinsights.authorizedEditor` to the Acme manager, Bob, on `bobs-editor-view`.

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/editor-view-set/authorizedViews/bobs-editor-view:setIamPolicy

Request JSON body: 
    
    
    {
      "policy": {
        "bindings": [
          {
            "role": "roles/contactcenterinsights.editor",
            "members": [
              "user:manager.bob@acme.com"
            ]
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/editor-view-set/authorizedViews/bobs-editor-view:setIamPolicy"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/editor-view-set/authorizedViews/bobs-editor-view:setIamPolicy" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "version": 1,
      "etag": "BwW...",
      "bindings": [
        {
          "role": "roles/contactcenterinsights.editor",
          "members": [
            "user:manager.bob@acme.com"
          ]
        }
      ]
    }
    

### Create an agent's authorized view

### REST

This example creates an authorized view for the Acme agent named Carol. This authorized view has the ID `carols-viewer-view`, which filters conversations for `agent_id = agent-carol`.

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViews?authorized_view_id=carols-viewer-view

Request JSON body: 
    
    
    {
      "displayName": "Carol's Viewer View",
      "value": {
        "filter": "agent_id = \"agent-carol\""
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViews?authorized_view_id=carols-viewer-view"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViews?authorized_view_id=carols-viewer-view" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/authorizedViews/carols-viewer-view",
      "displayName": "Carol's Viewer View",
      "createTime": "2022-01-01T00:00:00.000000Z",
      "updateTime": "2022-01-01T00:00:00.000000Z",
      "conversationFilter": "agent_id = \"agent-carol\""
    }
    

### Grant the Authorized Viewer role to an agent

### REST

This example grants `roles/contactcenterinsights.authorizedViewer` to Carol on `carols-viewer-view`.

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/viewer-view-set/authorizedViews/carols-viewer-view:setIamPolicy

Request JSON body: 
    
    
    {
      "policy": {
        "bindings": [
          {
            "role": "roles/contactcenterinsights.viewer",
            "members": [
              "user:agent.carol@acme.com"
            ]
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/viewer-view-set/authorizedViews/carols-viewer-view:setIamPolicy"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/viewer-view-set/authorizedViews/carols-viewer-view:setIamPolicy" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "version": 1,
      "etag": "BwW...",
      "bindings": [
        {
          "role": "roles/contactcenterinsights.viewer",
          "members": [
            "user:agent.carol@acme.com"
          ]
        }
      ]
    }
    

### Create another agent's authorized view

### REST

This example creates an authorized view for the Acme agent named Dave. This authorized view has the ID `daves-viewer-view`, which filters conversations for `agent_id = agent-dave`.

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViews?authorized_view_id=daves-viewer-view

Request JSON body: 
    
    
    {
      "displayName": "Dave's Viewer View",
      "value": {
        "filter": "agent_id = \"agent-dave\""
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViews?authorized_view_id=daves-viewer-view"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViews?authorized_view_id=daves-viewer-view" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/authorizedViews/daves-viewer-view",
      "displayName": "Dave's Viewer View",
      "createTime": "2022-01-01T00:00:00.000000Z",
      "updateTime": "2022-01-01T00:00:00.000000Z",
      "conversationFilter": "agent_id = \"agent-dave\""
    }
    

### Grant Authorized Viewer role to another agent

### REST

This example grants `roles/contactcenterinsights.authorizedViewer` to Dave on `daves-viewer-view`.

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/viewer-view-set/authorizedViews/daves-viewer-view:setIamPolicy

Request JSON body: 
    
    
    {
      "policy": {
        "bindings": [
          {
            "role": "roles/contactcenterinsights.viewer",
            "members": [
              "user:agent.dave@acme.com"
            ]
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/viewer-view-set/authorizedViews/daves-viewer-view:setIamPolicy"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authorizedViewSets/viewer-view-set/authorizedViews/daves-viewer-view:setIamPolicy" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "version": 1,
      "etag": "BwW...",
      "bindings": [
        {
          "role": "roles/contactcenterinsights.viewer",
          "members": [
            "user:agent.dave@acme.com"
          ]
        }
      ]
    }
    

## What's next?

  * [Use authorized views](https://docs.cloud.google.com/gemini-enterprise-cx/insights/use-authorized-views)
  * [Best practices for authorized views](https://docs.cloud.google.com/gemini-enterprise-cx/insights/best-practices-for-authorized-views)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

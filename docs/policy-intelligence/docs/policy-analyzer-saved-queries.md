---
url: https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-saved-queries/
title: Manage saved queries \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:48.646507+00:00
---

# Manage saved queries  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-saved-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Manage saved queries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to create, manage, and run saved [Policy Analyzer queries](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies). You can create up to 200 saved queries on an asset. This limit does not include the saved queries of its children. For example, if you have 10 projects under an organization, each project can have up to 200 saved queries and the organization can have up to 200 saved queries.

## Before you begin

  1. Enable the Cloud Asset API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudasset.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required roles

To get the permissions that you need to create and manage saved queries, ask your administrator to grant you the [Cloud Asset Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.owner) (`roles/cloudasset.owner`) IAM role on the project, folder, or organization that you will save your query to. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create and manage saved queries. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage saved queries:

  * `cloudasset.savedqueries.create`
  * `cloudasset.savedqueries.delete`
  * `cloudasset.savedqueries.get`
  * `cloudasset.savedqueries.list`
  * `cloudasset.savedqueries.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a saved query

### gcloud

To create a saved Policy Analyzer query in a parent project, folder, or organization, use the `gcloud asset saved-queries create` command. 

Before using any of the command data below, make the following replacements: 

  * `SCOPE_RESOURCE_TYPE_PLURAL`: The type of the resource that you want to scope your search to, in plural form. Only IAM allow policies attached to this resource and to its descendants will be analyzed. Use the value `projects`, `folders`, or `organizations`. 
  * `SCOPE_RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to scope your search to. Only IAM allow policies attached to this resource and to its descendants will be analyzed. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `FULL_RESOURCE_NAME`: Optional. The full resource name of the resource that you want to analyze access for. For a list of full resource name formats, see [Resource name format](https://docs.cloud.google.com/asset-inventory/docs/resource-name-format). 
  * `PRINCIPAL`: Optional. The principal whose access you want to analyze, in the form `PRINCIPAL_TYPE:ID`—for example, `user:my-user@example.com`. For a full list of the principal types, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers). 
  * `PERMISSION_1`, `PERMISSION_2`... `PERMISSION_N`: Optional. The permissions that you want to check for—for example, `compute.instances.get`. If you list multiple permissions, Policy Analyzer will check for any of the permissions listed. 
  * `QUERY_ID`: The ID to use for the saved query, which must be unique in the specified parent resource (project, folder, or organization). You can use letters, numbers, and hyphens in the query ID. 
  * `RESOURCE_TYPE`: The resource type that you want to save a query for. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to save a query for. Project IDs can be alphanumeric or numeric. Folder and organization IDs are numeric. 
  * `LABEL_KEY` and `LABEL_VALUE`: Optional. A comma-separated list of key/value pairs to attach to the query, which can be used in search and list operations. You can include up to 10 labels for each saved query. 
  * `DESCRIPTION`: Optional. A string describing the query.



Save the following content in a file called `request.json`: 
    
    
    {
      "IamPolicyAnalysisQuery": {
        "scope": "SCOPE_RESOURCE_TYPE_PLURAL/SCOPE_RESOURCE_ID",
        "resourceSelector": {
          "fullResourceName": "FULL_RESOURCE_NAME"
        },
        "identitySelector": {
          "identity": "PRINCIPAL"
        },
        "accessSelector": {
          "permissions": [
            "PERMISSION_1",
            "PERMISSION_2",
            "PERMISSION_N"
          ]
        }
      }
    }

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset saved-queries create \
    QUERY_ID \
    --RESOURCE_TYPE=RESOURCE_ID \
    --query-file-path=request.json \
    --labels="LABEL_KEY=LABEL_VALUE" \
    --description="DESCRIPTION"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset saved-queries create `
    QUERY_ID `
    --RESOURCE_TYPE=RESOURCE_ID `
    --query-file-path=request.json `
    --labels="LABEL_KEY=LABEL_VALUE" `
    --description="DESCRIPTION"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset saved-queries create ^
    QUERY_ID ^
    --RESOURCE_TYPE=RESOURCE_ID ^
    --query-file-path=request.json ^
    --labels="LABEL_KEY=LABEL_VALUE" ^
    --description="DESCRIPTION"

The response contains the saved query. For example, it might look like the following: 
    
    
    content:
      iamPolicyAnalysisQuery:
        resourceSelector:
          fullResourceName: //cloudresourcemanager.googleapis.com/projects/my-project
        identitySelector:
          identity: user:my-user@example.com
        scope: projects/scope-project
    createTime: '2022-04-18T22:47:25.640783Z'
    description: A query checking what permissions my-user@example.com has on my-project
    labels:
      user: my-user
    lastUpdateTime: '2022-04-18T22:47:25.640783Z'
    name: projects/12345678901/savedQueries/my-query
    

### REST

To create a saved Policy Analyzer query in a parent project, folder, or organization, use the Cloud Asset Inventory API's `[savedQueries.create](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/create)` method. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type that you want to save a query for. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to save a query for. Project IDs can be alphanumeric or numeric. Folder and organization IDs are numeric. 
  * `QUERY_ID`: The ID to use for the saved query, which must be unique in the specified parent resource (project, folder, or organization). You can use letters, numbers, and hyphens in the query ID. 
  * `SCOPE_RESOURCE_TYPE`: The type of the resource that you want to scope your search to. Only IAM allow policies attached to this resource and to its descendants will be analyzed. Use the value `projects`, `folders`, or `organizations`. 
  * `SCOPE_RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to scope your search to. Only IAM allow policies attached to this resource and to its descendants will be analyzed. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `FULL_RESOURCE_NAME`: Optional. The full resource name of the resource that you want to analyze access for. For a list of full resource name formats, see [Resource name format](https://docs.cloud.google.com/asset-inventory/docs/resource-name-format). 
  * `PRINCIPAL`: Optional. The principal whose access you want to analyze, in the form `PRINCIPAL_TYPE:ID`—for example, `user:my-user@example.com`. For a full list of the principal types, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers). 
  * `PERMISSION_1`, `PERMISSION_2`... `PERMISSION_N`: Optional. The permissions that you want to check for—for example, `compute.instances.get`. If you list multiple permissions, Policy Analyzer will check for any of the permissions listed. 
  * `LABEL_KEY` and `LABEL_VALUE`: Optional. A key/value pair to attach to the query, which can be used in search and list operations. You can include up to 10 labels for each saved query. 
  * `DESCRIPTION`: Optional. A string describing the query.



HTTP method and URL: 
    
    
    POST https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/savedQueries?savedQueryId=QUERY_ID

Request JSON body: 
    
    
    {
      "content": {
        "iamPolicyAnalysisQuery": {
          "scope": "SCOPE_RESOURCE_TYPE/SCOPE_RESOURCE_ID",
          "resourceSelector": {
            "fullResourceName": "FULL_RESOURCE_NAME"
          },
          "identitySelector": {
            "identity": "PRINCIPAL"
          },
          "accessSelector": {
            "permissions": [
              "PERMISSION_1",
              "PERMISSION_2",
              "PERMISSION_N"
            ]
          }
        }
      },
      "labels": {
        "LABEL_KEY": "LABEL_VALUE"
      },
      "description": "DESCRIPTION"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/savedQueries?savedQueryId=QUERY_ID"

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
        -Uri "https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/savedQueries?savedQueryId=QUERY_ID" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response contains the saved query. For example, it might look like the following: 
    
    
    {
      "name": "projects/12345678901/savedQueries/my-query",
      "description": "A query checking what permissions my-user@example.com has on my-project",
      "createTime": "2022-04-18T22:47:25.640783Z",
      "lastUpdateTime": "2022-04-18T22:47:25.640783Z",
      "labels": {
        "user": "my-user"
      },
      "content": {
        "iamPolicyAnalysisQuery": {
          "scope": "projects/scope-project",
          "resourceSelector": {
            "fullResourceName": "//cloudresourcemanager.googleapis.com/projects/my-project"
          },
          "identitySelector": {
            "identity": "user:my-user@example.com"
          }
        }
      }
    }
    

## Run a saved query

### gcloud

To run a saved analysis query, use the `[gcloud asset analyze-iam-policy](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy)` command. 

Before using any of the command data below, make the following replacements: 

  * `SCOPE_RESOURCE_TYPE`: The type of the resource that you want to scope your search to. Only IAM allow policies attached to this resource and to its descendants will be analyzed. Use the value `project`, `folder`, or `organization`. 
  * `SCOPE_RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to scope your search to. Only IAM allow policies attached to this resource and to its descendants will be analyzed. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `RESOURCE_TYPE_PLURAL`: The resource type where the query is saved. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_NUM_ID`: The numeric ID of the Google Cloud project, folder, or organization where the query is saved. You can't use the alphanumeric project ID to identify a project—you must use the project number. 
  * `QUERY_ID`: The ID of the saved query that you want to use.



Execute the [gcloud asset analyze-iam-policy](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset analyze-iam-policy \
    --SCOPE_RESOURCE_TYPE=SCOPE_RESOURCE_ID \
    --saved-analysis-query=RESOURCE_TYPE_PLURAL/RESOURCE_NUM_ID/savedQueries/QUERY_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset analyze-iam-policy `
    --SCOPE_RESOURCE_TYPE=SCOPE_RESOURCE_ID `
    --saved-analysis-query=RESOURCE_TYPE_PLURAL/RESOURCE_NUM_ID/savedQueries/QUERY_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset analyze-iam-policy ^
    --SCOPE_RESOURCE_TYPE=SCOPE_RESOURCE_ID ^
    --saved-analysis-query=RESOURCE_TYPE_PLURAL/RESOURCE_NUM_ID/savedQueries/QUERY_ID

The response contains the results of running the saved query on the specified resource. For examples of query results, see [Analyze IAM policies](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies). 

### REST

To run a saved analysis query, use the Cloud Asset Inventory API's `[analyzeIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy)` method. 

Before using any of the request data, make the following replacements: 

  * `SCOPE_RESOURCE_TYPE`: The type of the resource that you want to scope your search to. Only IAM allow policies attached to this resource and to its descendants will be analyzed. Use the value `projects`, `folders`, or `organizations`. 
  * `SCOPE_RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to scope your search to. Only IAM allow policies attached to this resource and to its descendants will be analyzed. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `RESOURCE_TYPE`: The resource type where the query is saved. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_NUM_ID`: The numeric ID of the Google Cloud project, folder, or organization where the query is saved. You can't use the alphanumeric project ID to identify a project—you must use the project number. 
  * `QUERY_ID`: The ID of the saved query that you want to use.

**Note:** If you want more detailed query results, you can [enable advanced options](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#options). 

HTTP method and URL: 
    
    
    POST https://cloudasset.googleapis.com/v1/SCOPE_RESOURCE_TYPE/SCOPE_RESOURCE_ID:analyzeIamPolicy

Request JSON body: 
    
    
    {
      "savedAnalysisQuery": "RESOURCE_TYPE/RESOURCE_NUM_ID/savedQueries/QUERY_ID"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "X-HTTP-Method-Override: GET" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudasset.googleapis.com/v1/SCOPE_RESOURCE_TYPE/SCOPE_RESOURCE_ID:analyzeIamPolicy"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "X-HTTP-Method-Override" = "GET" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://cloudasset.googleapis.com/v1/SCOPE_RESOURCE_TYPE/SCOPE_RESOURCE_ID:analyzeIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response contains the results of running the saved query on the specified resource. For examples of query results, see [Analyze IAM policies](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies). 

## Get a saved query

### gcloud

To get a saved Policy Analyzer query, use the `gcloud asset saved-queries get` command. 

Before using any of the command data below, make the following replacements: 

  * `QUERY_ID`: The ID of the saved query that you want to get. 
  * `RESOURCE_TYPE`: The resource type where the query is saved. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization where the query is saved. Project IDs can be alphanumeric or numeric. Folder and organization IDs are numeric. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset saved-queries describe QUERY_ID --RESOURCE_TYPE=RESOURCE_NUM_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset saved-queries describe QUERY_ID --RESOURCE_TYPE=RESOURCE_NUM_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset saved-queries describe QUERY_ID --RESOURCE_TYPE=RESOURCE_NUM_ID

The response contains the saved query. For example, it might look like the following: 
    
    
    content:
      iamPolicyAnalysisQuery:
        resourceSelector:
          fullResourceName: //cloudresourcemanager.googleapis.com/projects/my-project
        identitySelector:
          identity: user:my-user@example.com
        scope: projects/scope-project
    createTime: 2022-04-18T22:47:25.640783Z
    description: A query checking what permissions my-user@example.com has on my-project
    labels:
      user: my-user
    lastUpdateTime: 2022-04-18T22:47:25.640783Z
    name: projects/12345678901/savedQueries/my-query
    

### REST

To get a saved Policy Analyzer query, use the Cloud Asset Inventory API's `[savedQueries.get](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/get)` method. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type where the query is saved. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_NUM_ID`: The numeric ID of the Google Cloud project, folder, or organization where the query is saved. You can't use the alphanumeric project ID to identify a project—you must use the project number. 
  * `QUERY_ID`: The ID of the saved query that you want to get. 



HTTP method and URL: 
    
    
    GET https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_NUM_ID/savedQueries/QUERY_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "X-HTTP-Method-Override: GET" \  
         "https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_NUM_ID/savedQueries/QUERY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "X-HTTP-Method-Override" = "GET" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_NUM_ID/savedQueries/QUERY_ID" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The response contains the saved query. For example, it might look like the following: 
    
    
    {
      "name": "projects/12345678901/savedQueries/my-query",
      "description": "A query checking what permissions my-user@example.com has on my-project",
      "createTime": "2022-04-18T22:47:25.640783Z",
      "lastUpdateTime": "2022-04-18T22:47:25.640783Z",
      "labels": {
        "user": "my-user"
      },
      "content": {
        "iamPolicyAnalysisQuery": {
          "scope": "projects/scope-project",
          "resourceSelector": {
            "fullResourceName": "//cloudresourcemanager.googleapis.com/projects/my-project"
          },
          "identitySelector": {
            "identity": "user:my-user@example.com"
          }
        }
      }
    }
    

## List saved queries

### gcloud

To list all saved Policy Analyzer queries in a project, folder, or organization, use the `gcloud asset saved-queries list` command. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type where the queries are saved. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to list saved queries for. Project IDs can be alphanumeric or numeric. Folder and organization IDs are numeric. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset saved-queries list --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset saved-queries list --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset saved-queries list --RESOURCE_TYPE=RESOURCE_ID

The response contains all saved Policy Analyzer queries for the project, folder, or organization. For example, it might look like the following: 
    
    
    savedQueries:
    - content:
        iamPolicyAnalysisQuery:
          resourceSelector:
            fullResourceName: //cloudresourcemanager.googleapis.com/projects/my-project
          identitySelector:
            identity: user:my-user@example.com
          scope: projects/scope-project
      createTime: '2022-04-15T21:17:33.777212Z'
      description: A query checking what permissions my-user@example.com has on my-project
      labels:
        missing-info: permissions
      lastUpdateTime: '2022-04-15T21:17:33.777212Z'
      name: projects/12345678901/savedQueries/query-1
    - content:
        iamPolicyAnalysisQuery:
          accessSelector:
            permissions:
            - iam.roles.get
            - iam.roles.list
          identitySelector:
            identity: user:my-user@example.com
          scope: projects/scope-project
      createTime: '2022-04-18T22:47:25.640783Z'
      description: A query checking what resources my-user@example.com has permission to view roles on
      labels:
        missing-info: resource
      lastUpdateTime: '2022-04-18T22:47:25.640783Z'
      name: projects/12345678901/savedQueries/query-2
    

### REST

To list all saved Policy Analyzer queries in a project, folder, or organization, use the Cloud Asset Inventory API's `[savedQueries.list](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/list)` method. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type where the queries are saved. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to list saved queries for. Project IDs can be alphanumeric or numeric. Folder and organization IDs are numeric. 



HTTP method and URL: 
    
    
    GET https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/savedQueries

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "X-HTTP-Method-Override: GET" \  
         "https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/savedQueries"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "X-HTTP-Method-Override" = "GET" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/savedQueries" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/list). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The response contains all saved Policy Analyzer queries for the project, folder, or organization. For example, it might look like the following: 
    
    
    {
      "savedQueries": [
        {
          "name": "projects/12345678901/savedQueries/query-1",
          "description": "A query checking what permissions my-user@example.com has on my-project",
          "createTime": "2022-04-15T21:17:33.777212Z",
          "lastUpdateTime": "2022-04-15T21:17:33.777212Z",
          "labels": {
            "missing-info": "permission"
          },
          "content": {
            "iamPolicyAnalysisQuery": {
              "scope": "projects/scope-project",
              "resourceSelector": {
                "fullResourceName": "//cloudresourcemanager.googleapis.com/projects/my-project"
              },
              "identitySelector": {
                "identity": "user:my-user@example.com"
              }
            }
          }
        },
        {
          "name": "projects/12345678901/savedQueries/query-2",
          "description": "A query checking what resources my-user@example.com has permission to view roles on",
          "createTime": "2022-04-18T22:47:25.640783Z",
          "lastUpdateTime": "2022-04-18T22:47:25.640783Z",
          "labels": {
            "missing-info": "resource"
          },
          "content": {
            "iamPolicyAnalysisQuery": {
              "scope": "projects/scope-project",
              "accessSelector": {
                "permissions": [
                  "iam.roles.get",
                  "iam.roles.list"
                ]
              },
              "identitySelector": {
                "identity": "user:my-user@example.com"
              }
            }
          }
        }
      ]
    }
    

## Update a saved query

### gcloud

To update a saved Policy Analyzer query, use the `gcloud asset saved-queries update` command. 

Before using any of the command data below, make the following replacements: 

  * `UPDATED_QUERY`: Optional. The updated Policy Analyzer query that you want to save. To learn how to format the query, see Create a saved query. 
  * `RESOURCE_TYPE`: The resource type where the query is saved. Use the value `project`, `folder`, or `organization`. 
  * `QUERY_ID`: The ID of the saved query that you want to edit. 
  * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization where the query is saved. Project IDs can be alphanumeric or numeric. Folder and organization IDs are numeric. 
  * `UPDATED_LABELS`: Optional. The updated labels that you want to attach to the saved query. You can also remove labels with the `--remove-labels="KEY_1,KEY_2"` flag, or clear all labels with the `--clear-labels` flag. 
  * `UPDATED_DESCRIPTION`: Optional. An updated description for the saved query.



Save the following content in a file called `request.json`: 
    
    
    {
      "IamPolicyAnalysisQuery": {
        UPDATED_QUERY
      }
    }

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset saved-queries update \
    QUERY_ID \
    --RESOURCE_TYPE=RESOURCE_ID \
    --query-file-path=request.json \
    --update-labels="UPDATED_LABELS" \
    --description="DESCRIPTION"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset saved-queries update `
    QUERY_ID `
    --RESOURCE_TYPE=RESOURCE_ID `
    --query-file-path=request.json `
    --update-labels="UPDATED_LABELS" `
    --description="DESCRIPTION"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset saved-queries update ^
    QUERY_ID ^
    --RESOURCE_TYPE=RESOURCE_ID ^
    --query-file-path=request.json ^
    --update-labels="UPDATED_LABELS" ^
    --description="DESCRIPTION"

The response contains the updated query. 

### REST

To update a saved Policy Analyzer query, use the Cloud Asset Inventory API's `[savedQueries.patch](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/patch)` method. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type where the query is saved. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_NUM_ID`: The numeric ID of the Google Cloud project, folder, or organization where the query is saved. You can't use the alphanumeric project ID to identify a project—you must use the project number. 
  * `QUERY_ID`: The ID of the saved query that you want to edit. 
  * `UPDATED_FIELDS`: A comma-separated lists of the fields that you want to update. For example, if you are updating the content, labels, and description fields, you would use the value `content,labels,description`. 
  * `UPDATED_QUERY`: Optional. The updated Policy Analyzer query that you want to save. To learn how to format the query, see Create a saved query. 
  * `UPDATED_LABELS`: Optional. The updated labels that you want to attach to the saved query. 
  * `UPDATED_DESCRIPTION`: Optional. An updated description for the saved query.



HTTP method and URL: 
    
    
    POST https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_NUM_ID/savedQueries/QUERY_ID?update_mask=UPDATED_FIELDS

Request JSON body: 
    
    
    {
      "content": {
        "iamPolicyAnalysisQuery": {
          UPDATED_QUERY
      },
      "labels": {
        UPDATED_LABELS
      },
      "description": "UPDATED_DESCRIPTION"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "X-HTTP-Method-Override: GET" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_NUM_ID/savedQueries/QUERY_ID?update_mask=UPDATED_FIELDS"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "X-HTTP-Method-Override" = "GET" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_NUM_ID/savedQueries/QUERY_ID?update_mask=UPDATED_FIELDS" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/patch). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response contains the updated query. 

## Delete a saved query

### gcloud

To delete a saved Policy Analyzer query, use the `gcloud asset saved-queries delete` command. 

Before using any of the command data below, make the following replacements: 

  * `QUERY_ID`: The ID of the saved query that you want to delete. 
  * `RESOURCE_TYPE`: The resource type where the query is saved. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_NUM_ID`: The numeric ID of the Google Cloud project, folder, or organization where the query is saved. You can't use the alphanumeric project ID to identify a project—you must use the project number. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset saved-queries delete \
    QUERY_ID \
    --RESOURCE_TYPE=RESOURCE_NUM_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset saved-queries delete `
    QUERY_ID `
    --RESOURCE_TYPE=RESOURCE_NUM_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset saved-queries delete ^
    QUERY_ID ^
    --RESOURCE_TYPE=RESOURCE_NUM_ID

### REST

To delete a saved Policy Analyzer query, use the Cloud Asset Inventory API's `[savedQueries.delete](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/delete)` method. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type where the query is saved. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_NUM_ID`: The numeric ID of the Google Cloud project, folder, or organization where the query is saved. You can't use the alphanumeric project ID to identify a project—you must use the project number. 
  * `QUERY_ID`: The ID of the saved query that you want to delete. 



HTTP method and URL: 
    
    
    DELETE https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_NUM_ID/savedQueries/QUERY_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "X-HTTP-Method-Override: GET" \  
         "https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_NUM_ID/savedQueries/QUERY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "X-HTTP-Method-Override" = "GET" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_NUM_ID/savedQueries/QUERY_ID" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

If the query is successfully deleted, the API returns an empty response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

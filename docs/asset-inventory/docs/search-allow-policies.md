---
url: https://docs.cloud.google.com/asset-inventory/docs/search-allow-policies/
title: Search for IAM allow policies on resources \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:43:52.413557+00:00
---

# Search for IAM allow policies on resources  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/search-allow-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Guides ](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview)



Send feedback 

#  Search for IAM allow policies on resources Stay organized with collections  Save and categorize content based on your preferences. 

You can search for IAM allow policies on your resources in a project, folder, or organization, and filter the returned results using a query.

**Note:** To find deny policies, you can use a [resource search](https://docs.cloud.google.com/asset-inventory/docs/search-resources#deny-policies).

## Before you begin

  1. Enable the Cloud Asset Inventory API in the project you're running Cloud Asset Inventory commands from.

[Enable the Cloud Asset Inventory API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com)

  2. Make sure your account has the [correct role to call the Cloud Asset Inventory API](https://docs.cloud.google.com/asset-inventory/docs/roles-permissions#roles). For individual permissions for each call type, see [Permissions](https://docs.cloud.google.com/asset-inventory/docs/roles-permissions#permissions).




## Construct a query

Before constructing a query, it can be useful to start with a search request that _doesn't_ specify a query. Use the fields and values from the full response to create a query using the [search query syntax](https://docs.cloud.google.com/asset-inventory/docs/search-query-syntax), and refine it until the results you want are returned.

Fields that can be used in a query are detailed in the [`IamPolicySearchResult` reference documentation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllIamPolicies#IamPolicySearchResult.FIELDS).

Keep in mind the following limitations when constructing a query:

  * The [`policy` field](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Policy) is a nested object, so can only be used with the `:` operator.

  * Not all asset types are searchable. See [Resource types](https://docs.cloud.google.com/asset-inventory/docs/asset-types#resource-types) to confirm if a service isn't available in the search APIs.




The following additional fields can also be used to restrict your results to certain principal types, permissions, or roles:

Field | Description | `memberTypes` |  Contains one of the following [ IAM principal types](https://docs.cloud.google.com/iam/docs/principals-overview#principal-types):

  * `user`
  * `group`
  * `domain`
  * `serviceAccount`
  * `allUsers`
  * `allAuthenticatedUsers`



##### Example
    
    
    memberTypes=user  
  
---|---  
`policy.role.permissions` |  Contains specific [ IAM permissions](https://docs.cloud.google.com/iam/docs/permissions-reference).

##### Example
    
    
    policy.role.permissions=storage.buckets.create

**Note** : The caller must have the `iam.roles.get` permission for permissions to be listed in a `searchAllIamPolicies` response.  
`roles` |  Contains specific [ IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles). 

##### Example
    
    
    roles=roles/storage.objectAdmin  
  
## Search for IAM allow policies

Before constructing a query, it can be useful to start with a search request that _doesn't_ specify a query. Use the fields and values from the full response to create a query using the [search query syntax](https://docs.cloud.google.com/asset-inventory/docs/search-query-syntax), and refine it until the results you want are returned.

#### Console

To search for IAM allow policy metadata, complete the following steps.

  1. Go to the **Asset Inventory** page in the Google Cloud console.

[Go to Asset Inventory](https://console.cloud.google.com/iam-admin/asset-inventory/policies)

  2. Change to the project, folder, or organization you want to search.
  3. Click the **IAM policy** tab.
  4. To search allow policies, enter a query in the **Filter** field. See [ Search query syntax](https://docs.cloud.google.com/asset-inventory/docs/search-query-syntax) to learn how to write a search query.

To make constructing queries easier, you can click the **Filter** field to display and add the available searchable fields to your query.




After performing a search, the allow policies matching the query are listed in the **Results** table. Double-click your query to edit it, or use the **Filter results** pane to apply quick **Query presets** or restrict the search results by specific criteria.

To view the query as a Google Cloud CLI command, click **View query**.

To export the results, click **Download CSV**.

#### gcloud
    
    
    gcloud asset search-all-iam-policies \
        --scope=SCOPE_PATH \
        --query="QUERY" \
        --asset-types=ASSET_TYPE_1,ASSET_TYPE_2,... \
        --order-by="ORDER_BY"

Provide the following values:

  * `SCOPE_PATH`: Use one of the following values:

    * `projects/PROJECT_ID`, where `PROJECT_ID` is the ID of the project that has assets with IAM allow policies you want to search for. 
    * `projects/PROJECT_NUMBER`, where `PROJECT_NUMBER` is the number of the project that has assets with IAM allow policies you want to search for. 

How to find a Google Cloud project number

### Google Cloud console

To find a Google Cloud project number, complete the following steps:

      1. Go to the **Welcome** page in the Google Cloud console.

[ Go to Welcome](https://console.cloud.google.com/welcome)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box, and then search for your project name. The project name, project number, and project ID are shown near the **Welcome** heading. 

Up to 4,000 resources are displayed. If you don't see the project you're looking for, go to the [**Manage resources**](https://console.cloud.google.com//cloud-resource-manager) page and filter the list using the name of that project. 

### gcloud CLI

You can retrieve a Google Cloud project number with the following command:
    
    gcloud projects describe PROJECT_ID --format="value(projectNumber)"

    * `folders/FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that has assets with IAM allow policies you want to search for. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organizations/ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that has assets with IAM allow policies you want to search for. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `QUERY`: Optional. The query expression. If not specified or empty, all resources are searched for in the specified scope. To learn how to write a search query, see [Search query syntax](https://docs.cloud.google.com/asset-inventory/docs/search-query-syntax). 
  * `ASSET_TYPE_#`: Optional. A comma-separated list of [searchable asset types](https://docs.cloud.google.com/asset-inventory/docs/asset-types). [RE2-compatible regular expressions](https://github.com/google/re2/wiki/Syntax) are supported. If the regular expression doesn't match any supported asset type, an `INVALID_ARGUMENT` error is returned. When `--asset-types` isn't specified, all asset types are returned. 
  * `ORDER_BY`: Optional. A comma-separated list of fields specifying the sorting order of the results. The default order is ascending. Add `DESC` after the field name to indicate descending order. See the [ reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies#--order-by) for a list of fields you can sort by. 



You can use the [`--format`](https://docs.cloud.google.com/sdk/gcloud/reference#--format) and [`--flatten`](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten) flags to format the gcloud CLI output.

See the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies) for all options. 

### Example

Run the following command to get a list of all the Compute Engine instances (`compute.googleapis.com/Instance`) in the `my-project` project with an IAM allow policy binding them to the user `alex@example.com`. The results are in descending order by resource (`resource DESC`). 
    
    
    gcloud asset search-all-iam-policies \
        --scope=projects/my-project \
        --query="policy:\"user:**alex@example.com** \"" \
        --asset-types=compute.googleapis.com/Instance \
        --order-by="resource DESC"

#### Example response
    
    
    ---
    assetType: compute.googleapis.com/Instance
    folders:
    - folders/0000000000000
    organization: organizations/0000000000000
    policy:
      bindings:
      - members:
        - user:alex@example.com
        role: roles/compute.viewer
      - members:
        - user:alex@example.com
        role: roles/editor
      - members:
        - user:alex@example.com
        role: roles/owner
    project: projects/0000000000000
    resource: //compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/debian
    

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/SCOPE_PATH:searchAllIamPolicies
    

**Note** : You can use a `GET` method for this request with parameters as a query string. However, the request URL is [length limited](https://docs.cloud.google.com/apis/docs/http#long_request_urls), meaning the server rejects the request if the query string is too long. To avoid length restrictions, use a `POST` request instead, set a header of `X-HTTP-Method-Override: GET`, and use a JSON body for your parameters. 

Request JSON body:
    
    
    {
      "query": "QUERY",
      "assetTypes": [
        "ASSET_TYPE_1",
        "ASSET_TYPE_2",
        "..."
      ],
      "orderBy": "ORDER_BY",
      "pageSize": "PAGE_SIZE",
      "pageToken": "PAGE_TOKEN"
    }

Provide the following values:

  * `SCOPE_PATH`: Use one of the following values:

    * `projects/PROJECT_ID`, where `PROJECT_ID` is the ID of the project that has assets with IAM allow policies you want to search for. 
    * `projects/PROJECT_NUMBER`, where `PROJECT_NUMBER` is the number of the project that has assets with IAM allow policies you want to search for. 

How to find a Google Cloud project number

### Google Cloud console

To find a Google Cloud project number, complete the following steps:

      1. Go to the **Welcome** page in the Google Cloud console.

[ Go to Welcome](https://console.cloud.google.com/welcome)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box, and then search for your project name. The project name, project number, and project ID are shown near the **Welcome** heading. 

Up to 4,000 resources are displayed. If you don't see the project you're looking for, go to the [**Manage resources**](https://console.cloud.google.com//cloud-resource-manager) page and filter the list using the name of that project. 

### gcloud CLI

You can retrieve a Google Cloud project number with the following command:
    
    gcloud projects describe PROJECT_ID --format="value(projectNumber)"

    * `folders/FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that has assets with IAM allow policies you want to search for. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organizations/ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that has assets with IAM allow policies you want to search for. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `QUERY`: Optional. The query expression. If not specified or empty, all resources are searched for in the specified scope. To learn how to write a search query, see [Search query syntax](https://docs.cloud.google.com/asset-inventory/docs/search-query-syntax). 
  * `ASSET_TYPE_#`: Optional. An array of [searchable asset types](https://docs.cloud.google.com/asset-inventory/docs/asset-types). [RE2-compatible regular expressions](https://github.com/google/re2/wiki/Syntax) are supported. If the regular expression doesn't match any supported asset type, an `INVALID_ARGUMENT` error is returned. When `assetTypes` isn't specified, all asset types are returned. 
  * `ORDER_BY`: Optional. A comma-separated list of fields specifying the sorting order of the results. The default order is ascending. Add `DESC` after the field name to indicate descending order. See the [ reference documentation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllIamPolicies#body.QUERY_PARAMETERS.order_by) for a list of fields you can sort by. 
  * `PAGE_SIZE`: Optional. The number of results to return per page. The maximum is 500. If the value is set to `0` or a negative value, an appropriate default is selected. A `nextPageToken` is returned to retrieve subsequent results. 
  * `PAGE_TOKEN`: Optional. Long request responses are separated over multiple pages. When `pageToken` isn't specified, the first page is returned. Subsequent pages can be called by using the previous response's `nextPageToken` as the `pageToken` value. 



See the [REST reference](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllIamPolicies) for all options.

### Command examples

Run one of the following commands to get a list of all the Compute Engine instances (`compute.googleapis.com/Instance`) in the `my-project` project with an IAM allow policy binding them to the user `alex@example.com`. The results are in descending order by resource (`resource DESC`). 

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "X-HTTP-Method-Override: GET" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "query": "policy:\"user:**alex@example.com** \"",
                "assetTypes": ["compute.googleapis.com/Instance"],
                "orderBy": "resource DESC"
              }' \
         https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-HTTP-Method-Override" = "GET";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "query": "policy:\"user:**alex@example.com** \"",
      "assetTypes": ["compute.googleapis.com/Instance"],
      "orderBy": "resource DESC"
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies" | Select-Object -Expand Content

#### Example response
    
    
    {
      "resource": "//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/debian",
      "project": "projects/0000000000000",
      "policy": {
        "bindings": [
          {
            "role": "roles/compute.viewer",
            "members": [
              "user:alex@example.com"
            ]
          },
          {
            "role": "roles/editor",
            "members": [
              "user:alex@example.com"
            ]
          },
          {
            "role": "roles/owner",
            "members": [
              "user:alex@example.com"
            ]
          }
        ]
      },
      "assetType": "compute.googleapis.com/Instance",
      "folders": [
        "folders/0000000000000"
      ],
      "organization": "organizations/0000000000000"
    }

#### C#

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://docs.cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.Asset.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.html);
    using System.Collections.Generic;
    using System.Linq;
    
    public class SearchAllIamPoliciesSample
    {
        public SearchAllIamPoliciesResponse SearchAllIamPolicies(string scope, string query)
        {
            // Create the client.
            [AssetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html) client = [AssetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html#Google_Cloud_Asset_V1_AssetServiceClient_Create)();
    
            // Build the request.
            [SearchAllIamPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.SearchAllIamPoliciesRequest.html) request = new [SearchAllIamPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.SearchAllIamPoliciesRequest.html)
            {
                Scope = scope,
                Query = query,
            };
    
            // Call the API.
            PagedEnumerable<SearchAllIamPoliciesResponse, IamPolicySearchResult> response = client.[SearchAllIamPolicies](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.AssetServiceClient.html#Google_Cloud_Asset_V1_AssetServiceClient_SearchAllIamPolicies_Google_Cloud_Asset_V1_SearchAllIamPoliciesRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Return the first page.
            IEnumerable<SearchAllIamPoliciesResponse> byPages = response.AsRawResponses();
            return byPages.First();
        }
    }

#### Go

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://docs.cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample search-all-iam-policies searches all IAM policies within the given scope.
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"log"
    
    	asset "cloud.google.com/go/asset/apiv1"
    	"cloud.google.com/go/asset/apiv1/assetpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	scope := flag.String("scope", "", "Scope of the search.")
    	query := flag.String("query", "", "Query statement.")
    	flag.Parse()
    	ctx := context.Background()
    	client, err := asset.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("asset.NewClient: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/asset/latest/apiv1.html#cloud_google_com_go_asset_apiv1_Client_Close)()
    
    	req := &assetpb.SearchAllIamPoliciesRequest{
    		Scope: *scope,
    		Query: *query,
    	}
    	it := client.SearchAllIamPolicies(ctx, req)
    	for {
    		policy, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			log.Fatal(err)
    		}
    		fmt.Println(policy)
    	}
    }
    

#### Java

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://docs.cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[InvalidArgumentException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InvalidArgumentException.html);
    import com.google.cloud.asset.v1.[AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html);
    import com.google.cloud.asset.v1.[AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html).[SearchAllIamPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.SearchAllIamPoliciesPagedResponse.html);
    import com.google.cloud.asset.v1.[SearchAllIamPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.SearchAllIamPoliciesRequest.html);
    import java.io.IOException;
    
    public class SearchAllIamPoliciesExample {
    
      // Searches for all the iam policies within the given scope.
      public static void searchAllIamPolicies(String scope, String query) {
        // TODO(developer): Replace these variables before running the sample.
        int pageSize = 0;
        String pageToken = "";
    
        [SearchAllIamPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.SearchAllIamPoliciesRequest.html) request =
            [SearchAllIamPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.SearchAllIamPoliciesRequest.html).newBuilder()
                .setScope(scope)
                .setQuery(query)
                .setPageSize(pageSize)
                .setPageToken(pageToken)
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html) client = [AssetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.html).create()) {
          [SearchAllIamPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AssetServiceClient.SearchAllIamPoliciesPagedResponse.html) response = client.searchAllIamPolicies(request);
          System.out.println("Search completed successfully:\n" + response.getPage().getValues());
        } catch (IOException e) {
          System.out.println(String.format("Failed to create client:%n%s", e.toString()));
        } catch ([InvalidArgumentException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InvalidArgumentException.html) e) {
          System.out.println(String.format("Invalid request:%n%s", e.toString()));
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.out.println(String.format("Error during SearchAllIamPolicies:%n%s", e.toString()));
        }
      }
    }

#### Node.js

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://docs.cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const scope = '';
    // const query = '';
    // const pageSize = 0;
    // const pageToken = '';
    
    const util = require('util');
    const {AssetServiceClient} = require('[@google-cloud/asset](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)');
    
    const client = new [AssetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)();
    const projectId = await client.getProjectId();
    
    async function searchAllIamPolicies() {
      const request = {
        scope: `projects/${projectId}`,
        query: query,
        pageSize: pageSize,
        pageToken: pageToken,
      };
      const options = {
        autoPaginate: false,
      };
    
      // Handle the operation using the promise pattern.
      const result = await client.searchAllIamPolicies(request, options);
      // Do things with with the response.
      console.log(util.inspect(result, {depth: null}));
    }

#### PHP

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://docs.cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Asset\V1\Client\AssetServiceClient;
    use Google\Cloud\Asset\V1\SearchAllIamPoliciesRequest;
    
    /**
     * @param string $scope      Scope of the search
     * @param string $query      (Optional) Query statement
     * @param int    $pageSize   (Optional) Size of each result page
     * @param string $pageToken  (Optional) Token produced by the preceding call
     */
    function search_all_iam_policies(
        string $scope,
        string $query = '',
        int $pageSize = 0,
        string $pageToken = ''
    ) {
        // Instantiate a client.
        $asset = new AssetServiceClient();
    
        // Run request
        $request = (new SearchAllIamPoliciesRequest())
            ->setScope($scope)
            ->setQuery($query)
            ->setPageSize($pageSize)
            ->setPageToken($pageToken);
        $response = $asset->searchAllIamPolicies($request);
    
        // Print the resources that the policies are set on
        foreach ($response->getPage() as $policy) {
            print($policy->getResource() . PHP_EOL);
        }
    }

#### Python

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://docs.cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    # TODO scope = 'Scope of the search'
    # TODO query = 'Query statement'
    # TODO page_size = Size of each result page
    
    client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html)()
    response = client.[search_all_iam_policies](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceClient_search_all_iam_policies)(
        request={"scope": scope, "query": query, "page_size": page_size}
    )
    for policy in response:
        print(policy)
        break

#### Ruby

To learn how to install and use the client library for Cloud Asset Inventory, see [Cloud Asset Inventory client libraries](https://docs.cloud.google.com/asset-inventory/docs/client-libraries). 

To authenticate to Cloud Asset Inventory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/asset"
    
    # scope = 'SCOPE_OF_THE_QUERY'
    # query = 'QUERY_STATEMENT'
    # page_size = 'SIZE_OF_EACH_RESULT_PAGE'
    # page_token = 'TOKEN_PRODUCED_BY_THE_PRECEDING_CALL'
    asset_service = Google::Cloud::[Asset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset.html).[asset_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset/latest/Google-Cloud-Asset.html)
    
    response = asset_service.search_all_iam_policies(
      scope:      scope,
      query:      query,
      page_size:  page_size,
      page_token: page_token
    )
    # Do things with the response
    response.page.each do |policy|
      puts policy
    end

## Additional search examples

The following code samples show specific search queries for both gcloud and REST to help you to construct your own searches.

### Resources with IAM allow policies

The following sample shows how to search for all resources with IAM allow policies in the `my-project` project.

#### gcloud
    
    
    gcloud asset search-all-iam-policies \
        --scope=projects/**my-project** \
        --flatten="policy.bindings[].members[]" \
        --format="table(resource, policy.bindings.role, policy.bindings.members)"

#### REST

HTTP method and URL:
    
    
    GET https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies
    

### Command examples

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "Authorization" = "Bearer $cred"
    }
    
    
    Invoke-WebRequest `
      -Method GET `
      -Headers $headers `
      -Uri "https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies" | Select-Object -Expand Content

### Named resources with IAM allow policies

The following sample shows how to search for all resources with `example` in their name that have IAM allow policies.

#### gcloud
    
    
    gcloud asset search-all-iam-policies \
        --scope=projects/**my-project** \
        --query="resource:example"

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies
    

**Note** : You can use a `GET` method for this request with parameters as a query string. However, the request URL is [length limited](https://docs.cloud.google.com/apis/docs/http#long_request_urls), meaning the server rejects the request if the query string is too long. To avoid length restrictions, use a `POST` request instead, set a header of `X-HTTP-Method-Override: GET`, and use a JSON body for your parameters. 

Request JSON body:
    
    
    {
      "pageSize": 1,
      "query": "resource:example"
    }

### Command examples

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "X-HTTP-Method-Override: GET" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "pageSize": 1,
                "query": "resource:example"
              }' \
         https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-HTTP-Method-Override" = "GET";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "pageSize": 1,
      "query": "resource:example"
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies" | Select-Object -Expand Content

### IAM allow policies on projects, folders, and organizations

The following sample shows how to search for all IAM allow policies on all projects and folders in the organization with the ID `my-organization-id`.

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

  1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

  2. Click the **switcher** list box in the menu bar.
  3. Select your organization from the list box.
  4. Click the **All** tab. The organization ID is shown next to the organization name.



### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

#### gcloud
    
    
    gcloud asset search-all-iam-policies \
        --scope=organizations/**my-organization-id** \
        --asset-types=cloudresourcemanager.*

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies
    

**Note** : You can use a `GET` method for this request with parameters as a query string. However, the request URL is [length limited](https://docs.cloud.google.com/apis/docs/http#long_request_urls), meaning the server rejects the request if the query string is too long. To avoid length restrictions, use a `POST` request instead, set a header of `X-HTTP-Method-Override: GET`, and use a JSON body for your parameters. 

Request JSON body:
    
    
    {
      "assetTypes": "cloudresourcemanager.*",
      "pageSize": 1,
    }

### Command examples

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "X-HTTP-Method-Override: GET" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "assetTypes": "cloudresourcemanager.*",
                "pageSize": 1,
              }' \
         https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-HTTP-Method-Override" = "GET";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "assetTypes": "cloudresourcemanager.*",
      "pageSize": 1,
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies" | Select-Object -Expand Content

### Owners on a project

The following sample shows how to search for principals with the [Owner role](https://docs.cloud.google.com/iam/docs/understanding-roles#owner) (`roles/owner`) on the project `my-project`.

This request only returns principals who have been granted the Owner role on the project. It doesn't include principals who inherit the Owner role through [policy inheritance](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control).

#### gcloud
    
    
    gcloud asset search-all-iam-policies \
        --scope=projects/**my-project** \
        --query="roles:roles/owner" \
        --asset-types=cloudresourcemanager.* \
        --flatten="policy.bindings[].members[]" \
        --format="table(policy.bindings.members)"

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies
    

**Note** : You can use a `GET` method for this request with parameters as a query string. However, the request URL is [length limited](https://docs.cloud.google.com/apis/docs/http#long_request_urls), meaning the server rejects the request if the query string is too long. To avoid length restrictions, use a `POST` request instead, set a header of `X-HTTP-Method-Override: GET`, and use a JSON body for your parameters. 

Request JSON body:
    
    
    {
      "assetTypes": "cloudresourcemanager.*",
      "pageSize": 1,
      "query": "roles:roles/owner"
    }

### Command examples

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "X-HTTP-Method-Override: GET" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "assetTypes": "cloudresourcemanager.*",
                "pageSize": 1,
                "query": "roles:roles/owner"
              }' \
         https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-HTTP-Method-Override" = "GET";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "assetTypes": "cloudresourcemanager.*",
      "pageSize": 1,
      "query": "roles:roles/owner"
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies" | Select-Object -Expand Content

### Projects where a principal has the owner role

The following sample shows how to search for projects where `alex@example.com` has the [Owner role](https://docs.cloud.google.com/iam/docs/understanding-roles#owner) (`roles/owner`), in the organization with the ID `my-organization-id`.

This request only returns the projects on which `alex@example.com` has been granted the Owner role. It doesn't include projects that `alex@example.com` has [inherited](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control) the Owner role on.

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

  1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

  2. Click the **switcher** list box in the menu bar.
  3. Select your organization from the list box.
  4. Click the **All** tab. The organization ID is shown next to the organization name.



### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

#### gcloud
    
    
    gcloud asset search-all-iam-policies \
        --scope=organizations/**my-organization-id** \
        --query="policy:(roles/owner **alex@example.com**)" \
        --asset-types=cloudresourcemanager.googleapis.com/Project \
        --format="table(resource)"

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies
    

**Note** : You can use a `GET` method for this request with parameters as a query string. However, the request URL is [length limited](https://docs.cloud.google.com/apis/docs/http#long_request_urls), meaning the server rejects the request if the query string is too long. To avoid length restrictions, use a `POST` request instead, set a header of `X-HTTP-Method-Override: GET`, and use a JSON body for your parameters. 

Request JSON body:
    
    
    {
      "assetTypes": "cloudresourcemanager.googleapis.com/Project",
      "pageSize": 1,
      "query": "policy:(roles/owner **alex@example.com**)"
    }

### Command examples

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "X-HTTP-Method-Override: GET" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "assetTypes": "cloudresourcemanager.googleapis.com/Project",
                "pageSize": 1,
                "query": "policy:(roles/owner **alex@example.com**)"
              }' \
         https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-HTTP-Method-Override" = "GET";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "assetTypes": "cloudresourcemanager.googleapis.com/Project",
      "pageSize": 1,
      "query": "policy:(roles/owner **alex@example.com**)"
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies" | Select-Object -Expand Content

### Roles a principal has on a project

The following sample shows how to search for the roles `alex@example.com` has on the `my-project` project.

This request only returns the roles that `alex@example.com` is granted on the project. It doesn't include roles that `alex@example.com` inherited through [policy inheritance](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control).

#### gcloud
    
    
    gcloud asset search-all-iam-policies \
        --scope=projects/**my-project** \
        --query="policy:**alex@example.com** " \
        --asset-types=cloudresourcemanager.googleapis.com/Project \
        --flatten="policy.bindings[]" \
        --format="table(policy.bindings.role)"

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies
    

**Note** : You can use a `GET` method for this request with parameters as a query string. However, the request URL is [length limited](https://docs.cloud.google.com/apis/docs/http#long_request_urls), meaning the server rejects the request if the query string is too long. To avoid length restrictions, use a `POST` request instead, set a header of `X-HTTP-Method-Override: GET`, and use a JSON body for your parameters. 

Request JSON body:
    
    
    {
      "assetTypes": "cloudresourcemanager.googleapis.com/Project",
      "pageSize": 1,
      "query": "policy:**alex@example.com** "
    }

### Command examples

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "X-HTTP-Method-Override: GET" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "assetTypes": "cloudresourcemanager.googleapis.com/Project",
                "pageSize": 1,
                "query": "policy:**alex@example.com** "
              }' \
         https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-HTTP-Method-Override" = "GET";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "assetTypes": "cloudresourcemanager.googleapis.com/Project",
      "pageSize": 1,
      "query": "policy:**alex@example.com** "
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies" | Select-Object -Expand Content

### Permissions a principal has on a project

The following sample shows how to search for the permissions `alex@example.com` has on the `my-project` project.

This request only returns the permissions that `alex@example.com` has on the project. It doesn't include permissions that `alex@example.com` inherited through [policy inheritance](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control).

#### gcloud
    
    
    gcloud asset search-all-iam-policies \
        --scope=projects/**my-project** \
        --query="policy:**alex@example.com** policy.role.permissions:\"\"" \
        --asset-types=cloudresourcemanager.* \
        --format="default(explanation.matchedPermissions)"

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies
    

**Note** : You can use a `GET` method for this request with parameters as a query string. However, the request URL is [length limited](https://docs.cloud.google.com/apis/docs/http#long_request_urls), meaning the server rejects the request if the query string is too long. To avoid length restrictions, use a `POST` request instead, set a header of `X-HTTP-Method-Override: GET`, and use a JSON body for your parameters. 

Request JSON body:
    
    
    {
      "assetTypes": "cloudresourcemanager.*",
      "pageSize": 1,
      "query": "policy:**alex@example.com**  policy.role.permissions:\"\""
    }

### Command examples

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "X-HTTP-Method-Override: GET" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "assetTypes": "cloudresourcemanager.*",
                "pageSize": 1,
                "query": "policy:**alex@example.com**  policy.role.permissions:\"\""
              }' \
         https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-HTTP-Method-Override" = "GET";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "assetTypes": "cloudresourcemanager.*",
      "pageSize": 1,
      "query": "policy:**alex@example.com**  policy.role.permissions:\"\""
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies" | Select-Object -Expand Content

### Principals who can access Cloud Storage buckets

The following sample shows how to search for principals who can access Cloud Storage buckets in the `my-project` project.

#### gcloud
    
    
    gcloud asset search-all-iam-policies \
        --scope=projects/**my-project** \
        --query="policy.role.permissions:storage.buckets" \
        --asset-types=cloudresourcemanager.* \
        --flatten="policy.bindings[].members[]" \
        --format="table(policy.bindings.members)"

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies
    

**Note** : You can use a `GET` method for this request with parameters as a query string. However, the request URL is [length limited](https://docs.cloud.google.com/apis/docs/http#long_request_urls), meaning the server rejects the request if the query string is too long. To avoid length restrictions, use a `POST` request instead, set a header of `X-HTTP-Method-Override: GET`, and use a JSON body for your parameters. 

Request JSON body:
    
    
    {
      "assetTypes": "cloudresourcemanager.*",
      "pageSize": 1,
      "query": "policy.role.permissions:storage.buckets"
    }

### Command examples

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "X-HTTP-Method-Override: GET" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "assetTypes": "cloudresourcemanager.*",
                "pageSize": 1,
                "query": "policy.role.permissions:storage.buckets"
              }' \
         https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-HTTP-Method-Override" = "GET";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "assetTypes": "cloudresourcemanager.*",
      "pageSize": 1,
      "query": "policy.role.permissions:storage.buckets"
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/projects/**my-project** :searchAllIamPolicies" | Select-Object -Expand Content

### Service accounts that have an owner role

The following sample shows how to search for service accounts with the [Owner role](https://docs.cloud.google.com/iam/docs/understanding-roles#owner) (`roles/owner`) in the organization with the `my-organization-id`. You can use this query to help reduce your risk profile.

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

  1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

  2. Click the **switcher** list box in the menu bar.
  3. Select your organization from the list box.
  4. Click the **All** tab. The organization ID is shown next to the organization name.



### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

#### gcloud

This example uses the `grep` command, which is available in Cloud Shell and Unix-like operating systems. 
    
    
    gcloud asset search-all-iam-policies \
        --scope=organizations/**my-organization-id** \
        --query="policy:(roles/owner serviceAccount)" \
        --flatten="policy.bindings[].members[]" \
        --format="table(resource.segment(3):label=RESOURCE_TYPE, resource.basename():label=RESOURCE, policy.bindings.members)" |
        grep serviceAccount

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies
    

**Note** : You can use a `GET` method for this request with parameters as a query string. However, the request URL is [length limited](https://docs.cloud.google.com/apis/docs/http#long_request_urls), meaning the server rejects the request if the query string is too long. To avoid length restrictions, use a `POST` request instead, set a header of `X-HTTP-Method-Override: GET`, and use a JSON body for your parameters. 

Request JSON body:
    
    
    {
      "pageSize": 1,
      "query": "policy:(roles/owner serviceAccount)"
    }

### Command examples

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "X-HTTP-Method-Override: GET" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "pageSize": 1,
                "query": "policy:(roles/owner serviceAccount)"
              }' \
         https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-HTTP-Method-Override" = "GET";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "pageSize": 1,
      "query": "policy:(roles/owner serviceAccount)"
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies" | Select-Object -Expand Content

### Resources with roles granted to a domain

The following sample shows how to search for resources with roles granted to the `example.com` domain, in the organization with the ID `my-organization-id`.

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

  1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

  2. Click the **switcher** list box in the menu bar.
  3. Select your organization from the list box.
  4. Click the **All** tab. The organization ID is shown next to the organization name.



### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

#### gcloud
    
    
    gcloud asset search-all-iam-policies \
        --scope=organizations/**my-organization-id** \
        --query="policy:\"domain:**example.com** \"" \
        --flatten="policy.bindings[]" \
        --format="table(resource, policy.bindings.role)"

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies
    

**Note** : You can use a `GET` method for this request with parameters as a query string. However, the request URL is [length limited](https://docs.cloud.google.com/apis/docs/http#long_request_urls), meaning the server rejects the request if the query string is too long. To avoid length restrictions, use a `POST` request instead, set a header of `X-HTTP-Method-Override: GET`, and use a JSON body for your parameters. 

Request JSON body:
    
    
    {
      "pageSize": 1,
      "query": "policy:\"domain:DOMAIN_NAME\""
    }

### Command examples

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "X-HTTP-Method-Override: GET" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "pageSize": 1,
                "query": "policy:\"domain:DOMAIN_NAME\""
              }' \
         https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-HTTP-Method-Override" = "GET";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "pageSize": 1,
      "query": "policy:\"domain:DOMAIN_NAME\""
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies" | Select-Object -Expand Content

### Resources with roles granted to the public

The following sample shows how to search for resources with roles granted to the the public, in the organization with the ID `my-organization-id`.

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

  1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

  2. Click the **switcher** list box in the menu bar.
  3. Select your organization from the list box.
  4. Click the **All** tab. The organization ID is shown next to the organization name.



### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

#### gcloud
    
    
    gcloud asset search-all-iam-policies \
        --scope=organizations/**my-organization-id** \
        --query="memberTypes:(allUsers OR allAuthenticatedUsers)" \
        --format="table(resource)"

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies
    

**Note** : You can use a `GET` method for this request with parameters as a query string. However, the request URL is [length limited](https://docs.cloud.google.com/apis/docs/http#long_request_urls), meaning the server rejects the request if the query string is too long. To avoid length restrictions, use a `POST` request instead, set a header of `X-HTTP-Method-Override: GET`, and use a JSON body for your parameters. 

Request JSON body:
    
    
    {
      "pageSize": 1,
      "query": "memberTypes:(allUsers OR allAuthenticatedUsers)"
    }

### Command examples

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "X-HTTP-Method-Override: GET" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "pageSize": 1,
                "query": "memberTypes:(allUsers OR allAuthenticatedUsers)"
              }' \
         https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-HTTP-Method-Override" = "GET";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "pageSize": 1,
      "query": "memberTypes:(allUsers OR allAuthenticatedUsers)"
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies" | Select-Object -Expand Content

### Principals who can change IAM allow policies in an organization

The following sample shows how to search for principals who can change IAM allow policies in the organization with the ID `my-organization-id`.

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

  1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

  2. Click the **switcher** list box in the menu bar.
  3. Select your organization from the list box.
  4. Click the **All** tab. The organization ID is shown next to the organization name.



### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

#### gcloud
    
    
    gcloud asset search-all-iam-policies \
        --scope=organizations/**my-organization-id** \
        --query="policy.role.permissions:(resourcemanager.organizations.setIamPolicy OR resourcemanager.folders.setIamPolicy OR resourcemanager.projects.setIamPolicy)" \
        --format="json(resource, policy.bindings, explanation.matchedPermissions)"

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies
    

**Note** : You can use a `GET` method for this request with parameters as a query string. However, the request URL is [length limited](https://docs.cloud.google.com/apis/docs/http#long_request_urls), meaning the server rejects the request if the query string is too long. To avoid length restrictions, use a `POST` request instead, set a header of `X-HTTP-Method-Override: GET`, and use a JSON body for your parameters. 

Request JSON body:
    
    
    {
      "pageSize": 1,
      "query": "policy.role.permissions:(resourcemanager.organizations.setIamPolicy OR resourcemanager.folders.setIamPolicy OR resourcemanager.projects.setIamPolicy)"
    }

### Command examples

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "X-HTTP-Method-Override: GET" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "pageSize": 1,
                "query": "policy.role.permissions:(resourcemanager.organizations.setIamPolicy OR resourcemanager.folders.setIamPolicy OR resourcemanager.projects.setIamPolicy)"
              }' \
         https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-HTTP-Method-Override" = "GET";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "pageSize": 1,
      "query": "policy.role.permissions:(resourcemanager.organizations.setIamPolicy OR resourcemanager.folders.setIamPolicy OR resourcemanager.projects.setIamPolicy)"
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/organizations/**my-organization-id** :searchAllIamPolicies" | Select-Object -Expand Content

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

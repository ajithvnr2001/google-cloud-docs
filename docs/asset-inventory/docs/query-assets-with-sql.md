---
url: https://docs.cloud.google.com/asset-inventory/docs/query-assets-with-sql/
title: Query assets with SQL \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:35.054464+00:00
---

# Query assets with SQL  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/query-assets-with-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Guides ](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview)



Send feedback 

#  Query assets with SQL Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature requires access to the [Security Command Center Premium or Enterprise tier](https://cloud.google.com/security-command-center/pricing#tier-pricing), or [Gemini Cloud Assist](https://cloud.google.com/products/gemini/cloud-assist). For new sign ups to the Security Command Center Premium or Enterprise tier, it can take up to 6 hours for access to the API, and up to 48 hours for historical data to be ready.

You can query assets in your project, folder, or organization using a [BigQuery SQL](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)-compatible dialect.

## Before you begin

  1. Enable the Cloud Asset Inventory API in the project you're running Cloud Asset Inventory commands from.

[Enable the Cloud Asset Inventory API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com)

  2. Make sure your account has the [correct role to call the Cloud Asset Inventory API](https://docs.cloud.google.com/asset-inventory/docs/roles-permissions#roles). For individual permissions for each call type, see [Permissions](https://docs.cloud.google.com/asset-inventory/docs/roles-permissions#permissions).




## Limitations

  * [Asset type](https://docs.cloud.google.com/asset-inventory/docs/asset-types) names have `.` and `/` replaced with `_`. For example, `compute.googleapis.com/Instance` becomes `compute_googleapis_com_Instance`.

  * The request must be a `SELECT` query.

  * [Legacy BigQuery SQL](https://docs.cloud.google.com/bigquery/docs/reference/legacy-sql) isn't supported.

  * Query results [larger than 10GB aren't supported](https://docs.cloud.google.com/bigquery/quotas#query_jobs).

  * Query results larger than 10MB or 1,000 rows are always paginated.

  * Queries [must take less than 6 hours to process](https://docs.cloud.google.com/bigquery/quotas#query_jobs).

  * Query results can only be exported to a BigQuery dataset in the `US` [multi-region](https://docs.cloud.google.com/bigquery/docs/locations#multi-regions).




## Tables you can query

You can query the following tables:

  * For `RESOURCE` content types, table names in the dataset correspond to the asset type name, assuming that asset type exists. For example, the `compute_googleapis_com_Instance` table contains Compute Engine instance metadata.

  * For non-`RESOURCE` content types, table names in the dataset correspond to the [RPC/REST content type names](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types). For example, `ACCESS_POLICY`.

  * To query resource standard metadata across resource types, use the table name `STANDARD_METADATA`. This includes all fields except `resource.DATA`, which is specific to each resource type.




## Query asset metadata

#### Console

To query the asset metadata for your project, folder, or organization, complete the following steps:

  1. In the Google Cloud console, go to the **Asset query** tab on the **Asset Inventory** page.

[Go to Asset query](https://console.cloud.google.com/iam-admin/asset-inventory/query)

If the **Asset query** tab doesn't appear, you need access to the [ Security Command Center Premium or Enterprise tier](https://docs.cloud.google.com/security-command-center/pricing#tier-pricing), or [ Gemini Cloud Assist](https://cloud.google.com/products/gemini/cloud-assist). 

  2. Change to the project, folder, or organization you want to query.
  3. Click the **Asset query** tab.
  4. To query asset metadata, either use a sample query or build your own:

     * To use a sample, click an entry in the **Query library** tab to preview the query. Click **Apply** to copy that sample into the **Edit query** box, then either edit the query, or click **Run** to execute it.
     * To build your own query, enter the query text directly into the **Edit query** box, then click **Run** to execute it. To assist in writing your own query, you can click a table in the **Select table** pane to preview its schema and content. See [ Query syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax) to learn how to construct a query.

The asset metadata matching the query is shown in the **Query result** tab.

  5. Optional: To download the query result sets in CSV format, click **Export**.

The maximum size of the CSV file is 2 MB. If the download request fails because the file size exceeds this limit, a message appears with instructions for exporting the full results.




#### gcloud
    
    
    gcloud asset query \
        --SCOPE \
        --statement="SQL_SELECT_QUERY" \
        --timeout="TIMEOUTs"

Provide the following values:

  * `SCOPE`: Use one of the following values:

    * `project=PROJECT_ID`, where `PROJECT_ID` is the ID of the project that has the assets you want to query. 
    * `folder=FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that has the assets you want to query. 

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

    * `organization=ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that has the assets you want to query. 

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

  * `SQL_SELECT_QUERY`: An SQL `SELECT` query.
  * `TIMEOUT`: Optional. The maximum time, in seconds, that a client waits for the query to complete before continuing. Use timeouts to asynchronously run your query, and retrieve the results later with job references. 



See the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/asset/query) for all options. 

### Example

Run the following command to get the names and asset types of the first two Compute Engine instances in the `my-project` project. 
    
    
    gcloud asset query \
        --project=**my-project** \
        --statement="
          SELECT
            name, assetType
          FROM
            compute_googleapis_com_Instance
          LIMIT 2"

### Finished job response

The following sample shows a response to the previous example query. The response contains a job reference and tells you whether the job has finished (`done: true`). If the job has finished, then the `queryResult` object is populated with the appropriate data, and the results are listed afterward.
    
    
    done: true
    jobReference: 0000000000000000000000000000000000000000000000000000000000000000
    queryResult:
      nextPageToken: ''
      totalRows: '2'
    
    name: //compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/instance-1
    assetType: compute.googleapis.com/Instance
    
    name: //compute.googleapis.com/projects/my-project/zones/us-central1-c/instances/instance-2
    assetType: compute.googleapis.com/Instance

### Unfinished job response

If you set a timeout in your request, the query is performed asynchronously and you are sent a response that indicates the job is unfinished (`done: false`). These sorts of responses contain a job reference and an unpopulated `queryResult` object:
    
    
    done: false
    jobReference: 0000000000000000000000000000000000000000000000000000000000000000
    queryResult:
      nextPageToken: ''
      totalRows: '0'

You can use the `jobReference` value to retrieve the query results later, after the job has completed and the data is available.

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/SCOPE_PATH:queryAssets
    

Request JSON body:
    
    
    {
      "statement": "SQL_SELECT_QUERY",
      "timeout": "TIMEOUTs",
      "pageSize": "PAGE_SIZE",
      "pageToken": "PAGE_TOKEN"
    }

Provide the following values:

  * `SCOPE_PATH`: Use one of the following values:

    * `projects/PROJECT_ID`, where `PROJECT_ID` is the ID of the project that has the assets that you want to query. 
    * `projects/PROJECT_NUMBER`, where `PROJECT_NUMBER` is the number of the project that has the assets you want to query. 

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

    * `folders/FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that has the assets that you want to query. 

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

    * `organizations/ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that has the assets that you want to query. 

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

  * `SQL_SELECT_QUERY`: An SQL `SELECT` query.
  * `TIMEOUT`: Optional. The maximum time, in seconds, that a client waits for the query to complete before continuing. Use timeouts to asynchronously run your query, and retrieve the results later with job references. 
  * `PAGE_SIZE`: Optional. The number of results to return per page. The maximum is 500. If the value is set to `0` or a negative value, an appropriate default is selected. A `nextPageToken` is returned to retrieve subsequent results. 
  * `PAGE_TOKEN`: Optional. Long request responses are separated over multiple pages. When `pageToken` isn't specified, the first page is returned. Subsequent pages can be called by using the previous response's `nextPageToken` as the `pageToken` value. 



See the [REST reference](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets) for all options.

### Command examples

Run one of the following commands to get the names and asset types of the first two Compute Engine instances in the `my-project` project. 

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "statement": "
                  SELECT
                    name, assetType
                  FROM
                    compute_googleapis_com_Instance
                  LIMIT 2"
              }' \
         https://cloudasset.googleapis.com/v1/projects/**my-project** :queryAssets

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "statement": "
        SELECT
          name, assetType
        FROM
          compute_googleapis_com_Instance
        LIMIT 2"
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/projects/**my-project** :queryAssets" | Select-Object -Expand Content

### Finished job response

The following sample shows a response to the previous example query. The response contains a job reference and tells you whether the job has finished (`"done": true`). If the job has finished, then the `queryResult` object is populated with the appropriate data.

Query results are split into `rows`, an array that contains asset metadata, and `schema`, an object which describes the schema for each asset in the `rows` array. This is done to minimize duplication of field names and types in large responses.

Similarly, `f` and `v` are used in the `rows` array instead of `fields` and `value` to keep responses as small as possible.
    
    
    {
      "jobReference": "0000000000000000000000000000000000000000000000000000000000000000",
      "done": true,
      "queryResult": {
        "rows": [
          {
            "f": [
              {
                "v": "//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/instance-1"
              },
              {
                "v": "compute.googleapis.com/Instance"
              }
            ]
          },
          {
            "f": [
              {
                "v": "//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/instance-2"
              },
              {
                "v": "compute.googleapis.com/Instance"
              }
            ]
          }
        ],
        "schema": {
          "fields": [
            {
              "field": "name",
              "type": "STRING",
              "mode": "NULLABLE",
              "fields": []
            },
            {
              "field": "assetType",
              "type": "STRING",
              "mode": "NULLABLE",
              "fields": []
            }
          ]
        },
        "nextPageToken": "",
        "totalRows": "1"
      }
    }

### Unfinished job response

If you set a timeout in your request, the query is performed asynchronously and you are sent a response that indicates the job is unfinished (`"done": false`). These sorts of responses contain a job reference and an unpopulated `queryResult` object:
    
    
    {
      "jobReference": "0000000000000000000000000000000000000000000000000000000000000000",
      "done": false,
      "queryResult": {
        "rows": [],
        "schema": {
          "fields": []
        },
        "nextPageToken": "",
        "totalRows": "0"
      }
    }

You can use the `jobReference` value to retrieve the query results later, after the job has completed and the data is available.

## Retrieve query results later

To retrieve a request later that has taken time to complete, make one the following requests.

#### gcloud
    
    
    gcloud asset query \
        --SCOPE \
        --job-reference="JOB_REFERENCE"

Provide the following values:

  * `SCOPE`: Use one of the following values:

    * `project=PROJECT_ID`, where `PROJECT_ID` is the ID of the project that has the assets that you want to query. 
    * `folder=FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that has the assets that you want to query. 

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

    * `organization=ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that has the assets that you want to query. 

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

  * `JOB_REFERENCE`: The job reference value returned in a previous response. 



### Example

Run the following command to get the results of a previously run query in the `my-project` project. 
    
    
    gcloud asset query \
        --project=**my-project** \
        --job-reference="**0000000000000000000000000000000000000000000000000000000000000000** "

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/SCOPE_PATH:queryAssets
    

Request JSON body:
    
    
    {
      "jobReference": "JOB_REFERENCE",
      "pageToken": "PAGE_TOKEN"
    }

Provide the following values:

  * `SCOPE_PATH`: Use one of the following values:

    * `projects/PROJECT_ID`, where `PROJECT_ID` is the ID of the project that has the assets you want to query. 
    * `projects/PROJECT_NUMBER`, where `PROJECT_NUMBER` is the number of the project that has the assets you want to query. 

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

    * `folders/FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that has the assets you want to query. 

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

    * `organizations/ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that has the assets you want to query. 

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

  * `JOB_REFERENCE`: The job reference value returned in a previous response. 
  * `PAGE_TOKEN`: Optional. Long request responses are separated over multiple pages. When `pageToken` isn't specified, the first page is returned. Subsequent pages can be called by using the previous response's `nextPageToken` as the `pageToken` value. 



### Command examples

Run one of the following commands to get the results of a previously run query.

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "jobReference": "**0000000000000000000000000000000000000000000000000000000000000000** "
              }' \
         https://cloudasset.googleapis.com/v1/projects/**my-project** :queryAssets

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "jobReference": "**0000000000000000000000000000000000000000000000000000000000000000** "
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/projects/**my-project** :queryAssets" | Select-Object -Expand Content

## Export query results to BigQuery

Query results are returned as Query Assets API responses. To export the results to your own BigQuery table, specify a BigQuery destination in the request. If you don't already have one, you must [create a BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets) before making these requests.

#### gcloud
    
    
    gcloud asset query \
        --SCOPE \
        --billing-project=BILLING_PROJECT_ID \
        --statement="SQL_SELECT_QUERY" \
        --bigquery-table=projects/BIGQUERY_PROJECT_ID/datasets/DATASET_ID/tables/TABLE_NAME \
        --write-disposition="WRITE_METHOD"

Provide the following values:

  * `SCOPE`: Use one of the following values:

    * `project=PROJECT_ID`, where `PROJECT_ID` is the ID of the project that has the asset metadata you want to export with an SQL query. 
    * `folder=FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that has the asset metadata you want to export with an SQL query. 

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

    * `organization=ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that has the asset metadata you want to export with an SQL query. 

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

  * `BILLING_PROJECT_ID`: The project ID that the default Cloud Asset Inventory service agent is in that has permissions to manage your BigQuery datasets and tables. [ Read more about setting the billing project](https://docs.cloud.google.com/asset-inventory/docs/multiple-projects#orchestrator). 

  * `SQL_SELECT_QUERY`: An SQL `SELECT` query.
  * `BIGQUERY_PROJECT_ID`: The ID of the project that the BigQuery table is in that you want to export to. 
  * `DATASET_ID`: The ID of the BigQuery dataset.
  * `TABLE_NAME`: The BigQuery table that you're exporting your metadata to. If it doesn't exist, it's created. 
  * `WRITE_METHOD`: Specifies the behavior if the BigQuery destination table or partition already exists. The following values are supported: 

    * `write-empty`: Default. If the existing table contains data, a duplicate error is returned in the job result. 
    * `write-append`: Appends data to the table or the latest partition.
    * `write-truncate`: Overwrites the entire table or all partitions data.



### Example

Run the following command to get the names and asset types of the first two Compute Engine instances in the `my-project` project, and export the results to the `my-table` BigQuery table in the `my-project` project, overwriting the entire table if it already exists. 
    
    
    gcloud asset query \
      --project=**my-project** \
      --statement="
        SELECT
          name, assetType
        FROM
          compute_googleapis_com_Instance
        LIMIT 2" \
      --bigquery-table=projects/**my-project** /datasets/**my-dataset** /tables/**my-table** \
      --write-disposition="write-truncate"

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/SCOPE_PATH:queryAssets
    

Headers:
    
    
    X-Goog-User-Project: BILLING_PROJECT_ID

Request JSON body:
    
    
    {
      "statement": "SQL_SELECT_QUERY",
      "outputConfig": {
        "bigqueryDestination": {
          "dataset": "projects/BIGQUERY_PROJECT_ID/datasets/DATASET_ID",
          "table": "TABLE_NAME",
          "writeDisposition": "WRITE_METHOD"
        }
      },
      "pageSize": "PAGE_SIZE"
    }

Provide the following values:

  * `SCOPE_PATH`: Use one of the following values:

    * `projects/PROJECT_ID`, where `PROJECT_ID` is the ID of the project that has the asset metadata you want to export with an SQL query. 
    * `projects/PROJECT_NUMBER`, where `PROJECT_NUMBER` is the number of the project that has the asset metadata you want to export with an SQL query. 

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

    * `folders/FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that has the asset metadata you want to export with an SQL query. 

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

    * `organizations/ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that has the asset metadata you want to export with an SQL query. 

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

  * `BILLING_PROJECT_ID`: The project ID that the default Cloud Asset Inventory service agent is in that has permissions to manage your BigQuery datasets and tables. [ Read more about setting the billing project](https://docs.cloud.google.com/asset-inventory/docs/multiple-projects#orchestrator). 
  * `SQL_SELECT_QUERY`: An SQL `SELECT` query.
  * `BIGQUERY_PROJECT_ID`: The ID of the project that the BigQuery table is in that you want to export to. 
  * `DATASET_ID`: The ID of the BigQuery dataset.
  * `TABLE_NAME`: The BigQuery table that you're exporting your metadata to. If it doesn't exist, it's created. 
  * `WRITE_METHOD`: Specifies the behavior if the BigQuery destination table or partition already exists. The following values are supported: 

    * `WRITE_EMPTY`: Default. If the existing table contains data, a duplicate error is returned in the job result. 
    * `WRITE_APPEND`: Appends data to the table or the latest partition.
    * `WRITE_TRUNCATE`: Overwrites the entire table or all partitions data.
  * `PAGE_SIZE`: Optional. The number of results to return per page. The maximum is 500. If the value is set to `0` or a negative value, an appropriate default is selected. A `nextPageToken` is returned to retrieve subsequent results. 



### Command examples

Run one of the following commands to get the names and asset types of the first two Compute Engine instances in the `my-project` project, and export the results to the `my-table` BigQuery table in the `my-project` project, overwriting the entire table if it already exists. 

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "X-Goog-User-Project: BILLING_PROJECT_ID" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "statement": "
                  SELECT
                    name, assetType
                  FROM
                    compute_googleapis_com_Instance
                  LIMIT 2",
                "outputConfig": {
                  "bigqueryDestination": {
                    "dataset": "projects/**my-project** /datasets/**my-dataset** ",
                    "table": "**my-table** ",
                    "writeDisposition": "WRITE_TRUNCATE"
                  }
                }
              }' \
         https://cloudasset.googleapis.com/v1/projects/**my-project** :queryAssets

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-Goog-User-Project" = "BILLING_PROJECT_ID";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "statement": "
        SELECT
          name, assetType
        FROM
          compute_googleapis_com_Instance
        LIMIT 2",
      "outputConfig": {
        "bigqueryDestination": {
          "dataset": "projects/**my-project** /datasets/**my-dataset** ",
          "table": "**my-table** ",
          "writeDisposition": "WRITE_TRUNCATE"
        }
      }
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/projects/**my-project** :queryAssets" | Select-Object -Expand Content

## Additional SQL query examples

The following code samples show specific SQL queries you can use to search for assets, to help you construct your own queries.

### Compute Engine VM instances in a specific region

Additionally, return their `name` and when they were created.
    
    
    SELECT
      name,
      resource.DATA.creationTimestamp
    FROM
      compute_googleapis_com_Instance
    WHERE
      resource.location LIKE '%asia%'
    

### Details of an app running in a Kubernetes pod

Return the namespace, version, and timestamp of the app `ingress-nginx`. Learn more about [JSON functions used in BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/json_functions).
    
    
    SELECT
      name AS pod_name,
      JSON_EXTRACT_SCALAR(resource.data.metadata, '$.namespace') AS namespace,
      resource.data.metadata.creationTimestamp AS creation_time,
      JSON_EXTRACT_SCALAR(resource.data.metadata.labels, "$['app.kubernetes.io/name']") AS app_label,
      resource.data.metadata.labels['app.kubernetes.io/version'] AS version
    FROM
      k8s_io_Pod
    WHERE
      JSON_EXTRACT_SCALAR(resource.data.metadata, '$.namespace') = "default"
      AND JSON_EXTRACT_SCALAR(resource.data.metadata.labels, "$['app.kubernetes.io/name']") = "ingress-nginx"
    

### How many BigQuery datasets are in each project
    
    
      SELECT
        ancestor AS project,
        COUNT(*)
      FROM
        bigquery_googleapis_com_Dataset
      CROSS JOIN
        UNNEST (ancestors) AS ancestor
      WHERE
        ancestor LIKE '%project%'
      GROUP BY
        ancestor
      ORDER BY
        2 DESC
    

### How many Compute Engine VM instances are in each region
    
    
    SELECT
      resource.location,
      COUNT(*)
    FROM
      compute_googleapis_com_Instance
    GROUP BY
      resource.location
    

### Name and assetType of all resources in a region
    
    
    SELECT
      name,
      assetType
    FROM
      STANDARD_METADATA
    WHERE
      resource.location LIKE '%asia%'
    

### Publicly available Cloud Storage buckets

Additionally, return their `name`.
    
    
    SELECT
      name
    FROM
      IAM_POLICY
    CROSS JOIN
      UNNEST(iamPolicy.bindings) AS binding
    WHERE
      ('allUsers' IN UNNEST(binding.members)
      OR 'allAuthenticatedUsers' IN UNNEST(binding.members))
      AND assetType = 'storage.googleapis.com/Bucket'
    

### Subnetworks that don't have attached VM instances
    
    
    SELECT
      subnetwork_table.name
    FROM
      compute_googleapis_com_Subnetwork AS subnetwork_table
    LEFT JOIN (
      SELECT
        interface.subnetwork AS subnetwork
      FROM
        compute_googleapis_com_Instance
      CROSS JOIN
        UNNEST(resource.DATA.networkInterfaces) AS interface) AS instance_table
    ON
      SUBSTR(subnetwork_table.name, 25) = SUBSTR(instance_table.subnetwork,38)
    WHERE
      instance_table.subnetwork IS NULL
      AND NOT subnetwork_table.name LIKE '%default%'
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

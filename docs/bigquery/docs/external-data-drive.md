---
url: https://docs.cloud.google.com/bigquery/docs/external-data-drive/
title: Create Google Drive external tables \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:33.067288+00:00
---

# Create Google Drive external tables  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/external-data-drive/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create Google Drive external tables

Google Drive external tables let you query data in Drive files—such as CSV, newline-delimited JSON, Avro, and Google Sheets files— directly from BigQuery without loading the data into BigQuery storage. You can create external tables over both personal and shared Drive files.

This document describes how to create and query Drive external tables.

## Before you begin

Before you create an external table, ensure that you have the required permissions to create the table. For more information on Drive, see [Drive training and help](https://support.google.com/a/users/answer/9282958).

### Retrieve Drive URIs

To create an external table for a Google Drive data source, you must provide the Drive URI. You can retrieve the Drive URI directly from the URL of your Drive data:

**URI format**

  * `https://docs.google.com/spreadsheets/d/FILE_ID`

or

  * `https://drive.google.com/open?id=FILE_ID`




where `FILE_ID` is the alphanumeric ID for your Drive file.

### Authenticate and enable Drive access

Accessing data hosted within Drive requires an additional OAuth scope. To authenticate to BigQuery and enable drive access, do the following:

###  Console 

Follow the web-based authentication steps when you create an external table in the Google Cloud console. When you are prompted, click **Allow** to give BigQuery Client Tools access to Drive.

###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Enter the following command to ensure that you have the latest version of the Google Cloud CLI.
         
         gcloud components update
         

  3. Enter the following command to authenticate with Drive.
         
         gcloud auth login --enable-gdrive-access
         


**Note:** If you use Cloud Shell to access your Drive data, you do not need to update the Google Cloud CLI or authenticate with Drive.

###  API 

Request the appropriate [OAuth scope for Drive](https://developers.google.com/identity/protocols/googlescopes#drive) in addition to the scope for BigQuery:

  1. Sign in by running the [`gcloud auth login --enable-gdrive-access` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login).
  2. Obtain the OAuth access token with the Drive scope that is used for your API by running the [`gcloud auth print-access-token` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token).



###  Python 

  1. [Create an OAuth Client ID](https://support.google.com/cloud/answer/6158849).

  2. Set up [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) in your local environment with the required scopes by doing the following:

     1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI, then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) it by running the following command:
            
            gcloud init

     2. Create local authentication credentials for your Google Account:
            
            gcloud auth application-default login \
                --client-id-file=CLIENT_ID_FILE \
                --scopes=https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/cloud-platform

Replace `CLIENT_ID_FILE` with the file containing your OAuth Client ID.

For more information, see [User credentials provided by using the gcloud CLI](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal).




###  Java 

  1. [Create an OAuth Client ID](https://support.google.com/cloud/answer/6158849).

  2. Set up [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) in your local environment with the required scopes by doing the following:

     1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI, then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) it by running the following command:
            
            gcloud init

     2. Create local authentication credentials for your Google Account:
            
            gcloud auth application-default login \
                --client-id-file=CLIENT_ID_FILE \
                --scopes=https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/cloud-platform

Replace `CLIENT_ID_FILE` with the file containing your OAuth Client ID.

For more information, see [User credentials provided by using the gcloud CLI](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal).




### Required roles

To create an external table, you need the `bigquery.tables.create` BigQuery Identity and Access Management (IAM) permission.

Each of the following predefined Identity and Access Management roles includes this permission:

  * BigQuery Data Editor (`roles/bigquery.dataEditor`)
  * BigQuery Data Owner (`roles/bigquery.dataOwner`)
  * BigQuery Admin (`roles/bigquery.admin`)



If you are not a principal in any of these roles, ask your administrator to grant you access or to create the external table for you.

For more information on Identity and Access Management roles and permissions in BigQuery, see [Predefined roles and permissions](https://docs.cloud.google.com/bigquery/docs/access-control).

## Create external tables

You can create a permanent table linked to your external data source by:

  * Using the Google Cloud console
  * Using the bq command-line tool's `mk` command
  * Creating an [`ExternalDataConfiguration`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#externaldataconfiguration) when you use the [`tables.insert`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables/insert) API method
  * Using the client libraries



To create an external table:

###  Console 

  1. In the Google Cloud console, open the BigQuery page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

If you don't see the left pane, click last_page **Expand left pane** to open the pane.

  3. In the **Explorer** pane, expand your project, click **Datasets** , and then select a dataset.

  4. In the details pane, click **Create table** add_box.

  5. On the **Create table** page, in the **Source** section:

     * For **Create table from** , select **Drive**.

     * In the **Select Drive URI** field, enter the Drive URI. Note that wildcards are not supported for Drive URIs.

     * For **File format** , select the format of your data. Valid formats for Drive data include:

       * Comma-separated values (CSV)
       * Newline delimited JSON
       * Avro
       * Sheets
**Note:** In the Google Cloud console, choosing Avro or Datastore backup hides the **Automatically detect** option because these file types are self-describing.
  6. (Optional) If you choose Sheets, in the **Sheet range (Optional)** box, specify the sheet and cell range to query. You can specify a sheet name, or you can specify `sheet_name!top_left_cell_id:bottom_right_cell_id` for a cell range; for example, "Sheet1!A1:B20". If **Sheet range** is not specified, the first sheet in the file is used.

  7. On the **Create table** page, in the **Destination** section:

     * For **Dataset name** , choose the appropriate dataset, and in the **Table name** field, enter the name of the table you're creating in BigQuery.

![Select dataset](https://docs.cloud.google.com/static/bigquery/images/create-table-select-dataset.png)

     * Verify that **Table type** is set to **External table**.

  8. In the **Schema** section, enter the [schema](https://docs.cloud.google.com/bigquery/docs/schemas) definition.

     * For JSON or CSV files, you can check the **Auto-detect** option to enable schema [auto-detect](https://docs.cloud.google.com/bigquery/docs/schema-detect). **Auto-detect** is not available for Datastore exports, Firestore exports, and Avro files. Schema information for these file types is automatically retrieved from the self-describing source data.
     * Enter schema information manually by: 
       * Enabling **Edit as text** and entering the table schema as a JSON array. Note: You can view the schema of an existing table in JSON format by entering the following command in the bq command-line tool: `bq show --format=prettyjson DATASET.TABLE`.
       * Using **Add field** to manually input the schema.
  9. Click **Create table**.

  10. If necessary, select your account and then click **Allow** to give the BigQuery client tools access to Drive.




You can then run a query against the table as if it were a standard BigQuery table, subject to the [limitations](https://docs.cloud.google.com/bigquery/external-data-sources#external_data_source_limitations) on external data sources.

After your query completes, you can download the results as CSV or JSON, save the results as a table, or save the results to Sheets. See [Download, save, and export data](https://docs.cloud.google.com/bigquery/bigquery-web-ui#exportdata) for more information.

###  bq 

You create a table in the bq command-line tool using the `bq mk` command. When you use the bq command-line tool to create a table linked to an external data source, you can identify the table's schema using:

  * A [table definition file](https://docs.cloud.google.com/bigquery/external-table-definition) (stored on your local machine)
  * An inline schema definition
  * A JSON schema file (stored on your local machine)



To create a permanent table linked to your Drive data source using a table definition file, enter the following command.
    
    
    bq mk \
    --external_table_definition=DEFINITION_FILE \
    DATASET.TABLE

Where:

  * `DEFINITION_FILE` is the path to the [table definition file](https://docs.cloud.google.com/bigquery/external-table-definition) on your local machine.
  * `DATASET` is the name of the dataset that contains the table.
  * `TABLE` is the name of the table you're creating.



For example, the following command creates a permanent table named `mytable` using a table definition file named `mytable_def`.
    
    
    bq mk --external_table_definition=/tmp/mytable_def mydataset.mytable
    

To create a permanent table linked to your external data source using an inline schema definition, enter the following command.
    
    
    bq mk \
    --external_table_definition=SCHEMA@SOURCE_FORMAT=DRIVE_URI \
    DATASET.TABLE

Where:

  * `SCHEMA` is the schema definition in the format `FIELD:DATA_TYPE,FIELD:DATA_TYPE`.
  * `SOURCE_FORMAT` is `CSV`, `NEWLINE_DELIMITED_JSON`, `AVRO`, or `GOOGLE_SHEETS`.
  * `DRIVE_URI` is your Drive URI.
  * `DATASET` is the name of the dataset that contains the table.
  * `TABLE` is the name of the table you're creating.



For example, the following command creates a permanent table named `sales` linked to a Sheets file stored in Drive with the following schema definition: `Region:STRING,Quarter:STRING,Total_sales:INTEGER`.
    
    
    bq mk \
    --external_table_definition=Region:STRING,Quarter:STRING,Total_sales:INTEGER@GOOGLE_SHEETS=https://drive.google.com/open?id=1234_AbCD12abCd \
    mydataset.sales
    

To create a permanent table linked to your external data source using a JSON schema file, enter the following command.
    
    
    bq mk \
    --external_table_definition=SCHEMA_FILE@SOURCE_FORMAT=DRIVE_URI \
    DATASET.TABLE

Where:

  * `SCHEMA_FILE` is the path to the JSON schema file on your local machine.
  * `SOURCE_FORMAT` is `CSV`, `NEWLINE_DELIMITED_JSON`, `AVRO`, or `GOOGLE_SHEETS`.
  * `DRIVE_URI` is your Drive URI.
  * `DATASET` is the name of the dataset that contains the table.
  * `TABLE` is the name of the table you're creating.



If your [table definition file](https://docs.cloud.google.com/bigquery/external-table-definition) contains [Sheets-specific configuration](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#GoogleSheetsOptions), then you can skip leading rows and specify a defined sheet range.

The following example creates a table named `sales` linked to a CSV file stored in Drive using the `/tmp/sales_schema.json` schema file.
    
    
    bq mk \
    --external_table_definition=/tmp/sales_schema.json@CSV=https://drive.google.com/open?id=1234_AbCD12abCd \
    mydataset.sales
    

After the permanent table is created, you can then run a query against the table as if it were a standard BigQuery table, subject to the [limitations](https://docs.cloud.google.com/bigquery/external-data-sources#external_data_source_limitations) on external data sources.

After your query completes, you can download the results as CSV or JSON, save the results as a table, or save the results to Sheets. See [Download, save, and export data](https://docs.cloud.google.com/bigquery/bigquery-web-ui#exportdata) for more information.

###  API 

Create an [`ExternalDataConfiguration`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#externaldataconfiguration) when you use the [`tables.insert`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables/insert) API method. Specify the `schema` property or set the `autodetect` property to `true` to enable schema auto detection for supported data sources. 

###  Python 
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    import google.auth
    
    credentials, project = google.auth.default()
    
    # Construct a BigQuery client object.
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)(credentials=credentials, project=project)
    
    # TODO(developer): Set dataset_id to the ID of the dataset to fetch.
    # dataset_id = "your-project.your_dataset"
    
    # Configure the external data source.
    dataset = client.[get_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_dataset)(dataset_id)
    table_id = "us_states"
    schema = [
        [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SchemaField](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.schema.SchemaField.html)("name", "STRING"),
        [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SchemaField](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.schema.SchemaField.html)("post_abbr", "STRING"),
    ]
    table = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.Table.html)(dataset.table(table_id), schema=schema)
    external_config = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[ExternalConfig](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.ExternalConfig.html)("GOOGLE_SHEETS")
    # Use a shareable link or grant viewing access to the email address you
    # used to authenticate with BigQuery (this example Sheet is public).
    sheet_url = (
        "https://docs.google.com/spreadsheets"
        "/d/1i_QCL-7HcSyUZmIbP9E6lO_T5u3HnpLe7dnpHaijg_E/edit?usp=sharing"
    )
    [external_config](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.html).source_uris = [sheet_url]
    options = [external_config](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.html).[google_sheets_options](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.ExternalConfig.html#google_cloud_bigquery_external_config_ExternalConfig_google_sheets_options)
    assert options is not None
    [options](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.ExternalConfig.html#google_cloud_bigquery_external_config_ExternalConfig_options).skip_leading_rows = 1  # Optionally skip header row.
    [options](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.ExternalConfig.html#google_cloud_bigquery_external_config_ExternalConfig_options).[range](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.GoogleSheetsOptions.html#google_cloud_bigquery_external_config_GoogleSheetsOptions_range) = (
        "us-states!A20:B49"  # Optionally set range of the sheet to query from.
    )
    table.[external_data_configuration](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.Table.html#google_cloud_bigquery_table_Table_external_data_configuration) = external_config
    
    # Create a permanent table linked to the Sheets file.
    table = client.[create_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_create_table)(table)  # Make an API request.
    
    # Example query to find states starting with "W".
    sql = 'SELECT * FROM `{}.{}` WHERE name LIKE "W%"'.format(dataset_id, table_id)
    
    results = client.[query_and_wait](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_query_and_wait)(sql)  # Make an API request.
    
    # Wait for the query to complete.
    w_states = list(results)
    print(
        "There are {} states with names starting with W in the selected range.".format(
            len(w_states)
        )
    )

###  Java 
    
    
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import com.google.auth.oauth2.[ServiceAccountCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ServiceAccountCredentials.html);
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[ExternalTableDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExternalTableDefinition.html);
    import com.google.cloud.bigquery.[Field](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Field.html);
    import com.google.cloud.bigquery.[GoogleSheetsOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.GoogleSheetsOptions.html);
    import com.google.cloud.bigquery.[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html);
    import com.google.cloud.bigquery.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Schema.html);
    import com.google.cloud.bigquery.[StandardSQLTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardSQLTypeName.html);
    import com.google.cloud.bigquery.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html);
    import com.google.cloud.bigquery.[TableInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableInfo.html);
    import com.google.cloud.bigquery.[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html);
    import com.google.common.collect.ImmutableSet;
    import java.io.IOException;
    
    // Sample to queries an external data source using a permanent table
    public class QueryExternalSheetsPerm {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String datasetName = "MY_DATASET_NAME";
        String tableName = "MY_TABLE_NAME";
        String sourceUri =
            "https://docs.google.com/spreadsheets/d/1i_QCL-7HcSyUZmIbP9E6lO_T5u3HnpLe7dnpHaijg_E/edit?usp=sharing";
        [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Schema.html) schema =
            [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Schema.html).of(
                [Field](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Field.html).of("name", [StandardSQLTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardSQLTypeName.html).STRING),
                [Field](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Field.html).of("post_abbr", [StandardSQLTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardSQLTypeName.html).STRING));
        String query =
            String.format("SELECT * FROM %s.%s WHERE name LIKE 'W%%'", datasetName, tableName);
        queryExternalSheetsPerm(datasetName, tableName, sourceUri, schema, query);
      }
    
      public static void queryExternalSheetsPerm(
          String datasetName, String tableName, String sourceUri, [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Schema.html) schema, String query) {
        try {
    
          [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) credentials =
              [ServiceAccountCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ServiceAccountCredentials.html).[getApplicationDefault](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)();
    
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery =
              [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).newBuilder().setCredentials(credentials).build().getService();
    
          // Skip header row in the file.
          [GoogleSheetsOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.GoogleSheetsOptions.html) sheetsOptions =
              [GoogleSheetsOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.GoogleSheetsOptions.html).newBuilder()
                  .setSkipLeadingRows(1) // Optionally skip header row.
                  .setRange("us-states!A20:B49") // Optionally set range of the sheet to query from.
                  .build();
    
          [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) tableId = [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html).of(datasetName, tableName);
          // Create a permanent table linked to the Sheets file.
          [ExternalTableDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExternalTableDefinition.html) externalTable =
              [ExternalTableDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExternalTableDefinition.html).newBuilder(sourceUri, sheetsOptions).setSchema(schema).build();
          bigquery.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_create_com_google_cloud_bigquery_DatasetInfo_com_google_cloud_bigquery_BigQuery_DatasetOption____)(TableInfo.of(tableId, externalTable));
    
          // Example query to find states starting with 'W'
          [TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html) results = bigquery.[query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_query_com_google_cloud_bigquery_QueryJobConfiguration_com_google_cloud_bigquery_BigQuery_JobOption____)([QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html).of(query));
    
          results
              .[iterateAll](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html#com_google_cloud_bigquery_TableResult_iterateAll__)()
              .forEach(row -> row.forEach(val -> System.out.printf("%s,", val.toString())));
    
          System.out.println("Query on external permanent table performed successfully.");
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) | InterruptedException | IOException e) {
          System.out.println("Query not performed \n" + e.toString());
        }
      }
    }

## Query external tables

For more information, see [Query Drive data](https://docs.cloud.google.com/bigquery/docs/query-drive-data).

## The `_FILE_NAME` pseudocolumn

Tables based on external data sources provide a pseudo column named `_FILE_NAME`. This column contains the fully qualified path to the file to which the row belongs. This column is available only for tables that reference external data stored in **Cloud Storage** and **Google Drive**.

The `_FILE_NAME` column name is reserved, which means that you cannot create a column by that name in any of your tables.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

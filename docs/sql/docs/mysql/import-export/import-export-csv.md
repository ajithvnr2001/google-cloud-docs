---
url: https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-csv/
title: Export and import using CSV files \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:59.185413+00:00
---

# Export and import using CSV files  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-csv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Export and import using CSV files Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-csv "View this page for the PostgreSQL database engine") | SQL Server

This page describes exporting and importing data into Cloud SQL instances using CSV files.

**Note:** If you're migrating an entire database from a supported database server (on-premises, in AWS, or Cloud SQL) to a new Cloud SQL instance, you can use the [Database Migration Service](https://docs.cloud.google.com/database-migration/docs) instead of exporting and then importing files. If you're exporting because you want to create a new instance from the exported file, consider [ restoring from a backup to a different instance](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restoring#restorebackups-another-instance) or [cloning the instance](https://docs.cloud.google.com/sql/docs/mysql/clone-instance).

You can cancel the import of data into Cloud SQL instances and the export of data from the instances. This data is contained in CSV files. For more information about cancelling an import or export operation, see [Cancel the import and export of data](https://docs.cloud.google.com/sql/docs/mysql/import-export/cancel-import-export).

## Before you begin

Before you begin an export or import operation:

  * Ensure that your database has adequate free space. 

Export and import operations use database resources, but they do not interfere with normal database operations unless the instance is under-provisioned.

**Important** : Before starting a large operation, ensure that at least 25 percent of the disk is free on the instance. Doing so helps prevent issues with aggressive autogrowth, which can adversely affect the availability of the instance.
  * [Verify](https://docs.cloud.google.com/sql/docs/mysql/import-export#verify) that the CSV file has the expected data and that it's in the correct format. CSV files must have one line for each row of data fields.
  * Follow the [best practices for exporting and importing data.](https://docs.cloud.google.com/sql/docs/mysql/import-export)



## Export data from Cloud SQL for MySQL

### Required roles and permissions for exporting from Cloud SQL for MySQL

To export data from Cloud SQL into Cloud Storage, the user initiating the export must have one of the following roles:

  * The [Cloud SQL Editor](https://docs.cloud.google.com/sql/docs/mysql/iam-roles) role 
  * A [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), including the following permissions: 
    * `cloudsql.instances.get`
    * `cloudsql.instances.export`



Additionally, the service account for the Cloud SQL instance must have one of the following roles:

  * The `storage.objectAdmin` Identity and Access Management (IAM) role
  * A custom role, including the following permissions: 
    * `storage.objects.create`
    * `storage.objects.list` (for exporting files in parallel only)
    * `storage.objects.delete` (for exporting files in parallel only)



For help with IAM roles, see [Identity and Access Management](https://docs.cloud.google.com/storage/docs/access-control/iam).

**Note** : The changes that you make to the IAM permissions and roles might take a few minutes to take effect. For more information, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

### Export data to a CSV file from Cloud SQL for MySQL

You can export your data in CSV format, which is usable by other tools and environments. Exports happen at the database level. During a CSV export, you can specify the schemas to export. All schemas at the database level are eligible for export.

**Note:** Cloud SQL uses double quotes (hex value "22") as the default escape character. This can be a problem for databases where values for `NULL` are entered as string literals. When importing a file that was exported using the default escape character, the file doesn't treat the value as `NULL` but as `"NULL"`. We recommend that you use `--escape="5C"` to override the default when you export the file. 

To export data from a database on a Cloud SQL instance to a CSV file in a Cloud Storage bucket:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Export**.
  4. In the **File format** section, click **CSV**.
  5. For **SQL query** , enter a SQL query to specify the table to export data from. 

For example, to export the entire contents of the `entries` table in the `guestbook` database, you enter 
         
         SELECT * FROM guestbook.entries;

Your query must specify a table in the specified database. You can't export an entire database in CSV format. 

**Note:** While in-transit, the query might be processed in intermediate locations other than the location of the target instance

  6. Optional: Select **Offload export to a temporary instance** to allow other operations to occur while the export is ongoing.
  7. Optional: Click **Show database options** , and then select the name of the database from the **Database** drop-down menu.
  8. In the **Destination** section, add the name of the bucket, folder, and file that you want to export to, or click **Browse** to find or create a bucket, folder, or file. 

If you click **Browse** :

     1. In the **Location** section, select a Cloud Storage bucket or folder for your export. **Note:** If you need to create a new storage bucket, click the bucket with the **+** sign in the **Location** section. This opens **Create a bucket** , where you can add a name and other configurations for the bucket. Select a **standard** storage class for your bucket.
     2. In the **Name** box, add a name for the `CSV` file, or select an existing file from the list in the **Location** section.

You can use a file extension of `.gz` (the complete extension would be `.csv.gz`) to compress your export file.

     3. Click **Select**.
  9. Click **Export** to start the export.



### gcloud

  1. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  2. Upload the file to your bucket.

For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Find the service account for the Cloud SQL instance you're exporting from. You can do this running the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command. Look for the `serviceAccountEmailAddress` field in the output. 
         
         gcloud sql instances describe INSTANCE_NAME

  4. Use `[ gcloud storage buckets add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)` to grant the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the Cloud SQL instance service account. For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  5. Export the database: **Note:** Use the `--offload` flag if you want to use serverless export. Otherwise, remove it from the following command.
         
         gcloud sql export csv INSTANCE_NAME gs://BUCKET_NAME/FILE_NAME \
         --database=DATABASE_NAME \
         --offload \
         --query=SELECT_QUERY
         

For information about using the `export csv` command, see the [`sql export csv`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/csv) command reference page.

**Note:** While in-transit, the SELECT_QUERY might be processed in intermediate locations other than the location of the target instance.

  6. If you do not need to retain the IAM role you set previously, [revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) it now.



### REST v1

  1. Create a bucket for the export: 
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION_NAME --project=PROJECT_NAME
         

This step is not required, but strongly recommended, so you do not open up access to any other data.

  2. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  3. Export your database: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * bucket_name: The Cloud Storage bucket name
     * path_to_csv_file: The path to the CSV file
     * database_name: The name of a database inside the Cloud SQL instance
     * offload: Enables serverless export. Set to `true` to use serverless export. **Note:** Serverless export costs extra. See the [pricing page](https://docs.cloud.google.com/sql/pricing#storage-networking-prices).
     * select_query: SQL query for export (optional) **Note:** While in-transit, the query might be processed in intermediate locations other than the location of the target instance.
     * escape_character: The character that should appear before a data character that needs to be escaped. The value of this argument has to be a character in Hex ASCII Code. For example, "22" represents double quotes. (optional)
     * quote_character:The character that encloses values from columns that have a string data type. The value of this argument has to be a character in Hex ASCII Code. For example, "22" represents double quotes. (optional)
     * fields_terminated_by: The character that split column values. The value of this argument has to be a character in Hex ASCII Code. For example, "2C" represents a comma. (optional)
     * lines_terminated_by: The character that split line records. The value of this argument has to be a character in Hex ASCII Code. For example, "0A" represents a new line. (optional)

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/export

Request JSON body: 
    
    {
     "exportContext":
       {
          "fileType": "CSV",
          "uri": "gs://bucket_name/path_to_csv_file",
          "databases": "database_name",
          "offload": true | false
          "csvExportOptions":
           {
               "selectQuery":"select_query",
               "escapeCharacter":"escape_character",
               "quoteCharacter":"quote_character",
               "fieldsTerminatedBy":"fields_terminated_by",
               "linesTerminatedBy":"lines_terminated_by"
           }
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
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/export"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

If your select query specifies a database, it overrides the `databases` property. 

  4. If you do not need to retain the IAM permissions you set previously, remove them now. 

For the complete list of parameters for the request, see the [instances:export](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/export) page. 

### REST v1beta4

  1. Create a bucket for the export: 
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION_NAME --project=PROJECT_NAME

This step is not required, but strongly recommended, so you do not open up access to any other data.

  2. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  3. Export your database: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * bucket_name: The Cloud Storage bucket name
     * path_to_csv_file: The path to the CSV file
     * database_name: The name of a database inside the Cloud SQL instance
     * offload: Enables serverless export. Set to `true` to use serverless export. **Note:** Serverless export costs extra. See the [pricing page](https://docs.cloud.google.com/sql/pricing#storage-networking-prices).
     * select_query: SQL query for export (optional) **Note:** While in-transit, the query might be processed in intermediate locations other than the location of the target instance.
     * escape_character: The character that should appear before a data character that needs to be escaped. The value of this argument must be in [ASCII hex format](https://ascii.cl/). For example, "22" represents double quotes. (optional)
     * quote_character: The character that encloses values from columns that have a string data type. The value of this argument must be in [ASCII hex format](https://ascii.cl/). For example, "22" represents double quotes. (optional)
     * fields_terminated_by: The character that splits column values. The value of this argument must be in [ASCII hex format](https://ascii.cl/). For example, "2C" represents a comma. (optional) 
     * lines_terminated_by: The character that split line records. The value of this argument must be in [ASCII hex format](https://ascii.cl/). For example, "0A" represents a new line. (optional) 

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/export

Request JSON body: 
    
    {
     "exportContext":
       {
          "fileType": "CSV",
          "uri": "gs://bucket_name/path_to_csv_file",
          "databases": "database_name",
          "offload": true | false
          "csvExportOptions":
           {
               "selectQuery": "select_query",
               "escapeCharacter":  "escape_character",
               "quoteCharacter": "quote_character",
               "fieldsTerminatedBy": "fields_terminated_by",
               "linesTerminatedBy": "lines_terminated_by"
           }
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/export"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

If your select query specifies a database, it overrides the `databases` property. 

  4. If you do not need to retain the IAM role you set previously, [revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) it now.

For the complete list of parameters for the request, see the [instances:export](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/export) page. 

### Customize the format of a CSV export file

You can use `gcloud` or the REST API to customize your CSV file format. When you perform an export, you can specify the following formatting options:

CSV option | Default value | gcloud flag | REST API property | Description  
---|---|---|---|---  
Escape |  `"5C"` ASCII hex code for file separator.  | `--escape` | `escapeCharacter` |  Character that appears before a data character that needs to be escaped.  Available only for MySQL and PostgreSQL.   
Quote |  `"22"` ASCII hex code for double quotes.  | `--quote` | `quoteCharacter` |  Character that encloses values from columns that have a string data type.  Available only for MySQL and PostgreSQL.   
Field delimiter |  `"2C"` ASCII hex code for comma.  | `--fields-terminated-by` | `fieldsTerminatedBy` |  Character that splits column values.  Available only for MySQL and PostgreSQL.   
Newline character |  `"0A"` ASCII hex code for newline.  | `--lines-terminated-by` | `linesTerminatedBy` |  Character that splits line records.  Available only for MySQL.   
  
For example, a `gcloud` command using all of these arguments could be like the following:
    
    
    gcloud sql export csv INSTANCE_NAME gs://BUCKET_NAME/FILE_NAME \
    --database=DATABASE_NAME \
    --offload \
    --query=SELECT_QUERY \
    --quote="22" \
    --escape="5C" \
    --fields-terminated-by="2C" \
    --lines-terminated-by="0A"

The equivalent REST API request body would look like this:
    
    
    {
     "exportContext":
       {
          "fileType": "CSV",
          "uri": "gs://bucket_name/path_to_csv_file",
          "databases": ["DATABASE_NAME"],
          "offload": true,
          "csvExportOptions":
           {
               "selectQuery": "SELECT_QUERY",
               "escapeCharacter":  "5C",
               "quoteCharacter": "22",
               "fieldsTerminatedBy": "2C",
               "linesTerminatedBy": "0A"
           }
       }
    }

The preceding `gcloud` and API examples are equivalent to running the following SQL statement:
    
    
    SELECT [QUERY] INTO OUTFILE ... CHARACTER SET 'utf8mb4'
                FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"'
                ESCAPED BY '\\' LINES TERMINATED BY '\n'

## Import data to Cloud SQL for MySQL

### Required roles and permissions for importing to Cloud SQL for MySQL

To import data from Cloud Storage into Cloud SQL, the user initiating the import must have one of the following roles: 

  * The [Cloud SQL Admin](https://docs.cloud.google.com/sql/docs/mysql/iam-roles) role 
  * A [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), including the following permissions: 
    * `cloudsql.instances.get`
    * `cloudsql.instances.import`



Additionally, the service account for the Cloud SQL instance must have one of the following roles:

  * The `storage.objectAdmin` IAM role
  * A custom role, including the following permissions: 
    * `storage.objects.get`
    * `storage.objects.list` (for importing files in parallel only)



For help with IAM roles, see [Identity and Access Management](https://docs.cloud.google.com/storage/docs/access-control/iam).

**Note** : The changes that you make to the IAM permissions and roles might take a few minutes to take effect. For more information, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

### Export data from your local MySQL server to a CSV file

To export a MySQL table for import into Cloud SQL, we recommend that you format the file using the following command:
    
    
    mysql --host=INSTANCE_IP --user=USER_NAME --password DATABASE \
    -e " SELECT * FROM TABLE INTO OUTFILE 'FILE_NAME' CHARACTER SET 'utf8mb4'
         FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' ESCAPED BY '\"' "

You can customize the format of your CSV export file.

### Import data from a CSV file to Cloud SQL for MySQL

  * The database and table you are importing into must exist on your Cloud SQL instance. For help with creating a database, see [Creating a database](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases#create). 

To create a table, use the [ `CREATE TABLE`](https://dev.mysql.com/doc/refman/8.4/en/creating-tables.html) SQL statement in the `mysql` client.

  * Your CSV file must conform to the CSV file format requirements. 
  * If you are importing data that you exported from an on-premises MySQL server: 
    1. [Create a bucket in Cloud Storage](https://docs.cloud.google.com/storage/docs/creating-buckets).
    2. [Upload the SQL dump file](https://docs.cloud.google.com/storage/docs/uploading-objects) to the Cloud Storage bucket.

**Note:** The default behavior for Cloud SQL is to import columns in your CSV file in the same order as the table schema. If the order is different in your CSV file or if some columns are skipped, use [ importContext.csvImportOptions.columns[]](https://cloud.google.com/sdk/gcloud/reference/sql/import/csv#--columns) to import data from the CSV file. **Note:** You cannot import a CSV file that was created using one database engine into an instance created using another database engine.

### CSV file format requirements 

CSV files must have one line for each row of data and use comma-separated fields.

To import data to a Cloud SQL instance using a CSV file:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Import**.
  4. In the **File format** section, select **CSV**.
  5. In the **Select source file** section, enter the path to the bucket and CSV file or upload a local CSV file to use for the import. To browse to the file: 
     1. Click **Browse**.
     2. In the **Location** section, double-click the name of the bucket in the list.
     3. Select the file in the list.
     4. Click **Select**.

You can import a compressed (`.gz`) or an uncompressed (`.csv`) file.

  6. In the **Destination** section, specify the **Database** and **Table** in your Cloud SQL instance where you want to import the CSV file.
  7. Click **Import** to start the import.



### gcloud

  1. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  2. Upload the file to your bucket.

For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Upload data from the CSV file to the bucket.
  4. Identify the service account for the Cloud SQL instance you're exporting from. You can do this running the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command with the instance name. Look for the `serviceAccountEmailAddress` field in the output. 
         
         gcloud sql instances describe INSTANCE_NAME

  5. Copy the serviceAccountEmailAddress field.
  6. Use `[ gcloud storage buckets add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)` to grant the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the Cloud SQL instance service account for the bucket. For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  7. Import the file: 
         
         gcloud sql import csv INSTANCE_NAME gs://BUCKET_NAME/FILE_NAME \
         --database=DATABASE_NAME \
         --table=TABLE_NAME

For information about using the `import csv` command, see the [`sql import csv`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/import/csv) command reference page.

  8. If you do not need to retain the IAM permissions you set previously, remove them using [ `gcloud storage buckets remove-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/remove-iam-policy-binding). 



### REST v1

  1. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  2. Upload the file to your bucket.

For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Provide your instance with the `storage.objectAdmin` and `objectViewer` [IAM roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  4. Import the file: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * bucket_name: The Cloud Storage bucket name
     * path_to_csv_file: The path to the CSV file
     * database_name: The name of a database inside the Cloud SQL instance
     * table_name: The name of the database table
     * escape_character: The character that should appear before a data character that needs to be escaped. The value of this argument has to be a character in Hex ASCII Code. For example, "22" represents double quotes. (optional)
     * quote_character: The character that encloses values from columns that have a string data type. The value of this argument has to be a character in Hex ASCII Code. For example, "22" represents double quotes. (optional)
     * fields_terminated_by: The character that split column values. The value of this argument has to be a character in Hex ASCII Code. For example, "2C" represents a comma. (optional) 
     * lines_terminated_by: The character that split line records. The value of this argument has to be a character in Hex ASCII Code. For example, "0A" represents a new line. (optional) 

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "CSV",
          "uri": "gs://bucket_name/path_to_csv_file",
          "database": "database_name",
          "csvImportOptions":
           {
             "table": "table_name",
             "escapeCharacter": "escape_character",
             "quoteCharacter": "quote_character",
             "fieldsTerminatedBy": "fields_terminated_by",
             "linesTerminatedBy": "lines_terminated_by"
           }
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
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/import"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

For the complete list of parameters for the request, see the [instances:import](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/import) page. 
  5. If you do not need to retain the IAM permissions you set previously, remove the permissions. 



### REST v1beta4

  1. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  2. Upload the file to your bucket.

For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  4. Import the file: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * bucket_name: The Cloud Storage bucket name
     * path_to_csv_file: The path to the CSV file
     * database_name: The name of a database inside the Cloud SQL instance
     * table_name: The name of the database table
     * escape_character: The character that should appear before a data character that needs to be escaped. The value of this argument must be in [ASCII hex format](https://ascii.cl/). For example,"22" represents double quotes. (optional)
     * quote_character: The character that encloses values from columns that have a string data type. The value of this argument must be in [ASCII hex format](https://ascii.cl/). For example, "22" represents double quotes. (optional)
     * fields_terminated_by: The character that split column values. The value of this argument must be in [ASCII hex format](https://ascii.cl/). For example, "2C" represents a comma. (optional) 
     * lines_terminated_by: The character that split line records. The value of this argument must be in [ASCII hex format](https://ascii.cl/). For example, "0A" represents a new line. (optional) 

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "CSV",
          "uri": "gs://bucket_name/path_to_csv_file",
          "database": "database_name",
          "csvImportOptions":
           {
             "table": "table_name",
             "escapeCharacter": "escape_character",
             "quoteCharacter": "quote_character",
             "fieldsTerminatedBy": "fields_terminated_by",
             "linesTerminatedBy": "lines_terminated_by"
           }
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/import"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

For the complete list of parameters for the request, see the [instances:import](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/import) page. 
  5. If you do not need to retain the IAM permissions you set previously, remove the permissions. 



### Customize the format of a CSV file for Cloud SQL for MySQL

You can use `gcloud` or the REST API to customize your CSV file format.

A sample `gcloud` command follows:
    
    
    gcloud sql import csv INSTANCE_NAME gs://BUCKET_NAME/FILE_NAME \
    --database=DATABASE_NAME \
    --table=TABLE_NAME \
    --quote="22" \
    --escape="5C" \
    --fields-terminated-by="2C" \
    --lines-terminated-by="0A"

The equivalent REST API request body would look like this:
    
    
    {
     "importContext":
       {
          "fileType": "CSV",
          "uri": "gs://bucket_name/path_to_csv_file",
          "database": ["DATABASE_NAME"],
          "csvImportOptions":
           {
               "table": "TABLE_NAME",
               "escapeCharacter":  "5C",
               "quoteCharacter": "22",
               "fieldsTerminatedBy": "2C",
               "linesTerminatedBy": "0A"
           }
       }
    }

The preceding `gcloud` and API examples are equivalent to running the following SQL statement:
    
    
    LOAD DATA LOCAL INFILE ... CHARACTER SET 'utf8mb4'
    FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' ESCAPED BY '\\'.
    

**Note:** If you use custom format options in your import commands, make sure the exported file was created with the same options.

If you get an error such as `ERROR_RDBMS`, ensure the table exists. If the table exists, confirm that you have the correct permissions on the bucket. For help configuring access control in Cloud Storage, see [ Create and Manage Access Control Lists](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists). 

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/import) is constructed for this task, see the [APIs Explorer on the instances:import page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/import). 

## What's next

  * Learn how to [check the status of import and export operations](https://docs.cloud.google.com/sql/docs/mysql/import-export/checking-status-import-export).
  * Learn more about [best practices for importing and exporting data](https://docs.cloud.google.com/sql/docs/mysql/import-export).
  * [Known issues for imports and exports](https://docs.cloud.google.com/sql/docs/mysql/known-issues#import-export).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

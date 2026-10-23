---
url: https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality/
title: Use auto data quality \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:14.290160+00:00
---

# Use auto data quality  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Use auto data quality Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use Knowledge Catalog (formerly Dataplex Universal Catalog) data quality scans to measure, monitor, and manage the quality of your data. Data quality scans help you automate the process of validating your data for completeness, validity, and consistency.

With data quality scans, you can define rules to check for missing values, ensure values match a regular expression or belong to a set, verify uniqueness, or use custom SQL for more complex validations such as anomaly detection. This document explains how to create and manage data quality scans.

Learn more about [data quality scans](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview). Learn more about [reusing data quality rules](https://docs.cloud.google.com/knowledge-catalog/docs/reuse-data-quality-rules) across multiple scans.

**Note:** The steps in this document show how to manage data quality scans across your project. You can also create and manage data quality scans when working with a specific table.

## Before you begin

  1. Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

  2. Optional: To generate recommendations for data quality rules based on the results of a data profile scan, [create and run the data profile scan](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-profiling).



### Required roles and permissions

This section describes the IAM roles and permissions needed to use Knowledge Catalog data quality scans.

### User roles and permissions

To get the permissions that you need to run and manage data quality scans, ask your administrator to grant you the following IAM roles: 

  * Run a data quality scan on a BigQuery table: 
    * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) on the project to run scan jobs
    * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on the BigQuery table to be scanned
  * Publish data quality scan results to Knowledge Catalog: 
    * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) on the scanned table
    * [Dataplex Catalog Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`) on the `@bigquery` entry group in the same location as the table
  * Perform specific tasks on `DataScan` resources: 
    * [Dataplex DataScan Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`) on the project for full access
    * [Dataplex DataScan Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanCreator) (`roles/dataplex.dataScanCreator`) on the project to create scans
    * [Dataplex DataScan Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`) on the project for write access
    * [Dataplex DataScan Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanViewer) (`roles/dataplex.dataScanViewer`) on the project to read scan metadata
    * [Dataplex DataScan DataViewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanDataViewer) (`roles/dataplex.dataScanDataViewer`) on the project to read scan data including rules and results



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to run and manage data quality scans. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to run and manage data quality scans:

  * Run a data quality scan on a BigQuery table: 
    * `bigquery.jobs.create` on the project to run scan jobs
    * `bigquery.tables.get` on the BigQuery table to be scanned
    * `bigquery.tables.getData` on the BigQuery table to be scanned
  * Publish data quality scan results to Knowledge Catalog: 
    * `bigquery.tables.update` on the scanned table
    * `dataplex.entryGroups.useDataQualityScorecardAspect` on the `@bigquery` entry group in the same location as the table
  * Create a `DataScan`: `dataplex.datascans.create` on the project 
  * Delete a `DataScan`: `dataplex.datascans.delete` on the project 
  * View `DataScan` metadata: `dataplex.datascans.get` on the project 
  * View `DataScan` details including rules and results: `dataplex.datascans.getData` on the project 
  * List `DataScan`s: `dataplex.datascans.list` on the project 
  * Run a `DataScan`: `dataplex.datascans.run` on the project 
  * Update a `DataScan`: `dataplex.datascans.update` on the project 
  * Get or set IAM policy on a `DataScan`: 
    * `dataplex.datascans.getIamPolicy` on the project
    * `dataplex.datascans.setIamPolicy` on the project



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you need to access columns protected by BigQuery column-level access policies, then you also need permissions for those columns.

**Note:** Knowledge Catalog doesn't create a BigQuery job in your project for data quality scans. However, you need the `bigquery.jobs.create` permission to create a `DryRun` job to check for permissions for the table.

### Knowledge Catalog service account roles and permissions

**Note:** If you are scanning CMEK-encrypted BigQuery resources, you must also grant the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role to the relevant service agents. For more information, see [DataScans CMEK permissions](https://docs.cloud.google.com/knowledge-catalog/docs/cmek#datascans-cmek-permissions).

If you haven't created any data quality or data profile scans or you don't have a Knowledge Catalog lake in this project, create a service identifier by running: `gcloud beta services identity create --service=dataplex.googleapis.com`. This command returns a Knowledge Catalog service identifier if it exists.

To ensure that the Knowledge Catalog service account of the project containing the data quality scan has the necessary permissions to read data from various sources and export results, ask your administrator to grant the following IAM roles to the Knowledge Catalog service account of the project containing the data quality scan: 

**Important:** You must grant these roles to the Knowledge Catalog service account of the project containing the data quality scan, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Read BigQuery table data: [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on tables to be scanned and any other tables referenced in rules 
  * Read Iceberg REST Catalog, SAP Business Data Cloud Delta Lake, and Apache Hive on Google Cloud Lakehouse table data: [BigLake Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`) on respective tables to be scanned and any other tables referenced in rules 
  * Export scan results to a BigQuery table: [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) on the results dataset and table 
  * Scan BigQuery data organized in a Knowledge Catalog lake: 
    * [Dataplex Metadata Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataReader) (`roles/dataplex.metadataReader`) on Dataplex resources
    * [Dataplex Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`) on Dataplex resources
  * Scan a BigQuery external table from Cloud Storage: [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the Cloud Storage bucket 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to read data from various sources and export results. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to read data from various sources and export results:

  * Read BigQuery table data: 
    * `bigquery.tables.get` on BigQuery tables
    * `bigquery.tables.getData` on BigQuery tables
  * Export scan results to a BigQuery table: 
    * `bigquery.datasets.get` on results dataset and table
    * `bigquery.tables.create` on results dataset and table
    * `bigquery.tables.get` on results dataset and table
    * `bigquery.tables.getData` on results dataset and table
    * `bigquery.tables.update` on results dataset and table
    * `bigquery.tables.updateData` on results dataset and table
  * Scan BigQuery data organized in a Knowledge Catalog lake: 
    * `dataplex.lakes.list` on Dataplex resources
    * `dataplex.lakes.get` on Dataplex resources
    * `dataplex.zones.list` on Dataplex resources
    * `dataplex.zones.get` on Dataplex resources
    * `dataplex.entities.list` on Dataplex resources
    * `dataplex.entities.get` on Dataplex resources
    * `dataplex.operations.get` on Dataplex resources
  * Scan a BigQuery external table from Cloud Storage: 
    * `storage.buckets.get` on the Cloud Storage bucket
    * `storage.objects.get` on the Cloud Storage bucket



Your administrator might also be able to give the Knowledge Catalog service account of the project containing the data quality scan these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you need to access columns protected by BigQuery column-level access policies, then assign the Knowledge Catalog service account permissions for those columns.

If a table has BigQuery row-level access policies enabled, then you can only scan rows visible to the Knowledge Catalog service account. Note that the individual user's access privileges are not evaluated for row-level policies.

### Networking requirements

To run a scan, you must enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-pga) on the [VPC subnet](https://docs.cloud.google.com/vpc/docs/subnets) that you use for the scan. If you don't specify a subnet, make sure your default subnet has Private Google Access enabled.

## Define data quality rules

You can define data quality rules by using the following:

  * [Built-in rules](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#predefined-rules)

  * [Custom SQL checks](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#supported-custom-sql-rule-types)

  * [Reusable rules](https://docs.cloud.google.com/knowledge-catalog/docs/reuse-data-quality-rules), including [system rule templates](https://docs.cloud.google.com/knowledge-catalog/docs/reuse-data-quality-rules#system-templates)




If you're using the Google Cloud CLI, you can define these rules in a [JSON or YAML file](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec).

The examples in the following sections show how to define a variety of data quality rules. The rules validate a sample table that contains data about customer transactions. Assume the table has the following schema:

**Column name** | **Column type** | **Column description**  
---|---|---  
transaction_timestamp  | Timestamp  | Timestamp of the transaction. The table is partitioned on this field.   
customer_id  | String  | A customer ID in the format of 8 letters followed by 16 digits.   
transaction_id  | String  | The transaction ID needs to be unique across the table.   
currency_id  | String  | One of the supported currencies. The currency type must match one of the available currencies in the dimension table `dim_currency`.   
amount  | float  | Transaction amount.   
discount_pct  | float  | Discount percentage. This value must be between 0 and 100.   
  
### Define data quality rules using built-in rule types

The following examples are based on built-in rule types. You can create rules based on built-in rule types using the Google Cloud console or the API. Knowledge Catalog might recommend some of these rules.

Column name  |  Rule Type  |  Suggested dimension  |  Rule parameters   
---|---|---|---  
`transaction_id` |  Uniqueness check  |  Uniqueness  |  Threshold: `Not Applicable`  
`amount` |  Null check  |  Completeness  |  Threshold: `100%`  
`customer_id` | Regex (regular expression) check  |  Validity  | Regular expression: `^[a-zA-Z]{8}[0-9]{16}$`   
Threshold: `100%`  
`currency_id` |  Value set check  |  Validity  |  Set of: `USD,JPY,INR,GBP,CAN`   
Threshold: `100%`  
  
### Define data quality rules using custom SQL rules

To build custom SQL rules, use the following framework:

  * When you create a rule that evaluates one row at a time, create an expression that generates the number of successful rows when Knowledge Catalog evaluates the query `SELECT COUNTIF(CUSTOM_SQL_EXPRESSION) FROM TABLE`. Knowledge Catalog checks the number of successful rows against the threshold.

  * When you create a rule that evaluates across the rows or uses a table condition, create an expression that returns success or failure when Knowledge Catalog evaluates the query `SELECT IF(CUSTOM_SQL_EXPRESSION) FROM TABLE`.

  * When you create a rule that evaluates the invalid state of a dataset, provide a statement that returns invalid rows. If any rows are returned, the rule fails. Omit the trailing semicolon from the SQL statement.

  * You can refer to a data source table and all of its precondition filters by using the data reference parameter `${data()}` in a rule, instead of explicitly mentioning the source table and its filters. Examples of precondition filters include row filters, sampling percents, and incremental filters. The `${data()}` parameter is case-sensitive.




The following examples are based on custom SQL rules.

Rule type  | Rule description  | SQL expression   
---|---|---  
Row condition  | Checks if the value of the `discount_pct` is between 0 and 100.  | `0` <`discount_pct` AND `discount_pct` < `100`  
Row condition  | Reference check to validate that `currency_id` is one of the supported currencies.  | `currency_id in (select id from my_project_id.dim_dataset.dim_currency)`  
Table condition  | Aggregate SQL expression that checks if the average `discount_pct` is between 30% and 50%.  | `30<avg(discount) AND avg(discount) <50`  
Row condition  | Checks if a date is not in the future.  | `TIMESTAMP(transaction_timestamp) < CURRENT_TIMESTAMP()`  
Table condition  |  A [ BigQuery user-defined function (UDF)](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions) to check that the average transaction amount is less than a predefined value per country. Create the (Javascript) UDF by running the following command: 
    
    
            CREATE OR REPLACE FUNCTION
            myProject.myDataset.average_by_country (
              country STRING, average FLOAT64)
            RETURNS BOOL LANGUAGE js AS R"""
            if (country = "CAN" && average < 5000){
              return 1
            } else if (country = "IND" && average < 1000){
              return 1
            } else { return 0 }
            """;
           

|  Example rule to check the average transaction amount for `country=CAN`. 
    
    
            myProject.myDataset.average_by_country(
            "CAN",
            (SELECT avg(amount) FROM
              myProject.myDataset.transactions_table
                WHERE currency_id = 'CAN'
            ))
            
  
Table condition  |  A [BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction) predict clause to identify anomalies in `discount_pct`. It checks if a discount should be applied based on `customer`, `currency`, and `transaction`. The rule checks if the prediction matches the actual value, at least 99% of times. Assumption: The ML model is created before using the rule. Create the ML model using the following command: 
    
    
      CREATE MODEL
      model-project-id.dataset-id.model-name
            OPTIONS(model_type='logistic_reg') AS
      SELECT
      IF(discount_pct IS NULL, 0, 1) AS label,
      IFNULL(customer_id, "") AS customer,
      IFNULL(currency_id, "") AS currency,
      IFNULL(amount, 0.0) AS amount
      FROM
      `data-project-id.dataset-id.table-names`
      WHERE transaction_timestamp < '2022-01-01';
      

|  The following rule checks if prediction accuracy is greater than 99%. 
    
    
          SELECT
            accuracy > 0.99
          FROM
           ML.EVALUATE
            (MODEL model-project-id.dataset-id.model-name,
             (
              SELECT
                customer_id,
                currency_id,
                amount,
                discount_pct
              FROM
                data-project-id.dataset-id.table-names
              WHERE transaction_timestamp > '2022-01-01';
             )
            )
          
  
Row condition  |  A [BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction) predict function to identify anomalies in `discount_pct`. The function checks if a discount should be applied based on `customer`, `currency` and `transaction`. The rule identifies all the occurrences where the prediction didn't match. Assumption: The ML model is created before using the rule. Create the ML model using the following command: 
    
    
      CREATE MODEL
      model-project-id.dataset-id.model-name
            OPTIONS(model_type='logistic_reg') AS
      SELECT
      IF(discount_pct IS NULL, 0, 1) AS label,
      IFNULL(customer_id, "") AS customer,
      IFNULL(currency_id, "") AS currency,
      IFNULL(amount, 0.0) AS amount
      FROM
      `data-project-id.dataset-id.table-names`
      WHERE transaction_timestamp < '2022-01-01';
      

|  The following rule checks if the discount prediction matches with the actual for every row. 
    
    
           IF(discount_pct > 0, 1, 0)
              =(SELECT predicted_label FROM
               ML.PREDICT(
                MODEL model-project-id.dataset-id.model-name,
                  (
                    SELECT
                      customer_id,
                      currency_id,
                      amount,
                      discount_pct
                    FROM
                      data-project-id.dataset-id.table-names AS t
                        WHERE t.transaction_timestamp =
                         transaction_timestamp
                       LIMIT 1
                  )
                )
             )
          
  
SQL assertion | Validates if the `discount_pct` is greater than 30% for today by checking whether any rows exist with a discount percent less than or equal to 30. | `SELECT * FROM my_project_id.dim_dataset.dim_currency WHERE discount_pct <= 30 AND transaction_timestamp >= current_date()`  
SQL assertion (with [data reference parameter](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#data-reference-parameter)) | Checks if the `discount_pct` is greater than 30% for all the supported currencies today. The date filter `transaction_timestamp >= current_date()` is applied as a row filter on the data source table. The data reference parameter `${data()}` acts as a placeholder for `my_project_id.dim_dataset.dim_currency WHERE transaction_timestamp >= current_date()` and applies the row filter. | `SELECT * FROM ${data()} WHERE discount_pct > 30`  
  
### Define data quality rules using the gcloud CLI

The following example YAML file uses some of the same rules as the sample rules using built-in types and the sample custom SQL rules. This YAML file also contains other specifications for the data quality scan, such as filters and sampling percent. When you use the gcloud CLI to create or update a data quality scan, you can use a YAML file like this as input to the `--data-quality-spec-file` argument.
    
    
    **rules :
    - uniquenessExpectation: {}
      column: transaction_id
      dimension: UNIQUENESS
    - nonNullExpectation: {}
      column: amount
      dimension: COMPLETENESS
      threshold: 1
    - regexExpectation:
        regex: '^[a-zA-Z]{8}[0-9]{16}$'
      column : customer_id
      ignoreNull : true
      dimension : VALIDITY
      threshold : 1
    - setExpectation :
        values :
        - 'USD'
        - 'JPY'
        - 'INR'
        - 'GBP'
        - 'CAN'
      column : currency_id
      ignoreNull : true
      dimension : VALIDITY
      threshold : 1
    - rangeExpectation:
        minValue : '0'
        maxValue : '100'
      column : discount_pct
      ignoreNull : true
      dimension : VALIDITY
      threshold : 1
    - rowConditionExpectation:
        sqlExpression : 0 < `discount_pct` AND `discount_pct` < 100
      column: discount_pct
      dimension: VALIDITY
      threshold: 1
    - rowConditionExpectation:
        sqlExpression : currency_id in (select id from `my_project_id.dim_dataset.dim_currency`)
      column: currency_id
      dimension: VALIDITY
      threshold: 1
    - tableConditionExpectation:
        sqlExpression : 30 < avg(discount_pct) AND avg(discount_pct) < 50
      dimension: VALIDITY
    - rowConditionExpectation:
        sqlExpression : TIMESTAMP(transaction_timestamp) < CURRENT_TIMESTAMP()
      column: transaction_timestamp
      dimension: VALIDITY
      threshold: 1
    - sqlAssertion:
        sqlStatement : SELECT * FROM `my_project_id.dim_dataset.dim_currency` WHERE discount_pct > 100
      dimension: VALIDITY
      debugQueries:
      - sqlStatement: SELECT MAX(discount_pct) FROM `my_project_id.dim_dataset.dim_currency`
    samplingPercent: 50
    rowFilter: discount_pct > 100
    postScanActions:
      bigqueryExport:
        resultsTable: projects/my_project_id/datasets/dim_dataset/tables/dim_currency
      notificationReport:
        recipients:
          emails:
          - '222larabrown@gmail.com'
          - 'cloudysanfrancisco@gmail.com'
        scoreThresholdTrigger:
          scoreThreshold: 50
        jobFailureTrigger: {}
        jobEndTrigger: {}
    catalogPublishingEnabled: true
    **
    

## Configure execution identity

By default, data quality scans run using the Knowledge Catalog service account. You can override this to use a custom service account or your own End-User Credentials (EUC).

Using a custom execution identity changes how you are billed for the scan. When you specify a custom execution identity, the compute and storage costs associated with the scan are billed directly to your BigQuery project, bypassing the standard Knowledge Catalog Premium SKUs.

### Required permissions for custom execution identities

To configure a custom service account or use end-user credentials, you must have the following additional Identity and Access Management (IAM) permissions:

  * To use a **custom service account** , you need: 
    * The `iam.serviceAccounts.actAs` permission granted for the project that contains the service account (for example, `roles/iam.serviceAccountUser`).
    * Your project's Service Agent (`service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com`) needs the `iam.serviceAccounts.getAccessToken` permission on the custom service account (for example, by having the `roles/iam.serviceAccountTokenCreator` role).
    * The custom service account needs `bigquery.tables.getData` on the table to scan, `bigquery.jobs.insert` in the scan project, and `bigquery.dataEditor` on the export dataset (if using export).
  * To use **End-User Credentials** , you need: 
    * `bigquery.tables.getData` on the table to scan.
    * `bigquery.jobs.insert` in the scan project.
    * `bigquery.dataEditor` on the export dataset (if using export).



To configure the execution identity, select one of the following options:

### Console

To configure the execution identity in the Google Cloud console, select the identity when you create your data quality scan.

In the **Execution Identity** section, select one of the following:

  * **Dataplex Service Agent** : The default behavior.
  * **Service Account** : Enter the email address of the service account that you want to use.
  * **User Credential** : Use your own credentials to run the scan.



### REST

To use a custom service account, add the `executionIdentity` object to your `DataScan` resource definition during the `create` request:
    
    
    "executionIdentity": {
      "serviceAccount": {
         "email": "YOUR_SERVICE_ACCOUNT_EMAIL"
      }
    }
      

Replace the following:

  * `YOUR_SERVICE_ACCOUNT_EMAIL`: the email address of the service account that you want to use.



To use end-user credentials, specify the `userCredential` object instead:
    
    
    "executionIdentity": {
      "userCredential": {}
    }
      

**Note:** The execution identity is immutable. You can only set it when you create a scan. You can't change it by updating an existing scan.

## Create a data quality scan

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Click **Create data quality scan**.

  3. In the **Define scan** window, fill in the following fields:

     1. Optional: Enter a **Display name**.

     2. Enter an **ID**. See the [resource naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

     3. Optional: Enter a **Description**.

     4. In the **Table** field, click **Browse**. Choose the table to scan, and then click **Select**. Only standard BigQuery, Iceberg REST Catalog, SAP BDC Delta, and Hive on Google Cloud Lakehouse tables are supported.

For tables in multi-region datasets, choose a region where to create the data scan.

To browse the tables organized within Knowledge Catalog lakes, click **Browse within Knowledge Catalog Lakes**.

     5. In the **Scope** field, choose **Incremental** or **Entire data**.

        * If you choose **Incremental** : In the **Timestamp column** field, select a column of type `DATE` or `TIMESTAMP` from your BigQuery table that increases as new records are added, and that can be used to identify new records. It can be a column that partitions the table.
     6. Optional: To filter your data, select the **Filter rows** checkbox. Provide a row filter consisting of a valid SQL expression that can be used as a part of a [`WHERE` clause in GoogleSQL syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#where_clause). For example, `col1 >= 0`. The filter can be a combination of multiple column conditions. For example, `col1 >= 0 AND col2 < 10`.

     7. To sample your data, in the **Sampling size** list, select a sampling percentage. Choose a percentage value that ranges between 0.0% and 100.0% with up to 3 decimal digits. For larger datasets, choose a lower sampling percentage. For example, for a 1 PB table, if you enter a value between 0.1% and 1.0%, the data quality scan samples between 1-10 TB of data. For incremental data scans, the data quality scan applies sampling to the latest increment.

     8. Optional: To publish the data quality scan results as Knowledge Catalog metadata, select the **Publish results to Knowledge Catalog** checkbox.

You can view the latest scan results on the **Data quality** tab in the BigQuery and Knowledge Catalog pages for the source table. To enable users to access the published scan results, see the Grant access to data quality scan results section of this document. 

     9. For **Credential type** , see [Configure execution identity](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality#configure-execution-identity).

     10. To [create a data quality scan using rules](https://docs.cloud.google.com/knowledge-catalog/docs/reuse-data-quality-rules#create-scan-catalog), select **Rule type > Create with entry based rule**.

     11. In the **Schedule** section, choose one of the following options:

        * **Repeat** : Run the data quality scan on a schedule: hourly, daily, weekly, monthly, or custom. Specify how often the scan runs and at what time. If you choose custom, use [cron](https://en.wikipedia.org/wiki/Cron) format to specify the schedule.

        * **On-demand** : Run the data quality scan on demand.

        * **One-time run** : Run the data quality scan once now, and remove the scan after the auto-deletion time. This feature is in [preview](https://cloud.google.com/products/#product-launch-stages).

          * **Set post-scan results auto-deletion** : The auto-deletion time is the time span between when the scan is executed and when the scan is deleted. A data quality scan without a specified auto-deletion time is automatically deleted 24 hours after its execution. The auto-deletion time can range from 0 seconds (immediate deletion) to 365 days.
     12. Click **Continue**.

  4. In the **Data quality rules** window, define the rules to configure for this data quality scan.

     1. Click **Add rules** , and then choose from the following options.

        * **Profile based recommendations** : Build rules from the recommendations based on an existing data profiling scan.

          1. **Choose columns** : Select the columns to get recommended rules for.

          2. **Choose scan project** : If the data profiling scan is in a different project than the project where you are creating the data quality scan, then select the project to pull profile scans from.

          3. **Choose profile results** : Select one or more profile results and then click **OK**. This populates a list of suggested rules that you can use as a starting point.

          4. Select the checkbox for the rules that you want to add, and then click **Select**. Once selected, the rules are added to your current rule list. Then, you can edit the rules.

        * **Built-in rule types** : Build rules from predefined rules. See the list of [predefined rules](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#predefined-rules).

          1. **Choose columns** : Select the columns to select rules for.

          2. **Choose rule types** : Select the rule types that you want to choose from, and then click **OK**. The rule types that appear depend on the columns that you selected.

          3. Select the checkbox for the rules that you want to add, and then click **Select**. Once selected, the rules are added to your current rules list. Then, you can edit the rules.

        * **SQL row check rule** : Create a custom SQL rule to apply to each row.

          1. In **Dimension** , choose one dimension.

          2. In **Passing threshold** , choose a percentage of records that must pass the check.

          3. In **Column name** , choose a column.

          4. In the **Provide a SQL expression** field, enter a SQL expression that evaluates to a boolean `true` (pass) or `false` (fail). For more information, see [Supported custom SQL rule types](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#supported-custom-sql-rule-types) and the examples in [Define data quality rules](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality#sample-rules).

          5. Click **Add**.

        * **SQL aggregate check rule** : Create a custom SQL table condition rule.

          1. In **Dimension** , choose one dimension.

          2. In **Column name** , choose a column.

          3. In the **Provide a SQL expression** field, enter a SQL expression that evaluates to a boolean `true` (pass) or `false` (fail). For more information, see [Supported custom SQL rule types](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#supported-custom-sql-rule-types) and the examples in [Define data quality rules](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality#sample-rules).

          4. Click **Add**.

        * **SQL assertion rule** : Create a custom SQL assertion rule to check for an invalid state of the data.

          1. In **Dimension** , choose one dimension.

          2. Optional: In **Column name** , choose a column.

          3. In the **Provide a SQL statement** field, enter a SQL statement that returns rows that match the invalid state. If any rows are returned, this rule fails. Omit the trailing semicolon from the SQL statement. For more information, see [Supported custom SQL rule types](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#supported-custom-sql-rule-types) and the examples in [Define data quality rules](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality#sample-rules).

          4. Click **Add**.

     2. Optional: For any data quality rule, you can assign a custom rule name to use for monitoring and alerting, and a description. To do this, edit a rule and specify the following details:

        * **Rule name** : Enter a custom rule name with up to 63 characters. The rule name can include letters (a-z, A-Z), digits (0-9), and hyphens (-) and must start with a letter and end with a number or a letter.
        * **Description** : Enter a rule description with a maximum length of 1,024 characters.
     3. Repeat the previous steps to add additional rules to the data quality scan. When finished, click **Continue**.

  5. Optional: Export the scan results to a BigQuery standard table. In the **Export scan results to BigQuery table** section, do the following:

     1. In the **Select BigQuery dataset** field, click **Browse**. Select a BigQuery dataset to store the data quality scan results.

     2. In the **BigQuery table** field, specify the table to store the data quality scan results. If you're using an existing table, make sure that it is compatible with the [export table schema](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality#table-schema). If the specified table doesn't exist, Knowledge Catalog creates it for you.

**Note:** You can use the same results table for multiple data quality scans.
  6. Optional: Add labels. Labels are key-value pairs that let you group related objects together or with other Google Cloud resources.

  7. Optional: Set up email notification reports to alert people about the status and results of a data quality scan job. In the **Notification report** section, click add **Add email ID** and enter up to five email addresses. Then, select the scenarios that you want to send reports for:

     * **Quality score ( <=)**: sends a report when a job succeeds with a data quality score that is lower than the specified target score. Enter a target quality score between 0 and 100.
     * **Job failures** : sends a report when the job itself fails, regardless of the data quality results.
     * **Job completion (success or failure)** : sends a report when the job ends, regardless of the data quality results.
  8. Click **Create**.

After the scan is created, you can run it at any time by clicking **Run now**.




### gcloud

To create a data quality scan, use the [`gcloud dataplex datascans create data-quality` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality).

If the source data is organized in a Knowledge Catalog lake, include the `--data-source-entity` flag:
    
    
    gcloud dataplex datascans create data-quality DATASCAN \
        --location=LOCATION \
        --data-quality-spec-file=DATA_QUALITY_SPEC_FILE \
        --data-source-entity=DATA_SOURCE_ENTITY
    

If the source data isn't organized in a Knowledge Catalog lake, include the `--data-source-resource` flag:
    
    
    gcloud dataplex datascans create data-quality DATASCAN \
        --location=LOCATION \
        --data-quality-spec-file=DATA_QUALITY_SPEC_FILE \
        --data-source-resource=DATA_SOURCE_RESOURCE
    

Replace the following variables:

  * `DATASCAN`: The name of the data quality scan.
  * `LOCATION`: The Google Cloud region in which to create the data quality scan.
  * `DATA_QUALITY_SPEC_FILE`: The path to the JSON or YAML file containing the specifications for the data quality scan. The file can be a local file or a Cloud Storage path with the prefix `gs://`. Use this file to specify the data quality rules for the scan. You can also specify additional details in this file, such as filters, sampling percent, and post-scan actions like exporting to BigQuery or sending email notification reports. See the [documentation for JSON representation](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec) and the [example YAML representation](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality#create-scan-using-gcloud).
  * `DATA_SOURCE_ENTITY`: The Knowledge Catalog entity that contains the data for the data quality scan. For example, `projects/test-project/locations/test-location/lakes/test-lake/zones/test-zone/entities/test-entity`.
  * `DATA_SOURCE_RESOURCE`: The name of the resource that contains the data for the data quality scan. For example, `//bigquery.googleapis.com/projects/test-project/datasets/test-dataset/tables/test-table`.



###  C# 

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedDataScanServiceClientSnippets
    {
        /// <summary>Snippet for CreateDataScan</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void CreateDataScanRequestObject()
        {
            // Create client
            [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html) dataScanServiceClient = [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html#Google_Cloud_Dataplex_V1_DataScanServiceClient_Create)();
            // Initialize request argument(s)
            [CreateDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateDataScanRequest.html) request = new [CreateDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateDataScanRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                DataScan = new [DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.html)(),
                DataScanId = "",
                ValidateOnly = false,
            };
            // Make the request
            Operation<DataScan, OperationMetadata> response = dataScanServiceClient.[CreateDataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html#Google_Cloud_Dataplex_V1_DataScanServiceClient_CreateDataScan_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Dataplex_V1_DataScan_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<DataScan, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<DataScan, OperationMetadata> retrievedResponse = dataScanServiceClient.[PollOnceCreateDataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html#Google_Cloud_Dataplex_V1_DataScanServiceClient_PollOnceCreateDataScan_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

###  Go 

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewDataScanClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_DataScanClient_NewDataScanClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.CreateDataScanRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#CreateDataScanRequest.
    	}
    	op, err := c.CreateDataScan(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

###  Java 

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CreateDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataScanRequest.html);
    import com.google.cloud.dataplex.v1.[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan.html);
    import com.google.cloud.dataplex.v1.[DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html);
    import com.google.cloud.dataplex.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html);
    
    public class SyncCreateDataScan {
    
      public static void main(String[] args) throws Exception {
        syncCreateDataScan();
      }
    
      public static void syncCreateDataScan() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html) dataScanServiceClient = [DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html).create()) {
          [CreateDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataScanRequest.html) request =
              [CreateDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataScanRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .setDataScan([DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan.html).newBuilder().build())
                  .[setDataScanId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataScanRequest.Builder.html#com_google_cloud_dataplex_v1_CreateDataScanRequest_Builder_setDataScanId_java_lang_String_)("dataScanId1260787906")
                  .setValidateOnly(true)
                  .build();
          [DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan.html) response = dataScanServiceClient.[createDataScanAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html#com_google_cloud_dataplex_v1_DataScanServiceClient_createDataScanAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_LocationName_com_google_cloud_dataplex_v1_DataScan_java_lang_String_)(request).get();
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    //
    // ** This file is automatically generated by gapic-generator-typescript. **
    // ** https://github.com/googleapis/gapic-generator-typescript **
    // ** All changes to this file may be overwritten. **
    
    
    
    'use strict';
    
    function main(parent, dataScan) {
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the parent location:
       *  `projects/{project}/locations/{location_id}`
       *  where `project` refers to a *project_id* or *project_number* and
       *  `location_id` refers to a Google Cloud region.
       */
      // const parent = 'abc123'
      /**
       *  Required. DataScan resource.
       */
      // const dataScan = {}
      /**
       *  Optional. DataScan identifier. If not provided, a unique ID will be
       *  generated with the prefix "data-scan-".
       *  * Must contain only lowercase letters, numbers and hyphens.
       *  * Must start with a letter.
       *  * Must end with a number or a letter.
       *  * Must be between 1-63 characters.
       *  * Must be unique within the customer project / location.
       */
      // const dataScanId = 'abc123'
      /**
       *  Optional. Only validate the request, but do not perform mutations.
       *  The default is `false`.
       */
      // const validateOnly = true
    
      // Imports the Dataplex library
      const {DataScanServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
      // Instantiates a client
      const dataplexClient = new [DataScanServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
      async function callCreateDataScan() {
        // Construct request
        const request = {
          parent,
          dataScan,
        };
    
        // Run request
        const [operation] = await dataplexClient.createDataScan(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateDataScan();
    }
    
    process.on('unhandledRejection', err => {
      console.error(err.message);
      process.exitCode = 1;
    });
    main(...process.argv.slice(2));
    

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Copyright 2026 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    import google.api_core.exceptions
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def create_data_quality_scan_global(
        project_id: str,
        dataset_id: str,
        table_id: str,
        location: str,
        column_id_1: str,
        column_id_2: str,
    ) -> None:
        """Creates a Dataplex Data Quality Scan using global API endpoint routing.
    
        Args:
            project_id (str): Google Cloud project ID where the scan is created.
            dataset_id (str): Target BigQuery dataset ID.
            table_id (str): Target BigQuery table ID to scan.
            location (str): Google Cloud region where serverless compute runs.
            column_id_1 (str): Name of the first column to evaluate.
            column_id_2 (str): Name of the second column to evaluate.
        """
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataScanServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_scan_service.DataScanServiceClient.html)()
    
        parent = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_scan_service.DataScanServiceClient.html#google_cloud_dataplex_v1_services_data_scan_service_DataScanServiceClient_common_location_path)(project=project_id, location=location)
    
        # A bigquery table with at least 2 columns is assumed.
        bigquery_table = (
            f"//bigquery.googleapis.com/projects/{project_id}"
            f"/datasets/{dataset_id}/tables/{table_id}"
        )
    
        data_quality_spec = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataQualitySpec](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DataQualitySpec.html)(
            rules=[
                [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataQualityRule](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DataQualityRule.html)(
                    name="global-null-assertion",
                    dimension="COMPLETENESS",
                    description="Fails if any row contains a null value",
                    sql_assertion=[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataQualityRule](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DataQualityRule.html).[SqlAssertion](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DataQualityRule.SqlAssertion.html)(
                        # Use ${data()} as the placeholder for the table Dataplex is scanning
                        sql_statement=(
                            "SELECT * FROM ${data()} "
                            f"WHERE {column_id_1} IS NULL OR {column_id_2} IS NULL"
                        )
                    ),
                )
            ]
        )
    
        data_scan = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataScan](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DataScan.html)(
            display_name="Global Data Quality Scan",
            data=[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataSource](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DataSource.html)(resource=bigquery_table),
            data_quality_spec=data_quality_spec,
        )
    
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CreateDataScanRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.CreateDataScanRequest.html)(parent=parent, data_scan=data_scan)
    
        try:
            operation = client.[create_data_scan](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_scan_service.DataScanServiceClient.html#google_cloud_dataplex_v1_services_data_scan_service_DataScanServiceClient_create_data_scan)(request=request)
            print(operation.result())
        except google.api_core.exceptions.AlreadyExists:
            print("A scan with this ID already exists.")
        except google.api_core.exceptions.InvalidArgument as e:
            print(f"Your scan configuration is invalid: {e}")
        except google.api_core.exceptions.GoogleAPIError as e:
            print(f"Unexpected exception: {e}")
    
    

###  Ruby 

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the create_data_scan call in the DataScanService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::DataScanService::Client#create_data_scan.
    #
    def create_data_scan
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::DataScanService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::CreateDataScanRequest.new
    
      # Call the create_data_scan method.
      result = client.create_data_scan request
    
      # The returned object is of type Gapic::Operation. You can use it to
      # check the status of an operation, cancel it, or wait for results.
      # Here is how to wait for a response.
      result.wait_until_done! timeout: 60
      if result.response?
        p result.response
      else
        puts "No response received."
      end
    end

### REST

To create a data quality scan, use the [`dataScans.create` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/create).

The following request creates a one-time data quality scan:
    
    
    POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/dataScans?data_scan_id=DATASCAN_ID
    
    {
    "data": {
      "resource": "//bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID"
    },
    "type": "DATA_QUALITY",
    "executionSpec": {
      "trigger": {
        "oneTime": {
          "ttl_after_scan_completion": "120s"
        }
      }
    },
    "dataQualitySpec": {
      "rules": [
        {
          "nonNullExpectation": {},
          "column": "COLUMN_NAME",
          "dimension": "DIMENSION",
          "threshold": 1
        }
      ],
      "filter": "FILTER_CONDITION"
    }
    }

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: The region where to create the data quality scan.
  * `DATASCAN_ID`: The ID of the data quality scan.
  * `DATASET_ID`: The ID of BigQuery dataset.
  * `TABLE_ID`: The ID of BigQuery table.
  * `COLUMN_NAME`: The column name for the rule.
  * `DIMENSION`: The dimension for the rule, for example `VALIDITY`.
  * `FILTER_CONDITION`: An optional [AIP-160 filter string](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#rule-filtering) to selectively run rules (for example, `name = \"RULE_NAME\"`).



If you want to build rules for the data quality scan by using rule recommendations that are based on the results of a data profiling scan, get the recommendations by calling the [`dataScans.jobs.generateDataQualityRules` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans.jobs/generateDataQualityRules) on the data profiling scan.

**Note:** If your BigQuery table is configured with the **Require partition filter** set to `true`, use the BigQuery partition column as the data quality scan row filter or timestamp column. 

### Export table schema

To export the data quality scan results to an existing BigQuery table, make sure that it is compatible with the following table schema:

Column name | Column data type | Sub field name  
(if applicable) | Sub field data type | Mode | Example  
---|---|---|---|---|---  
data_quality_scan | `struct/record` | `resource_name` | `string` | nullable | `//dataplex.googleapis.com/projects/test-project/locations/europe-west2/datascans/test-datascan`  
`project_id` | `string` | nullable | `dataplex-back-end-dev-project`  
`location` | `string` | nullable | `us-central1`  
`data_scan_id` | `string` | nullable | `test-datascan`  
`display_name` | `string` | nullable | `datascan-display-name`  
data_source | `struct/record` | `resource_name` | `string` | nullable | Entity case:  
`//dataplex.googleapis.com/projects/dataplex-back-end-dev-project/locations/europe-west2/lakes/a0-datascan-test-lake/zones/a0-datascan-test-zone/entities/table1`  
  
Table case: `//bigquery.googleapis.com/projects/test-project/datasets/test-dataset/tables/test-table`  
`dataplex_entity_project_id` | `string` | nullable | `dataplex-back-end-dev-project`  
`dataplex_entity_project_number` | `integer` | nullable | `123456789`  
`dataplex_lake_id` | `string` | nullable | (Valid only if source is entity)  
`test-lake`  
`dataplex_zone_id` | `string` | nullable | (Valid only if source is entity)  
`test-zone`  
`dataplex_entity_id` | `string` | nullable | (Valid only if source is entity)  
`test-entity`  
`table_project_id` | `string` | nullable | `test-project`  
`table_project_number` | `integer` | nullable | `987654321`  
`dataset_id` | `string` | nullable | (Valid only if source is table)  
`test-dataset`  
`table_id` | `string` | nullable | (Valid only if source is table)  
`test-table`  
data_quality_job_id | `string` |  |  | nullable | `caeba234-cfde-4fca-9e5b-fe02a9812e38`  
data_quality_job_configuration | `json` |  |  | nullable | `{"trigger": "ondemand", "incremental": true}`  
job_labels | `json` |  |  | nullable | `{"key1":value1}`  
job_start_time | `timestamp` |  |  | nullable | `2023-01-01 00:00:00 UTC`  
job_end_time | `timestamp` |  |  | nullable | `2023-01-01 00:00:00 UTC`  
job_quality_result | `struct/record` | `passed` | `boolean` | nullable | `true`/`false`  
`score` | `float` | nullable | `90.8`  
`incremental_start` | `string` | nullable | `2023-01-01T00:00:00`  
`incremental_end` | `string` | nullable | `2024-01-01T00:00:00`  
job_dimension_result | `json` |  |  | nullable | `{"ACCURACY":{"passed":true,"score":100},"CONSISTENCY":{"passed":false,"score":60}}`  
job_rows_scanned | `integer` |  |  | nullable | `7500`  
rule_name | `string` |  |  | nullable | `test-rule`  
rule_description | `string` |  |  | nullable | `Test rule description`  
rule_type | `string` |  |  | nullable | `Range Check`  
rule_evaluation_type | `string` |  |  | nullable | `Per row`  
rule_column | `string` |  |  | nullable | `Rule only attached to a certain column`  
rule_dimension | `string` |  |  | nullable | `UNIQUENESS`  
rule_threshold_percent | `float` |  |  | nullable | (0.0-100.0)  
`Rule-threshold-pct in API * 100`  
rule_parameters | `json` |  |  | nullable | `{min: 24, max:5345}`  
rule_passed | `boolean` |  |  | nullable | `true`  
rule_rows_evaluated | `integer` |  |  | nullable | `7400`  
rule_rows_passed | `integer` |  |  | nullable | `3`  
rule_rows_passed_percent | `float` |  |  | nullable | (0.0-100.0)  
`80.0` (indicates 80%)  
rule_rows_null | `integer` |  |  | nullable | `4`  
rule_failed_records_query | `string` |  |  | nullable | `"SELECT * FROM `test-project.test-dataset.test-table` WHERE (NOT((`cTime` >= '15:31:38.776361' and `cTime` <= '19:23:53.754823') IS TRUE));"`  
created_on | `timestamp` |  |  | nullable | `2023-01-01 00:00:00 UTC`  
last_updated | `timestamp` |  |  | nullable | `2023-01-01 00:00:00 UTC`  
rule_assertion_row_count | `integer` |  |  | nullable | `10`  
debug_queries | `struct/record` | `description` | `string` | nullable | `Test debug query description`  
`sql_statement` | `string` | nullable | `SELECT MIN(col1) AS min_col1, AVG(col1) FROM ${data()}`  
`debug_query_results` | `struct/record` | repeated | `[{"name": "min_col1", "type": "INTEGER", "value": "5"}, {"type": "FLOAT", "value": "7"}]`  
↳ `name` | `string` | nullable | The name of query result column, like `min_col1`  
↳ `type` | `string` | nullable | The type of query result column, like `INTEGER`  
↳ `value` | `string` | nullable | The value of query result column, like `5`  
rule_attributes | `json` |  |  | nullable | `{"key": "value"}`  
rule_source | `struct/record` | `rule_path_elements` | `struct/record` | repeated | `[{"entry_source": {"entry_type": "bigquery_table"}}]`  
↳ `entry_source` | `struct/record` | nullable | `{"entry_type": "bigquery_table"}`  
↳ `entry_type` | `string` | nullable | `bigquery_table`  
↳ `entry` | `string` | nullable | `projects/test-project/locations/us/entryGroups/@bigquery/entries/test-table`  
↳ `display_name` | `string` | nullable | `test-table`  
↳ `entry_link_source` | `struct/record` | nullable | `{"entry_link_type": "table_spec"}`  
↳ `entry_link_type` | `string` | nullable | `table_spec`  
↳ `entry_link` | `string` | nullable | `projects/test-project/locations/us/entryLinks/test-link`  
**Note:** Column `rule_assertion_row_count` is only applicable for [SQL Assertion rule](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualityRule#SqlAssertion).

When you configure [BigQueryExport](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec#bigqueryexport) for a data quality scan job, follow these guidelines:

  * For the field `resultsTable`, use the format: `//bigquery.googleapis.com/projects/{project-id}/datasets/{dataset-id}/tables/{table-id}`.
  * Use a BigQuery standard table.
  * If the table doesn't exist when the scan is created or updated, Knowledge Catalog creates the table for you.
  * By default, the table is partitioned on the `job_start_time` column daily.
  * If you want the table to be partitioned in other configurations or if you don't want the partition, then recreate the table with the required schema and configurations and then provide the pre-created table as the results table.
  * Make sure the results table is in the same location as the source table.
  * If VPC-SC is configured on the project, then the results table must be in the same VPC-SC perimeter as the source table.
  * If the table is modified during the scan execution stage, then the current running job exports to the previous results table and the table change takes effect from the next scan job.
  * Don't modify the table schema. If you need customized columns, create a view upon the table.
  * To reduce costs, set an expiration on the partition based on your use case. For more information, see how to [set the partition expiration](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#partition-expiration).



## Run a data quality scan

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Click the data quality scan to run.

  3. Click **Run now**.




### gcloud

To run a data quality scan, use the [`gcloud dataplex datascans run` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/datascans/run):
    
    
    gcloud dataplex datascans run DATASCAN \
    --location=LOCATION \
    

Replace the following variables:

  * `LOCATION`: The Google Cloud region in which the data quality scan was created.
  * `DATASCAN`: The name of the data quality scan.



###  C# 

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    
    public sealed partial class GeneratedDataScanServiceClientSnippets
    {
        /// <summary>Snippet for RunDataScan</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void RunDataScanRequestObject()
        {
            // Create client
            [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html) dataScanServiceClient = [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html#Google_Cloud_Dataplex_V1_DataScanServiceClient_Create)();
            // Initialize request argument(s)
            [RunDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.RunDataScanRequest.html) request = new [RunDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.RunDataScanRequest.html)
            {
                DataScanName = [DataScanName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName.html).[FromProjectLocationDataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName.html#Google_Cloud_Dataplex_V1_DataScanName_FromProjectLocationDataScan_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATASCAN]"),
            };
            // Make the request
            [RunDataScanResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.RunDataScanResponse.html) response = dataScanServiceClient.[RunDataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html#Google_Cloud_Dataplex_V1_DataScanServiceClient_RunDataScan_Google_Cloud_Dataplex_V1_DataScanName_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

###  Go 

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewDataScanClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_DataScanClient_NewDataScanClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.RunDataScanRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#RunDataScanRequest.
    	}
    	resp, err := c.RunDataScan(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

###  Java 

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[DataScanName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanName.html);
    import com.google.cloud.dataplex.v1.[DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html);
    import com.google.cloud.dataplex.v1.[RunDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunDataScanRequest.html);
    import com.google.cloud.dataplex.v1.[RunDataScanResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunDataScanResponse.html);
    
    public class SyncRunDataScan {
    
      public static void main(String[] args) throws Exception {
        syncRunDataScan();
      }
    
      public static void syncRunDataScan() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html) dataScanServiceClient = [DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html).create()) {
          [RunDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunDataScanRequest.html) request =
              [RunDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunDataScanRequest.html).newBuilder()
                  .setName([DataScanName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanName.html).of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString())
                  .build();
          [RunDataScanResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunDataScanResponse.html) response = dataScanServiceClient.runDataScan(request);
        }
      }
    }

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_run_data_scan():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataScanServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_scan_service.DataScanServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[RunDataScanRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.RunDataScanRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[run_data_scan](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_scan_service.DataScanServiceClient.html#google_cloud_dataplex_v1_services_data_scan_service_DataScanServiceClient_run_data_scan)(request=request)
    
        # Handle the response
        print(response)
    
    

###  Ruby 

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the run_data_scan call in the DataScanService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::DataScanService::Client#run_data_scan.
    #
    def run_data_scan
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::DataScanService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::RunDataScanRequest.new
    
      # Call the run_data_scan method.
      result = client.run_data_scan request
    
      # The returned object is of type Google::Cloud::Dataplex::V1::RunDataScanResponse.
      p result
    end

### REST

To run a data quality scan, use the [`dataScans.run` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/run).

### Airflow

To run a data quality scan using a Directed Acyclic Graph (DAG) in [Managed Service for Apache Airflow (Cloud Composer)](https://docs.cloud.google.com/composer/docs), use the [`DataplexRunDataQualityScanOperator`](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataplex/index.html#airflow.providers.google.cloud.operators.dataplex.DataplexRunDataQualityScanOperator):
    
    
    from datetime import datetime
    from airflow import DAG
    from airflow.providers.google.cloud.operators.dataplex import DataplexRunDataQualityScanOperator
    
    with DAG(
      "dataplex_auto_dq_scan",
      start_date=datetime(2026, 1, 1),
      schedule_interval="@daily",
      catchup=False,
    ) as dag:
    
      run_dq_scan = DataplexRunDataQualityScanOperator(
          task_id="run_dataplex_dq_scan",
          project_id="PROJECT_ID",
          region="REGION",
          data_scan_id="DATASCAN_ID",
      )
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `REGION`: The Google Cloud region in which the data quality scan was created.
  * `DATASCAN_ID`: The ID of your data quality scan.



**Note:** Run isn't supported for data quality scans that are on a one-time schedule.

## Cancel a data quality scan job

If a data quality scan job is running longer than expected or was started with an incorrect configuration, you can cancel it. This is a best-effort operation. If the job is already in a terminal state (such as `SUCCEEDED` or `FAILED`), the cancellation request is ignored.

### Required roles and permissions

To get the permissions that you need to cancel a data quality scan job, ask your administrator to grant you the [Dataplex Editor](https://docs.cloud.google.com/iam/docs/understanding-roles#dataplex.editor) (`roles/dataplex.editor`) or [Dataplex DataScan Administrator](https://docs.cloud.google.com/iam/docs/understanding-roles#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`) IAM role on your project.

### Cancel a job

You can cancel a running or pending data quality scan job by using the REST API.

### Console

  1. In the Google Cloud console, go to the **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/data-profiling-and-quality)

  2. Click the name of the data quality scan that contains the job you want to cancel.

  3. In the **Job history** tab, locate the job with a status of **Running** or **Pending**.

  4. Click **Cancel** associated with the job.




### REST

Use the [`projects.locations.dataScans.jobs.cancel`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans.jobs/cancel) method.
    
    
    POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/dataScans/DATASCAN_ID/jobs/JOB_ID:cancel
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the region where the data scan is located.
  * `DATASCAN_ID`: the ID of the data scan.
  * `JOB_ID`: the ID of the job to cancel.



## View the data quality scan results

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Click the name of a data quality scan.

     * The **Overview** section displays information about the most recent jobs, including when the scan was run, the number of records scanned in each job, whether all the data quality checks passed, and if there were failures, the number of data quality checks that failed.

     * The **Data quality scan configuration** section displays details about the scan.

  3. To see detailed information about a job, such as data quality scores that indicate the percentage of rules that passed, which rules failed, and the job logs, click the **Jobs history** tab. Then, click a job ID.


**Note:** If you exported the scan results to a BigQuery table, then you can also access the scan results from the table. The data quality scores are available if you published the scan results as Knowledge Catalog metadata.

### gcloud

To view the results of a data quality scan job, use the [`gcloud dataplex datascans jobs describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/datascans/jobs/describe):
    
    
    gcloud dataplex datascans jobs describe JOB \
    --location=LOCATION \
    --datascan=DATASCAN \
    --view=FULL
    

Replace the following variables:

  * `JOB`: The job ID of the data quality scan job.
  * `LOCATION`: The Google Cloud region in which the data quality scan was created.
  * `DATASCAN`: The name of the data quality scan the job belongs to.
  * `--view=FULL`: To see the scan job result, specify `FULL`.



###  C# 

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    
    public sealed partial class GeneratedDataScanServiceClientSnippets
    {
        /// <summary>Snippet for GetDataScan</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void GetDataScanRequestObject()
        {
            // Create client
            [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html) dataScanServiceClient = [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html#Google_Cloud_Dataplex_V1_DataScanServiceClient_Create)();
            // Initialize request argument(s)
            [GetDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetDataScanRequest.html) request = new [GetDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetDataScanRequest.html)
            {
                DataScanName = [DataScanName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName.html).[FromProjectLocationDataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName.html#Google_Cloud_Dataplex_V1_DataScanName_FromProjectLocationDataScan_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATASCAN]"),
                View = [GetDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetDataScanRequest.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetDataScanRequest.Types.html).[DataScanView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetDataScanRequest.Types.DataScanView.html).[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetDataScanRequest.Types.DataScanView.html#Google_Cloud_Dataplex_V1_GetDataScanRequest_Types_DataScanView_Unspecified),
            };
            // Make the request
            [DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.html) response = dataScanServiceClient.[GetDataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html#Google_Cloud_Dataplex_V1_DataScanServiceClient_GetDataScan_Google_Cloud_Dataplex_V1_DataScanName_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

###  Go 

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewDataScanClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_DataScanClient_NewDataScanClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.GetDataScanRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#GetDataScanRequest.
    	}
    	resp, err := c.GetDataScan(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

###  Java 

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan.html);
    import com.google.cloud.dataplex.v1.[DataScanName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanName.html);
    import com.google.cloud.dataplex.v1.[DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html);
    import com.google.cloud.dataplex.v1.[GetDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataScanRequest.html);
    
    public class SyncGetDataScan {
    
      public static void main(String[] args) throws Exception {
        syncGetDataScan();
      }
    
      public static void syncGetDataScan() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html) dataScanServiceClient = [DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html).create()) {
          [GetDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataScanRequest.html) request =
              [GetDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataScanRequest.html).newBuilder()
                  .setName([DataScanName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanName.html).of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString())
                  .build();
          [DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan.html) response = dataScanServiceClient.getDataScan(request);
        }
      }
    }

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_get_data_scan():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataScanServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_scan_service.DataScanServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[GetDataScanRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.GetDataScanRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_data_scan](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_scan_service.DataScanServiceClient.html#google_cloud_dataplex_v1_services_data_scan_service_DataScanServiceClient_get_data_scan)(request=request)
    
        # Handle the response
        print(response)
    
    

###  Ruby 

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the get_data_scan call in the DataScanService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::DataScanService::Client#get_data_scan.
    #
    def get_data_scan
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::DataScanService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::GetDataScanRequest.new
    
      # Call the get_data_scan method.
      result = client.get_data_scan request
    
      # The returned object is of type Google::Cloud::Dataplex::V1::DataScan.
      p result
    end

### REST

To view the results of a data quality scan, use the [`dataScans.get` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/get).

### View published results

If the data quality scan results are published as Knowledge Catalog metadata, then you can see the latest scan results on the BigQuery and Knowledge Catalog pages in the Google Cloud console, on the source table's **Data quality** tab. 

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. Search for and then select the table.

  3. Click the **Data quality** tab.

The latest published results are displayed.

**Note:** Published results might not be available if a scan is running for the first time.



### View historical scan results

Knowledge Catalog saves the data quality scan history of the last 300 jobs or for the past year, whichever occurs first.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Click the name of a data quality scan.

  3. Click the **Jobs history** tab.

The **Jobs history** tab provides information about past jobs, such as the number of records scanned in each job, the job status, the time the job was run, and whether each rule passed or failed.

  4. To view detailed information about a job, click any of the jobs in the **Job ID** column.




### gcloud

To view historical data quality scan jobs, use the [`gcloud dataplex datascans jobs list` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/datascans/jobs/list):
    
    
    gcloud dataplex datascans jobs list \
    --location=LOCATION \
    --datascan=DATASCAN \
    

Replace the following variables:

  * `LOCATION`: The Google Cloud region in which the data quality scan was created.
  * `DATASCAN`: The name of the data quality scan to view historical jobs for.



###  C# 

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using System;
    
    public sealed partial class GeneratedDataScanServiceClientSnippets
    {
        /// <summary>Snippet for ListDataScanJobs</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void ListDataScanJobsRequestObject()
        {
            // Create client
            [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html) dataScanServiceClient = [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html#Google_Cloud_Dataplex_V1_DataScanServiceClient_Create)();
            // Initialize request argument(s)
            [ListDataScanJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScanJobsRequest.html) request = new [ListDataScanJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScanJobsRequest.html)
            {
                ParentAsDataScanName = [DataScanName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName.html).[FromProjectLocationDataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName.html#Google_Cloud_Dataplex_V1_DataScanName_FromProjectLocationDataScan_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATASCAN]"),
                Filter = "",
            };
            // Make the request
            PagedEnumerable<ListDataScanJobsResponse, DataScanJob> response = dataScanServiceClient.[ListDataScanJobs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html#Google_Cloud_Dataplex_V1_DataScanServiceClient_ListDataScanJobs_Google_Cloud_Dataplex_V1_DataScanName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Iterate over all response items, lazily performing RPCs as required
            foreach ([DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob.html) item in response)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
    
            // Or iterate over pages (of server-defined size), performing one RPC per page
            foreach ([ListDataScanJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListDataScanJobsResponse.html) page in response.AsRawResponses())
            {
                // Do something with each page of items
                Console.WriteLine("A page of results:");
                foreach ([DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob.html) item in page)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
            }
    
            // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
            int pageSize = 10;
            Page<DataScanJob> singlePage = response.ReadPage(pageSize);
            // Do something with the page of items
            Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
            foreach ([DataScanJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanJob.html) item in singlePage)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
            // Store the pageToken, for when the next page is required.
            string nextPageToken = singlePage.NextPageToken;
        }
    }

###  Go 

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewDataScanClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_DataScanClient_NewDataScanClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.ListDataScanJobsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#ListDataScanJobsRequest.
    	}
    	it := c.ListDataScanJobs(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*dataplexpb.ListDataScanJobsResponse)
    	}
    }
    

###  Java 

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[DataScanJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanJob.html);
    import com.google.cloud.dataplex.v1.[DataScanName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanName.html);
    import com.google.cloud.dataplex.v1.[DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html);
    import com.google.cloud.dataplex.v1.[ListDataScanJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataScanJobsRequest.html);
    
    public class SyncListDataScanJobs {
    
      public static void main(String[] args) throws Exception {
        syncListDataScanJobs();
      }
    
      public static void syncListDataScanJobs() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html) dataScanServiceClient = [DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html).create()) {
          [ListDataScanJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataScanJobsRequest.html) request =
              [ListDataScanJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataScanJobsRequest.html).newBuilder()
                  .setParent([DataScanName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanName.html).of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString())
                  .setPageSize(883849137)
                  .setPageToken("pageToken873572522")
                  .setFilter("filter-1274492040")
                  .build();
          for ([DataScanJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanJob.html) element : dataScanServiceClient.listDataScanJobs(request).iterateAll()) {
            // doThingsWith(element);
          }
        }
      }
    }

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_list_data_scan_jobs():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataScanServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_scan_service.DataScanServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[ListDataScanJobsRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListDataScanJobsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_data_scan_jobs](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_scan_service.DataScanServiceClient.html#google_cloud_dataplex_v1_services_data_scan_service_DataScanServiceClient_list_data_scan_jobs)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    
    

###  Ruby 

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the list_data_scan_jobs call in the DataScanService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::DataScanService::Client#list_data_scan_jobs.
    #
    def list_data_scan_jobs
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::DataScanService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::ListDataScanJobsRequest.new
    
      # Call the list_data_scan_jobs method.
      result = client.list_data_scan_jobs request
    
      # The returned object is of type Gapic::PagedEnumerable. You can iterate
      # over elements, and API calls will be issued to fetch pages as needed.
      result.each do |item|
        # Each element is of type ::Google::Cloud::Dataplex::V1::DataScanJob.
        p item
      end
    end

### REST

To view historical data quality scan jobs, use the [`dataScans.jobs.list` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans.jobs/list).

### Job statuses

Data scan jobs can have the following statuses:

  * **`PENDING`** : the job is created but hasn't started running. In this state, the scan actively sets up infrastructure or acquires slots. This phase can take 10 to 20 seconds or more, depending on schema complexity and resource contention.

  * **`RUNNING`** : the job is running.

  * **`CANCELING`** : the job is canceling.

  * **`CANCELLED`** : the job is successfully canceled.

  * **`SUCCEEDED`** : the job completes successfully. The completion status might lag the actual query completion by up to 60 seconds because of post-processing steps, such as aggregation and metadata synchronization.

  * **`FAILED`** : the job fails because of an error. The completion status might lag the actual query completion by up to 60 seconds because of post-processing steps, such as aggregation and metadata synchronization.

  * **`SUCCEEDED_WITH_ERRORS`** : the job completes successfully, but some errors occur during execution.




#### Monitoring best practices

When you monitor your data scan jobs, keep the following best practices in mind:

  * **Avoid aggressive polling** : avoid aggressive polling (for example, calling `GetJob` or equivalent every 1 to 5 seconds). Aggressive polling wastes API quota and does not accelerate state transitions.

  * **Use exponential backoff** : if repetitive polling is unavoidable, use exponential backoff starting at 10 to 15 seconds.

  * **Use asynchronous event-driven decoupling (Recommended)** : instead of synchronous API polling, use Eventarc triggers that listen to Cloud Audit Logs (`cloudaudit.googleapis.com`). You can use these triggers to initiate downstream workflows immediately upon DataScan job completion events. This approach bypasses API polling limits, conserves quota, and reduces perceived latency.




## Grant access to data quality scan results

To enable the users in your organization to view the scan results, do the following:

  1. In the Google Cloud console, go to the Knowledge Catalog **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Click the data quality scan you want to share the results of.

  3. Click the **Permissions** tab.

  4. Do the following:

     * To grant access to a principal, click person_add **Grant access**. Grant the **Dataplex DataScan DataViewer** role to the associated principal.
     * To remove access from a principal, select the principal that you want to remove the **Dataplex DataScan DataViewer** role from. Click person_remove **Remove access** , and then confirm when prompted.



## Set alerts in Logging

To set alerts for data quality failures using the logs in Cloud Logging, follow these steps:

### Console

  1. In the Google Cloud console, go to the Logging **Logs Explorer**.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** window, enter your query. See sample queries.

  3. Click **Run query**.

  4. Click **Create alert**. This opens a side panel.

  5. Enter your alert policy name and click **Next**.

  6. Review the query.

     1. Click **Preview logs** to test your query. This shows logs with matching conditions.

     2. Click **Next**.

  7. Set the time between notifications and click **Next**.

  8. Define who should be notified for the alert and click **Save** to create the alert policy.




Alternatively, you can configure and edit your alerts by navigating in the Google Cloud console to **Monitoring** > **Alerting**.

### gcloud

Not supported.

### REST

Learn how to [set alerts in Logging](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-by-api).

### Sample queries for setting job level or dimension level alerts

  * A sample query to set alerts on overall data quality failures for a data quality scan:
        
        resource.type="dataplex.googleapis.com/DataScan"
        AND labels."dataplex.googleapis.com/data_scan_state"="SUCCEEDED"
        AND resource.labels.resource_container="projects/112233445566"
        AND resource.labels.datascan_id="a0-test-dec6-dq-3"
        AND NOT jsonPayload.dataQuality.passed=true
        

  * A sample query to set alerts on data quality failures for a dimension (for example, uniqueness) of a given data quality scan:
        
        resource.type="dataplex.googleapis.com/DataScan"
        AND labels."dataplex.googleapis.com/data_scan_state"="SUCCEEDED"
        AND resource.labels.resource_container="projects/112233445566"
        AND resource.labels.datascan_id="a0-test-dec6-dq-3"
        AND jsonPayload.dataQuality.dimensionPassed.UNIQUENESS=false
        

  * A sample query to set alerts on data quality failures for a table.

    * Set alerts on data quality failures for a BigQuery table that isn't organized in a Knowledge Catalog lake:
          
          resource.type="dataplex.googleapis.com/DataScan"
          AND jsonPayload.dataSource="//bigquery.googleapis.com/projects/test-project/datasets/testdataset/table/chicago_taxi_trips"
          AND labels."dataplex.googleapis.com/data_scan_state"="SUCCEEDED"
          AND resource.labels.resource_container="projects/112233445566"
          AND NOT jsonPayload.dataQuality.passed=true
          

    * Set alerts on data quality failures for a BigQuery table that's organized in a Knowledge Catalog lake:
          
          resource.type="dataplex.googleapis.com/DataScan"
          AND jsonPayload.dataSource="projects/test-project/datasets/testdataset/table/chicago_taxi_trips"
          AND labels."dataplex.googleapis.com/data_scan_state"="SUCCEEDED"
          AND resource.labels.resource_container="projects/112233445566"
          AND NOT jsonPayload.dataQuality.passed=true
          




### Sample queries to set per rule alerts

  * A sample query to set alerts on all failing data quality rules with the specified custom rule name for a data quality scan:
        
        resource.type="dataplex.googleapis.com/DataScan"
        AND jsonPayload.ruleName="custom-name"
        AND jsonPayload.result="FAILED"
        

  * A sample query to set alerts on all failing data quality rules of a specific evaluation type for a data quality scan:
        
        resource.type="dataplex.googleapis.com/DataScan"
        AND jsonPayload.evalutionType="PER_ROW"
        AND jsonPayload.result="FAILED"
        

  * A sample query to set alerts on all failing data quality rules for a column in the table used for a data quality scan:
        
        resource.type="dataplex.googleapis.com/DataScan"
        AND jsonPayload.column="CInteger"
        AND jsonPayload.result="FAILED"
        




## Troubleshoot a data quality failure

For each job with row-level rules that fail, Knowledge Catalog provides a query to get the failed records. Run this query to see the records that did not match your rule.

**Note:** The query returns all of the columns of the table, not just the failed column.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Click the name of the data quality scan whose records you want to troubleshoot.

  3. Click the **Jobs history** tab.

  4. Click the job ID of the job that identified data quality failures.

  5. In the job results window that opens, in the **Rules** section, find the column **Query to get failed records**. Click **Copy query to clipboard** for the failed rule.

  6. [Run the query in BigQuery](https://docs.cloud.google.com/bigquery/docs/running-queries) to see the records that caused the job to fail.




### gcloud

Not supported.

### REST

  1. To get the job that identified the data quality failures, use the [`dataScans.get` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualityResult).

In the response object, the `failingRowsQuery` field shows the query.

  2. [Run the query in BigQuery](https://docs.cloud.google.com/bigquery/docs/running-queries) to see the records that caused the job to fail.




Knowledge Catalog also runs the debug query, provided it was included during the rule creation. The debug query results are included in each rule's output. This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

### Console

Not supported.

### gcloud

Not supported.

### REST

To get the job that identified the data quality failures, use the [`dataScans.get` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualityResult). In the response object, the `debugQueriesResultSets` field shows the results of the debug queries.

## Manage data quality scans for a specific table

The steps in this document show how to manage data profile scans across your project by using the Knowledge Catalog **Data profiling & quality** page in the Google Cloud console.

You can also create and manage data profile scans when working with a specific table. In the Google Cloud console, on the Knowledge Catalog page for the table, use the **Data quality** tab. Do the following:

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

Search for and then select the table. 

  2. Click the **Data quality** tab.

  3. Depending on whether the table has a data quality scan whose results are published as Knowledge Catalog metadata, you can work with the table's data quality scans in the following ways:

     * **Data quality scan results are published** : the latest scan results are displayed on the page.

To manage the data quality scans for this table, click **Data quality scan** , and then select from the following options:

       * **Create new scan** : create a new data quality scan. For more information, see the Create a data quality scan section of this document. When you create a scan from a table's details page, the table is preselected.

       * **Run now** : run the scan.

       * **Edit scan configuration** : edit settings including the display name, filters, and schedule.

To edit the data quality rules, on the **Data quality** tab, click the **Rules** tab. Click **Modify rules**. Update the rules and then click **Save**.

       * **Manage scan permissions** : control who can access the scan results. For more information, see the Grant access to data quality scan results section of this document.

       * **View historical results** : view detailed information about previous data quality scan jobs. For more information, see the View data quality scan results and View historical scan results sections of this document.

       * **View all scans** : view a list of data quality scans that apply to this table.

     * **Data quality scan results aren't published** : select from the following options:

       * **Create data quality scan** : create a new data quality scan. For more information, see the Create a data quality scan section of this document. When you create a scan from a table's details page, the table is preselected.

       * **View existing scans** : view a list of data quality scans that apply to this table.




## Update a data quality scan

You can edit various settings for an existing data quality scan, such as the display name, filters, schedule, and data quality rules.

**Note:** If an existing data quality scan publishes the results to the BigQuery and Knowledge Catalog pages in the Google Cloud console, and you instead want to publish future scan results as Knowledge Catalog metadata, you must edit the scan and re-enable publishing. You might need additional permissions to enable catalog publishing.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Click the name of a data quality scan.

  3. To edit settings including the display name, filters, and schedule, click **Edit**. Edit the values and then click **Save**.

  4. To edit the data quality rules, on the scan details page, click the **Current rules** tab. Click **Modify rules**. Update the rules and then click **Save**.




### gcloud

To update the description of a data quality scan, use the [`gcloud dataplex datascans update data-quality` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality):
    
    
    gcloud dataplex datascans update data-quality DATASCAN \
    --location=LOCATION \
    --description=DESCRIPTION
    

Replace the following:

  * `DATASCAN`: The name of the data quality scan to update.
  * `LOCATION`: The Google Cloud region in which the data quality scan was created.
  * `DESCRIPTION`: The new description for the data quality scan.

**Note:** You can update specification fields, such as `rules`, `rowFilter`, or `samplingPercent`, in the data quality specification file. Refer to [JSON](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec) and [YAML](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality#create-scan-using-gcloud) representations.

###  C# 

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedDataScanServiceClientSnippets
    {
        /// <summary>Snippet for UpdateDataScan</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void UpdateDataScanRequestObject()
        {
            // Create client
            [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html) dataScanServiceClient = [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html#Google_Cloud_Dataplex_V1_DataScanServiceClient_Create)();
            // Initialize request argument(s)
            [UpdateDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateDataScanRequest.html) request = new [UpdateDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateDataScanRequest.html)
            {
                DataScan = new [DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.html)(),
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)(),
                ValidateOnly = false,
            };
            // Make the request
            Operation<DataScan, OperationMetadata> response = dataScanServiceClient.[UpdateDataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html#Google_Cloud_Dataplex_V1_DataScanServiceClient_UpdateDataScan_Google_Cloud_Dataplex_V1_DataScan_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<DataScan, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<DataScan, OperationMetadata> retrievedResponse = dataScanServiceClient.[PollOnceUpdateDataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html#Google_Cloud_Dataplex_V1_DataScanServiceClient_PollOnceUpdateDataScan_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

###  Go 

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewDataScanClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_DataScanClient_NewDataScanClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.UpdateDataScanRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#UpdateDataScanRequest.
    	}
    	op, err := c.UpdateDataScan(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

###  Java 

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan.html);
    import com.google.cloud.dataplex.v1.[DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html);
    import com.google.cloud.dataplex.v1.[UpdateDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataScanRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    
    public class SyncUpdateDataScan {
    
      public static void main(String[] args) throws Exception {
        syncUpdateDataScan();
      }
    
      public static void syncUpdateDataScan() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html) dataScanServiceClient = [DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html).create()) {
          [UpdateDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataScanRequest.html) request =
              [UpdateDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataScanRequest.html).newBuilder()
                  .setDataScan([DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan.html).newBuilder().build())
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().build())
                  .setValidateOnly(true)
                  .build();
          [DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan.html) response = dataScanServiceClient.[updateDataScanAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html#com_google_cloud_dataplex_v1_DataScanServiceClient_updateDataScanAsync_com_google_cloud_dataplex_v1_DataScan_com_google_protobuf_FieldMask_)(request).get();
        }
      }
    }

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_update_data_scan():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataScanServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_scan_service.DataScanServiceClient.html)()
    
        # Initialize request argument(s)
        data_scan = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataScan](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DataScan.html)()
        data_scan.data.entity = "entity_value"
    
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[UpdateDataScanRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.UpdateDataScanRequest.html)(
            data_scan=data_scan,
        )
    
        # Make the request
        operation = client.[update_data_scan](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_scan_service.DataScanServiceClient.html#google_cloud_dataplex_v1_services_data_scan_service_DataScanServiceClient_update_data_scan)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

###  Ruby 

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the update_data_scan call in the DataScanService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::DataScanService::Client#update_data_scan.
    #
    def update_data_scan
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::DataScanService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::UpdateDataScanRequest.new
    
      # Call the update_data_scan method.
      result = client.update_data_scan request
    
      # The returned object is of type Gapic::Operation. You can use it to
      # check the status of an operation, cancel it, or wait for results.
      # Here is how to wait for a response.
      result.wait_until_done! timeout: 60
      if result.response?
        p result.response
      else
        puts "No response received."
      end
    end

### REST

To edit a data quality scan, use the [`dataScans.patch` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/patch).

**Note:** Update isn't supported for data quality scans that are on a one-time schedule.

## Delete a data quality scan

### Console

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Click the scan you want to delete.

  3. Click **Delete** , and then confirm when prompted.




### gcloud

### gcloud

To delete a data quality scan, use the [`gcloud dataplex datascans delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/datascans/delete):
    
    
    gcloud dataplex datascans delete DATASCAN \
    --location=LOCATION \
    --async
    

Replace the following variables:

  * `DATASCAN`: The name of the data quality scan to delete.
  * `LOCATION`: The Google Cloud region in which the data quality scan was created.



###  C# 

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedDataScanServiceClientSnippets
    {
        /// <summary>Snippet for DeleteDataScan</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void DeleteDataScanRequestObject()
        {
            // Create client
            [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html) dataScanServiceClient = [DataScanServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html#Google_Cloud_Dataplex_V1_DataScanServiceClient_Create)();
            // Initialize request argument(s)
            [DeleteDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteDataScanRequest.html) request = new [DeleteDataScanRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteDataScanRequest.html)
            {
                DataScanName = [DataScanName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName.html).[FromProjectLocationDataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanName.html#Google_Cloud_Dataplex_V1_DataScanName_FromProjectLocationDataScan_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATASCAN]"),
                Force = false,
            };
            // Make the request
            Operation<Empty, OperationMetadata> response = dataScanServiceClient.[DeleteDataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html#Google_Cloud_Dataplex_V1_DataScanServiceClient_DeleteDataScan_Google_Cloud_Dataplex_V1_DataScanName_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<Empty, OperationMetadata> retrievedResponse = dataScanServiceClient.[PollOnceDeleteDataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScanServiceClient.html#Google_Cloud_Dataplex_V1_DataScanServiceClient_PollOnceDeleteDataScan_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

###  Go 

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewDataScanClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_DataScanClient_NewDataScanClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.DeleteDataScanRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#DeleteDataScanRequest.
    	}
    	op, err := c.DeleteDataScan(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

###  Java 

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[DataScanName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanName.html);
    import com.google.cloud.dataplex.v1.[DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html);
    import com.google.cloud.dataplex.v1.[DeleteDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataScanRequest.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    
    public class SyncDeleteDataScan {
    
      public static void main(String[] args) throws Exception {
        syncDeleteDataScan();
      }
    
      public static void syncDeleteDataScan() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html) dataScanServiceClient = [DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html).create()) {
          [DeleteDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataScanRequest.html) request =
              [DeleteDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataScanRequest.html).newBuilder()
                  .setName([DataScanName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanName.html).of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString())
                  .[setForce](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataScanRequest.Builder.html#com_google_cloud_dataplex_v1_DeleteDataScanRequest_Builder_setForce_boolean_)(true)
                  .build();
          dataScanServiceClient.[deleteDataScanAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.html#com_google_cloud_dataplex_v1_DataScanServiceClient_deleteDataScanAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_DataScanName_)(request).get();
        }
      }
    }

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_delete_data_scan():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataScanServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_scan_service.DataScanServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DeleteDataScanRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DeleteDataScanRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_data_scan](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_scan_service.DataScanServiceClient.html#google_cloud_dataplex_v1_services_data_scan_service_DataScanServiceClient_delete_data_scan)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

###  Ruby 

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the delete_data_scan call in the DataScanService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::DataScanService::Client#delete_data_scan.
    #
    def delete_data_scan
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::DataScanService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::DeleteDataScanRequest.new
    
      # Call the delete_data_scan method.
      result = client.delete_data_scan request
    
      # The returned object is of type Gapic::Operation. You can use it to
      # check the status of an operation, cancel it, or wait for results.
      # Here is how to wait for a response.
      result.wait_until_done! timeout: 60
      if result.response?
        p result.response
      else
        puts "No response received."
      end
    end

### REST

### REST

To delete a data quality scan, use the [`dataScans.delete` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/delete).

**Note:** Delete isn't supported for data quality scans that are on a one-time schedule.

## What's next

  * Follow a tutorial to [build a policy-as-code data quality workflow](https://docs.cloud.google.com/knowledge-catalog/docs/build-policy-as-code-data-quality-workflow).
  * Follow a tutorial to [manage data quality rules as code with Terraform](https://docs.cloud.google.com/knowledge-catalog/docs/manage-data-quality-rules-as-code).
  * Learn about [data profiling](https://docs.cloud.google.com/knowledge-catalog/docs/data-profiling-overview).
  * Learn how to [use data profiling](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-profiling).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

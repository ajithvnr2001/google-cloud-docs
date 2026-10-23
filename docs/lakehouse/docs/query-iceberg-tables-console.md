---
url: https://docs.cloud.google.com/lakehouse/docs/query-iceberg-tables-console/
title: Quickstart: Create and query an Iceberg table in Lakehouse using the Google Cloud console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:52.963686+00:00
---

# Quickstart: Create and query an Iceberg table in Lakehouse using the Google Cloud console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/query-iceberg-tables-console/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and query an Iceberg table in Lakehouse using the Google Cloud console

In this quickstart, you use the Google Cloud console to learn how borderless Lakehouse lets you manage and share Apache Iceberg tables across Google Cloud and open-source engines by storing table metadata, including schemas, snapshots, and storage locations, in the Lakehouse runtime catalog.

To complete this quickstart, you perform the following steps in the Google Cloud console:

  1. **Create a Cloud Storage bucket** : Create a bucket in Cloud Storage to store your Iceberg table data and metadata files.
  2. **Create a catalog** : Create a multiple-bucket catalog in the Lakehouse runtime catalog backed by your bucket with credential vending enabled.
  3. **Create a namespace and an Iceberg table** : Use the **Lakehouse** page in the Google Cloud console to create a namespace and an Iceberg table with BigQuery data manipulation language (DML) enabled.
  4. **Modify data and query the table in BigQuery** : Use BigQuery DML statements (`INSERT`, `UPDATE`, and `DELETE`) to modify rows in the Iceberg table and query the results using the 4-part **P.C.N.T** (**Project.Catalog.Namespace.Table**) syntax, with no ETL or manual table registration needed.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the BigLake, Cloud Storage, and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com,storage.googleapis.com,bigquery.googleapis.com)

  5. Make sure that you have the following role or roles on the project: BigLake Admin (`roles/biglake.admin`), Storage Admin (`roles/storage.admin`), and BigQuery Job User (`roles/bigquery.jobUser`) 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the BigLake, Cloud Storage, and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com,storage.googleapis.com,bigquery.googleapis.com)

  9. Make sure that you have the following role or roles on the project: BigLake Admin (`roles/biglake.admin`), Storage Admin (`roles/storage.admin`), and BigQuery Job User (`roles/bigquery.jobUser`) 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 




## Create a Cloud Storage bucket

Create a Cloud Storage bucket in the Google Cloud console to store your Iceberg table data and metadata files:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click **Create**.

  3. In the **Get started** section, enter a globally unique bucket name (for example, `lakehouse-quickstart-UNIQUE_ID` or `PROJECT_ID-lakehouse`), and then click **Continue**.

  4. In the **Choose where to store your data** section, leave **Location type** set to **Multi-region** (**us (multiple regions in United States)**), and then click **Create**.

  5. If the **Public access will be prevented** dialog appears, click **Confirm**.




## Create a catalog in the Lakehouse runtime catalog

Create a multiple-bucket catalog in the Lakehouse runtime catalog for your Apache Iceberg tables. A multiple-bucket catalog lets you name your catalog independently of any bucket name and associate multiple Cloud Storage buckets with a single catalog. To secure access to these buckets, enable credential vending mode so that the catalog can automatically issue temporary storage credentials directly to your client engines.

  1. In the Google Cloud console, go to the **Lakehouse** page.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Click **Create catalog** and select **Lakehouse runtime catalog**.

  3. In the **Catalog details** section, configure the following settings:

     * **Catalog type** : Select **Iceberg Rest Catalog**.
     * **Lakehouse catalog bucket options** : Select **Multiple bucket catalog**.
     * **Default Catalog Cloud Storage path** : Click **Browse** , select the bucket that you created, and click **Select**.
     * **Catalog ID** : Enter `quickstart_catalog`.
     * **Primary location** : Select **Multi-region** , and then select **US (multiple regions in United States)**.
  4. Click **Continue** , and then in the **Data paths** section, click **Continue**.

  5. In the **Authentication method** section, select **Credential vending mode**.

With credential vending, the catalog securely issues temporary, table-scoped storage tokens to client engines and BigQuery, so external engines don't need direct IAM permissions on your bucket.

  6. Click **Create**.

Your catalog is created and the **Catalog details** page opens.

  7. Under **Authentication method** , click **Set bucket permissions** , and then in the dialog, click **Confirm**.

This step grants the catalog's service account the required permissions on your Cloud Storage bucket to vend temporary credentials.




## Create a namespace and an Iceberg table

Now that you have a catalog, use the **Lakehouse** page in the Google Cloud console to create a namespace and an Iceberg table.

### Create a namespace

  1. On the **Catalog Details** page for `quickstart_catalog`, click add_box **Create namespace**.

  2. In the **Namespace name** field, enter `quickstart_namespace`.

  3. Leave **Location** set to the default Cloud Storage path that's automatically populated in the field.

  4. Click **Create**.




### Create an Iceberg table

  1. On the **Catalog Details** page, click `quickstart_namespace`.

The **Namespace Details** page opens.

  2. Click add_box **Create Table**.

  3. In the **Create Table** pane, configure the following settings:

     * **Table format** : Verify that **Iceberg** is selected.
     * **Table name** : Enter `quickstart_table`.
     * **Location** : Leave the default Cloud Storage path.
  4. Under **Schema** , click **Add field** twice to add two columns to the table:

     * For the first field, enter `id` in the **Field name** field, and select **INTEGER** from the **Type** menu.
     * For the second field, enter `name` in the **Field name** field, and select **STRING** from the **Type** menu.
  5. Under **Properties** , find the predefined `gcp.biglake.bigquery-dml.enabled` property and change its **Value** from `false` to `true`. Leave `gcp.biglake.table-management.enabled` set to `false`.

Setting `gcp.biglake.bigquery-dml.enabled` to `true` lets you modify data in the Iceberg table using BigQuery DML statements such as `INSERT`, `UPDATE`, `DELETE`, and `MERGE`. For more information, see [Configure table options](https://docs.cloud.google.com/lakehouse/docs/table-options).

  6. Click **Create**.

Your new Iceberg table (`quickstart_table`) appears on the **Namespace details** page, and the Lakehouse runtime catalog writes the initial Iceberg metadata file to your Cloud Storage bucket.




## Modify data and query the table in BigQuery

With `quickstart_table` created and BigQuery DML enabled, you can insert, update, delete, and query rows directly in BigQuery using the 4-part **P.C.N.T** (**Project.Catalog.Namespace.Table**) syntax. In each statement, replace `PROJECT_ID` with your Google Cloud project ID:

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, click add_box **SQL query**.

  3. Insert three rows of sample data:
         
         INSERT INTO `PROJECT_ID.quickstart_catalog.quickstart_namespace.quickstart_table` (id, name)
         VALUES (1, 'one'), (2, 'two'), (3, 'three');

Click **Run**. When the `INSERT` statement completes, BigQuery writes the Parquet data files to your Cloud Storage bucket and commits a new Iceberg snapshot to the Lakehouse runtime catalog.

  4. Modify a row in the table:
         
         UPDATE `PROJECT_ID.quickstart_catalog.quickstart_namespace.quickstart_table`
         SET name = 'updated'
         WHERE id = 1;

Click **Run**.

  5. Delete a row from the table:
         
         DELETE FROM `PROJECT_ID.quickstart_catalog.quickstart_namespace.quickstart_table`
         WHERE id = 3;

Click **Run**.

  6. Query the table to verify your changes:
         
         SELECT * FROM `PROJECT_ID.quickstart_catalog.quickstart_namespace.quickstart_table`
         ORDER BY id;

Click **Run**. The **Query results** pane shows the remaining two rows, including the updated value for `id = 1`:
         
         +----+---------+
         | id | name    |
         +----+---------+
         |  1 | updated |
         |  2 | two     |
         +----+---------+
         




Because the Lakehouse runtime catalog manages the Iceberg metadata and credential vending is enabled, you can also read from or write to `quickstart_table` using any Iceberg-compatible open-source engine, such as Apache Spark, Trino, or Apache Flink, without granting them direct IAM access to your bucket.

## Clean up

To avoid incurring unnecessary charges to your Google Cloud account, delete the resources you created in this quickstart. Deleting the table, namespace, and catalog removes the metadata registration from the Lakehouse runtime catalog, while deleting the bucket removes the underlying Parquet data and Iceberg metadata files stored in Cloud Storage:

  1. In the Google Cloud console, go to the **Lakehouse** page.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Delete the table from your catalog:

     1. Click `quickstart_catalog`, and then click `quickstart_namespace`.
     2. In the **Namespace details** table, in the row for `quickstart_table`, click more_vert **More > Delete**.
     3. Enter `DELETE` to confirm and click **Delete**.
  3. Delete the namespace from your catalog:

     1. Return to the **Catalog details** page for `quickstart_catalog`.
     2. In the row for `quickstart_namespace`, click more_vert **More namespace actions > Delete**.
     3. Enter `DELETE` to confirm and click **Delete**.
  4. Delete your catalog:

     1. Return to the **Lakehouse** page.
     2. In the row for `quickstart_catalog`, click more_vert **More catalog actions > Delete**.
     3. Enter `DELETE` to confirm and click **Delete**.
  5. Delete your Cloud Storage bucket and all its contents:

     1. Go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Select the checkbox next to the bucket that you created for this quickstart and click **Delete**.

     3. Enter `DELETE` to confirm and click **Delete**.




## What's next

  * Try the [Create and query an Iceberg table using the Google Cloud CLI quickstart](https://docs.cloud.google.com/lakehouse/docs/query-iceberg-tables-with-lakehouse).
  * Learn how to [modify data with BigQuery DML statements](https://docs.cloud.google.com/lakehouse/docs/modify-data-dml) and [configure table options](https://docs.cloud.google.com/lakehouse/docs/table-options).
  * Try the [Set up cross-cloud data access codelab](https://docs.cloud.google.com/lakehouse/docs/cross-cloud-data-access-codelab) to query data across Amazon Web Services (AWS), AlloyDB for PostgreSQL, and Cloud Storage without ETL.
  * Learn about [multiple-bucket catalogs](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint#storage-multiple-buckets) and the [Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint).
  * Learn how to [manage catalogs in the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/manage-catalogs).
  * Learn about [Apache Iceberg tables managed by Lakehouse](https://docs.cloud.google.com/lakehouse/docs/lakehouse-tables).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

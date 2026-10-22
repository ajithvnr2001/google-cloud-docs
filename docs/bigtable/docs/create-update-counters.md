---
url: https://docs.cloud.google.com/bigtable/docs/create-update-counters/
title: Quickstart: Create and update counters in Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:16.840212+00:00
---

# Quickstart: Create and update counters in Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/create-update-counters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and update counters in Bigtable

Learn how to create and update counters in Bigtable using _aggregates_ , table cells that aggregate values at write time. This quickstart uses the Google Cloud console, the Google Cloud CLI, or the `cbt` CLI to create the following counters:

  * A counter that keeps a running sum
  * A counter that keeps track of the minimum of all added values
  * A counter that keeps track of the maximum of all added values



## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. After initializing the gcloud CLI, update it and install the required components: 
         
         gcloud components update
         gcloud components install cbt

  6. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Cloud Bigtable API and Cloud Bigtable Admin API APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable bigtable.googleapis.com bigtableadmin.googleapis.com

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. After initializing the gcloud CLI, update it and install the required components: 
         
         gcloud components update
         gcloud components install cbt

  13. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Cloud Bigtable API and Cloud Bigtable Admin API APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable bigtable.googleapis.com bigtableadmin.googleapis.com

  16. Run the following commands to ensure that the gcloud CLI is up to date and includes the `cbt` CLI : 
         
         gcloud components update
         
         gcloud components install cbt




## Create a Bigtable instance

###  Console 

  1. In the Google Cloud console, go to the **Create instance** page.

[Go to Create instance](https://console.cloud.google.com/bigtable/create-instance)

  2. In the **Instance name** field, enter `Counters quickstart instance`.

  3. In the **Instance ID** field, enter `counters-quickstart-instance`.

  4. Click **Continue**.

  5. In the **Select your edition** section, select **Enterprise**.

  6. Click **Continue**.

  7. In the **Storage type** section, select **SSD**.

  8. Click **Continue**.

  9. In the **Cluster ID** field, enter `counters-quickstart-cluster`.

  10. In the **Region** list, select **us-east1 (South Carolina)**.

  11. In the **Zone** list, select **us-east1-c**.

  12. In the node scaling section, select **Autoscaling** , and then do the following:

     1. For the minimum number of nodes, enter `1`.
     2. For the maximum number of nodes, enter `3`.
  13. Click **Create** to create the instance.




###  gcloud 

  1. Use the [`bigtable instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/create) to create an instance.
         
         gcloud bigtable instances create counters-quickstart-instance \
             --display-name="Counters quickstart instance" \
             --edition=ENTERPRISE \
             --cluster-config=id="counters-quickstart-cluster",zone="us-east1-c"
         




## Connect to your instance

  1. Configure the `cbt` CLI to use your project and instance by creating a `.cbtrc` file.
         
         echo project = PROJECT_ID >> ~/.cbtrc && echo instance = counters-quickstart-instance >> ~/.cbtrc
         

Replace PROJECT_ID with the ID of the project that you are using.

  2. Verify that you set up the `.cbtrc` file correctly.
         
         cat ~/.cbtrc
         

The terminal displays the contents of the `.cbtrc` file, which looks similar to the following:
         
         project = PROJECT_ID
         instance = counters-quickstart-instance

Now you can use the `cbt` CLI with your instance.




## Create a table with aggregate column families

###  Console 

  1. In the left navigation pane of the Google Cloud console, click **Tables**.

  2. Click add_box **Create table**.

  3. In the **Table ID** field, enter `counters_quickstart_table`.

  4. Under **Column families** , for each column family that you want to add, click **Add a column family** and enter the following settings:

     * **`sum_family`** :

       1. In the **Column family name** field, enter `sum_family`.
       2. In the **Column family type** section, select **Aggregate**.
       3. In the **Aggregator** list, select **Sum**.
       4. In the **Set garbage collection policy** section, select **Never collect garbage**.
       5. Click **Done**.
     * **`min_family`** :

       1. In the **Column family name** field, enter `min_family`.
       2. In the **Column family type** section, select **Aggregate**.
       3. In the **Aggregator** list, select **Min**.
       4. In the **Set garbage collection policy** section, select **Never collect garbage**.
       5. Click **Done**.
     * **`max_family`** :

       1. In the **Column family name** field, enter `max_family`.
       2. In the **Column family type** section, select **Aggregate**.
       3. In the **Aggregator** list, select **Max**.
       4. In the **Set garbage collection policy** section, select **Never collect garbage**.
       5. Click **Done**.
  5. Click **Create**.

  6. To view your new column families and their aggregate configurations:

     1. In the navigation menu, click **Bigtable Studio**.
     2. In the **Object Explorer** tree on the left, expand **Tables** , then expand `counters_quickstart_table`, and then expand **Column Families**. **Note** : Aggregate column families have a functions function icon and an aggregation type, such as `Sum`. To view the details of an aggregate column family, hover over its name. 



###  cbt 

  1. Use the [`cbt createtable`](https://docs.cloud.google.com/bigtable/docs/cbt-reference#create_a_table) command to create a table named `counters_quickstart_table` that has three aggregate column families. Configure each column family with a different aggregation type:

     * Column family `max_family` is of type `Max` with an input type of `Int64`.
     * Column family `min_family` is of type `Min` with an input type of `Int64`.
     * Column family `sum_family` is of type `Sum` with an input type of `Int64`.
    
    cbt createtable counters_quickstart_table families=sum_family:never:intsum,min_family:never:intmin,max_family:never:intmax
    

  2. List your column families by running the [`cbt ls`](https://docs.cloud.google.com/bigtable/docs/cbt-reference#list_tables_and_column_families) command.
         
         cbt ls counters_quickstart_table
         

The shell displays output similar to the following:
         
         Family Name     GC Policy
         -----------     ---------
         max_family      <never>
         min_family      <never>
         sum_family      <never>
         




## Create counters in the table

  1. Use the [`cbt addtocell`](https://docs.cloud.google.com/bigtable/docs/cbt-reference#add_a_value_to_an_aggregate_cell_write) command to write an initial value of `5` to a new column in each of the three column families, using a row key of `row-key1` and a timestamp of `0`. This operation creates aggregate cells, which you use as counters.
         
         cbt addtocell counters_quickstart_table row-key1 sum_family:sum_column=5@0
         cbt addtocell counters_quickstart_table row-key1 min_family:min_column=5@0
         cbt addtocell counters_quickstart_table row-key1 max_family:max_column=5@0
         




## Read the data

You can read the data from your table by querying it with SQL in the Google Cloud console or by using the `cbt` CLI .

### Query the table in the Google Cloud console with SQL

  1. In the Google Cloud console, open the **Bigtable instances** page.

[Go to instances list](https://console.cloud.google.com/bigtable)

  2. Select `counters-quickstart-instance` from the list.

  3. In the navigation menu, click **Bigtable Studio**.

  4. Click the **Editor** tab.

  5. Paste this query into the editor:
         
         SELECT * FROM `counters_quickstart_table`
         

  6. Click **Run**. The query results appear in the **Results** table and look similar to the following:

_key | max_family | min_family | sum_family  
---|---|---|---  
row-key1 | { "max_column": 5 } | { "min_column": 5 } | { "sum_column": 5 }  



### Read with `cbt` CLI 

  1. To view the counter values as integers rather than bytes, define a YAML file the `cbt` CLI can use to format the output. Run the following:
         
         echo "families:" > ~/cbtformat.yaml
         echo "  max_family:" >> ~/cbtformat.yaml
         echo "    default_encoding: BigEndian" >> ~/cbtformat.yaml
         echo "    default_type: INT64" >> ~/cbtformat.yaml
         echo "  min_family:" >> ~/cbtformat.yaml
         echo "    default_encoding: BigEndian" >> ~/cbtformat.yaml
         echo "    default_type: INT64" >> ~/cbtformat.yaml
         echo "  sum_family:" >> ~/cbtformat.yaml
         echo "    default_encoding: BigEndian" >> ~/cbtformat.yaml
         echo "    default_type: INT64" >> ~/cbtformat.yaml
         

  2. Verify that you set up the `cbtformat.yaml` file correctly.
         
         cat ~/cbtformat.yaml
         

The terminal displays the contents of the `cbtformat.yaml` file, which looks similar to the following:
         
         families:
           max_family:
             default_encoding: BigEndian
             default_type: INT64
           min_family:
             default_encoding: BigEndian
             default_type: INT64
           sum_family:
             default_encoding: BigEndian
             default_type: INT64
         

  3. Use the [`cbt read`](https://docs.cloud.google.com/bigtable/docs/cbt-reference#read_rows) command to pass the YAML file and read the data you added to the table. The table now has three columns, each with a different aggregation type.
         
         cbt read counters_quickstart_table format-file=$HOME/cbtformat.yaml
         

The shell displays output similar to the following. The values are formatted as integers, and the timestamps are in UTC format.
         
         row-key1
           max_family:max_column                    @ 1970/01/01-00:00:00.000000
             5
           min_family:min_column                    @ 1970/01/01-00:00:00.000000
             5
           sum_family:sum_column                    @ 1970/01/01-00:00:00.000000
             5
         




## Update the counters

  1. Add a value of 3 to each column in the table, using the **same timestamps** that you used when you created the cells. In each column, the cell value is merged with the existing value based on the cell's aggregation type.
         
         cbt addtocell counters_quickstart_table row-key1 sum_family:sum_column=3@0
         cbt addtocell counters_quickstart_table row-key1 min_family:min_column=3@0
         cbt addtocell counters_quickstart_table row-key1 max_family:max_column=3@0
         

  2. Use the `cbt read` command again to read the data in the table. Each cell now contains an aggregated value.
         
         cbt read counters_quickstart_table format-file=$HOME/cbtformat.yaml
         

The `sum_column` contains the sum of 5 and 3 (8), `min_column` contains the minimum of the two values that were written to it (3), and `max_column` contains the maximum of the two values that were written to it (5).
         
         row-key1
           max_family:max_column                    @ 1970/01/01-00:00:00.000000
             5
           min_family:min_column                    @ 1970/01/01-00:00:00.000000
             3
           sum_family:sum_column                    @ 1970/01/01-00:00:00.000000
             8
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

###  Console 

  1. Delete the `counters_quickstart_table` table:

     1. In the Google Cloud console, go to the **Bigtable instances** page.

[Go to instances list](https://console.cloud.google.com/bigtable)

     2. In the list of instances, click **Counters quickstart instance**.

     3. In the left navigation pane, click **Tables**.

     4. Click more_vert next to `counters_quickstart_table`, and then click **Delete**.

     5. Enter `counters_quickstart_table` to confirm, and then click **Delete**.

  2. Delete the instance:

     1. In the Google Cloud console, go to the **Bigtable instances** page.

[Go to instances list](https://console.cloud.google.com/bigtable)

     2. Click **Counters quickstart instance**.

     3. Click **Delete instance**.

     4. Enter `counters-quickstart-instance` to confirm, and then click **Delete**.

  3. In the terminal, delete the configuration files and optional credentials:

     1. Delete the `.cbtrc` file:
            
            rm ~/.cbtrc
            

     2. Delete the formatting file:
            
            rm ~/cbtformat.yaml
            

     3. Optional: Revoke credentials from the gcloud CLI:
            
            gcloud auth revoke
            




###  cbt 

  1. In the terminal, delete the table `counters_quickstart_table`:
         
         cbt deletetable counters_quickstart_table
         

  2. Delete the instance:
         
         cbt deleteinstance counters-quickstart-instance
         

  3. Delete the `.cbtrc` file:
         
         rm ~/.cbtrc
         

  4. Delete the formatting file:
         
         rm ~/cbtformat.yaml
         

  5. Optional: Revoke credentials from the gcloud CLI:
         
         gcloud auth revoke
         




## What's next

  * [Learn more about aggregates](https://docs.cloud.google.com/bigtable/docs/aggregates).
  * [Use SQL to query Bigtable data](https://docs.cloud.google.com/bigtable/docs/introduction-sql).
  * [Work through a quickstart using the `cbt` CLI ](https://docs.cloud.google.com/bigtable/docs/create-instance-write-data-cbt-cli).
  * Explore [additional code samples](https://docs.cloud.google.com/bigtable/docs/samples).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

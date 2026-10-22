---
url: https://docs.cloud.google.com/dataflow/docs/tutorials/beam-yaml-builder-form/
title: Create pipelines using the builder form in the job builder UI \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:48.947686+00:00
---

# Create pipelines using the builder form in the job builder UI  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/tutorials/beam-yaml-builder-form/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Create pipelines using the builder form in the job builder UI Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to use [Apache Beam YAML](https://beam.apache.org/documentation/sdks/yaml/) syntax to create Dataflow data processing pipelines. You'll learn how to read data from a file, apply transformations, and write the results to another file, using the job builder UI in the Google Cloud console. This tutorial is intended for developers who are new to Apache Beam or want to learn how to use the YAML API for building pipelines.

The following table shows a pipeline graph in the Google Cloud console and its corresponding YAML specification.

![A graph of the Dataflow job.](https://docs.cloud.google.com/static/dataflow/images/beam-yaml_map-fields-python_graph.png) | 
    
    
    pipeline:
      transforms:
        - name: ReadFromCsv
          type: ReadFromCsv
          config:
            path: 'gs://[...]/restaurant-data.csv'
        - name: MapToFields
          type: MapToFields
          input: ReadFromCsv
          config:
            language: python
            fields:
              Lowercase_menu_item: Item.lower()
              Total_price: Price + Tax
            append: true
        - name: WriteToJson
          type: WriteToJson
          input: MapToFields
          config:
            path: 'gs://[...]/restaurant-data_map-fields.json'  
  
---|---  
  
## Job builder overview

Using the builder form in the job builder UI offers several benefits:

  * **No-code pipeline building:** Visually design and configure Dataflow pipelines without writing code or needing deep Beam SDK knowledge.
  * **Rapid development:** Quickly prototype and build custom pipelines, especially when existing [Google-provided Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates) don't meet your specific requirements.
  * **Visual interface:** A graphical representation of the pipeline helps you understand the flow of data through sources, transforms, and sinks.
  * **Beam YAML integration:**
    * **Save and load:** Save pipelines created in the Google Cloud console as Beam YAML files for version control, sharing, and reuse, or load existing Beam YAML files into the builder.
    * **CLI deployment:** Use exported YAML definitions to launch jobs by using the gcloud CLI.
  * **Support for common operations:** Configure various sources, sinks, and transformations, such as filtering, mapping, SQL, group-by, join, and explode.



For more information, see the [Job builder UI overview](https://docs.cloud.google.com/dataflow/docs/guides/job-builder).

## Objectives

In this tutorial, you will learn how to do the following:

  * Create Beam YAML pipelines that read, write, and transform data.
  * Filter data based on content.
  * Map fields using Python expressions.
  * Use SQL to query and aggregate data.
  * Build and run Beam YAML pipelines using the builder form in the job builder UI in the Google Cloud console.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Dataflow](https://cloud.google.com/dataflow/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Complete the following steps before running your pipeline.

### Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataflow, Compute Engine, Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataflow,compute_component,storage_api)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Dataflow, Compute Engine, Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataflow,compute_component,storage_api)




### Create a Cloud Storage bucket

Before you can run a pipeline, you must create a Cloud Storage bucket.

  1. Create a Cloud Storage bucket:

     1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Click add_box **Create**. 
     3. On the **Create a bucket** page, enter your bucket information. To go to the next step, click **Continue**. 
        1. For **Name your bucket** , enter a unique bucket name. Don't include sensitive information in the bucket name, because the bucket namespace is global and publicly visible. 
        2. In the **Choose where to store your data** section, do the following: 
           1. Select a [Location type](https://docs.cloud.google.com/storage/docs/locations).
           2. Choose a location where your bucket's data is permanently stored from the **[Location type](https://docs.cloud.google.com/storage/docs/locations#available-locations)** drop-down menu. 
              * If you select the [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) location type, you can also choose to enable [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) by using the relevant checkbox. 
           3. To set up [cross-bucket replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-bucket-replication), select **Add cross-bucket replication via Storage Transfer Service** and follow these steps: 

#### Set up cross-bucket replication

              1. In the **Bucket** menu, select a bucket.
              2. In the **Replication settings** section, click **Configure** to configure settings for the replication job.

The **Configure cross-bucket replication** pane appears.

                 * To filter objects to replicate by object name prefix, enter a prefix that you want to include or exclude objects from, then click add **Add a prefix**.
                 * To set a storage class for the replicated objects, select a storage class from the **Storage class** menu. If you skip this step, the replicated objects will use the destination bucket's storage class by default.
                 * Click **Done**.

        3. In the **Choose how to store your data** section, do the following: 
           1. In the **Set a default class** section, select the following: **Standard**. 
           2. To enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), in the **Optimize storage for data-intensive workloads** section, select **Enable hierarchical namespace on this bucket**. **Note:** You cannot enable hierarchical namespace in existing buckets.
        4. In the **Choose how to control access to objects** section, select whether or not your bucket enforces [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention), and select an [access control method](https://docs.cloud.google.com/storage/docs/access-control) for your bucket's objects. **Note:** You cannot change the **Prevent public access** setting if this setting is enforced at an [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention).
        5. In the **Choose how to protect object data** section, do the following: 
           * Select any of the options under **Data protection** that you want to set for your bucket. 
             * To enable [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete), click the **Soft delete policy (For data recovery)** checkbox, and specify the number of days you want to retain objects after deletion.
             * To set [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning), click the **Object versioning (For version control)** checkbox, and specify the maximum number of versions per object and the number of days after which the noncurrent versions expire.
             * To enable the retention policy on objects and buckets, click the **Retention (For compliance)** checkbox, and then do the following: 
               * To enable [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock), click the **Enable object retention** checkbox.
               * To enable [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock), click the **Set bucket retention policy** checkbox, and choose a unit of time and a length of time for your retention period.
           * To choose how your object data will be encrypted, expand the **Data encryption** section (expand_more), and select a [**Data encryption** method](https://docs.cloud.google.com/storage/docs/encryption).
     4. Click **Create**. 
  2. Copy the following, as you need them in a later section:

     * Your Cloud Storage bucket name.
     * Your Google Cloud project ID.

To find this ID, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).




### VPC network

By default, each new project starts with a [default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network). If the default network for your project is [disabled](https://docs.cloud.google.com/vpc/docs/vpc#org-policies) or was deleted, you need to have a network in your project for which your user account has the [Compute Network User role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`).

## Read, write, and transform data

This section shows how you can use Beam YAML syntax with Dataflow to read, write, and filter data using the following:

  * User interface-driven development to build and run jobs in the job builder UI in the Google Cloud console. Specifically, you'll use the builder form in the job builder UI, so you don't manually need to create the YAML files.
  * CSV file data stored in a publicly-viewable Cloud Storage bucket. This data contains mock restaurant menu data and looks like the following:

#### `restaurant-data.csv`
        
        Menu item,Category,Price,Tax
        Classic Cheeseburger,Entree,9.99,0.7
        Margherita Pizza,Entree,14.50,1.02
        Grilled Salmon with Asparagus,Entree,21.99,1.54
        Chicken Caesar Salad,Salad,12.75,0.89
        Spaghetti Carbonara,Entree,16.25,1.14
        Beef Tacos (3),Entree,10.50,0.74
        Vegetable Stir-Fry,Entree,13.00,0.91
        Shrimp Scampi,Entree,19.75,1.38
        Chicken Pot Pie,Entree,15.50,1.09
        Steak Frites,Entree,28.00,1.96
        Lobster Mac and Cheese,Entree,25.50,1.79
        Pork Belly Bao Buns (2),Appetizer/Side,11.25,0.79
        Mushroom Risotto,Entree,17.50,1.23
        Fish and Chips,Entree,14.00,0.98
        Buffalo Wings (6),Appetizer/Side,9.50,0.67
        French Onion Soup,Appetizer/Side,7.00,0.49
        Tomato Soup with Grilled Cheese,Appetizer/Side,10.00,0.7
        Avocado Toast,Appetizer/Side,8.50,0.6
        Quesadilla with Chicken,Appetizer/Side,11.75,0.82
        Pad Thai,Entree,15.00,1.05
        Chicken Tikka Masala,Entree,18.50,1.3
        Burrito Bowl,Entree,13.50,0.95
        Sushi Combo (8 pieces),Entree,22.00,1.54
        Greek Salad,Salad,11.00,0.77
        Clam Chowder,Appetizer/Side,8.00,0.56
        New York Cheesecake,Dessert,6.50,0.46
        Chocolate Lava Cake,Dessert,7.50,0.53
        Apple Pie,Dessert,5.00,0.35
        Tiramisu,Dessert,8.00,0.56
        Crème brûlée,Dessert,7.00,0.49
        Iced Coffee,Beverage,3.50,0.25
        Lemonade,Beverage,3.00,0.21
        Orange Juice,Beverage,4.00,0.28
        Soda,Beverage,2.50,0.18
        Craft Beer,Beverage,6.00,0.42
        Glass of Wine,Beverage,9.00,0.63
        Margarita,Beverage,12.00,0.84
        Moscow Mule,Beverage,11.50,0.81
        Old Fashioned,Beverage,13.00,0.91
        Espresso,Beverage,3.00,0.21
        Cappuccino,Beverage,4.50,0.32
        Latte,Beverage,5.00,0.35
        Mocha,Beverage,5.50,0.39
        Hot Chocolate,Beverage,4.00,0.28
        Breakfast Burrito,Breakfast,10.50,0.74
        Pancakes (3),Breakfast,8.00,0.56
        Waffles,Breakfast,9.00,0.63
        Eggs Benedict,Breakfast,14.00,0.98
        Omelette,Breakfast,11.00,0.77
        Fruit Salad,Salad,7.50,0.53
        Yogurt Parfait,Breakfast,6.00,0.42




### Read and filter data

The following example shows you how to read data from a CSV file, filter it for specific information, and write the filtered data to a JSON file.

This sample uses the [`Filter` transform](https://beam.apache.org/documentation/sdks/yaml/#add-a-filter), which lets you selectively keep data that meets certain criteria. The following example filters a dataset to keep only the records where the `Price` is greater than or equal to `20.00`.

To read the CSV data and output filtered JSON content, complete the following steps:

  1. In the Google Cloud console, go to the Dataflow **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow)

  2. Click add_box**Create Job From Builder**.

  3. On the **Job builder** tab, leave **Builder form** selected.

  4. In the **Job name** field, enter `filter-python-job`.

  5. For **Job type** , leave radio_button_checked**Batch** selected.

  6. In the **Sources** section:

     1. In the **Source name** field in the **New source** panel, change the name to `ReadCsv`.

     2. In the **Source type** list, select **CSV from Cloud Storage**.

     3. In the **CSV location** field, enter:
            
            cloud-samples-data/dataflow/tutorials/restaurant-data.csv
            

     4. Click **Done**.

  7. In the **Transforms** section:

     1. Click **Add a transform**.

     2. In the **Transform name** field, enter `FilterPrice`.

     3. In the **Transform type** list, select **Filter (Python)**.

     4. In the **Python filter expression** field, enter `Price >= 20.00`.

     5. In the **Input step for the transform** list, leave `ReadCsv` selected.

     6. Click **Done**.

  8. In the **Sinks** section:

     1. In the **Sink name** field, change the name to `WriteJson`.

     2. In the **Sink type** list, select **JSON files on Cloud Storage**.

     3. In the **JSON location** field, enter:
            
            BUCKET_NAME/output/restaurant-data_filtered.json
            

Replace `BUCKET_NAME` with the name of your Cloud Storage bucket.

     4. In the **Input step for the sink** list, leave `FilterPrice` selected.

     5. Click **Done**.

  9. In the **Dataflow Options** section, click **Run job** arrow_drop_down.




#### Examine the job output

When the job completes, complete the following steps to see the output from the pipeline:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click the name of the bucket that you created in Create a Cloud Storage bucket.

  3. Click the file named `restaurant-data_filtered.json-00000-of-00001`.

  4. In the **Object details** page, click the authenticated URL to view the pipeline output.




The output should look similar to the following:
    
    
    {"Item":"Grilled Salmon with Asparagus","Category":"Entree","Price":21.99,"Tax":1.54}
    {"Item":"Steak Frites","Category":"Entree","Price":28.0,"Tax":1.96}
    {"Item":"Lobster Mac and Cheese","Category":"Entree","Price":25.5,"Tax":1.79}
    {"Item":"Sushi Combo (8 pieces)","Category":"Entree","Price":22.0,"Tax":1.54}
    

### Map fields using Python

With the [`MapToFields` transform](https://beam.apache.org/documentation/sdks/yaml-udf/), you can create new fields based on existing ones. The following example creates a lowercase version of a menu item, calculates a total price, and appends the values after the existing values.

  1. Go to the Dataflow **Jobs** page in the Google Cloud console.

[Go to Jobs](https://console.cloud.google.com/dataflow)

  2. Click add_box**Create job from builder**.

  3. On the **Job builder** tab, leave **Builder form** selected.

  4. In the **Job name** field, enter `map-python-job`.

  5. For **Job type** , leave radio_button_checked**Batch** selected.

  6. In the **Sources** section:

     1. In the **Source name** field in the **New source** panel, change the name to `ReadFromCsvPy`.

     2. In the **Source type** list, select **CSV from Cloud Storage**.

     3. In the **CSV location** field, enter:
            
            cloud-samples-data/dataflow/tutorials/restaurant-data.csv
            

     4. Click **Done**.

  7. In the **Transforms** section:

     1. Click **Add a transform**.

     2. In the **Transform name** field, enter `MapToFieldsPy`.

     3. In the **Transform type** list, select **Map fields (Python)**.

     4. Leave check_box**Preserve existing fields** selected.

     5. In the **Mapped fields** section, click **Add a field**.

     6. In the **New field** panel that opens, put `Lowercase_menu_item` as the **Field name**.

     7. In the **Python expression** field, put `Item.lower()`.

     8. Click **Done**.

     9. In the same **Mapped fields** section, click **Add a field** again.

     10. In the **New field** panel that opens, put `Total_price` as the **Field name**.

     11. In the **Python expression** field, put `Price + Tax`.

     12. In this **New field** panel, click **Done**.

     13. In this **New transform** panel, click **Done**.

  8. In the **Sinks** section:

     1. In the **Sink name** field, change the name to `WriteToJsonPy`.

     2. In the **Sink type** list, select **JSON files on Cloud Storage**.

     3. In the **JSON location** field, enter:
            
            BUCKET_NAME/output/restaurant-data_map-fields.json
            

Replace `BUCKET_NAME` with the name of your Cloud Storage bucket.

     4. In the **Input step for the sink** list, leave `MapToFieldsPy` selected.

     5. Click **Done**.

  9. In the **Dataflow Options** section, click **Run job** arrow_drop_down.




#### Examine the job output

When the job completes, complete the following steps to see the output from the pipeline:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click the name of the bucket that you created in Create a Cloud Storage bucket.

  3. Click the file named `restaurant-data_map-fields.json-00000-of-00001`.

  4. In the **Object details** page, click the authenticated URL to view the pipeline output.




The output should look similar to the following:
    
    
    {"Item":"Classic Cheeseburger","Category":"Entree","Price":9.99,"Tax":0.7,"Lowercase_menu_item":"classic cheeseburger","Total_price":10.69}
    {"Item":"Margherita Pizza","Category":"Entree","Price":14.5,"Tax":1.02,"Lowercase_menu_item":"margherita pizza","Total_price":15.52}
    {"Item":"Grilled Salmon with Asparagus","Category":"Entree","Price":21.99,"Tax":1.54,"Lowercase_menu_item":"grilled salmon with asparagus","Total_price":23.53}
    {"Item":"Chicken Caesar Salad","Category":"Salad","Price":12.75,"Tax":0.89,"Lowercase_menu_item":"chicken caesar salad","Total_price":13.64}
    {"Item":"Spaghetti Carbonara","Category":"Entree","Price":16.25,"Tax":1.14,"Lowercase_menu_item":"spaghetti carbonara","Total_price":17.39}
    {"Item":"Beef Tacos (3)","Category":"Entree","Price":10.5,"Tax":0.74,"Lowercase_menu_item":"beef tacos (3)","Total_price":11.24}
    [...]
    

### Transform data using SQL

The [`Sql` transform](https://beam.apache.org/documentation/sdks/yaml/#named-transforms) lets you run SQL queries on your data. The following example groups menu items by category (such as `Entree`, `Beverage`, or `Dessert`) and adds a column with the count of the items in each category.

To use the job builder UI to create your pipeline, follow these steps:

  1. Go to the Dataflow **Jobs** page in the Google Cloud console.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Click add_box**Create job from builder**.

  3. In the **Job builder** tab, in the **Job name** field, enter `sql-transform-job`.

  4. For **Job type** , leave radio_button_checked**Batch** selected.

  5. In the **Sources** section:

     1. In the **Source name** field, change the name to `SqlTransformSource`.

     2. In the **New source** tab, for **Source type** , select **CSV from Cloud Storage**. The **CSV location** field opens.

     3. For **CSV location** , enter:
            
            cloud-samples-data/dataflow/tutorials/restaurant-data.csv
            

     4. Click **Done**.

  6. In the **Transforms** section:

     1. Click **Add a transform**.

     2. In the **Transform name** field, update the name to `SqlTransform`.

     3. For **Transform type** , select **SQL transform**. The **SQL transform** options open.

     4. In the **SQL expression** field, enter:
            
            select Category, count(*) as category_count from PCOLLECTION group by Category
            

     5. Click **Done**.

  7. In the **Sinks** section:

     1. For **Sink name** , enter `SqlTransformSink`.

     2. For **Sink type** , select **JSON files on Cloud Storage**. The **Write to JSON files on Cloud Storage** options open.

     3. For **JSON location** , enter:
            
            BUCKET_NAME/output/restaurant-data_transform-sql.json
            

Replace `BUCKET_NAME` with the name of your Cloud Storage bucket.

     4. Click **Done**.

  8. Optional: View the generated YAML definition for this pipeline.

     1. Navigate to the top of the Job builder tab.

     2. Select **YAML editor**. You should see the YAML definition. It should look like the following:

#### Generated YAML specification
            
            pipeline:
              transforms:
                - name: SqlTransformSource
                  type: ReadFromCsv
                  config:
                    path: 'gs://cloud-samples-data/dataflow/tutorials/restaurant-data.csv'
                - name: SqlTransform
                  type: Sql
                  config:
                    query: >-
                      select Category, count(*) as category_count from PCOLLECTION group by
                      Category
                  input:
                    input0: SqlTransformSource
                - name: SqlTransformSink
                  type: WriteToJson
                  input: SqlTransform
                  config:
                    path: 'gs://BUCKET_NAME/output/restaurant-data_transform-sql.json'

  9. In the **Dataflow Options** section, click **Run job** arrow_drop_down.




#### Examine the job output

When the job completes, complete the following steps to see the output from the pipeline:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click the name of the bucket that you created in Create a Cloud Storage bucket.

  3. Click the file named `restaurant-data_transform-sql.json-00000-of-00001`.

  4. In the **Object details** page, click the authenticated URL to view the pipeline output.




The output should look similar to the following:
    
    
    {"Category":"Entree","category_count":16}
    {"Category":"Beverage","category_count":14}
    {"Category":"Appetizer\/Side","category_count":7}
    {"Category":"Dessert","category_count":5}
    {"Category":"Breakfast","category_count":6}
    {"Category":"Salad","category_count":3}
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resources

If you want to reuse the project later, you can keep the project but delete the resources that you created during the tutorial.

#### Stop the Dataflow pipeline

  1. In the Google Cloud console, go to the Dataflow **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Click the job that you want to stop.

To stop a job, the status of the job must be **running**.

  3. In the job details page, click **Stop**.

  4. Click **Cancel**.

  5. To confirm your choice, click **Stop Job**.




#### Delete your Cloud Storage bucket

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the checkbox for the bucket that you want to delete. 
  3. To delete the bucket, click delete **Delete** , and then follow the instructions. 



## What's next

  * Learn more about creating jobs using the [job builder UI overview](https://docs.cloud.google.com/dataflow/docs/guides/job-builder) in the Google Cloud console.
  * Learn about job builder custom jobs in [Create a custom job with the job builder](https://docs.cloud.google.com/dataflow/docs/guides/job-builder-custom-job).
  * Read the [Beam YAML API](https://beam.apache.org/documentation/sdks/yaml/) overview.
  * View more [Beam YAML examples](https://beam.apache.org/releases/yamldoc/current/examples.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

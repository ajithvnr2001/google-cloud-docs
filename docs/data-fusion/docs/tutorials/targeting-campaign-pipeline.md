---
url: https://docs.cloud.google.com/data-fusion/docs/tutorials/targeting-campaign-pipeline/
title: Create a target campaign pipeline \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:24.169332+00:00
---

# Create a target campaign pipeline  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/tutorials/targeting-campaign-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a target campaign pipeline

Learn how to use Cloud Data Fusion to clean, transform, and process customer data to select candidates for a target campaign.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/?walkthrough_id=data-fusion--create-data-pipeline)

* * *

## Scenario

You want to create custom marketing materials for an ongoing campaign promotion, and you'd like to distribute the materials directly to the home mailboxes of your customers.

Your campaign has two constraints:

  * **Location** : You only deliver to customers in California, Washington, and Oregon.
  * **Cost** : To save on fuel, you deliver to quickly accessible customer homes. You deliver only to customers who live on avenues.



This tutorial shows you how to generate the list of customer addresses for the campaign. In this tutorial, you do the following:

  1. Clean the customer data: filter customers that live on an avenue in California, Washington, or Oregon.
  2. Create a pipeline that does the following:

     * Joins the filtered customer data with a public dataset that contains state abbreviations.
     * Stores the cleaned and joined data in a BigQuery table that you can query (by using the BigQuery web interface) or analyze (by using Data Studio).



## Objectives

  * Connect Cloud Data Fusion to two data sources
  * Apply basic transformations
  * Join the two data sources
  * Write the output data to a sink



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud Data Fusion, BigQuery, Cloud Storage, and Dataproc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datafusion.googleapis.com,bigquery.googleapis.com,storage.googleapis.com,dataproc.googleapis.com)

  7. [ Create a Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance).  
This tutorial assumes that you use the default Compute Engine service account. 

**Note:** Ensure that you check the estimated cost before proceeding. To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

## Manage permissions

Create and assign the required custom roles and permissions.

### Create a custom role and add permissions

  1. In the Google Cloud console, go to the **Roles** page:

[Go to the Roles page](https://console.cloud.google.com/iam-admin/roles)

  2. Click **add Create role**.

  3. In the **Title** field, enter `Custom Role-Tutorial`.

  4. Click **add Add permissions**.

  5. In the **Add permissions** window, select the following permissions and click **Add** :

     * `bigquery.datasets.create`
     * `bigquery.jobs.create`
     * `storage.buckets.create`
  6. Click **Create**.




### Assign custom role to the default Compute Engine service account

  1. Go to the Cloud Data Fusion **Instances** page: 

[Create an instance](https://console.cloud.google.com/data-fusion)

  2. Click the name of your instance.

  3. Make a note of the default **Dataproc Service Account**. The instance details page contains this information.

The following is the format of the Managed Service for Apache Spark service account name:

`CUSTOMER_PROJECT_NUMBER-compute@developer.gserviceaccount.com`.

Learn more about [Managed Service for Apache Spark service accounts](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#dataproc_service_accounts_2). 

  4. Go to the **IAM** page:

[Go to the Roles page](https://console.cloud.google.com/iam-admin/iam)

  5. In the **Filter** bar, enter the name of your default Managed Service for Apache Spark service account.

  6. For your default Compute Engine service account, click **edit Edit**.

  7. Click **add Add another role**.

  8. In the **Select a role** field, select **Custom Role-Tutorial**.

  9. Click **Save**.

  10. Ensure that the service account is already assigned the Cloud Data Fusion Runner role.




## Prepare the customer data

This tutorial requires the following two input datasets, both of which are provided with your Cloud Data Fusion instance:

  * **Sample customer data** : A CSV file named `customers.csv`.
  * **State abbreviations** : A BigQuery table named `state_abbreviations`.



### Load the customer data

**Note:** The customer data is in a Cloud Storage bucket. The Cloud Storage bucket is publicly available through the **Sample Buckets** connection, provided by default with your Cloud Data Fusion instance.

  1. Go to the Cloud Data Fusion **Instances** page: 

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. For the Cloud Data Fusion instance you are using, click **View instance**. The Cloud Data Fusion web interface opens in a new tab.

  3. Click **Wrangler**. The **Wrangler** page opens.

  4. In the **Connections** pane, **GCS > Sample Buckets**.

  5. Click **campaign-tutorial**.

  6. Click **customers.csv**.

  7. In the **Parsing options** window, specify the following:

     * **Format** : `csv`
     * **Enable quoted value** : `False`
     * **Use first row as header** : `False`
     * **File-encoding** : `UTF-8`
  8. Click **Confirm**. Customer data is loaded in a new tab in Wrangler.

![Loaded customer data](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/targeting-campaign-pipeline/customers-workspace-no-transforms.png)




### Clean the customer data

This contains two sub-tasks:

  * Setting the schema
  * Filtering the customer data to present only the target audience you need



#### Set the schema

Set the schema of the data by assigning appropriate names to the table columns. To give the columns, such as `body_1` and `body_2`, more informative names, follow these steps:.

  1. In the right pane, click the **Columns** tab.
  2. Click the **Column names** drop-down and select **Set all**.
  3. In the **Bulk set column names** dialog, enter the following, comma-separated column names:
         
         Name,StreetAddress,City,State,Country
         

  4. Click **Apply**.




#### Filter the data

Filter the data to display only customers that live in California, Oregon, or Washington.

Remove all rows that contain values other than those states:

  1. Click the **State** column drop-down and select **Filter**.
  2. In the filter window, do the following:

     1. Click **Keep rows**.
     2. Click the **If** drop-down, and select **value matches regex**.
     3. Enter the following regular expression:
            
            ^(California|Oregon|Washington)$
            

     4. Click **Apply**.

The values in the **State** column are **California** , **Oregon** , or **Washington**.




Filter the data to display only customers that live on avenues. Keep only the addresses that contain the string `Avenue`:

  1. Click the **StreetAddress** column drop-down, and select **Filter**.
  2. In the filter window, do the following: 
     1. Click **Keep rows**.
     2. Click the **If** drop-down, select **value contains** , and enter `Avenue`.
     3. Select **Ignore case**.
     4. Click **Apply**.



Before performing parallel-processing jobs on your entire dataset, Wrangler displays only the first 1000 values of your dataset. Because you filtered some data, only a few customers remain in the Wrangler display.

## Create a batch pipeline

You've cleaned your data and you've run transformations on a subset of your data. You can now create a batch pipeline to run transformations on your entire dataset.

Cloud Data Fusion translates the pipeline that you build in the Studio into an Apache Spark program that executes transformations in parallel on an ephemeral Managed Service for Apache Spark cluster. This process lets you execute complex transformations over vast quantities of data in a scalable, reliable manner, without having to handle the infrastructure.

  1. On the Wrangler page, click **Create a pipeline**.
  2. Select **Batch pipeline**. The Studio page opens.
  3. On the Studio page, a **GCSFile** source node is connected to a **Wrangler** node.

![GCSFile node connected to Wrangler node](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/targeting-campaign-pipeline/source-and-wrangler-in-studio.png)

The transformations you applied on the Wrangler page appear in the **Wrangler** node on the Studio page.

  4. To view the transformations that you applied, hold the pointer over the **Wrangler** node and click **Properties**.

The transformations you applied appear in the **Directives**.

![View applied transformations](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/targeting-campaign-pipeline/wrangler-config.png)

  5. Click **Validate**.

  6. Click **close Close**.


You can apply more transformations by clicking **Wrangle** , which takes you back to the Wrangler page. The transformation that you added appears on the Studio page. 

For example, you realize the **Country** column isn't needed because the value is always `USA`. You delete the column by following these steps:

  1. Click **Wrangle**.
  2. Click the down arrow next to **Country** and select **Delete Column**.
  3. Click **Apply**. The Wrangler page closes and the Wrangler Properties window opens on the Studio page. In the **Directives** , `drop Country` appears.
  4. Click close **Close**.



### Abbreviate the state names

The navigation system in your delivery vehicle only recognizes addresses that contain abbreviated state names (CA, not California), and your customer data contains full state names.

The public BigQuery `state_abbreviations` table contains two columns: one with the full state names and one with the abbreviated state names. You can use this table to update the state names in your customer data.

#### View the state names data in BigQuery

  1. In a separate tab, go to the BigQuery Studio page:

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Click **Create SQL query** and enter the following query in the query editor:
         
         SELECT * FROM `dis-user-guide.campaign_tutorial.state_abbreviations`
         

  3. Click **Run**.

BigQuery displays a list of state names and their abbreviations.




#### Access the BigQuery table

Add a source in your pipeline that will access the BigQuery `state_abbreviations` table.

  1. Go to the Cloud Data Fusion Studio page and expand the **Source** menu.
  2. Click **BigQuery**.

A BigQuery source node appears on the canvas, along with the other two nodes.

  3. Hold the pointer over the **BigQuery** source node and click **Properties**.

     1. In the **Dataset Project ID** field, enter `dis-user-guide`.
     2. In the **Reference Name** field, enter `state_abbreviations`.
     3. In the **Dataset** field, enter `campaign_tutorial`.
     4. In the **Table** field, enter `state_abbreviations`.
  4. Populate the schema of the table from BigQuery by clicking **Get Schema**.

  5. Click close **Close**.




#### Join the two data sources

To generate output that contains customer data with abbreviated state names, join the two data sources, the customer data, and the state abbreviations.

  1. Go to the Cloud Data Fusion Studio page and expand the **Analytics** menu.
  2. Click **Joiner**.

A **Joiner** node, representing an action similar to a SQL Join, appears on the canvas.

  3. Connect the **Wrangler** node and the **BigQuery** node to the **Joiner** node: Drag a connection arrow on the right edge of the source node and drop onto the destination node.

![Join Wrangler and BigQuery nodes to Joiner node](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/targeting-campaign-pipeline/joiner-connections.png)

  4. Hold the pointer over the **Joiner** node and click **Properties**.

     1. In the **Fields** section, expand **Wrangler** and **BigQuery**.

        1. Clear the Wrangler **state** checkbox.
        2. Clear the BigQuery **name** checkbox because you want only the abbreviated state name and not the full state name.
        3. Keep the BigQuery **abbreviation** checkbox selected, and change the alias to `State`.

![Joiner node properties](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/targeting-campaign-pipeline/joiner-config-fields.png)

     2. In the **Join Type** field, leave the value as **Outer**. For **Required inputs** , select the **Wrangler** checkbox.

     3. In the **Join condition** section, for Wrangler, select **State**. For BigQuery, select **name**.

     4. Generate the schema of the resultant join. Click **Get Schema**.

     5. Click **Validate**.

     6. Click close **Close**.




### Store the output to BigQuery

Store the result of your pipeline into a BigQuery table. Where you store your data is called a sink.

  1. Go to the Cloud Data Fusion Studio page and expand **Sink**.
  2. Click **BigQuery**.
  3. Connect the **Joiner** node to the **BigQuery** node.

![Connect Joiner node and BigQuery node](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/targeting-campaign-pipeline/complete-pipeline-studio.png)

  4. Hold the pointer over the **BigQuery** node and click **Properties**.

     1. In the **Dataset** field, enter `dis_user_guide`.
     2. In the **Table** field, select `customer_data_abbreviated_states`.
     3. Click close **Close**.



## Deploy and run the pipeline

  1. On the Studio page, click **Name your pipeline** and enter `CampaignPipeline`.
  2. Click **Save**.
  3. In the upper-right corner, click **Deploy**.
  4. After deployment completes, click **Run**.



Running your pipeline can take a few minutes. While you wait, you can observe the **Status** of the pipeline transition from _Provisioning_ > _Starting_ > _Running_ > _Deprovisioning_ > _Succeeded_.

## View the results

  1. In the Google Cloud console, go to the BigQuery page:

[ Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Click **Create SQL query**.

  3. Query the `customer_data_abbreviated_states` table:
         
         SELECT * FROM dis_user_guide.customer_data_abbreviated_states LIMIT 1000
         

![View the results](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/targeting-campaign-pipeline/bigquery-output-results.png)

**Note:** For further analysis, you can [connect this table to Data Studio](https://docs.cloud.google.com/bigquery/docs/visualize-looker-studio). 



You have successfully created a data pipeline.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the BigQuery dataset

To delete the BigQuery dataset that you created in this tutorial, do the following:

  1. In the Google Cloud console, go to the BigQuery page. 

[ Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Select the `dis_user_guide` dataset.
  3. Click _delete_ **Delete dataset**.



### Delete the Cloud Data Fusion instance

Follow these instructions to [ delete your Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/delete-instance).

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn more about [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/overview). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

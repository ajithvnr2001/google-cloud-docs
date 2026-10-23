---
url: https://docs.cloud.google.com/vision-ai/docs/occupancy-bq-tutorial/
title: Create an occupancy analytics app with BigQuery forecasting \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:33.952688+00:00
---

# Create an occupancy analytics app with BigQuery forecasting  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/occupancy-bq-tutorial/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Create an occupancy analytics app with BigQuery forecasting Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise Agent Platform Vision is an AI-powered platform you can use to ingest, analyze, and store video data. Gemini Enterprise Agent Platform Vision lets you build and deploy AI applications. You can build end-to-end Gemini Enterprise Agent Platform Vision solutions by leveraging Gemini Enterprise Agent Platform Vision's integration with other product components.

To start implementing solutions using the Gemini Enterprise Agent Platform Vision platform, review the following Agent Platform Vision concepts and components:

  * **Streams** : Represent a video streaming layer from your solution. The stream source can be a live video (for example, an IP camera) or a video file (for example, an MP4 file).

  * **Applications** : Enable the connection between a stream and an AI processor to perform a machine learning operation on the video. For example, you can connect a camera stream to an AI model that counts people passing in front of it. 

  * **App output destination** : Send analyzed data to a storage destination (Gemini Enterprise Agent Platform Vision's Media Warehouse or BigQuery) or receive live data. Storing to Gemini Enterprise Agent Platform Vision's Media Warehouse lets you search analysis output and metadata from the AI processors used on data from the ingested streams. Storing to BigQuery lets you use the product's offline analytics capabilities. If you directly receive app output, you can use insights to instantly inform business decisions. For more information, see [Overview: Connect app output to a data destination](https://docs.cloud.google.com/vision-ai/docs/connect-data-destination). 




## Objectives

This tutorial shows you how to do the following:

  * Create a BigQuery dataset and table.
  * Build a Gemini Enterprise Agent Platform Vision occupancy analytics app that connects to BigQuery.
  * Create a Compute Engine VM instance and set up its environment.
  * Stream video from the VM instance to the app.
  * Use stored app output to create a forecasting model with BigQuery ML.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Agent Platform Vision](https://docs.cloud.google.com/vision-ai/pricing) (Streams - Data ingested, Streams - Data consumed, Models - Occupancy analytics suite) 
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)
  * [BigQuery](https://cloud.google.com/bigquery/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the BigQuery, Compute Engine and Vision AI APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,visionai.googleapis.com,bigquery.googleapis.com)

  5. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the following roles to the service account: **Vision AI > Vision AI Editor, Compute Engine > Compute Instance Admin (beta), BigQuery > BigQuery Data Owner, Storage > Storage Object Viewer†**. 

To grant a role, find the **Select a role** list, then select the role. 

To grant additional roles, click add **Add another role** and add each additional role. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

Do not close your browser window. You will use it in the next step. 

  6. Create a service account key: 

     1. In the Google Cloud console, click the email address for the service account that you created. 
     2. Click **Keys**. 
     3. Click **Add key** , and then click **Create new key**. 
     4. Click **Create**. A JSON key file is downloaded to your computer. 
     5. Click **Close**. 
  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  10. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Enable the BigQuery, Compute Engine and Vision AI APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,visionai.googleapis.com,bigquery.googleapis.com)

  13. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the following roles to the service account: **Vision AI > Vision AI Editor, Compute Engine > Compute Instance Admin (beta), BigQuery > BigQuery Data Owner, Storage > Storage Object Viewer†**. 

To grant a role, find the **Select a role** list, then select the role. 

To grant additional roles, click add **Add another role** and add each additional role. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

Do not close your browser window. You will use it in the next step. 

  14. Create a service account key: 

     1. In the Google Cloud console, click the email address for the service account that you created. 
     2. Click **Keys**. 
     3. Click **Add key** , and then click **Create new key**. 
     4. Click **Create**. A JSON key file is downloaded to your computer. 
     5. Click **Close**. 
  15. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  16. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  17. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




† Role only needed if you copy a sample video file from a Cloud Storage bucket.

## Set up BigQuery to receive data

To be able to receive data and make predictions from your analytics app data, you must create a BigQuery dataset and table that match the processed information.

### Create a dataset

Before you can create a BigQuery table, you must first create a dataset to receive the analyzed information from your app.

###  Console 

  1. Open the BigQuery page in the Google Cloud console.

[Go to the BigQuery page](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** panel, select the project where you want to create the dataset.

  3. Expand the more_vert **Actions** option and click **Create dataset**.

  4. On the **Create dataset** page:

     * For **Dataset ID** , enter `occupancy_dataset`.
     * For **Data location** , choose a geographic [location](https://docs.cloud.google.com/bigquery/docs/locations) for the dataset. After a dataset is created, the location can't be changed.

**Note:** If you choose `EU` or an EU-based region for the dataset location, your Core Agent Platform Vision Customer Data resides in the EU. Core Agent Platform Vision Customer Data is defined in the [Service Specific Terms](https://cloud.google.com/terms/service-terms#13-google-bigquery-service).

     * For **Default table expiration** , choose one of the following options:

       * **Never:** (Default) Tables created in the dataset are never automatically deleted. You must delete them manually.
       * **Number of days after table creation:** This value determines when a newly created table in the dataset is deleted. This value is applied if you don't set a table expiration when the table is [created](https://docs.cloud.google.com/bigquery/docs/tables#create-table).

**Note:** If your project is not associated with a billing account, BigQuery automatically sets the default table expiration for datasets that you create in the project. You can specify a shorter default table expiration for a dataset, but you can't specify a longer default table expiration.
     * Click **Create dataset**.




### Create a BigQuery table

### Console

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** pane, expand your project, and then select the `occupancy_dataset` dataset. 
  3. In the **Dataset info** section, click add_box **Create table**. 
  4. In the **Create table** panel, specify the following details: 
     1. In the **Source** section, select **Empty table** in the **Create table from** list. 
     2. In the **Destination** section, specify the following details: 
        1. Verify that in the **Dataset** field `occupancy_dataset` is specified. 
        2. In the **Table** field, enter `occupancy_dataset_table`. 
        3. Verify that the **Table type** field is set to **Native table**. 
     3. In the **Schema** section, enter the [schema](https://docs.cloud.google.com/bigquery/docs/schemas) definition. You can enter schema information manually by doing the following: 
        * Click toggle_on **Edit as text** and paste the following JSON array schema. When you use a JSON array, you generate the schema using the same process as [creating a JSON schema file](https://docs.cloud.google.com/bigquery/docs/schemas#specifying_a_json_schema_file). 
              
              [
                  {
                    "name": "ingestion_time",
                    "type": "TIMESTAMP",
                    "mode": "REQUIRED"
                  },
                  {
                    "name": "application",
                    "type": "STRING",
                    "mode": "REQUIRED"
                  },
                  {
                    "name": "instance",
                    "type": "STRING",
                    "mode": "REQUIRED"
                  },
                  {
                    "name": "node",
                    "type": "STRING",
                    "mode": "REQUIRED"
                  },
                  {
                    "name": "annotation",
                    "type": "STRING"
                  }
              ]

     4. Click **Create table**.



## Create an occupancy count application

After you have set up your BigQuery dataset and table, you can create the app that processes the data sent to these BigQuery resources.

### Create an empty app

Before you can populate the app graph, you must first create an empty app.

### Console

Create an app in the Google Cloud console.

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Click the add**Create** button.

  3. Enter `occupancy-bq-app` as the app name and choose your region.

  4. Click **Create**.




### Add app component nodes

After you have created the empty application, you can then add the three nodes to the app graph:

  1. **Ingestion node** : The stream resource that ingests data sent from a Compute Engine VM instance you create.
  2. **Processing node** : The occupancy analytics model that acts on ingested data.
  3. **BigQuery node** : The connector node that lets your app to store metadata to your BigQuery table.



### Console

Add component nodes to your app in the console.

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Next to the name of your `occupancy-bq-app` application in the list, select schema**View app**. This takes you to the graph visualization of the processing pipeline.




**Add a data ingestion node**

  1. To add an input stream node, select the **Streams** option in the **Connectors** section of the side menu.

  2. In the **Source** section of the **Stream** menu that opens, select add**Add streams**.

  3. In the **Add streams** menu, choose radio_button_checked**Register new streams** and add `occupancy-bq-stream` as the stream name.

  4. To add the stream to the app graph, click **Add streams**.




**Add a data processing node**

  1. To add the occupancy count model node, select the **occupancy analytics** option in the **Specialized models** section of the side menu.

  2. Leave the default selections check_box**People** and check_box**Vehicles**.




**Add a BigQuery node**

  1. To add the output destination (storage) node, select the **BigQuery** option in the **Connectors** section of the side menu.

  2. In the **BigQuery** menu, search for `occupancy_dataset_table` and select your table.

  3. In the **Store metadata from:** section, select both check_box**Streams** and check_box**Occupancy analytics**.




## Deploy your app for use

After you have built your end-to-end app with all the necessary components, the last step to using the app is to deploy it.

### Console

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Next to the name of your `occupancy-bq-app` application in the list, select schema**View app**.

  3. From the application graph builder page, click the play_arrow**Deploy** button.

  4. In the following confirmation dialog, select **Deploy**.

The deploy operation might take several minutes to complete. After deployment finishes, green check marks appear next to the nodes.




## Set up a remote machine to stream video

Now that you have a deployed occupancy count app ready to receive, process, and store streaming data out to a BigQuery table, you must actually stream video data into the app.

In this tutorial you create a Compute Engine VM instance that hosts a video, and you send that streaming video data from the VM.

### Create a Linux VM

The first step in sending video from a Compute Engine VM instance is creating the VM instance.

###  Console 

  1. In the console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select your project and click **Continue**.

  3. Click **Create instance**.

  4. Specify a **Name** for your VM. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

  5. Optional: Change the **Zone** for this VM. Compute Engine randomizes the list of zones within each region to encourage use across multiple zones.

  6. Accept the remaining default options. For more information about these options, see [Create and start a VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#startinstanceconsole).

  7. To create and start the VM, click **Create**.




### Set up the VM environment

After the VM has started, you can use the console to establish an SSH connection in your browser. After establishing this connection, you can download the `vaictl` command-line tool to ingest video into your app.

###  Console 

**Establish an SSH connection to your VM**

  1. In the console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Connect** section of the instance line you created, click on **SSH**. This opens an SSH connection in a new browser window.

![The SSH option in the UI](https://docs.cloud.google.com/static/vision-ai/docs/images/ssh-option.png)




**Download the`vaictl` command-line tool**

  1. In the **SSH-in-browser** window, download the Gemini Enterprise Agent Platform Vision (`vaictl`) command-line tool using the following command:
         
         wget https://github.com/google/visionai/releases/download/v0.0.5/visionai_0.0-5_amd64.deb
         

  2. Install the command-line tool by running the following command:
         
         sudo apt install ./visionai_0.0-5_amd64.deb
         

  3. You can test the installation by running the following command:
         
         vaictl --help
         




## Ingest a video file into your app

After you set up your VM environment, you can copy a sample video file and then use `vaictl` to stream the video data to your occupancy count app.

After you send this command, you must let several hours of data to stream before you move to the next step.

### SSH-in-browser

**Copy a sample video to your VM**

  1. In the **SSH-in-browser** window for your VM, copy a sample video with the following [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command. Replace the following variable: 
     * SOURCE: The location of a video file to use. You can use your own video file source (for example, `gs://BUCKET_NAME/FILENAME.mp4`), or use one of the sample videos: 
       * `gs://cloud-samples-data/vertex-ai-vision/street_vehicles_people.mp4` (video with people and vehicles, [ video source](https://pixabay.com/videos/traffic-london-england-21438/)) 
       * `gs://cloud-samples-data/vertex-ai-vision/highway_vehicles.mp4` (video with vehicles only, [video source](https://pixabay.com/videos/traffic-car-highway-street-27260/)) 
    
    gcloud storage cp SOURCE .




**Stream video from VM and ingest data into your app**

  1. To send this local video file to the app input stream, use the following command. You must take the following variable substitutions: 
     * PROJECT_ID: Your Google Cloud project ID.
     * LOCATION_ID: Your location ID. For example, `us-central1`. [More information](https://cloud.google.com/about/locations). 
     * LOCAL_FILE.EXT: The filename of a local video file. For example, `my-video.mp4`. 
     * `--loop` flag: Optional. Loops file data to simulate streaming. 

This command streams a video file to a stream. If using the `--loop` flag, the video is looped into the stream until you stop the command: 
    
    vaictl -p PROJECT_ID \
        -l LOCATION_ID \
        -c application-cluster-0 \
        --service-endpoint visionai.googleapis.com \
    send video-file to streams 'occupancy-bq-stream' --file-path LOCAL_FILE.EXT --loop




It might take ~100 seconds between starting the `vaictl` ingest operation and the video appearing in the dashboard.

After the stream ingestion is available, you can see the video feed in the **Streams** tab of the Gemini Enterprise Agent Platform Vision dashboard by selecting the `occupancy-bq-stream` stream.

[Go to the Streams tab](https://console.cloud.google.com/ai/vision-ai/video-streams)

## Build a forecasting model with BigQuery ML

You now have a functioning app storing metadata out to BigQuery. After you have a couple of hours of data streamed into your app, you can begin to build a forecasting model with BigQuery ML.

### Optional: Run an occupancy query

You can view the app-produced data stored to the table by running a simple query.

###  Console 

  1. In the Google Cloud console, open the BigQuery page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Select arrow_drop_down**Expand** next to `occupancy_dataset`, and select `occupancy_dataset_table`.

  3. In the table detail view, click add_box**Compose new query**.

![Compose new query](https://docs.cloud.google.com/static/vision-ai/docs/images/bq-compose-new-query.png)

  4. Enter the following Google Standard SQL query in the **Query editor** text area:
         
         SELECT
          *
         FROM (
          SELECT
            TIMESTAMP_TRUNC(PARSE_TIMESTAMP('"%Y-%m-%dT%H:%M:%E*SZ"', JSON_QUERY(annotation,
                  "$.currentTime")), MINUTE) currentTime,
            CAST(JSON_QUERY(annotation,
                '$.stats.fullFrameCount[0].count') AS INT64) AS count,
            JSON_QUERY(annotation,
              '$.stats.fullFrameCount[0].entity.labelString') AS type
          FROM
            `PROJECT_ID.occupancy_dataset.occupancy_dataset_table` )
         WHERE
          count IS NOT NULL

  5. Optional: To change the data processing location, click **Edit** > **Query settings**. Under **Processing location** , click **Auto-select** and choose your data's [location](https://docs.cloud.google.com/bigquery/docs/locations). Finally, click **Save** to update the query settings.

  6. Click **Run**.




This creates a query job that writes the output to a temporary table.

Running this query produces a table with time and count information when people are present in the video.

currentTime | count | type  
---|---|---  
2022-08-10 16:17:00 UTC | 2 | "Person"  
2022-08-10 16:17:00 UTC | 2 | "Person"  
2022-08-10 16:17:00 UTC | 4 | "Person"  
2022-08-10 16:17:00 UTC | 1 | "Person"  
2022-08-10 16:17:00 UTC | 5 | "Person"  
2022-08-10 16:17:00 UTC | 2 | "Person"  
  
### Create a view for training

A _view_ is a virtual table defined by a SQL query. When you create a view, you query it in the same way you query a table, and the results contain data only from the tables and fields specified in the query that defines the view. 

After seeing the data stored to the table, you can create a view, and then inspect the contents of the resulting table. You use this view data to train your forecasting model.

You can create a view by composing a SQL query that is used to define the data accessible to the view. The SQL query must consist of a `SELECT` statement. For more information about BigQuery views, see [Introduction to views](https://docs.cloud.google.com/bigquery/docs/views-intro).

To create a training table view:

###  Console 

  1. In the Google Cloud console, open the BigQuery page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Select arrow_drop_down**Expand** next to `occupancy_dataset`, and select `occupancy_dataset_table`.

  3. In the table detail view, click add_box**Compose new query**.

![Compose new query](https://docs.cloud.google.com/static/vision-ai/docs/images/bq-compose-new-query.png)

  4. Enter the following Google Standard SQL query in the **Query editor** text area:
         
         CREATE VIEW `PROJECT_ID.occupancy_dataset.forecast_training_data` AS (
           WITH
             raw_counts AS (
             SELECT
               *
             FROM (
               SELECT
                 TIMESTAMP_TRUNC(
                   PARSE_TIMESTAMP('"%Y-%m-%dT%H:%M:%E*SZ"',
                                   JSON_QUERY(annotation,
                                               "$.currentTime")),
                                 MINUTE) AS currentTime,
                 CAST(JSON_QUERY(annotation,
                     '$.stats.fullFrameCount[0].count') AS INT64) AS count,
                 JSON_QUERY(annotation,
                   '$.stats.fullFrameCount[0].entity.labelString') AS type
               FROM
                 `PROJECT_ID.occupancy_dataset.occupancy_dataset_table` )
             WHERE
               count IS NOT NULL )
           SELECT
             currentTime,
             SUM(count) AS total_count,
             type
           FROM
             raw_counts
           GROUP BY
             currentTime, type)

  5. Click **Run**. 




### Optional: Query the view

Run the following query to see the results of the new view training data:

###  Console 

  1. In the `occupancy_dataset_table` table detail view, click add_box**Compose new query**.

  2. Enter the following Google Standard SQL query in the **Query editor** text area:
         
         SELECT
          *
         FROM
           `PROJECT_ID.occupancy_dataset.forecast_training_data`
         ORDER BY
          currentTime, type
         LIMIT
          100

  3. Click **Run**.




This returns a result sorted by time that looks like the following:

currentTime | total_count | type  
---|---|---  
2022-08-10 16:17:00 UTC | 129 | "Person"  
2022-08-10 16:18:00 UTC | 150  | "Person"  
2022-08-10 16:19:00 UTC | 80 | "Person"  
2022-08-10 16:20:00 UTC | 129 | "Person"  
2022-08-10 16:21:00 UTC | 142 | "Person"  
2022-08-10 16:22:00 UTC | 71 | "Person"  
2022-08-10 16:22:00 UTC | 2 | "Vehicle"  
  
### Train the forecast model with BigQuery ML

Now that you have data in a view to serve as training data, you can train the forecast model with BigQuery ML.

###  Console 

  1. In the `occupancy_dataset_table` table detail view, click add_box**Compose new query**.

  2. Enter the following Google Standard SQL query in the **Query editor** text area:
         
         CREATE OR REPLACE MODEL `PROJECT_ID.occupancy_dataset.occupancy_forecast_model`
           OPTIONS( MODEL_TYPE = "ARIMA_PLUS",
             TIME_SERIES_TIMESTAMP_COL = "currentTime",
             TIME_SERIES_DATA_COL = "total_count",
             TIME_SERIES_ID_COL = "type" ) AS
         SELECT
           *
         FROM
           `PROJECT_ID.occupancy_dataset.forecast_training_data`

  3. Click **Run**.




The query takes several minutes to complete. After the first iteration is complete, your model (`occupancy_forecast_model`) appears in the navigation panel. Because the query uses a `CREATE MODEL` statement to create a model, you don't see query results.

You can observe the model as it's being trained by viewing the **Model stats** tab. As soon as the first iteration completes, the tab is updated. The stats continue to update as each iteration completes.

## Get an occupancy prediction with BigQuery

After your model is done training, you can get a prediction from the model about occupancy count.

The following [`ML.FORECAST`](https://docs.cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-forecast) query uses the [`HORIZON`](https://docs.cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-forecast#horizon) function input to make a forecast of the next 60 minutes.

###  Console 

  1. In the `occupancy_dataset_table` table detail view, click add_box**Compose new query**.

  2. Enter the following Google Standard SQL query in the **Query editor** text area:
         
         SELECT
           *
         FROM
           ML.FORECAST(MODEL `PROJECT_ID.occupancy_dataset.occupancy_forecast_model`,
           STRUCT(60 AS HORIZON))

  3. Click **Run**.




The model produces forecasts under `forecast_value` for future timestamps where type is `"Person"`. For example, on `2022-08-12` at `11:06:00`, the model forecasts there will be ~15.26 "Persons" in total.

type | forecast_timestamp | forecast_value | standard_error | confidence_level | prediction_interval_lower_bound | prediction_interval_upper_bound  
---|---|---|---|---|---|---  
"Person" | **2022-08-12 11:06:00 UTC** | **15.2621986941298** | 2.56470066 | 0.95 | 10.2444693 | 20.2799280  
"Person" | 2022-08-12 11:07:00 UTC | 13.235260043001354 | 3.19379743 | 0.95 | 6.98672921 | 19.4837908  
"Person" | 2022-08-12 11:08:00 UTC | 16.257331475128712 | 3.87581375 | 0.95 | 8.67446430 | 23.8401986  
"Person" | 2022-08-12 11:09:00 UTC | 31.432229611853742 | 4.24905293 | 0.95 | 23.1191356 | 39.7453236  
"Person" | 2022-08-12 11:10:00 UTC | 26.199214148193725 | 4.26157413 | 0.95 | 17.8616229 | 34.5368053  
"Person" | 2022-08-12 11:11:00 UTC | 26.211573546307324 | 4.27962512 | 0.95 | 17.8386663 | 34.5844807  
  
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



### Delete individual resources

#### Delete Compute Engine VM instance

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkbox for the instance that you want to delete. 
  3. To delete the instance, click more_vert **More actions** , click **Delete** , and then follow the instructions. 



#### Delete BigQuery dataset

  1. In the Google Cloud console, open the BigQuery page. 

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Select arrow_drop_downexpand next to your project and locate your `occupancy_dataset` dataset. 
  3. To delete the dataset, click more_vert **Actions** , click **Delete** , and then follow the instructions. 



#### Delete a stream

  1. In the Google Cloud console, go to the **Streams** page. 

[Go to the Streams tab](https://console.cloud.google.com/ai/vision-ai/video-streams)

  2. Locate your `occupancy-bq-stream` stream. 
  3. To delete the stream, click more_vert **Actions** , click **Delete stream** , and then follow the instructions. 



#### Delete an app

  1. In the Google Cloud console, go to the **Applications** page. 

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

**Note:** You must first undeploy your app before you can delete it. 
  2. Locate your `occupancy-bq-app` app. 
  3. To delete the app, click more_vert **Actions** , click **Delete application** , and then follow the instructions. 



## What's next

  * Read more about [Responsible AI practices](https://ai.google/responsibilities/responsible-ai-practices/).
  * Learn about other components you can add to an app in [Build an app](https://docs.cloud.google.com/vision-ai/docs/build-app).
  * Learn about other output storage and processing options in [Connect app output to a data destination ](https://docs.cloud.google.com/vision-ai/docs/connect-data-destination).
  * Read about how to [Search Warehouse data in the console](https://docs.cloud.google.com/vision-ai/docs/search-streaming-warehouse).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

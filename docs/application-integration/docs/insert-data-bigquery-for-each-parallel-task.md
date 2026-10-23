---
url: https://docs.cloud.google.com/application-integration/docs/insert-data-bigquery-for-each-parallel-task/
title: Insert data into BigQuery using a For Each Parallel task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:05.141419+00:00
---

# Insert data into BigQuery using a For Each Parallel task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/insert-data-bigquery-for-each-parallel-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Insert data into BigQuery using a For Each Parallel task

In this tutorial you'll create an Application Integration and a sub-integration to process a series of records. For each record, the main integration asynchronously invokes the sub-integration, which takes the data for each record and inserts it as a row in a table in a BigQuery dataset.

In this tutorial, you'll complete the following tasks: 

  * Set up a BigQuery connection
  * Set up a sub-integration
  * Set up the main integration
  * Test your integration



## Before you begin

  * Ensure that you have access to Application Integration.
  * Do the following in your Google Cloud project:

    * Grant the following roles to the service account that you want to use to create the connection: 
      * `roles/bigquery.dataEditor`
      * `roles/bigquery.readSessionUser`
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`
    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

If these services have not been enabled for your project previously, you are prompted to enable them when creating the connection in the Create Connection page.




## Set up a BigQuery connection

Start by creating the BigQuery dataset and table to use in this tutorial. After you've created the dataset and table, create a BigQuery connection. You'll use this connection in an integration later on in this tutorial. 

### Set up a BigQuery dataset and table

To set up your BigQuery dataset and table, perform the following steps:

  1. In the [Cloud console](https://console.cloud.google.com/) page, select your Google Cloud project. 
  2. To launch a Cloud Shell session from the Google Cloud console, click the ![Activate Cloud Shell icon](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell** icon in the [Cloud console](https://console.cloud.google.com/). This launches a session in the bottom pane of Google Cloud console. 
  3. To enable BigQuery APIs, enter the following commands in your Cloud Shell terminal: 
         
         export PROJECT_ID=project_id
         export REGION=region
         gcloud services enable --project "${PROJECT_ID}" \
             bigquery.googleapis.com \
             bigquerystorage.googleapis.com

In this command, replace: 
     * `project_id` with the project ID of your Google Cloud project. 
     * `region` with the region that you want to use to create your BigQuery dataset. 
  4. To create a BigQuery dataset with the name `bq_tutorial`, enter the following command in your Cloud Shell terminal: 
         
         bq  --project_id ${PROJECT_ID} --location ${REGION} mk bq_tutorial
             

  5. To create a BigQuery table with the name `tutorial`, enter the following command in your Cloud Shell terminal: 
         
         bq --project_id ${PROJECT_ID} \
                 query  \
                 --nouse_legacy_sql \
               'create table bq_tutorial.tutorial (
               unique_key STRING NOT NULL,
               created_date STRING,
               closed_date STRING,
               agency STRING,
               agency_name STRING,
               complaint_type STRING,
               descriptor STRING,
               location_type STRING,
               incident_zip STRING,
               incident_address STRING,
               street_name STRING,
               cross_street_1 STRING,
               cross_street_2 STRING,
               intersection_street_1 STRING,
               intersection_street_2 STRING,
               address_type STRING,
               city STRING,
               landmark STRING,
               facility_type STRING,
               status STRING,
               due_date STRING,
               resolution_action_updated_date STRING,
               community_board STRING,
               borough STRING,
               x_coordinate_state_plane STRING,
               y_coordinate_state_plane STRING,
               park_facility_name STRING,
               park_borough STRING,
               school_name STRING,
               school_number STRING,
               school_region STRING,
               school_code STRING,
               school_phone_number STRING,
               school_address STRING,
               school_city STRING,
               school_state STRING,
               school_zip STRING,
               school_not_found STRING,
               school_or_citywide_complaint STRING,
               vehicle_type STRING,
               taxi_company_borough STRING,
               taxi_pick_up_location STRING,
               bridge_highway_name STRING,
               bridge_highway_direction STRING,
               bridge_highway_segment STRING,
               road_ramp STRING,
               garage_lot_name STRING,
               ferry_direction STRING,
               ferry_terminal_name STRING,
               latitude STRING,
               longitude STRING,
               location STRING
               ) '
           

  6. Verify that your BigQuery table is created. 
     1. In the [Cloud console](https://console.cloud.google.com/) page, click the menu **Navigation menu**.
     2. In the **Analytics** section, click **BigQuery**. 
     3. Expand your project and confirm that the `bq_tutorial` dataset is listed. 
     4. Expand the **bq_tutorial** dataset and confirm that the `tutorial` table is listed. 
     5. Click the documents table to view the schema. 



### Create a BigQuery connection

Next, you'll create a BigQuery connection. A BigQuery connection lets you insert, read, update and delete rows in a BigQuery table and use the resulting output in an integration. After creating the BigQuery connection, you'll use this connection in an integration later in this tutorial to add rows to the BigQuery table. 

To create a BigQuery connection, complete the following steps:

  1. In the [Cloud console](https://console.cloud.google.com/) page, select your Google Cloud project. 
  2. Open the [connections page](https://console.cloud.google.com//connectors/connections). 
  3. Click **\+ CREATE NEW** to open the **Create Connection** page.
  4. Configure the connection: 
     1. In the **Create Connection** section, complete the following: 
        * **Connector** : Select **BigQuery** from the drop down list of available Connectors.
        * **Connector version** : Select the latest Connector version from the drop down list of available versions. 
        * In the **Connection Name** field, enter a name for the Connection instance. For this tutorial, enter **connector-bq-tutorial**. **Note:** Connection names must meet the following criteria: 
          * Connection names can use letters, numbers, or hyphens.
          * Letters must be lower case.
          * Connection names must begin with a letter and end with a letter or number.
          * Connection names cannot exceed 63 characters.
        * Optionally, add a **Description** of the connection instance.
        * **Service Account** : Select a service account that has the required roles.
        * **Project ID** : Enter the ID of the Google Cloud project where the BigQuery data resides.
        * **Dataset ID** : Enter the ID of the BigQuery dataset that you want to use. For this tutorial, enter **bq_tutorial**.
        * Optionally, click **\+ ADD LABEL** to add a label in the form of a key/value pair.
        * Click **Next**.
     2. **Location** : Select a region from where the connection will run. Supported regions for connectors include: 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

        * Click **Next**.
     3. **Authentication** : The BigQuery connection does not require authentication configuration. Click **Next**. 
     4. **Review** : Review your connection's configuration details. In this section, the connection and authentication details of the new connection are displayed for your review. 
  5. Click **Create**.

**Note:** It could take a few minutes to create the connector.

## Set up a sub-integration

In this tutorial, the sub-integration takes each record sent to it by the main integration and inserts it as a row in the `tutorial` table in the `bq_tutorial` dataset. 

### Create a sub-integration

To create the sub-integration, complete the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Click **Create integration**.
  4. In the **Create Integration** dialog, do the following:
     * Enter a name, for example, enter **Process-each-record** **Note** : Integration names must meet the following requirements: 
       * Names must start and end with letters or numbers.
       * Names cannot contain spaces or more than one dash or underscore in a row.
     * Optionally, enter a description. For example, enter **API Trigger to process each record (sub-integration)**
     * Select the region where you want to create your integration. 
  5. Click **Create** to open the integration editor.



### Add an API Trigger

To add an API Trigger to the integration, do the following: 

  1. In the integration editor, select **Add a task/trigger > Triggers** to display a list of available triggers.
  2. Drag the **API Trigger** element to the integration editor.



### Add a Data Mapping task

To add a Data Mapping task in the integration, complete the following steps: 

  1. Select **+Add a task/trigger > Tasks** in the integration editor to display the list of available tasks. 
  2. Drag the **Data Mapping** element to the integration editor.



### Configure the BigQuery connection

Now you are ready to use the BigQuery connection that you created earlier in the sub-integration. To configure the BigQuery connection in this integration, complete the following steps: 

  1. Select **+Add a task/trigger > Tasks** in the integration editor to display the list of available tasks. 
  2. Drag the **Connectors** element to the integration editor.
  3. Click the **Connectors** task element on the designer to view the task configuration pane.
  4. Click the edit icon on the right panel and update the Label to **Insert row to BigQuery**.
  5. Click **Configure task**. 

The **Configure connector task** dialog appears. 

  6. In the **Configure connector task** dialog, do the following: 
     1. Select the connection region where you created your BigQuery connection. 
     2. Select the BigQuery connection that you want to use. For this tutorial, select **connector-bq-tutorial**. 
     3. Once a connection is chosen, the **Type** column appears. Select **Entities** and then **tutorial** from the list of available entities.
     4. Once a type is chosen, the **Operation** column appears. Select **Create**.
     5. Click **Done** to complete the connection configuration and close the dialog.



### Connect the integration elements

Next, add edge connections to connect the **API Trigger** to the **Data Mapping** task and the **Data Mapping** task to the **Connectors** task. An edge connection is a connection between any two elements in an integration. For more information on edges and edge conditions, see [Edges](https://docs.cloud.google.com/application-integration/docs/edge-overview).

To add the edge connections, complete the following steps:

  1. Click the **Fork** control point at the bottom of the **API Trigger** element. Drag and drop the edge connection at the **Join** control point at the top of the **Data Mapping** element. 
  2. Click the **Fork** control point at the bottom of the **Data Mapping** element. Drag and drop the edge connection at the **Join** control point at the top of the **Connectors** element. 



### Configure the Data Mapping task

To configure the Data Mapping task, complete the following steps: 

  1. In the integration editor, click the **Data Mapping** task to view the task configuration pane. 
  2. Click **Open Data Mapping Editor**. 
  3. In the **Data Mapping Editor** , click **Add** to add a new variable. 
  4. In the **Create Variable** dialog, enter the following information: 
     * **Name:** Enter **record**. 
     * **Data Type:** Select **JSON**. 
     * **Schema:** Select **Infer from a sample JSON payload**. Enter the following sample JSON payload: 
           
           {
                         "unique_key":"304271",
                         "created_date":"02/06/2007 12:00:00 AM",
                         "closed_date":"03/01/2007 12:00:00 AM",
                         "agency":"TLC",
                         "agency_name":"Taxi and Limousine Commission",
                         "complaint_type":"Taxi Complaint",
                         "descriptor":"Driver Complaint",
                         "location_type":"Street",
                         "incident_zip":"10001",
                         "incident_address":"",
                         "street_name":"",
                         "cross_street_1":"",
                         "cross_street_2":"",
                         "intersection_street_1":"WEST 29 STREET",
                         "intersection_street_2":"7 AVENUE",
                         "address_type":"INTERSECTION",
                         "city":"NEW YORK",
                         "landmark":"",
                         "facility_type":"N/A",
                         "status":"Closed",
                         "due_date":"02/28/2007 12:00:00 AM",
                         "resolution_action_updated_date":"03/01/2007 12:00:00 AM",
                         "community_board":"05 MANHATTAN",
                         "borough":"MANHATTAN",
                         "x_coordinate_state_plane":"986215",
                         "y_coordinate_state_plane":"211740",
                         "park_facility_name":"",
                         "park_borough":"MANHATTAN",
                         "school_name":"",
                         "school_number":"",
                         "school_region":"",
                         "school_code":"",
                         "school_phone_number":"",
                         "school_address":"",
                         "school_city":"",
                         "school_state":"",
                         "school_zip":"",
                         "school_not_found":"",
                         "school_or_citywide_complaint":"",
                         "vehicle_type":"",
                         "taxi_company_borough":"",
                         "taxi_pick_up_location":"Other",
                         "bridge_highway_name":"",
                         "bridge_highway_direction":"",
                         "road_ramp":"",
                         "bridge_highway_segment":"",
                         "garage_lot_name":"",
                         "ferry_direction":"",
                         "ferry_terminal_name":"",
                         "latitude":"40.74785373937869",
                         "longitude":"-73.99290823133913",
                         "location":"(40.74785373937869, -73.99290823133913)"
                       }
                     

  5. Click **Create**. 
  6. When the variable is created, in the **Data Mapping Editor** , complete the following steps: 
     * Drag the new **record** variable to the **Input** column. 
     * Drag the **connectorInputPayload** variable to the **Output** column.
  7. Close the **Data Mapping Editor** to return to the integration editor. 



### Publish the sub-integration

To publish the sub-integration, in the integration editor, click **Publish**. 

## Set up the main integration

In this section, you set up the main integration, which uses a **For Each Parallel** task to process each record. This main integration then invokes the sub-integration once for each record. 

### Create the main integration

To create the main integration, complete the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Click **Create integration**.
  4. In the **Create Integration** dialog, do the following:
     * Enter a name, for example, enter **process-records**. **Note** : Integration names must meet the following requirements: 
       * Names must start and end with letters or numbers.
       * Names cannot contain spaces or more than one dash or underscore in a row.
     * Optionally, enter a description. For example, enter **API Trigger to process records (main integration)**
     * Select the region where you want to create your integration. 
  5. Click **Create** to open the integration editor.



### Add an API Trigger

To add an API Trigger to the integration, do the following: 

  1. In the integration editor, select **Add a task/trigger > Triggers** to display a list of available triggers.
  2. Drag the **API Trigger** element to the integration editor.



### Add a For Each Parallel task

To add a For Each Parallel task in the integration, complete the following steps: 

  1. Select **+Add a task/trigger > Tasks** in the integration editor to display the list of available tasks. 
  2. Drag the **For Each Parallel** element to the integration editor.



### Connect the integration elements

Next, add an edge connection to connect the API Trigger to the For Each Parallel task.

To add the edge connection, click the **Fork** control point at the bottom of the API Trigger element. Drag and drop the edge connection at the **Join** control point at the top of the For Each Parallel task element.

### Configure the For Each Parallel task

To configure the For Each Parallel task, complete the following steps: 

  1. In the integration editor, click the **For Each Parallel** task to view the task configuration pane. 
  2. Under **Array Selection > List to iterate**, click **Add new variable** to add a new variable. 
  3. In the **Create Variable** dialog, enter the following information: 
     * **Name:** Enter `records`
     * **Data Type:** Select **JSON**. 
     * **Schema:** Select **Infer from a sample JSON payload**. Enter the following sample JSON payload: 
           
           [{
                           "unique_key":"304271",
                           "created_date":"02/06/2007 12:00:00 AM",
                           "closed_date":"03/01/2007 12:00:00 AM",
                           "agency":"TLC",
                           "agency_name":"Taxi and Limousine Commission",
                           "complaint_type":"Taxi Complaint",
                           "descriptor":"Driver Complaint",
                           "location_type":"Street",
                           "incident_zip":"10001",
                           "incident_address":"",
                           "street_name":"",
                           "cross_street_1":"",
                           "cross_street_2":"",
                           "intersection_street_1":"WEST 29 STREET",
                           "intersection_street_2":"7 AVENUE",
                           "address_type":"INTERSECTION",
                           "city":"NEW YORK",
                           "landmark":"",
                           "facility_type":"N/A",
                           "status":"Closed",
                           "due_date":"02/28/2007 12:00:00 AM",
                           "resolution_action_updated_date":"03/01/2007 12:00:00 AM",
                           "community_board":"05 MANHATTAN",
                           "borough":"MANHATTAN",
                           "x_coordinate_state_plane":"986215",
                           "y_coordinate_state_plane":"211740",
                           "park_facility_name":"",
                           "park_borough":"MANHATTAN",
                           "school_name":"",
                           "school_number":"",
                           "school_region":"",
                           "school_code":"",
                           "school_phone_number":"",
                           "school_address":"",
                           "school_city":"",
                           "school_state":"",
                           "school_zip":"",
                           "school_not_found":"",
                           "school_or_citywide_complaint":"",
                           "vehicle_type":"",
                           "taxi_company_borough":"",
                           "taxi_pick_up_location":"Other",
                           "bridge_highway_name":"",
                           "bridge_highway_direction":"",
                           "road_ramp":"",
                           "bridge_highway_segment":"",
                           "garage_lot_name":"",
                           "ferry_direction":"",
                           "ferry_terminal_name":"",
                           "latitude":"40.74785373937869",
                           "longitude":"-73.99290823133913",
                           "location":"(40.74785373937869, -73.99290823133913)"
                         }]
                       

  4. Click **Create**. 
  5. In the **Sub-integration Details** section, enter the following information: 
     * **API Trigger ID:** Select the API Trigger element in the sub-integration. For example, select **Process-each-record_API_1**. 
     * **Execution strategy:** Select **ASYNC**. 
     * Select **Run a single integration**. 
  6. In the **On each execution** section, for **Where to map individual array elements** , enter the name of the variable in the data mapping task in the sub-integration. In this case, enter **record**. The sub-integration variables are listed only for publsihed integrations. If the variables aren't listed, refresh the page, as it takes some time for the variables to be visible after the sub-integration is published. 



### Publish the main integration

To publish the main integration, in the integration editor, click **Publish**. 

## Test your integration

To test your integration, complete the following steps: 

  1. Download sample data to your Cloud Shell: 
     1. To launch a Cloud Shell session from the Google Cloud console, click the ![Activate Cloud Shell icon](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell** icon in the [Cloud console](https://console.cloud.google.com/). This launches a session in the bottom pane of Google Cloud console. 
     2. Enter the following command in your Cloud Shell terminal: 
            
            wget https://raw.githubusercontent.com/GoogleCloudPlatform/application-integration-samples/main/assets/bq-sample-dataset.json
                    

     3. To verify that the sample data was downloaded, enter the following command in your Cloud Shell terminal: 
            
            ls -la bq-sample-dataset.json

The downloaded file is listed in the Cloud Shell terminal. 
  2. To select three random entries from the sample dataset and store them in a way that you can pass them to the integration, enter the following commands in your Cloud Shell terminal: 
         
         AUTH=$(gcloud auth print-access-token)
         export SAMPLE_DOCS=$(jq $(r=$((RANDOM % 1000)) ; echo ".[$r:$((r + 3))]") < bq-sample-dataset.json | jq -Rs '.')
                     
         generate_post_data()
           {
             cat <<EOF
               {
                 "triggerId": "api_trigger/process-records_API_1",
                 "inputParameters": 
                   {
                     "records": 
                       {
                         "jsonValue": $SAMPLE_DOCS
                       }
                   }
               }
               EOF
           }

  3. To start the testing, enter the following command in your Cloud Shell terminal: 
         
         curl -X POST \
           https://integrations.googleapis.com/v1/projects/project_id/locations/region/integrations/process-records:execute \
           -H "Authorization: Bearer $AUTH" \
           -H "Content-Type: application/json" \
           -d "$(generate_post_data)"

In this command, replace: 
     * `project_id` with the project ID of your Google Cloud project. 
     * `region` with the region where you created your integration. 
This command invokes the main integration and passes the entries from the sample dataset to the main integration. The main integration then passes each entry to the sub-integration, which adds the data as a row in your BigQuery table. 
  4. To verify that your BigQuery table now contains these records, perform the following steps: 
     1. In the [Cloud console](https://console.cloud.google.com/) page, click the menu **Navigation menu**.
     2. In the **Analytics** section, click **BigQuery**. 
     3. Expand your project and click the `bq_tutorial` dataset. 
     4. Expand the **bq_tutorial** dataset and click the `tutorial` table. 
     5. Click the **Table Explorer** tab to view the inserted records. 



## What's next

Try building integrations with other connectors. For the list of all the supported connectors, see [ Connector reference](https://docs.cloud.google.com/integration-connectors/docs/connector-reference-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

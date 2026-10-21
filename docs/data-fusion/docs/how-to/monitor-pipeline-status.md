---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/monitor-pipeline-status/
title: Monitor pipeline status \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:36.359340+00:00
---

# Monitor pipeline status  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/monitor-pipeline-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Monitor pipeline status Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to publish Cloud Data Fusion pipeline events, such as pipeline status, to Pub/Sub topics. It also describes how to create Cloud Run functions that process the Pub/Sub messages and take actions, such as identifying and retrying failed pipelines.

## Before you begin

  * [Create a topic](https://docs.cloud.google.com/pubsub/docs/create-topic#create_a_topic_2) where Pub/Sub can publish Cloud Data Fusion pipeline events.



### Required roles

To ensure that the Cloud Data Fusion Service Account has the necessary permissions to publish pipeline events to a Pub/Sub topic, ask your administrator to grant the [Pub/Sub Publisher ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) IAM role to the Cloud Data Fusion Service Account on the project where you create the Pub/Sub topic. **Important:** You must grant this role to the Cloud Data Fusion Service Account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors.  For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the Cloud Data Fusion Service Account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Manage event publishing in a Cloud Data Fusion instance

You can manage event publishing in new and existing Cloud Data Fusion instances using the REST API in versions 6.7.0 and later.

### Publish events in a new instance

Create a new instance and include the `EventPublishConfig` field. For more information about required fields for new instances, see the [Instances resource](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances) reference.
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://datafusion.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances?instanceId=INSTANCE_ID" \
      -d '{
        "version": "VERSION_NUMBER",
        "event_publish_config": {
          "enabled": true,
          "topic": "projects/PROJECT_ID/topics/TOPIC_ID"
        }
      }'
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID
  * `LOCATION`: the location of your project
  * `INSTANCE_ID`: the ID of your Cloud Data Fusion instance
  * `VERSION_NUMBER`: The version of Cloud Data Fusion where you create the instance–for example, `6.10.1`
  * `TOPIC_ID`: the ID of the Pub/Sub topic



### Enable event publishing in an existing Cloud Data Fusion instance

Update the [`EventPublishConfig`](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances#eventpublishconfig) field in an existing Cloud Data Fusion instance:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      https://datafusion.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID?updateMask=event_publish_config \
      -d '{
        "event_publish_config": {
          "enabled": true,
          "topic": "projects/PROJECT_ID/topics/TOPIC_ID"
        }
    }'
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID
  * `LOCATION`: the [location](https://cloud.google.com/data-fusion/pricing#supported_regions) of your project
  * `INSTANCE_ID`: the ID of your Cloud Data Fusion instance
  * `TOPIC_ID`: the ID of the Pub/Sub topic



### Remove event publishing from an instance

To remove event publishing from an instance, update the event publishing `enabled` value to `false`:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \ "https://datafusion.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID?updateMask=event_publish_config" \
      -d '{ "event_publish_config": { "enabled": false } }'
    

## Create functions to read Pub/Sub messages

Cloud Run functions can read Pub/Sub messages and act on them, such as retrying failed pipelines. To make a Cloud Run functions, do the following:

  1. In the Google Cloud console, go to the **Cloud Run functions** page.

[Go to Cloud Run functions](https://console.cloud.google.com/functions/list)

  2. Click **Create function**.

  3. Enter a function name and region.

  4. In the **Trigger type** field, select **Cloud Pub/Sub**.

  5. Enter the Pub/Sub topic ID.

  6. Click **Next**.

  7. Add functions to read the Pub/Sub messages and take other actions. For example, you can add functions for the following use cases:

     * Send alerts for pipeline failures.
     * Send alerts for KPIs, such as record count or run information.
     * Restart a failed pipeline that hasn't been rerun.

For Cloud Run function examples, see the use case section.

  8. Click **Deploy**. For more information, see [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/docs/deploy#console).




### Use case: Document pipeline status and retry failed pipelines

The following example Cloud Run functions read Pub/Sub messages about the pipeline run status, and then retry the failed pipelines in Cloud Data Fusion.

These example functions refer to the following Google Cloud components:

  * **Google Cloud project** : the project where Cloud Run functions and Pub/Sub topics are created
  * **Pub/Sub topic** : the Pub/Sub topic linked to your Cloud Data Fusion instance
  * **Cloud Data Fusion instance** : the Cloud Data Fusion instance where you design and execute pipelines
  * **BigQuery table** : the BigQuery table that captures the pipeline status and the run and rerun details
  * **Cloud Run function** : the Cloud Run function where you deploy the code that retries failed pipelines


  1. The following Cloud Run function example reads the Pub/Sub messages about Cloud Data Fusion status events.
         
         # Triggered from a message on a Pub/Sub topic.
         @functions_framework.cloud_event
         def cdf_event_trigger(cloud_event):
         
         decoded_message = base64.b64decode(cloud_event.data["message"]["data"]).decode('utf-8') # Decode Pub/Sub message.
         pubsub_message = json.loads(decoded_message)
         
         # Extract pipeline run details.
         projectName = pubsub_message["projectName"]
         publishTime = pubsub_message["publishTime"]
         instanceName = pubsub_message["instanceName"]
         namespace = pubsub_message["programStatusEventDetails"]["namespace"]
         applicationName = pubsub_message["programStatusEventDetails"]["applicationName"]
         status = pubsub_message["programStatusEventDetails"]["status"]
         event_timestamp = pd.to_datetime(pubsub_message["programStatusEventDetails"]["eventTime"], unit = 'ms')
         
         print(f"projectName: {projectName}")
         print(f"publishTime: {publishTime}")
         print(f"instanceName: {instanceName}")
         print(f"namespace: {namespace}")
         print(f"applicationName: {applicationName}")
         print(f"status: {status}")
         print(f"event timestamp: {event_timestamp}")
         try:
             error = pubsub_message["programStatusEventDetails"]["error"]
             print(f"error: {error}")
         except:
             print(f"Pipeline: {applicationName}'s current status: {status}")
         

  2. The following example function creates and saves a BigQuery table, and queries the pipeline run details.
         
         # Global variables.
         pipeline_rerun_count = 0
         has_pipeline_failed_and_rerun_recently = False # Timeframe: within last 60 minutes.
         table_id = "bigquery-table-1" # The BigQuery target table for storing pipeline run information.
         
         # Update BigQuery table with the pipeline status and rerun details.
         schema=[
             bigquery.SchemaField("Project_Name", "STRING"),
             bigquery.SchemaField("Instance_Name", "STRING"),
             bigquery.SchemaField("Namespace", "STRING"),
             bigquery.SchemaField("Pipeline_Name", "STRING"),
             bigquery.SchemaField("Pipeline_Status", "STRING"),
             bigquery.SchemaField("Event_Timestamp", "TIMESTAMP"),
             bigquery.SchemaField("Pipeline_Rerun_Count", "INTEGER"),
         ]
         
         # Prepare DataFrame to load the data in BigQuery.
         data = {'Project_Name':[projectName], 'Instance_Name':[instanceName], 'Namespace':[namespace], 'Pipeline_Name':[applicationName], 'Pipeline_Status':[status], 'Event_Timestamp':[event_timestamp], 'Pipeline_Rerun_Count':[pipeline_rerun_count]}
         dataframe = pd.DataFrame(data)
         
         # Prepare BigQuery data load job configuration.
         job_config = bigquery.LoadJobConfig(schema=schema)
         
         job = bq_client.load_table_from_dataframe(dataframe, table_id, job_config=job_config)
         job.result()  # Wait for the job to complete.
         
         table = bq_client.get_table(table_id)  # Make an API request.
         print("BigQuery table: {} updated.".format(table_id))
         

  3. The following example function checks for pipelines that have failed and whether they were rerun in the last hour.
         
         bq_client = bigquery.Client()
         
         if status == "FAILED":
             print(f"ALERT -- Pipeline: {applicationName} has failed. Checking for rerun: pipeline hasn't failed and rerun in the last 60 minutes.")
         
             QUERY = f"""
                 SELECT * FROM `{table_id}`
                 WHERE Pipeline_Name = "{applicationName}" AND Pipeline_Status = "FAILED"
                 AND "{event_timestamp}" < DATETIME_ADD(Event_Timestamp, INTERVAL 60 MINUTE)
                 AND Pipeline_Rerun_Count > 0
                 """
         
             query_job = bq_client.query_and_wait(QUERY)  # API request.
             row_count = query_job.total_rows  # Waits for query to finish.
             print(f"Query job result row count: {row_count}")
         
             if (row_count > 0):
                 print("Pipeline has FAILED and rerun recently...")
                 global has_pipeline_failed_and_rerun_recently
                 has_pipeline_failed_and_rerun_recently = True
         

  4. If the failed pipeline hasn't run recently, the following example function reruns the failed pipeline.
         
         if not has_pipeline_failed_and_rerun_recently:
             applicationName = applicationName
             auth_token = get_access_token()
             post_headers = {"Authorization": "Bearer " + auth_token,"Accept": "application/json"}
             cdap_endpoint = "https://instance1-project1-dot-location1.datafusion.googleusercontent.com/api"
             run_pipeline_endpoint = cdap_endpoint + "/v3/namespaces/{}/apps/{}/workflows/DataPipelineWorkflow/start".format(namespace, applicationName)
         
             # Start the job.
             response = requests.post(run_pipeline_endpoint,headers=post_headers)
             print(f"Response for restarting the failed pipeline: {response}")
             global pipeline_rerun_count
             pipeline_rerun_count = 1
         




## What's next

  * Learn how to [write Cloud Run functions](https://docs.cloud.google.com/functions/docs/writing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

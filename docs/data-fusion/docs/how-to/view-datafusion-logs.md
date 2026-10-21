---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/view-datafusion-logs/
title: View Cloud Data Fusion logs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:35.755356+00:00
---

# View Cloud Data Fusion logs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/view-datafusion-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  View Cloud Data Fusion logs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to access and view pipeline logs and service logs for Cloud Data Fusion.

Starting with Cloud Data Fusion version 6.11, pipeline logs and service logs are available in Cloud Logging.

## About log types

Cloud Data Fusion generates several types of logs to help monitor and troubleshoot data integration processes:

Pipeline logs
    These logs provide detailed information about individual pipeline runs, including preview runs. They cover all stages of a pipeline run, such as pre-run setup, job execution, and post-run activities.

Service logs
    These logs provide detailed information about Cloud Data Fusion system services, such as AppFabric and AppFabric processor.

Audit logs
    Cloud Data Fusion generates audit logs, such as [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity). For more information, see [Cloud Data Fusion audit logging](https://docs.cloud.google.com/data-fusion/docs/how-to/audit-logging). 

Advanced pipeline logs
    These logs provide detailed information about individual pipeline runs. These logs are particularly useful for troubleshooting pipeline failures, as they capture information even before the Managed Service for Apache Spark cluster finishes provisioning, which can help identify cluster issues or delays. For more information, see [View advanced pipeline logs in Cloud Logging](https://docs.cloud.google.com/data-fusion/docs/how-to/viewing-stackdriver-logs). 

## Pricing

Cloud Logging and Cloud Monitoring usage incurs charges. For more information, see [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing).

## Optional: Import the Cloud Data Fusion Logging dashboard

To view pipeline logs and service logs using the Cloud Data Fusion Logging dashboard, import the dashboard:

  1. In the Google Cloud console, go to the Cloud Monitoring **Dashboards** page.

[Go to Dashboards](https://console.cloud.google.com/monitoring/dashboards)

  2. Click **View dashboard templates**.

  3. Search for **Cloud Data Fusion Logging** and select the dashboard.

  4. Click playlist_add **Add Cloud Data Fusion Logging dashboard to your list**.




## View pipeline logs

You can view pipeline logs using the Cloud Data Fusion Logging dashboard or directly in the Logs Explorer.

### View pipeline logs using dashboard

  1. If you haven't done already, import the **Cloud Data Fusion Logging** dashboard.

  2. In the **My dashboards** section, click **Cloud Data Fusion Logging**.

  3. In the **Pipeline logs** section, view the list of pipeline logs. You can filter the logs by severity, field names, and values.

To refine your search using queries, use Logs Explorer.




### View pipeline logs in Logs Explorer

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Enter the following query:
         
         resource.type="datafusion.googleapis.com/PipelineV2"
         

This displays the list of pipeline logs. You can use filters to refine the results.




### Filter pipeline logs

You can filter pipeline logs by run ID, instance ID, pipeline ID, location, namespace, or custom labels.

Every Cloud Data Fusion pipeline run is assigned a unique `RunID`. After you deploy and run your pipeline, you can find the `RunID` of your pipeline and view the corresponding pipeline logs.

To filter pipeline logs by `RunID`, follow these steps:

  1. [Get the pipeline's RunID](https://docs.cloud.google.com/data-fusion/docs/how-to/viewing-stackdriver-logs#get_the_pipelines_runid).

  2. In the Google Cloud console, go to the **Logs Explorer** page.

  3. Enter the following query:
         
         resource.type="datafusion.googleapis.com/PipelineV2" resource.labels.run_id=RUN_ID
         




## View service logs

You can view service logs using the Cloud Data Fusion Logging dashboard or in the Logs Explorer.

### View service logs using dashboard

  1. If you haven't done already, import the **Cloud Data Fusion Logging** dashboard.

  2. In the **My dashboards** section, click **Cloud Data Fusion Logging**.

  3. In the **Service logs** section, view the list of service logs. You can filter the logs by severity, field names, and values.

To refine your search using queries, use Logs Explorer.




### View service logs in Logs Explorer

Starting with Cloud Data Fusion version 6.11.1.1, system service logs use the `InstanceV3` monitored-resource (`datafusion.googleapis.com/InstanceV3`) by default. These logs use the `services-v3` log name suffix and don't include the `org_id` or `namespace` labels found in the previous version. While `InstanceV2` log emission is disabled by default for new and upgraded instances, you can re-enable `InstanceV2` logging using the Cloud Data Fusion REST API if your operations rely on the legacy labels.

To view service logs in Logs Explorer, follow these steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Find the service logs by entering the specific query for that service.

Service name | Log query for InstanceV2 | Log query for InstanceV3  
---|---|---  
Appfabric | 
         
         resource.type="datafusion.googleapis.com/InstanceV2"
         labels.".serviceId"="appfabric"
         

| 
         
         resource.type="datafusion.googleapis.com/InstanceV3"
         labels.".serviceId"="appfabric"
           
  
AppFabric processor | 
         
         resource.type="datafusion.googleapis.com/InstanceV2"
         labels.".serviceId"="appfabric.processor"
         

| 
         
         resource.type="datafusion.googleapis.com/InstanceV3"
         labels.".serviceId"="appfabric.processor"
           
  
Dataset executor | 
         
         resource.type="datafusion.googleapis.com/InstanceV2"
         labels.".serviceId"="dataset.executor"
         

| 
         
         resource.type="datafusion.googleapis.com/InstanceV3"
         labels.".serviceId"="dataset.executor"
           
  
Log saver | 
         
         resource.type="datafusion.googleapis.com/InstanceV2"
         labels.".serviceId"="log.saver"
         

| 
         
         resource.type="datafusion.googleapis.com/InstanceV3"
         labels.".serviceId"="log.saver"
           
  
Metadata service | 
         
         resource.type="datafusion.googleapis.com/InstanceV2"
         labels.".serviceId"="metadata.service"
         

| 
         
         resource.type="datafusion.googleapis.com/InstanceV3"
         labels.".serviceId"="metadata.service"
           
  
Metrics | 
         
         resource.type="datafusion.googleapis.com/InstanceV2"
         labels.".serviceId"="metrics"
         

| 
         
         resource.type="datafusion.googleapis.com/InstanceV3"
         labels.".serviceId"="metrics"
           
  
Pipeline Studio | 
         
         resource.type="datafusion.googleapis.com/InstanceV2" 
         resource.labels.namespace="system"
         labels.".userserviceid"="studio"
         

| 
         
         resource.type="datafusion.googleapis.com/InstanceV3"
         labels.".userserviceid"="studio"
           
  
Runtime | 
         
         resource.type="datafusion.googleapis.com/InstanceV2"
         labels.".serviceId"="runtime"
         

| 
         
         resource.type="datafusion.googleapis.com/InstanceV3"
         labels.".serviceId"="runtime"
           
  
Wrangler service | 
         
         resource.type="datafusion.googleapis.com/InstanceV2"
         resource.labels.namespace="system"
         labels.".applicationId"="dataprep"
         labels.".userserviceid"="service"
         

| 
         
         resource.type="datafusion.googleapis.com/InstanceV3"
         labels.".applicationId"="dataprep"
         labels.".userserviceid"="service"
           
  



### Enable InstanceV2 logs

By default, Cloud Data Fusion instances running version 6.11.1.1 or later disable `InstanceV2` logging. If your operations require the previous logging format (for example, if you rely on the `org_id` or `namespace` labels), you can re-enable `InstanceV2` logs using the Cloud Data Fusion REST API.

To enable `InstanceV2` logs, use the [`instances.patch`](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/patch) method with `enable_instance_v2_logs` set to `true`. This setting emits both `InstanceV2` and `InstanceV3` logs.
    
    
       curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-GFE-SSL: yes" \
      -H "Host: datafusion.googleapis.com" \
      -d '{"loggingConfig": {"enable_instance_v2_logs": true}}' \
      "https://datafusion.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID?updateMask=loggingConfig"
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID
  * `LOCATION`: the [location](https://cloud.google.com/data-fusion/pricing#supported_regions) of your instance
  * `INSTANCE_ID`: the ID of your Cloud Data Fusion instance



### Configurable logging in Cloud Data Fusion

Cloud Data Fusion 6.11.0 offers configurable logging, with Cloud Logging enabled by default. While disabling Cloud Logging is possible, it's strongly recommended to keep it enabled to ensure you have access to critical pipeline and instance logs.

To disable Cloud Logging, run the following command:
    
    
    echo '{ "loggingConfig": {"instance_cloud_logging_disabled": "true"}}' | curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        --data @- \
        "https://datafusion.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances?instanceId=$INSTANCE_ID?updateMask=logging_config"
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID
  * `LOCATION`: the [location](https://cloud.google.com/data-fusion/pricing#supported_regions) of your instance
  * `INSTANCE_ID`: the ID of your Cloud Data Fusion instance



## What's next

  * Learn more about [Cloud Data Fusion audit logging](https://docs.cloud.google.com/data-fusion/docs/how-to/audit-logging).
  * Learn how to [view advanced pipeline logs](https://docs.cloud.google.com/data-fusion/docs/how-to/viewing-stackdriver-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

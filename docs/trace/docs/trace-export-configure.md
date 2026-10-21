---
url: https://docs.cloud.google.com/trace/docs/trace-export-configure/
title: Configure exports \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:38.071744+00:00
---

# Configure exports  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/trace-export-configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Configure exports Stay organized with collections  Save and categorize content based on your preferences. 

**Caution** : As of February 18, 2026, the export of span data to BigQuery by using Cloud Trace sinks is [deprecated](https://docs.cloud.google.com/stackdriver/docs/deprecations). Sinks used to export spans to BigQuery will be removed on or after February 18, 2027. You can't create or modify trace sinks. For information about how to view your span data in BigQuery, see [Migrate to Observability Analytics](https://docs.cloud.google.com/trace/docs/analytics-migrate). 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to export traces by using the Cloud Trace API and the Google Cloud CLI. You must use version 274.0.0 or later of the Google Cloud CLI. For information on how to update the Google Cloud CLI, see [`gcloud components update` ](https://docs.cloud.google.com/sdk/gcloud/reference/components/update).

Some samples on this page were generated using `curl`. For information on configuring this tool, see Using `curl`.

For an example that illustrates using the Google Cloud CLI commands to list, create, describe, update, and delete a sink, see End-to-end example.

## Terminology

To simplify the examples on this page, environment variables have been used.

The Google Cloud CLI examples use the following environment variables:

  * `SINK_ID`: The name, or the identifier, of the sink. For example, `my-sink`. You don't need to provide the fully qualified command to the Google Cloud CLI, as it can determine your Google Cloud project.
  * `DESTINATION`: Stores the fully qualified name of the destination. This must be a BigQuery dataset. For example, a valid destination is:
        
        bigquery.googleapis.com/projects/DESTINATION_PROJECT_NUMBER/datasets/DATASET_ID
        

where `DESTINATION_PROJECT_NUMBER` is the Google Cloud project number of the destination, and `DATASET_ID` is the BigQuery dataset identifier.

**Note:** There is limited semantic checking on the format of the destination. For example, if you omit the `DATASET_ID` when you issue a create command, the create command doesn't fail but traces won't be exported successfully.



The `curl` examples use the following environment variables:

  * `ACCESS_TOKEN`: Stores the authorization token. For more information, see Using `curl`.
  * `PROJECT_ID`: Stores the Google Cloud project identifier or project number.
  * `PROJECT_NUMBER`: Stores the Google Cloud project number.
  * `SINK_ID`: The name, or the identifier, of the sink. For example, `my-sink`.
  * `SINK_BODY`: Stores the description of a [`TraceSink`](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2beta1/projects.traceSinks#TraceSink) resource. The TraceSink resource includes a name and the sink destination. The name must specify the Google Cloud project _number_.
  * `DESTINATION`: Stores the fully qualified name of the destination. This must be a BigQuery dataset.



## Configuring the destination

To export traces to BigQuery, do the following:

  1. Create the destination dataset.

  2. Create the sink by using the Cloud Trace API or Google Cloud CLI. For details, see Creating a sink.

  3. Grant the sink the role of [`dataEditor`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor) for your BigQuery dataset:

     1. Obtain the writer identity from the sink. For information on writer identity, see [Sink properties and terminology](https://docs.cloud.google.com/trace/docs/trace-export-overview#sink-terms).

The writer identity for a sink is included in the response data to the create command. It is also included in the response data of the list command.

     2. Add the sink's writer identity as a service account to your BigQuery dataset and give it the role of [BigQuery data editor](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor).

        * To add the permissions using Google Cloud console, see [Controlling access to a dataset](https://docs.cloud.google.com/bigquery/docs/dataset-access-controls).

        * To add the permissions using Google Cloud CLI, use the `add-iam-policy-binding` command and supply your Google Cloud project identifier and the sink's writer identity:
              
              gcloud projects add-iam-policy-binding ${DESTINATION_PROJECT_ID} \
                --member serviceAccount:${WRITER_IDENTITY} \
                --role roles/bigquery.dataEditor
              

In previous command, `WRITER_IDENTITY` is an environment variable that stores the writer identity of the sink and `DESTINATION_PROJECT_ID` is the Google Cloud project identifier of the BigQuery dataset.




## Listing sinks

To list all sinks in your Google Cloud project, including their writer identities, invoke the [`traceSinks.list`](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2beta1/projects.traceSinks/list) method.

### gcloud

To list the sinks defined with the default project by using the Google Cloud CLI, run the following command:
    
    
    gcloud alpha trace sinks list
    

### Protocol

To list sinks by using `curl`, send a `GET` request to:
    
    
    https://cloudtrace.googleapis.com/v2beta1/projects/${PROJECT_NUMBER}/traceSinks
    

For example, the following request retrieves all sinks: 
    
    
    curl --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}"  https://cloudtrace.googleapis.com/v2beta1/projects/${PROJECT_NUMBER}/traceSinks
    

## Show details of a specific sink

To show the details of a specific sink that is in your Google Cloud project, invoke the [`traceSinks.get`](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2beta1/projects.traceSinks/get) method.

### gcloud

To display the details of the sink whose identifier is stored in `SINK_ID` by using the Google Cloud CLI, run the following command: 
    
    
    gcloud alpha trace sinks describe ${SINK_ID}
    

### Protocol

To display the details of the sink whose identifier is stored in `SINK_ID` by using `curl`, send a `GET` request to:
    
    
    https://cloudtrace.googleapis.com/v2beta1/projects/${PROJECT_NUMBER}/traceSinks/%{SINK_ID}
    

For example, the following request retrieves the details of the specified sink:
    
    
    curl --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}"  https://cloudtrace.googleapis.com/v2beta1/projects/${PROJECT_NUMBER}/traceSinks/${SINK_ID}
    

## Creating a sink

To create a sink in your Google Cloud project, invoke the [`traceSinks.create`](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2beta1/projects.traceSinks/create) method. The destination for a sink must be a BigQuery dataset.

This dataset must exist before you create the sink. Trace doesn't verify the existence of the destination. See [Creating datasets](https://docs.cloud.google.com/bigquery/docs/datasets) for information on creating BigQuery datasets.

### gcloud

To create a sink by using the Google Cloud CLI, run the following command: 
    
    
    gcloud alpha trace sinks create ${SINK_ID} ${DESTINATION}
    

### Protocol

To create a sink by using curl, send a `POST` request to:
    
    
    https://cloudtrace.googleapis.com/v2beta1/projects/${PROJECT_NUMBER}/traceSinks
    

For example, to create a sink named `test_sink` to export trace spans to `test_dataset` in the project with `${PROJECT_NUMBER}`, define the environment variable `SINK_BODY` as shown:
    
    
    SINK_BODY='{"name":"projects/12345/traceSinks/test_sink","output_config":{"destination":"bigquery.googleapis.com/projects/12345/datasets/test_dataset"}}'
    

To create the sink, run the following command: 
    
    
    curl --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}"  --header "Content-Type: application/json"  -X POST -d ${SINK_BODY} https://cloudtrace.googleapis.com/v2beta1/projects/${PROJECT_NUMBER}/traceSinks
    

It might take several minutes after you create a sink before trace spans are exported to the destination.

## Deleting a sink

To delete a sink that is in your Google Cloud project, invoke the [`traceSinks.delete`](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2beta1/projects.traceSinks/delete) command.

### gcloud

To delete the sink whose identifier is stored in `SINK_ID` by using the Google Cloud CLI, run the following command: 
    
    
    gcloud alpha trace sinks delete ${SINK_ID}
    

### Protocol

To delete the sink whose identifier is stored in `SINK_ID` by using `curl`, send a `DELETE` request to:
    
    
    https://cloudtrace.googleapis.com/v2beta1/projects/${PROJECT_NUMBER}/traceSinks/${SINK_ID}
    

For example, the following request deletes a sink: 
    
    
    curl --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}"  -X DELETE https://cloudtrace.googleapis.com/v2beta1/projects/${PROJECT_NUMBER}/traceSinks/${SINK_ID}
    

## Updating a sink

To update a sink that is in your Google Cloud project, invoke the [`traceSinks.patch`](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2beta1/projects.traceSinks/patch) command.

This dataset must exist before you create the sink. Trace doesn't verify the existence of the destination.

### gcloud

To update the sink whose identifier is stored in `SINK_ID` by using the Google Cloud CLI, run the following command:
    
    
    gcloud alpha trace sinks update ${SINK_ID} ${DESTINATION}
    

The environment variable `DESTINATION`, stores the new destination for the sink. 

### Protocol

To update the destination of the sink whose identifier is stored in `SINK_ID` by using `curl`, send a `PATCH` request to:
    
    
    https://cloudtrace.googleapis.com/v2beta1/projects/${PROJECT_NUMBER}/traceSinks/${SINK_ID}
    

For example, the following request updates the destination of a sink: 
    
    
    curl --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}"  --header "Content-Type: application/json"  -X PATCH -d ${SINK_BODY} https://cloudtrace.googleapis.com/v2beta1/projects/${PROJECT_NUMBER}/traceSinks/${SINK_ID}?update_mask=output_config.destination
    

For an example of a `SINK_BODY`, see the example to create a sink.

It might take several minutes after you update a sink before trace spans are exported to the new destination.

## End-to-end example

This section illustrates using the Google Cloud CLI commands to list, create, describe, update, and delete a sink. The commands were executed for a project with the project identifier `a-sample-project`. This project was pre-configured to contain 2 BigQuery datasets. Lastly, in these examples, the sink and the destination are in the same project. This isn't a requirement. The sink and destination can be in different Google Cloud projects.

### Configuration steps

  1. Verify the default project setting:
         
         $ gcloud config list
         

Sample response:
         
         [compute]
         zone = us-east1-b
         [core]
         account = user@example.com
         disable_usage_reporting = True
         project = a-sample-project
         
         Your active configuration is: [default]
         

  2. Verify that Google Cloud CLI is at least 274.0.0:
         
         $ gcloud --version
         

Sample response:
         
         Google Cloud SDK 275.0.0
         alpha 2020.01.03
         beta 2020.01.03
         bq 2.0.51
         core 2020.01.03
         gsutil 4.46
         kubectl 2020.01.03
         

  3. Identify available datasets in the default project:
         
         $ bq ls
         

Sample response:
         
         datasetId
          ---------------
           dataset_1
           dataset_other
         

Note that the first time you use `bq` commands, you might need to select the project.




### Setup the environment variables

  1. Set the env variables used by the Google Cloud CLI command:
         
         $ PROJECT_ID=a-sample-project
         $ PROJECT_NUMBER=123456789000
         $ SINK_ID=a-sample-sink
         $ DATA_SET_NAME=dataset_1
         $ DESTINATION=bigquery.googleapis.com/projects/${PROJECT_NUMBER}/datasets/${DATA_SET_NAME}
         

In this example, the destination and sink are in the same project. This isn't a requirement. The sink and destination can be in different Google Cloud projects.

  2. Verify the settings:
         
         $ echo $SINK_ID
         a-sample-sink
         $ echo $DATA_SET_NAME
         dataset_1
         $ echo $DESTINATION
         bigquery.googleapis.com/projects/123456789000/datasets/dataset_1
         




### List sinks

To list all sinks, run the following command:
    
    
    $ gcloud alpha trace sinks list
    

Because this project doesn't have any sinks, the response is:
    
    
    Listed 0 items.
    

### Create a sink

  1. To create a sink, run the following command:
         
         $ gcloud alpha trace sinks create ${SINK_ID} ${DESTINATION}
         

Sample response:
         
         You can give permission to the service account by running the following command.
         gcloud projects add-iam-policy-binding bigquery-project \
         --member serviceAccount:export-0000001cbe991a08-3434@gcp-sa-cloud-trace.iam.gserviceaccount.com \
         --role roles/bigquery.dataEditor
         

Notice that the service account name includes `export-0000001cbe991a08-3434`. The number 0000001cbe991a08 is the hexadecimal representation of the `PROJECT_NUMBER`. The value `3434` is a random value.

Prior to executing the Google Cloud CLI in the previous response, you **must** replace `bigquery-project` with your project identifier.

  2. Verify sink was created:
         
         $ gcloud alpha trace sinks list
         

Sample response:
         
         NAME           DESTINATION                                                       WRITER_IDENTITY
         a-sample-sink  bigquery.googleapis.com/projects/123456789000/datasets/dataset_1  export-0000001cbe991a08-3434@gcp-sa-cloud-trace.iam.gserviceaccount.com
         

  3. Describe the sink in detail:
         
         $ gcloud alpha trace sinks describe ${SINK_ID}
         

Sample response:
         
         destination: bigquery.googleapis.com/projects/123456789000/datasets/dataset_1
         name: a-sample-sink
         writer_identity: export-0000001cbe991a08-3434@gcp-sa-cloud-trace.iam.gserviceaccount.com
         

  4. Grant the `bigquery.dataEditor` permission to the write identity of the sink. The sink create command returns a Google Cloud CLI command that you can use to update the permission.

For this command to be successful, do the following:

     * Ensure that you have permission to modify the destination permissions.
     * Replace `bigquery-project` with your project identifier:
    
    gcloud projects add-iam-policy-binding ${PROJECT_ID} --member serviceAccount:export-0000001cbe991a08-3434@gcp-sa-cloud-trace.iam.gserviceaccount.com --role roles/bigquery.dataEditor
    

Notice that the first entry in this sample response is the writer identity of the sink:



    
    
        Updated IAM policy for project [a-sample-project].
        bindings:
        - members:
          - serviceAccount:export-0000001cbe991a08-3434@gcp-sa-cloud-trace.iam.gserviceaccount.com
          role: roles/bigquery.dataEditor
        - members:
          - user:user@example.com
          role: roles/cloudtrace.admin
        - members:
          - serviceAccount:service-123456789000@compute-system.iam.gserviceaccount.com
          role: roles/compute.serviceAgent
        - members:
          - serviceAccount:service-123456789000@container-engine-robot.iam.gserviceaccount.com
          role: roles/container.serviceAgent
        - members:
          - serviceAccount:service-123456789000@container-analysis.iam.gserviceaccount.com
          role: roles/containeranalysis.ServiceAgent
        - members:
          - serviceAccount:service-123456789000@containerregistry.iam.gserviceaccount.com
          role: roles/containerregistry.ServiceAgent
        - members:
          - serviceAccount:123456789000-compute@developer.gserviceaccount.com
          - serviceAccount:123456789000@cloudservices.gserviceaccount.com
          role: roles/editor
        - members:
          - user:user@example.com
          role: roles/owner
        etag: BwWbqGVnShQ=
        version: 1
    

### Change the sink destination

In this example, the destination is changed from `dataset_1` to `dataset_other`:

  1. Update the environment variables `DATA_SET_NAME` and `DESTINATION`:
         
         $ DATA_SET_NAME=dataset_other
         $ DESTINATION=bigquery.googleapis.com/projects/${PROJECT_NUMBER}/datasets/${DATA_SET_NAME}
         $ echo ${DESTINATION}
         bigquery.googleapis.com/projects/123456789000/datasets/dataset_other
         

Be sure to refresh the value of `DESTINATION` after modifying the `DATA_SET_NAME` or `PROJECT_NUMBER`.

  2. Change the sink destination:
         
         $ gcloud alpha trace sinks update ${SINK_ID} ${DESTINATION}
         

A sample output is:
         
         Updated [https://cloudtrace.googleapis.com/v2beta1/projects/123456789000/traceSinks/a-sample-sink].
         destination: bigquery.googleapis.com/projects/123456789000/datasets/dataset_other
         name: a-sample-sink
         writer_identity: export-0000001cbe991a08-3434@gcp-sa-cloud-trace.iam.gserviceaccount.com
         

Execute the describe command to view the details of the sink:
         
         $ gcloud alpha trace sinks describe ${SINK_ID}
         destination: bigquery.googleapis.com/projects/123456789000/datasets/dataset_other
         name: a-sample-sink
         writer_identity: export-0000001cbe991a08-3434@gcp-sa-cloud-trace.iam.gserviceaccount.com
         

When you update the destination of a sink, you don't change the sinks writer identity and therefore you don't need to update permissions for the sink.




### Delete a sink

To delete a sink, run the following command:
    
    
    $ gcloud alpha trace sinks delete ${SINK_ID}
    

Sample output is:
    
    
    Really delete sink [a-sample-sink]?
    
    Do you want to continue (y/N)? y
    
    Deleted [https://cloudtrace.googleapis.com/v2beta1/projects/123456789000/traceSinks/a-sample-sink].
    

You can verify the result by running the `list` command:
    
    
    $ gcloud alpha trace sinks list
    Listed 0 items.
    

## Validation

You can use the Cloud Monitoring `exported_span_count` metric as the basis for a chart that displays the errors when Trace data is exported to BigQuery. You can also create an alerting policy to notify you if an export errors occur.

### Creating a chart

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Spans Exported to BigQuery` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **Cloud Trace**.
     2. In the **Active metric categories** menu, select **Bigquery_explort**.
     3. In the **Active metrics** menu, select **Spans Exported to BigQuery**. 
     4. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. Configure how the data is viewed. 
     1. Leave the **Filter** element empty. With this choice, the chart displays all status data.
     2. In the **Aggregation** element, set the first menu to **Mean** , and set the second menu to **status**.

These selections result in a single time series for each unique status value. The following table displays the possible status values:

**Status** value| Meaning and corrective action  
---|---  
`ok` | The data transfer was successful.  
`bigquery_permission_denied` | The data export to the destination failed. The export can fail for any of the following reasons:  

        * The service account in the trace sink doesn't have permission to write to the destination dataset. See Permission denied.
        * The destination of the dataset in the sink doesn't exist. See Invalid destination.
        * BigQuery internal errors. This is an unexpected and transient error.  
`bigquery_quota_exceeded` | The BigQuery project has exceeded its BigQuery streaming quota. See Quota exhausted.  
`invalid_span  
internal_errors`  
`invalid_destination` | Unknown error preventing the export of data to BigQuery. To resolve this condition, please contact technical support or ask a question on Stack Overflow. For information, see [Getting support](https://docs.cloud.google.com/stackdriver/docs/getting-support).   
  
For more information about configuring a chart, see [Select metrics when using Metrics Explorer.](https://docs.cloud.google.com/monitoring/charts/metrics-selector)




If your Trace sink is successfully exporting data, the chart created with the previous settings displays a single time series with the status value of `ok`. If errors occur during the export, then additional time series appear in the chart.

### Creating an alerting policy

To create an alerting policy that triggers if there are errors exporting [Cloud Trace](https://docs.cloud.google.com/trace/docs) data to BigQuery, use the following settings.

#### Steps to create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy).

To create an alerting policy, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the resource, metric, and filters, expand the **Select a metric** menu and then use the values in the **New condition** table: 
     1. Optional: To limit the menu to relevant entries, enter the resource or metric name in the filter bar. 
     2. Select a **Resource type**. For example, select **VM instance**.
     3. Select a **Metric category**. For example, select **instance**.
     4. Select a **Metric**. For example, select **CPU Utilization**.
     5. Select **Apply**.
  5. Click **Next** and then configure the alerting policy trigger. To complete these fields, use the values in the **Configure alert trigger** table. 
  6. Click **Next**.
  7. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.

To be notified when alerts are opened and closed, check **Notify on alert closure**. By default, notifications are sent only when alerts are opened.

  8. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  9. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  10. Click **Alert name** and enter a name for the alerting policy.
  11. Click **Create Policy**.

**New condition**  
Field |   
Value  
---|---  
**Resource and Metric** | In the **Resources** menu, select **Cloud Trace**.  
In the **Metric categories** menu, select **Bigquery_export**.  
In the **Metrics** menu, select **Spans Exported to BigQuert**.   
**Filter** | `status != ok`  
**Across time series  
Time series group by** | `status`  
**Across time series  
Time series aggregation** | `sum`  
  
**Rolling window** | `1 m`  
  
**Rolling window function** | `rate`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Alert trigger** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold value** | `0`  
**Retest window** | `1 minute`  
  
## Using curl

This section describes the conventions and setup used for invoking the Cloud Trace API by using the `curl` tool:

### Authentication

  1. Create an environment variable to hold your Google Cloud project identifier:
         
         PROJECT_ID=my-project
         

  2. Create an environment variable to hold your Google Cloud project number:
         
         PROJECT_NUMBER=12345
         

  3. Authenticate the Google Cloud CLI:
         
         gcloud auth login
         

  4. Set the default Google Cloud project identifier:
         
         gcloud config set project ${PROJECT_ID}
         

  5. Create an authorization token and save it in an environment variable:
         
         ACCESS_TOKEN=`gcloud auth print-access-token`
         

  6. Verify the access token:
         
         echo ${ACCESS_TOKEN}
         

The response to the command should be a long string of characters. For example, on one system, the response begins as:
         
         y29.GluiBjo....
         


**Note:** Access tokens expire. If your `curl` commands fail with an authentication error, create a new access token.

### Invoking `curl`

Each `curl` command includes a set of arguments, followed by the URL of a Cloud Trace API resource. The common arguments include values specified by the `PROJECT_ID` and `ACCESS_TOKEN` environment variables.

Each `curl` invocation has the following general form:
    
    
    curl --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}" [OTHER_ARGS]
    https://cloudtrace.googleapis.com/[API_VERSION]/projects/${PROJECT_ID}/[RESOURCE]
    

where:

  * `[OTHER_ARGS]` (Optional): Omit this field if you are issuing a `GET` request. For other types of HTTP requests, replace this place holder with the request type and any additional data needed to satisfy the request.
  * `[API_VERSION]`: Specify the version of the API.
  * `[RESOURCE]`: Specify the Cloud Trace API resource name.



For example, to list the most recent 1000 traces in your project, execute the following:
    
    
    curl --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}" https://cloudtrace.googleapis.com/v1/projects/${PROJECT_ID}/traces
    

## Troubleshooting

This section contains troubleshooting information that might help you resolve failures when configuring an export.

### Invalid argument error for dataset

The following error message indicates that the dataset name is invalid:
    
    
    ERROR: (gcloud.alpha.trace.sinks.create) INVALID_ARGUMENT: Request contains an invalid argument.
    - '@type': type.googleapis.com/google.rpc.DebugInfo
      detail: '[ORIGINAL ERROR] generic::invalid_argument: sink destination is malformed:
        bigquery.googleapis.com/projects/123456789000/datasets/a-sample-project:dataset_1.
    
    

The error is cause by the destination including the Google Cloud project identifier, `a-sample-project`, as a qualifier to the dataset name.

To resolve this error, replace `a-sample-project:dataset_1` with `dataset_1` and then issue the create command.

Note that you can list your datasets with the `bq ls` command.

### No trace data is being received

There are multiple reasons why you might not receive trace data in BigQuery.

#### Invalid destination

Verify the dataset name and the **project number** are correct.

  * To verify the dataset name is correct. To list the datasets in your current project, run `bq ls`.

If you chose to use environment variables, verify that the value of each variable is correct by issuing a echo command. For example, verify that your destination is correct:
        
        $ echo ${DESTINATION}
        bigquery.googleapis.com/projects/123456789000/datasets/dataset_other
        

Because `DESTINATION` is dependent on the value of `PROJECT_NUMBER` and `DATA_SET_NAME`, these two variables must be set first. Also, if you modify either of these two variables, you must refresh the value stored in `DESTINATION`.

  * To determine your current projects number, run the following:
        
        gcloud projects list --filter="${PROJECT_ID}"
        

You can set the `PROJECT_NUMBER` programmatically by using the following command:
        
        $ PROJECT_NUMBER=`gcloud projects list --filter="${PROJECT_ID}" --format="value(PROJECT_NUMBER)"`
        




#### Invalid permissions

Verify that the service account has been granted the role of `DataEditor` for BigQuery. You can verify the permissions by running the following command:
    
    
    $ gcloud projects get-iam-policy ${PROJECT_ID}
    

The response of this command describes all of the IAM bindings. In this case, the result is as shown. Notice that the sink writer identity has the role of `dataEditor`:
    
    
    bindings:
    - members:
      - serviceAccount:export-0000001cbe991a08-3434@gcp-sa-cloud-trace.iam.gserviceaccount.com
      role: roles/bigquery.dataEditor
    - members:
      [Note, content truncated]
    

#### Quota exhausted

If you've been receiving data and it suddenly stops or your data is incomplete, you might be exhausting your BigQuery streaming quota. To view your quota, go to the **IAM & admin** page and select **Quotas**. Search for the **BigQuery API**. There are two relevant entries: Streaming rows per minute per resource, Streaming bytes per minute per resource.

[Go to Quotas](https://console.cloud.google.com/quotas)

## What's next

For information about the BigQuery schema, see [Export to BigQuery](https://docs.cloud.google.com/trace/docs/trace-export-bigquery).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

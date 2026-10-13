---
url: https://docs.cloud.google.com/data-fusion/docs/reference/cdap-reference/
title: CDAP reference \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:17:14.328105+00:00
---

# CDAP reference  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/reference/cdap-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Reference ](https://docs.cloud.google.com/data-fusion/docs/reference)



Send feedback 

#  CDAP reference Stay organized with collections  Save and categorize content based on your preferences. 

When using Cloud Data Fusion, you use both the Google Cloud console and the Cloud Data Fusion web interface. You use the Google Cloud console to create a Cloud Data Fusion instance. You then use the Cloud Data Fusion web interface to create and manage your pipelines.

Alternatively, you can use command-line tools to create and manage your Cloud Data Fusion instances and pipelines.

  * The [REST reference](https://docs.cloud.google.com/data-fusion/docs/reference/rest) describes the API for creating and managing your Cloud Data Fusion instances on Google Cloud.
  * This page describes the REST API for creating and managing pipelines and datasets. Throughout this page, there are links to the CDAP documentation site, where you can find more detailed information.



## Before you begin

Before you use the REST API, download the Google Cloud CLI and set environment variables for your Google Cloud CLI access credentials and CDAP API endpoint.

### Download and log in to the Google Cloud CLI

  1. [Install and initialize the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs).

  2. Log in to the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login): 
         
         $ gcloud auth login
         




### Set environment variables

  1. **AUTH_TOKEN**
         
         export AUTH_TOKEN=$(gcloud auth print-access-token)
         

  2. **CDAP_ENDPOINT**

The CDAP_ENDPOINT can be obtained using either the Google Cloud CLI or the Cloud Data Fusion REST API. Use the value of the `apiEndpoint`, not the `serviceEndpoint` field. It has the format `hostname/api` (example: `https://my-instance-my-project-id-dot-usc1.datafusion.googleusercontent.com/api`).

### gcloud

In a local terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true), run the following gcloud CLI commands to set the `CDAP_ENDPOINT` environment variable to `apiEndpoint` of your instance.
         
         export INSTANCE_ID=your-instance-name
         
         
         export CDAP_ENDPOINT=$(gcloud beta data-fusion instances describe \
             --location=region-name \
             --format="value(apiEndpoint)" \
           ${INSTANCE_ID})
         

### API

Use the **Try this API** panel to submit an `instances.get` request:

     1. Fill in the `name` request parameter. Provide your project-id, instance [region](https://docs.cloud.google.com/compute/docs/regions-zones#available), and instance-name in the following format: 
            
            projects/project-id/locations/region/instances/instance-name
                        

     2. Click **EXECUTE** to submit the request, and then copy the **`apiEndpoint`** listed in the HTTP response.
     3. Run the following command after inserting the **`apiEndpoint`** : 
            
            export CDAP_ENDPOINT=apiEndpoint
            




## Deploy a pipeline

To deploy a Cloud Data Fusion pipeline, submit the following HTTP `PUT` request.
    
    
    PUT -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps/pipeline-name"
    

Parameter | Description  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.   
`pipeline-name` | Your pipeline name.  
  
For more information, see CDAP's [Create an Application](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+HTTP+RESTful+API#Create-an-Application).

The body of the HTTP `PUT` request is a JSON object in the following format:
    
    
    {
      "name": "MyPipeline",
      "artifact": {
        "name": "cdap-data-pipeline",
        "version": "6.0.0",
        "scope": "system"
      },
      "config": {
        . . .
        "connections": [ . . . ],
        "engine": "spark",
        "postActions": [ . . . ],
        "stages": [ . . . ],
        "schedule": "0 * * * *",
      },
      "__ui__": {
        . . .
      }
    }
    

For more information, see the CDAP [Pipeline Configuration File Format](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480412184/Developing+Pipelines#Pipeline-Configuration-File-Format) and [Creating a Batch Pipeline](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480412184/Developing+Pipelines#Creating-a-Batch-Pipeline).

## Retrieve pipelines

### Retrieve all pipelines

To list Cloud Data Fusion pipelines in the specified namespace, submit the following HTTP `GET` request.
    
    
    GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps"
    

Parameter | Description  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
  
For more information, see [Deployed Applications](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+HTTP+RESTful+API#Details-of-Deployed-Applications-in-Batch).

### Retrieve batch pipelines

To list Cloud Data Fusion batch pipelines in the specified namespace, submit the following HTTP `GET` request.
    
    
    GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps?artifactName=cdap-data-pipeline"
    

Parameter | Description  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
  
For more information, see [Deployed Applications](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+HTTP+RESTful+API#Details-of-Deployed-Applications-in-Batch).

### Retrieve real-time pipelines

To list Cloud Data Fusion real-time pipelines in the specified namespace, submit the following HTTP `GET` request.
    
    
    GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps?artifactName=cdap-data-streams"
    

Parameter | Description  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
  
For more information, see [Deployed Applications](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+HTTP+RESTful+API#Details-of-Deployed-Applications-in-Batch).

### Retrieve pipeline details

To list the details of a pipeline in the specified namespace, submit the following HTTP `GET` request:
    
    
    GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps/pipeline-name"
    

Parameter | Description  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`pipeline-name` | Your pipeline name.  
**Note:** You cannot use API response to import pipelines directly. To convert an API JSON to be import-ready, you can use a Python snippet similar to the following: 
    
    
    def convert_api_json_to_import(api_json):   
    
        conf_data = api_json.pop('configuration')   
    
        api_json['config'] = json.loads(conf_data)
    

For more information, see [Details of a Deployed Application](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+HTTP+RESTful+API#Details-of-Deployed-Applications-in-Batch).

## Batch pipelines

### Start a batch pipeline

To start a batch pipeline, submit the following HTTP `POST` request.
    
    
    POST -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps/pipeline-name/workflows/DataPipelineWorkflow/start"
    

Parameter | Description / value  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`pipeline-name` | Your pipeline name.  
  
For more information, see [Start a Program](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+HTTP+RESTful+API#Start-a-Program).

### Stop a batch pipeline

To stop a batch pipeline, submit the following HTTP `POST` request.
    
    
    POST -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps/pipeline-name/workflows/DataPipelineWorkflow/stop"
    

Parameter | Description / value  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`pipeline-name` | Your pipeline name.  
  
For more information, see [Stop a program](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+HTTP+RESTful+API#Stop-a-Program).

### Schedule a batch pipeline

**Note:** Scheduling is available only for batch pipelines.

By default, scheduling is disabled. To enable scheduling for your pipeline, submit the following HTTP `POST` request.
    
    
    POST -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps/pipeline-name/schedules/dataPipelineSchedule/enable"
    

Parameter | Description / value  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`pipeline-name` | Your pipeline name.  
**Note:** When you create a schedule in CDAP, use Coordinated Universal Time (UTC).

For more information, see [Schedule a Program](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+HTTP+RESTful+API#Schedule-Lifecycle).

### Batch pipeline run records

To get the run records of a Cloud Data Fusion batch pipeline, submit the following HTTP `GET` requests.

**Run records of a batch pipeline**

The returned information includes the `run id`s of a batch pipeline.
    
    
    GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps/pipeline-name/workflows/DataPipelineWorkflow/runs
    

**Records of a batch pipeline run**
    
    
    GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps/pipeline-name/workflows/DataPipelineWorkflow/runs/run-id
    

Parameter | Description  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`pipeline-name` |   
`run-id` |  To find the run ID, see Batch pipeline run records, which returns a list of run IDs.   
  
For more information, see [List Schedules](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+HTTP+RESTful+API#List-Schedules).

### Logs for a batch pipeline

You can view the logs of a pipeline or of a specific pipeline run.

  * To view the logs of a batch pipeline, submit the following HTTP `GET` request.
        
        GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps/pipeline-name/workflows/DataPipelineWorkflow/logs?start=start-ts&stop=stop-ts
        

  * To view logs of a specific run of a batch pipeline, submit the following HTTP `GET` request.
        
        GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps/pipeline-name/workflows/DataPipelineWorkflow/runs/run-id/logs?start=start-ts&stop=stop-ts"
        


Parameter | Description / value  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`pipeline-name` | Your pipeline name.  
`run-id` |  Relevant only if you want to view logs of a specific pipeline run. To find the run ID, see [Batch pipeline run records](https://docs.cloud.google.com/data-fusion/docs/reference/cdap-reference#batch_pipeline_run_records), which returns a list of run IDs.   
  
For more information, see [Downloading Application Logs](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477790558/Logging+HTTP+RESTful+API#Downloading-Application-Logs).

### Metrics for a batch pipeline

To view specific metrics for a batch pipeline, submit the following HTTP `POST` request.
    
    
    POST -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/metrics/query"
    

The body of the HTTP `POST` request is a JSON object in the following format:
    
    
    {
      "query": {
        "tags": {
          "namespace": "default",
          "app": "pipeline name",
          "workflow": "DataPipelineWorkflow",
          "run": "run-id"
        },
        "metrics": [
          "metric1 name",
          "metric2 name",
          ...
        ],
        "timeRange": {
          "aggregate": true
        }
      }
    }
    

Query parameter | Description / value  
---|---  
`pipeline name` | Your pipeline name.  
`run-id` |  To find the run ID, see Batch pipeline run records, which returns a list of run IDs.   
`metric name` | Metric names follow the format:  
`user.pipeline-stage.metric`

  * `pipeline-stage` is any of the stage names in the body of the HTTP `PUT` request that you configured when you deployed your pipeline. In the following example, `BigQuery` or `GoogleCloudStorage` are possible values for `pipeline-stage`. 
        
        {
          "stages": [
            {
              "name": "BigQuery",
              ...
            },
            {
              "name": "GoogleCloudStorage",
              ...
            },
            ...
          ],
          ...
        }         

  * `metrics` can be any of: 
    * `records.in`
    * `records.out`
    * `records.error`
    * `process.time.total`
    * `process.time.avg`
    * `process.time.max`
    * `process.time.min`
    * `process.time.stddev`

  
  
For example, the following query gets the `records.out` and `process.time.avg` metrics for the `BigQuery` stage of the batch pipeline, `batch-pipeline`.
    
    
    {
      "query": {
        "tags": {
          "namespace": "default",
          "app": "batch-pipeline",
          "workflow": "DataPipelineWorkflow",
          "run": "81e3d583-f68b-11e9-aba0-0242b9f29569"
        },
        "metrics": [
          "user.BigQuery.records.out",
          "user.BigQuery.process.time.avg"
        ],
        "timeRange": {
          "aggregate": true
        }
      }
    }
    

For more information, see [CDAP Metrics Microservices](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477692194) and [Cloud Data Fusion flow control](https://docs.cloud.google.com/data-fusion/docs/concepts/flow-control).

## Real-time pipelines

### Start a real-time pipeline

To start a real-time pipeline, submit the following HTTP `POST` request.
    
    
    POST -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps/pipeline-name/spark/DataStreamsSparkStreaming/start"
    

Parameter | Description / value  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`pipeline-name` | Your pipeline name.  
  
For more information, see [Starting a Program](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+HTTP+RESTful+API#Start-a-Program).

### Stop a real-time pipeline

To stop a real-time pipeline, submit the following HTTP `POST` request.
    
    
    POST -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps/pipeline-name/spark/DataStreamsSparkStreaming/stop"
    

Parameter | Description / value  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`pipeline-name` | | `pipeline-name`  
  
For more information, see [Stop a Program](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+HTTP+RESTful+API#Stop-a-Program).

### Real-time pipeline run records

To get the run records of a Cloud Data Fusion real-time pipeline, submit the following HTTP `GET` requests.

**Run records of a real-time pipeline**

The returned information includes the `run id`s of a real-time pipeline.
    
    
    GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps/pipeline-name/spark/DataStreamsSparkStreaming
    

**Records of a real-time pipeline run**
    
    
    GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps/pipeline-name/spark/DataStreamsSparkStreaming/run-id
    

Parameter | Description  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`pipeline-name` | Your pipeline name.  
`run-id` |  To find the run ID, see Real-time pipeline run records, which returns a list of run IDs.   
  
For more information, see [List Schedules](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+HTTP+RESTful+API#List-Schedules).

### Logs for a real-time pipeline

You can view the logs of a pipeline or of a specific pipeline run.

  * To view the logs of a real-time pipeline, submit the following HTTP `GET` request.
        
        GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps/pipeline-name/spark/DataStreamsSparkStreaming/logs?start=start-ts&stop=stop-ts"
        

  * To view logs of a specific run of a real-time pipeline, submit the following HTTP `GET` request.
        
        GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/apps/pipeline-name/spark/DataStreamsSparkStreaming/runs/run-id/logs?start=start-ts&stop=stop-ts"
        


Parameter | Description / value  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`pipeline-name` | Your pipeline name.  
`run-id` |  Relevant only if you want to view logs of a specific pipeline run. To find the run ID, call [Real-time pipeline run records](https://docs.cloud.google.com/data-fusion/docs/reference/cdap-reference#real-time_pipeline_run_records), which returns a list of run IDs.   
  
For more information, see [Downloading Application Logs](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477790558/Logging+HTTP+RESTful+API#Downloading-Application-Logs).

### Metrics for a real-time pipeline

To view specific metrics for a real-time pipeline, submit the following HTTP `POST` request.
    
    
    POST -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/metrics/query"
    

The body of the HTTP `POST` request is a JSON object in the following format:
    
    
    {
      "query": {
        "tags": {
          "namespace": "default",
          "app": "pipeline name",
          "spark": "DataStreamsSparkStreaming",
          "run": "run-id"
        },
        "metrics": [
          "metric1 name",
          "metric2 name",
          ...
        ],
        "timeRange": {
          "aggregate": true
        }
      }
    }
    

Query parameter | Description / value  
---|---  
`pipeline name` | Your pipeline name.  
`run-id` |  To find the run ID, call Real-time pipeline run records, which returns a list of run IDs.   
`metric name` | Metric names follow the format:  
`user.pipeline-stage.metric`

  * `pipeline-stage` is any of the stage names in the body of the HTTP `PUT` request that you configured when you deployed your pipeline. In the following example, `BigQuery` or `GoogleCloudStorage` are possible values for `pipeline-stage`. 
        
        {
         "stages": [
          {
           "name": BigQuery,
           "name": GoogleCloudStorage
          },
          ...
         ],
         ...
        }           

  * `metrics` can be any of: 
    * `records.in`
    * `records.out`
    * `records.error`
    * `process.time.total`
    * `process.time.avg`
    * `process.time.max`
    * `process.time.min`
    * `process.time.stddev`

  
  
For example, the following query gets the `records.out` and `process.time.avg` metrics for the `BigQuery` stage of the real-time pipeline, `rt-pipeline`.
    
    
    {
      "query": {
        "tags": {
          "namespace": "default",
          "app": "rt-pipeline",
          "spark": "DataStreamsSparkStreaming",
          "run": "81e3d583-f68b-11e9-aba0-0242b9f29570"
        },
        "metrics": [
          "user.BigQuery.records.out",
          "user.BigQuery.process.time.avg"
        ],
        "timeRange": {
          "aggregate": true
        }
      }
    }
    

For more information, see [Metrics HTTP RESTful API](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477692194) and [Cloud Data Fusion flow control](https://docs.cloud.google.com/data-fusion/docs/concepts/flow-control).

## Dataset metadata

### Metadata properties

To view metadata properties for your dataset, submit the following HTTP `GET` request.
    
    
    GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/default/datasets/dataset-id/metadata/properties"
    

Parameter | Description / value  
---|---  
`dataset-id` |  To get the dataset ID, submit an HTTP `GET` request that [lists all datasets](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477692177/Dataset+HTTP+RESTful+API#Listing-all-Datasets):  
`GET -H "Authorization: Bearer $(gcloud auth print-access-token) ${CDAP_ENDPOINT}/v3/namespaces/namespace-id/data/datasets`  
You can [create](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041) a [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725). The namespace ID must either be the name of the namespace when it was created or `default`, which is the name of the default namespace.   
  
For more information, see [Retrieving Properties](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477692187/Metadata+HTTP+RESTful+API#Retrieving-Properties).

### Metadata tags

To view metadata tags for your dataset, submit the following HTTP `GET` request.
    
    
    GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/default/datasets/dataset-id/metadata/tags"
    

Parameter | Description / value  
---|---  
`dataset-id` |  To get the dataset ID, submit an HTTP `GET` request that [lists all datasets](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477692177/Dataset+HTTP+RESTful+API#Listing-all-Datasets): `GET -H "Authorization: Bearer $(gcloud auth print-access-token) ${CDAP_ENDPOINT}/v3/namespaces/namespace-id/data/datasets`. You can [create](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041) a [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725). The namespace ID must either be the name of the namespace when it was created or `default`, which is the name of the default namespace.   
  
For more information, see [Retrieving Tags](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477692187/Metadata+HTTP+RESTful+API#Retrieving-Tags).

## Lineage

### Dataset lineage

To view the lineage of your dataset, submit the following HTTP `GET` request.
    
    
    GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/datasets/dataset-id/lineage?start=start-ts&end=end-ts"
    

Parameter | Description / value  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`dataset-id` |  To get the dataset ID, submit an HTTP `GET` request that [lists all datasets](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477692177/Dataset+HTTP+RESTful+API#Listing-all-Datasets): `GET -H "Authorization: Bearer $(gcloud auth print-access-token) ${CDAP_ENDPOINT}/v3/namespaces/namespace-id/data/datasets`. You can [create](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041) a [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725). The namespace ID must either be the name of the namespace when it was created or `default`, which is the name of the default namespace.   
`start-ts` | Starting timestamp of lineage in seconds.  
`end-ts` | Ending timestamp of lineage in seconds.  
  
For more information, see [Viewing Lineages](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477692187/Metadata+HTTP+RESTful+API#Viewing-Lineages).

### Field level lineage

To view the lineage of fields in your dataset in a specified range of time, submit the following HTTP `GET` request.
    
    
    GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/datasets/dataset-id/lineage/fields?start=start-ts&end=end-ts[&prefix=prefix>]"
    

Parameter | Description / value  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`dataset-id` |  To get the dataset ID, submit an HTTP `GET` request that [lists all datasets](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477692177/Dataset+HTTP+RESTful+API#Listing-all-Datasets): `GET -H "Authorization: Bearer $(gcloud auth print-access-token) ${CDAP_ENDPOINT}/v3/namespaces/namespace-id/data/datasets`.   
`start-ts` | Starting timestamp of lineage in seconds.  
`end-ts` | Ending timestamp of lineage in seconds.  
  
For more information, see [Field Level Lineage](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477692187/Metadata+HTTP+RESTful+API#Field-Level-Lineage).

## Secure storage

Use the CDAP Secure Storage HTTP RESTful API to add, retrieve, and delete secure keys.

### Add a secure key

To add a secure key to secure storage, submit the following HTTP `PUT` request.
    
    
    PUT -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/securekeys/secure-key-id"
    

Parameter | Description  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`secure-key-id` | Name of the key to add to secure storage.  
  
The body of the HTTP `PUT` request is a JSON object in the following format:
    
    
    {
      "description": "Example Secure Key",
      "data": "secure-contents",
      "properties": {
        "property-key": "property-value"
      }
    }
    

For more information, see [Add a Secure Key](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/801767425/Using+Secure+Keys) and the [Administrator Guide: Secure Storage](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480347053).

### Retrieve a secure key

To retrieve a secure key from secure storage, submit the following HTTP `GET` request.
    
    
    GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/securekeys/secure-key-id"
    

Parameter | Description  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`secure-key-id` | Name of the key to retrieve from secure storage.  
  
For more information, see [Retrieve a Secure Key](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477790661/Security+HTTP+RESTful+API#Retrieve-a-Secure-Key) and the [Administration Manual: Secure Storage](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480347053).

### Retrieve the metadata for a secure key

To retrieve the metadata for a secure key from secure storage, submit the following HTTP `GET` request.
    
    
    GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/securekeys/secure-key-id/metadata"
    

Parameter | Description  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`secure-key-id` | Name of the key to retrieve from secure storage.  
  
The metadata of the secure key is returned as a JSON object— the secure key name (the secure-key-id), description, created timestamp, and the map of properties—in the response body.

**Example response** :
    
    
    {
      "name": "secure-key-id",
      "description": "Example Secure Key",
      "createdEpochMs": 1471718010326,
      "properties": {
        "property-key": "property-value"
      }
    }
    

For more information, see [Retrieve a Secure Key](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477790661/Security+HTTP+RESTful+API#Retrieve-a-Secure-Key), [Retrieve the Metadata for a Secure Key](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477790661/Security+HTTP+RESTful+API#Retrieve-the-Metadata-for-a-Secure-Key), and the [Administration Manual: Secure Storage](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480347053).

### List all secure keys

To list all the keys in a namespace from secure storage, submit the following HTTP `GET` request.
    
    
    GET -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/securekeys"
    

Parameter | Description  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
  
For more information, see [List all Secure Keys](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477790661/Security+HTTP+RESTful+API#List-all-Secure-Keys) and the [Administration Manual: Secure Storage](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480347053).

### Delete a secure key

To delete a secure key from secure storage, submit the following HTTP `DELETE` request.
    
    
    DELETE -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/namespace-id/securekeys/secure-key-id"
    

Parameter | Description  
---|---  
`namespace-id` | The namespace ID must either be the name of the [namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313725/Namespaces) when it was [created](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices) or `default`, which is the name of the default namespace.  
`secure-key-id` | Name of the key to delete from secure storage.  
  
For more information, see [Remove a Secure Key](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477790661/Security+HTTP+RESTful+API#Remove-a-Secure-Key) and the [Administration Manual: Secure Storage](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480347053).

## Delete a namespace

To delete a Cloud Data Fusion namespace, submit the following HTTP `PATCH` request to enable `enable.unrecoverable.reset`.
    
    
    PATCH -H 'Content-Type: application/json' -H "Authorization: Bearer ${AUTH_TOKEN}" 'https://datafusion.googleapis.com/v1beta1/projects/project-id/locations/region/instances/instance-name?updateMask=options' -d '{ "options": { "enable.unrecoverable.reset": "true" } }'
    

After the `enable.unrecoverable.reset` property is set to `true`, [restart](https://cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/restart) the instance:
    
    
    gcloud beta data-fusion instances restart --project=project-id --location=region instance-name
    

Delete the namespace with the following `DELETE` request or in the web interface.
    
    
    DELETE -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/unrecoverable/namespaces/namespace-id"
    

To avoid accidental deletion of the namespaces, update the `enable.unrecoverable.reset` property to set to `false`, and [restart](https://cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/restart) the instance .
    
    
    PATCH -H 'Content-Type: application/json' -H "Authorization: Bearer ${AUTH_TOKEN}" 'https://datafusion.googleapis.com/v1beta1/projects/project-id/locations/region/instances/instance-name?updateMask=options' -d '{ "options": { "enable.unrecoverable.reset": "false" } }'
    

Parameter | Description  
---|---  
`project-id` | The project ID that hosts the Cloud Data Fusion instance.   
`region` | The location of your Cloud Data Fusion instance.  
`instance-name` | The Cloud Data Fusion instance name.  
`namespace-id` | The name of the namespace to delete.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

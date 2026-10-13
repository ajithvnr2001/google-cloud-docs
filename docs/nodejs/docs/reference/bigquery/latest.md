---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/
title: Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:26.737689+00:00
---

# Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 8.0.0 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/)
  * [ 7.8.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/7.8.0/)
  * [ 7.7.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/7.7.0/)
  * [ 7.6.1 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/7.6.1/)
  * [ 7.5.2 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/7.5.2/)
  * [ 7.4.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/7.4.0/)
  * [ 7.3.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/7.3.0/)
  * [ 7.2.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/7.2.0/)
  * [ 7.1.1 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/7.1.1/)
  * [ 7.0.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/7.0.0/)
  * [ 6.2.1 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/6.2.1/)
  * [ 6.0.3 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/6.0.3/)
  * [ 5.12.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/5.12.0/)
  * [ 5.11.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/5.11.0/)
  * [ 5.10.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/5.10.0/)
  * [ 5.9.3 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/5.9.3/)
  * [ 5.8.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/5.8.0/)
  * [ 5.7.1 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/5.7.1/)
  * [ 5.6.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/5.6.0/)
  * [ 5.5.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/5.5.0/)



# [Google BigQuery: Node.js Client](https://github.com/googleapis/nodejs-bigquery)

[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages) [![npm version](https://img.shields.io/npm/v/@google-cloud/bigquery.svg)](https://www.npmjs.org/package/@google-cloud/bigquery)

Google BigQuery Client Library for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/nodejs-bigquery/blob/main/CHANGELOG.md).

  * [Google BigQuery Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/bigquery/latest)
  * [Google BigQuery Documentation](https://cloud.google.com/bigquery)
  * [github.com/googleapis/nodejs-bigquery](https://github.com/googleapis/nodejs-bigquery)



Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart
    * Before you begin
    * Installing the client library
    * Using the client library
  * Samples
  * Versioning
  * Contributing
  * License



## Quickstart

### Before you begin

  1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
  2. [Enable the Google BigQuery API](https://console.cloud.google.com/flows/enableapi?apiid=bigquery.googleapis.com).
  3. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation.



### Installing the client library
    
    
    npm install @google-cloud/bigquery
    

### Using the client library
    
    
    // Imports the Google Cloud client library
    const {BigQuery} = require('[@google-cloud/bigquery](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/overview.html)');
    
    async function createDataset() {
      // Creates a client
      const bigqueryClient = new [BigQuery](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html)();
    
      // Create the dataset
      const [dataset] = await bigqueryClient.[createDataset](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html)(datasetName);
      console.log(`Dataset ${dataset.id} created.`);
    }
    createDataset();
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/nodejs-bigquery/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code | Try it  
---|---|---  
Add Column Load Append | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/addColumnLoadAppend.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/addColumnLoadAppend.js,samples/README.md)  
Add Column Query Append | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/addColumnQueryAppend.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/addColumnQueryAppend.js,samples/README.md)  
Add Empty Column | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/addEmptyColumn.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/addEmptyColumn.js,samples/README.md)  
Auth View Tutorial | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/authViewTutorial.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/authViewTutorial.js,samples/README.md)  
Browse Table | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/browseTable.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/browseTable.js,samples/README.md)  
Cancel Job | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/cancelJob.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/cancelJob.js,samples/README.md)  
Client JSON Credentials | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/clientJSONCredentials.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/clientJSONCredentials.js,samples/README.md)  
Copy Table | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/copyTable.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/copyTable.js,samples/README.md)  
Copy Table Multiple Source | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/copyTableMultipleSource.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/copyTableMultipleSource.js,samples/README.md)  
Create Dataset | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/createDataset.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/createDataset.js,samples/README.md)  
Create Job | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/createJob.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/createJob.js,samples/README.md)  
Create Model | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/createModel.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/createModel.js,samples/README.md)  
Create Routine | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/createRoutine.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/createRoutine.js,samples/README.md)  
Create Routine DDL | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/createRoutineDDL.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/createRoutineDDL.js,samples/README.md)  
Create Table | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/createTable.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/createTable.js,samples/README.md)  
Create Table Clustered | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/createTableClustered.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/createTableClustered.js,samples/README.md)  
Create Table Column ACL | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/createTableColumnACL.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/createTableColumnACL.js,samples/README.md)  
Create Table Partitioned | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/createTablePartitioned.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/createTablePartitioned.js,samples/README.md)  
Create Table Range Partitioned | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/createTableRangePartitioned.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/createTableRangePartitioned.js,samples/README.md)  
Create View | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/createView.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/createView.js,samples/README.md)  
Ddl Create View | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/ddlCreateView.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/ddlCreateView.js,samples/README.md)  
Delete Dataset | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/deleteDataset.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/deleteDataset.js,samples/README.md)  
Delete Label Dataset | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/deleteLabelDataset.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/deleteLabelDataset.js,samples/README.md)  
Delete Label Table | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/deleteLabelTable.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/deleteLabelTable.js,samples/README.md)  
Delete Model | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/deleteModel.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/deleteModel.js,samples/README.md)  
Delete Routine | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/deleteRoutine.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/deleteRoutine.js,samples/README.md)  
Delete Table | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/deleteTable.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/deleteTable.js,samples/README.md)  
Extract Table Compressed | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/extractTableCompressed.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/extractTableCompressed.js,samples/README.md)  
Extract Table JSON | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/extractTableJSON.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/extractTableJSON.js,samples/README.md)  
Extract Table To GCS | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/extractTableToGCS.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/extractTableToGCS.js,samples/README.md)  
Get Dataset | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/getDataset.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/getDataset.js,samples/README.md)  
Get Dataset Labels | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/getDatasetLabels.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/getDatasetLabels.js,samples/README.md)  
Get Job | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/getJob.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/getJob.js,samples/README.md)  
BigQuery Get Model | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/getModel.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/getModel.js,samples/README.md)  
Get Routine | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/getRoutine.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/getRoutine.js,samples/README.md)  
BigQuery Get Table | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/getTable.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/getTable.js,samples/README.md)  
Get Table Labels | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/getTableLabels.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/getTableLabels.js,samples/README.md)  
Get View | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/getView.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/getView.js,samples/README.md)  
Insert Rows As Stream | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/insertRowsAsStream.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/insertRowsAsStream.js,samples/README.md)  
Inserting Data Types | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/insertingDataTypes.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/insertingDataTypes.js,samples/README.md)  
BigQuery Label Dataset | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/labelDataset.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/labelDataset.js,samples/README.md)  
Label Table | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/labelTable.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/labelTable.js,samples/README.md)  
List Datasets | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/listDatasets.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/listDatasets.js,samples/README.md)  
List Datasets By Label | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/listDatasetsByLabel.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/listDatasetsByLabel.js,samples/README.md)  
List Jobs | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/listJobs.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/listJobs.js,samples/README.md)  
BigQuery List Models | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/listModels.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/listModels.js,samples/README.md)  
BigQuery List Models Streaming | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/listModelsStreaming.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/listModelsStreaming.js,samples/README.md)  
List Routines | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/listRoutines.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/listRoutines.js,samples/README.md)  
List Tables | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/listTables.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/listTables.js,samples/README.md)  
Load CSV From GCS | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadCSVFromGCS.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadCSVFromGCS.js,samples/README.md)  
Load CSV From GCS Autodetect | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadCSVFromGCSAutodetect.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadCSVFromGCSAutodetect.js,samples/README.md)  
Load CSV From GCS Truncate | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadCSVFromGCSTruncate.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadCSVFromGCSTruncate.js,samples/README.md)  
Load JSON From GCS | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadJSONFromGCS.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadJSONFromGCS.js,samples/README.md)  
Load JSON From GCS Autodetect | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadJSONFromGCSAutodetect.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadJSONFromGCSAutodetect.js,samples/README.md)  
Load JSON From GCS Truncate | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadJSONFromGCSTruncate.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadJSONFromGCSTruncate.js,samples/README.md)  
Load Local File | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadLocalFile.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadLocalFile.js,samples/README.md)  
Load Orc From GCS Truncate | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadOrcFromGCSTruncate.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadOrcFromGCSTruncate.js,samples/README.md)  
Load Parquet From GCS Truncate | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadParquetFromGCSTruncate.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadParquetFromGCSTruncate.js,samples/README.md)  
Load Table Clustered | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadTableClustered.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadTableClustered.js,samples/README.md)  
Load Table GCS Avro | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadTableGCSAvro.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadTableGCSAvro.js,samples/README.md)  
Load Table GCS Avro Truncate | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadTableGCSAvroTruncate.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadTableGCSAvroTruncate.js,samples/README.md)  
Load Table GCSORC | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadTableGCSORC.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadTableGCSORC.js,samples/README.md)  
Load Table GCS Parquet | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadTableGCSParquet.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadTableGCSParquet.js,samples/README.md)  
Load Table Partitioned | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadTablePartitioned.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadTablePartitioned.js,samples/README.md)  
Load Table URI Firestore | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/loadTableURIFirestore.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/loadTableURIFirestore.js,samples/README.md)  
Nested Repeated Schema | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/nestedRepeatedSchema.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/nestedRepeatedSchema.js,samples/README.md)  
Query | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/query.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/query.js,samples/README.md)  
Query Batch | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryBatch.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryBatch.js,samples/README.md)  
Query Clustered Table | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryClusteredTable.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryClusteredTable.js,samples/README.md)  
Query Destination Table | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryDestinationTable.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryDestinationTable.js,samples/README.md)  
Query Disable Cache | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryDisableCache.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryDisableCache.js,samples/README.md)  
Query Dry Run | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryDryRun.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryDryRun.js,samples/README.md)  
Query External GCS Perm | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryExternalGCSPerm.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryExternalGCSPerm.js,samples/README.md)  
Query External GCS Temp | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryExternalGCSTemp.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryExternalGCSTemp.js,samples/README.md)  
Query Legacy | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryLegacy.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryLegacy.js,samples/README.md)  
Query Legacy Large Results | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryLegacyLargeResults.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryLegacyLargeResults.js,samples/README.md)  
Query Pagination | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryPagination.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryPagination.js,samples/README.md)  
Query Params Arrays | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryParamsArrays.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryParamsArrays.js,samples/README.md)  
Query Params Named | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryParamsNamed.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryParamsNamed.js,samples/README.md)  
Query Params Named Types | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryParamsNamedTypes.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryParamsNamedTypes.js,samples/README.md)  
Query Params Positional | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryParamsPositional.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryParamsPositional.js,samples/README.md)  
Query Params Positional Types | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryParamsPositionalTypes.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryParamsPositionalTypes.js,samples/README.md)  
Query Params Structs | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryParamsStructs.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryParamsStructs.js,samples/README.md)  
Query Params Timestamps | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryParamsTimestamps.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryParamsTimestamps.js,samples/README.md)  
Query Short Mode | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryShortMode.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryShortMode.js,samples/README.md)  
Query Stack Overflow | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/queryStackOverflow.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/queryStackOverflow.js,samples/README.md)  
Quickstart | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/quickstart.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/quickstart.js,samples/README.md)  
Relax Column | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/relaxColumn.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/relaxColumn.js,samples/README.md)  
Relax Column Load Append | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/relaxColumnLoadAppend.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/relaxColumnLoadAppend.js,samples/README.md)  
Relax Column Query Append | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/relaxColumnQueryAppend.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/relaxColumnQueryAppend.js,samples/README.md)  
Remove Table Clustering | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/removeTableClustering.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/removeTableClustering.js,samples/README.md)  
Set Client Endpoint | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/setClientEndpoint.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/setClientEndpoint.js,samples/README.md)  
Set User Agent | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/setUserAgent.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/setUserAgent.js,samples/README.md)  
Table Exists | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/tableExists.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/tableExists.js,samples/README.md)  
Undelete Table | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/undeleteTable.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/undeleteTable.js,samples/README.md)  
Update Dataset Access | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/updateDatasetAccess.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/updateDatasetAccess.js,samples/README.md)  
Update Dataset Description | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/updateDatasetDescription.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/updateDatasetDescription.js,samples/README.md)  
Update Dataset Expiration | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/updateDatasetExpiration.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/updateDatasetExpiration.js,samples/README.md)  
BigQuery Update Model | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/updateModel.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/updateModel.js,samples/README.md)  
Update Routine | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/updateRoutine.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/updateRoutine.js,samples/README.md)  
Update Table Column ACL | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/updateTableColumnACL.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/updateTableColumnACL.js,samples/README.md)  
Update Table Description | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/updateTableDescription.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/updateTableDescription.js,samples/README.md)  
Update Table Expiration | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/updateTableExpiration.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/updateTableExpiration.js,samples/README.md)  
Update View Query | [source code](https://github.com/googleapis/nodejs-bigquery/blob/main/samples/updateViewQuery.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigquery&page=editor&open_in_editor=samples/updateViewQuery.js,samples/README.md)  
  
The [Google BigQuery Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/bigquery/latest) documentation also contains samples.

## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/bigquery@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority.

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/nodejs-bigquery/blob/main/CONTRIBUTING.md).

Please note that this `README.md`, the `samples/README.md`, and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template. To edit one of these files, make an edit to its templates in [directory](https://github.com/googleapis/synthtool).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/nodejs-bigquery/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 

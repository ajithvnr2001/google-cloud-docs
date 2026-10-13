---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery
title: Interface BigQuery (2.73.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:41.630341+00:00
---

# Interface BigQuery (2.73.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BigQuery (2.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.73.0 (latest)  2.69.0  2.68.0  2.67.0  2.65.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.2  2.56.0  2.55.3  2.54.2  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.1  2.47.0  2.46.0  2.45.0  2.44.0  2.43.3  2.42.3  2.41.0  2.40.3  2.39.1  2.38.2  2.37.2  2.36.0  2.35.0  2.34.2  2.33.2 
    
    
    public interface BigQuery extends Service<BigQueryOptions>, AutoCloseable

An interface for Google Cloud BigQuery. See Also: [Google Cloud BigQuery](https://cloud.google.com/bigquery/what-is-bigquery)

## Implements

com.google.cloud.Service<com.google.cloud.bigquery.BigQueryOptions>, [AutoCloseable](https://docs.oracle.com/javase/8/docs/api/java/lang/AutoCloseable.html)

## Methods 

### cancel(JobId jobId)
    
    
    public abstract boolean cancel(JobId jobId)

Sends a job cancel request. This call will return immediately. The job status can then be checked using [#getJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery#com_google_cloud_bigquery_BigQuery_getJob_).

If the location of the job is not "US" or "EU", the `jobId` must specify the job location.

Example of cancelling a job.
    
    
     String jobName = "my_job_name";
     JobId jobId = JobId.of(jobName);
     boolean success = bigquery.cancel(jobId);
     if (success) {
       // job was cancelled
     } else {
       // job was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`jobId` | `[JobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobId)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if cancel was requested successfully, `false` if the job was not found  
  
### cancel(String jobId)
    
    
    public abstract boolean cancel(String jobId)

Sends a job cancel request. This call will return immediately. The job status can then be checked by using [#getJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery#com_google_cloud_bigquery_BigQuery_getJob_).

If the location of the job is not "US" or "EU", [#cancel(JobId)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery#com_google_cloud_bigquery_BigQuery_cancel_com_google_cloud_bigquery_JobId_) must be used instead.

Example of cancelling a job.
    
    
     String jobName = "my_job_name";
     boolean success = bigquery.cancel(jobName);
     if (success) {
       // job was cancelled
     } else {
       // job was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`jobId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if cancel was requested successfully, `false` if the job was not found  
  
### close()
    
    
    public default void close()

Closes any background resources and transport channels held by this service.

The default implementation does nothing. Implementations that manage background resources (such as gRPC channels or storage clients) should override this method to release them deterministically.

### create(DatasetInfo datasetInfo, BigQuery.DatasetOption[] options)
    
    
    public abstract Dataset create(DatasetInfo datasetInfo, BigQuery.DatasetOption[] options)

Creates a new dataset.

Example of creating a dataset.
    
    
     String datasetName = "my_dataset_name";
     Dataset dataset = null;
     DatasetInfo datasetInfo = DatasetInfo.newBuilder(datasetName).build();
     try {
       // the dataset was created
       dataset = bigquery.create(datasetInfo);
     } catch (BigQueryException e) {
       // the dataset was not created
     }
     

**Parameters**  
---  
**Name** | **Description**  
`datasetInfo` | `[DatasetInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo)`  
  
`options` | `[DatasetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.DatasetOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset)` |   
  
### create(JobInfo jobInfo, BigQuery.JobOption[] options)
    
    
    public abstract Job create(JobInfo jobInfo, BigQuery.JobOption[] options)

Creates a new job.

Example of loading a newline-delimited-json file with textual fields from GCS to a table.
    
    
     String datasetName = "my_dataset_name";
     String tableName = "my_table_name";
     String sourceUri = "gs://cloud-samples-data/bigquery/us-states/us-states.json";
     TableId tableId = TableId.of(datasetName, tableName);
     // Table field definition
     Field[] fields = new Field[] { Field.of("name", LegacySQLTypeName.STRING),
     Field.of("post_abbr", LegacySQLTypeName.STRING) };
     // Table schema definition
     Schema schema = Schema.of(fields);
     LoadJobConfiguration configuration = LoadJobConfiguration.builder(tableId, sourceUri)
         .setFormatOptions(FormatOptions.json())
         .setCreateDisposition(CreateDisposition.CREATE_IF_NEEDED)
         .setSchema(schema).build();
     // Load the table
     Job loadJob = bigquery.create(JobInfo.of(configuration));
     loadJob = loadJob.waitFor();
     // Check the table
     System.out.println("State: " + loadJob.getStatus().getState());
     return ((StandardTableDefinition) bigquery.getTable(tableId).getDefinition()).getNumRows();
     

Example of creating a query job.
    
    
     String query = "SELECT field FROM my_dataset_name.my_table_name";
     Job job = null;
     JobConfiguration jobConfiguration = QueryJobConfiguration.of(query);
     JobInfo jobInfo = JobInfo.of(jobConfiguration);
     try {
       job = bigquery.create(jobInfo);
     } catch (BigQueryException e) {
       // the job was not created
     }
     

**Parameters**  
---  
**Name** | **Description**  
`jobInfo` | `[JobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo)`  
  
`options` | `[JobOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.JobOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job)` |   
  
### create(RoutineInfo routineInfo, BigQuery.RoutineOption[] options)
    
    
    public abstract Routine create(RoutineInfo routineInfo, BigQuery.RoutineOption[] options)

Creates a new routine.

**Parameters**  
---  
**Name** | **Description**  
`routineInfo` | `[RoutineInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.RoutineInfo)`  
  
`options` | `[RoutineOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.RoutineOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Routine](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Routine)` |   
  
### create(TableInfo tableInfo, BigQuery.TableOption[] options)
    
    
    public abstract Table create(TableInfo tableInfo, BigQuery.TableOption[] options)

Creates a new table.

Example of creating a table.
    
    
     String datasetName = "my_dataset_name";
     String tableName = "my_table_name";
     String fieldName = "string_field";
     TableId tableId = TableId.of(datasetName, tableName);
     // Table field definition
     Field field = Field.of(fieldName, LegacySQLTypeName.STRING);
     // Table schema definition
     Schema schema = Schema.of(field);
     TableDefinition tableDefinition = StandardTableDefinition.of(schema);
     TableInfo tableInfo = TableInfo.newBuilder(tableId, tableDefinition).build();
     Table table = bigquery.create(tableInfo);
     

**Parameters**  
---  
**Name** | **Description**  
`tableInfo` | `[TableInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableInfo)`  
  
`options` | `[TableOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.TableOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Table)` |   
  
### createConnection()
    
    
    public abstract Connection createConnection()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Creates a new BigQuery query connection used for executing queries (not the same as BigQuery connection properties). It uses the BigQuery Storage Read API for high throughput queries by default. This overloaded method creates a Connection with default ConnectionSettings for query execution where default values are set for numBufferedRows (20000), useReadApi (true), useLegacySql (false).

Example of creating a query connection.
    
    
     Connection connection = bigquery.createConnection();
     

**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Connection)` |   
  
### createConnection(@NonNull ConnectionSettings connectionSettings)
    
    
    public abstract Connection createConnection(@NonNull ConnectionSettings connectionSettings)

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Creates a new BigQuery query connection used for executing queries (not the same as BigQuery connection properties). It uses the BigQuery Storage Read API for high throughput queries by default.

Example of creating a query connection.
    
    
     ConnectionSettings connectionSettings =
         ConnectionSettings.newBuilder()
             .setRequestTimeout(10L)
             .setMaxResults(100L)
             .setUseQueryCache(true)
             .build();
     Connection connection = bigquery.createConnection(connectionSettings);
     

**Parameter**  
---  
**Name** | **Description**  
`connectionSettings` | `@org.checkerframework.checker.nullness.qual.NonNull com.google.cloud.bigquery.ConnectionSettings`  
  
**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Connection)` |   
  
### delete(DatasetId datasetId, BigQuery.DatasetDeleteOption[] options)
    
    
    public abstract boolean delete(DatasetId datasetId, BigQuery.DatasetDeleteOption[] options)

Deletes the requested dataset.

Example of deleting a dataset, even if non-empty.
    
    
     String projectId = "my_project_id";
     String datasetName = "my_dataset_name";
     DatasetId datasetId = DatasetId.of(projectId, datasetName);
     boolean deleted = bigquery.delete(datasetId, DatasetDeleteOption.deleteContents());
     if (deleted) {
       // the dataset was deleted
     } else {
       // the dataset was not found
     }
     

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[DatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetId)`  
  
`options` | `[DatasetDeleteOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.DatasetDeleteOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if dataset was deleted, `false` if it was not found  
  
### delete(JobId jobId)
    
    
    public abstract boolean delete(JobId jobId)

Deletes the requested job.

**Parameter**  
---  
**Name** | **Description**  
`jobId` | `[JobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobId)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if job was deleted, `false` if it was not found  
  
### delete(ModelId modelId)
    
    
    public abstract boolean delete(ModelId modelId)

Deletes the requested model.

Example of deleting a model.
    
    
     String projectId = "my_project_id";
     String datasetName = "my_dataset_name";
     String tableName = "my_model_name";
     ModelId modelId = ModelId.of(projectId, datasetName, modelName);
     boolean deleted = bigquery.delete(modelId);
     if (deleted) {
       // the model was deleted
     } else {
       // the model was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`modelId` | `[ModelId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ModelId)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if model was deleted, `false` if it was not found  
  
### delete(RoutineId routineId)
    
    
    public abstract boolean delete(RoutineId routineId)

Deletes the requested routine.

Example of deleting a routine.
    
    
     String projectId = "my_project_id";
     String datasetId = "my_dataset_id";
     String routineId = "my_routine_id";
     RoutineId routineId = RoutineId.of(projectId, datasetId, routineId);
     boolean deleted = bigquery.delete(routineId);
     if (deleted) {
       // the routine was deleted
     } else {
       // the routine was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`routineId` | `[RoutineId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.RoutineId)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if routine was deleted, `false` if it was not found  
  
### delete(TableId tableId)
    
    
    public abstract boolean delete(TableId tableId)

Deletes the requested table.

Example of deleting a table.
    
    
     String projectId = "my_project_id";
     String datasetName = "my_dataset_name";
     String tableName = "my_table_name";
     TableId tableId = TableId.of(projectId, datasetName, tableName);
     boolean deleted = bigquery.delete(tableId);
     if (deleted) {
       // the table was deleted
     } else {
       // the table was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`tableId` | `[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if table was deleted, `false` if it was not found  
  
### delete(String datasetId, BigQuery.DatasetDeleteOption[] options)
    
    
    public abstract boolean delete(String datasetId, BigQuery.DatasetDeleteOption[] options)

Deletes the requested dataset.

Example of deleting a dataset from its id, even if non-empty.
    
    
     String datasetName = "my_dataset_name";
     boolean deleted = bigquery.delete(datasetName, DatasetDeleteOption.deleteContents());
     if (deleted) {
       // the dataset was deleted
     } else {
       // the dataset was not found
     }
     

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`options` | `[DatasetDeleteOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.DatasetDeleteOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if dataset was deleted, `false` if it was not found  
  
### delete(String datasetId, String tableId) (deprecated)
    
    
    public abstract boolean delete(String datasetId, String tableId)

**Deprecated.** _Now that BigQuery datasets contain multiple resource types, this invocation is ambiguous. Please use more strongly typed version of`#delete` that leverages an non-ambiguous resource type identifier such as `TableId`._

Deletes the requested table.

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`tableId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if table was deleted, `false` if it was not found  
  
### getDataset(DatasetId datasetId, BigQuery.DatasetOption[] options)
    
    
    public abstract Dataset getDataset(DatasetId datasetId, BigQuery.DatasetOption[] options)

Returns the requested dataset or `null` if not found.

Example of getting a dataset.
    
    
     String projectId = "my_project_id";
     String datasetName = "my_dataset_name";
     DatasetId datasetId = DatasetId.of(projectId, datasetName);
     Dataset dataset = bigquery.getDataset(datasetId);
     

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[DatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetId)`  
  
`options` | `[DatasetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.DatasetOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset)` |   
  
### getDataset(String datasetId, BigQuery.DatasetOption[] options)
    
    
    public abstract Dataset getDataset(String datasetId, BigQuery.DatasetOption[] options)

Returns the requested dataset or `null` if not found.

Example of getting a dataset.
    
    
     String datasetName = "my_dataset";
     Dataset dataset = bigquery.getDataset(datasetName);
     

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`options` | `[DatasetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.DatasetOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset)` |   
  
### getIamPolicy(TableId tableId, BigQuery.IAMOption[] options)
    
    
    public abstract Policy getIamPolicy(TableId tableId, BigQuery.IAMOption[] options)

Gets the IAM policy for a specified table.

**Parameters**  
---  
**Name** | **Description**  
`tableId` | `[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId)`  
  
`options` | `[IAMOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.IAMOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.Policy` |   
  
### getJob(JobId jobId, BigQuery.JobOption[] options)
    
    
    public abstract Job getJob(JobId jobId, BigQuery.JobOption[] options)

Returns the requested job or `null` if not found. If the location of the job is not "US" or "EU", the `jobId` must specify the job location.

Example of getting a job.
    
    
     String jobName = "my_job_name";
     JobId jobIdObject = JobId.of(jobName);
     Job job = bigquery.getJob(jobIdObject);
     if (job == null) {
       // job was not found
     }
     

**Parameters**  
---  
**Name** | **Description**  
`jobId` | `[JobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobId)`  
  
`options` | `[JobOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.JobOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job)` |   
  
### getJob(String jobId, BigQuery.JobOption[] options)
    
    
    public abstract Job getJob(String jobId, BigQuery.JobOption[] options)

Returns the requested job or `null` if not found. If the location of the job is not "US" or "EU", [#getJob(JobId, JobOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery#com_google_cloud_bigquery_BigQuery_getJob_) must be used instead.

Example of getting a job.
    
    
     String jobName = "my_job_name";
     Job job = bigquery.getJob(jobName);
     if (job == null) {
       // job was not found
     }
     

**Parameters**  
---  
**Name** | **Description**  
`jobId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`options` | `[JobOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.JobOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job)` |   
  
### getModel(ModelId tableId, BigQuery.ModelOption[] options)
    
    
    public abstract Model getModel(ModelId tableId, BigQuery.ModelOption[] options)

Returns the requested model or `null` if not found.

Example of getting a model.
    
    
     String projectId = "my_project_id";
     String datasetName = "my_dataset_name";
     String modelName = "my_model_name";
     ModelId modelId = ModelId.of(projectId, datasetName, tableName);
     Model model = bigquery.getModel(modelId);
     

**Parameters**  
---  
**Name** | **Description**  
`tableId` | `[ModelId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ModelId)`  
  
`options` | `[ModelOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.ModelOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Model)` |   
  
### getModel(String datasetId, String modelId, BigQuery.ModelOption[] options)
    
    
    public abstract Model getModel(String datasetId, String modelId, BigQuery.ModelOption[] options)

Returns the requested model or `null` if not found.

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`modelId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`options` | `[ModelOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.ModelOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Model)` |   
  
### getQueryResults(JobId jobId, BigQuery.QueryResultsOption[] options)
    
    
    public abstract QueryResponse getQueryResults(JobId jobId, BigQuery.QueryResultsOption[] options)

**Internal Only** : This feature is not stable for application use.

Returns results of the query associated with the provided job.

Users are encouraged to use [Job#getQueryResults(QueryResultsOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job#com_google_cloud_bigquery_Job_getQueryResults_) instead.

**Parameters**  
---  
**Name** | **Description**  
`jobId` | `[JobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobId)`  
  
`options` | `[QueryResultsOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.QueryResultsOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[QueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryResponse)` |   
  
### getRoutine(RoutineId routineId, BigQuery.RoutineOption[] options)
    
    
    public abstract Routine getRoutine(RoutineId routineId, BigQuery.RoutineOption[] options)

Returns the requested routine or `null` if not found.

**Parameters**  
---  
**Name** | **Description**  
`routineId` | `[RoutineId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.RoutineId)`  
  
`options` | `[RoutineOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.RoutineOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Routine](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Routine)` |   
  
### getRoutine(String datasetId, String routineId, BigQuery.RoutineOption[] options)
    
    
    public abstract Routine getRoutine(String datasetId, String routineId, BigQuery.RoutineOption[] options)

Returns the requested routine or `null` if not found.

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`routineId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`options` | `[RoutineOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.RoutineOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Routine](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Routine)` |   
  
### getTable(TableId tableId, BigQuery.TableOption[] options)
    
    
    public abstract Table getTable(TableId tableId, BigQuery.TableOption[] options)

Returns the requested table or `null` if not found.

Example of getting a table.
    
    
     String projectId = "my_project_id";
     String datasetName = "my_dataset_name";
     String tableName = "my_table_name";
     TableId tableId = TableId.of(projectId, datasetName, tableName);
     Table table = bigquery.getTable(tableId);
     

**Parameters**  
---  
**Name** | **Description**  
`tableId` | `[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId)`  
  
`options` | `[TableOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.TableOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Table)` |   
  
### getTable(String datasetId, String tableId, BigQuery.TableOption[] options)
    
    
    public abstract Table getTable(String datasetId, String tableId, BigQuery.TableOption[] options)

Returns the requested table or `null` if not found.

Example of getting a table.
    
    
     String datasetName = "my_dataset_name";
     String tableName = "my_table_name";
     Table table = bigquery.getTable(datasetName, tableName);
     

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`tableId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`options` | `[TableOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.TableOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Table)` |   
  
### insertAll(InsertAllRequest request)
    
    
    public abstract InsertAllResponse insertAll(InsertAllRequest request)

Sends an insert all request.

Example of inserting rows into a table without running a load job. To prevent duplicate rows, this method does not perform automatic retries unless insert IDs are provided. Transient service errors (such as UNAVAILABLE) may be thrown and should be handled by the caller when insert IDs are not provided.
    
    
     String datasetName = "my_dataset_name";
     String tableName = "my_table_name";
     TableId tableId = TableId.of(datasetName, tableName);
     // Values of the row to insert
     Map<String, Object> rowContent = new HashMap<>();
     rowContent.put("booleanField", true);
     // Bytes are passed in base64
     rowContent.put("bytesField", "Cg0NDg0="); // 0xA, 0xD, 0xD, 0xE, 0xD in base64
     // Records are passed as a map
     Map<String, Object> recordsContent = new HashMap<>();
     recordsContent.put("stringField", "Hello, World!");
     rowContent.put("recordField", recordsContent);
     InsertAllResponse response = bigquery.insertAll(InsertAllRequest.newBuilder(tableId).addRow("rowId", rowContent)
         // More rows can be added in the same RPC by invoking .addRow() on the
         // builder
         .build());
     if (response.hasErrors()) {
       // If any of the insertions failed, this lets you inspect the errors
       for (Entry<Long, List<BigQueryError>> entry : response.getInsertErrors().entrySet()) {
         // inspect row error
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertAllRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.InsertAllRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InsertAllResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.InsertAllResponse)` |   
  
### listDatasets(BigQuery.DatasetListOption[] options)
    
    
    public abstract Page<Dataset> listDatasets(BigQuery.DatasetListOption[] options)

Lists the project's datasets. This method returns partial information on each dataset: (Dataset#getDatasetId(), Dataset#getFriendlyName() and Dataset#getGeneratedId()). To get complete information use [#getDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery#com_google_cloud_bigquery_BigQuery_getDataset_).

Example of listing datasets, specifying the page size.
    
    
     // List datasets in the default project
     Page<Dataset> datasets = bigquery.listDatasets(DatasetListOption.pageSize(100));
     for (Dataset dataset : datasets.iterateAll()) {
       // do something with the dataset
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[DatasetListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.DatasetListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset)>` |   
  
### listDatasets(String projectId, BigQuery.DatasetListOption[] options)
    
    
    public abstract Page<Dataset> listDatasets(String projectId, BigQuery.DatasetListOption[] options)

Lists the datasets in the provided project. This method returns partial information on each dataset: (Dataset#getDatasetId(), Dataset#getFriendlyName() and Dataset#getGeneratedId()). To get complete information use either [#getDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery#com_google_cloud_bigquery_BigQuery_getDataset_).

Example of listing datasets in a project, specifying the page size.
    
    
     String projectId = "my_project_id";
     // List datasets in a specified project
     Page<Dataset> datasets = bigquery.listDatasets(projectId, DatasetListOption.pageSize(100));
     for (Dataset dataset : datasets.iterateAll()) {
       // do something with the dataset
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`options` | `[DatasetListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.DatasetListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset)>` |   
  
### listJobs(BigQuery.JobListOption[] options)
    
    
    public abstract Page<Job> listJobs(BigQuery.JobListOption[] options)

Lists the jobs.

Example of listing jobs, specifying the page size.
    
    
     Page<Job> jobs = bigquery.listJobs(JobListOption.pageSize(100));
     for (Job job : jobs.iterateAll()) {
       // do something with the job
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[JobListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.JobListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job)>` |   
  
### listModels(DatasetId datasetId, BigQuery.ModelListOption[] options)
    
    
    public abstract Page<Model> listModels(DatasetId datasetId, BigQuery.ModelListOption[] options)

Lists the models in the dataset.

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[DatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetId)`  
  
`options` | `[ModelListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.ModelListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Model)>` |   
  
### listModels(String datasetId, BigQuery.ModelListOption[] options)
    
    
    public abstract Page<Model> listModels(String datasetId, BigQuery.ModelListOption[] options)

Lists the models in the dataset.

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`options` | `[ModelListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.ModelListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Model)>` |   
  
### listPartitions(TableId tableId)
    
    
    public abstract List<String> listPartitions(TableId tableId)

**Parameter**  
---  
**Name** | **Description**  
`tableId` | `[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId)`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list of the partition ids present in the partitioned table  
  
### listProjects(BigQuery.ProjectListOption[] options)
    
    
    public abstract Page<Project> listProjects(BigQuery.ProjectListOption[] options)

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Lists the projects accessible to the caller.

**Parameter**  
---  
**Name** | **Description**  
`options` | `[ProjectListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.ProjectListOption)[]`  
options for listing projects  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Project)>` | a page of projects  
  
### listRoutines(DatasetId datasetId, BigQuery.RoutineListOption[] options)
    
    
    public abstract Page<Routine> listRoutines(DatasetId datasetId, BigQuery.RoutineListOption[] options)

Lists the routines in the specified dataset.

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[DatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetId)`  
  
`options` | `[RoutineListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.RoutineListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Routine](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Routine)>` |   
  
### listRoutines(String datasetId, BigQuery.RoutineListOption[] options)
    
    
    public abstract Page<Routine> listRoutines(String datasetId, BigQuery.RoutineListOption[] options)

Lists the routines in the specified dataset.

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`options` | `[RoutineListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.RoutineListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Routine](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Routine)>` |   
  
### listTableData(TableId tableId, BigQuery.TableDataListOption[] options)
    
    
    public abstract TableResult listTableData(TableId tableId, BigQuery.TableDataListOption[] options)

Lists the table's rows.

Example of listing table rows, specifying the page size.
    
    
     String datasetName = "my_dataset_name";
     String tableName = "my_table_name";
     TableId tableIdObject = TableId.of(datasetName, tableName);
     // This example reads the result 100 rows per RPC call. If there's no need
     // to limit the number,
     // simply omit the option.
     TableResult tableData = bigquery.listTableData(tableIdObject, TableDataListOption.pageSize(100));
     for (FieldValueList row : tableData.iterateAll()) {
       // do something with the row
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tableId` | `[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId)`  
  
`options` | `[TableDataListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.TableDataListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult)` |   
  
### listTableData(TableId tableId, Schema schema, BigQuery.TableDataListOption[] options)
    
    
    public abstract TableResult listTableData(TableId tableId, Schema schema, BigQuery.TableDataListOption[] options)

Lists the table's rows. If the `schema` is not `null`, it is available to the [FieldValueList](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FieldValueList) iterated over.

Example of listing table rows with schema.
    
    
     Schema schema = Schema.of(Field.of("word", LegacySQLTypeName.STRING),
         Field.of("word_count", LegacySQLTypeName.STRING), Field.of("corpus", LegacySQLTypeName.STRING),
         Field.of("corpus_date", LegacySQLTypeName.STRING));
     TableResult tableData = bigquery.listTableData(TableId.of("bigquery-public-data", "samples", "shakespeare"),
         schema);
     FieldValueList row = tableData.getValues().iterator().next();
     System.out.println(row.get("word").getStringValue());
     

**Parameters**  
---  
**Name** | **Description**  
`tableId` | `[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId)`  
  
`schema` | `[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Schema)`  
  
`options` | `[TableDataListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.TableDataListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult)` |   
  
### listTableData(String datasetId, String tableId, BigQuery.TableDataListOption[] options)
    
    
    public abstract TableResult listTableData(String datasetId, String tableId, BigQuery.TableDataListOption[] options)

Lists the table's rows.

Example of listing table rows, specifying the page size.
    
    
     String datasetName = "my_dataset_name";
     String tableName = "my_table_name";
     // This example reads the result 100 rows per RPC call. If there's no need
     // to limit the number,
     // simply omit the option.
     TableResult tableData = bigquery.listTableData(datasetName, tableName, TableDataListOption.pageSize(100));
     for (FieldValueList row : tableData.iterateAll()) {
       // do something with the row
     }
     

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`tableId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`options` | `[TableDataListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.TableDataListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult)` |   
  
### listTableData(String datasetId, String tableId, Schema schema, BigQuery.TableDataListOption[] options)
    
    
    public abstract TableResult listTableData(String datasetId, String tableId, Schema schema, BigQuery.TableDataListOption[] options)

Lists the table's rows. If the `schema` is not `null`, it is available to the [FieldValueList](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FieldValueList) iterated over.

Example of listing table rows with schema.
    
    
     String datasetName = "my_dataset_name";
     String tableName = "my_table_name";
     Schema schema = ...;
     String field = "field";
     TableResult tableData = bigquery.listTableData(datasetName, tableName, schema);
     for (FieldValueList row : tableData.iterateAll()) {
       row.get(field);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`tableId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`schema` | `[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Schema)`  
  
`options` | `[TableDataListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.TableDataListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult)` |   
  
### listTables(DatasetId datasetId, BigQuery.TableListOption[] options)
    
    
    public abstract Page<Table> listTables(DatasetId datasetId, BigQuery.TableListOption[] options)

Lists the tables in the dataset. This method returns partial information on each table: (Table#getTableId(), Table#getFriendlyName(), Table#getGeneratedId() and type, which is part of Table#getDefinition()). To get complete information use either [#getTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery#com_google_cloud_bigquery_BigQuery_getTable_).

Example of listing the tables in a dataset.
    
    
     String projectId = "my_project_id";
     String datasetName = "my_dataset_name";
     DatasetId datasetId = DatasetId.of(projectId, datasetName);
     Page<Table> tables = bigquery.listTables(datasetId, TableListOption.pageSize(100));
     for (Table table : tables.iterateAll()) {
       // do something with the table
     }
     

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[DatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetId)`  
  
`options` | `[TableListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.TableListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Table)>` |   
  
### listTables(String datasetId, BigQuery.TableListOption[] options)
    
    
    public abstract Page<Table> listTables(String datasetId, BigQuery.TableListOption[] options)

Lists the tables in the dataset. This method returns partial information on each table: (Table#getTableId(), Table#getFriendlyName(), Table#getGeneratedId() and type, which is part of Table#getDefinition()). To get complete information use either [#getTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery#com_google_cloud_bigquery_BigQuery_getTable_).

Example of listing the tables in a dataset, specifying the page size.
    
    
     String datasetName = "my_dataset_name";
     Page<Table> tables = bigquery.listTables(datasetName, TableListOption.pageSize(100));
     for (Table table : tables.iterateAll()) {
       // do something with the table
     }
     

**Parameters**  
---  
**Name** | **Description**  
`datasetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`options` | `[TableListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.TableListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Table)>` |   
  
### query(QueryJobConfiguration configuration, BigQuery.JobOption[] options)
    
    
    public abstract TableResult query(QueryJobConfiguration configuration, BigQuery.JobOption[] options)

Runs the query associated with the request, using an internally-generated random JobId.

If the location of the job is not "US" or "EU", #query(QueryJobConfiguration, JobId, JobOption...) must be used instead.

This method cannot be used in conjuction with [QueryJobConfiguration#dryRun()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration#com_google_cloud_bigquery_QueryJobConfiguration_dryRun__) queries. Since dry-run queries are not actually executed, there's no way to retrieve results.

Example of running a query.
    
    
     // BigQuery bigquery = BigQueryOptions.getDefaultInstance().getService();
     String query = "SELECT corpus FROM bigquery-public-data.samples.shakespeare GROUP BY corpus;";
     QueryJobConfiguration queryConfig = QueryJobConfiguration.newBuilder(query).build();
    
     // Print the results.
     for (FieldValueList row : bigquery.query(queryConfig).iterateAll()) {
       for (FieldValue val : row) {
         System.out.printf("%s,", val.toString());
       }
       System.out.printf("
    ");
     }
     

This method supports query-related preview features via environmental variables (enabled by setting the `QUERY_PREVIEW_ENABLED` environment variable to "TRUE"). Specifically, this method supports:

  * **Stateless queries** : query execution without corresponding job metadata 



The behaviour of these preview features is controlled by the bigquery service as well

**Parameters**  
---  
**Name** | **Description**  
`configuration` | `[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration)`  
  
`options` | `[JobOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.JobOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` | upon failure  
`[JobException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobException)` | upon failure  
  
### query(QueryJobConfiguration configuration, JobId jobId, BigQuery.JobOption[] options)
    
    
    public abstract TableResult query(QueryJobConfiguration configuration, JobId jobId, BigQuery.JobOption[] options)

Runs the query associated with the request, using the given JobId.

If the location of the job is not "US" or "EU", the `jobId` must specify the job location.

This method cannot be used in conjunction with [QueryJobConfiguration#dryRun()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration#com_google_cloud_bigquery_QueryJobConfiguration_dryRun__) queries. Since dry-run queries are not actually executed, there's no way to retrieve results.

See [#query(QueryJobConfiguration, JobOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery#com_google_cloud_bigquery_BigQuery_query_) for examples on populating a [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration).

**Parameters**  
---  
**Name** | **Description**  
`configuration` | `[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration)`  
  
`jobId` | `[JobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobId)`  
  
`options` | `[JobOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.JobOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` | upon failure  
`[JobException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobException)` | upon failure  
  
### queryArrow(QueryJobConfiguration configuration, BigQuery.JobOption[] options)
    
    
    public default ArrowQueryResult queryArrow(QueryJobConfiguration configuration, BigQuery.JobOption[] options)

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

**[Beta]** Runs the query associated with the request and returns an [ArrowQueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ArrowQueryResult) yielding Apache Arrow `VectorSchemaRoot` batches directly for zero-copy vector access.

Callers must manage off-heap native memory by closing the returned [ArrowQueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ArrowQueryResult) (e.g. via a `try-with-resources` block).

**Prerequisite:** Requires the BigQuery Storage Read API (` bigquerystorage.googleapis.com`) to be enabled on your GCP project.

**JVM Requirements (Java 16+):** Apache Arrow uses internal `java.nio` DirectByteBuffer access for off-heap buffer management. Applications running on Java 16 or newer must supply the following JVM argument:
    
    
     --add-opens=java.base/java.nio=org.apache.arrow.memory.core,ALL-UNNAMED
     

**Parameters**  
---  
**Name** | **Description**  
`configuration` | `[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration)`  
the query configuration  
`options` | `[JobOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.JobOption)[]`  
query options  
**Returns**  
---  
**Type** | **Description**  
`[ArrowQueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ArrowQueryResult)` | an [ArrowQueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ArrowQueryResult) streaming Arrow vectors  
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` | upon failure  
`[JobException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobException)` | upon failure  
  
### queryArrow(QueryJobConfiguration configuration, JobId jobId, BigQuery.JobOption[] options)
    
    
    public default ArrowQueryResult queryArrow(QueryJobConfiguration configuration, JobId jobId, BigQuery.JobOption[] options)

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

**[Beta]** Runs the query associated with the request, using the given JobId, and returns an [ArrowQueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ArrowQueryResult) yielding Apache Arrow `VectorSchemaRoot` batches directly for zero-copy vector access.

Callers must manage off-heap native memory by closing the returned [ArrowQueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ArrowQueryResult) (e.g. via a `try-with-resources` block).

**Prerequisite:** Requires the BigQuery Storage Read API (` bigquerystorage.googleapis.com`) to be enabled on your GCP project.

**JVM Requirements (Java 16+):** Apache Arrow uses internal `java.nio` DirectByteBuffer access for off-heap buffer management. Applications running on Java 16 or newer must supply the following JVM argument:
    
    
     --add-opens=java.base/java.nio=org.apache.arrow.memory.core,ALL-UNNAMED
     

**Parameters**  
---  
**Name** | **Description**  
`configuration` | `[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration)`  
the query configuration  
`jobId` | `[JobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobId)`  
the job ID to use  
`options` | `[JobOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.JobOption)[]`  
query options  
**Returns**  
---  
**Type** | **Description**  
`[ArrowQueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ArrowQueryResult)` | an [ArrowQueryResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ArrowQueryResult) streaming Arrow vectors  
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` | upon failure  
`[JobException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobException)` | upon failure  
  
### queryWithTimeout(QueryJobConfiguration configuration, JobId jobId, Long timeoutMs, BigQuery.JobOption[] options)
    
    
    public abstract Object queryWithTimeout(QueryJobConfiguration configuration, JobId jobId, Long timeoutMs, BigQuery.JobOption[] options)

Starts the query associated with the request, using the given JobId. It returns either TableResult for quick queries or Job object for long-running queries.

If the location of the job is not "US" or "EU", the `jobId` must specify the job location.

This method cannot be used in conjunction with [QueryJobConfiguration#dryRun()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration#com_google_cloud_bigquery_QueryJobConfiguration_dryRun__) queries. Since dry-run queries are not actually executed, there's no way to retrieve results.

See [#query(QueryJobConfiguration, JobOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery#com_google_cloud_bigquery_BigQuery_query_) for examples on populating a [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration).

**Parameters**  
---  
**Name** | **Description**  
`configuration` | `[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration)`  
  
`jobId` | `[JobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobId)`  
  
`timeoutMs` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
  
`options` | `[JobOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.JobOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` | upon failure  
`[JobException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobException)` | upon failure  
  
### setIamPolicy(TableId tableId, Policy policy, BigQuery.IAMOption[] options)
    
    
    public abstract Policy setIamPolicy(TableId tableId, Policy policy, BigQuery.IAMOption[] options)

Sets the IAM policy for a specified table.

**Parameters**  
---  
**Name** | **Description**  
`tableId` | `[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId)`  
  
`policy` | `com.google.cloud.Policy`  
  
`options` | `[IAMOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.IAMOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.Policy` |   
  
### testIamPermissions(TableId table, List<String> permissions, BigQuery.IAMOption[] options)
    
    
    public abstract List<String> testIamPermissions(TableId table, List<String> permissions, BigQuery.IAMOption[] options)

Tests whether the caller holds specific permissions on a BigQuery table. The returned list represents the subset of granted permissions.

**Parameters**  
---  
**Name** | **Description**  
`table` | `[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId)`  
  
`permissions` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
`options` | `[IAMOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.IAMOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### update(DatasetInfo datasetInfo, BigQuery.DatasetOption[] options)
    
    
    public abstract Dataset update(DatasetInfo datasetInfo, BigQuery.DatasetOption[] options)

Updates dataset information.

Example of updating a dataset by changing its description. 
    
    
     // String datasetName = "my_dataset_name";
     // String tableName = "my_table_name";
     // String newDescription = "new_description";
    
     Table beforeTable = bigquery.getTable(datasetName, tableName);
     TableInfo tableInfo = beforeTable.toBuilder().setDescription(newDescription).build();
     Table afterTable = bigquery.update(tableInfo);
     

**Parameters**  
---  
**Name** | **Description**  
`datasetInfo` | `[DatasetInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo)`  
  
`options` | `[DatasetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.DatasetOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset)` |   
  
### update(ModelInfo modelInfo, BigQuery.ModelOption[] options)
    
    
    public abstract Model update(ModelInfo modelInfo, BigQuery.ModelOption[] options)

Updates model information.

Example of updating a model by changing its description.
    
    
     String datasetName = "my_dataset_name";
     String modelName = "my_model_name";
     String newDescription = "new_description";
     Model beforeModel = bigquery.getModel(datasetName, modelName);
     ModelInfo modelInfo = beforeModel.toBuilder().setDescription(newDescription).build();
     Model afterModel = bigquery.update(modelInfo);
     

Example of updating a model by changing its expiration.
    
    
     String datasetName = "my_dataset_name";
     String modelName = "my_model_name";
     Model beforeModel = bigquery.getModel(datasetName, modelName);
    
     // Set model to expire 5 days from now.
     long expirationMillis = DateTime.now().plusDays(5).getMillis();
     ModelInfo modelInfo = beforeModel.toBuilder().setExpirationTime(expirationMillis).build();
     Model afterModel = bigquery.update(modelInfo);
     

**Parameters**  
---  
**Name** | **Description**  
`modelInfo` | `[ModelInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ModelInfo)`  
  
`options` | `[ModelOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.ModelOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Model)` |   
  
### update(RoutineInfo routineInfo, BigQuery.RoutineOption[] options)
    
    
    public abstract Routine update(RoutineInfo routineInfo, BigQuery.RoutineOption[] options)

Updates routine information.

**Parameters**  
---  
**Name** | **Description**  
`routineInfo` | `[RoutineInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.RoutineInfo)`  
  
`options` | `[RoutineOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.RoutineOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Routine](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Routine)` |   
  
### update(TableInfo tableInfo, BigQuery.TableOption[] options)
    
    
    public abstract Table update(TableInfo tableInfo, BigQuery.TableOption[] options)

Updates table information.

Example of updating a table by changing its description.
    
    
     String datasetName = "my_dataset_name";
     String tableName = "my_table_name";
     String newDescription = "new_description";
     Table beforeTable = bigquery.getTable(datasetName, tableName);
     TableInfo tableInfo = beforeTable.toBuilder().setDescription(newDescription).build();
     Table afterTable = bigquery.update(tableInfo);
     

Example of updating a table by changing its expiration.
    
    
     String datasetName = "my_dataset_name";
     String tableName = "my_table_name";
     Table beforeTable = bigquery.getTable(datasetName, tableName);
    
     // Set table to expire 5 days from now.
     long expirationMillis = DateTime.now().plusDays(5).getMillis();
     TableInfo tableInfo = beforeTable.toBuilder().setExpirationTime(expirationMillis).build();
     Table afterTable = bigquery.update(tableInfo);
     

**Parameters**  
---  
**Name** | **Description**  
`tableInfo` | `[TableInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableInfo)`  
  
`options` | `[TableOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.TableOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Table)` |   
  
### writer(JobId jobId, WriteChannelConfiguration writeChannelConfiguration)
    
    
    public abstract TableDataWriteChannel writer(JobId jobId, WriteChannelConfiguration writeChannelConfiguration)

Returns a channel to write data to be inserted into a BigQuery table. Data format and other options can be configured using the [WriteChannelConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.WriteChannelConfiguration) parameter. If the job is not in "US" or "EU", the `jobId` must contain the location of the job.

Example of creating a channel with which to write to a table.
    
    
     String datasetName = "my_dataset_name";
     String tableName = "my_table_name";
     String csvData = "StringValue1
    StringValue2
    ";
     String location = "us";
     TableId tableId = TableId.of(datasetName, tableName);
     WriteChannelConfiguration writeChannelConfiguration = WriteChannelConfiguration.newBuilder(tableId)
         .setFormatOptions(FormatOptions.csv()).build();
     // The location must be specified; other fields can be auto-detected.
     JobId jobId = JobId.newBuilder().setLocation(location).build();
     TableDataWriteChannel writer = bigquery.writer(jobId, writeChannelConfiguration);
     // Write data to writer
     try {
       writer.write(ByteBuffer.wrap(csvData.getBytes(Charsets.UTF_8)));
     } finally {
       writer.close();
     }
     // Get load job
     Job job = writer.getJob();
     job = job.waitFor();
     LoadStatistics stats = job.getStatistics();
     return stats.getOutputRows();
     

**Parameters**  
---  
**Name** | **Description**  
`jobId` | `[JobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobId)`  
  
`writeChannelConfiguration` | `[WriteChannelConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.WriteChannelConfiguration)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TableDataWriteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableDataWriteChannel)` |   
  
### writer(WriteChannelConfiguration writeChannelConfiguration)
    
    
    public abstract TableDataWriteChannel writer(WriteChannelConfiguration writeChannelConfiguration)

Returns a channel to write data to be inserted into a BigQuery table. Data format and other options can be configured using the [WriteChannelConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.WriteChannelConfiguration) parameter. If the job is not in "US" or "EU", [#writer(JobId, WriteChannelConfiguration)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery#com_google_cloud_bigquery_BigQuery_writer_com_google_cloud_bigquery_JobId_com_google_cloud_bigquery_WriteChannelConfiguration_) must be used instead.

Example of creating a channel with which to write to a table.
    
    
     String datasetName = "my_dataset_name";
     String tableName = "my_table_name";
     String csvData = "StringValue1
    StringValue2
    ";
     TableId tableId = TableId.of(datasetName, tableName);
     WriteChannelConfiguration writeChannelConfiguration = WriteChannelConfiguration.newBuilder(tableId)
         .setFormatOptions(FormatOptions.csv()).build();
     TableDataWriteChannel writer = bigquery.writer(writeChannelConfiguration);
     // Write data to writer
     try {
       writer.write(ByteBuffer.wrap(csvData.getBytes(Charsets.UTF_8)));
     } finally {
       writer.close();
     }
     // Get load job
     Job job = writer.getJob();
     job = job.waitFor();
     LoadStatistics stats = job.getStatistics();
     return stats.getOutputRows();
     

Example of writing a local file to a table.
    
    
     String datasetName = "my_dataset_name";
     String tableName = "my_table_name";
     Path csvPath = FileSystems.getDefault().getPath(".", "my-data.csv");
     String location = "us";
     TableId tableId = TableId.of(datasetName, tableName);
     WriteChannelConfiguration writeChannelConfiguration = WriteChannelConfiguration.newBuilder(tableId)
         .setFormatOptions(FormatOptions.csv()).build();
     // The location must be specified; other fields can be auto-detected.
     JobId jobId = JobId.newBuilder().setLocation(location).build();
     TableDataWriteChannel writer = bigquery.writer(jobId, writeChannelConfiguration);
     // Write data to writer
     try (OutputStream stream = Channels.newOutputStream(writer)) {
       Files.copy(csvPath, stream);
     }
     // Get load job
     Job job = writer.getJob();
     job = job.waitFor();
     LoadStatistics stats = job.getStatistics();
     return stats.getOutputRows();
     

**Parameter**  
---  
**Name** | **Description**  
`writeChannelConfiguration` | `[WriteChannelConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.WriteChannelConfiguration)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TableDataWriteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableDataWriteChannel)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

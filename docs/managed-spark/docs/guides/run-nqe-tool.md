---
url: https://docs.cloud.google.com/managed-spark/docs/guides/run-nqe-tool/
title: Run the Native Query Execution qualification tool \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:17.763585+00:00
---

# Run the Native Query Execution qualification tool  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/run-nqe-tool/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Run the Native Query Execution qualification tool Stay organized with collections  Save and categorize content based on your preferences. 

To identify batch workloads that can achieve faster runtimes with Native Query Execution (NQE), you can use the qualification tool. The tool analyzes Spark event logs to estimate potential runtime savings and identify any operations that are not supported by the NQE engine.

Google Cloud provides two methods for running the qualification analysis: qualification job and qualification script. The recommended approach for most users is the qualification job, which automates the discovery and analysis of batch workloads. The alternative qualification script is available for the specific use case of analyzing a known event log file. Choose the method that best fits your use case:

  * Qualification Job (Recommended): This is the primary and recommended method. It is a PySpark job that automatically discovers and analyzes recent batch workloads across one or more Google Cloud projects and regions. Use this method when you want to perform a broad analysis without needing to manually locate individual event log files. This approach is ideal for large-scale evaluation of NQE suitability.

  * Qualification Script (Alternative): This is an alternative method for advanced or specific use cases. It is a shell script that analyzes a single Spark event log file or all event logs within a specific Cloud Storage directory. Use this method if you have the Cloud Storage path to the event logs you want to analyze.




### Qualification job

The qualification job simplifies large-scale analysis by programmatically scanning for Managed Service for Apache Spark batch workloads and submitting a distributed analysis job. The tool evaluates jobs across your organization, eliminating the need to manually find and specify event log paths.

## Grant IAM roles

For the qualification job to access batch workload metadata and read Spark event logs in Cloud Logging, the service account that runs the workload must have the following IAM roles granted in all projects to be analyzed:

  * [Managed Service for Apache Spark Viewer (roles/dataproc.viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.viewer)
  * [Logs Viewer (roles/logging.viewer)](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer)



## Submit the qualification job

You submit the qualification job using the gcloud CLI tool. The job includes a PySpark script and a JAR file that are hosted in a public Cloud Storage bucket.

You can run the job in either of the following execution environments:

  * As a Managed Service for Apache Spark batch workload. This is simple, stand-alone job execution.

  * As a job that runs on a Managed Service for Apache Spark cluster. This approach can be useful to integrate the job into a workflow.




## Job arguments

Argument | Description | Required? | Default Value  
---|---|---|---  
`--project-ids` | A single Project ID or a comma-separated list of Google Cloud project IDs to scan for batch workloads. | No | The project where the qualification job is running.  
`--regions` | A single region or a comma-separated list of regions to scan within the specified projects. | No | All regions within the specified projects.  
`--start-time` | The start date for filtering batches. Only batches created on or after this date (format: YYYY-MM-DD) will be analyzed. | No | No start date filter is applied.  
`--end-time` | The end date for filtering batches. Only batches created on or before this date (format: YYYY-MM-DD) will be analyzed. | No | No end date filter is applied.  
`--limit` | The maximum number of batches to analyze per region. The most recent batches are analyzed first. | No | All batches that match the other filter criteria are analyzed.  
`--output-gcs-path` | The Cloud Storage path (for example, `gs://your-bucket/output/`) where the result files will be written. | Yes | None.  
`--input-file` | The Cloud Storage path to a text file for bulk analysis. If provided, this argument overrides all other scope-defining arguments (`--project-ids`, `--regions`, `--start-time`, `--end-time`, `--limit`). | No | None.  
  
## Qualification job examples

  * A Managed Service for Apache Spark batch job to perform simple, ad-hoc analysis. Job arguments are listed after the `--` separator.
        
        gcloud dataproc batches submit pyspark gs://qualification-tool/performance-boost-qualification.py \
            --project=PROJECT_ID \
            --region=REGION \
            --jars=gs://qualification-tool/dataproc-perfboost-qualification-1.2.jar \
            -- \
            --project-ids=COMMA_SEPARATED_PROJECT_IDS \
            --regions=COMMA_SEPARATED_REGIONS \
            --limit=MAX_BATCHES \
            --output-gcs-path=gs://BUCKET
        

  * A Managed Service for Apache Spark batch job to analyze up to 50 of the most recent batches found in `sample_project` in the `us-central1` region, The results are written to bucket in Cloud Storage. Job arguments are listed after the `--` separator.
        
        gcloud dataproc batches submit pyspark gs://qualification-tool/performance-boost-qualification.py \
            --project=PROJECT_ID \
            --region=US-CENTRAL1 \
            --jars=gs://qualification-tool/dataproc-perfboost-qualification-1.2.jar \
            -- \
            --project-ids=PROJECT_ID \
            --regions=US-CENTRAL1 \
            --limit=50 \
            --output-gcs-path=gs://BUCKET/
        

  * A Managed Service for Apache Spark job submitted to a Managed Service for Apache Spark cluster for bulk analysis in a large-scale, repeatable, or automated analysis workflow. Job arguments are placed in an INPUT_FILE that is uploaded to a BUCKET in Cloud Storage. This method is ideal for scanning different date ranges or batch limits across different projects and regions in a single run.
        
        gcloud dataproc jobs submit pyspark gs://qualification-tool/performance-boost-qualification.py \
            --cluster=CLUSTER_NAME \
            --region=REGION \
            --jars=gs://qualification-tool/dataproc-perfboost-qualification-1.2.jar \
            -- \
            --input-file=gs://INPUT_FILE \
            --output-gcs-path=gs://BUCKET
        

Notes:

INPUT_FILE: Each line in the file represents a distinct analysis request and uses a format of single-letter flags followed by their values, such as, `-p PROJECT-ID -r REGION -s START_DATE -e END_DATE -l LIMITS`.

Example input file content:
        
        -p project1 -r us-central1 -s 2024-12-01 -e 2024-12-15 -l 100
        -p project2 -r europe-west1 -s 2024-11-15 -l 50
        

These arguments direct the tool to analyze the following two scopes:

    * Up to 100 batches in project1 in the `us-central1` region created between December 1, 2025 and December 15, 2025.
    * Up to 50 batches in project2 in the `europe-west1` region created on or after November 15, 2025.



### Qualification script

Use this method if you have the direct Cloud Storage path to a specific Spark event log that you want to analyze. This approach requires you to download and run a shell script, `run_qualification_tool.sh`, on a local machine or a Compute Engine VM that is configured with access to the event log file in Cloud Storage.

Perform the following steps to run the script against Managed Service for Apache Spark batch workload event files.

1.Copy the [`run_qualification_tool.sh`](https://storage.googleapis.com/qualification-tool/run_qualification_tool.sh) into a local directory that contains the Spark event files to analyze.

  1. Run the qualification script to analyze one event file or a set of event files contained in the script directory.
         
         ./run_qualification_tool.sh -f EVENT_FILE_PATH/EVENT_FILE_NAME \
             -o CUSTOM_OUTPUT_DIRECTORY_PATH \
             -k SERVICE_ACCOUNT_KEY  \
             -x MEMORY_ALLOCATEDg  \
             -t PARALLEL_THREADS_TO_RUN
         

**Flags and values:**

`-f` (required): See Spark event file locations to locate Spark workload event files.

     * EVENT_FILE_PATH (required unless EVENT_FILE_NAME is specified): Path of the event file to analyze. If not provided, the event file path is assumed to be the current directory.

     * EVENT_FILE_NAME (required unless EVENT_FILE_PATH is specified): Name of the event file to analyze. If not provided, the event files found recursively in the `EVENT_FILE_PATH` are analyzed.

`-o`(optional): If not provided, the tool creates or uses an existing `output` directory under the current directory to place output files.

     * CUSTOM_OUTPUT_DIRECTORY_PATH: Output directory path to output files.

`-k` (optional):

     * SERVICE_ACCOUNT_KEY: The [service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete) in JSON format if needed to access the EVENT_FILE_PATH.

`-x` (optional):

     * MEMORY_ALLOCATED: Memory in gigabytes to allocate to the tool. By default, the tool uses 80% of the free memory available in the system and all available machine cores.

`-t`(optional):

     * PARALLEL_THREADS_TO_RUN: The number of parallel threads for the tool to execute. By default, the tool executes all cores.

**Example command usage:**
    
    ./run_qualification_tool.sh -f gs://dataproc-temp-us-east1-9779/spark-job-history \
        -o perfboost-output -k /keys/event-file-key -x 34g -t 5
    

In this example, the qualification tool traverses the `gs://dataproc-temp-us-east1-9779/spark-job-history` directory, and analyzes Spark event files contained in this directories and its subdirectories. Access to the directory is provided the `/keys/event-file-key`. The tool uses `34 GB memory` for execution, and runs `5` parallel threads.




## Spark event file locations

Perform any of the following steps to find the Spark event files for Managed Service for Apache Spark batch workloads:

  1. In Cloud Storage, find the `spark.eventLog.dir` for the workload, then download it.

     1. If you can't find the `spark.eventLog.dir`, set the `spark.eventLog.dir` to a Cloud Storage location, and then rerun the workload and download the `spark.eventLog.dir`.
  2. If you have configured [Spark History Server](https://docs.cloud.google.com/managed-spark/docs/guides/monitor-troubleshoot-batches#persistent_history_server) for the batch job:

     1. Go to the Spark History Server, then select the workload.
     2. Click **Download** in the **Event Log** column.

**Tip:** Managed Service for Apache Spark job analysis: To run the qualification tool on [Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job) Spark jobs: 

  * Find the `spark.eventLog.dir` for the Managed Service for Apache Spark jobs in Cloud Storage, then download it. 
  * Run the tool against the event logs. If the tool recommends using Native Query Execution, migrate the jobs to Managed Service for Apache Spark batch workloads, then run the workloads with Native Query Execution. 



## Qualification tool output files

Once the qualification job or script analysis is complete, the qualification tool places the following output files in a `perfboost-output` directory in the current directory:

  * `AppsRecommendedForBoost.tsv`: A tab-separated list of applications recommended for use with Native Query Execution.

  * `UnsupportedOperators.tsv`: A tab-separated list of applications not recommended for use with Native Query Execution.


Qualification tool output file contents are tab-separated. You can view the files with a CSV or TSV file reader, such as Google Sheets.**Note:** When the qualification tool attempts to save an output file, if the file exists in the output directory, the tool adds an incremental suffix to the filename before saving the new file.

### `AppsRecommendedForBoost.tsv` output file

The following table shows the contents of a sample `AppsRecommendedForBoost.tsv` output file. It contains a row for each analysed application.

Sample `AppsRecommendedForBoost.tsv` output file:

applicationId | applicationName | rddPercentage | unsupportedSqlPercentage | totalTaskTime | supportedTaskTime | supportedSqlPercentage | recommendedForBoost | expectedRuntimeReduction  
---|---|---|---|---|---|---|---|---  
app-2024081/batches/083f6196248043938-000 | projects/example.com:dev/locations/us-central1  
6b4d6cae140f883c0  
11c8e | 0.00% | 0.00% | 548924253 | 548924253 | 100.00% | TRUE | 30.00%  
app-2024081/batches/60381cab738021457-000 | projects/example.com:dev/locations/us-central1  
474113a1462b426bf  
b3aeb | 0.00% | 0.00% | 514401703 | 514401703 | 100.00% | TRUE | 30.00%  
  
Column descriptions:

  * `applicationId`: The `ApplicationID` of the Spark application. Use this to identify the corresponding batch workload.

  * `applicationName`: The name of the Spark application.

  * `rddPercentage`: The percentage of RDD operations in the application. RDD operations are not supported by Native Query Execution.

  * `unsupportedSqlPercentage:` Percentage of SQL operations not supported by Native Query Execution.

  * `totalTaskTime`: Cumulative task time of all tasks executed during the application run.

  * `supportedTaskTime`: The total task time supported by Native Query Execution.




The following columns provide important information to help you determine if Native Query Execution can benefit your batch workload:

  * **`supportedSqlPercentage`:** The percentage of SQL operations supported by native query execution. The higher the percentage, the greater the runtime reduction that can be achieved by running the application with Native Query Execution.

  * **`recommendedForBoost`:** If `TRUE`, running the application with Native Query Execution is recommended. If `recommendedForBoost` is `FALSE`, **don't use Native Query Execution on the batch workload.**

  * **`expectedRuntimeReduction`:** The expected percentage reduction in application runtime when you run the application with Native Query Execution.




### `UnsupportedOperators.tsv` output file.

The `UnsupportedOperators.tsv` output file contains a list of operators used in workload applications that are not supported by Native Query Execution. Each row in the output file lists an unsupported operator.

**Note:** If you open a Google Cloud support ticket and include the `UnsupportedOperators.tsv` file, Managed Service for Apache Spark can evaluate supporting additional operators. For more information, see [Get support](https://docs.cloud.google.com/managed-spark/docs/support/getting-support).

Column descriptions:

  * `unsupportedOperator`: The name of the operator that is not supported by Native Query Execution.

  * `cumulativeCpuMs`: The number of CPU milliseconds consumed during the execution of the operator. This value reflects the relative importance of the operator in the application.

  * `count`: The number of times the operator is used in the application.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

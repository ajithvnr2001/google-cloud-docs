---
url: https://docs.cloud.google.com/mainframe-connector/docs/standalone-mode/
title: Run Mainframe Connector in standalone mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:55.712970+00:00
---

# Run Mainframe Connector in standalone mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/standalone-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-connector/docs/overview)



Send feedback 

#  Run Mainframe Connector in standalone mode Stay organized with collections  Save and categorize content based on your preferences. 

Mainframe Connector version 5.13.0 and later supports running Mainframe Connector as a standalone job on Google Cloud. This feature lets you run Mainframe Connector as a containerized batch job, for example, as a Cloud Run job, Google Kubernetes Engine job, or within a Docker container. This option helps you avoid installing Mainframe Connector locally on your mainframe, and makes it easier for you to integrate your mainframe queued sequential access method (QSAM) file parsing to existing extract, transform, and load (ETL) workflows.

When you use the standalone version of the Mainframe Connector, you must set up the ETL workflow that loads the QSAM file to Google Cloud by yourself.

## Before you begin

  * [Deploy Mainframe Connector on Cloud Run](https://docs.cloud.google.com/mainframe-connector/docs/deploy-mainframe-connector).
  * [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) or identify an existing service account to use with Mainframe Connector. This service account must have permissions to access Cloud Storage buckets, BigQuery datasets, and any other Google Cloud resource that you want to use.
  * Ensure that the service account you created is assigned the [Cloud Run Invoker role](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.invoker).
  * Ensure that the mainframe data is already available on Google Cloud as a QSAM file.



## Transcode data using Mainframe Connector in standalone mode on Cloud Run

Mainframe Connector provides two ways in which you can run Mainframe Connector as a standalone job on Google Cloud:

  * Using `qsam` commands (release 5.16.0 and later)
  * Using the `gsutil cp` command



### Advantages of `qsam` commands

The `qsam` commands provide the following advantages:

  * Support for compound data types, including the OCCURS clause (lists), REDEFINES clause, and nested records. For more information about these data types, see [`qsam` and `vsam` transcoding reference](https://docs.cloud.google.com/mainframe-connector/docs/qsam-vsam-transcoding).
  * Support for the configuration of the transcoding process through a [transcoder configuration file](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration). This capability offers more flexibility when decoding data to Google Cloud, and encoding the data back to the mainframe.
  * Support for the creation of a [spillover dataset](https://docs.cloud.google.com/mainframe-connector/docs/spillover-dataset), which is a table of transcoding errors that can be used for error inspection.
  * Support for [multiple input and output formats](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#transcodeformat). This capability lets you load your data to and from various data warehouses.



### Run Mainframe Connector in standalone mode using `qsam` commands

To transcode your data using Mainframe Connector in standalone mode using `qsam` commands, use the following steps:

  1. Create a YAML file with commands to do the following:

     * Read your dataset
     * Transcode it to a [supported format](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#transcodeformat)
     * Upload it to Cloud Storage

The input dataset must be a QSAM file with fixed or variable record length. You can use the following sample YAML file to read your dataset, transcode it to the ORC format, and upload it to Cloud Storage.

In the following sample, we use the Cloud Storage [`DataPath`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#datapath) for `INFILE`, `OUTFILE`, `COPYBOOK`, and `TRANSCODE_CONFIGURATION`.
    
    environmentVariables:
    - name: "INFILE"
      value: "INFILE"
    - name: "OUTFILE"
      value: "OUTFILE"
    - name: "COPYBOOK"
      value: "COPYBOOK"
    - name: "TRANSCODE_CONFIGURATION"
      value: "TRANSCODE_CONFIGURATION"
    - name: "LOG_PROJECT"
      value: "LOG_PROJECT"
    - name: "IBM_JAVA_OPTIONS"
      value: "-XX:+UseContainerSupport"
    
    command:
      qsam decode $INFILE $OUTFILE
      --copybook $COPYBOOK
      --transcode-configuration ${TRANSCODE_CONFIGURATION}
      --output-format orc
      --parallelism 8
      --chunk-size "512Mib"
    

Replace the following:

     * `INFILE`: The name of the input file.
     * `OUTFILE`: The name of the output file.
     * `COPYBOOK_PATH`: The path to the copybook DD.
     * `TRANSCODE_CONFIGURATION_PATH`: The path to the transcode configuration file.
     * `LOG_PROJECT`: The name of the log project.

The following is an example YAML file:
    
    environmentVariables:
    - name: "INFILE"
      value: "gs://my_bucket/my/input.dat"
    - name: "OUTFILE"
      value: "gs://my_bucket/my/output.orc"
    - name: "COPYBOOK"
      value: "gs://my_bucket/my/copybook.cpy"
    - name: "TRANSCODE_CONFIGURATION"
      value: "gs://my_bucket/my/transcode-configuration-file.json"
    - name: "LOG_PROJECT"
      value: "the log project"
    - name: "IBM_JAVA_OPTIONS"
      value: "-XX:+UseContainerSupport"
    command:
      qsam decode $INFILE $OUTFILE
      --copybook $COPYBOOK
      --transcode-configuration ${TRANSCODE_CONFIGURATION}
      --output-format orc
      --parallelism 8
      --chunk-size "512Mib"
    

**Note**

     * Variables with the suffix `FILLER` are ignored during the import process.
     * Starting from version 5.12.0, Mainframe Connector replaces hyphens ("-") with underscores ("_") in variable names. If you want to keep hyphens in your variable names, disable this automatic conversion by setting the database variable `BQSH_FEATURE_CONVERT_UNDERSCORE_IN_FIELDS_NAME` to `false`.
  2. Create a `job.yaml` file with the following command.
         
         kind: Job
         metadata:
           name: JOB
         spec:
           template:
             spec:
               template:
                 spec:
                   containers:
                   - image: IMAGE
                     command:
                     - bash
                     - /opt/mainframe-connector/standalone.sh
                     - --argsFrom
                     - LOCATION_OF_THE_COMMAND_YAML_FILE
         

Replace the following:

     * JOB: the name of your Cloud Run job. Job names must be 49 characters or less and must be unique per region and project.
     * IMAGE: the URL of job container image, for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * LOCATION_OF_THE_COMMAND_YAML_FILE: the location of the YAML file that you created in the previous step.
  3. Deploy the new job using the following command:
         
         gcloud run jobs replace job.yaml
         

  4. Run the job using the following command:
         
         gcloud run jobs execute JOB_NAME

Replace JOB_NAME with the name of the job.




For more information on creating and executing a Cloud Run job, see [Create a new job](https://docs.cloud.google.com/run/docs/create-jobs#job) and [Execute a job](https://docs.cloud.google.com/run/docs/execute/jobs#execute_jobs).

### Run Mainframe Connector in standalone mode using the `gsutil cp` command

To transcode your data using Mainframe Connector in standalone mode using the `gsutil cp` command, use the following steps:

  1. Create a YAML file with commands to do the following:

     * Read your dataset
     * Transcode it to ORC
     * Upload it to Cloud Storage

The input dataset must be a QSAM file with fixed or variable record length. You can use the following sample YAML file to read your dataset, transcode it to the ORC format, and upload it to Cloud Storage.

In the following sample, read the data from the [INFILE dataset](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names), and the record layout from the [COPYBOOK DD](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names).
    
    environmentVariables:
    - name: "INFILE"
      value: "INFILE"
    - name: "INFILE_DSN"
      value: "INFILE_DSN"
    - name: "GCSDSNURI"
      value: "INFILE_DSN_FILEPATH"
    - name: "COPYBOOK"
      value: "COPYBOOK_FILEPATH"
    - name: "LOG_PROJECT"
      value: "LOG_PROJECT"
    - name: "IBM_JAVA_OPTIONS"
      value: "-XX:+UseContainerSupport"
    command:
      gsutil cp gs://outputbucket/output
      --parallelism 8
      --maxChunkSize "512Mib"
      --parser_type=copybook
    

Replace the following:

     * `INFILE`: The name of the input file.
     * `INFILE_DSN`: The name of the input Data Source Name (DSN) file.
     * `INFILE_DSN_FILEPATH`: The path to the input DSN file.
     * `COPYBOOK_FILEPATH`: The path to the copybook DD.
     * `LOG_PROJECT`: The name of the log project.

The following is an example YAML file:
    
    environmentVariables:
      - name: "INFILE"
        value: "input.dat"
      - name: "INFILE_DSN"
        value: "input.dat"
      - name: "GCSDSNURI"
        value: "gs://inputbucket/inputfolder"
      - name: "COPYBOOK"
        value: "gs://inputbucket/copybook.cpy"
      - name: "LOG_PROJECT"
        value: "the log project"
      - name: "IBM_JAVA_OPTIONS"
        value: "-XX:+UseContainerSupport"
      command:
        gsutil cp gs://outputbucket/output
        --parallelism 8
        --maxChunkSize "512Mib"
        --parser_type=copybook
    

**Note**

     * Variables with the suffix `FILLER` are ignored during the import process.
     * Starting from version 5.12.0, Mainframe Connector replaces hyphens ("-") with underscores ("_") in variable names. If you want to keep hyphens in your variable names, disable this automatic conversion by setting the database variable `BQSH_FEATURE_CONVERT_UNDERSCORE_IN_FIELDS_NAME` to `false`.

For the complete list of environment variables supported by Mainframe Connector, see [Environment variables](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables).

If you want to log the commands executed during this process, you can [enable load statistics](https://docs.cloud.google.com/mainframe-connector/docs/reference#enable_load_statistics).

  2. Create a `job.yaml` file with the following command.
         
         kind: Job
         metadata:
           name: JOB
         spec:
           template:
             spec:
               template:
                 spec:
                   containers:
                   - image: IMAGE
                     command:
                     - bash
                     - /opt/mainframe-connector/standalone.sh
                     - --argsFrom
                     - LOCATION_OF_THE_COMMAND_YAML_FILE
         

Replace the following:

     * JOB: the name of your Cloud Run job. Job names must be 49 characters or less and must be unique per region and project.
     * IMAGE: the URL of job container image, for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * LOCATION_OF_THE_COMMAND_YAML_FILE: the location of the YAML file that you created in the previous step.
  3. Deploy the new job using the following command:
         
         gcloud run jobs replace job.yaml
         

  4. Run the job using the following command:
         
         gcloud run jobs execute JOB_NAME

Replace JOB_NAME with the name of the job.




For more information on creating and executing a Cloud Run job, see [Create a new job](https://docs.cloud.google.com/run/docs/create-jobs#job) and [Execute a job](https://docs.cloud.google.com/run/docs/execute/jobs#execute_jobs).

## Export BigQuery table into Mainframe dataset

You can export BigQuery table into mainframe dataset by creating a YAML file that executes a SQL read from the [QUERY DD file](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names), and exports the resulting dataset to Cloud Storage as a binary file, as follows.

The steps to create and execute the Cloud Run job are the same as mentioned in the section Transcode data using Mainframe Connector in standalone mode on Cloud Run. The only difference is the instructions mentioned in the YAML file. Mainframe Connector provides two ways in which you can export BigQuery table:

  * Using `qsam` commands (release 5.16.0 and later)
  * Using the `bq export` command




###  Use `qsam` commands 
    
    
    environmentVariables:
      - name: "QUERY"
        value: "QUERY_PATH"
      - name: "OUTFILE"
        value: "OUTFILE"
      - name: "COPYBOOK"
        value: "COPYBOOK_PATH"
      - name: "TRANSCODE_CONFIGURATION"
        value: "TRANSCODE_CONFIGURATION_PATH"
      - name: "PROJECT_ID"
        value: "PROJECT_ID"
      - name: "LOCATION"
        value: "LOCATION"
      - name: "LOG_PROJECT"
        value: "LOG_PROJECT"
      - name: "IBM_JAVA_OPTIONS"
        value: "-XX:+UseContainerSupport"
    command:
    qsam encode \
      $QUERY
      $OUTFILE
      --copybook ${COPYBOOK_PATH}
      --transcode-configuration ${TRANSCODE_CONFIGURATION_PATH}
      --input-format=BIGQUERY \
      --input-parameter project_id=${PROJECT_ID} \
      --input-parameter location=${LOCATION}
    

Replace the following:

  * `QUERY_PATH`: The SQL query to execute. The result of the query will be encoded into a binary file.
  * `OUTFILE`: The Cloud Storage bucket that will contain the output binary file.
  * `COPYBOOK_PATH`: The path to the copybook DD.
  * `TRANSCODE_CONFIGURATION_PATH`: The path to the transcoder configuration file.
  * `LOG_PROJECT`: The name of the log project.
  * `PROJECT_ID`: The project ID in which you want to execute the query.
  * `LOCATION`: The a region or multi-region where the query will be executed. We recommended that you run the query in a location close to the data. The default value is US.



The following is an example YAML file:
    
    
    environmentVariables:
    - name: "QUERY"
      value: "gs://my_bucket/my/input.sql"
    - name: "OUTFILE"
      value: "gs://my_bucket/my/output.orc"
    - name: "COPYBOOK"
      value: "gs://my_bucket/my/copybook.cpy"
    - name: "TRANSCODE_CONFIGURATION"
      value: "gs://my_bucket/my/transcode-configuration-file.json"
    - name: "PROJECT_ID"
      value: "my-project"
    - name: "LOCATION"
      value: "US"
    - name: "LOG_PROJECT"
      value: "my-log-project"
    - name: "IBM_JAVA_OPTIONS"
      value: "-XX:+UseContainerSupport"
      command:
      qsam encode \
        $QUERY
        $OUTFILE
        --copybook ${COPYBOOK_PATH}
        --transcode-configuration ${TRANSCODE_CONFIGURATION_PATH}
        --input-format=BIGQUERY \
        --input-parameter project_id=${PROJECT_ID} \
        --input-parameter location=${LOCATION}
    

###  Use `bq export` command 
    
    
    environmentVariables:
    - name: "COPYBOOK"
      value: "COPYBOOK_FILEPATH"
    - name: "LOG_PROJECT"
      value: "LOG_PROJECT"
    - name: "IBM_JAVA_OPTIONS"
      value: "-XX:+UseContainerSupport"
    command:
      bq export --project_id="PROJECT_NAME" --location="LOCATION" --sql="select * from project.dataset.table" --bucket="BUCKET"
    

Replace the following:

  * `COPYBOOK_FILEPATH`: The path to the copybook DD.
  * `LOG_PROJECT`: The name of the log project.
  * `PROJECT_NAME`: The name of the project in which you want to execute the query.
  * `LOCATION`: The location for where the query will be executed. We recommended that you execute the query in a location close to the data.
  * `BUCKET`: The Cloud Storage URI that will contain the output binary file.



The following is an example YAML file:
    
    
    environmentVariables:
    - name: "COPYBOOK"
      value: "gs://inputbucket/copybook.cpy"
    - name: "LOG_PROJECT"
      value: "my-log-project"
    - name: "IBM_JAVA_OPTIONS"
      value: "-XX:+UseContainerSupport"
    command:
      bq export --project_id="my-project" --run_mode="gcsoutput" --location=US --sql="select * from project.dataset.table" --bucket="gs://outputbucket/data.dat"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

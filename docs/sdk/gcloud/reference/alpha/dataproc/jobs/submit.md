---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/
title: gcloud alpha dataproc jobs submit \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:32:04.438987+00:00
---

# gcloud alpha dataproc jobs submit  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataproc jobs submit Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataproc jobs submit - submit Dataproc jobs to execute on a cluster 
SYNOPSIS
    

`gcloud alpha dataproc jobs submit` `COMMAND` [`--async`] [`--bucket`=`BUCKET`] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Submit Dataproc jobs to execute on a cluster. 
EXAMPLES
     To submit a Hadoop MapReduce job, run: 
    
    
    [gcloud alpha dataproc jobs submit hadoop](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/hadoop) --cluster my-cluster --jar my_jar.jar -- arg1 arg2

To submit a Spark Scala or Java job, run: 
    
    
    [gcloud alpha dataproc jobs submit spark](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/spark) --cluster my-cluster --jar my_jar.jar -- arg1 arg2

To submit a PySpark job, run: 
    
    
    [gcloud alpha dataproc jobs submit pyspark](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/pyspark) --cluster my-cluster my_script.py -- arg1 arg2

To submit a Spark SQL job, run: 
    
    
    [gcloud alpha dataproc jobs submit spark-sql](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/spark-sql) --cluster my-cluster --file my_queries.q

To submit a Pig job, run: 
    
    
    [gcloud alpha dataproc jobs submit pig](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/pig) --cluster my-cluster --file my_script.pig

To submit a Hive job, run: 
    
    
    [gcloud alpha dataproc jobs submit hive](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/hive) --cluster my-cluster --file my_queries.q

FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--bucket`=`BUCKET`
     The Cloud Storage bucket to stage files in. Defaults to the cluster's configured bucket. 
`--region`=`REGION`
     Dataproc region to use. Each Dataproc region constitutes an independent resource namespace constrained to deploying instances into Compute Engine zones inside the region. Overrides the default `dataproc/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[flink](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/flink)`
     `(ALPHA)` Submit a Flink job to a cluster. 
`[hadoop](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/hadoop)`
     `(ALPHA)` Submit a Hadoop job to a cluster. 
`[hive](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/hive)`
     `(ALPHA)` Submit a Hive job to a cluster. 
`[pig](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/pig)`
     `(ALPHA)` Submit a Pig job to a cluster. 
`[presto](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/presto)`
     `(ALPHA)` Submit a Presto job to a cluster. 
`[pyspark](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/pyspark)`
     `(ALPHA)` Submit a PySpark job to a cluster. 
`[spark](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/spark)`
     `(ALPHA)` Submit a Spark job to a cluster. 
`[spark-r](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/spark-r)`
     `(ALPHA)` Submit a SparkR job to a cluster. 
`[spark-sql](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/spark-sql)`
     `(ALPHA)` Submit a Spark SQL job to a cluster. 
`[trino](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/trino)`
     `(ALPHA)` Submit a Trino job to a cluster. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud dataproc jobs submit](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit)
    
    
    [gcloud beta dataproc jobs submit](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/submit)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

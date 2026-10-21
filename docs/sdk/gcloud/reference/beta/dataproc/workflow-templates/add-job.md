---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/
title: gcloud beta dataproc workflow-templates add-job \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:08:58.467723+00:00
---

# gcloud beta dataproc workflow-templates add-job  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataproc workflow-templates add-job Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataproc workflow-templates add-job - add Dataproc jobs to workflow template 
SYNOPSIS
    

`gcloud beta dataproc workflow-templates add-job` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To add a Hadoop MapReduce job, run: 
    
    
    [gcloud beta dataproc workflow-templates add-job hadoop](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/hadoop) --workflow-template my_template --jar my_jar.jar -- arg1 arg2

To add a Spark Scala or Java job, run: 
    
    
    [gcloud beta dataproc workflow-templates add-job spark](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/spark) --workflow-template my_template --jar my_jar.jar -- arg1 arg2

To add a PySpark job, run: 
    
    
    [gcloud beta dataproc workflow-templates add-job pyspark](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/pyspark) --workflow-template my_template my_script.py -- arg1 arg2

To add a Spark SQL job, run: 
    
    
    [gcloud beta dataproc workflow-templates add-job spark-sql](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/spark-sql) --workflow-template my_template --file my_queries.q

To add a Pig job, run: 
    
    
    [gcloud beta dataproc workflow-templates add-job pig](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/pig) --workflow-template my_template --file my_script.pig

To add a Hive job, run: 
    
    
    [gcloud beta dataproc workflow-templates add-job hive](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/hive) --workflow-template my_template --file my_queries.q

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[hadoop](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/hadoop)`
     `(BETA)` Add a hadoop job to the workflow template. 
`[hive](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/hive)`
     `(BETA)` Add a Hive job to the workflow template. 
`[pig](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/pig)`
     `(BETA)` Add a Pig job to the workflow template. 
`[presto](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/presto)`
     `(BETA)` Add a Presto job to the workflow template. 
`[pyspark](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/pyspark)`
     `(BETA)` Add a PySpark job to the workflow template. 
`[spark](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/spark)`
     `(BETA)` Add a Spark job to the workflow template. 
`[spark-r](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/spark-r)`
     `(BETA)` Add a SparkR job to the workflow template. 
`[spark-sql](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/spark-sql)`
     `(BETA)` Add a SparkSql job to the workflow template. 
`[trino](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/trino)`
     `(BETA)` Add a Trino job to the workflow template. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud dataproc workflow-templates add-job](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job)
    
    
    [gcloud alpha dataproc workflow-templates add-job](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/add-job)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

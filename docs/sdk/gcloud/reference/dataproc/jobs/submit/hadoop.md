---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop/
title: gcloud dataproc jobs submit hadoop \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:50:13.982505+00:00
---

# gcloud dataproc jobs submit hadoop  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dataproc jobs submit hadoop Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dataproc jobs submit hadoop - submit a Hadoop job to a cluster 
SYNOPSIS
    

`gcloud dataproc jobs submit hadoop` (`--class`=`MAIN_CLASS` | `--jar`=`MAIN_JAR`) (`--cluster`=`CLUSTER` | `--cluster-labels`=[`KEY`=`VALUE`,…]) [`--archives`=[`ARCHIVE`,…]] [`--async`] [`--bucket`=`BUCKET`] [`--driver-log-levels`=[`PACKAGE`=`LEVEL`,…]] [`--driver-required-memory-mb`=`DRIVER_REQUIRED_MEMORY_MB`] [`--driver-required-vcores`=`DRIVER_REQUIRED_VCORES`] [`--files`=[`FILE`,…]] [`--jars`=[`JAR`,…]] [`--labels`=[`KEY`=`VALUE`,…]] [`--max-failures-per-hour`=`MAX_FAILURES_PER_HOUR`] [`--max-failures-total`=`MAX_FAILURES_TOTAL`] [`--properties`=[`PROPERTY`=`VALUE`,…]] [`--properties-file`=`PROPERTIES_FILE`] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`] [-- `JOB_ARGS` …]
DESCRIPTION
     Submit a Hadoop job to a cluster. 
EXAMPLES
     To submit a Hadoop job that runs the main class of a jar, run: 
    
    
    gcloud dataproc jobs submit hadoop --cluster=my-cluster --jar=my_jar.jar -- arg1 arg2

To submit a Hadoop job that runs a specific class of a jar, run: 
    
    
    gcloud dataproc jobs submit hadoop --cluster=my-cluster --class=org.my.main.Class --jars=my_jar1.jar,my_jar2.jar -- arg1 arg2

To submit a Hadoop job that runs a jar that is already on the cluster, run: 
    
    
    gcloud dataproc jobs submit hadoop --cluster=my-cluster --jar=file:///usr/lib/hadoop-op/hadoop-op-examples.jar -- wordcount gs://my_bucket/my_file.txt gs://my_bucket/output

POSITIONAL ARGUMENTS
    

[-- `JOB_ARGS` …]
     The arguments to pass to the driver. 

The '--' argument must be specified between gcloud specific args on the left and JOB_ARGS on the right. 

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--class`=`MAIN_CLASS`
     The class containing the main method of the driver. Must be in a provided jar or jar that is already on the classpath 
`--jar`=`MAIN_JAR`
     The HCFS URI of jar file containing the driver jar. 
Exactly one of these must be specified: 

`--cluster`=`CLUSTER`
     The Dataproc cluster to submit the job to. 
`--cluster-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

Labels of Dataproc cluster on which to place the job. 

OPTIONAL FLAGS
    

`--archives`=[`ARCHIVE`,…]
     Comma separated list of archives to be provided to the job. must be one of the following file formats: .zip, .tar, .tar.gz, or .tgz. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--bucket`=`BUCKET`
     The Cloud Storage bucket to stage files in. Defaults to the cluster's configured bucket. 
`--driver-log-levels`=[`PACKAGE`=`LEVEL`,…]
     A list of package to log4j log level pairs to configure driver logging. For example: root=FATAL,com.example=INFO 
`--driver-required-memory-mb`=`DRIVER_REQUIRED_MEMORY_MB`
     The memory allocation requested by the job driver in megabytes (MB) for execution on the driver node group (it is used only by clusters with a driver node group). 
`--driver-required-vcores`=`DRIVER_REQUIRED_VCORES`
     The vCPU allocation requested by the job driver for execution on the driver node group (it is used only by clusters with a driver node group). 
`--files`=[`FILE`,…]
     Comma separated list of file paths to be provided to the job. A file path can either be a path to a local file or a path to a file already in a Cloud Storage bucket. 
`--jars`=[`JAR`,…]
     Comma separated list of jar files to be provided to the MR and driver classpaths. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--max-failures-per-hour`=`MAX_FAILURES_PER_HOUR`
     Specifies the maximum number of times a job can be restarted per hour in event of failure. Default is 0 (no retries after job failure). 
`--max-failures-total`=`MAX_FAILURES_TOTAL`
     Specifies the maximum total number of times a job can be restarted after the job fails. Default is 0 (no retries after job failure). 
`--properties`=[`PROPERTY`=`VALUE`,…]
     A list of key value pairs to configure Hadoop. 
`--properties-file`=`PROPERTIES_FILE`
     Path to a local file or a file in a Cloud Storage bucket containing configuration properties for the job. The client machine running this command must have read permission to the file. 

Specify properties in the form of property=value in the text file. For example: 
    
    
      # Properties to set for the job:
      key1=value1
      key2=value2
      # Comment out properties not used.
      # key3=value3

If a property is set in both `--properties` and `--properties-file`, the value defined in `--properties` takes precedence. 

`--region`=`REGION`
     Dataproc region to use. Each Dataproc region constitutes an independent resource namespace constrained to deploying instances into Compute Engine zones inside the region. Overrides the default `dataproc/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha dataproc jobs submit hadoop](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/hadoop)
    
    
    [gcloud beta dataproc jobs submit hadoop](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/submit/hadoop)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 

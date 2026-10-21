---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/
title: gcloud dataproc batches submit \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:50:09.400141+00:00
---

# gcloud dataproc batches submit  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dataproc batches submit Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dataproc batches submit - submit a Dataproc batch job 
SYNOPSIS
    

`gcloud dataproc batches submit` `COMMAND` [`--async`] [`--batch`=`BATCH`] [`--container-image`=`CONTAINER_IMAGE`] [`--history-server-cluster`=`HISTORY_SERVER_CLUSTER`] [`--kms-key`=`KMS_KEY`] [`--labels`=[`KEY`=`VALUE`,…]] [`--metastore-service`=`METASTORE_SERVICE`] [`--properties`=[`PROPERTY`=`VALUE`,…]] [`--region`=`REGION`] [`--request-id`=`REQUEST_ID`] [`--resource-manager-tag`=`KEY`=`VALUE`] [`--service-account`=`SERVICE_ACCOUNT`] [`--staging-bucket`=`STAGING_BUCKET`] [`--tags`=[`TAGS`,…]] [`--ttl`=`TTL`] [`--user-workload-authentication-type`=`USER_WORKLOAD_AUTHENTICATION_TYPE`] [`--version`=`VERSION`] [`--network`=`NETWORK` | `--subnet`=`SUBNET`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Submit a Dataproc batch job. 
EXAMPLES
     To submit a PySpark job, run: 
    
    
    [gcloud dataproc batches submit pyspark](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark) my-pyspark.py --region='us-central1' --deps-bucket=gs://my-bucket --py-files='path/to/my/python/scripts'

To submit a Spark job, run: 
    
    
    [gcloud dataproc batches submit spark](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark) --region='us-central1' --deps-bucket=gs://my-bucket --jar='my_jar.jar' -- ARG1 ARG2

To submit a Spark-R job, run: 
    
    
    [gcloud dataproc batches submit spark-r](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-r) my-main-r.r --region='us-central1' --deps-bucket=gs://my-bucket -- ARG1 ARG2

To submit a Spark-Sql job, run: 
    
    
    [gcloud dataproc batches submit spark-sql](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql) 'my-sql-script.sql' --region='us-central1' --deps-bucket=gs://my-bucket --vars='variable=value'

FLAGS
    

`--async`
     Return immediately without waiting for the operation in progress to complete. 
`--batch`=`BATCH`
     The ID of the batch job to submit. The ID must contain only lowercase letters (a-z), numbers (0-9) and hyphens (-). The length of the name must be between 4 and 63 characters. If this argument is not provided, a random generated UUID will be used. 
`--container-image`=`CONTAINER_IMAGE`
     Optional custom container image to use for the batch/session runtime environment. If not specified, a default container image will be used. The value should follow the container image naming format: {registry}/{repository}/{name}:{tag}, for example, gcr.io/my-project/my-image:1.2.3 
`--history-server-cluster`=`HISTORY_SERVER_CLUSTER`
     Spark History Server configuration for the batch/session job. Resource name of an existing Dataproc cluster to act as a Spark History Server for the workload in the format: "projects/{project_id}/regions/{region}/clusters/{cluster_name}". 
`--kms-key`=`KMS_KEY`
     Cloud KMS key to use for encryption. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--metastore-service`=`METASTORE_SERVICE`
     Name of a Dataproc Metastore service to be used as an external metastore in the format: "projects/{project-id}/locations/{region}/services/{service-name}". 
`--properties`=[`PROPERTY`=`VALUE`,…]
     Specifies configuration properties for the workload. See [Dataproc Serverless for Spark documentation](https://cloud.google.com/dataproc-serverless/docs/concepts/properties) for the list of supported properties. 
Region resource - Dataproc region to use. Each Dataproc region constitutes an independent resource namespace constrained to deploying instances into Compute Engine zones inside the region. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--region` on the command line with a fully specified name; 
  * set the property `dataproc/region` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--region`=`REGION`
     ID of the region or fully qualified identifier for the region. 

To set the `region` attribute: 

  * provide the argument `--region` on the command line; 
  * set the property `dataproc/region`. 


`--request-id`=`REQUEST_ID`
     A unique ID that identifies the request. If the service receives two batch create requests with the same request_id, the second request is ignored and the operation that corresponds to the first batch created and stored in the backend is returned. Recommendation: Always set this value to a UUID. The value must contain only letters (a-z, A-Z), numbers (0-9), underscores (`), and hyphens (-). The maximum length is 40 characters. `
`--resource-manager-tag`=KEY`=`VALUE``
     Resource Manager Tags to be associated with the compute resources created for the workload. Only one key-value pair can be specified per flag. Repeat the flag to specify multiple tags. 
`--service-account`=SERVICE_ACCOUNT``
     The IAM service account to be used for a batch/session job. 
`--staging-bucket`=STAGING_BUCKET``
     The Cloud Storage bucket to use to store job dependencies, config files, and job driver console output. If not specified, the default [staging bucket] (https://cloud.google.com/dataproc-serverless/docs/concepts/buckets) is used. 
`--tags`=[TAGS`,…]`
     Network tags for traffic control. 
`--ttl`=TTL``
     The duration after the workload will be unconditionally terminated, for example, '20m' or '1h'. Run [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--user-workload-authentication-type`=USER_WORKLOAD_AUTHENTICATION_TYPE``
     Whether to use END_USER_CREDENTIALS or SERVICE_ACCOUNT to run the workload. 
`--version`=VERSION``
     Optional runtime version. If not specified, a default version will be used. 
At most one of these can be specified: 

`--network`=NETWORK``
     Network URI to connect network to. 
`--subnet`=SUBNET``
     Subnetwork URI to connect network to. Subnet must have Private Google Access enabled. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[pyspark](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark)`
     Submit a PySpark batch job. 
`[pyspark-notebook](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark-notebook)`
     Submit a PySpark notebook batch job. 
`[spark](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark)`
     Submit a Spark batch job. 
`[spark-r](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-r)`
     Submit a Spark R batch job. 
`[spark-sql](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql)`
     Submit a Spark SQL batch job. 
NOTES
     This variant is also available: 
    
    
    [gcloud beta dataproc batches submit](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/batches/submit)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 

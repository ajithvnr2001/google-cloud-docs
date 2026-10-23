---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/restartable-jobs/
title: Restartable jobs \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:04.281046+00:00
---

# Restartable jobs  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/restartable-jobs/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Restartable jobs Stay organized with collections  Save and categorize content based on your preferences. 

By default, Managed Service for Apache Spark jobs won't automatically restart on failure. By using optional settings, you can set jobs to restart on failure. When you set a job to restart, you specify the maximum number of retries per hour (max value is 10 retries per hour) or the maximum number of total retries (max value is 240 total retries) or both.

Restarting jobs mitigates common types of job failure, including out-of-memory issues and unexpected Compute Engine virtual machine reboots. Restartable jobs are particularly useful for long-running and streaming jobs. For example, you can restart Spark streaming jobs running on Managed Service for Apache Spark clusters to ensure that the streaming jobs are resilient.

## Restartable job semantics

The following semantics apply to reporting the success or failure of jobs:

  * A job is reported **successful** if the driver terminates with code `0`.
  * A job is reported **failed** if: 
    * The driver terminates with a non-zero code more than 4 times in 10 minutes.
    * The driver terminates with a non-zero code, and has exceeded the `max_failures_per_hour` or the`max_failures_total` setting.
  * A job will be **restarted** if the driver exits with a non-zero code, is not thrashing, and is within the `max_failures_per_hour` and `max_failures_total` settings.



## Job design considerations

  * Design your jobs to gracefully handle restarting. For example, if your job writes to a directory, your job accommodate the possibility that the directory will exist when the job is restarted.
  * Apache Spark streaming jobs that checkpoint can be restarted after failure, but they won't report Yarn status.



## Create and use restartable jobs

You can specify the maximum number of times a job can be restarted per hour and the maximum number of total retries when submitting the job through the gcloud CLI [gcloud](https://docs.cloud.google.com/sdk/gcloud/reference) command-line tool, the [Managed Service for Apache Spark REST API](https://docs.cloud.google.com/managed-spark/docs/reference/rest), or the [Google Cloud console](https://console.cloud.google.com/).

**Example:** If you want to allow your job to retry up to 10 times, but no more than 5 times in one hour, set `max-failures-total` to 10 and `max-failures-per-hour` to 5.

### gcloud

Specify the maximum number of times a job can be restarted per hour (the max value is 10 retries per hour) or the maximum number of total retries (max value is 240 total retries) or both, using the `--max-failures-per-hour` and `--max-failures-total` flags, respectively. 
    
    
    gcloud dataproc jobs submit job type \
        --region=region \
        --max-failures-per-hour=number \
        --max-failures-total=number \
        ... other args
    

### REST API

Specify the maximum number of times a job can be restarted per hour (max value is 10 retries per hour) or the maximum number of total retries (max value is 240 total retries) or both, by setting the [Job.JobScheduling](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/JobScheduling) `maxFailuresPerHour` and/or `maxFailuresTotal`fields, respectively. 

**Example**
    
    
    POST /v1/projects/project-id/regions/us-central1/jobs:submit/
    {
    "projectId": "project-id",
    "job": {
    "placement": {
      "clusterName": "example-cluster"
    },
    "reference": {
      "jobId": "cea7ae0b...."
    },
    "sparkJob": {
      "args": [
        "1000"
      ],
      "mainClass": "org.apache.spark.examples.SparkPi",
      "jarFileUris": [
        "file:///usr/lib/spark/examples/jars/spark-examples.jar"
      ]
    },
    **"scheduling":** {
      **"maxFailuresPerHour":** 5
      **"maxFailuresTotal":** 10
    }
    }
    }
    

To examine the JSON body of a Managed Service for Apache Spark API request or response, construct the request or select the resource to list from the appropriate Managed Service for Apache Spark page of the Google Cloud console, then click **Equivalent REST** at the bottom of the page.

### Console

You can submit restartable jobs by specifying the **max restarts per hour** on the Managed Service for Apache Spark [Submit a job](https://console.cloud.google.com/dataproc/jobs/jobsSubmit) page (the maximum value is 10 times per hour). The max restarts total setting isn't available on the Google Cloud console.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

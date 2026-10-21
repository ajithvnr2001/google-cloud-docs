---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-rotation/
title: Cluster rotation \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:41.436988+00:00
---

# Cluster rotation  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-rotation/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Cluster rotation Stay organized with collections  Save and categorize content based on your preferences. 

.

Organization security policies, regulatory compliance rules, and other considerations can prompt you to "rotate" your Managed Service for Apache Spark clusters at regular intervals by deleting, then recreating clusters on a schedule. As part of cluster rotation, new clusters can be provisioned with the latest Managed Service for Apache Spark image versions while retaining the configuration settings of the replaced clusters.

This page shows you how to set up clusters that you plan to rotate ("rotated clusters"), submit jobs to them, and then rotate the clusters as needed.

[Custom image](https://docs.cloud.google.com/managed-spark/docs/guides/images) cluster rotation: You can apply previous or new customizations to a previous or new Managed Service for Apache Spark base image when recreating the custom image cluster.

## Set up rotated clusters

To set up rotated clusters, create unique, timestamp-suffixed cluster names to distinguish previous from new clusters, and then attach labels to clusters that indicate if a cluster is part of a rotated cluster pool and actively receiving new job submissions. This example uses `cluster-pool` and `cluster-state=active` labels for these purposes, but you can use your own label names.

  1. Set environment variables: 
         
         PROJECT=project ID \
           REGION=[region](https://docs.cloud.google.com/compute/docs/regions-zones#available) \
           CLUSTER_POOL=cluster-pool-name \
           CLUSTER_NAME=$CLUSTER_POOL-$(date '+%Y%m%d%H%M') \
           BUCKET=Cloud Storage bucket-name
         

Notes:

     * cluster-pool-name: The name of the cluster pool associated with one or more clusters. This name is used in the cluster name and with the `cluster-pool` label attached to the cluster to identify the cluster as part of the pool.
  2. Create the cluster. You can add arguments and use different labels.
         
         gcloud dataproc clusters create ${CLUSTER_NAME} \
           --project=${PROJECT_ID} \
           --region=${REGION} \
           --bucket=${BUCKET} \
           --labels="cluster-pool=${CLUSTER_POOL},cluster-state=active"
         




## Submit jobs to clusters

The following Google Cloud CLI and [Apache Airflow directed acyclic graph (DAG)](https://docs.cloud.google.com/composer/docs/how-to/using/writing-dags) examples submit an Apache Pig job to a cluster. Cluster labels are used to submit the job to an active cluster within a cluster pool.

### gcloud

Submit an Apache Pig job located in Cloud Storage. Pick the cluster using labels.
    
    
    gcloud dataproc jobs submit pig \
        --region=${REGION} \
        --file=gs://${BUCKET}/scripts/script.pig \
        --cluster-labels="cluster-pool=${CLUSTER_POOL},cluster-state=active"
      

### Airflow

Submit an Apache Pig job located in Cloud Storage using Airflow. Pick the cluster using labels.
    
    
    from airflow import DAG
    from airflow.providers.google.cloud.operators.dataproc import DataprocSubmitJobOperator
    from datetime import datetime
    
    # Declare variables
    project_id=  # e.g: my-project
    region="us-central1"
    dag_id='pig_wordcount'
    cluster_labels={"cluster-pool":${CLUSTER_POOL},
                    "cluster-state":"active"}
    wordcount_script="gs://bucket-name/scripts/wordcount.pig"
    
    # Define DAG
    
    dag = DAG(
        dag_id,
        schedule_interval=None,
        start_date=datetime(2023, 8, 16),
        catchup=False
    )
    
    PIG_JOB = {
        "reference": {"project_id": project_id},
        "placement": {"cluster_labels": cluster_labels},
        "pig_job": {"query_file_uri": wordcount_script},
    }
    
    wordcount_task = DataprocSubmitJobOperator(
        task_id='wordcount',
        region=region,
        project_id=project_id,
        job=PIG_JOB,
        dag=dag
    )
    

## Rotate clusters

  1. Update the cluster labels attached to the clusters you are rotating out. This examples uses the `cluster-state=pendingfordeletion` label to signify that the cluster is not receiving new job submissions and is being rotated out, but you can use your own label for this purpose. 
         
         gcloud dataproc clusters update ${CLUSTER_NAME} \
             --region=${REGION} \
             --update-labels="cluster-state=pendingfordeletion"
         

After the cluster label is updated, the cluster does not receive new jobs since jobs are submitted to clusters within a cluster pool with `active` labels only (see Submit jobs to clusters).

  2. Delete clusters you are rotating out after they finish running jobs.

**Note:** You can automate this step with a monitoring script that fetches clusters with the `cluster-state=pendingfordeletion` label (or other label you added with the previous command), checks that no jobs are running on the cluster, and then deletes the cluster.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 

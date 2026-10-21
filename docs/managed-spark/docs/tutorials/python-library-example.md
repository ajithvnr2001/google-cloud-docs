---
url: https://docs.cloud.google.com/managed-spark/docs/tutorials/python-library-example/
title: Use the Cloud Client Libraries for Python \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:52.657632+00:00
---

# Use the Cloud Client Libraries for Python  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/tutorials/python-library-example/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use the Cloud Client Libraries for Python Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial includes a [Cloud Shell walkthrough](https://docs.cloud.google.com/shell/docs/tutorials) that uses the [Google Cloud client libraries for Python](https://docs.cloud.google.com/python/docs/reference/dataproc/latest) to programmatically call [Managed Service for Apache Spark gRPC APIs](https://docs.cloud.google.com/managed-spark/docs/reference/rpc) to create a cluster and submit a job to the cluster.

The following sections explain the operation of the walkthrough code contained in the GitHub [GoogleCloudPlatform/python-dataproc](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-dataproc/samples/generated_samples) repository.

The walkthrough tutorial code makes separate API requests to create a cluster, submit a job to the cluster, then delete the cluster. You can use an [inline workflow](https://docs.cloud.google.com/managed-spark/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.WorkflowTemplateService.InstantiateInlineWorkflowTemplate) to accomplish these tasks with one API request (see [instantiate_inline_workflow_template.py](https://github.com/googleapis/google-cloud-python/blob/main/packages/google-cloud-dataproc/samples/generated_samples/dataproc_v1_generated_workflow_template_service_instantiate_inline_workflow_template_async.py) for an example).

## Run the Cloud Shell walkthrough

Click **Open in Cloud Shell** to run the walkthrough.

[ Open in Cloud Shell ](https://ssh.cloud.google.com/cloudshell/open?cloudshell_git_repo=https://github.com/googleapis/python-dataproc&cloudshell_working_dir=samples/snippets&tutorial=python-api-walkthrough.md&cloudshell_open_in_editor=submit_job_to_cluster.py)

## Understand the code

This section explains how the tutorial code uses the Cloud Client Libraries for Python to authenticate with Google Cloud, create a cluster, submit a Spark job, and clean up by deleting the cluster.

### Application Default Credentials

The Cloud Shell walkthrough in this tutorial provides authentication by using your Google Cloud project credentials. When you run code locally, the recommended practice is to use [service account credentials](https://docs.cloud.google.com/docs/authentication/production#obtaining_and_providing_service_account_credentials_manually) to authenticate your code.

### Create a Managed Service for Apache Spark cluster

The following values are set to create the cluster:

  * The project in which the cluster will be created
  * The region where the cluster will be created
  * The name of the cluster
  * The cluster config, which specifies one master and two primary workers



Default config settings are used for the remaining cluster settings. You can override default cluster config settings. For example, you can add secondary VMs (default = 0) or specify a non-default VPC network for the cluster. For more information, see [CreateCluster](https://docs.cloud.google.com/managed-spark/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.ClusterController.CreateCluster).
    
    
    def quickstart(project_id, region, cluster_name, gcs_bucket, pyspark_file):
        # Create the cluster client.
        cluster_client = dataproc_v1.ClusterControllerClient(
            client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
        )
    
        # Create the cluster config.
        cluster = {
            "project_id": project_id,
            "cluster_name": cluster_name,
            "config": {
                "master_config": {"num_instances": 1, "machine_type_uri": "n1-standard-2"},
                "worker_config": {"num_instances": 2, "machine_type_uri": "n1-standard-2"},
            },
        }
    
        # Create the cluster.
        operation = cluster_client.create_cluster(
            request={"project_id": project_id, "region": region, "cluster": cluster}
        )
        result = operation.result()
    
        print(f"Cluster created successfully: {result.cluster_name}")
    

### Submit a job

The following values are set to submit the job:

  * The project in which the cluster will be created
  * The region where the cluster will be created
  * The job config, which specifies the cluster name and the Cloud Storage filepath (URI) of the PySpark job



See [SubmitJob](https://docs.cloud.google.com/managed-spark/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.JobController.SubmitJob) for more information.
    
    
    # Create the job client.
    job_client = dataproc_v1.JobControllerClient(
        client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
    )
    
    # Create the job config.
    job = {
        "placement": {"cluster_name": cluster_name},
        "pyspark_job": {"main_python_file_uri": f"gs://{gcs_bucket}/{spark_filename}"},
    }
    
    operation = job_client.submit_job_as_operation(
        request={"project_id": project_id, "region": region, "job": job}
    )
    response = operation.result()
    
    # Dataproc job output is saved to the Cloud Storage bucket
    # allocated to the job. Use regex to obtain the bucket and blob info.
    matches = re.match("gs://(.*?)/(.*)", response.driver_output_resource_uri)
    
    output = (
        storage.Client()
        .get_bucket(matches.group(1))
        .blob(f"{matches.group(2)}.000000000")
        .download_as_bytes()
        .decode("utf-8")
    )
    
    print(f"Job finished successfully: {output}\r\n")

### Delete the cluster

The following values are set to delete the cluster:

  * The project in which the cluster will be created
  * The region where the cluster will be created
  * The name of the cluster



For more information, see the [DeleteCluster](https://docs.cloud.google.com/managed-spark/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.JobController.DeleteCluster).
    
    
    # Delete the cluster once the job has terminated.
    operation = cluster_client.delete_cluster(
        request={
            "project_id": project_id,
            "region": region,
            "cluster_name": cluster_name,
        }
    )
    operation.result()
    
    print(f"Cluster {cluster_name} successfully deleted.")
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 

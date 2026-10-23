---
url: https://docs.cloud.google.com/managed-spark/docs/samples/dataproc-update-cluster/
title: Update a cluster \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:00.933601+00:00
---

# Update a cluster  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/samples/dataproc-update-cluster/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Samples ](https://docs.cloud.google.com/managed-spark/docs/samples)



#  Update a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This sample walks a user through updating a Cloud Dataproc cluster using the Python client library.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataproc/latest). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import dataproc_v1 as dataproc
    
    
    def update_cluster(project_id, region, cluster_name, new_num_instances):
        """This sample walks a user through updating a Cloud Dataproc cluster
        using the Python client library.
    
        Args:
            project_id (str): Project to use for creating resources.
            region (str): Region where the resources should live.
            cluster_name (str): Name to use for creating a cluster.
        """
    
        # Create a client with the endpoint set to the desired cluster region.
        client = dataproc.ClusterControllerClient(
            client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
        )
    
        # Get cluster you wish to update.
        cluster = client.get_cluster(
            project_id=project_id, region=region, cluster_name=cluster_name
        )
    
        # Update number of clusters
        mask = {"paths": {"config.worker_config.num_instances": str(new_num_instances)}}
    
        # Update cluster config
        cluster.config.worker_config.num_instances = new_num_instances
    
        # Update cluster
        operation = client.update_cluster(
            project_id=project_id,
            region=region,
            cluster=cluster,
            cluster_name=cluster_name,
            update_mask=mask,
        )
    
        # Output a success message.
        updated_cluster = operation.result()
        print(f"Cluster was updated successfully: {updated_cluster.cluster_name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataproc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

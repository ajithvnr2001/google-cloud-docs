---
url: https://docs.cloud.google.com/dataproc/docs/concepts/regional-endpoints/
title: Cluster region \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:39:10.823547+00:00
---

# Cluster region  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc/docs/concepts/regional-endpoints/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Cluster region Stay organized with collections  Save and categorize content based on your preferences. 

You specify a Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available), such as "us-east1" or "europe-west1", when you create a Managed Service for Apache Spark cluster. Managed Service for Apache Spark will isolate cluster resources, such as VM instances and Cloud Storage and metadata storage, within a zone within the specified region.

You can optionally specify a zone within the specified cluster region, such as "us-east1-a" or "europe-west1-b", when you create a cluster. If you don't specify the zone, [Managed Service for Apache Spark Auto Zone Placement](https://docs.cloud.google.com/managed-spark/docs/concepts/auto-zone) will choose a zone within your specified cluster region to locate clusters resources.

The regional namespace corresponds to the `/regions/REGION` segment of Managed Service for Apache Spark resource URIs (see, for example, the cluster [`networkUri`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#GceClusterConfig.FIELDS.network_uri)).

## Region names

Region names follow a standard naming convention based on [Compute Engine regions](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available). For example, the name for the Central US region is `us-central1`, and the name of the Western Europe region is `europe-west1`. Run the `gcloud compute regions list` command to see a listing of available regions.

**Note:** When new regions are added to Compute Engine, they become available for use with Managed Service for Apache Spark.

### Location and regional endpoints

Google Cloud APIs can provide support for **locational** and **regional** endpoints:

  * **Locational endpoints** ensure that in-transit data remains in the specified location when accessed through private connectivity.

Format: `{location}-{service}.googleapis.com`

Example: `us-central-1-dataproc.googleapis.com`

  * **Regional endpoints** ensure that in-transit data remains in the specified location when accessed through either private connectivity or the public internet.

Format: `{service}.{location}.rep.googleapis.com`

Example: `dataproc.us-central1.rep.googleapis.com`




The default Managed Service for Apache Spark endpoint is **location endpoint**. See the [Managed Service for Apache Spark release notes](https://docs.cloud.google.com/managed-spark/docs/release-notes) for announcements on Managed Service for Apache Spark support of regional endpoints.

## Create a cluster

### Console

Specify a Compute Engine region in the **Region** field in the **Define your cluster** section on the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page in the Google Cloud console.

### gcloud CLI

When you create a cluster, specify a region using the required `--region` flag.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        other args ...
    

### REST API

Use the `REGION` URL parameter in a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request to specify the cluster region.

### gRPC

Set the client transport address to the locational endpoint using the following pattern:

`REGION-dataproc.googleapis.com`

**Python ([google-cloud-python](https://github.com/googleapis/python-dataproc)) example:**
    
    
    from google.cloud import dataproc_v1
    from google.cloud.dataproc_v1.gapic.transports import cluster_controller_grpc_transport
    
    transport = cluster_controller_grpc_transport.ClusterControllerGrpcTransport(
        address='**us-central1-dataproc.googleapis.com** :443')
    client = dataproc_v1.ClusterControllerClient(transport)
    
    project_id = 'my-project'
    region = 'us-central1'
    cluster = {...}

**Java([google-cloud-java](https://github.com/googleapis/google-cloud-java/tree/main/java-dataproc)) example:**
    
    
    ClusterControllerSettings settings =
         ClusterControllerSettings.newBuilder()
            .setEndpoint("**us-central1-dataproc.googleapis.com** :443")
            .build();
     try (ClusterControllerClient clusterControllerClient = ClusterControllerClient.create(settings)) {
       String projectId = "my-project";
       String region = "us-central1";
       Cluster cluster = Cluster.newBuilder().build();
       Cluster response =
           clusterControllerClient.createClusterAsync(projectId, region, cluster).get();
     }

## What's next

  * [Geography and Regions](https://docs.cloud.google.com/docs/geography-and-regions)
  * [Compute Engine Engine→Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones)
  * [Compute Engine→Global, Regional, and Zonal Resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources)
  * [Managed Service for Apache Spark Auto Zone Placement](https://docs.cloud.google.com/managed-spark/docs/concepts/auto-zone)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

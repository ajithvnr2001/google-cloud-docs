---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-availability/
title: High Availability Mode \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:39.984839+00:00
---

# High Availability Mode  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-availability/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  High Availability Mode Stay organized with collections  Save and categorize content based on your preferences. 

When creating a Managed Service for Apache Spark cluster, you can put the cluster into Hadoop High Availability (HA) mode by specifying the number of master instances in the cluster. The number of masters can only be specified at cluster creation time.

Currently, Managed Service for Apache Spark supports two master configurations:

  * 1 master (default, non HA)
  * 3 masters (Hadoop HA)



## Comparison of default and Hadoop High Availability mode

Due to the complexity and higher cost of HA mode, use the default mode unless your use case requires HA mode. 

  * **Compute Engine failure:** In the rare case of an unexpected Compute Engine failure, Managed Service for Apache Spark instances will experience a machine reboot. The default single-master configuration for Managed Service for Apache Spark is designed to recover and continue processing new work in such cases, but in-flight jobs will necessarily fail and need to be retried, and HDFS will be inaccessible until the single NameNode fully recovers on reboot. In **HA mode** , [HDFS High Availability](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HDFSHighAvailabilityWithQJM.html) and [YARN High Availability](https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/ResourceManagerHA.html) are configured to allow uninterrupted YARN and HDFS operations despite any single-node failures/reboots.

  * **Job driver termination:** The driver/main program of any jobs you run still represents a potential single point of failure if the correctness of your job depends on the driver program running successfully. Jobs submitted through the Dataproc Jobs API are not considered "high availability," and will still be terminated on failure of the master node that runs the corresponding job driver programs. For individual jobs to be resilient against single-node failures using a HA Cloud Dataproc cluster, the job must either 1) run without a synchronous driver program or 2) it must run the driver program itself inside a YARN container and be written to handle driver-program restarts. See [Launching Spark on YARN](http://spark.apache.org/docs/latest/running-on-yarn.html#launching-spark-on-yarn) for an example of how restartable driver programs can run inside YARN containers for fault tolerance.

  * **Zonal failure:** As is the case with all Managed Service for Apache Spark clusters, all nodes in a High Availability cluster reside in the same zone. If there is a failure that impacts all nodes in a zone, the failure will not be mitigated.




### Instance Names

The default master is named `cluster-name-m`; HA masters are named `cluster-name-m-0`, `cluster-name-m-1`, `cluster-name-m-2`.

### Apache ZooKeeper

In an HA Managed Service for Apache Spark cluster, the [Zookeeper component](https://docs.cloud.google.com/managed-spark/docs/concepts/components/zookeeper) is automatically installed on cluster master nodes. All masters participate in a ZooKeeper cluster, which enables automatic failover for other Hadoop services.

### HDFS

In a standard Managed Service for Apache Spark cluster:

  * `cluster-name-m` runs: 
    * NameNode
    * Secondary NameNode



In a High Availability Managed Service for Apache Spark cluster:

  * `cluster-name-m-0` and `cluster-name-m-1` run: 
    * NameNode
    * ZKFailoverController
  * All masters run JournalNode
  * There is no Secondary NameNode



Please see the [HDFS High Availability](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HDFSHighAvailabilityWithQJM.html) documentation for additional details on components.

### YARN

In a standard Managed Service for Apache Spark cluster, `cluster-name-m` runs ResourceManager.

In a High Availability Managed Service for Apache Spark cluster, all masters run ResourceManager.

See the [YARN High Availability](https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/ResourceManagerHA.html) documentation for additional details on components.

## Create a High Availability cluster

### Console

  * Open the Managed Service for Apache Spark [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page. 
  * In the **Define your cluster shape** section, select **High availability**.
  * By default, driver node settings are the same as primary worker settings. Under **Additional configuration** , you can edit **Driver node** to clear the checkbox, **Default driver node to the same as primary worker** , then specify driver node settings.



### gcloud command

**gcloud CLI setup:** You must [setup and configure](https://docs.cloud.google.com/sdk/docs/quickstarts) the gcloud CLI to use the Google Cloud CLI. To create an HA cluster with [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create), run the following command: 
    
    
    gcloud dataproc clusters create cluster-name \
        --region=region \
        --num-masters=3 \
        ... other args
    

### REST API

To create an HA cluster, use the [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) API, setting [masterConfig.numInstances](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#InstanceGroupConfig) to `3`. An easy way to construct the JSON body of an HA cluster create request is to create the request from [**Create a cluster**](https://console.cloud.google.com/dataproc/clusters/create) page of the Google Cloud console. Select High Availability (3 masters, N workers) in the Cluster type field of the Define your cluster shape section, then click the Equivalent REST link at the bottom of the page. Here's a snippet of a sample JSON output produced by the console for an HA cluster create request: 
    
    
    ...
    masterConfig": {
      **"numInstances": 3** ,
      "machineTypeUri": "n1-standard-4",
      "diskConfig": {
        "bootDiskSizeGb": 500,
        "numLocalSsds": 0
      }
    }
    ...
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

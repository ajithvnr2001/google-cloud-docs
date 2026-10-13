---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/dataproc/
title: Managed Service for Apache Spark provisioner properties \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:23.158310+00:00
---

# Managed Service for Apache Spark provisioner properties  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/dataproc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Managed Service for Apache Spark provisioner properties Stay organized with collections  Save and categorize content based on your preferences. 

The Managed Service for Apache Spark provisioner in Cloud Data Fusion calls the Dataproc API to create and delete clusters in your Google Cloud projects. You can configure the clusters in the provisioner's settings.

For more information about compatibility between Cloud Data Fusion versions and Managed Service for Apache Spark versions, see [Version compatibility](https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters#version-compatibility).

## Properties

Property | Description  
---|---  
**Project ID** | The Google Cloud project where the Managed Service for Apache Spark cluster gets created. The project must have the Dataproc API enabled.  
**Creator service account key** | The service account key provided to the provisioner must have permission to access the Managed Service for Apache Spark and Compute Engine APIs. Because your account key is sensitive, we recommend that you provide the account key using [Secure Storage](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477790661/Security+HTTP+RESTful+API). After you create the secure key, you can add it to a namespace or a system compute profile. For a namespace compute profile, click the shield shield and select the secure key. For a system compute profile, enter the name of the key in the **Secure Account Key** field.  
**Region** | A geographical location where you can host your resources, such as the compute nodes for the Managed Service for Apache Spark cluster.  
**Zone** | An isolated deployment area within a region.  
**Network** | The VPC network in your Google Cloud project that will be used when creating a Managed Service for Apache Spark cluster.  
**Network host project ID** | If the network resides in another Google Cloud project, enter the ID of that project. For a Shared VPC, enter the host project ID where the network resides.  
**Subnet** | The subnet to use when creating clusters. It must be within the given network and in the region that the zone is in. If left blank, a subnet is selected based on the network and zone.  
**Runner service account** | The service account name of the Managed Service for Apache Spark virtual machines (VM) that are used for running programs. If left blank, the default Compute Engine service account is used.  
**Number of masters** | The number of master nodes in the cluster. These nodes contain the YARN Resource Manager, HDFS NameNode, and all drivers. Must be set to **1** or **3**. Default is **1**.  
**Master machine type** | The type of master machine to use. Select one of the following machine types:

  * n1
  * n2
  * n2d
  * e2

In Cloud Data Fusion version 6.7.2 and later, the default is **e2**. In version 6.7.1, the default is **n2.** In version 6.7.0 and earlier, the default is **n1**.  
**Master cores** | Number of virtual cores allocated to a master node. Default is **2**.  
**Master memory (GB)** | The amount of memory, in gigabytes, allocated to a master node. Default is **8 GB**.  
**Master disk size (GB)** | Disk size, in gigabytes, allocated to a master node. Default is **1000 GB**.  
**Master disk type** | Type of boot disk for a master node:

  * Standard Persistent Disk
  * SSD Persistent Disk

Default is **Standard Persistent Disk.**  
**Worker machine type** | The type of worker machine to use. Select one of the following machine types:

  * n1
  * n2
  * n2d
  * e2

In Cloud Data Fusion version 6.7.2 and later, the default is **e2**. In version 6.7.1, the default is **n2.** In version 6.7.0 and earlier, the default is **n1**.  
**Worker cores** | Number of virtual cores allocated to a worker node. Default is **2**.  
**Worker memory (GB)** | The amount of memory, in gigabytes, allocated to a worker node. Default is **8 GB**.  
**Worker disk size (GB)** | Disk size, in gigabytes, allocated to a worker node. Default is **1000 GB**.  
**Worker disk type** | Type of boot disk for a worker node:

  * Standard Persistent Disk
  * SSD Persistent Disk

Default is **Standard Persistent Disk.**  
**Use predefined Autoscaling** | Enables using [predefined Managed Service for Apache Spark autoscaling](https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters#enable-predefined-autoscaling).  
**Number of primary workers** | Worker nodes contain a YARN NodeManager and an HDFS DataNode. Default is **2**.  
**Number of secondary workers** | Secondary worker nodes contain a YARN NodeManager, but not an HDFS DataNode. This is normally set to zero, unless an autoscaling policy requires it to be higher.  
**Autoscaling policy** | Path for the autoscaling policy ID or the resource URI. For information about configuring and using Managed Service for Apache Spark autoscaling to automatically and dynamically resize clusters to meet workload demands, see [When to use autoscaling](https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters#autoscaling) and [Autoscale Managed Service for Apache Spark clusters](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/autoscaling).  
**Metadata** | Additional metadata for instances running in your cluster. You can typically use it for tracking billing and chargebacks. For more information, see [Cluster metadata](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/metadata).  
**Network tags** | Assign Network tags to apply firewall rules to the specific nodes of a cluster. Network tags must start with a lowercase letter and can contain lowercase letters, numbers, and hyphens. Tags must end with a lowercase letter or number.  
**Enable Secure Boot** | Enables [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) on the Managed Service for Apache Spark VMs. Default is **False**.  
**Enable vTPM** | Enables virtual Trusted Platform Module ([vTPM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm)) on the Managed Service for Apache Spark VMs. Default is **False**.  
**Enable Integrity Monitoring** | Enables virtual [Integrity Monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring) on the Managed Service for Apache Spark VMs. Default is **False**.  
**Image version** | The Managed Service for Apache Spark image version. If left blank, one is automatically selected. If the **Custom image URI** property is left blank, this property is ignored.  
**Custom image URI** | The Managed Service for Apache Spark image URI. If left blank, it's inferred from the **Image version** property.  
**Staging bucket** | Cloud Storage bucket used to stage job dependencies and config files for running pipelines in Managed Service for Apache Spark.  
**Temp bucket** | Cloud Storage bucket used to store ephemeral cluster and jobs data, such as Spark history files in Managed Service for Apache Spark. This property was introduced in Cloud Data Fusion version 6.9.2.  
**Encryption key name** | The customer managed encryption key (CMEK) that's used by Managed Service for Apache Spark.  
**OAuth scopes** | The OAuth 2.0 scopes that you might need to request to access Google APIs, depending on the level of access you need. [Google Cloud Platform Scope](https://www.googleapis.com/auth/cloud-platform) is always included. This property was introduced in Cloud Data Fusion version 6.9.2.  
**Initialization actions** | A list of scripts to be executed during initialization of the cluster. Initialization actions should be placed on Cloud Storage.  
**Cluster properties** | Cluster properties overriding the default configuration properties of the Hadoop services. For more information on applicable key-value pairs, see [Cluster properties](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/cluster-properties).  
**Common labels** | Labels to organize the Managed Service for Apache Spark clusters and jobs being created. You can label each resource and then filter the resources by labels. Information about labels is forwarded to the billing system, so customers can [break down your billing charges](https://docs.cloud.google.com/billing/docs/how-to/bq-examples) by label.  
**Max idle time** | Configure Managed Service for Apache Spark to delete a cluster if it's idle longer than the specified number of minutes. Clusters are normally deleted directly after a run ends, but deletion can fail in rare situations. For more information, see [Troubleshoot deleting clusters](https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters). Default is **30** minutes.  
**Skip cluster delete** | Whether to skip cluster deletion at the end of a run. You must manually delete clusters. This should only be used when debugging a failed run. Default is **False**.  
**Enable Stackdriver Logging Integration** | Enable the Stackdriver logging integration. Default is **True**.  
**Enable Stackdriver Monitoring Integration** | Enable the Stackdriver monitoring integration. Default is **True**.  
**Enable Component Gateway** | Enable the component gateway to access to the cluster's interfaces, such as the YARN ResourceManager and Spark HistoryServer. Default is **False**.  
**Prefer external IP** | When the system is running on Google Cloud in the same network as the cluster, it normally uses the internal IP address when communicating with the cluster. To always use the external IP address, set this value to **True**. Default is **False**.  
**Create poll delay** | The number of seconds to wait after creating a cluster to begin polling to see if the cluster has been created. Default is **60** seconds. Polling settings control how often cluster status is polled when creating and deleting clusters. If you have many pipelines scheduled to run at the same time, you may want to change these settings.  
**Create poll jitter** | Maximum amount of random jitter, in seconds, to add to the delay when creating a cluster. You can use this property to prevent many simultaneous API calls in Google Cloud when you have a lot of pipelines that are scheduled to run at the exact same time. Default is **20** seconds.  
**Delete poll delay** | The number of seconds to wait after deleting a cluster to begin polling to see if the cluster has been deleted. Default is **30** seconds.  
**Poll interval** | The number of seconds to wait between polls for cluster status. Default is **2**.  
  
## Managed Service for Apache Spark profile web interface properties mapped to JSON properties

Managed Service for Apache Spark profile UI property name | Managed Service for Apache Spark profile JSON property name  
---|---  
**Profile label** | `name`  
**Profile name** | `label`  
**Description** | `description`  
**Project ID** | `projectId`  
**Creator service account key** | `accountKey`  
**Region** | `region`  
**Zone** | `zone`  
**Network** | `network`  
**Network host project ID** | `networkHostProjectId`  
**Subnet** | `subnet`  
**Runner service account** | `serviceAccount`  
**Number of masters** | `masterNumNodes`  
**Master machine type** | `masterMachineType`  
**Master cores** | `masterCPUs`  
**Master memory (GB)** | `masterMemoryMB`  
**Master disk size (GB)** | `masterDiskGB`  
**Master disk type** | `masterDiskType`  
**Number of primary workers** | `workerNumNodes`  
**Number of secondary workers** | `secondaryWorkerNumNodes`  
**Worker machine type** | `workerMachineType`  
**Worker cores** | `workerCPUs`  
**Worker memory (GB)** | `workerMemoryMB`  
**Worker disk size (GB)** | `workerDiskGB`  
**Worker disk type** | `workerDiskType`  
**Metadata** | `clusterMetaData`  
**Network tags** | `networkTags`  
**Enable Secure Boot** | `secureBootEnabled`  
**Enable vTPM** | `vTpmEnabled`  
**Enable Integrity Monitoring** | `integrityMonitoringEnabled`  
**Image version** | `imageVersion`  
**Custom image URI** | `customImageUri`  
**Cloud Storage bucket** | `gcsBucket`  
**Encryption key name** | `encryptionKeyName`  
**Autoscaling policy** | `autoScalingPolicy`  
**Initialization actions** | `initActions`  
**Cluster properties** | `clusterProperties`  
**Labels** | `clusterLabels`  
**Max idle time** | `idleTTL`  
**Skip cluster delete** | `skipDelete`  
**Enable Stackdriver Logging Integration** | `stackdriverLoggingEnabled`  
**Enable Stackdriver Monitoring Integration** | `stackdriverMonitoringEnabled`  
**Enable Component Gateway** | `componentGatewayEnabled`  
**Prefer external IP** | `preferExternalIP`  
**Create poll delay** | `pollCreateDelay`  
**Create poll jitter** | `pollCreateJitter`  
**Delete poll delay** | `pollDeleteDelay`  
**Poll interval** | `pollInterval`  
  
## Best Practices

When you create a static cluster for your pipelines, refer to the [cluster configuration best practices](https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters#best_practices).

## What's next

  * Learn more about [managing compute profiles](https://docs.cloud.google.com/data-fusion/docs/how-to/manage-compute-profiles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

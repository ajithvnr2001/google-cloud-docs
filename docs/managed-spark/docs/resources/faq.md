---
url: https://docs.cloud.google.com/managed-spark/docs/resources/faq/
title: Managed Service for Apache Spark on clusters FAQ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:44.216375+00:00
---

# Managed Service for Apache Spark on clusters FAQ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/resources/faq/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Resources ](https://docs.cloud.google.com/managed-spark/docs/resources)



Send feedback 

#  Managed Service for Apache Spark on clusters FAQ Stay organized with collections  Save and categorize content based on your preferences. 

## General

### What is Managed Service for Apache Spark?

Managed Service for Apache Spark is a fast, easy-to-use, low-cost and fully managed service that lets you run the Apache Spark and Apache Hadoop ecosystem on Google Cloud Platform. Managed Service for Apache Spark provisions big or small clusters rapidly, supports many popular job types, and is integrated with other Google Cloud Platform services, such as Cloud Storage and Cloud Logging, thus helping you reduce TCO.

### How is Managed Service for Apache Spark different from traditional Hadoop clusters?

Managed Service for Apache Spark is a managed Spark/Hadoop service intended to make Spark and Hadoop easy, fast, and powerful. In a traditional Hadoop deployment, even one that is cloud-based, you must install, configure, administer, and orchestrate work on the cluster. By contrast, Managed Service for Apache Spark handles cluster creation, management, monitoring, and job orchestration for you.

### How can I use Managed Service for Apache Spark?

There are a number of ways you can use a Managed Service for Apache Spark cluster depending on your needs and capabilities. You can use the browser-based [Google Cloud console](https://console.cloud.google.com/) to interact with Managed Service for Apache Spark. Or, because Managed Service for Apache Spark is integrated with the [Google Cloud CLI](https://docs.cloud.google.com/sdk), you can use the Google Cloud CLI. For programmatic access to clusters, use the Managed Service for Apache Spark REST API. You can also make SSH connections to master or worker nodes in your cluster.

### How does Managed Service for Apache Spark work?

Managed Service for Apache Spark is a managed framework that runs on the Google Cloud Platform and ties together several popular tools for processing data, including Apache Hadoop, Spark, Hive, and Pig. Managed Service for Apache Spark has a set of control and integration mechanisms that coordinate the lifecycle, management, and coordination of clusters. Managed Service for Apache Spark is integrated with the YARN application manager to make managing and using your clusters easier.

### What type of jobs can I run?

Managed Service for Apache Spark provides out-of-the box and end-to-end support for many of the most popular job types, including Spark, Spark SQL, PySpark, MapReduce, Hive, and Pig jobs.

### What Cluster Manager does Managed Service for Apache Spark use with Spark?

Managed Service for Apache Spark runs [Spark on YARN](https://spark.apache.org/docs/latest/running-on-yarn.html).

### How frequently are the components in Managed Service for Apache Spark updated?

Managed Service for Apache Spark is updated when major releases occur in underlying components (Hadoop, Spark, Hive, Pig). Each major Managed Service for Apache Spark release supports specific versions of each component (see [Supported Managed Service for Apache Spark versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions#supported-dataproc-image-versions)).

### Is Managed Service for Apache Spark integrated with other Google Cloud Platform products?

Yes, Managed Service for Apache Spark has native and automatic integrations with Compute Engine, Cloud Storage, Bigtable, BigQuery, Logging, and Cloud Monitoring. Moreover, Managed Service for Apache Spark is integrated into tools that interact with the Cloud Platform including the [gcloud CLI](https://docs.cloud.google.com/sdk) and the [Google Cloud console](https://console.cloud.google.com/).

### Can I run a persistent cluster?

Once started, Managed Service for Apache Spark clusters continue to run until shut down. You can run a Managed Service for Apache Spark cluster for as long as you need.

## Cluster management

### Can I run more than one cluster at a time?

Yes, you can run more than one Managed Service for Apache Spark cluster per project simultaneously. By default, all projects are subject to [Google Cloud resource quotas](https://docs.cloud.google.com/compute/docs/resource-quotas). You can easily [check your quota usage](https://docs.cloud.google.com/compute/docs/resource-quotas#checking_your_quota) and [request an increase](https://docs.cloud.google.com/compute/quotas#requesting_additional_quota) to your quota. For more information, see [Managed Service for Apache Spark resource quotas](https://docs.cloud.google.com/managed-spark/docs/resources/quotas).

### How can I create or destroy a cluster?

You can create and destroy clusters in several ways. The Managed Service for Apache Spark sections in the [Google Cloud console](https://console.cloud.google.com/) make it easy to manage clusters from your browser. Clusters can also be managed via the command line through the [gcloud CLI](https://docs.cloud.google.com/sdk). For more complex or advanced use cases, the Cloud Managed Service for Apache Spark REST API can be used to programmatically manage clusters.

### Can I apply customized settings when I create a cluster?

Managed Service for Apache Spark supports initialization actions that are executed when a cluster is created. These initialization actions can be scripts or executables that Managed Service for Apache Spark will run when provisioning your cluster to customize settings, install applications, or make other modifications to your cluster.

### How do I size a cluster for my needs?

Cluster sizing decisions are influenced by several factors, including the type of work to be performed, cost constraints, speed requirements, and your resource quota. Since Managed Service for Apache Spark can be deployed on a variety of machine types, you have the flexibility to choose the resources you need, when you need them.

### Can I resize my cluster?

Yes, you can easily resize your cluster, even during job processing. You can resize your cluster through the [Google Cloud console](https://console.cloud.google.com/) or through the command line. Resizing can increase or decrease the number of workers in a cluster. Workers added to a cluster will be the same type and size as existing workers. Resizing clusters is acceptable and supported except in special cases, such as reducing the number of workers to one or reducing HDFS capacity below the amount needed for job completion.

## Job and workflow management

### How can I submit jobs on my cluster?

There are several ways to submit jobs on a Managed Service for Apache Spark cluster. The easiest way is to use the Managed Service for Apache Spark [Submit a job](https://console.cloud.google.com/dataproc/jobs/jobsSubmit) page on the Google Cloud console or the gcloud CLI [gcloud dataproc jobs submit](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit) command. For programmatic job submission, see the [Dataproc API reference](https://docs.cloud.google.com/managed-spark/docs/reference#cloud-dataproc-api).

### Can I run more than one job at a time?

Yes, you can run more than one job at a time on a Managed Service for Apache Spark cluster. Cloud Managed Service for Apache Spark utilizes a resource manager (YARN) and application-specific configurations, such as scaling with Spark, to optimize the use of resources on a cluster. Job performance will scale with cluster size and the number of active jobs.

### Can I cancel jobs on my cluster?

Definitely. Jobs can be canceled via the [Google Cloud console](https://console.cloud.google.com/) web interface or the command line. Managed Service for Apache Spark utilizes YARN application cancellation to stop jobs upon request.

### Can I automate jobs on my cluster?

Jobs can be automated to run on clusters through several mechanisms. You can use the [gcloud CLI](https://docs.cloud.google.com/sdk) Google Cloud CLI or the Managed Service for Apache Spark REST APIs to automate the management and workflow of clusters and jobs.

## Development

### What development languages are supported?

You can use languages supported by the Spark/Hadoop ecosystem, including Java, Scala, Python, and R.

### Does Managed Service for Apache Spark have an API?

Yes, Managed Service for Apache Spark has a set of RESTful APIs that allow you to programmatically interact with clusters and jobs.

### Can I SSH into a cluster?

Yes, you can SSH into every machine (master or worker node) within a cluster. You can SSH from a browser or from the command line.

### Can I access the Spark/Hadoop Web UIs?

Yes, the Hadoop and Spark UIs (Spark, Hadoop, YARN UIs) are accessible within a cluster. Rather than opening ports for the UIs, we recommend using an SSH tunnel, which will securely forward traffic from clusters over the SSH connection.

### Can I install or manage software on my cluster?

Yes, as with a Hadoop cluster or server, you can install and manage software on a Managed Service for Apache Spark cluster.

### What is the default replication factor?

Due to performance considerations as well as the high reliability of storage attached to Managed Service for Apache Spark clusters, the default replication factor is set at 2.

### What operating system (OS) is used for Managed Service for Apache Spark?

Managed Service for Apache Spark is based on Debian and Ubuntu. The latest images are based on Debian 10 Buster and Ubuntu 18.04 LTS.

### Where can I learn about Hadoop streaming?

You can review the [Apache project documentation](http://hadoop.apache.org/docs/r1.2.1/streaming.html).

### How do I install the gcloud dataproc command?

When you install the [gcloud CLI](https://docs.cloud.google.com/sdk), the standard `gcloud` command-line tool is installed, including `gcloud dataproc` commands.

## Data access & availability

### How can I get data in and out of a cluster?

Managed Service for Apache Spark utilizes the Hadoop Distributed File System (HDFS) for storage. Additionally, Managed Service for Apache Spark automatically installs the HDFS-compatible Google Cloud Storage connector, which enables the use of Cloud Storage in parallel with HDFS. Data can be moved in and out of a cluster through upload/download to HDFS or Cloud Storage.

### Can I use Cloud Storage with Dataproc?

Yes, Managed Service for Apache Spark clusters automatically install the Cloud Storage connector. There are a number of benefits to choosing Cloud Storage over traditional HDFS including data persistence, reliability, and performance.

### Can I get Cloud Storage Connector support?

Yes, when used with Managed Service for Apache Spark, the Cloud Storage connector is supported at the same level as Managed Service for Apache Spark (see [Get support](https://docs.cloud.google.com/managed-spark/docs/support/getting-support)). All connector users can use the `google-cloud-dataproc` tag on [Stack Overflow](https://stackoverflow.com/questions/tagged/google-cloud-dataproc) for connector questions and answers.

### What's the ideal file size for datasets on HDFS and Cloud Storage?

To improve performance, store data in larger file sizes, for example, file sizes in the 256MB–512MB range.

### How reliable is Managed Service for Apache Spark?

Because Managed Service for Apache Spark is built on reliable and proven Google Cloud Platform technologies, including Compute Engine, Cloud Storage, and Monitoring, it is designed for high availability and reliability. As a generally available product, you can review the [Managed Service for Apache Spark SLA](https://cloud.google.com/dataproc/sla).

### What happens to my data when a cluster is shut down?

Any data in Cloud Storage persists after your cluster is shut down. This is one of the reasons to choose Cloud Storage over HDFS since HDFS data is removed when a cluster is shut down (unless it is transferred to a persistent location prior to shutdown).

## Logging, monitoring, & debugging

### What sort of logging and monitoring is available?

By default, Managed Service for Apache Spark clusters are integrated with Monitoring and Logging. Monitoring and Logging make it easy to get detailed information about the health, performance, and status of your Managed Service for Apache Spark clusters. Both application (YARN, Spark, etc.) and system logs are forwarded to Logging.

### How can I view logs from Managed Service for Apache Spark?

You can view logs from Managed Service for Apache Spark in several ways. You can visit Logging to view aggregated cluster logs in a web browser. Additionally, you can use the command-line (SSH) to manually view logs or monitor application outputs. Finally, details are also available via the Hadoop application web UIs, such as the YARN web interface.

### How can clusters be monitored?

Clusters can be easily monitored through Monitoring or the Cloud Managed Service for Apache Spark section of the [Google Cloud console](https://console.cloud.google.com/). You can also monitor your clusters through command-line (SSH) access or the application (Spark, YARN, etc.) web interfaces.

## Security & access

### How is my data secured?

Google Cloud Platform employs a rich security model, which also applies to Cloud Managed Service for Apache Spark. Managed Service for Apache Spark provides authentication, authorization, and encryption mechanisms, such as SSL, to secure data. Data can be user encrypted in transit to and from a cluster, upon cluster creation or job submission.

### How can I control access to my Managed Service for Apache Spark cluster?

Google Cloud Platform offers authentication mechanisms, which can be used with Managed Service for Apache Spark. Access to Managed Service for Apache Spark clusters and jobs can be granted to users at the project level.

## Billing

### How is Managed Service for Apache Spark billed?

Managed Service for Apache Spark is billed by the second, and is based on the size of a cluster and the length of time the cluster is operational. In computing the cluster component of the fee, Managed Service for Apache Spark charges a flat fee based on the number of virtual CPUs (vCPUs) in a cluster. This flat fee is the same regardless of the machine type or size of the Compute Engine resources used.

### Am I charged for other Google Cloud resources?

Yes, running a Managed Service for Apache Spark cluster incurs charges for other Google Cloud resources used in the cluster, such as Compute Engine and Cloud Storage. Each item is stated separately in your bill, so you know exactly how your costs are calculated and allocated.

### Is there a minimum or maximum time for billing?

Google Cloud charges are calculated by the second, not by the hour. Currently, Compute Engine has a 1-minute minimum billing increment. Therefore, Managed Service for Apache Spark also has a 1-minute minimum billing increment.

## Availability

### Who can create a Managed Service for Apache Spark cluster?

Managed Service for Apache Spark is generally available which means all Google Cloud Platform customers can use it.

### In which regions is Managed Service for Apache Spark available?

Managed Service for Apache Spark is available across all regions and zones of the Google Cloud platform.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

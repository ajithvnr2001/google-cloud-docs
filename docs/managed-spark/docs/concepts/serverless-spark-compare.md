---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/serverless-spark-compare/
title: Compare Managed Service for Apache Spark serverless and cluster deployments \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:41.136123+00:00
---

# Compare Managed Service for Apache Spark serverless and cluster deployments  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/serverless-spark-compare/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Compare Managed Service for Apache Spark serverless and cluster deployments Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark now includes the previous "Dataproc on Compute Engine" (cluster deployment) and the previous "Google Cloud Serverless for Apache Spark" (serverless deployment) product options.

While both options provide a managed highly scalable, production-ready, and secure Spark environment that is OSS-compatible with full support for data formats, they differ in how they manage underlying infrastructure and bill for resources. Review the following features and use cases to help you choose a Spark solution.

For more information about Managed Service for Apache Spark serverless deployments, see [Managed Service for Apache Spark serverless deployment overview](https://docs.cloud.google.com/managed-spark/docs/serverless-overview).

## Compare Managed Service for Apache Spark deployments

The following table lists key differences between Managed Service for Apache Spark cluster and serverless deployments.

Deployment | Serverless | Cluster  
---|---|---  
Processing frameworks | Batch workloads and interactive sessions: Spark | Spark. Other open source frameworks, such as Hive, Flink, Trino, and Kafka  
Serverless | Yes | No  
Startup time | 50s | 120s  
Infrastructure control | No | Yes  
Resource management | Serverless | YARN  
GPU support | [Yes](https://docs.cloud.google.com/managed-spark/docs/guides/gpus-serverless) | Yes  
Interactive sessions | Yes | No   
Custom containers | [Yes](https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers) | No  
VM access (SSH) | No | Yes  
Java versions | Java 17, 21 | Java 17 and previous versions  
  
## Decide on the best Managed Service for Apache Spark deployment

This section outlines core Managed Service for Apache Spark strengths and primary use cases to help you select the best Managed Service for Apache Spark deployment—cluster or serverless— for your Spark workloads.

### Overview

Managed Service for Apache Spark deployments differ in the degree of control, infrastructure management, and billing mode that each offer.

  * **serverless deployment:** Managed Service for Apache Spark offers Spark-jobs-as-a-service, running Spark on fully managed Google Cloud infrastructure. You pay for job runtime.
  * **cluster deployment:** Offers Spark-clusters-as-a-service, running managed Spark on your Compute Engine infrastructure. You pay for cluster uptime.



Due to these differences, each Managed Service for Apache Spark deployment is best suited in the following use cases:

Deployment | Use cases  
---|---  
serverless | Different dedicated job environments  
Scheduled batch workloads  
Code management prioritized over infrastructure management  
cluster | Long-running, shared environments  
Workloads requiring granular control over infrastructure  
Migrating legacy Hadoop and Spark environments  
  
### Key differences

Feature | serverless deployment | cluster deployment  
---|---|---  
**Management model** | Fully managed, serverless execution environment. | Cluster-based. You provision and manage clusters.  
**Control & customization** | Less infrastructure control, with focus on submitting code and specifying Spark parameters. | Greater control over cluster configuration, machine types, and software. Ability to use spot VMs, and reuse reservations and Compute Engine resource capacity. Suitable for workloads that have a dependency on specific VM shapes, such as CPU architectures.  
**Use cases** | Ad-hoc queries, interactive analysis, new Spark pipelines, and workloads with unpredictable resource needs. | Long-running, shared clusters, migrating existing Hadoop and Spark workloads with custom configs, workloads requiring deep customization.  
**Operational overhead** | Lower overhead. Google Cloud manages the infrastructure, scaling, and provisioning, enabling a `NoOps` model. [Gemini Cloud Assist](https://docs.cloud.google.com/managed-spark/docs/guides/ai-investigations-with-gca) makes troubleshooting easier while serverless [autotuning](https://docs.cloud.google.com/managed-spark/docs/concepts/autotuning) helps provide optimal performance. | Higher overhead that requires cluster management, scaling, and maintenance.  
**Efficiency model** | No idle compute overhead: compute resource allocation only when the job is running. No startup and shutdown cost. Shared interactive sessions supported for improved efficiency. | Efficiency gained by sharing clusters across jobs and teams, with a sharing, [multi-tenancy model](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/sa-multi-tenancy).  
**Location control** | Managed Service for Apache Spark supports regional workloads without extra cost to provide extra reliability and obtainability. | Clusters are zonal. The zone can be auto-selected during cluster creation.  
**Cost** | Billed only for the duration of the Spark job execution, not including startup and teardown, based on resources consumed. Billed as Data Compute Units (DCU) used and other infrastructure costs. | Billed for the time the cluster is running, including startup and teardown, based on the number of nodes. Includes Managed Service for Apache Spark license fee plus infrastructure cost.  
**Committed Usage Discounts (CUDs)** | BigQuery spend-based CUDs apply to Managed Service for Apache Spark jobs. | Compute Engine CUDs apply to all resource usage.  
**Image and runtime control** | Users can pin to minor Managed Service for Apache Spark runtime versions; subminor versions are managed by Managed Service for Apache Spark. | Users can pin to minor and subminor Managed Service for Apache Spark image versions.  
**Resource management** | serverless | YARN  
**GPU support** | [Yes](https://docs.cloud.google.com/managed-spark/docs/guides/gpus-serverless) | [Yes](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/gpus)  
**Interactive sessions** | Yes | No  
**Custom containers** | [Yes](https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers) | No  
**VM access (SSH)** | No | [Yes](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh)  
**Java versions** | Java `17`, `21` | Previous versions supported  
**Startup time** | 50s | 120s  
  
### When to choose serverless deployment

Managed Service for Apache Spark serverless deployment abstracts away the complexities of cluster management, allowing you to focus on Spark code. This makes it an excellent choice for use in the following data processing scenarios:

  * **Ad-hoc and interactive analysis:** For data scientists and analysts who run interactive queries and exploratory analysis using Spark, the serverless model provides a quick way to get started without focusing on infrastructure.
  * **Spark-based applications and pipelines:** When building new data pipelines or applications on Spark, Managed Service for Apache Spark can significantly accelerate development by removing the operational overhead of cluster management.
  * **Workloads with sporadic or unpredictable demand:** For intermittent Spark jobs or jobs with fluctuating resource requirements, serverless [autoscaling](https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling) and pay-per-use pricing (charges apply to job resource consumption) can significantly reduce costs.
  * **Developer productivity focus:** By eliminating the need for cluster provisioning and management, Managed Service for Apache Spark speeds the creation of business logic, provides faster insights, and increases productivity.
  * **Simplified operations and reduced overhead:** Managed Service for Apache Spark infrastructure management reduces operational burdens and costs.



### When to choose cluster deployment

You can use Managed Service for Apache Spark cluster deployment to run Apache Spark and other open source data processing frameworks. It offers a high degree of control and flexibility, making it the preferred choice in the following scenarios:

  * **Migrating existing Hadoop and Spark workloads:** Supports migrating on-premises Hadoop or Spark clusters to Google Cloud. Replicate existing configurations with minimal code changes, particularly when using older Spark versions.
  * **Deep customization and control:** Lets you customize cluster machine types, disk sizes, and network configurations. This level of control is critical for performance tuning and optimizing resource utilization for complex, long-running jobs.
  * **Long-running and persistent clusters:** Supports continuous, long-running Spark jobs and persistent clusters for multiple teams and projects.
  * **Diverse open source ecosystem:** Provides a unified environment to run data processing pipelines running Hadoop ecosystem tools, such as Hive, Pig, or Presto, with your Spark workloads.
  * **Security compliance:** Enables control over infrastructure to meet specific security or compliance standards, such as safeguarding personally identifiable information (PII) or protected health information (PHI).
  * **Infrastructure flexibility:** Offers Spot VMs and the ability to reuse reservations and Compute Engine resource capacity to balance resource use and facilitate your cloud infrastructure strategy.



### Summing up

The decision whether to use Managed Service for Apache Spark cluster or serverless deployment depends on your workload requirements, operational preferences, and preferred level of control.

  * **Choose Managed Service for Apache Spark serverless** for its ease of use, cost-efficiency for intermittent workloads, and its ability to accelerate development for new Spark applications by removing the overhead of infrastructure management.
  * **Choose Managed Service for Apache Spark clusters** when you need maximum control, need to migrate Hadoop or Spark workloads, or require a persistent, customized, shared cluster environment.



After evaluating the factors listed in this section, select the most efficient and cost-effective Managed Service for Apache Spark deployment to run Spark to unlock the full potential of your data.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 

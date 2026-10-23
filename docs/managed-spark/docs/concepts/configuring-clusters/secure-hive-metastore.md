---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/secure-hive-metastore/
title: Create and secure a Hive metastore cluster \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:34.144229+00:00
---

# Create and secure a Hive metastore cluster  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/secure-hive-metastore/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Create and secure a Hive metastore cluster Stay organized with collections  Save and categorize content based on your preferences. 

**Objective:** Replace the default Hive metastore password when you create a Managed Service for Apache Spark cluster for added security.

## Overview

When you create a Managed Service for Apache Spark cluster, the Apache Hive application and its components, including Hive metastore, are installed on the cluster, and a default password is set in the `hive-site.xml` file located on the cluster master node.

Specifying your own Hive metastore password is recommended to accomplish the following goals:

  * As a best-practice security measure to ensure you control access to the local Hive metastore by providing your own password

  * To specify a known password that controls access to external Hive metastores used with external databases that are shared among different clusters




## Set the Hive metastore password

Run the following [Google Cloud CLI Managed Service for Apache Spark clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command to create a Managed Service for Apache Spark cluster and specify a Hive metastore password.
    
    
    gcloud dataproc clusters create cluster-name
     --properties="hive:javax.jdo.option.ConnectionPassword=HIVE_METASTORE_PASSWORD"
    

Notes:

  * See [Create a key](https://docs.cloud.google.com/kms/docs/create-key) to create a key in Cloud Key Management Service.
  * The Hive metastore password is stored only on cluster master node(s), not on worker nodes.



For additional information on securing Managed Service for Apache Spark clusters see [Managed Service for Apache Spark security best practices](https://docs.cloud.google.com/managed-spark/docs/concepts/security-best-practices).

## Unsupported Scenarios

Managed Service for Apache Spark does not support the following Hive metastore scenarios, regardless of whether you use the default or a user-supplied Hive metastore password:

  * You use an embedded metastore client in the Spark driver running in cluster mode, so that the worker nodes require Hive passwords. This scenario can cause connectivity problems with the metastore database since the connection is not made through the `HiveMetaStore` process running on the Managed Service for Apache Spark master node.

  * You deactivate Hive metastore and `hive-server2` to use your own MySQL database. In this scenario, the `spark.hadoop.javax.jdo.option.ConnectionURL=jdbc:mysql://CLUSTER_NAME-m/metastore` property has no effect.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

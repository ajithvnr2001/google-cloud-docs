---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/services/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:44.128590+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/services/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark Stay organized with collections  Save and categorize content based on your preferences. 

This page lists services that Managed Service for Apache Spark [image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions#supported-dataproc-image-versions) run on Managed Service for Apache Spark cluster nodes.

## All nodes

The following services run on all nodes in a cluster.

Node type | Service | Image versions | Description  
---|---|---|---  
All nodes | [google-dataproc-agent](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/life-of-a-job) | all | Receives jobs from Managed Service for Apache Spark and launches job drivers  
[google-fluentd](https://docs.cloud.google.com/logging/docs/agent/logging) | all | Collects and pushes logs to Logging  
  
## Standard clusters

The following services run on standard clusters.

Node type | Service | Image versions | Description  
---|---|---|---  
Master | [hadoop-hdfs-namenode](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html#NameNode_and_DataNodes) | all | Manages the HDFS filesystem  
[hadoop-hdfs-secondarynamenode](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html#Secondary_NameNode) | all | Checkpoints the NameNode  
[hadoop-mapreduce-historyserver](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-hs/HistoryServerRest.html) | all | Serves mapreduce application history information  
[hadoop-yarn-resourcemanager](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html) | all | Schedules and manages YARN applications  
[hadoop-yarn-timelineserver](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/TimelineServer.html) | 1.3+ | Serves YARN application history information  
[hive-metastore](https://cwiki.apache.org/confluence/display/hive/design#Design-Metastore) | all | Manages Hive table metadata. As a default, uses the local `mariadb` (image versions < 1.5) or `mysql` (image versions 1.5+) database on the master node as the Hive table metadata store. Using the default database is not recommended because these databases are tied to the cluster's lifecycle. Instead, use either of the following as the Hive metastore database (in recommendation order): 

  1. [Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs)
  2. [Cloud SQL instance](https://github.com/GoogleCloudDataproc/initialization-actions/tree/master/cloud-sql-proxy)

  
[hive-server2](https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Overview) | all | Serves queries received from clients (primarily [beeline shell queries](https://cwiki.apache.org/confluence/display/hive/HiveServer2+Clients#HiveServer2Clients-Beeline%E2%80%93CommandLineShell)) against Hive  
[mariadb](https://mariadb.org/) | < 1.5 | A relational database used as the default underlying database for Hive metastore in Managed Service for Apache Spark < 1.5 images  
[mysql](https://www.mysql.com/) | 1.5+ | A relational database used as the default underlying database for Hive metastore in Managed Service for Apache Spark 1.5+ images   
[nfs-kernel-server](https://help.ubuntu.com/community/SettingUpNFSHowTo) | < 1.3 | NFS is the Network File System.  
[spark-history-server](https://spark.apache.org/docs/latest/monitoring.html) | all | Serves Spark application history information  
All Workers | [hadoop-yarn-nodemanager](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/NodeManager.html) | all | Launches and manages YARN containers  
Primary Workers only | [hadoop-hdfs-datanode](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html#NameNode_and_DataNodes) | all | Stores HDFS blocks  
  
## HA Clusters

In Managed Service for Apache Spark [High Availability (HA) clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-availability), different services run on different master nodes, as show below. HA cluster worker node services are the same as those listed for standard clusters.

Node type | Service | Image versions | Description  
---|---|---|---  
All masters | [hadoop-hdfs-journalnode](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HDFSHighAvailabilityWithQJM.html#Architecture) | all | A quorum of journal nodes maintains an edit log of HDFS namespace modifications. If a failover occurs, the Standby NameNode reads the edit log and takes control from the Active NameNode.  
[hadoop-yarn-resourcemanager](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html) | all | Schedules and manages YARN applications  
[hive-metastore](https://cwiki.apache.org/confluence/display/hive/design#Design-Metastore) | all | Manages Hive table metadata. As a default, uses the local `mariadb` (image versions < 1.5) or `mysql` (image versions 1.5+) database on the master node as the Hive table metadata store. Using the default database is not recommended because these databases are tied to the cluster's lifecycle. Instead, use either of the following as the Hive metastore database (in recommendation order): 

  1. [Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs)
  2. [Cloud SQL instance](https://github.com/GoogleCloudDataproc/initialization-actions/tree/master/cloud-sql-proxy)

  
[hive-server2](https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Overview) | all | Serves queries received from clients (primarily [beeline shell queries](https://cwiki.apache.org/confluence/display/hive/HiveServer2+Clients#HiveServer2Clients-Beeline%E2%80%93CommandLineShell)) against Hive  
[zookeeper-server](https://zookeeper.apache.org/) | all | A ZooKeeper quorum is used for distributed coordination. In [High Availability (HA) clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-availability), it is used for [HDFS NameNodes](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HDFSHighAvailabilityWithQJM.html#Components) and [YARN resource managers](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/ResourceManagerHA.html#RM_Failover) leader election.  
Masters 0 and 1 only | [hadoop-hdfs-namenode](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html#NameNode_and_DataNodes) | all | Manages the HDFS filesystem  
[hadoop-hdfs-zkfc](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HDFSHighAvailabilityWithQJM.html#Components) | all | ZKFC is the `ZKFailoverController` process, which runs with the HDFS NameNode. It monitors the health of the NameNode, and manages leader election via ZooKeeper in the event of a failover.  
Master 0 only | [hadoop-mapreduce-historyserver](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-hs/HistoryServerRest.html) | all | Serves mapreduce application history information  
[hadoop-yarn-timelineserver](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/TimelineServer.html) | 1.3+ | Serves YARN application history information  
[mariadb](https://mariadb.org/) | < 1.5 | A relational database used as the default underlying database for Hive metastore in Managed Service for Apache Spark < 1.5 images  
[mysql](https://www.mysql.com/) | 1.5+ | A relational database used as the default underlying database for Hive metastore in Managed Service for Apache Spark 1.5+ images  
[nfs-kernel-server](https://help.ubuntu.com/community/SettingUpNFSHowTo) | < 1.3 | NFS is the Network File System.  
[spark-history-server](https://spark.apache.org/docs/latest/monitoring.html) | all | Serves Spark application history information  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 

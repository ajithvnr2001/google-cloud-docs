---
url: https://docs.cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals/
title: Managed Service for Apache Spark principals \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:41:42.310392+00:00
---

# Managed Service for Apache Spark principals  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark principals Stay organized with collections  Save and categorize content based on your preferences. 

When you use Managed Service for Apache Spark to create clusters and run jobs on your clusters, the service sets up the necessary [Managed Service for Apache Spark roles and permissions](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam) in your project to access and use the Google Cloud resources it needs to accomplish these tasks. However, if you do cross-project work, for example to access data in another project, you will need to set up the necessary roles and permissions to access cross-project resources.

To help you do cross-project work successfully, this document lists the different principals that use Managed Service for Apache Spark and the roles that contain the necessary permissions for those principals to access and use Google Cloud resources.

There are three principals (identities) that access and use the Managed Service for Apache Spark:

  1. User Identity
  2. Control Plane Identity
  3. Data Plane Identity

![dataproc-service-accounts1](https://docs.cloud.google.com/static/managed-spark/images/dataproc-service-accounts1.png)




## Dataproc API User (User identity)

Example: _username@example.com_

This is the user that calls Managed Service for Apache Spark to create clusters, submit jobs, and make other requests to the service. The user is usually an individual, but it can also be a [service account](https://docs.cloud.google.com/iam/docs/understanding-service-accounts) if Managed Service for Apache Spark is invoked through an API client or from another Google Cloud service such as Compute Engine, Cloud Run functions, or Managed Service for Apache Airflow.

**Related roles**

  * [Dataproc roles](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#roles), [Project roles](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#project_roles)



**Notes**

  * Dataproc API-submitted jobs run as `root` on Linux.
  * Managed Service for Apache Spark clusters inherit project-wide Compute Engine SSH metadata unless explicitly blocked by setting `--metadata=block-project-ssh-keys=true` when you create your cluster (see [Cluster metadata](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/metadata)).

  * HDFS user directories are created for each project-level SSH user. These HDFS directories are created at cluster deployment time, and a new (post-deployment) SSH user is not given an HDFS directory on existing clusters.




## Managed Service for Apache Spark Service Agent (Control Plane identity)

Example: _service- project-number@dataproc-accounts.iam.gserviceaccount.com_

The [Managed Service for Apache Spark Service Agent service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#service_agent_account) is used to perform a broad set of system operations on resources located in the project where a Managed Service for Apache Spark cluster is created, including:

  * Creation of Compute Engine resources, including VM instances, instance groups, and instance templates
  * `get` and `list` operations to confirm the configuration of resources such as images, firewalls, Managed Service for Apache Spark initialization actions, and Cloud Storage buckets
  * Auto-creation of the Managed Service for Apache Spark [staging and temp buckets](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket) if the staging or temp bucket is not specified by the user
  * Writing cluster configuration metadata to the staging bucket
  * Accessing [VPC networks in a host project](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/network#create_a_cluster_that_uses_a_network_in_another_project)



**Related roles**

  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent)



## Managed Service for Apache Spark VM service account (Data Plane identity)

Example: _project-number -compute@developer.gserviceaccount.com_

Your application code runs as the [VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#VM_service_account) on Managed Service for Apache Spark VMs. User jobs are granted the roles (with their associated permissions) of this service account.

The VM service account does the following:

  * Communicates with the Managed Service for Apache Spark control plane.
  * Reads and writes data from and to the [Managed Service for Apache Spark staging and temp buckets](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket).
  * As needed by your Managed Service for Apache Spark jobs, reads and writes data from and to Cloud Storage, BigQuery, Cloud Logging, and other Google Cloud resources.



**Related roles**

  * [Dataproc Worker](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#roles)
  * [Cloud Storage roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles)
  * [BigQuery roles](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery)

**Note:** For interactive workloads, users can opt to use their user identity to access Cloud Storage objects in buckets owned by the same project that contains the cluster (see [Managed Service for Apache Spark Personal Cluster Authentication](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/personal-auth)).

## What's next

  * Learn more about [Managed Service for Apache Spark roles and permissions](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam).
  * Learn more about [Managed Service for Apache Spark service accounts](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts).
  * See [BigQuery Access Control](https://docs.cloud.google.com/bigquery/docs/access-control).
  * See [Cloud Storage Access Control options](https://docs.cloud.google.com/storage/docs/access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/database-options/
title: Best practices for planning your database deployments on GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:15.671175+00:00
---

# Best practices for planning your database deployments on GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/database-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Best practices for planning your database deployments on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains best practices for running databases in containers on GKE. You can use a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) to create a set of Kubernetes-managed containerized database instances. You then create a [Service](https://kubernetes.io/docs/concepts/services-networking/service/) to provide access to the database independently of any particular Pod. The Service remains unchanged even if the Pod is moved to a different node.

To access the data in your database instance, you create a [`PersistentVolumeClaim`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#persistentvolumeclaims) (PVC) resource and make it available to your workload.

Databases rely on local disks for persistence. A database that runs as a Service in a Kubernetes cluster and its database files in a `PersistentVolumeClaim` is bound to the lifecycle of the cluster. If the cluster is deleted, the database is also deleted.

If you are building or deploying a stateful application running in GKE, consider using one of the following deployment options for database instances:

  * **Fully-managed databases** : A managed database, such as [Cloud SQL](https://docs.cloud.google.com/sql) or [Spanner](https://docs.cloud.google.com/spanner), provides reduced operational overhead and is optimized for Google Cloud infrastructure. Managed databases require less effort to maintain and operate than a database that you deploy directly in Kubernetes.
  * **Kubernetes application** : You can deploy and run a database instance (such as [MySQL](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workloads/mysql)) on a GKE cluster.

For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). 

## Considerations for database deployments on GKE

Each of the preceding options has trade-offs, given your business goals and constraints. Use the following table to decide if database deployment on GKE is the right choice for you.

Consideration  | Description   
---|---  
Database independence  | The lifecycle of a PersistentVolumeClaim is tied to the corresponding GKE cluster. If you don't want your database lifecycle to depend on a particular GKE cluster, consider keeping the database separate, as a managed database or in a VM instance.   
Scaling with GKE  | **Vertical scaling** : You can configure [your Pods requests to scale automatically](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler). However, you must ensure that your database application can withstand disruptions when your Pods scale up with vertical Pod autoscaling. **Horizontal scaling** : Your database may be able to horizontally scale reads or writes by adding replicas. Whether your database supports horizontal scaling depends on whether it has a single writer or multi-writer architecture. To use horizontal scaling, you may need to update the database configuration, in addition to scaling up the number of replicas.  
GKE overhead  | On Autopilot clusters, you aren't billed for resource reservations, only for [ resource requests](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests). On Standard clusters, GKE [ reserves resources](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#memory_cpu) for its own operations. Databases on Standard clusters aren't scaled automatically, so overhead might be high for small Pods.  
Number of database instances  | In the context of Kubernetes, each database instance runs in its own Pod and has its own PersistentVolumeClaim. If you have a high number of instances, you have to operate and manage a large set of Pods, nodes, and volume claims. You might want to use a managed database instead.   
Database backup in GKE  | A PersistentVolumeClaim is scoped to a GKE cluster. This scoping means that when a GKE cluster is deleted, the volume claim is deleted. Any database files in the cluster are also deleted. To guard against accidental loss of the database files, we recommend replication or frequent backup. You can use [ Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) to take snapshots of your application configuration and volume data at periodic intervals. Backup for GKE handles the scheduling of volume backups, managing the backup lifecycle, and restoring of backups to a cluster.   
Kubernetes-specific recovery behavior  | When a Pod fails in Kubernetes, it is re-created. From a database instance perspective, this means that when a Pod is re-created, any configuration that isn't persistent within a database or on stable storage outside Pods is also re-created.   
Database architecture  | If your database is configured to use an [active-passive architecture](https://www.cockroachlabs.com/blog/brief-history-high-availability/#what-is-active-passive-availability), you have to ensure that only one replica is configured as Primary. Many relational databases have an option for active-passive failover, where a secondary can be promoted to primary in the event of a primary failure.   
Database migration  | If you plan to migrate your existing database system to GKE, refer to [ Database migration: Concepts and principles (Part 1)](https://docs.cloud.google.com/solutions/database-migration-concepts-principles-part-1) and [ Database migration: Concepts and principles (Part 2)](https://docs.cloud.google.com/solutions/database-migration-concepts-principles-part-2).   
User re-training  | If you move from a self-managed or provider-managed deployment to a Kubernetes database deployment, you need to retrain database administrators to operate in the new environment as reliably as they operate in the current environment. Application developers might also have to learn about differences to a lesser extent.   
  
The preceding table provides a discussion of some of the considerations for database deployment. However, the table doesn't include all possible considerations. You also need to consider disaster recovery, connection pooling, and monitoring.

## What's next

  * Learn how to [deploy a highly-available MySQL topology on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workloads/mysql).
  * Learn how to [deploy a highly-available PostgreSQL instance on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workloads/postgresql).
  * Learn more about [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke), a service for backing up and restoring workloads in GKE.
  * Explore [Persistent Volumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) in more detail.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/cross-data-center-replication/about-cross-data-center-replication/
title: About cross-data-center replication \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:25:23.564663+00:00
---

# About cross-data-center replication  |  AlloyDB Omni for Kubernetes: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/cross-data-center-replication/about-cross-data-center-replication/

This page documents AlloyDB Omni version **16.9.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)



Send feedback 

#  About cross-data-center replication Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/cross-data-center-replication/about-cross-data-center-replication)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/cross-data-center-replication/about-cross-data-center-replication)

This page provides an overview of AlloyDB Omni cross-data-center replication. 

AlloyDB Omni cross-data-center replication lets you create secondary database clusters and instances from a primary database cluster to make the resources available in different data centers, in the event of an outage in the primary data center. These secondary database clusters function as copies of your primary database cluster resources.

Key concepts in this page include the following:

  * **Primary database cluster.** A read-write database cluster in a single data center.
  * **Secondary database cluster.** A read-only database cluster in a different data center than the primary, that replicates from the primary database cluster asynchronously. In the event of a failure of an AlloyDB Omni primary database cluster, you can promote a secondary database cluster to a primary database cluster.



## Benefits

The benefits of cross-data-center replication on AlloyDB Omni include the following:

  * **Disaster recovery.** In the event the primary database cluster's data center becomes unavailable, you can promote AlloyDB Omni resources in another data center to serve requests.

  * **Geographically distributed data.** Distributing the data geographically brings the data closer to you and decreases read latency.

  * **Geographic load balancing.** In the event of slow or overloaded connections in one data center, you can route traffic to another data center.

  * **Improved read performance.** It makes AlloyDB Omni resources available closer to your application's data center.

  * **Switchover.** You can perform a switchover for testing your disaster recovery setup or performing migration of your workload.




## How to work with cross-data-center replication

Working with AlloyDB Omni cross-data-center replication involves the following tasks:

  * [**Create a secondary database cluster.**](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/cross-data-center-replication/work-with-cross-data-center-replication#secondary-db-cluster-instance) A secondary database cluster is a continuously updated copy of your AlloyDB Omni primary cluster.

  * [**View a secondary database cluster.**](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/cross-data-center-replication/work-with-cross-data-center-replication#view-secondary-cluster) After you create a secondary database cluster, you can view its status and replication status.

  * [**Promote a secondary database cluster.**](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/cross-data-center-replication/work-with-cross-data-center-replication#promote-secondary-cluster) You can read the data in a secondary database cluster but cannot write to it until you promote it to a primary database cluster.

There are two common scenarios for promoting your secondary database cluster to a primary database cluster:

    * **Data center migration.** Perform a planned migration of the AlloyDB Omni resources from their primary data center to another data center.

    * **Disaster recovery.** Rapidly activate the AlloyDB Omni resources in a secondary data center in the event that the resources in the primary data center become unavailable. Due to replication lag, some data loss might occur.

Promoting a secondary database cluster converts it to a standalone fully functional database cluster with read and write capabilities. The promoted database cluster no longer replicates the data from the primary database cluster it was formerly associated with.

  * [**Switchover.**](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/cross-data-center-replication/work-with-cross-data-center-replication#switchover-secondary) Switchover lets you reverse the roles of your primary and secondary database cluster. You can perform a switchover for testing your disaster recovery setup or performing migration of your workload. When you complete the switchover, the direction of replication is reversed.




## What's next

  * [Work with cross-data-center replication](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

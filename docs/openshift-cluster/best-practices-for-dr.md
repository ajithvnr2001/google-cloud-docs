---
url: https://docs.cloud.google.com/openshift-cluster/best-practices-for-dr/
title: Best practices for disaster recovery \u00a0|\u00a0 Cluster Services for OpenShift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:07:51.969316+00:00
---

# Best practices for disaster recovery  |  Cluster Services for OpenShift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/openshift-cluster/best-practices-for-dr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Services for OpenShift ](https://docs.cloud.google.com/openshift-cluster)
  * [ Guides ](https://docs.cloud.google.com/openshift-cluster/overview)



Send feedback 

#  Best practices for disaster recovery Stay organized with collections  Save and categorize content based on your preferences. 

Disaster recovery (DR) is essential for maintaining the continuity of your applications that are deployed on the OpenShift Container Platform on Google Cloud. This document provides an overview of the architectural options for DR with OpenShift on Google Cloud, helping your organization to achieve minimal downtime and rapid recovery in the event of a disaster. 

This document is intended for system administrators, cloud architects, and application developers who are responsible for maintaining the availability and resilience of applications on the OpenShift Container Platform deployed on Google Cloud.

This document is part of a series that focuses on the application-level strategies that ensure your workloads remain highly available and quickly recoverable in the face of failures. The documents in this series are as follows:

  * Best practices for disaster recovery (this page)
  * [Best practices for high availability](https://docs.cloud.google.com/openshift-cluster/best-practices-for-ha)
  * [Disaster recovery strategies for active-passive setups](https://docs.cloud.google.com/openshift-cluster/dr-for-active-passive-setups)
  * [Disaster recovery strategies for active-inactive setups](https://docs.cloud.google.com/openshift-cluster/dr-for-active-inactive-setups)



### DR planning

Planning for DR is a critical component of running production workloads in the cloud. Although OpenShift and Google Cloud offer robust infrastructure-level redundancy, you must also design and configure your applications to quickly recover from catastrophic failures.

Effective DR planning involves a layered approach. You begin by defining clear recovery time objectives (RTO) and recovery point objectives (RPO) for your application and system for rapid redeployment.

Your secrets and credentials must also be recoverable and securely managed. By considering all of these factors, you can achieve a DR posture that lets you quickly create a new OpenShift cluster in a different region or fail over to a inactive secondary cluster. This secondary cluster remains offline until a failure occurs, at which point it is started and brought online to take over operations with minimal downtime.

## Architectures for DR

There are different options for deployment architectures that you can use for DR with OpenShift on Google Cloud. Each of these options has different implications for cost, complexity, and availability. The following table provides an overview of these architectures:

**Architecture** | **Description** | **Use case** | **Advantages** | **Disadvantages**  
---|---|---|---|---  
Active-passive | One cluster is active, handling all traffic, and the other is passive and ready to take over. Data is replicated to the passive cluster. | Suitable for applications with moderate RTO and RPO requirements. | Simpler to implement, lower cost for standby cluster. | Higher RTO due to failover time, potential data sync delays.  
Active-inactive | Similar to active-passive, but the inactive cluster is not used until a DR event. Data is regularly backed up. | Ideal for cost-sensitive environments that allow for higher RTO and RPO.  | Lower operational cost when inactive, suitable for DR where a secondary system is not actively running (cold DR). | Higher RTO due to activation and sync time, although there is the potential for data to go out of date.  
Active-active | Both clusters are active, handling traffic with load balancing and data replication between regions. | Critical applications requiring minimal downtime and high availability. | Lowest RTO and RPO, continuous availability. | Highest complexity and cost, requires robust network and data syncs.  
  
## What's next

  * Learn how to [implement monitoring and alerting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/monitoring/about-openshift-container-platform-monitoring#monitoring-targets-for-user-defined-projects_monitoring-stack-architecture) for cluster health, replication status, backup success, and application performance in both primary and secondary environments.
  * Learn how to [install OpenShift on Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/installing_on_google_cloud/index).
  * Learn more about [Red Hat solutions on Google Cloud](https://cloud.google.com/solutions/redhat)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

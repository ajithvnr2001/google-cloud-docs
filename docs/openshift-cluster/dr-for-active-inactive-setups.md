---
url: https://docs.cloud.google.com/openshift-cluster/dr-for-active-inactive-setups/
title: Disaster recovery strategies for active-inactive setups \u00a0|\u00a0 Cluster Services for OpenShift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:16.799988+00:00
---

# Disaster recovery strategies for active-inactive setups  |  Cluster Services for OpenShift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/openshift-cluster/dr-for-active-inactive-setups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Services for OpenShift ](https://docs.cloud.google.com/openshift-cluster)
  * [ Guides ](https://docs.cloud.google.com/openshift-cluster/overview)



Send feedback 

#  Disaster recovery strategies for active-inactive setups Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to plan and implement _active-inactive_ disaster recovery for OpenShift deployments on Google Cloud to help you to achieve minimal downtime and rapid recovery in the event of a disaster. It provides best practices for backing up data, managing configuration as code, and handling secrets to help to ensure that you can quickly recover your applications in the event of a disaster. 

This document is intended for system administrators, cloud architects, and application developers who are responsible for maintaining the availability and resilience of applications on Red Hat OpenShift Container Platform that is deployed on Google Cloud.

This document is part of a series that focuses on the application-level strategies that ensure your workloads remain highly available and quickly recoverable in the face of failures. It assumes that you have read [Best practices for disaster recovery](https://docs.cloud.google.com/openshift-cluster/best-practices-for-dr). The documents in this series are as follows:

  * [Best practices for disaster recovery](https://docs.cloud.google.com/openshift-cluster/best-practices-for-dr)
  * [Best practices for high availability](https://docs.cloud.google.com/openshift-cluster/best-practices-for-ha)
  * [Disaster recovery strategies for active-passive setups](https://docs.cloud.google.com/openshift-cluster/dr-for-active-passive-setups)
  * Disaster recovery strategies for active-inactive setups (this page)



## Architecture for disaster recovery

Active-inactive DR involves maintaining a secondary region as a standby, which is activated only during disasters. Unlike active-passive setups, where data is continuously replicated, this strategy relies on periodic backups that are stored in Cloud Storage, with infrastructure provisioned and data restored during failover. You can use tools such as [Velero](https://velero.io/docs/v1.15/), integrated with OpenShift API for Data Protection (OADP), to perform periodic backups. This approach minimizes costs, making it ideal for applications that can tolerate longer recovery times. It can also help organizations to align with extended recovery time objectives (RTO) and recovery point objectives (RPO).

In an active-inactive DR scenario, data is regularly backed up to the standby region, but not actively replicated. The infrastructure is provisioned as part of the failover process and data is restored from the most recent backup. You can use the OpenShift API for Data Protection (OADP), which is based on the Velero open-source project, to perform regular backups. We recommend that you store these backups in Cloud Storage buckets with versioning enabled. In the event of a disaster, you can use OADP to restore the contents of the cluster. This approach minimizes ongoing costs but results in longer RTO and potentially higher RPO compared to active-passive. This setup is suitable for applications with longer recovery time objectives.

The following diagram shows an active-inactive deployment and the failover process:

![Failover process.](https://docs.cloud.google.com/static/openshift-cluster/images/dr-failover.svg)

The failover process is as follows:

  1. A DR event is triggered when a monitored service becomes unavailable.
  2. A pipeline automatically provisions infrastructure in the DR region.
  3. A new OpenShift cluster is provisioned.
  4. Application data, secrets, and objects are restored from the latest backup through OADP.
  5. Cloud DNS record is updated to point to the regional load balancers in the DR region.



As shown in the preceding diagram, two separate OpenShift regional clusters are deployed, each in a different Google Cloud region, such as `us-central1` and `europe-west1`. Each cluster must be highly available within its region and use multiple zones to allow for redundancy.

### Description of components in an active-inactive DR scenario

The architecture has the following configuration:

  * **Primary region (Region A)** : Contains the fully operational OpenShift cluster serving production traffic.
  * **Secondary region (Region B)** : Initially contains minimal resources (VPC and subnets). Infrastructure (Compute Engine instances and OCP) is provisioned during failover.
  * **Backup storage** : Google Cloud Storage buckets store periodic backups (OADP or Velero for application objects, as well as PVs and database backups). We recommend that you use versioning and cross-region replication for the bucket.
  * **Configuration management** : Git repository stores Infrastructure as Code (IaC, for example, Terraform) and Kubernetes or OpenShift manifests (for GitOps).
  * **Backup tooling** : OADP (Velero) configured in the primary cluster to perform scheduled backups to Cloud Storage.
  * **Orchestration** : Scripts or automation tools trigger infrastructure provisioning and restore processes during failover.



### Products used

  * [Google Compute Engine](https://docs.cloud.google.com/compute/docs)
  * [Google Cloud Global External HTTPS Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Google Cloud Passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer)
  * [Cloud DNS](https://docs.cloud.google.com/dns/docs)
  * [Network endpoint groups](https://docs.cloud.google.com/load-balancing/docs/negs)
  * [Cloud Storage](https://docs.cloud.google.com/storage/docs)
  * [Cloud SQL](https://docs.cloud.google.com/sql/docs)
  * [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks)
  * [Secret Manager](https://docs.cloud.google.com/secret-manager/docs)
  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs)
  * [VPC Network](https://docs.cloud.google.com/vpc/docs/vpc)



## Use cases

Active-inactive DR is recommended for the following use cases:

  * Applications that can tolerate longer RTOs (for example, several minutes to hours).
  * Environments where cost optimization is important, and the expense of a continuously running standby cluster is prohibitive. The primary ongoing cost is for object storage rather than for running compute instances.
  * Development, testing, or less critical production workloads.
  * Archival or batch processing systems where recovery time is less critical.



## Design considerations

This section describes design factors, best practices, and design recommendations that you should consider when you use this reference architecture to develop a topology that meets your specific requirements for security, reliability, cost, and performance.

### Application configuration as code (GitOps)

We recommend that you adopt a GitOps approach to store all cluster and application configurations in a Git repository. This approach enables quick restoration in a DR scenario by enabling syncing to a state that is known to be running reliably in another cluster. Backups ensure you have snapshots of your runtime state, however, you also need a reliable way to redeploy application logic, manifests, and infrastructure definitions rapidly after a disaster.

### Use the OpenShift GitOps Operator

The [OpenShift GitOps operator](https://docs.openshift.com/gitops/1.15/understanding_openshift_gitops/about-redhat-openshift-gitops.html), based on Argo CD, provides a Red Hat-supported way to implement GitOps patterns directly within an OpenShift environment. It automates the process of continuously reconciling your cluster state with your chosen configuration and stores it in a Git repository.

The OpenShift GitOps operator's controller continuously ensures that the cluster's state matches the configuration defined in this repository. If resources drift or are missing, it automatically reconciles them. To learn more, see [About Red Hat OpenShift GitOps](https://docs.redhat.com/en/documentation/red_hat_openshift_gitops/1.15/html/understanding_openshift_gitops/about-redhat-openshift-gitops).

### DR scenario execution

In the event of a disaster, do the following:

  * Set up a new OpenShift cluster in another region.
  * Install the OpenShift GitOps operator.
  * Apply the same Application manifest referencing your Git repository.



The operator synchronizes the cluster state to match your repository, quickly redeploying deployments, services, routes, operators, and any other resources that are defined in your code.

To help avoid any issues during DR, we recommend that you do the following:

  * Maintain strict branching and tagging strategies in your Git repository so you can identify stable configurations suitable for DR.
  * Check that your DR cluster has network connectivity and appropriate permissions to access the Git repository.
  * Include all resource types as code to avoid manual intervention during failover (for example, infrastructure components, application workloads, and configurations).



### Firewall rules

[Define unified firewall policies](https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/installing_on_gcp/installing-restricted-networks-gcp#installation-creating-gcp-firewall-rules-vpc_installing-restricted-networks-gcp) and apply them consistently across both clusters to control traffic flow and enhance security.

Follow the least privilege principle, which means that you restrict the inbound and outbound traffic to only what's necessary for application functionality.

## Deployment

To learn how to deploy a topology based on this reference architecture, see the [Red Hat documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/installing_on_gcp/installing-gcp-default).

## What's next

  * Learn how to [implement monitoring and alerting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/monitoring/about-openshift-container-platform-monitoring#monitoring-targets-for-user-defined-projects_monitoring-stack-architecture) for cluster health, replication status, backup success, and application performance in both primary and secondary environments.
  * Learn how to [install OpenShift on Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/installing_on_google_cloud/index).
  * Learn more about [Red Hat solutions on Google Cloud](https://cloud.google.com/solutions/redhat).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

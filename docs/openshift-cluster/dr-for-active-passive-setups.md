---
url: https://docs.cloud.google.com/openshift-cluster/dr-for-active-passive-setups/
title: Disaster recovery strategies for active-passive setups \u00a0|\u00a0 Cluster Services for OpenShift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:07:52.208779+00:00
---

# Disaster recovery strategies for active-passive setups  |  Cluster Services for OpenShift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/openshift-cluster/dr-for-active-passive-setups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Services for OpenShift ](https://docs.cloud.google.com/openshift-cluster)
  * [ Guides ](https://docs.cloud.google.com/openshift-cluster/overview)



Send feedback 

#  Disaster recovery strategies for active-passive setups Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to plan and implement _active-passive_ disaster recovery for OpenShift deployments on Google Cloud to help you to achieve minimal downtime and rapid recovery in the event of a disaster. It provides best practices for backing up data, managing configuration as code, and handling secrets to help to ensure that you can quickly recover your applications in the event of a disaster. 

This document is intended for system administrators, cloud architects, and application developers who are responsible for maintaining the availability and resilience of applications on Red Hat OpenShift Container Platform that is deployed on Google Cloud.

This document is part of a series that focuses on the application-level strategies that ensure your workloads remain highly available and quickly recoverable in the face of failures. It assumes that you have read [Best practices for disaster recovery](https://docs.cloud.google.com/openshift-cluster/best-practices-for-dr). The documents in this series are as follows:

  * [Best practices for disaster recovery](https://docs.cloud.google.com/openshift-cluster/best-practices-for-dr)
  * [Best practices for high availability](https://docs.cloud.google.com/openshift-cluster/best-practices-for-ha)
  * Disaster recovery strategies for active-passive setups (this page)
  * [Disaster recovery strategies for active-inactive setups](https://docs.cloud.google.com/openshift-cluster/dr-for-active-inactive-setups)



## Architecture for disaster recovery

The following architecture diagram shows an active-passive deployment scenario for OpenShift on Google Cloud:

![Active-passive deployment, explained in following text.](https://docs.cloud.google.com/static/openshift-cluster/images/active-passive.svg)

As shown in the preceding diagram, in an active-passive deployment for disaster recovery, an OpenShift cluster in the primary region handles all production traffic. A secondary cluster in a different region is kept ready to take over if the primary fails. This setup ensures minimal downtime by having the secondary cluster pre-provisioned and in a _warm_ state, meaning it's set up with the necessary infrastructure and application components but not actively serving traffic until needed. Application data is replicated to the passive cluster to minimize data loss, aligning with the RPO.

One of the regional clusters acts as the primary (active) site and handles all of the production traffic. A secondary cluster, in a different region, is the standby for disaster recovery. The secondary cluster is kept in a warm state, and is ready to take over with minimal delay in case of a primary cluster failure.

### Description of components in an active-passive DR scenario

This architecture has the following configuration:

  * **Primary OpenShift cluster (active)** : Located in the primary Google Cloud region, this cluster runs the production workload and actively serves all user traffic under normal operating conditions.
  * **Secondary OpenShift cluster (passive)** : Located in a separate Google Cloud region for fault isolation, this cluster acts as the warm standby cluster. It's partially set up and running and is ready to take over if the primary system fails. It has the necessary infrastructure, OpenShift configuration, and application components deployed on it, but it doesn't serve live production traffic until a failover event is triggered.
  * **Google Cloud regions** : Geographically isolated locations that provide the foundation for disaster recovery. Using separate regions ensures that a large-scale event impacting one region doesn't affect the standby cluster.
  * **Global External HTTPS Load Balancer** : Acts as the single, global entry point for application traffic. Under normal conditions, it's configured to route all traffic to the primary (active) cluster. Its health checks monitor the primary cluster's availability.
  * **Data replication mechanism** : Continuous process or tools that are responsible for copying essential application data from the primary cluster to the secondary cluster (for example, databases or persistent volumes state). This approach ensures data consistency and minimizes data loss during a failover, helping you to meet your RPO.
  * **Monitoring and health checks:** Systems that continuously assess the health and availability of the primary cluster and its applications, for example, Cloud Monitoring, load balancer health checks, internal cluster monitoring. These systems are important for the quick detection of any failures.
  * **Failover mechanism:** A predefined process (manual, semi-automated, or fully automated) to redirect traffic from the primary to the secondary cluster upon detection of an unrecoverable failure in the primary. This process typically involves updating the Global Load Balancer's backend configuration to target the secondary cluster, making it the new active site.
  * **VPC Network** : The underlying Google Cloud network infrastructure that creates the necessary connectivity between regions for data replication and management.



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

Active-passive DR is recommended for the following use cases:

  * Applications that require a lower RTO (for example, minutes to hours) than would be achievable with cold restores, where data is restored from a backup that is not immediately accessible.
  * Systems where continuous data replication is feasible and the RPO must be minimized (for example, minutes to seconds).
  * Regulated industries with strict downtime limits and critical business applications where the cost of maintaining a warm standby cluster is justified by the business impact of downtime.



## Design considerations

This section describes design factors, best practices, and design recommendations that you should consider when you use this reference architecture to develop a topology that meets your specific requirements for security, reliability, cost, and performance.

### Safeguarding application state and configuration

OpenShift Container Platform provides OADP and offers comprehensive disaster recovery protection for applications running in clusters. You can use it to back up the Kubernetes and OpenShift objects that are used by both containerized applications and virtual machines (for example, deployments, services, routes, PVCs, ConfigMaps, secrets, and CRDs). However, OADP does not support full cluster backup and restore. To learn how to configure and schedule backups, and how to restore operations, see the [Red Hat documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/backup_and_restore/oadp-application-backup-and-restore#oadp-introduction).

OADP provides backup and restore processes for persistent volumes that rely on the block storage and NFS stores that are used by the applications. You can action these processes by using tools such as Restic or Kopia to snapshot or perform file-level backup.

OADP is useful for backing up object definitions, ensuring configuration consistency, and potentially restoring specific applications or namespaces if needed, complementing data replication.

To further reduce RPO and RTO in an active-passive configuration, we recommend that you configure data replication between primary and secondary regions.

Data replication is important for ensuring the secondary cluster can take over seamlessly. As outlined in the following section, implementation of data replication from the primary to the secondary clusters depends on the storage type that the application uses.

#### Block storage (persistent volumes)

Use Google Persistent Disk Asynchronous Replication to copy data from the primary to the secondary region. In this approach, you create a primary disk in the primary region, a secondary disk in the secondary region, and set up replication between them. The use of consistent groups ensures that both disks contain replication data from a common point in time, which is then used for DR. To learn more, see [Configure Persistent Disk Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/configure).

#### PersistentVolumes objects

In OpenShift, create [PersistentVolumes objects](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/understanding-persistent-storage#persistent-volumes_understanding-persistent-storage) in both clusters that link to these disks, and make sure that applications use the same Persistent Volume Claims (PVCs) in both clusters.

#### Application-level replication

Some applications (for example, databases and message queues) have built-in replication features that you can configure across clusters. You can also use a managed service like Pub/Sub to facilitate replication for specific types of application data or events.

#### Database backups

Applications can depend on different kinds of database products. To help outline design considerations for database backups, this document uses PostgreSQL as an example database.

#### Self-hosted backups using an in-cluster database operator

Database operators like the CloudNative PostgreSQL Operator can facilitate scheduled backups and disaster recovery for PostgreSQL clusters. CloudNative PostgreSQL Operator natively integrates with tools like `pg_basebackup` and supports streaming replication backups. You can store backups in cloud storage services such as Google Cloud Storage (Cloud Storage) for durability and recovery.

You can set up streaming replication between primary and secondary regional clusters to ensure that, even in the case of outage in the primary region, data is available. This streaming replication is typically synchronous within a region, and asynchronously across regions. For detailed configuration steps, see the [CloudNativePG documentation](https://cloudnative-pg.io/documentation/1.25/replication/#synchronous-replication).

In the case of a disaster, you can restore backups to a new PostgreSQL cluster, ensuring minimal downtime and data loss. The following is an example configuration snippet for enabling scheduled backups using the CloudNative PostgreSQL Operator:
    
    
    apiVersion: postgresql.cnpg.io/v1
    kind: ScheduledBackup
    metadata:
      name: backup-example
    spec:
      schedule: "0 0 0 * * *"
      backupOwnerReference: self
    cluster:
      name: pg-backup
    

#### Managed services

Managed databases like Cloud SQL have built-in backup and replication features. We recommend that you set up asynchronous replication from the primary database instance to a replica in the secondary region. To learn more, see [About replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/replication). In OpenShift, configure secrets or config maps to point to the correct database connection strings for each cluster.

Because asynchronous replication results in a non-zero RPO, there's a potential for loss of the most recent data writes. You must design your application to mitigate against data loss. Alternatively, consider using another replication method.

We also recommend that you enable Cloud SQL automated backups. To learn more, see [Create and manage on-demand and automatic backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backing-up).

### Failover process

In the event of primary cluster failure, Cloud DNS automatically redirects traffic to the secondary regional cluster based on health checks and failover policies.

When the secondary cluster is promoted from a read replica to a primary, it takes over as an active site and serves production traffic. This promotion is necessary to be able to accept database writes.

To set up DR for Cloud SQL, follow the steps described in the [Google Cloud SQL disaster recovery documentation](https://docs.cloud.google.com/sql/docs/postgres/intro-to-cloud-sql-disaster-recovery#dr-architecture). Using asynchronous database or storage replication causes a non-zero RPO to help to ensure that your application can tolerate loss of most recent writes. Alternatively, consider using another replication method.

### Secure secret management

Secrets like database passwords, API keys, and TLS certificates are important aspects of DR. You must be able to restore these secrets securely and reliably in a new cluster.

Common approaches to secret management are as follows:

  * **Use external secrets** : Use a tool like the [external secrets operator](https://docs.openshift.com/container-platform/4.17/nodes/pods/nodes-pods-secrets-store.html#secrets-store-google_nodes-pods-secrets-store) to pull secrets from Google Secret Manager.
  * **Backup secrets with OADP Operator** : If you don't use an external store, ensure that secrets are included in your backups.
  * **Regular rotation** : Rotate secrets regularly and ensure your secret management strategy accommodates DR scenarios.
  * **Testing** : Test secret restoration in a staged environment to confirm that all services can start with the provided credentials.
  * **Validation** : Validate that your DR cluster has the necessary IAM roles or authentication methods to retrieve secrets from external stores.



### Networking and traffic management

Use Google Cloud's Global External HTTPS Load Balancer as the primary ingress point to distribute traffic between multiple OpenShift clusters (for example, primary and secondary clusters). This global service directs user requests to the appropriate backend cluster based on proximity, health, and availability.

To connect the Global Load Balancer to your OpenShift clusters, you can use either of the following approaches:

  * **Use regional load balancers (internet NEGs)** : Configure Google Cloud internet network endpoint groups (NEGs) to point to the external IP addresses of the Regional Load Balancers exposing each of your OpenShift clusters' ingress services (OCP Routers). The Global Load Balancer then routes traffic to these regional load balancer IPs. This approach provides an abstraction layer but involves a hop to an additional network.
  * **Direct Pod Routing (`Compute Engine_VM_IP_PORT NEGs`)**: Configure the OpenShift Ingress Controller integration to use Google Cloud Network Endpoint Groups (NEGs) of type Compute Engine_VM_IP_PORT. This approach allows the Global Load Balancer to target the OpenShift Ingress Controller (Router) pods directly using their internal PodIP:TargetPort. This method bypasses the extra hop and additional node proxying. It typically results in lower latency, and enables more direct health checking from the global load balancer.



Both setups allow the Global Load Balancer to manage traffic distribution effectively across clusters in different regions. To learn more, see [Set up a global external Application Load Balancer with an external backend](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-external-backend).

### VPCs

We recommend the following approaches for VPC management:

  * **Shared VPC** : Use a [Shared VPC](https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/installing_on_gcp/installing-gcp-shared-vpc) to centralize network management for both primary and secondary clusters. This approach simplifies administration and ensures consistent network policies across regions.
  * **Global Dynamic Routing** : Enable Global Dynamic Routing within your VPCs to automatically propagate routes between regions, ensuring seamless connectivity between clusters.
  * **Custom Mode VPCs** : Use custom mode VPCs and create specific subnets in the regions where your clusters run. This is often necessary for VPC-native pod networking required by methods like Compute Engine_VM_IP_PORT routing.
  * **VPC Network Peering** : If it's necessary for you to use separate VPC networks for each region and cluster, use VPC Network Peering to connect the regions and clusters.



### Subnets and IP addresses

Create regional subnets in each region to maintain network segmentation and avoid IP address conflicts.

Ensure that there are non-overlapping IP ranges between regions to prevent routing issues.

### Cross-cluster traffic with Red Hat Service Mesh

OpenShift supports Service Mesh federation, which enables communication between services deployed across multiple OpenShift clusters. This function is particularly useful for DR scenarios where services might need to communicate across clusters during failover or data replication.

To learn how to set up Service Mesh federation between primary and secondary clusters, see the [Red Hat documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/service_mesh/service-mesh-2-x#ossm-federation-overview_federation).

## Deployment

To learn how to deploy a topology based on this reference architecture, see the [Red Hat documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/installing_on_gcp/installing-gcp-default).

## What's next

  * Learn how to [implement monitoring and alerting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/monitoring/about-openshift-container-platform-monitoring#monitoring-targets-for-user-defined-projects_monitoring-stack-architecture) for cluster health, replication status, backup success, and application performance in both primary and secondary environments.
  * Learn how to [install OpenShift on Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/installing_on_google_cloud/index).
  * Learn more about [Red Hat solutions on Google Cloud](https://cloud.google.com/solutions/redhat).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

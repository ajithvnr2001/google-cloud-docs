---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/db-self-managed-oracle-ref-arc/
title: Self-managed Oracle database reference architecture \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:50:01.931213+00:00
---

# Self-managed Oracle database reference architecture  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/db-self-managed-oracle-ref-arc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Self-managed Oracle database reference architecture Stay organized with collections  Save and categorize content based on your preferences. 

This reference architecture provides a conceptual framework for deploying and operating self-managed Oracle databases on Google Distributed Cloud (GDC) air-gapped. This solution lets you maintain critical database workloads by using the official [Oracle Database Operator for Kubernetes](https://github.com/oracle/oracle-database-operator) on [standard clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-standard-cluster).

The architecture focuses on enabling a Bring-Your-Own-License (BYOL) model, allowing you to deploy standardized, secure, and highly available databases within isolated environments. It covers the full lifecycle from provisioning and networking to production-grade operations like high availability, backup, restore, and observability.

**Important:** This solution will be fully managed by yourself, as the customer, and not by Google engineering.

### Features and capabilities

The solution provides several core functional components for database management:

  * **Automated lifecycle management** : Use the Oracle Database Operator to automate provisioning, cloning, patching, and configuration of Single Instance Databases (SIDB).
  * **High availability** : Integrated support for Oracle Data Guard to provide synchronous or asynchronous replication and automated failover capabilities. High availability is supported within a single zone.
  * **Persistent storage integration** : Seamlessly utilize GDC existing [standard-rwo](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/access-persistent-storage) storage classes for database files to ensure data durability.
  * **Secure image management** : Support for mirroring Oracle container images from the [Oracle Container Registry](https://container-registry.oracle.com/) to local Harbor registries, including integrated [vulnerability scanning](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/scan-vulnerabilities).
  * **Unified observability** : Built-in mechanisms for exporting database metrics to Prometheus and forwarding alert logs using sidecar patterns.
  * **Flexible networking** : Support for internal and external L4 Load Balancers to expose database endpoints securely.



### Architectural principles

  * **Self-managed approach** : Provides the architectural framework for deploying and managing Oracle workloads.
  * **Cloud-native operations** : Uses the operator pattern to manage stateful workloads, ensuring consistency across different environments.
  * **Database-aware resiliency** : Prioritizes database-level replication (Data Guard) over infrastructure-level replication to ensure logical consistency and faster recovery.
  * **Security-focused design** : Adheres to air-gapped requirements by using local registries, mandatory image scanning, and explicit network policies for all database traffic.



## Architecture

The architecture illustrates the relationship between the GDC standard cluster, the Oracle Database Operator, the SIDB resources, and the supporting infrastructure like Harbor.

![Self-managed Oracle database architecture diagram.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/solutions/images/dbs-managed-oracle-overview.png)

## Concepts and technologies

This section details the functional components, their responsibilities, and how they communicate within the system.

### Infrastructure and platform

  * **GDC standard cluster** : The primary compute environment where the Oracle Operator and database pods reside.
  * **Harbor Registry** : The secure, local source of truth for all container images. It provides automated scanning to ensure images are free from known vulnerabilities.
  * **Persistent storage** : GDC standard-rwo storage classes provide the underlying block storage required for Oracle data files, redo logs, and control files using a PersistentVolumeClaim.



### Services and logic

  * **Oracle Database Operator** : The controller responsible for watching custom resources like `SingleInstanceDatabase` and `DataguardBroker`. It reconciles these into standard Kubernetes objects, including StatefulSets for database pods and services for networking.
  * **Single Instance Database (SIDB)** : A containerized deployment using the Oracle multi-tenant architecture (CDB/PDB). You can deploy multiple distinct SIDB instances or consolidate workloads by creating multiple Pluggable Databases (PDBs) within a single SIDB.
  * **Data Guard Broker** : Orchestrates role transitions between primary and standby instances. It manages the database role labels, for example `database.oracle.com/role: primary`, used by Kubernetes services to route traffic correctly after a failover.
  * **L4 Load Balancer** : Provides stable IP addresses for database connectivity.



### Data flow and interfaces

  * **SQL*Net (Port 1521)** : The primary protocol for application connectivity.
  * **Observability exporter** : Exposes a `/metrics` endpoint for Prometheus.
  * **Alert logs** : Standard database alert logs are sent to `stdout` for collection by the GDC logging agent.
  * **RMAN channels** : Used by `CronJob` resources to stream backups to S3-compatible object storage.



## Considerations

  * **Scalability and performance** : 
    * Worker nodes must be sized with a minimum of 8 vCPUs and 32 GiB RAM for production workloads.
    * Using `nodeSelector` or taints and tolerations is a best practice to dedicate specific nodes to database workloads.
    * Performance is heavily dependent on the underlying storage; using `standard-rwo` with high IOPS is recommended.
  * **Resource management and licensing** : 
    * This solution follows a Bring-Your-Own-License (BYOL) model.
    * Advanced features like Transparent Data Encryption (TDE), Advanced Compression, and Active Data Guard (read-only standby) require specific Enterprise Edition licenses.
    * The Oracle Database Free edition can be used for development and testing.
  * **Availability and reliability** : 
    * High availability is achieved through single-zone Data Guard configurations where primary and standby instances reside in the same namespace.
    * Using a Service with a selector for the `primary` role label ensures seamless client redirection during failover without client-side changes.
    * For data protection, the solution uses RMAN for backups to an S3-compatible bucket.
  * **Operational management** : 
    * While the operator simplifies deployment, day-to-day operations like tuning and complex restores still benefit from database administration expertise.
    * The use of a sidecar container is recommended for forwarding detailed trace and audit logs that are not sent to `stdout`.



## Design decision

The primary architectural choices for this solution focus on balancing automation with the constraints of an air-gapped environment.

### Data Guard versus storage-level replication

Data Guard is the high-availability mechanism because it is database-aware. This approach protects against logical corruption and ensures zero data loss in maximum availability mode by validating blocks before they are written to the standby. While this requires additional licensing for Enterprise Edition and more setup overhead than volume snapshots, it provides the required consistency for refinement workloads.

### Service management for load balancers

By default, setting the `loadBalancer: true` parameter in the `SingleInstanceDatabase` specification automatically creates an external load balancer service. For an internal load balancer, a separate service resource must be created manually to include the necessary `networking.gke.io/load-balancer-type: "Internal"` annotation. This manual approach provides declarative control over annotations and labels that the default operator-managed service may not expose.

### Observability strategy of sidecars for logs

The solution recommends using sidecar containers for log forwarding. This decouples log collection from the main database process, ensuring that heavy logging volume does not impact database performance. While this increases the resource footprint per database pod, it ensures reliable telemetry collection without affecting database stability.

## Assumptions and limitations

### Assumptions

  * The environment has a pre-configured and accessible Harbor instance for image hosting.
  * Cert-manager comes pre-installed on the standard cluster to handle the operator's webhook certificates.
  * An S3-compatible object store is available for RMAN backup targets.



### Limitations

  * **Single-zone HA** : High-availability configurations are supported within a single zone.
  * **No Oracle RAC** : Support for Real Application Clusters (RAC) is not included; the solution focuses on Single Instance and Data Guard.
  * **Standard clusters only** : The solution is validated for GDC standard clusters and is not supported on shared user clusters.



## What's next

  * [Deploy self-managed Oracle databases](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/db-deploy-self-managed-oracle)
  * [Deploy highly-available self-managed Oracle databases](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/db-deploy-ha-self-managed-oracle)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/postgres-db-architecture/
title: PostgreSQL database reference architecture on GDC air-gapped \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:13.536125+00:00
---

# PostgreSQL database reference architecture on GDC air-gapped  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/postgres-db-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  PostgreSQL database reference architecture on GDC air-gapped Stay organized with collections  Save and categorize content based on your preferences. 

This reference architecture provides a conceptual framework for deploying and operating customer-managed [PostgreSQL](https://www.postgresql.org/) databases on Google Distributed Cloud (GDC) air-gapped. This solution enables organizations to maintain critical database workloads by leveraging a highly available (HA), multi-zone cluster deployed on virtual machines.

The architecture focuses on a resilient 3-node configuration that ensures database availability even in the event of a single zone or infrastructure failure. It covers the full lifecycle from automated provisioning and networking to production-grade operations like high availability, backup, restore, and observability.

### Features and capabilities

The solution provides several core functional components for database management:

  * Automated high availability: Use [Patroni](https://github.com/patroni/patroni) and [etcd](https://etcd.io/) to provide automatic leader election and failover, ensuring the database remains operational without manual intervention.
  * Multi-zone resiliency: Distribute database nodes across three distinct availability zones to protect against localized hardware or infrastructure outages.
  * Standardized automation: Provision the entire stack using Ansible-based playbooks with [Autobase](https://github.com/vitabaks/autobase) to ensure repeatable and consistent deployments.
  * Connection pooling: Integrated [PgBouncer](https://www.pgbouncer.org/) service to manage high connection counts and stabilize resource consumption on the database nodes.
  * Global load balancing: Use the platform-managed [Global L4 Load Balancer](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/expose-services) to provide a single, stable virtual IP (VIP) that is accessible across all zones.
  * Air-gapped readiness: Specialized workflows for packaging all required operating system dependencies and binaries for deployment in disconnected environments.
  * Data protection: Leverage standard tools such as `pg_dump` and `pg_basebackup` alongside GDC storage snapshots to maintain a robust backup and recovery strategy.



## Architecture

The architecture consists of a three VM environment distributed across three availability zones that run a colocated stack of services.

![Three VM architecture that runs a colocated stack of services.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/solutions/images/postgre-diagram.png)

### Architectural principles

  * Majority-based consensus: Uses a quorum-based model where a majority of nodes (2 out of 3) must agree on the cluster state, preventing "split-brain" scenarios and ensuring data integrity.
  * Separation of concerns: Each VM runs a colocated but distinct stack of services (database, HA manager, consensus, and pooler) to provide a self-contained and resilient node.
  * Database-aware failover: Prioritizes database health metrics with Patroni's REST API to coordinate traffic redirection through the platform load balancer.
  * Infrastructure as code: Relies on automated playbooks for all configuration tasks, reducing the risk of human error during deployment and scaling.



## Concepts and technologies

This section details the functional components, their responsibilities, and how they communicate within the system.

### Infrastructure and platform

  * Virtual Machines (VMs): Dedicated compute instances distributed across zones to host the database stack.
  * Global L4 Load Balancer: A platform-managed service providing a stable virtual IP (VIP) that routes traffic to the current cluster leader.
  * Persistent storage: High-performance SSD-backed storage is required to meet the strict latency requirements for the consensus layer's write-ahead logs.



### Services and logic

  * PostgreSQL 17: The core relational database engine responsible for data persistence and query execution.
  * Patroni: The high availability manager that monitors the local PostgreSQL process and coordinates leader elections using etcd.
  * etcd: The distributed configuration store that provides the consensus layer and holds the authoritative state of the cluster.
  * PgBouncer: A lightweight connection pooler that sits in front of PostgreSQL to handle incoming application connections efficiently.



### Data flow and interfaces

  * PgBouncer (Port 6432): The primary entry point for application database traffic.
  * Patroni API (Port 8008): An HTTPS REST interface used by the load balancer to perform health checks and identify the current leader using the `/primary` endpoint.
  * etcd (Port 2379): The communication channel for the consensus cluster to maintain state and perform elections.



## Considerations

  * Scalability and performance: 
    * Database nodes should be sized based on workload, with a minimum of 2 vCPUs and 8 GiB RAM. Production workloads typically start at 8 vCPUs and 32 GiB.
    * Performance relies on low-latency storage; SSDs are required to ensure etcd can process data syncs in under 10ms.
    * Synchronous replication: The overhead of synchronous replication depends directly on inter-zone network latency. To ensure optimal performance for zero-data-loss configurations, low inter-zone latency is required.
  * Resource management and licensing: 
    * This solution relies on free, open-source database components.
    * [Autobase](https://github.com/vitabaks/autobase) is used as the reference automation tool to streamline the installation and configuration of the HA stack. However, the architecture is not exclusively tied to Autobase, and the underlying open-source components can be managed using custom pipelines.
    * For organizations requiring formal support for the automation package, [third-party paid support](https://autobase.tech/docs/support) is available.
    * Connection pooling with PgBouncer is essential to prevent CPU and memory exhaustion caused by high user connection counts.
  * Availability and reliability: 
    * High availability is achieved through a 3-node quorum. The failure of any single node or zone does not interrupt the service.
    * Cluster stability: Maintaining a reliable quorum requires low network latency between nodes. Average round-trip times (RTT) should ideally be under 10ms to prevent election timeouts and cluster instability.
  * Operational management: 
    * Routine tasks such as minor version patching and major upgrades remain the responsibility of the customer's operations team.
    * Outputs from the VMs' `stdout` are automatically ingested into the GDC air-gapped monitoring platform. A guide will be published in the future on how to integrate more detailed monitoring for the individual components.
    * A robust backup strategy should be implemented using database-native tools and platform snapshots. Detailed guides for these procedures will be published separately.



## Design decision

The architectural choices for this solution provide a resilient path for multi-zone deployments.

### Virtual machines over Kubernetes

A VM-based approach was selected to provide multi-zone high availability. GDC doesn't support Kubernetes clusters that span multiple physical zones. Therefore, deploying dedicated VMs into separate zones is necessary to achieve a robust cross-zone architecture. This configuration can survive the total failure of a single infrastructure zone.

### Platform-native global load balancing

The architecture leverages the GDC Global L4 Load Balancer instead of software-based proxies on the VMs. This approach provides several advantages:

  * Global reach: Provides a stable virtual IP that is accessible across all zones.
  * Platform managed: The VIP is managed independently by the platform's control plane.
  * Simplified failover: Failover is managed through standard health-check probes rather than complex local software configurations.
  * High availability: Removing reliance on local proxies ensures that the entry point for database traffic remains resilient.



## Assumptions and limitations

### Assumptions

  * The environment has a local registry or mechanism to import packaged OS dependencies and binaries.
  * Key-based SSH access is available to all target VMs for Ansible-based automation.
  * The project has sufficient quota for multi-zone VM and Load Balancer provisioning.



### Limitations

  * Manual maintenance: Operating system patching and PostgreSQL version upgrades are manual tasks and are not automated by the solution.
  * Storage sensitivity: The consensus layer (etcd) is highly sensitive to disk latency. Sustained high storage contention can impact the stability of the consensus layer.
  * Network stability: The high availability manager relies on consistent, low-latency network connectivity between zones. Delays or network jitter can influence the timing of cluster coordination and role transitions.



## Additional materials

  * Reference automation code repository: [Autobase Source Code on GitHub](https://github.com/vitabaks/autobase)
  * [PostgreSQL database reference implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/postgres-db-implementation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

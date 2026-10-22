---
url: https://docs.cloud.google.com/alloydb/omni/docs/overview/
title: AlloyDB Omni overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:11:10.968290+00:00
---

# AlloyDB Omni overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/omni/docs/overview)



Send feedback 

#  AlloyDB Omni overview Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB Omni is a downloadable database software package that lets you deploy a streamlined version of [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview) in computing environments that you manage. AlloyDB Omni and the fully managed AlloyDB service on Google Cloud share the same core components. AlloyDB uses a cloud-native disaggregated storage layer, while AlloyDB Omni is deployed on the storage of your choice.

AlloyDB Omni's portability lets you run it in many environments, including the following:

  * Your private data centers
  * Any public cloud
  * Your laptop
  * Cloud-based VM instances



AlloyDB Omni offers several enhancements—in addition to standard PostgreSQL—that support scalability, availability, reliability, performance, AI, and natural language. For more information, see [AlloyDB Omni additions to standard PostgreSQL](https://docs.cloud.google.com/alloydb/omni/docs/additions-to-postgresql).

## AlloyDB Omni use cases

AlloyDB Omni is well-suited to the following scenarios:

  * You need a scalable, high-performance version of PostgreSQL that you must run on-premises due to regulatory or data sovereignty requirements.
  * You need a database that continues to run even when it's disconnected from the internet.
  * You want to migrate away from a legacy database without committing to a fully managed cloud service like AlloyDB for PostgreSQL.

**Note:** AlloyDB Omni is a downloadable version of AlloyDB for PostgreSQL, and is self-managed. To upgrade to the fully managed database version, you can choose to migrate your AlloyDB Omni database to AlloyDB for PostgreSQL using any PostgreSQL-supported migration methods, including third-party tools such as Striim.

## Key features

  * A 100% PostgreSQL-compatible database server.
  * Support for AlloyDB AI, which helps you build enterprise-grade generative AI applications using your operational data.
  * Integrations with the Google Cloud AI ecosystem including the [Vertex AI Model Garden](https://cloud.google.com/model-garden) and open-source generative AI tools.
  * Support for autopilot features from AlloyDB for PostgreSQL in Google Cloud that lets AlloyDB Omni self-manage and self-tune.

For example, AlloyDB Omni supports automatic memory management and adaptive autovacuum of stale data.

  * The AlloyDB Omni columnar engine, which keeps relevant data in an in-memory columnar format for faster analytical queries, reporting, and hybrid transactional and analytical processing (HTAP) workloads.

  * The AlloyDB Omni web user interface, which enables graphical telemetry monitoring and configuration audits for your self-managed clusters.




In performance tests, transactional workloads in AlloyDB Omni are more than 2X faster, and analytical queries are up to 100X faster, than standard PostgreSQL.

## AlloyDB Omni deployment choices

In the Google Cloud console, you can explore deployment options, access learning resources, and manage licenses directly from the **AlloyDB Omni** landing page:

[Go to AlloyDB Omni](https://console.cloud.google.com/alloydb/omni)

The console landing page features two primary tabs:

  * **Deployment options** : Provides tailored paths and guides for installing AlloyDB Omni across different infrastructure environments, along with access to codelabs and AI demos.
  * **Subscriptions** : Centralizes license management for production deployments. You can calculate and purchase licenses based on total vCPU count, scale vCPUs, view costs, and manage commitment discounts.



You can install AlloyDB Omni using one of the following deployment options:

![Deployment options for AlloyDB Omni](https://docs.cloud.google.com/static/alloydb/omni/docs/images/alloydb-omni-deployment-options.png)

  * AlloyDB Omni using containers: a [standalone database container](https://docs.cloud.google.com/alloydb/omni/containers/17-next/docs/overview). Run AlloyDB Omni on a Linux system with SSD storage and at least 8GB of memory per CPU.

  * [AlloyDB Omni using the container orchestrator](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/overview): part of a container in a Kubernetes environment. The AlloyDB Omni Kubernetes operator is an extension to the Kubernetes API that lets you run AlloyDB Omni in most CNCF-compliant Kubernetes environments.

The AlloyDB Omni operator simplifies basic database operations, which lets you automate single or high availability (HA) deployments and day-2 operations like backup, restore, failover, and setting up cross-region disaster recovery (DR).

  * [AlloyDB Omni using RPM](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/overview): a standalone package that runs directly in a VM or bare metal. AlloyDB Omni using RPM runs as a set of integrated software components directly on the host operating system. It uses the standard Linux file system for storage, letting you use your existing storage infrastructure and management practices.

  * [AlloyDB Omni using the RPM orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/overview) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)): a Red Hat Package Manager (RPM) deployment for VMs or bare-metal servers. This option includes an orchestration platform that automates deployment and management in non-Kubernetes environments. It extends cloud-like flexibility to your choice of infrastructure, without requiring containerization layers like Docker.




Your applications connect to and communicate with your AlloyDB Omni database, as applications connect to and communicate with a standard PostgreSQL database server. User access control also relies on PostgreSQL standards.

You can configure the AlloyDB Omni database behavior using database flags, including logging, vacuuming, and the columnar engine. For more information, see [Available AlloyDB Omni download and installation options](https://docs.cloud.google.com/alloydb/omni/docs/available-download-install-options).

### AlloyDB Omni as a container

Google distributes AlloyDB Omni as a container that you can run with container runtimes such as Docker and Podman. You can also deploy AlloyDB Omni containers in a Kubernetes environment with many basic operations automated.

Operationally, containers offer the following advantages:

  * Transparent dependency management: all necessary dependencies are bundled in the container and tested by Google to ensure that they are fully compatible with AlloyDB Omni.
  * Portability: you can expect AlloyDB Omni to operate consistently across environments.
  * Security isolation: you choose what the AlloyDB Omni container has access to on the host machine.
  * Resource management: you can define the amount of compute resources that you want the AlloyDB Omni container to use.
  * Seamless patching and upgrades: to patch a container, replace the existing image with a new one.



### AlloyDB Omni in a RHEL environment

AlloyDB Omni provides two deployment options for a RHEL environment, which depend on your automation and scaling requirements.

#### AlloyDB Omni using RPM

The RPM deployment option is a standalone Red Hat Package Manager (RPM) installation designed for environments when you want a non-containerized AlloyDB Omni database. This option supports RHEL 9 and Rocky Linux 9.

  * Direct OS integration: runs as a set of integrated software components directly on the host operating system (OS).
  * Existing storage: uses the standard Linux file system (ext4 and xfs), which supports existing storage infrastructure and management practices.
  * Simplicity: well-suited for single-instance setups where deep integration with the host OS is required, without additional orchestration layers.



#### The RPM orchestrator

The RPM orchestrator deployment option ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) uses the same RPM packages as AlloyDB Omni using RPM, but adds an orchestration platform to automate management in non-Kubernetes environments.

  * Cloud-like flexibility: extends automation to on-premises infrastructure, handling bootstrapping, failover, and lifecycle management.
  * Automation frameworks: integrates with popular tools like Ansible, allowing teams to use existing skill sets. You can also use purpose-built command line tools.
  * Enterprise features: specifically designed to support high availability (HA) and disaster recovery (DR) through a centralized cluster manager.



## Data backup and disaster recovery

AlloyDB Omni features a continuous backup and recovery system that lets you create a new database cluster based on any point in time within an adjustable retention period. This lets you recover from data-loss accidents.

In addition, AlloyDB Omni can create and store complete backups of your database cluster's data, either on demand or on a regular schedule. At any time, you can restore from a backup to an AlloyDB Omni database cluster that contains all the data from the original database cluster at the time the backup was created.

As a further method of disaster recovery, you can achieve cross-data-center replication by creating secondary database clusters in separate data centers. AlloyDB Omni asynchronously streams data from a designated primary database cluster to each of its secondary clusters. Whenever needed, you can promote a secondary database cluster into a primary AlloyDB Omni database cluster.

## AlloyDB Omni components

AlloyDB Omni consists of two sets of architecture components: PostgreSQL components with AlloyDB Omni enhancements and AlloyDB Omni-specific components.

The following diagram shows both sets of components, including the infrastructure layer that the components reside in, and features for each component.

![Architecture of AlloyDB Omni, showing AlloyDB for PostgreSQL-specific and PostgreSQL components.](https://docs.cloud.google.com/static/alloydb/omni/docs/images/alloydb-omni-architecture.png)

### Data storage

AlloyDB Omni stores data in fixed-size pages that are stored in the underlying file system. When a query needs to access data, AlloyDB Omni first checks the buffer pool. If the pages that hold the required data aren't found in the buffer pool, then AlloyDB Omni reads the required pages from the file system.

Accessing data from the buffer pool is significantly faster than reading from the file system. Maximizing the buffer pool size for the data an application accesses is an important factor. You can optionally add an ultra-fast cache layer to further enhance query performance.

### Resource management

AlloyDB Omni uses automatic dynamic memory management to let the buffer pool grow and shrink dynamically within configured bounds depending on the memory demands of the system. Therefore, there is no need to tune the buffer pool size. When you diagnose performance issues, first consider metrics like the buffer pool hit rate and the read rate to determine if your application is benefiting from the buffer pool. If not, that indicates that the application's dataset doesn't fit in the buffer pool, and you might consider resizing to a larger machine with more memory.

The process of retrieving, filtering, aggregating, sorting, and projecting data all require CPU resources on the database server. To reduce the amount of CPU resources required for this process, minimize the amount of data to manipulate. Monitor the CPU utilization on the database server to ensure the steady-state utilization is around 70%. This amount leaves sufficient headroom on the server for spikes in utilization or changes in access patterns over time. Running at closer to 100% utilization introduces overhead due to process scheduling and context switching and might create bottlenecks in other parts of the system. High CPU utilization is another key metric to use when making decisions about machine specifications.

Input/Output Operations Per Second (IOPS) is an important factor in database application performance, measuring how many input or output operations per second the underlying storage device can deliver to the database. To avoid exceeding the IOPS limits of database storage, minimize reads and writes to storage. Maximize the amount of data that fits in the buffer pool or in the cache layer.

### Columnar engine

The built-in columnar engine accelerates analytical query processing that typically involves full table scans, complex joins, and aggregates.

  * **In-memory column store** : contains table and materialized-view data for selected columns in a column-oriented format. By default, the column store consumes 30% of available memory. To change the amount of memory usable by the column store, set the `google_columnar_engine.memory_size_in_mb` parameter in the `postgresql.conf` used by your AlloyDB Omni instance.

  * **Columnar query planner and execution engine** : supports the use of the column store in queries.




For more information, see [About the AlloyDB for PostgreSQL columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about).

### Automatic memory management

The automatic memory manager continuously monitors and optimizes memory consumption across an entire AlloyDB Omni instance. When you run your workloads, this module adjusts the shared buffer cache size based on memory pressure.

By default, the automatic memory manager sets the upper limit to 80% of system memory and allocates 10% of system memory for the shared buffer cache. To change the upper limit for the size of the shared buffer cache, set the `shared_buffers` parameter in the `postgresql.conf` used by your AlloyDB Omni instance.

### Adaptive autovacuum

Adaptive autovacuum analyzes operations based on the database workload and automatically adjusts the frequency of vacuuming. This automatic adjustment helps the database maintain optimal performance, even as the workload changes, without interference from the vacuum process.

Adaptive autovacuum uses the following factors to determine the frequency and intensity of vacuuming operations:

  * Size of the database
  * Number of dead tuples in the database
  * Age of the data in the database
  * Number of transactions per second versus estimated vacuum speed
  * Resource utilization



### AI/ML worker

In AlloyDB Omni, the AI/ML background worker provides the capabilities necessary for calling Vertex AI models directly from the database. The AI/ML worker runs as a process called `omni ml worker`.

### The web UI

The optional web UI is a self-managed web console that gives you observability into your database instances.

This interface maps graphical dashboards for custom features—like the columnar engine and model endpoint integrations—that typical open-source PostgreSQL visualizers can't track.

Complete the following optional setups to install and connect to the web UI:

  * [Install using containers](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install-web-ui)
  * [Install using the container orchestrator](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/install-web-ui)
  * [Install using RPM](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/install-web-ui)
  * [Install using the RPM orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-web-ui)



### Orchestrator control plane

The RPM orchestrator deployment option uses a centralized cluster manager to automate cluster-wide operations, including bootstrapping and failover.

### Management interfaces

The RPM orchestrator deployment option provides a command-line utility (`alloydbctl`) and Ansible roles to let you manage one or more clusters at scale.

### Performance optimization

The RPM orchestrator deployment option includes integrated support for PgBouncer for connection pooling and HAProxy for load balancing across read-write and read-only endpoints.

## What's next

  * [Choose an AlloyDB Omni deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment).

  * Get started with the following AlloyDB Omni deployment options:

    * [AlloyDB Omni using containers](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/overview)
    * [AlloyDB Omni using the container orchestrator](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/overview)
    * [AlloyDB Omni using RPM](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/overview)
    * [AlloyDB Omni using the RPM orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/overview)
  * Learn how to install and connect to the web UI:

    * [Install using containers](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install-web-ui)
    * [Install using the container orchestrator](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/install-web-ui)
    * [Install using RPM](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/install-web-ui)
    * [Install using the RPM orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-web-ui)
  * [Manage AlloyDB Omni subscriptions in the Google Cloud console](https://console.cloud.google.com/alloydb/omni/subscriptions).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 

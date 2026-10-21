---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/SelfManagedMySQLArchitecture/
title: MySQL database reference architecture on GDC air-gapped \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:30:09.861718+00:00
---

# MySQL database reference architecture on GDC air-gapped  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/SelfManagedMySQLArchitecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  MySQL database reference architecture on GDC air-gapped Stay organized with collections  Save and categorize content based on your preferences. 

This reference architecture provides a conceptual framework for deploying and operating highly available, customer-managed _MySQL 8.4_ databases on Google Distributed Cloud (GDC) air-gapped. It enables enterprise and early access customers to reliably maintain critical database workloads using a robust, multi-zone virtual machine (VM) setup.

Because GDC air-gapped lacks support for cross-zone Kubernetes stretch clusters, this architecture relies strictly on dedicated VMs deployed across three availability domains to ensure continuous operations and withstand a full zone failure without data loss.

### Features and capabilities

  * **Multi-zone resiliency:** A highly resilient 3-node configuration deployed across three distinct availability zones to protect against single infrastructure zone failures.
  * **Automated high availability and consensus:** Uses _Group Replication_ for Paxos-based consensus clustering, providing automatic failure detection, node agreement, and global data synchronization without split-brain scenarios.
  * **Intelligent traffic routing:** Co-located _MySQL Router_ instances manage connection routing. The router directs write operations (for example, port 6446) strictly to an active primary node and load-balances read operations (for example, port 6447) across synced replicas.
  * **Global load balancing:** Integrates with the built-in _GDC Global L4 Load Balancer_ to provide a single, stable Virtual IP (VIP) for client applications, abstracting the underlying node topology.



### Architectural principles

  * **Quorum-based consensus:** Prioritizes strict data consistency. Group Replication enforces a Paxos-based model requiring majority agreement, eliminating the risk of data loss or split-brain during network partitions.
  * **Separation of concerns:** Decouples the database engine and consensus layer (Group Replication) from the client traffic routing layer (MySQL Router), while simplifying cluster lifecycle management using MySQL Shell.
  * **Infrastructure optimization:** Specifically designed for air-gapped environments, utilizing robust VMs to bypass current Kubernetes networking limitations.



## Architecture

![Three VM architecture that runs a colocated stack of services.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/solutions/images/mysql-diagram.png)

### Concepts and technologies

This section details the functional components and their specific responsibilities within the multi-zone architecture.

#### Infrastructure and platform

  * **Virtual Machines (VMs):** Three dedicated Compute instances, each deployed into a separate availability zone to form the failure domain boundaries.
  * **GDC Global L4 Load Balancer:** A platform-managed networking construct that exposes a stable internal VIP, automatically evaluating MySQL Router health checks to redirect inbound traffic.



#### Services and logic

  * **MySQL 8.4:** The core relational database engine.
  * **Group Replication / InnoDB Cluster:** The built-in clustering framework responsible for multi-master replication and verifying node quorum using Paxos.
  * **MySQL Shell:** The unified command-line interface used specifically to configure, provision, and administer the InnoDB cluster instances.
  * **MySQL Router:** Acts as the traffic router on each VM. Configured dynamically to listen to the cluster metadata and forward traffic: active/backup for writes and round-robin for reads.



#### Data flow and interfaces

  1. Applications send database requests to the _GDC Global L4 Load Balancer VIP_.
  2. The Load Balancer proxies the connection to a healthy _MySQL Router_ instance on one of the VMs.
  3. Based on the requested port, MySQL Router dynamically forwards traffic: _Port 6446_ strictly targets the active node for writes, while _Port 6447_ cycles reads across the cluster.



## Considerations

  * **Performance vs. consistency trade-offs:** Because Group Replication enforces consensus, transactions require acknowledgment from cluster peers. Performance directly correlates to the inter-zone network latency within the GDC environment.
  * **Resource management:** Deploying MySQL Router directly on the database VMs optimizes hardware utilization but requires careful resource tuning to prevent connection pooling overhead from starving the core MySQL processes.



## Design decision

  * **Virtual machines over Kubernetes:** GDC air-gapped does not support Kubernetes clusters that span multiple physical zones. A VM-based approach was strictly chosen because deploying dedicated VMs across separate zones is the only viable method to achieve true multi-zone high availability and survive a total zone failure.
  * **InnoDB Cluster vs. Orchestrator and ProxySQL:** A traditional primary/secondary architecture paired with ProxySQL and Orchestrator was evaluated as a feasible alternative. However, the built-in _InnoDB Cluster_ (Group Replication + MySQL Router + MySQL Shell) was selected instead because it eliminates reliance on third-party routing overlays and drastically simplifies the operational complexity around failovers by keeping the consensus directly within MySQL.
  * **Platform built-in global load balancing:** Leveraging the built-in GDC Global L4 Load Balancer ensures that the VIP is controlled by the GDC control plane, keeping the entry point resilient and simplifying cross-zone traffic delivery.



## Assumptions and limitations

### Assumptions

  * **Availability of infrastructure:** Customers have sufficient project quota to provision dedicated, properly sized VMs and Global Load Balancers distributed evenly across three availability zones.
  * **Secure networking:** Key-based access and proper ProjectNetworkPolicies (PNPs) are established to permit intra-cluster Group Replication synchronization and MySQL Router traffic.



### Limitations

  * **Kubernetes unsupported:** Customers strictly seeking containerized/Kubernetes-based solutions cannot achieve multi-zone HA until stretch clusters are fully supported by the platform.
  * **Manual upgrades required:** Unlike managed services, this solution places the responsibility of routine OS-level patching and database minor version upgrades entirely on the customer.
  * **Network latency sensitivity:** Replication demands a high-quality, stable network. Network jitter or latency spikes between the air-gapped zones will proportionally delay write operations across the MySQL cluster.



## Additional materials

  * **Solution Reference Implementation (SRI):** [Solution Reference Implementation for Highly-Available, Multi-Zone MySQL 8 in GDC air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/SelfManagedMySQLImplementation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

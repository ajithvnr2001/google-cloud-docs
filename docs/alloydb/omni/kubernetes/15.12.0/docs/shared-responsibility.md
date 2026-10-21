---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/shared-responsibility/
title: AlloyDB Omni shared responsibility \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.12.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:14:02.568780+00:00
---

# AlloyDB Omni shared responsibility  |  AlloyDB Omni for Kubernetes: 15.12.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/shared-responsibility/

This page documents AlloyDB Omni version **15.12.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/resources)



Send feedback 

#  AlloyDB Omni shared responsibility Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.12.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/shared-responsibility)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/shared-responsibility)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/shared-responsibility)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/shared-responsibility)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/shared-responsibility)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/shared-responsibility)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/shared-responsibility)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/shared-responsibility)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/shared-responsibility)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/shared-responsibility)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/shared-responsibility)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/shared-responsibility)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/shared-responsibility)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/shared-responsibility)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/shared-responsibility)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/shared-responsibility)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/shared-responsibility)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/shared-responsibility)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/shared-responsibility)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/shared-responsibility)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/shared-responsibility)

This page describes what you, as an AlloyDB Omni customer, are responsible for, and what Google is responsible for. 

As an AlloyDB Omni customer, you are responsible for configuring and operating AlloyDB Omni to make sure that your workloads get the most value from the service.

Layer | Google's responsibility | Customer responsibility  
---|---|---  
**Hardware and host** | Physical infrastructure | Provide minimum and recommended requirements (if applicable) | Provision physical servers, VMs, or edge devices like power, cooling, and hardware.  
| Host operating system (OS) | Provide minimum and recommended requirements (if applicable) | Manage the Linux kernel, apply OS security patches, and harden the host nodes.  
**Kubernetes** | Cluster management | Provide minimum and recommended requirements (if applicable) | Manage the cluster on a daily basis—including upgrades—following industry-standard best practices.  
| Storage (CSI/PV) | Provide minimum and recommended requirements (if applicable) | Provision the storage class and manage the underlying appliances. AlloyDB Omni requires a block device, so make sure to choose block device class.  
| Networking (CNI) | Provide minimum and recommended requirements (if applicable) | Provision and manage the network layer—for example, pod networking, ingress controllers, load balancers, and firewall rules between nodes.  
| Role-based access control (RBAC) | Provide the service accounts, roles, and role bindings required for the AlloyDB Omni Kubernetes operator. | Apply these role-based access control (RBAC) rules to the cluster and make sure that they align with internal security policies. To access AlloyDB Omni resources, create additional RBAC roles and role bindings.  
| Secret management | Read standard Kubernetes Secrets to provision resources, such as the initial `postgres` user. | Create, secure, and rotate Kubernetes Secrets in the cluster.  
| Certificate management | Rely on standard bare Kubernetes Secrets and `cert-manager` for certificate integration. | Install, configure, and manage the lifecycle of `cert-manager`.  
**Operator software** | Development and release | Develop the AlloyDB Omni operator logic and CRDs and publish container images, Helm charts, and OLM bundles. | None. Customers can use artifacts stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) for their deployments.  
| Installation and lifecycle | Provide documentation and upgrade artifacts. | 

  * Verify the compatibility table before installing or upgrading.
  * Follow instructions to [install](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/deploy-kubernetes) or [upgrade](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/upgrade-kubernetes-overview) AlloyDB Omni components.

  
**Database engine** | Database binary | Provide the AlloyDB container images with proprietary optimizations like the columnar engine and AI acceleration. | None.  
| Patching | Release security patches and minor and major version updates for the engine. Provide upgrade instructions. | Schedule upgrades as soon as possible, depending on the criticality of each release.  
| User management | 

  * Provision the initial AlloyDB Omni operator operator-related users.
  * Provision the user-facing `postgres` superuser using a user-provided password from a Kubernetes Secret.
  * Provide instructions to integrate with Microsoft Active Directory.

| 

  * Provide the password for the initial superuser using a Kubernetes Secret.
  * Create and manage all other roles and users.

  
**Data management** | Backups | Provide the `BackupPlan` and `Backup` CRDs and logic to manage backups, which are managed using `pgBackrest` with S3-compatible integration. | Configure backup schedules and retention, and provision the local, S3 or Cloud Storage target storage bucket.  
| High availability (HA) | Provide the auto-failover logic and healing mechanisms. | Provision sufficient nodes and zones to provide a standby target to support failover.  
| Encryption (at rest) | None. | Manage storage layer encryption to make sure that it meets your requirements.  
| Encryption (in transit) | Provide mTLS for internal operator components and to configure server-side TLS for user-to-database connections. | Connect to the database using secure TLS clients and manage the underlying certificate infrastructure.  
**Observability** | Metrics | Expose internal database metrics using a Prometheus-compatible endpoint. | Deploy and manage the scraper using Prometheus, Open Telemetry, or other compatible solutions and their storage stack. Monitor the overall health of the system.  
| Logging | Write PostgreSQL and audit logs to files on disk in the container, and rotate them. | Deploy log collectors—for example, Fluentd and Fluent Bit—to ship logs to a storage backend (like Splunk or ELK). Make sure that the log collectors are extracted to preserve logs for a recommended minimum of one month.  
| Visualization | Provide sample metrics and log dashboards to monitor standard workloads. | Deploy and monitor the health of the visualization tool, like Grafana. Create dashboards and incorporate them in your daily operational tasks.  
| Alerting | None | Manage the alerting pipeline—for example, PagerDuty integration.  
**Support** | Troubleshooting | Provide support for software bugs and engine errors. To obtain this support, you need a [license subscription](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/run-alloydb-omni-production). | Provide initial support through documentation and knowledge base. Debug infrastructure-related issues.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

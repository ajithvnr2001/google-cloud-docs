---
url: https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/overview/
title: AlloyDB Omni using RPM overview \u00a0|\u00a0 AlloyDB Omni for Linux: 17.5.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:24.239535+00:00
---

# AlloyDB Omni using RPM overview  |  AlloyDB Omni for Linux: 17.5.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/overview/

This page documents AlloyDB Omni version **17.5.0** using the **Linux** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Linux: 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/overview)



Send feedback 

#  AlloyDB Omni using RPM overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 17.5.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/overview)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/overview)



AlloyDB Omni for Linux ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) is a downloadable, self-managed version of AlloyDB for PostgreSQL, available as Red Hat Package Manager (RPM). You can install AlloyDB Omni for Linux directly onto a Red Hat Enterprise Linux (RHEL) or Red Hat-compatible environment using standard operating system package managers.

This software lets you deploy the AlloyDB engine—the same engine that powers the fully managed AlloyDB for PostgreSQL service in Google Cloud—on your own infrastructure. You can run AlloyDB Omni for Linux on your bare metal or virtual machines.

AlloyDB Omni for Linux supports RHEL 9 and Rocky Linux 9. You must have AlloyDB Omni database version 17 or later.

To get started with this deployment model, [submit this form to request access](https://forms.gle/zxuHekMtV67Bw9Av9).

## Use cases

AlloyDB Omni for Linux is designed for environments where containerization isn't preferred or where deep integration with the host operating system is required. Common use cases include the following:

  * Modernizing legacy applications: upgrade existing PostgreSQL workloads running on Linux servers to AlloyDB Omni for Linux to gain performance and manageability improvements without replatforming to containers.
  * Edge computing: deploy high-performance databases in remote data centers where resource constraints or operational models favor direct operating system (OS) installation.
  * Development and testing: give developers a powerful, local database instance that mirrors the production AlloyDB for PostgreSQL environment, enabling consistent testing and rapid iteration.
  * High database performance: experience high performance on bare metal or virtual environments.



## Benefits

AlloyDB Omni for Linux offers the following benefits:

  * Superior performance: it uses the AlloyDB for PostgreSQL columnar engine and intelligent caching to deliver faster analytical queries and higher transaction throughput compared to standard PostgreSQL.
  * Full control: it installs directly on the OS, giving system administrators complete control over resource allocation, file system configuration, and network settings using standard Linux tools.
  * 100% PostgreSQL compatibility: it is fully compatible with PostgreSQL, which lets you use existing tools, drivers, and extensions without code changes.
  * Operational simplicity: it integrates natively with RHEL systems. You can manage the database service using `systemctl` and install or update it using `dnf`, fitting seamlessly into existing Linux administration workflows.
  * Intelligent automation: to reduce administrative toil, it includes autopilot features like automatic memory management and adaptive autovacuum.
  * Automatic memory management: it dynamically adjusts the shared buffer cache based on system memory pressure, optimizing resource usage without manual tuning.



## AlloyDB Omni for Linux architecture

AlloyDB Omni for Linux runs as a set of integrated software components directly on the host operating system. It uses the standard Linux file system for storage, letting you use your existing storage infrastructure and management practices.

### Core components

The AlloyDB Omni for Linux architecture consists of the following primary RPM packages that work together to deliver the database service:

  * `alloydbomni`: this package is the core database engine. It contains the enhanced PostgreSQL server binaries, the AlloyDB for PostgreSQL columnar engine, and the autopilot management extensions. It runs as a system service (managed by `systemd`), handling client connections, query processing, and data storage.
  * `alloydbomni_monitor`: this package is a lightweight monitoring agent that runs alongside the core engine. It collects telemetry and performance metrics from the AlloyDB for PostgreSQL instance and exposes them over the Prometheus protocol for observability tools.



### System integration

AlloyDB Omni for Linux integrates directly with the Linux ecosystem:

  * Service management: the database runs as a `systemd` service (`alloydbomni17.service`). Administrators use standard commands, such as `systemctl start`, `systemctl stop`, and `systemctl status`, to manage the database lifecycle.
  * Package management: installation and updates are handled using the `dnf` package manager, which allows for straightforward version control and dependency management through standard repositories.
  * File system: data is stored in standard directories (for example, `/var/lib/postgresql/`), which enables the use of standard Linux backup tools and storage snapshots. However, you can configure a different directory for data storage.



## What's next

  * See [available download and installation options](https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/available-download-install-options).
  * [Install AlloyDB Omni for Linux](https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/deploy-vm).
  * Learn about [resource considerations that affect performance](https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/resource-considerations).
  * Learn about [available download and installation options](https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/available-download-install-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 

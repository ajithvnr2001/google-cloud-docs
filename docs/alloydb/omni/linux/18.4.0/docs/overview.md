---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/overview/
title: AlloyDB Omni using RPM overview \u00a0|\u00a0 AlloyDB Omni using RPM: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:32:36.050750+00:00
---

# AlloyDB Omni using RPM overview  |  AlloyDB Omni using RPM: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/overview/

This page documents AlloyDB Omni version **18.4.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/overview)



Send feedback 

#  AlloyDB Omni using RPM overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/overview)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/overview)



To run high-performance database workloads directly on your own infrastructure without the overhead of containers, use the AlloyDB Omni Red Hat Package Manager (RPM) deployment option. This overview describes how to install and manage the AlloyDB for PostgreSQL engine on standard Linux distributions like RHEL 9 and Rocky Linux 9.

**Note:** You must have AlloyDB Omni database version 18 or later.

To get started with this deployment model, [submit this form to request access](https://forms.gle/zxuHekMtV67Bw9Av9).

## Use cases

The RPM deployment option is designed for environments where containerization isn't preferred or where deep integration with the host operating system is required. Common use cases include the following:

  * Modernizing legacy applications: upgrade existing PostgreSQL workloads running on Linux servers to the RPM deployment option to gain performance and manageability improvements without replatforming to containers.
  * Edge computing: deploy high-performance databases in remote data centers where resource constraints or operational models favor direct operating system (OS) installation.
  * Development and testing: give developers a powerful, local database instance that mirrors the production AlloyDB for PostgreSQL environment, enabling consistent testing and rapid iteration.
  * High database performance: experience high performance on bare metal or virtual environments.
  * Securing data at rest: secure all data at rest in your AlloyDB Omni clusters without modifying your application code by enabling [transparent data encryption](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/transparent-data-encryption-omni). By enabling this feature, you ensure that all critical data at rest is automatically encrypted before being written to disk. This helps you meet compliance requirements and protects sensitive information.



## Benefits

AlloyDB Omni using RPM offers the following benefits:

  * Superior performance: it uses the AlloyDB for PostgreSQL columnar engine and intelligent caching to deliver faster analytical queries and higher transaction throughput compared to standard PostgreSQL.
  * Full control: it installs directly on the OS, giving system administrators complete control over resource allocation, file system configuration, and network settings using standard Linux tools.
  * 100% PostgreSQL compatibility: it is fully compatible with PostgreSQL, which lets you use existing tools, drivers, and extensions without code changes.
  * Operational simplicity: it integrates natively with RHEL systems. You can manage the database service using `systemctl` and install or update it using `dnf`, fitting seamlessly into existing Linux administration workflows.
  * Intelligent automation: it reduces administrative toil through autopilot features like adaptive autovacuum and automatic memory management, which dynamically adjusts the shared buffer cache based on system memory pressure to optimize resource usage without manual tuning.



## Architecture

The RPM deployment option runs as a set of integrated software components directly on the host operating system. It uses the standard Linux file system for storage, letting you use your existing storage infrastructure and management practices.

### Core components

The RPM deployment option architecture consists of the following primary RPM packages that work together to deliver the database service:

  * `alloydbomni`: this package is the core database engine. It contains the enhanced PostgreSQL server binaries, the AlloyDB for PostgreSQL columnar engine, and the autopilot management extensions. It runs as a system service (managed by `systemd`), handling client connections, query processing, and data storage.
  * `alloydbomni_monitor`: this package is a lightweight monitoring agent that runs alongside the core engine. It collects telemetry and performance metrics from the AlloyDB for PostgreSQL instance and exposes them over the Prometheus protocol for observability tools.
  * `alloydbomni_ui` (optional): this package provides the [AlloyDB Omni web user interface](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/install-web-ui), a self-managed web console that gives you observability into your database clusters, including CPU and memory telemetry charts (using metrics from `alloydbomni_monitor` and Prometheus), database sizes, active database flags, columnar engine statistics, and query insights.



### System integration

The RPM deployment option integrates directly with the Linux ecosystem:

  * Service management: the database runs as a `systemd` service (`alloydbomni18.service`). Administrators use standard commands, such as `systemctl start`, `systemctl stop`, and `systemctl status`, to manage the database lifecycle.
  * Package management: installation and updates are handled using the `dnf` package manager, which allows for straightforward version control and dependency management through standard repositories.
  * File system: data is stored in standard directories (for example, `/var/lib/postgresql/`), which enables the use of standard Linux backup tools and storage snapshots. However, you can configure a different directory for data storage.



## What's next

  * See [available download and installation options](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/available-download-install-options).
  * Learn about [resource considerations that affect performance](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/resource-considerations).
  * [Plan your RPM installation](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/plan-installation-linux).
  * [Install the web UI](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/install-web-ui).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 

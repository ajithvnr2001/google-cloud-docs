---
url: https://docs.cloud.google.com/feeds/composer-release-notes.xml
title: Managed Service for Apache Airflow - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:46:43.945417+00:00
---

# Managed Service for Apache Airflow - Release notes

> Source: https://docs.cloud.google.com/feeds/composer-release-notes.xml

tag:google.com,2016:composer-release-notesManaged Service for Apache Airflow - Release notesGoogle Cloud Platform2026-10-13T00:00:00-07:00October 13, 2026tag:google.com,2016:composer-release-notes#October_13_20262026-10-13T00:00:00-07:00Feature 

[Development mode environments](https://docs.cloud.google.com/composer/docs/composer-3/create-environments#development-mode) and [Environment hibernation](https://docs.cloud.google.com/composer/docs/composer-3/hibernate-environments) are now generally available (GA).

You can now create Managed Airflow (Gen 3) environments with Airflow 3 in development mode to test and develop DAGs before publishing them to production. You can hibernate development mode environments when you no longer need them. Hibernation reduces most environment costs to zero.

]]> September 25, 2026tag:google.com,2016:composer-release-notes#September_25_20262026-09-25T00:00:00-07:00Change 

_(Airflow 3.3.1, 3.2.2, and 2.11.1)_ The `apache-airflow-providers-google` package was upgraded to version 22.4.0. For more information about changes, see the [apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/changelog.html).

### Fixed

Fixed an issue where OpenID Connect (OIDC) ID token audience strings were incorrectly converted to lowercase. The audience field now preserves case-sensitivity. This fixes integration failures with external services that require case-sensitive audience values.

### Change

Airflow 2.10.5 is no longer included in new Managed Airflow images and builds

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Managed Airflow (Gen 3):

  * [composer-3-airflow-3.3.1-build.3](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-3-1-build-3)
  * [composer-3-airflow-3.2.2-build.7](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-2-2-build-7)
  * [composer-3-airflow-2.11.1-build.20](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-20) (default)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Managed Airflow (Gen 2):

  * [composer-2.17.14-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-14-airflow-2-11-1) (default)



### Deprecated

The following Managed Airflow versions and builds have reached their [end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support): composer-3-airflow-2.9.3-build.33, composer-3-airflow-2.10.5-build.13, composer-3-airflow-2.9.3-build.34, composer-3-airflow-2.10.5-build.14, composer-2.14.1-airflow-2.9.3, composer-2.14.1-airflow-2.10.5, composer-2.14.2-airflow-2.9.3, and composer-2.14.2-airflow-2.10.5.

]]> September 02, 2026tag:google.com,2016:composer-release-notes#September_02_20262026-09-02T00:00:00-07:00Announcement 

A new Managed Service for Apache Airflow release has started on **September 02, 2026**. Get ready for upcoming changes and features as we roll out the new release to all regions. This release is in progress at the moment. Listed changes and features might not be available in some regions yet.

### Feature

Managed Airflow (Gen 3) environments now provide Out-of-Memory (OOM) event logs to help troubleshoot and diagnose memory exhaustion.

### Change

Improved Airflow task resilience against transient Kubernetes pod connection issues.

### Change

Improved Airflow web server update process during environment upgrade operations.

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Managed Airflow (Gen 3):

  * [composer-3-airflow-3.3.1-build.2](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-3-1-build-2)
  * [composer-3-airflow-3.2.2-build.6](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-2-2-build-6)
  * [composer-3-airflow-2.11.1-build.19](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-19) (default)
  * [composer-3-airflow-2.10.5-build.52](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-52)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Managed Airflow (Gen 2):

  * [composer-2.17.13-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-13-airflow-2-11-1) (default)
  * [composer-2.17.13-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-13-airflow-2-10-5)

]]> August 28, 2026tag:google.com,2016:composer-release-notes#August_28_20262026-08-28T00:00:00-07:00Feature 

[Orchestration Pipelines](https://docs.cloud.google.com/composer/docs/composer-3/run-orchestration-pipelines) are now **generally available (GA)**.

]]> August 26, 2026tag:google.com,2016:composer-release-notes#August_26_20262026-08-26T00:00:00-07:00Feature 

_(Airflow 3.3.1 and 3.2.2)_ Environments with Airflow 3.3.1 and 3.2.2 now support loading snapshots from environments with Airflow 2.11.1. This feature lets you migrate from Airflow 2.11.1 environments to Airflow 3 using snapshots, provided that your DAGs in Airflow 2.11.1 are compatible with Airflow 3.

This feature is gradually rolling out over several releases. In this release, it's available in the following regions: europe-north1, europe-west3, us-east1, and us-west2.

### Fixed

_(Airflow 3.3.1)_ Backported [#71091](https://github.com/apache/airflow/pull/71091) to fix a warning about invalid characters for stats reporting generated by the DAG processor for every file.

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Managed Airflow (Gen 3):

  * [composer-3-airflow-3.3.1-build.0](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-3-1-build-0)
  * [composer-3-airflow-3.2.2-build.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-2-2-build-5)
  * [composer-3-airflow-2.11.1-build.18](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-18) (default)
  * [composer-3-airflow-2.10.5-build.51](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-51)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Managed Airflow (Gen 2):

  * [composer-2.17.12-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-12-airflow-2-11-1) (default)
  * [composer-2.17.12-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-12-airflow-2-10-5)



### Deprecated

The following Managed Airflow versions and builds have reached their [end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support): composer-3-airflow-2.9.3-build.32, composer-3-airflow-2.10.5-build.12, composer-2.14.0-airflow-2.10.5, composer-2.14.0-airflow-2.9.3.

]]> August 25, 2026tag:google.com,2016:composer-release-notes#August_25_20262026-08-25T00:00:00-07:00Feature 

[Managed Airflow remote Model Context Protocol (MCP) server](https://docs.cloud.google.com/composer/docs/composer-3/use-composer-mcp) is now generally available (GA).

### Feature

[Managed Airflow Agent](https://docs.cloud.google.com/composer/docs/composer-3/troubleshoot-tasks-and-dag-runs-with-agent) is now available in Google Cloud Console. The agent can help you understand, diagnose, and resolve issues with failed Airflow tasks and DAG runs, optimize your environment's performance, identify existing or potential issues, bottlenecks, and areas for optimization.

]]> August 20, 2026tag:google.com,2016:composer-release-notes#August_20_20262026-08-20T00:00:00-07:00Announcement 

A new Managed Service for Apache Airflow release has started on **August 20, 2026**. Get ready for upcoming changes and features as we roll out the new release to all regions. This release is in progress at the moment. Listed changes and features might not be available in some regions yet.

### Feature

**Airflow 3.3.1** is available in Managed Airflow (Gen 3).

### Change

Airflow 3.1.8 is no longer included in Managed Airflow images and builds.

### Feature

[Composer Local Development CLI tool](https://docs.cloud.google.com/composer/docs/composer-3/run-local-airflow-environments) now supports deployment with Podman in Linux and Windows.

### Change

_(Airflow 3.2.2, 3.1.8, and 2.11.1)_ The `apache-airflow-providers-google` package was upgraded to version 22.3.0. For more information about changes, see the [apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/changelog.html).

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Managed Airflow (Gen 3):

  * [composer-3-airflow-3.3.1-build.0](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-3-1-build-0) (extended upgrade timeline version)
  * [composer-3-airflow-3.2.2-build.4](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-2-2-build-4) (extended upgrade timeline version)
  * [composer-3-airflow-2.11.1-build.17](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-17) (extended upgrade timeline version)
  * [composer-3-airflow-2.10.5-build.50](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-50) (extended upgrade timeline version)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Managed Airflow (Gen 2):

  * [composer-2.17.11-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-11-airflow-2-11-1) (extended upgrade timeline version)
  * [composer-2.17.11-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-11-airflow-2-10-5) (extended upgrade timeline version)

]]> August 10, 2026tag:google.com,2016:composer-release-notes#August_10_20262026-08-10T00:00:00-07:00Change 

_(Managed Airflow Gen 3)_ Adjusted the formula used to calculate the number of Airflow web server workers based on allocated CPU and memory resources. This update aligns with resource consumption changes in recent Airflow versions, improving web server stability.

### Change

_(Airflow 3.2.2 and 2.11.1)_ The `[api]rbac_bindings` Airflow configuration option is blocked and it isn't possible to override its value.

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Managed Airflow (Gen 3):

  * [composer-3-airflow-3.2.2-build.2](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-2-2-build-2)
  * [composer-3-airflow-3.1.8-build.4](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-8-build-4)
  * [composer-3-airflow-2.11.1-build.15](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-15)
  * [composer-3-airflow-2.10.5-build.48](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-48)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Managed Airflow (Gen 2):

  * [composer-2.17.10-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-10-airflow-2-11-1)
  * [composer-2.17.10-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-10-airflow-2-10-5)

]]> August 05, 2026tag:google.com,2016:composer-release-notes#August_05_20262026-08-05T00:00:00-07:00Change 

_(Airflow 3.2.2, 3.1.8, and 2.11.1)_ The `google-cloud-dataproc` package was upgraded to version 5.30.0, which includes support for Managed Service for Apache Spark [flexible instance configurations](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flexible-vms) (flexible VMs).

This package was upgraded in Airflow 2.10.5 in a [previous release](https://docs.cloud.google.com/composer/docs/release-notes#July_16_2026).

### Change

_(Airflow 3.2.2, 3.1.8, and 2.11.1)_ The `apache-airflow-providers-google` package was upgraded to version 22.2.2. For more information about changes, see the [apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/changelog.html).

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Managed Airflow (Gen 3):

  * [composer-3-airflow-3.2.2-build.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-2-2-build-1)
  * [composer-3-airflow-3.1.8-build.3](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-8-build-3)
  * [composer-3-airflow-2.11.1-build.14](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-14) (default)
  * [composer-3-airflow-2.10.5-build.47](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-47)



These builds are versions with an extended upgrade timeline.

### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Managed Airflow (Gen 2):

  * [composer-2.17.9-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-9-airflow-2-11-1) (default)
  * [composer-2.17.9-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-9-airflow-2-10-5)



These images are versions with an extended upgrade timeline.

### Deprecated

The following Managed Airflow versions and builds have reached their [end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support): composer-3-airflow-2.10.5-build.11, composer-3-airflow-2.9.3-build.31, composer-2.13.9-airflow-2.9.3, and composer-2.13.9-airflow-2.10.5.

]]> July 29, 2026tag:google.com,2016:composer-release-notes#July_29_20262026-07-29T00:00:00-07:00Feature 

**Airflow 3.2.2** is available in Managed Airflow (Gen 3).

### Change

_(Airflow 3.2.2)_ The [Multi-Team](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/multi-team.html) Airflow feature isn't available. The `[core]multi_team` Airflow configuration option is set to `False` and it isn't possible to override it.

### Fixed

_(Airflow 3.2.2)_ Backported [#69877](https://github.com/apache/airflow/pull/69877) to restore the ability to deliver failure and retry alerts through a pluggable email backend (configured through the `[email]email_backend` Airflow configuration option).

### Change

_(Managed Airflow Gen 3 with Airflow 2)_ Default triggerer resources are changing to 1 vCPU and 2 GB memory to match Airflow 3 defaults. This change is available in the Google Cloud CLI, Terraform, and Cloud Composer API and is gradually rolling out in the Google Cloud console.

### Fixed

A correct error message is now generated when an environment creation request fails because of malformed network and subnetwork identifiers.

### Fixed

_(Available without upgrading)_ The correct default task priority weight of `1` is now shown for tasks in the Google Cloud console.

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Managed Airflow (Gen 3):

  * [composer-3-airflow-3.2.2-build.0](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-2-2-build-0)
  * [composer-3-airflow-3.1.8-build.2](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-8-build-2)
  * [composer-3-airflow-2.11.1-build.13](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-13) (default)
  * [composer-3-airflow-2.10.5-build.46](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-46)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Managed Airflow (Gen 2):

  * [composer-2.17.8-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-8-airflow-2-11-1) (default)
  * [composer-2.17.8-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-8-airflow-2-10-5)



### Deprecated

The following Managed Airflow versions and builds have reached their [end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support): composer-3-airflow-2.10.5-build.10, composer-3-airflow-2.9.3-build.30, composer-2.13.8-airflow-2.9.3, and composer-2.13.8-airflow-2.10.5.

]]> July 24, 2026tag:google.com,2016:composer-release-notes#July_24_20262026-07-24T00:00:00-07:00Announcement 

Starting in September, 2026, **Airflow 2.10.5 will no longer be included** in new Managed Airflow images and builds. This change will not affect existing images and builds.

### Announcement

Starting in September 2026, we are changing the version support policy for Managed Airflow (Gen 2) to align it with the Managed Airflow (Gen 3) policy. The changes will **affect Airflow 2 versions that we release** :

  * In Managed Airflow (Gen 2), we will **release only new images with Airflow 2.11**. New Airflow 2.10.5 images will no longer be released.
  * In Managed Airflow (Gen 3) we will keep releasing new builds of Airflow 3 (no changes) and will release only new Airflow 2.11 builds. New Airflow 2.10.5 builds will no longer be released.

]]> July 16, 2026tag:google.com,2016:composer-release-notes#July_16_20262026-07-16T00:00:00-07:00Feature 

**Airflow 3.1.8** is available in Managed Airflow (Gen 3).

### Change

Airflow 3.1.7 is no longer included in Managed Airflow images and builds.

### Fixed

_(Airflow 3.1.8)_ Backported [#64031](https://github.com/apache/airflow/pull/64031) to fix an issue in the Airflow UI when viewing tasks in non-terminal states (scheduled, running) with "Show Gantt" enabled.

### Change

_(Airflow 2.10.5)_ The `google-cloud-dataproc` package was upgraded to version 5.30.0, which includes support for Managed Service for Apache Spark [flexible instance configurations](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flexible-vms) (flexible VMs). You can configure these extra options in the cluster configuration.

### Change

_(Airflow 3.1.8)_ The `apache-airflow-providers-google` package was upgraded to version 22.2.0. For more information about changes, see the [apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/changelog.html).

### Change

_(Airflow 2.11.1)_ The `apache-airflow-providers-google` package was upgraded to version 22.2.1. For more information about changes, see the [apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/changelog.html).

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Managed Airflow (Gen 3):

  * [composer-3-airflow-3.1.8-build.0](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-8-build-0)
  * [composer-3-airflow-2.11.1-build.11](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-11) (default)
  * [composer-3-airflow-2.10.5-build.44](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-44)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Managed Airflow (Gen 2):

  * [composer-2.17.7-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-7-airflow-2-11-1) (default)
  * [composer-2.17.7-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-7-airflow-2-10-5)



### Deprecated

The following Managed Airflow versions and builds have reached their [end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support): composer-3-airflow-2.10.5-build.9, composer-3-airflow-2.9.3-build.29, composer-2.13.7-airflow-2.9.3, composer-2.13.7-airflow-2.10.5.

]]> July 13, 2026tag:google.com,2016:composer-release-notes#July_13_20262026-07-13T00:00:00-07:00Issue 

In Managed Airflow (Gen 3) builds with Airflow 2.11.1 starting from [composer-3-airflow-2.11.1-build.7](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-7), the Airflow web server requires at least 3 GB of memory (the default amount of memory for a Small environment preset is 4 GB).

If the Airflow web server has less than 3 GB of memory, it might experience intermittent out-of-memory (OOM) issues. To resolve these issues, [increase the web server memory](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments#web-server-parameters) to at least 3 GB.

]]> July 07, 2026tag:google.com,2016:composer-release-notes#July_07_20262026-07-07T00:00:00-07:00Change 

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Managed Airflow (Gen 3):

  * [composer-3-airflow-3.1.7-build.13](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-13)
  * [composer-3-airflow-2.11.1-build.9](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-9) (default)
  * [composer-3-airflow-2.10.5-build.42](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-42)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Managed Airflow (Gen 2):

  * [composer-2.17.6-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-6-airflow-2-11-1) (default)
  * [composer-2.17.6-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-6-airflow-2-10-5)



### Deprecated

The following Managed Airflow versions and builds have reached their [end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support): composer-3-airflow-2.9.3-build.28, composer-3-airflow-2.10.5-build.0, composer-3-airflow-2.10.5-build.2, composer-3-airflow-2.10.5-build.3, composer-3-airflow-2.10.5-build.4, composer-3-airflow-2.10.5-build.5, composer-3-airflow-2.10.5-build.6, composer-3-airflow-2.10.5-build.7, composer-3-airflow-2.10.5-build.8, composer-2.13.6-airflow-2.9.3, and composer-2.13.6-airflow-2.10.5.

]]> June 29, 2026tag:google.com,2016:composer-release-notes#June_29_20262026-06-29T00:00:00-07:00Change 

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Managed Airflow (Gen 3):

  * [composer-3-airflow-3.1.7-build.12](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-12)
  * [composer-3-airflow-2.11.1-build.8](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-8) (default)
  * [composer-3-airflow-2.10.5-build.41](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-41)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Managed Airflow (Gen 2):

  * [composer-2.17.5-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-5-airflow-2-11-1) (default)
  * [composer-2.17.5-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-5-airflow-2-10-5)

]]> June 26, 2026tag:google.com,2016:composer-release-notes#June_26_20262026-06-26T00:00:00-07:00Change 

The `apache-airflow-providers-google` package was upgraded to version 22.1.0. For more information about changes, see the [apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/changelog.html).

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Managed Airflow (Gen 3):

  * [composer-3-airflow-3.1.7-build.11](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-11)
  * [composer-3-airflow-2.11.1-build.7](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-7) (default)
  * [composer-3-airflow-2.10.5-build.40](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-40)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Managed Airflow (Gen 2):

  * [composer-2.17.4-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-4-airflow-2-11-1) (default)
  * [composer-2.17.4-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-4-airflow-2-10-5)



### Deprecated

The following Managed Airflow versions and builds have reached their [end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support): composer-3-airflow-2.9.3-build.25, composer-3-airflow-2.9.3-build.26, composer-3-airflow-2.9.3-build.27, composer-2.13.3-airflow-2.9.3, composer-2.13.4-airflow-2.9.3, composer-2.13.5-airflow-2.9.3, composer-2.13.3-airflow-2.10.5, composer-2.13.4-airflow-2.10.5, composer-2.13.5-airflow-2.10.5.

]]> June 12, 2026tag:google.com,2016:composer-release-notes#June_12_20262026-06-12T00:00:00-07:00Feature 

New Managed Airflow (Gen 2) environments created while the Restrict Endpoint Usage organization policy is active now use regional endpoints for services like Cloud Storage, Cloud Logging, Pub/Sub, and Data Lineage. For more information, see [Configure environments with Restrict Endpoint Usage policy](https://docs.cloud.google.com/composer/docs/composer-2/configure-restrict-endpoint-usage-environments).

]]> June 08, 2026tag:google.com,2016:composer-release-notes#June_08_20262026-06-08T00:00:00-07:00Change 

Several API dependencies that aren't required by Managed Airflow (Gen 3) are now phased out and must be enabled separately if you want to create Managed Airflow (Gen 2) environments in a new project. This change was [announced previously](https://docs.cloud.google.com/composer/docs/release-notes#June_16_2025).

The following API dependencies were phased out:

  * artifactregistry.googleapis.com
  * cloudbuild.googleapis.com
  * container.googleapis.com



The following API dependencies aren't phased out yet and are scheduled to be detached from the Cloud Composer API in the future:

  * sqladmin.googleapis.com



Existing Managed Airflow (Gen 3) and Managed Airflow (Gen 2) environments in projects where the Cloud Composer API is already enabled aren't impacted.

You can do the following:

  * If your project has only Managed Airflow (Gen 3) environments, then you can manually disable the listed APIs that were phased out.
  * If your project has Managed Airflow (Gen 2) environments, then we recommend to keep these APIs enabled because disabling them might lead to environment's malfunction.
  * If you want to create Managed Airflow (Gen 2) environments in a new project, you can enable the listed APIs manually or using a Google Cloud CLI command. For more information, see [Enable Managed Airflow (Gen 2) dependencies](https://docs.cloud.google.com/composer/docs/composer-2/enable-composer-service#enable-gen-2-dependencies).
  * If you use automation scripts to provision Managed Airflow (Gen 2) environments, then make sure that the listed APIs are enabled in addition to the Cloud Composer API.



August 17, 2026 update: The pubsub.googleapis.com API dependency was phased out but was restored and is scheduled to be detached from the Cloud Composer API in the future.

]]> June 02, 2026tag:google.com,2016:composer-release-notes#June_02_20262026-06-02T00:00:00-07:00Feature 

_(Managed Airflow Gen 3)_ You can now [access Cloud Run endpoints restricted to internal ingress traffic](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network#cloud-run-traffic) through your environment's network attachment. This feature is available through gcloud CLI beta commands and beta Cloud Composer API in all Managed Airflow (Gen 3) versions.

]]> May 27, 2026tag:google.com,2016:composer-release-notes#May_27_20262026-05-27T00:00:00-07:00Feature 

Managed Service for Apache Airflow now [supports Google Cloud tags](https://docs.cloud.google.com/composer/docs/composer-3/create-and-manage-tags) for environments.

[Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) provide a way to create annotations for resources, and conditionally allow or deny policies based on whether a resource has a specific tag.

### Feature

In Managed Airflow (Gen 3), it is now possible to create Kubernetes Secrets with the `kubernetes.io/dockerconfigjson` [secret type](https://kubernetes.io/docs/concepts/configuration/secret/#secret-types) through the beta Cloud Composer API, in addition to the default `Opaque` secret type. For more information, see [Manage Kubernetes Secrets](https://docs.cloud.google.com/composer/docs/composer-3/use-kubernetes-pod-operator#api).

### Fixed

(Airflow 3) The INFO log level filter in Airflow UI now correctly displays log messages with this logging level.

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Managed Airflow (Gen 3):

  * [composer-3-airflow-3.1.7-build.10](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-10)
  * [composer-3-airflow-2.11.1-build.6](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-6) (default)
  * [composer-3-airflow-2.10.5-build.39](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-39)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Managed Airflow (Gen 2):

  * [composer-2.17.3-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-3-airflow-2-11-1) (default)
  * [composer-2.17.3-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-3-airflow-2-10-5)



### Deprecated

The following Managed Airflow versions and builds have reached their [end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support): composer-3-airflow-2.9.3-build.24, composer-2.13.2-airflow-2.9.3, composer-2.13.2-airflow-2.10.5.

]]> May 14, 2026tag:google.com,2016:composer-release-notes#May_14_20262026-05-14T00:00:00-07:00Change 

The `[scheduler]print_stats_interval` Airflow configuration option can now be overridden in environments with Airflow 2.10.5 and later. This option previously was blocked.

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Managed Airflow (Gen 3):

  * [composer-3-airflow-3.1.7-build.9](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-9)
  * [composer-3-airflow-2.11.1-build.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-5) (default)
  * [composer-3-airflow-2.10.5-build.38](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-38)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Managed Airflow (Gen 2):

  * [composer-2.17.2-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-2-airflow-2-11-1) (default)
  * [composer-2.17.2-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-2-airflow-2-10-5)



### Deprecated

The following Managed Airflow versions and builds have reached their [end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support): composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.3, and composer-2.13.1-airflow-*.

### Issue

The `google-api-core` preinstalled package versions from 2.28.0 to 2.30.2 might cause degraded environment performance, which can result in longer times to execute a task and longer times to move a task from the queued to the executing state.

Affected Managed Airflow (Gen 3) builds:

  * composer-3-airflow-3.1.7-build.0 to composer-3-airflow-3.1.7-build.5
  * composer-3-airflow-3.1.0-build.5 to composer-3-airflow-3.1.0-build.10
  * composer-3-airflow-2.11.1-build.0
  * composer-3-airflow-2.10.5-build.22 to composer-3-airflow-2.10.5-build.33
  * composer-3-airflow-2.9.3-build.42 to composer-3-airflow-2.9.3-build.53



Affected Managed Airflow (Gen 2) builds:

  * composer-2.16.10-airflow-2.11.1
  * composer-2.16.0-airflow-2.10.5 to composer-2.16.10-airflow-2.10.5
  * composer-2.16.0-airflow-2.9.3 to composer-2.16.10-airflow-2.9.3



We recommend to upgrade your environment to the following versions, which contain a version of the package where the problem is fixed or isn't present:

  * composer-3-airflow-3.1.7-build.7 and later
  * composer-3-airflow-2.11.1-build.3 and later
  * composer-3-airflow-2.10.5-build.36 and later
  * composer-3-airflow-2.9.3-build.54 (contains 2.27.0)
  * composer-2.17.0-airflow-2.11.1 and later
  * composer-2.17.0-airflow-2.10.5 and later
  * composer-2.16.11-airflow-2.11.1 (contains 2.27.0)
  * composer-2.16.11-airflow-2.10.5 (contains 2.27.0)
  * composer-2.16.11-airflow-2.9.3 (contains 2.27.0)



As a workaround, you can manually install a later version of the `google-api-core` package to an affected environment by specifying `>=2.30.3` as the required version.

]]> May 11, 2026tag:google.com,2016:composer-release-notes#May_11_20262026-05-11T00:00:00-07:00Change 

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Managed Airflow (Gen 3):

  * [composer-3-airflow-3.1.7-build.8](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-8)
  * [composer-3-airflow-2.11.1-build.4](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-4) (default)
  * [composer-3-airflow-2.10.5-build.37](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-37)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Managed Airflow (Gen 2):

  * [composer-2.17.1-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-1-airflow-2-11-1) (default)
  * [composer-2.17.1-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-1-airflow-2-10-5)



### Deprecated

The following Managed Airflow versions and builds have reached their [end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support): composer-3-airflow-2.9.3-build.22 and composer-2.13.0-airflow-*.

]]> May 06, 2026tag:google.com,2016:composer-release-notes#May_06_20262026-05-06T00:00:00-07:00Announcement 

Managed Airflow (Gen 2) environments can no longer be created in Johannesburg (africa-south1). We're switching this region to supporting only Managed Airflow (Gen 3) environments. Existing Managed Airflow (Gen 2) environments in this region aren't affected by this change.

]]> April 28, 2026tag:google.com,2016:composer-release-notes#April_28_20262026-04-28T00:00:00-07:00Feature 

Managed Airflow (Gen 3) environments with Airflow 3 support [access with external identities](https://docs.cloud.google.com/composer/docs/composer-3/access-environments-with-workforce-identity-federation) through workforce identity federation starting from version composer-3-airflow-3.1.7-build.7.

### Change

The default version of Airflow is changed to 2.11.1.

### Fixed

Fixed an issue where DAGs were imported from snapshots even when the "Skip copying Cloud Storage data" option was selected.

### Fixed

The `GOOGLE_CLOUD_PROJECT` environment variable is now set on schedulers and triggerers. It's no longer required to set the project ID explicitly when configuring the Secret Manager backend.

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Managed Airflow (Gen 3):

  * [composer-3-airflow-3.1.7-build.7](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-7)
  * [composer-3-airflow-2.11.1-build.3](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-3) (default)
  * [composer-3-airflow-2.10.5-build.36](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-36)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Managed Airflow (Gen 2):

  * [composer-2.17.0-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-0-airflow-2-11-1) (default)
  * [composer-2.17.0-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-0-airflow-2-10-5)



### Deprecated

Airflow 2.9.3 is no longer included in Managed Airflow images and builds.

### Deprecated

The following Managed Airflow versions and builds have reached their [end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support):

  * composer-3-airflow-2.9.3-build.20
  * composer-3-airflow-2.10.2 builds from build.0 to build.13
  * composer-2.12.1-airflow-*

]]> April 22, 2026tag:google.com,2016:composer-release-notes#April_22_20262026-04-22T00:00:00-07:00Feature 

Managed Service for Apache Airflow supports Gemini Cloud Assist Investigations capabilities. The new troubleshooting agent can now troubleshoot failed Airflow task instances and DAG runs. The feature is available through Gemini Cloud Assist Investigations, which is currently accessible in Private Preview.

]]> April 15, 2026tag:google.com,2016:composer-release-notes#April_15_20262026-04-15T00:00:00-07:00Announcement 

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem.

### Feature

**Airflow 3** is now generally available (GA) in Cloud Composer 3 starting from the composer-3-airflow-3.1.7-build.4 Airflow build.

### Feature

[Cloud Composer remote Model Context Protocol (MCP) server](https://docs.cloud.google.com/composer/docs/composer-3/use-composer-mcp) is available in Preview.

You can use Cloud Composer remote Model Context Protocol (MCP) server to connect to Cloud Composer from AI applications such as Gemini CLI, ChatGPT, Claude, or in AI applications that you're developing. The Cloud Composer MCP server lets you manage Cloud Composer environments and get details about executed DAG runs and Airflow tasks.

]]> April 10, 2026tag:google.com,2016:composer-release-notes#April_10_20262026-04-10T00:00:00-07:00Fixed 

Fixed a problem with missing DAG description and schedule in the DAG UI which occurred in environments with Airflow 3 in some cases.

Fixed an issue where DAG descriptions and schedules occasionally weren't displayed in DAG UI for environments with Airflow 3.

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Cloud Composer 3:

  * [composer-3-airflow-3.1.7-build.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-5)
  * [composer-3-airflow-2.11.1-build.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-1)
  * [composer-3-airflow-2.10.5-build.34](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-34) (default)
  * [composer-3-airflow-2.9.3-build.54](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-54)



These builds are versions with an extended upgrade timeline.

### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Cloud Composer 2:

  * [composer-2.16.11-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-16-11-airflow-2-11-1)
  * [composer-2.16.11-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-16-11-airflow-2-10-5) (default)
  * [composer-2.16.11-airflow-2.9.3](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-16-11-airflow-2-9-3)



These images are versions with an extended upgrade timeline.

]]> April 01, 2026tag:google.com,2016:composer-release-notes#April_01_20262026-04-01T00:00:00-07:00Feature 

**Airflow 2.11.1 is available** in Cloud Composer 3 and Cloud Composer 2.

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Cloud Composer 3:

  * [composer-3-airflow-2.11.1-build.0](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-0)
  * [composer-3-airflow-3.1.7-build.4](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-4)
  * [composer-3-airflow-2.10.5-build.33](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-33) (default)
  * [composer-3-airflow-2.9.3-build.53](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-53)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Cloud Composer 2:

  * [composer-2.16.10-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-16-10-airflow-2-11-1)
  * [composer-2.16.10-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-16-10-airflow-2-10-5) (default)
  * [composer-2.16.10-airflow-2.9.3](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-16-10-airflow-2-9-3)

]]> March 27, 2026tag:google.com,2016:composer-release-notes#March_27_20262026-03-27T00:00:00-07:00Announcement 

Cloud Composer 2 environments can no longer be created in Melbourne (australia-southeast2). We're switching this region to supporting only Cloud Composer 3 environments. Existing Cloud Composer 2 environments in this region aren't affected by this change.

### Announcement

A new Cloud Composer release has started on **March 27, 2026**. Get ready for upcoming changes and features as we roll out the new release to all regions. This release is in progress at the moment. Listed changes and features might not be available in some regions yet.

### Change

_(Airflow 3.1.7)_ Starting from version composer-3-airflow-3.1.7-build.1, Airflow workers no longer have direct access to the Airflow database of your environment.

This feature was [announced previously](https://docs.cloud.google.com/composer/docs/release-notes#March_17_2026) and has finished gradually rolling out to all regions supported by Cloud Composer 3.

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Cloud Composer 3:

  * [composer-3-airflow-3.1.7-build.3](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-3)
  * [composer-3-airflow-2.10.5-build.32](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-32) (default)
  * [composer-3-airflow-2.9.3-build.52](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-52)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Cloud Composer 2:

  * [composer-2.16.9-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-16-9-airflow-2-10-5) (default)
  * [composer-2.16.9-airflow-2.9.3](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-16-9-airflow-2-9-3)



### Deprecated

The following Cloud Composer versions and builds have reached their [end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support): composer-3-airflow-2.9.3-build.19 and composer-2.12.0-*.

]]> March 19, 2026tag:google.com,2016:composer-release-notes#March_19_20262026-03-19T00:00:00-07:00Announcement 

Cloud Composer 2 environments can no longer be created in Berlin (europe-west10) and Dallas (us-south1). We're switching these regions to supporting only Cloud Composer 3 environments. Existing Cloud Composer 2 environments in these regions aren't affected by this change.

### Change

_(Airflow 3.1.7 in Cloud Composer 3)_ The `apache-airflow-providers-cncf-kubernetes` package was [upgraded to version 10.14.0](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/changelog.html). For changes in other packages, see the [preinstalled packages changelog](https://cloud.google.com/composer/docs/versions-packages).

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Cloud Composer 3:

  * [composer-3-airflow-3.1.7-build.2](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-2)
  * [composer-3-airflow-2.10.5-build.31](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-31) (default)
  * [composer-3-airflow-2.9.3-build.51](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-51)



### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Cloud Composer 2:

  * [composer-2.16.8-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-16-8-airflow-2-10-5) (default)
  * [composer-2.16.8-airflow-2.9.3](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-16-8-airflow-2-9-3)

]]>

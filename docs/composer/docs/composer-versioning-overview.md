---
url: https://docs.cloud.google.com/composer/docs/composer-versioning-overview/
title: Managed Service for Apache Airflow versioning overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:38.777402+00:00
---

# Managed Service for Apache Airflow versioning overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-versioning-overview/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Resources ](https://docs.cloud.google.com/composer/docs/resources)



Send feedback 

#  Managed Service for Apache Airflow versioning overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Managed Service for Apache Airflow versioning and lists differences between major Managed Airflow versions.

## Major versions of Managed Airflow

Managed Airflow has the following major versions:

  * **Managed Airflow (Gen 3)**. This version has simplified network setup and hides infrastructure components including the environment's cluster and environment's dependencies on other services.

  * **Managed Airflow (Gen 2)**. In this version, the environment's cluster scales automatically to meet the resource demands.

**Important:** On **September 15, 2026** , versions 2.0.x of Managed Airflow (Gen 2) will reach their planned end of life, and you won't be able to use them. Versions 2.1.x and later aren't affected by this change. We recommend [upgrading](https://docs.cloud.google.com/composer/docs/composer-2/upgrade-environments) your environment to the latest Managed Airflow (Gen 2) version or [migrating to Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/latest/migrate-composer-1-to-3).
  * **Managed Airflow (Legacy Gen 1)**. Has manual environment scaling, the infrastructure is deployed to your projects and networks.

**Important:** On **March 25, 2024** , Managed Airflow (Legacy Gen 1) entered its post-maintenance mode. Google will not release any further updates to Managed Airflow (Legacy Gen 1), including new versions of Airflow, bugfixes, and security updates. On **September 15, 2026** , all Managed Airflow (Legacy Gen 1) environments will reach their planned end of life, and you won't be able to use them. We recommend [migration to Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/latest/migrate-composer-1-to-3).



## Comparison of Managed Airflow versions

The following table lists major differences between Managed Airflow (Legacy Gen 1), Managed Airflow (Gen 2), and Managed Airflow (Gen 3).

Feature | Managed Airflow (Legacy Gen 1) | Managed Airflow (Gen 2) | Managed Airflow (Gen 3)  
---|---|---|---  
Image version | `composer-1.b.c-airflow-x.y.z` | `composer-2.b.c-airflow-x.y.z` | `composer-3-airflow-x.y.z-build.t`  
Airflow versions | Airflow 1.10.* and Airflow 2 | Airflow 2 | Airflow 2, Airflow 3  
Python versions | 3.8.12 | 3.11.8 (3.11.5 and 3.8.12 in earlier versions) | 3.11.8  
Environment's cluster | [Standard mode VPC-native or Routes-based Google Kubernetes Engine cluster](https://docs.cloud.google.com/composer/docs/composer-1/environment-architecture#cluster) | [Autopilot mode VPC-native Google Kubernetes Engine cluster](https://docs.cloud.google.com/composer/docs/composer-2/environment-architecture#cluster) | Environment's cluster is not deployed into your project.  
Horizontal scaling | Can adjust the number of nodes in the environment's cluster. This changes the number of Airflow workers.  
Can adjust the number of Airflow schedulers. | Automatically scaling number of Airflow workers, based on demand. Can set and change upper and lower limits for the number of workers.   
Can adjust the number of Airflow schedulers and triggerers | Automatically scaling number of Airflow workers, based on demand. Can set and change upper and lower limits for the number of workers.   
Can adjust the number of Airflow schedulers, triggerers, and DAG processors  
Vertical scaling | Can set machine types for cluster nodes, Airflow web server and database when creating an environment. Can change machine types for Airflow web server and database. | Can set and change the workloads configuration: CPU, memory, and storage parameters for Airflow workers, schedulers, web server, and the environment size. | Can set and change the workloads configuration: CPU, memory, and storage parameters for Airflow workers, schedulers, web server, DAG processors, and the environment size.  
Pricing model | [Managed Airflow (Legacy Gen 1) pricing model](https://docs.cloud.google.com/composer/pricing#sku-composer-1) | [Managed Airflow (Gen 2) pricing model](https://docs.cloud.google.com/composer/pricing#sku-composer-2) | [Managed Airflow (Gen 3) pricing model](https://docs.cloud.google.com/composer/pricing)  
Access control | [Managed Airflow (Legacy Gen 1) roles](https://docs.cloud.google.com/composer/docs/composer-1/access-control) | [Managed Airflow roles. Uses Workload Identity Federation for GKE and requires additional permissions for the Managed Airflow Service Agent account.](https://docs.cloud.google.com/composer/docs/composer-2/access-control#composer-sa) | Managed Airflow roles. Uses Workload Identity Federation for GKE. Extra permissions are not required  
Access through Workforce Identity Federation | Not supported | [Supported](https://docs.cloud.google.com/composer/docs/composer-2/access-environments-with-workforce-identity-federation) | [Supported](https://docs.cloud.google.com/composer/docs/composer-3/access-environments-with-workforce-identity-federation)  
Highly Resilient environments | Not supported | [Supported](https://docs.cloud.google.com/composer/docs/composer-2/set-up-highly-resilient-environments) | [Supported](https://docs.cloud.google.com/composer/docs/composer-3/set-up-highly-resilient-environments)  
Database retention policy | Not supported | Not yet available | [Supported](https://docs.cloud.google.com/composer/docs/composer-3/configure-db-retention)  
Private IP networking | [VPC peerings](https://docs.cloud.google.com/composer/docs/composer-1/configure-private-ip) | [Private Service Connect](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-service-connect) | [Simplified network setup. Can be changed between Public and Private IP in an existing environment.](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type)  
VPC Service Controls | Supported | Supported | Supported  
Airflow executors | Celery Executor | Celery Executor | [CeleryKubernetes Executor](https://docs.cloud.google.com/composer/docs/composer-3/use-celery-kubernetes-executor)  
Airflow triggerer (deferrable operators) | Not supported | [Supported](https://docs.cloud.google.com/composer/docs/composer-2/use-deferrable-operators) | [Supported](https://docs.cloud.google.com/composer/docs/composer-3/use-deferrable-operators)  
Custom service account for KubernetesPodOperator | Supported | [Supported](https://docs.cloud.google.com/composer/docs/composer-2/use-kubernetes-pod-operator#composer-2-kpo-access-project-resources) | [Not supported](https://docs.cloud.google.com/composer/docs/composer-3/use-kubernetes-pod-operator#composer-3-kpo-access-project-resources)  
CMEK | [Supported](https://docs.cloud.google.com/composer/docs/composer-1/configure-cmek-encryption) | [Supported](https://docs.cloud.google.com/composer/docs/composer-2/configure-cmek-encryption) | [Supported](https://docs.cloud.google.com/composer/docs/composer-3/configure-cmek-encryption)  
Web server access controls | [Supported](https://docs.cloud.google.com/composer/docs/composer-1/create-environments#web-server-access) | [Supported](https://docs.cloud.google.com/composer/docs/composer-2/create-environments#web-server-access) | [Supported](https://docs.cloud.google.com/composer/docs/composer-3/create-environments#web-server-access)  
Restarting web server | [Supported](https://docs.cloud.google.com/composer/docs/composer/docs/how-to/accessing/airflow-web-interface#restarting) | [Supported](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface#restarting) | [Supported](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface#restarting)  
Web server plugins | [Supported in Airflow 1 environments with disabled DAG serialization.](https://docs.cloud.google.com/composer/docs/composer-1/dag-serialization#disable) | Supported | Supported, plugins can be disabled and enabled on demand.  
Scheduler plugins | Not supported | Supported | Not supported  
Listeners | Not supported | Supported | [Only task-level listeners](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/listeners.html#taskinstance-state-change-events)  
TimeTables | [Only Built-In](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/timetable.html#built-in-timetables) | Custom and Built-In | [Only Built-In](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/timetable.html#built-in-timetables)  
Scheduler custom PyPI packages | Not supported | Supported | Not supported  
Installing custom plugins | [Supported](https://docs.cloud.google.com/composer/docs/composer-1/install-plugins) | [Supported](https://docs.cloud.google.com/composer/docs/composer-2/install-plugins) | [Supported](https://docs.cloud.google.com/composer/docs/composer-3/install-plugins)  
Maintenance operations | All tasks can be impacted. | Tasks that take less than 55 minutes to execute are not impacted. | Tasks that take less than 24 hours to execute are not impacted.  
Storing Snapshots | Supported for Airflow 2.x and 1.10.15 versions | Supported | Supported  
Loading Snapshots | Not supported | Supported | Supported  
Scheduled Snapshots | Not supported | [Supported](https://docs.cloud.google.com/composer/docs/composer-2/configure-scheduled-snapshots) | [Supported](https://docs.cloud.google.com/composer/docs/composer-3/configure-scheduled-snapshots)  
Custom environment's bucket | Not supported | [Supported](https://docs.cloud.google.com/composer/docs/composer-2/use-custom-bucket) | [Supported](https://docs.cloud.google.com/composer/docs/composer-3/custom-bucket)  
Saving Airflow task logs only in Cloud Logging | Not supported | [Supported](https://docs.cloud.google.com/composer/docs/composer-2/enable-saving-logs-to-environment-bucket) | [Supported](https://docs.cloud.google.com/composer/docs/composer-3/enable-saving-logs-to-environment-bucket)  
Data lineage integration | Not supported | [Supported](https://docs.cloud.google.com/composer/docs/composer-2/lineage-integration) | [Supported](https://docs.cloud.google.com/composer/docs/composer-3/lineage-integration)  
Composer Local Development CLI tool | Not supported | [Supported](https://docs.cloud.google.com/composer/docs/composer-2/run-local-airflow-environments) | [Supported](https://docs.cloud.google.com/composer/docs/composer-3/run-local-airflow-environments)  
  
## Comparison of Airflow versions

Managed Airflow (Gen 3) provides environments with Airflow 2 and Airflow 3.

### Support for Managed Airflow (Gen 3) features

The following table summarizes Managed Airflow (Gen 3) features that **aren't yet supported** in Airflow 3.

Feature | Status | Description  
---|---|---  
Upgrades to Airflow 3 (snapshots) | Not yet supported in Airflow 3 | Side-by-side migration of existing Managed Airflow (Gen 3) environments from Airflow 2 to Airflow 3 using snapshots.  
Upgrades to Airflow 3 (in-place) | Not yet supported in Airflow 3 | In-place upgrades of existing Managed Airflow (Gen 3) environments from Airflow 2 to Airflow 3 by specifying a version with Airflow 3 during an upgrade.  
  
#### Known issues in Airflow 3

The following known issues have been identified in Airflow 3:

  * Warning messages in the logs of Airflow workloads. These messages can be safely ignored.
  * The `airflowctl` utility can't be easily used from headless environments such as Airflow workers in Managed Airflow or Docker containers. This is a limitation of the utility. For more information about this limitation, see [Issue 58230](https://github.com/apache/airflow/issues/58230) in the Airflow repository on GitHub.



### Support for Airflow 3 features

The following table lists [Airflow 3 features](https://airflow.apache.org/blog/airflow-three-point-oh-is-here/) and their support:

Feature | Status  
---|---  
[Airflow 3.0 UI](https://airflow.apache.org/docs/apache-airflow/stable/ui.html) | Supported  
[DAG versioning](https://airflow.apache.org/blog/airflow-three-point-oh-is-here/#dag-versioning) | Supported  
[Backfills (from Airflow UI)](https://airflow.apache.org/blog/airflow-three-point-oh-is-here/#backfills-improvements) | Supported  
[Event-driven scheduling](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/event-scheduling.html) | Supported  
[Assets](https://airflow.apache.org/docs/apache-airflow/3.0.0/authoring-and-scheduling/assets.html) | Supported  
[Inference execution and hyper-parameter tuning](https://airflow.apache.org/blog/airflow-three-point-oh-is-here/#inference-execution-and-hyper-parameter-tuning) | Supported  
[airflowctl command-line tool](https://pypi.org/project/apache-airflow-ctl/) | Supported  
[DAG bundles (other than LocalDagBundle)](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/dag-bundles.html) | Not yet supported in Airflow 3  
[Edge Executor and tasks in other programming languages](https://airflow.apache.org/blog/airflow-three-point-oh-is-here/#run-anywhere-in-any-language) | Not yet supported in Airflow 3  
  
## Managed Service for Apache Airflow images

To run Apache Airflow, Managed Airflow builds Docker images that bundle Airflow releases with other common binaries and Python libraries.

Managed Airflow images include Airflow modifications that are specific to Managed Airflow and unsuitable for the upstream Airflow codebase. Each Managed Airflow image contains preinstalled packages along with Managed Airflow-specific Airflow changes.

Google periodically releases [new Managed Airflow images](https://docs.cloud.google.com/composer/docs/composer-versions):

  * In Managed Airflow (Gen 3), images include new builds of supported Airflow versions. You can select an Airflow version and a build that you want to use. Your environment gets Managed Airflow improvements automatically.

  * In Managed Airflow (Gen 2) and Managed Airflow (Legacy Gen 1), images include Managed Airflow improvements and new builds of supported Airflow versions. To get Managed Airflow improvements, you upgrade your environment to a later version of Managed Airflow.




## Version deprecation and support

###  Gen 3 

Google supports an [Airflow build](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3) for a period of time after it was released:

  * **0-12 months from the release date** : Managed Airflow (Gen 3) environments running this Airflow build are supported.

  * **12+ months from the release date** : Managed Airflow (Gen 3) environments running these versions are unsupported.

After an Airflow build is no longer supported, environments running this Airflow build are also unsupported and entirely user-managed.


**Deprecated:** In the past, some Airflow builds in Managed Airflow (Gen 3) had their end of support date listed as "To be announced". This approach was deprecated. We're now providing support dates that depend on the date when a particular Airflow build was released. All Airflow builds that didn't have an end of support date when this change was introduced **are supported until July 1, 2026**. Because of this change, some Airflow builds released before July 1, 2025 are supported for longer than the regular support period of 12 months. All builds released after July 1, 2025 use the regular support period. All Airflow builds that had their support date shorter than 12 months are now supported for 12 months since the date of their initial release.

Environments work with supported and unsupported Airflow builds in the following way:

  * You can create environments with all Airflow builds that are supported.

  * You can still use an environment with an Airflow build that is no longer supported. The environment still works, you can keep using it, and you can [upgrade it](https://docs.cloud.google.com/composer/docs/composer-3/upgrade-environments) to a [supported Airflow build](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3).

  * In some cases, an upgrade to a later Airflow version or build is the only available solution for a security vulnerability.




###  Gen 2 

Google supports [Managed Airflow (Gen 2) versions](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2) for a period of time after the version's release:

  * **0-12 months from the release date** : Managed Airflow (Gen 2) environments running these versions are supported.

  * **12+ months from the release date** : Managed Airflow (Gen 2) environments running these versions are unsupported.

**Important:** In some cases, an upgrade to a more recent Managed Airflow and Airflow version is the only available solution for a security vulnerability.



You can use Managed Airflow versions after the date they are no longer supported. For example, if your environment is based on a Managed Airflow version that is past the support period, the environment still works and you can keep using it. In this case, we recommend you to [upgrade](https://docs.cloud.google.com/composer/docs/composer-2/upgrade-environments) your environment to a [supported version](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2).

###  Gen 1 (Legacy) 

New Managed Airflow (Legacy Gen 1) versions were released until the end of March 2023. All released Managed Airflow (Legacy Gen 1) versions follow the same version deprecation policy as Managed Airflow (Gen 2) and are supported according to it.

**Deprecated:** On **March 25, 2024** , Managed Airflow (Legacy Gen 1) entered its post-maintenance mode. Google will not release any further updates to Managed Airflow (Legacy Gen 1), including new versions of Airflow, bugfixes, and security updates. On **September 15, 2026** , all Managed Airflow (Legacy Gen 1) environments will reach their planned end of life, and you will not be able to use them. We recommend [migration to Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/latest/migrate-composer-1-to-3).

## Version schemas

This section describes Airflow and Managed Airflow version schemas and version aliases.

### Airflow version schema

Airflow follows the [semantical software versioning schema](https://semver.org). Each version of Airflow has a _major_ , _minor_ , and _patch_ version.

###  Gen 3 

In Managed Airflow (Gen 3), new Airflow versions and builds become available as the time goes.

Your environment can function with all previous Airflow versions and builds, and receives updates to its infrastructure components automatically. Each version and build is supported as described in Version deprecation and support, and you can choose to upgrade your Airflow version to a later version or build.

###  Gen 2 

For a list of Airflow versions supported in each Managed Airflow version, see the [list of Managed Airflow versions](https://docs.cloud.google.com/composer/docs/composer-versions).

  * In each release, Managed Airflow (Gen 2) supports **two minor versions of Airflow 2**.

For example, Managed Airflow 2.4.0 supports Airflow 2.4.* and Airflow 2.5.*.

**Deprecated:** This approach [is deprecated](https://docs.cloud.google.com/composer/docs/release-notes#July_24_2026). Starting in **September, 2026** , we will **release only new builds of Airflow 2.11** in Managed Airflow (Gen 2).
  * For each minor version of Airflow 2, Managed Airflow **supports one patch version**.

For example, for Airflow 2.4.*, Managed Airflow supports Airflow 2.4.3.

  * When a new patch version of Airflow 2 becomes available in Managed Airflow, the corresponding release has two patch versions of Airflow 2 available for the same minor version of Airflow. The previous patch version is then removed in one of the next releases.

For example, Managed Airflow 2.3.4 supports both Airflow 2.5.1 and Airflow 2.5.3.

  * Managed Airflow can **skip some Airflow patch versions** between releases of Managed Airflow. In addition, if there are functional, quality, or performance issues with a specific patch version of Airflow, Managed Airflow can also skip this version.

For example, Airflow 2.1.3 is skipped and Airflow 2.1.4 is available.

  * A Managed Airflow release running a stable Airflow version can include Airflow updates that are backported from a later Airflow version.




###  Gen 1 (Legacy) 

The latest version of Airflow supported in Managed Airflow (Legacy Gen 1) is Airflow 2.4.3.

Only Managed Airflow (Legacy Gen 1) supports Airflow 1.10.15, which is the latest released version of Airflow 1.

### Managed Airflow version schema

###  Gen 3 

Managed Airflow (Gen 3) versioning schema captures Airflow versions and builds:

**`composer-3-airflow-x.y.z-build.t`**

Where:

  * `composer-3` is the major version of Managed Airflow.

  * `airflow-x.y.z.build.t` is the Airflow version and build. Every next release of the same Airflow version in Managed Airflow (Gen 3) has a higher build number. The build number is defined by Managed Airflow and not by the Airflow open source project.




###  Gen 2 

Managed Airflow (Gen 2) image versioning schema captures Managed Airflow and Airflow versions:

**`composer-2.b.c-airflow-x.y.z`**

Where:

  * `composer-2.b.c` denotes the minor and patch version of Managed Airflow-managed customizations in Managed Airflow (Gen 2). As a general rule, minor versions of Managed Airflow correspond to significant changes in functionality compared to the previous minor version, such as when the available set of Airflow versions is changed. Patch versions are updated in subsequent releases.

  * `airflow-x.y.z` is the Airflow release, it denotes the major, minor, and patch version of Airflow that's used in a specific Managed Airflow image.




###  Gen 1 (Legacy) 

Managed Airflow (Legacy Gen 1) image versioning schema captures Managed Airflow and Airflow versions:

**`composer-1.b.c-airflow-x.y.z`**

Where:

  * `composer-1.b.c` is the version of Managed Airflow-managed customizations
  * `airflow-x.y.z` is the Airflow release



### Version aliases

Version aliases work in the following way:

  * Managed Airflow resolves the version alias to the full format when it creates your environment:

    * All version aliases become `composer-3-airflow-x.y.z-build.t` in Managed Airflow (Gen 3).
    * All version aliases become `composer-a.b.c-airflow-x.y.z` in Managed Airflow (Gen 2) and Managed Airflow (Legacy Gen 1).
  * In Managed Airflow (Gen 3), using a version alias, such as `composer-3-airflow-x.y` **does not automatically upgrade the Airflow version and build** of your environment. The environment stays on the same Airflow build and version until you upgrade it. The environment still receives automatic infrastructure upgrades, as usual.

  * In Managed Airflow (Gen 2) and Managed Airflow (Legacy Gen 1), using a version alias, such as `composer-a-airflow-x.y.z` **does not provide automatic upgrades** for an environment. The environment stays on the same Managed Airflow and Airflow version until you upgrade it.




#### Managed Airflow (Gen 3) version aliases

Managed Airflow (Gen 3) supports the following version aliases:

Alias | Airflow version  
---|---  
`composer-3-airflow-2` | Latest version and build of Airflow 2  
`composer-3-airflow-x.y` | Latest version and build of Airflow within `x.y` major and minor versions  
`composer-3-airflow-x.y.z` | Latest build of the specified version of Airflow  
  
#### Managed Airflow (Gen 2) version aliases

Managed Airflow (Gen 2) supports the following version aliases:

Alias | Managed Airflow version | Airflow version  
---|---|---  
`composer-2-airflow-2` | Latest version of Managed Airflow (Gen 2) | Latest version of Airflow 2  
`composer-2-airflow-x.y` | Latest version of Managed Airflow (Gen 2) | Latest version of Airflow within `x.y` major and minor versions  
`composer-2-airflow-x.y.z` | Latest version of Managed Airflow (Gen 2) | Specified version of Airflow  
`composer-2.b.c-airflow-x.y` | Specified version of Managed Airflow (Gen 2) | Latest version of Airflow available within `x.y` major and minor versions  
  
#### Managed Airflow (Legacy Gen 1) version aliases

Managed Airflow (Legacy Gen 1) supports the following version aliases:

Alias | Managed Airflow version | Airflow version  
---|---|---  
`composer-1-airflow-2` | Latest version of Managed Airflow (Legacy Gen 1) | Latest version of Airflow 2  
`composer-1-airflow-1` | Latest version of Managed Airflow (Legacy Gen 1) | Latest version of Airflow 1  
`composer-1-airflow-x.y` | Latest version of Managed Airflow (Legacy Gen 1) | Latest version of Airflow within `x.y` major and minor versions  
`composer-1-airflow-x.y.z` | Latest version of Managed Airflow (Legacy Gen 1) | Specified version of Airflow  
`composer-1.b.c-airflow-x.y` | Specified version of Managed Airflow (Legacy Gen 1) | Latest version of Airflow available within `x.y` major and minor versions.  
  
The following version aliases point to Managed Airflow (Gen 3). You can still use them, but consider switching to aliases for your version of Managed Airflow.

  * `composer-latest-airflow-x.y` is equal to `composer-3-airflow-x.y`.
  * `composer-latest-airflow-x.y.z` is equal to `composer-3-airflow-x.y.z`.



### Version arguments in Google Cloud CLI

When you [create](https://docs.cloud.google.com/composer/docs/composer-2/create-environments) or [upgrade](https://docs.cloud.google.com/composer/docs/composer-2/upgrade-environments) a Managed Airflow environment using Google Cloud CLI, you can specify Managed Airflow and Airflow versions:

###  Gen 3 

  * `--image-version` argument specifies the Airflow version and build in the `composer-3-airflow-x.y.z-build.t` format. You can use version aliases, which are resolved by Google Cloud CLI into the full format.

  * `--airflow-version` specifies the Airflow version in the following formats:

    * The `x.y.z` format is for the latest build of the specified version of Airflow. This format is equal to the `composer-3-airflow-x.y.z` version alias.

    * The `x.y` format is for the latest build of Airflow available within `x.y` major and minor versions. This format is equal to the `composer-3-airflow-x.y` version alias.

    * `x.y.z-build.t` is the specified version and build of Airflow. This format is equal to `composer-3-airflow-x.y.z-build.t`.




###  Gen 2 

  * `--image-version` argument specifies Managed Airflow (Gen 2) and Airflow versions:

    * `composer-a.b.c-airflow-x.y.z` format creates an environment with the specified versions of Managed Airflow and Airflow.
    * Version aliases first resolve to the `composer-a.b.c-airflow-x.y.z` format and then create an environment with the specified versions of Managed Airflow (Gen 2) and Airflow.
  * `--airflow-version` specifies the Airflow version in the following formats:

    * The `x.y.z` format is for the latest version of Managed Airflow (Gen 2) and the specified version of Airflow. This format is equal to the `composer-2-airflow-x.y.z` version alias.

    * The `x.y` format is for the latest version of Managed Airflow (Gen 2) and the latest version of Airflow available within `x.y` major and minor versions. This format is equal to the `composer-2-airflow-x.y` version alias.




###  Gen 1 (Legacy) 

  * `--image-version` argument specifies Managed Airflow (Legacy Gen 1) and Airflow versions:

    * `composer-a.b.c-airflow-x.y.z` format creates an environment with the specified versions of Managed Airflow and Airflow.
    * Version aliases first resolve to the `composer-a.b.c-airflow-x.y.z` format and then create an environment with the specified versions of Managed Airflow (Legacy Gen 1) and Airflow.
  * `--airflow-version` specifies the Airflow version in the following formats:

    * The `x.y.z` format is for the latest version of Managed Airflow (Legacy Gen 1) and the specified version of Airflow. This format is equal to the `composer-1-airflow-x.y.z` version alias.

    * The `x.y` format is for the latest version of Managed Airflow (Legacy Gen 1) and the latest version of Airflow available within `x.y` major and minor versions. This format is equal to the `composer-1-airflow-x.y` version alias.




## What's next

  * [Managed Airflow images](https://docs.cloud.google.com/composer/docs/composer-versions)
  * [Create an environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments)
  * [Upgrade an existing Managed Airflow environment](https://docs.cloud.google.com/composer/docs/composer-2/upgrade-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 

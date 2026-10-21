---
url: https://docs.cloud.google.com/migrate/anthos/docs/release-notes/
title: Migrate to Containers release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:38:25.725734+00:00
---

# Migrate to Containers release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/anthos/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Resources ](https://docs.cloud.google.com/migrate/containers/docs/resources)



Send feedback 

#  Migrate to Containers release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Migrate to Containers. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/migrateanthos-release-notes.xml) directly. 

## May 06, 2024

v1.15.0

Announcement

The Migrate to Containers UI in the Google Cloud console, `migctl`, and CRDs that used processing clusters to migrate workloads to Google Cloud are no longer available.

To perform migrations, use the Migrate to Containers CLI on your local machine. For more information, see [Migrate to Containers overview](https://www.cloud.google.com/migrate/containers/docs/getting-started).

If you have any questions or require additional support, then reach out to [m2c-external-feedback@google.com](mailto:m2c-external-feedback@google.com).

## January 03, 2024

v1.15.0

Deprecated

The Migrate to Containers UI in the Google Cloud console, `migctl`, and CRDs that use processing clusters to migrate workloads to Google Cloud are now deprecated. They are supported for existing users until May 2024, after which they will no longer be available. If you're new to Migrate to Containers, then use the Migrate to Containers CLI to perform migrations on your local machine. For more information, see [Migrate to Containers CLI architecture](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/architecture).

## November 29, 2023

v1.15.0

Change

Support for IBM WebSphere Application Server migrations has been enhanced. The `websphere-container` plugin now supports WebSphere Application Server traditional as a source and as a target.

v1.15.0

Deprecated

The `websphere-traditional` plugin is now deprecated. For existing customers, it is still supported till December 2023, after which it will no longer be available. If you're new to WebSphere workload modernization, then use the `websphere-container` plugin with the Migrate to Containers CLI instead.

v1.15.0

Announcement

On November 29, 2023 we released version 1.4.0 of the Migrate to Containers modernization plugins.

Learn how to [Upgrade Migrate to Containers plugins](https://docs.cloud.google.com/migrate/containers/docs/upgrade#upgrade_plugins).

v1.15.0

Change

The following changes have been made to the migration plan format for Tomcat workloads:

  * A new field `baseImage` of type `object` has been added that lets you do the following:

    * Specify the Docker community image or provide your own Docker image to use as the base image for the migration using the `baseImage.name` property of type `string`.

    * Specify a custom Tomcat installation path using the `baseImage.catalinaHome` property of type `string`.

  * The `fromImage` field of type `string` has been replaced by the `baseImage.name` property.

  * Two new fields `userName` and `groupName` of type `string` have been added that let you specify a custom user and group under which you want the application to run.




## October 30, 2023

v1.15.0

Change

The plugins for migrating Apache, JBoss, WordPress, and IBM WebSphere traditional applications to containers are now generally available. These plugins provide a streamlined and simplified experience for migrating applications based on these frameworks.

v1.15.0

Announcement

On October 30, 2023 we released version 1.3.1 of the Migrate to Containers modernization plugins.

Learn how to [Upgrade Migrate to Containers plugins](https://docs.cloud.google.com/migrate/containers/docs/upgrade#upgrade_plugins).

## August 22, 2023

v1.15.0

Announcement

On August 22, 2023 we released version 1.3.0 of the Migrate to Containers modernization plugins.

Learn how to [Upgrade Migrate to Containers plugins](https://docs.cloud.google.com/migrate/containers/docs/upgrade#upgrade_plugins).

v1.15.0

Change

Linux system service endpoints are no longer automatically discovered and must be manually specified while [customizing the Linux migration plan](https://docs.cloud.google.com/migrate/containers/docs/customizing-a-migration-plan#service-endpoints).

v1.15.0

Change

The following changes have been made to the discovery parameters for the Tomcat plugin:

  * The `java-version` parameter is now added as input to Tomcat migrations.
  * The `catalina-base` parameter can now include multiple directories delimited with colons (`:`).
  * The `java-version`, `catalina-base` and `catalina-home` parameters are now mandatory.



v1.15.0

Change

The following changes have been made to the IBM WebSphere Application Server migration:

  * Renamed the plugin from `websphere-container` to `websphere-traditional-container`. This plugin now supports WebSphere Application Server Traditional as a migration source.

  * Added support for WebSphere Application Server Liberty as a target.

  * The `was-home` parameter is now mandatory.




## June 27, 2023

v1.15.0

Announcement

On June 27, 2023 we released version 1.2.0 of the Migrate to Containers modernization plugins.

Learn how to [Upgrade Migrate to Containers plugins](https://docs.cloud.google.com/migrate/containers/docs/upgrade#upgrade_plugins).

v1.15.0

Fixed

The following issues were fixed: 

  * Unsupported Apache module caused the migration to get stuck in the generate artifacts phase.
  * Duplicate migration warnings appeared for JBoss Wildfly workloads.
  * Duplicate `sensitiveDataPath` entries found in JBoss Wildfly migration plan.



## May 22, 2023

v1.15.0

Announcement

On May 22, 2023 we released Migrate to Containers 1.15.0.

v1.15.0

Deprecated

In-place processing on Anthos on AWS is no longer supported. You cannot install new versions of Migrate to Containers on Anthos on AWS clusters. To migrate application components of VMs on AWS, you can migrate VMs from AWS to Compute Engine using Migrate to Virtual Machines v5, and then use Migrate to Containers to perform a migration from the created Compute Engine instance. For more information, see the [Migrate to Virtual Machines version 5.0 documentation](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0).

v1.15.0

Deprecated

The use of migration sources based on Migrate to Virtual Machines v4 is no longer supported.

To migrate application components from VMs running on VMWare clusters, you can use Migrate to Virtual Machines v5 integration. For more information, see [Adding Migrate to Virtual Machines as a migration source](https://docs.cloud.google.com/migrate/containers/docs/adding-a-migration-source#adding_as_a_migration_source).

To migrate application components from AWS or Azure use Migrate to Virtual Machines v5 to migrate VMs to Compute Engine, and then use Migrate to Containers to perform a migration from the created Compute Engine instance. For more information, see the [Migrate to Virtual Machines version 5.0 documentation](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0).

v1.15.0

Deprecated

In-place processing on Anthos on VMware is no longer supported. You cannot install new versions of Migrate to Containers on Anthos on VMWare clusters. Instead, you can migrate application components to GKE or Anthos clusters on bare metal using Migrate to Virtual Machines v5 or the local VMWare source respectively.

v1.15.0

Deprecated

The legacy Linux runtime is now deprecated. The generated migration plan now uses the enhanced Linux runtime by default. You can choose to use the legacy Linux runtime, which is planned to be supported until August 2023, by setting the value of the `v2kServiceManager` flag in the migration plan to false.

To see how to convert existing migrations to the new Linux runtime, see [Upgrade container workloads for enhanced runtime](https://docs.cloud.google.com/migrate/containers/docs/convert-runtime).

If you have migrated applications using the legacy runtime, you can install the legacy runtime support using the following command:
    
    
    migctl setup install --runtime

For more information, see [Before you begin deploying a Linux workload to a target cluster](https://docs.cloud.google.com/migrate/containers/docs/deploying-to-target-cluster#before_you_begin).

v1.15.0

Fixed

Enhanced the Windows features filtering to only allow features supported by Windows Docker images to work.

## March 28, 2023

v1.14.1

Announcement

On March 27, 2023 we released version 1.1.0 of the Migrate to Containers modernization plugins. 

Learn how to [Upgrade Migrate to Containers plugins](https://docs.cloud.google.com/migrate/containers/docs/upgrade#upgrade_plugins).

v1.14.1

Feature

Introduced the following features for JBoss migration:

  * Support for JBoss versions has been extended and Migrate to Containers now supports migration of JBoss EAP versions 7.0 - 7.4 to equivalent Wildfly community based container images, besides migrations of Wildfly versions 8.1.0 - 26.1.1.
  * Secrets are now automatically created from extracted security realms configuration and key-stores. This new feature fixes potential security risks and lets you update secrets without having to recreate images.
  * The `targetImageHome` property has been added to the migration plan to allow users to specify an alternative container image with a different `JBOSS_HOME` location.
  * The `ExcludeFiles` property has been added to the migration plan, which lets you explicitly exclude files and directories from the container image.
  * The data migration feature now automates the creation and mounting of a Persistent Volume Claim (PVC) for the `$JBOSS_HOME/standalone/data` directory. This directory is available for use by services that require storing content in the file system.



v1.14.1

Feature

**Preview** : Added support for refactoring WordPress Servers running on Apache2 Linux to containers, which lets you deploy WordPress sites as containers on GKE, GKE Autopilot clusters, Anthos clusters, and Cloud Run. 

For more information, see [Migrate a WordPress site](https://docs.cloud.google.com/migrate/containers/docs/migrating-overview#migrate_a_wordpress_site).

v1.14.1

Fixed

Filtering out files located at `/tmp` when discovering Tomcat application dependencies.

v1.14.1

Issue

Docker images may contain broken symlinks. Ensure that the tar archive artifacts added to dockerfile don't contain symlinks that don't resolve to another file in the archive. If they do, either retrieve the files from the source VM and add them to the dockerfile manually, or replace the symlinks in the source VM and perform extraction again.

## March 20, 2023

v1.14.1

Announcement

On March 20, 2023 we released Migrate to Containers 1.14.1.

v1.14.1

Feature

Migrate to Containers now supports [Workforce identity federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services).

v1.14.1

Announcement

Documentation restructured to provide better visibility of high-level tasks.

v1.14.1

Deprecated

Using Anthos for VMware processing clusters for containerisation of VMware sources is now deprecated and is planned to be supported till July 2023.

v1.14.1

Issue

The following are open issues:

  * `migctl migration status` sometimes prints an error message before the migration table. This message does not indicate a concrete problem and can be ignored.
  * The UI fails when performing "Processing Cluster Add" having Resource Location Org Policy. To overcome that the processing cluster installation should be done using migctl and the target region should be provided using `--gcp-region`.
  * Creation of multiple source providers at the same time might cause timeouts. If this happens, delete and recreate source provider objects that failed to be created.
  * Replicated VM deletion might hang depending on other object deletion. To prevent this from happening, delete the Migrate to Virtual Machines (M2VM) source after deleting the corresponding Migration objects. Otherwise, if this happens, delete the M2VM replications manually.
  * Generated Kubernetes deployment specifications might contain invalid (non-DNS1123 compliant) container names when such names appear in the source VM. To prevent this from happening, go over the migration plan before generating artifacts and change the names to be DNS1123 compliant.



v1.14.1

Fixed

The following issues were fixed:

  * `migctl setup uninstall failure - source snapshot is not deleted`. This is happening when the corresponding source provider was already deleted. 
  * Starting a migration from the UI page "Sources & Candidates" might get stuck on a "retrying" step.



## December 06, 2022

v1.14.0

Announcement

On Dec 6, 2022 we released Migrate to Containers 1.14.0.

v1.14.0

Feature

Enhanced control on the verbosity of backend logs. You can now use the `migctl logging set-verbosity <verbosity>` command, where verbosity `0` corresponds to info logs only and verbosity `1` shows debug logs. See [migctl reference](https://docs.cloud.google.com/migrate/containers/docs/migctl-reference).

v1.14.0

Feature

Support for refactoring Apache 2 Linux based applications to containers, which lets you deploy Apache 2 application components as containers on GKE, GKE Autopilot clusters, Anthos clusters, and Cloud Run, released for Public Preview. See [Migrate Apache 2 Servers](https://docs.cloud.google.com/migrate/containers/docs/migrating-overview#migrate_an_apache_server).

v1.14.0

Feature

Support for refactoring applications running on JBoss Enterprise Application Platform or [WildFly](https://www.wildfly.org/about/) application platform to containers, which lets you deploy the application as containers on GKE, GKE Autopilot clusters, Anthos clusters, and Cloud Run, released for Public Preview. See [Migrate JBoss Servers](https://docs.cloud.google.com/migrate/containers/docs/migrating-overview#migrate_a_jboss_server).

v1.14.0

Deprecated

Containerization from AWS, Azure, and local vSphere (Anthos on vSphere) sources and local processing in AWS clusters are now deprecated and planned to be supported until April 2023.

v1.14.0

Fixed

The following issues were fixed:

  * Windows IIS modernization - In case IIS files are not accessible to BUILTIN/Administrators, the discovery phase of IIS modernization will fail.
  * Support migration of Windows IIS sites where Administrator user has no permissions to access the IIS configuration files.
  * On Linux migrations, if the migration plan YAML is missing the Image section, the task will fail with a panic instead of an indicative message.



v1.14.0

Issue

The following are open issues:

  * migctl migration status sometimes prints an error message before the migration table. This message does not indicate a concrete problem and can be ignored.
  * UI fails when performing "Processing Cluster Add" having Resource Location Org Policy. To overcome that, the processing cluster installation should be done using migctl and the target region should be provided using `--gcp-region`.
  * Two migrations from different M2VM sources on the same VM can affect each other. When using M2VM sources, users should avoid creating multiple Migration objects from different sources at the same time for the same VM.
  * Creation of multiple source providers at the same time may cause timeouts. If this happens users should delete and recreate source provider objects that failed to be created.
  * Replicated VM deletion can hang depending on other object deletion. To prevent this from happening users should delete M2VM source after deleting the corresponding Migration objects. Otherwise, if this happens users should delete the M2VM replications manually.
  * migctl setup uninstall failure - source snapshot is not deleted. This is happening when the corresponding source provider was already deleted. If this happens users should recreate the corresponding source provider and after migrations are removed to proceed with uninstalling.
  * Starting a migration from the UI page "Sources & Candidates" might get stuck on a "retrying" step. If this happens users should create a Migration using the VM name as input.



## September 20, 2022

v1.13.0

Announcement

On Sep 20, 2022 we released Migrate to Containers 1.13.0

v1.13.0

Feature

Support for refactoring Tomcat applications to containers, which lets you deploy Tomcat application components as containers on GKE, GKE Autopilot clusters, Anthos clusters and Cloud Run, has moved from the Public Preview stage to General Availability.

v1.13.0

Feature

Added Kubevirt UEFI support. Virtual machines with UEFI firmware can now be migrated without user interaction. Migrations to Anthos VM Runtime that previously failed due to this limitation will need to be recreated.

v1.13.0

Feature

Added periodic health checks for migration sources to assure migration source availability and health. Migrate for Containers periodically checks the status of the source providers to reflect potential problems such as missing service accounts or lack of permissions. This enhancement helps ensure smooth operation and alerts you of failure cases.

v1.13.0

Feature

New progress indication to Migrate to Containers CLI tool - Running `migctl migration status` displays the progress of snapshot creation stage, upload progress of generate artifact stage, and for Linux migration, the progress of packing the image file.

v1.13.0

Feature

Windows IIS Application modernization:

  * Added support for Windows services. This allows you to specify Windows services that should be part of the migrated Windows IIS application. With this new capability you can migrate Windows IIS applications that are dependent on other windows services.

  * Added support for generation of Kubernetes health probes. Health probe monitoring can help reduce the downtime of your application and provide better service monitoring. Migrate for Containers creates the required probes section in the deployment YAML. The Windows IIS health probes are enabled by default and can be disabled or modified while customizing the migration plan.

  * Added support for automated COM object registration. Windows DLLs that contain COM objects are copied to the target image and are automatically registered as a COM object.




v1.13.0

Fixed

The following issues were fixed:

  * Removed support for Windows SAC images following Microsoft announcement concerning Windows Server Semi-Annual Channel end of servicing.

  * Propagate discovery failures into the migration status.

  * Don't show the warning `skipping setup of default image and artifact repositories because either --json-key, --gcp-project or --gcp-region weren't specified` when all parameters are given on Anthos on Bare Metal installations.

  * The v2k-websphere image is now up-to-date (the promoted one).

  * Separated the logic of creating a source and validating its status. When creating an unhealthy source, the create command would succeed with an indication that there is a problem in the source.




v1.13.0

Issue

The following are open issues:

  * If IIS files are not accessible to BUILTIN/Administrators, the discovery phase of IIS modernization will fail.

  * Support migration of Windows IIS sites where Administrator user has no permissions to access the IIS configuration files.

  * On Linux migrations, if the migration plan YAML is missing the Image section, the task will fail with a panic instead of an indicative message. 

  * On Migrate for Compute Engine, source creation can fail because it's unable to find a secret caused by a race issue of the reconciler and the secret creation. Workaround: reconciler should be updated of the new secret after a few minutes. `Error: Source mysrc was created with an error: Secret <some_secret> not found`

  * On Tomcat, if path X is defined on excludeFiles, and its ancestor directory is defined on additionalFIles, we will migrate X instead of excluding it. 

  * When using Migrate for Compute Engine 5 as a migration source, if two Migrate To Container sources were created referring to the same Migrate for Compute Engine source, migrations created from both sources may interfere with each other. Workaround: delete one of the sources.




## July 13, 2022

v1.12.0

Feature

**List the source inventory for Google Compute Engine, local-vmware, and Migrate for Compute Engine 5.x sources**

Migrate to Containers has added support for the inventory listings of VMs in connected sources. Users can list an inventory of the VMs in connected Migrate to Containers sources. The new inventory listings are available for Google Compute Engine, local-vmware, and Migrate for Compute Engine v5.0 sources.

v1.12.0

Feature

**Support for local-ovf sources**

Migrate to Containers has added support for creating Anthos VM runtimes from local OVF files. This enables users to modernize VMs to the Anthos VM Runtime by importing their OVF file into their local Anthos bare metal cluster using Migrate to Containers.

v1.12.0

Feature

**Modernize VMs to run Anthos for VMs (A4VM)**

Migrate to Containers has added a new modernization feature, which enables traditional VMs to run on Anthos for VMs. Anthos for VMs extends Anthos on bare metal (now known as Google Distributed Cloud Virtual) to let you run and manage containers and VMs on a unified, Google Cloud-connected platform in your data center or at the edge. For more information on this feature, see [About Anthos for VMs](https://docs.cloud.google.com/anthos/a4vm/docs/concepts/about_a4vm).

v1.12.0

Announcement

**Improved migration flow and task APIs**

A new structured method for generalizing the Migrate to Containers containerization process is available. The new structure provides more flexibility and more granular control of the automated containerization process. The new structure enables users to customize the process and enables support for additional software framework modernization. The following containerization tasks elements are available:

  * AppXGenerateArtifactsTask 
  * AppXGenerateArtifactsFlow



The following migration types are now deprecated and planned to be removed in version 1.13. The corresponding AppX objects and parameters can be used to perform migration for these workload types:

  * `system` \- Legacy linux migrations
  * `iis` \- Legacy windows IIS migrations



The following APIs (CRDs) have been deprecated since version 1.11 and are planned to be removed in version 1.13:

  * [GenerateArtifactsFlow CRD](https://docs.cloud.google.com/migrate/containers/docs/generateartifactsflow-crd)
  * [GenerateArtifactsTask CRD](https://docs.cloud.google.com/migrate/containers/docs/generateartifactstask-crd)
  * [WindowsGenerateArtifacts CRD](https://docs.cloud.google.com/migrate/containers/docs/windows-generateartifacts-crd)
  * [WindowsGenerateArtifactsTask CRD](https://docs.cloud.google.com/migrate/containers/docs/windows-generateartifactstask-crd)



## June 21, 2022

v1.11.0

Fixed

`migctl` fails to get artifacts getting EOF from storage provider.

v1.11.0

Fixed

In some cases where strict network policies were applied, GKE failed to apply AppArmor profiles which are needed for M2C and failed to upgrade, causing the cluster to be in an usable state.

v1.11.0

Fixed

Wrong default value was set for serverautostart in Windows IIS migration. sites were not started in some cases.

v1.11.0

Fixed

Prevent concurrent migrations on the same migrating VM. In rare cases, when doing two m4ce migrations on the same source VM, both migrations could fail due to interfering with each other's operations.

v1.11.0

Feature

**Migration fit assessment**

Migrate to Containers offers a fit assessment tool that runs on a VM workload to determine the workload's fit for migration to a container. To learn more about the tool see, [Using the fit assessment tool](https://docs.cloud.google.com/migrate/containers/docs/fit-assessment).

v1.11.0

Feature

**Tomcat health probes**

Tomcat deployments will use Kubernetes readiness and liveness probes by default. Users can disable or modify those probes while editing the migration plan. Use health probes to provide better pod management and reduce down time during scaling and rolling updates. To learn more about the available probes, see [Set Tomcat health probes](https://docs.cloud.google.com/migrate/containers/docs/tomcat/tomcat-customizing-a-migration-plan#set_tomcat_health_probes).

v1.11.0

Feature

**Linux Service Manager health probes**

Linux Service Manager deployments will use Kubernetes readiness and liveness probes by default. Users can select which services are probed while editing the migration plan. Use health probes to provide better pod management and reduce down time during scaling and rolling updates. To learn more about the available probes, see [Set Linux v2kServiceManager health probes](https://docs.cloud.google.com/migrate/containers/docs/customizing-a-migration-plan#set_linux_v2kservicemanager_health_probes).

v1.11.0

Feature

**Windows features**

The following functions were added to the Windows IIS migration flow:

  * MSVC Runtime support - The migration flow will discover Microsoft Visual C++ runtime libraries installed on the source VM and will allow installing these runtimes on the migrated container.
  * PATH environment variable extraction - The migration flow will discover additional PATH variable entries and will add them to the PATH variable in the migrated container.



v1.11.0

Feature

**Inventory retrieval for Local VMWare, Google Compute Engine, and Migrate for Compute Engine v5 source providers**

A VM inventory is now available for local VMWare, Google Computer Engine, and Migrate 4 Computer Engine v5 source providers and is accessible through both Cloud Console and `migctl`. Using this feature, the list of candidate VMs for migration can be viewed for a given source, including the VM ID required to start a new migration.

  * To access the inventory through Cloud Console: go to your sources page, and select a source from the dropdown.

  * To access the inventory through migctl run the `migctl source list-vms <my-source>` command.




## May 17, 2022

v1.11.1

Feature

**Tomcat improvements**

  * On the migration plan `fromImage` field, in case the tool did not automatically discover the Tomcat version used on original VM, a placeholder text (example: `tomcat:<TomcatVersion>-jre11-openjdk`) was added that would need to be populated by the user. If the information is not populated a blocking warning will be surfaced on Artifacts generation step, requiring the user to provide the Tomcat version details.

  * Renaming `catalinaHome.tar.gz` artifact to `tomcatServer.tar.gz`.

  * `bin` and `lib` directories are filtered from the `tomcatServer.tar.gz` file.

  * Users can now choose to upload certificates into the repository by setting on the migration plan the `includeSensitiveData` parameter to true.




v1.11.1

Fixed

**224545749:** Linux system container extraction step getting stuck in some scenarios.

v1.11.1

Issue

Uninstall might be stuck when a sourcesnapshot CRD cannot be deleted. To workaround please run `kubectl edit sourcesnapshot -n v2k-system` and remove all finalizers

v1.11.1

Issue

**218855996:** Windows global path variables and short folders names are not migrated

v1.11.1

Feature

**Artifact Repository Health Checks**

  * When creating a new artifacts repository, or updating an existing one, migctl will wait for health information and produce a warning in case the provided service account does not have permissions to upload artifacts to the specified bucket. To skip the synchronous health checks, –async can be passed to the migctl command.

  * When creating a new migration, migctl will query the migration's specified artifact repository (or the default if it was not specified), and produce a warning in case the provided service account does not have permissions to upload artifacts to the specified bucket.

  * When generating artifacts for the migration, migctl will query the migration's specified artifact repository (or the default one if it was not specified), and produce a warning in case the provided service account does not have permissions to upload artifacts to the specified bucket.




v1.11.1

Feature

**Building and deploying Windows containers with Skaffold**

Skaffold yamls generated as part of the migration artifacts for Windows flow now help operators to accelerate container image build and deploy to GKE and Anthos clusters.

v1.11.1

Fixed

**220853359:** ABM can be installed without specifying all of `–gcp-project`, `–gcp-region` and `–json-sa`. In this case the default repositories are simply not created.

v1.11.1

Issue

**223553376:** Secrets created by migctl (for example when creating a source provider) may not always be cleaned up when the objects that depend on them are deleted (for example when issuing `migctl source delete …`).

v1.11.1

Issue

**216537540:** migctl cannot be used to upgrade the m2c installation newer than the migctl version. For example, if migctl is 1.9.0, it cannot upgrade a cluster to have 1.11.0.

v1.11.1

Fixed

**227137961:** Prevent concurrent migration on the same migrating VM when using M4CE5.X source.

v1.11.1

Fixed

**224485583:** null value of `serverautostart` for some Windows migration plans.

v1.11.1

Issue

**208361449:** Artifact repository Health checks are not implemented for S3 repositories. Migctl commands that query the health state of the repository will warn that health checks cannot be performed.

v1.11.1

Feature

**V1 API**

Migrate for Anthos and GKE API has graduated to v1 in 1.11.1 release. The v1beta2 Migration API is deprecated and will be supported until May 2023.

v1.11.1

Fixed

**225638684:** OpenLiberty containers may fail to run web applications deployed as WAR archives.

v1.11.1

Issue

**204879458:** If image repository permissions are invalid, migration will get stuck in ExtractImage instead of UploadImage step

v1.11.1

Issue

Migctl may fail installation on GKE clusters with the following error:
    
    
    Error: failed creating Cloud Storage bucket (-migration-artifacts) for Migration artifacts, 
    googleapi: Error 400: Invalid bucket name: '-migration-artifcats', invalid
    

In this case, please uninstall and install with the `--gcp-project` and `--gcp-region` flags.

## March 28, 2022

v1.11.0

Feature

**Splitting IIS sites into individual containers**

Previously to break down N discovered IIS sites into individual containers, you had to manually edit the migration plan to include one site at a time and generate containers artifacts N times. This new feature enables automatic breakdown of N discovered sites into N individual containers in one iteration through a parameter on the migration plan. For more information, see [Split a single VM into multiple containers](https://docs.cloud.google.com/migrate/anthos/docs/windows/customizing-a-migration-plan#split_a_single_vm_into_multiple_containers).

v1.11.0

Feature

**Building and deploying containers with Skaffold**

Skaffold yamls generated as part of the migration artifacts for Tomcat, WebSphere and Linux system container flows now help you to accelerate container image builds and deployments to GKE and Anthos clusters

v1.11.0

Feature

**Replatform Tomcat applications to containers enhancements**

The Tomcat application replatforming flow now enables you to manually specify a Tomcat server installation directory before the migration. This allows you to override the related automatic discovery in cases where you know and would like to provide an exact location. For more information see, [Adding a target project](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/how-to/target-project).

v1.11.0

Feature

**In-place migration on Anthos Bare Metal Clusters**

Support has been added for implementing Anthos clusters on Bare Metal as processing clusters to perform migrations for on-premise workloads. This public preview offering will serve customers who would like to deploy on-premises workloads on Anthos Bare Metal clusters allowing the migration to containers to take place on-premise as well. For more information see, [Configuring a processing cluster on Anthos on Bare Metal](https://docs.cloud.google.com/migrate/anthos/docs/configuring-a-cluster-abm).

v1.11.0

Feature

**Migrate for Compute Engine v5.0 as a migration support**

Currently, Migrate for GKE and Anthos uses Migrate for Compute Engine 4.X to enable workload migration from VMWare on-premise, AWS EC2, and Azure VM environments to Google Cloud. To simplify setup and elevate the operator experience migrating from inventories in these environments, we now offer using the new Migrate for Compute Engine v5.X managed service. This new integration is now in public preview. For more information, see [Enabling Google services and configuring service accounts](https://docs.cloud.google.com/migrate/anthos/docs/config-dev-env).

v1.11.0

Feature

**Replatform Websphere applications to containers**

Version 1.11 introduces a new public offering for replatforming VMs based on WebSphere applications into containers using tWAS (traditional WebSphere Server) container image or Open Liberty community images. Migrate for Anthos and GKE now enables: * Detecting VMs that host WebSphere servers * Discovering WebSphere applications using the IBM binary scanner tool * Splitting the applications into individual containers to increase agility in deployment and operation management * Generating docker file, deployment spec and other artifacts that support deployment to Google modern application platforms and Day2 operations.

v1.11.0

Fixed

**194186514** : Resolved migrations done in Anthos on AWS might succeed even though the files were not uploaded.

v1.11.0

Fixed

**208040681** : Resolved operating system field 'disappearing' after running guest level discovery.

v1.11.0

Issue

**223553376** : Secrets created by migctl, for example when creating a source provider, may not always be cleaned up when the objects that depend on them are deleted. For example when issuing `migctl source delete`.

v1.11.0

Issue

**218855996** : Windows global path variables and short folders names are not migrated.

v1.11.0

Issue

**225638684** : OpenLiberty containers may fail to run web applications deployed as WAR archives.

v1.11.0

Issue

Uninstall might be stuck when a sourcesnapshot CRD cannot be deleted. To workaround this please run `kubectl edit sourcesnapshot -n v2k-system` and remove all finalizers

v1.11.0

Issue

**204879458** : If image repository permissions are invalid, the migration will get stuck in the `ExtractImage` step instead of the `UploadImage` step

v1.11.0

Issue

**216537540** : `migctl` cannot be used to upgrade the Migrate installation newer than the `migctl` version. For example, if `migctl` is version 1.9.0, it cannot upgrade a cluster to 1.11.0.

## January 08, 2022

v1.10.0

Feature

**Windows connection strings**

Migrate for Anthos and GKE supports connection strings at the site and global scopes. See [Setting connection strings for a data provider](https://docs.cloud.google.com/migrate/anthos/docs/windows/customizing-a-migration-plan#connect-string) for more information.

v1.10.0

Fixed

**211625398** : GKE 1.22 support

v1.10.0

Feature

**Reducing system container image size**

New alerts have been added to the migration plan to alert you when files may be too large for a successful image. See [Specifying content to exclude from the migration](https://docs.cloud.google.com/migrate/anthos/docs/customizing-a-migration-plan#specifying_content_to_exclude_from_the_migration) for more information.

## December 22, 2021

v1.10.0

Security

**Security updates**

1.10.1 Security updates available. See [Upgrading Migrate for Anthos and GKE](https://docs.cloud.google.com/migrate/anthos/docs/upgrade) for upgrade instructions.

## December 08, 2021

v1.10.0

Feature

**Fit assessment for Tomcat application servers workloads**

The fit assessment tool now supports assessments of Linux workloads running Tomcat application servers. The new assessment capability allows users to inspect their Tomcat applications for automated containerization to GKE, GKE Autopilot, or Cloud Run

v1.10.0

Feature

**Replatform Tomcat applications to containers**

Version 1.10 introduces a new public offering for replatforming VMs based on Tomcat applications into containers using Apache Tomcat OSS community images. Migrate for GKE now enables: * Detect VMs that host Tomcat web servers and indicate their fit level for containerization. * Discover Tomcat applications as part of the migration processing and their breakdown into individual containers over the Tomcat community images.

See [Migrating Tomcat Workloads](https://docs.cloud.google.com/migrate/anthos/docs/public-preview/tomcat-migration) Migrating Tomcat Workloads.

v1.10.0

Feature

**Fit assessment of Google Compute Engine VM workloads**

The fit assessment tool now supports assessment of Google Compute Engine VM workloads by running the collection scripts directly on the assessed Google Compute Engine VM, or through a remote SSH from the CLI. The new assessment feature enables users to inspect their workload for automated containerization to GKE, GKE AutoPilot and Cloud Run using Migrate For Anthos and GKE.

v1.10.0

Feature

**Assessment of workloads for Shift to Google Compute Engine**

Added support for assessing Lift & Shift migrations to Google Compute Engine. The fit assessment tool is enhanced with additional assessment capabilities which can indicate a VM's fit score toward a Lift & Shift migration using [Migrate for Compute Engine](https://docs.cloud.google.com/migrate/compute-engine). The fit assessment report provides users recommended actions based on conditions that can impact automated migration. With the advanced details users can choose the best workloads for migration and fix issues before they impact the automated migration process.

v1.10.0

Feature

**Source platform indication and VM path on Fit Assessment reports**

The fit assessment reports in HTML and Cloud Console include information on the source platform of the assessed VM, and a unique ID per platform. This allows users to compare and view information on their assessed workloads from various platforms.

v1.10.0

Feature

**Assessment for containerization on Cloud Run**

The fit assessment tool now supports assessments of workloads for containerization to Google [Cloud Run](https://docs.cloud.google.com/run) \- A Google cloud fully managed serverless platform. The new assessment allows users to inspect their workloads for automated containerization using [Migrate for Anthos and GKE](https://docs.cloud.google.com/migrate/anthos).

v1.10.0

Feature

**Assessment for containerization on GKE Auto Pilot**

The fit assessment tool now supports assessments of workloads for containerization to [GKE Auto Pilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) \- A new mode of operation in Google Kubernetes Engine (GKE) that is designed to reduce the operational cost of GKE clusters. The new assessment capability allows users to inspect their workloads for automated containerization to GKE Auto Pilot using [Migrate for Anthos and GKE](https://docs.cloud.google.com/migrate/anthos).

v1.10.0

Feature

**Using RVTools output as a data source for fit assessment**

The fit assessment tool now supports analyzing the RVTools .xlsx report file from a single VMware vCenter by running `$./mfit discover rvtools name.xlsx`. RVTools utilities are used to retrieve VMWare VSphere management data. With the RVTools data source users can easily generate detailed fit assessment reports based on their existing RVTools export.

v1.10.0

Feature

**Fit assessment automatic version checks**

The fit assessment tool now checks for the availability of a new version by probing a version check Google Cloud Storage resource.

v1.10.0

Feature

**Migrate to GKE Autopilot clusters and Cloud Run now in GA**

Simplified Linux service manager, which lets you deploy containers to GKE Autopilot clusters and to Cloud Run, is now the default service manager for any migrations performed with Migrate for Anthos and GKE.

See [Migrating to Autopilot clusters and Cloud Run](https://docs.cloud.google.com/migrate/anthos/docs/services-manager) for more on these new features.

v1.10.0

Feature

**Fit assessment of AWS EC2 workloads**

The fit assessment tool now supports assessments of AWS EC2 workloads by running the collection scripts directly on the assessed AWS EC2 VM, or through a remote SSH from the CLI. The new assessment feature enables users to inspect their workload for automated containerization to GKE, GKE AutoPilot and Cloud Run using Migrate For Anthos and GKE.

v1.10.0

Fixed

**206772515** : Fixed a bug where ** in a v2kServiceManager log path was not supported.

v1.10.0

Fixed

**190575888** : Design updates to mFIT HTML report, fonts changes, layout bugs and graphs position on report.

v1.10.0

Fixed

**205159324** : Fixed a bug where `services-config.yaml` was not created even when the migration completed successfully in the new Linux system container runtime.

v1.10.0

Fixed

**205159086** : On newer Ubuntu versions migrated workloads will fail.

v1.10.0

Fixed

**199382909** : Data migration plans will not have comments when using the UI.

v1.10.0

Fixed

**190704603** : Change to mFIT CLI Help text - 'Import collector script artifacts'.

v1.10.0

Issue

**208040681** : Operating system field 'disappears' after running guest level discovery.

v1.10.0

Issue

Uninstall might be stuck when a sourcesnapshot CRD cannot be deleted. To workaround please run `kubectl edit sourcesnapshot -n v2k-system` and remove all finalizers

v1.10.0

Issue

**204879458** : If your image repository permissions are invalid, migration will get stuck in ExtractImage instead of the UploadImage step.

v1.10.0

Issue

**194186514** : Migration done in Anthos on AWS might succeed even though the files were not uploaded.

## October 05, 2021

v1.9.0

Feature

**Containerize to GKE Autopilot and GKE Cloud Run now in GA**

Adding non-privileged lightweight system init with a simplified Linux service manager has moved from the Public Preview stage to General Availability. This feature allows you deploy containers to GKE Autopilot clusters as well as to Cloud Run. The new non-privileged system init replaces the previous design, which was based on nested containers, with a new system init based on Linux Containers (LXC) that has a smaller footprint.

v1.9.0

Feature

**Fit assessment tool now in GA**

The migration fit assessment tool has moved from the Public Preview to General Availability. The migrate fit assessment tool helps users assess their workloads' fit for containerization. The provides users with detailed technical insights and a fit score per workload. The HTML fit assessment report enables users to easily share assessment data offline. The JSON file report allows them to view their assessment directly on the cloud console.

v1.9.0

Fixed

**187922406** Fixed LVM mount failure caused from broken device mapper devices.

v1.9.0

Fixed

**196712456, 201610944** [MFIT] Minor html report UI improvements.

v1.9.0

Fixed

**197432816** [MFIT] More granular assessment of supported Windows versions.

v1.9.0

Fixed

**194605214** Use controller storage by default for pod log collection for logging migration tasks. Setup max log file size and file rotation.

v1.9.0

Fixed

**197206783** [MFIT] Fixed failure to run guest collect script via SSH with a non-root remote user.

v1.9.0

Fixed

**198092293** [MFIT] vSphere level <-> guest level data correlation failure with certain NIC configurations.

## August 17, 2021

v1.8.1

Fixed

**183082390** : The collection script used by the Linux discovery tool uses `service --status-all` to query system V services. This call no longer takes an arbitrary amount of time to return.

v1.8.1

Feature

When you generate the migration artifacts, Migrate for Anthos and GKE now generates the new `logs.yaml` file from the migration plan. This file contains the list of log files detected on the source VM. You can now edit the `logs.yaml` file to configure logging and the data written to Cloud Logging.

See [Customizing log data written to Cloud Logging](https://docs.cloud.google.com/migrate/anthos/docs/customizing-a-migration-plan#log-files) for more.

v1.8.1

Fixed

**179171930** : A migrated container workload can now be deployed to a cluster running GKE 1.20 and later.

Before you run your migrated workloads, you must install `migctl` with runtime support for [Container-Optimized OS nodes](https://docs.cloud.google.com/container-optimized-os/docs) on your cluster:

`migctl setup install --runtime`

See [Deploying a Linux workload to a target cluster](https://docs.cloud.google.com/migrate/anthos/docs/deploying-to-target-cluster) for more information.

v1.8.1

Fixed

**183564181** : When you call `migctl setup upgrade` on Anthos clusters on VMware or Anthos clusters on AWS without the necessary platform argument (`--gkeop` or `--gke-on-aws`), `migctl` no longer uninstalls Migrate for Anthos and GKE.

v1.8.1

Feature

Version 1.8 added the initial support for the preview release of the enhanced runtime, which lets you deploy containers to GKE Autopilot clusters and to Cloud Run. This release adds the following new features to the preview: 

  * You no longer set an annotation in the migration plan to enable the enhanced runtime. Instead, you now set `v2kServiceManager`. 
  * The environment variable `HC_GAMMA_RUNTIME` has been renamed to `HC_V2K_SERVICE_MANAGER`.
  * The `prestart` and `poststart` entries in the `config.yaml` file now automatically populated. 
  * Added support to the `config.yaml` file that lets you specify environment variables at the global level or at the application level. 
  * Added logging support that lets you customize log data written to Cloud Logging. 



See [Enhanced runtime](https://docs.cloud.google.com/migrate/anthos/docs/enhanced-runtime) for more on these new features

v1.8.1

Fixed

**171686793** : The `migctl setup upgrade --gkeop` command no longer creates a new ImageRepositiry or ArtifactRepository object that lacked Google Cloud access credentials.

v1.8.1

Fixed

**179028669** : `migctl doctor` no longer crashes if a GKE cluster is currently repairing.

v1.8.1

Change

The `cos-runtime` option to the [migctl setup install](https://docs.cloud.google.com/migrate/anthos/docs/migctl-reference#migctl-setup-install) command has been renamed to `runtime`.

v1.8.1

Feature

Version 1.8 added the initial support for the preview release of the fit assessment tool. The fit assessment tool for version 1.8.1 adds new functionality, including:

  * Ability to collect data for a Windows VM
  * Ability to remotely collect data for Linux and Windows VMs using VMware tools
  * Ability to remotely collect data over SSH



See [Using the fit assessment tool](https://docs.cloud.google.com/migrate/anthos/docs/fit-assessment) for more.

v1.8.1

Fixed

**166014117** : The documentation has been updated to describe how to delete the migration to free up the source VM after a successful migration. See [Deleting a migration](https://docs.cloud.google.com/migrate/anthos/docs/deploying-to-target-cluster#delete-migration) for more.

v1.8.1

Feature

Added support for specifying [connection strings](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/connection-string-syntax) when migrating a Windows workload. Connection strings define a connection from the migrated container workload to a .NET Framework data provider. 

See [Setting connection strings for a data provider](https://docs.cloud.google.com/migrate/anthos/docs/windows/customizing-a-migration-plan#connect-string) for more.

v1.8.1

Issue

**197206783** : The user credentials passed to the `mfit discover ssh ...` command must be the credentials of the root user on the VM. Running the command as a non-root user executes the command successfully, but only collects a small part of the data required for a full assessment.

v1.8.1

Issue

**194186514** : When using Anthos clusters on AWS as the processing cluster to perform migrations of AWS workloads, if you have insufficient credentials to create an ECR repository, sometimes the migration succeeds. However, the ECR repository is not created.

**Workaround** : Update your credentials, then recreate and retry the migration.

## June 29, 2021

Feature

Added support for the preview release of the _fit assessment tool_ that is intended to eventually replace the existing [Linux discovery tool](https://docs.cloud.google.com/migrate/anthos/docs/linux-assessment-tool). The new fit assessment tool provides you with:

  * Ability to get the inventory information about VMware VMs through direct connection to vCenter.
  * Enhanced HTML output that makes it easier to view the assessment results.
  * New collection script, `mfit_linux_collect.sh`, and new assessment tool, `mfit`.



See [Using the fit assessment tool](https://docs.cloud.google.com/migrate/anthos/docs/fit-assessment) for more.

Issue

**179171930** : A migrated container workload cannot be deployed to a cluster running GKE 1.20 and later.

Issue

**195341095** : Migrate for Anthos and GKE does not support software RAID disks.

Feature

Enhanced runtime support added which lets you deploy containers to GKE Autopilot clusters and to Cloud Run, and simplifies the process of deploying containers to Anthos clusters on AWS that use workload identity. This feature is in preview.

See [Enhanced runtime](https://docs.cloud.google.com/migrate/anthos/docs/enhanced-runtime) for more.

Issue

**166014117** : If you are using Migrate for Compute Engine with Migrate for Anthos and GKE to migrate Linux workloads, after you complete a successful migration, delete the migration to free up the source VM.

Fixed

**179976237** : You can now create a Docker image file registry configuration with the name of a previously deleted configuration.

Issue

**187922406** : A migration might fail due to a LVM (Logical Volume Manager) failure.

**Workaround** : Recreate and retry the migration.

## May 19, 2021

v1.7.5

Feature

New rule added to the Linux discovery tool to display information when multiple NICs are detected because multiple NICs can increase the effort required to migrate the workload. For a complete list of updates and information on using the new tool, see [Using the Linux discovery tool](https://docs.cloud.google.com/migrate/anthos/docs/linux-assessment-tool).

v1.7.5

Fixed

**162275866:** When generating migration artifacts, you no longer see the following error:

`Error: failed to update vgenerateartifactsflow.kb.io`

v1.7.5

Fixed

**186512095:** When building a Windows container, you no longer have to edit the generated Dockerfile to change the image tag to `latest`.

v1.7.5

Feature

A generated migration plan now contains entries for Service endpoints and NFS mounts discovered on the source VM. You can now edit the migration plan to add, remove, or delete these entries. See [Customizing a migration plan](https://docs.cloud.google.com/migrate/anthos/docs/customizing-a-migration-plan) for more.

v1.7.5

Change

Removed from the legacy PV-based Migrate for Anthos versions a Webhook that was simplifying the definition of Migrate for Anthos pods. This Webhook was not being used in any subsequent versions, including the latest 1.6 and 1.7 releases.

v1.7.5

Fixed

**185975192:** Webhook certificates no longer expire after one month. An expired certificate caused API requests to fail.

v1.7.5

Change

Following the Microsoft decision to end support for the [Windows 10, version 1909](https://docs.microsoft.com/en-us/lifecycle/announcements/windows-10-1909-end-of-servicing) architecture, the Google Kubernetes Engine (GKE) team removed support for this architecture on its GKE and Anthos clusters. This change means that you must update all Windows containers built for this architecture.

When migrating Windows workloads, you have to perform the following:

  * If you have existing Windows containers that you created using Migrate for Anthos version 1.7 or earlier, then you have to rebuild the containers to create containers capable of running on supported Windows architectures.

  * If you are currently using Migrate for Anthos to migrate Windows workloads, you must update your Migrate for Anthos processing clusters to use version 1.7.5 and update the node pools to use the supported Windows architecture.




### Rebuild deployed Windows containers

If you have existing Windows containers created using Migrate for Anthos version 1.7 or earlier, rebuild the container to use a supported Windows architecture. You require the generated artifacts folder generated for the container to make this change:

  1. At the top of the Dockerfile in the generated artifacts folder, edit the `FROM` command to update the image. 

For example, for the following `FROM` command:

`FROM mcr.microsoft.com/windows/servercore/iis:windowsservercore:1909`

Replace the image as shown below: 

`FROM mcr.microsoft.com/windows/servercore/iis:latest`

The following table shows the existing image and the image used to replace it:


Existing image name | New image name  
---|---  
mcr.microsoft.com/windows/servercore:1909 | mcr.microsoft.com/windows/servercore/iis:latest  
mcr.microsoft.com/windows/servercore/iis:windowsservercore-1909 | mcr.microsoft.com/windows/servercore/iis:latest  
mcr.microsoft.com/dotnet/framework/aspnet:3.5-windowsservercore-1909 | mcr.microsoft.com/dotnet/framework/aspnet:3.5  
mcr.microsoft.com/dotnet/framework/aspnet:4.8-windowsservercore-1909 | mcr.microsoft.com/dotnet/framework/aspnet:4.8  
mcr.microsoft.com/dotnet/framework/wcf:4.8-windowsservercore-1909 | mcr.microsoft.com/dotnet/framework/wcf:latest  
  
  1. Rebuild the container images as described at [Building the container image](https://docs.cloud.google.com/migrate/anthos/docs/windows/build-container-image#building_the_container_image).



### Update your Migrate for Anthos processing clusters

If you are currently using Migrate for Anthos to migrate new Windows workloads, you must update your version of Migrate for Anthos to 1.7.5 and update your processing cluster to use a node pool of type `WINDOWS_LTSC`. Node pools of type `WINDOWS_SAC` are no longer supported.

To update your processing cluster:

  1. [Update your version of Migrate for Anthos to 1.7.5](https://docs.cloud.google.com/migrate/anthos/docs/upgrade).

  2. On your processing cluster, replace the `WINDOWS_SAC` node pool with `WINDOWS_LTSC`.

     1. Add the `WINDOWS_LTSC` new pool:
            
            --project=project-name --zone=gcp-zone --cluster=cluster-name \
            --image-type=WINDOWS_LTSC --num-nodes=1 --scopes="cloud-platform" \
            --machine-type=n1-standard-4```
            

     1. Delete the `WINDOWS_SAC` node pool:

**Note:** You can determine the name of the node pool that each node in your cluster belongs to, as well as the name of the node`s architecture, by running`kubectl describe nodes` command while authenticated to the cluster. 
            
            --project=project-name --zone=gcp-zone --cluster=cluster-name```
            




## April 06, 2021

v1.7.0

Issue

**183564181:** When you call `migctl setup upgrade` on Anthos clusters on VMware or Anthos clusters on AWS without the necessary platform argument (`--gkeop` or `--gke-on-aws`), `migctl` uninstalls Migrate for Anthos and fails on the install.

**Workaround:** Rerun `migctl setup upgrade` with the correct argument.

v1.7.0

Issue

**179171930:** This release of Migrate for Anthos does not support GKE 1.20.

**Workaround:** Use GKE 1.19 or earlier.

v1.7.0

Issue

**182450827:** If you installed Migrate for Compute Engine on your processing cluster to work with Migrate for Anthos, and want to perform four or more concurrent migrations, you cannot use GKE 1.18.

**Workaround:** Use GKE 1.16 on your processing cluster.

v1.7.0

Issue

**162275866:** When generating migration artifacts, you might see the following error:

`Error: failed to update vgenerateartifactsflow.kb.io:`

`Post https://controllers-webhook-service.v2k-system.svc:443/validate-anthos-migrate-cloud-google-com-v1beta2-generateartifactsflow?timeout=30s:`

`no endpoints available for service "controllers-webhook-service"`

**Workaround:** Try generating artifacts again. If not, check the manager status.

  1. Get the pod:

`kubectl get pod -n v2k-system`

  2. Look for a pod with name that starts with `controllers-controller-manager-` and describe it to see its status and event.




v1.7.0

Issue

After completing the installation of Migrate for Anthos, run the following command to apply a required patch:

`kubectl patch mutatingwebhookconfigurations.admissionregistration.k8s.io controllers-mutating-webhook-configuration --type json --patch '[{"op": "remove", path: "/webhooks/9"}]'`

v1.7.0

Feature

By default, Migrate for Anthos [automatically disables unneeded services](https://docs.cloud.google.com/migrate/anthos/docs/planning-best-practices#disable_unneeded_services) on a VM when you migrate it to a container. You can now edit the migration plan to optionally disable additional services on the container, either services discovered by Migrate for Anthos or your own list of services. See [Customizing a migration plan](https://docs.cloud.google.com/migrate/anthos/docs/customizing-a-migration-plan) for more.

v1.7.0

Issue

**183082390:** The collection script used by the Linux discovery tool uses `service --status-all` to query system V services. Depending on the services installed on the VM, `service --status-all` might call custom routines. In some cases, this call might take an arbitrary amount of time depending on the services installed.

v1.7.0

Issue

**182208300:** When building a Docker image for a Windows container, examine the logs. Sometimes an internal step can fail, even when the build command shows that the build was successful.

v1.7.0

Issue

**156207267:** When using Anthos clusters on VMware for your processing cluster, the migration might get stuck at the image extraction step, and the relevant migration pod shows volume attachment errors similar to the following:
    
    
    Warning FailedAttachVolume 5s (x10 over 4m15s)
    attachdetach-controller AttachVolume.Attach failed for volume migration-b849e1-dd:
    Invalid configuration for device 0.
    

The issue is triggered by a Kubernetes in-tree vsphere driver that is unable to cleanup leftovers from previous migration operations on the same node.

**Workaround:** Either:

  * Cordon the affected node by:

    1. Running the following command:

`kubectl cordon [node_id]`

    1. Restarting the migration.
  * Restart the affected node.




v1.7.0

Fixed

**178469863:** Running migctl setup install with either the --node-selector or --tolerations flag no longer returns an error.

v1.7.0

Issue

**179860971:** The status error returned when you enter an incorrect VM ID in the console is not helpful:

`googleapi: got HTTP response code 404 with body:`

**Workaround** : View the error in the **Events** tab in the console for more information:

  1. Click the **Migrations** tab to display a table containing the available migrations.

  2. In the row for the desired migration, select the migration **Name** to open the **Details** tab.

  3. Select the **Events** tab.




v1.7.0

Feature

This release updates the Linux discovery tool to replace the CSV output with an HTML and JSON output. Also, the fit score of 0-10 has been replaced with a fit assessment value, new rules have been added, and more information about the source VM has been added to the report. For a complete list of updates and information on using the new tool see [Using the Linux discovery tool](https://docs.cloud.google.com/migrate/anthos/docs/linux-assessment-tool).

v1.7.0

Fixed

**175000470:** The issue caused by adding a source when using a service account without the `compute.disks.create` permission has been fixed.

v1.7.0

Issue

**179028669:** `migctl doctor` crashes if a GKE cluster is currently repairing.

**Workaround:** If `migctl` crashes, then validate that any `kubectl` command can run on the cluster before retrying the command.

v1.7.0

Issue

**186512095:** When building a Windows container, you must edit the generated Dockerfile to change the image tag to `latest`. For example:

`from` _image_name_`:latest`

v1.7.0

Issue

**183321483:** If you are using a CRD file to create a migration source, and you include a secret in the CRD, then deleting the migration source might also delete the secret.

**Workaround:** Recreate the secret after deleting the migration source.

## February 23, 2021

v1.6.0

Fixed

**180576558** : Fixed an issue where the Linux discovery tool calculated an incorrect score.

v1.6.0

Fixed

Fixed an issue where using an Envoy proxy sidecar, not as part of Istio or Anthos Service Mesh, created networking issues with the migrated workload.

## February 01, 2021

v1.6.0

Feature

Released a fix, rolling out gradually and taking full effect 2/5/2021, for a `migctl` setup installation that fails on a GKE cluster when the automatically created bucket already exists.

v1.6.0

Feature

Released a fix, rolling out gradually and taking full effect 2/5/2021, for a `migctl` crash when `kubectl` is not in `PATH`.

## January 25, 2021

v1.6.0

Feature

In many on-prem environments, outbound internet access is tightly controlled through the use of an HTTPS proxy server. If your environment uses a proxy server to control outbound internet access, then you can now configure Migrate for Anthos to use that proxy server. See [Configuring an HTTPS proxy](https://docs.cloud.google.com/migrate/anthos/docs/proxy-server) for more.

v1.6.0

Issue

**175000470** : When adding a source when using a service account without the `compute.disks.create` permission, the source becomes ready but the migration will fail to create disks.

**Workaround** : Make sure that service account has the `compute.disks.create` permission.

v1.6.0

Feature

Migrate for Anthos now includes the `deployment_spec.yaml` file in `artifacts.zip` for Windows migrations. You can use the `deployment_spec.yaml` file to deploy your migrated Windows workloads. See [Deploying a Windows workload to a target cluster](https://docs.cloud.google.com/migrate/anthos/docs/windows/deploying-to-target-cluster) for more.

v1.6.0

Issue

**185975192:** Webhook certificates can expire after one month, causing API requests to fail.

v1.6.0

Change

Removed support for the `--password` option to the `migctl` command when creating a migration source on Anthos clusters on VMware:

`migctl source create local-vmware local-vmware-src --vc '1.2.3.4' --username 'admin' --password 'pass1'`

You are now prompted to enter the password. See [Adding a migration source](https://docs.cloud.google.com/migrate/anthos/docs/adding-a-migration-source) for more.

v1.6.0

Issue

**178469863** : Running `migctl setup install` with either the `--node-selector` or `--tolerations` flag returns an error. 

**Note** : Running the `migctl setup install` command with both flags succeeds. This error only occurs when using one flag.

**Workaround** : Run `migctl setup install` without the option, and then manually add the nodeSelectors or tolerations to CSI and Controller pods. See [Creating and managing cluster labels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels) and [Controlling scheduling with node taints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-taints) for more.

v1.6.0

Issue

**174655315** : A migration might stop responding when generating artifacts and remain in the retrying state. You might also see this error in the logs or in the verbose migration status:

`D 2020-12-01T18:43:53Z SHELL ERROR: '2020/12/01 18:43:53 appending [/tarlayer/layer.tar.gz]: reading tar "/tarlayer/layer.tar.gz": flate: corrupt input before offset 681999708'`

**Workaround** : Re-run `migctl migration generate-artifacts`.

v1.6.0

Issue

**171686793** : The `migctl setup upgrade --gkeop` command might create a new ImageRepositiry or ArtifactRepository object that lacked Google Cloud access credentials.

**Workaround** : Use the following command to upgrade the cluster:

`migctl setup upgrade --json-key key`

Where _key_ is the JSON key for the service account required for `migctl` installation. See [Configuring service accounts](https://cloud.google.com/migrate/anthos/docs/config-dev-env#configuring_service_accounts).

v1.6.0

Feature

Previous releases of Migrate for Anthos required that you used Google Container Registry (GCR) and Google Cloud Storage for data repositories. This release adds support for additional repositories, including ECR, S3, and Docker registries that support basic authentication. See [Defining data repositories](https://docs.cloud.google.com/migrate/anthos/docs/data-repos) for more.

v1.6.0

Issue

If you try to mount a secret on a deployed pod you will not be able to access it in `/run/secrets`. This is typically an issue when giving workload identity permissions to the pod (where a secret is added by Kubernetes to hold the workload identity credentials). 

The contents of the secrets directory are in `/kubernetes-info/secrets`.

**Workaround** : Run the following command on the deployed pod: 

`ln -s /kubernetes-info/secrets /run/secrets`

If the `/run` mount gets deleted (by a process in the pod, or by a pod reset), you might have to run the command again.

v1.6.0

Feature

Support added for using Anthos clusters on AWS as processing clusters to perform migrations of AWS workloads. This feature is in [preview](https://cloud.google.com/products#product-launch-stages). See [Prerequisites for migrating Linux VMs on AWS](https://docs.cloud.google.com/migrate/anthos/docs/migration-prerequisites-aws) for more.

v1.6.0

Issue

If you delete the configuration for a Docker image file registry, create a new one with a different configuration name. You cannot recreate a configuration with the name of a previously deleted configuration.

This issue affects Docker image file registries implemented by using GCR or by using Docker registries using basic auth. It does not affect ECR. See [Defining data repositories](https://docs.cloud.google.com/migrate/anthos/docs/data-repos) for more information.

**Workaround:** Use the `migctl docker-registry update` command to modify an existing configuration rather than deleting it and recreating it.

v1.6.0

Issue

**172414359** : Exporting multiple cloned VMs simultaneously from the same source might fail.

**Workaround** : Re-run the `migctl migration generate-artifacts` command again.

v1.6.0

Issue

**174299021** : When creating a migration source or executing a migration, you might see this error:

`"Error: Internal error occurred: failed calling webhook "vmigration.kb.io": Post https://controllers-webhook-service.v2k-system.svc:443/validate-anthos-migrate-cloud-google-com-v1beta2-migration?timeout=30s: unexpected EOF"`

**Workaround** : Recreate the source or migration.

## November 16, 2020

v1.5.0

Fixed

When creating a migration source for Compute Engine workload, Migrate for Anthos now tests that the GCP specified project exists. Source creation fails when either the project does not exist or the user has no read permissions to the project. An error message is shown indicating that the required project could not be found.

v1.5.0

Fixed

**170618192** : Similarly to Linux migrations, Windows migrations now add to the generate artifacts object an annotation containing the migration spec and comments.

v1.5.0

Fixed

**171173082** : Mistakenly creating a local VMware source on a Cloud-based cluster, normally used only in an on-prem migration, no longer results in the source being in `PROCESSING` state forever but instead returns an error.

v1.5.0

Fixed

**170566991** : For Windows migrations, only HTTP and HTTPS site bindings are supported. See [Edit the migration-plan](https://docs.cloud.google.com/migrate/anthos/docs/windows/customizing-a-migration-plan) for information on how to remove the unsupported binding.

v1.5.0

Fixed

**170604382** : Running `migctl` when not connected to a cluster no longer results in a `panic` error, but instead returns an error message describing the issue.

v1.5.0

Fixed

**169919740** : When using a [custom services blocklist](https://docs.cloud.google.com/migrate/anthos/docs/custom-blocklist) to disable a service in a workload, if the service was already disabled by default, the migrated container no longer can crash when deployed.

## October 08, 2020

v1.5.0

Feature

Support for migrating Windows VM workloads has moved from the Beta stage to general availability. 

This release adds full support for migrating Windows VM workloads to the Google Cloud Console, including the ability to create a Windows migration source. See [Migrating a Windows VM](https://docs.cloud.google.com/migrate/anthos/docs/windows/migrating-win-vm-overview) for more.

v1.5.0

Feature

Migrate for Anthos provides tools that you run on a Linux or Windows VM workload to determine the workload's fit for migration to a container. See [Using the Linux discovery tool](https://docs.cloud.google.com/migrate/anthos/docs/ldt-doc) and [Using the Windows discovery tool](https://docs.cloud.google.com/migrate/anthos/docs/wdt-doc) for more.

v1.5.0

Feature

Custom Services Blocklist support added which lets you define a list of services to disable in a migrated container. See [Custom Services Blocklist](https://docs.cloud.google.com/migrate/anthos/docs/custom-blocklist) for more.

v1.5.0

Issue

**170706786** : The Linux Discovery Tool might return exit code 0 even when all information was collected successfully.

**Workaround:** Make sure you run the tool as a 'root' user or as a user with full sudo access.

v1.5.0

Feature

The `image` field value of the [GenerateArtifactsFlow CRD](https://docs.cloud.google.com/migrate/anthos/docs/generateartifactsflow-crd) defines the names and locations of two images created from a migrated VM. In previous releases, the names contained a predefined tag.

To ensure that the tag value is unique, the format of the tag has changed for this release to specify the timestamp of the migration. 

You can also explicitly set the tag if you prefer to another value. See [Setting the name of the container image](https://docs.cloud.google.com/migrate/anthos/docs/customizing-a-migration-plan#setting_the_name_of_the_container_image) for more.

v1.5.0

Issue

**167656057** : Installation on a GKE cluster with ACM might fail. Indication of the error can be seen in the Migrate for Anthos upgrade job, in the `v2k-system` namespace.

For example:
    
    
    kubectl logs -n v2k-system controllers-upgrade-fzlmz
    

Shows this error:

`failed to validate admission controller - admission webhook "validation.gatekeeper.sh" does not support dry run`

**Workaround** : `gatekeeper` is an ACM component. Manually deleting the upgrader job fixes the issue.

For example:

`kubectl delete job -n v2k-system controllers-upgrade`

v1.5.0

Issue

**171123825** : In some cases, migration process might fail, and Cloud Logging indicate errors such as:

`"failed to load map, error 6"`

or:

`"failed in domap for addition of new path sdd"`

**Workaround** : Delete the migration and restart it. In rare cases, a re-installation of the product is required.

v1.5.0

Issue

**170627229** : Migrated workload of a JBoss application might fail at startup. Cloud Logging indicates an error in the form:
    
    
    ERROR [org.jboss.as.server] (Controller Boot Thread) ...:
    Caught exception during boot: java.lang.IllegalStateException: ...: 
    Could not rename /opt/jboss-7.1.1/standalone/configuration/.../standalone_xml_history/current to
    /opt/jboss-7.1.1/standalone/configuration/.../standalone_xml_history/...
    

**Workaround** : Update your Dockerfile to remove the directory by adding a line in the form:
    
    
    RUN rm -rf jboss-location/standalone/configuration/standalone_xml_history/current
    

Where _jboss-location_ is a path such as `/usr/local/share/jboss` or `/opt/jboss-7.1.1`.

v1.5.0

Feature

When you deploy your migrated Windows containers to a cluster, you can now use a Group Managed Service Account (gMSA) to execute the container under a specific service account identity. See [Configuring gMSA](https://docs.cloud.google.com/migrate/anthos/docs/windows/customizing-a-migration-plan#setting_the_location_for_deployment_artifacts) for more.

v1.5.0

Issue

**144896313** : Migrated workloads do not support SELinux. However, if the source VM had SELinux enabled at the time of migration, and you then check the status of SELinux on the migrated workload, SELinux will appear to be enabled. This issue has no affect on migrated workloads.

v1.5.0

Issue

**157062328** : In some cases, adding a service to the blocklist using a configmap will not actually stop that service from running on the deployed workload.

**Workaround** : Disable the service using in the Dockerfile (rather than a config-map), and rebuild the image.

v1.5.0

Issue

**171714535** : In a GKE on-prem environment configured to use an egress HTTP/HTTPS proxy, the migration process might get stuck.

**Workaround** : Please contact [support](https://docs.cloud.google.com/support/docs/role-based-support) for more information.

v1.5.0

Issue

**163800225** : kubectl port-forward might not work properly for a deployed workload.

Please contact [support](https://docs.cloud.google.com/support/docs/role-based-support) for more information.

## July 28, 2020

v1.4.0

Issue

**161104564:** Creating a Linux migration with wrong `os-type` specification causes the migration process to get stuck until deleted.

v1.4.0

Deprecated

The `migctl migration cleanup` command has been removed and is no longer necessary.

v1.4.0

Feature

To edit the migration plan, you must now use the `migctl migration get my-migration` command to download the plan. After you are done editing the plan, you have to upload it by using the `migctl migration update my-migration` command. See [Customizing a migration plan](https://docs.cloud.google.com/migrate/containers/docs/release-notes/customizing-a-migration-plan) for more.

v1.4.0

Issue

**152974631:** Using GKE nodes with CPU and Memory configurations below the recommended values might cause migrations to get stuck.

v1.4.0

Feature

Added the `node-selectors` and `tolerations` options to the `migctl setup install` installation command that lets you install Migrate for Anthos on a specific set of nodes or node pools in a cluster. See [Installing Migrate for Anthos](https://docs.cloud.google.com/migrate/anthos/docs/installing-migrate-components).

v1.4.0

Feature

Added support for Anthos GKE on-prem clusters running on VMware. On-prem support lets you migrate source VM workloads in a vCenter/vSphere environment to a GKE on-prem cluster running in the same vCenter/vSphere environment. See [Migration prerequisites](https://docs.cloud.google.com/migrate/containers/docs/release-notes/migration-prerequisites) for the requirements for on-prem migration.

v1.4.0

Deprecated

In previous releases, you used a command in the form: `migctl source create ce my-ce-src --project my-project --zone zone` to create a migration for Compute Engine. The `--zone` option has been removed when creating a Compute Engine migration. Using the `--zone` option in this release causes an error.

v1.4.0

Feature

You can use Migrate for Anthos to migrate Windows VMs to workloads on GKE. This process clones your Compute Engine VM disks and uses the clone to generate artifacts (including a Dockerfile and a zip archive with extracted workload files and settings) you can use to build a deployable GKE image. See [Adding a Windows migration source](https://docs.cloud.google.com/migrate/containers/docs/release-notes/windows/migrating-win-vm-overview).

v1.4.0

Issue

**161214397:** In case of a missing service-account to upload container images to the Container Registry, the migration might get stuck. 

**Workaround:** Add the service-account. If you are using the Migrate for Anthos CRD API, delete the GenerateArtifactsTask and recreate it. If using the `migctl` CLI tool, delete the migration and recreate it. You can first download the migration YAML using `migctl migration get` to back up any customizations you have made.

v1.4.0

Feature

Added the new `--json-key sa.json` option to the `migctl source create ce` command to create a migration for Compute Engine, where `sa.json` specifies a service account. See [Optionally creating a service account when using Compute Engine as a migration source](https://docs.cloud.google.com/migrate/containers/docs/release-notes/config-dev-env#optionally_creating_a_service_account_when_using_as_a_migration_source) for more.

v1.4.0

Issue

**161135630:** Attempting multiple migrations of the same remote VM (from VMware, AWS or Azure) simultaneously, might result in a stuck migration process.

**Workaround:** Delete the stuck migration.

v1.4.0

Feature

Migrate for Anthos now includes [Custom Resource Definitions (CRDs)](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) that enable you to easily create and manage migrations using an API. For example, you can use these CRDs to build your own automated tools.

v1.4.0

Issue

**160309992:** Editing a migration plan from the GUI console might fail if it was also edited using `migctl`.

v1.4.0

Issue

**161787358:** In some cases, upgrading from version v1.3 to v1.4 might fail with `Failed to convert source` message. 

**Workaround:** Re-run the upgrade command.

v1.4.0

Feature

You can now use the [Google Cloud Console](https://console.cloud.google.com) to:

  * Install Migrate for Anthos on a processing cluster
  * Create a migration source for a Compute Engine VM



See [Installing Migrate for Anthos](https://docs.cloud.google.com/migrate/anthos/docs/installing-migrate-components) and [Adding a migration source](https://docs.cloud.google.com/migrate/anthos/docs/adding-a-migration-source) for more.

v1.4.0

Issue

**153811691, 153439420:** Migrate for Anthos support for older Java does not handle OpenJDK 7 and 8 CPU resource calculations.

v1.4.0

Issue

**161110816:** `migctl migration create` with a source that doesn't exist fails with a non-informative error message: `request was denied`.

v1.4.0

Fixed

**GKE on-prem preview:** If a source was created with `migctl source create` using the wrong credentials, you could not delete the migration with `migctl migration delete`. This issue has been fixed in the GA release of on-prem support.

v1.4.0

Deprecated

The `migctl migration logs` command has been removed. You now use the Google Console to view logs.

v1.4.0

Issue

**160858543, 160836394, 160844377, 154430477, 154403665, 153241390, 153239696, 152408818, 151516642, 132002453:** Unstable network in Migrate for Anthos infrastructure, or a GKE node restart, might cause migration to get stuck. 

**Workaround:** Delete the migration and re-create it. If recreating the migration does not solve the issue, please contact [support](https://docs.cloud.google.com/support-hub#migrate-for-compute-engine-formerly-velostrata).

v1.4.0

Issue

**160523841, 159106543:** For Anthos GKE on-prem, in rare cases of high load, vSphere may report a failure when creating a resource even though the resource was correctly created. This may cause a snapshot or cloned VM resource leak when deleting the migration operation. The VMs or snapshots can then be manually deleted in vSphere.

v1.4.0

Deprecated

In version 1.4, by default Migrate for Anthos installs to and performs migrations in the `v2k-system` namespace. In previous release, you could specify the namespace. The option to specify a namespace has been removed.

v1.4.0

Issue

**157890913, 160082702, 161125635, 159693579** : A migration might continue to indicate that it is running, while an issue encountered prevents further processing.

**Workaround** : Check event messages on the migration object using the verbose `migctl` status command: `migctl migration status migration_name -v`. You might be able to correct the issue to allow the migration to continue or the migration should be deleted and recreated if an Error event is listed without further retries.

An example is when creating a Windows migration on a cluster with no Windows nodes. In this case the event message will show: `Warning FailedScheduling 10s Pod discover-xyz 0/1 nodes are available: 1 node(s) didn't match node selector.`

v1.4.0

Feature

The Google Cloud Console provides a web-based, graphical user interface that you can use to manage your Google Cloud Console projects and resources. Migrate for Anthos now supports the migration of workloads by using the Google Cloud Console. 

In this release, the Migrate for Anthos on the Cloud Consoledoes not support migrations for Windows or for on-prem, including monitoring Windows or on-prem migrations.

v1.4.0

Feature

Changed the default settings on the Cloud processing cluster for migrating Linux workloads:

  * You no longer have to specify the `--scopes "cloud-platform"` option when creating the processing cluster. 

  * You now must create a service account, with the necessary permissions, to:

    * Install Migrate for Anthos

    * Use Compute Engine as the migration source




If you currently have a processing cluster that uses the `--scopes "cloud-platform"` option, your cluster will continue to work. However, for new processing clusters, you should use the new procedure. See [Enabling Google services and configuring service accounts](https://docs.cloud.google.com/migrate/anthos/docs/config-dev-env) for more.

v1.4.0

Issue

**155051522:** CSI health-check events are reported to their matching StorageClass object, and are not propagated to their matching SourceProvider object.

## March 30, 2020

v1.3.0

Issue

**152194161:** Your migrated workload container fails when running a cluster with GKE nodes of type "COS". When you run the command `kubectl logs [podname]`, you might see the following:
    
    
    apparmor.go:385] Couldn't set label to lxc-container-default - write /proc/1/attr/current: no such file or directory
    

This is an indication that the required AppArmor profiles are not installed on the GKE nodes. To solve this, run `migctl setup install --cos-runtime`.

v1.3.0

Issue

**151505531, 150052607:** In some cases, migration can be stuck with no progress. When running `migctl migration status migration-name --verbose`, you might see an event such as this:
    
    
    could not find attached GCE PD
    

**Workaround:** Delete the migration using `migctl migration delete` and re-create it.

v1.3.0

Feature

Introducing a unified migration workflow across all supported VM sources -- VMware, AWS EC2, Azure VMs and Compute Engine VMs.

v1.3.0

Feature

The Migrate for Anthos software runtime layer now offers a compatibility feature for older Java versions that are not container aware by reflecting the correct resource allocations in the container's `/proc` file system.

v1.3.0

Feature

New `migctl` CLI for deploying Migrate for Anthos, creating and operating migrations using a structured workflow and a migration processing cluster.

v1.3.0

Issue

**148334068:** When Migrating a physical VM from on-premises connected via Migrate for Compute Engine, Migrate for Anthos attempts to optimize network utilization and discards (rather than stream) blocks that are not in use on the source VM file system. In some cases, this might cause VMware storage sessions to time out. For assistance, please contact support.

v1.3.0

Feature

Migrate for Anthos v1.0 Marketplace deployment is now removed. Migrate for Anthos v1.3 allows installation in v1.0 compatibility mode where needed.

v1.3.0

Feature

Migrations are defined and operated using a Kubernetes CRD.

v1.3.0

Issue

**146699220:** When the source VM has a systemd service with a `NICE` config property, the service might not start when running in a container.

**Workaround:** Remove the `NICE` property in the source VM before the migration.

v1.3.0

Feature

Preview features -- contact your Google Sales representative to enroll.

  * Migrating Windows VMs with IIS ASP.NET web applications to Windows 2019 containers on GKE.
  * Processing migrations in Anthos on-prem.



v1.3.0

Issue

**GKE on-prem preview:** If a source was created with `migctl source create` using the wrong credentials, migrations will fail. Attempts to delete the migration with `migctl migration delete` may hang in a "Terminating" state, as in the following example:
    
    
    ubuntu@gke-on-prem-admin-appliance-1:~/$ ./migctl migration list
    NAME       PROCESS              STATE                   STATUS        PROGRESS   AGE
    my-vm-01   generate-artifacts   createSourceSnapshots   TERMINATING   [2/13]     
    

v1.3.0

Issue

**149900626:** Some file systems not listed in [Compatible VM operating systems](https://docs.cloud.google.com/migrate/containers/docs/release-notes/compatible-os-versions) may fail to migrate. When running `migctl migration logs migration-name`, the logs in Cloud Logging may show a message such as:
    
    
    failed to mount - exit status 32 - mount: /tmp/bootdir: unknown filesystem type 'LVM2\_member'.
    

v1.3.0

Issue

**147211918:** In some cases, migration from AWS or Azure as a source can be stuck with no progress. If this happens, run `kubectl describe storageclass` to view related events. You can also check the status of the matching Cloud Details in Migrate for Compute Engine.

v1.3.0

Issue

**144896313:** Migration of Security-Enhanced Linux (SELinux) is not supported.

v1.3.0

Feature

Automated generation of a suggested migration plan (specified in a CRD), CI/CD artifacts and deployment specs. The migration process now results in extracting and generating container and deployment artifacts, including a container image and a Dockerfile, extracted data in a persistent volume, deployment/statefulSet, PVC and PV specs in an auto-generated YAML file for easy workload deployment.

## December 19, 2019

v1.0.1

Fixed

Using `kubectl exec` on a migration pod would sometimes display superfluous `bash` warnings about `LC_ALL`.

v1.0.1

Fixed

Migrate for Anthos failed to recognize a reference to a disk specified as a `PARTUUID` in the `fstab` file. `PARTUUID` is now supported.

v1.0.1

Fixed

The Migrate for Compute Engine password could be inadvertently logged in Stackdriver Logging.

v1.0.1

Fixed

When resolving block devices in a multipath device, the operation appeared to succeed even if there was an error with one of the block devices.

v1.0.1

Fixed

Migrate for Anthos CSI drive would sometimes fail connecting to the migrated VM.

v1.0.1

Fixed

Deleting a `StatefulSet` attached to a persistent volume would leave the volume in an attached state./p>

v1.0.1

Fixed

The `kubectl cp` command would fail when copying files to the migrated pod.

v1.0.1

Fixed

Resolving source storage devices would sometimes fail without error if one of the devices has no partitions.

v1.0.1

Fixed

Using configuration YAML from a version prior to 1.0 caused the pod to enter a crashloop stage.

An error message now is now displayed to request that you update to [the latest definition](https://docs.cloud.google.com/migrate/anthos/docs/yaml-reference).

v1.0.1

Fixed

When specifying a mixed-case value for the `clone_vm_disks` script's `-A <var>app-name</var>` argument, the YAML file generated by the script would include a workload name that could not be deployed.

The command now checks for a valid input value.

v1.0.1

Fixed

Attempting to switch to a non-root user with the `su` command after connecting to the machine with `ssh` would fail when you had previously used `su` to switch to another user.

## November 13, 2019

v1.0.0

Issue

Resolving source storage devices would sometimes fail without error if one of the devices has no partitions.

v1.0.0

Feature

For information on operating systems supported by Migrate for Anthos, see [Compatible VM operating systems](https://docs.cloud.google.com/migrate/anthos/docs/compatible-os-versions).

v1.0.0

Feature

You can monitor export of short-term storage to a persistent volume using `kubectl`. For more information, see [Exporting streaming PVs to permanent storage](https://docs.cloud.google.com/migrate/anthos/docs/export-storage).

v1.0.0

Issue

Migrate for Anthos CSI drive may sometimes fail connecting to the migrated VM.

v1.0.0

Issue

Operating systems running `systemd` versions lower than 234 are limited to 65536 open files.

v1.0.0

Issue

Using configuration YAML from a version prior to 1.0 causes the pod to enter a crashloop stage.

To work around this, update your YAML file to conform to [the latest definition](https://docs.cloud.google.com/migrate/anthos/docs/yaml-reference).

v1.0.0

Issue

For known issues and workarounds, see [Troubleshooting Migrate for Anthos](https://docs.cloud.google.com/migrate/anthos/docs/troubleshooting).

v1.0.0

Feature

Migrate for Anthos supports migrating existing VMware, Amazon EC2, Azure, and Compute Engine VMs to containers on Google Kubernetes Engine. For more information, see [Benefits of Migrate for Anthos](https://docs.cloud.google.com/migrate/anthos/docs/anthos-migrate-benefits).

v1.0.0

Issue

On the Migrate for Compute Engine portlet in VMWare vCenter, VMs will be shown as Managed by Migrate for Compute Engine during migration process. Only the cache and storage migration status are updated in this view. Other functionality, such as Migrate for Compute Engine actions, may not be functional.

v1.0.0

Issue

When resolving block devices in a multipath device, the operation appears to succeed even if there was an error with one of the block devices.

v1.0.0

Issue

The `kubectl cp` command fails when copying files to the migrated pod.

v1.0.0

Issue

Attempting to switch to a non-root user with the `su` command after connecting to the machine with `ssh` fails when you have previously used `su` to switch to another user.

To work around this issue, use `kubectl exec` instead of `ssh` to get a shell to the container.

v1.0.0

Issue

The Migrate for Compute Engine password can be inadvertently logged in Stackdriver Logging.

v1.0.0

Issue

When using a private GKE cluster, the GKE master might be unable to reach Migrate for Anthos infrastructure (specifically, the admission-controller) by default. This is because the admission-controller pod listens on port 7000.

To work around this issue, add port 7000 to the firewall rules of the master node. For more, see [Creating a private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#add_firewall_rules).

v1.0.0

Issue

Migrate for Anthos fails to recognize a reference to a disk specified as a `PARTUUID` in the `fstab` file.

v1.0.0

Issue

VMs using EFI configurations are not compatible for migration with this release.

v1.0.0

Issue

When specifying a mixed-case value for the `clone_vm_disks` script's `-A <var>app-name</var>` argument, the YAML file generated by the script includes a workload name that can not be deployed.

To work around this issue, specify the argument's value in lowercase only.

v1.0.0

Issue

Using `kubectl exec` on a migration pod sometimes displays superfluous `bash` warnings about `LC_ALL`. These are only cosmetic.

v1.0.0

Issue

Deleting a StatefulSet attached to a persistent volume will leave the volume in an attached state.

v1.0.0

Feature

Using a `ConfigMap`, you can have content from application log files you specify written to Stackdriver Logging (a default list is included). For more, see [Configuring logging to Stackdriver Logging](https://docs.cloud.google.com/migrate/anthos/docs/configuring-stackdriver-logging).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

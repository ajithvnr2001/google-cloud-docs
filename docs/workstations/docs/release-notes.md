---
url: https://docs.cloud.google.com/workstations/docs/release-notes/
title: Cloud Workstations release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:49:26.282938+00:00
---

# Cloud Workstations release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Resources ](https://docs.cloud.google.com/workstations/docs/resources)



Send feedback 

#  Cloud Workstations release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud Workstations. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/workstations-release-notes.xml) directly. 

## October 20, 2026

Feature

Cloud Workstations supports automatic failover for [boost configurations](https://docs.cloud.google.com/workstations/docs/boost-workstation#automatic-failover) in [Preview](https://cloud.google.com/products#product-launch-stages). When you enable automatic failover, Cloud Workstations automatically provisions a workstation VM using the boost configuration if Compute Engine lacks capacity for the default machine type during startup.

## October 05, 2026

Feature

Cloud Workstations supports [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview) control packages to help you meet regulatory, data residency, and data sovereignty requirements.

Specifically, the Cloud Workstations API (`v1`, `v1beta`, and `v1alpha`) supports the following [Assured Workloads control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages):

  * [Data Boundary for FedRAMP High](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-high)
  * [Data Boundary for FedRAMP Moderate](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-moderate)
  * [Data Boundary for Impact Level 2 (IL2)](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il2)
  * [Data Boundary for Impact Level 4 (IL4)](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il4)
  * [Data Boundary for Impact Level 5 (IL5)](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il5)
  * [US Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-support) (AW Regional Controls - Premium)
  * [EU Data Boundary with Access Justifications](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-access-justifications)



For more information about compliance-supported regions for each control package and API fields that aren't intended for sensitive data, see [Regulatory support in Cloud Workstations](https://docs.cloud.google.com/workstations/docs/workstations-regulatory-compliance).

## September 24, 2026

Feature

Cloud Workstations is a covered [product](https://cloud.google.com/security/compliance/hipaa#covered-products) under [Google Cloud HIPAA BAA](https://cloud.google.com/terms/hipaa-baa).

## September 23, 2026

Feature

[Regional endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints#cloud-workstations) (`workstations.REGION.rep.googleapis.com`) are generally available (GA) for Cloud Workstations. Regional endpoints help you meet data residency requirements by routing and terminating HTTPS connections to the Cloud Workstations API within a specific region, keeping data in transit within your chosen regional boundary.

Regional endpoints for Cloud Workstations are available in the following [regions](https://docs.cloud.google.com/workstations/docs/locations):

  * `asia-south1` (Mumbai, India, APAC)
  * `europe-west6` (Zurich, Switzerland, Europe)
  * `us-central1` (Council Bluffs, Iowa, North America)
  * `us-east1` (Moncks Corner, South Carolina, North America)
  * `us-east4` (Ashburn, Virginia, North America)
  * `us-east5` (Columbus, Ohio, North America)
  * `us-west1` (The Dalles, Oregon, North America)
  * `us-west4` (Las Vegas, Nevada, North America)



You can also use the Google Cloud CLI `gcloud workstations` command group to configure regional endpoints. For more information, see [Regional service endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints#cloud-workstations) and the [Cloud Workstations REST API reference](https://docs.cloud.google.com/workstations/docs/reference/rest).

## September 14, 2026

Feature

Cloud Workstations supports customizing [provisioned IOPS and throughput](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs#gcehyperdiskbalancedhighavailability) for Hyperdisk Balanced High Availability disks. This customization feature is in Preview.

## August 26, 2026

Feature

Cloud Workstations supports an [agent-optimized development](https://docs.cloud.google.com/workstations/docs/agent-optimized-development) experience.

## August 12, 2026

Feature

Cloud Workstations supports [Compute Engine suspend and resume](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance) in Preview. You can configure workstation VMs to suspend when they reach their idle timeouts, referred to as auto-sleep in the Google Cloud Console, rather than shutting down and deleting the VM, by using the [IdleAction](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs#idleaction) workstation configuration setting.

## August 03, 2026

Change

Updated the following [JetBrains preconfigured base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) to version 2026.x:

  * [CLion 2026.1](https://youtrack.jetbrains.com/articles/CPP-A-230654453/CLion-2026.1)
  * [GoLand 2026.2](https://youtrack.jetbrains.com/articles/GO-A-231736055/GoLand-2026.2)
  * [IntelliJ Ultimate 2026.1](https://youtrack.jetbrains.com/articles/IDEA-A-2100662608/IntelliJ-IDEA-2026.1-Latest-Builds)
  * [PhpStorm 2026.2](https://youtrack.jetbrains.com/articles/WI-A-231736318/PhpStorm-2026.2)
  * [WebStorm 2026.1](https://youtrack.jetbrains.com/articles/WEB-A-233538705/WebStorm-2026.1)
  * [RubyMine 2026.1](https://youtrack.jetbrains.com/articles/RUBY-A-220365320/RubyMine-2026.1)
  * [PyCharm 2026.1](https://youtrack.jetbrains.com/articles/PY-A-233538506/PyCharm-2026.1)
  * [Rider 2026.1](https://youtrack.jetbrains.com/issues?q=project:%20Rider%20%7B2026.1%7D)



## July 08, 2026

Announcement

The base VM for your workstation includes the Content-Addressable Storage File System (CASFS) kernel module, which lets you run the Android Build File System (ABFS). For more information about the introduction of this module, see the [Container-Optimized OS Milestone 129 LTS release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m129#February_20_2026).

Feature

The [Data Agent Toolkit Extension](https://docs.cloud.google.com/data-cloud-extension) is installed by default in Code OSS for Cloud Workstations.

## June 08, 2026

Feature

The workstation configuration creation page in the Google Cloud console has been optimized to make configuration creation faster and easier. Common machine settings are grouped into selectable machine presets, frequently used settings are consolidated on the **Configuration essentials** landing page, and a pending cluster with default settings is automatically provisioned when no cluster exists in your selected region.

## May 29, 2026

Announcement

The [preconfigured base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) include [Antigravity CLI](https://antigravity.google/product/antigravity-cli).

Feature

Cloud Workstations supports configuring custom startup scripts from the Google Cloud Console. When you create or edit a workstation configuration, you can specify the Cloud Storage path to your startup script under the advanced environment customization options. For more information, see [Run custom startup scripts](https://docs.cloud.google.com/workstations/docs/startup-scripts).

Announcement

The base VM was upgraded to use [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits) [129 LTS](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m129).

Feature

The [JetBrains RubyMine preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses a custom gem directory (`/usr/local/share/gems/ruby/3.1.0`).

## May 18, 2026

Feature

Cloud Workstations supports resizing workstations' persistent directories. For more information, see [Resize workstation persistent directories](https://docs.cloud.google.com/workstations/docs/resize-workstation-persistent-directories).

## May 10, 2026

Announcement

The base VM was upgraded to use [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits) [125 LTS](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125).

## May 08, 2026

Feature

You can configure a workstation authorization URL for workstation clusters.

When you specify an authorization URL, unauthorized HTTP or HTTPS requests received by workstation VMs in the cluster are redirected to this endpoint. The endpoint is then responsible for retrieving an access token and redirecting back to the original hostname with the token.

## May 04, 2026

Feature

The [JetBrains Rider preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) includes .NET 10.0 and drops .NET 6.0.

Feature

The [JetBrains RubyMine preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) installs Ruby using `ruby-build` instead of RVM (Ruby Version Manager).

## April 27, 2026

Feature

Cloud Workstations UI supports additional machine series and types, including **A2** , **A3** , **C3** , **C4** , **G4** , **M3** , **N4** , and **Z3**. You can also select **Confidential C3 standard** machine types. For more information, see [Available machine types](https://docs.cloud.google.com/workstations/docs/available-machine-types).

The [preconfigured base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) include a notification when the `running_timeout` for the workstation is close to being reached.

## April 13, 2026

Feature

The [preconfigured base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) include a `/google/scripts/keep_alive.sh` script to prevent idle timeouts when running long-running background tasks.

## April 06, 2026

Feature

You can automatically redirect and restart stopped workstations by configuring the `workstation_launch_url` Workstation cluster field. To set a custom URL or use the built-in Google Cloud Console launcher, [update your cluster](https://docs.cloud.google.com/workstations/docs/create-cluster#workstation-cluster).

## March 26, 2026

Announcement

The [Cloud Workstations base editor](https://docs.cloud.google.com/workstations/docs/preconfigured-ides#cloud-workstations-base-editor) (Code OSS for Cloud Workstations) has been upgraded to `1.109.5`.

## March 06, 2026

Announcement

The [Cloud Workstations base editor](https://docs.cloud.google.com/workstations/docs/preconfigured-ides#cloud-workstations-base-editor) (Code OSS for Cloud Workstations) has been upgraded to `1.108.2`. The last image that offers the previous version is tagged `code-oss-1.104.3`.

## February 19, 2026

Feature

You can configure [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) for persistent directories directly in the Google Cloud console. This option is available in the **Disk type** menu when you create or update workstation configurations for supported machine series.

Additionally, [C3 machine types](https://docs.cloud.google.com/workstations/docs/available-machine-types) are available for selection in the Google Cloud console. For the C3 machine series, which only supports Hyperdisk, the console automatically selects Hyperdisk as the disk type.

## February 18, 2026

Feature

Clicking **Launch** for a workstation in the Google Cloud console opens a page that automatically starts the workstation and connects to it. You can bookmark this page to restart and access your workstation. To start a workstation without connecting, select **Start** in the **Launch** drop-down menu.

## February 06, 2026

Feature

Cloud Workstations supports specifying a custom startup script to be executed on the workstation's host VM during boot.

Provide the custom startup script as a Google Cloud Storage URL, such as `gs://BUCKET/FILE`, using the `--startup-script-uri` flag with the [`gcloud workstations configs create`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/create) and [`gcloud workstations configs update`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/update) commands.

Feature

You can provide [custom metadata](https://docs.cloud.google.com/compute/docs/metadata/overview) for a workstation's host VM.

Use the `--instance-metadata` flag with the [`gcloud workstations configs create`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/create) and [`gcloud workstations configs update`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/update) commands. Format the metadata as a comma-separated list of key-value pairs—for example, `--instance-metadata=key1=value1,key2=value2`.

Note that updating metadata replaces all existing custom metadata for the workstation instance.

## January 31, 2026

Feature

Cloud Workstations supports [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) (`hyperdisk-balanced-ha`) for persistent directories on configurations using A3, C3, C4, G4, M3, N4, N4D, and Z3 machine series. You can specify the disk type using the `--disk-type` flag with the [`gcloud workstations configs create`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/create) and [`gcloud workstations configs update`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/update) commands.

Cloud Workstations supports A3 machine types with Hyperdisk only. For more details, see [Available machine types](https://docs.cloud.google.com/workstations/docs/available-machine-types) and [Available GPUs](https://docs.cloud.google.com/workstations/docs/available-gpus).

## December 05, 2025

Change

Cloud Workstations predefined images include [Eclipse Temurin](https://adoptium.net/temurin) JDK 21 and 25. JDK 11 is no longer pre-installed. To continue using JDK 11, [customize your container images](https://docs.cloud.google.com/workstations/docs/customize-container-images).

Change

Cloud Workstations predefined images include [Node.js](https://nodejs.org/) 24 (LTS). The previous version, 20.19.6, is no longer pre-installed. To continue using a previous version, you can [customize your container images](https://docs.cloud.google.com/workstations/docs/customize-container-images) to include it or add a version manager like [NVM](https://www.nvmnode.com/).

## July 07, 2025

Feature

Cloud Workstations is available in the `europe-central2` region (Warsaw). For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

## June 09, 2025

Feature

The JetBrains [readiness server](https://docs.cloud.google.com/workstations/docs/develop-code-using-local-jetbrains-ides#add_a_server_readiness_check) lets you configure the port it listens on and the timeout when you specify the `JETBRAINS_READY_SERVER_PORT` and `JETBRAINS_READY_SERVER_TIMEOUT` environment variables in your workstation environment. For more information about setting environment variables, see [Customizing your environment](https://docs.cloud.google.com/workstations/docs/create-configuration#customize_environment).

## June 03, 2025

Change

The [JetBrains CLion preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [CLion 2025.1.1](https://youtrack.jetbrains.com/articles/CPP-A-230654398/CLion-2025.1.1-251.25410.104-build-Release-Notes)

Change

The [JetBrains IntelliJ Ultimate preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [IntelliJ-IDEA 2025.1.1](https://youtrack.jetbrains.com/articles/IDEA-A-2100662430/IntelliJ-IDEA-2025.1.1.1-251.25410.129-build-Release-Notes)

Change

The [JetBrains Rider preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [Rider 2025.1.2](https://youtrack.jetbrains.com/issues?q=project:%20Rider%20%7Bavailable%20in%7D:%20%7B2025.1.2%20\(251.25410.119\)%7D)

Change

The [JetBrains GoLand preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [GoLand 2025.1.1](https://youtrack.jetbrains.com/articles/GO-A-231735963/GoLand-2025.1.1-251.25410.140-build-Release-Notes)

Change

The [JetBrains RubyMine preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [RubyMine 2025.1.1](https://youtrack.jetbrains.com/articles/RUBY-A-220365264/RubyMine-2025.1.1-251.25410.120-build-Release-Notes)

Change

The [JetBrains WebStorm preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [WebStorm 2025.1.1](https://youtrack.jetbrains.com/articles/WEB-A-233538594/WebStorm-2025.1.1-251.25410.117-build-Release-Notes)

Change

The [JetBrains PyCharm preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [PyCharm 2025.1.1.1](https://youtrack.jetbrains.com/articles/PY-A-233538403/PyCharm-2025.1.1.1-251.25410.159-build-Release-Notes)

Change

The [JetBrains PhpStorm preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [PhpStorm 2025.1.1](https://youtrack.jetbrains.com/articles/WI-A-231736231/PhpStorm-2025.1.1-251.25410.148-build-Release-Notes)

## March 27, 2025

Feature

Cloud Workstations is available in the `me-central2` region (Dammam, Saudi Arabia, Middle East). For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

## January 09, 2025

Feature

Cloud Workstations support for cloning of persistent directories is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Clone a workstation](https://docs.cloud.google.com/workstations/docs/clone-workstation). For reference information, see [REST workstations](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs.workstations#resource:-workstation) and [RPC google.cloud.workstations.v1](https://docs.cloud.google.com/workstations/docs/reference/rpc/google.cloud.workstations.v1#workstation).

## November 18, 2024

Announcement

The [Cloud Workstations base editor](https://docs.cloud.google.com/workstations/docs/preconfigured-ides#cloud-workstations-base-editor) (Code OSS) has been upgraded to 1.94.2. The last image that offers the previous version is tagged `code-oss-1.89.1`.

## November 08, 2024

Feature

Cloud Workstations supports granting access to individual ports. For details, see the [Grant access to individual Cloud Workstations ports](https://docs.cloud.google.com/workstations/docs/configure-port-access) page.

## September 23, 2024

Feature

Cloud Workstations is available in the `us-west4` region (Las Vegas, Nevada, North America). For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

## September 16, 2024

Announcement

Cloud Workstations [preconfigured base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) use Ubuntu 24.04. The last images built on Ubuntu 22.04 are tagged with `last-ubuntu2204` for building backwards compatible custom images.

Change

Cloud Workstations preconfigured base images default to Python 3.12.3.

## August 06, 2024

Feature

If you specify a source workstation during workstation creation, Cloud Workstations supports cloning of persistent directories. For more information, see [REST workstations](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs.workstations#resource:-workstation), [RPC google.cloud.workstations.v1beta](https://docs.cloud.google.com/workstations/docs/reference/rpc/google.cloud.workstations.v1beta#workstation), or [gcloud beta workstations create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/workstations/create).

## June 17, 2024

Feature

Cloud Workstations is available in the `australia-southeast2` region (Melbourne, Australia). For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

## June 13, 2024

Feature

Cloud Workstations is available in the `asia-northeast3` region (Seoul, South Korea). For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

## June 10, 2024

Change

Workstations that enable nested virtualization are hosted on VMs running Container-Optimized OS (COS) instead of Ubuntu.

## May 28, 2024

Change

The [Code-OSS preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses version 1.89.1.

## May 27, 2024

Feature

Cloud Workstations is available in the `us-east5` region (Columbus, Ohio, North America). For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

Feature

Cloud Workstations is available in the `southamerica-east1` region (Osasco, São Paulo, Brazil, South America). For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

## April 29, 2024

Change

Cloud Workstations base images default to Python `3.10.12`

Announcement

[Cloud Workstations base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) use Ubuntu 22.04. The last images built on Ubuntu 20.04 are tagged with `last-ubuntu2004` for building backwards compatible custom images.

## April 08, 2024

Feature

Code Transformations for Gemini Code Assist are available for [Public Preview](https://cloud.google.com/products#product-launch-stages). You can use an inline text box directly in your code file to do the following:

  * Generate comment lines to document your code.
  * Troubleshoot code with issues.
  * Improve code readability.
  * Make code more efficient.



You can also view context sources of a generated response in the **Gemini: Chat** pane.

For more information, see [Code with Gemini Code Assist](https://docs.cloud.google.com/workstations/docs/write-code-gemini#use-code-transformation-features).

## March 22, 2024

Feature

Support for GPUs is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Available GPUs](https://docs.cloud.google.com/workstations/docs/available-gpus).

Feature

Cloud Workstations supports the following machine type:

  * a2-megagpu-16g



For more information, see [Available machine types](https://docs.cloud.google.com/workstations/docs/available-machine-types), [REST workstationConfigs](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs#gceinstance), or [RPC google.cloud.workstations.v1beta GceInstance](https://docs.cloud.google.com/workstations/docs/reference/rpc/google.cloud.workstations.v1beta#gceinstance).

## February 22, 2024

Feature

Cloud Workstations supports [Image Streaming](https://docs.cloud.google.com/workstations/docs/architecture#image-streaming), which provides faster workstations startup by reducing image pull time.

## February 14, 2024

Feature

Cloud Workstations is available in the `europe-west8` region (Milan, Italy, Europe). For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

## January 12, 2024

Feature

Cloud Workstations supports the following machine types:

  * e2-medium 

  * n1-standard-1




For more information, see [Available machine types](https://docs.cloud.google.com/workstations/docs/available-machine-types), [REST workstationConfigs](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs#gceinstance), or [RPC google.cloud.workstations.v1beta GceInstance](https://docs.cloud.google.com/workstations/docs/reference/rpc/google.cloud.workstations.v1beta#gceinstance).

## December 15, 2023

Feature

Support for [custom domains](https://docs.cloud.google.com/workstations/docs/set-up-custom-domains-for-cloud-workstations) is [generally available](https://cloud.google.com/products#product-launch-stages) through the `gcloud` CLI and REST API. To access your workstations, you can specify a trusted, custom domain rather than using the default `cloudworkstations.dev` domain.

## December 11, 2023

Feature

Cloud Workstations supports the following machine type:

  * n2d-highmem



For more information, see [Available machine types](https://docs.cloud.google.com/workstations/docs/available-machine-types), [REST workstationConfigs](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs#gceinstance), or [RPC google.cloud.workstations.v1beta GceInstance](https://docs.cloud.google.com/workstations/docs/reference/rpc/google.cloud.workstations.v1beta#gceinstance).

## November 07, 2023

Feature

Cloud Workstations is available in the `asia-east2` region (Hong Kong, APAC). For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

## November 06, 2023

Change

The [Code-OSS preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses version 1.83.1.

## November 03, 2023

Feature

Support for [custom domains](https://docs.cloud.google.com/workstations/docs/set-up-custom-domains-for-cloud-workstations) is available in [preview](https://cloud.google.com/products#product-launch-stages) through the `gcloud` CLI and REST API. To access your workstations, you can specify a trusted, custom domain rather than using the default `cloudworkstations.dev` domain.

## November 01, 2023

Feature

Duet AI for Cloud Workstations is available. Use Duet AI, your AI-powered collaborator, to accomplish tasks more effectively and efficiently. Duet AI provides contextualized responses to your prompts to help guide you on what you're trying to do with your code. It also shares source citations regarding which documentation and code samples the assistant used to generate its responses. 

If you use the Code - OSS base image, you can use Duet AI in the Cloud Workstations base editor. For more information, see the [Duet AI in Google Cloud overview](https://docs.cloud.google.com/duet-ai/docs/overview) and [Code with Duet AI assistance](https://docs.cloud.google.com/workstations/docs/write-code-duet-ai).

## October 25, 2023

Feature

Cloud Workstations is available in the `northamerica-northeast1` region (Montréal, Québec, North America). For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

## October 02, 2023

Feature

If you use the latest [preconfigured base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) for JetBrains IDEs, the `.vmoptions` and `.properties` files persist across workstations. For more information, see [Customize JetBrains IDE vmoptions and properties](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images#customize_jetbrains_ide_vmoptions_and_properties).

## September 11, 2023

Change

The [JetBrains GoLand preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [GoLand 2023.2.1](https://youtrack.jetbrains.com/articles/GO-A-231735815).

Change

The [JetBrains IntelliJ Ultimate preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [IntelliJ-IDEA 2023.2.1](https://youtrack.jetbrains.com/articles/IDEA-A-2100661651).

Change

The [JetBrains PhpStorm preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [PhpStorm 2023.2.1](https://youtrack.jetbrains.com/articles/WI-A-231736074).

Change

The [JetBrains PyCharm Professional preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [PyCharm Professional 2023.2.1](https://youtrack.jetbrains.com/articles/PY-A-233538128).

Change

The [JetBrains CLion preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [CLion 2023.2.1](https://youtrack.jetbrains.com/articles/CPP-A-230654255).

Change

The [JetBrains WebStorm preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [WebStorm 2023.2.1](https://youtrack.jetbrains.com/articles/WEB-A-233538436).

Change

The [JetBrains RubyMine preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [RubyMine 2023.2.1](https://youtrack.jetbrains.com/articles/RUBY-A-220365103).

## August 29, 2023

Feature

Duet AI for Cloud Workstations is available in [Preview](https://cloud.google.com/products#product-launch-stages). Use Duet AI, your AI-powered collaborator, to accomplish tasks more effectively and efficiently. Duet AI provides contextualized responses to your prompts to help guide you on what you're trying to do with your code. It also shares source citations regarding which documentation and code samples the assistant used to generate its responses. 

If you use the Code - OSS base image, you can use Duet AI in the Cloud Workstations base editor. For more information, see the [Duet AI in Google Cloud overview](https://docs.cloud.google.com/duet-ai/docs/overview) and [Code with Duet AI assistance](https://docs.cloud.google.com/workstations/docs/write-code-duet-ai).

## August 26, 2023

Feature

Posit Workbench (including RStudio Pro) integration is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Develop code using Posit Workbench](https://docs.cloud.google.com/workstations/docs/develop-code-using-posit-workbench-rstudio).

## August 15, 2023

Change

The [JetBrains PyCharm Professional preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses Python version 3.8 as the default for `python`, `python3`, `pip`, and `pip3`. However, Python version 3.10 remains available.

## July 21, 2023

Feature

Cloud Workstations is available in the `europe-west12` region (Turin, Italy, Europe). For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

## July 04, 2023

Feature

Cloud Workstations is available in the `australia-southeast1` region (Sydney, Australia, APAC). For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

## June 21, 2023

Feature

The following [Google Cloud CLI commands](https://docs.cloud.google.com/sdk/gcloud/reference/workstations) are generally available (GA):

  * `gcloud workstations`
  * `gcloud workstations configs`
  * `gcloud workstations clusters`



## June 14, 2023

Change

The [JetBrains CLion preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [CLion 2023.1.3](https://youtrack.jetbrains.com/articles/CPP-A-230654224/CLion-2023.1.3-231.9011.31-build-Release-Notes).

## June 13, 2023

Change

The [Available GPUs](https://docs.cloud.google.com/workstations/docs/available-gpus) page contains additional instructions for using the `gcloud` CLI or `curl` to specify a GPU machine type.

## May 24, 2023

Feature

Cloud Workstations adds Google Cloud console support for the `me-west1` region (Tel Aviv, Israel, Middle East). For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

## May 10, 2023

Announcement

[Cloud Workstations](https://cloud.google.com/workstations) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) and is backed by a [Service Level Agreement (SLA)](https://docs.cloud.google.com/workstations/sla).

Feature

This release includes support for the following features:

  * API and `gcloud` CLI support for the `me-west1` [region](https://docs.cloud.google.com/workstations/docs/locations) (Tel Aviv, Israel, Middle East).
  * API support for [GPUs](https://docs.cloud.google.com/workstations/docs/available-gpus) is available in [preview](https://cloud.google.com/products#product-launch-stages).
  * [Terraform](https://docs.cloud.google.com/workstations/docs/terraform-support-for-cloud-workstations) support is available in [preview](https://cloud.google.com/products#product-launch-stages).
  * [Posit Workbench (including RStudio Pro)](https://docs.cloud.google.com/workstations/docs/develop-code-using-posit-workbench-rstudio) integration is available in [preview](https://cloud.google.com/products#product-launch-stages).
  * [BeyondCorp Enterprise integration for the Cloud Workstations API](https://docs.cloud.google.com/workstations/docs/tutorial-help-secure-workstations-api-using-beyondcorp-enterprise) is available in [preview](https://cloud.google.com/products#product-launch-stages).



## May 05, 2023

Feature

Cloud Workstations supports the following machine types:

  * n1-standard-64
  * n1-standard-96



For more information, see [Available machine types](https://docs.cloud.google.com/workstations/docs/available-machine-types), [REST workstationConfigs](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs#gceinstance), or [RPC google.cloud.workstations.v1beta GceInstance](https://docs.cloud.google.com/workstations/docs/reference/rpc/google.cloud.workstations.v1beta#gceinstance).

## April 25, 2023

Change

The [Code-OSS preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses version 1.77.3.

## April 24, 2023

Change

The [JetBrains CLion preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [CLion 2023.1.1](https://youtrack.jetbrains.com/articles/CPP-A-230654219).

Change

The [JetBrains WebStorm preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [WebStorm 2023.1](https://youtrack.jetbrains.com/articles/WEB-A-233538410).

Change

The [JetBrains IntelliJ Ultimate preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [IntelliJ-IDEA 2023.1](https://youtrack.jetbrains.com/articles/IDEA-A-2100661478/IntelliJ-IDEA-2023.1-231.8109.175-build-Release-Notes).

Change

The [JetBrains GoLand preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [GoLand 2023.1](https://youtrack.jetbrains.com/articles/GO-A-231735788).

Change

The [JetBrains PhpStorm preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [PhpStorm 2023.1](https://youtrack.jetbrains.com/articles/WI-A-231736052/PhpStorm-2023.1-231.8109.199-build-Release-Notes).

Change

The [JetBrains Rider preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [Rider 2023.1](https://youtrack.jetbrains.com/issues?q=project:%20Rider%20Available%20in:%202023.1*).

Change

The [JetBrains RubyMine preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [RubyMine 2023.1](https://youtrack.jetbrains.com/articles/RUBY-A-220365068).

Change

The [JetBrains PyCharm Professional preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [PyCharm Professional 2023.1](https://youtrack.jetbrains.com/articles/PY-A-233538090/PyCharm-2023.1-231.8109.197-build-Release-Notes).

## April 21, 2023

Feature

Cloud Workstations supports the following machine types:

  * n1-standard-2
  * n1-standard-8
  * n1-standard-16
  * n1-standard-32
  * n2-standard-2
  * n2-standard-4



For more information, see [Available machine types](https://docs.cloud.google.com/workstations/docs/available-machine-types), [REST workstationConfigs](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs#gceinstance), or [RPC google.cloud.workstations.v1beta GceInstance](https://docs.cloud.google.com/workstations/docs/reference/rpc/google.cloud.workstations.v1beta#gceinstance).

## April 03, 2023

Change

Cloud Workstations is beginning the migration of [preconfigured base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) to Ubuntu as their base OS. The last images built using Debian are tagged with `:last-debian` in Artifact Registry to allow more time for you to make adjustments to custom images.

Change

The [JetBrains PhpStorm preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [PhpStorm 2022.3.3](https://youtrack.jetbrains.com/articles/WI-A-231736047/PhpStorm-2022.3.3-223.8836.42-build-Release-Notes).

Change

The [JetBrains CLion preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [CLion 2022.3.3](https://youtrack.jetbrains.com/articles/CPP-A-230654213).

Change

The [JetBrains PyCharm Professional preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [PyCharm Professional 2022.3.3](https://youtrack.jetbrains.com/articles/PY-A-233538082/PyCharm-2022.3.3-223.8836.43-build-Release-Notes).

Change

The [JetBrains GoLand preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [GoLand 2022.3.3](https://youtrack.jetbrains.com/articles/GO-A-231735782/GoLand-2022.3.3-223.8836.34-build-Release-Notes).

Change

The [JetBrains Rider preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [Rider 2022.3.3](https://youtrack.jetbrains.com/issues?q=project:%20Rider%20Available%20in:%202022.3*).

Change

The [JetBrains IntelliJ Ultimate preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [IntelliJ-IDEA 2022.3.3](https://youtrack.jetbrains.com/articles/IDEA-A-2100661467/IntelliJ-IDEA-2022.3.3-223.8836.41-build-Release-Notes).

Change

The [JetBrains WebStorm preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [WebStorm 2022.2.3](https://youtrack.jetbrains.com/articles/WEB-A-233538407/WebStorm-223.8836.50-Release-Notes).

Change

The [JetBrains RubyMine preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [RubyMine 2022.3.3](https://youtrack.jetbrains.com/articles/RUBY-A-220365063/RubyMine-2022.3.3-223.8836.42-build-Release-Notes).

## March 31, 2023

Feature

You can use a pre-customized snapshot as the source of a Persistent Disk in Cloud Workstations. For more information, see [About disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots). See also the `sourceSnapshot` within `GceRegionalPersistentDisk` field added to the following REST API resources: [workstation configurations](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs#gceregionalpersistentdisk), and `source_snapshot` in the following RPC resources: [workstations.v1beta](https://docs.cloud.google.com/workstations/docs/reference/rpc/google.cloud.workstations.v1beta#gceregionalpersistentdisk).

Feature

Cloud Workstations is available in the `asia-northeast1` region (Tokyo, Japan, APAC). For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

## March 30, 2023

Feature

You can use [container output logging](https://docs.cloud.google.com/workstations/docs/container-output-logging) to view standard output and standard error logs generated by a workstation container.

## March 29, 2023

Feature

Cloud Workstations is available in the following regions:

  * `asia-south1` (Mumbai, India APAC)
  * `us-east4` (Ashburn, Virginia, North America)



For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

## March 20, 2023

Feature

Newly-created clusters write `vm_assignments` and `disk_assignments` [platform logs](https://docs.cloud.google.com/workstations/docs/platform-logging) to Cloud Logging, indicating when VM instances and persistent disks are allocated to a workstation.

## March 17, 2023

Feature

Cloud Workstations is available in the following regions:

  * `europe-west6` (Zurich, Switzerland, Europe)
  * `europe-west9` (Paris, France, Europe)



For more information, see [Locations](https://docs.cloud.google.com/workstations/docs/locations).

## February 07, 2023

Feature

You can use customer-managed encryption keys (CMEK) to protect Persistent Disks in Cloud Workstations. CMEK in Cloud Workstations is available in Beta. For more information, see [Encrypt workstation resources using customer-managed encryption keys](https://docs.cloud.google.com/workstations/docs/encrypt-workstation-resources-using-cmek).

## January 31, 2023

Feature

Cloud Workstations makes the following machine types available:

  * n2-standard-8
  * n2-standard-16
  * n2-standard-32



For more information, see [Available machine types](https://docs.cloud.google.com/workstations/docs/available-machine-types), [REST workstationConfigs](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs#gceinstance), or [RPC google.cloud.workstations.v1beta GceInstance](https://docs.cloud.google.com/workstations/docs/reference/rpc/google.cloud.workstations.v1beta#gceinstance).

## January 17, 2023

Feature

You can apply custom labels to Cloud Workstations resources. For more information, see [Label resources](https://docs.cloud.google.com/workstations/docs/label-resources) and [Customize workstation configurations](https://docs.cloud.google.com/workstations/docs/customize-workstation-configurations#labels). See also the `labels` field added to the following REST API resources: [workstation clusters](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters), [workstation configurations](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs), [workstations](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs.workstations), and the following RPC resources: [location](https://docs.cloud.google.com/workstations/docs/reference/rpc/google.cloud.location) and [workstations.v1beta](https://docs.cloud.google.com/workstations/docs/reference/rpc/google.cloud.workstations.v1beta).

## October 28, 2022

Change

The [JetBrains RubyMine preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [RubyMine 2022.2.3](https://www.jetbrains.com/ruby/whatsnew/2022-3/).

Change

The [JetBrains PyCharm Professional preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [PyCharm Professional 2022.2.3](https://youtrack.jetbrains.com/articles/PY-A-233538010/PyCharm-2022.2.3-222.4345.23-build-Release-Notes).

Change

The [Code-OSS preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses version 1.73.1.

Change

The [JetBrains WebStorm preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [WebStorm 2022.2.3](https://youtrack.jetbrains.com/articles/WEB-A-233538376/WebStorm-222.4345.14-Release-Notes).

Change

The [JetBrains PhpStorm preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [PhpStorm 2022.2.3](https://youtrack.jetbrains.com/articles/WI-A-231736011/PhpStorm-2022.2.3-222.4345.15-build-Release-Notes).

Change

The [JetBrains IntelliJ Ultimate preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [IntelliJ-IDEA 2022.2.3](https://youtrack.jetbrains.com/articles/IDEA-A-237338663/IntelliJ-IDEA-2022.2.3-222.4345.14-build-Release-Notes).

Change

The [JetBrains Rider preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) continues to use [Rider 2022.2.3](https://www.jetbrains.com/rider/whatsnew/2022-3/). It appears in this list of JetBrains IDEs for completeness.

Change

The [JetBrains CLion preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [CLion 2022.2.4](https://youtrack.jetbrains.com/articles/CPP-A-230654181?_ga=2.88834651.1967166031.1678384520-1418335837.1678384520).

Change

The [JetBrains GoLand preconfigured base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) uses [GoLand 2022.2.4](https://youtrack.jetbrains.com/articles/GO-A-231735760/GoLand-2022.2.4-222.4345.24-build-Release-Notes).

## October 11, 2022

Announcement

Cloud Workstations is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information about using Cloud Workstations, see the [documentation](https://docs.cloud.google.com/workstations/docs/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

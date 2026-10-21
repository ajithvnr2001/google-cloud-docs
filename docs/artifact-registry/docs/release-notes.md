---
url: https://docs.cloud.google.com/artifact-registry/docs/release-notes/
title: Artifact Registry release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:37:02.811237+00:00
---

# Artifact Registry release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Resources ](https://docs.cloud.google.com/artifact-registry/docs/resources)



Send feedback 

#  Artifact Registry release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Artifact Registry. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/artifactregistry-release-notes.xml) directly. 

## September 15, 2026

v1

Feature

Artifact Registry support for managing Conda packages with Artifact Registry repositories is in [Preview](https://cloud.google.com/products#section-22). For more information, see [Get started with Conda packages](https://docs.cloud.google.com/artifact-registry/docs/conda).

## August 07, 2026

v1.

Feature

Artifact Analysis supports malicious package scanning for language packages within container images. Malicious package data is obtained from the [OpenSSF Malicious Packages Repository](https://github.com/ossf/malicious-packages) and reported as **CRITICAL** severity findings. This feature identifies threats such as typosquatting, dependency confusion, and account takeovers. For more information, see [Vulnerability sources](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview#sources).

## July 24, 2026

v1

Feature

Connector repositories act as proxies for upstream sources. All requests to the repository are proxied to the upstream source and no artifacts are cached in Artifact Registry. This configuration allows for full auditability of upstream sources and supports cases where third-party policies prevent artifact caching. For more information, see [Connector repositories overview](https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-overview).

## April 15, 2026

v1

Feature

Platform logs can record data about successful and failed requests made to Artifact Registry repositories. For more information, see [Access and use platform logs](https://docs.cloud.google.com/artifact-registry/docs/platform-logs).

## April 06, 2026

v1.

Feature

You can [manually prewarm images](https://docs.cloud.google.com/artifact-registry/docs/prewarm-images) in Artifact Registry to reduce the cold-start latency for deployments. This feature is only available using the API.

## February 06, 2026

v1.

Feature

When a vulnerability scan detects a secret, Artifact Analysis creates a secret-type occurrence with details about the secret. For more information, see [Scan for secrets](https://docs.cloud.google.com/artifact-analysis/docs/secret-scanning).

## January 28, 2026

v1.

Feature

Artifact Analysis now supports custom organization policies on notes and occurrences. For more information, see [Use custom organization policies](https://docs.cloud.google.com/artifact-analysis/docs/custom-constraints).

## January 21, 2026

v1.

Feature

Artifact Registry is available in the `asia-southeast3` region (Bangkok). For more information, see [Global locations](https://cloud.google.com/about/locations).

## January 20, 2026

v1.

Feature

Artifact Registry now calculates fingerprints for each version of a package pushed to the Artifact Registry repository. You can use the fingerprint to validate that the package wasn't modified when moving between Google Cloud systems, such as Compute Engine and Cloud Build. This feature is in [public preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [Use fingerprints to verify package version identities](https://docs.cloud.google.com/artifact-registry/docs/fingerprint).

## December 22, 2025

v1.

Feature

You can now view attachments for non-Docker Artifact Registry repositories in the Google Cloud console. This feature is in [public preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [List attachments](https://docs.cloud.google.com/artifact-registry/docs/manage-metadata-with-attachments#view).

## December 19, 2025

v1.

Feature

Download rules are now available for Apt repositories in Artifact Registry. For more information, see [Restrict artifact downloads](https://docs.cloud.google.com/artifact-registry/docs/protect-artifacts#restrict_artifact_downloads).

## December 15, 2025

v1.

Feature

When you push a Java, Python, or Node.js package to Artifact Registry, Artifact Analysis can now scan the package for vulnerabilities. For more information, see the following topics:

  * [Package scanning overview](https://docs.cloud.google.com/artifact-analysis/docs/package-scanning-overview).
  * [Scan packages automatically](https://docs.cloud.google.com/artifact-analysis/docs/package-scan-automatic)



## November 24, 2025

v1.

Feature

You can now use [`ExportArtifact()`](https://cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories/exportArtifact) to export an artifact to a Cloud Storage bucket.

## November 04, 2025

v1.

Feature

Artifact Registry support for managing Ruby gems with Artifact Registry repositories is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see the following topics:

  * [Get started with Ruby gems](https://cloud.google.com/artifact-registry/docs/ruby)
  * [Store Ruby gems in Artifact Registry (Quickstart)](https://cloud.google.com/artifact-registry/docs/ruby/store-ruby)



## September 23, 2025

v1

Feature

Layer-based scanning for Artifact Analysis is in [Preview](https://cloud.google.com/products#product-launch-stages). You can view vulnerability metadata for a specific layer of your image digest in the Google Cloud Console and in the GCloud CLI. For more information, see the following topics:

**Google Cloud Console** :

  * [View layer metadata for Go images](https://docs.cloud.google.com/artifact-analysis/docs/scan-go-automatically#layer)
  * [View layer metadata for Java images](https://docs.cloud.google.com/artifact-analysis/docs/scan-java-automatically#layer)
  * [View layer metadata for Node.js images](https://docs.cloud.google.com/artifact-analysis/docs/scan-nodejs-automatically#layer)
  * [View layer metadata for Python images](https://docs.cloud.google.com/artifact-analysis/docs/scan-python-automatically#layer)



**GCloud CLI**

  * [View layer metadata for Go images](https://docs.cloud.google.com/artifact-analysis/docs/scan-go-automatically#layer-gcloud)
  * [View layer metadata for Java images](https://docs.cloud.google.com/artifact-analysis/docs/scan-java-automatically#layer-gcloud)
  * [View layer metadata for Node.js images](https://docs.cloud.google.com/artifact-analysis/docs/scan-nodejs-automatically#layer-gcloud)
  * [View layer metadata for Python images](https://docs.cloud.google.com/artifact-analysis/docs/scan-python-automatically#layer-gcloud)



## August 29, 2025

v1

Change

The Container Analysis API now supports the option of returning partial results during region-down failure conditions when listing notes, listing occurrences, or generating vulnerability summaries. For more information, view the `returnPartialSuccess` parameter for the following requests:

  * [v1.projects.locations.notes.list](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.locations.notes/list)
  * [v1.projects.locations.occurrences.getVulnerabilitySummary](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.locations.occurrences/getVulnerabilitySummary)
  * [v1.projects.locations.occurrences.list](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.locations.occurrences/list)
  * [v1.projects.notes.list](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.notes/list)
  * [v1.projects.occurrences.getVulnerabilitySummary](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences/getVulnerabilitySummary)
  * [v1.projects.occurrences.list](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences/list)
  * [v1beta1.projects.locations.notes.list](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes/list)
  * [v1beta1.projects.locations.occurrences.getVulnerabilitySummary](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/getVulnerabilitySummary)
  * [v1beta1.projects.locations.occurrences.list](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/list)
  * [v1beta1.projects.notes.list](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.notes/list)
  * [v1beta1.projects.occurrences.getVulnerabilitySummary](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.occurrences/getVulnerabilitySummary)
  * [v1beta1.projects.occurrences.list](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.occurrences/list)



## June 25, 2025

v1

Announcement

Artifact Registry generic repositories are now [generally available](https://cloud.google.com/products#product-launch-stages).

Generic repositories store versioned, immutable artifacts that don't have to adhere to any specific package format in Artifact Registry. You can store and manage arbitrary files such as archives, binaries, and media files with no package specifications or management clients.

To get started with generic repositories, see the [quickstart](https://docs.cloud.google.com/artifact-registry/docs/generic/store-generic).

## April 15, 2025

v1

Feature

Artifact Registry attachments are available in [Preview](https://cloud.google.com/products#section-22) for all repository formats. Attachments are artifacts that store metadata about a related artifact stored in Artifact Registry. To get started with attachments, see [Store artifact metadata in attachments](https://docs.cloud.google.com/artifact-registry/docs/store-artifact-metadata-in-attachments).

## April 09, 2025

v1

Feature

Gemini Cloud Assist for Artifact Registry is in [Preview](https://cloud.google.com/products#section-22). You can [learn about your container images with Gemini assistance](https://docs.cloud.google.com/artifact-registry/docs/docker/learn-about-your-container-images-with-gemini-assistance). 

To learn more, read the [Gemini Cloud Assist overview](https://docs.cloud.google.com/gemini/docs/cloud-assist/overview).

## March 14, 2025

v1

Feature

Security Command Center ingests Artifact Analysis scanning findings from images scanned in Artifact Registry and deployed to supported runtimes.

In Security Command Center, you can view container image vulnerabilities within your running workloads across all projects alongside your other security risks in. You can also export these findings to BigQuery for in-depth analysis and long-term storage. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [vulnerability assessment](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#ar-vuln-assessment).

v1

Feature

Artifact Registry remote repositories and virtual repositories for Go are now [Generally Available](https://cloud.google.com/products#section-22). To learn more about Go format repositories, read [Work with Go modules](https://docs.cloud.google.com/artifact-registry/docs/go).

## March 04, 2025

v1

Feature

Artifact Registry is available in the `europe-north2` region (Stockholm). For more information, see [Global locations](https://cloud.google.com/about/locations).

## February 28, 2025

v1

Feature

Artifact Registry is now enabled for use with Cloud KMS Autokey.

Using keys generated by Autokey can help you consistently align with industry standards and recommended practices for data security, including the HSM protection level, separation of duties, key rotation, location, and key specificity. Keys requested using Autokey function identically to other Cloud HSM keys with the same settings.

For more information, see [Enabling customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek). To learn more about Cloud KMS Autokey, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

## February 19, 2025

v1

Issue

Artifact Registry might give a 400 error on pushes or pulls for Workforce Identity Federation users. This issue is caused by Workforce Identity Federation [attribute mappings](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings) in the Artifact Registry URL causing problems on the backend.

To mitigate this issue, you can push or pull from Artifact Registry without attribute mappings, or reduce the length of your attribute mappings.

## November 20, 2024

v1

Feature

Artifact Registry is available in the `northamerica-south1` region (Querétaro, Mexico, North America). For more information, see [Global locations](https://cloud.google.com/about/locations).

## November 19, 2024

v1

Feature

Artifact Registry now provides the option to enable or disable vulnerability scanning on individual repositories. By giving you more granular control over the number of images scanned, this feature can help you manage scanning costs and reduce noise in vulnerability scanning results.

This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

For more information, see [Enable or disable automatic scanning](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning).

## November 11, 2024

v1

Feature

The [Container Registry -> Artifact Registry Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.containerRegistryMigrationAdmin) role simplifies the IAM roles required for the transition from Container Registry to Artifact Registry. For instructions on how to use the role, see [Automatically migrate from Container Registry to Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/auto-migrate-gcr-ar).

## October 21, 2024

v1

Feature

Artifact Analysis now supports manual scans for vulnerabilities in the following types of packages:

  * AlmaLinux OS
  * Chainguard
  * .NET
  * Google Distroless
  * NPM
  * PHP
  * Python
  * Ruby
  * Rust
  * Red Hat Universal Base Image (UBI) 
  * Rocky Linux
  * SUSE Linux Enterprise Server (SLES)
  * Wolfi



You can use the On-Demand Scanning API to manually scan container images locally on your computer or in your registry. Artifact Analysis scans for vulnerabilities in these new packages types, in addition to already supported package types. 

These capabilities are [Generally Available (GA)](https://cloud.google.com/products/#product-launch-stages).

For more information, see [Container scanning overview](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview).

v1

Feature

Artifact Analysis now supports scanning for vulnerabilities in the following types of operating systems:

  * AlmaLinux OS
  * Chainguard
  * Google Distroless
  * Red Hat Universal Base Image (UBI)
  * Rocky Linux
  * SUSE Linux Enterprise Server (SLES)
  * Wolfi



If the Container Scanning API is enabled, it scans container images pushed to Artifact Registry addressing these new operating systems, in addition to already supported operating system and language package vulnerabilities. 

These capabilities are [Generally Available](https://cloud.google.com/products#product-launch-stages). 

For more information, see [Container scanning overview](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview), or [enable Container Scanning API](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning).

## October 18, 2024

v1

Feature

Artifact Registry remote repositories support setting standard Artifact Registry repositories as upstreams for [supported formats](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview#ar-upstreams).

To learn more about how remote repositories work, read the [Remote repository overview](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview).

## October 15, 2024

v1

Feature

Organization policy constraints for Artifact Registry is available in **General Availability**.

For more information, see [Use custom organization policies](https://docs.cloud.google.com/artifact-registry/docs/custom-constraints).

## October 09, 2024

v1

Feature

Artifact Registry artifact download rules are in Preview.

Download rules let you restrict downloads at the repository and package level. To learn more, see [Restrict artifact downloads](https://docs.cloud.google.com/artifact-registry/docs/protect-artifacts#restrict_artifact_downloads). To configure download rules, follow the instructions in [Restrict artifact downloads with download rules](https://docs.cloud.google.com/artifact-registry/docs/restrict-artifact-downloads).

## October 03, 2024

v1

Feature

Artifact Registry support for [OCI specifications v1.1](https://github.com/opencontainers/image-spec) is [generally available](https://cloud.google.com/products/#product-launch-stages) in Docker format repositories.

You can upload containerized metadata about another container image to Artifact Registry as an attachment. To learn more, see [Manage container metadata](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-metadata).

## September 30, 2024

v1

Feature

Artifact Analysis is gradually rolling out regionalized data storage and endpoints to help support compliance with data residency requirements. The Container Analysis API stores metadata in the same region or multi-region as the Artifact Registry repository where your image is scanned. 

For more information, see [Metadata storage locations](https://docs.cloud.google.com/artifact-analysis/docs/locations).

## August 30, 2024

v1

Feature

Artifact Registry records metrics and logs for your projects. To explore the available Artifact Registry metrics and logs, view your project in the [Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer) or the [Logs Explorer](https://console.cloud.google.com/logs/query).

For more information about metrics and logs, read [Observability in Google Cloud](https://docs.cloud.google.com/stackdriver/docs).

v1

Change

Updates to the Artifact Registry API are as follows:

  * Add or update file annotations with [`UpdateFile()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateFile).
  * Add or update package version annotations with [`UpdateVersion()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateVersion).
  * Filter by annotation or name with [`ListFiles()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListFiles), [`ListPackages()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListPackages), and [`ListVersions()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListVersions).
  * Filter by name with [`ListTags()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListTags), [`ListRepositories()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListRepositories) and [`ListDockerImages()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListDockerImages).
  * Order by `name`, `createTime`, or `updateTime` for [`ListFiles()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListFiles), [`ListVersions()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListVersions), [`ListRepositories()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListRepositories), and [`ListPackages()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListPackages).



## August 21, 2024

v1

Change

The following Artifact Registry Cloud Audit Log method names have changed:

  * `Docker-EmptyTarBlob` is renamed `Docker-ServeBlob`
  * `Docker-GetEmptyTags` is renamed `Docker-GetTags`
  * `Docker-HeadEmptyTarBlob` is renamed `Docker-HeadBlob`
  * `Kfp-UploadPackage-Redirect` is renamed `Kfp-UploadPackage`
  * `Apt-ViewRemoteIndexFile` is renamed to indicate the type of file requested: 
    * `Apt-ViewIndexFile`: when a repository metadata file is requested
    * `Apt-Contents`: when the Contents index file for a specific repository component and architecture type is requested
    * `Apt-ViewArchIndexFile`: when the Packages index file for a specific repository component and architecture type is requested
  * `Apt-ViewRemotePackageFile` is renamed `Apt-ViewPackageFile`
  * `Yum-ViewUpstreamFile` is renamed to indicate the type of file requested: 
    * `Yum-ViewIndexKey`: when the public key for signing Yum packages is requested
    * `Yum-ViewIndexFile`: when one of a repository's index files is requested
    * `Yum-ViewPackageFile`: when a Yum package file is requested



For more information on Artifact Registry logs, see [Audit Logging](https://docs.cloud.google.com/artifact-registry/docs/audit-logging).

## May 24, 2024

v1

Feature

[Cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy) for Artifact Registry are Generally Available (GA).

Cleanup policies help you manage artifacts by automatically deleting artifacts that you no longer need, while keeping artifacts that you want to store.

Deletions requested by Cleanup policies count against Artifact Registry delete request [quota and limits](https://docs.cloud.google.com/artifact-registry/quotas).

## May 10, 2024

v1

Feature

Artifact Registry generic repositories are available in Preview.

Generic repositories store versioned, immutable artifacts that don't have to adhere to any specific package format in Artifact Registry. You can store and manage arbitrary files such as archives, binaries, and media files with no package specifications or management clients.

To get started with generic repositories, see the [quickstart](https://docs.cloud.google.com/artifact-registry/docs/generic/store-generic).

## April 19, 2024

v1

Feature

Artifact Registry download file feature is Generally Available (GA) for standard repositories and remote repositories.

The download file feature allows users to download individual files without configuring authentication for format-specific tooling. For more information, see [Download files](https://docs.cloud.google.com/artifact-registry/docs/repositories/download-files).

## April 18, 2024

v1

Feature

The immutable tags setting is generally available for Docker repositories. When tags are immutable, you can't change the image digest that a tag references in the repository. You can configure this setting when you [create a repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) or [change the setting](https://docs.cloud.google.com/artifact-registry/docs/repositories/update-repo-settings) on an existing repository.

## April 02, 2024

v1

Feature

Artifact Analysis automatic scanning for Ruby, Rust, .NET and PHP vulnerabilities in container images is now [generally available](https://cloud.google.com/products/#product-launch-stages). If the Container Scanning API is enabled, it scans container images pushed to Artifact Registry for Ruby, Rust, .NET and PHP vulnerabilities, in addition to already supported operating system and language package vulnerabilities.

Artifact Analysis returns Ruby, Rust, .NET and PHP vulnerability results for images that have a [supported](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview#feature-support) or unsupported operating system. When you push new versions of images to the registry, you might see more successful vulnerability scans against images without a supported operating system.

For more information, see [Container scanning overview](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview).

## March 25, 2024

v1

Change

Artifact Analysis support for Vulnerability Exploitability eXchange (VEX) statements now includes the capability to upload VEX statements for multiple versions of an image. You can specify whether to associate a VEX statement with one image digest, or all versions of an image. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). To learn more, see [Upload VEX statements](https://docs.cloud.google.com/artifact-analysis/docs/upload-vex).

v1

Feature

The software bill of materials (SBOM) feature is now [Generally Available (GA)](https://cloud.google.com/products#product-launch-stages). To learn more, see [SBOM overview](https://docs.cloud.google.com/artifact-analysis/docs/sbom-overview).

## March 22, 2024

v1

Change

Effective March 22, 2024, Artifact Registry npm repositories enforce not including uppercase letters in package names in order to match [npmjs naming rules](https://docs.npmjs.com/cli/v10/configuring-npm/package-json). Packages with uppercase letters in their names pushed to Artifact Registry prior to this date aren't affected by this change unless you want to push them to a new repository.

## March 19, 2024

v1

Fixed

Fixed the issue causing images copied to Artifact Registry from Container Registry with the [automatic migration tool](https://docs.cloud.google.com/artifact-registry/docs/transition/auto-migrate-gcr-ar) to fail to propagate their creation time to Artifact Registry. Artifact Registry creation time is set to the time the image was uploaded to Container Registry, and update time is set to the time the image is copied to Artifact Registry.

## March 15, 2024

v1

Feature

Artifact Registry remote repositories support basic authentication to user-defined and preset upstream sources for Docker, Maven, npm, and Python formats.

To create a remote repository using a preset or user-defined upstream source, see [Create remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo). For more information on remote repository authentication, see [Configure authentication to remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/configure-remote-authentication).

v1

Issue

Images copied to Artifact Registry from Container Registry with the [automatic migration tool](https://cloud.google.com/artifact-registry/docs/transition/auto-migrate-gcr-ar) are failing to propagate their upload time to Artifact Registry, and instead have their upload time value set to zero, resulting in an upload time of early 1970. If you have cleanup policies that delete images based on upload time, this might mean all your copied images are deleted. We are actively working on a fix for this issue.

## January 31, 2024

v1

Feature

Artifact Registry is available in the `africa-south1` [region](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations#location-r) (Johannesburg, South Africa).

## January 12, 2024

v1

Feature

Artifact Registry Tags are Generally Available (GA). Tags are key-value pairs that you can use to group repositories and other resources across Google Cloud for reporting, auditing, and access control within your Google Cloud organization. To learn more, see [Tag repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/tag-repos).

## October 31, 2023

v1

Feature

Artifact Registry remote repositories now support authentication to Docker Hub upstream repositories. 

To create a Docker Hub remote repository, take the [quickstart](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-dockerhub-remote-repository).

## October 27, 2023

v1

Feature

Artifact Registry remote repositories are now generally available. 

Remote repositories store artifacts from external sources such as Docker Hub or PyPI. A remote repository acts as a proxy for the external source so that you have more control over your external dependencies. The first time that you request a version of a package, Artifact Registry downloads and caches the package in the remote repository. The next time you request the same package version, Artifact Registry serves the cached copy.

To get started with remote repositories, try the [quickstart](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-dockerhub-remote-repository).

v1

Feature

Artifact Registry virtual repositories are now generally available.

Virtual repositories act as a single access point to download, install, or deploy artifacts in the same format from one or more upstream repositories. An upstream repository can be an Artifact Registry standard or remote repository.

To get started with virtual repositories, [create a virtual repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo), or see an example of how to use the different repository modes together in the repository overview [usage example](https://docs.cloud.google.com/artifact-registry/docs/repositories#example).

## September 19, 2023

v1

Change

Artifact Registry is now available in the `me-central2` [region](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations#location-r) (Dammam, Saudi Arabia).

## September 13, 2023

v1

Feature

Artifact Registry now supports HTTP access to Apt repositories. For more information, see [Configure HTTP access to an Apt repository](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure#configure_http_access_to_an_apt_repository).

## August 29, 2023

v1

Feature

Artifact Analysis automatic scanning for Python and Node.js (npm) vulnerabilities in container images is now [generally available](https://cloud.google.com/products/#product-launch-stages). If the Container Scanning API is enabled, it scans container images pushed to Artifact Registry for Python and Node.js vulnerabilities, in addition to operating system vulnerabilities.

Artifact Analysis returns Python and Node.js vulnerability results for images that have a [supported](https://docs.cloud.google.com/artifact-analysis/docs/os-overview#linux-versions) or unsupported operating system. When you push new versions of images to the registry, you might see more successful vulnerability scans and corresponding charges against images without a supported operating system.

For more information, see [Python overview](https://docs.cloud.google.com/artifact-analysis/docs/python-overview) and [Node.js overview](https://docs.cloud.google.com/artifact-analysis/docs/nodejs-overview).

v1

Feature

Artifact Analysis now offers the ability to export a consolidated software bill of materials (SBOM) for scanned containers in Artifact Registry. SBOMs are generated in the Software Package Data Exchange (SPDX) format; however, you can also ingest externally created SBOMs in either SPDX or CycloneDx formats. With this new capability, you can centrally manage SBOMs to gain visibility into key information about your software supply chain.

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages). To learn more about our SBOM capabilities, see [SBOM overview](https://docs.cloud.google.com/artifact-analysis/docs/sbom-overview).

v1

Feature

Artifact Analysis now offers support for Vulnerability Exploitability eXchange (VEX). VEX is a type of security advisory that indicates whether a product is affected by a known vulnerability. For every container image pushed to Artifact Registry, Artifact Analysis can store an associated VEX statement.

You can upload VEX files to describe any vulnerabilities discovered in specific artifacts and provide context about their impact. VEX statuses can be used to assist your organization in triaging vulnerabilities. 

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages). To learn more, see [Upload and view VEX statements](https://docs.cloud.google.com/artifact-analysis/docs/upload-view-vex-statements).

## August 22, 2023

v1

Feature

Artifact Registry is now available in the `europe-west10` [region](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations#location-r) (Berlin, Germany).

## August 16, 2023

v1

Feature

Artifact Registry remote repositories for OS packages are now in [Preview](https://cloud.google.com/products#product-launch-stages).

A remote repository stores artifacts from external sources such as Docker Hub, Maven Central, the Python Package Index (PyPI), Debian or CentOS. A remote repository acts as a proxy for the external source to enable more control over external dependencies. 

For more information on which public OS package repositories are supported by Artifact Registry remote repositories, see [OS packages supported upstreams](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview#supported-os-upstreams). To create a remote repository for OS packages, see [Create remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo#create-gcloud).

## July 11, 2023

v1

Announcement

Starting July 11, 2023, Artifact Registry write requests and delete requests have their own quotas. For more information on this change, see [Quotas and limits](https://docs.cloud.google.com/artifact-registry/quotas).

v1

Feature

[Cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy) for Artifact Registry are now in Preview. Cleanup policies help you manage artifacts by automatically deleting artifacts that you no longer need, while keeping artifacts that you want to store.

Deletions requested by Cleanup policies count against Artifact Registry delete request [quota and limits](https://docs.cloud.google.com/artifact-registry/quotas).

## June 30, 2023

v1

Feature

[Go repositories](https://docs.cloud.google.com/artifact-registry/docs/go) are now generally available.

[Storage and network egress charges](https://cloud.google.com/artifact-registry/pricing) apply to all formats that are generally available.

## March 30, 2023

v1

Feature

Artifact Registry is now available in the `me-central1` [region](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations#location-r) (Doha, Qatar).

## March 29, 2023

v1

Feature

Artifact Registry is now available in the `europe-west12` [region](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations#location-r) (Turin, Italy).

## March 28, 2023

v1

Feature

Artifact Registry repositories with [gcr.io domain support](https://docs.cloud.google.com/artifact-registry/docs/transition/setup-gcr-repo) are now [generally available](https://cloud.google.com/products#product-launch-stages). These repositories can host your existing Container Registry images and automatically redirect requests for gcr.io hosts to corresponding Artifact Registry repositories.

## March 23, 2023

v1

Feature

The immutable tags setting is now in Preview for Docker repositories. When tags are immutable, you cannot change the image digest that a tag references in the repository. You can configure this setting when you [create a repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) or [change the setting](https://docs.cloud.google.com/artifact-registry/docs/repositories/update-repo-settings) on an existing repository.

## February 14, 2023

v1

Feature

Artifact Registry remote repositories and virtual repositories are now in Preview. These features help you to optimize your build and deployment workflows.

  * [Remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo) cache artifacts from external sources, including Docker Hub, Maven Central, PyPI, and the npm registry.
  * [Virtual repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo) provide a single access point to download artifacts from multiple remote or standard repositories. Each upstream repository has a set priority to protect against issues with dependency confusion.



## February 09, 2023

v1

Feature

Container Analysis automatic scanning for Java and Go vulnerabilities in container images is now [generally available](https://cloud.google.com/products/#product-launch-stages). If the Container Scanning API is enabled, it scans container images pushed to Artifact Registry for Java and Go vulnerabilities, in addition to operating system vulnerabilities.

Container Analysis returns Java and Go vulnerability results for images that have a [supported](https://docs.cloud.google.com/container-analysis/docs/os-overview#linux-versions) or unsupported operating system. When you push new versions of images to the registry, you might see more successful vulnerability scans and corresponding charges against images without a supported operating system.

For more information, see the [Types of scanning](https://docs.cloud.google.com/container-analysis/docs/scanning-types) in the Container Analysis documentation

## October 11, 2022

v1

Feature

When users enable the Container Scanning API and push container images to Artifact Registry, automatic container scanning now generates metadata including a software bill of materials (SBOM) dependency list. Users can analyze the metadata to gain insights into software dependencies and vulnerabilities. For more information, see [Examine dependencies](https://docs.cloud.google.com/container-analysis/docs/examine-dependencies). This feature is in [private preview](https://cloud.google.com/products#product-launch-stages).

## October 07, 2022

v1

Change

Version 2.2.0 of the Java credential helpers for [authentication](https://cloud.google.com/artifact-registry/docs/java/authentication) are now available. This version improves performance and reduces the quantity of logging messages.

  * [Artifact Registry Maven Wagon](https://search.maven.org/artifact/com.google.cloud.artifactregistry/artifactregistry-maven-wagon)
  * [Artifact Registry Gradle Plugin](https://plugins.gradle.org/plugin/com.google.cloud.artifactregistry.gradle-plugin)



## September 13, 2022

v1

Feature

Artifact Registry is now available in the `me-west1` [region](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations#location-r) (Tel Aviv, Israel).

## August 25, 2022

v1

Feature

Container Analysis automatic scanning for Java and Go vulnerabilities in container images is now in Preview. If the Container Scanning API is enabled, it scans container images pushed to Artifact Registry for Java and Go vulnerabilities, in addition to operating system vulnerabilities.

Container Analysis returns Java and Go vulnerability results for images that have a [supported](https://docs.cloud.google.com/container-analysis/docs/os-overview#linux-versions) or unsupported operating system. When you push new versions of images to the registry, you might see more successful vulnerability scans and corresponding charges against images without a supported operating system.

For more information, see the [Types of scanning](https://docs.cloud.google.com/container-analysis/docs/scanning-types) in the Container Analysis documentation.

## July 02, 2022

v1

Feature

Artifact Registry is now available in the `us-south1` [region](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations#location-r) (Dallas, United States).

## June 09, 2022

v1

Feature

[Audit logs](https://docs.cloud.google.com/artifact-registry/docs/audit-logging) for Maven, npm, and Python repositories are now available in Cloud Logging.

## May 25, 2022

v1

Feature

[Apt](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian) and [Yum](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm) repositories are now generally available.

## May 24, 2022

v1

Feature

Artifact Registry is now available in the `us-east5` [region](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations#location-r) (Columbus, United States).

## May 10, 2022

v1

Feature

Artifact Registry is now available in the `europe-southwest1` [region](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations#location-r) (Madrid, Spain).

## May 03, 2022

v1

Feature

Artifact Registry is now available in the `europe-west9` [region](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations#location-r) (Paris, France).

## May 02, 2022

v1

Change

Getting and listing Artifact Registry locations in a project now requires the following permissions:

  * `artifactregistry.locations.list`
  * `artifactregistry.locations.get`



You can grant these permissions with the [Artifact Registry Reader role](https://docs.cloud.google.com/artifact-registry/docs/access-control#roles) (`roles/artifactregistry.reader`) role or another role that includes these permissions.

## April 20, 2022

v1

Feature

Artifact Registry is now available in `europe-west8` [region](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations#location-r) (Milan, Italy).

## March 25, 2022

v1

Feature

Artifact Registry support for attaching tags to repositories is now in [Preview](https://cloud.google.com/products#product-launch-stages). Tags are key-value pairs that you can use to group repositories and other resources across Google Cloud for reporting, auditing, and access control within your Google Cloud organization.. To learn more, see [Tagging repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/tag-repos).

## March 01, 2022

v1beta2

Change

Support for Python repository hostnames ending in `pypi.pkg.dev` is no longer available. If you use commands that reference hosts with `LOCATION-pypi.pkg.dev` you must replace these references with `LOCATION-python.pkg.dev`.

The `pypi.pkg.dev` hostname was available when Python repositories were available in alpha, and alpha users were notified about the change.

## February 15, 2022

v1beta2

Feature

On-Demand Scanning for Go packages is now [generally available](https://cloud.google.com/products/#product-launch-stages).

You can [scan your container images](https://docs.cloud.google.com/container-analysis/docs/go-quickstart) and identify [Go package vulnerabilities](https://docs.cloud.google.com/container-analysis/docs/go-overview).

## November 15, 2021

v1beta2

Feature

Artifact Registry repositories with [gcr.io domain support](https://docs.cloud.google.com/artifact-registry/docs/transition/setup-gcr-repo) are now available in [Preview](https://cloud.google.com/products#product-launch-stages). These _gcr.io repositories_ provide some features that are backwards-compatible with Container Registry.

## October 04, 2021

v1beta2

Feature

You can now specify a release or snapshot [version policy](https://docs.cloud.google.com/artifact-registry/docs/java#policy) for Maven repositories when you [create](https://docs.cloud.google.com/artifact-registry/docs/manage-repos#create) them. You cannot change the version policy of an existing repository. Repositories created before availability of this feature accept both snapshot and release packages.

## September 08, 2021

v1beta2

Feature

[Maven](https://docs.cloud.google.com/artifact-registry/docs/java), [npm](https://docs.cloud.google.com/artifact-registry/docs/nodejs), and [Python](https://docs.cloud.google.com/artifact-registry/docs/python) repositories are now generally available. 

[Storage and network egress charges](https://cloud.google.com/artifact-registry/pricing) apply to all formats that are in Preview or are generally available.

## August 03, 2021

v1beta2

Feature

[Apt](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian) and [Yum](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm) repositories are now in Preview. 

[Storage and network egress charges](https://cloud.google.com/artifact-registry/pricing) apply to all formats that are in Preview or are generally available.

## July 23, 2021

v1beta2

Feature

Artifact Registry now supports Cloud External Key Manager (Cloud EKM) when using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek).

## July 13, 2021

v1beta2

Feature

On-Demand Scanning for Java packages is now [generally available](https://cloud.google.com/products/#product-launch-stages).

You can [scan your container images](https://docs.cloud.google.com/container-analysis/docs/java-quickstart) and identify [Java package vulnerabilities](https://docs.cloud.google.com/container-analysis/docs/java-overview).

## June 04, 2021

v1beta2

Feature

[Maven](https://docs.cloud.google.com/artifact-registry/docs/java), [npm](https://docs.cloud.google.com/artifact-registry/docs/nodejs), and [Python](https://docs.cloud.google.com/artifact-registry/docs/python) repositories are now in Preview. 

[Storage and network egress charges](https://cloud.google.com/artifact-registry/pricing) apply to all formats that are in Preview or are generally available.

## June 03, 2021

v1beta2

Feature

Artifact Registry now supports Access Transparency. Access Transparency provides you with logs of actions that Google staff have taken when accessing your data. To learn more about Access Transparency, see the [Overview of Access Transparency](https://docs.cloud.google.com/logging/docs/audit/access-transparency-overview#overview).

## May 03, 2021

v1beta2

Feature

Artifact Registry now supports [audit logging](https://docs.cloud.google.com/artifact-registry/docs/audit-logging) for container images in Cloud Audit Logs.

## February 26, 2021

v1beta2

Feature

Support for Python packages in private Python repositories is now in alpha. This feature is only available to alpha users. If you are interested in joining the alpha, fill in the [sign up form](https://docs.google.com/forms/d/e/1FAIpQLSf5q3CeDna_c27ifadF1KO17W3PrYO91w-UI-jjUdnvGS1cmQ/viewform?usp=sf_link).

  * See the [quickstart](https://docs.cloud.google.com/artifact-registry/docs/python/quickstart) to get started.
  * Learn more about working with Python packages in the [overview](https://docs.cloud.google.com/artifact-registry/docs/python).



## February 02, 2021

v1beta2

Feature

On-Demand Scanning is available in Preview. You can manually scan Docker container images stored locally on your computer or remotely in Artifact Registry. To get started with manual scanning, see [On-Demand Scanning quickstart](https://docs.cloud.google.com/container-analysis/docs/ods-quickstart)

## November 16, 2020

v1beta2

Announcement

[Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) is now [generally available](https://cloud.google.com/products/#product-launch-stages). To learn about transitioning from Container Registry, see the [transition overview](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr).

## August 17, 2020

v1beta2

Feature

You can now use Pub/Sub to configure notifications for changes in Docker repositories. For more information, see [Configuring Pub/Sub notifications](https://docs.cloud.google.com/artifact-registry/docs/configure-notifications).

## July 14, 2020

v1beta2

Feature

You can now use Customer-Managed Encryption Keys (CMEK) to protect repository data in Artifact Registry. For more information, see [Enabling customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek).

## March 16, 2020

v1beta2

Feature

Artifact Registry is now in beta.

Artifact Registry is the evolution of Container Registry, with support for Docker as well as Maven and npm package formats.

If you currently use Container Registry, see [Migration and upgrade from Container Registry](https://docs.cloud.google.com/artifacts/docs/upgrade) for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

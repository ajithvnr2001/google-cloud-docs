---
url: https://docs.cloud.google.com/feeds/artifactregistry-release-notes.xml
title: Artifact Registry - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:45:20.831737+00:00
---

# Artifact Registry - Release notes

> Source: https://docs.cloud.google.com/feeds/artifactregistry-release-notes.xml

tag:google.com,2016:artifactregistry-release-notesArtifact Registry - Release notesGoogle Cloud Platform2026-09-15T00:00:00-07:00September 15, 2026tag:google.com,2016:artifactregistry-release-notes#September_15_20262026-09-15T00:00:00-07:00v1 

### Feature

Artifact Registry support for managing Conda packages with Artifact Registry repositories is in [Preview](https://cloud.google.com/products#section-22). For more information, see [Get started with Conda packages](https://docs.cloud.google.com/artifact-registry/docs/conda).

]]> July 24, 2026tag:google.com,2016:artifactregistry-release-notes#July_24_20262026-07-24T00:00:00-07:00v1 

### Feature

Connector repositories act as proxies for upstream sources. All requests to the repository are proxied to the upstream source and no artifacts are cached in Artifact Registry. This configuration allows for full auditability of upstream sources and supports cases where third-party policies prevent artifact caching. For more information, see [Connector repositories overview](https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-overview).

]]> April 15, 2026tag:google.com,2016:artifactregistry-release-notes#April_15_20262026-04-15T00:00:00-07:00v1 

### Feature

Platform logs can record data about successful and failed requests made to Artifact Registry repositories. For more information, see [Access and use platform logs](https://docs.cloud.google.com/artifact-registry/docs/platform-logs).

]]> April 06, 2026tag:google.com,2016:artifactregistry-release-notes#April_06_20262026-04-06T00:00:00-07:00v1 

### Feature

You can [manually prewarm images](https://docs.cloud.google.com/artifact-registry/docs/prewarm-images) in Artifact Registry to reduce the cold-start latency for deployments. This feature is only available using the API.

]]> January 21, 2026tag:google.com,2016:artifactregistry-release-notes#January_21_20262026-01-21T00:00:00-08:00v1 

### Feature

Artifact Registry is available in the `asia-southeast3` region (Bangkok). For more information, see [Global locations](https://cloud.google.com/about/locations).

]]> January 20, 2026tag:google.com,2016:artifactregistry-release-notes#January_20_20262026-01-20T00:00:00-08:00v1 

### Feature

Artifact Registry now calculates fingerprints for each version of a package pushed to the Artifact Registry repository. You can use the fingerprint to validate that the package wasn't modified when moving between Google Cloud systems, such as Compute Engine and Cloud Build. This feature is in [public preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [Use fingerprints to verify package version identities](https://docs.cloud.google.com/artifact-registry/docs/fingerprint).

]]> November 24, 2025tag:google.com,2016:artifactregistry-release-notes#November_24_20252025-11-24T00:00:00-08:00v1 

### Feature

You can now use [`ExportArtifact()`](https://cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories/exportArtifact) to export an artifact to a Cloud Storage bucket.

]]> November 04, 2025tag:google.com,2016:artifactregistry-release-notes#November_04_20252025-11-04T00:00:00-08:00v1 

### Feature

Artifact Registry support for managing Ruby gems with Artifact Registry repositories is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see the following topics:

  * [Get started with Ruby gems](https://cloud.google.com/artifact-registry/docs/ruby)
  * [Store Ruby gems in Artifact Registry (Quickstart)](https://cloud.google.com/artifact-registry/docs/ruby/store-ruby)

]]> September 23, 2025tag:google.com,2016:artifactregistry-release-notes#September_23_20252025-09-23T00:00:00-07:00v1 

### Feature

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

]]> August 29, 2025tag:google.com,2016:artifactregistry-release-notes#August_29_20252025-08-29T00:00:00-07:00v1 

### Change

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

]]> June 25, 2025tag:google.com,2016:artifactregistry-release-notes#June_25_20252025-06-25T00:00:00-07:00v1 

### Announcement

Artifact Registry generic repositories are now [generally available](https://cloud.google.com/products#product-launch-stages).

Generic repositories store versioned, immutable artifacts that don't have to adhere to any specific package format in Artifact Registry. You can store and manage arbitrary files such as archives, binaries, and media files with no package specifications or management clients.

To get started with generic repositories, see the [quickstart](https://docs.cloud.google.com/artifact-registry/docs/generic/store-generic).

]]> April 15, 2025tag:google.com,2016:artifactregistry-release-notes#April_15_20252025-04-15T00:00:00-07:00v1 

### Feature

Artifact Registry attachments are available in [Preview](https://cloud.google.com/products#section-22) for all repository formats. Attachments are artifacts that store metadata about a related artifact stored in Artifact Registry. To get started with attachments, see [Store artifact metadata in attachments](https://docs.cloud.google.com/artifact-registry/docs/store-artifact-metadata-in-attachments).

]]> April 09, 2025tag:google.com,2016:artifactregistry-release-notes#April_09_20252025-04-09T00:00:00-07:00v1 

### Feature

Gemini Cloud Assist for Artifact Registry is in [Preview](https://cloud.google.com/products#section-22). You can [learn about your container images with Gemini assistance](https://docs.cloud.google.com/artifact-registry/docs/docker/learn-about-your-container-images-with-gemini-assistance). 

To learn more, read the [Gemini Cloud Assist overview](https://docs.cloud.google.com/gemini/docs/cloud-assist/overview).

]]> March 14, 2025tag:google.com,2016:artifactregistry-release-notes#March_14_20252025-03-14T00:00:00-07:00v1 

### Feature

Security Command Center ingests Artifact Analysis scanning findings from images scanned in Artifact Registry and deployed to supported runtimes.

In Security Command Center, you can view container image vulnerabilities within your running workloads across all projects alongside your other security risks in. You can also export these findings to BigQuery for in-depth analysis and long-term storage. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [vulnerability assessment](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#ar-vuln-assessment).

### Feature

Artifact Registry remote repositories and virtual repositories for Go are now [Generally Available](https://cloud.google.com/products#section-22). To learn more about Go format repositories, read [Work with Go modules](https://docs.cloud.google.com/artifact-registry/docs/go).

]]> March 04, 2025tag:google.com,2016:artifactregistry-release-notes#March_04_20252025-03-04T00:00:00-08:00v1 

### Feature

Artifact Registry is available in the `europe-north2` region (Stockholm). For more information, see [Global locations](https://cloud.google.com/about/locations).

]]> February 28, 2025tag:google.com,2016:artifactregistry-release-notes#February_28_20252025-02-28T00:00:00-08:00v1 

### Feature

Artifact Registry is now enabled for use with Cloud KMS Autokey.

Using keys generated by Autokey can help you consistently align with industry standards and recommended practices for data security, including the HSM protection level, separation of duties, key rotation, location, and key specificity. Keys requested using Autokey function identically to other Cloud HSM keys with the same settings.

For more information, see [Enabling customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek). To learn more about Cloud KMS Autokey, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

]]> February 19, 2025tag:google.com,2016:artifactregistry-release-notes#February_19_20252025-02-19T00:00:00-08:00v1 

### Issue

Artifact Registry might give a 400 error on pushes or pulls for Workforce Identity Federation users. This issue is caused by Workforce Identity Federation [attribute mappings](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings) in the Artifact Registry URL causing problems on the backend.

To mitigate this issue, you can push or pull from Artifact Registry without attribute mappings, or reduce the length of your attribute mappings.

]]> November 20, 2024tag:google.com,2016:artifactregistry-release-notes#November_20_20242024-11-20T00:00:00-08:00v1 

### Feature

Artifact Registry is available in the `northamerica-south1` region (Querétaro, Mexico, North America). For more information, see [Global locations](https://cloud.google.com/about/locations).

]]> November 19, 2024tag:google.com,2016:artifactregistry-release-notes#November_19_20242024-11-19T00:00:00-08:00v1 

### Feature

Artifact Registry now provides the option to enable or disable vulnerability scanning on individual repositories. By giving you more granular control over the number of images scanned, this feature can help you manage scanning costs and reduce noise in vulnerability scanning results.

This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

For more information, see [Enable or disable automatic scanning](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning).

]]> November 11, 2024tag:google.com,2016:artifactregistry-release-notes#November_11_20242024-11-11T00:00:00-08:00v1 

### Feature

The [Container Registry -> Artifact Registry Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.containerRegistryMigrationAdmin) role simplifies the IAM roles required for the transition from Container Registry to Artifact Registry. For instructions on how to use the role, see [Automatically migrate from Container Registry to Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/auto-migrate-gcr-ar).

]]> October 21, 2024tag:google.com,2016:artifactregistry-release-notes#October_21_20242024-10-21T00:00:00-07:00v1 

### Feature

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

### Feature

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

]]> October 18, 2024tag:google.com,2016:artifactregistry-release-notes#October_18_20242024-10-18T00:00:00-07:00v1 

### Feature

Artifact Registry remote repositories support setting standard Artifact Registry repositories as upstreams for [supported formats](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview#ar-upstreams).

To learn more about how remote repositories work, read the [Remote repository overview](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview).

]]> October 15, 2024tag:google.com,2016:artifactregistry-release-notes#October_15_20242024-10-15T00:00:00-07:00v1 

### Feature

Organization policy constraints for Artifact Registry is available in **General Availability**.

For more information, see [Use custom organization policies](https://docs.cloud.google.com/artifact-registry/docs/custom-constraints).

]]> October 09, 2024tag:google.com,2016:artifactregistry-release-notes#October_09_20242024-10-09T00:00:00-07:00v1 

### Feature

Artifact Registry artifact download rules are in Preview.

Download rules let you restrict downloads at the repository and package level. To learn more, see [Restrict artifact downloads](https://docs.cloud.google.com/artifact-registry/docs/protect-artifacts#restrict_artifact_downloads). To configure download rules, follow the instructions in [Restrict artifact downloads with download rules](https://docs.cloud.google.com/artifact-registry/docs/restrict-artifact-downloads).

]]> October 03, 2024tag:google.com,2016:artifactregistry-release-notes#October_03_20242024-10-03T00:00:00-07:00v1 

### Feature

Artifact Registry support for [OCI specifications v1.1](https://github.com/opencontainers/image-spec) is [generally available](https://cloud.google.com/products/#product-launch-stages) in Docker format repositories.

You can upload containerized metadata about another container image to Artifact Registry as an attachment. To learn more, see [Manage container metadata](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-metadata).

]]> September 30, 2024tag:google.com,2016:artifactregistry-release-notes#September_30_20242024-09-30T00:00:00-07:00v1 

### Feature

Artifact Analysis is gradually rolling out regionalized data storage and endpoints to help support compliance with data residency requirements. The Container Analysis API stores metadata in the same region or multi-region as the Artifact Registry repository where your image is scanned. 

For more information, see [Metadata storage locations](https://docs.cloud.google.com/artifact-analysis/docs/locations).

]]> August 30, 2024tag:google.com,2016:artifactregistry-release-notes#August_30_20242024-08-30T00:00:00-07:00v1 

### Feature

Artifact Registry records metrics and logs for your projects. To explore the available Artifact Registry metrics and logs, view your project in the [Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer) or the [Logs Explorer](https://console.cloud.google.com/logs/query).

For more information about metrics and logs, read [Observability in Google Cloud](https://docs.cloud.google.com/stackdriver/docs).

### Change

Updates to the Artifact Registry API are as follows:

  * Add or update file annotations with [`UpdateFile()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateFile).
  * Add or update package version annotations with [`UpdateVersion()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateVersion).
  * Filter by annotation or name with [`ListFiles()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListFiles), [`ListPackages()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListPackages), and [`ListVersions()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListVersions).
  * Filter by name with [`ListTags()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListTags), [`ListRepositories()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListRepositories) and [`ListDockerImages()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListDockerImages).
  * Order by `name`, `createTime`, or `updateTime` for [`ListFiles()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListFiles), [`ListVersions()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListVersions), [`ListRepositories()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListRepositories), and [`ListPackages()`](https://docs.cloud.google.com/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListPackages).

]]> August 21, 2024tag:google.com,2016:artifactregistry-release-notes#August_21_20242024-08-21T00:00:00-07:00v1 

### Change

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

]]> May 24, 2024tag:google.com,2016:artifactregistry-release-notes#May_24_20242024-05-24T00:00:00-07:00v1 

### Feature

[Cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy) for Artifact Registry are Generally Available (GA).

Cleanup policies help you manage artifacts by automatically deleting artifacts that you no longer need, while keeping artifacts that you want to store.

Deletions requested by Cleanup policies count against Artifact Registry delete request [quota and limits](https://docs.cloud.google.com/artifact-registry/quotas).

]]> May 10, 2024tag:google.com,2016:artifactregistry-release-notes#May_10_20242024-05-10T00:00:00-07:00v1 

### Feature

Artifact Registry generic repositories are available in Preview.

Generic repositories store versioned, immutable artifacts that don't have to adhere to any specific package format in Artifact Registry. You can store and manage arbitrary files such as archives, binaries, and media files with no package specifications or management clients.

To get started with generic repositories, see the [quickstart](https://docs.cloud.google.com/artifact-registry/docs/generic/store-generic).

]]>

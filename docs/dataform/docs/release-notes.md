---
url: https://docs.cloud.google.com/dataform/docs/release-notes/
title: Dataform release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:21:55.077764+00:00
---

# Dataform release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Resources ](https://docs.cloud.google.com/dataform/docs/quotas)



Send feedback 

#  Dataform release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Dataform. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/dataform-release-notes.xml) directly. 

## October 14, 2026

Feature

You can automatically preserve BigQuery data policies and data governance tags (Preview) applied to tables across Dataform executions by enabling the `preserveGovernanceControls` option in your table or workflow configuration. For more information, see [Preserve access controls metadata](https://docs.cloud.google.com/dataform/docs/create-tables#preserve-access-controls). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## October 13, 2026

Feature

You can use Developer Connect to [connect Dataform repositories to Secure Source Manager repositories](https://docs.cloud.google.com/dataform/docs/connect-repository#dev-connect). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 01, 2026

Feature

Dataform provides support for automated metadata enrichment and Knowledge Catalog data quality scorecard integration for Dataform workflows and BigQuery pipelines. For more information, see [Add metadata for Knowledge Catalog](https://docs.cloud.google.com/dataform/docs/create-tables#add-metadata). This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

## September 28, 2026

Feature

[Extended access options and user credentials authentication](https://docs.cloud.google.com/dataform/docs/schedule-runs) for running and scheduling Dataform workflows are now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## September 21, 2026

Feature

The Dataform remote Model Context Protocol (MCP) server now supports pipeline authoring in development workspaces and Git repository operations. AI agents can create and list workspaces, search and edit files, commit changes and push commits to remote Git providers, update repository settings, and organize repositories in folders. For more information, see [Use the Dataform remote MCP server](https://docs.cloud.google.com/dataform/docs/use-dataform-mcp) and the [Dataform MCP reference](https://docs.cloud.google.com/dataform/docs/reference/mcp). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## September 17, 2026

Feature

You can [use unit tests to test Dataform actions](https://docs.cloud.google.com/dataform/docs/test-data#unit-tests) against mock data with an expected result set. Dataform unit tests are [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## August 17, 2026

Feature

You can now use the [Dataform remote Model Context Protocol (MCP) server](https://docs.cloud.google.com/dataform/docs/use-dataform-mcp) to manage data transformation workflows through AI agents. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## August 13, 2026

Feature

Dataform workflows and BigQuery pipelines now support automated metadata enrichment for BigQuery tables and views, allowing you to define semantic metadata directly in SQLX configurations for synchronization with the Knowledge Catalog. For more information, see [Add metadata for Knowledge Catalog](https://docs.cloud.google.com/dataform/docs/create-tables#add-metadata). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## July 27, 2026

Feature

[Dataform deployments](https://docs.cloud.google.com/dataform/docs/deployments) provide a centralized experience for creating and managing pipeline deployments connected to remote Git repositories. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## July 13, 2026

Security

A Missing Authorization vulnerability was discovered in repositories in BigQuery, Dataform, and Colab Enterprise. An authenticated attacker could potentially escalate permissions and perform cross-tenant repository takeover. For more information, see the [GCP-2026-047](https://docs.cloud.google.com/dataform/docs/security-bulletins#gcp-2026-047) Dataform security bulletin.

## June 29, 2026

Feature

You can grant workflows [access to Bigtable, Google Drive, and Knowledge Catalog](https://docs.cloud.google.com/dataform/docs/schedule-runs) when running or scheduling them with your Google Account user credentials. Extended access options are available in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 29, 2026

Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for the `Folder` and `TeamFolder` resources. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/dataform/docs/create-custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

Breaking

[Strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode) is enforced globally for all Dataform repositories, requiring the use of a custom service account or user credentials for running Dataform workflows, BigQuery pipelines, notebooks, and data preparations.

## April 24, 2026

Announcement

Cloud Composer is now called Managed Service for Apache Airflow. The names for associated APIs, client libraries, CLI commands, and Identity and Access Management (IAM) resources remain unchanged. For more information, see [Managed Airflow overview](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview).

Announcement

Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and Identity and Access Management (IAM) resources remain unchanged. For more information, see [Knowledge Catalog overview](https://docs.cloud.google.com/dataplex/docs/introduction).

Announcement

Vertex AI is now called Gemini Enterprise Agent Platform. The names for associated APIs, client libraries, CLI commands, and Identity and Access Management (IAM) resources remain unchanged. For more information, see [Agent Platform overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview).

## April 16, 2026

Feature

You can [connect Dataform repositories to third-party Git repositories using Developer Connect](https://docs.cloud.google.com/dataform/docs/connect-repository#dev-connect), removing the need for manual secrets management and enabling support for repositories in privately hosted networks. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## April 02, 2026

Feature

The [Dataform folders and repositories](https://docs.cloud.google.com/dataform/docs/organize-code-assets) feature is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). This feature lets you organize code assets like notebooks and saved queries into a hierarchical structure with IAM policy inheritance. This release also introduces `deleteTree` API methods for deleting folders and team folders.

## January 28, 2026

Feature

You can [organize your code assets into a hierarchical structure](https://docs.cloud.google.com/dataform/docs/organize-code-assets) with folders and repositories using the Dataform API. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

## January 19, 2026

Breaking

[Dataform workflows](https://docs.cloud.google.com/dataform/docs/sql-workflows), [BigQuery notebooks](https://docs.cloud.google.com/bigquery/docs/orchestrate-notebooks), [pipelines](https://docs.cloud.google.com/bigquery/docs/schedule-pipelines), and [data preparations](https://docs.cloud.google.com/bigquery/docs/orchestrate-data-preparations) are enforcing strict act-as mode at the project level. To avoid failures and maintain automatic releases, you must use custom service accounts instead of the default Dataform service agent across all repositories. You must also grant the Service Account User role (`roles/iam.serviceAccountUser`) to the default Dataform service agent and relevant principals. For more information and to verify act-as permissions, see [Use strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode).

## December 16, 2025

Feature

[Strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode) for Dataform is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). This feature enhances security by requiring users to have the `iam.serviceAccounts.actAs` permission on the service account used to run workflows, ensuring a more secure and predictable permissions model for your Dataform projects.

## December 15, 2025

Feature

You can verify and resolve `iam.serviceAccounts.actAs` permission issues in Dataform by checking Cloud Logging, interpreting log entries, and granting the necessary IAM roles. For more information, see [Verify act-as permissions for the effective service account](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode#verify-permissions). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

## December 09, 2025

Feature

Dataform offers [enhanced IAM permissions](https://docs.cloud.google.com/dataform/docs/access-control#use-config-api), providing more granular control over resource creation and scheduling. Administrators can also [enable private workspaces](https://docs.cloud.google.com/dataform/docs/access-control#enable-private-workspaces) to restrict access to the workspace creator. These features are in [preview](https://cloud.google.com/products#product-launch-stages).

## November 18, 2025

Feature

Dataform now lets you automate the creation of [BigLake tables for Apache Iceberg in BigQuery](https://docs.cloud.google.com/dataform/docs/create-tables#create-iceberg-table). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## November 13, 2025

Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for the `CompilationResult`, `ReleaseConfig`, `WorkflowConfig`, `WorkflowInvocation`, and `Workspace` resources. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/dataform/docs/create-custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## October 06, 2025

Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some Dataform resources. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/dataform/docs/create-custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

Feature

You can set the priority of BigQuery jobs in Dataform to run queries as interactive jobs that start running as quickly as possible or as batch jobs with lower priority. For more information, see [Create a workflow configuration](https://docs.cloud.google.com/dataform/docs/schedule-runs#create-workflow-configuration) and [InvocationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/InvocationConfig). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## September 08, 2025

Feature

You can now [update an incremental table schema without a full table refresh](https://docs.cloud.google.com/dataform/docs/create-tables#change-schema-without-refresh). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## September 02, 2025

Feature

Dataform now automatically selects a processing location based on the datasets referenced in your SQL queries. This makes setting the default location optional in your workflow configurations. For more information, see [About repository settings](https://docs.cloud.google.com/dataform/docs/manage-repository#repository-settings). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## August 21, 2025

Security

A security vulnerability was discovered in the Dataform API. This vulnerability could potentially allow unauthorized access to customer code repositories and data. For more information, see [GCP-2025-045 security bulletin](https://docs.cloud.google.com/dataform/docs/security-bulletins#gcp-2025-045).

## July 14, 2025

Feature

Updates to the automatic cataloging of Dataform metadata in Dataplex improve the near real-time [management](https://docs.cloud.google.com/dataplex/docs/catalog-overview) and [search](https://docs.cloud.google.com/dataplex/docs/search-assets) capabilities for repository metadata. These features are [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## June 12, 2025

Announcement

Dark theme is now available for BigQuery and Dataform. To turn on the dark theme, go to the Console, open the **Settings and utilities** menu next to your avatar, and select **Preferences**. On the **User preferences** page, select **Appearance** in the navigation, select your color theme, and save your selection.

## May 29, 2025

Feature

You can now use your Google Account user credentials to authorize the creation, scheduling, and running of pipelines, the scheduling of notebooks and data preparations, and the creation of workflow configurations. For more information, see [Schedule runs](https://docs.cloud.google.com/dataform/docs/schedule-runs). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

## May 28, 2025

Feature

You can now use strict act-as mode to enable an additional security check for certain user actions in Dataform. For more information, see [Use strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

## December 19, 2024

Feature

You can now [search for](https://docs.cloud.google.com/dataplex/docs/search-assets) and view the metadata of Dataform repositories in the Dataplex console. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

Feature

You can now manage Dataform repositories in Dataplex. Metadata of Dataform repositories is automatically available in Dataplex, without additional configuration. For more information, see [Manage Dataform assets with Dataplex](https://cloud.google.com/dataform/docs/use-dataplex). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## October 10, 2024

Announcement

Dataform is available in the following regions:

  * asia-northeast2
  * asia-south2
  * australia-southeast2
  * europe-central2
  * europe-north1
  * europe-west8
  * europe-west9
  * europe-west10
  * me-west1
  * northamerica-northeast2
  * southamerica-west1
  * us-west3



For more information, see [Locations](https://docs.cloud.google.com/dataform/docs/locations).

## September 30, 2024

Change

The maximum size limit for workspaces encrypted with customer-managed encryption keys (CMEK) is 512 MB. For more information about Dataform quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/dataform/docs/quotas). For more information about encrypting Dataform repositories with CMEK, see [Use customer-managed encryption keys](https://docs.cloud.google.com/dataform/docs/cmek).

## September 09, 2024

Feature

You can now set a default Dataform customer-managed encryption keys (CMEK) key for your project to encrypt multiple Dataform repositories with the same CMEK key. For more information, see [Use Dataform default CMEK keys](https://docs.cloud.google.com/dataform/docs/cmek#default-keys).

## August 12, 2024

Feature

Customer-Managed Encryption Keys (CMEK) in Dataform are [generally available](https://cloud.google.com/products#product-launch-stages) (GA). For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/dataform/docs/cmek).

Feature

You can now use Cloud External Key Manager (Cloud EKM) keys to protect Dataform data. Cloud EKM keys in Dataform are [generally available](https://cloud.google.com/products#product-launch-stages) (GA). For more information, see [Using and managing external keys](https://docs.cloud.google.com/dataform/docs/cmek#ekm).

## August 05, 2024

Feature

[Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview) supports Dataform in the [GA stage](https://cloud.google.com/products#product-launch-stages).

## July 31, 2024

Change

The maximum size limit for repositories encrypted with customer-managed encryption keys (CMEK) is 512 MB. For more information about Dataform quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/dataform/docs/quotas). For more information about encrypting Dataform repositories with CMEK, see [Use customer-managed encryption keys](https://docs.cloud.google.com/dataform/docs/cmek).

## July 18, 2024

Announcement

As of Dataform Core [`3.0.0.`](https://github.com/dataform-co/dataform/releases/tag/3.0.0), Dataform doesn't distribute a Docker image. You can build your own Docker image of Dataform, which you can use to run the equivalent of Dataform CLI commands. To build your own Docker image, see [Containerize an application](https://docs.docker.com/guides/workshop/02_our_app/) in the Docker documentation.

## June 21, 2024

Announcement

The 3.0.0 version of the open-source Dataform framework is available.

The `workflow_settings.yaml` file, which was introduced in Dataform Core 3.0.0-beta.0, replaces `dataform.json`.

You can specify the Dataform Core version directly in the `workflow_settings.yaml` file, which removes the need for `package.json` for most repositories. To have package dependencies other than `@dataform/core`, the `package.json` file is still required.

No immediate action to convert existing Dataform code is required. You can continue to use `dataform.json` and `package.json` in existing repositories.

You can convert your `dataform.json` file into `workflow_settings.yaml` by following the instructions in the [3.0.0 GitHub release](https://github.com/dataform-co/dataform/releases/tag/3.0.0).

New repositories use `workflow_settings.yaml` by default. You can replace the `workflow_settings.yaml` file with `dataform.json` to continue using the JSON format. If you remove `workflow_settings.yaml`, you need to add a `package.json` file to your repository to install `@dataform/core`.

For more information, see the [3.0.0 release on GitHub](https://github.com/dataform-co/dataform/releases/tag/3.0.0).

## June 17, 2024

Feature

You can now inspect past manual compilation results of a selected release configuration. For more information, see [View details of a release configuration](https://docs.cloud.google.com/dataform/docs/release-configurations#release-configuration-details).

## May 29, 2024

Feature

Dataform Core `includeDependentAssertions` and `dependOnDependencyAssertions` parameters for adding assertions as dependencies are available.

You can set the `includeDependentAssertions` parameter in a selected action to automatically add assertions of a selected dependency action as dependencies of the edited action. 

You can set `dependOnDependencyAssertions` the parameter in a selected action to automatically add assertions of all dependency actions as dependencies of the edited action. 

For more information, see [Set assertions as dependencies](https://docs.cloud.google.com/dataform/docs/assertions#add_assertions_as_dependencies).

## May 10, 2024

Feature

Gemini, an AI-powered collaborator in Google Cloud, can help you generate code in Dataform. This feature is in [preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Write queries with Gemini assistance](https://docs.cloud.google.com/dataform/docs/develop-with-ai).

## April 02, 2024

Feature

You can now use Customer-Managed Encryption Keys (CMEK) to protect repositories in Dataform. CMEK in Dataform is available in [preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/dataform/docs/cmek).

## March 13, 2024

Announcement

The 3.0.0-beta.0 version of the open-source Dataform framework is available. This update introduces significant changes, including, but not limited to, the following:

  * Deprecation of `dataform.json` in favor of `workflow_settings.yaml`
  * Stateless package installation by `@dataform/cli`
  * Warehouse-agnostic compilation output



You don't need to take immediate action to update your Dataform code.

For more information, see the [3.0.0-beta.0 release on GitHub](https://github.com/dataform-co/dataform/releases/tag/3.0.0-beta.0).

## March 12, 2024

Feature

Granting repository access to all authenticated users is available. For more information, see [Grant public access to a repository](https://docs.cloud.google.com/dataform/docs/access-control#grant_public_access_to_a_repository).

## March 11, 2024

Announcement

Dataform is available in the africa-south1 region. For more information, see [Locations](https://docs.cloud.google.com/dataform/docs/locations).

## February 26, 2024

Announcement

Dataform is available in the us-south1 region. For more information, see [Locations](https://docs.cloud.google.com/dataform/docs/locations).

## February 21, 2024

Feature

[Support for VPC Service Controls](https://docs.cloud.google.com/dataform/docs/vpc-service-controls) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## February 15, 2024

Announcement

Dataform is available in the following regions:

  * asia-east2
  * asia-northeast3
  * asia-southeast2
  * europe-southwest1
  * europe-west12
  * me-central1
  * me-central2
  * northamerica-northeast
  * us-east4
  * us-east5
  * us-west2
  * us-west4



For more information, see [Locations](https://docs.cloud.google.com/dataform/docs/locations).

## January 29, 2024

Feature

[Support for VPC Service Controls](https://docs.cloud.google.com/dataform/docs/vpc-service-controls) is available in [preview](https://cloud.google.com/products#product-launch-stages).

## January 17, 2024

Change

The **Releases & Scheduling** tab replaces the **Release configurations** and **Workflow configurations** tabs in repositories. Configuration and monitoring of release configurations and workflow configurations is available in the **Releases & Scheduling** tab.

For more information, see [Create a release configuration](https://docs.cloud.google.com/dataform/docs/release-configurations), and [Schedule executions with workflow configurations](https://docs.cloud.google.com/dataform/docs/workflow-configurations).

## December 11, 2023

Feature

[Display of files as workspace tabs](https://docs.cloud.google.com/dataform/docs/workspaces) is available.

## December 07, 2023

Announcement

The 2.8.0 version of the open-source Dataform framework is available. This update introduces performance improvements. For more information, see the [2.8.0: Packaging and compilation performance improvements](https://github.com/dataform-co/dataform/releases/tag/2.8.0) release on GitHub.

## December 05, 2023

Feature

[Terraform IAM policy for the Dataform repository resource](https://docs.cloud.google.com/dataform/docs/terraform#iam-terraform) is available.

## December 04, 2023

Feature

[Preview of uncommitted changes during a commit](https://docs.cloud.google.com/dataform/docs/version-control) is available.

## November 16, 2023

Announcement

Dataform is compliant with VPAT.

For more information, see [Dataform compliance](https://docs.cloud.google.com/dataform/docs/compliance).

## October 27, 2023

Feature

[Batch workspace deletion](https://docs.cloud.google.com/dataform/docs/create-workspace#delete-workspace) is available.

## October 26, 2023

Feature

[File search](https://docs.cloud.google.com/dataform/docs/workspaces#code-tab) is available in workspaces.

## October 23, 2023

Announcement

The 2.7.0 version of the [open-source Dataform framework](https://github.com/dataform-co/dataform) is available. This update introduces explicitly listed column names in incremental insert statements. For more information, see the [2.7.0: Updates for Dataform GCP incremental SQL](https://github.com/dataform-co/dataform/releases/tag/2.7.0) release on GitHub.

## October 20, 2023

Feature

[Workforce identity federation](https://docs.cloud.google.com/dataform/docs/access-control#workforce-identity-federation) is available.

## October 17, 2023

Feature

`ssh_authentication_config` and `service_account` fields are available in the [`google_dataform_repository`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/dataform_repository) Dataform Terraform resource.

## October 13, 2023

Feature

[Formatting](https://docs.cloud.google.com/dataform/docs/create-workspace) of Dataform core and JavaScript code is available.

## September 07, 2023

Feature

Service account delegation for workflow execution is now available. You can configure service account delegation for whole [repositories](https://docs.cloud.google.com/dataform/docs/create-repository), or for individual [workflow configurations](https://docs.cloud.google.com/dataform/docs/workflow-configurations).

## September 06, 2023

Feature

[Organizational policy for restricting remote repositories](https://docs.cloud.google.com/dataform/docs/restrict-git-remotes) is available.

## August 31, 2023

Announcement

[Legacy Dataform](https://dataform.co/) will be deprecated on February 26, 2024, after which you will not be able to access legacy projects.

We recommend migration to Dataform in Google Cloud Platform. 

To learn more about Dataform in Google Cloud Platform, see [Overview of Dataform](https://docs.cloud.google.com/dataform/docs/overview).

To discover how to migrate legacy projects, see [Migrate from legacy Dataform](https://docs.cloud.google.com/dataform/docs/migration).

## August 22, 2023

Announcement

Dataform is compliant with SOC 2 and SOC 3.

For more information, see [Dataform compliance](https://docs.cloud.google.com/dataform/docs/compliance).

## August 18, 2023

Feature

[SSH authentication](https://docs.cloud.google.com/dataform/docs/connect-repository#authenticate_a_remote_repository_through_ssh) for GitHub, GitLab, and Bitbucket Cloud repositories is supported.

Feature

[Connecting Dataform repositories to Bitbucket Cloud repositories](https://docs.cloud.google.com/dataform/docs/connect-repository) is supported.

## August 09, 2023

Announcement

Dataform is compliant with HIPAA, ISO/IEC 27001, and SOC 1.

For more information, see [Dataform compliance](https://docs.cloud.google.com/dataform/docs/compliance).

## August 02, 2023

Feature

[Filtering and sorting repositories](https://docs.cloud.google.com/dataform/docs/repositories) are available.

## August 01, 2023

Feature

The following [Dataform API](https://docs.cloud.google.com/dataform/reference/rest) methods for version control are available:

  * `CommitRepositoryChanges()`
  * `ReadRepositoryFile()`
  * `QueryRepositoryDirectoryContents()`
  * `FetchRepositoryHistory()`



The following fields of `Repository` are available:

  * `labels`
  * `set_authenticated_user_admin`



## July 27, 2023

Feature

[Selection of files for a commit](https://docs.cloud.google.com/dataform/docs/version-control) is available.

## June 19, 2023

Feature

[Filtering the compiled graph](https://docs.cloud.google.com/dataform/docs/workspaces) in a workspace is available.

## May 04, 2023

Announcement

[Dataform](https://docs.cloud.google.com/dataform) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Feature

Dataform [release configurations](https://docs.cloud.google.com/dataform/docs/release-configurations) are available. Release configurations let you configure execution environments, for example, staging and production.

Feature

Dataform [workflow configurations](https://docs.cloud.google.com/dataform/docs/workflow-configurations) are available. Workflow configurations let you execute SQL workflows on a schedule.

## April 18, 2023

Feature

[Cloud Logging](https://docs.cloud.google.com/dataform/docs/cloud-logging) is available for Dataform in Preview.

## March 24, 2023

Feature

[Workspace compilation overrides](https://docs.cloud.google.com/dataform/docs/workspace-compilation-overrides) are available in Preview.

## March 21, 2023

Announcement

Dataform in Preview is available in the following regions:

  * australia-southeast1
  * southamerica-east1



## March 10, 2023

Announcement

Dataform in Preview is available in the following regions:

  * asia-south1
  * europe-west6



## March 09, 2023

Feature

[Query preview](https://docs.cloud.google.com/dataform/docs/preview-queries) in a workspace is available in Preview.

## March 06, 2023

Announcement

Dataform in Preview is available in the following regions:

  * asia-northeast1
  * europe-west2
  * europe-west3
  * us-east1



## February 14, 2023

Announcement

Dataform in Preview is available in the following regions: 

  * asia-southeast1
  * europe-west1
  * us-west1



## January 27, 2023

Announcement

Dataform in Preview is available in the asia-east1 region.

## January 25, 2023

Feature

Workspace navigation tabs are available in Preview.

## January 09, 2023

Feature

[Display of a SQL workflow as a compiled graph in a workspace](https://docs.cloud.google.com/dataform/docs/workspaces) is available in Preview.

## November 25, 2022

Feature

[Real-time validation of compiled queries against BigQuery](https://docs.cloud.google.com/dataform/docs/workspaces) is available in Preview.

Fixed

Definition of BigQuery variables in the `pre_operations` block of `type: incremental` queries that contain a `uniqueKey` is available in Preview.

## October 21, 2022

Feature

[Configuration of policy tags in the `config` block](https://docs.cloud.google.com/dataform/docs/policy-tags) is available in Preview.

## August 25, 2022

Announcement

Dataform is available in Preview.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

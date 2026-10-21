---
url: https://docs.cloud.google.com/feeds/dataform-release-notes.xml
title: Dataform - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:59.794550+00:00
---

# Dataform - Release notes

> Source: https://docs.cloud.google.com/feeds/dataform-release-notes.xml

tag:google.com,2016:dataform-release-notesDataform - Release notesGoogle Cloud Platform2026-10-13T00:00:00-07:00October 13, 2026tag:google.com,2016:dataform-release-notes#October_13_20262026-10-13T00:00:00-07:00Feature 

You can use Developer Connect to [connect Dataform repositories to Secure Source Manager repositories](https://docs.cloud.google.com/dataform/docs/connect-repository#dev-connect). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> October 01, 2026tag:google.com,2016:dataform-release-notes#October_01_20262026-10-01T00:00:00-07:00Feature 

Dataform provides support for automated metadata enrichment and Knowledge Catalog data quality scorecard integration for Dataform workflows and BigQuery pipelines. For more information, see [Add metadata for Knowledge Catalog](https://docs.cloud.google.com/dataform/docs/create-tables#add-metadata). This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

]]> September 28, 2026tag:google.com,2016:dataform-release-notes#September_28_20262026-09-28T00:00:00-07:00Feature 

[Extended access options and user credentials authentication](https://docs.cloud.google.com/dataform/docs/schedule-runs) for running and scheduling Dataform workflows are now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

]]> September 21, 2026tag:google.com,2016:dataform-release-notes#September_21_20262026-09-21T00:00:00-07:00Feature 

The Dataform remote Model Context Protocol (MCP) server now supports pipeline authoring in development workspaces and Git repository operations. AI agents can create and list workspaces, search and edit files, commit changes and push commits to remote Git providers, update repository settings, and organize repositories in folders. For more information, see [Use the Dataform remote MCP server](https://docs.cloud.google.com/dataform/docs/use-dataform-mcp) and the [Dataform MCP reference](https://docs.cloud.google.com/dataform/docs/reference/mcp). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

]]> September 17, 2026tag:google.com,2016:dataform-release-notes#September_17_20262026-09-17T00:00:00-07:00Feature 

You can [use unit tests to test Dataform actions](https://docs.cloud.google.com/dataform/docs/test-data#unit-tests) against mock data with an expected result set. Dataform unit tests are [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

]]> August 17, 2026tag:google.com,2016:dataform-release-notes#August_17_20262026-08-17T00:00:00-07:00Feature 

You can now use the [Dataform remote Model Context Protocol (MCP) server](https://docs.cloud.google.com/dataform/docs/use-dataform-mcp) to manage data transformation workflows through AI agents. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

]]> August 13, 2026tag:google.com,2016:dataform-release-notes#August_13_20262026-08-13T00:00:00-07:00Feature 

Dataform workflows and BigQuery pipelines now support automated metadata enrichment for BigQuery tables and views, allowing you to define semantic metadata directly in SQLX configurations for synchronization with the Knowledge Catalog. For more information, see [Add metadata for Knowledge Catalog](https://docs.cloud.google.com/dataform/docs/create-tables#add-metadata). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> July 27, 2026tag:google.com,2016:dataform-release-notes#July_27_20262026-07-27T00:00:00-07:00Feature 

[Dataform deployments](https://docs.cloud.google.com/dataform/docs/deployments) provide a centralized experience for creating and managing pipeline deployments connected to remote Git repositories. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> July 13, 2026tag:google.com,2016:dataform-release-notes#July_13_20262026-07-13T00:00:00-07:00Security 

A Missing Authorization vulnerability was discovered in repositories in BigQuery, Dataform, and Colab Enterprise. An authenticated attacker could potentially escalate permissions and perform cross-tenant repository takeover. For more information, see the [GCP-2026-047](https://docs.cloud.google.com/dataform/docs/security-bulletins#gcp-2026-047) Dataform security bulletin.

]]> June 29, 2026tag:google.com,2016:dataform-release-notes#June_29_20262026-06-29T00:00:00-07:00Feature 

You can grant workflows [access to Bigtable, Google Drive, and Knowledge Catalog](https://docs.cloud.google.com/dataform/docs/schedule-runs) when running or scheduling them with your Google Account user credentials. Extended access options are available in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> April 29, 2026tag:google.com,2016:dataform-release-notes#April_29_20262026-04-29T00:00:00-07:00Feature 

You can use custom constraints with Organization Policy to provide more granular control over specific fields for the `Folder` and `TeamFolder` resources. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/dataform/docs/create-custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Breaking

[Strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode) is enforced globally for all Dataform repositories, requiring the use of a custom service account or user credentials for running Dataform workflows, BigQuery pipelines, notebooks, and data preparations.

]]> April 24, 2026tag:google.com,2016:dataform-release-notes#April_24_20262026-04-24T00:00:00-07:00Announcement 

Cloud Composer is now called Managed Service for Apache Airflow. The names for associated APIs, client libraries, CLI commands, and Identity and Access Management (IAM) resources remain unchanged. For more information, see [Managed Airflow overview](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview).

### Announcement

Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and Identity and Access Management (IAM) resources remain unchanged. For more information, see [Knowledge Catalog overview](https://docs.cloud.google.com/dataplex/docs/introduction).

### Announcement

Vertex AI is now called Gemini Enterprise Agent Platform. The names for associated APIs, client libraries, CLI commands, and Identity and Access Management (IAM) resources remain unchanged. For more information, see [Agent Platform overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview).

]]> April 16, 2026tag:google.com,2016:dataform-release-notes#April_16_20262026-04-16T00:00:00-07:00Feature 

You can [connect Dataform repositories to third-party Git repositories using Developer Connect](https://docs.cloud.google.com/dataform/docs/connect-repository#dev-connect), removing the need for manual secrets management and enabling support for repositories in privately hosted networks. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

]]> April 02, 2026tag:google.com,2016:dataform-release-notes#April_02_20262026-04-02T00:00:00-07:00Feature 

The [Dataform folders and repositories](https://docs.cloud.google.com/dataform/docs/organize-code-assets) feature is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). This feature lets you organize code assets like notebooks and saved queries into a hierarchical structure with IAM policy inheritance. This release also introduces `deleteTree` API methods for deleting folders and team folders.

]]> January 28, 2026tag:google.com,2016:dataform-release-notes#January_28_20262026-01-28T00:00:00-08:00Feature 

You can [organize your code assets into a hierarchical structure](https://docs.cloud.google.com/dataform/docs/organize-code-assets) with folders and repositories using the Dataform API. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

]]> January 19, 2026tag:google.com,2016:dataform-release-notes#January_19_20262026-01-19T00:00:00-08:00Breaking 

[Dataform workflows](https://docs.cloud.google.com/dataform/docs/sql-workflows), [BigQuery notebooks](https://docs.cloud.google.com/bigquery/docs/orchestrate-notebooks), [pipelines](https://docs.cloud.google.com/bigquery/docs/schedule-pipelines), and [data preparations](https://docs.cloud.google.com/bigquery/docs/orchestrate-data-preparations) are enforcing strict act-as mode at the project level. To avoid failures and maintain automatic releases, you must use custom service accounts instead of the default Dataform service agent across all repositories. You must also grant the Service Account User role (`roles/iam.serviceAccountUser`) to the default Dataform service agent and relevant principals. For more information and to verify act-as permissions, see [Use strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode).

]]> December 16, 2025tag:google.com,2016:dataform-release-notes#December_16_20252025-12-16T00:00:00-08:00Feature 

[Strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode) for Dataform is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). This feature enhances security by requiring users to have the `iam.serviceAccounts.actAs` permission on the service account used to run workflows, ensuring a more secure and predictable permissions model for your Dataform projects.

]]> December 15, 2025tag:google.com,2016:dataform-release-notes#December_15_20252025-12-15T00:00:00-08:00Feature 

You can verify and resolve `iam.serviceAccounts.actAs` permission issues in Dataform by checking Cloud Logging, interpreting log entries, and granting the necessary IAM roles. For more information, see [Verify act-as permissions for the effective service account](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode#verify-permissions). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

]]> December 09, 2025tag:google.com,2016:dataform-release-notes#December_09_20252025-12-09T00:00:00-08:00Feature 

Dataform offers [enhanced IAM permissions](https://docs.cloud.google.com/dataform/docs/access-control#use-config-api), providing more granular control over resource creation and scheduling. Administrators can also [enable private workspaces](https://docs.cloud.google.com/dataform/docs/access-control#enable-private-workspaces) to restrict access to the workspace creator. These features are in [preview](https://cloud.google.com/products#product-launch-stages).

]]> November 18, 2025tag:google.com,2016:dataform-release-notes#November_18_20252025-11-18T00:00:00-08:00Feature 

Dataform now lets you automate the creation of [BigLake tables for Apache Iceberg in BigQuery](https://docs.cloud.google.com/dataform/docs/create-tables#create-iceberg-table). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

]]> November 13, 2025tag:google.com,2016:dataform-release-notes#November_13_20252025-11-13T00:00:00-08:00Feature 

You can use custom constraints with Organization Policy to provide more granular control over specific fields for the `CompilationResult`, `ReleaseConfig`, `WorkflowConfig`, `WorkflowInvocation`, and `Workspace` resources. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/dataform/docs/create-custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

]]> October 06, 2025tag:google.com,2016:dataform-release-notes#October_06_20252025-10-06T00:00:00-07:00Feature 

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some Dataform resources. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/dataform/docs/create-custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

You can set the priority of BigQuery jobs in Dataform to run queries as interactive jobs that start running as quickly as possible or as batch jobs with lower priority. For more information, see [Create a workflow configuration](https://docs.cloud.google.com/dataform/docs/schedule-runs#create-workflow-configuration) and [InvocationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/InvocationConfig). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

]]> September 08, 2025tag:google.com,2016:dataform-release-notes#September_08_20252025-09-08T00:00:00-07:00Feature 

You can now [update an incremental table schema without a full table refresh](https://docs.cloud.google.com/dataform/docs/create-tables#change-schema-without-refresh). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> September 02, 2025tag:google.com,2016:dataform-release-notes#September_02_20252025-09-02T00:00:00-07:00Feature 

Dataform now automatically selects a processing location based on the datasets referenced in your SQL queries. This makes setting the default location optional in your workflow configurations. For more information, see [About repository settings](https://docs.cloud.google.com/dataform/docs/manage-repository#repository-settings). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

]]> August 21, 2025tag:google.com,2016:dataform-release-notes#August_21_20252025-08-21T00:00:00-07:00Security 

A security vulnerability was discovered in the Dataform API. This vulnerability could potentially allow unauthorized access to customer code repositories and data. For more information, see [GCP-2025-045 security bulletin](https://docs.cloud.google.com/dataform/docs/security-bulletins#gcp-2025-045).

]]> July 14, 2025tag:google.com,2016:dataform-release-notes#July_14_20252025-07-14T00:00:00-07:00Feature 

Updates to the automatic cataloging of Dataform metadata in Dataplex improve the near real-time [management](https://docs.cloud.google.com/dataplex/docs/catalog-overview) and [search](https://docs.cloud.google.com/dataplex/docs/search-assets) capabilities for repository metadata. These features are [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

]]> June 12, 2025tag:google.com,2016:dataform-release-notes#June_12_20252025-06-12T00:00:00-07:00Announcement 

Dark theme is now available for BigQuery and Dataform. To turn on the dark theme, go to the Console, open the **Settings and utilities** menu next to your avatar, and select **Preferences**. On the **User preferences** page, select **Appearance** in the navigation, select your color theme, and save your selection.

]]> May 29, 2025tag:google.com,2016:dataform-release-notes#May_29_20252025-05-29T00:00:00-07:00Feature 

You can now use your Google Account user credentials to authorize the creation, scheduling, and running of pipelines, the scheduling of notebooks and data preparations, and the creation of workflow configurations. For more information, see [Schedule runs](https://docs.cloud.google.com/dataform/docs/schedule-runs). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

]]> May 28, 2025tag:google.com,2016:dataform-release-notes#May_28_20252025-05-28T00:00:00-07:00Feature 

You can now use strict act-as mode to enable an additional security check for certain user actions in Dataform. For more information, see [Use strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

]]> December 19, 2024tag:google.com,2016:dataform-release-notes#December_19_20242024-12-19T00:00:00-08:00Feature 

You can now [search for](https://docs.cloud.google.com/dataplex/docs/search-assets) and view the metadata of Dataform repositories in the Dataplex console. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

### Feature

You can now manage Dataform repositories in Dataplex. Metadata of Dataform repositories is automatically available in Dataplex, without additional configuration. For more information, see [Manage Dataform assets with Dataplex](https://cloud.google.com/dataform/docs/use-dataplex). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

]]>

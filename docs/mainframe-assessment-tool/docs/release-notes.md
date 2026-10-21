---
url: https://docs.cloud.google.com/mainframe-assessment-tool/docs/release-notes/
title: Mainframe Assessment Tool release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:00:58.625491+00:00
---

# Mainframe Assessment Tool release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-assessment-tool/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Assessment Tool ](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [ Resources ](https://docs.cloud.google.com/mainframe-assessment-tool/docs/release-notes)



Send feedback 

#  Mainframe Assessment Tool release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to Mainframe Assessment Tool. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/mainframeassessmenttool-release-notes.xml) directly. 

## August 18, 2026

Feature

Mainframe Assessment Tool version 3.5.0 is available with the following new features and improvements:

  * Introduced system health diagnostics to help you diagnose configuration issues before running assessments. You can now use the **System Health** section in **Settings** to validate required IAM permissions and test Gemini model connectivity before running assessments.

For more information, see [Configure settings](https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-settings).

  * Updated the **Google Cloud project** field in **Settings > General settings** to be read-only, displaying the Google Cloud project ID used by Mainframe Assessment Tool. You can no longer modify the project ID directly from the UI. To use a different project for your assessment, configure a project override on your VM instance or cluster deployment. If you configured a project ID in Mainframe Assessment Tool version 3.4.0 or earlier, that saved setting is used by default instead of the project where your instance is deployed.

For more information, see [Override the Google Cloud project](https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-settings#override-gcp-project).

  * Expanded Business Rules Extraction to support large mainframe applications with up to 5 million lines of code (LoC).

  * Enhanced HTML documentation exports to include detailed dataset logic alongside Markdown tables.

  * Enhanced JCL utility detection to support additional utilities and parameter propagation from JCL `PARM` statements to COBOL programs.




## July 22, 2026

Feature

Mainframe Assessment Tool version 3.4.0 is available with the following new features and improvements:

  * Business Rules Extraction is now generally available ([GA](https://docs.cloud.google.com/products#product-launch-stages)) with the following features and improvements:

    * Introduced business rules specifications. Mainframe Assessment Tool now generates a business specification for extracted business rules, which is available on the **Specification** tab.

For more information, see [Review the business rules](https://docs.cloud.google.com/mainframe-assessment-tool/docs/business-rules-extraction#review-rules).

    * Added code references to business rules extraction. Each extracted rule now links to the exact source code from which it was derived. Code references are grouped by asset and included in exports, letting you trace and verify every rule against the original source.

For more information, see [Extract business rules](https://docs.cloud.google.com/mainframe-assessment-tool/docs/business-rules-extraction).

    * Enhanced Business Rule exports to include the generated process-flow graph alongside the extracted rules.

    * Improved the reliability of Business Rules Extraction on large applications, including more robust handling of very large rule sets.

  * Enhanced AI-generated summaries to link directly to referenced mainframe assets, including COBOL programs, JCL jobs, datasets, and DB2 tables.

  * Added filtering to the **CICS File Definitions** table in the **Datasets** report.

  * Improved detection of JCL utility programs with extended coverage for utilities such as DFSORT and IDCAMS.




Change

Mainframe Assessment Tool no longer generates code suggestions (program translation). Code modernization tasks, including program translation, should now be performed using the Antigravity workflow. Previously generated code remains available within the tool to view and export.

For more information about code modernization, see [Modernize and validate](https://docs.cloud.google.com/mainframe-assessment-tool/docs/modernize-validate).

Fixed

Mainframe Assessment Tool version 3.4.0 fixes the following issues:

  * Fixed security vulnerabilities to help ensure a more secure assessment environment.



## June 25, 2026

Feature

Mainframe Assessment Tool version 3.3.0 is available with the following new features and improvements:

  * Added the Business Rules Extraction (BRE) visualization on the **Business Flow** tab to support hierarchical exploration.

For more information, see [Extract business rules](https://docs.cloud.google.com/mainframe-assessment-tool/docs/business-rules-extraction).

  * Added parsing and analysis support for the Natural programming language on z/OS. This enhancement lets you parse Natural programming language assets, resolve dependencies for Data Definition Modules (DDMs), Adabas databases, and screen maps (MAPS) to automatically generate detailed technical specifications.

For more information, see [Supported languages](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview#supported-languages) and [Database schemas](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview#database_schemas).

  * Added basic support for the REXX programming language ([Preview](https://docs.cloud.google.com/products#product-launch-stages)), enabling you to analyze, summarize, and visualize REXX assets within Mainframe Assessment Tool.

For more information, see [Supported languages](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview#supported-languages).

  * Introduced per-assessment settings for advanced Gemini configuration and data residency, letting you control model execution and data locality.

You can choose a quality level (Fast, Balanced, or Deep) for a model, pin a specific model, and restrict AI requests to a selected region. To prevent silent model substitution, any quality level is marked as unavailable if its models are not served in your selected region.

You can no longer select Gemini 2.5 Flash Lite, Gemini 2.5 Flash, Gemini 2.5 Pro, and Gemini 3 Flash Preview, as they are deprecated.

For more information, see [Create and update assessments](https://docs.cloud.google.com/mainframe-assessment-tool/docs/perform-assessment).

  * Enhanced the Ask Gemini feature to use the Gemini 3.5 Flash model, which optimizes performance and shortens response times.

  * Enhanced parsing for COBOL programs by improving the resolution of programming linkages and dependency graphs.

  * Upgraded the base Mainframe Assessment Tool virtual machine image to Debian 13.




Issue

Mainframe Assessment Tool version 3.3.0 has the following open issues:

  * When a Business Rules Extraction (BRE) job is in progress and you edit the assessment settings, the BRE job might get stuck. To resolve this issue, edit assessment settings only when a BRE job is not in progress.



Fixed

Mainframe Assessment Tool version 3.3.0 fixes the following issues:

  * Fixed an issue where upgrades could sometimes fail or cause errors.



## May 26, 2026

Feature

Mainframe Assessment Tool version 3.2.0 is available with the following new features and improvements:

  * Added support for [Gemini 3.5 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash) on global endpoints.

For more information, see [Configure general settings](https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-settings#general-settings).

  * Added automatic dependency mapping and Enhanced AI Insights for HLASM, including high-level descriptions and dedicated business logic summaries specifically tuned for HLASM programs.

For more information, see [Discover and analyze source code](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results#discover-analyze).

  * Expanded Business Rules Extraction (BRE) to support all languages available in Mainframe Assessment Tool.

For more information, see [Supported languages](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview#supported-languages) and [Extract business rules](https://docs.cloud.google.com/mainframe-assessment-tool/docs/business-rules-extraction).

  * Added the `SearchContent` and `ExploreData` tools to the Model Context Protocol (MCP) server, enabling agents to search and explore data across source code, AI-generated specifications, and business rules within an assessment.

For more information, see [MCP server tools](https://docs.cloud.google.com/mainframe-assessment-tool/docs/mcp-server#mcp_server_tools).

  * Improved static analysis dashboards to better handle large-scale code bases with faster load times and cleaner visualizations.




Fixed

Mainframe Assessment Tool version 3.2.0 fixes the following issues:

  * Improved security by addressing multiple identified vulnerabilities, ensuring a more secure assessment environment.



## May 05, 2026

Feature

Mainframe Assessment Tool version 3.1.0 is available with the following new features and improvements:

  * Added support for the UniVerse BASIC programming language, enabling you to parse, analyze, and visualize UniVerse BASIC assets within Mainframe Assessment Tool.

For more information, see [Supported languages](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview#supported-languages).

  * Enhanced business rules extraction capabilities to support jobs with multiple driver modules.

For more information, see [Extract business rules](https://docs.cloud.google.com/mainframe-assessment-tool/docs/business-rules-extraction).

  * Improved the performance and robustness of business rules extraction jobs to run at scale by preventing the extraction agent from running for too long while processing large extraction jobs.




Fixed

Mainframe Assessment Tool version 3.1.0 fixes the following issues:

  * Fixed an issue where circular references in call chains caused performance degradation.
  * Fixed an issue affecting calls to embedding Gemini models when using the global Agent Platform endpoint.



## April 01, 2026

Feature

Mainframe Assessment Tool version 3.0.0 is available with the following new features and improvements:

  * Introduced Business Rule Extraction ([Preview](https://cloud.google.com/products#product-launch-stages)), an autonomous agentic workflow to automatically identify and extract business rules directly from mainframe source code. This feature uses Gemini to streamline the discovery of complex mainframe application logic, letting you review, filter, tag, and export the extracted rules for deeper analysis by using Gemini CLI.

For more information, see [Extract business rules](https://docs.cloud.google.com/mainframe-assessment-tool/docs/business-rules-extraction).

  * Introduced an upgraded version of **Ask Gemini** ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) now powered by specialized AI agents for deeper application insights. This enhanced assistant integrates directly with the Mainframe Assessment Tool database to analyze source code, specifications, and business rules letting you generate real-time charts to visualize complex assessment data.

For more information, see [Ask Gemini](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results#ask-gemini).

  * Added support for detecting and parsing FTP scripts, which improves JCL specification accuracy for jobs that include file transfer steps.




Fixed

Mainframe Assessment Tool version 3.0.0 fixes the following issue:

  * Fixed a persistent error state in the Gemini CLI or MCP server where large data fetches or extended idle periods could drop active connections. This fix resolves connectivity issues.



Issue

Mainframe Assessment Tool version 3.0.0 has the following open issues:

  * In some cases, charts generated by **Ask Gemini** appear empty. Although the chart area is empty, data points might still be visible when you hover over the chart.



## March 03, 2026

Feature

Mainframe Assessment Tool version 2.12.0 is available with the following new features and improvements:

  * Mainframe Assessment Tool now supports the following Gemini models:

    * Gemini 3.1 Pro ([Preview](https://cloud.google.com/products#product-launch-stages))
    * Gemini 3 Flash ([Preview](https://cloud.google.com/products#product-launch-stages))
  * Introduced the **Migratable units** report type on the **Discovery** page. This feature automatically partitions assets into migration units based on call and data dependencies to generate a preliminary migration plan.

For more information, see [View and understand assessment results](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results).

  * Added support for detailed logic visualizations for PL/I programs ([Preview](https://cloud.google.com/products#product-launch-stages)), available on the **Detailed logic** page for each PL/I asset.

For more information, see [View and understand assessment results](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results).

  * Introduced schedule analysis support for BMC Control-M XML scheduler configuration files. AI-generated scheduler workflows and specifications are available on the **Assets** page. This data is included in exported HTML and JSON reports.

For more information, see [View AI-generated insights for assets](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results#view-assets).

  * Enhanced automatic analysis of the execution mode (batch or online). The analysis output is displayed in the **All assets** table on the **Assets** page. This analysis is now derived from IMS or CSD configurations, CICS map usage, and screen transaction analysis.

For more information, see [View AI-generated insights for assets](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results#view-assets).

  * Added an option for exporting the full assessment report in JSON format.

For more information, see [Export assessment results](https://docs.cloud.google.com/mainframe-assessment-tool/docs/export-results).




Change

Mainframe Assessment Tool no longer supports Gemini 3 Pro ([Preview](https://cloud.google.com/products#product-launch-stages)). You can use Gemini 3.1 Pro ([Preview](https://cloud.google.com/products#product-launch-stages)) or Gemini 3 Flash ([Preview](https://cloud.google.com/products#product-launch-stages)) instead.

Fixed

Mainframe Assessment Tool version 2.12.0 fixes the following issues:

  * Fixed an issue where exported HTML reports do not include images from the **Domains** page.



## January 19, 2026

Feature

Mainframe Assessment Tool version 2.11.0 is available with the following new features and improvements:

  * Added Gemini 3 Flash ([Preview](https://cloud.google.com/products#product-launch-stages))

  * Added a setting to change the thinking level configuration for supported Gemini models. This setting lets you control the reasoning depth for AI-generated insights.

For more information, see [Configure general settings](https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-settings).

  * Introduced domain architecture diagrams (Experimental). These diagrams are available on the **Domains** page when Gemini 3 Pro ([Preview](https://cloud.google.com/products#product-launch-stages)) is selected as the model.

For more information, see [View and understand assessment results](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results).

  * Enhanced CICS support by parsing CICS Configuration Files (CSD). The surfaced details are available in the **Transactions** and **Orphan Modules** reports.

  * Added support for Easytrieve macro files, which provides more complete and accurate asset summaries by incorporating source file dependencies.

  * Added an **Execution mode** field to the **Assets list** , which specifies whether an asset is a batch or online asset.




## December 16, 2025

Feature

Mainframe Assessment Tool version 2.10.0 is available with the following new features and improvements:

  * Added Gemini 3 Pro ([Preview](https://cloud.google.com/products#product-launch-stages)) as a supported model.

  * Introduced Mainframe Assessment Tool MCP server ([Preview](https://cloud.google.com/products#product-launch-stages)). The MCP server enables AI agents to interact with Mainframe Assessment Tool using the [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro).

For more information, see [Mainframe Assessment Tool MCP server](https://docs.cloud.google.com/mainframe-assessment-tool/docs/mcp-server).

  * Added a setting that lets you use a Vertex AI global endpoint. This setting improves availability with the global Vertex AI endpoint and provides an alternative when an AI model is not available in the region where Mainframe Assessment Tool is deployed.

For more information, see [Configure general settings](https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-settings#general-settings).

  * Enhanced AI insights for PL/I.

  * Improved source code identification accuracy for assembler macros and PL/I.

  * Added identification of duplicate programs, which you can view in the **Duplicate entities** report on the **Discovery** page.




Fixed

Mainframe Assessment Tool version 2.10.0 fixes the following issues:

  * Fixed an issue that occasionally caused a mismatch in the high-level summary.



## December 01, 2025

Fixed

Mainframe Assessment Tool version 2.9.2 fixes the following issues:

  * Fixed an issue where assessments might get stalled in the **High level analysis** step due to handling of task dependencies for domain assignments.



## November 17, 2025

Fixed

Mainframe Assessment Tool version 2.9.1 fixes the following issues:

  * Fixed an issue where JCL job analysis failed for jobs containing `IF` or `ENDIF` statements, which in some cases prevented the analysis from completing.



Issue

Mainframe Assessment Tool version 2.9.1 has the following open issues:

  * After an upgrade, modifying an existing assessment by either uploading new files or updating settings starts a re-analysis of the entire assessment. This behavior might result in a longer processing time and higher costs for the first change made to an existing assessment.



## November 13, 2025

Feature

Mainframe Assessment Tool version 2.9.0 is available with the following new features and improvements:

  * Added options to modify existing assessments including the following:

    * Added an option to upload additional zip files containing new application files to an existing assessment.
    * Added an option to change the settings of an existing assessment.

For more information, see [Configure settings](https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-settings).

  * Enhanced PL/I analysis including the following:

    * Added analysis for PL/I programs to identify interactions with DB2 databases, including create, read, update, and delete operations. This information appears in the **Databases** report type.
    * Added support for CICS integration for PL/I, including detection and parsing of `EXEC CICS` statements and extracting program-to-program calls (`LINK`, `XCTL`) and CICS map usage.
    * Expanded analysis to detect calls to IBM MQ and common system utilities. These extracted dependencies appear in a new chart within the **Module Types** report type.
    * Added cyclomatic complexity for PL/I sources. This metric now appears in the **Complexity** table under the **Complexity** report type.

For more information, see [View and understand assessment results](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results).

  * Added data sets to the **Assets** list, which includes an AI-generated description providing high-level insights into each data set's business purpose.

  * Added support for IMS DC integration with COBOL, including details on IMS transactions, and online COBOL programs.

  * Improved cost-efficiency for JCL job AI analysis.

  * Enabled Cloud logging by default in the Mainframe Assessment Tool settings.




Fixed

Mainframe Assessment Tool version 2.9.0 fixes the following issues:

  * Parsing issues for BMS files that use continuous lines in a fixed-format coding style.
  * Parsing failures for PL/I files that contain non-unicode characters.
  * High CPU and memory usage when running very large assessments.



## October 09, 2025

Feature

Mainframe Assessment Tool version 2.8.0 is available with the following new features and improvements:

  * Added an option to export the assessment static analysis data to Neo4j.

For more information, see [Export assessment data to your Neo4j database](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results#export-to-neo4j).

  * Added support for `Natural for z/OS` and `Fortran` programming languages.

For more information, see [Mainframe Assessment Tool overview](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview).

  * Added support for IMS DB, including detection and parsing of IMS `DBD` and `PSB` definitions, and extracting CRUD information from COBOL programs. The **Databases** report displays the extracted IMS DB information and the IMS DB is integrated into the **Job Connections** report.

  * Added support for IMS Data Communications (DC), including detection and parsing of IMS Message Format Service (MFS) and configuration files containing `APPLCLTN` and `TRANSACT` macros. A new **Transaction** report type displays the extracted relationships between programs, transactions, and screens.

For more information, see [View and understand assessment results](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results).

  * Added the capability to track and analyze Vertex AI costs by automatically adding custom metadata labels to all Vertex AI model requests.

For more information, see [Track Vertex AI costs using custom metadata labels](https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-settings#vertex-costs).

  * Improved cost-efficiency for paragraph-level summaries by optimizing Vertex context cache usage.




## September 09, 2025

Fixed

Mainframe Assessment Tool version 2.7.0 fixes the following issues:

  * When AI analysis fails for an asset, the issue details are not displayed. 
  * Assessments that are in the **In progress** state don't resume after the Mainframe Assessment Tool VM is restarted. 
  * In some cases, dataset fields are not parsed correctly from VSAM files.



Feature

Mainframe Assessment Tool version 2.7.0 is available with the following new features and improvements:

  * Added support for deploying Mainframe Assessment Tool on Google Kubernetes Engine (GKE) clusters. 

For more information, see [Set up and access Mainframe Assessment Tool](https://docs.cloud.google.com/mainframe-assessment-tool/docs/create-instance).

  * Gemini 2.5 Flash-Lite and Gemini 2.5 Flash are now the default models for AI analysis, with Gemini 2.5 Flash used adaptively to optimize performance. 

  * Enhanced the **Assets** page by adding columns for **High-level analysis** and **Code suggestions** , letting you sort and filter by these fields for faster access to insights. 

  * Expanded the list of known built-in mainframe programs.




## August 12, 2025

Feature

Mainframe Assessment Tool version 2.6.0 is available with the following new features and improvements:

  * Introduced basic support for PL/I programming language ([Preview](https://cloud.google.com/products#product-launch-stages)) with program-level summaries, domains, and code suggestions.

For more information, see [Mainframe Assessment Tool overview](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview).

  * Enhanced the **Assessments** page to granularly reflect the status of different phases in the assessment, such as initial analysis, high level analysis, and code suggestions. 

  * Enhanced the **Assets** page to show granular analysis status and error count for each asset. 

  * Enhanced the **Domains** page user interface for improved usability.

  * Enhanced the **Dataset Lineage** table to include temporary datasets for the **Datasets** report type.




Fixed

Mainframe Assessment Tool version 2.6.0 fixes the following issues:

  * Inconsistent font rendering on Windows and Linux clients when compared to Mac.
  * When requesting code suggestions for all languages and detailed logic for very large assessments, the **Assets** page might become unavailable or take longer to load.



Issue

Mainframe Assessment Tool version 2.6.0 has the following open issues:

  * Assessments that are in the **In progress** state don't resume after the Mainframe Assessment Tool VM is restarted.



## July 21, 2025

Feature

Mainframe Assessment Tool version 2.5.0 is available with the following new features and improvements:

  * Significant enhancements to the COBOL code parsing logic for faster processing and improved tolerance for unexpected lines in COBOL code syntax.



Fixed

Mainframe Assessment Tool version 2.5.0 fixes the following issues:

  * When code suggestions and detailed logic are enabled for large assessments, the **Assessment** page sometimes becomes unresponsive.
  * In some cases, upgrading to a new version of Mainframe Assessment Tool fails due to patterns in the existing assessments. 
  * In cases where errors result in very large log files, the Mainframe Assessment Tool logs fail to download. 
  * For very large assessments, exporting reports times out and fails.



Issue

Mainframe Assessment Tool version 2.5.0 has the following open issues:

  * When requesting code suggestions for all languages and detailed logic for very large assessments (a few hundred programs or more), the **Assets** page might become unavailable or take longer to load.

To resolve this issue, we recommend that you split your application files into smaller zip files based on business domains and create a separate assessment for each domain. Alternatively, avoid enabling code suggestions and detailed logic for very large assessments.

  * Assessments that are in the **In progress** state don't resume after the Mainframe Assessment Tool VM is restarted.




## June 30, 2025

Issue

Mainframe Assessment Tool version 2.4.0 has the following open issues:

  * When requesting code suggestions and detailed logic for very large assessments (several hundred programs or more), the assessment page might become unavailable. To resolve this issue, we recommend that you split your application files into smaller zip files based on business domains and create a separate assessment for each domain.

  * Assessments that are in the **In progress** state don't resume after the Mainframe Assessment Tool VM is restarted.




Feature

Mainframe Assessment Tool version 2.4.0 is available with the following new features and improvements:

  * Added Gemini 2.5 Flash as a supported model.
  * Enhanced the user interface for improved usability and faster access to domains, assets, and AI-generated insights. This update includes the following new pages: 
    * An **Assets** page to surface program, job, and screen AI-generated insights.
    * A **Domains** page to consolidate AI-generated insights on business domains.
  * Significant enhancements to improve performance and shorten assessment duration.
  * Enhanced scalability to support larger assessments, increasing the maximum supported zip file size to 400 MB.
  * Added support for RPG include files to improve the quality of AI-generated insights for RPG.
  * Improved COBOL parsing to enhance support for dynamic calls.



Fixed

Mainframe Assessment Tool version 2.4.0 fixes the following issues:

  * Assessment failures caused by parsing of invalid DB2 statements.
  * In some rare cases, an issue caused the assessment to run infinitely.



Announcement

Gemini 1.5 Pro and Gemini 1.5 Flash models are not available for new assessments.

## May 15, 2025

Fixed

Mainframe Assessment Tool version 2.3.1 fixes the following issues:

  * Incorrect Gemini model used for connectivity check on the **Settings** page.
  * Issues with selecting Gemini 2.0 Flash-Lite on the **Settings** page.



## May 12, 2025

Feature

Mainframe Assessment Tool version 2.3.0 is available with the following new features and improvements:

  * Gemini 2.0 Flash-Lite and Gemini 2.0 Flash are now the default models for AI insights, with Gemini 2.0 Flash used adaptively to optimize performance.
  * RPG support for specification and code suggestions [(Preview)](https://cloud.google.com/products#product-launch-stages).
  * Enhanced the user interface navigation, general layout, and the **Settings** page to improve usability and provide easier access to assessment results.



Fixed

Mainframe Assessment Tool version 2.3.0 fixes the following issues:

  * Database performance bottlenecks, which in rare cases led to unresponsiveness in the Mainframe Assessment Tool user interface.



## April 03, 2025

Feature

Mainframe Assessment Tool version 2.2.0 is available with the following new features and improvements:

  * Enhanced the **AI Insights** page user interface for improved usability and faster access to insights.
  * Added Spring Batch code suggestions for JCL jobs.
  * Added domain summaries for **Assessment Domains**.
  * Added Gemini 2.5 Pro Experimental as a supported model.
  * Added version upgrade support. This version supports upgrades from Mainframe Assessment Tool 2.1.0.
  * Added SQL code suggestions for COBOL programs.



## March 19, 2025

Announcement

Mainframe Assessment Tool version 2.1.0 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Feature

Mainframe Assessment Tool version 2.1.0 is available with the following new features and improvements:

  * Added an option to categorize jobs and programs into **Assessment Domains**. You can configure this option when creating a new assessment.
  * Enhanced JCL job summaries to include dataflow information (ETL graph and summary), shown as part of JCL job summaries.
  * Enhanced specifications for HLASM now include business logic information for relevant programs, similar to COBOL programs.
  * Enhanced specifications for Easytrieve now include report generation and formatting information.
  * Added the option to export reports for a filtered subset of programs and jobs.
  * **Gemini 1.5 Flash** and **Gemini 2.0 Flash** (used adaptively to optimize performance) are now the default models for AI insights.



Issue

Mainframe Assessment Tool version 2.1.0 has the following open issues: 

  * **Driver Modules** tab: The **Driver Module** filter is not applied to the **Count of Modules** table.
  * In some cases, filters that were previously set on the **Databases** sub-tab under **Data Lineage** might apply to the main **Databases** tab as well.



## March 12, 2025

Fixed

Mainframe Assessment Tool version 2.0.1 fixes the following issue:

  * Compatibility issues when uploading assessment zip files from Windows machines.



Issue

Mainframe Assessment Tool version 2.0.1 has the following open issues:

  * **Driver Modules** tab: The **Driver Module** filter is not applied to the **Count of Modules** table.
  * In some cases, filters that were previously set on the **Databases** sub-tab under **Data Lineage** might apply to the main **Databases** tab as well.



## February 12, 2025

Feature

Mainframe Assessment Tool version 2.0.0 is available with the following new features and improvements:

  * Redesigned the user interface for a modern and visually appealing experience. This update includes streamlined navigation, insightful new discovery charts, enhanced filtering, and a new **Dashboard** page for quick access to helpful resources.
  * Added the ability to configure advanced settings specific to each assessment, such as generated code languages and tech stack hints. When creating an assessment, you can configure the following options: 
    * Select if you want to include detailed paragraph-level summaries.
    * Select the programming languages for which to generate code suggestions.
  * Added Gemini 2.0 Flash-Lite (Preview) and Gemini 2.0 Pro (Experimental) as supported models.
  * Improved SQL code suggestions for JCL jobs.
  * Enhanced accuracy and adjusted formatting of specifications for COBOL programs involving CICS transactions.
  * Enhanced the format and styling of exported reports.



Issue

Mainframe Assessment Tool version 2.0.0 has the following open issues:

  * **Driver Modules** tab: The **Driver Module** filter is not applied to the **Count of Modules** table.
  * In some cases, filters that were previously set on the **Databases** sub-tab under **Data Lineage** might apply to the main **Databases** tab as well.



Fixed

Mainframe Assessment Tool version 2.0.0 fixes the following issues:

  * Numerous COBOL parsing issues.



## January 28, 2025

Fixed

Mainframe Assessment Tool version 1.6.1 fixes the following issues:

  * If a COBOL program exceeds 5,000 lines of code, an inaccurate paragraph-level summary of the program might be displayed.

  * Improved handling of code containing non-Latin characters and Unicode-encoded null terminators.




Issue

Mainframe Assessment Tool version 1.6.1 has the following open issues:

  * **Driver Modules tab** : the **Driver Module** filter is not applied to the **Count of Modules** table.

  * In some cases, filters that were previously set on the **Databases** sub-tab under **Data Lineage** might apply to the main **Databases** tab as well.




## January 08, 2025

Fixed

Mainframe Assessment Tool version 1.6.0 fixes the following issues:

  * Numerous COBOL parsing issues.



Feature

Mainframe Assessment Tool version 1.6.0 is available with the following new features and improvements:

  * Added **Gemini 2.0 Flash Experimental** as an additional supported model.
  * Introduced new data-focused capabilities under the **Discovery** tab: 

    * **JCL Job Dependency** tab, presenting graphs describing read and write operations.
    * **Databases** tab, providing details on DB2 tables (parsed from COBOL code).
    * **Datasets** tab, providing details on datasets.
  * Enhanced **Discovery** functionalities, including **Inventory** , **Module Types** , and **Complexity**. 

  * Added an option to export a report for the assessment.

  * Improved dataset name parsing from JCL jobs. 

  * Improved COBOL parsing performance.

  * Improved detection of Easytrieve files.




Issue

Mainframe Assessment Tool version 1.6.0 has the following open issues:

  * **Driver Modules** tab: the **Driver Module** filter is not applied to the **Count of Modules** table.
  * In some cases, filters that were previously set on the **Databases** sub-tab under **Data Lineage** might apply to the main **Databases** tab.



## December 05, 2024

Feature

Mainframe Assessment Tool version 1.5.0 is available with the following new features and improvements:

  * The high-level design for the generated code is available for COBOL, Easytrieve, and HSLASM programs in the new **Suggested design** tab.
  * Enhanced quality of Q&A responses.
  * Standardized column and filter names in the **Discovery** tab.



Fixed

Mainframe Assessment Tool version 1.5.0 fixes the following issues:

  * Numerous COBOL parsing issues.
  * Improved parsing of non-UTF-8 encoded COBOL files.
  * Improved handling of AI analyses with long duration.



## November 14, 2024

Fixed

Mainframe Assessment Tool version 1.4.0 fixes the following issues:

  * Numerous COBOL parsing issues.
  * DB concurrency issues.
  * Incorrect description of paragraphs that include `EXIT PROGRAM` statement.
  * Incorrectly displaying variable names instead of programs names under call dependency, in some cases.
  * Providing a large assessment description resulted with an internal error.



Feature

Mainframe Assessment Tool version 1.4.0 is available with the following new features and improvements:

  * Significant specification improvements for COBOL and JCL.
  * Significant code suggestion improvements.
  * Code suggestions for HLASM and EZT.
  * Ability to provide tech stack guidance for suggested code.
  * Improved surfacing of code generation issues.
  * Assessment progress indication.
  * Cross-assessment LLM response cache, and a **Clear LLM Cache** operation on the settings page to purge cached responses.
  * Support for Vertex AI cached context to improve performance and reduce costs.
  * Parsing performance improvements.
  * Presenting LINK commands as part of CICS calls.



## October 14, 2024

Feature

Mainframe Assessment Tool version 1.3.4 is available with the following new features:

  * Parsing enhancement of COBOL, JCL and copybooks.
  * Improved program-level specifications for COBOL, Easytrieve and Assembler.
  * Improved surfacing of missing data issues. 
  * Added an option to customize advanced AI configuration, such as the model and the level of the generated details.
  * Add an option to filter by a program or job status in the **AI** tab.
  * Precision and performance improvements by leveraging the latest Gemini 1.5 models.



Issue

Mainframe Assessment Tool version 1.3.4 has the following open issue:

  * When working with multiple assessments, tab filters in the **Discovery** view don't work as expected. When adding and removing filters, data may appear from multiple assessments. To resolve this, either re-apply filters for the relevant assessment, or exit the **Discovery** view and return to it, which will clear the filters.



Fixed

Mainframe Assessment Tool version 1.3.4 fixes the following issues:

  * Filtering in the **Data Lineage** and **Driver Modules** tabs.
  * Numerous stability issues.



## September 18, 2024

Fixed

Mainframe Assessment Tool version 1.3.2 fixes the following issues:

  * For JCLs that have steps that are referring to Procedures (PROCs), if a PROC doesn't exist, Mainframe Assessment Tool skips that PROC and continues with specification generation for the rest of the JCL.
  * Fixed numerous stability and performance issues.



Feature

Mainframe Assessment Tool version 1.3.2 is available with the following new features:

  * The **Missing Modules** tab now reports missing dataset schemas.



## September 09, 2024

Issue

The following is an open known issue with Mainframe Assessment Tool 1.3.1:

  * For JCLs that have steps that are referring to Procedures (PROCs), if a PROC doesn't exist, an error appears in the **AI [Experimental]** tab, and specifications generation fails for that JCL.



## September 05, 2024

Feature

Mainframe Assessment Tool version 1.3.1 is available with the following new features:

  * Added AI-generated summarization for ASM and EZT programs.
  * Added visualization of copybook dependencies.
  * Added information about parsing issues.
  * Added information about orphan programs (programs that are neither called nor call another program).
  * Added icons in the AI tab to indicate the program type.
  * Improved file parsing performance.
  * Added resolution of TSO program executions in JCL programs.



## July 18, 2024

Feature

Mainframe Assessment Tool version 1.3.0 is available with the following new features:

  * Enhanced Call Dependency graph to include dependencies between Jobs, Programs, and Procedures.
  * Added information about CICS calls used in each program.
  * Added information about JCL Substitution Parameters.
  * Added AI-generated summary describing how program outputs are calculated.
  * Added the **Verify Connectivity** button that allows to confirm access to the Google Cloud resources required for AI features. 
  * Added the **Create Support Bundle** button to collect the necessary troubleshooting information that can be shared with the support team.



Fixed

The following issue is fixed in Mainframe Assessment Tool version 1.3.0:

  * Parsing issues for COBOL and JCL.



## June 19, 2024

Feature

Mainframe Assessment Tool version 1.2.3 is available with the following new features:

  * Improved program-level and job-level summarization.
  * Added support for the latest Gemini 1.5 Pro and Flash models.
  * Improved troubleshooting information for AI analysis issues.
  * Added top-level category tree in the AI tab.



Fixed

Fixed numerous parsing issues for COBOL and JCL.

## May 09, 2024

Feature

Several improvements to the AI capabilities:

  * The experimental **Q &A** tab is available, which lets you use natural language to ask general questions about the imported code.
  * Integration with Gemini 1.0 Ultra is available.
  * SQL stored procedure code generation for JCL jobs is available.



Feature

Improved support for COBOL extensions (DATACOM).

Feature

Improved PDF export through better rendering and compression.

Fixed

The following issues were fixed:

  * Improve error handling in case of LLM errors and timeouts.
  * Allow for larger LLM output and handle cases where the size exceeds the allowed size.
  * PROC file detection errors for files with no extension.



## March 25, 2024

Announcement

Mainframe Assessment Tool is now in Preview.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

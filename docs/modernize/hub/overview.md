---
url: https://docs.cloud.google.com/modernize/hub/overview/
title: Google Cloud Modernization Hub overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:20.192698+00:00
---

# Google Cloud Modernization Hub overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/modernize/hub/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Google Cloud Modernize ](https://docs.cloud.google.com/modernize/hub)
  * [ Modernization Hub ](https://docs.cloud.google.com/modernize/hub)
  * [ Guides ](https://docs.cloud.google.com/modernize/hub/overview)



Send feedback 

#  Google Cloud Modernization Hub overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Google Cloud Modernization Hub is a workspace in the Google Cloud console that helps you to evaluate, plan, and modernize your legacy enterprise workloads on Google Cloud. With Modernization Hub, you can run automated code assessments, follow guided setup workflows, and convert legacy applications written in Java or .NET by using AI-powered tools.

## Key capabilities

Modernization Hub provides the following capabilities:

  * **Workload assessment:** run containerized code scans in the background by using the App Modernization Assessment (`codmod`) for source archives stored in Cloud Storage without provisioning separate Compute Engine instances.
  * **Automated blocker detection:** identify Windows Registry calls, Windows Communication Foundation (WCF) services, Internet Information Services (IIS) dependencies, legacy Java EE namespaces, or proprietary mainframe DB2 schemas in downloadable HTML and Markdown assessment reports.
  * **AI-assisted code transformation:** use Gemini-powered modernization assistants, specialized AI agents, and Antigravity to explain legacy code, refactor dependencies, and accelerate code conversion.
  * **Continuous modernization updates:** Track new refactoring recipes, AI agent capabilities, and product releases directly from the integrated **What's new** feed in Modernization Hub.
  * **Migration risk reduction:** reduce migration risk by using proven migration patterns, automated deployment scripts, and parallel validation tools such as Dual Run for mainframes.



## Supported modernization workloads

Modernization Hub supports assessment and transformation for four core enterprise workload categories. The following table summarizes the assessment tools and target runtimes for each workload:

Workload stack | Assessment tool | Key analysis output | Target runtime  
---|---|---|---  
**ASP.NET / .NET Framework** | App Modernization Assessment (`codmod`) | Linux container readiness, Windows API blockers, NuGet upgrades | Cloud Run, Google Kubernetes Engine  
**Enterprise Java** | App Modernization Assessment (`codmod`) | Linux container readiness, Java EE / JDK blockers, Maven and Gradle upgrades | Cloud Run, GKE  
**Mainframe (COBOL, PL/I, JCL)** | Mainframe Assessment Tool (MAT) | Dependency mapping, complexity scoring, DB2 schema inventory | Compute Engine, Dual Run  
**Legacy Databases (Oracle, SQL Server)** | Database Migration Accelerator (DMA) | Migration readiness, effort estimation, PL/SQL and T-SQL conversion analysis | AlloyDB for PostgreSQL, Cloud SQL for PostgreSQL  
  
### .NET applications

If you run legacy ASP.NET or .NET Framework workloads on Windows, Modernization Hub helps you evaluate container compatibility and modernize your applications for Linux:

  * **Identify Linux container blockers:** identify Windows-specific dependencies such as Windows Registry calls, WCF services, and IIS modules that prevent deployment to Cloud Run or GKE.
  * **Estimate framework upgrade effort:** review compatibility scores and dependency upgrade paths to migrate from .NET Framework 4.x to a modern, cross-platform .NET release.
  * **Automate code conversion:** combine `codmod` assessment reports with specialized .NET agentic skills in [Antigravity](https://antigravity.google/) to refactor legacy Windows dependencies, update NuGet packages, and prepare applications for container deployment. For information about setup prerequisites, see [Refactor .NET code with Antigravity](https://docs.cloud.google.com/modernize/hub/assess-dotnet#refactor-with-antigravity).



### Java applications

If you are modernizing enterprise Java applications, Modernization Hub provides automated analysis powered by the `codmod` engine to evaluate container readiness and upgrade paths to modern Java Long-Term Support (LTS) releases:

  * **Automated`codmod` assessment:** upload your Java source archive to a Cloud Storage bucket and run containerized `codmod` scans from the console.
  * **Actionable reporting:** download HTML and Markdown reports detailing Java EE to Jakarta EE (`javax.*` to `jakarta.*`) namespace changes, deprecated JDK APIs, and Maven or Gradle dependency upgrades.
  * **AI-driven refactoring:** apply recommended transformations and refactoring recipes to prepare Java workloads for Cloud Run or GKE.



### Mainframe workloads

If you are modernizing mission-critical mainframe environments, Modernization Hub provides tooling across four lifecycle stages to transition COBOL, PL/I, Assembler, and JCL assets to Google Cloud:

  * **Assessment:** use Mainframe Assessment Tool to analyze legacy mainframe codebases, map application dependencies, extract business rules, and score migration complexity using guided Google Cloud CLI setup scripts.
  * **Data modernization:** use Mainframe Connector to offload mainframe datasets directly to Cloud Storage and BigQuery for analytics, archiving, and AI processing without disrupting operations.
  * **Automated testing:** use Dual Run to execute existing mainframe workloads in parallel with modernized Google Cloud systems, verifying functional equivalence, performance, and data integrity before cutover.



### Database workloads

If you are migrating relational databases (such as Oracle or Microsoft SQL Server) to fully managed Google Cloud databases, Modernization Hub provides specialized tooling across four modernization capabilities:

  * **Application code conversion** : use Database Migration Agent for Application Code Conversion to refactor embedded application SQL and database connection layers. The agent uses test-driven development (TDD) multi-agent loops to verify functional equivalence alongside your .NET modernization. This agent is available in Antigravity, Claude Code, and Cursor.
  * **Resident code conversion** : use Database Migration Agent for Resident Code Conversion to translate database-resident logic (stored procedures, triggers, views, and schemas) from proprietary dialects such as Oracle PL/SQL or SQL Server T-SQL into target-compatible PL/pgSQL. This agent is available in Antigravity, Claude Code, and Cursor.
  * **Readiness assessment** : use Database Migration Accelerator (DMA) to evaluate migration readiness based on database metadata and calculate the effort required to transition to AlloyDB for PostgreSQL or Cloud SQL for PostgreSQL.
  * **Continuous database migration** : Use Database Migration Service to configure networking, manage continuous data replication, and monitor migration status in the Google Cloud console.



## Discover modernization tools

The **Overview** page helps you discover modernization tools and expert support across the Google Cloud ecosystem:

  * **Explore integrated services:** access dedicated migration interfaces, such as Database Migration Service, without leaving your modernization workflow.
  * **Access AI agents ([Preview](https://cloud.google.com/products#product-launch-stages)):** request early access to specialized IDE agents that automate resident database conversion and application SQL refactoring in tools like Antigravity, Cursor, and Claude Code.
  * **Consult Google specialists:** connect directly with Google Cloud migration architects through the Rapid Migration and Modernization Program (RaMP) for complex, large-scale modernization planning.



## Track release updates

The **What's new** feed on the **Overview** page shows you release announcements, feature launches, and protocol updates across the modernization portfolio, such as Mainframe Assessment Tool features, `codmod` updates, and Dual Run protocol releases, with direct links to the relevant release notes.

## Review the modernization journey

Modernization Hub guides your modernization initiative through four milestones:

  * **Discover:** define your modernization path (replatform, refactor, or rewrite) and select the right migration tools for your stack.
  * **Assess:** quantify technical debt, detect code and schema blockers, and estimate project effort by running automated scans.
  * **Transform:** modernize code, convert database schemas, and establish continuous data replication using AI-assisted agents and CLI tools.
  * **Run and optimize:** deploy containerized workloads to Cloud Run or GKE, and use Gemini Cloud Assist and Active Assist to optimize performance and manage cloud costs.



## Getting support

Modernization Hub is in [Preview](https://cloud.google.com/products#product-launch-stages). During Preview, standard Google Cloud 24/7 support service level agreements (SLAs) don't apply.

To report issues, request assistance, or submit product feedback, email [modernization-hub-feedback-external@google.com](mailto:modernization-hub-feedback-external@google.com).

## What's next

  * Learn how to [assess .NET applications](https://docs.cloud.google.com/modernize/hub/assess-dotnet).
  * Learn how to [assess Java applications](https://docs.cloud.google.com/modernize/hub/assess-java).
  * Learn how to [set up Mainframe Assessment Tool (MAT)](https://docs.cloud.google.com/modernize/hub/setup-mat).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

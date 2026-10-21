---
url: https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview/
title: Mainframe Assessment Tool overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:38:08.183387+00:00
---

# Mainframe Assessment Tool overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Assessment Tool ](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview)



Send feedback 

#  Mainframe Assessment Tool overview Stay organized with collections  Save and categorize content based on your preferences. 

Mainframe Assessment Tool helps assess your existing mainframe codebase and plan your migration to Google Cloud. Mainframe Assessment Tool automates assessment, saving you time and resources. It uses generative AI to help you understand your existing codebase and generate documentation.

The mainframe migration journey has the following phases: discover and assess, plan, and migrate workloads. Mainframe Assessment Tool helps you discover and assess your existing codebase and plan your migration, you can then modernize your code for migration by using the mainframe modernization products available in Google Cloud. For more information about modernizing your mainframe application, see [mainframe modernization overview](https://docs.cloud.google.com/mainframe-assessment-tool/docs/mainframe-modernization-overview).

### Supported languages

The level of analysis and available insights varies by language. For specific capabilities, see [Supported languages](https://docs.cloud.google.com/mainframe-assessment-tool/docs/support-matrix#supported-languages) in the support matrix.

Mainframe Assessment Tool supports the analysis of the following languages and artifacts:

  * COBOL programs and copybooks
  * JCL jobs, procedures, includes, and card data
  * HLASM programs
  * BMS screen maps
  * RPG/RPGLE programs and include files
  * Easytrieve programs
  * Natural for z/OS programs, Data Definition Modules (DDMs), and screen maps (MAPS)
  * PL/I programs ([Preview](https://docs.cloud.google.com/products#product-launch-stages))
  * REXX programs ([Preview](https://docs.cloud.google.com/products#product-launch-stages))
  * Fortran ([Preview](https://docs.cloud.google.com/products#product-launch-stages))
  * UniVerse BASIC ([Preview](https://docs.cloud.google.com/products#product-launch-stages))



You can [extract business rules](https://docs.cloud.google.com/mainframe-assessment-tool/docs/business-rules-extraction) only from COBOL, Assembler (HLASM), Easytrieve, PL/I, Natural, and RPG programs.

### Databases and datasets

Mainframe Assessment Tool supports the following databases and datasets:

  * DB2: through Embedded SQL
  * IMS DB: through `EXEC DLI` and `CBLTDLI` calls
  * Adabas: through Natural Data Definition Modules (DDMs)
  * QSAM and VSAM datasets



### Transaction monitors

Mainframe Assessment Tool supports the following transaction monitors:

  * CICS: through `EXEC CICS` statements
  * IMS DC: through `CBLTDLI` calls



### Scheduler configurations

Mainframe Assessment Tool supports the following scheduler configurations:

  * BMC Control-M



For more detailed information about what is supported for each of these technologies, see the [Support matrix](https://docs.cloud.google.com/mainframe-assessment-tool/docs/support-matrix).

## Mainframe migration journey

The following diagram illustrates the overall migration journey of mainframe applications:

![Phases of mainframe migration journey](https://docs.cloud.google.com/static/mainframe-assessment-tool/docs/images/overview.png)

The migration journey has the following phases:

  * **Discover and assess your existing codebase:** Mainframe Assessment Tool helps you perform an assessment of the mainframe application footprint, technology stack, and dependencies. After you upload a zip file that contains code for one or more mainframe applications, Mainframe Assessment Tool scans the application code and provides you with an assessment. Automating the assessment process with Mainframe Assessment Tool saves your organization the time and effort of manually collecting and processing the application code.
  * **Plan the migration:** You can use the detailed assessment from Mainframe Assessment Tool to plan your migration more quickly and to lower migration risks. To help you plan, Mainframe Assessment Tool automatically groups mainframe assets into sequenced migratable units based on call and data dependencies, and user configuration.
  * **Migrate workloads:** Depending on the choices that you made during the planning phase, you can use Google Cloud solutions to start migrating.



## Code modernization

After you complete your assessment by using Mainframe Assessment Tool, you can start modernizing your code. This process involves transforming your legacy mainframe applications into modern, cloud-native applications. By modernizing, you can enhance agility, scalability, and security, while reducing maintenance costs and complexity.

The key activities in the modernization process include the following:

  1. **Generate and transform code:** Use [Antigravity](https://antigravity.google/) to convert your mainframe application to modernized applications using natural language prompts and automated workflows. Antigravity uses Mainframe Assessment Tool through the MCP server to understand your application context and generate modernized code.
  2. **Modernize and migrate mainframe data:** Use [Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs/overview) to make mainframe data fully accessible to Google Cloud services by copying it off the mainframe and into Cloud Storage, BigQuery and databases.
  3. **Reduce migration risks with parallel testing:** Use [Dual Run](https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-overview) to run workloads on both your mainframe and Google Cloud simultaneously to ensure consistency and functional validation before production.



For more information about the tools and processes involved in modernizing your mainframe applications, see [mainframe modernization overview](https://docs.cloud.google.com/mainframe-assessment-tool/docs/mainframe-modernization-overview).

## Data collection security and privacy

Mainframe Assessment Tool only collects information extracted from the zip file that you provide. It doesn't collect personally identifiable information (PII) or data subject to Payment Card Industry (PCI) data security standard, or Health Insurance Portability and Accountability Act (HIPAA) compliance requirements.

All the collected data is used only to assess and analyze your applications for the purposes of cloud migration assessment and planning. Your data is never exported outside the VM on which it is deployed. The source code is uploaded to Gemini Enterprise Agent Platform, but the model is not enriched by information extracted from this source code.

## What's next

  * Review the [Support matrix](https://docs.cloud.google.com/mainframe-assessment-tool/docs/support-matrix) for supported languages, database schemas, transaction monitors, and schedulers.
  * [Configure your Google Cloud project for Mainframe Assessment Tool](https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-your-project).
  * [Set up and access Mainframe Assessment Tool](https://docs.cloud.google.com/mainframe-assessment-tool/docs/create-instance).
  * [Perform an assessment](https://docs.cloud.google.com/mainframe-assessment-tool/docs/perform-assessment).
  * [Review assessment results](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 

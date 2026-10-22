---
url: https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results/
title: Review assessment results \u00a0|\u00a0 Mainframe Assessment Tool \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:48.136657+00:00
---

# Review assessment results  |  Mainframe Assessment Tool  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Assessment Tool ](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview)



Send feedback 

#  Review assessment results Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to review the assessment of the discovered assets, and analyze the application source files using generative AI.

The assessment results provide you with details such as the lines of code and number of calls found in the application, which help you plan your migration. Also, the analysis provides you with a summary of the program, which helps you understand the semantics of the program.

## Before you begin

  * [Create an assessment](https://docs.cloud.google.com/mainframe-assessment-tool/docs/perform-assessment)



## Review application assessment results

To open an assessment to review results, follow these steps:

  1. Open the Mainframe Assessment Tool in a web browser.
  2. In the navigation menu, click **Assessments**.
  3. On the **Assessments** page, to open a specific assessment, click the arrow_forward expander arrow.



The assessment dashboard appears, and it includes the following pages:

  * **Discovery** : Discover and analyze source code.
  * **Domains** : Review AI-generated insights for your business domains.
  * **Assets** : Review AI-generated insights for assets.
  * **Business rules** : Learn how to [extract business rules](https://docs.cloud.google.com/mainframe-assessment-tool/docs/business-rules-extraction) and explore hierarchical Business Rules Extraction (BRE) visualizations on the **Business Flow** tab.



### Discover and analyze source code

The **Discovery** page provides an overview of analysis of the application source code that you uploaded for assessment.

To discover and analyze your source code, follow these steps:

  1. Click **Discovery**.

  2. To select a report type, in the **Report type** list, select the report type that you want to view.

The following table lists different report types and their description: 

Report type | Description | Details  
---|---|---  
**Inventory** | Provides details about the number of files, code lines, and program types, including scheduler configuration files (BMC Control-M). | 
     * **Count by file type:** number of files per language.
     * **Lines of code by file type:** number of code lines per file type.
     * **Actual vs commented lines of code:** number of code lines compared to number of comment lines.
     * **Category - batch/online:** number of batch programs compared to online programs.
     * **Total lines of code:** total number of lines of code across all files included in the assessment. Use this data to understand the overall size of the codebase.  
**Module Types** | Categorizes modules based on their call relationships, specifically for COBOL and JCL. | 
     * **Modules called from COBOL programs:** number of modules that are called directly from within the COBOL source code.
     * **Modules called from JCL:** number of modules that are called directly in your JCL files.
     * **Top 5 COBOL module utilities:** list of frequently used utilities used by your COBOL programs.
     * **Top 5 JCL module utilities:** list of frequently used utilities in the JCL jobs.  
**Complexity** | For COBOL programs, shows the complexity of the source code by using [Cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity) (McCabe's metric). McCabe's metrics represent the number of execution paths or decision points in the source code. This qualitative value helps you identify which applications might be easier or more complex to modernize. | 
     * **Complexity table:** a file-by-file breakdown of the calculated complexity metrics such as complexity count. A higher complexity count suggests a more complex program.
       * Simple: complexity < 100
       * Medium: 100 <= complexity < 500
       * Complex: 500 <= complexity < 1000
       * Very complex: 1000 <= complexity
     * **Complexity mapping:** visual representation of the complexity table that provides an overview of the complexity in your codebase.  
**Call Dependency** | Displays the call graph of all uploaded entities, including resolved dynamic COBOL calls and calls extracted from other [supported languages](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview#supported-languages). Call resolution for PL/I supports only static calls. | The size of the icons is related to the number of incoming and outgoing calls.  
**Driver Modules** | Shows modules that call many other modules. | The size of the icons is related to the number of incoming and outgoing calls.  
**Datasets** | Provides a detailed view of all datasets involved in the assessment. | 
     * **Dataset Lineage:** shows how each dataset is used across different jobs, steps, and programs.
     * **Dataset Fields:** lists all fields within each dataset, along with their data types, start positions, sizes, key indicators, and other properties.  
**Databases** | Lists the DB2 tables and IMS segments used in the assessment. | Details the data lineage, columns, and properties for each segment and table.  
**Orphan Programs** | Lists all programs that neither call another entity nor are called by another entity. | 
     * **Program name:** identifies the program module that has been found within the uploaded source code but does not appear to be called or executed by any other part of the application.
     * **Original source file:** the name of the file that contains the source code for the corresponding program name.  
**Missing Modules** | Shows modules used in the code but not found during input analysis. | 
     * **Missing from file:** the specific source file that contains a reference to a module or component that couldn't be found within the uploaded assessment files.
     * **Missing module name:** the name of the module or component that is missing within the uploaded files.
     * **Missing module type:** the type of the missing component, which helps in understanding the nature of the dependency. For example, `DATASET_SCHEMA`, `COPYBOOK`, or `PROC`.
Use this tab to understand what was missing and consider adding these modules before re-running the assessment.  
**Parse Issues** | Shows all errors encountered during source code parsing. | 
     * **Source File:** name of the specific file from your uploaded source code in which the parser found an issue.
     * **Severity:** indicates the seriousness of the parsing issue. For example, `Warning`.
     * **Issues:** provides a description of the issue found by the code parser.  
**CICS Calls** | Shows the CICS calls made from each program and their parameters. | You can filter the results by command, program, or parameter.  
**JCL Job Connections** | Displays dependencies between JCL jobs based on shared datasets, DB2 tables, and IMS segments. | 
     * **Connected jobs based on a shared data source:** shows the connection between two jobs if one job writes data to a shared data source and the other job reads from that same data source. Jobs that only read from the same data source are not connected to each other.
     * **Connected jobs based on a shared data source (tabular view):** shows the connection details between the jobs.
     * **Job dependencies from writers to readers:** shows the writer job, the writer program, the data source, the reader program, and the reader job.  
**JCL Substitution Params** | Shows the resolved values of the JCL parameters. | 
     * **Job name:** uniquely identifies a specific JCL job, a set of instructions for the mainframe that executes a batch process.
     * **Step Name:** identifies a single execution step within a JCL job. A job consists of one or more steps; each step typically runs a specific program or procedure.
     * **Data definition name:** shows the name of a data definition statement in a JCL procedure.
     * **Data set name:** identifies the name of a file, or dataset, as it exists on the mainframe's storage volumes.
     * **Parameter Name:** refers to a symbolic parameter that acts as a variable within a JCL procedure.
     * **Parameter Value:** refers to the value that is assigned to a symbolic parameter within a JCL procedure.  
**Transactions** | Displays the extracted relationships between programs, transactions, and screens for IMS and CICS. | 
     * **Program:** the name of an online IMS or CICS program.
     * **Transaction:** an IMS or CICS transaction code that can be used to schedule execution of the program.
     * **Screen:** the name of the screen or map that is used by the program or transaction.  
**Duplicate Entities** | Lists programs that have the same program ID. | 
     * **Name:** the name of one of the programs in a set of programs with the same program ID.
     * **Type:** the type of the program; for example, `COBOL` or `JCL`.
     * **Source file:** the source file containing this program.
     * **Additional source file:** lists the other source files that contain programs with the same program ID.  
**Migratable units** | Partitions assets into migration units to generate a preliminary migration plan. | 
     * **Migratable units graph:** shows how migration units depend on each other in a dependency diagram (DAG).
     * **Migratable units list:** the list of migratable units with the name of migratable units, asset count, and source line count.
You can also see the assets graph and the list of assets and asset types associated with a migratable unit.
     * **Assets graph:** displays the dependencies between assets within a migratable unit.
     * **Assets list:** lists assets in the migratable unit with columns for migratable unit name, asset name, asset type, and the lines of code (source lines).  
  



### Review AI-generated insights for your business domains

The **Domains** page provides AI-generated insights for the business domains associated with this assessment. An assessment can have multiple domains, as many as you specified when creating the assessment. Each domain has its own status, summary, business logic, data flow, and associated assets. Domains help you partition portions of your codebase as belonging to a specific business function.

This feature requires that you enable AI insights and add a business domain when you create the assessment. If this page is unavailable, create a new assessment, and enable AI insights.

To get an AI-generated description of your application's business domains, follow these steps:

  1. Click **Domains**.

A list of domains is displayed, along with the status of each domain.

  2. To see the summary, business logic, and data flow of a specific domain, click **Show more**.

You see detailed AI-generated descriptions of your application's business domain. These descriptions include the purpose, logic, processing data, data flow, and data dependencies.

  3. To search for a specific domain, in the **Search** field, enter the domain name.

  4. Optional: To view the list of assets associated with this domain, click **View assets**.




### Domain images

**Note:** This is an experimental feature.

The **Domains** page also displays AI-generated images representing your business domains. Each domain image is generated based on the domain specification to visually represent the functions and systems described in the domain.

Domain image generation has the following requirements:

  * Use of the global Agent Platform endpoint.
  * Supported AI models: Gemini 3.5 Flash, Gemini 3.1 Pro ([Preview](https://cloud.google.com/products#product-launch-stages)) and Gemini 3 Flash ([Preview](https://cloud.google.com/products#product-launch-stages)). Mainframe Assessment Tool uses the Gemini 3 Pro Image ([Preview](https://cloud.google.com/products#product-launch-stages)) for domain image generation.



### Review AI-generated insights for assets

The **Assets** page provides a summary and detailed logic for a program or job in your mainframe application. You can also view the status, type, language, and execution mode (batch or online) for each asset.

For scheduler configuration assets, such as BMC Control-M, Mainframe Assessment Tool provides AI-generated insights that help you visualize the scheduler workflow, including a listing of scheduled jobs, timelines for daily, weekly, or monthly schedules, and dependency graphs showing job relationships. This data is also available in the exported HTML and JSON reports.

The **Assets** page displays a new entry in the table for each discovered asset, showing its assessment status.

  * **Pending:** asset is waiting its turn for analysis.
  * **In Progress:** asset assessment is in progress.
  * **Completed:** asset analysis has been completed.
  * **Warning:** assessment is complete with a non-blocking warning during code generation.



To narrow the selection of assets, apply filters in the `Filter` field. Select a property name to filter on and enter a property value. For example, to filter for all assets by their assessment status, set the property name to `Status`, and select a value such as `Warning` or `Completed`.

To view details of an asset, follow these steps:

  1. In the **All assets** table, click the name of an asset.

The **Summary** page appears; this page provides an AI-generated summary of the asset, along with the business case, and the user interaction analysis.

  2. To view the detailed logic about the asset, click **Detailed Logic**.

For COBOL programs and JCL jobs, the **Detailed logic** page provides granular, paragraph-level, and method-level details about the asset along with test cases. If the JCL job is referenced by a scheduler configuration in the assessment, this page also includes information about its scheduler job prerequisites, dependent jobs, and execution schedules.

  3. To view the output fields, click **Output fields**.

For COBOL programs, the **Output fields** page provides a summary of specific data fields that a program generates and their descriptions.

  4. To view the BMS screen, click **BMS maps**.

For BMS assets, the **BMS maps** page shows you the interface screen.




## Ask Gemini

**Note:** To use the **Ask Gemini** feature, you must configure and use the global Agent Platform endpoint because this feature uses Gemini preview models.

The **Ask Gemini** chat pane lets you explore your assessment using natural language. You can ask questions about source code and business logic, query assessment data such as line counts or complexity metrics, and generate visualizations like charts.

To use **Ask Gemini** , follow these steps:

  1. Click the ![the ask Gemini icon](https://docs.cloud.google.com/static/mainframe-assessment-tool/docs/images/ask_gemini.png)**Ask Gemini** icon.

  2. Enter your question and press **Enter**. Responses are streamed in real time.

  3. To start a new conversation, click add **New chat**.

  4. To view or resume previous conversations, click more_vert **More** > **Show chat history**.

  5. To delete a conversation, click more_vert **More** > **Show chat history** , and then click delete the conversation that you want to remove.

  6. To switch to the classic chat experience, click more_vert **More** > **Use classic chat**. To switch back, click more_vert **More** > **Use enhanced chat**.




## What's next

  * Learn how to [export assessment results](https://docs.cloud.google.com/mainframe-assessment-tool/docs/export-results).
  * Learn how to [extract business rules](https://docs.cloud.google.com/mainframe-assessment-tool/docs/business-rules-extraction).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

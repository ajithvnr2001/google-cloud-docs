---
url: https://docs.cloud.google.com/mainframe-assessment-tool/docs/modernize-validate/
title: Modernize and validate \u00a0|\u00a0 Mainframe Assessment Tool \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:26.846865+00:00
---

# Modernize and validate  |  Mainframe Assessment Tool  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-assessment-tool/docs/modernize-validate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Assessment Tool ](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview)



Send feedback 

#  Modernize and validate Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to modernize your mainframe applications by using Antigravity with the outputs from Mainframe Assessment Tool, and then validate the deployed applications on Google Cloud by using Dual Run.

After assessing your mainframe application and extracting business rules with Mainframe Assessment Tool, you can use Antigravity to transform your legacy code into high-quality, cloud-native code. This process uses technical metadata and business requirements to ensure the target application is architecturally and functionally equivalent to the original.

After your modernized application is deployed to Google Cloud, Dual Run helps reduce the risk of the transition. It lets you run workloads simultaneously on your existing mainframe and on Google Cloud, comparing outputs like daily reports and online transactions. This real-time testing helps you gather data on functional equivalence, performance, and stability, ensuring a reduced-risk transition.

By following the instructions on this page, you'll learn how to:

  * Use Antigravity for modernization tasks, leveraging the `AGENTS.md` file created by Mainframe Assessment Tool.
  * Enable communication between Antigravity and the assessment data.
  * Use Dual Run to validate your deployed application.



This page is intended for IT professionals, architects, and engineers involved in mainframe modernization projects.

## Before you begin

To prepare your environment for code modernization, complete the following steps.

### Roles and permissions

  * Make sure that you have the necessary IAM roles to access the Mainframe Assessment Tool MCP server. For more information, see [Mainframe Assessment Tool MCP server](https://docs.cloud.google.com/mainframe-assessment-tool/docs/mcp-server).
  * Confirm you have access to Antigravity and permissions to run agent workflows. For more information, see [Antigravity documentation](https://antigravity.google/docs/mcp).



### Requirements

Before modernizing application code with [Antigravity](https://antigravity.google/), verify that you have the following:

  * **A local workspace:** create a dedicated directory on your computer to store your exported configuration files, agent skills, and generated code.
  * **An active MCP server** : ensure that the Mainframe Assessment Tool MCP server is [enabled and accessible](https://docs.cloud.google.com/mainframe-assessment-tool/docs/mcp-server#enable-mcp-server) from your local environment.
  * **MCP connection and agent skill:** on the **Assessments** page in Mainframe Assessment Tool, click **Use with Antigravity** in the toolbar to configure Antigravity: 
    * **Configure MCP:** view the connection details to [connect Antigravity to the MCP server](https://docs.cloud.google.com/mainframe-assessment-tool/docs/mcp-server#connect-mcp-server).
    * **Download Skill:** download `skill.zip`, which contains the `mat-backend-query` agent skill for querying call trees, database access patterns, and dataset I/O metrics. For extraction instructions, see [Install and use the Mainframe Assessment Tool agent skill](https://docs.cloud.google.com/mainframe-assessment-tool/docs/mcp-server#install-agent-skill).
  * **Exported agent configuration (`AGENTS.md`):** [export the `AGENTS.md` file](https://docs.cloud.google.com/mainframe-assessment-tool/docs/business-rules-extraction#export-rules) from your completed business rules extraction job. This file provides Antigravity with context about your assessment.



## Configure the `AGENTS.md` file

Antigravity uses the `AGENTS.md` file that you exported from Mainframe Assessment Tool to communicate with your assessment. The `AGENTS.md` file contains the unique identifiers for the assessment and the specific business rules extraction job.

To configure Antigravity to modernize code, follow these steps:

  1. Go to the root directory of your workspace.

  2. Check if an `AGENTS.md` file already exists.

Based on whether the file exists, do one of the following:

     * If an `AGENTS.md` file doesn't exist, place the `AGENTS.md` file that you downloaded from the Mainframe Assessment Tool in this directory.

     * If the `AGENTS.md` file already exists, open the existing file and append the following content to the end of the file.
           
           ## Mainframe Assessment Tool MCP Configuration
           
               assessmentID: ASSESSMENT_ID
               jobID: JOB_ID
           

Replace the following:

       * `ASSESSMENT_ID`: your specific assessment ID.
       * `JOB_ID`: the job ID of the business rules extraction job from Mainframe Assessment Tool.



## Modernize your mainframe application code with Antigravity

After you configure Antigravity to modernize code, it automatically uses the `assessmentID` and `jobID` from your `AGENTS.md` file to contextually understand your application.

Antigravity uses the [Mainframe Assessment Tool MCP server tools](https://docs.cloud.google.com/mainframe-assessment-tool/docs/mcp-server#mcp-server-tools) and combines multiple data sources from your assessment and design phases to perform analysis and generate the following:

  * Validated business rules: core business logic extracted from legacy code and verified by stakeholders.
  * Target data model: optimized data structures designed for your target Google Cloud environment, such as Cloud Spanner or Cloud SQL.
  * Product Requirements Document (PRD): a human-readable specification that serves as the blueprint for the modernized application.
  * Modernized application code: cloud-native code in the language of your choice that implements the business rules.



To use the information gathered during your assessment to understand and modernize your mainframe application, you can use prompts like the following in Antigravity:

  * To retrieve business rules, plan the target data model, and generate a PRD:
        
        Get business rules for business rules extraction job JOB_NAME.
        Based on these rules, suggest a target data model for Spanner  and
        generate a Product Requirements Document.
        

Replace `JOB_NAME` with the job name of the business rules extraction job from Mainframe Assessment Tool.

  * To generate the modernized code:
        
        Generate the Java code to implement the business rules from the business rules
        extraction job ID:JOB_NAME by using the suggested Spanner 
        data model.
        

Replace `JOB_NAME` with the job name of the business rules extraction job from Mainframe Assessment Tool.




## Review the generated code

After generating the code, verify the output to ensure accuracy and architectural alignment.

Review Checklist  
---  
**Logic accuracy** | Compare generated methods against the validated business rules in your business rules extraction Job. Make sure that every rule is mapped to a code block.  
**Architectural alignment** | Verify the code correctly implements the suggested data structures and uses appropriate Google Cloud client libraries.  
**Security and performance** | Scan for hard-coded credentials or inefficient loops. Use Antigravity to fine-tune specific code sections for performance.  
  
## Validate the modernized code with Dual Run

Dual Run lets you simultaneously run workloads on your existing mainframes and on Google Cloud, letting you perform real-time testing and quickly gather data on performance and stability.

For more information, see [Dual Run overview](https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-overview).

## What's next

  * Learn more about [Antigravity](https://antigravity.google/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 

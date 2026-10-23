---
url: https://docs.cloud.google.com/mainframe-assessment-tool/docs/business-rules-extraction/
title: Extract business rules \u00a0|\u00a0 Mainframe Assessment Tool \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:25.147307+00:00
---

# Extract business rules  |  Mainframe Assessment Tool  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-assessment-tool/docs/business-rules-extraction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Assessment Tool ](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview)



Send feedback 

#  Extract business rules Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions on how to extract business rules from applications written in the [supported languages](https://docs.cloud.google.com/mainframe-assessment-tool/docs/support-matrix#core-analysis-capabilities). This feature helps you validate business logic and identify obsolete rules in your mainframe codebase.

During business rule extraction, Mainframe Assessment Tool analyzes your mainframe application codebase to identify the business rules, and presents them in a standardized, human-readable format.

## Benefits of business rules extraction

Business rules extraction helps you achieve the following goals:

  * **Create a single source of truth:** Mainframe Assessment Tool extracts your mainframe application logic into human-readable business rules in Gherkin, a plain-text domain-specific language (DSL) used in behavior-driven development (BDD). This standardized format translates complex code into clear scenarios, bridging the gap between technical discovery and business intent.
  * **Eliminate obsolete logic:** identify and remove irrelevant rules to streamline the migration to Google Cloud.
  * **Accelerate modernization:** generate application specifications from your mainframe code to speed up the modernization process.
  * **Reduce risk:** minimize functional divergence by validating the extracted rules with business process owners before modernization.



This page is intended for mainframe developers, enterprise architects, and business analysts who want to understand and modernize legacy mainframe applications by extracting business rules from source code.

This page explains how to do the following:

  * Extract business rules: run an extraction job to identify business rules in your mainframe application.
  * Review and validate rules: analyze the extracted rules to ensure accuracy and relevance to your modernization goals.
  * Update rule status: update the status of the extracted rules to reflect their relevance to your modernization goals.
  * Export business rules: export the extracted rules to a file for further analysis or modernization.



## Before you begin

Before you begin, make sure that you have completed the following tasks:

  * Create an assessment: make sure that you have an existing assessment with uploaded mainframe assets such as programs and copybooks. For more information, see [Create an assessment](https://docs.cloud.google.com/mainframe-assessment-tool/docs/perform-assessment).
  * Identify the entry point: select the primary module in your mainframe application that serves as the entry point for business rules extraction.
  * Use the global Agent Platform endpoint because this feature uses Gemini preview models.



## Start a business rules extraction job

Mainframe Assessment Tool uses Gemini-powered agents to analyze your code. These agents perform the extraction in several steps, such as parsing code, identifying decision logic, and generating natural language output.

You can run multiple extraction jobs within a single assessment to analyze large applications incrementally. This process lets you focus on specific business functions such as invoicing or payroll by selecting different sets of assets for each job. Each time you start a new extraction, you can select a different set of assets for analysis.

To start a business rules extraction job, follow these steps:

  1. Open the Mainframe Assessment Tool in a web browser.
  2. In the navigation menu, click **Assessments**.
  3. On the **Assessments** page, to open a specific assessment, click the arrow_forward expander arrow.
  4. Click **Business rules**.
  5. Click **New extraction job**.
  6. To configure the details of the extraction job, on the **Basic information** page, follow these steps:

     1. For **Name** , enter a unique identifier for the job.
     2. Optional: For **Description** , enter a short description of the job (up to 128 characters).
     3. Optional: For **Focus prompt** , provide specific instructions to focus the extraction. For example: 
        * `Extract only the tax calculation logic`
        * `Extract only rules involving the accounts data`
        * `Extract only rules that are implemented in the branch of the code that handles car insurance`
     4. Click **Next**.
  7. From **Module list** , select one or more primary modules to analyze.

These modules serve as the entry points for the extraction. When you select primary modules, Mainframe Assessment Tool automatically identifies and includes all dependencies, such as copybooks and called programs. This ensures that the business rules are complete and reflect the full application logic.

  8. After you've selected the primary modules, click **Run extraction job**.




While a job is running, the **Extraction jobs** table shows you the status of the job. This status indicates the number of internal planning steps that the agent has successfully completed out of the total required for that specific analysis.

After the extraction job finishes, the status in the **Extraction jobs** table changes to **Completed**.

## Review the business rules

After Mainframe Assessment Tool extracts business rules, you can review and refine them. This review process ensures that only correct and necessary rules are used for modernization, and helps you identify obsolete or incorrect logic before the rules are modernized.

To review business rules in an extraction job, follow these steps:

  1. In the **Extraction jobs** table, select the job you want to review.

The job overview displays the configuration details, such as the description, the focus prompt, and the list of assets included in the analysis. You also see a table with the extracted business rules and their associated tags.

  2. To explore the extracted rules hierarchically, click **Business Flow**.

  3. To view the generated specifications, click **Specifications**.

The **Specifications** tab displays the following information:

     * **Objective:** a summary of the system and its operational framework.
     * **Functional Requirements:** specific behaviors the system must support.
     * **User Journeys:** end-to-end scenarios derived from the business rules.
     * **Glossary:** definitions of key terms and acronyms used in the application.
     * **Recommended Modernization Order:** a suggested step-by-step approach to modernize the mainframe application.
  4. On the **Business rules** tab, review the extracted business rules and their tags.

  5. To open the **Rule details** pane, select a specific rule.

The **Rule details** pane displays the following information:

     * **Name:** the name of the business rule.
     * **Summary:** a description of the rule's purpose and function.
     * **Confidence:** a percentage indicating the system's confidence in the extracted rule.
     * **Justification:** an explanation of how the rule was derived and why it is considered accurate.
     * **Tags:** the tags that Mainframe Assessment Tool automatically assigns to the rule. Use these tags to understand the rule's context and to filter the rules.
     * **Rule content:** the details of the business rule, such as input data, output data, business logic, and edge cases.
     * **Assets:** the source code assets associated with the business rule that map the rule back to the mainframe code.
     * **Code references:** shows the source code snippets used to derive each rule. Rules that span across multiple source assets will show the relevant code snippets from all of them.



## Update rule status

When business rules are extracted, they are assigned an initial status of **Awaiting review**. During your review, you must validate these rules to make sure that they reflect the current business intent and identify rules that should be considered for modernization. By selecting a status, you make sure that the modernization specifications accurately reflect your current business needs.

To select the status of business rules, follow these steps:

  1. In the **Business rules** table, select the rules that you want to update.
  2. Click the **Change status** menu and then select one of the following statuses:

     * **Awaiting review:** the default status for all rules. Indicates that the rule has not been reviewed.
     * **Validated:** select this status to confirm that the rule is accurate and active. Mainframe Assessment Tool uses rules that you mark as **Validated** to regenerate application specifications for modernization.
     * **Pending validation** : select this status if the rule requires further analysis or additional input for validation.
     * **Obsolete:** select this status to flag rules that are no longer relevant. Mainframe Assessment Tool excludes rules marked as **Obsolete** from export and modernization.



## Export business rules

After you review the extracted business rules, you can export them to a file. Exporting business rules lets you use the rules as input with tools such as Antigravity for modernization and analysis, share them with stakeholders, or perform offline analysis.

To export business rules, follow these steps:

  1. In the **Business rules** table, select the rules that you want to export.
  2. To export business rules in JSON format, click **Export**.
  3. To export the agent configuration in Markdown for use with Antigravity, click **Export for Gemini Modernization**. This configuration lets Antigravity connect and directly download the rules.



## What's next

  * Learn how to [export assessment results](https://docs.cloud.google.com/mainframe-assessment-tool/docs/export-results).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

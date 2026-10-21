---
url: https://docs.cloud.google.com/database-migration/docs/convert-sql-with-dms/
title: Convert SQL with Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:38.696365+00:00
---

# Convert SQL with Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/convert-sql-with-dms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/overview)



Send feedback 

#  Convert SQL with Database Migration Service Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service helps you convert Oracle and SQL Server schema to PostgreSQL. You accomplish this using conversion workspaces and Gemini-powered conversion.

  * Conversion workspaces provide tools to convert schema and code objects.

  * Gemini assistance uses the power of AI to reduce migration time and complexity.

  * See  Supported scenarios for links to scenario-specific documentation.




## Conversion workspaces

Use conversion workspaces to expedite and improve the migration process for heterogeneous databases. The conversion workspaces handle code and schema conversion, simplifying the transition to your destination database.

They offer tools that let you monitor conversion progress with robust overviews. Conversion workspaces also facilitate collaborative conversion issue solving in the conversion editor, where you can adjust the resulting PostgreSQL code in real time.

![Conversion workspace screen where the animation shows users clicking
           between three different tabs: Conversion Overview, Conversion Issues,
           and Code.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/switching_tabs_ws_overview.gif) **Figure 1.** Conversion workspace overview screen, where you can monitor the progress of your conversion, view issues and inspect the resulting PostgreSQL code. (click to enlarge) ![Conversion workspace screen where the animation shows users clicking
           between three different tabs: Conversion Overview, Conversion Issues,
           and Code.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/switching_tabs_ws_overview.gif)

## Accelerate code and schema conversion with Gemini

Gemini-powered conversion features in Database Migration Service help you apply the power of AI to reduce the time and complexity of your migrations.

Use the following complimentary approaches for a complete end-to-end Gemini-powered code object conversion experience:

### Auto-conversion

Gemini-powered conversion engine can automatically enhance the deterministic conversion patterns used by Database Migration Service. When you enable the auto-conversion feature, Gemini processes all your converted schema is processed to significantly reduce the number of manual adjustments needed in your PostgreSQL code.

After all augmentations are complete, you can explore the details for each object:

  * **Conversion summary** includes an overview of how and why Gemini fixed issues found in the deterministic conversion, as well as a list of issues that still require further adjustments.

  * **Code comparison** provides you with a side-by-side comparison between Gemini-powered augmentations and the deterministic conversion.


![Gemini-powered auto-conversion panel with details regarding what
           adjustments are implemented to the converted schema.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/auto_conversion_overview_oracle_csql.png) **Figure 2.** Gemini-powered auto-conversion panel where you can inspect the details of code and schema. (click to enlarge) ![Gemini-powered auto-conversion panel with details regarding what
           adjustments are implemented to the converted schema.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/auto_conversion_overview_oracle_csql.png)

### Conversion assistant

Conversion assistant is a set of dedicated prompts that can help you better understand the conversion logic, propose fixes for conversion issues, or optimize converted code. For example, if certain Oracle functions don't have direct equivalents in PostgreSQL, you can use the **Help me fix object conversion issues** prompt to get a proposal of code changes that can fix the conversion issue.

The following image shows how to access Gemini prompts for code and schema conversion explainability in conversion workspaces:

![Gemini conversion assistant prompts
      for code and schema conversion explainability.](https://docs.cloud.google.com/static/database-migration/docs/images/prompts_dropdown_csql.png) **Figure 3.** Gemini conversion assistant prompts. (click to enlarge) ![Gemini prompts
      for code and schema conversion explainability.](https://docs.cloud.google.com/static/database-migration/docs/images/prompts_dropdown_csql.png)

### Conversion Quality Assessments

Gemini also helps ensure the quality and functional equivalence of your converted code with quality assessments. These assessments automatically analyze the converted code for correctness and to verify that it behaves the same as your source code.

You can run assessments automatically as part of the conversion process or manually on specific objects. The results provide a detailed quality report, and surface any potential issues, helping you migrate with greater confidence. This feature works in tandem with Auto-conversion and the conversion assistant to provide a more reliable conversion experience.

![Gemini conversion quality report panel in the conversion workspace.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/oracle_gemini_qa_reports.png) **Figure 4.** Example Gemini conversion quality assessment report.(click to enlarge) ![Gemini conversion quality report panel in the conversion workspace.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/oracle_gemini_qa_reports.png)

### Pattern matching

When you fix conversion issues in your workspace, Gemini models can learn the pattern from your fixes and suggest changes to other faulty objects in the workspace. For example, after you've fixed object conversion issues manually or with the conversion assistant prompt, and when Gemini models have analyzed enough of your fixes, you can review AI-generated suggestions to further refine your code.

The following image shows the Gemini suggestions fix issues in conversion workspaces:

![Gemini suggestions fix issues dialog.](https://docs.cloud.google.com/static/database-migration/docs/images/fix_suggestions_dialog_alloy.png) **Figure 5.** Gemini suggestions fix issues dialog. (click to enlarge) ![Gemini suggestions fix issues dialog.](https://docs.cloud.google.com/static/database-migration/docs/images/fix_suggestions_dialog_alloy.png)

## Supported scenarios

See the following pages for more information about Database Migration Service conversion workspaces and Gemini-powered conversion:

Oracle to Cloud SQL for PostgreSQL
    

  * [ About conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/about-conversion-ws)
  * [ Convert Oracle code and schema to Cloud SQL for PostgreSQL with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini)


Oracle to AlloyDB for PostgreSQL
    

  * [ About conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-conversion-ws)
  * [ Convert Oracle code and schema to Cloud SQL for PostgreSQL with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini)


SQL Server to Cloud SQL for PostgreSQL
    

  * [ About conversion workspaces](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces)
  * [ Convert SQL Server code and schema to Cloud SQL for PostgreSQL with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/code-conversion-with-gemini)


SQL Server to AlloyDB for PostgreSQL
    

  * [ About conversion workspaces](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/about-conversion-workspaces)
  * [ Convert SQL Server code and schema to AlloyDB for PostgreSQL with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/code-conversion-with-gemini)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/example-workflow-cw-issues-with-gemini/
title: Example workflow: Fix conversion issues in all code objects with Gemini assistance \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:48.969487+00:00
---

# Example workflow: Fix conversion issues in all code objects with Gemini assistance  |  Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/example-workflow-cw-issues-with-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for AlloyDB ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



Send feedback 

#  Example workflow: Fix conversion issues in all code objects with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

In this example scenario, you convert SQL Server code and schema where multiple code objects use the same SQL Server function that causes conversion issues. The rule-based conversion engine can't find a PostgreSQL equivalent for that function, so you need to fix the conversion issues yourself. To speed up the conversion process, you use Gemini conversion assistance to find out how to change the SQL Server code.

Your SQL code and schema are stored in the region where you create the conversion workspace. If you use assisted code and schema conversion with Gemini models, your code and schemas might be processed in other regions. 

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

In your Gemini-powered workflow, you follow these steps:

  1. You open the details pane for one of the affected objects, and select ![Gemini conversion assistant icon.](https://docs.cloud.google.com/static/database-migration/docs/images/assist_icon.svg)**Assist** > **Help me fix object conversion issues**.

![A screenshot that shows how to access Gemini prompts
      for code and schema conversion explainability.](https://docs.cloud.google.com/static/database-migration/docs/images/prompts_dropdown_sqlserver.png) **Figure 1.** Gemini conversion assistant prompts. (click to enlarge) ![A screenshot that shows how to access Gemini prompts
      for code and schema conversion explainability.](https://docs.cloud.google.com/static/database-migration/docs/images/prompts_dropdown_sqlserver.png)

The Gemini pane opens.

  1. In the Gemini pane, you click **Insert suggestion** and then save SQL changes.

  2. You repeat the steps for every faulty code object.

As you apply the code proposals, Gemini models learn the pattern and offer to add the fix to all objects with the same issue. The **Review suggestions from Gemini** dialog appears.

![Gemini fix issues dialog.](https://docs.cloud.google.com/static/database-migration/docs/images/fix_suggestions_dialog_csql_psql.png) **Figure 2.** Gemini fix issues dialog. (click to enlarge) ![Gemini fix issues dialog.](https://docs.cloud.google.com/static/database-migration/docs/images/fix_suggestions_dialog_csql_psql.png)
  3. You click **Review suggestions** , and proceed to review suggested changes.

  4. For each object, you click **Accept code** and exit the Gemini suggestions view.




Now the conversion issue fix is applied to all faulty code objects in your workspace.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

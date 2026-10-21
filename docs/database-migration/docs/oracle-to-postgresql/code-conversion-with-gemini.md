---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini/
title: Convert Oracle code and schema with Gemini assistance \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:01:04.277086+00:00
---

# Convert Oracle code and schema with Gemini assistance  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)



Send feedback 

#  Convert Oracle code and schema with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service integrates Gemini for Google Cloud into the [ conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/work-with-conversion-workspaces) to help you speed up and improve the conversion process in the following areas:

  * Enhance the deterministic conversion results with  Gemini-powered auto-conversion to use the power of AI to significantly reduce the number of manual adjustments needed in your PostgreSQL code. 

  * Provide code explainability features with the  conversion assistant: a set of dedicated prompts that can help you better understand the conversion logic, propose fixes for conversion issues, or optimize converted code. 
  * Verify converted code with  Gemini quality assessments. Gemini can help analyze the converted code for correctness and functional equivalence with your source code. 
  * Expedite applying fixes for conversion issues with Gemini code conversion suggestions: a mechanism where the Gemini model can learn as you fix conversion issues and suggest changes to other faulty objects in the workspace. 

You can also combine this feature with code explainability for a complete, end-to-end Gemini-powered code object conversion experience. For more information, see [ Example workflow for fixing code objects with conversion issues](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/example-workflow-cw-issues-with-gemini). 




Your SQL code and schema are stored in the region where you create the conversion workspace. If you use assisted code and schema conversion with Gemini models, your code and schemas might be processed in other regions.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Costs

To use Gemini assistance in Database Migration Service conversion workspaces you need to enable Gemini for Google Cloud API. Pricing for Gemini applies. For more information, see [ Gemini for Google Cloud pricing](https://docs.cloud.google.com/products/gemini/pricing).

## Before you begin

To use Gemini-powered features in Database Migration Service, enable Gemini for Google Cloud in your project.

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudaicompanion.googleapis.com)

After you enable Gemini for Google Cloud in your project, you can use all Gemini-powered conversion features in your workspace.

### Required roles

To get the permissions that you need to use Gemini-enhanced conversion features, ask your administrator to grant you the [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) role on your project. 

For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation. 

This predefined role contains the permissions required to use Gemini-enhanced conversion features. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform heterogeneous SQL Server migrations with Database Migration Service: 

  * `datamigration.*`
  * `cloudaicompanion.entitlements.get`



## Use Gemini auto-conversion

When you convert your source schema, Database Migration Service uses the deterministic conversion rules to create the PostgreSQL syntax equivalents. Auto-conversion integrates Gemini-powered corrections on top of the deterministic results to reduce the number of conversion issues and improve conversion quality.

You can perform additional quality and functional equivalence assessments for code objects enhanced with Gemini-powered corrections. For more information, see  Gemini quality assessments.

To use auto-conversion, do the following:

  1. [ Create a new conversion workspace](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace). Make sure you immediately upgrade it to use the latest streamlined experience. 
  2. Go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  3. Enable auto-conversion for your workspace. 
  4. Convert your source code and schema. Click move_down **Convert source**. 

Database Migration Service automatically employs Gemini-powered enhancements in the conversion. You can use the tree view to see which objects are augmented with Gemini: 

![Conversion tree view with Gemini-powered augmentation summary.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/tree_view_gemini_augmentation.png) **Figure 1.** Source schema tree view with Gemini augmentation status. (click to enlarge) ![Conversion tree view with Gemini-powered augmentation summary.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/tree_view_gemini_augmentation.png)
  5. In the tree view, select any augmented object to view the details of enhancements provided by auto-conversion. If you don't like the changes introduced by Gemini, click **Use deterministic code instead** to revert the object to the deterministic conversion results. 

![Gemini-powered auto-conversion panel with details regarding what
               adjustments are implemented to the converted schema.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/auto_conversion_overview_oracle_csql.png) **Figure 2.** Gemini-powered auto-conversion panel where you can inspect the details of code and schema augmentations. (click to enlarge) ![Gemini-powered auto-conversion panel with details regarding what
               adjustments are implemented to the converted schema.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/auto_conversion_overview_oracle_csql.png)



### Enable auto-conversion

If you previously disabled auto-conversion, you can enable it in the Gemini panel:

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Click pen_spark **Gemini**. 

Gemini side panel opens.

  3. Select the **Auto-conversion** checkbox, and click **Save settings**. 

Your conversion workspace will now auto-conversion when you convert your schema. 

  4. Optional: In the **Convert source objects with Gemini?** dialog, click **Convert**. 

Your converted objects aren't modified when you enable auto-conversion. You can [ convert your schema](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/convert-sql) again at a later time. 




### Disable auto-conversion

To disable auto-conversion, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Click pen_spark **Gemini**. 

Gemini side panel opens.

  3. Clear the **Auto-conversion** checkbox, and click **Save settings**. 

Your conversion workspace will now use deterministic code and schema conversion when you convert your schema. 

  4. Optional: In the **Convert source objects?** dialog, click **Convert**. 

Your converted objects aren't modified when you disable auto-conversion. You can convert your schema again at a later time if you want to revert the conversion results to use deterministic conversion rules. 




## Use Gemini conversion assistant

The conversion assistant is a set of dedicated prompts that you can use to gain a better understanding of the object conversion logic, ask for ideas on how to optimize code and remedy your conversion issues, or even add comments to your schema for self-documenting database objects.

![A screenshot that shows how to access Gemini prompts
      for code and schema conversion explainability.](https://docs.cloud.google.com/static/database-migration/docs/images/prompts_dropdown_csql.png) **Figure 1.** Gemini conversion assistant prompts. (click to enlarge) ![A screenshot that shows how to access Gemini prompts
      for code and schema conversion explainability.](https://docs.cloud.google.com/static/database-migration/docs/images/prompts_dropdown_csql.png)

### Enable conversion assistant

Conversion assistant is enabled by default when you enable the Gemini for Google Cloud in your project. If you previously disabled the conversion assistant, you can enable it again in your workspace. To enable conversion assistant, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Click pen_spark **Gemini**. 

Gemini side panel opens.

  3. Select the **Conversion assistance** checkbox, and click **Save settings**. 



### Disable conversion assistant

To disable conversion assistant, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Click pen_spark **Gemini**. 

Gemini side panel opens.

  3. Select the **Conversion assistance** checkbox, and click **Save settings**. 



### Help me fix object conversion issues

The rule-based code and schema conversion engine might sometimes encounter issues when translating objects from Oracle to PostgreSQL. For example, certain Oracle functions might not have direct equivalents in PostgreSQL. You can use the _Help me fix object conversion issues_ prompt to get a proposal of code changes that can fix the conversion issue.

This prompt is only available for [ editable code objects](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/about-conversion-workspaces#editable-objects) that have conversion issues. You can't view this prompt for other types of objects in the conversion workspace.

To use this prompt, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces**.

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. From the list of available conversion workspaces, select the conversion workspace that you want to work with.

The conversion workspace editor opens.

  3. In the **Oracle** panel, select one of your Oracle objects.

  4. In the object details view, select ![Gemini conversion assistant icon.](https://docs.cloud.google.com/static/database-migration/docs/images/assist_icon.svg)**Assist** > **Help me fix object conversion issues**.

A pane with prompt results opens.

  5. Verify the diff screen that shows proposed improvements. If you like the results, you can use the **Insert suggestion** button to update the converted object.

  6. Repeat the steps for every faulty code object. As you apply the code proposals,  Gemini models learn the pattern and can offer suggestions on how to propagate the fixes to all faulty objects in your workspace.




### Explain the conversion logic for this object

With the _Explain the conversion logic for this object_ prompt, you can get a step-by-step explanation of what the converted code does, including a summary of best practices applied in the new code.

To request an explanation of the object conversion logic, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces**.

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. From the list of available conversion workspaces, select the conversion workspace that you want to work with.

The conversion workspace editor opens.

  3. In the **Oracle** panel, select one of your Oracle objects.

  4. In the object details view, select ![Gemini conversion assistant icon.](https://docs.cloud.google.com/static/database-migration/docs/images/assist_icon.svg)**Assist** > **Explain the conversion logic for this object**.

A pane with prompt results opens.




### Help me optimize this code

Sometimes the results of rule-based code and schema conversion can be technically correct, but not fully optimized for PostgreSQL environments. You can use the _Help me optimize this code_ prompt to get a proposal with code optimizations for your database object.

To use this prompt, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces**.

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. From the list of available conversion workspaces, select the conversion workspace that you want to work with.

The conversion workspace editor opens.

  3. In the **Oracle** panel, select one of your Oracle objects.

  4. In the object details view, select ![Gemini conversion assistant icon.](https://docs.cloud.google.com/static/database-migration/docs/images/assist_icon.svg)**Assist** > **Help me optimize this code**.

A pane with prompt results opens.

  5. In the results panel, read the explanation, review the code, and make sure proposal is in line with what you need. If you like the results, you can use the **Insert suggestion** button to update the converted object.




### Add comments to explain the purpose of this object

The _Add comments to explain the purpose of this object_ prompt produces a proposal for code comments that you can add to your database object for self-documenting schema.

To use this prompt, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces**.

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. From the list of available conversion workspaces, select the conversion workspace that you want to work with.

The conversion workspace editor opens.

  3. In the **Oracle** panel, select one of your Oracle objects.

  4. In the object details view, select ![Gemini conversion assistant icon.](https://docs.cloud.google.com/static/database-migration/docs/images/assist_icon.svg)**Assist** > **Add comments to explain the purpose of this object**.

A pane with prompt results opens.

  5. In the results panel, read the explanation, review the code, and make sure proposal is in line with what you need. If you like the results, you can use the **Insert suggestion** button to update the converted object.




## Ensure conversion quality with Gemini quality assessments

Gemini can help you validate the output of code and schema conversion with quality assessments. These assessments focus on verifying the functional equivalence of the converted code (that is, to make sure that PostgreSQL code produces the same results as the source SQL Server code), but the reports also include detailed feedback regarding overall conversion quality. Any issues found with the code are raised as new conversion issues.

![Gemini conversion quality report panel in the conversion workspace.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/oracle_gemini_qa_reports.png)**Figure 3.** Example Gemini conversion quality assessment report. 

You can configure automatic quality assessments for your workspace, or manually run the reports for select objects.

### Enable automatic quality assessments

You can configure your conversion workspace to automatically run Gemini quality assessments on eligible code objects. This feature requires that you also enable  Gemini auto-conversion.

To configure automatic quality assessments, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Click pen_spark **Gemini**. 

Gemini side panel opens.

  3. Select the **Conversion quality assessment** checkbox, and click **Save settings**. 



Now Database Migration Service automatically creates quality assessment reports for your converted objects.

### Run a manual quality assessment report

You can run a quality assessment on demand for any supported code object that was converted with the  Gemini auto-conversion feature.

To run a manual quality assessment:

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. In the conversion workspace editor, use the source panel to select an object whose conversion is augmented with Gemini. 

You can use the `Augmented by Gemini` filter for easier navigation. For more information, see [ Filter objects in the source schema view](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/work-with-conversion-workspaces#filter-objects). 

  3. In the **Conversion details** panel, select the **Quality assessment report** tab, and click **Assess the quality of this code**. 
  4. The assessment runs, and the results are displayed in the **Quality assessment report** tab. 



### Limitations for quality assessments

  * Gemini quality assessments are supported only for objects converted with the  Gemini auto-conversion feature.
  * Schema objects aren't supported by quality assessments.
  * The assessment primarily focuses on functional equivalence and overall quality. The reports don't include performance testing.



## Propagate conversion issue fixes with Gemini code conversion

When you fix conversion issues in your workspace, Gemini models can learn from your fixes and suggest changes to other faulty objects in the workspace. This way you can propagate your fixes to multiple objects without making all edits manually.

### Enable Gemini conversion suggestions

Conversion suggestions are enabled by default when you enable the Gemini for Google Cloud in your project. If you previously disabled this feature, you can enable it again in your workspace. To enable conversion assistant, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Click pen_spark **Gemini**. 

Gemini side panel opens.

  3. Select the **Pattern matching** checkbox, and click **Save settings**. 



### Disable Gemini conversion suggestions

To disable conversion suggestions, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Click pen_spark **Gemini**. 

Gemini side panel opens.

  3. Clear the **Pattern matching** checkbox, and click **Save settings**. 



### View Gemini conversion suggestions in Database Migration Service

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

When you fix object issues (by editing the SQL object's code or applying the code proposed by the  Help me fix object conversion issues prompt), Gemini models analyze your changes. After enough changes are made, Gemini integration displays a prompt and suggests further edits.

**Important:** Gemini models need to analyze the changes you make before they can offer AI suggestions. For highly intricate edits, Gemini models might need to analyze multiple fixes of that issue before it can suggest further changes. Gemini assistance works automatically, you can't activate these suggestions on demand.

To access Gemini suggestions:

  1. In the Google Cloud console, go to **Conversion workspaces**.

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. From the list of available conversion workspaces, select the conversion workspace that you want to work with.

The conversion workspace editor opens.

  3. In the **Oracle** panel, select the object whose generated SQL you want to adjust.

  4. Fix conversion issues that you encounter with the object and save code changes. You can [ edit the code manually](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/work-with-conversion-workspaces#fix-conversion-issues), or use the  Help me fix object conversion issues prompt.

Gemini models analyze your most recent fixes until it can suggest similar updates to other objects with conversion issues. When Gemini models have analyzed enough of your fixes, the **Review suggestions from Gemini** dialog is displayed.

![Gemini fix issues dialog.](https://docs.cloud.google.com/static/database-migration/docs/images/fix_suggestions_dialog_csql_psql.png) **Figure 2.** Gemini fix issues dialog. (click to enlarge) ![Gemini fix issues dialog.](https://docs.cloud.google.com/static/database-migration/docs/images/fix_suggestions_dialog_csql_psql.png)
  5. To view AI-generated suggestions that are based on the changes you made, click **Review suggestions**.




### Review Gemini conversion suggestions

The **Fix issues with Gemini** page displays suggestions generated by Gemini models based on the code changes that you have made. These suggestions contain similar changes that you can apply to other objects. For every suggestion, you can review, change, accept, or ignore the suggestion.

**Important:** Gemini models propose fixes that are based on your existing changes.

The **Fix issues with Gemini** page displays three variants of an object's source code, which you can select in the **Edit view** menu:

  * Original source code (read-only)
  * Draft destination source code (read-only)
  * Destination source code generated with Gemini assistance (editable)



The **Objects** pane contains a list of objects that have issues and fixes suggested by Gemini models.

To review Gemini suggestions, follow these steps:

  1. Click an object to display the related AI-suggested fix.
  2. Review and edit the code that Gemini models suggested.
  3. Do one of the following:

     * To accept the suggestion (including your edits), click **Accept code**. The changes are applied to the object in the conversion workspace, and the object state in the objects list changes from **Pending** to **Accepted**.

     * To keep the suggestion (including your edits) without applying the changes, switch to a different object. The object remains in the **Pending** state. You can edit the code and accept or ignore the suggestion later.

     * To ignore pending or accepted suggestions (and revert your edits), click **Ignore code**. The object state in the objects list changes from **Pending** to **Ignored**. Your changes are reverted. You can edit the code and apply it later.




To close Gemini suggestions and discard all changes that you haven't applied, follow these steps:

  1. On the **Fix issues with Gemini** page, click the back arrow.
  2. In the **Close Gemini** dialog, click **Close**.

The current Gemini session is closed. To go back to the suggestions page,  access Gemini suggestions again.




## What's next

  * See how to work with [ conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/work-with-conversion-workspaces).

  * Read [ Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).

  * Learn [ how Gemini uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

  * Follow the [ sample workflow for fixing conversion issues with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/example-workflow-cw-issues-with-gemini).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

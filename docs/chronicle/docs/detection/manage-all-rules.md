---
url: https://docs.cloud.google.com/chronicle/docs/detection/manage-all-rules/
title: Edit rules in the Rules Editor \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:12:14.845661+00:00
---

# Edit rules in the Rules Editor  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/manage-all-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Edit rules in the Rules Editor

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

The Rules editor in Google Security Operations is the primary interface to create, view, test, and manage your YARA-L detection rules. It provides a dedicated environment for security engineers to author and refine detection logic that identifies threats and suspicious activity in ingested log data.

**Note:** The **Rule editing** window includes an automatic completion feature to show the correct YARA-L syntax for each section of the rule. Use this feature when you create and edit a rule to see automatic recommendations and verify the correct YARA-L syntax.

## Create and edit rules

To open the **Rules editor** , click **Detections > Rules & detections** > the **Rules editor** tab.

### Create a new rule

Rules use the YARA-L 2.0 query language. Before creating a new rule for the first time, see [Get Started: YARA-L 2.0 in SecOps](https://docs.cloud.google.com/chronicle/docs/yara-l/getting-started).

To create a new rule, follow these steps:

  1. In the **Rules editor** , click **New** to open the **Rules editor** window.

The system automatically populates the default rule template and generates a unique name for the rule. Create your new rule in YARA-L.

**Note:** If you're converting a Search query to a rule, include the `nocase` option with the rule filters. The Search web interface sets the default option for **Case sensitivity** to **Off**. Adding the `nocase` option ensures that your rule has the same behavior. For a rule example using the `nocase` option, see [Regular expressions in a rule](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples#regular-expression-queries).
  2. In the **Bind to scope** menu, select the scope to add it to the rule. For more information about adding a scope to a rule, see [data RBAC impact on Rules](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-impact#rules).

  3. Click **Save new rule**.

Google SecOps checks the syntax of your rule. If the rule is valid, it saves and enables the rule automatically. If the rule is invalid, it returns an error.

The run frequency for multi-event rules is automatically set based on the rule's match window:

     * For a window size up to 48 hours, the run frequency defaults to 1 hour (customizable to 10 minutes for match windows under 60 minutes).
     * For a window size greater than 48 hours, the run frequency is automatically set to `match_window / 10`.

For more information, see [Understand rule run scheduling](https://docs.cloud.google.com/chronicle/docs/detection/rule-execution-frequency).

  4. (Optional) To delete the new rule, click **Discard**.

**Note:** Once you save a rule, you can't delete it using the **Rules editor** or the **Rules** dashboard.



### Edit a rule

To edit an existing rule, follow these steps:

  1. Use the **Search rules** field to find an existing rule, or scroll through the rules list. Click a rule in the side panel to view the details in the rule display panel.

  2. Select the rule to edit from the **Rules list**. 

The rule displays in the **Rule editing** window. The rule menu offers the following options for each rule:

     * **Live rule** : Enable or disable the rule.
     * **Duplicate rule** : Make a copy of the rule.
     * **View rule detections** : Open the **Rule Detections** window to display detections captured by this rule.
  3. To update the rule's scope, select the scope from the **Bind to scope** menu. For more information about adding a scope to a rule, see [data RBAC impact on Rules](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-impact#rules).




## View current detections

View information about current detections associated with a rule in one of these ways:

  * Click the rule in the rules list. 

Click **View rule detections** to open **Rule detections** view. This view displays the rule's metadata and a graph showing the number of detections found by the rule over recent days.

  * Click **Edit rule** to open the **Rules editor**.

The **Timeline** tab lists events detected by the rule. Select an event and open the associated raw log or UDM event.

To change the information shown on the **Timeline** tab, click  view_column  **Columns** to open the multicolumn view options. The multicolumn view lets you choose from various categories of log information, including common types, such as `hostname` and `user`, and more specific categories provided by UDM.




## Test your rule

Click **Run test** to test your custom rules. Google SecOps runs the rule on events in the specified time range, generates results, and displays them in the **Test rule results** window.

**Note:** If your rule uses the [`suppression_window` option](https://docs.cloud.google.com/chronicle/docs/yara-l/options-syntax#suppression), this option is not applied when you test the rule using **Run test**. Suppression is a post-processing step that only takes place after detections have been written by a live rule.

Click **Cancel test** at any time to stop the process.

**Note:** Successive executions of the same test rule may generate different test detections and is expected behavior. Google SecOps runs a test rule in multiple parallel processes and detections are streamed to the dashboard as each process finishes. Minor timing differences can affect which duplicate detections are removed. By extension, results may not match those of live rules or retrohunts.**Note:** Test rule detections aren't persisted and don't generate alerts. This behavior allows rule authors to iterate without affecting production. Test rule detections may differ from retrohunt or live rule detections because the evaluation windows may be aligned differently.**Note:** These test results aren't saved and won't be viewable in the **Rules** dashboard.

For more information, see [View rule errors](https://docs.cloud.google.com/chronicle/docs/detection/rule-errors).

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

You can also execute the tests to validate your curated rules.

For community blogs on managing rules, see: [Rules editor navigation](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-SIEM-Rules-Editor-Navigation/ta-p/659309)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

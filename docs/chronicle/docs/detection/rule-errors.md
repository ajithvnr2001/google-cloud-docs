---
url: https://docs.cloud.google.com/chronicle/docs/detection/rule-errors/
title: View and troubleshoot rules \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:14:43.366361+00:00
---

# View and troubleshoot rules  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/rule-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View and troubleshoot rules

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document outlines the two primary categories of errors encountered when working with detection logic: _compilation errors_ and _runtime errors_ :

  * **Compilation errors**: Identify syntax or logic issues through static analysis.
  * **Runtime errors**: Surface specifically during active rule testing, live execution, or the performance of a retrohunt.



## Compilation errors

Google Security Operations identifies compilation errors when you save or test the rule.

Click errorto view error details in the **Runtime Error** dialog.

If there is no error in your rule, the icon is a green  done. If the error message includes a column or line position, that part of the rule is displayed with a red underline in the rules editor. More complex errors don't included a position because they are caused by a combination of issues in multiple places.

If you try to save a rule or test a rule that has a compilation error, a runtime error is displayed. You cannot save a rule or run a test until the compilation error is fixed.

## Runtime errors

Runtime errors don't display during compile time. Some runtime errors prevent a rule from completing, like `query took too long to execute`, which occurs sporadically. To verify if your rule has runtime errors, click **Run test** in the rules editor.

If a runtime error occurs, a link is displayed in the **Test rule results** bar that gives more information about the error that occurred.

It's possible to get unknown runtime errors that don't have a useful description. This indicates that the system is encountering this particular error for the first time and it doesn't have a user message associated with the error. If this happens, contact your Google SecOps representative for assistance.

If a runtime error occurs during live rule or retrohunt execution, a link is displayed on the **Detections** page that gives more information about the error that occurred.

Similarly to test the rule, runtime errors that occur during live rule or retrohunt execution have an indicator with clickable, underlined text that gives more information about the error that occurred.

**Note:** It's possible for runtime errors to go away. This usually occurs because the error was caused by a bug in our system and we reprocessed the failing rules after the bug was fixed.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/looker/docs/lookml-validation/
title: Validating your LookML \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:41.063717+00:00
---

# Validating your LookML  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/lookml-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Validating your LookML Stay organized with collections  Save and categorize content based on your preferences. 

When you edit your LookML, the Looker IDE will alert you to any unresolved syntax errors within a single file (see the [Looker IDE overview](https://docs.cloud.google.com/looker/docs/looker-ide#ad_hoc_error_checking) documentation page).

To perform a full model validation, use the LookML Validator. Some errors, such as an invalid field reference due to a missing join, require a holistic look at the model and therefore are only surfaced when the LookML Validator is run. Be sure to validate your LookML changes before publishing them to the production environment. Although validation won't catch _every_ issue, such as database permission issues, it will prevent most errors.

**Note:** The LookML Validator shouldn't be confused with the [Content Validator](https://docs.cloud.google.com/looker/docs/content-validation), which instead checks to see if the changes you've made will break any saved Looks.

The LookML Validator scans only LookML files that have been updated since the last LookML validation, or files that are affected by updates:

  * If a model-level setting changes, everything is validated again.
  * If a view changes, only the Explores where it is used are validated again.
  * If an Explore changes, only that Explore is validated again.

**Tip:** If you notice that the LookML validation takes a long time to complete, the first thing to check is the [`include`](https://docs.cloud.google.com/looker/docs/reference/param-model-include) parameter in your model file. If you include all your view files (`include: "*.view"`), the LookML Validator will have to check them all, which can affect performance. If this is the case, update the model file's `include` parameter so that only the needed view files are included.

### Running validation

To run the LookML Validator, select the **Validate LookML** button at the top right of the Looker IDE; or select the **Project Health** icon at the top of the IDE to open the **Project Health** panel, and then click the **Validate LookML** icon.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-validate-lookml-2402.png)

After you run the LookML Validator, you may see a list of errors and other warnings that you should address. You can select any arrow to expand the lists of errors or warnings.

![](https://docs.cloud.google.com/static/looker/docs/images/lookml-warnings-expanded-list-720.png)

The validator button in the **Project Health** panel will become available again if you make and save another change.

### Validation messages

Looker displays validation messages after running validation on your LookML.

**Note:** LookML dashboards show informational messages, rather than warnings, in the sidebar when [permissive localization](https://docs.cloud.google.com/looker/docs/model-localization#localization_level) is enabled.

#### No LookML errors found

When there are no issues found by the validator, Looker displays a green checkmark along with the text **No LookML errors found**.

![](https://docs.cloud.google.com/static/looker/docs/images/no-lookml-errors-720.png)

#### LookML errors

LookML errors are issues that could prevent queries from running. The number in parentheses is the number of errors found (nine in the following example):

![Example of a validation message with the text LookML Errors \(9\).](https://docs.cloud.google.com/static/looker/docs/images/lookml-errors-message-720.png)

Within the expanded list of issues you will see the reason validation didn't pass. Often times, if you click on the error, it will bring you directly to the problem row of code. You'll see a red "X" next to the row. Hovering over it will provide more detailed error information in some cases:

![Example of an error that appears upon hover for a type parameter definition with no value, with error text stating that you must provide a value for type.](https://docs.cloud.google.com/static/looker/docs/images/lookml-row-error-720.png)

> **Chat Team Tip** : The validation error we are asked about most is "Unknown or inaccessible field." Visit the [Error: Unknown or inaccessible field](https://docs.cloud.google.com/looker/docs/best-practices/error-unknown-or-inaccessible-field) Best Practices page for the causes and what to do about it.

#### LookML warnings

LookML warnings may not prevent a query from being run, but they may still result in broken or unintended functionality for your users. As with errors, the number in parentheses is the number of warnings found (three warnings in the following example):

![Example of a validation message with the text LookML Warnings \(3\).](https://docs.cloud.google.com/static/looker/docs/images/lookml-warnings-message-720.png)

As with LookML errors, you can expand warnings and jump to the problem code by selecting the warning in the **Project Health** panel and then hovering over the red **X** icon to view more information:

![Example of a warning with text stating that the Explore must match a view name, or that the Explore must have a from or view_name property.](https://docs.cloud.google.com/static/looker/docs/images/lookml-row-warning-712.png)

## Deploying your changes

After you've validated that your changes will work properly, you can use Looker's Git integration to [commit and deploy your changes to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#getting_your_changes_to_production).

**Note:** If you change field names that serve as filters in your Looks or dashboards, be sure to review the **Filters** section of your scheduled Looks and dashboards and update the filters as needed to reflect your changes. If a scheduled content delivery includes filters that no longer function (for example, if the referenced field has changed), the scheduled delivery could expose unfiltered data.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

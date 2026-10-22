---
url: https://docs.cloud.google.com/looker/docs/ci-lookml-validator/
title: Continuous Integration LookML Validator \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:34.552500+00:00
---

# Continuous Integration LookML Validator  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/ci-lookml-validator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Continuous Integration LookML Validator Stay organized with collections  Save and categorize content based on your preferences. 

For LookML projects where all the developers are working in the [Looker IDE](https://docs.cloud.google.com/looker/docs/looker-ide), there is [LookML validation](https://docs.cloud.google.com/looker/docs/lookml-validation) built in to the process of deploying the project to production. But for LookML projects where some or all of your developers are working outside of the Looker IDE, using an external IDE like VSCode or Vim to write LookML, it is possible to deploy the project to production without ever validating your LookML syntax. In this case, you can run the Continuous Integration (CI) LookML Validator to find syntax issues with your LookML, such as a missing `}` or an invalid `${}` reference.

See the LookML Validator options section of this page for details on the options that you can configure when you [create or edit a CI suite](https://docs.cloud.google.com/looker/docs/ci-create-suite). For information on running the LookML Validator, see the [Running Continuous Integration suites](https://docs.cloud.google.com/looker/docs/ci-run-suite) documentation page.

In the [run results page](https://docs.cloud.google.com/looker/docs/ci-view-results), the LookML Validator provides the LookML errors in your project, along with a link to the LookML:

![Continuous Integration results page showing LookML Validator findings](https://docs.cloud.google.com/static/looker/docs/images/ci-lookml-results-2506.png)

## LookML Validator options

The following sections describe the options for running the LookML Validator:

  * Setting a severity threshold
  * Timeout



### Setting a severity threshold

The severity level setting determines the lowest severity level of LookML message that will cause the CI run to show a **Failed** CI [status](https://docs.cloud.google.com/looker/docs/ci-view-results#status) on the [CI **Runs** page](https://docs.cloud.google.com/looker/docs/ci-view-results) and the [CI run results page](https://docs.cloud.google.com/looker/docs/ci-view-results#ci-run-results).

In the Looker IDE, LookML validation returns syntax messages at three levels of severity: info, [warning](https://docs.cloud.google.com/looker/docs/lookml-validation#lookml_warnings), and [error](https://docs.cloud.google.com/looker/docs/lookml-validation#lookml_errors).

By default, the LookML Validator will cause a **Failed** CI status only if the LookML Validator finds LookML warnings or errors in the LookML project. You can select the lowest-level message severity for which the CI LookML Validator should return a **Failed** result:

  * **Error** : The CI LookML Validator will return a **Failed** result if the LookML validation returns an error message.
  * **Warning** : The CI LookML Validator will return a **Failed** result if the LookML validation returns a warning or an error message.
  * **Info** : The CI LookML Validator will return a **Failed** result if the LookML validation returns an info, a warning, or an error message.



This severity threshold affects only the CI run status value. Regardless of the severity level setting, the LookML Validator results will show all syntax issues and display all the LookML syntax messages on the CI run results page. 

### Timeout

You can specify the number of seconds that the CI LookML Validator should run before timing out (the default is 600 seconds). If the CI LookML Validator takes longer than the timeout duration, the validation will abandon the job and return an **Error** run status. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

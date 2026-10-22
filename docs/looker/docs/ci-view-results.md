---
url: https://docs.cloud.google.com/looker/docs/ci-view-results/
title: Viewing the results of a CI run \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:46.056918+00:00
---

# Viewing the results of a CI run  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/ci-view-results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Viewing the results of a CI run Stay organized with collections  Save and categorize content based on your preferences. 

With Looker Continuous Integration (CI), if you manually trigger a [new run of a suite](https://docs.cloud.google.com/looker/docs/ci-run-suite#manual-run) or a [rerun of a previous CI run](https://docs.cloud.google.com/looker/docs/ci-run-suite#manual-rerun), the Looker IDE automatically displays the run results page for the manual run. Otherwise, no matter how a run is triggered, a Looker user with the [`see_ci`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_ci) permission can access the run results from the **Runs** page in the Looker IDE:

![Continuous Integration Runs page showing a table with previous CI runs](https://docs.cloud.google.com/static/looker/docs/images/ci-runs-page-2506.png)

The **Runs** page lists the CI runs for the LookML project, along with the following information:

  * **Status** : The status of the run: 
    * **Queued** : The run is waiting for another CI run to be completed before starting.
    * **Running** : The validators defined by the CI suite are running.
    * **Passed** : All of the validators in the CI suite were completed successfully and none of the validators returned an error.
    * **Failed** : All of the validators in the CI suite were completed successfully and at least one of the validators returned an error.
    * **Error** : One or more of the validators in the CI suite failed to run.
    * **Cancelled** : The CI run was cancelled.
  * **Suite** : The name of the CI suite.
  * **Trigger** : How the suite was triggered (manual, pull request, schedule, or API).
  * **Git state** : Information about the branch or commit that was validated in the run: 
    * For manual runs, the value is either "Production" or the name of the development branch.
    * For runs triggered by a schedule, the value is always "Production."
    * For runs triggered by a pull request, the value is a hyperlink to the commit SHA of the pull request. Click the commit SHA hyperlink to open the pull request in another browser tab.
  * **Triggered at** : The time that the CI run was initiated.



## CI run results

On the **Runs** page, click the **View Run** button for a CI run to see its validation results:

![Continuous Integration Runs result page showing the results of a CI run](https://docs.cloud.google.com/static/looker/docs/images/ci-results-2506.png)

The run results page for a CI suite shows the following information:

  1. The LookML project and Git details that the run validated (and the commit, for runs triggered by a pull request).
  2. Information about the CI run: 
     * How and when the run was triggered.
     * The Looker user who initiated the run (for manual runs) or the branch and commit (for runs triggered by a pull request).
     * How long it took the CI run to be completed.
     * How long the run was waiting in the queue before beginning.
  3. For validators that return errors, the results page shows each error, along with the error message and links to the LookML, Explore, or content so that you can test and correct each error.
  4. For validators that found no errors, the results page shows a success message.



### Viewing results for incremental validation

For CI validator runs configured for incremental validation (for the [SQL Validator](https://docs.cloud.google.com/looker/docs/ci-sql-validator#incremental_validation) or the [Content Validator](https://docs.cloud.google.com/looker/docs/ci-content-validator#incremental_validation)), the validator will return errors that exist only on the development branch or pull request commit; validators enabled for incremental validation won't return an error if the error already exists in the production version.

The following is an example of a results page for an incremental validation of the SQL Validator:

![Continuous Integration Runs result page showing the results of an incremental SQL Validator run](https://docs.cloud.google.com/static/looker/docs/images/ci-results-incremental-2506.png)

  1. The results page shows errors that exist only in the development branch or commit.
  2. If an Explore has no changes in the development branch or commit, the validator will skip the Explore during validation. These Explores are marked with "Skipped" in the validator results.
  3. The validators that were run incrementally are marked with "Incremental" in the validation results.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

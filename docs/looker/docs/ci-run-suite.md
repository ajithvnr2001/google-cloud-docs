---
url: https://docs.cloud.google.com/looker/docs/ci-run-suite/
title: Running Continuous Integration suites \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:29.235266+00:00
---

# Running Continuous Integration suites  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/ci-run-suite/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Running Continuous Integration suites Stay organized with collections  Save and categorize content based on your preferences. 

Continuous Integration (CI) runs can be triggered in several ways:

  * Automatically when a pull request is submitted to your LookML project's repository by a Looker developer (see the [Creating a Continuous Integration suite](https://docs.cloud.google.com/looker/docs/ci-create-suite#pr-trigger) page for information on setting this up).
  * Automatically when a dbt Cloud CI job finishes (see the [Creating a Continuous Integration suite](https://docs.cloud.google.com/looker/docs/ci-create-suite#dbt-trigger) page for information on setting this up).
  * Automatically on a recurring schedule (see the [Creating a Continuous Integration suite](https://docs.cloud.google.com/looker/docs/ci-create-suite#schedule-trigger) page for information on setting this up).
  * Manually triggering a new run of a CI suite from the Looker IDE.
  * Manually re-running a previous CI run from the Looker IDE.



Once the validation tests have completed, you can review the results, as described on the [Viewing Continuous Integration run results](https://docs.cloud.google.com/looker/docs/ci-view-results) documentation page.

## Automatic triggering from pull requests

If you've enabled your CI suite with [**Trigger on pull requests from Looker**](https://docs.cloud.google.com/looker/docs/ci-create-suite#triggers), CI will trigger a validation run automatically when a Looker developer submits a pull request to your LookML repository. (You can optionally specify that pull requests only to [certain branches in your repository](https://docs.cloud.google.com/looker/docs/ci-create-suite#target-branches) should trigger automatic CI runs.)

For automatic pull request validation runs, CI validates the latest pull request commit and returns all of the errors in that version of the repository.

**Note:** For validators in the CI suite that are configured to perform incremental validation, the validator will return errors that exist only on the pull request commit itself; validators enabled for incremental validation won't return an error if it already exists in the production version. See the [SQL Validator](https://docs.cloud.google.com/looker/docs/ci-sql-validator#incremental_validation) or [Content Validator](https://docs.cloud.google.com/looker/docs/ci-content-validator#incremental_validation) documentation for more information on incremental validation.

See the [Viewing Continuous Integration run results](https://docs.cloud.google.com/looker/docs/ci-view-results) documentation page for information on viewing the results.

## Automatic triggering from dbt Cloud

If you have enabled your CI suite with [**Trigger on pull requests from dbt Cloud**](https://docs.cloud.google.com/looker/docs/ci-create-suite#dbt-trigger), CI will trigger a validation run automatically when the specified dbt Cloud CI job finishes.

A CI run triggered by a dbt Cloud CI job is designed to check if schema changes made in dbt will break LookML content. During the run, Looker performs the following actions:

  1. Receives the notification from dbt Cloud upon job completion.
  2. Extracts the details of the temporary schema created by dbt Cloud for that specific run.
  3. Overrides the configured User Attribute (for example, the schema attribute for your connection) with the name of this temporary schema.
  4. Executes the CI validators against this temporary schema.



This lets you catch breaking changes (like dropped columns or renamed tables) before the dbt changes are merged to production. Once the run finishes, the user attribute value reverts to its standard value for the CI users.

## Automatic triggering on a schedule

If you've enabled your CI suite with [**Trigger on a schedule**](https://docs.cloud.google.com/looker/docs/ci-create-suite#triggers), CI will trigger a validation run automatically on the schedule that you specify.

For automatic scheduled validation runs, CI validates the production version of the repository and returns all of the errors in that version.

See the [Viewing Continuous Integration run results](https://docs.cloud.google.com/looker/docs/ci-view-results) documentation page for information on viewing the results.

## Manually triggering a new run of a CI suite

A Looker user with the [`see_ci`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_ci) permission can manually trigger a CI run from the Looker IDE.

To manually trigger a new run of a CI suite, follow these steps:

  1. From the [Looker IDE](https://docs.cloud.google.com/looker/docs/looker-ide), click the **Continuous Integration** icon from the IDE navigation bar.
  2. Click **Suites** to open the **Suites** page.
  3. Click the **Run suite** button for the CI suite that you want to run (if you don't have any CI suites for your project, you can [create a CI suite](https://docs.cloud.google.com/looker/docs/ci-create-suite)).
  4. In the **Trigger a run manually** dialog, use the **Workspace** options to select the branch that you want to validate (see the Workspace section for details):

     * To validate the production version of your LookML project, click **Production**.
     * If you want to validate a development branch of your LookML project, click **Dev Mode**. Use the **Branch** pull-down menu to select which development branch to validate.
  5. To trigger the run of the CI suite, click **Start run**.




The CI suite may take several minutes to complete running, depending on the size of your project, the validators that are included in the CI suite, and the configuration of the CI suite.

After you trigger a run, the Looker IDE will display the **Run** page for the suite that you triggered. Once the validation tests are completed, the **Run** page will show the results for each of the validators. You can navigate away from the **Run** page while the validation tests are running, and then later return to the **Run** page to see the results.

**Tip:** You can also [set up alerting](https://docs.cloud.google.com/looker/docs/ci-create-suite#alerting) for your CI suite to receive email notifications when a CI run fails, errors, passes, or is cancelled, instead of having to check the **Runs** page.

See the [Viewing Continuous Integration run results](https://docs.cloud.google.com/looker/docs/ci-view-results) documentation page for information on viewing the results.

### Workspace

When you manually trigger a CI run, you can use the **Workspace** options to validate either the production version of your repository or a development branch of your repository.

For the **Production** option, if you want to identify which branch or commit is used for the production version, you can look in the Looker IDE in the **Default Production Branch** field of the **Git Summary** section of the [**Branch Management**](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#managing_git_branches) page of the **Project Settings** :

  * For projects configured with [advanced deploy mode](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode), the production version is a commit or tag that is selected in the [deployment manager](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode#deployment_manager) by a Looker developer who has the [`deploy` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#deploy).
  * For projects without advanced deploy mode, the production version is the branch configured in the **Git Production Branch Name** field in the **Project Configuration** page of the [**Project Settings**](https://docs.cloud.google.com/looker/docs/git-options#project_settings).



For the **Dev Mode** option, note the following for validating development branches in your project:

  * To see the branches in your LookML project and to identify the production branch and the personal branches of your developers, refer to the [**Branch Management**](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#managing_git_branches) page of the **Project Settings** of your project in the Looker IDE.
  * To validate a development branch, the development branch must be pushed to your LookML repository. In the Looker IDE, that means the developer must click the [**Commit Changes & Push**](https://docs.cloud.google.com/looker/docs/git-command-reference#commit) button or select the **Commit** option from the [Git Actions panel](https://docs.cloud.google.com/looker/docs/git-command-reference) in the IDE.



## Manually re-running a previous CI run

For runs that have finished (if the run passed, failed, errored, or was cancelled), a Looker user with the [`see_ci`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_ci) permission can manually trigger a rerun of the CI run from the Looker IDE:

  * If you rerun a PR-triggered run, Continuous Integration runs against the same commit as the original run.
  * If you rerun a manually-triggered run, Continuous Integration runs against the production state or branch HEAD _at the time of the rerun_ , which will include any subsequents commits that were made since the initial CI run.



In addition, if you have edited the CI suite since the initial run, a rerun will include any changes that you made to the CI suite since the initial run.

To rerun a CI run, follow these steps:

  1. From the [Looker IDE](https://docs.cloud.google.com/looker/docs/looker-ide), click the **Continuous Integration** icon from the IDE navigation bar.
  2. Click **Runs** to open the **Runs** page.
  3. On the **Runs** page, click the **View Run** button for the CI run you want to cancel.
  4. On the run results page for the selected run, click the **Rerun** button at the top of the page.



Once you click **Rerun** , the Content Validator will initiate the run and return you to the **Run** page for the new run.

See the [Viewing Continuous Integration run results](https://docs.cloud.google.com/looker/docs/ci-view-results) documentation page for information on viewing the results.

## Cancelling a CI run

If you want to cancel a CI run that is running, you can do so from its **Run** page by following these steps:

  1. From the [Looker IDE](https://docs.cloud.google.com/looker/docs/looker-ide), click the **Continuous Integration** icon from the IDE navigation bar.
  2. Click **Runs** to open the **Runs** page.
  3. On the **Runs** page, click the **View Run** button for the CI run you want to cancel.
  4. On the **Run** page for the selected run, click the **Cancel** button at the top of the page.



Once you click **Cancel** , Continuous Integration will cancel the run display the **Cancelled** status on the **Run** page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

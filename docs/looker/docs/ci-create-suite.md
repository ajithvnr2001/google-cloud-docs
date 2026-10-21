---
url: https://docs.cloud.google.com/looker/docs/ci-create-suite/
title: Creating a Continuous Integration suite \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:48.090839+00:00
---

# Creating a Continuous Integration suite  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/ci-create-suite/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Creating a Continuous Integration suite Stay organized with collections  Save and categorize content based on your preferences. 

A Continuous Integration (CI) suite is a set of validation instructions that is associated with your LookML project. A Looker user with the [`manage_ci`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_ci) permission can configure the following in a CI suite:

  * How a CI validation run is triggered ([manually from the Looker IDE](https://docs.cloud.google.com/looker/docs/ci-run-suite#manual-run) or [automatically when a pull request is submitted to your repository](https://docs.cloud.google.com/looker/docs/ci-run-suite#pr-run)).
  * Which CI validators to run.
  * Additional options for each validation test. See the documentation pages for each of the validators for details: 
    * [SQL Validator](https://docs.cloud.google.com/looker/docs/ci-sql-validator)
    * [Assert Validator](https://docs.cloud.google.com/looker/docs/ci-assert-validator)
    * [Content Validator](https://docs.cloud.google.com/looker/docs/ci-content-validator)
    * [LookML Validator](https://docs.cloud.google.com/looker/docs/ci-lookml-validator)
    * [Style Validator](https://docs.cloud.google.com/looker/docs/ci-style-validator)



## Before you begin

Before you can create a CI suite, you need the following:

  * A Looker instance that meets the [requirements for CI](https://docs.cloud.google.com/looker/docs/continuous-integration#requirements) and that is [enabled for CI](https://docs.cloud.google.com/looker/docs/continuous-integration#enable-ci).
  * A Looker user account with the [`manage_ci`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_ci) permission (this permission is included in the Admin [permission set](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission_sets)).
  * A LookML project with at least one commit that has been deployed to production. CI background services can retrieve the project's Git configuration only if the project is in [Production Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode). If the project only exists in Development Mode, CI will return errors when configuring webhook triggers.



## Creating a CI suite

You can configure and run the validators on the **Suites** page in the Looker IDE:

![CI suites page](https://docs.cloud.google.com/static/looker/docs/images/ci-suites-page-updated-2506.png)

To create a CI suite, follow these steps:

  1. From the [Looker IDE](https://docs.cloud.google.com/looker/docs/looker-ide), click the **Continuous Integration** icon from the IDE navigation bar.
  2. Click the **Suites** tab to open the **Suites** page.
  3. On the **Suites** page, you can create a new suite or edit an existing suite: 
     * To create a new suite, click the **Create suite** button.
     * To edit an existing suite, click the **Edit suite** button for the suite.
  4. Enter a name for the **Suite name**. If you are editing an existing suite, you can optionally click the pencil icon to edit the suite name.
  5. (Optional) Enable the **Trigger on a schedule** toggle if you want to set up automatic validation testing on a recurring schedule. See the Trigger on a schedule section of this page for more information.
  6. (Optional) Enable the **Trigger on pull requests from Looker** toggle if you want to set up automatic validation testing whenever a Looker developer submits a pull request to your repository. See the Trigger on pull requests from Looker section of this page for more information.

If you enable pull request triggering for a CI suite, you can optionally use the **Only for target branch** field to specify that pull requests only to specific branches in the repository should trigger a run of the CI suite. See the Trigger on pull requests from Looker section of this page for more information.

  7. (Optional) Turn on the **Trigger on pull requests from dbt Cloud** toggle if you want to set up automatic validation testing whenever a [dbt Cloud CI job](https://docs.getdbt.com/docs/deploy/continuous-integration?version=2.0) is run. See the Trigger on pull requests from dbt Cloud section of this page for more information.

  8. (Optional) Turn on the **Enable email alerts** toggle if you want to receive email alerts based on the status of a CI run. See the Set up alerting section of this page for more information.

  9. Optionally, enable the validator toggles to turn on a validator and configure its options. See the documentation pages for each of the validators for details:

     * [SQL Validator](https://docs.cloud.google.com/looker/docs/ci-sql-validator)
     * [Assert Validator](https://docs.cloud.google.com/looker/docs/ci-assert-validator)
     * [Content Validator](https://docs.cloud.google.com/looker/docs/ci-content-validator)
     * [LookML Validator](https://docs.cloud.google.com/looker/docs/ci-lookml-validator)
     * [Style Validator](https://docs.cloud.google.com/looker/docs/ci-style-validator)
  10. Save your changes:

     * If you're creating a new suite, click the **Create suite** button.
     * If you're editing an existing suite, click the **Update suite** button.



### Triggers

CI runs can be triggered in several ways:

  * Automatically, on a recurring schedule.
  * Automatically, when a pull request is submitted to your LookML project's repository by a Looker developer.
  * Automatically, when a dbt Cloud CI job creates a pull request.
  * Manually, [using the **Run suite** button](https://docs.cloud.google.com/looker/docs/ci-run-suite#manual-run) on the **Suites** page in the Looker IDE.
  * Manually, by [rerunning a previous CI run](https://docs.cloud.google.com/looker/docs/ci-run-suite#manual-rerun), from the **Runs** page of the Looker IDE.



#### Trigger on a schedule

You can configure a CI suite to automatically trigger on a schedule by enabling the **Trigger on a schedule** toggle.

When this toggle is enabled, you can select the frequency and specifics for automatically running your CI suite:

  * **Monthly** , on a specific day and time
  * **Weekly** , on a specific day and time
  * **Daily** , at a specific time
  * **Hourly** or every 2, 3, 4, 6, 8, or 12 hours, starting and ending at specific times of the day
  * **Minutes** every 5, 10, 15, 20, or 30 minutes, starting and ending at specific times of the day
  * **Specific months** of the year, on a specific day and time
  * **Specific days** of the week at a specific time



#### Trigger on pull requests from Looker

To configure a CI suite for automatic triggering on pull request, enable the **Trigger on pull requests from Looker** toggle. To use pull request triggering, your Git repository must be configured by your Looker admin on the [**Continuous Integration** Admin](https://docs.cloud.google.com/looker/docs/admin-panel-platform-ci#github) page of Looker).

**Tip:** Even if you configure the CI suite to run automatically on pull requests, you can still initiate a [manual run](https://docs.cloud.google.com/looker/docs/ci-run-suite#manual-run) or [manually rerun a previous run](https://docs.cloud.google.com/looker/docs/ci-run-suite#manual-rerun) of the CI suite from the Looker IDE.

If you enable pull request triggers for a CI suite, you can optionally specify that pull requests only to specific branches in the repository should trigger a run of the CI suite. To limit automatic pull request triggers of CI runs to specific branches in your repository, enter a comma-separated list of the branches in the **Only for target branch** field.

For example, if a repository has three branches named `main`, `release_1`, and `dev`, you can enter `main, release_1` in the **Only for target branch** field. This means that CI runs will be triggered when a Looker developer submits a pull request to either the `main` or the `release_1` branch. If a Looker developer submits a pull request to the `dev` branch, this won't trigger an automatic run of the CI suite.

#### Trigger on pull requests from dbt Cloud

If you've configured the [dbt Cloud integration](https://docs.cloud.google.com/looker/docs/admin-panel-platform-ci#dbt-cloud) on your instance, you can configure a CI suite to trigger automatically when a dbt Cloud CI job finishes. The CI suite verifies whether changes in your dbt models will cause SQL errors in your Looker Explores before the dbt changes are deployed.

**Note:** For [Looker (Google Cloud core) instances](https://docs.cloud.google.com/looker/docs/looker-core-overview) that use [private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) or [hybrid connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private-ip-public-ip) with [Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psc), or for instances within a [VPC Service Controls perimeter](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc), you must update your networking configuration to allow ingress and egress traffic to and from your dbt Cloud host URL. For more information, see the [dbt Cloud Configuration](https://docs.cloud.google.com/looker/docs/admin-panel-platform-ci#dbt-cloud) section on the Admin settings - Continuous Integration page.

To configure this trigger, enable the **Trigger on pull requests from dbt Cloud** toggle when creating or editing a CI suite.

When you've enabled this trigger, configure the following options:

  * **dbt Cloud Job** : Select the dbt Cloud CI job from the drop-down field that should trigger this suite.

**Note:** Only CI job types are supported and displayed in this drop-down. Manual dbt Cloud runs aren't supported.
  * **Schema user attribute** : Select the Looker user attribute that holds the schema name for your database connection. Only user attributes that have been [enabled for CI in the **Admin** panel](https://docs.cloud.google.com/looker/docs/admin-panel-platform-ci#user-attributes) will appear in this list.




When you save the suite with this trigger enabled, Looker automatically registers a webhook in your dbt Cloud account to listen for job completions.

For dbt Cloud-triggered runs, Looker dynamically identifies the temporary schema created by the dbt Cloud run and overrides the selected user attribute with this temporary schema name for the duration of the CI run.

**Note:** CI runs that are triggered by dbt Cloud CI jobs run against the production LookML branch. Therefore, Content Validator, LookML Validator, and Style Validator runs that are triggered by dbt Cloud CI jobs won't test for errors on development branches.

## Set up alerting

To receive email alerts based on the status of your CI runs, you can set up alerting for a CI suite. This lets you monitor Continuous Integration runs without having to consult the **Runs** page in the Looker IDE.

To configure email alerts for a CI suite, follow these steps when creating or editing a CI suite:

  1. Enable the **Enable email alerts** toggle.
  2. In the **Email addresses** field, enter a comma-separated list of the email addresses that should receive the alerts.
  3. Use the checkboxes to select the job statuses that should trigger an alert: 
     * **Failed** : Triggers an email when a CI run fails validation tests.
     * **Error** : Triggers an email when a CI run encounters a system or configuration error.
     * **Passed** : Triggers an email when a CI run completes successfully.
     * **Cancelled** : Triggers an email when a CI run is cancelled.



## Deleting a suite

To delete a CI suite, perform the following steps:

  1. From the [Looker IDE](https://docs.cloud.google.com/looker/docs/looker-ide), click the **Continuous Integration** icon from the IDE navigation bar.
  2. Click the **Suites** tab to open the **Suites** page.
  3. On the **Suites** page, click the **Edit suite** button for the suite.
  4. On the suite's page, click the **Delete suite** button.
  5. In the confirmation dialog, click the **Delete suite** button.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

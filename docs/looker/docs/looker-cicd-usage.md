---
url: https://docs.cloud.google.com/looker/docs/looker-cicd-usage/
title: Multi-tier Looker CI/CD usage and workflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:55.189556+00:00
---

# Multi-tier Looker CI/CD usage and workflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-cicd-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Multi-tier Looker CI/CD usage and workflow Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This guide explains how to operate a multi-tier continuous delivery (CD) pipeline across multiple Looker instances. For automated testing and validation within your LookML projects, see [Looker Continuous Integration](https://docs.cloud.google.com/looker/docs/continuous-integration).

This page explains how to use a multi-tier CI/CD workflow in Looker after such a workflow has been [installed and configured](https://docs.cloud.google.com/looker/docs/looker-cicd-installation).

These instructions use a three-tier system that comprises development, QA, and production. However, you can apply the same principles to a two-tier or four-tier system.

These instructions also assume the use of GitHub as your Git provider. You _can_ use other Git providers to create a CI/CD workflow; however, you must possess the expertise to modify these instructions for your provider.

## Workflow overview

LookML developers begin by writing code in their development branch, which is normally named something like `dev-my-user-ydnv`, test their changes with [Looker Continuous Integration](https://docs.cloud.google.com/looker/docs/continuous-integration) (or by [manually running a CI suite](https://docs.cloud.google.com/looker/docs/ci-run-suite#manual-run)), and commit their code. Finally, they open a pull request to merge their code with the `main` branch.

When the pull request is opened, it brings the developer to GitHub. The developer should write a meaningful PR title by using conventional commits style and add a comment to the description that will be included in the changelog. If [pull request triggering](https://docs.cloud.google.com/looker/docs/ci-create-suite#pr-trigger) is configured, Looker Continuous Integration automatically validates the pull request, and developers can [view the results](https://docs.cloud.google.com/looker/docs/ci-view-results) in Looker or in GitHub.

Next, the developer should select a reviewer in GitHub. The reviewer will receive a notification and can add their review to the PR. If the reviewer approves the change, the PR is merged with the `main` branch. A WebHook is called and the development environment now sees the change.

Automatically, the [Release Please automation](https://docs.cloud.google.com/looker/docs/looker-cicd-installation#release_please) will run and open a second PR to create a new tagged release. Or, if there is already a PR open for this purpose, Release Please updates that PR. The release PR has a version number associated with it, as well as a changelog that includes the titles and descriptions of the included changes.

When the Release Please generated PR is approved and merged, a new version tag is generated and the changelog is merged with the `main` branch. The QA and production instances of Looker can select this version using [Advanced Deploy Mode](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode).

## Best practices for numbering releases and naming commits

The releases and their associated tags can be named and numbered in any way that makes sense in your environment. However, [Semantic Versioning](https://semver.org/) is used here, and is highly suggested because it works well with the [Release Please plugin](https://docs.cloud.google.com/looker/docs/looker-cicd-installation#release_please).

In Semantic Versioning the version consists of three numbers separated by periods: `MAJOR.MINOR.PATCH`

  * `PATCH` is incremented every time a release fixes a bug
  * `MINOR` is incremented and `PATCH` is set back to zero every time the release adds or refines a feature while being backward compatible
  * `MAJOR` is incremented and both `MINOR` and `PATCH` are set to zero when a feature is added that is _not_ backward compatible



[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) is a system of naming commits by the impact they have on end users. While not required, the use of conventional commit naming is also useful for the Release Please plugin.

In conventional commit naming, each commit message is prepended with an indicator of the scope of the change:

  * A bug fix is indicated with `fix:` like `fix: set proper currency symbol on sale_amt format`
  * A new feature is indicated with `feat:` like `feat: added explore for sales by territory`
  * A feature with a breaking change is indicated by `feat!:` like `feat!: rewrote sales explore to use the new calendar view`
  * When documentation is updated, but LookML is not changed, the commit message starts with `doc:`



If conventional commits are used consistently, determining the semantic number to be used next is generally straightforward. If the commit log only consists of `fix:` and `doc:` commits, the `PATCH` should be incremented. If there is a `feat:` commit then `MINOR` should be incremented. If there is a `feat!:` then `MAJOR` should be incremented. The Release Please plugin can even generate a CHANGELOG file and tag the release automatically.

## Using Advanced Deploy Mode

After changes are made and submitted as a PR on the development instance the [Release Please plugin](https://docs.cloud.google.com/looker/docs/looker-cicd-installation#release_please) will tag the changes with a version tag like `v1.2.3`. Looker's [Advanced Deploy Mode](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode) then makes these versions available in the Looker UI for the QA and production instances.

To deploy a change, choose the Deployment Manager from the Looker IDE:

![Looker Deployment Manager location in IDE.](https://docs.cloud.google.com/static/looker/docs/images/cicd-deployment-manager.png)

Click the **Select Commit** link in the upper right of the Deployment Manager. Next, select the three-dot menu that is associated with the tag that you want to deploy, and choose **Deploy to Environment** :

![Looker Deployment Manager UI for deploying to environment.](https://docs.cloud.google.com/static/looker/docs/images/cicd-deployment-mgr-a.png)

You don't need to tag the deployment again, so choose **Deploy without tagging** and press the **Deploy to Environment** button:

![Looker Deployment Manager UI for deploying without tagging.](https://docs.cloud.google.com/static/looker/docs/images/cicd-deployment-mgr-b.png)

Finally, push to production using the Deployment Manager.

## Using Looker Continuous Integration

To verify changes in a development branch or as part of a pull request, developers can use [Looker Continuous Integration](https://docs.cloud.google.com/looker/docs/continuous-integration). Continuous Integration provides the following validators:

  * [SQL Validator](https://docs.cloud.google.com/looker/docs/ci-sql-validator) — Verifies that the dimensions in your Explores run correctly against your database.
  * [Assert Validator](https://docs.cloud.google.com/looker/docs/ci-assert-validator) — Runs any LookML [data tests](https://docs.cloud.google.com/looker/docs/reference/param-model-test) that were created by your Looker developers and returns all failures and errors.
  * [Content Validator](https://docs.cloud.google.com/looker/docs/ci-content-validator) — Runs the Looker [content validation](https://docs.cloud.google.com/looker/docs/content-validation) to test for errors in the Looks and dashboards in your LookML project.
  * [LookML Validator](https://docs.cloud.google.com/looker/docs/ci-lookml-validator) — Runs the [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation) to test for LookML errors in the project.
  * [Style Validator](https://docs.cloud.google.com/looker/docs/ci-style-validator) — Enforces LookML coding standards, naming conventions, and structural best practices across your project.



You can group these validators into [Continuous Integration suites](https://docs.cloud.google.com/looker/docs/ci-create-suite) and run them [automatically on pull requests, on a schedule, or manually](https://docs.cloud.google.com/looker/docs/ci-run-suite).

### SQL Validator

The Continuous Integration SQL Validator verifies that the dimensions in your Explores run correctly against your database. It tests whether fields that are defined in LookML Views correspond to valid SQL columns or expressions in the database.

The SQL Validator has the following key capabilities:

  * Runs queries with `LIMIT 0` and `WHERE 1=2` clauses to validate SQL without incurring data-scanning costs.
  * Supports [incremental validation](https://docs.cloud.google.com/looker/docs/ci-sql-validator#incremental_validation) to test only the Explores that changed in the development branch.
  * Scopes validation to [specific Explores to query](https://docs.cloud.google.com/looker/docs/ci-sql-validator#explores-to-query) or [exclude](https://docs.cloud.google.com/looker/docs/ci-sql-validator#explores-to-exclude).
  * Excludes specific dimensions from validation by using [LookML tags or SQL comments](https://docs.cloud.google.com/looker/docs/ci-sql-validator#exclude-dimensions) (`tags: ["ci: ignore"]` or `-- ci: ignore`).



For more information and configuration options, see the [Continuous Integration SQL Validator](https://docs.cloud.google.com/looker/docs/ci-sql-validator) documentation page.

### LookML Validator

The Continuous Integration LookML Validator checks your LookML project for syntax errors, such as missing brackets or invalid field references. This validator is especially helpful for developers who write LookML outside the Looker IDE.

The LookML Validator has the following key capabilities:

  * Lets you set a [severity threshold](https://docs.cloud.google.com/looker/docs/ci-lookml-validator#setting_a_severity_threshold) (Error, Warning, or Info) that determines what message severity level causes a run to fail.
  * Lets you configure a [timeout](https://docs.cloud.google.com/looker/docs/ci-lookml-validator#timeout) duration for validation runs.



For more information and configuration options, see the [Continuous Integration LookML Validator](https://docs.cloud.google.com/looker/docs/ci-lookml-validator) documentation page.

### Content Validator

The Continuous Integration Content Validator verifies that saved content, such as Looks and user-defined dashboards (UDDs), still functions properly after LookML changes are made.

The Content Validator has the following key capabilities:

  * Scopes validation to [specific content folders](https://docs.cloud.google.com/looker/docs/ci-content-validator#folders-validate) or [Explores](https://docs.cloud.google.com/looker/docs/ci-content-validator#explores-to-query).
  * Excludes content in [personal folders](https://docs.cloud.google.com/looker/docs/ci-content-validator#exclude-personal-folders).
  * Supports [incremental validation](https://docs.cloud.google.com/looker/docs/ci-content-validator#incremental_validation) to find errors that are unique to the development branch.



For more information and configuration options, see the [Continuous Integration Content Validator](https://docs.cloud.google.com/looker/docs/ci-content-validator) documentation page.

### Assert Validator

The Continuous Integration Assert Validator runs [LookML data tests](https://docs.cloud.google.com/looker/docs/reference/param-model-test) that are defined in your project to verify model logic and data integrity.

For example, a LookML data test might look like the following:
    
    
    test: historic_revenue_is_accurate {
      explore_source: orders {
        column: total_revenue { field: orders.total_revenue }
        filters: [orders.created_date: "2024"]
      }
      assert: revenue_is_expected_value {
        expression: ${orders.total_revenue} = 626000 ;;
      }
    }
    

The Assert Validator has the following key capabilities:

  * Scopes assert validation to [specific Explores to query](https://docs.cloud.google.com/looker/docs/ci-assert-validator#explores-to-query) or [exclude](https://docs.cloud.google.com/looker/docs/ci-assert-validator#explores-to-exclude).
  * Lets you configure [query concurrency](https://docs.cloud.google.com/looker/docs/ci-assert-validator#query-concurrency) to manage database load.



For more information and configuration options, see the [Continuous Integration Assert Validator](https://docs.cloud.google.com/looker/docs/ci-assert-validator) documentation page.

### Managing and running CI suites

To manage and run Continuous Integration tests, follow these steps:

  * **Create suites** : Configure which validators to run and set their options on the [**Suites** page](https://docs.cloud.google.com/looker/docs/ci-create-suite) in the Looker IDE. For more information, see the [Creating a Continuous Integration suite](https://docs.cloud.google.com/looker/docs/ci-create-suite) documentation page.
  * **Trigger runs** : Trigger validation runs [automatically on pull requests](https://docs.cloud.google.com/looker/docs/ci-run-suite#pr-run), [on a schedule](https://docs.cloud.google.com/looker/docs/ci-run-suite#schedule-run), or [manually](https://docs.cloud.google.com/looker/docs/ci-run-suite#manual-run) for a development branch or production. For more information, see the [Running Continuous Integration suites](https://docs.cloud.google.com/looker/docs/ci-run-suite) documentation page.
  * **View results** : Review error messages, affected LookML lines, and links to Explores and dashboards on the [CI run results page](https://docs.cloud.google.com/looker/docs/ci-view-results). For more information, see the [Viewing the results of a CI run](https://docs.cloud.google.com/looker/docs/ci-view-results) documentation page.



## Link stability for Looks and dashboards

By default, Looks and dashboards are given ascending numeric IDs that are used in the URL for the Look or dashboard. However, there is no way to keep these in sync across systems. Therefore, a URL for a specific dashboard in development won't point to the same dashboard in QA or production.

For UDDs there is an option to use a slug instead of an ID as part of the URL. The slug is a semi-random set of characters rather than a number. The slug can be set as part of the import and so that a similar URL can point to the same UDD on development, QA, and production. Using slugs instead of IDs is a best practice, particularly when "clicking through" to a UDD from Look or another UDD.

The slug can be found by inspecting the output of `gzr dashboard cat`. The slug can be used in the dashboard URL in place of the numeric ID.

## Migrating user content with Gazer

Copying content such as Looks and dashboards between the development, QA, and production is often useful. You may want to produce content that showcases new LookML additions, or verify that saved content still functions correctly after LookML changes. In these situations [Gazer](https://github.com/looker-open-source/gzr) can be used to copy content between instances.

### LookML dashboards

LookML dashboards are synced between instances during the regular LookML CI/CD workflow. However, if any UDDs are synced with LookML dashboards, they can be updated with Gazer by using the following command:
    
    
    gzr dashboard sync_lookml DASHBOARD_ID --host TARGET_SYSTEM_URL
    

### User-defined dashboards

User Defined Dashboards (UDDs) can be migrated with Gazer by referencing the dashboard's ID and the URL of the Looker instance where the UDD resides. Gazer saves the dashboard configuration to a JSON file which is then imported into the target Looker instance.

The command to extract the UDD configuration is as follows:
    
    
    gzr dashboard cat DASHBOARD_ID --host TARGET_SYSTEM_URL --dir .
    

This will generate a file named `Dashboard_DASHBOARD_ID_DASHBOARD_NAME.json` that contains the dashboard's configuration.

The UDD can be imported into the target system using the following command:
    
    
    gzr dashboard import Dashboard_DASHBOARD_ID_DASHBOARD_NAME.json FOLDER_ID \
        --host TARGET_SYSTEM_URL
    

### Looks

Look migration works very similarly to UDD migration. First, use Gazer to save the Look configuration to a JSON file:
    
    
    gzr look cat LOOK_ID --host SOURCE_SYSTEM_URL --dir .
    

Then, import the Look into the target instance:
    
    
    gzr look import Look_LOOK_ID_LOOK_NAME.json FOLDER_ID \
        --host TARGET_SYSTEM_URL
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

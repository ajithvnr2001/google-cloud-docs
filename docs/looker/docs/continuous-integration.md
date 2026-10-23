---
url: https://docs.cloud.google.com/looker/docs/continuous-integration/
title: Looker Continuous Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:37:05.779003+00:00
---

# Looker Continuous Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/continuous-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker Continuous Integration Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Looker's Continuous Integration is based on the legacy standalone Spectacles service. Looker will continue to integrate and evolve the Spectacles features into Looker's Continuous Integration, and the legacy standalone Spectacles service itself will be discontinued starting November 30, 2026. Existing Spectacles customers will receive an email with details. If you have any questions or require assistance, please contact us at [spectacles-support@google.com](mailto:spectacles-support@google.com). 

The **Looker Continuous Integration (CI)** features let you run tests on your LookML project to deliver more reliable, efficient, and user-friendly data experiences. You can use the CI validators to catch issues with SQL, data tests, content, LookML, and coding style before they hit production to verify your LookML and prevent query errors for your users. You can also configure the CI validators to run automatically when a pull request is submitted to your LookML repository, on a schedule, or when a dbt Cloud CI job finishes.

CI is composed of the following validators, which run different checks against your Looker instance:

  * [SQL Validator](https://docs.cloud.google.com/looker/docs/ci-sql-validator) — Verifies that the dimensions in your Explores run correctly against your database.
  * [Assert Validator](https://docs.cloud.google.com/looker/docs/ci-assert-validator) — Runs any LookML [data tests](https://docs.cloud.google.com/looker/docs/reference/param-model-test) that were created by your Looker developers and returns all failures and errors.
  * [Content Validator](https://docs.cloud.google.com/looker/docs/ci-content-validator) — Runs the Looker [content validation](https://docs.cloud.google.com/looker/docs/content-validation) to test for errors in the Looks and dashboards in your LookML project.
  * [LookML Validator](https://docs.cloud.google.com/looker/docs/ci-lookml-validator) — Runs the [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation) to test for LookML errors in the project.
  * [Style Validator](https://docs.cloud.google.com/looker/docs/ci-style-validator) — Enforces LookML coding standards, naming conventions, and structural best practices across your project.



To use these validators on your LookML instance, you can create a _CI suite_ , which defines a set of validators and their options that are associated with your LookML project. See the following pages for information on CI suites:

  * [Creating a Continuous Integration suite](https://docs.cloud.google.com/looker/docs/ci-create-suite)
  * [Running Continuous Integration suites](https://docs.cloud.google.com/looker/docs/ci-run-suite)
  * [Viewing the results of a CI run](https://docs.cloud.google.com/looker/docs/ci-view-results)



## Requirements

To use Continuous Integration, you need the following:

  * A [Looker-hosted](https://docs.cloud.google.com/looker/docs/glossary#looker-hosted) instance that is enabled for Continuous Integration.

**Note:** For [Looker (Google Cloud core) instances](https://docs.cloud.google.com/looker/docs/looker-core-overview), Continuous Integration is supported on instances that are configured with [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections) or with [private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) or [hybrid connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private-ip-public-ip) that use [Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psc). In addition, Continuous Integration is supported on Looker (Google Cloud core) instances that are enabled for [CMEK](https://docs.cloud.google.com/looker/docs/looker-core-cmek) or that are within a [VPC Service Controls perimeter](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc). Continuous Integration is not supported on Looker (Google Cloud core) instances that are configured with private connections or hybrid connections that use [private services access](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psa). To use the [CI GitHub app](https://docs.cloud.google.com/looker/docs/admin-panel-platform-ci#github) or the [dbt Cloud integration](https://docs.cloud.google.com/looker/docs/admin-panel-platform-ci#dbt-cloud) on an instance that uses private connections, hybrid connections, or a VPC Service Controls perimeter, you must update your networking configuration to allow ingress and egress traffic to and from GitHub and your dbt Cloud host URL.
  * A Looker CI user account. When you enable Continuous Integration on your instance, Looker automatically creates 10 Looker CI users in the [**Looker CI Users** user group](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups#ci-users) with the [**Looker CI Users** role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#ci-users). A Looker admin can view the Looker CI users from the **Service Accounts** tab of the [**Users**](https://docs.cloud.google.com/looker/docs/admin-panel-users-users) Admin page.




## Compliance capabilities of Continuous Integration

Looker CI is not included in the [FedRAMP High, FedRAMP Moderate, or DoD Impact Level 5 (IL5) authorization boundaries](https://docs.cloud.google.com/assured-workloads/docs/control-packages#regulatory-data-boundaries).

Prior to enabling the Looker CI setting for your Looker instance, consult with your authorizing body to determine whether Looker CI's compliance offerings meet your organization's specific security and regulatory requirements.

For Looker (Google Cloud core) instances, each [Assured Workloads control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages) that becomes available will add Looker CI features as default offerings as that package's change requirements and processes are met.

## Enabling Continuous Integration

To enable Continuous Integration, a Looker admin must perform the following tasks:

  * Enable the instance for Continuous Integration in the [**Continuous Integration** page](https://docs.cloud.google.com/looker/docs/admin-panel-platform-ci) of the Looker **Admin** panel.
  * [Install the CI GitHub app in your GitHub organization](https://docs.cloud.google.com/looker/docs/admin-panel-platform-ci#github). (This is highly recommended for all implementations, and required if you want to [use pull requests to trigger CI validation runs](https://docs.cloud.google.com/looker/docs/ci-create-suite#pr-trigger)).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

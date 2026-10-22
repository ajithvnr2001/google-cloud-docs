---
url: https://docs.cloud.google.com/looker/docs/ci-assert-validator/
title: Continuous Integration Assert Validator \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:39.765692+00:00
---

# Continuous Integration Assert Validator  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/ci-assert-validator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Continuous Integration Assert Validator Stay organized with collections  Save and categorize content based on your preferences. 

The Continuous Integration (CI) Assert Validator runs the LookML [data tests](https://docs.cloud.google.com/looker/docs/reference/param-model-test) that were created by Looker developers in your LookML project and shows the results for each data test. For data tests that fail, the Assert Validator shows the error.

LookML data tests allow you to validate the logic of your Looker model. Data tests can test complex assumptions, such as the following:

  * Revenue in May of last year should equal $204,259.
  * Conversion rate should be greater than zero.
  * Order status shouldn't be null.



A LookML data test is made up of a small [`explore_source`](https://docs.cloud.google.com/looker/docs/reference/param-model-test#explore_source) query and a [`yesno` assert expression](https://docs.cloud.google.com/looker/docs/reference/param-model-test#assert), such as in the following example:
    
    
    test: historic_revenue_is_accurate {
      explore_source: orders {
        column: total_revenue { field: orders.total_revenue }
        filters: [orders.created_date: "2024"]
      }
      assert: revenue_is_expected_value {
        expression: ${orders.total_revenue} = 626000 ;;
      }
    }
    

**Tip:** Once you write a LookML data test, you can [test it in the Looker IDE](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#running_data_tests).

See the Assert Validator options section of this page for details on the options that you can configure when you [create or edit a CI suite](https://docs.cloud.google.com/looker/docs/ci-create-suite). For information on running the Assert Validator, see the [Running Continuous Integration suites](https://docs.cloud.google.com/looker/docs/ci-run-suite) documentation page.

In the [run results page](https://docs.cloud.google.com/looker/docs/ci-view-results), the Assert Validator shows the results for each data test. For data tests that fail, the Assert Validator shows the error or errors, as follows:

![Continuous Integration results page showing Assert Validator findings](https://docs.cloud.google.com/static/looker/docs/images/ci-assert-results-2506.png)

## Assert Validator options

There are several options you can specify when you [create or edit a Continuous Integration suite](https://docs.cloud.google.com/looker/docs/ci-create-suite) to configure how Assert Validator runs. The options are described in the following sections of this page:

  * Explores to query
  * Explores to exclude
  * Query concurrency



### Explores to query

By default, the Assert Validator will run each data test in your LookML project.

Data tests are defined using an [`explore_source`](https://docs.cloud.google.com/looker/docs/reference/param-model-test#explore_source) parameter that points to an Explore in your project, and you can use the **Explores to query** field to limit assert validation to specific Explores that your data tests are based on.

You can specify Explores in the following format: `model_name/explore_name`

For example, to specify the Explores named `users` and `orders` in the `thelook.model.lkml` file, you would enter the following: `thelook/users, thelook/orders`

See the [SQL Validator](https://docs.cloud.google.com/looker/docs/ci-sql-validator#explores-to-query) documentation page for more information about and examples of how to specify Explores and models in this field.

### Explores to exclude

By default, the Assert Validator will run each data test in your LookML project. You can use the **Explores to exclude** field to exclude from assert validation specific Explores that your data tests are based on. The Assert Validator won't run data tests that are based on these excluded Explores.

You can specify Explores in the following format: `model_name/explore_name`

See the [SQL Validator](https://docs.cloud.google.com/looker/docs/ci-sql-validator#explores-to-query) documentation page for more information about and examples of how to specify Explores and models in this field.

### Query concurrency

By default, the Assert Validator runs no more than 10 queries at a time to avoid overwhelming your Looker instance. You can use the **Query concurrency** field to specify a different maximum number of queries that the Assert Validator can run concurrently. 

The maximum value for the **Query concurrency** field is limited to the [Max concurrent queries for this connection](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max-queries) setting on your database connection.

If you notice a slowdown in your Looker instance while running Assert validation, you can decrease this value.

**Tip:** You can also restrict validation to a specific Explore or model by using the **Explores to query** option, or exclude Explores and models by using the Explores to exclude option.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/looker/docs/reference/param-model-test/
title: test \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:10:47.933447+00:00
---

# test  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-model-test/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  test Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    test: historic_revenue_is_accurate {
      explore_source:  orders {
        column:  total_revenue {
          field:  orders.total_revenue 
        }
        filters: [orders.created_date:  "2017"]
      }
      assert:  revenue_is_expected_value {
        expression: ${orders.total_revenue} = 626000 ;;
      }
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) `test` \- or - [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) `test` \- or - [Data Test File](https://docs.cloud.google.com/looker/docs/other-project-files#data_test_files) `test` |  Default Value None Accepts The identifier of the data test, plus subparameters defining the test assertions and query.   
---|---  
  
## Definition

**Tip:** See the [LookML data tests: Recommendations and best practices](https://discuss.google.dev/t/lookml-data-tests-recommendations-and-best-practices/112693) Looker Community post for further tips and information about data tests.

Looker has the [LookML validator](https://docs.cloud.google.com/looker/docs/lookml-validation) to verify that your LookML code is syntactically valid and the [Content Validator](https://docs.cloud.google.com/looker/docs/content-validation) to verify object references between your content and your model.

In addition to those validators, the `test` parameter lets you validate the logic of your model. For each data test, you create a query and a `yesno` assertion statement. The data test runs the test query and verifies that the assertion is true for each row of the test query. If the assertion statement returns `yes` for every row of the test query, the data test passes.

If your project settings are configured to [require data tests to pass before deploying to production](https://docs.cloud.google.com/looker/docs/git-options#require-data-tests), and if your project has one or more `test` parameters, the IDE will present the **Run Tests** button after you commit changes to the project. LookML developers must run the data tests before deploying changes to production.

**Note:** By default, new LookML projects [require data tests to pass](https://docs.cloud.google.com/looker/docs/git-options#require-data-tests).

Regardless of whether your project requires data tests before deploying to production, a LookML developer in [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode) can [run data tests](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#running_data_tests) at any time to verify the model's logic.

You can create data tests in [model files](https://docs.cloud.google.com/looker/docs/reference/param-model), [view files](https://docs.cloud.google.com/looker/docs/reference/param-view), or in separate, dedicated [data test files](https://docs.cloud.google.com/looker/docs/other-project-files#data_test_files). When using a dedicated file to house your data tests, remember to [`include`](https://docs.cloud.google.com/looker/docs/reference/param-model-include) the data test file in any model file or view file where you want to run your data tests.

A data test cannot have the same name and `explore_source` as another data test in the same project. If you are using the same `explore_source` for multiple data tests in your project, be sure that the names of the data tests are all unique.

The `test` parameter has the following subparameters:

  * `explore_source`: Defines the query to use in the data test.
  * `assert`: Defines a Looker expression that is run on every row of the test query to verify the data.



Once you define the LookML for your test, you can run the data test to verify that your test works properly and to see if your model's logic passes the test (you must be in [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode) to run data tests).

There are several ways to initiate data tests for a project:

![](https://docs.cloud.google.com/static/looker/docs/images/dev-git-data-tests-run-2112.png)

  1. If your project settings are configured to [require data tests to pass before deploying your files to production](https://docs.cloud.google.com/looker/docs/git-options#require-data-tests), the IDE will present the **Run Tests** button after you [commit](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#committing_changes) changes to the project. This will run all the tests for your project, no matter which file defines the test. You must pass the data tests before you can deploy your changes to production.
  2. In the **Project Health** panel, select the **Run Data Tests** button. This will run all data tests in your project, no matter which file defines the test.
  3. Select the **Run LookML Tests** option from the file's menu. This will run only the tests defined in the current file.



Once you run the data tests, the **Project Health** panel will display the progress and results.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-git-data-tests-results-2112.png)

You can select the **Explore Query** link for each test result to open an Explore with the query that is defined in the data test.

### `explore_source`

The `explore_source` parameter in a data test uses the same syntax and logic as the [`explore_source` parameter of a derived table](https://docs.cloud.google.com/looker/docs/reference/param-view-explore-source). The one difference is that a data test's `explore_source` doesn't support the `derived_column`, `bind_filters`, and `bind_all_filters` subparameters.

> __**Handy Tip** : An easy way to get the `explore_source` LookML is to use an existing Explore to create your query. In the Explore, select **Get LookML** from the Explore's gear menu and then select the **Derived Table** tab to get the LookML for the query. See the documentation on [creating native derived tables](https://docs.cloud.google.com/looker/docs/creating-ndts#using_an_explore_to_begin_defining_your_ndts) for more information.

Note the following for the `explore_source` of a data test:

  * A data test's `explore_source` query is a standard Looker query, meaning that the test's `explore_source` query has a limit of 5,000 rows. Be sure that your query doesn't go over 5,000 rows so that you get a complete result set to test. You can incorporate filters or sorting in your `explore_source` to reduce the number of rows in your query, or to bring the relevant rows to the top of the query.

  * An `explore` with `extension: required` cannot be used as an `explore_source` for a [data test](https://docs.cloud.google.com/looker/docs/reference/param-model-test). The [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_changes) will generate an error that the `explore_source` cannot be found.




### `assert`

The `assert` subparameter defines the criteria by which the `explore_source` query's result is considered valid. The `expression` subparameter accepts a [Looker expression](https://docs.cloud.google.com/looker/docs/functions-and-operators) that results in a `yesno` (Boolean). After the `explore_source` query is run, the assertion's expression is evaluated for every row of the query's result set. If there is a `no` response for any row of the query, the data test fails. If the query itself has errors, the test also fails.

A test can have multiple `assert` declarations. For the test to pass, each assertion has to be true for every row of the `explore_source` query.

> __**Handy Tip** : You can use the [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations#creating_table_calculations_in_looker) dialog to test the Looker expression syntax to use in your test's `expression` parameter.

For use in data tests, fields in the Looker expression must be fully scoped, meaning they are specified using the `view_name.field_name` format. For example, the following expression declares the field as `aircraft_engine_types.aircraft_engine_type_id`:
    
    
    assert: engine_type_id_not_null {
      expression: NOT is_null(${aircraft_engine_types.aircraft_engine_type_id}) ;;
    }
    

## Examples

### Ensuring that a primary key is unique

The following data test creates a query from the `orders` Explore and defines an `expression` to test that order IDs are unique in the result set. The `explore_source` query creates a count of rows associated with each ID in the database. If the ID is unique, the database should have only one row for an ID. Furthermore, it sorts on the count and limits the result set to one row, so the query response will be the ID with the highest count. If any ID has a count higher than 1, we know there are multiple rows for that ID and therefore the ID is not unique. If that's the case, this data test will fail.
    
    
    test: order_id_is_unique {
      explore_source: orders {
        column: id {}
        column: count {}
        sorts: [orders.count: desc]
        limit: 1
      }
      assert: order_id_is_unique {
        expression: ${orders.count} = 1 ;;
      }
    

### Verifying a known value

This next data test checks to make sure that the 2017 revenue value is always $626,000. In this dataset, that is a known value that should never change.
    
    
    test: historic_revenue_is_accurate {
      explore_source: orders {
        column: total_revenue {
          field: orders.total_revenue
        }
        filters: [orders.created_date: "2017"]
      }
      assert: revenue_is_expected_value {
        expression: ${orders.total_revenue} = 626000 ;;
      }
    }
    

### Confirming there are no null values

This next data test checks to make sure that there are no null values in the data. This `explore_source` uses a `sort` to be sure that any nulls will be returned at the top of query. Sorting for nulls can vary, based on your dialect. The following test uses `desc: yes` as an example.
    
    
    test: status_is_not_null {
      explore_source: orders {
        column: status {}
        sorts: [orders.status: desc]
        limit: 1
      }
      assert: status_is_not_null {
        expression: NOT is_null(${orders.status}) ;;
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/looker/docs/creating-looker-expressions/
title: Create Looker expressions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:45.298085+00:00
---

# Create Looker expressions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/creating-looker-expressions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Create Looker expressions Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page is part of the [Retrieve and chart data](https://docs.cloud.google.com/looker/docs/retrieve-and-chart-data) learning series. 

Looker expressions are formulas you use to perform custom calculations and apply advanced logic within Looker. Use Looker expressions to create dynamic table calculations, custom fields, custom filters, and data tests. This capability helps you extract specific insights and customize your data analysis. This guide describes how to construct and use Looker expressions effectively.

## Shortcuts for common functions

Before creating Looker expressions, check if your task can be completed using built-in shortcuts:

  * **Table calculations** : If your admin has granted you [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) to create [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations), you can use [Shortcut calculations](https://docs.cloud.google.com/looker/docs/table-calculations#quick_calculations) to quickly perform common calculations on numeric fields in an Explore's data table.
  * **Custom fields** : If your admin has granted you [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields) to create [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields), you can use the following: 
    * [Custom groups](https://docs.cloud.google.com/looker/docs/custom-fields#custom_grouping) to group values under custom labels without needing to develop `CASE WHEN` logic in [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameters or [`type: case`](https://docs.cloud.google.com/looker/docs/reference/param-field-case) fields.
    * [Custom bins](https://docs.cloud.google.com/looker/docs/custom-fields#custom_binning) to group numeric type dimensions in custom tiers without needing to develop [`type: tier`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#tier) LookML fields.



## Looker expressions

Looker expressions are used to perform calculations for:

  * [Table calculations](https://docs.cloud.google.com/looker/docs/table-calculations)
  * [Custom fields](https://docs.cloud.google.com/looker/docs/custom-fields)
  * [Custom filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom-filters)
  * [Data tests](https://docs.cloud.google.com/looker/docs/reference/param-model-test)



A Looker expression is built from a combination of these elements: 

  * **`NULL`** : The value `NULL` indicates there is no data, and can be useful when you want to check that something is empty or doesn't exist.

  * **A constant** : A constant is an unchanging value that you provide. A number such as `7` or a string such as `Completed` are constants.

  * **A Looker field** : A reference to a Looker field, which includes dimensions, measures, and table calculations.

  * **A Looker operator** : For a list of available operators, see [Looker functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators). Supported operators include the following categories:

    * Mathematical operators (such as `+`, `-`, `*`, and `/`)
    * Comparison operators (such as `=`, `>`, and `<=`)
    * Logical operators (such as `AND`, `OR`, and `NOT`)
  * **A Looker function** : Similar to spreadsheet functions, functions let you transform your data or reference data in complex ways. For a list of available functions, see [Looker functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators).




## Create Looker expressions

[Table calculations](https://docs.cloud.google.com/looker/docs/table-calculations), [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields), and [custom filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom-filters) use the Looker expression editor. As you type your expression, Looker prompts you with functions, operators, and field names that you might want to use.

**Tip:** If you are a Looker developer creating a [data test](https://docs.cloud.google.com/looker/docs/reference/param-model-test) to verify the logic of your model, you can use the Looker expression editor to build a Looker expression, then copy the expression into your data test's `expression` parameter. 

### See all suggestions

Access the Looker expression editor in an Explore by creating a [table calculation](https://docs.cloud.google.com/looker/docs/table-calculations), [custom field](https://docs.cloud.google.com/looker/docs/custom-fields), or [custom filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom-filters).

Type a space to see a list of all fields, functions, and operators that you can choose from. If a field is currently selected in the Explore, Looker displays a black dot to the left of the field and displays the field at the top of the list.

Start typing in the Looker expression editor to shorten the list to items that you are interested in.

The editor for custom fields displays Explore fields that are currently in use, if they are compatible with the custom field's function.

### Add a field

To include a Looker field in your expression, start typing the field's name. As you type, the editor narrows your search to a list of fields and functions that contain what you've typed. You can type the name of the field as it appears on the Explore page, or you can use its LookML name if you know it.

When you select a field from the list, Looker adds it to your expression using the LookML name in the form `${view_name.field_name}`. This ensures that all of your fields have unique names in your expression.

**Note:** For detailed instructions about using fields, see Use fields. 

### Add totals

If you are creating an expression that is based on an Explore where you [displayed totals](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#displaying_totals), you can also include column and row totals in your expression. Column totals appear in the editor with the word **Total** in front of the LookML iteration of the field name. For example, for a field named **Count** , Looker gives the column total for that field the name `Count - Total`.

The _LookML name_ for totals is in the form `${view_name.field_name:total}`, where `:total` is added to the end of the field name.

For row totals, the words **Row Totals** appear in front of the field name in the editor. In the _LookML name_ of the field, `:row_total` is added to the end of the field name, such as `${view_name.field_name:row_total}`.

### Add operators

You can add logical operators such as `AND`, `OR`, and `NOT` to your expression if needed. Ordinarily `AND` operators are evaluated before `OR` operators, but you can override this behavior by using parentheses. You can also use comparison operators (such as `>`, `=`, and `<=`) and mathematical operators (such as `+` and `*`).

When you hold the pointer over an operator, notes for proper use display in the information pane.

**Note:** For detailed instructions about using operators, see Use operators. 

### Add functions

To include a Looker function in your expression, start typing the function's name. As you type, the editor narrows your search to a list of fields and functions that contain what you've typed.

Functions may be constructed of arguments (or variables) that require a certain type, such as a field, a number, or yes/no. When you hold the pointer over a function, check the notes in the information pane to understand which arguments you need to provide, and what type they need to be.

For a full list of functions, see [Looker functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators).

**Note:** For detailed instructions about using functions, see Use functions. 

### Use error hints and the information pane

Looker displays an information pane next to the Looker expression editor. This pane provides documentation and suggestions, especially if your expression contains an error.

The information pane provides the following information:

  * **Error highlighting** : Looker underlines in red any parts of the expression that are not yet correct.

  * **Suggestions and error details** : Looker gives suggestions about what to add next in your expression. If there is an error, it explains why the error occurs.

  * **Documentation** : Looker displays documentation about the function or operator you are working with. For example, while you type the first argument of an `if` function, Looker indicates that the first argument should evaluate as `yes` or `no`. Click the function name to view its documentation.




### Include comments

You can include comments in Looker expressions by beginning the comment line with `#` in the expression editor.

## Use fields

Sometimes you want to use the value of a field (a dimension, measure, or table calculation) in an expression. You might want to add the value of the field to something else, check that it has a certain value, or include it in a function.

As described in Add a field, you can type the name of the field into the expression editor, and Looker helps you find the correct reference format. When you add a field to an expression, Looker uses the field's LookML identifier, such as `${view_name.field_name}`. Type the field name as it appears in the field picker, and the expression editor displays the field picker name alongside the LookML identifier.

There are several ways to retrieve a value:

  * **Get a value from the same row** : The most basic way to use a field is to reference it directly, such as `${product.category}`. This references the value for that field in the current row.

  * **Get a value from a different row** : You can also retrieve a field's value from a different row. For example, to get the Product Category from the previous row, use an offset function such as `offset(${product.category}, -1)`. For a list of positional functions, see [Positional functions](https://docs.cloud.google.com/looker/docs/functions-and-operators#rows).

  * **Get a value from a pivoted column** : To get values from pivoted columns, use pivot functions such as `pivot_index(${order.total_sales}, 1)`. For a list of pivot functions, see [Pivot functions](https://docs.cloud.google.com/looker/docs/functions-and-operators#pivots).

  * **Get a total from a row or a column** : If you [displayed totals in your Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#displaying_totals), you can get total values by adding `:total` (for column totals) or `:row_total` (for row totals) to the field name, using the format `${field_name:total}`. For example: `${orders.count} / ${orders.count:total}`.




**Note:** When referencing fields in a [custom filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom-filters), you can use only dimensions - not measures, totals, or table calculations. Additionally, you cannot refer to values in other rows or pivoted columns. This is because Looker must be able to turn your filter into SQL to retrieve your data. 

Not all time and date options are supported in [custom filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom-filters) or [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields). For more information, see the [dimension group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#custom_filters_and_custom_fields_dont_support_all_timeframes) parameter description. 

When referencing fields in a [table calculation](https://docs.cloud.google.com/looker/docs/table-calculations), you can reference any value from any dimension, measure, or other table calculation. 

## Use operators

Looker expressions can include logical, comparison, and mathematical operators to create different conditions:

  * Logical operators (such as `AND`, `OR`, and `NOT`)
  * Comparison operators (such as `>` and `<`)
  * Mathematical operators (such as `+` and `-`)



Unless you specify otherwise with parentheses, `AND` logic is evaluated before `OR` logic. The following expression without additional parentheses:
    
    
    if (
      ${order_items.days_to_process}>=4 OR
      ${order_items.shipping_time}>5 AND
      ${order_facts.is_first_purchase},
    "review", "okay")
    

is evaluated as:
    
    
    if (
      ${order_items.days_to_process}>=4 OR
      (${order_items.shipping_time}>5 AND ${order_facts.is_first_purchase}),
    "review", "okay")
    

In Looker, use `yes` and `no` instead of `true` and `false`. These logical constants are _not_ the same thing as the literal strings `"yes"` and `"no"`. For more information, see [Logical constants](https://docs.cloud.google.com/looker/docs/functions-and-operators#logical_constants).

## Use functions

Looker expressions often include one or more functions to retrieve or calculate data. They are similar to spreadsheet functions.

Functions take the form of a name followed by parentheses, such as `my_function()`. Values passed inside the parentheses are arguments, like `my_function(argument_1, argument_2)`.

For example, the [`now`](https://docs.cloud.google.com/looker/docs/functions-and-operators#function-now) function takes no arguments and returns the current date and time: `now()`.

The [`round`](https://docs.cloud.google.com/looker/docs/functions-and-operators#function-round) function takes one numeric argument: `round(3.2)`. The result is `3`.

To know which arguments to provide:

  * The information pane next to the expression editor provides documentation for the active function.
  * For a complete list of functions, see [Looker functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators).



Consider the [`contains`](https://docs.cloud.google.com/looker/docs/functions-and-operators#function-contains) function:

Function | Syntax | Purpose  
---|---|---  
contains {:#function-contains} | `contains(string, search_string)` | Returns `Yes` if `string` contains `search_string`, and `No` otherwise.  
  
The `contains` function requires two arguments: `string` and `search_string`. The `string` argument represents the field or text to search in, and `search_string` represents the term to search for:
    
    
    contains(${customer.feedback_text}, "great")
    

If "great" appears in the customer feedback, the function returns `Yes`. Otherwise, it returns `No`.

You can nest functions inside other functions:
    
    
    contains(
      if(
        is_null(${customer.feedback_text}),
        ${customer.comment_text},
        ${customer.feedback_text}
      ),
    "great")
    

This expression evaluates in three steps:

  1. The `is_null` function checks if customer feedback text is empty.
  2. The `if` function returns the feedback text if present; otherwise it returns the comment text.
  3. The `contains` function searches the returned text for "great."



Logically, this expression means: "If there is customer feedback, search in that text. If not, search in customer comments instead. In both cases, look for the word 'great.'"

**Note:** [Custom filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom-filters) and [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields) can use most functions, but cannot use certain mathematical functions or functions that refer to other rows or pivot columns. For details on supported functions, see [Looker functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators). 

You can use any function in a [table calculation](https://docs.cloud.google.com/looker/docs/table-calculations) or in the `expression` parameter of a [data test](https://docs.cloud.google.com/looker/docs/reference/param-model-test). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

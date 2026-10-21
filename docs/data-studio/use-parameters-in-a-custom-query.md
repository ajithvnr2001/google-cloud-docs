---
url: https://docs.cloud.google.com/data-studio/use-parameters-in-a-custom-query/
title: Use parameters in a custom query \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:20.826583+00:00
---

# Use parameters in a custom query  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/use-parameters-in-a-custom-query/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Use parameters in a custom query Stay organized with collections  Save and categorize content based on your preferences. 

Parameters let you build responsive, customizable reports by passing parameters from a data source back to the underlying SQL query. To use a parameter inside your custom query, follow the syntax guidelines that are documented in [Running parameterized queries](https://docs.cloud.google.com/bigquery/docs/parameterized-queries).

* * *

## Standard parameters

You can use the following parameters in any custom query:

Parameter | Purpose  
---|---  
`@DS_START_DATE` | Gets the beginning of the report date range.  
`@DS_END_DATE` | Gets the end of the report date range.  
`@DS_USER_EMAIL` | Gets the email address of the logged-in user.  
  
To use these parameters, follow these steps:

  1. In the **Parameters** section of the connection panel, enable the parameters that you want to use. Data Studio prompts you to grant access to your email address when you enable the `@DS_USER_EMAIL` parameter.
  2. In your query, use uppercase formatting when typing the parameter names.



Data Studio passes all parameter values as text strings. To handle parameter strings as calendar dates, numbers, or other data types, use an appropriate SQL conversion function, such as `PARSE_DATE`, `PARSE_TIMESTAMP`, or `CAST`.

### Use date parameters to pass date ranges to the underlying query

If your report includes a [date range control](https://docs.cloud.google.com/data-studio/date-range-control), viewers can use that control to request different starting and ending dates directly from the database.

### Use the email parameter to provide row-level access to the data

The email parameter lets you show only the data that is associated with the logged-in user of a report, data source, or exploration. That user must be logged in to a Google Account and must consent to providing their email address to Data Studio. If the viewer doesn't consent, all charts in the report that are based on this data source display an authorization error.

* * *

## Custom parameters

You can use any parameters that you create in the Data Studio user interface inside your custom query.

### Create a parameter in the connection page

  1. In the **Parameters** section of the custom query editor, click **+ADD PARAMETER**.
  2. Configure the [parameter options](https://docs.cloud.google.com/data-studio/parameters).
  3. Click **OK**.



### Hide custom parameters in the data source

By default, report editors can modify custom parameters directly inside reports. To prevent report editors from changing a parameter's value, you can hide the parameter right in the data source configuration:

  1. Click more_vert **More options**.
  2. Click **Hide**.



Learn more about [allowing data source parameters in reports](https://docs.cloud.google.com/data-studio/parameters).

* * *

## Use a parameter in a custom query

In the body of your custom SQL query, replace a hard-coded value with an identifier that begins with the `@` character (for example, `@param_name`).

* * *

## Parameter examples

Following are some examples of using parameters:

### Custom parameter example
    
    
    SELECT word FROM `TABLE` WHERE corpus = @corpus;
    

### String with `CONTAINS` and a numeric threshold
    
    
    SELECT * FROM `bigquery-public-data.baseball.games_post_wide`
    WHERE REGEXP_CONTAINS(gameId, @s)
    AND attendance > @attendance LIMIT 100;
    

### Multi-select string parameter

Notice how `UNNEST` flattens the array list of multi-select parameter values:
    
    
    SELECT * from user.users as user WHERE display_name in UNNEST(@name);
    

### Date parameter using standard formatting
    
    
    SELECT creation_date, age, display_name from user.users as user
    WHERE creation_date > PARSE_DATE('%Y%m%d', @DS_START_DATE)
    AND creation_date < PARSE_DATE('%Y%m%d', @DS_END_DATE);
    

### Date parameter using Unix timestamp in microseconds
    
    
    SELECT creation_date, age, display_name from user.users as use
    WHERE creation_date > UNIX_MICROS(PARSE_TIMESTAMP('%Y%m%d', @DS_START_DATE))
    AND creation_date < UNIX_MICROS(PARSE_TIMESTAMP('%Y%m%d', @DS_END_DATE))
    

### Email parameter example
    
    
    SELECT * FROM Sales WHERE sales-rep-email = @DS_USER_EMAIL;
    

* * *

## Related resources

  * [About parameters](https://docs.cloud.google.com/data-studio/parameters)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

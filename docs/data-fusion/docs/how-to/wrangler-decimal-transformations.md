---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-decimal-transformations/
title: Work with decimal data \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:39.771122+00:00
---

# Work with decimal data  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-decimal-transformations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Work with decimal data Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to convert fields into the decimals and perform transformations on them when you prepare data in the Wrangler workspace of the Cloud Data Fusion Studio.

## Read decimal data

  1. [Go to the Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. Open an object, such as a table, from a database or a Cloud Storage file.

     * For a database or a BigQuery connection, if the table has a decimal column, Wrangler converts it into a `BigDecimal` type. When you create the pipeline from Wrangler, the column is then converted to the `decimal` data type.
     * If your dataset contains non-decimal data that you want to convert to decimals, use the `set-column` directive:
           
           set-column : DECIMAL_COLUMN exp:{new("java.math.BigDecimal", INPUT_COLUMN)}
           

Replace the following:

       * `DECIMAL_COLUMN`: the decimal column to be transformed. After the directive executes, the column's data type changes to `BigDecimal`, and the schema also contains the appropriate data type.

       * `INPUT_COLUMN`: the column that gets converted, which can be one of the following types: `STRING`, `INTEGER`, `LONG`, `FLOAT`, or `DOUBLE`.

     * If your dataset includes values with varying scale, such as 1.05, 2.698, 5.8745512, set the scale with a Wrangler directive and edit the schema in the pipeline to set the scale for the decimal column.

To set the scale in the Wrangler, use a directive similar to the following:
           
           set-column : OUTPUT_COLUMN exp:{new("java.math.BigDecimal", DECIMAL_COLUMN).setScale()}
           

The following example converts a column called `cost` from a string to a decimal, sets a scale of 9, and outputs the results to a new column called `output-column`:
           
           set-column : output-column exp:{new("java.math.BigDecimal", "cost").setScale(9)}
           




## Transform decimal data

Decimal columns in Wrangler use the Java BigDecimal class. After the columns are converted to the BigDecimal data type, transform the columns with methods from [`Class BigDecimal`](https://docs.oracle.com/javase/8/docs/api/java/math/BigDecimal.html).

Transformation | Directive  
---|---  
Get the absolute value | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.abs()`  
Get the precision of a decimal value | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.precision()`  
Get the scale of a decimal value | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.scale()`  
Get the unscaled value of a decimal value | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.unscaledValue()`  
Add two decimal columns | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.add(DECIMAL_COLUMN_2)`  
Subtract a decimal from another | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.subtract(DECIMAL_COLUMN_2)`  
Multiply a decimal with another | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.multiply(DECIMAL_COLUMN_2)`  
Divide a decimal column by another and return the quotient | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.divide(DECIMAL_COLUMN_2)`  
Divide a decimal column by another and return the remainder | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.remainder(DECIMAL_COLUMN_2)`  
Convert decimal to a integer | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.intValue()`  
Convert decimal to a long | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.longValue()`  
Convert decimal to a float | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.floatValue()`  
Convert decimal to a double | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.doubleValue()`  
Check if a decimal value is equal to another | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.equals(DECIMAL_COLUMN_2)`  
Find the maximum of two decimal columns | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.max(DECIMAL_COLUMN_2)`  
Find the minimum of two decimal columns | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.min(DECIMAL_COLUMN_2)`  
Move the decimal point n places to the left | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.movePointLeft(n)`  
Move the decimal point n places to the right | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.movePointRight(n)`  
Get the nth power of a decimal | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.pow(n)`  
Negate a decimal | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.negate()`  
Strip trailing zeros in a decimal | `set-column : OUTPUT_COLUMN DECIMAL_COLUMN.stripTrailingZeros()`  
  
Replace the following:

  * `OUTPUT_COLUMN`: the column containing the output of the operation.
  * `DECIMAL_COLUMN`: the decimal column that's transformed.
  * `DECIMAL_COLUMN_2`: the second decimal column included in the operation, such as when you add the values from two decimal columns together.



## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

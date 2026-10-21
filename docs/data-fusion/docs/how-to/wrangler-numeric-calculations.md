---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-numeric-calculations/
title: Work with numbers \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:28.909275+00:00
---

# Work with numbers  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-numeric-calculations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Work with numbers Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to perform numeric calculations when you prepare data in the Wrangler workspace of the Cloud Data Fusion Studio.

You can perform these transformations in columns of the following data types:

  * Integer
  * Decimal
  * Double
  * Float
  * Long
  * Short

**Note:** To use numeric functions on decimal columns, use the [Wrangler CLI](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#wrangler-cli).

For more information, see the [`set-column`](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382107931) directive.

You can use numeric functions on one or more columns. The available numeric functions vary by the number of columns you select. You can choose to create a new column with the results of the calculations, or you can have the results appear in the column where you add the transformation.

If you apply a numeric function to a single column, the behavior is different than if you apply a numeric function to multiple columns. For example:

  * If you use the `Multiply()` function on _a single column_ , you specify the decimal value to multiply each value in the column by. Wrangler performs the multiplication on the sample data and displays the new values in the same column or in a new column.
  * If you use the `Multiply()` function on _multiple columns_ , Wrangler multiplies the values in each row for the selected columns and displays the new values in the first column of the transformation.



## Perform numeric calculations on values in one column

To apply a numeric calculation to one column, follow these steps:

  1. [Go to the Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Select **Calculate** and select an option—for example, **Add**.

To complete the calculation, some functions require you to enter a decimal value. For example, if you select **Subtract** , you must enter the value to subtract from each row.

  4. Optional: to create a new column for the calculated values, select the **Copy to a new column** checkbox.

  5. Click **Apply**.




The values change based on the calculation. Wrangler adds the corresponding directive as a step in the recipe. For example, if you subtract two from each value in the `Price` column, Wrangler adds the following transformation to the recipe:
    
    
    set-column :Price Price - 2
    

When you run the data pipeline, the transformation is applied to all values in the column.

### Supported calculations for one column

You can perform the following calculations on all values in one column:

Function | Description  
---|---  
[Absolute value](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396788355/Absolute+value+function) | Returns the absolute value for each value in a column. For example, the absolute value of -10 is 10.  
[Add](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396821110/Add+function) | Adds a positive or negative decimal to a column or adds multiple columns to output the sum of each row.  
[Arccos](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396919145/Arccos+function) | Returns the inverse of cosine for each value in a column.  
[Arcsin](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396919152/Arcsin+function) | Returns the inverse of sin for each value in a column.  
[Arctan](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396919159/Arctan+function) | Returns the inverse of tangent for each value in a column.  
[Ceil](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396788362/Ceil+function) | Returns the smallest integer greater than or equal to the numeric value in each cell of a column. For example, if the value is 2.21, Ceil returns 3. If the value is 5.88, Ceil returns 6. If the value is -5.15, Ceil returns -5.  
[Cos](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396919128/Cos+function) | Returns cosine of each column value.  
[Cube](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396788338/Cube+function) | Raises each value in the column to the power of 3.  
[Cube root](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/399180179/Cube+root+function) | Returns the cube root of each value in the column.  
[Divide](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396821124/Divide+function) | Divides each value in the column by a positive or negative decimal or divides each value in two columns.  
[Floor](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396788369/Floor+function) | Returns the largest integer greater than or equal to the numeric value in each cell of a column. For example, if the value is 2.21, FLOOR returns 2. If the value is 5.88, FLOOR returns 5. Likewise, if the value is -5.15, FLOOR returns -6.  
[Log](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/399180186/Log+function) | Returns the logarithm of each value in a column.  
[Modulo](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396788297/Modulo+function) | Returns the remainder when dividing each value in the column by a positive decimal or returns the remainder when dividing each value in two columns.  
[Multiply](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396788280/Multiply+function) | Multiplies each value in the column by a positive or negative decimal or multiplies each value in two columns.  
[Natural Log](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/399180193/Natural+log+function) | Returns the natural logarithm of each value in a column.  
[Power of](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396821131/Power+of+function) | Raises the column value to the specified power of value.  
[Random](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1795424262/Random+function) | Generates random, unpredictable Double values in a specified column.  
[Round](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1801093165/Round+function) | Rounds each value in a column.  
[Sin](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396821070/Sin+function) | Returns the sin for each value in a column.  
[Square](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396788314/Square+function) | Raises each value in the column to the power of 2.  
[Square root](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396788321/Square+root+function) | Returns the square root of each value in a column.  
[Substract](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396821117/Subtract+function) | Subtracts a positive or negative decimal to each value in the column.  
[Tan](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396821087/Tan+function) | Returns the tangent for each value in a column.  
  
## Perform numeric calculations on values in two columns

To apply a numeric calculation to two columns, follow these steps:

  1. [Go to the Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, select the checkbox by two column names.
  3. Go to a column name and click the arrow_drop_down expander arrow.
  4. Select **Calculate** and select an option—for example, **Add**.
  5. Optional: to create a new column for the calculated values, select the **Copy to a new column** checkbox. Otherwise, the calculated values override existing values.
  6. Click **Apply**.



The values change based on the calculation. Wrangler adds the corresponding directive as a step in the recipe. For example, if you add the values in each row of the `Q1_Sales` and `Q2_Sales` columns and create a new column called `H1_Sales`, Wrangler adds the following transformation to the recipe:
    
    
    set-column :H1_Sales arithmetic:add(Q1_Sales, Q2_Sales)
    

When you run the data pipeline, Wrangler performs the transformation and creates a new column called `H1_Sales` with the total of `Q1_Sales` and `Q2_Sales`.

### Supported calculations in two columns

You can perform the following numeric calculations on values in each row in two columns:

Function | Description  
---|---  
[Add](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396821110/Add+function) | Adds a positive or negative decimal to a column or adds multiple columns to output the sum of each row.  
[Average](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1827602441/Average+function) | Returns the average of each row in multiple columns.  
[Divide](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396821124/Divide+function) | Divides each value in the column by a positive or negative decimal or divides each value in two columns.  
[Equal](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1795129358/Equal+function) | Boolean function that compares two columns to see if values match, row by row. Returns `true` or `false`.  
[LCM](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1795227649/LCM+function) | Returns the least common multiple of each number in two columns.  
[Max](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1795194881/Max+function) | Returns the maximum value for each row in two columns.  
[Min](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1794867224/Min+function) | Returns the minimum value for each row in two columns.  
[Modulo](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396788297/Modulo+function) | Returns the remainder when dividing each value in the column by a positive decimal or returns the remainder when dividing each value in two columns.  
[Multiply](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396788280/Multiply+function) | Multiplies each value in the column by a positive or negative decimal or multiplies each value in two columns.  
[Subtract](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396821117/Subtract+function) | Subtracts a positive or negative decimal to each value in the column.  
  
## Perform numeric calculations on values in three or more columns

Cloud Data Fusion supports performing numeric calculations on values in three or more columns in version 6.8.0 and later.

To apply a numeric calculation to three or more columns, follow these steps:

  1. [Go to the Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, select the checkbox by two column names.
  3. Go to a column name and click the arrow_drop_down expander arrow.
  4. Select **Calculate** and select an option—for example, **Add**.
  5. Optional: to create a new column for the calculated values, select the **Copy to a new column** checkbox. Otherwise, the calculated values override existing values.
  6. Click **Apply**.



The values change based on the calculation. Wrangler adds the corresponding directive as a step in the recipe. For example, if you add the values in each row of the `Q1_Sales`, `Q2_Sales`, `Q3_Sales`, and `Q4_Sales` columns and create a new column called `2022_Sales`, Wrangler adds the following transformation to the recipe:
    
    
    set-column :2022_Sales arithmetic:add(Q1_Sales, Q2_Sales, Q3_Sales, Q4_Sales)
    

When you run the data pipeline, Wrangler performs the transformation and creates a new column called `2022_Sales` with the total of `Q1_Sales`, `Q2_Sales`, `Q3_Sales`, and `Q4_Sales`.

### Supported calculations in three or more columns

You can perform the following calculations on values in each row in three or more columns:

Function | Description  
---|---  
[Add](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396821110/Add+function) | Adds a positive or negative decimal to a column or adds multiple columns to output the sum of each row.  
[Average](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1827602441/Average+function) | Returns the average of each row in multiple columns.  
[Equal](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1795129358/Equal+function) | Boolean function that compares two columns to see if values match, row by row. Returns `true` or `false`.  
[Max](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1795194881/Max+function) | Returns the maximum value for each row in two columns.  
[Min](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1794867224/Min+function) | Returns the minimum value for each row in two columns.  
[Multiply](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/396788280/Multiply+function) | Multiplies each value in the column by a positive or negative decimal or multiplies each value in two columns.  
  
## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

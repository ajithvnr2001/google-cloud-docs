---
url: https://docs.cloud.google.com/data-studio/tutorial-create-calculated-fields/
title: Tutorial: Create calculated fields in Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:09.323867+00:00
---

# Tutorial: Create calculated fields in Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/tutorial-create-calculated-fields/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Tutorial: Create calculated fields in Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

## Objectives

In this tutorial, you'll accomplish the following:

  * Learn how to create an arithmetic calculated field.
  * Create a conditional expression to evaluate your data and return different results.
  * Learn different approaches to implementing calculated fields.



## Scenario

Suppose you manage an online pet supply store. You might measure sales data, such product codes (SKU), item names, price, and quantity sold. Here's an example:

SKU  |  Item  |  Price  |  Qty Sold   
---|---|---|---  
D-001  |  Healthy Dog Dog Food  |  79.96  |  16   
B-002  |  Parrot Perch  |  74.97  |  8   
B-001  |  Pretty Bird Bird Seed  |  31.96  |  20   
C-002  |  Hungry Kitty Cat Food  |  29.98  |  3   
D-002  |  Playful Puppy Toy  |  17.97  |  11   
C-001  |  Happy Cat Catnip  |  14.97  |  4   
  
Calculated fields in Data Studio can help you manipulate and extend this data. In this exercise, you'll use calculated fields to perform these tasks:

  * Calculate the total value of each order.
  * Apply a discount to orders over a certain amount.
  * Categorize sales into departments.

**Tip:** There can often be more than one way to achieve a particular result with calculated fields, depending on your needs and how you want to use those fields. This tutorial walks you through one approach (using separate fields for the calculations). At the end of this document, you'll find some alternative solutions.

## Sample data

To complete this exercise as written, use the following sample data. Otherwise, use your own data (adjusting the field names accordingly). You'll need access to Google Sheets. Alternatively, you could use the [File Upload connector](https://docs.cloud.google.com/data-studio/upload-csv-files) to import the data into Data Studio.

Copy and paste this data into a text file:
    
    
    SKU,Item,Price,Qty Sold
    D-001,Healthy Dog Dog Food,79.96,16
    B-002,Parrot Perch,74.97,8
    B-001,Pretty Bird Bird Seed,31.96,20
    C-002,Hungry Kitty Cat Food,29.98,3
    D-002,Playful Puppy Toy,17.97,11
    C-001,Happy Cat Catnip,14.97,4
    

## Step 1: Prepare the data

**Objective:** Create a Google Sheet using the sample data shown previously.

  1. Copy the sample data in the previous box.
  2. Open a text editor, paste in the sample data, and save the file as `pet-store-data.csv`. **Important:** Be sure to save this file as plain text; otherwise, Sheets won't be able to import the data. 
     * On Windows, you can use Notepad.
     * On macOS, you can use TextEdit and then select **Format > Make plain text**.
     * On Chrome OS, you can use the Text app or Google Docs and then select **File > Download** and choose **Plain Text**.


  * [Create a new Google Sheet](https://sheet.new).

  * In Sheets, select **File > Import.**

  * Select **Upload** and then upload the sample data file you created in step 2.

  * Select **Replace spreadsheet**.

  * Name your spreadsheet `Pet Store`.




## Step 2: Create a report and add the data

**Objective:** Connect a data source to the Pet Store spreadsheet and add it to a report.

  1. [Create a new report](https://docs.cloud.google.com/data-studio/tutorial-create-a-new-report) in Data Studio.
  2. In the **Add data to report** panel, select the Google Sheets [connector](https://docs.cloud.google.com/data-studio/connector).
  3. Select the `Pet Store` spreadsheet and worksheet you just created.
  4. Leave the default options selected.
  5. Click **ADD**.



In a moment, you'll see the new report, with a table on the canvas that uses fields from the Pet Store data source.

**Tip:** If you don't see the `Pet Store` spreadsheet in the list, try reloading Data Studio.

## Step 3: Create the subtotal field

**Objective:** Create a field that calculates the order subtotal.**Tip:** You can create two kinds of calculated fields: _chart-specific calculated fields_ and _data source calculated fields_. In this tutorial, you'll create data source calculated fields. The main benefits of data source calculated fields are that you can use them in any chart based on this data source and they can refer to other calculated fields.

Learn more [data source versus chart-specific calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields#data_source_versus_chart-specific_calculated_fields).

  1. In the menu, select **Resource > Manage added data sources**.

  2. Locate the **Pet Store** data source and then click ![Edit icon.](https://docs.cloud.google.com/static/data-studio/images/gmcreategoogblue48dp-2020-04-02.png)**EDIT**.

The **data source fields** panel appears.

  3. Click ![](https://docs.cloud.google.com/static/data-studio/images/icaddcirclegoogblue2xweb48dp-2017-11-03.png)**ADD A FIELD**.

The calculated field editor appears.

  4. In **Field Name** , enter `Subtotal`.

  5. In **Formula** , enter `Price * Qty Sold`.

**Tip:** The formula editor autocompletes dimension, metric, or function names as you type. You can also drag fields from the **Available Fields** list into your formula.
  6. Click **SAVE**.

  7. Return to the main data source editor by clicking **ALL FIELDS**.




## Step 4: Create the discount field

**Objective:** Create a field that applies a variable discount rate to orders of a certain value.

Suppose that you want to give different discount rates depending on the value of the order. Create another calculated field, called `Discount`, that evaluates the **Subtotal** field and applies the following discounts.

Subtotal value  |  Discount rate   
---|---  
0 - 99  |  0   
100 - 499  |  5%   
500 or more  |  10%   
  
> **Hints:**
> 
>   * In this step, you'll only calculate the discount. You'll apply it in the following step by multiplying the **Subtotal** field by the **Discount** field.
>   * Use the [`CASE` expression](https://docs.cloud.google.com/data-studio/case-searched) to evaluate the **Subtotal** field. 
>     * Use a `WHEN` clause for each discount rate.
>     * Use an `ELSE` clause to return the full price (0% discount).
>   * Express the discount as a decimal value. For example, a 25% discount would be .25.
> 


####  Solution 
    
    
    CASE
    WHEN Subtotal > 499 THEN .9
    WHEN Subtotal > 100 THEN .95
    ELSE 1
    END

**Note:** `WHEN` clauses are evaluated in order, and the first one that is true is the one whose `THEN` clause is returned.

## Step 5: Create the total field

**Objective:** Create a field that applies the discount rate to the subtotal.

Create another calculated field, called `Total`, that multiples the **Subtotal** field by the **Discount** field.

####  Solution 

`Subtotal * Discount`

## Step 6: Create the department field

**Objective:** Create a calculated field that categorizes sold items into departments.

Create a final calculated field, called `Department`, that parses the SKU field and assigns new values depending on the SKU. You'll group dog, cat, and bird related items into separate departments.

> **Hint:** Use the `CASE` statement again, this time with the [`STARTS_WITH`](https://docs.cloud.google.com/data-studio/startswith) (or [`REGEXP_MATCH`](https://docs.cloud.google.com/data-studio/regexpmatch)) function.

####  Solution 
    
    
    CASE
    WHEN STARTS_WITH(SKU, "C") THEN "Cat"
    WHEN STARTS_WITH(SKU, "D") THEN "Dog"
    WHEN STARTS_WITH(SKU, "B") THEN "Bird"
    ELSE "Misc"
    END

## Step 7: See your data in a report

**Objective:** Visualize your calculated fields.

  1. After saving the **Department** field, on the left, return to the data source editor by clicking **ALL FIELDS**.
  2. Click **DONE** and then close the manage data sources panel.



You can now add your new calculated fields to charts by using these steps:

  1. Select the table.
  2. Add each calculated field you created to the table by dragging them from the **Data** panel onto the table or into the table's **Setup** panel.



## Alternative solutions

The previous solution breaks the problem up into individual chunks and creates discrete fields to handle each chunk, as you've done with the **Subtotal** , **Discount** , and **Total** fields.

Another approach is to perform all the calculations in a single calculated field. For example, you could combine steps 3 - 5 of this tutorial into one field:
    
    
    CASE
    WHEN Price * Qty Sold > 499 THEN (Price * Qty Sold) * .9
    WHEN Price * Qty Sold > 100 THEN (Price * Qty Sold) * .95
    ELSE Price * Qty Sold
    END

There are advantages and disadvantages to each approach:

Breaking down complex formulas into separate fields can make your formulas easier to read and write as well as less error-prone. Separate fields can also be useful in more contexts. For example, using a separate field for the discount rate lets you use that field in other calculations or display it in your reports. One drawback to creating formulas with lots of discrete calculated fields is that it may not be obvious what each one does, so you'll need to edit them individually to see how they are calculated.

On the other hand, centralizing all the logic into one field can make formulas easier to understand and edit. But you also might have to do a lot of repetitive typing, and a complex formula may be harder to extend or maintain. For example, say you had 10 product tiers with different order quantity thresholds. Or say you wanted to use the same discounts for a different product line. In these cases, it might be easier or more efficient to use separate fields for those thresholds and discounts.

### The middle path

This solution blends the two approaches described previously. It keeps the main logic in a single field while breaking out some of the dependent logic into separate fields:
    
    
    CASE
    WHEN Subtotal > Large Order THEN Subtotal * Large Order Discount
    WHEN Subtotal > Medium Order THEN Subtotal * Medium Order Discount
    ELSE Subtotal
    END

For this solution, we've created separate fields to hold values for large and medium orders and corresponding discounts.

![A calculated field called Large Order with 499 entered in the Formula box.](https://docs.cloud.google.com/static/data-studio/images/large-order-2021-04-30.png)

![A calculated field called Large Order Discount with .9 entered in the Formula box.](https://docs.cloud.google.com/static/data-studio/images/large-order-discount-2021-04-30.png)

This solution has the advantage of being easy to read, flexible, and relatively easy to adjust as needed.

## Related resources

  * [About calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Function list](https://docs.cloud.google.com/data-studio/function-list)
  * [Parameters](https://docs.cloud.google.com/data-studio/parameters)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/data-studio/filter-by-multiple-email-addresses-per-row/
title: Filter by multiple email addresses per row \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:20.016635+00:00
---

# Filter by multiple email addresses per row  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/filter-by-multiple-email-addresses-per-row/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)



Send feedback 

#  Filter by multiple email addresses per row Stay organized with collections  Save and categorize content based on your preferences. 

**Prerequisites:** This solution relies on the following tasks in Data Studio: 

  * [Filtering by email address](https://docs.cloud.google.com/data-studio/filter-by-email-address)
  * [Data blending](https://docs.cloud.google.com/data-studio/how-blends-work)
  * [Creating data sources](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [Adding charts to a report](https://docs.cloud.google.com/data-studio/tutorial-add-charts-to-your-report)



Filtering by email address works by comparing the address of the logged in viewer to a field in your data source that contains valid email addresses. For each row in your data, the filter checks whether the viewer's email address matches the address in that row.

Consider the following data:

Email  |  Data   
---|---  
alan@example.com  |  abc   
mary@example.com  |  cde   
alan@example.com  |  efg   
mary@example.com  |  ghi   
  
If this data is filtered by email address, and a user `alan@example.com` views the filtered report, then this user sees only the data `abc` and `efg`. If another user, `mary@example.com`, views the same report, then this users sees the data `cde` and `ghi`.

This approach works if there is a one-to-one relationship between viewers and the data. But what if you also want the user `manager@example.com` to see the data? That is, you want many people to see the same rows of data (a many-to-many relationship.)

Because filtering by email works on only one address per row, you can't include a list of email addresses in your **Email** field. For example, including a list of email addresses in the **Email** field as follows won't work:

Email  |  Data   
---|---  
alan@example.com, manager@example.com, vp@example.com, bigwig@customer.com  |  abc   
  
## Solution: Use data blending

You can create a many-to-many relationship between email addresses and your data by blending a table of addresses with your data, using any common field as a join key.

### Fruit stand example

You manage a produce company, and want show your sales representatives how they are performing at the various fruit stands they service. Multiple sales people can service multiple stands. To filter the data so your sales people only see their data, you could do the following:

#### Step 1: Create an access control list table

In this step, you'll create an access control list (ACL) table that contains the email addresses of the authorized sales people, paired with a data field (a fruit stand name) that can be used as a join key in the blend.

Sales Rep Email  |  Join key   
---|---  
salesrep1@example.com  |  Fruit Stand A   
salesrep2@example.com  |  Fruit Stand A   
salesrep1@example.com  |  Fruit Stand B   
salesrep2@example.com  |  Fruit Stand C   
  
_Access control list (ACL) table_

Note that the user `salesrep1@example.com` can see data for Fruit Stand A and Fruit Stand B, while the user `salesrep2@example.com` can see data for Fruit Stand A and Fruit Stand C.

#### Step 2: Create the data table

The data table tracks the sales each representative made to each fruit stand.

**Note:** This table doesn't need to have the sales rep's email addresses, only the same values as in the join key (the fruit stand name). Also note the name of the join key field is not relevant: blending joins based on the data, not the field name. Fruit Stand  |  Fruit  |  Sales   
---|---|---  
Fruit Stand A  |  Apple  |  50   
Fruit Stand A  |  Banana  |  26   
Fruit Stand A  |  Orange  |  20   
Fruit Stand A  |  Pear  |  93   
Fruit Stand B  |  Apple  |  98   
Fruit Stand B  |  Banana  |  86   
Fruit Stand B  |  Orange  |  7   
Fruit Stand B  |  Pear  |  85   
Fruit Stand C  |  Apple  |  21   
Fruit Stand C  |  Banana  |  61   
Fruit Stand C  |  Orange  |  3   
Fruit Stand C  |  Pear  |  78   
  
_Data table_

#### Step 3: Apply the email filter to the ACL table

To apply the email filter to the ACL table, complete these steps:

  1. [Edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source) for the ACL table.
  2. Click **FILTER BY EMAIL**.
  3. Select the **Sales Rep Email** field for the filter.



![](https://docs.cloud.google.com/static/data-studio/images/acl-table-with-filter-2020-05-14.png)

#### Step 4: Blend the ACL table with the data table

Finally, [blend the ACL table with the data table](https://docs.cloud.google.com/data-studio/create-edit-and-manage-blends). To add the sales rep email as a column to the data table, start from the ACL table and then left-join the data table.

With no email filter applied, you'll see all the records for both sales representatives. However, with the email filter applied, blending the ACL table with the sales data table filters that data according to which sales person is viewing the report. Here's what each representative would see when they view the report:

_Sales Rep 1 sees this:_

Fruit Stand | Fruit | Sales  
---|---|---  
Fruit Stand A | Apple | 50  
Fruit Stand A | Banana | 26  
Fruit Stand A | Orange | 20  
Fruit Stand A | Pear | 93  
Fruit Stand B | Apple | 98  
Fruit Stand B | Banana | 86  
Fruit Stand B | Orange | 7  
Fruit Stand B | Pear | 85  
  
_Sales Rep 2 sees this:_

Fruit Stand | Fruit | Sales  
---|---|---  
Fruit Stand A | Apple | 50  
Fruit Stand A | Banana | 26  
Fruit Stand A | Orange | 20  
Fruit Stand A | Pear | 93  
Fruit Stand C | Apple | 21  
Fruit Stand C | Banana | 61  
Fruit Stand C | Orange | 3  
Fruit Stand C | Pear | 78  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

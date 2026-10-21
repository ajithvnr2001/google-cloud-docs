---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/calculate-resource-usage/
title: Calculate resource usage \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:42:00.292876+00:00
---

# Calculate resource usage  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/calculate-resource-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Calculate resource usage Stay organized with collections  Save and categorize content based on your preferences. 

The pricing calculator estimates the cost of using Google Distributed Cloud (GDC) air-gapped resources in the GDC console. The calculator is in the table format with each column representing the following:

  * **SKU:** The name of the resource represented as a stock keeping unit (SKU).
  * **Quantity:** An input field column for citing the quantity of a specific SKU.
  * **Cost:** The total estimated cost and exclusive taxes that show in the calculator's footer.

**Note:** The calculator represents the **SKU** and **Quantity** columns in the **Compute and Infrastructure security** row as **Server** and **Number of servers**.



As you enter quantities into input fields for each line item SKU, the cost column updates with new values.

## Before you begin

To get the permissions you need to manage billing reports, ask your Organization IAM admin to grant you the corresponding role in the applicable namespace.

## Use the pricing calculator

To use the calculator, complete the following steps:

  1. Enter the quantity of resources required for a particular SKU into the corresponding input field. The following image shows entering a quantity into the **Number of servers** field:

![Pricing Calculator enter quantity of resources](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/billing-number-of-servers-column.png)

  2. Press `ENTER`. You see the line item cost update.

![Pricing Calculator quantity column updates](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/billing-cost-column-updates.png)

The total estimated cost in the footer also updates. ![Pricing Calculator total cost footer updates](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/billing-total-estimated-cost-updates.png)




The cost for each line item is a cumulative total accrued over a time period you can adjust only on monthly intervals. The calculator sets the default time period to one month, and it calculates the total estimated cost for a one month period. See Set the time period to adjust the time period of calculation.

## SKU cost types

The following explains the SKU cost types available in the pricing calculator:

  * **Flat rate:** The cumulative SKU costs that accrue over the selected time period.

  * **One-time charge:** The SKU cost you add once to the total cost regardless of the selected time period. This SKU cost is in contrast to the Flat Rate SKU cost, which accumulates over time. One-time charge SKUs have a text indicator in the name column.

  * **Support:** The SKU costs have both a base fee and a variable percentage fee component.

    * The base fee is a Flat rate support cost.
    * The variable percentage fee is calculated on a percentage of the total Flat rate costs, and doesn't include the One-time charge SKU costs and the Support base fee.



### Set the time period

You can attain a longer term GDC cost projection by adjusting the calculator's selected time period. The selector's available period options are as follows:

  * **1 month**
  * **3 months**
  * **6 months**
  * **9 months**
  * **1 year**
  * **Date Range** for a custom date.



To adjust the selected time period, complete the following steps:

  1. Click the time period _edit_ **Edit** icon in the footer.

  2. Select your preferred time period.

  3. Click **Confirm**.

  4. The **Cost** column updates along with the time period and total estimated cost.




For custom date ranges, the calculator adjusts the Flat Rate SKU costs based on month intervals, rounding up to include the latest interval. For example:

  * Selecting a range of November 15 to December 14 is equivalent to a one month period.
  * Selecting a range of November 15 to December 15 is equivalent to a two month period.



## Export to local file and print

You can export the Pricing Calculator data into comma-separated-value (CSV) and portable document file (PDF) format. These formats let you share the data for other programs to access them.

### Export to CSV or PDF

To export the calculator data, complete the following:

  1. In the footer, click **Export** , and then select **CSV** or **PDF**.

![Pricing Calculator click Export button](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/billing-calculator-export-csv-or-pdf.png)

  2. A file containing the Pricing Calculator data saves to your local computer.




### Optional: Print local file

To print the data, do the following:

  * **CSV**

    1. Import the newly saved file into a program that offers a structured table format, such as a spreadsheet.
    2. Format the data to your preference, and print.
  * **PDF**

    1. Locate the newly saved file on your local computer.
    2. Print the file following the steps for your local application or operating system.



## Troubleshooting

If the pricing calculator is not loading, contact your IO to validate the category fields in all the SKU descriptions. This is the list of valid categories:

  1. Backup

  2. Compute

  3. Databases

  4. DeveloperTools

  5. GKE

  6. Networking

  7. Observability

  8. Security

  9. Storage

  10. StorageTransfer

  11. VertexAIML

  12. Marketplace

  13. Edge

  14. Support




Any other categories in the SKU description will lead to failure in loading the pricing calculator. The IO should change the category field in the SKU description CR to match any one in this list.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

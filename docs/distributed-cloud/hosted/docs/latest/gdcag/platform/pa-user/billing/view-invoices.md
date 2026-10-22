---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/view-invoices/
title: View invoices \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:50.926857+00:00
---

# View invoices  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/view-invoices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  View invoices Stay organized with collections  Save and categorize content based on your preferences. 

The Spend Reports dashboard is a cost management tool to help you understand the costs that reconcile to your invoice. The dashboard displays a detailed view of your costs for an invoice in a date range that includes the SKU description. You can also export the report in the dashboard to a comma separated values (CSV) file.

To get the permissions that you need to view the Invoice Reports dashboard, ask your IAM Org Admin to grant you the corresponding project viewer role for the `platform-obs` project.

To access the Spend Reports dashboard and get an invoice using the `kubectl` CLI, work through the following steps:

### Console

  1. Sign into the GDC console.
  2. In the navigation menu, select **Billing > Reports**. The **Billing reports** page opens. 
  3. In the **Spend Reports** section, click **View dashboard** to open the Spend reports dashboard. 



### CLI

**Note:** To get the permissions that you need to get an invoice, ask your IAM Org Admin to grant you the Billing Viewer (`billing-viewer`) role for the `billing-system` namespace.

To list spend reports, use the following command:
    
    
    gdcloud system billing spend list
    

For more information, see [gdcloud system billing spend list](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/infrastructure/gdcloud-system-reference/gdcloud-system-billing-spend-list).

To get a spend report, use the following command:
    
    
    gdcloud system billing spend get --invoice-id=invoice_id
    

Replace `invoice_id` with the ID for the invoice to use in the spend report.

For more information, see [gdcloud system billing spend get](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/infrastructure/gdcloud-system-reference/gdcloud-system-billing-spend-get).

To fetch the invoice using a kubectl command, run the following:
    
    
    kubectl get invoice -n billing-system --kubeconfig MGMT_API_SERVER_KUBECONFIG
    

Replace `MGMT_API_SERVER_KUBECONFIG` with the Management API server kubeconfig file.

The Spend Reports dashboard consists of the following tables and graphs:

### Spend Reports Table

The **Spend Reports Table** is a table that presents a detailed view of your costs for an invoice. The **Spend Reports Table** displays the following columns:

Column | Description  
---|---  
**Invoice ID** | The unique ID of the invoice from a specific `invoice_line_item`.  
**Billing Account ID** | Your GDC account ID number.  
**SKU** | The description of what the SKU represents.  
**SKU ID** | The ID number of the SKU.  
**Usage start date** | The first day of the month when starting a specific `invoice_line_item`.  
**Usage end date** | The final day of the month when ending a specific `invoice_line_item`.  
**Unit price ($)** | The cost per quantity in United States Dollar (USD) amount.   
  
For example, the unit price for Compute depends on the amount of servers you used.  
**Usage amount** | The amount of each unit you used.  
**Usage unit** | The type of unit you used.  
**Cost** | The total cost of each SKU by line.  
  
### Total Cost by Product Family

The **Total Cost by Product Family** table presents a detailed view of your costs for an invoice. The **Total Cost by Product Family** table displays the following columns:

Column | Description  
---|---  
**Invoice ID** | The unique ID of the invoice from a specific `invoice_line_item`.  
**Billing Account ID** | Your GDC account ID number.  
**Payment Account ID** | The ID of your organization payment account.  
**Product Family** | The product group type. For example, compute.  
**SKU** | The description of what the SKU represents.  
**SKU ID** | The ID number of the SKU.  
**Cost** | The cumulative cost of the specified product family SKU.  
**Tier Start Usage** | The starting unit of the tier that applies to that particular line item. This value is empty if there is a flatrate SKU.  
  
### Total Cost by Cloud Service Model

The **Total Cost by Cloud Service Model** table presents a detailed view of your costs for a product type. The **Total Cost by Cloud Service Model** table displays the following columns:

Column | Description  
---|---  
**Invoice ID** | The unique ID of the invoice from a specific `invoice_line_item`.  
**Billing Account ID** | Your GDC account ID number.  
**Payment Account ID** | The ID of your organization payment account.  
**Cloud Service Model** | The cloud service category. For example, IaaS  
**SKU** | The description of what the SKU represents.  
**SKU ID** | The ID number of the SKU.  
**Cost** | The cumulative cost of the specified service model SKU.  
**Tier Start Usage** | The starting unit of the tier that applies to that particular line item. This value is empty if there is a flatrate SKU.  
  
### Cost by Month

The **Cost by Month** graph displays graphs of your costs in a monthly view. The **Cost by Month** graph informs you of how much your costs have increased or decreased in a month by month basis. The monitoring instance defaults the monthly view to **All**.

To customize the view by month, do the following:

  1. In the menu bar, set your preferred time range from the **Timepicker** drop-down.
  2. Select your preferred period of time.



### Cumulative Total Cost

The **Cumulative Total Cost** graph scales your cumulative total cost in a given timeline.

### Filter invoice data

You can filter values you see in the Invoice Reports dashboard through the menu bar. The menu bar lets you customize the values you see in the **Invoices Table** , **Cost by Month** and **Cumulative Total Cost** sections. The menu bar consists of the following tabs:

Tab | Description  
---|---  
**Invoice date** | A drop-down that filters the **Spend Reports Table** and **Total Cost (USD)** column on your preferred date.  
**Billing Account ID** | Your GDC account ID number.  
**SKU** | A drop-down that lets you select which SKU to view.  
**Threshold (USD)** | An input field you add in USD to cap the dollar amount of the **Cumulative Total Cost** graph.  
  
### Export and print invoices

You can export and print invoices to a portable document format (PDF) using either the dashboard user interface or the CLI.

###  Dashboard 

To export an invoice to PDF and print, do the following:

  1. From the navigation menu, click the **Dashboards** icon.
  2. In the **Billing** folder, select the **Spend Reports** dashboard.
  3. From the menu bar, select an invoice date from the **Invoice Date** drop-down, and a billing account ID number from the **Billing Account ID** drop-down. After selecting these values, the dashboard generates and auto-fills the following input fields:

![Spend dashboard shows input field values to export the invoice](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/billing-invoice-viper0.png)

Input field | Description  
---|---  
**Organization name** | The name of your organization.  
**Invoice ID** | The ID of the invoice.  
**Generated date** | The date when you created the exported invoice.  
**Payment Account ID** | The ID of your organization payment account.  
**Billing Account ID** | Your GDC account ID number.  
**Billing time range** | The invoice dates you selected to export.  
**Currency** | The asset type abbreviated by country. For example: **USD**.  
**Total cost** | The cumulative costs of all SKUs in the invoice.  
  4. From your keyboard, press `V` to preview the entire dashboard panel.

  5. Press `CTRL + P` or `Command + P` to open your browser's default print setting.

  6. Select **Save to PDF** to save the invoice to an exported PDF file in your preferred directory. You can print this PDF file at any time.

![Invoice PDF showing values of the selected invoice to export](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/pa_invoice_dashboard_billing_invoice.png)




### gdcloud

To export a spend report, use the `gdcloud system billing spend export` command.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/looker/docs/publishing-looks-with-public-urls/
title: Public sharing, importing, and embedding of Looks \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:13.943934+00:00
---

# Public sharing, importing, and embedding of Looks  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/publishing-looks-with-public-urls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Public sharing, importing, and embedding of Looks Stay organized with collections  Save and categorize content based on your preferences. 

Looker admins and other users with the `create_public_looks` permission can enable public access for a [saved Look](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks). For users to be able to enable public access for a Look, an admin must also enable [the **Public URLs** setting](https://docs.cloud.google.com/looker/docs/managing-business-user-features#public_sharing,_importing,_and_embedding).

The first step in any method of public sharing, importing, or embedding is to enable public access on the Look you want to share.

## Enabling public access for a specific Look

Public access lets you share your Look with a broader audience. When public access is enabled on a Look, Looker provides a list of shortened, unguessable public URLs. Those URLs allow anyone that you share them with to view the Look's data or its visualization.

To enable public access for a saved Look:

  1. If you are in [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode), select **Exit Development Mode**.
  2. Navigate to the Look you want to share.
  3. Select the Look's gear menu.
  4. Select **Edit Settings**. Looker displays the **Look Settings** window. ![](https://docs.cloud.google.com/static/looker/docs/images/browse-looks-public-access-on-2218.png)
  5. In the **Look Settings** window, turn on the **Public Access** option.
  6. Select **Save**. This will make the previously grayed out URLs for the Look accessible to you.



Once you have enabled public access for the Look, you can copy its URLs from the following sections of the **Look Settings** window, allowing you to use the URLs in the following ways:

  * **URL** : Share the Look's data formatted as TXT, CSV, JSON, or HTML by sharing the Look's URL.
  * **Embed Visualization** : Publicly embed the Look's visualization in an HTML page with `<iframe>` code.
  * **Embed Data Table** : Publicly embed the Look's data table in an HTML page with `<iframe>` code.
  * **Google Spreadsheet** : Export the Look's data into Google Sheets.
  * **Excel Web Query File** : Export the Look's data into Excel.



The following sections walk you through each option.

## Sharing Look results through a public URL

To share Look data through a public URL, copy and use the URL from the **URL** section of the **Look Settings** window. The 32-character hash that appears in the URL should make it unguessable, so no one will be able to access this data unless you explicitly provide them with this URL.

> Anyone who has the URL will be able to access the data without logging in to Looker. Therefore, don't put sensitive data into any public Look.

### Changing the format

You can share and access the data in text, JSON, CSV, and HTML formats by changing the format extension of the URL. For example:

  * https://instance_name.looker.com/looks/tRpghtMTZc6ByPHVMJX8hk9FspZx3VjS**.txt**
  * https://instance_name.looker.com/looks/tRpghtMTZc6ByPHVMJX8hk9FspZx3VjS**.json**
  * https://instance_name.looker.com/looks/tRpghtMTZc6ByPHVMJX8hk9FspZx3VjS**.csv**
  * https://instance_name.looker.com/looks/tRpghtMTZc6ByPHVMJX8hk9FspZx3VjS**.html**



### Default application of visualization and `value_format` settings

Looker applies any [`value_format`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format) settings that you've put in place. Looker also applies some visualization settings to your public URLs, causing your data to appear similar to a [table chart](https://docs.cloud.google.com/looker/docs/legacy-table-options). Any of the following [Plot](https://docs.cloud.google.com/looker/docs/legacy-table-options#plot_menu_options) and [Series](https://docs.cloud.google.com/looker/docs/legacy-table-options#series_menu_options) visualization menu settings for the Look will be applied to the public URLs:

  * [Show Row Numbers](https://docs.cloud.google.com/looker/docs/legacy-table-options#show_row_numbers)
  * [Hide Totals](https://docs.cloud.google.com/looker/docs/legacy-table-options#hide_totals)
  * [Hide Row Totals](https://docs.cloud.google.com/looker/docs/legacy-table-options#hide_row_totals)
  * [Limit Displayed Rows](https://docs.cloud.google.com/looker/docs/legacy-table-options#limit_displayed_rows) to a maximum of 500 rows shown or hidden
  * [Show Full Field Name](https://docs.cloud.google.com/looker/docs/legacy-table-options#show_full_field_name)
  * [Custom labels](https://docs.cloud.google.com/looker/docs/legacy-table-options#customizations) for each column (note that JSON files will always use raw field names, not the field label)



### Removing visualization or `value_format` options

The application of visualization options shows up in the URL as the `apply_vis=true` argument. If you don't want visualization options applied, remove the `apply_vis=true` from the URL.

The application of any [`value_format`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format) settings shows up in the URL as the `apply_formatting=true` argument. If you don't want `value_format` settings to be applied, remove the `apply_formatting=true` from the URL.

The following sample URL shows both arguments (scroll to see the full text):
    
    
    https://instance_name.looker.com/looks/JRJTR5dDYZRVX56vyrmnpKn2HRbnhsMq.txt?apply_formatting=true&apply_vis=true
    

## Public embedding with `iframe` tag

You can embed a Look's visualization or data table into a website using an HTML `iframe` tag.

If you want to embed the visualization that is saved with your Look, use the **Embed Visualization** `iframe` code from the **Look Settings** window.

If you want to embed the data table that is saved with your Look, use the **Embed Data Table** `iframe` code from the **Look Settings** window.

> Public embedded tables cannot be sorted.

It is also possible to view an embedded visualization or data table without inserting the HTML `iframe` tag into your HTML code.

For other types of embedding, see the [Private embedding](https://docs.cloud.google.com/looker/docs/private-embedding) and [Signed embedding](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding) documentation pages.

### Viewing an embedded visualization or data table without an iframe

To view an embedded visualization or data table without inserting it with an HTML `iframe` tag, you can paste the embed link in your browser. For example, suppose the iframe link for an embedded visualization looks like the following:
    
    
    <iframe src="https://mycompany.looker.com/embed/public/CNdbvTys8ZVgQn423Sf4y2GYhy6b6522" width="600" height="338" frameborder="0"></iframe>
    

In this example, you can view just the embedded visualization by pasting the following URL into your browser:
    
    
    https://mycompany.looker.com/embed/public/CNdbvTys8ZVgQn423Sf4y2GYhy6b6522
    

## Exporting to Google Sheets

You can also export a Look's data directly into a Google Sheet without having to download it first.

> You can also export data directly to Google Sheets using the Google Sheets action from the [Looker Action Hub](https://docs.cloud.google.com/looker/docs/action-hub#the_looker_action_hub) rather than implementing the following method. See the [Looker Actions — Google Sheets](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-google-sheets-integration) Best Practices page for more information.

To import the data into a Google spreadsheet, copy the **Google Spreadsheet** formula from the **Look Settings** window. Paste the formula into the cell of the Google spreadsheet where you want the upper-left cell of your data to appear, then hit **Enter**. You might need to refresh the Sheet to see your imported data.

### Tips and notes for Google spreadsheets

There are some things to keep in mind when using this method to export data to a Google Sheet:

  * Google Sheets are [limited to 5 million cells](https://support.google.com/drive/answer/37603) for the entire Sheet, so your data table's columns, rows, or tabs cannot exceed that limit.
  * The URL in the Google spreadsheet function points to the saved Look rather than to a specific query. Although this lets you make changes to the data exporting to the spreadsheet, be careful when you update a Look on which a spreadsheet relies. For example, if you overwrite a saved Look, your Google spreadsheet will begin to populate with the new format.
  * Looker recommends importing a single Look to any given worksheet (tab) in your Google Sheet. The Google array functions — like `VLOOKUP`, `HLOOKUP`, and `ARRAYFORMULA` — can help you filter, extract, and copy data between Sheets. You can also place results on separate Sheets, then build one main Sheet that graphs it all.
  * The `ImportXML` function is subject to changes within Google Sheets; these changes may have downstream impacts to your workflow in Looker.
  * You may need to force the data in the Sheet to refresh. See the [Exporting Data to Google Sheets](https://www.googlecloudcommunity.com/gc/Technical-Tips-Tricks/Exporting-Data-to-Google-Sheets/ta-p/588441) Community post for more information.



## Exporting to Excel

To import the data into Microsoft Excel, you will need to download a `.iqy` file by completing these steps:

  1. Enable public access for the Look as described in the **Enabling public access for a specific Look** section.
  2. Save these settings. The **Look Settings** option for Excel Web Query File will now show a download link next to it.
  3. Select **Download** to download the `.iqy` file to your computer.



Read the following instructions for using Looker with Excel spreadsheets on a Mac for more information on how to use the `.iqy` file depending on your version of Excel.

> Both Google and Excel will only interact with servers that have valid SSL certificates. If your Looker instance is hosted by Looker this won't be a concern. However, if you have a customer-hosted Looker instance, your admins will need to have followed [these instructions for configuring an SSL certificate for proper HTTPS](https://docs.cloud.google.com/looker/docs/ssl-certificate-for-proper-https) when they initially set up Looker.

### Tips and notes for Microsoft Excel spreadsheets to Mac Office 2011

There are some things to keep in mind when using Looker in combination with Excel spreadsheets on a Mac.

#### Initial data import

  1. Download the `.iqy` file to a known location on your computer.
  2. From the **Data** drop-down menu in Excel's menu bar, select **Get External Data** > **Run Saved Query**.
  3. From the **Enable** drop-down menu in the prompt, select **Query Files**.
  4. Navigate to the saved `.iqy` file.
  5. Select **Get Data**.
  6. Select a location in the spreadsheet to place data and select **OK**.



#### Refresh Data

  1. Select Excel's **Data** tab.
  2. Select the **Refresh Data** button.



### Tips and notes for Microsoft Excel spreadsheets to Windows Office 2013

There are some things to keep in mind when using Looker in combination with Excel spreadsheets on Windows.

#### Initial data import

  1. Download the `.iqy` file to a known location on your computer.
  2. Select the **Data** tab in Excel.
  3. Select the **Existing Connection** button.
  4. Select **Browse for More**.
  5. Navigate to the `.iqy` file.
  6. Select **Open**.
  7. Select location in spreadsheet to place data.



#### Refresh Data

  1. Select Excel's **Data** tab.
  2. Select the **Refresh Data** button.



## For admins: Enabling public URLs

For any of the features that are described on this documentation page to work, you must [enable **Public URLs**](https://docs.cloud.google.com/looker/docs/managing-business-user-features#public_sharing,_importing,_and_embedding).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

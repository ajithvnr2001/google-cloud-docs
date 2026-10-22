---
url: https://docs.cloud.google.com/data-studio/connect-to-looker/
title: Connect to Looker \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:32.274038+00:00
---

# Connect to Looker  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-looker/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to Looker Stay organized with collections  Save and categorize content based on your preferences. 

The Looker [connector](https://docs.cloud.google.com/data-studio/connector) lets you add a Looker [Explore](https://docs.cloud.google.com/looker/docs/glossary#explore) as a [data source](https://docs.cloud.google.com/data-studio/data-source) so that you can analyze Looker data from within Data Studio. This document describes how to create a data source with data from a Looker (original) instance or from a Looker (Google Cloud core) instance that uses a public IP network connection.

**Note:** If you are using [Data Studio Pro](https://docs.cloud.google.com/data-studio/about-pro), you can also use the Looker instance ID to connect to a Looker (Google Cloud core) [private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options) instance. Your Data Studio Pro Google Cloud project must be in the same network as the Google Cloud project that hosts the Looker (Google Cloud core) instance. For more information, see the [Connecting to a private connections instance from a Data Studio Pro report or a Looker report](https://docs.cloud.google.com/looker/docs/looker-core-connect-to-private-ip-lsp-sil) documentation page.

## Before you begin

Your Looker instance must fulfill certain [requirements to be eligible to connect to Data Studio](https://docs.cloud.google.com/data-studio/limits-of-the-looker-connector). Additionally, a Looker [Admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) must enable the [Data Studio BI connector](https://docs.cloud.google.com/looker/docs/bi-connectors#looker_studio) in the **Platform** section of the instance's **Admin** panel.

To add a Looker Explore as a data source in Data Studio, you must have [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permissions for the model that contains the Explore.

A Looker data source uses [viewer's data credentials](https://docs.cloud.google.com/data-studio/data-credentials), so any user viewing Looker data in Data Studio must have at least [`access_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#access_data) and [`clear_cache_refresh`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#clear_cache_refresh) permissions for the model that contains the data source's Looker Explore.

Learn more about the [Looker permissions that are required](https://docs.cloud.google.com/data-studio/overview-of-looker-connector-permissions) to enable the Looker connector, create a Looker data source, and view Looker data in Data Studio.

## Use the Looker connector to add a Looker Explore as a data source

To add a Looker Explore as a data source for a Data Studio report, you must complete the following tasks:

  1. Connect to a Looker instance and link your Looker and Google accounts.
  2. Select a Looker model and Explore.



Each Looker data source represents a single Looker Explore. You can add multiple Explores to a Data Studio report, even those that don't belong to the same Looker model.

### Connect to a Looker instance

To connect to a Looker instance, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. On the Data Studio home page, in the top left, click ![](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** , and then select **Data Source**.
  3. Select the Looker connector.
  4. Enter the URL for the Looker instance that contains the Looker Explore that you want to connect to. This is the URL that you use to access Looker on your browser.

**Note:** If you are using [Data Studio Pro](https://docs.cloud.google.com/data-studio/about-pro), you can also use the Looker instance ID to connect to a Looker (Google Cloud core) [private IP](https://docs.cloud.google.com/looker/docs/looker-core-networking-options) instance that is on the same network as Data Studio. For more information, see the [Connecting to a private IP instance from Data Studio Pro, Looker reports, or Connected Sheets](https://docs.cloud.google.com/looker/docs/looker-core-connect-to-private-ip-lsp-looker-reports) documentation page.
     1. If the instance URL belongs to a Looker instance that doesn't meet the Looker connector requirements, Data Studio displays the message `Invalid Looker URL or the Looker URL does not support account linking. Please use different Looker URL.`
     2. If you have previously connected a Looker instance as a data source, that Looker instance name appears under **Saved Looker Instances**. You can click the name of a Looker instance and proceed to the section on selecting a model.
  5. Click **Connect Looker Account**.

  6. In the authorization menu, click **Agree and continue** to link your Google Account credentials to your Looker account credentials. You can link one Google Account to one Looker account for each Looker instance that you connect to Data Studio.

  7. In the Looker instance menu, select **AUTHENTICATE** ​​.


**Note:** When you link your accounts, the instance URL is stored by Google outside of the Looker environment. You can unlink your Google and Looker accounts from the [Account Linking](https://myaccount.google.com/accountlinking) page in your Google Account profile. Unlinking your accounts will prevent the data source from connecting to Looker data.

Now you're ready to select a model–Explore pair to connect to as a data source for your report.

### Select a model and an Explore

Once you have connected to a Looker instance, a list of models that are defined in that instance automatically populates a new panel that is called **Models** in the **Add data to report** windows.

To select a model, follow these steps:

  1. In the **Models** panel, scroll the list of pre-populated models, or click the magnifying glass icon to open a search field where you can enter the name of a specific model. Hover over a model name to see the [model filename](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files) as it appears in the Looker project. Click the model name to select the model. A new panel will populate with the list of Explores that are defined within that model.
  2. To select an Explore, scroll the list or click the magnifying glass icon to open a search field where you can enter the name of a specific Explore. Hover over an Explore name to see the [`explore` parameter value](https://docs.cloud.google.com/looker/docs/glossary#explore-parameter) as it's declared in the [model file](https://docs.cloud.google.com/looker/docs/glossary#model-file). Click the Explore name to select the Explore.
  3. Click **CONNECT**.



It may take a few minutes to connect to the Looker Explore. Once it is connected, the data source has the format `Explore — model`. [Learn more about how Looker Explores appear and behave in Data Studio reports.](https://docs.cloud.google.com/data-studio/looker-explore-data-on-a-report)

### Add the Looker data source to a report

To add the data source to a report, you can choose one of the following options:

  * Select **CREATE REPORT** to [create a report](https://docs.cloud.google.com/data-studio/tutorial-create-a-new-report) that includes a chart that is pre-populated with some fields from this data source.
  * Select **EXPLORE** to open a blank report that uses the Looker data source.



You're now ready to [view and interact with Looker data](https://docs.cloud.google.com/data-studio/view-and-interact-with-looker-data-on-a-report) in your report.

Once you have created your Looker data source and added it to a report, Data Studio displays a list of the fields that are associated with the Looker Explore. From this list, you can perform the following tasks:

  * Change the [data source type](https://docs.cloud.google.com/data-studio/embedded-data-sources) from an embedded data source to a reusable data source.
  * Update the data source [data freshness](https://docs.cloud.google.com/data-studio/manage-data-freshness). The the default data freshness value for a Looker data source is 12 hours.
  * Manage whether other report editors can [edit the field definitions](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports) at the chart level for reports that use this data source.
  * [Make a copy of the data source](https://docs.cloud.google.com/data-studio/copy-a-data-source).



## Support for VPC Service Controls in Looker (Google Cloud core)

Data Studio can connect to Looker (Google Cloud core) projects that are protected by VPC Service Controls (VPC-SC) perimeters through [viewer IP-based access levels](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels). The Looker connector passes the report viewer's IP address to Looker (Google Cloud core), which can then enforce any IP-based access levels that have been set up.

**Note:** Scheduled email delivery doesn't work with data that is protected using IP-based access levels with VPC Service Controls. (This is because Data Studio cannot pass the email recipient's IP address to Looker (Google Cloud core) to assess IP-based access levels when generating the email.)

## Related resources

  * [Create a data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [Creating and editing Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores)
  * [Viewing and interacting with Explores](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores)
  * [Connecting to Data Studio](https://docs.cloud.google.com/looker/docs/looker-studio-connector)
  * [Looker and Data Studio shared terms and concepts](https://docs.cloud.google.com/looker/docs/looker-and-studio-shared-terms-glossary)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

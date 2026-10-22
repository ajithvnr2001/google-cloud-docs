---
url: https://docs.cloud.google.com/data-studio/connect-to-google-ads/
title: Connect to Google Ads \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:33.471785+00:00
---

# Connect to Google Ads  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-google-ads/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to Google Ads Stay organized with collections  Save and categorize content based on your preferences. 

Google Ads lets you reach potential customers with online ads. The Data Studio Google Ads connector enables Google Ads advertisers to access performance report data within Data Studio.

## How to connect to Google Ads

A Data Studio data source can connect to any one Google Ads account to which you have access. Google Ads users with manager (MCC) accounts can connect to and report on up to 50 sub-accounts per data source.

### Select an individual account

  1. [Sign in to Data Studio.](https://datastudio.google.com)

  2. On the Data Studio home page, in the top left, click add **Create** , and then select **Data Source**.

  3. Select the **Google Ads** connector.

  4. If prompted to grant Data Studio access to your account, click **AUTHORIZE**.

> You can [revoke this access](https://support.google.com/accounts/answer/14012355) at any time.

  5. Click **ALL ACCOUNTS**.

  6. Select an account. You can search by account ID or by name.

  7. Select **Overall Account Fields**.

The **Overall Account Fields** selection combines all your Google Ads fields into a single list for a selected customer account, which lets you combine the dimensions and metrics from any of your Google Ads reports in your Data Studio reports.

  8. Click **CONNECT**.

     1. The data source fields panel appears.
     2. The data source is now connected to your [dataset](https://docs.cloud.google.com/data-studio/dataset).



### Select manager (MCC) accounts

If you have access to a Google Ads manager account, you can select **MANAGER ACCOUNTS** in the **Accounts** panel. Select the account and any sub-accounts to include in this data source. You can select up to 50 sub-accounts.

**Important:** If you select a manager account, you must have access in Google Ads to that manager account and to any sub-accounts that you select. Report viewers must also have access to the manager account and all selected sub-accounts to view the data. Access to the selected sub-accounts alone is not sufficient if the viewer doesn't also have access to the manager account.

#### Currency conversion

Use the currency drop-down menu on the right to filter your accounts according to currency type.

If you select **All currencies** and choose accounts that use different currencies, Data Studio converts all revenue-related fields to the currency of the top-level manager (MCC) account. See [About converting currencies for manager accounts](https://support.google.com/google-ads/answer/7379939) for more details about currency conversion.

## Configure the data source

The data source fields panel is where you configure the data source by renaming fields and adding descriptions, adding calculated fields, and changing data types and aggregations. Learn more about [working with data source fields](https://docs.cloud.google.com/data-studio/model-your-data).

## Control who sees the data

At the top of the fields panel, you can change the data credentials. Credentials control who can see the data that this data source provides.

**OWNER'S CREDENTIALS** let other people view or create reports that use this data without requiring them to have their own access to the dataset.

**VIEWER'S CREDENTIALS** , on the other hand, require each user of the data source to provide their own credentials to access the dataset.

**SERVICE ACCOUNT CREDENTIALS** rely on a special type of Google Account that represents a non-human user that can authenticate and be authorized to access data.

[Learn more about data credentials](https://docs.cloud.google.com/data-studio/data-credentials-article).

## Create a new report from the data source

To create a new report from the data source, follow these steps:

  1. In the upper right, click **CREATE REPORT**. The report editor appears.
  2. Click **ADD TO REPORT**. 
     1. This action adds the data source to the report.
     2. You can now create charts and controls that get their data from this data source.



### New to Data Studio?

Take the [Create a report tutorial](https://docs.cloud.google.com/data-studio/tutorial-create-a-new-report).

**Tip: Want to use this data source with different accounts?** Try adding a data control. 

Data controls give report viewers a way to select the account that provides the data that they want to see in a report. Data controls can eliminate the need to create separate reports and data sources for your various accounts. [Learn more about data controls](https://docs.cloud.google.com/data-studio/data-control).

## Notes

When connecting to Google Ads, keep the following notes and limitations in mind.

#### Zero impression entities

Entities, such as AdGroup or Campaign, with zero impressions won't appear in Google Ads data sources.

#### Creative assets reporting

The Google Ads connector for Data Studio is aligned with the public Google Ads API for creative assets reporting. To return accurate results when using **Clicks** or **Impressions** metrics in combination with creative asset dimensions, be sure to also include the **Ad Type** and **Asset ID** dimensions in your chart. Otherwise, the chart may show inaccurate results. Charts that aren't correctly configured will display a message that warns you about the invalid combination of dimensions and metrics.

#### Ads Location Extension data

Starting on May 4, 2026, the following location extension fields in the Google Ads and New Search Ads 360 connectors were deprecated and stopped serving data:

  * Affiliate location address line 1
  * Affiliate location address line 2
  * Affiliate location business name
  * Affiliate location city
  * Affiliate location country code
  * Affiliate location phone number
  * Affiliate location postal code
  * Affiliate location province
  * Store location address line 1
  * Store location address line 2
  * Store location business name
  * Store location city
  * Store location country code
  * Store location phone number
  * Store location postal code
  * Store location province



Reports that use these fields return an error. To avoid disruption, you must update your reports and data sources to use the corresponding **Asset location** fields:

  * Asset location address line 1
  * Asset location address line 2
  * Asset location business name
  * Asset location city
  * Asset location country code
  * Asset location phone number
  * Asset location postal code
  * Asset location province



[Learn more about Ads location assets](https://support.google.com/google-ads/answer/2404182).

#### Auction Insights data

Starting on August 24, 2024, Auction Insights fields won't be available for new data sources in Data Studio. Starting on September 23, 2024, existing data sources will lose access to Auction Insights fields. To prevent your reports breaking, we recommend removing these fields from your reports and charts:

  * **Auction Insight - Domain**
  * **Auction Insight - avg. position**
  * **Abs. top of page rate**
  * **Position above rate**
  * **Impr. share**
  * **Outranking Share**
  * **Overlap Rate**
  * **Top of page rate**
  * **Auction Insight - Store display name**
  * **Shopping impression share**
  * **Shopping outranking share**
  * **Shopping overlap Rate**



> **Frequently asked questions about Auction Insights deprecation**
> 
> _Why is Action Insights data being removed from Data Studio?_
> 
> The removal of this data is an update to the Data Studio product.
> 
> _Can I get an exception from this product change?_
> 
> No. Auction Insights data will be removed from all Data Studio reports without exception.
> 
> _Will this affect existing reports that have Auction Insights data?_
> 
> Yes. On September 23, 2024, the data connectors on Data Studio will no longer return Auction Insights data. The data won't be available for new reports starting on August 24, 2024.
> 
> _Will the rest of my report continue to function properly?_
> 
> It depends on whether the specific charts include Auction Insights data. If your report includes Auction Insights data, it may no longer function properly.
> 
> _Does it matter which connector I use to get Auction Insights?_
> 
> No. This change will impact Auction Insights data regardless of the connector that is used to access it. These include (but are not limited to) the Google Ads, BigQuery, and Google Sheets connectors.

## Related resources

[Learn more about Google Ads](https://ads.google.com)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

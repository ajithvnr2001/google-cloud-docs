---
url: https://docs.cloud.google.com/marketplace/docs/partners/reports/report-VM-customer-tracking/
title: Virtual machine (VM) customer tracking reports \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:22.603661+00:00
---

# Virtual machine (VM) customer tracking reports  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/reports/report-VM-customer-tracking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Virtual machine (VM) customer tracking reports Stay organized with collections  Save and categorize content based on your preferences. 

For VM products, you can get the _VM customer tracking report_ that includes customers' information, such as email addresses and phone numbers. To access the VM customer tracking report, visit the destination that you specified when you [set up to receive reports](https://docs.cloud.google.com/marketplace/docs/partners/reports/set-up-reports).

**Note:** This report was previously called the _lead generation report_ and has been renamed. If you've already set up and received lead generation reports, you continue to receive the reports as VM customer tracking reports.

If you want to collect this information, open a support ticket. For information on how to get support, see [Get support for Marketplace partners](https://docs.cloud.google.com/marketplace/docs/partners/get-support). When you open your ticket, provide the following information:

  * For each product, the fields that you want in your report.

  * The URL for the privacy policy that governs how you use the fields that you collect. We recommend being explicit about what you use the information for, so that customers are comfortable sharing their information.




The fields and privacy policy are used to create a consent form. When customers start deploying a VM product for the first time, they see the information that you want to collect and your privacy policy. After reviewing the information, customers can grant or deny their consent to share their information with you.

The first row of the report holds the number of customers who opted out of sharing their information, and the start and end times that are covered by the report. All customer answers in the report are from between the two times. The times are based on the UTC timezone, and are in the ISO format `YYYY-MM-DDTHH:MM:SS+00:00`. For example, midnight UTC on March 14, 2019 is shown as `2019-03-14T00:00:00+00:00`.

## Report frequency

This report is uploaded daily.

## Report fields

For customers who opted in, the report contains the following information:

**Field** | **Description**  
---|---  
Name | The customer's name.  
Email | The customer's email address.  
Company | The customer's company name. If the customer isn't associated with a company, the value is `_none_`.  
Country Code | The two-letter country code for the customer's country. For example, the two-letter code for France is `FR`.  
Address | The customer's address.  
Phone | The customer's phone number.  
**Note:** As we add features and make improvements to Cloud Marketplace, we add columns as needed to existing reports. If you set up any automated processing of your reports, you should configure it so that it operates based on the names of the columns, and doesn't depend on the total number of columns staying the same.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/test-usage-reporting/
title: Test usage reporting for SaaS products \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:39.534756+00:00
---

# Test usage reporting for SaaS products  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/test-usage-reporting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Test usage reporting for SaaS products Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to test usage reporting for the SaaS products that you offer through Google Cloud Marketplace.

## Before you begin

  * To test usage reporting, your product's pricing plan must be approved by Google. For more details, see [Submit your pricing for review](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/select-pricing#submit-pricing).

**Note:** When you make a change to your product's approved pricing plans, it might take up to four business days for Google to approve the changes.
  * Make sure that you use a Test Billing Account, which has 100% discounted usage. For steps to set up a Test Billing Account, see [Create a Test Billing Account](https://docs.cloud.google.com/marketplace/docs/partners/create-test-billing-account).

  * Verify that you've turned on Customer incremental insights reports. This involves the following steps:

    * [Set up to receive reports](https://docs.cloud.google.com/marketplace/docs/partners/reports/set-up-reports).
    * [Turn on Customer incremental insights reports](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight#turn-on-customer-incremental-insights).
    * For details on the report structure and fields, see [Customer incremental insights reports](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight).



## Run a test to generate usage

You verify your usage reporting by running a test that generates usage reports, and then comparing the usage reports to your expected outcomes. To run the test, do the following:

  1. In Producer Portal, switch to a Google Cloud project that's associated with your Test Billing Account.

  2. From your product's Google Cloud Marketplace listing page, use your Test Billing Account to purchase the product.

  3. Send an initial usage report for a single, recognizable metric. This should equal more than US$0.01, and be less than the amount of usage that you expect for one hour of usage. For example, if your product bills per GiB per hour, send a single usage report that's equivalent to one GiB per hour. This makes it easier to verify that metering and billing are working as expected when you compare against the Customer incremental insights report.

For details about how to send usage reports, including how to format reports and usage times, see [Reporting usage to Google](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/backend-integration#for_usage-based_pricing_reporting_usage_to_google).

  4. Continue to send at least one usage report per hour for at least six hours. If you send more than one usage report per hour, this doesn't affect the required minimum length of the test, which remains six hours.

  5. For the duration of the testing period, create logs that contain the usage information that you're reporting in Google Sheets or CSV format, with the following format:

Time (UTC) | `operationID` | `startTime` | `endTime` | `consumerId` | `metricName` | `metricValue`  
---|---|---|---|---|---|---  
TIME | OPERATION_ID | START_TIME | END_TIME | project_number: PROJECT_NUMBER | METRIC_NAME | METRIC_VALUE  
  
Provide these logs, in Google Sheets or CSV format, to your Cloud Marketplace partner engineering team.

  6. After you receive the Customer incremental insights report corresponding to the time period during which you ran your tests, Google compares the values in your report with your expected values, including the following fields:

     * `charges`
     * `sku_id`
     * `sku_description`
     * `usage`
     * `unit`
     * `currency`
     * `external_account_id`

Google sends you the results of their comparison.




## Clean up after testing

After Google receives and verifies your usage from the testing period, you clean up the resources that you created for testing by doing the following:

  * Stop sending usage reports for the entitlements that you created for testing.
  * Cancel all entitlements that you created for testing.
  * Remove any Google team members that you added to your Cloud Billing account during testing.



## Related topics

  * [Preview your product in Producer Portal](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/test-preview), to see how it appears to Cloud Marketplace users.
  * [Preview your product's pricing](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/test-preview-pricing).



[ Previous arrow_back  Preview pricing plans  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/test-preview-pricing)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

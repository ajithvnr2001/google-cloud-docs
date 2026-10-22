---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-billing/
title: Monitor Pay-as-you-go billing \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:54.272721+00:00
---

# Monitor Pay-as-you-go billing  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-billing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Monitor Pay-as-you-go billing Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

There are several tools you can use to estimate, view, and validate your Apigee Pay-as-you-go billing. This topic discusses how billing or organization administrators can: 

  * Estimate your bill
  * Validate your bill
  * Configure a Cloud Billing alert
  * Get answers to billing questions



## Roles and permissions required

To view project billing and configure alerts, you need the following roles: 

  * **Apigee Organization Admin** (`roles/apigee.admin`)
  * **Billing Account Viewer** (`roles/billing.viewer`)



## Estimate your bill

When you use Pay-as-you-go pricing for Apigee, you are charged for the following: 

  * The number of active environments per region.
  * The number of API calls to your proxies.
  * The number of proxy deployment units used.



Using the above resource usage criteria, you can estimate your future bill in two ways: 

  * Use the Google Cloud pricing calculator.
  * Compare usage data with the Apigee pricing table.



For information on ways to view and monitor your resource usage, see [ View Pay-as-you-go resource usage](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-usage). 

### Use the Google Cloud pricing calculator

To use the pricing calculator to estimate your bill: 

  1. Open the **Google Cloud Pricing Calculator**. 

[Go to the Pricing Calculator](https://cloud.google.com/products/calculator)

  2. Select or search for the **Apigee** product.
  3. Select the **Apigee Pay-as-you-go** product tab.
  4. Enter the name of the environment you want to use to estimate pricing.
  5. Enter the following details about your planned or existing Apigee instance: 
     * **Regions** : Enter the number of regions where the selected environment is deployed.
     * **Standard proxy deployments per region** : Enter the number of Standard API proxies deployed to the environment, per region.
     * **Extensible proxy deployments per region** : Enter the number of Extensible API proxies deployed to the environment, per region.
     * **Standard API proxy calls** : Enter the average number of monthly Standard API proxy calls for this environment, as expressed in the desired unit of measurement (thousand, million, billion).
     * **Extensible API proxy calls** : Enter the average number of monthly Extensible API proxy calls for this environment, as expressed in the desired unit of measurement (thousand, million, billion).
     * **Add-ons:**
       * Select the **Analytics** checkbox to estimate the cost for enabling the [Apigee API Analytics add-on](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-analytics-add-on) in eligible Intermediate or Comprehensive Pay-as-you-go environments.
       * Select the **API Security** checkbox to estimate the cost for enabling the [Advanced API Security add-on](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-security-add-on) in eligible Intermediate or Comprehensive Pay-as-you-go environments. Apigee Analytics is required in order to enable the API Security add-on.
  6. Click **Add to estimate**.



Once the estimate is generated, you can email, save or download the estimate for future reference.

Additional Google Cloud networking charges apply and are billed separately. You can use the calculator to add additional charges to your estimate, such as network data transfer, Cloud load balancing, Cloud DNS, Cloud KMS, and Compute Engine services. See [Pay-as-you-go pricing examples](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-examples) to learn more about cost estimates for other products and services.

**Note** : The Google Cloud pricing calculator should only be used to generate estimates for Pay-as-you-go pricing. It is not designed to optimize resource configurations in Apigee Pay-as-you-go organizations.

### Compare usage data with pricing information

You can also compare your current usage data with prices found in this [table](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview#payg-table-updated) to get a reasonable approximation of your future bills.

For more information on best practices for implementing your Apigee policies and targets to optimize performance, see the [API Proxy](https://github.com/apigee/api-platform-samples/tree/master/perf-proxies) used for testing. More recommendations can be found in the [Introduction to Antipatterns](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/intro).

## Validate your bill

When you review your billing for Apigee with Pay-as-you-go pricing, you can expect to see usage details corresponding to the three metered resources described above. This section explains how to: 

  * View your bill on Cloud Billing.
  * Understand how the Apigee billing SKUs correspond to resource use.



### View your bill on Cloud Billing

To view your Pay-as-you-go bill on Cloud Billing: 

  1. Open the **Billing** page in the Google Cloud console. 

[Go to Billing](https://cloud.google.com/console/billing)

  2. If you have more than one billing account, select **Go to linked billing account** to view the current project's billing account. To locate a different billing account, select **Manage billing accounts** and choose the account you'd like to view.
  3. Select **Reports**.
  4. Click **Show Filters** to access the **Filters** menu if it is not already open.
  5. In the **Time range** field, select **Usage date** to view a current snapshot of billing in a date range, or select **Invoice month** to view charges for a specific invoice.
  6. Select **Group By > SKU**. 
  7. From the **Services** drop-down list, select **Apigee**. The list of SKUs included in your bill is displayed.
  8. To filter the list of SKUs, select the SKUs you want to view from the **SKUs** drop-down list. 

**Note** : If your usage of any of these SKUs is **0** , they don't appear in the **Group By > SKU** pull-down menu.


**Note** : The billing report summarizes costs per region. If your environment is attached to multiple instances in a region, you will see a corresponding increase in the usage hours and cost. 

### Understand your bill

When reviewing your Pay-as-you-go pricing plan bill, you may see one or more of the following SKUs: 

**Pricing attribute** | **SKU** | **SKU ID** | **Price**  
---|---|---|---  
The number of active environments per region |  | Apigee Active Base Environment Usage Hours | C112-9373-5FC4 | $0.5 per hour per region  
---|---|---  
Apigee Active Intermediate Environment Usage Hours | 421B-D6C0-52A2 | $2.0 per hour per region  
Apigee Active Comprehensive Environment Usage Hours | 01C8-CFFA-106E | $4.7 USD per hour per region  
The number of API calls made to your proxies |  | Apigee Standard API Calls: number of API calls processed by Apigee Standard API Proxy | 49D4-8AAF-6094 | $0.00002/call up to 50M $0.000016/call 50M to 500M $0.000013/call > 500M   
---|---|---  
Apigee Extensible API Calls: number of API calls processed by Apigee Extensible API Proxy | 023D-4D0B-712E | $0.0001/call up to 50M $0.00008/call 50M to 500M $0.000064/call > 500M   
The number of proxy deployment units used |  | Apigee Proxy/Shared Flow Deployment Unit Usage Hours Included in Base Environment | 20F4-DE1D-0E80 | $0 (Up to 20 deployment units, overage not allowed)  
---|---|---  
Apigee Proxy/Shared Flow Deployment Unit Usage Hours Included in Intermediate Environment | 4836-1B91-161A | $0 (Up to 50 deployment units, overage not allowed)  
Apigee Proxy/Shared Flow Deployment Unit Usage Hours Included in Comprehensive Environment | 477D-FA48-D913 | $0 (Up to 100 deployment units, overage not allowed)  
Apigee Proxy/Shared Flow Deployment Unit Overage Usage Hours in Comprehensive Environment | 71C2-1AC1-805B | $0.04 per hour per region  
The number of API requests processed by Apigee API Analytics services |  | Apigee API Analytics Add-on: number of API requests processed by Apigee Analytics services | D062-B5FB-5C59 | $20 (per 1M Apigee API Analytics API calls)  
---|---|---  
The number of API requests processed by Apigee Advanced API Security services |  | Apigee Advanced API Security Add-on: number of API requests processed by Apigee Advance API Security services | 572E-C6FE-7BB3 | $20 (per 1M Advanced API Security API calls)  
---|---|---  
  
To validate your bill, you can refer to the detailed SKU pricing for each of the resources listed above on the [SKUs page](https://cloud.google.com/skus?currency=USD&filter=Apigee).

To learn more about viewing billing reports and cost trends, see [View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports). 

## Configure a Cloud Billing alert

You can be notified if your billable or forecasted charges exceed a set budget by creating an alert using the **Budgets & alerts** page in the Google Cloud console. 

To configure a billing alert, follow the steps outlined in [Set budget threshold rules and actions](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-actions). For complete Cloud Billing documentation, including details of the roles and permissions required to set budgets and alerts, see [ Cloud Billing documentation](https://docs.cloud.google.com/billing/docs).

**Note** : In the billing dialog, the Apigee products are prefixed with **Apigee**. If you want to set an alert on an Apigee resource, select the **Apigee** service. Then, you can select the resource, such as **Apigee Active Base Environment Usage Hours**.

## Get answers to billing questions

Use the following resources to get help with any other general billing questions: 

  * To view billing reports, see [View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports).
  * To learn more about billing, read the [Billing documentation](https://docs.cloud.google.com/billing/docs).
  * To resolve billing concerns, use the [Google Cloud Billing Troubleshooter](https://support.google.com/cloud/troubleshooter/7279311?ref_topic=6288636).
  * To change or disable billing on a project, go to the [Billing menu](https://console.cloud.google.com/billing) in the Google Cloud console console. For more information, see [Modify a project's billing settings](https://docs.cloud.google.com/billing/docs/how-to/modify-project).

**Note** : If you disable billing for a project, some of your Apigee and Cloud resources may be removed and cannot be recovered. Rather than disabling billing, consider deleting your Pay-as-you-go organization or switching to an Apigee Subscription plan. For more information on these options, see [Discontinue Apigee Pay-as-you-go pricing services](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-discontinue).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

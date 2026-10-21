---
url: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/configure-usage-reports/
title: Configure usage reporting to Google \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:48:07.572553+00:00
---

# Configure usage reporting to Google  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/configure-usage-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Configure usage reporting to Google Stay organized with collections  Save and categorize content based on your preferences. 

If you choose usage-based pricing for your product, you must report your app's usage to the [Service Control API](https://docs.cloud.google.com/service-infrastructure/docs/overview).

For an introduction to Service Control, see the [Getting Started Guide](https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started).

## Before you begin

  * Set up access to the Cloud Commerce Partner Procurement API, as described in [ Integrate your app](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/technical-integration-setup).
  * We recommend that you use Producer Portal to [create a service account](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/backend-integration#producer-portal-service-accounts)for use with Service Control.



## (For usage-based pricing) Report usage

When an entitlement is created, you must call the Partner Procurement API to retrieve a `usageReportingId`, using the following `HTTP GET` request:
    
    
    GET v1/providers/YOUR_PARTNER_ID/entitlements/ENTITLEMENT_ID
    

The response contains information about the entitlement, in the following format:
    
    
    {
      "name": "providers/YOUR_PARTNER_ID/entitlements/ENTITLEMENT_ID",
      "provider": "YOUR_PARTNER_ID",
      "account": "USER_ACCOUNT_ID",
      "product": "example-messaging-service",
      "plan": "pro",
      "usageReportingId": "USAGE_REPORTING_ID",
      "state": "ENTITLEMENT_ACTIVATION_REQUESTED",
      "updateTime": "...",
      "createTime": "..."
    }

To report usage, you must first make a [`services.check`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check) API call, to check the service's configuration. In the response, if the `checkErrors[]` object is empty, make a [`services.report`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/report) API call to send the usage report.

**Caution:** To avoid large unexpected charges, test usage-based reporting with small amounts of usage (less than $100 USD) per Cloud Billing account in that Cloud Billing account's currency.

The usage report is a Service Control API [`Operation`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation). The following is an example of a usage report for `example-messaging-service` that sends information about the storage being used by the customer:
    
    
    POST https://servicecontrol.googleapis.com/v1/services/example-messaging-service.gcpmarketplace.example.com:report
    
    
    
    {
      "operations": [{
        "operationId": "1234-example-operation-id-4567",
        "operationName": "Hourly Usage Report",
        "consumerId": "USAGE_REPORTING_ID",
        "startTime": "2019-02-06T12:00:00Z",
        "endTime": "2019-02-06T13:00:00Z",
        "metricValueSets": [{
          "metricName": "example-messaging-service/UsageInGiB",
          "metricValues": [{ "int64Value": "150" }]
        }],
        "userLabels": {
          "cloudmarketplace.googleapis.com/resource_name": "order_history_cache",
          "cloudmarketplace.googleapis.com/container_name": "storefront_prod",
          "environment": "prod",
          "region": "us-west2"
        }
      }]
    }

where:

  * `operationId` is a unique string that your service instance generates. Use the same `operationId` for your `check` and `report` operations.
  * `consumerId` is the same as the `usageReportingId` from the entitlement.
  * `startTime` and `endTime` represent the start and end times of the total interval for the `report` Operation. In most cases, the `startTime` of a `report` Operation should have the same value as the `endTime` of the previous `report` Operation. If a customer's service is disabled before the `startTime` of a `report` Operation, the `services.check` API call sends an error in the `checkErrors[]` object, and the customer isn't charged for the corresponding interval.
  * [`MetricValueSet`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet) contains one or more intermediate time intervals and corresponding updated metric values. You define your service's metrics when you [choose and submit your pricing model](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/select-pricing). You view and reference the identifiers for your metrics in the **Technical integration** section of Producer Portal.
  * `userLabels` are user-created labels, defined as key-value strings that follow specific [syntax requirements](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). These labels are forwarded to Cloud Billing [cost management](https://docs.cloud.google.com/cost-management) tools for attribution. For recommendations related to usage labeling, see [Best practices for usage labeling](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/best-practices-labeling).



If the `services.check` API returns one or more of the following errors, we recommend that you stop providing your service to the customer until the error is resolved:

  * `SERVICE_NOT_ACTIVATED`
  * `BILLING_DISABLED`
  * `PROJECT_DELETED`



[ Previous arrow_back  Manage customer entitlements  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/manage-entitlements)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

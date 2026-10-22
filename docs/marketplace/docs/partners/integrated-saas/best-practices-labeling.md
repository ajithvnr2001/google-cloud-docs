---
url: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/best-practices-labeling/
title: Best practices for usage labeling \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:55.636079+00:00
---

# Best practices for usage labeling  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/best-practices-labeling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Best practices for usage labeling Stay organized with collections  Save and categorize content based on your preferences. 

For usage-based SaaS products, Google Cloud Marketplace attributes usage to a single Google Cloud project, specified by the `usageReportingId` field. In some scenarios, a SaaS product might be shared broadly within a customer's organization and used across many customer projects. To enable support for more specific cost attribution, we recommend that usage-based SaaS products include the optional `userLabels` field on their usage report [operation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation).

If your service already supports a concept of [resource labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels), we recommend that you forward those labels in your usage reports. Labels must conform to the [syntax requirements](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#requirements).

## Usage labels

Cloud Marketplace reserves the following labels. You can use these labels to identify additional context for usage within your service platform. We recommend that you include these labels in your usage reports by default.

Label Key| Label Value| Description>| cloudmarketplace.googleapis.com/resource_name | USER_SUPPLIED | The name of the resource associated with a usage metric.  
---|---|---  
cloudmarketplace.googleapis.com/container_name | USER_SUPPLIED | The name of a resource container.  
  
Labels are forwarded to Cloud Billing [cost management](https://docs.cloud.google.com/cost-management) tools, including [cost reports](https://docs.cloud.google.com/billing/docs/how-to/reports) and [billing exports](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).

## Usage labeling example

For this example, imagine your organization offers a storage product called **SaaS Storage Solutions**.

A customer, Carl, has purchased your storage offering for their Google Cloud project `e-commerce-website`, to host the `user_profiles_db` and `products_db` databases for their ecommerce website:

  * `user_profiles_db` contains information about users that visit Carl's site.
  * `products_db` contains information about products that Carl sells on their site.



If you want to provide Carl a detailed cost breakdown of their usage, you can use the `userLabels` key-value pair to report the cost of usage for each database separately.

For example, to report the cost attributed to Carl's `products_db` storage usage, you could send the following report, which indicates that Carl's `products_db` storage is costing them 100 units:
    
    
    operation = {
      'operationId': '<UUID>',
      'operationName': 'db-total-storage',
      'consumerId': 'project:carl_website',
      'startTime': '<Timestamp>',
      'endTime': '<Timestamp>',
      'metricValues': [{
          'int64Value': 100,
      }],
      'userLabels': {
        'cloudmarketplace.googleapis.com/container_name': 'e-commerce-website',
        'cloudmarketplace.googleapis.com/resource_name': 'products_db'
      }
    }
    
    service.services().report(
      serviceName=service_name, body={
        'operations': [operation]
    }).execute()
    

In this example, `service_name` is the Project ID of Carl's Google Cloud project.

For a more detailed example of using `userLabels`, refer to the [SaaS codelab](https://developers.google.com/gcp-marketplace-saas).

[ Previous arrow_back  Best practices for usage reporting  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/best-practices-reporting)

[ Next Configure your reporting to use Virtual Private Cloud (VPC)  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/configure-vpc)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

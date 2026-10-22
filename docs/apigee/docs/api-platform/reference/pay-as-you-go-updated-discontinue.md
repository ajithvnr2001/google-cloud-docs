---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-discontinue/
title: Discontinue Apigee Pay-as-you-go pricing services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:53.991115+00:00
---

# Discontinue Apigee Pay-as-you-go pricing services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-discontinue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Discontinue Apigee Pay-as-you-go pricing services Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

To discontinue usage of existing Apigee Pay-as-you-go services, you can: 

  * Delete your Pay-as-you-go organization.
  * Switch your existing Pay-as-you-go organization to Subscription pricing.



## Delete a Pay-as-you-go organization

If you want to discontinue use of your Apigee organization and ensure that no further charges accrue through Pay-as-you-go pricing, you can delete your Pay-as-you-go organization using the [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest). See [ Delete an Apigee organization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/delete).

### Soft delete

Pay-as-you-go organization deletion using the API triggers a _soft delete_ process that retains the organization for 30 days. After 30 days, the organization is permanently deleted. To recover your organization within the 30 day window, contact [Google Cloud Support](https://cloud.google.com/support-hub).

If Apigee identifies a critical vulnerability in your organization within the 30 day window following deletion (the soft-delete state), and the vulnerability can't be remediated without permanent deletion, Apigee reserves the right to perform an immediate hard-delete of the organization. This action overrides the standard 30-day retention period, but may be required to protect our internal Service Level Objectives (SLOs) and maintain platform security.

### Inadvertent deletion

It is possible to inadvertently delete your Pay-as-you-go organization by taking one of the following actions: 

  * Disabling billing for the Google Cloud project where your organization was created.
  * Disabling the Apigee API (apigee.googleapis.com) for the Google Cloud project where your organization was created.



In both cases, the organization will remain in a soft delete state for 30 days, but can be recovered within one hour of re-enabling billing or Apigee API access in the Google Cloud project where the organization was created. In most cases, the organization can be fully recovered if deleted due to API disablement. However, organizations deleted due to billing disablement may not be fully recoverable. After 30 days, the organization is permanently deleted.

Other Google Cloud resources will be created and used during your preview of Apigee Pay-as-you-go, as noted in [Pay-as-you-go pricing overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview#get-started-pay-as-you-go-updated). These resources must also be deleted to prevent additional charges from accruing.

## Switch an existing Apigee paid organization from Pay-as-you-go to Subscription pricing

To switch an existing Apigee paid organization from Pay-as-you-go pricing to Subscription pricing, contact a [Google Cloud Sales specialist.](https://cloud.google.com/contact?direct=true&pre_product=apigee) See the [Apigee Pricing](https://cloud.google.com/apigee/pricing) page for more information on current Apigee Subscription options.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

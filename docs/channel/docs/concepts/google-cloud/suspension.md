---
url: https://docs.cloud.google.com/channel/docs/concepts/google-cloud/suspension/
title: Google Cloud suspensions overview \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:21:34.045906+00:00
---

# Google Cloud suspensions overview  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/concepts/google-cloud/suspension/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ Guides ](https://docs.cloud.google.com/channel/docs/overview)



Send feedback 

#  Google Cloud suspensions overview Stay organized with collections  Save and categorize content based on your preferences. 

You can use either the Google Cloud console or the [Cloud Channel API](https://docs.cloud.google.com/channel/docs/reference/rest) to issue suspensions for Google Cloud (formerly Google Cloud Platform) entitlements. For example, you can suspend a customer's entitlement for deliquency. In rare cases, Google may issue suspensions due to potential violations of the [Google Cloud terms of service](https://cloud.google.com/terms).

[Billing administrators](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) on the sub billing account will receive an email informing them of the suspension along with details on why their account was suspended. You define the terms of use for a customer and are responsible for providing an acceptable explanation for the suspension. Your customers must work with you to remove the suspension.

## Understanding suspended accounts

You can suspend a customer's entitlements using the Google Cloud console. To do so, select the resource you want to suspend and click **Suspend**. If you want to use the Cloud Channel API, use the [`account.customers.entitlements.suspend` method](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/suspend). You need to provide the entitlement's resource name to suspend its use for the customer.

When you suspend a sub billing account, you limit a customer's options without completely interrupting their active services.

While suspended, the customer:

  * Can't create new virtual machines on Google Cloud projects associated with the suspended subaccount.
  * Can access and modify existing Google Cloud projects.
  * Can access and modify existing virtual machines on an active project.



## Understanding reactivated accounts

When you're ready to remove a suspension, you can either reactivate the entitlement through the Google Cloud console, or use the Cloud Channel API's [`accounts.customers.entitlements.activate` method](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/activate). Like suspensions, you need to provide the entitlement's resource name to activate it.

Lifting a suspension will remove any existing limitations on owned Google Cloud projects.

If you can't remove the suspension, or have trouble doing so, [contact Customer Support](https://support.google.com/channelservices/answer/6182474) for help.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

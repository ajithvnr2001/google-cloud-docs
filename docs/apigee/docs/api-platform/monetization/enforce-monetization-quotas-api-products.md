---
url: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enforce-monetization-quotas-api-products/
title: Enforcing monetization quotas in API products \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:46:07.655529+00:00
---

# Enforcing monetization quotas in API products  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enforce-monetization-quotas-api-products/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Enforcing monetization quotas in API products Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

To enforce monetization quotas in API products, when [adding](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#add) or [editing](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#edit) an API product set the monetization quota in the **Quota** field, as shown in the following figure.

![API product details showing Quota field](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/apiproduct-quota.png)

For more information, see [Understanding monetization quotas](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/overview#quota). 

To enforce the quota defined at the API product level, when configuring the associated API proxies ensure that you attach a quota policy and enable the [<UseQuotaConfigInAPIProduct>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy#usequotaconfiginapiproduct) element. For more information, see [ Enforcing monetization quotas in an API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enforce-monetization-limits#quotas). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

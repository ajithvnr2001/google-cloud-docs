---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-faq/
title: Pay-as-you-go pricing FAQ \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:00.278420+00:00
---

# Pay-as-you-go pricing FAQ  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Pay-as-you-go pricing FAQ Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## Get started with Pay-as-you-go pricing

Who must I contact to get started with Apigee Pay-as-you-go?
    You don't need to speak to anyone. You can get started now. Start experimenting! See [ Get started with Apigee Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview#get-started-pay-as-you-go-updated) for more detail.
I am a current Apigee Subscription customer. Can I add an organization with Pay-as-you-go pricing?
    Yes. Existing Subscription customers can add a Pay-as-you-go organization alongside their entitlements under their existing Subscription agreement.

## Feature availability

Which Apigee features are available with Pay-as-you-go pricing?
    Apigee core API management features are available. Apigee API Analytics and Advanced API Security are available as add-ons. See the [ Apigee Pay-as-you-go billing rates](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview#payg-table-updated) for more information.
Can I use Pay-as-you-go pricing for Apigee hybrid?
    Pay-as-you-go pricing is not available for [Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/what-is-hybrid) at this time.

## Understanding environments

When do I choose the environment type for my Apigee instance?
    You select the environment type when creating an environment. The default environment type is _Base._
How do I add a new environment?
    You can [create a new environment](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with#create) using the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee) or the Apigee API.
Do I have to recreate and redeploy proxies if I want to use them in a new environment?
    Once you create a new environment, you can deploy any existing proxies to the new environment. You can also undeploy those proxies from the old environment if they are no longer required. If an old environment no longer contains deployed proxies, you can [delete the environment](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with#delete) to prevent any Pay-as-you-go charges from accruing.
How do I change the type of an existing environment?
    You can update the type of an existing environment using the Apigee API or the Apigee UI in the Google Cloud console, subject to the limits specified in Comparison of environment types. See [ Update Pay-as-you-go environment types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/update-environment-types) for more details.
Can I downgrade an environment type once the environment is created?
    You can downgrade a Comprehensive environment to an Intermediate environment if your proxies and other resource requirements fall into the Intermediate entitlements. Similarly, you can downgrade an Intermediate environment to a Base environment, if your proxies and other resource requirements comply with the Base entitlements. 

## Performance issues

How can I achieve high availability for my APIs?
    High availability is available only in the Comprehensive environment type. Apigee environments deployed in a single region (also called instance) have an SLA of 99.9%. When the same environment is deployed to two or more regions, the SLA increases to 99.99%. For example, a production environment deployed in `us-west` and `us-east` would have an SLA of 99.99%.
Why would I want to add more regions in my environment?
    A multi-region setup can have several positive impacts on performance. You may want to add additional regions for redundancy to lower latency for clients, scale beyond the limits of a single region, or keep data within a regional boundary. However, adding additional regions will increase the total cost. See [ Expanding Apigee to multiple regions](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/multi-region) for further information.

## Usage and monitoring

How can I view and understand the details of my usage?
    There are several tools you can use to view your Apigee resource usage, monitor your billing, and estimate projected costs. To estimate and monitor your billing, see [Monitor Pay-as-you-go billing](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-billing). For more information on resource usage, see [ View Pay-as-you-go resource usage.](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-usage)

## Billing and pricing

How much will I have to pay?
    

When you use Pay-as-you-go pricing for Apigee, you are charged for the following: 

  * **The number of active environments per region.**

You are charged based on the number and types of environments you select. To learn more about environment types, see [Apigee Pay-as-you-go environment types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-environment-types).

  * **The number of API calls to your proxies.**

You are charged for the number of API calls to the proxies deployed in your environments. For more information on Basic and Extensible policies and their impact on API proxy type, see [ Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types). 

  * **The number of proxy deployment units used.**

You are charged for the number of proxy deployment units used in an environment, per hour, per region. For more information on the proxy deployment units available in each environment type, see [ Apigee Pay-as-you-go billing rates](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview#paygv2-table).




Charges for using Google Cloud network infrastructure will apply. You can use the [ Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator) to estimate these costs. See [ Use the Google Cloud pricing calculator](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-billing#calculator) for more information.

    For several example scenarios and information regarding network charges, see [ Pay-as-you-go example pricing](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-examples).
Will I be charged for "unsuccessful" API calls under the Pay-as-you-go model?
    Yes. API requests, whether they are successful or not, are processed by the Apigee runtime and are included in the count of API calls to your proxies.
How does using Pay-as-you-go differ from using an Apigee evaluation organization?
    Apigee is still available for free under a time-limited evaluation agreement for new Apigee customers. The [evaluation option](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure#org_types) does not support production workloads and is not covered by Google support terms. 
Can I apply my Google Cloud credits to Pay-as-you-go?
    Google Cloud credits not limited to use for specific products will automatically apply to all Google Cloud credit-applicable services, including Apigee Pay-as-you-go.
Are there any limitations to consider when using the pricing calculator to estimate my bill?
    Yes. Your individual needs may increase the complexity of your infrastructure and require review of the Apigee product configuration [limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits). 
How can I get a monthly bill for Apigee Pay-as-you-go?
    You can find a list of resources for help with billing questions in [ Answer billing questions](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-view-usage#billingquestions).
Can I switch from Pay-as-you-go pricing to Subscription pricing?
    Yes. To switch from Pay-as-you-go pricing to Subscription pricing, contact [Apigee Sales](https://pages.apigee.com/contact-sales-reg.html).
Can I switch from Subscription pricing to Pay-as-you-go pricing?
    Yes, but you can only do so at the time of renewal for your Subscription. The Pay-as-you-go billing model is only available for Apigee, so it may not be suitable for customers with legacy Apigee offerings. Customers with legacy Apigee offerings (Edge) should migrate to Apigee first before switching to Pay-as-you-go.
What happens if I disable billing for the Google Cloud project I used to create my Pay-as-you-go organization?
    If you disable billing for a project, some of your Apigee and Cloud resources may be removed and cannot be recovered. Rather than disabling billing to discontinue using Apigee Pay-as-you-go, consider deleting your Pay-as-you-go organization or switching to an Apigee Subscription plan. For more information on these options, see [Discontinue Apigee Pay-as-you-go services](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-discontinue).

## Google Cloud projects and Apigee organizations

What happens if I delete the Google Cloud project that I used to create my Apigee organization, but I do not delete my Apigee organization first? 
    If you delete the Google Cloud project used to create your Apigee organization, the Apigee organization is automatically deleted within seven days.
What happens to my Apigee organization and services if I delete and then restore the Google Cloud project that I used to create my Apigee organization, but I do not explicitly delete my Apigee organization?
    If you delete the Google Cloud project used to create your Apigee organization, the Apigee organization is automatically deleted. It is possible to cancel the project delete process and restore a project within seven days of deletion. However, the Apigee organization may not be fully recoverable even if you restore the Google Cloud project within the seven day period. For more information, see [Shutting down (deleting) projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).
What happens if my Apigee organization is deleted and a critical vulnerability is detected within 30 days of deletion? 
    If Apigee identifies a critical vulnerability in your organization within the 30 day window following deletion (the soft-delete state), and the vulnerability can't be remediated without permanent deletion, Apigee reserves the right to perform an immediate hard-delete of the organization. This action overrides the standard 30-day retention period, but may be required to protect our internal Service Level Objectives (SLOs) and maintain platform security.
What happens if the customer-managed encryption key (CMEK) for my Apigee instance becomes invalid? 
    If your CMEK becomes invalid, your Apigee instance will become inaccessible. This can occur due to key rotation, destruction, or if Apigee loses the necessary permission to access the key. You must resolve this issue promptly. If the problem is not fixed within 30 days, the Apigee instance will be automatically deleted. For more information, see [Best practices for Apigee CMEK](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-best-practices).

## Support

How do I get support for my Pay-as-you-go org?
    Google Cloud Apigee customers with a **Pay-as-you-go** pricing plan can access support by signing up for a Google Cloud support plan. More information and detailed descriptions of available support plans are available from [Cloud Customer Care](https://docs.cloud.google.com/support). Once enrolled, customers can request help and submit cases in the console to [Google Cloud Support](https://cloud.google.com/support-hub). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/marketplace/docs/partners/get-started/
title: Requirements for Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:56:13.353942+00:00
---

# Requirements for Google Cloud Marketplace  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/get-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/partners/transaction-models)



Send feedback 

#  Requirements for Google Cloud Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

If you want to offer products on Google Cloud Marketplace, you must meet the following listing requirements. You must also maintain [operational requirements](https://docs.cloud.google.com/marketplace/docs/partners/operational-requirements) for the types of products that you're offering.

If you make changes to your product or organization that affect your compliance with these listing requirements or invalidate documentation that you provided to Google during onboarding, you must notify Google and submit your product for re-review and re-approval.

**Note:** Google offers a standard revenue share for products you sell through Cloud Marketplace that meet all of the listed requirements and pass a business case review during Google's internal product validation process. If your product doesn't meet the requirements, or doesn't pass the business case review, but you want to proceed with offering that product through Cloud Marketplace, Google might offer you an adjusted revenue share.

## Requirements for your organization

  * Your organization must join and maintain good standing in [Google Cloud Partner Network](https://partners.cloud.google.com).

**Note:** If you aren't yet a Google Cloud partner, learn more and sign up on [Partner Network Hub](https://partners.cloud.google.com/enrollment).

After your organization has joined Google Cloud Partner Network, you get access to Partner Network Hub.

  * Your organization must be incorporated in one of [the supported regions](https://docs.cloud.google.com/marketplace/docs/partners/receive-payments#supported-regions).

  * Your organization must have a [Cloud Marketplace vendor account](https://docs.cloud.google.com/marketplace/docs/partners/offer-products#vendor-agreement) and [payment profile](https://docs.cloud.google.com/marketplace/docs/partners/receive-payments#automated-payments) in good standing.




## Requirements for your product

  * Your product must be production-ready (not alpha or beta) to be publicly listed and sold through Cloud Marketplace.

  * Your product must be enterprise-ready, including a professional online presence, a defined sales motion, customer support, and adherence to strong security best practices.

  * Your product must not include known vulnerabilities, viruses, spyware, Trojan horses, or other malicious code of any kind.

  * You must verify to Google Cloud through an approval process during onboarding that you host your software product primarily on Google Cloud.




The following sections describe the common approved hosting patterns.

### Pattern 1: Fully hosted on Google Cloud

Your entire product, and all of its supporting components, run entirely on Google Cloud. The following architecture diagram provides an example of this pattern.

![An architecture diagram that shows an entire product running on .](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern1.png)Click image to view an enlarged version.![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern1.png)

### Pattern 2: Compute or data plane on Google Cloud

Your product's compute or data plane runs on Google Cloud, but smaller control planes or support infrastructure, such as logging or AI inference, run on-premises or on another cloud. In this case, your Google Cloud-hosted compute or data plane must be the resource whose consumption increases the fastest when your users increase their consumption. The following architecture diagram provides an example of this pattern.

![An architecture diagram that shows a product whose compute plane runs on , along with support infrastructure that doesn't.](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern2.png)Click image to view an enlarged version.![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern2.png)

### Pattern 3: Storage and backup on Google Cloud

Your storage, backup, replication, or data recovery (DR) product must replicate all data to Google Cloud, while the product's control plane can run on-premises or on other clouds. The following architecture diagram provides an example of this pattern.

![An architecture diagram showing a product which uses  for its storage and backup plane.](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern3.png)Click image to view an enlarged version.![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern3.png)

### Pattern 4: Migration to Google Cloud

Your product is migration tooling that has Google Cloud as its only destination for migration, but can run on-premises or on another cloud as a migration source. The following architecture diagram provides an example of this pattern.

![An architecture diagram that shows a product with  as its migration destination.](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern4.png)Click image to view an enlarged version.![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern4.png)

### Pattern 5: Agent data analysis on Google Cloud

Your product's compute or data plane runs on Google Cloud. Your product's monitoring or security agents can run on-premises or on another cloud, but they must send data to a Google Cloud-hosted environment for storage and analysis. The following architecture diagram provides an example of this pattern.

![An architecture diagram that shows a product with on-premises security agents that send data to .](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern5.png)Click image to view an enlarged version.![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern5.png)

### Pattern 6: Datasets hosted on Google Cloud

Your product is a dataset hosted on and delivered through Google Cloud. The following architecture diagram provides an example of this pattern.

![An architecture diagram that shows a dataset hosted on and delivered through .](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern6.png)Click image to view an enlarged version.![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern6.png)

### Pattern 7: Deployment on Google Distributed Cloud

Your product is a virtual machine (VM) or Kubernetes product that's deployed to and runs on devices connected to Google Distributed Cloud. Your product might connect to the internet to integrate with other Google Cloud-hosted apps or services. The following architecture diagram provides an example of this pattern.

![An architecture diagram that shows a dataset hosted on and delivered through .](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern7.png)Click image to view an enlarged version.![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern7.png)

### Pattern 8: AI agents hosted on Google Cloud

Your product is an AI Agent as a Service registered through Gemini Enterprise and all of its supporting components, including the AI agent, run entirely on Google Cloud. The following architecture diagram provides an example of this pattern.

![An architecture diagram that shows an entire productAI agent as a hosted on and delivered through .](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern8.png)Click image to view an enlarged version.![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern8.png)

### Pattern 9: AI agents with hybrid infrastructure

Your product is an AI Agent as a Service registered through Gemini Enterprise, your core product runs on Google Cloud and uses either Google foundational models or models from the [Model Garden](https://docs.cloud.google.com/model-garden). Smaller control planes or supporting infrastructure, run on-premises or on another cloud. In this case, your Google Cloud-hosted Agent must be the resource whose consumption increases the fastest when your users increase their consumption. The following architecture diagram provides an example of this pattern.

![An architecture diagram that shows the agent running on , along with support infrastructure that doesn't.](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern9.png)Click image to view an enlarged version.![](https://docs.cloud.google.com/static/marketplace/docs/partners/images/pattern9.png)

### Additional product requirements

  * You must ensure that your products on Cloud Marketplace have the same capabilities and features as any versions of those products that you offer outside of Cloud Marketplace.
  * You must ensure that your data products don't contain any "personally identifiable sensitive information" as defined in the Protecting Americans' Data from Foreign Adversaries Act of 2024.
  * You must ensure that your products with components deployed into customer-owned Google Cloud project(s) implement customer tenant consumption tracking for [SaaS](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/partner-consumption-tracking), [VM](https://docs.cloud.google.com/marketplace/docs/partners/vm/partner-consumption-tracking), or [Kubernetes](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes/partner-consumption-tracking) solutions.
  * Your listing must result in meaningful Google Cloud consumption by the customer procuring or using the solution.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

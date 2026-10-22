---
url: https://docs.cloud.google.com/application-integration/docs/faq/
title: Frequently asked questions \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:58.883489+00:00
---

# Frequently asked questions  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Resources ](https://docs.cloud.google.com/application-integration/docs/release-notes)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Frequently asked questions

Learn about common issues you might encounter or questions you might have while using Application Integration.

## About Application Integration

### What is Application Integration?

Application Integration is an Integration-Platform-as-a-Service (iPaaS) solution in Google Cloud that offers a comprehensive set of core integration tools to connect and manage the multitude of applications and data required to support various business operations. 

See [Application Integration overview](https://docs.cloud.google.com/application-integration/docs/overview) for more information.

### Can I try Application Integration on a trial basis?

As part of Google Cloud Free Tier, you can start using Application Integration for free of charge in your Google Cloud project. Using Application Integration in Free Tier is subject to the certain usage limitations. 

See [Application Integration Free Tier](https://docs.cloud.google.com/application-integration/docs/pricing#free_use) for more information.

### Does Application Integration have an API?

Yes, Application Integration has a set of RESTful APIs that allow you to programmatically create, update, delete, and manage your integrations.

See [Application Integration API](https://docs.cloud.google.com/application-integration/docs/reference/rest) for more information.

## Integrations

### How many integrations can I create in my Google Cloud project?

A maximum of 1000 integrations can be created in a Google Cloud project.

See [Application Integration usage limits](https://docs.cloud.google.com/application-integration/docs/quotas#usage-limits) for more information.

### Can I run more than one integration at a time?

Yes, See [Application Integration resource quotas ](https://docs.cloud.google.com/application-integration/docs/quotas#resource-quotas) for more details.

### Can I only create an integration in the region which was used during Application Integration setup?

Not necessarily, Application Integration lets you provision or add new regions after you have set it up in your Google Cloud project. For information on the supported locations, see [Application Integration locations](https://docs.cloud.google.com/application-integration/docs/locations).

### Does each integration version count as an individual integration?

No, an integration version is the structure or state of the integration and its tasks or triggers at a specific point in time. You can have up to 100 versions of an integration.

For more information about integration versions, see [Integration versions](https://docs.cloud.google.com/application-integration/docs/integration-versions).

### How do I recover a deleted integration?

Recovering a deleted integration is currently not supported in Application Integration.

### What should I do if my integration flow is failing with errors?

In Application Integration, errors might occur when you are testing and publishing an integration, or during the execution of an integration. These errors can occur due to various client-side and server-side issues. Application Integration offers multiple error handling methods to respond and recover from the errors that are encountered when creating, testing, publishing, or running your integrations. You can use [error handling methods](https://docs.cloud.google.com/application-integration/docs/error-handling) for both synchronous and asynchronous modes of integration execution. 

In Application Integration, errors might occur when you are testing and publishing an integration, or during the execution of an integration. To learn how to handle errors, see [Error handling](https://docs.cloud.google.com/application-integration/docs/error-handling). 

## Pricing

Application Integration uses the pay-as-you-go pricing model where you only pay for what you use beyond the monthly Google Free Tier usage limitations. 

Pricing for Application Integration is calculated on a monthly basis. It's based on the number of integration executions or metered execution count, the amount of data processed, and the number of connection nodes used. 

For more information, see [Application Integration pricing](https://docs.cloud.google.com/application-integration/docs/pricing#payg).

### Am I charged for using other Google Cloud resources in Application Integration?

Yes, running an integration in Application Integration incurs charges for other Google Cloud resources used in the integration, such as Integration Connectors, Secret Manager, and Cloud Key Management Service. Each item is stated separately in your bill, so you know exactly how your costs are calculated and allocated.

### Is there a daily limit for the number of integrations that can be created during the public preview release?

See Application Integration [quotas and limits ](https://docs.cloud.google.com/application-integration/docs/quotas) for details.

## Integration Connectors

### What are Integration Connectors?

Integration Connectors let you connect to various data sources from your integrations. With connectors, both Google Cloud services and other business applications are exposed to your integrations through a transparent, standard interface. As an integration developer, you can quickly connect to a growing pool of applications and systems without the need for protocol-specific knowledge or the use of custom code.

For more information, see [Integration Connectors overview](https://docs.cloud.google.com/integration-connectors/docs/about-connectors).

### Should I set up and provision Integration Connectors independently of Application Integration?

No, Integration Connectors is automatically provisioned in your Google Cloud project when you set up Application Integration.

### Will I be billed separately for use of Integration Connectors in Application Integration?

Yes, you will be billed separately for using Integration Connectors. Pricing for the connection nodes vary depending on the type of connectors used. 

If you use connectors for Google services, the first two connection nodes are free. Each subsequent connection node is charged at $0.35 per hour. If you use connectors for non-Google services, then you're charged at a flat rate of $0.70 per hour per connection node.

For more information about the Integration Connectors pricing, see [Integration Connectors pricing](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

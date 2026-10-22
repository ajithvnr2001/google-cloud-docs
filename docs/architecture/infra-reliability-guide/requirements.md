---
url: https://docs.cloud.google.com/architecture/infra-reliability-guide/requirements/
title: Assess the reliability requirements for your cloud workloads \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:39.493281+00:00
---

# Assess the reliability requirements for your cloud workloads  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/infra-reliability-guide/requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Assess the reliability requirements for your cloud workloads Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-09-23 UTC

The first step toward building reliable infrastructure for your cloud workloads is to identify the reliability requirements of the workloads. This part of the [Google Cloud infrastructure reliability guide](https://docs.cloud.google.com/architecture/infra-reliability-guide) provides guidelines to help you define the reliability requirements of workloads that you deploy in Google Cloud.

## Determine workload-specific requirements

The reliability requirements of an application depend on the nature of the service that the application provides or the process that it performs. For example, an application that provides ATM services for a bank might need 5-nines availability. A website that supports an online trading platform might need 5-nines availability _and_ a fast response time. A batch process that writes banking transactions to an accounting ledger at the end of every day might have a data-freshness target of eight hours.

Within an application, the individual components or operations might have varying reliability requirements. For example, an order-processing application might need higher reliability for operations that write data to the orders database when compared with read requests.

Assessing the reliability requirements of your workloads granularly helps you focus your spending and effort on the workloads that are critical for your business.

## Identify critical periods

There might be periods when an application is more business-critical than at other times. These periods are often the times when the application has peak load. Identify these periods, plan adequate capacity, and test the application against peak-load conditions. To avoid the risk of application outages during peak-load periods, you can use appropriate operational practices like freezing the production code.

The following are examples of applications that experience seasonal spikes in load:

  * The inventory module of a financial accounting application is typically used more heavily on the days when the monthly, quarterly, or annual inventory audits are scheduled.
  * An ecommerce website would have significant spikes in load during peak shopping seasons or promotional events.
  * A database that supports the student admissions module of a university would have a high volume of write operations during certain months of every year.
  * An online tax-filing service would have a high load during the tax-filing season.
  * An online trading platform might need 5-nines availability and fast response time, but only during trading hours (for example, 8 AM to 5 PM from Monday to Friday).



## Consider other non-functional requirements

Besides reliability requirements, enterprise applications can have other important non-functional requirements for security, performance, cost, and operational efficiency. When you assess the reliability requirements of an application, consider the dependencies and trade-offs with these other requirements.

The following are examples of requirements that aren't for reliability, but can involve trade-offs with reliability requirements.

  * **Cost optimization:** To optimize IT cost, your organization might impose quotas for certain cloud resources. For example, to reduce the cost of third-party software licenses, your organization might set quotas for the number of compute cores that can be provisioned. Similar quotas can exist for the amount of data that can be stored and the volume of cross-region network traffic. Consider the effects of these cost constraints on the options available for designing reliable infrastructure.
  * **Data residency:** To meet regulatory requirements, your application might need to store and process data in specific countries, even if the business serves users globally. Consider such data residency constraints when deciding the regions and zones where your applications can be deployed.



Certain design decisions that you make to meet other requirements can help improve the reliability of your applications. The following are some examples:

  * **Deployment automation:** To operate your cloud deployments efficiently, you might decide to automate the provisioning flow by using infrastructure as code (IaC). Similarly, you might automate the application build and deployment process by using a continuous integration and continuous deployment (CI/CD) pipeline. Using IaC and CI/CD pipelines can help improve not just operational efficiency, but also the reliability of your workloads.
  * **Security controls:** Security controls that you implement can also help improve the availability of the application. For example, Google Cloud Armor security policies can help ensure that the application remains available during denial of service (DoS) attacks.
  * **Content caching:** To improve the performance of a content-serving application, you might enable caching as part of your load balancer configuration. With this design, users experience not only faster access to content but also higher availability. They can access cached content even when the origin servers are down.



## Reassess requirements periodically

As your business evolves and grows, the requirements of your applications might change. Reassess your reliability requirements periodically, and make sure that they align with the current business goals and priorities of your organization.

Consider an application that provides a standard level of availability for all users. You might have deployed the application in two zones within a region, with a regional load balancer as the frontend. If your organization plans to launch a premium service option that provides higher availability, then the reliability requirements of the application have changed. To meet the new availability requirements, you might need to deploy the application to multiple regions and use a global load balancer with Cloud CDN enabled.

Another opportunity to reassess the availability requirements of your applications is after an outage occurs. Outages might expose mismatched expectations across different teams within your business. For example, one team might consider a 45-minute outage once a year (that is, 99.99% _annual_ availability) as acceptable. But another team might expect a maximum downtime of 4.3 minutes per month (that is, 99.99% _monthly_ availability). Depending on how you decide to modify or clarify the availability requirements, you should adjust your architecture to meet the new requirements.

[ Previous arrow_back  Building blocks of reliability  ](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks)

[ Next Design reliable infrastructure  arrow_forward  ](https://docs.cloud.google.com/architecture/infra-reliability-guide/design)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-23 UTC."],[],[]] 

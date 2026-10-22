---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/business-continuity/
title: Business continuity planning and disaster recovery \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:23.996663+00:00
---

# Business continuity planning and disaster recovery  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/business-continuity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Business continuity planning and disaster recovery Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee is a multitenant, self-service, cloud-based platform that runs in a fully redundant (live/live) configuration across multiple datacenters in multiple regions of the globe. Apigee uses Google Cloud for its cloud-based platform. As part of the services we build on Google Cloud, we use multiple data centers within each region and service live traffic for our customers across these multiple data centers. We do not have a "live" data center and a "standby" (or "secondary" or "failover") data center. We have two (or more) data centers constantly and simultaneously servicing customer traffic in each region globally. 

## **BCP/DR plan**

Apigee Business Continuity Planning and Disaster Recovery (BCP/DR) is a platform-wide plan and does not contain detailed tasks for individual customers. Rather, the platform is configured to process customer data requests regardless of disruptions and outages. The data will continue to flow even if an entire data center is offline. If an entire region were to go offline, a single-region customer could experience an outage of API processing services. For customers looking for more than "in-region" redundant services, Apigee is available at a globally redundant level of redundant data centers where traffic can be serviced in multiple regions or countries so that if an entire region were to go offline, the data would still flow. 

Single-region customer services are not automatically transferred to another region because of possible geographic restrictions on data processing and access. Apigee services are hosted for customers in the region identified by the customer. Because there may be specific regulations or customer commitments to their users on geographic locations of data, services will not automatically move to an alternate region, as this could potentially compromise Google's commitments to its customers or Google customers' commitments to their customers. 

Google does not share the full BCP/DR plan with any individual customer, as it contains internal sensitive information and references to our customers. Our privacy policy prevents sharing the platform BCP/DR plan with individual customers that could potentially expose other customer names. We offer this same level of privacy to each customer. 

## **BCP/DR Management**

A Google Information Security team is responsible for the oversight of the Business Resiliency program while a rotating Incident Commander is responsible for management and resolution of all incidents. The Incident Commander has operational and engineering personnel on call at all times along with playbooks for all actions that may need to be taken. 

## **BCP/DR Testing**

Google performs operational processes that support BCP/DR testing of the platform on a more frequent cadence than our full annual BCP/DR testing. Each month we perform load swings from our live/live environment while we perform updates to the systems running the service. This process involves taking down one entire data center's worth of systems while the load is handled by the peer datacenter. During this process, after any updates are performed, the first data center is brought back up and services are run live/live again to verify that no issues were introduced. Then the peer datacenter is brought down for the same updates and then brought back online again. Google uses tools and techniques to drain traffic and send a small percentage of traffic to recently updated services to check for any issues or errors before going back to full load processing. 

This consistent operational process exceeds industry-standard bi-annual resiliency "testing" of our service by making it an operational task that occurs more frequently. 

In addition to the operational processes described above, Google also conducts BCP/DR exercises at least once annually where engineering and operations team members test a real disaster scenario. This provides additional training and experience for our personnel on our larger BCP/DR plans for the enterprise as a whole in addition to the service itself. 

The BCP/DR testing done by Google does not use "failover exercises" or "secondary locations" because all of that is built into the running system. 

Google does maintain Playbooks for use by all operational and engineering teams. These playbooks are reviewed and updated at least annually and used in all of our BCP/DR testing and training exercises. 

Annual BCP/DR test reports are available for customers. We also share the results of our operational tasks and annual DR exercise test reports with our third-party auditors, and these form the basis for the auditor's review of our compliance with PCI, HIPAA, ISO, contractual, and other requirements. 

### **Customer BCP/DR tests**

Customers are encouraged to have their own DR plans incorporate Apigee services. Customers can and should consider how Apigee can redirect traffic as needed for customers to maintain end-user services even during a customer data center outage or other disaster event. However, this level of testing is outside the scope of the Apigee DR plan. We encourage customers to perform BCP/DR testing on their own applications and include Apigee in the test. 

### **RTO/RPO**

Apigee does not offer recovery point and recovery time objectives (RPO/RTO) for customers or in contracts related to BCP/DR activities. SLAs are the cloud equivalent of the RTO/RPO data points. Because Apigee is a redundant cloud based service with both management and runtime services being architected with redundant live services, RTO and RPO can both be seen as 'real-time'. Single region customers receive a minimum of redundant services in different datacenters within the same region. Customers desiring higher levels of redundancy can opt for multi-region services. 

### **Pandemic plan**

Google includes a pandemic plan as part of the overall BCP/DR plan and processes. For business operations such as support, Google operates a 24x7 global support team across multiple offices and remote locations. If a pandemic in one area of the globe impacts one of our support locations, personnel in other offices will be alerted and cover the shifts normally handled by the impacted office. For other business services such as sales, the workforce is globally distributed. All teams at Google are equipped to work remotely if needed. Tools used are cloud-based and lend themselves naturally to a pandemic response plan. 

### **Updates**

Google reviews and updates our BCP/DR plan at least annually. Information gathered from incidents, product changes, industry standards, risk analysis activities, and BCP/DB testing are used to update the plan. 

### **Business Impact Analysis and Risk Assessments**

Google conducts a business impact analysis and a Risk assessment annually. Results of the BIA and the RA are prioritized and documented in the issue tracking system. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

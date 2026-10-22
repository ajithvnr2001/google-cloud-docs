---
url: https://docs.cloud.google.com/apigee/docs/api-platform/test/performance-testing/
title: Performance and load testing \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:52.393601+00:00
---

# Performance and load testing  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/test/performance-testing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Performance and load testing Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/faq/performance-testing) documentation._

Performance Testing or Stress testing is sending through a heavy load of normal traffic (either high volume or large size payload). There is no prohibition against this type of testing in Apigee. This traffic will be counted against any API call budget or limits the customer may have in their agreement.

## Notice for performance and load testing activities

In order to best support the customer, Apigee appreciates being notified prior to these tests. To notify Apigee operations of your planned performance testing, open a Support ticket at least 14 days before the start of testing and provide the following information:

  1. Test Plan 
     1. What will be tested (Destination URLs and IP addresses)?
     2. What is the Source (IP addresses) of the test traffic?
     3. Duration of the test window (start & Stop date/time/Timezone).
  2. Tester Info 
     1. Who will be doing the testing?
     2. Contact details for the tester.
  3. Test Limits 
     1. Is there an upper limit to the testing? A max TPS?
     2. Is there a max payload size for the test?



We do not have a team dedicated to monitoring customer environments during load testing activities. Feel free to conduct your testing and raise cases with the appropriate priority should you face any issues. 

  * P1: For production-impacting issues severely affecting live API traffic
  * P2: For issues that have significant user impact, but the production API traffic is unaffected
  * P3: For non-critical issues



## Best practices for conducting performance and load testing

Performance and load testing should closely simulate the workloads that are expected to be run in production. The following are some best practices to follow when performing performance testing: 

  * Simulate real production traffic by using the same client libraries as in production.
  * Configure the load test to send traffic similar to those encountered in production traffic. For example: 
    * Distribute API calls across proxies and environments to match production traffic patterns. Avoid testing a single "testing proxy," as this does not accurately simulate real-world network paths and infrastructure usage.
    * Proxies should have the same set of policies as in production. 
    * Use client header and payload data similar to that used in production environments.
    * Target servers used in testing should replicate the behavior of production servers in terms of latency, availability, and payload size.
  * Ensure that the load test sends requests to the same regions used for production traffic.
  * If traffic to the instance is lower than 500 TPS, slowly ramp up to 500 TPS over 120 seconds. 
  * Once traffic to the instance exceeds 500 TPS, we recommend increasing the TPS by approximately 30% every 90 seconds.
  * If you expect an increase in organic traffic greater than 30% in 90 seconds, _or_ you expect peak traffic to exceed 5000 TPS, open a Support case at least 14 days in advance of your planned testing. Apigee can support both testing traffic scenarios, but additional tuning may be required.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

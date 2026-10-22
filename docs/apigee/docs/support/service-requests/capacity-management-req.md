---
url: https://docs.cloud.google.com/apigee/docs/support/service-requests/capacity-management-req/
title: Infrastructure capacity management \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:32.908239+00:00
---

# Infrastructure capacity management  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/support/service-requests/capacity-management-req/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Infrastructure capacity management Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/service-requests/capacity-management-req) documentation._

Infrastructure capacity management requests, like increasing or decreasing the number of Message Processors based on expected API traffic volume, are meant to manage the infrastructure capacity in Apigee. 

These requests are typically made when you anticipate an increase in the API traffic volume for a certain time due to events such as an upcoming holiday shopping season or planned sales promotions. 

**Note:** This service request type applies only to Apigee users. Users of Apigee hybrid have full access to their respective environments to manage the capacity themselves. 

Service request description | Can I do this myself? | How to perform this operation?  
---|---|---  
Apigee infrastructure capacity management | No | Follow the guidelines provided in the following section and file a support ticket with the Support team.   
  
### Guidelines for raising an Infrastructure Capacity Management request

Follow these steps to create a support request at least 14 days before the start of the desired capacity change. Timely communication with support will ensure that your Apigee organization will have sufficient capacity to handle the expected demand. 

  1. Estimate the maximum traffic volume expected during the time period along with the maximum payload. 
  2. Perform [ stress/load testing](https://docs.cloud.google.com/apigee/docs/support/service-requests/stress-load-req) on your API proxies with the estimated maximum volume of traffic and payload. Resolve any issues observed during the testing. 
  3. File a support ticket with the following details: 
     1. Apigee organization details: 
        * Google Cloud Project ID
        * Apigee organization name
     2. Details of the event with dates when the higher traffic volume is expected 
        * Event start date
        * Event end date
     3. The maximum traffic volume and payload size expected
     4. References to any previous support tickets when the load/stress testing was performed
     5. Any other details which Apigee Support needs to be aware of



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

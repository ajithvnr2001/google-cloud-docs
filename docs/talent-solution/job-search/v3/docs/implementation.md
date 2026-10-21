---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/implementation/
title: Implementing Job search (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:47.512591+00:00
---

# Implementing Job search (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/implementation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Implementing Job search (v3) Stay organized with collections  Save and categorize content based on your preferences. 

You can implement the Cloud Talent Solution Job search API to leverage Google machine learning (ML) technology with your existing search solution.

## Important considerations

  1. The CTS Job search API is designed to be customizable, so you can configure the API according to your business needs. See [Best Practices](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/best-practices) for a discussion of the parameters that you can adjust.

  2. Evaluate your capacity needs prior to implementing Job search. CTS should provide appropriate capacity to account for uploading jobs and/or companies, as well as handling daily operations such as job updates. Some important questions to consider when planning capacity:

     * How frequently are jobs Created, Updated and Deleted (CUD), and how often do job seekers receive job email alerts? There are 2 main use cases:

       1. Capacity for the initial load or reload.
       2. Capacity for normal operations.
     * How frequently are job seekers searching for jobs?

       1. Capacity at peak.
       2. Capacity for normal operations.



## Uploading your data to the Job search API

  1. Before you can implement Job search, Cloud Talent Solution must be hooked up to your system. Follow the [quickstart](https://cloud.google.com/talent-solution/job-search/v3/docs/before-you-begin) guides to set up Cloud Talent Solution.

  2. Upload your jobs/companies data to the CTS Job search API. The API indexes your data alongside your existing database and uses pre-trained, built-in ML algorithms to return relevant search results. For most users, using the pre-trained model is a more than sufficient improvement.

  3. (Optional). You can further train the built-in CTS API algorithms using your own data.

     1. To make efficient use of this option you need to identify 1 or 2 metrics that are most important to your business goals and track these throughout a period of training.
     2. This phase generally takes weeks, depending on your system and the amount of uploaded data.
     3. While training is underway, be sure to split your site traffic so that the performance of the CTS Job search API can be directly compared to your existing job search solution.

Recommended setup:

     1. CTS Job search API : 10%
     2. CTS Job search API control group: 10%
     3. Existing search solution: 80%

At the conclusion of the training period you'll compare the performance of the trained CTS ML algorithm to your existing job search solution and make changes to the API configuration as needed.




## Go-live

Once the Job search API is integrated into your system and your site traffic is routed through it, the API will begin returning relevant results to your users immediately. It's important to design your integration solution in a fault-tolerant manner. That way, if for any reason the Job search API needs to be tweaked you can route traffic back through your existing backend with no interruption to your users.

## Launch checklist

For a detailed checklist of tasks to complete during implementation, see our [launch checklist](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/launch).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

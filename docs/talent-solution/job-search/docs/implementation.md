---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/implementation/
title: Implementing Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:51.433630+00:00
---

# Implementing Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/implementation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Guides ](https://docs.cloud.google.com/talent-solution/job-search/docs/basics)



Send feedback 

#  Implementing Job Search Stay organized with collections  Save and categorize content based on your preferences. 

You can implement Cloud Talent Solution - Job Search to leverage Google machine learning (ML) technology with your existing search solution.

## Important considerations

  1. CTS - Job Search is designed to be customizable, so you can configure the APIs according to your business needs. See [Best Practices](https://docs.cloud.google.com/talent-solution/job-search/docs/best-practices) for a discussion of the parameters that you can adjust.

  2. Evaluate your capacity needs prior to implementing Job Search. CTS should provide appropriate capacity to account for uploading jobs and/or companies, as well as handling daily operations such as job updates. Some important questions to consider when planning capacity:

     * How frequently are jobs Created, Updated and Deleted (CUD), and how often do job seekers receive job email alerts? There are 2 main use cases:

       1. Capacity for the initial load or reload.
       2. Capacity for normal operations.
     * How frequently are job seekers searching for jobs?

       1. Capacity at peak.
       2. Capacity for normal operations.



## Uploading your data to Job Search

  1. Before you can implement Job Search, Cloud Talent Solution must be hooked up to your system. Follow the [quickstart](https://cloud.google.com/talent-solution/job-search/docs/before-you-begin) guides to set up Cloud Talent Solution.

  2. Upload your jobs/companies data to Job Search. The API indexes your data alongside your existing database and uses pre-trained, built-in ML algorithms to return relevant search results. For most users, using the pre-trained model is a more than sufficient improvement.




## Go-live

Once Job Search is integrated into your system and your site traffic is routed through it, the APIs will begin returning relevant results to your users immediately. It's important to design your integration solution in a fault-tolerant manner. That way, if for any reason Job Search parameters need to be tweaked you can route traffic back through your existing backend with no interruption to your users.

## Launch checklist

For a detailed checklist of tasks to complete during implementation, see our [launch checklist](https://docs.cloud.google.com/talent-solution/job-search/docs/launch).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

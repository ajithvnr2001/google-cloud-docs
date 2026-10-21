---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/custom-ranking/
title: Custom Ranking (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:32.748541+00:00
---

# Custom Ranking (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/custom-ranking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Custom Ranking (v3) Stay organized with collections  Save and categorize content based on your preferences. 

The custom ranking feature allows you to introduce your own business logic to control the ranking of jobs returned by Cloud Talent Solution. A job seeker searching on a site can set their search query and other filters as always, and you can add a ranking expression to the search request. Cloud Talent Solution determines the relevant jobs to the query defined by the job seeker, and ranks the results based on the custom ranking expression. This ranked list is then returned to you so that you can display it to the job seeker.

## Benefits

Custom ranking allows you to control on how the results are listed. Using a custom ranking lets you define weights you can assign to custom attributes. You can use a combination of weights and custom attributes to build a custom ranking expression to determine the order the returned listings.

Custom ranking is built on the existing job search service. It leverages the values provided in any customer defined combination of the custom attributes.

### Use Case

The end user searches for "Software Engineer". The company wants to showcase higher return listings for "Software Engineer". Using Custom Ranking allows the company to place a value on these listings and show them to the end user in the order determined by the custom ranking expression.

A company has two nearly identical job listings with job-A having a higher cost per click (CPC) than job-B. Custom ranking can be used to increase the visibility of job-A by setting the ranking of the CPC custom attribute adjusted with weights.

## How to use

Custom ranking supports the following mathematical operators: `+`, `-`, `*`, `/`, `(`, `)`

You can use the field names of custom attributes and these mathematical operators to define a custom ranking expression.

For example, consider that you have two custom attributes: CPC and freshness, where freshness is the number of days since the job was posted. Now you want to rank jobs by CPC and freshness, where CPC counts for 75% of the ranking and freshness counts for 25%. You can create a custom ranking expression as follows:
    
    
    (0.75*CPC) + (0.25 *Freshness)
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

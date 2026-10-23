---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/featured-jobs/
title: Featured job search \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:48.264165+00:00
---

# Featured job search  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/featured-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Guides ](https://docs.cloud.google.com/talent-solution/job-search/docs/basics)



Send feedback 

#  Featured job search Stay organized with collections  Save and categorize content based on your preferences. 

A **featured job** search allows you to influence your users' search results by ranking jobs according to promotional value rather than purely by relevance. A featured job search only returns relevant jobs with an assigned promotional value.

Featured job searches are useful in cases where you want the ability to sponsor individual jobs in your index. For example, a career site promoting business critical jobs can use a featured jobs search to return only sponsored jobs to job seekers. A video tutorial on implementing featured jobs is also [available](https://docs.cloud.google.com/talent-solution/job-search/docs/video).

## Implementing featured job search

There are two steps to implement a featured job search:

  1. Create Job resources with `promotionValue` fields set to a value greater than 0.

  2. Set the `searchMode` to `FEATURED_JOB_SEARCH`. `FEATURED_JOB_SEARCH` only returns jobs that both match the job seeker's search critera and have a promotion value > 0.




Results are ordered in decreasing order of their `promotionValue`. A search with mode set to `FEATURED_JOB_SEARCH` **never** returns jobs with a promotion value of 0. In the case of a tie, the API uses relevance to any other provided search criteria to determine the order of results. A featured job search respects all additional filters applied to the search request (for example, location).

## Featured job search best practices

Because a featured job search only returns promoted jobs to a job seeker, enabling it (setting `searchMode` to `FEATURED_JOB_SEARCH` for specified Job entities) can lead to a trade-off between your business value and the search relevance value the job seeker is looking for. A regular search returns all matching jobs in your index, including any jobs with a promotion value, but does not take the promotion values into account when determining result order.

Featured job searches give you the ability to influence search results and highlight jobs based on a single variable (`promotionValue`). For applications that require balancing relevance with multiple promotional tiers, such as a multi-tiered Cost-per-Click (CPC) subscriber system, Job Search supports a separate multi-variable custom ranking feature. See the custom ranking [best practices](https://docs.cloud.google.com/talent-solution/job-search/docs/best-practices#custom_ranking) documentation for more details.

### Using featured job search with `enableBroadening` and `disableKeywordMatch`

A featured job search can be used in combination with the `disableKeywordMatch` and `enableBroadening` parameters. These additional fields affect the order of the returned results. See the Job Search [best practices](https://docs.cloud.google.com/talent-solution/job-search/docs/best-practices#factors_affecting_search_results) documentation for more information on `enableBroadening` and `disableKeywordMatch`.

**Note:** Avoid using featured job search when `disableKeywordMatch` is set to `false` When `disableKeywordMatch` is turned off, a job seeker's query may return results with irrelevant but highly-promoted jobs listed first. This sacrifices search relevance and therefore relevance-related performance metrics. For example: You assign a high promotional value to a "Software Engineer" job with "experience with server administration" listed in the job description. A user queries for "Restaurant Server" and `disableKeywordMatch` is set to `false`. The top result is "Software Engineer" because the keyword "server" matched the description of a job with a high promotional value even though it's irrelevant to the job seeker.Featured job search | `diasableKeywordMatch` | `enableBroadening` | Outcome  
---|---|---|---  
+ | + | + | Returns a higher number of jobs, including any featured jobs in both relevant and query expanded results.  
+ | - | - | Avoid using featured job search when `disableKeywordMatch` is set to `false`.  
+ | - | + | Avoid using featured job search when `disableKeywordMatch` is set to `false`.  
+ | + | - | Returns a higher number of jobs, including any featured jobs in both relevant and keyword matched results.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

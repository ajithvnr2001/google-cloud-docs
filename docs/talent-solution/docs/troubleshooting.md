---
url: https://docs.cloud.google.com/talent-solution/docs/troubleshooting/
title: Cloud Talent Solution troubleshooting \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:02.641397+00:00
---

# Cloud Talent Solution troubleshooting  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Support ](https://docs.cloud.google.com/talent-solution/docs/troubleshooting)



Send feedback 

#  Cloud Talent Solution troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

## Why isn't a job returning for a certain non-English search keyword?

Cloud Talent Solution relies on Google Translate to translate non-English search queries and job data. Because job searches are usually performed on short strings of keywords, some word context might be missing. This can result in an unexpected translation output. We've accounted for the lack of context in German and French to ensure quality results, but rely entirely on Google Translate for other languages. If the language in question is not English, German, or French, and you're unsatisfied with results, try entering the exact job search query into [Google Translate](http://translate.google.com/). If the translation isn't accurate, please [suggest an edit to the translation in Google Translate](https://support.google.com/translate/answer/2534530). If the results for English, German, or French queries aren't optimal, please [contact support](https://console.cloud.google.com/support/cases).

## Why isn't a job returning when its `requisitionId` is entered as a search keyword?

Cloud Talent Solution typically detects common `requisitionId` regular expressions. However, it's possible that the structure of a `requisitionId` is similar to some other important information, such as part of a location or address. For best results:

  * Ensure that your `requisitionId` fields are populated with the requisition IDs your users expect to be able to search for, since your system may be designed to have multiple versions of requisition IDs (one for your internal, technical purposes, and another for the user).
  * Help Cloud Talent Solution look strictly for the job with a particular requisition ID by [prefixing searches for requisition IDs](https://cloud.google.com/talent-solution/job-search/docs/search#using_search_operators) with `req:` or `requisition:`. You can add this prefix by giving users a dedicated field to search for requisition ID or by using a regular expression in your own business logic to identify requisition ID structures.



## Why are jobs returning from outside of the search location and radius?

When a radius (such as 15 miles) is used in the search query, Cloud Talent Solution uses that value to add the specified additional radius to the edges of the total area of the location indicated in the search query. For example, a search is performed looking for jobs within a 15-mile radius of Mountain View, CA. This search will return results including jobs inside Mountain View city limits as well as jobs within a 15 mile radius of the city limit boundaries. If this was already your expectation, the issue may be a result of one of the following:

  * A job has its [`PostingRegion`](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#postingregion) set to `ADMINISTRATIVE_AREA` or `NATION`, meaning that it the job will return for searches within the specified `ADMINISTRATIVE_AREA` or `NATION`, as long as the scope of the query's search is within the corresponding `ADMINISTRATIVE_AREA` or `NATION`. This functionality exists to support jobs that can accommodate a job seeker from a particular region, rather than a defined city.
  * A job has an ambiguous [`address`](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.jobs) that Cloud Talent Solution resolves to a location that isn't the same as the one that you or the employer intended. For best results, ensure that your jobs have full street addresses.



## Why are other jobs returning for a specific job's requisitionId as a keyword?

When Cloud Talent Solution doesn't semantically understand the keywords in a job seeker's query, Cloud Talent Solution may separate keywords to attempt to derive meaning, and/or fall back to more of a keyword-based search. In this scenario, you may have more jobs that mention the searched requisition ID or parts of it (such as a zip code, if Cloud Talent Solution assumed part of the requisition ID was a zip code). You can help Cloud Talent Solution look strictly for the job with a particular requisition ID by [prefixing searches for requisition IDs](https://cloud.google.com/talent-solution/job-search/docs/search#using_search_operators) with `req:` or `requisition:`. You can add this prefix by giving users a dedicated field to search for requisition ID or by using a regular expression in your own business logic to identify requisition ID structures.

## For a location-ranked query, if two jobs have the exact same address, how is their rank determined?

Cloud Talent Solution uses the relevance of job results to determine the order of jobs that are the same distance from a location.

## Can I use my own fields if you don't have the standard fields I need?

Yes. See more information about [using custom attributes](https://cloud.google.com/talent-solution/job-search/docs/custom-attributes).

## How can I influence the order of search results?

You can [use the custom ranking](https://cloud.google.com/talent-solution/job-search/docs/custom-ranking) functionality when making search requests.

## For additional troubleshooting for the below cases, see [here](https://support.google.com/cloud/troubleshooter/9400003)

  1. A job or jobs are being returned in search results that should not contain these jobs.
  2. A job or jobs are not being returned in search results that should contain these jobs.
  3. A job or jobs are being returned too high or too low in the search results.
  4. Similar jobs are being returned next to each other in the search results.
  5. Not enough jobs are being returned in my search results.



If your issue is not addressed here, please [contact support](https://docs.cloud.google.com/talent-solution/docs/support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

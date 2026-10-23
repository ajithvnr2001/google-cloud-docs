---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/launch/
title: Job Search launch checklist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:12.608335+00:00
---

# Job Search launch checklist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/launch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Guides ](https://docs.cloud.google.com/talent-solution/job-search/docs/basics)



Send feedback 

#  Job Search launch checklist Stay organized with collections  Save and categorize content based on your preferences. 

The first 3 sections apply to all Job Search use cases. Specific instructions tailored to different applications of Job Search are available in section 4.

## 1\. Prepare

  * Identify your business goals and the key metric(s) to track during setup and testing.
  * Download the [client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries) in the language of your choice.
  * Create an architecture summary. Include:
    * An overall architecture diagram.
    * A summary of process flows outlining:
      * Creating jobs and companies.
      * Updating jobs.
      * Latency.
      * Maintenance efforts.


  * Estimate your quota:
    * Estimate how frequently jobs are CUD (Created, Updated and Deleted) and how often job seekers are receiving job email alerts. There are 2 main use cases:
      * Capacity for the initial load or reload.
      * Capacity for normal operations.
    * Estimate how frequently job seekers are searching for jobs:
      * Capacity at peak.
      * Capacity for normal operations.



## 2\. Index companies and jobs

  * Create Company objects:
    * Create at least one [Company](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.companies). We recommend creating Company objects for all companies in your database with open jobs.


  * Create Job objects:
    * Create [Jobs](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job) for your Companies. We recommend creating Job objects for all open jobs in your database.


  * Test retrieval of Companies and Jobs:
    * Use the [GET](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/get) method to ensure that created Companies and Jobs are correctly indexed by CTS.



## 3\. Implement search and client events

  * Implement basic search:
    * Implement search in your existing UI.
      * Use our how-to guides for implementation tips for [basic search](https://docs.cloud.google.com/talent-solution/job-search/docs/search).
    * Implement search filters.
      * Use our how-to guide for [search filters](https://docs.cloud.google.com/talent-solution/job-search/docs/search-filters).
    * Implement location search.
      * Allow job seekers to find jobs in their preferred location by enabling [location search](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery#locationfilter).
    * Implement autocomplete.
      * Improve your search UX with the CTS [autocomplete](https://docs.cloud.google.com/talent-solution/job-search/docs/autocomplete) feature.
    * Implement [pagination](https://docs.cloud.google.com/talent-solution/job-search/docs/search#pagination).
      * As a best practice, we recommend returning 20 or fewer jobs per page to reduce latency in our API return.
    * Enable [spell checking](https://docs.cloud.google.com/talent-solution/job-search/docs/search#spell_checking).
      * Return relevant results even if a job seeker mistypes a keyword.
    * Implement [histograms](https://docs.cloud.google.com/talent-solution/job-search/docs/histogram).
      * Return the number of jobs associated with a given query.
    * Implement [client events](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rpc/google.cloud.talent.v4#google.cloud.talent.v4.ClientEvent).
      * Add client event data to your domain to improve the relevance of your search results over time. Use our [how-to guide](https://docs.cloud.google.com/talent-solution/job-search/docs/events) for implementation tips.



## 4\. Recommendations according to use cases

### Job boards

We recommend that job boards implement the following features to get the most out of Cloud Talent Solution:

  * Incorporate business logic into your search results. Cloud Talent Solution allows you to return high-value job postings at the top of your search results. Consult our [best practices](https://docs.cloud.google.com/talent-solution/job-search/docs/best-practices#configuring_the_api_custom_ranking) and determine which of the following options makes the most sense for your business needs:
    * [Featured Jobs](https://docs.cloud.google.com/talent-solution/job-search/docs/featured-jobs): Highlight important jobs at the top of your search results based on your assigned promotional value.
    * [Custom ranking](https://docs.cloud.google.com/talent-solution/job-search/docs/custom-ranking): Highlight jobs based on multiple variables rather than a single variable. This option is most useful for applications with multi-tiered Cost-per-Click subscriber systems.


  * [Commute Search](https://docs.cloud.google.com/talent-solution/job-search/docs/search-commute): Allow your customers to search for jobs based on their commute preferences.


  * [Email alerts](https://docs.cloud.google.com/talent-solution/job-search/docs/email-alerts): Power your email campaigns with the same relevant results your users get from searching. See the Email alerts [implementation guide](https://docs.cloud.google.com/talent-solution/job-search/docs/email) for details.



### Staffing agencies

We recommend that staffing agencies implement the following features to get the most out of Cloud Talent Solution:

  * Search by requisition ID:
    * For recruiters who need to search by requisition ID, we recommend setting the [search request](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rpc/google.cloud.talent.v4#google.cloud.talent.v4.SearchJobsRequest) flag `disable_keyword_match` to its default of `false` to ensure that only the specific job required is returned.
    * Alternatively, you can allow recruiters to search by requisition ID by querying `reqid:(requisition id)`. If this is a common use-case for your users we recommend highlighting this ability in your UI.



### Career site providers

We recommend that career site providers implement the following features to get the most out of Cloud Talent Solution:

  * Incorporate business logic into your search results. Cloud Talent Solution allows you to return high-value job postings at the top of your search results. Consult our [best practices](https://docs.cloud.google.com/talent-solution/job-search/docs/best-practices#configuring_the_api_custom_ranking) guide for details.
    * [Featured Jobs](https://docs.cloud.google.com/talent-solution/job-search/docs/featured-jobs): Highlight important jobs at the top of your search results based on your assigned promotional value.


  * [Commute Search](https://docs.cloud.google.com/talent-solution/job-search/docs/search-commute): Allow your customers to search for jobs based on their commute preferences.


  * [Email alerts](https://docs.cloud.google.com/talent-solution/job-search/docs/email-alerts): Power your email campaigns with the same relevant results your users get from searching. See the Email alerts [implementation guide](https://docs.cloud.google.com/talent-solution/job-search/docs/email) for details.


  * Search by requisition ID:
    * For recruiters who need to search by requisition ID, we recommend setting the [search request](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rpc/google.cloud.talent.v4#google.cloud.talent.v4.SearchJobsRequest) flag `disable_keyword_match` to its default of `false` to ensure that only the specific job required is returned.
    * Alternatively, you can allow recruiters to search by requisition ID by querying `reqid:(requisition id)`. If this is a common use-case for your users we recommend highlighting this ability in your UI.


  * [Query broadening](https://docs.cloud.google.com/talent-solution/job-search/docs/video#best_practices_for_search_results): Relax restrictions on location and job categories in order to increase the number of results returned. While the relevance of overall search results may decrease, engagement metrics such as click through rate may increase.



### Job aggregators

We recommend that job aggregators implement the following features to get the most out of Cloud Talent Solution:

  * Incorporate business logic into your search results. Cloud Talent Solution allows you to return high-value job postings at the top of your search results. Consult our [best practices](https://docs.cloud.google.com/talent-solution/job-search/docs/best-practices#configuring_the_api_custom_ranking) and determine which of the following options makes the most sense for your business needs:
    * [Featured Jobs](https://docs.cloud.google.com/talent-solution/job-search/docs/featured-jobs): Highlight important jobs at the top of your search results based on your assigned promotional value.
    * [Custom ranking](https://docs.cloud.google.com/talent-solution/job-search/docs/custom-ranking): Highlight jobs based on multiple variables rather than a single variable. This option is most useful for applications with multi-tiered Cost-per-Click subscriber systems.


  * [Email alerts](https://docs.cloud.google.com/talent-solution/job-search/docs/email-alerts): Power your email campaigns with the same relevant results your users get from searching. See the Email alerts [implementation guide](https://docs.cloud.google.com/talent-solution/job-search/docs/email) for details.



## Best practices

For a more details on the features and parameters listed here, see our [best practices](https://docs.cloud.google.com/talent-solution/job-search/docs/best-practices) documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

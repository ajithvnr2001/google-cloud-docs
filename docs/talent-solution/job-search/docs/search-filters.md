---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/search-filters/
title: Using search filters \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:10.438844+00:00
---

# Using search filters  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/search-filters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Guides ](https://docs.cloud.google.com/talent-solution/job-search/docs/basics)



Send feedback 

#  Using search filters Stay organized with collections  Save and categorize content based on your preferences. 

Optionally, a search can include one or more [`JobQuery`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery) filters that restrict the search according to different criteria such as location, companies, compensation, and more.

  * **Location** : Use [`locationFilter`](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery#locationfilter) to search inside a geographic area.

  * **Job category** : Return jobs belonging to a specific category by using [`JobCategory`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#jobcategory). Categories are predefined and include, for example, `ACCOUNTING_AND_FINANCE` and `EDUCATION`. All categories are determined by the Cloud Talent Solution models and are recommended for use in terms of category-based sorting.

  * **Employment type** : Return jobs belonging to one or more employment type definitions, such as `FULL_TIME` or `VOLUNTEER`. See [`EmploymentType`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#employmenttype) for details.

  * **Date range** : Restrict the search to jobs published within the specified date range by using [`publishTimeRange`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery).

  * **Language codes** : Returns jobs that match the specified language code, as determined by the jobs' [`languageCodes`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.language_code) field. This field specifies the language of the job posting, and has no relation to any posted language fluency requirements.

  * **Company name** : Returns jobs from companies with a [`companyDisplayName`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.companyDisplayName) string matching the search query text string. Note that `companyDisplayName` is the human-readable name of the company (such as "Google") as opposed to `name` which is a generated ID (such as "companies/80df2034-176e-44a8-b763-b5370f2463a5").

  * **Commute** : Allows your users to specify a maximum commute time as well as traffic conditions, time of day, and commute method. Job are returned from within a calculated area based on these variables. See the [Commute Search](https://docs.cloud.google.com/talent-solution/job-search/docs/commute-search) implementation guide for more information.

  * **Compensation** : Use [`compensationFilter`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery#compensationfilter) to filter search results based on compensation amounts.

  * **Query language code** : Specifies the language of the query string in BCP-47 format, for example "en-US". If left blank, the default is US English. This field is not related to `languageCode`, which specifies the language of returned job listings. See the [JobQuery documentation](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery) for details. Sample code:

"jobQuery": {"query":"general", "query_language_code":"fr-FR"}}




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

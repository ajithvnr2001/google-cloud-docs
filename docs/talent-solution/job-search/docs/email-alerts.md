---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/email-alerts/
title: Email alerts \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:49.868394+00:00
---

# Email alerts  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/email-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Guides ](https://docs.cloud.google.com/talent-solution/job-search/docs/basics)



Send feedback 

#  Email alerts Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Talent Solution also offers a search API, [`SearchJobsForAlert`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/searchForAlert), that's tuned to the needs of "passive job seekers." These are individuals who are not necessarily actively looking for a job, but might be inclined to apply for one if the right circumstances arise.

You can leverage Cloud Talent Solution to populate the contents of an email campaign designed to deliver periodic updates of jobs that an individual might be interested in. The results of `SearchJobsForAlert` may be different to those from `searchJobs` and are intended for use in job alert emails and other campaigns targeted towards passive job seekers.

**Note:** You can use Cloud Talent Solution to populate email content, but it does not generate the emails themselves. You must create the emails using your own system.

Use the date range filter ([`publishTimeRange`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery)) when calling `SearchJobsForAlert` to restrict the set of jobs being searched to those posted since the last alert was generated. For additional information on using this feature, see the email alerts [implementation guide](https://docs.cloud.google.com/talent-solution/job-search/docs/email).

For information about searching, see [Search Basics](https://docs.cloud.google.com/talent-solution/job-search/docs/search).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

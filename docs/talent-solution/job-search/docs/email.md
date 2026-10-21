---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/email/
title: Implementing email alerts \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:00.969157+00:00
---

# Implementing email alerts  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/email/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Guides ](https://docs.cloud.google.com/talent-solution/job-search/docs/basics)



Send feedback 

#  Implementing email alerts Stay organized with collections  Save and categorize content based on your preferences. 

Using CTS email alerts allows you to engage with your users by automatically sending out email notifications for relevant jobs. For details on the `searchJobsForAlert` search method, see the [email alerts](https://cloud.google.com/talent-solution/job-search/docs/email-alerts) how-to guide.

To make sure that job seekers receive a variety of jobs in their notifications, it's important to consider the following settings:

  * **Diversification level** : Job queries sometimes return multiple similar results. The CTS [`DiversificationLevel`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3p1beta1/DiversificationLevel) parameter detects clusters of highly similar results and displays only one representative job from that group high up in the results. The remainder are returned lower down. This improves the diversification of relevant jobs sent to job seekers and leads to increased engagement. Enable this feature by changing `DiversificationLevel` from unspecified to `SIMPLE`.

  * **The`offset` field**: The [`offset`](https://cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3p1beta1/projects.jobs/search#request-body) field specifies a starting position in the ranked list of relevant jobs returned from a query. Entering a value in this field allows you to send multiple intra-day emails to a job seeker with offset results in each (for example results 1-10 in the first email, 11-20 in the next). While this works only for searches with more search results than the designated `offset` value, it reduces the chances of a job seeker repeatedly seeing the same job opening.

  * **Date and time restrictions** : You can adjust the date and time parameters to only show jobs posted within a certain time frame by using the [`TimestampRange`](https://cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3p1beta1/JobQuery#timestamprange) filter. Depending on how many new jobs are posted daily, you can set this restriction to the last 1 day, 3 days, and so on. This ensures that only the most recently-posted jobs are shown in the email alert.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

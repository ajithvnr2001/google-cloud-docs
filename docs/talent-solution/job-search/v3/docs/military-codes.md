---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/military-codes/
title: Military codes (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:59.348213+00:00
---

# Military codes (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/military-codes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Military codes (v3) Stay organized with collections  Save and categorize content based on your preferences. 

## Background

Job openings should be discoverable by all job seekers with the right skills. Every year an estimated 250,000 men and women transition out of the United States military, where they have gained amazing skills that can be challenging to translate into civilian language. Military code-based search is designed to make it easier for service members to find civilian jobs.

In the US military, occupational codes are used to identify specific jobs. Each service member's role is defined by a code that reflects their branch of the service and career path. The US Army and US Marines use military occupational specialty codes (MOS), the US Air Force uses Air Force specialty codes (AFSC), and the US Navy uses Navy enlisted classification codes (NEC). Transitioning service members can search for jobs using any of the three supported US military occupational speciality codes (MOS, AFSC, or NEC) and Job search will return relevant results to the job seeker.

## Examples

### Army and Marines military occupational specialties codes (MOS)

The code "42B" is the Army's MOS code for a Human Resource Officer. Sample results:

![](https://docs.cloud.google.com/static/talent-solution/job-search/v3/docs/images/42b.png)  


### Air Force specialty codes (AFSC)

The code "10C0" is the United States Air Force AFSC code for an Operations Commander. Sample results:

![](https://docs.cloud.google.com/static/talent-solution/job-search/v3/docs/images/10c0.png)  


### Navy enlisted classification (NEC)

The code "001045" is the United States Navy NEC code for a Network Maintenance Technician. Sample results:

![](https://docs.cloud.google.com/static/talent-solution/job-search/v3/docs/images/001045.png)  


## Feature access

Military code-based search is offered as a part of the Cloud Talent Solution search algorithm, so all users have access to this feature. There is nothing on the development side that needs to be done, and you are not required to modify your existing job titles and descriptions in any way.

Because this technology is still new, we recommended that you incorporate an element into your UI that makes job seekers aware of this feature. For example, you can call out "military occupation code" in the search box and drop down:

![](https://docs.cloud.google.com/static/talent-solution/job-search/v3/docs/images/moc-feature-callout.png)  


## Integration best practices

To ensure that results are returned to your users, set [enableBroadening](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs/search#body.request_body.FIELDS.enable_broadening) to TRUE to expand the number of jobs searched for relevant results. See the Job search [best practices](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/best-practices) documentation for details on using this parameter.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

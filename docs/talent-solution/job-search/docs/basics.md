---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/basics/
title: Job Search basics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:13.626433+00:00
---

# Job Search basics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/basics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Guides ](https://docs.cloud.google.com/talent-solution/job-search/docs/basics)



Send feedback 

#  Job Search basics Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Talent Solution (CTS) - Job Search is designed to transform the recruiting and talent acquisition industry by powering your job search and candidate matching solutions with built-in Machine Learning (ML) algorithms. CTS - Job Search is designed to be integrated with your existing job search site. Your site may belong to any of four basic use cases:

  1. **Job boards** (returns a list of jobs to job seekers)
  2. **Career site providers** (provides career site services to client companies)
  3. **Staffing agencies** (provides short- or long-term employees to clients)
  4. **Applicant tracking systems** (tracks applicants throughout the hiring process)



Business goals and metrics vary significantly between companies. Job Search is designed to be customizable, so you can modify API performance based on your needs. The [best practices](https://docs.cloud.google.com/talent-solution/job-search/docs/best-practices), [implementation guide](https://docs.cloud.google.com/talent-solution/job-search/docs/implementation), and [launch checklist](https://docs.cloud.google.com/talent-solution/job-search/docs/best-practices) documentation is intended to guide you through factors that you need to consider when setting up the Job Search to meet your specific goals.

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/overview-image.png)

## How the Job Search works

CTS - Job Search enables you to leverage Google's Machine Learning (ML) technology within your own website. You send a list of jobs and companies to CTS, which stores them and indexes them into a searchable form. It uses a pre-trained ML model with your provided data to return relevant search results. You can then render the API output to your company site as viewable results. As soon as Job Search is integrated with your system your users will begin seeing high quality search results immediately.

## Multi-tenancy

Cloud Talent Solution supports three organizational tiers. All data uploaded to CTS is owned by a project that you create in Google Cloud. Optionally, data can be assigned to one or more **tenants** , a middle organizational layer between the project and data levels. A tenant enforces data isolation for the client (for example, data can't be queried across more than one tenant in a single API call) as well as machine learning training models. Setting up multiple tenants in a single project is useful for situations where you are supporting more than one customer and don't want to share data between them, but would like to use the same project for billing and reporting internally. For example:

  * Job site providers building job sites for organizations with multiple subsidiary companies.
  * Hiring agencies building applicant tracking systems for multiple businesses.



To learn more about multi-tenancy, see the [Best Practices](https://docs.cloud.google.com/talent-solution/job-search/docs/best-practices#multi-tenancy_optional) documentation.

## Implementing Job Search

For more information on implementing Job Search in your UI, see our [implementation guide](https://docs.cloud.google.com/talent-solution/job-search/docs/implementation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

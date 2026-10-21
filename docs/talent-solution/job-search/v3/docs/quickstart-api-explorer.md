---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/quickstart-api-explorer/
title: Cloud Talent Solution using the API Explorer (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:45.728191+00:00
---

# Cloud Talent Solution using the API Explorer (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/quickstart-api-explorer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Cloud Talent Solution using the API Explorer (v3) Stay organized with collections  Save and categorize content based on your preferences. 

The [API Explorer](https://developers.google.com/apis-explorer/#p/jobs/v3/) is an excellent way to try out the Cloud Talent Solution. The Explorer presents a form that shows the parameters for each method. Fill in the form, execute the API call, and see the results. Click the following button to view API Explorer.

[Try It!](https://developers.google.com/apis-explorer/#p/jobs/v3/)

The API Explorer appears:

> ![APIs Explorer form](https://docs.cloud.google.com/static/talent-solution/job-search/v3/docs/images/api-explorer1.png)

## Authorize API Explorer

First, ensure that you have the "Cloud Talent Solution Project Editor" permissions as described on the [Access control](https://docs.cloud.google.com/talent-solution/docs/access-control) page. You can do this by updating the "IAM & Admin" section for your Google Cloud Platform project (see [Before you begin](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/before-you-begin) for instructions on creating a new project).

Click **Authorize requests using OAuth 2.0**. The **Select OAuth 2.0 scopes** form appears:

> ![APIs Explorer authorization](https://docs.cloud.google.com/static/talent-solution/job-search/v3/docs/images/api-explorer2.png)

Select both the scope items in the list as indicated in the screenshot above and click **Authorize**.

The **API Explorer** form for Cloud Talent Solution appears with a list of API methods.

## Choosing a method

Choose the method you want to call. This tutorial shows you how to list the companies you have created. If there are no companies created, the response is an empty result set. To create a new company, follow the broader procedures shown below, while looking up the [reference documentation](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.companies) to guide you through the required data for each API call.

To list the companies you have created, click **jobs.projects.companies.list** , shown below:

> ![Try-it form](https://docs.cloud.google.com/static/talent-solution/job-search/v3/docs/images/api-explorer3.png)

The companies.list method form appears

> ![Try-it form](https://docs.cloud.google.com/static/talent-solution/job-search/v3/docs/images/api-explorer4.png)

## Fill in the parameters

Fill in the following fields on the form:

  * **parent** : `projects/{project-id}`
  * **pageSize** : `20`



Substitute your project ID for `{project_id}`, but copy all the other fields without changes.

**Note** : These fields hold string values, but don't put quotes around the values. If a value has inner strings, like **filter** , then use double quotation marks around the inner strings.

> ![Try-it form](https://docs.cloud.google.com/static/talent-solution/job-search/v3/docs/images/api-explorer5.png)

## Execute the method

Click the **Execute** button. If you get an error message, check that you entered the information as shown above. Make any changes in the form and click **Execute** again. (You might have to click **Execute** twice). If you receive an empty result set, there are no companies already created. Retry this tutorial with the **jobs.projects.companies.create** method to create a company.

Feel free to explore the API methods and forms on your own.

**Tip** : After you get the output you want, bookmark the API Explorer URL. When you want to run the method again, paste the URL into your browser. The form is already populated with your values. Make any change you wish and then re-authorize the Explorer and click **Execute** to run the method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

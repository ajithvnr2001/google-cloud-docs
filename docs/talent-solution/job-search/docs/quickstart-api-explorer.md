---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/quickstart-api-explorer/
title: Try Cloud Talent Solution using the API Explorer \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:30.209196+00:00
---

# Try Cloud Talent Solution using the API Explorer  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/quickstart-api-explorer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Guides ](https://docs.cloud.google.com/talent-solution/job-search/docs/basics)



Send feedback 

#  Try Cloud Talent Solution using the API Explorer Stay organized with collections  Save and categorize content based on your preferences. 

You can use the API Explorer tool to send trial requests to Cloud Talent Solution. The Explorer presents a form that shows the parameters for each method. Fill in the form, execute the API call, and see the results. You must have completed the "GCP Console set-up" section of the [Before You Begin](https://cloud.google.com/talent-solution/job-search/docs/before-you-begin#overview) page before you can use API Explorer.

Click the following button to view API Explorer:

[Try It!](https://developers.google.com/apis-explorer/#p/jobs/v4/)

You are automatically redirected to the REST reference [overview](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/?apix=true) documentation.

## Choose a method

Choose the method you want to call. This demonstration walks you through listing the companies associated with your Google Cloud Platform service account. If you have not yet created any companies, the API will return an empty list. To try out a different method, follow the broader steps outlined below while referring to the [reference documentation](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/?apix=true) to guide you through the required data for each API call.

To list companies, click **projects.tenants.companies.list** :

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/list_companies.png)

You are redirected to the [`projects.tenants.companies.list`](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.companies/list) page and the method API Explorer form appears:

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/api_explorer.png)

## Fill in the parameters

Of the fields listed on the form, only `parent` is required. We recommend filling in a value for `pageSize` as well, especially if you have already created a large number of companies.

Fill in the following fields on the form:

  * **parent** : `projects/{projectId}/tenants/{tenantId}`
  * **pageSize** : `20`

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/parameters.png)


**Note:** If a string value has inner strings, like **filter** , use double quotation marks around the inner strings instead of single quotes.

Substitute your project ID for `{project_id}`, but copy all the other fields without changes. You can find your project ID by navigating to the project drop-down menu in your [GCP Console](http://console.cloud.google.com):

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/project_id.png)

## Authorize API Explorer

First, ensure that you have the "Cloud Talent Solution Project Editor" [IAM](https://cloud.google.com/talent-solution/docs/iam) permissions enabled on your project. You can do this by navigating to **Identity > Service Accounts** in your GCP console:

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/iam.png)

Click **Google OAuth 2.0** and **API Key** :

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/auth.png)

## Execute the method

Click the **Execute** button. In the window that pops up, click **Allow**. The API will then return a result in the API Explorer sidebar. If you get an error message, check that you entered the information as shown above and that you have assigned the correct permissions to your service account. Make any changes in the form and click **Execute** again. If you receive an empty result set, there are no companies associated with your service account. You can retry this tutorial with the **jobs.projects.companies.create** method to create a company, or see the [create jobs and companies quickstart](https://cloud.google.com/talent-solution/job-search/docs/quickstart-jobs-and-companies).

Feel free to explore additional API methods and forms on your own.

**Tip** : After you get the output you want, bookmark the API Explorer URL. When you want to run the method again, paste the URL into your browser. The form is already populated with your values. Make any change you wish and click **Execute** to run the method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

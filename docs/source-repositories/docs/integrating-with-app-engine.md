---
url: https://docs.cloud.google.com/source-repositories/docs/integrating-with-app-engine/
title: Deploying from Cloud Source Repositories to App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:45.028606+00:00
---

# Deploying from Cloud Source Repositories to App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/integrating-with-app-engine/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Deploying from Cloud Source Repositories to App Engine Stay organized with collections  Save and categorize content based on your preferences. 

This topic describes how to integrate Cloud Source Repositories with App Engine.

App Engine is a web framework and cloud computing platform for developing and hosting web apps by using the Google Cloud.

You can deploy your code from Cloud Source Repositories to App Engine in the same way you would using a local files. The steps in this topic show you how.

**Note:** you must [create a repository](https://docs.cloud.google.com/source-repositories/docs/creating-an-empty-repository) and create code for a deployable app before deploying to App Engine.

## Clone a repository

If you have not already done so, clone the contents of the Google Cloud repository into a local Git repository by using the `gcloud source repos clone` command:
    
    
    gcloud source repos clone hello-world
    

## Deploy your app

  1. From a terminal window, navigate to your repository. In the following command, replace path_to_repository with the path to the repository that contains your application.
         
         cd path_to_repository

  2. Deploy your app:
         
         gcloud app deploy app.yaml
         

Follow the prompts to deploy and test your app.

To pick up new changes, such as when you push an update into your repository, re-run the `gcloud app deploy app.yaml` command.

  3. Verify that your app is running:
         
         gcloud app browse
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

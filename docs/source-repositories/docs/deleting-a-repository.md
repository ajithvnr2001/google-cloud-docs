---
url: https://docs.cloud.google.com/source-repositories/docs/deleting-a-repository/
title: Deleting repositories \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:05.109380+00:00
---

# Deleting repositories  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/deleting-a-repository/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Deleting repositories Stay organized with collections  Save and categorize content based on your preferences. 

This topic describes how to delete a repository by using the Google Cloud console or the command line.

To delete a repository, follow these steps.

###  console 

  1. In the Google Cloud console, open the **All repositories** page for Cloud Source Repositories.

[ Open Cloud Source Repositories](https://source.cloud.google.com/repos)

  2. Hold the pointer over the repository you want to delete and click **Settings** _settings_.

The **General settings** page opens.

  3. Click **Delete this repository** _delete_.

The **Remove repository** dialog opens.

  4. Type the name of the repository you want to delete.

  5. Click **Delete**.




###  gcloud 

From a terminal window, enter the following commands:
    
    
    gcloud init
    gcloud source repos delete [REPOSITORY_NAME]
    

Where `[REPOSITORY_NAME]` is the name of your repository.

The response looks like the following:
    
    
    If [REPOSITORY_NAME] is deleted, the name cannot be reused for up to
    seven days.
    
    Delete "[REPOSITORY_NAME]" in project "gcloud-test" (Y/n)?  y
    
    Deleted [REPOSITORY_NAME].
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

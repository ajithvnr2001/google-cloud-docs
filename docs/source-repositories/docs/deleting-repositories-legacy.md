---
url: https://docs.cloud.google.com/source-repositories/docs/deleting-repositories-legacy/
title: Deleting a repository \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:37.203670+00:00
---

# Deleting a repository  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/deleting-repositories-legacy/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)



Send feedback 

#  Deleting a repository Stay organized with collections  Save and categorize content based on your preferences. 

To delete a repository from [Cloud Source Repositories](https://docs.cloud.google.com/source-repositories/docs):

###  console 

  1. Open the source view in the Google Cloud console:

[Open the Source View in the Console](https://console.cloud.google.com/code/develop/repo)

  2. Click the **More** button ![More button](https://docs.cloud.google.com/static/source-repositories/docs/images/more-button.png) next to the repository you want to delete.

![Create Repository button](https://docs.cloud.google.com/static/source-repositories/docs/images/delete-repo.png)

  3. Select **Delete**.

  4. Enter the name of the repository where prompted and then confirm deletion.




###  gcloud 

From the command line, call:
    
    
    gcloud init
    gcloud source repos delete [REPOSITORY_NAME]
    

The response looks like:
    
    
    If [REPOSITORY_NAME] is deleted, the name cannot be reused for up to
    seven days.
    
    Delete "[REPOSITORY_NAME]" in project "gcloud-test" (Y/n)?  y
    
    Deleted [REPOSITORY_NAME].
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

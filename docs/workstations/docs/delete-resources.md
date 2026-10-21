---
url: https://docs.cloud.google.com/workstations/docs/delete-resources/
title: Delete resources \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:24.018473+00:00
---

# Delete resources  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/delete-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Delete resources Stay organized with collections  Save and categorize content based on your preferences. 

To avoid incurring charges to your Google Cloud account for the resources used, make sure that you remember to delete resources that you no longer need.

**Note:** Disabling the Cloud Workstations API doesn't delete Cloud Workstations resources. To avoid being billed, you must delete the underlying Cloud Workstations resources.

### Delete a workstation

To delete a workstation from the Google Cloud console:

  1. In the Google Cloud console, go to **Cloud Workstations** > **Workstations**.
  2. Select the checkbox beside the workstation that you want to delete.
  3. Click themore_vert**More** options menu and select **Delete** to delete the selected workstation.



If your workstation configuration uses persistent disks and the [reclaim policy](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs#reclaimpolicy) is set to retain persistent disks after you delete the workstation, be sure to remind your Cloud Workstations Admin to manually delete the persistent disk for you. 

### Delete a workstation configuration

If you created a new workstation configuration to learn about Cloud Workstations and you no longer need the configuration, you can delete it from the Google Cloud console:

  1. In the Google Cloud console, go to **Cloud Workstations > Workstation configurations**.
  2. Select the checkbox beside the workstation configuration that you want to delete.
  3. Click themore_vert**More** options menu and select **Delete** to delete the selected workstation configuration. 



### Delete a workstation cluster

To delete a workstation cluster from the Google Cloud console:

  1. In the Google Cloud console, go to **Cloud Workstations > Clusters**.
  2. Select the checkbox beside the cluster that you want to delete.
  3. Click themore_vert**More** options menu and select **Delete** to delete the selected workstation cluster. 



### Delete a Google Cloud project

To delete a Google Cloud project from the Google Cloud console or from the `gcloud` CLI: 

### Console

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### gcloud

**Caution** : Deleting a project has the following effects: 
    * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
    * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




## What's next

  * [Create a workstation](https://docs.cloud.google.com/workstations/docs/create-workstation) using your newly created workstation configuration.

  * Learn more about configuring additional options in your [workstation configuration](https://docs.cloud.google.com/workstations/docs/create-configuration).

  * Use the [Cloud Workstations base editor](https://docs.cloud.google.com/workstations/docs/base-editor-overview).

  * Customize your [workstation configuration](https://docs.cloud.google.com/workstations/docs/customize-development-environment).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

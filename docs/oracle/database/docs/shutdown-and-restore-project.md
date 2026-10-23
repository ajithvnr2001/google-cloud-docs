---
url: https://docs.cloud.google.com/oracle/database/docs/shutdown-and-restore-project/
title: Shut down and restore a project with Oracle resources \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:56.501108+00:00
---

# Shut down and restore a project with Oracle resources  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/shutdown-and-restore-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Shut down and restore a project with Oracle resources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to shut down (delete) and restore a Google Cloud project that contains Oracle Database@Google Cloud resources.

## Shut down (delete) a project

When you delete a project, it's marked for deletion and isn't usable. At the end of the recovery period, it's deleted. However, during the recovery period, the billing continues for the Oracle Database@Google Cloud resources. If you want to stop the billing for your Oracle Database@Google Cloud resources immediately, you can delete them before deleting the project itself. However, in this case, the resources are permanently deleted and you can't recover them.

**Caution:** Before proceeding to shut down the project and delete the resources, ensure that you've migrated your data.

Google Cloud adds a lien on the project containing your Oracle Database@Google Cloud resources to protect them against project deletion. Therefore, before deleting a project, you must remove its lien.

To delete a project, do the following:

  1. [Remove liens from the project](https://docs.cloud.google.com/resource-manager/docs/project-liens#removing_liens_from_a_project).
  2. [Shut down (delete) the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).



## Restore a project

You can only recover the project during recovery period. To learn about the recovery period and instructions to restore, see [Restore a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#restoring_a_project).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

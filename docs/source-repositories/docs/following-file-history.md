---
url: https://docs.cloud.google.com/source-repositories/docs/following-file-history/
title: Following the history of a file \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:09.844397+00:00
---

# Following the history of a file  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/following-file-history/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Following the history of a file Stay organized with collections  Save and categorize content based on your preferences. 

When viewing a file in Cloud Source Repositories, use the Blame or History options to learn more about changes to the file view, such as what lines changed and when.

## View the Blame pane

The Blame pane displays information about who made what change to a file and when.

![](https://docs.cloud.google.com/static/source-repositories/docs/images/blame-layer.png)

For each line in the file, this panel displays:

  * The name of the user who authored the commit.
  * A number that indicates when the change occurred in the history of that file.



A username and change number can appear multiple times for a given file. For example, if a user changed multiple lines in a file and submitted those changes in a single commit, each affected line would contain the same username and change number.

To open the Blame pane, follow these steps:

  1. In the Google Cloud console, open Cloud Source Repositories.

[Open Cloud Source Repositories](https://source.cloud.google.com/repos)

The **All repositories** page opens. Alternatively, you can open the [My source](https://docs.cloud.google.com/source-repositories/docs/browsing-repositories#browsing_to_a_repository) view.

  2. Click a repository.

  3. Browse to the file you want to view and click it.

  4. In the upper-right corner, click **Blame**.

![Blame link](https://docs.cloud.google.com/static/source-repositories/docs/images/blame-history-buttons.png)




### View additional details about a commit

With the Blame pane in view, you can view additional details about a change to a file.

To see additional details, hover over the change number and the author's name in the Blame pane.

A Commit Details dialog appears, which displays information such as:

  * The Commit ID
  * A description of the commit
  * The author commit date
  * The name of the author



To open the change history for this file, click **Show in change history** in the dialog.

## View the history of a file

You can also learn about how a file changed over time through the History option. This option opens a Change History section, which contains information about each commit that affected the file.

You can view the history for a file from the File view or the Blame layer.

###  File view 

  1. In the Google Cloud console, open Cloud Source Repositories.

[Open Cloud Source Repositories](https://source.cloud.google.com/repos)

The **All repositories** page opens. Alternatively, you can open the [My source](https://docs.cloud.google.com/source-repositories/docs/browsing-repositories#browsing_to_a_repository) view.

  2. Click a repository.

  3. Browse to the file you want to view and select it.

  4. Click **Change history** in the lower corner of the page.

The Commit History panel displays a list of commits. Each row displays the hash for that commit as a hyperlink.




###  Blame pane 

  1. In the Google Cloud console, open Cloud Source Repositories.

[Open Cloud Source Repositories](https://source.cloud.google.com/repos)

The **All repositories** page opens. Alternatively, you can open the [My source](https://docs.cloud.google.com/source-repositories/docs/browsing-repositories#browsing_to_a_repository) view.

  2. Click a repository.

  3. Browse to the file you want to view and click it.

  4. In the upper-right corner, click **Blame**.

![Blame link](https://docs.cloud.google.com/static/source-repositories/docs/images/blame-history-buttons.png)

  5. Choose one of the following options:

     * Click the change number.
     * Hold the pointer over the change number or author's name to open the Commit Details dialog, and then click **Show in change history**.



## Open a file as it existed for a specific commit

  1. Open the Change History pane using either the Blame pane or the Change History pane.

The Change History pane opens.

  2. Locate the commit.

  3. Hold the pointer over that commit's row.

A **View** button displays on the same row as the commit.

  4. Click **View**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

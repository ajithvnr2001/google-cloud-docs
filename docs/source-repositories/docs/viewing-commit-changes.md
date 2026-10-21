---
url: https://docs.cloud.google.com/source-repositories/docs/viewing-commit-changes/
title: Viewing commit changes \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:02.292082+00:00
---

# Viewing commit changes  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/viewing-commit-changes/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Viewing commit changes Stay organized with collections  Save and categorize content based on your preferences. 

You might want to see the specific changes that someone made to the files in a commit. In Cloud Source Repositories, you can views these changes by using the Files Changed section of the Commit Details view. 

![Commit Details Files Changed](https://docs.cloud.google.com/static/source-repositories/docs/images/commit-compare-files-changed.png)

## Access the Commit Details view

You can access the Commit Details view in the following ways:

  * From the Change History panel
  * From the Commit link



Both options are available when you open a file or folder in Cloud Source Repositories.

The following table lists examples of fields you can access in your commit event:

Field name | Description  
---|---  
commit | the ID of your commit  
author | the author of the commit  
parents | the ID of the parent commits as a list  
subject | the subject of the commit  
message | the message of the commit  
  
For a list of additional fields, see [CommitInfo](https://gerrit-review.googlesource.com/Documentation/rest-api-changes.html#commit-info).

### Use the Change History panel

  1. In the Google Cloud console, open Cloud Source Repositories.

[Open Cloud Source Repositories](https://source.cloud.google.com/repos)

The **All repositories** page opens. Alternatively, you can open the [My source](https://docs.cloud.google.com/source-repositories/docs/browsing-repositories#browsing_to_a_repository) view.

  2. Click a repository.

The **Repository Root** page opens.

  3. In the **Files** list, browse to the file you want to view, and then click it.

  4. In the adjacent pane, click **Change history**.

In the pane that is displayed, each row shows the hash ID for that commit formatted as a hyperlink.

  5. Click the hash ID link.

The [Commit Details](https://docs.cloud.google.com/source-repositories/docs/commit-details-overview) view opens.




### Use the Commit Information link

You can also open the Commit Details view by clicking the Commit link.

If you're viewing the latest version of the file for that branch, the Commit Information link displays the name of the branch, along with the hash of latest commit.

![Commit Information Link Latest](https://docs.cloud.google.com/static/source-repositories/docs/images/commit-info-latest.png)

If you're looking at a previous version of a file or folder, the Commit Information link displays the hash of the commit.

![Commit Information Link Latest](https://docs.cloud.google.com/static/source-repositories/docs/images/commit-info-commit.png)

If you're looking at a particular tag, the Commit Information link displays the hash associated with the tag.

![Commit Information Link Latest](https://docs.cloud.google.com/static/source-repositories/docs/images/commit-info-tag.png)

In all of these cases, click the hash of the commit to open the Commit Details view.

## View line changes

You can use the Commit Details view to see which lines were changed in each file. To view which lines changed in a file, follow these steps.

  1. Access the Commit Details view for a specific commit.

  2. Locate the file you want to view, and then click the down arrow expand_more to expand that row.

The Files Changed section expands to display the changes made in that file.

![A File with Changes Expanded](https://docs.cloud.google.com/static/source-repositories/docs/images/files-changed-expanded.png)




If you want to simultaneously view all changes to a file, click **Expand All** in the Files Changed section.

## Diff a file

To learn more about the changes to a specific file, open the Diff view. This view provides a diff of the file against the previous commit. You can also select other commits to compare the file against.

To diff a file, follow these steps:

  1. Access the Commit Details view for a specific commit.

  2. Click the path link for the file you want to view.

The Diff view opens. This view contains two panels. One panel displays the previous version of the file. The other panel displays the file as it existed at the time of the commit.

![Diff View](https://docs.cloud.google.com/static/source-repositories/docs/images/file-diff-view.png)




## Compare commits

Another way to learn about how your code has changed over time is to compare one commit to another.

To compare two commits, follow these steps:

  1. Access the Commit Details view for a specific commit.

  2. Click **Compare**.

The Compare screen opens. This screen allows you to select two different commits. By default, this screen compares the commit you selected when you opened the Commit Details screen to its immediate parent.

You can select different commits using the **Commit** and **To Parent** drop-down lists on the Breadcrumb.




## Navigate to a parent commit

Viewing the details of a specific commit can tell you a lot about what files were changed and why. You can get an even better understanding of your code's history by viewing the parent commit. A parent commit is a commit on which the current commit is based.

To access the parent commit, follow these steps:

  1. Access the Commit Details view for a specific commit.

  2. Click the link next to the **Parent**.




Often, a given commit has only a single parent. But there are times when a commit has multiple parents. This happens when a commit is the result of a merge of two or more branches. If a commit has multiple parents, the Commit Details view provides a drop-down list that you can use to diff against, and navigate to, a specific parent.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/secure-source-manager/docs/work-with-issues-pull-requests/
title: Work with issues and pull requests \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:17.925178+00:00
---

# Work with issues and pull requests  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/work-with-issues-pull-requests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Work with issues and pull requests Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to work with issues and pull requests in Secure Source Manager web interface.

To access the Secure Source Manager instance through its web interface, copy the following URL into your browser address bar.
    
    
    INSTANCE_ID-PROJECT_NUMBER.LOCATION.sourcemanager.dev

Replace the following: 

  * INSTANCE_ID with the instance name.
  * PROJECT_NUMBER with the instance's Google Cloud project number. For information on identifying projects, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * LOCATION with the instance's region.



## Required roles

To get the permissions that you need to work with issues and pull requests, ask your administrator to grant you the following IAM roles: 

  * [Secure Source Manager Instance Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`) on the Secure Source Manager instance
  * [Secure Source Manager Repo Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`) on the repository



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## View pull requests

You can view all pull requests you have access to, or pull requests for a specific repository.

Empty repositories don't have a **Pull requests** tab. Once you push to a repository you can view the pull request tab.

To view pull requests or issues assigned to you, navigate to the Secure Source Manager **Issues** or **Pull requests** tab and click **Assigned to me**.

To view pull requests for a repository:

  1. In the Secure Source Manager web interface, select your repository.
  2. From your repository page, click the **Pull requests** tab.
  3. You can filter or sort the pull requests by using the drop down menus for **Assignee** , **Type** , or **Sort.**



To view all pull requests:

  1. In the Secure Source Manager web interface, click the **Pull requests** tab.

**Note:** you must have the Repo Reader role (`roles/securesourcemanager.repoReader`) on a repository in order to see pull requests for that repository.
  2. You can filter or sort the pull requests by using the drop down menus for **Assignee** , **Type** , or **Sort.**




## Create a pull request

  1. In the Secure Source Manager web interface, select the repository you want to create a pull request for.
  2. From the repository page, click the **Pull requests** tab.
  3. Click **New pull request**.
  4. In the **merge into** menu, select the branch you want to merge the pull request into.
  5. In the **pull from** menu, select the branch to pull from.
  6. Click **New pull request**.
  7. Give the pull request a title and description, and attach any relevant files.
  8. Click **Create pull request**.

You are taken to the pull request page where you can add reviewers, labels, milestones, and assignees.




### Edit pull request details

You can add **Reviewers** , **Labels** , **Milestones** , **Assignees** and a **Due date** to a pull request.

**Note:** There are no email notifications for reviewers or assignees in this release.

To add **Reviewers** , **Labels** , **Milestones** , **Assignees** :

From the pull request page, click the ![gear icon](https://docs.cloud.google.com/secure-source-manager/images/gear-icon.png)**gear icon** next to the detail you want to edit.

Edits are saved automatically.

To update the **Due date** :

  1. Click the calendar icon in the **Due date** section, and select a date.
  2. Click the ![plus icon](https://docs.cloud.google.com/secure-source-manager/images/green-plus-icon.png)**plus icon** to save the due date.



## Review a pull request

Reviewers can add comments, request changes, and approve a pull request.

To review a pull request assigned to you:

  1. In the Secure Source Manager web interface, click the **Pull requests** tab.
  2. Click on **Assigned to you**.
  3. Click on the pull request you want to review.

The **Conversation** page opens. You can view any comments left by the pull request author, or other reviewers.

  4. To view and comment on the changed files, click the **Files changed** tab. You can change the behavior of whitespace visibility, view and diff options by clicking the **Whitespace** , **Split view** /**Unified view** , and **diff options** drop-down menus.

  5. To leave a comment, click **plus icon** next to the line you want to comment on.

  6. Click **Start review**.

  7. Leave any additional comments by clicking on the **plus icon** on the line you want to comment on, then click **Add comment**.

Comments support styling with markdown.

  8. To send your comments, approve the pull request, or request changes, click **Review**.

  9. Leave a comment to sum up your changes or leave the comment space blank and select from the following options:

     * **Approve** : approve the changes.
     * **Comment** : send your comments without approving the pull request.
     * **Request changes** : request changes to the pull request.

**Note:** If you are commenting on your own pull request, you can't approve or request changes to your pull request.



## Merge pull requests

  1. From the repository page, click the **Pull requests** tab.
  2. Select the pull request you want to merge.
  3. If there are no conflicts, click **Merge pull request**.



## View issues

  1. In the Secure Source Manager web interface, select your repository.
  2. From your repository page, click the **Issues** tab.
  3. You can filter or sort the issues by using the menus for **Assignee** , **Type** , or **Sort**.



## Create an issue

  1. In the Secure Source Manager web interface, select your repository.
  2. From the repository page, click the **Issues** tab.
  3. Click **New Issue**.
  4. Enter the Issue title and description, and then click **Create Issue**.
  5. On the Issue details page you can assign **Labels** , **Milestones** , **Assignees** , and specify a **branch** , or **tag**.

**Note:** There are no email notifications in this release.



## Add diagrams with Mermaid

Secure Source Manager supports rendering [Mermaid](https://mermaid.js.org/) diagrams in Markdown files (such as `README.md`), pull request descriptions, issues, and comments.

To add a diagram, use a `mermaid` fenced code block:
    
    
    ```mermaid
    graph TD
        A[Write Markdown] --> B(Click Preview Tab)
        B --> C{Does it render?}
        C -- Yes --> D[Success]
        C -- No --> E[Check Syntax]
    ```
    

Click the **Preview** tab in the Markdown editor to verify that your diagram renders before saving.

### Supported diagram types

Secure Source Manager supports the following Mermaid diagram types:

  * **Flowcharts** : `graph` or `flowchart` (supports `TD`, `TB`, `LR`, `BT`, `RL`)
  * **Sequence diagrams** : `sequenceDiagram`
  * **Class diagrams** : `classDiagram`
  * **Entity-relationship diagrams** : `erDiagram`
  * **State diagrams** : `stateDiagram` or `stateDiagram-v2`
  * **XY charts** : `xychart-beta` or `xychart`



### Rendering behavior and limitations

  * **Static rendering** : Diagrams render as static images. Interactive features (such as `click` callbacks and tooltips) and external scripts are disabled for security.
  * **Theme adaptation** : Diagrams automatically adapt to light and dark themes.
  * **Accessibility** : Rendered diagrams include alternative text populated with the diagram source code for screen readers.
  * **Unsupported diagram types** : Unsupported diagram types display an error message and don't render. These include Gantt, Mindmap, Pie, Gitgraph, User Journey, Requirement, C4, Timeline, Sankey, and Block diagrams. For unsupported diagram types, render the diagram locally to an image (PNG or SVG) and embed it using standard Markdown image syntax.



## What's next

  * [Use Git source code management](https://docs.cloud.google.com/secure-source-manager/docs/use-git) with Secure Source Manager.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:26.433586+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The GitHub connector for Gemini Enterprise lets you perform create, update, and read operations on GitHub data.

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service.

## Supported actions

When the GitHub data store is enabled, you can use natural language commands in Gemini Enterprise to perform GitHub actions.

The following GitHub actions that modify data are supported by the data store. Additional read-only actions are also available for tasks like searching and fetching context.

Action | Description  
---|---  
Add comment to pending review | Add a review comment to your latest pending pull request review.  
Add issue comment | Add a comment to a specific issue or pull request.  
Create branch | Create a new branch in a repository.  
Create gist | Create a new GitHub Gist.  
Create or update file | Create or update a single file in a repository.  
Dismiss notification | Mark a GitHub notification as read or done.  
Fork repository | Fork a repository to your account or a specified organization.  
Manage notification subscription | Ignore, watch, or delete a notification thread subscription.  
Manage repository notification subscription | Ignore, watch, or delete a repository's notification subscription.  
Mark all notifications read | Mark all notifications as read, optionally scoped to a repository.  
Merge pull request | Merge a pull request.  
Push files | Push multiple files to a repository in a single commit.  
Reply to pull request comment | Add a reply to an existing pull request comment.  
Star repository | Star a repository on behalf of the authenticated user.  
Trigger Actions workflow | Trigger a GitHub Actions workflow (run, cancel, or rerun jobs).  
Unstar repository | Unstar a repository on behalf of the authenticated user.  
Update gist | Update an existing GitHub Gist.  
Update pull request | Update an existing pull request.  
Write discussion comment | Add, reply to, update, delete, or mark/unmark as answer a discussion comment.  
Write GitHub project | Create or update GitHub Projects (project, items, fields, status updates).  
Write issue | Create or update an issue in a repository.  
Write repository label | Create, update, or delete a label on a repository.  
  
## Required permissions

To enable Gemini Enterprise to perform search using the GitHub data store, you need the following permissions:

**Permission Name** | **Permission Type** | **Reason for Access**  
---|---|---  
Repository: Actions  | Read and write  | Trigger, list, cancel, and rerun workflow runs; access job logs   
Repository: Administration  | Read-only  | List repository collaborators   
Repository: Contents  | Read and write  | Read files, commits, branches, tags, and releases; create branches, write files, push commits, and fork repositories   
Repository: Discussions  | Read and write  | Read GitHub Discussions and discussion categories; add, update, or delete discussion comments   
Repository: Issues  | Read and write  | Read issues, labels, comments, and search issues; create or update issues, post comments, and manage labels   
Repository: Metadata  | Read-only (Mandatory)  | Search for repositories and users   
Repository: Pull requests  | Read and write  | Read pull requests, diffs, and PR comments; merge, update, and add review comments and replies   
Repository: Code scanning alerts  | Read-only  | Read code scanning alerts   
Repository: Dependabot alerts  | Read-only  | Read Dependabot security alerts   
Repository: Secret scanning alerts  | Read-only  | Read secret scanning alerts   
Organization: Members  | Read-only  | View organization teams and their members   
Organization: Issue Types  | Read-only  | View organization issue types   
Organization: Projects  | Read and write  | Read and manage organization-level Projects v2 (projects, items, fields, and status updates)   
Account: Starring  | Read and write  | Star and unstar repositories   
Account: Profile  | Read and write  | Access user profile information   
**Note:** You need to create a GitHub App to use this connector. For more information, see [Creating GitHub apps](https://docs.github.com/en/apps/creating-github-apps)

For information on how to configure these permissions, see [Set permissions and obtain client ID and client secret](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github/github-configuration#set-permissions-and-get-credentials).

## Limitations

This section outlines known issues and limitations that may affect your use of the GitHub data store.

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing GitHub data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The GitHub data store is supported only in the `global`, `us`, and `eu` locations.



## What's next

  * To create and configure a connector with GitHub, see [Set up a GitHub data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

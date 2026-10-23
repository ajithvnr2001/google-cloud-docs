---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:44.719991+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Jira Cloud data store for Gemini Enterprise lets you search and perform actions on your projects, issues, and user information.

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service.

## Supported Jira Cloud versions

The Jira Cloud data store supports version 2 of the Jira Cloud REST API.

## Supported actions

When the Jira Cloud data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Create comment | Creates a new comment on a specified Jira issue to add feedback, updates, or notes.  
Update comment | Edits the text of an existing comment.  
Create issue | Creates a new issue in a Jira Cloud project. To create one, you need to provide a summary, the project ID, and the issue type ID.  
Update issue | Updates an existing issue in Jira Cloud. You need to provide the issue ID to identify it, and you can modify various fields such as the summary, description, and assignee.  
Change issue status | Change the status of an existing issue in Jira Cloud. You need to provide the issue ID to identify it.  
Upload attachment | Uploads an attachment to a specified Jira issue.  
Assign issue | Assigns an existing Jira issue to a specified user.  
Link issues | Creates a link between two Jira issues (for example, blocks, is blocked by, relates to).  
Create project | Creates a new Jira project with a specified name, key, project type, and template.  
Update project | Updates an existing Jira project's settings, such as name, key, description, or lead.  
Create worklog | Adds a time-tracking worklog entry to a Jira issue.  
Update worklog | Updates an existing worklog entry on a Jira issue.  
Get board | Gets a board in Jira.  
Get issues for board | Gets issues for a board in Jira.  
List boards | Lists boards in Jira.  
**Note:** Additional read-only actions are also available.

### Required scopes

To enable Gemini Enterprise to perform search and actions using the Jira Cloud data store, you need the following scopes:

#### Classic scopes

Connection mode | Permission | Purpose  
---|---|---  
**Federated search and actions** | `read:jira-user`, `read:jira-work` | Allows the assistant to fetch and display search results and user details in real-time.  
`write:jira-work` | Allows the assistant to modify work items (for example, updating issue fields), manage comments or issues, and upload attachments.  
`manage:jira-project` | Allows the assistant to manage Jira project settings and create new project-level objects such as versions and components. Required for the create and update project actions.  
**Federated search only** | `read:jira-user`, `read:jira-work` | Allows the assistant to search for and view issues, projects, and user profiles.  
**Data ingestion and actions** | `read:jira-work` | Allows the assistant to perform broad data crawling and indexing of work items.  
`write:jira-work` | Allows the assistant to perform write actions (creation, updates, comments, and attachments) on work items within the ingested environment.  
**Data ingestion** | `read:jira-work` | Allows the assistant to crawl and index Jira content for search availability.  
  
#### Granular scopes

Connection mode | Permission | Purpose  
---|---|---  
**Federated search and actions** | `write:comment:jira` | Allows the data store to post new comments or replies directly from the Gemini Enterprise interface.  
`write:issue:jira` | Allows the data store to create new issues or perform major edits to existing ones.  
`write:attachment:jira` | Allows the data store to upload attachments to Jira issues.  
`write:project:jira` | Allows the data store to create and update Jira projects.  
`write:issue-worklog:jira` | Allows the data store to create and update issue worklogs.  
`write:issue-link:jira` | Allows the data store to create and update links between issues.  
`read:issue:jira` | Allows the data store to read issues.  
`read:issue-type:jira` | Allows the data store to read issue types.  
`read:comment:jira` | Allows the data store to read comments.  
`read:comment.property:jira` | Allows the data store to read issue comment properties.  
`read:project:jira` | Allows the data store to read projects.  
`read:priority:jira` | Allows the data store to read priorities.  
`read:issue.transition:jira` | Allows the data store to read issue transitions.  
`read:issue-meta:jira` | Allows the data store to read issue metadata.  
`read:board-scope.admin:jira-software` | Allows the data store to read the configuration, project features, filters, properties, and quick filters for a board.  
`read:board-scope:jira-software` | Allows the data store to read boards, issues on a board, issues from a backlog, reports, and versions.  
`read:issue-details:jira` | Allows the data store to read issue details.  
`read:jql:jira` | Allows the data store to read Jira Query Language (JQL) queries.  
**Federated search only** | `read:issue:jira` | Allows the data store to read issues.  
`read:issue-type:jira` | Allows the data store to read issue types.  
`read:comment:jira` | Allows the data store to read comments.  
`read:comment.property:jira` | Allows the data store to read issue comment properties.  
`read:project:jira` | Allows the data store to read projects.  
`read:priority:jira` | Allows the data store to read priorities.  
`read:issue.transition:jira` | Allows the data store to read issue transitions.  
`read:issue-meta:jira` | Allows the data store to read issue metadata.  
`read:board-scope.admin:jira-software` | Allows the data store to read the configuration, project features, filters, properties, and quick filters for a board.  
`read:board-scope:jira-software` | Allows the data store to read boards, issues on a board, issues from a backlog, reports, and versions.  
`read:sprint:jira-software` | Allows the data store to read sprint details.  
`read:issue-details:jira` | Allows the data store to read issue details.  
`read:jql:jira` | Allows the data store to read Jira Query Language (JQL) queries.  
**Data ingestion and actions** | `read:user:jira`, `read:group:jira`, `read:avatar:jira` | Allows syncing user/group metadata and displaying user profiles.  
`read:issue-security-level:jira`, `read:issue-security-scheme:jira` | Allows for access control, ensuring the ingested data respects Jira's security boundaries.  
`read:audit-log:jira` | Allows tracking changes and performing incremental syncs to keep ingested data up to date.  
`write:comment:jira` | Allows adding comments to issues using the data store.  
`write:issue:jira` | Allows the assistant to create or modify issues.  
**Data ingestion** | `read:user:jira`, `read:group:jira`, `read:avatar:jira` | Allows crawling and indexing Jira content and user relationships.  
`read:issue-security-level:jira`, `read:issue-security-scheme:jira` | Allows mapping permissions so only authorized users can search the ingested data.  
`read:audit-log:jira` | Allows the sync engine to identify which items have been updated or deleted.  
`read:sprint:jira-software` | Allows the data store to read sprint details.  
  
For information on how to configure these scopes, see [Configure minimum application scope](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#configure-minimum-application-permissions).

## Rate limits for data ingestion

The Jira Cloud data store supports a default rate limit of 12 queries per second (QPS) for data ingestion. These rate limits apply exclusively to the ingestion of data from the Jira Cloud data store.

## Limitations

This section outlines known issues and limitations that may affect your use of the Jira Cloud data store.

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing Jira Cloud data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The Jira Cloud data store is supported only in the `global`, `us`, and `eu` locations.



The following are the limitations for the Jira Cloud ingestion data store:

  * For unstructured data, each media type has different restrictions. For more information, see [Prepare data for custom data sources](https://docs.cloud.google.com/gemini/enterprise/docs/prepare-data#unstructured).

  * For structured data, each document must not exceed 500 KB in size.

  * Application roles with specific, non-empty roles cannot be granted `Browse project` or security level permissions.

  * Document permissions determined by user custom fields or group custom fields are not supported.

  * Jira Cloud doesn't allow any restrictions on worklog levels.

  * Jira Cloud doesn't index PDF attachments that exceed 2,000 pages.

  * Attachments added to private comments don't inherit the access restrictions (ACLs) on the comments.

  * Only the previous 20 comments for an issue in Jira Cloud are fetched.

  * Sprint tables can't be ingested.

  * The legacy user management model is not supported for integration with Jira Cloud. Only the centralized user management model is supported. For more information, see [Atlassian Organization consolidation guide](https://support.atlassian.com/atlassian-cloud/kb/atlassian-organization-consolidation-guide/).

  * When querying a Jira entity (for example, an issue), related data like comments and attachments are not automatically included. This is because they are stored and indexed as separate entities. Searching based on the _content_ of an attachment to find the parent issue is not supported.




## What's next

  * To create and configure a data store with Jira Cloud, see [Set up a Jira Cloud data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

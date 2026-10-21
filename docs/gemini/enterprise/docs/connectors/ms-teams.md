---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:45.311765+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Microsoft Teams data store for Gemini Enterprise lets you search and perform actions on your channels, chats, and schedules.

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service.

## Supported Microsoft Teams versions

The Microsoft Teams data store supports Microsoft Teams version 2.1 and later.

## Supported actions

When the Microsoft Teams data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Send channel message | Sends a message to a specified channel.  
Send chat message | Sends a message in a chat.  
Update channel message | Updates an existing message in a specified channel.  
Update chat message | Updates an existing message in a chat.  
Create channel | Creates a new channel in a specified team.  
Update channel | Updates an existing channel's display name, description, or type in a specified team.  
Create chat | Creates a new one-to-one or group chat.  
Update chat | Updates metadata of an existing chat, such as the topic.  
Add member to channel | Adds a member to an existing channel.  
Create schedule | Creates a new schedule for a team in the Shifts application.  
Create time off entry | Creates a time-off entry for a team member.  
Update time off entry | Updates an existing time-off entry for a team member.  
**Note:** Additional read-only actions are also available.

## Required permissions

To enable Gemini Enterprise to perform federated search and actions using Microsoft Teams, you need the following graph permissions.

**Note:** An administrator must [grant consent](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#grant-admin-consent) for all the delegated permissions listed below. Once consent is granted, the "Status" column will display "Granted" with a green tick mark (✓).Connection mode | Permission | Permission type | Purpose  
---|---|---|---  
Federated search | `Channel.ReadBasic.All` | Delegated | Allows the app to read the names and descriptions of channels.  
`ChannelMember.Read.All` | Delegated | Allows the app to read the members of channels.  
`ChannelMessage.Read.All` | Delegated | Allows the app to read user channel messages.  
`Chat.Read` | Delegated | Allows the app to read all chats.  
`Chat.ReadBasic` | Delegated | Allows the app to read basic properties of chats.  
`ChatMessage.Read` | Delegated | Allows the app to read all one-to-one and group chats messages.  
`Group.Read.All` | Delegated | Allows the app to read the Microsoft Purview sensitivity labels assigned to a team's parent Microsoft 365 group, which are used to apply Sensitive Data Protection (redaction) to Microsoft Teams content.  
`Schedule.Read.All` | Delegated | Allows the app to read schedules, schedule groups, and shifts for teams.  
`Team.ReadBasic.All` | Delegated | Allows the app to read the names and description of teams.  
`TeamMember.Read.All` | Delegated | Allows the app to read the members of teams.  
`User.Read.All` | Delegated | Allows the app to read all users' full profiles.  
Federated search and actions | `Channel.Create` | Delegated | Allows the app to create channels in Microsoft Teams. Required for the create channel action.  
`Channel.ReadBasic.All` | Delegated | Allows the app to read the names and descriptions of channels.  
`ChannelMember.Read.All` | Delegated | Allows the app to read the members of channels.  
`ChannelMember.ReadWrite.All` | Delegated | Allows the app to add and remove members from channels. Required for the add member to channel action.  
`ChannelMessage.Read.All` | Delegated | Allows the app to read user channel messages.  
`ChannelMessage.ReadWrite` | Delegated | Allows the app to update channel messages. Required for the update channel message action.  
`ChannelMessage.Send` | Delegated | Allows the app to send messages in any channel.  
`ChannelSettings.ReadWrite.All` | Delegated | Allows the app to read and update the settings of channels. Required for the update channel action.  
`Chat.Create` | Delegated | Allows the app to create new chats. Required for the create chat action.  
`Chat.Read` | Delegated | Allows the app to read all chats.  
`Chat.ReadBasic` | Delegated | Allows the app to read basic properties of chats.  
`Chat.ReadWrite` | Delegated | Allows the app to read and write one-to-one and group chat threads, including chat messages. Required for the update chat and update chat message actions.  
`ChatMessage.Read` | Delegated | Allows the app to read all one-to-one and group chat messages.  
`ChatMessage.Send` | Delegated | Allows the app to send chat messages.  
`Group.Read.All` | Delegated | Allows the app to read the Microsoft Purview sensitivity labels assigned to a team's parent Microsoft 365 group, which are used to apply Sensitive Data Protection (redaction) to Microsoft Teams content.  
`Schedule.Read.All` | Delegated | Allows the app to read schedules, schedule groups, and shifts for teams.  
`Schedule.ReadWrite.All` | Delegated | Allows the app to create and update schedules, shifts, and time-off entries for teams. Required for the create schedule, create time off entry, and update time off entry actions.  
`Team.ReadBasic.All` | Delegated | Allows the app to read the names and description of teams.  
`TeamMember.Read.All` | Delegated | Allows the app to read the members of teams.  
`User.Read.All` | Delegated | Allows the app to read all users' full profiles.  
  
For information about how to configure these permissions, see [Configure the Microsoft Graph permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#microsoft-graph-minimum-permissions). For a detailed reference on graph permissions, see the Microsoft documentation on [Minimum graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

## Limitations

The Microsoft Teams data store for Gemini Enterprise has the following limitations:

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing Microsoft Teams data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The Microsoft Teams data store is supported only in the `global`, `us`, and `eu` locations.



## What's next

  * To create and configure a data store with Microsoft Teams, see [Set up a Microsoft Teams data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

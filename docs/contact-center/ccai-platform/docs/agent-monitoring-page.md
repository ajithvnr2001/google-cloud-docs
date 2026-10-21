---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-monitoring-page/
title: Agent monitoring page \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:42.158089+00:00
---

# Agent monitoring page  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-monitoring-page/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Agent monitoring page Stay organized with collections  Save and categorize content based on your preferences. 

The Agents page is a live view of all logged-in Agents (users who have the Agent role assigned) in your environment. It can be searched and filtered to provide helpful live views of your agents. Users with access to this page can also perform important actions like viewing Agent's assignment details, daily stats, changing the agent's status, and logging agents out.

**Note:** To appear on this page, the user must be logged in, assigned to a queue (unless filtered for to see "all" agents) and assigned the Agent role.

## Refresh rate

The Agent page is updated every **10-15 seconds** depending on the connectivity of the machine you are using. The Agent page always displays information and stats of the "Today" timeframe.

  1. Go to **Agents**.

The Agent Monitoring Page appears.

Column | Description  
---|---  
ID | The agent user ID.  
Agent | The Agent's name, shown as entered when the agent's user profile was created.  
Email | The email address for the user account.  
Actions | Allows Admins and Managers to perform actions like viewing assignment and other agent-specific details.  
Location | As entered in the user details under **Settings** > **Users & Teams**.  
Status | Shows the current status the Agent is in and allows Admins and Managers to change an agent's status.
     * If the agent is In-call or In-chat, The name of the queue followed by {call type, language, queue priority} will appear alongside the status name.
     * If an agent is not In-call or In-chat and a queue name appears, they have recently transferred a call or chat to the queue shown and it has not been answered by another agent or deflected.
     * On-hold shows with the queue name when the Agent has a caller on hold  
Elapsed Time | The amount of time the agent has been in the current status. When an agent has exceeded a certain threshold in a status, the color of the field will change. Thresholds are the following:
     * > 30 min = yellow highlight
     * > 60 min = red highlight  
On-Hold Time | Current duration caller has been placed on hold.  
Next Status | If the Agent is using the Next Status feature, the field show the status they will be placed in after their current interaction/s are completed.  
Total Calls | (Calls) Count of the number of completed inbound and outbound calls the agent has taken in the Today timeframe
     * Call count on the Agent monitoring page counts sessions not interactions
     * Call sessions are attributed to the last agent who handled the session
     * Outbound and inbound calls are included
     * Due to some date/time matching differences, this column should only be used as a guide - use downloadable reports for specific call interaction counts per agent  
Total Chats | (Chats) Completed chat sessions handled today  
Last End Time | The end time of the last completed session  
Last time offered | Shows the last time the agent was offered a call/chat notification. If the session was a multicast session, the agent may have received a notification but another agent picked up the call.  
Average Response Speed | (Chats) Average time for agent to respond to any consumer message sent  
AHT | Average Handle Time for the individual Agent.
     * Call: Includes hold and wrap-up time
     * Chat: includes chat duration  
Average Wrap-up | (Calls) Average duration agent is in wrap-up status after call sessions.  
Current Agent Network Quality | Provides a score based on the quality of the agent network. Possible values include: Excellent, Good, Average, Poor, Unusable.  
Missed Calls Due to Network Quality | The count of missed calls due to network quality.  
Concurrency Limit | (Chat) Current concurrent chats being handled by the Agent | Defined number of chats the agent is allowed to take. Chat concurrency can be set at the global and agent level.  
Total Deltacast Missed Call Count | (Calls) If you are using Deltacast routing and have set a threshold for how many calls an agent can take before they are placed in Missed Call status, this number will show the number of times that day the agent has been placed in Missed Call Status.  



## Search and sort agents

  1. Click **Agents**.

  2. Click in the search field.

  3. Enter the agent's name and press enter.

You can search for an Agent by first name, last name or both.

  4. Select the channel - Chat, Call, or All.

If an agent is assigned to any queues for chat or call, they will appear in the associated channel section. By default, the page shows only Call Agents.

When All is selected:

     * Both call and chat metrics columns will show.

     * Agents assigned to chat or call channels for queues will show.

     * Agents not assigned to channels/queues will show.




## Filters

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162fa7bb4543b1.png)

Filtering the page allows the current logged in user to customize the Agents monitoring to display on the page. Once you filtered and click **Apply** , you can bookmark or save the URL to return to the same view again.

When your view is filtered to a specific group of Agents, when you use the search field, only the agents in the current filter will show.

### Filter options

Select one or more of the following filter options to see specific Agents:

Option | Description  
---|---  
Team | Agents assigned to the team via sub-team or top-level Team  
Status | Shows current Agents in the selected status/es  
Queue Group | Select from available queue groups.  
Location | Agents with the selected location/s as set on the Users & Teams page  
Language | Agents assigned to queues for the selected language/s  
Role | Agents with assigned selected User Roles as set on the Users & Teams page. Must have Agent role assigned to show on this page.  
Agent | Agents selected by specific name  
Supervisor | Agents who are members of one or more teams the selected Supervisor is assigned as Team Manager  
On-hold | Current Agents who have calls on hold (by pressing the hold option). Calls on hold are separate from calls waiting in queue.  
  
### Steps to filter

  1. Click **Agents**.

  2. The current filter settings display in the **Filtered by** section.

  3. Click **Filter settings** to show the filter options.

  4. Select from the existing filters, or click **More Filters** , then select from the available list.

  5. Click **update** to add the filter options.

  6. Select one or more options from the filters using the checkbox.

  7. Click the collapse arrow or click off of the selection window after you have made your selections.

  8. Click **Apply** to save all filter selections. The filters will appear in the **Filtered by** area.

  9. Bookmark or save the URL to revisit or share this filter.

  10. Click **Reset Filters** to clear all selections.




## Actions

### View agent details and log an agent out

There are restrictions and limitations with the Log out agent action.

  1. Click on **Agents** in the menu bar.

  2. Locate the agent you wish to perform actions for by sorting or searching.

  3. Click on the **Actions** icon.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162fa7bb4845a1.png)

     1. **View Agent Details** launches a pop-up with any available information about the agent listed below:

**Total Calls** : Total inbound and outbound completed calls the agent handled today. If the agent was transferred a call and they were the last agent on the call, they receive the call count for that call rather than the first agent who picked it up.

**Handle time** : Average handle time for completed calls today.

**CSAT** : If CCAI Platform CSAT is being used, the average of the agent's combined scores will be shown. Avg. CSAT = Total of agent received CSAT scores/number of total scores. If you are utilizing a 3rd party service for CSAT, scores will not appear in the CCAI Platform portal.

**Hold Total** : The duration of the time an agent placed the caller on hold during a live call.

**Repeat Callers** : Shows if the agent has received calls from callers CCAI Platform has marked as repeat callers based on the contact record in your CRM.

**Total Chats** : Number of completed chats by the agent today. If the agent was transferred a chat and they were the last agent on the chat, they receive the chat count for that chat rather than the first agent who answered the chat.

**Teams** : Number of and which teams the agent is assigned to. See Users: Agents, Managers, Admins, and Teams for more information on assigning users to teams.

**Assigned Queues** : The queues for which the agent is assigned directly as an individual agent.

**Assigned Queues From Team** : Queues the agent is assigned to receive calls from based a team they belong to being assigned to the queue.

     2. Select **Log Out Agent** to log the agent out of CCAI Platform, which places the agent in the **Offline** status.

     3. Select **Logout** to confirm the action.

     4. The agent will no longer appear on the Agent monitoring page once the agent is logged out.




### Change an agent's status

There are restrictions and limitations to changing an agent's status.

  1. Click on **Agents** in the menu bar.

  2. Locate the agent you wish to perform actions for by sorting or searching (described above).

  3. Place your mouse over the status field and click on the actions icon next to the Agent.

  4. Select from the list of available default and custom statuses.

**Note:** The status "Special Task" is only available from this view, agents do not see the "Special Task" status in their view.



## Use queues or teams to sort agents

Want to see a certain list of agents based on Queue assignments but don't see a way to do it from the above options? Try this trick.

  1. Click on **Dashboard > Call** or **Chat** in the top menu bar.

  2. Use the Queue filter to select the group of agents you would like to monitor.

  3. Click on the **Logged in Agents** section of the Dashboard.

  4. You will be brought to the Agent page with the Agents which are assigned to your selected Queue.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

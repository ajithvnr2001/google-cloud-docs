---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status-update/
title: Update an agent's status \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:01.021515+00:00
---

# Update an agent's status  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Update an agent's status Stay organized with collections  Save and categorize content based on your preferences. 

Agents sometimes don't change their status or log out at the end of their workday. This affects agent adherence reports and can impact call routing. Users with **Admin** or **Manager** roles assigned are able to change an agent's status in the CCAI Platform portal.

Logging out an agent is not considered a standard status change so it requires slightly different steps.

  * An agent's status cannot be changed and the **Log out agent** button will be hidden in the Actions drop-down from the following statuses:

    * In-call

    * In-chat

    * Offline (if the agent is offline, the agent is not shown on the agent page).

  * Managers can only see agents in their assigned teams and any sub-teams they are a manager for on the agents page, so they can only change the status of agents who are on one of their assigned teams.

  * When the agent's workstation is offline, the log out feature won't update an agent's status in the agent list. That is, if the agent does not sign out and shuts down their system, their status will be updated at the time their system becomes active again.

  * The status "Special Task" is only available from the agent page view; agents don't see the "Special Task" status in their view.




## Log an agent out

After an agent is logged out or placed in offline status, the sign in dialog will be presented upon their next visit to the sign in screen or the agent adapter.

  1. In the CCAI Platform portal, go to the **agents** display.

  2. By sorting or searching, locate the agent for whom you want to perform actions.

  3. Click the **actions** icon and select **log out agent**.

![Log out agents button](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1ff2770b.png)

  4. Click **Logout** to confirm the action.




## Change an agent's status

  1. In the CCAI Platform portal, go to the **Agents** display.

  2. Locate the agent you want to perform actions for by sorting or searching.

  3. Click the actions icon for the specific user.

![Change agent status](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1ff2b362.gif)

  4. Select from the list of available default and custom statuses.

**Note:** The status "Special Task" is only available from this view. Agents don't see the "Special Task" status in their view.



## FAQ

Q: Why is the agent I'm trying to log out still showing as logged in?

A: Possible reasons include:

  * If the agent's workstation is offline (they shut it down), then CCAI Platform cannot reach the console and is unable to log the agent out until the system is active again.

  * If the agent is in In-call or In-chat, the log out feature is not available.




Q: How can I change an agent from offline to another status?

A: Agents who are offline don't appear on the **agent monitoring** display and therefore are unable to have their status changed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

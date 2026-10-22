---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/twinning/
title: Twinning: Call \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:58.285607+00:00
---

# Twinning: Call  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/twinning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Twinning: Call Stay organized with collections  Save and categorize content based on your preferences. 

Twinning allows a primary extension (the web desktop agent adapter) and a secondary extension (for example, mobile phone number) to operate as a single phone. Twinning is ideal for support agents who are frequently on the go, since it allows them to forward support calls to their preferred phone number in addition to handling calls at their desk using the web adapter. Another example is a front desk phone set up as the office's primary extension; you can use Twinning to forward those calls to a mobile phone.

Twinning supports international phone numbers.

When an agent chooses to forward calls in the Agent Adapter, the call is sent to the phone number but the agent will continue to receive call notifications in their web adapter. They are still able to answer the call there if needed. Agents are able to receive all call types using this method.

The key capabilities and benefits of twinning include:

  * **Support for routing using DID** : Twinning is able to route calls using a unique identifier known as a Direct Inward Dialing (DID) number. A DID number is a telephone number that is used to directly connect to a specific extension or department within an organization.

  * **CRM ticket generation** : Twinned calls handled through an extension on a mobile phone still generate a CRM ticket.

  * **Reporting and monitoring** : Twinned calls will be displayed in reporting and on all monitoring pages. The record appears as a regular call and does not identify whether it was answered through an extension.

  * **No internet connection required** : The call is made over PSTN.

  * **Compatible with multicast and deltacast routing** : If certain agents in a queue are able to use twinning while others are not, all agents will still receive the call.




## Configuration

Agents will receive twinned calls from the number set as the Global default outbound phone number. Agents should add this phone number to their contacts to avoid having the call marked as spam.

  * When you select **Forward calls to phone number** in the Agent Adapter, all incoming calls for the agent will now be routed to the phone number entered in their user profile.

  * If agents have the web adapter actively open at the same time, they should turn off auto answer.




Because twinned calls are not using the Agent Adapter, the following adapter features are not accessible when Twinning is enabled:

  * `Transfers`

  * `SmartActions`

  * `Hang up`

  * `Call back`




## Grant mobile calls permissions

By default, the Agent role does not allow agents to forward calls to their phones. To allow this capability, you must create a new **Mobile Calls** permission and assign it to any users you want to be able to forward calls. The new role must include the Mobile Calls permission **only** in order to apply it to existing agents.

  1. Go to **Settings > Users & Teams**. Select the **Roles & Permissions** tab at the top of the page.

  2. Click **\+ Add Roles**.

  3. Scroll to **User Profile - My Profile** and click the  arrow_drop_down  on the right to expand the menu.

  4. Check the box next to **Mobile Calls**.

  5. Scroll back to the top to give the new role a **Role name** , **Label name** , and **Description**.

  6. Click **Save** to create the new role.

  7. Click the **Manage Users & Teams** tab at the top of the page to navigate back to the teams page, then click the edit button (pencil icon) next to the user you want to assign the Mobile Calls role to.

  8. Under **Roles** , select **Mobile Calls** from the drop-down menu. Click **Update** to assign the role.




Learn more about [roles and permissions documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent_team_configuration#custom_roles_and_permissions).

## Enable agents to receive calls on their mobile

  1. In the CCAI Platform portal, go to **Settings** > **Operation Management** > **Agent Status**.

  2. Under **Availability Preferences** select **Allow agents to receive calls on their mobile phone**.

  3. Instruct the agent(s) you assigned the Mobile Calls role to to log out of CCAI Platform and then log back in again. If they don't, the new mobile calling fields and features won't appear.




## (Optional) Increase deltacast timeout for mobile agents

Agents who are on-the-go might require more time to pick up a call than agents sitting at a desktop. If you are using deltacast, you can increase the amount of time agents have to pick up calls. To change Deltacast timeout:

  1. Go to **Settings** > **Operation Management** > **Deltacast**.

  2. Set the Deltacast timeout value. The default value is 5 seconds.




## Instructions for agents: Set up call forwarding

Agents must take the following steps in order to enable call forwarding. Make sure that the agents have signed out of CCAI Platform and logged back in again after you assigned them the Mobile Calls role and enabled the twinning feature, otherwise required fields and menu items won't appear.

### Set your mobile number

  1. In the main CCAI Platform menu, select **My Profile**.

  2. In the **Mobile Calls** > **Phone Number** field, enter the phone number you want to receive calls on.




### Enable call forwarding in the Agent Adapter

Agents should now be able to see the **Availability Preferences** feature in the **Change status** drop-down menu in their Call Adapter.

The default setting is **Only Web Agent Adapter (Desktop)**. Even when set to **Forward calls to phone number** , the agent will continue to receive call notifications in their web adapter and are still able to answer the call there if needed.

  1. Open the **Availability Preferences** menu in the **Change status** drop-down.

  2. Select **Forward calls to phone number**.

  3. Click **Save**. 




Any incoming calls for the agent will now be sent to the phone number specified in their user profile.

## View an agent's phone number

You are able to see an agent's mobile phone number, but are not able to change it.

  1. Go to **Settings > Users & Teams**.

  2. Select the edit button next to an agent to view the phone number.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

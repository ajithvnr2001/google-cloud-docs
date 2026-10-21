---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/standard-reports/
title: Creating and viewing standard reports \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:09:37.096733+00:00
---

# Creating and viewing standard reports  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/standard-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Creating and viewing standard reports Stay organized with collections  Save and categorize content based on your preferences. 

CCAI Platform provides two different reporting capabilities; Standard Reports and Advanced Reports. 

## Viewing Chat CSAT Scores

  1. In the Contact Center AI Platform (CCAI Platform) portal, go to **Reports** > **Calls and Chats.**

  2. In Step 1: Select Session Type, choose **Chats**.

  3. In Step 2: Select Chat Types, select the chosen chat types.




The Performance Metrics report is pre-selected.

  1. Select the checkboxes next to **Avg. CSAT Rating** and **Lowest CSAT Rating**.

  2. Select the **Individual Call History Report**.




Select the **Timeframe** and **Time zone** and click **Download.**

The reports will download.

Open both reports generated.

The Individual Chat History Report will show the individual chats and contains the scores, if given, in the CSAT column.

The Chat Type Performance Report will show the summary values for Average CSAT Rating and Lowest CSAT Rating for the time period selected.

## Get session data reports

Session data reports provide session data for chat or call sessions that you specify. You can use this data to map the customer journey across a session or to perform analysis for a quality assurance program.

You can set user level permissions to limit access to session data reports. By selecting **Assigned Teams Only** , only the assigned team has access to the session data report.

To generate a session data report, follow these steps.

  1. In the CCAI Platform portal, click **Reports > Session Data**. If you don't see the **Reports** menu, click menu **Menu**.

  2. Under **Session Types** , select **Calls** or **Chats**.

  3. Under **Session ID(s)** , enter your session ID, and then press **Enter**. Repeat to enter additional session IDs. For more information, see [Session metadata file](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-session-metadata).

  4. Click **Request Data**.




## Using the Report builder

The Report Builder in the Reports tab lets you generate standard reports for the metrics that are important to your organization.

Reports are generated based on three categories: Agents & Teams, Call & Chat, and Queues.

When selected, each report type downloads as a separate CSV file. A folder containing all selected reports will be downloaded once the reports are generated.

The following sections outline the various report types and some example questions that could be answered by the report data.

### Historical data versus Dashboard (real-time) data

With so many data points at your fingertips, there is a lot to take in! The following guidelines can help you compare data across the CCAI Platform real-time and historical reporting features.

  * Reports and dashboards exclude calls abandoned during the menu selection by a consumer if the setting in **Settings** > **Operation Management** >**Customer Abandoned Details** is on. For more details see [Operation Management Settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Operations_Management).

  * Report data excludes voicemails whereas the call dashboard includes voicemails.

  * Report data includes short-abandoned calls, whereas the dashboard may not include this data based on settings in **Settings** > **Operation Management** >**Customer Abandoned Details**.




### Data Limits

The only limit will be in the "Agent Timeline" The report will be broken up into multiple files if it exceeds 1 million rows. Each fill will have up to 1 million rows. 2,300,000 lines will be broken up into 3 files, two that are 1 million in length and one 300k in length

### Sample Reports

There are different report types available, depending on the dataset you are accessing.

When selected, each report type downloads as a separate CSV file.

A folder containing all selected reports will be downloaded once the reports are generated.

  * **Performance Metrics Report** : Custom report where Agents show on each individual row, and the selected metrics appear in each column. Aggregates all agents selected into one report.

    * _What was the average hold time and Average Handle time for Agent A last week?_
  * **Individual Call History Report** : Individual session interaction history for the session type selected. Individual CSV files are created for each Agent selected.

    * _What were 5 call IDs that Agent A handled last week?_

    * _What was the queue time for call 1234 last week?_

  * **Agent Activity - Summary Report** (includes calls and chats when enabled): Generates one csv for all Agents selected. Contains data showing cumulative duration in each status and number of interactions attempted and completed. _How long was Agent A in each status last week?_

  * **Agent Activity - Timeline Report** (includes calls and chats when enabled): Detailed timeline of every event, either performed by an Agent to performed by the system to an Agent's account. CSV files contain data for all Agents selected.

    * _What time exactly did Agent A login and then what time did they take their first call?_

    * _What time was Agent A offered a call using Deltacast?_

    * _Did Agent A try to pick up their calls from 11-12pm?_

  * **Disposition Report** (includes calls and chats when enabled): Lists all selected disposition codes for all agents or queues within the selected timeframe.




### Creating Standard Reports

#### Agents & Teams

  1. From the CCAI Platform portal, go to **Reports > Agent & Teams**.

  2. Select the individual or group of Agents or Teams for which you need to download data:

**All Agents** : Includes all agents within your CCAI Platform environment

**Select Agents and Teams** : Multi-select agents or entire teams by starting to type the Agent or Team name and selecting the option when it appears. Repeat until all Agent and Teams have been selected.

  3. In the **Session Types** list, select **Calls** or **Chats**. Chats include SMS messages.

  4. If you select **Calls** , checkboxes for call types appear. Select the call types that you want to include in the report.

  5. Select the reports needed, and when available select the metrics to include.

  6. Select the **Timeframe** : Adjust period of time the report will cover:

Today: The current date based on your locally configured time zone

Past 24 hours

This week: Starts on Monday at 12:00 am

Last Month

This quarter: Starts at the first day of the current calendar quarter until the current day

Custom: Sliding 90-day range

  7. Select the **time zone** the reports should be generated to reflect.

  8. Click **Download Report**.




#### Calls and Chats

  1. Go to **Reports > Calls & Chats**

  2. Select the **Session Type** For Calls or Chats. A list of call and chat types is provided after step 6.

  3. **Select the reports needed, and when available select the metrics to include**.

  4. Select the **Timeframe**.

  5. Select the **time zone** the reports should be generated to reflect.

  6. Click **Download**.




##### Call and chat types

You can select the call or chat types that you want to include in your reports.

Here are the available call types:

  * **Voice Inbound (IVR)** : standard PSTN calls

  * **Voice Inbound (IVR via Mobile)** : fallback PSTN calls made using the mobile SDKs

  * **Voice Inbound (Mobile)** : calls placed by end-users using the mobile SDKs

  * **Voice Callback (Web)** : calls initiated from the web SDK

  * **Voice Inbound (API)** : calls initiated using an API

  * **Voice Scheduled (Mobile)** : calls scheduled using the mobile SDKs

  * **Voice Scheduled (Web)** : calls scheduled using the web SDK

  * **Voice Outbound** : calls placed by agents dialing a number

  * **Voice Outbound (API)** : calls initiated using an API

  * **Voice Scheduled (API)** : calls initiated by an outbound dialer campaign

  * **Voice Internal** : agent-to-agent calls

  * **Voice Inbound (Direct)** : calls initiated by end-users using agents' direct numbers

  * **Voice Outbound (Direct)** calls initiated by agents using their direct numbers

  * **Voice Outbound (UCaaS)** : outbound, unified communications as a service (UCaaS) calls

  * **Voice Inbound (Extension)** : inbound end-user to agent calls




Here are the available chat types:

  * **Messaging Inbound (Mobile Chat)** : chats initiated by end-users using the mobile SDKs

  * **Messaging Inbound (Web Chat)** : chats initiated by end-users using the web SDK

  * **Messaging Inbound (SMS)** : SMS chats initiated by end-users

  * **Messaging Outbound (SMS)** : SMS chats initiated by agents

  * **Messaging Outbound (SMS via API)** : SMS chats initiated by an API

  * **Messaging Inbound (SMS Direct)** : SMS chats initiated by end-users using agents' direct numbers

  * **Messaging Outbound (SMS Direct)** : SMS chats initiated by agents using their direct numbers

  * **Messaging Outbound (SMS Direct via API)** : SMS chats initiated by an API using agents' direct numbers

  * **Messaging (WhatsApp)** : chats initiated using WhatsApp




#### Queues

  1. From the CCAI Platform portal, go to **Reports > Queues**.

  2. Select the individual or group of Queues for which you need to download data:

**All Queues** : Includes all queues within your CCAI Platform environment.

**Select Queues** : Multi-select queues by starting to type the queue name and selecting the option when it appears. Repeat until all queues have been selected.

  3. Select the **Session Type** : Calls or chats. Chats include SMS messages.

  4. **Select the reports needed, and when available select the metrics to include**. See Report Types for details.

Performance Metrics Report: Select from the available metrics to include.

Individual Call History Report

Disposition Report

  5. Select the **Timeframe** : Adjust period of time the report will cover:

Today: The current date based on your locally configured time zone

Past 24 hours

This week: Starts on Monday at 12:00 am

This quarter: Starts at the first day of the current calendar quarter until the current day

Custom: Sliding 90-day range

  6. Select the **time zone** the reports should be generated to reflect.

  7. Click **Download**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

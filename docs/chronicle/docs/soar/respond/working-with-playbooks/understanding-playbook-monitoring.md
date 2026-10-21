---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/understanding-playbook-monitoring/
title: Monitor playbook performance \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:55:38.077188+00:00
---

# Monitor playbook performance  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/understanding-playbook-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor playbook performance

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document outlines the key locations within the Google Security Operations platform that provide detailed visibility into the execution and performance of your playbooks: 

  * **Playbook monitoring on the**Playbooks** page**: The monitoring feature lets customers use automation to its full capacity. This interface is displayed for each individual playbook. 
  * **Playbook side drawer on the**Cases** page**: The summary feature minimizes the time that an analyst needs to get decisions when handling a case. This interface is displayed as a side drawer for each running playbook on the **Cases** page. 
  * **[Response Health Hub](https://docs.cloud.google.com/chronicle/docs/reports/response-health-monitoring-and-troubleshooting-dashboard)** : Provides platform-wide visibility into playbook performance, execution latency, queue backlogs, automation effectiveness, and integration health across environments. 



This visibility is essential for auditing, debugging errors, and confirming successful workflow completion.

## Access the playbook monitor

The **Playbook monitoring** side drawer is available for each playbook on the **Playbooks** page. 

On the **Playbooks** page, click **Playbook monitoring** to open the side drawer for the selected playbook. 

**Note:** The Playbook simulator needs to be turned off to see the **Playbook monitoring** side drawer. 

The **Playbook monitoring** side drawer contains the following information: 

  * **Runs** : How many times the playbook or playbook block ran during the defined time period. Thousands will be represented by a _K_ , and millions will be represented by an _M_. If a playbook block is added as part of a playbook to an existing alert, the block won't be counted. 
  * **Redundant** : The number of times the playbook or playbook block failed to run because it exceeded the limit of **one** automatically added playbook per alert. A count greater than one suggests you should revise the playbook using logical blocks or other steps to manage execution limits. 
  * **Closed alerts** : Percentage of alerts that were closed by this playbook. 
  * **Average run time** : Average time that this playbook took to run. This statistic can prove useful in identifying weak points in playbooks, such as manual actions and frequently-errored steps. 
  * **Playbook runs status pie chart** : This chart is a cumulative view of playbook statuses over a specified time period, with four possible outcomes: **Finished Successfully** , **Failed** , **Waiting for User Action** , or **Terminated**. Click any section of the chart to view the search results page listing cases with playbooks in that specific status. 
  * **Playbook trends line chart** : This line chart tracks the performance of your playbooks by displaying completed, failed, terminated, and total runs. Use it to evaluate the performance of new playbooks or to verify the impact of recent improvements to existing ones. Place your pointer over any point on the line to see detailed metrics. For example, if you notice a playbook only ran 20 times last month, refine its trigger logic to make it more selective. You can then check the **Playbook Trends** chart to confirm that the playbook's success rate improved after your changes. 
  * **Environments bar chart** : Displays all the environments where this playbook ran. Click each section to return to the search results page. 



##  Access the playbook summary 

To access the playbook summary, follow these steps:

  1. On the **Cases** page, select a case, click an alert, then click the **Playbooks** tab.
  2. Click the hyperlinked playbook name on the left. The playbook summary side drawer opens. This shows the following information:
     * Playbook name and status 
     * Time and length of playbook run 
     * **Pending actions** : When a playbook waits for action from a security engineer, the platform prominently displays a notification at the top of the playbook summary and sends a push notification to the relevant user. 
     * **Integrations** : The platform displays a list of all integrations used by the playbook. Clicking an integration highlights the corresponding step in the playbook viewer, letting the analyst immediately focus on that section. 
     * **Playbook flow** : A detailed view of each step that was run, along with its status and step result. 
     * **Errors** : A list of all errors encountered. Errors that halt the playbook are highlighted in the summary banner, while those that were skipped or non-critical appear at the bottom. For full details, click any error to view the logs page, where you can also rerun the failed action or the entire playbook. 



## Playbook recovery mechanism

The playbook execution engine includes a self-healing mechanism to recover playbooks that get stuck in an executing state (for example, due to an unexpected backend disruption). If a playbook remains in an incomplete state for longer than the configured timeout (default is 48 hours), the system will automatically restart the playbook and resume its execution from the last pending step. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

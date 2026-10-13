---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen/
title: Playbook and automation overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:34.174650+00:00
---

# Playbook and automation overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Playbook and automation overview

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

A playbook is built on triggers, actions, and flows, working together to automate incident response and other security operations tasks. When a trigger initiates a playbook, it proceeds through a series of defined actions to achieve a specific resolution.

The execution of a playbook follows an organized progression:

  * [Trigger](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-triggers-in-playbooks) (yellow box): This is the mandatory first component that initiates the playbook. It defines the conditions or events that cause the playbook to run.
  * [Actions](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-actions-in-playbooks) (blue box): After the trigger, the playbook moves to a set of defined actions it must perform. These are the specific tasks or operations the playbook executes, such as enriching data, notifying users, or isolating a compromised host.
  * [Flow](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-flows-in-playbooks) (purple box): The final component involves determining the flow of the playbook, typically using `if-then-else` conditions. This method gives the playbook the ability to make decisions based on the outcomes of previous actions and branch into different paths to reach a final resolution.



## Open the Playbooks page

To open the **Playbooks** page, go to **Response > Playbooks**.

The following actions are available: 

  * **Plus** ![addicon](https://docs.cloud.google.com/static/chronicle/images/soar/addicon.png): Add a new playbook or block. Select the folder and environment for your new playbook or block. You can select one or multiple environments, environment groups, or a combination of both. If a playbook is associated with a specific environment group, its scope automatically updates if the environment group's scope changes. 
  * **Edit** ![multipleselecticon](https://docs.cloud.google.com/static/chronicle/images/soar/multipleselecticon.png): Select single or multiple playbooks and blocks for use with the **Actions** menu. To rename a folder, click **Edit** , hold the pointer over the folder name, and enter the new name. Once you edit a playbook, you can delete playbooks, as needed. 
  * **Filter** ![filtericon](https://docs.cloud.google.com/static/chronicle/images/soar/filtericon.png): Click  filter_alt  **Filter** and filter the display based on the following criteria:
    * **Playbook simulator is on** toggle 
    * **Show Active Playbooks** toggle 
    * **Priority** : Set the attachment order of playbooks for the alert. Only one playbook attaches automatically, based on priority. 
    * **Environments** : Multi-select option for environments and environment groups.
  * **Menu** ![menuicon](https://docs.cloud.google.com/static/chronicle/images/soar/menuicon.png): Click  edit  **Edit** and select the required playbooks or blocks before using **Menu** to perform bulk actions:
    * **New Folder** : Add a new playbooks folder; the playbook automatically inherits any changes made to its associated environment groups. You can apply playbooks associated with environment groups to cases originating from any environment within those groups.
    * **Duplicate** : Create a duplicate playbook with these options:
      * Keep or change priority
      * Keep in same folder or move to a different folder
    * **Single** , **multiple** , or **all** environments, where **all** indicates all defined environments, present or future.
    * **Export and Import** : Transfer playbooks and playbook blocks between staging and production servers. Playbooks are exported or imported with their customized views included. The system accepts only ZIP files for import. 
    * **Move to** : Move playbooks and blocks to a different folder, or create a new folder.
    * **Delete** : Delete playbooks and blocks. After you click **Delete** , you can delete playbooks. 
  * **Search** : You can use the Search bar to find the playbook you are looking for. 



## Top section of Playbook Designer

The top section of the Playbook Designer provides a comprehensive overview and essential controls for your playbook. You'll find the following features:

  * Horizontal toggle to enable or disable the playbook, offering quick activation or deactivation.
  * Concise summary, detailing the playbook's name, creator, creation timestamp, and associated environment, along with a brief description.
  * Activate the simulator for testing and to add a customized view for enhanced visibility.



Using the Playbook Designer's features, you can do the following actions:

Icon | Description  
---|---  
[ ![openstepicon](https://docs.cloud.google.com/static/chronicle/images/soar/openstepicon.png)  
**Open Step Selection**](https://docs.cloud.google.com/static/chronicle/images/soar/openstepicon.png) | Opens a side drawer with available **Triggers** , **Actions** , **Flow** , and **Blocks**.  
[ ![fittoscreenicon](https://docs.cloud.google.com/static/chronicle/images/soar/fittoscreenicon.png)  
**Fits to screen**](https://docs.cloud.google.com/static/chronicle/images/soar/fittoscreenicon.png) | Automatically adjusts the playbook to fit entirely on the screen.  
[ ![rearrangeicon](https://docs.cloud.google.com/static/chronicle/images/soar/rearrangeicon.png)  
**Rearrange**](https://docs.cloud.google.com/static/chronicle/images/soar/rearrangeicon.png) | Reverts the playbook to its default arrangement.  
[ ![zoomicon](https://docs.cloud.google.com/static/chronicle/images/soar/zoomicon.png)  
**Zoom**](https://docs.cloud.google.com/static/chronicle/images/soar/zoomicon.png) | Zooms in to one or multiple steps in the playbook.  
[ ![downloadpngicon](https://docs.cloud.google.com/static/chronicle/images/soar/downloadpngicon.png)  
**Download**](https://docs.cloud.google.com/static/chronicle/images/soar/downloadpngicon.png) | Downloads the playbook as a PNG file.  
[ ![undoicon](https://docs.cloud.google.com/static/chronicle/images/soar/undoicon.png)  
**Undo**](https://docs.cloud.google.com/static/chronicle/images/soar/undoicon.png) | Reverts any changes that you've made.  
[ ![redoicon](https://docs.cloud.google.com/static/chronicle/images/soar/redoicon.png)  
**Redo**](https://docs.cloud.google.com/static/chronicle/images/soar/redoicon.png) | Revises any changes that you have previously undone.  
[ ![playbookmonitoringicon](https://docs.cloud.google.com/static/chronicle/images/soar/playbookmonitoringicon.png)  
**Playbook monitoring**](https://docs.cloud.google.com/static/chronicle/images/soar/playbookmonitoringicon.png) | Displays the individual playbook statistics.  
[ ![navigatoricon](https://docs.cloud.google.com/static/chronicle/images/soar/navigatoricon.png)  
**Playbook navigator**](https://docs.cloud.google.com/static/chronicle/images/soar/navigatoricon.png) | Displays all playbook actions and flows.  
  
  


For more information about the **Playbooks** page and how to collaborate with it, see the following:

  * [Define custom alert views from Playbook Designer](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/define-customized-alert-views-from-playbook-designer)
  * [Work with the Playbook Simulator](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/working-with-playbook-simulator)
  * [Understand playbook monitoring](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/understanding-playbook-monitoring)
  * [Use the Playbook Navigator](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-playbook-navigator)



## Playbook icons legend

The following icons appear on the **Cases > Playbooks** tab when a playbook is attached. 

[ ![customized alert view.](https://docs.cloud.google.com/static/chronicle/images/soar/playbookstatuslegend.png)](https://docs.cloud.google.com/static/chronicle/images/soar/playbookstatuslegend.png) [ ![customized alert view.](https://docs.cloud.google.com/static/chronicle/images/soar/actionsstatuslegend.png)](https://docs.cloud.google.com/static/chronicle/images/soar/actionsstatuslegend.png)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-predefined-widgets-in-playbook-views/
title: Configure predefined widgets in playbook views \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:36.122208+00:00
---

# Configure predefined widgets in playbook views  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-predefined-widgets-in-playbook-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure predefined widgets in playbook views

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

Predefined widgets are ready-made widgets linked to actions in integrations from the Content Hub. Created by Google SecOps experts, these widgets provide specific information for actions, saving time on customizing and building a playbook view.

After you download the integration, the actions appear as usual when creating a playbook, with special icons that indicate predefined widgets. 

You can use these widgets in existing playbooks or when creating new ones.

## Build a new playbook view with predefined widgets

  1. Go to **Google SecOps Content Hub > Response Integrations** and select **VirusTotal**.
  2. Click **Read More**. Some of the VirusTotal actions come with predefined widgets.  

  3. Download and configure the VirusTotal integration as required.
  4. Go to **Response > Playbooks** and explore how to use an action with a predefined widget.
  5. Create a new playbook, open the **Step Selector** and drag the **VirusTotal Enrich hash** action. 
  6. Click **Add View** and enter a name (contains VirusTotal widgets) and choose a role. In this example, leave the checkbox selected to include predefined widgets. You can choose to opt out or remove them later after creating the view.  

  7. After you create the view, the widget is automatically added to the view. You can only edit these options in this widget: **Name** , **Description** , **Conditions**.  

  8. After the playbook is attached to an alert, it appears on the **Playbook** tab of the case alert view. 



### Add predefined widgets to an existing playbook

  1. Locate the required playbook and open the **Step Selection**.
  2. Drag the **VirusTotal Enrich URL** action into the playbook, and click **Save**.
  3. Open the view, where the predefined widget appears in the **Predefined** column.
  4. Drag it into the view. 



  


**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

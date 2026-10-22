---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/define-customized-alert-views-from-playbook-designer/
title: Configure custom alert views \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:52.891154+00:00
---

# Configure custom alert views  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/define-customized-alert-views-from-playbook-designer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure custom alert views 

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to create customized alert views on each playbook for specific Google SecOps roles. The customized alert views make sure that each Google SecOps user can see the alerts tailored to their specific needs. 

You create the views in the playbook designer and are composed of various widgets that you can drag and edit to create the required view based on the playbook results. For a detailed description of all widgets, see [Default alert view](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/define-default-alert-view-admin). 

**Note:** If a user is newly assigned to a SOC role, the custom alert view for a playbook may not appear immediately. To resolve this, rerun the playbook to render the view. 

By creating customized alert views, you can decide, in advance, what information you want to display to different roles. For example, if you have a collaborator user and you created a Google SecOps role for that user called _Premium Customer Role_ , you can then build a view that contains only the information that fits their role without compromising your organization's security. 

If you don't define a view for a specific Google SecOps role, users with that role will see the default alert view. 

**Note:** A widget won't display for the user if there are no results. 

The customized alert view configuration within the playbook designer may include the following widgets:

  * **JSON results** : View a [JSON](https://en.wikipedia.org/wiki/JSON) result in the system.
  * **Entity Highlights** : View entities associated with the alert.
    * If you're a unified Google SecOps customer, click **Explore** to be redirected to the alert **Asset** page to perform more actions. The page you land on depends on the type of entity. For more information, see [Investigation views](https://docs.cloud.google.com/chronicle/docs/investigation/investigation-views). 
    * If you need more detailed information before taking action, click the entity to go to the **Entity Explorer** page and view its full details.
    * To have a quick look prior to taking action, click **View Details** and a side drawer opens with the entity's highlights.
    * To run a specific action on an entity, you can click  settings  **Settings** and create a manual action from here.
  * **Events Table** : View all alert events and their properties. Click any of the table rows to open a side drawer to see events details. 
  * **HTML** : View the HTML code that contains relevant information from the playbook results.
  * **Free Text** : View Admin-defined information. 
  * **Key Value** : View specific details from various sources and display them in the view. For example: Key- Product Value- [Alert.Product]
  * **Entities Graph** : View a visual graph and other case entity details. Click an entity and a side drawer opens.
  * **Insights** : This widget contains all the Insights from the Playbook insights actions, general insights and any other insights you have added. They will be presented in HTML format.
  * **Pending Actions** : Quickly view all actions awaiting your input to keep the playbook running.
  * **Quick Actions** : This widget provides analysts with immediate access to relevant actions directly within the alert context. For detailed instructions on configuring Quick Actions, including defining actions and parameters, see [Take actions on a case](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/quick-actions).
  * **Rule Overview** : Available only for users of the Google SecOps unified platform. This widget provides information on the curated or custom rule associated with an alert, including a **View Details** button that opens a rule-overview sidebar with comprehensive rule information, including Rule Details (Name, Description, State, Severity, MITRE tags) and YARA-L Rule Code. It also includes a friendly link to manage the rule in the [Curated detections tab](/chronicle/docs/detection/use-curated-detections).



## Create a customized alert view 

This example shows how to build a customized alert view on a phishing email for a Tier 1 role. 

**To add a customized alert view, do the following:**

  1. Go to the alert's **Overview** tab.
  2. On the **Playbooks** page, go to the **Phishing Email** playbook and click **Add View**.
  3. Enter a template name, choose the required role, and then click **Add** ; in this case, _Tier One_. 
  4. Create your customized view by selecting from the following widgets. Drag the selected widgets into the view and then configure them according to your requirements. 
  5. Add a **Pending Actions** widget.
  6. Add two **Free Text** widgets. One is displayed, if there's an approval action. This contains the following placeholder:  
`[Case Outcome - Block approved .ScriptResult]`  
The other widget appears if the outcome isn't approved. `[Case Outcome - Block not approved .ScriptResult]`
  7. Add another **Free Text** widget and name it `Attack Details - Mitre`. This contains the following placeholder: `[Mitre Attack Details.ScriptResult]`. 
  8. Add the **Entities Highlights** widget. 
  9. Add a **JSON** widget, and add the following placeholder: `[Exchange_Search Mails_1.JsonResult]`. 
  10. Add the **HTML** widget. 
  11. Once the appropriate alert has been ingested into the system and the playbook has run, the Tier One role user can enter the platform and see the alert **Overview** with the playbook results. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

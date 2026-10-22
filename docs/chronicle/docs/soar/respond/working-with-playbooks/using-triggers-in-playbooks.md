---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-triggers-in-playbooks/
title: Manage playbook triggers \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:11.197349+00:00
---

# Manage playbook triggers  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-triggers-in-playbooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage playbook triggers

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

An ingestion trigger defines the initial conditions that cause a playbook to attach automatically when a new alert or case enters the system. You configure these triggers during the initial phase of building a playbook.

To view your options, open the **Triggers** menu and select the **Ingestion** tab.

## Available ingestion triggers

The options on the **Ingestion** tab dynamically change based on the scope you choose when setting up the playbook.

### Case scope ingestion triggers

When you configure a playbook with a **Case** scope, the menu filters down to these options:

  * **All** : Attaches the playbook to every newly created case.
  * **Custom Trigger** : Attaches the playbook based on specific filtering rules you define.
  * **Tag Name** : Attaches the playbook only when a case contains specific tags. You can manage these tags in **SOAR Settings > Case Data > Tags**.



### Alert scope ingestion triggers

When you configure a playbook with an **Alert** scope, you can choose from these options:

  * **Alert Trigger Value** : Triggers based on a predefined field from the connector. We recommend using **Custom Trigger** instead.
  * **Alert Type** : Triggers based on the **Rule Generator** field configured during connector setup. For details, see [Configure the connector](https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/configuring-the-connector).
  * **All** : Triggers the playbook for every alert generated in your environment.
  * **Custom List** : Triggers based on a predefined custom list in your settings.
  * **Custom Trigger** : Triggers based on custom placeholders for specific matches.
  * **Network Name** : Triggers if an alert involves an entity within a defined subnet.
  * **Product Name** : Triggers when an alert comes from a specific product or connector.
  * **Tag Name** : Triggers if a specific tag is added during ingestion. You can manage these tags in **SOAR Settings > Case Data > Tags**.



For event-based and lifecycle triggers that fire during an active investigation, see [Use reaction triggers in playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-reaction-triggers-in-playbooks).

## Add an ingestion trigger to a playbook

To add an ingestion trigger to your workflow, follow these steps:

  1. Create a new playbook. For details, see [Create and edit a playbook with Gemini](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/create-edit-playbook-with-gemini).
  2. In the playbook creation dialog, select your playbook **Scope** (**Alert** or **Case**) to load the correct trigger set, then click **Create**.
  3. On the **Step Selection** menu, select **Triggers**.
  4. Select the **Ingestion** tab, choose a trigger, and drag it to the first step box on the playbook canvas.
  5. Double-click the trigger icon on the canvas to open the parameters side drawer.
  6. Under **Parameters** , define your evaluation criteria (such as **Equal** , **Contains** , or **Starts With**) and enter the target value for your automation rules. 



After you save your changes, the parameter details appear directly in the trigger description on the canvas.

You can now continue building the playbook with actions. For more information, see [Manage actions in playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-actions-in-playbooks).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-automation/
title: Create your first playbook \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:30.751013+00:00
---

# Create your first playbook  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-automation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create your first playbook 

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to create your first playbook using the actions you created in [Create custom actions](https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-action).

The playbook you'll build is for a basic phishing use case and automates the following steps:

  * **Extract domain details** : The playbook extracts the domain from a URL found in an alert.
  * **Enrich the domain** : It then enriches the entity with additional information.
  * **Add an insight** : The playbook adds an insight containing the domain's country.
  * **Check a custom list** : It checks if the country is on a custom list.
  * **Use an**IF** condition**: An **IF** condition is used to determine if the case requires further investigation based on whether the country is on the custom list.



## Enable actions in the playbook designer

To make sure that the custom actions you created are enabled in the Integrated Developer Environment (IDE), click the **Enable** toggle to the on position. Once enabled, these actions are available in the playbook designer.

## Create a custom list of OECD countries

To determine if a domain's country requires further investigation, you need to create a custom list of Organisation for Economic Co-operation and Development (OECD) countries. You can then use this list in your playbook to check against the domain's country.

To create a custom list of OECD countries, follow these steps:

  1. Go to **Settings > Environments**.
  2. Click **Custom lists**.
  3. In the **Custom lists** section, click  add **Add**.
  4. In the **Add Custom List** dialog, enter and **Entity Identifier** , **Category** , and **Environment**.
  5. Click **Add**.



## Create an automation playbook

To create an automation playbook, follow these steps:

  1. Go to **Playbook Designer** and click add**Add**. 
  2. In the **Create New** dialog, select the **Playbook** radio button.
  3. Choose a folder and an environment for the playbook. 
  4. Enter a name for the playbook (next to the playbook toggle) to start customizing your playbook. 



## Import a premade playbook

To import a premade playbook, follow these steps:

  1. In the **Playbook Designer** , click format_list_bulleted**List** > login **Import**.  
[Create my first automation playbook](https://docs.cloud.google.com/static/chronicle/docs/soar/respond/start-developing/my-first-automation-playbook_v3.zip)
  2. Every playbook starts with a trigger. To set this playbook's trigger, drag the **All** trigger from the **Triggers** menu to the first step of the playbook. This causes the playbook to activate on every alert ingested into Google Security Operations. 



## Create a playbook

To create a playbook using the actions from your "WHOIS XML API" integration, follow these steps:

  1. In the **Actions** tab, click the **WHOIS XML API** list. Your custom actions will appear under the integration name. If they're not visible, confirm that they're enabled and saved in the IDE module. 
  2. Drag the **Get Domain Details** action into the playbook, placing it right after the trigger.



## Customize the action

You can customize the action to run on a specific scope. In this example, run the action on all entities that are URLs. For the domain name field, use the `Entity.Identifier` placeholder.

To make these customizations, do the following:

  1. Insert the placeholder: click data_array **Placeholder** and search for `Entity.Identifier` in the search bar. This action connects to the "WHOIS" site, extracts the details of the Domain, and presents them in JSON format.
  2. Define the scope. The action connects to the "WHOIS" site, extracts domain details, and presents them in JSON format.
  3. Check availability. The **Check Availability** parameter you defined for the action checks if the domain is available or not.
  4. After adding the **Get Domain Details** action, drag the **Enrich Entities** action into your playbook. Customize it to run on All URLs. Because you designed this action to operate on a specific entity scope, you don't need to define the **Domain name** field, as you did with the previous action. 



## Add the Entity Insight action

Add the **Add Entity Insight** action which is part of the Google SecOps Integration:

  1. Define the scope. For the **Entity** scope, select **All URLs** , as you did for the previous actions in the playbook.
  2. Extract the JSON field. In the **Insight** field, open the **Google SecOps Expression builder** to extract the country field from the JSON result.
  3. Open the expression builder for the JSON output: Click the placeholder icon (`data_array`), choose the playbook list, and select `WHOIS XML API_Get Domain Details_1.JsonResult`. This opens the expression builder for the JSON output.



## Extract the country field from the JSON

The JSON sample in the expression builder is the same one you inserted in the IDE for [Create your custom action](https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-action). To extract the `Country` field, follow these steps:

  1. Click **Country** in the JSON.
  2. Click arrow_right **Run** to test the placeholder, and view the result under the **Results** field. 



## Create an entity

To run the **Is in custom list** action, you need to create a new entity from the country related to the domain. To do this, follow these steps:

  1. From **Google SecOps Integration** , drag the **Create Entity** action into the playbook.
  2. Configure the action to run on **All URLs**.
  3. Use the expression builder to insert the `country` placeholder in the **Entity Identifies** field. For the **Entity Type** , choose **Generic Entity** and click **Save**.
  4. Add the **Is in Custom List** action:
     1. Drag the action into the playbook.
     2. Configure it to run on all generic entities (the entity you just created).
     3. For the **Category** , add the category you configured for your custom list of OECD countries.
  5. Add the **IF condition** to your playbook to determine whether the domain's country requires further investigation. The first branch checks if the script result for the **Is in Custom list** returned a false result and the **Else** branch will go to the opposite result. 
     * Add the **IF Condition** action to your playbook. Two branches appear.
  6. Customize the first branch. The first branch executes if the **Is in Custom List** action returns a false result. This means the domain's country is not in your custom list of OECD countries and requires further investigation.
  7. For the first action in this branch, drag a **Case Tag** action from the Google SecOps integration.



## Assign the case to a higher tier

Assign the case to a higher tier to further investigate this case. To do this, follow these steps:

  1. Drag the **Assign Case** action to the playbook.
  2. Choose **@Tier2** as the **Assigned User**. 



## Change the priority

Change the priority to **High** using the **Google SecOps Change Priority** action > click **Save**. 

## Customize the Else branch

After finishing the first branch, you can customize the **Else** branch. This branch handles cases where the domain's country is an OECD country, which you've decided doesn't require further investigation. To configure the **Else** branch, follow these steps:

  1. Add a case tag, as you did in the first branch, with the label **In OECD countries**.
  2. Add a **Close Case** action to this branch. Because closing a case is a sensitive action, you should configure it to run manually. In the **Settings** section of the action, select **Manual** mode.
**Note:** This requires an analyst's response before the action can be executed.
  3. In the **Parameters** section of the **Close Case** action, add the **Reason** , **Root Cause** , and **Comment**.
  4. Click **Save** to save the playbook with the added parameters. 



## View the playbook execution

To see your customized automation in action, follow these steps:

  1. In **Cases** , click  add  **Add** > **Simulate Cases**.
  2. Select **Phishing Email** case > click **Create**.
  3. Select the **Environment** > click **Simulate** to simulate the playbook execution.
  4. View the playbook running on the alert and see the results of each action in the playbook.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

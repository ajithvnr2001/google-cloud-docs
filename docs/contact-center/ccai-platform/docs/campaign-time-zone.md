---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-time-zone/
title: Time zone list management \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:26.475567+00:00
---

# Time zone list management  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-time-zone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Time zone list management Stay organized with collections  Save and categorize content based on your preferences. 

Time zone management settings simplify managing different time zones and calling time standards. With Time Zone Management settings, campaigns can be configured to only call authorized numbers during permitted time frames. This can help you comply with regional telemarketing regulations.

You need **Queues Manager View/Edit** permissions to configure time zone management settings.

## Understanding time zone components

Before setting up time zone management, it's important to understand the following key components:

  * **Time zone rule** : a rule specifying when an outbound call can be placed, consisting of a time zone code and time span

  * **Time zone schema** : a set of time zone rules grouped together with a unique name, used to organize and manage time zone settings

  * **Code** : a label for the time zone rule

  * **Time zone** : each rule can only contain one time zone

  * **Time span** : a range of times that apply to specific days




## Access time zone management settings

To access the time zone management settings, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Click the queue that you want to edit.

  3. Select **Manage setting** to open the time zone management settings menu.




## Create a time zone rule

  1. Select the **Add time zone rule button** in the upper right corner.

  2. Select a **Time Zone** from the drop-down in the **Time Zone** field. The time zones align with existing hours of operations time zones.

  3. Enter a name for your time zone rule in the code field.

  4. **Choose a time span** by selecting the radio button next to your selection:

     * **Default time span** : This option chooses every weekday by default, and you just need to select the time span for the rule (uses 24-hour time).

     * **Custom time span** : This option lets you adjust the hours for each day of the week individually (use 24-hour time).

  5. Click **Save**. You will then see this rule in the time zone rules tab, and it will be available to choose when creating a time zone schema.




## Edit a time zone rule

To edit a time zone rule, follow these steps:

  1. On the time zone rules list, select the options (3 horizontal dots) on the right-hand side of the **Time Zone Rule** to edit. You will see the option to delete or edit each rule.

  2. Click **Edit Rule**. A new box will appear where you can change the rule.

  3. Make your selections and click **Save**.




## Delete a time zone rule

If a time zone rule is deleted that is used in any time zone schema, you'll see a warning message. You can proceed, but the rule will be excluded from all schemas which contain it.

To delete a time zone rule, follow these steps:

  1. Select the Options (3 horizontal dots) on the right-hand side of the time zone rule menu page.

  2. Click **Delete Rule**.




## Create a time zone schema

You can group a collection of time zone rules to create a time zone schema. You can create up to 100 different Schemas if you have multiple campaigns, and each requires a different set of rules.

**Note:** A default time zone rule is automatically created for each time zone schema.

To create a new time zone schema:

  1. Go to the **Time Zone Schema**.

  2. Select the **Add time zone schema** button in the upper right corner.

  3. Enter a name for your **Time Zone Schema** in the **Name** field. Names must be unique, and no longer than 64 alphanumeric characters.

  4. Select a **Time Zone** from the drop-down in the **Time Zone** field.

  5. Choose a **Time Span** by selecting the radio button next to your selection:

     * **Default time span** : This option chooses every weekday by default. You just need to select the time span for the rule (use 24-hour time).

     * **Custom time span** : This option lets you adjust the hours for each day of the week individually (use 24-hour time).

  6. Click **Save** to save the schema. You may then add additional rules as needed.




## Add new rules to an existing time zone schema

To add new rules to an existing time zone schema:

  1. Go to the **Time Zone Schema** tab.

  2. Select the name of the **Time Zone Schema** to add the rule to.

  3. Here you will see a list of all the **Time Zone Rules** contained within the schema. Select **Add time zone rule** to add an existing rule, or **Create time zone rule** to create a new rule.

     * If you choose **Add time zone rule:**

       1. A drop-down list will appear where you can select an existing rule.

       2. Click **Save** to add the rule to the schema.

     * If you choose **Create time zone rule** :

       1. Select a time zone from the drop-down in the Time Zone field.

       2. Enter a name for your time zone rule in the Code field.

       3. Select the radio button for the Time Zone Span field to create a new rule (Every weekday + time span, or Custom time span).

          * **Default time span** : This option chooses every weekday by default, and you just need to select the time span for the rule (use 24-hour time).

          * **Custom time span** : This option lets you adjust the hours for each day of the week (use 24-hour time).

       4. Click **Save** to add the rule to the schema.




## Edit an existing time zone schema

There are two methods to edit a time zone schema, depending on whether you want to change the default rule or a secondary rule within the schema.

To edit the default rule in the schema:

  1. Select the options (3 horizontal dots) on the right-hand side of the Time Zone Schemas menu page. You will see the option to delete or edit the schema here.

  2. Click **Edit Schema**. A new box will appear where you can change the Schema.

  3. Make your selections and click **Save**.




To edit any rule in the schema:

If the rule applies to multiple Schemas, the rule will be changed for all Schemas which contain the rule.

  1. Select the folder with the time zone schema to change on the time zone schemas menu page.

  2. Select the Options (3 horizontal dots) on the right-hand side of the rules contained within. This will open the schema and you will see the full list of time zone rules.

  3. Select the options (3 horizontal dots) on the right-hand side of the Time Zone rules list. You will see the option to delete or edit each rule.

  4. To edit the rule, click **Edit Rule**. A new box will appear where you can change the rule.

  5. Make your selections and click **Save**.




## Delete an existing time zone schema

If a time zone schema is deleted that is used in any Queue, you will see a warning message. You can proceed, but the schema will be de-assigned from all Queues which contain it.

To delete an existing time zone schema:

  1. Select the Options (3 horizontal dots) on the right-hand side of the time zone schemas menu page. You will see the option to delete or edit the schema here.

  2. Click **Delete Schema**.

  3. A confirmation screen will appear, asking if you are sure you want to delete the schema.

     * Click **Cancel** if you decide to keep the schema.

     * Click **Delete** if you want to delete the schema.




## Applying time zone schemas to queues

Once created, time zone schemas can be applied to existing queues or new queues.

To apply a schema to an existing queue:

  1. Go to the **Queue Manager**.

  2. Locate the queue to apply the Schema to in the list.

  3. Hover over the queue to edit, and a pencil-shaped icon will appear in the far right column of the table. Select the pencil icon and an **Edit Queue** window will appear.

  4. In the **Edit Queue** window, there is an assign time zone schema field with a drop-down selector.

  5. Select the **Time Zone Schema** you want to use from the list.

  6. Select **Save** to update your selections.




To apply a schema to a new queue:

Schemas are not applied to queues by default. Queues can work either with or without time zone schemas.

To apply a time zone schema to a queue, follow these steps:

  1. Go to the **Queue Manager**.

  2. Select the **Create Queue** button in the upper right-hand corner of the page, and an **Add Queue** window will appear.

  3. At the bottom of the **Add Queue** window, there is an **Assign Time Zone Schema** field with a drop-down selector.

  4. Select the **Time Zone Schema** you want to use from the list.

  5. Click **Save** to update your selections.




## Use time zone schemas in queues

Here's how time zone schemas behave when applied to queues:

  * When uploading a queue CSV file, in order for time zone to be considered, it must be included as its own value.

  * Time zone schemas aren't applied by default. If none is assigned, the dialer calls all contacts in the list as usual.

  * Time zone schemas apply to all dialer modes once applied.

  * If a time zone schema is assigned to a queue, the dialer follows the rules contained in the schema.

    * The dialer compares the value from the contact's time zone field against the name of each rule in the assigned time zone schema.

    * If the values match, then the relevant time zone rule is applied, and the dialer only places a call during the time span in the related rule.

    * If the time zone field of a contact doesn't match any of the time zone rules in the schema, or is not set, then the default time zone rule for that schema is used.

  * The dialer skips contacts that it can't call and calls the ones that it can.

  * After all of the contacts in the list have been processed, the dialer begins the process again to see if there are any skipped calls that it can make.

  * New contacts are added to the list without triggering a list review.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

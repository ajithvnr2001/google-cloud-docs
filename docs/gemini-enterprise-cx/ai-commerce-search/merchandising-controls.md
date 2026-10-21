---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/merchandising-controls/
title: Serving controls in the Merchandising console \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:02.941770+00:00
---

# Serving controls in the Merchandising console  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/merchandising-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Serving controls in the Merchandising console Stay organized with collections  Save and categorize content based on your preferences. 

The Merchandising console is a tool designed for you to create and administer controls. It provides an approval flow so that every control can be proposed by all merchandisers and reviewed by approvers.

The Merchandising console helps [create serving controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#control-types) such as pinning, boost/bury, synonyms and facets. The Merchandising console brings you closer to a rules-as-a-service arrangement with AI Commerce Search. For example, instead of having to configure boost or bury manually, Merchandising console reduces the number of products that show up for specific queries.

## Configure Identity and Access Management in the Merchandising console

In Google Cloud, to access the Merchandising console tab, you must have at a minimum these permissions:

  1. **Project viewer (Viewer)** to access the project.

  2. **Retail editor** to edit and save Merchandising console settings.




### Access the console as a Creator

In the Merchandising console, **Creators** can:

  * Define the goal.
  * Select a control.
  * Set rules and preview.
  * Create a new control and save it as a draft for approval.
  * Submit a new control for approval.
  * View drafts they have created.
  * View all controls on the Google Cloud.



A **Creator** cannot, however, edit published controls.

![Merchandiser \(Creator\) view of the Merchandising console](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/merchandising-console-creator-view.png)Merchandiser (Creator) view of the Merchandising console

### Access the console as an Approver

In the Merchandising console, **Approvers** can:

  * Set approval flow.
  * See the status of all request.
  * Review and approve.
  * View and edit all controls on the Google Cloud.



![Merchandiser \(Approver\) view of the controls in the console](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/merchandising-console-approver-view.png)Merchandiser (Approver) view of the controls in the console

Click the arrows to expand the option that applies to you.

### Use the console as an administrator

![View the merchandising console tab in the Control page.](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/merchandising-console-tab.png)Merchandising console tab

Before you start, you must be a Google Cloud administrator to onboard users to the Merchandising console. Then, proceed with these next administrator set up steps.

#### Set up administrator access to Merchandising console

You need these IAM roles to access, edit, and assign **Creator** or **Approver** roles to a Merchandising console user:

  * To edit the Merchandising console, at least the **Retail Editor** role is required.
  * To assign **Creator** or **Approver** roles to a user, a **project-level IAM admin** role is required.

**Note:** A **Retail Editor** with such **IAM Admin** role won't be able to self-promote to a higher access privilege. 

For a complete layout of IAM project-level and AI Commerce Search permissions, refer to the [Predefined administrator roles](/gemini-enterprise-cx/ai-commerce-search/iam#roles) section in this [AI Commerce Search product](/gemini-enterprise-cx/ai-commerce-search/iam) documentation.

#### Access the Merchandising console tab

Access the Merchandising console by accessing the Merchandising console tab within the Google Cloud console:

  1. Navigate to **AI Commerce Search in Gemini Enterprise for Customer Experience**.
  2. Click **Controls**.
  3. Navigate to the **Merchandising console** tab.



#### Add Merchandising console users

If you're a Google Cloud console administrator, to give site merchandisers access to the Merchandising console and assign either a **Creator** or an **Approver** role to them:

  1. Go to the **Controls** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)
  2. Navigate to the **Merchandising console** tab.
  3. You can see the unique URL to the Merchandising console associated with the current Google Cloud project. Copy the link or directly open it in the Google Cloud console.
  4. Select the default serving config merchandisers are to use to **Preview** and **Attach** approved controls.
  5. Give users either **Approver** or **Creator** roles.
  6. You can see the unique URL to the Merchandising console associated with the current Google Cloud project. Copy the link or directly open it in the Google Cloud console.
  7. Select the default serving config for **Preview** in the **Merchandising** console.
  8. (Optional) Edit access to the Merchandising console using these functions:
     * **Add users** : Give users **Approver** or **Creator** access to the **Merchandising console**.
     * **Delete users** : Revoke access to the Merchandising console by deleting **Approvers** or **Creators**.
  9. Add approver emails. For each control submitted by merchandisers, the approver receives an email to review and approve this control.



#### Access the console as a user

If you have been given access with the URL, you have the option of using the Merchandising console instead of the standard Google Cloud console. To create controls using the Merchandising console: 

  1. Sign in using the credentials that your administrator provides you.
  2. Follow the Merchandising console documentation steps under [each serving control section](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#control-types).
  3. After submission, you receive a notification email with the subject **[Merchant Console] Proposed control awaiting review**.
  4. As an **Approver,** you can **accept,** **deny,** or **change** the control request.



See information about other controls for admins only.

### Use the console as a site merchandiser

Follow these steps to get started in the Merchandising console as a site merchandiser.

  1. **Set approval flow for questions.**
     1. Navigate to the _settings_**Settings** part of the main menu.
     2. By default, a predefined list of questions are set in **Define the goal** screen.
![Open merchandising console questions.](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/merchandising-console-questions.png)Merchandising console questions
     3. Add a question by clicking _add_box_**Add question** to help **Approvers** understand the purpose of the new controls. 
     4. Click **Save** to save the questions.
  2. **Create a control**.
     1. Go to the **Controls** section.
     2. Click _add_box_**Create control**.
     3. **Define the goal** : All questions previously defined are required to be answered. If you haven't defined any questions yet, this screen won't appear.
     4. **Select a control**. Specify the [control type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#control-types) and assign a name to the control.
     5. **Set rules** : For each rule, you can define triggers and actions.
     6. Define **Triggers** : The goal is to establish when to apply this control.
        * **Query terms** : This rule can be triggered when your search query contains or exactly matches specific terms. You can define these query terms.
        * **Applicable time ranges** : Time restrictions can be applied to confine the activation of this rule to specific time periods.
![Enter trigger definitions in the fields.](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/merchandising-console-triggers.png)Define triggers
     7. **Define actions** : Depending on the type of control, you can define actions, such as Item ID and position for a pinning control.
     8. **Preview a rule** : A dynamic preview of the rule can be seen on the screen.
     9. **Submit a rule** : After you click **Submit** to submit the rule set by the merchandiser, you can view the control as **Pending** in the controls list.
  3. **Approve a control**
     1. To grant approval for a control, click the _more_vert_**More** icon next to the control in the control list. Select **Review**. 
     2. A screen is provided for the given control where you can **Approve,** **Deny,** or **Approve with edits**.
     3. After approval, you are redirected to the controls list page that shows the control as **Approved**. ![The merchandising control stages.](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/merchandising-console-draft-stages.png)Merchandising console stages



## Create and manage controls in Merchandising console

This section covers all ways you can create and manage controls for your search functions in Merchandising console.

The Merchandising console features a user-friendly interface that lets you efficiently create and manage controls. This tool also facilitates an approval process, allowing any merchandiser to propose controls and merchandiser approvers to review them.

### Create serving controls in the Merchandising console

  * ![Create control in the merchandising console.](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/merchandising-create-control-1.png)
  * ![Create control as a Merchandiser Creator.](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/merchandising-create-control-merchandiser-creator-2.png)
  * ![Create control as a Merchandiser Approver.](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/merchandising-create-control-merchandiser-approver-2.png)



To create a serving control in Merchandising console, you must select an option for each configuration step in this order:

1\. Control type | 2\. Actions | 3\. Triggers | 4\. Serve  
---|---|---|---  
Search | Boost/bury | Query | Default search  
Browse | Pinning | Page category | Clienteling (serving config example)  
| Filtering | Time ranges | Test A (serving config example)  
| Synonyms |  | Test B (serving config example)  
| Redirect |  |   
  
Click each action for how to configure the controls in the Merchandising console.

### Configure a control in the Merchandising console

This section breaks down the components of control configurations in Merchandising console.

#### Control trigger

A control trigger, on the other hand, is the definition of when the control is applied. For example, according to a given time range or a query term.

#### Control service

A control is served according to configuration set in serving controls (rules), meaning the types of controls you can create, and in serving configs (set of rules) that determine where the controls are applied.

For more information, see [Relationship between serving controls and configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#relationship-serving-control-config).

#### Control actions

A control action is a classification of what the control does. This is the primary configuration for a control.

Scroll through the control action tabs for instructions on how to create, trigger and serve each control in the Merchandising console as a Creator. If you are an Approver, after reviewing the general instructions in your control action tab, refer to the special section for Additional approver steps.

###  Boost or bury 

  1. Click the URL provided by the administrator. Sign in.

This takes you to the **Controls** page in the **Merchandising console**.

  2. Click _add_box_**Create control**.

  3. Define the goals for your end users and timing required. All questions are required to be answered. Click **Next**.

  4. **Select a control**. Enter the name for your control, select the **Search** product, then choose the control type **Boost/Bury**.

  5. Configure your **Boost/Bury** control:

     1. Under **Triggers** , define what catalog attribute triggers this control by giving criteria to a related search query, such as _contains_ or _not in range_. If no catalog attribute has been configured, this control will always apply.

     2. Define an **Applicable time range** by entering a **Date range**. If any of the specified time ranges are met, the catalog attribute will be matched with the query during any of the specified time ranges. Add a time range with _add_box_**Add time range**.

     3. Define the **Boost/Bury actions** you want to trigger with this control. These actions are defined by a **Catalog attribute** such as _colors_ , a **Criteria** such as _contains,_ and **Value** such as _red._

     4. Click _add_box_**Add attribute** to add more attributes.

  6. Use the slider to set your **Boost/bury value**. Negative numbers are bury, and positive numbers are boost.

  7. Click **Submit** to submit your control request to an Approver. You will be able to see the status of submitted requests in the Merchandising Console. Alternatively, you can **Save** a control **Draft** for later. If you change your mind, you can delete your control request.




For more information, refer to [Create boost/bury controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#boost-bury) and their [rules](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#boost-bury).

###  Filter 

  1. Click the URL provided by the administrator. Sign in.

This takes you to the **Controls** page in the **Merchandising console**.

  2. Click _add_box_**Create control**.

  3. Define the goals for your end users and timing required. All questions are required to be answered. Click **Next**.

  4. **Select a control**. Enter the name for your control, select the **Search** or **Browse** product, then choose the control type **Filter**.

  5. Configure your **Filter** control:

     1. Under **Triggers** , define what catalog attribute triggers this control by giving criteria to a related search query or page category, such as _contains_ or _not in range_. If no catalog attribute has been configured, this control will always apply.

     2. Define an **Applicable time range** by entering a **Date range**. If any of the specified time ranges are met, the catalog attribute will be matched with the query during any of the specified time ranges. Add a time range with _add_box_**Add time range**.

     3. Define the **Filter actions** you want to trigger with this control. These actions are defined by a **Catalog attribute** such as _colors,_ a **Criteria** such as _contains,_ and **Value** such as _red._

     4. Click _add_box_**Add attribute** to add more attributes.

  6. Click **Submit** to submit your control request to an Approver. You will be able to see the status of submitted requests in the Merchandising Console. Alternatively, you can **Save** a control **Draft** for later. If you change your mind, you can delete your control request.




For more information, refer to [Create filter controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#filter) and their [rules](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#filter).

###  Redirect 

  1. Click the URL provided by the administrator. Sign in.

This takes you to the **Controls** page in the **Merchandising console**.

  2. Click _add_box_**Create control**.

  3. Define the goals for your end users and timing required. All questions are required to be answered. Click **Next**.

  4. **Select a control**. Enter the name for your control, select the **Search** product, then choose the control type **Redirect**.

  5. Configure your **Redirect** control:

     1. Under **Triggers** , define what catalog attribute triggers this control by giving criteria to a related search query, such as _contains_ or _not in range_. If no catalog attribute has been configured, this control will always apply.

     2. Define an **Applicable time range** by entering a **Date range**. If any of the specified time ranges are met, the catalog attribute will be matched with the query during any of the specified time ranges. Add a time range with _add_box_**Add time range**.

     3. Define the **Redirect actions** you want to trigger with this control by entering the redirect URL.

  6. Click **Submit** to submit your control request to an Approver. You will be able to see the status of submitted requests in the Merchandising Console. Alternatively, you can **Save** a control **Draft** for later. If you change your mind, you can delete your control request.




For more information, refer to [Create redirect controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#redirect) and their [rules](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#redirect).

###  Don't associate 

  1. Click the URL provided by the administrator. Sign in.

This takes you to the **Controls** page in the **Merchandising console**.

  2. Click _add_box_**Create control**.

  3. Define the goals for your end users and timing required. All questions are required to be answered. Click **Next**.

  4. **Select a control**. Enter the name for your control, select the **Search** product, then choose the control type **Do not associate**.

  5. Configure your **Do-not-associate** control:

     1. Under **Triggers** , define what catalog attribute triggers this control by giving criteria to a related search query, such as _contains_ or _not in range_. If no catalog attribute has been configured, this control will always apply.

     2. Define an **Applicable time range** by entering a **Date range**. If any of the specified time ranges are met, the catalog attribute will be matched with the query during any of the specified time ranges. Add a time range with _add_box_**Add time range**.

     3. Under **Do not associate actions,** specify the terms that should not be associated with the query terms you entered in the previous **Triggers** section. Enter them into the query terms and disassociated terms fields, respectively.

  6. Click **Submit** to send your control request to an Approver. You will be able to see the status of submitted requests in the Merchandising Console. Alternatively, you can **Save** a control **Draft** for later. If you change your mind, you can delete your control request.




For more information, refer to [Create do-not-associate controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#do-not-associate) and their [rules](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#do-not-associate).

###  Ignore 

  1. Click the URL provided by the administrator. Sign in.

This takes you to the **Controls** page in the **Merchandising console**.

  2. Click _add_box_**Create control**.

  3. Define the goals for your end users and timing required. All questions are required to be answered. Click **Next**.

  4. **Select a control**. Enter the name for your control, select the **Search** product, then choose the control type **Ignore**.

  5. Configure your **Ignore** control:

     1. Under **Triggers** , define what catalog attribute triggers this control by giving criteria to a related search query, such as _contains_ or _not in range_. If no catalog attribute has been configured, this control will always apply.

     2. Define an **Applicable time range** by entering a **Date range**. If any of the specified time ranges are met, the catalog attribute will be matched with the query during any of the specified time ranges. Add a time range with _add_box_**Add time range**.

     3. Enter the terms you want to have ignored under **Ignore actions**.

  6. Click **Submit** to submit your control request to an Approver. You will be able to see the status of submitted requests in the Merchandising Console. Alternatively, you can **Save** a control **Draft** for later. If you change your mind, you can delete your control request.




For more information, refer to [Create ignore controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#ignore) and their [rules](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#ignore).

###  Replacement 

  1. Click the URL provided by the administrator. Sign in.

This takes you to the **Controls** page in the **Merchandising console**.

  2. Click _add_box_**Create control**.

  3. Define the goals for your end users and timing required. All questions are required to be answered. Click **Next**.

  4. **Select a control**. Enter the name for your control, select the **Search** product, then choose the control type **Replacement**.

  5. Configure your **Replacement** control:

     1. Under **Triggers** , define what catalog attribute triggers this control by giving criteria to a related search query, such as _contains_ or _not in range_. If no catalog attribute has been configured, this control will always apply.

     2. Define an **Applicable time range** by entering a **Date range**. If any of the specified time ranges are met, the catalog attribute will be matched with the query during any of the specified time ranges. Add a time range with _add_box_**Add time range**.

     3. Under **Replacement actions,** define the query terms you want replaced in the first field, and their substitutes in the second field.

  6. Click **Submit** to send your control request to an Approver. You will be able to see the status of submitted requests in the Merchandising Console. Alternatively, you can **Save** a control **Draft** for later. If you change your mind, you can delete your control request.




For more information, refer to [Create replacement controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#replacement) and their [rules](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#replacement).

###  Pinning 

  1. Click the URL provided by the administrator. Sign in.

This takes you to the **Controls** page in the **Merchandising console**.

  2. Click _add_box_**Create control**.

  3. Define the goals for your end users and timing required. All questions are required to be answered. Click **Next**.

  4. **Select a control**. Enter the name for your control, select the **Search** product, then choose the control type **Pinning**.

  5. Configure your **Pinning** control:

     1. Under **Triggers** , define what catalog attribute triggers this control by giving criteria to a related search query, such as _contains_ or _not in range_. If no catalog attribute has been configured, this control will always apply.

     2. Define an **Applicable time range** by entering a **Date range**. If any of the specified time ranges are met, the catalog attribute will be matched with the query during any of the specified time ranges. Add a time range with _add_box_**Add time range**.

     3. Define the **Pinning actions** you want to trigger with this control. These actions are defined by **Product ID** and the pin position, preferably a number less than 120 (the typical page size). You can click _add_box_**Add product** and add up to 10.

  6. Click **Submit** to submit your control request to an Approver. You will be able to see the status of submitted requests in the Merchandising Console. Alternatively, you can **Save** a control **Draft** for later. If you change your mind, you can delete your control request.




For more information, refer to [Create pinning controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#pinning) and their [rules](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#pinning).

###  Two-way synonym 

  1. Click the URL provided by the administrator. Sign in.

This takes you to the **Controls** page in the **Merchandising console**.

  2. Click _add_box_**Create control**.

  3. Define the goals for your end users and timing required. All questions are required to be answered. Click **Next**.

  4. **Select a control**. Enter the name for your control, select the **Search** product, then choose the control type **Synonyms**.

  5. Configure your **Two-way synonym** control:

     1. Under **Triggers** , define what catalog attribute triggers this control by giving criteria to a related search query, such as _contains_ or _not in range_. If no catalog attribute has been configured, this control will always apply.

     2. Define an **Applicable time range** by entering a **Date range**. If any of the specified time ranges are met, the catalog attribute will be matched with the query during any of the specified time ranges. Add a time range with _add_box_**Add time range**.

     3. Define the **Synonym type** you want to trigger with this control. Select **Two-way**. See the section on [Synonyms](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#synonym) for more information on synonym types.

  6. Click **Submit**. This takes you to a detailed **Two-way synonym** configuration screen.

  7. Enter the synonyms in the field under **Two-way synonym actions**. This action links terms together bidirectionally to be treated the same in search results, so that a red sofa query results in red maroon sofa but maroon sofa queries are expanded to include all types of red sofas, such as crimson or pink.

  8. **Submit** again to send your control request to an Approver. You will be able to see the status of submitted requests in the Merchandising Console. Alternatively, you can **Save** a control **Draft** for later. If you change your mind, you can delete your control request.




For more information, refer to [Create two-way synonym controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#two-way-synonym) and their [rules](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#two-way-synonym).

###  One-way synonym 

  1. Click the URL provided by the administrator. Sign in.

This takes you to the **Controls** page in the **Merchandising console**.

  2. Click _add_box_**Create control**.

  3. Define the goals for your end users and timing required. All questions are required to be answered. Click **Next**.

  4. **Select a control**. Enter the name for your control, select the **Search** product, then choose the control type **Synonyms**.

  5. Configure your **One-way synonym** control:

     1. Under **Triggers** , define what catalog attribute triggers this control by giving criteria to a related search query, such as _contains_ or _not in range_. If no catalog attribute has been configured, this control will always apply.

     2. Define an **Applicable time range** by entering a **Date range**. If any of the specified time ranges are met, the catalog attribute will be matched with the query during any of the specified time ranges. Add a time range with _add_box_**Add time range**.

     3. Define the **Synonym type** you want to trigger with this control. Select **One-way**. See the section on [Synonyms](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#synonym) for more information on synonym types.

  6. Click **Submit**. This takes you to a detailed **One-way synonym** configuration screen.

  7. Enter your synonyms in the field under **One-way synonym actions**. This action links terms together unidirectionally to be treated the same in search results, so that a red sofa query includes maroon sofas, but a maroon sofa query does not return other types of red sofas, restricting the results to only maroon sofas.

  8. Click **Submit** again to send your control request to an Approver. You will be able to see the status of submitted requests in the Merchandising Console. Alternatively, you can **Save** a control **Draft** for later. If you change your mind, you can delete your control request.




For more information, refer to [Create one-way synonym controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#one-way-synonym) and their [rules](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#one-way-synonym).

#### Additional approver steps

These additional steps are available to Approvers in the Merchandising console for managing controls:

  1. **Define the goal** is optional for Approvers.

  2. **Approve** , **Deny** , or **Edit** any requests made by Creators for a **Boost/bury** control.

  3. The **Submit** step is optional. You can directly **Publish** a control.




You can also make a control inactive by removing all serving configs attached to it:

  1. Click the control configuration page indicated by the slider icon on the left side of the Merchandising console.

  2. Select the control you want to edit from the list.

  3. **Edit** the control.

  4. Navigate to the **Serving configs** section of the control **Edit** panel.

  5. Deselect the serving config by unchecking it.

  6. **Save**.




#### Recommendations boost or bury

  1. Click the URL provided by the administrator. Sign in.

This takes you to the **Controls** page in the **Merchandising console**.

  2. Click _add_box_**Create control**.
  3. Define the goals for your end users and timing required. All questions are required to be answered. Click **Next**.
  4. **Select a control**. Enter the name for your control, select the **Browse** product, then choose the control type **Boost/Bury**.
  5. Configure your **Boost/Bury** control:
     1. Under **Triggers** , enter the page categories are to trigger the control. If no catalog attributes are configured, then this control is always in effect.
     2. Define an **Applicable time range** by entering a **Date range**. If any of the specified time ranges are met, the catalog attribute will be matched with the query during any of the specified time ranges. Add a time range with _add_box_**Add time range**.
     3. Define the **Boost/Bury actions** you want to trigger with this control. These actions are defined by a **Catalog attribute** such as _colors,_ a **Criteria** such as _contains,_ and **Value** such as _red._
     4. Click _add_box_**Add attribute** to add more attributes.
  6. Use the slider to set your **Boost/bury value**. Negative numbers are bury, positive numbers are boost.
  7. Click **Submit** to submit your control request to an Approver. You will be able to see the status of submitted requests in the Merchandising Console. If you change your mind, you can delete your control request.



#### Approver steps

  1. Under **Serving configs** , assign your control to existing serving config.
  2. Approve the request for a **Boost/bury** control.



### Deactivate a control in production

![Merchandisers can initiate a control action by removing all serving configs attached to it.](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/merchandising-deactivate-control-prod-merchandiser.png)Merchandisers can initiate a control action by removing all serving configs attached to it.

For more information on creating controls in the Google Cloud console, refer to the [Create serving controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#control-types) page.

## Other controls (admin only)

Attribute controls | Autocomplete controls | Facet/tile controls  
---|---|---  
Type | Auto-learning |   
Indexable | Matching order | Ignore facet/tile values  
Dynamic faceting and tiling | Minimum length to trigger | Replace facet/tile values  
Searchable | Suggestion count | Set numerical intervals  
Retrievable | Deny list | Remove facets and tiles  
Exact match | Do-not-remove list | Force return facets (position)  
Filterable | Suggested terms list (manual) |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

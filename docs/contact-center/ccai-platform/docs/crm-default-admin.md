---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-default-admin/
title: CRM default administrator \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:05:54.356968+00:00
---

# CRM default administrator  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-default-admin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  CRM default administrator Stay organized with collections  Save and categorize content based on your preferences. 

The Contact Center AI Platform (CCAI Platform) CRM package sends multiple pieces of data during a support interaction, and all data interactions that take place in the CRM are assigned to a user. This feature provides the ability to define a CRM administrator to represent the default user for all CRM actions and events where a specific agent has not been identified or assigned. This will replace the default behavior where an agent is randomly selected for such events. If this feature is not used, CCAI Platform will randomly assign the ticket or case to any user.

Depending on the CRM, an administrator email, API or administrator token combination are required to enable the default user option.

After enabled, the times when tickets will be assigned to the administrator rather than a random user are:

  * **Ticket or case** and **contact** creation when a new chat is initiated before an agent is assigned to the chat

  * Voicemail tickets or cases before receiving a callback call

  * Call ticket or cases for abandoned calls (if enabled)




### Kustomer configuration

When using Kustomer as your agent platform, you can set a default user to route CRM actions to a specified user when no specific agent has been identified or assigned. By using the API key to set up the default user, you avoid the risk of the specified user being deleted.

To set up the default user using the API key, follow these steps:

  1. In the CCAI Platform portal, cick **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. For **Agent Platform** , select **Kustomer** .

  3. In the **API Key** field, enter your API key

  4. For **Default User** , select the **Use the API Key (admin user) for all record creations/updates that can't be attributed to a specific agent** checkbox.

  5. Click **Save**.




### MS Dynamics configuration

You must have an **Application User** set up in MS Dynamics prior to setting up a default user in the CCAI Platform portal. MS Dynamics doesn't support the option to leave tickets unassigned.

To set up the default user using the API key, follow these steps:

  1. In the CCAI Platform portal, cick **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. From the options for **Agent Platform** , select **MS Dynamics**.

  3. In the **Active Directory Application ID** field, enter your ID number.

  4. Create and enter a password in the **Set Active Directory Application Key Password**.

  5. For **Default User** , select the **Use the application user for all record creations/updates that can't be attributed to a specific agent** checkbox.

  6. Click **Save**.




To learn more about MS Dynamics and setting up a default user, see [Set up users, licenses, and security roles](https://learn.microsoft.com/en-us/dynamics365/field-service/users-licenses-permissions).

### Zendesk configuration

These steps require administrator permissions in both Zendesk and CCAI Platform.

  1. Follow the steps to generate a new API token in the Zendesk help center.

  2. In the CCAI Platform portal, cick **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  3. Enter the API token you just created in Zendesk in the **API Token** field.

  4. Enter an email with administrator permissions in Zendesk in the **Zendesk user email address** field.

  5. Mark the checkbox for **Default User.**

  6. Click **Save Changes**.




#### Zendesk troubleshooting

  * If "Zendesk user email address" and "API Token" combination is invalid, an error message is shown and values are reverted to previous setting values (other settings are saved). If values were blank before, it will revert to blank values.

  * If "Zendesk user email address" and "API Token" combination is invalid on save, the "Default User" checkbox will get unchecked.

  * If either "Zendesk user email address" or "API Token" is empty, the "Default User" checkbox will be disabled.




### Salesforce configuration

An account with administrator privileges is required for this feature.

  1. From the administrator portal, go to **Settings > Developer Settings**.

  2. Check to be sure all fields are completed in the CRM section.

  3. Be sure your Salesforce organization ID is **15** digits, not 18. Ex: instead of 00D0O000005Jj18UAC, remove the last three characters to be 00D0O000005Jj18.

  4. Navigate to the bottom of the page and enter your individual Salesforce login URL. This URL is your custom domain, not your lightning domain—for example, `https://{your-company-url}.my.salesforce.com`.

  5. Click **Save Login URL**.

  6. Click the **Link** button and enter your Salesforce administrator credentials in the display and click **Log In**.

  7. Once you are logged in, you will see the login listed as **Active** in green under **Connected administrator users**.

  8. Repeat Step 6 with another administrator account for redundancy in case the first account is disabled.

  9. Under **Default User** , select the **Use the admin user for all record creations/updates that can't be attributed to a specific agent** checkbox.

  10. To let agents retain ownership of CRM-related actions, select the **Always use the admin user for all record creation/updates** checkbox.

  11. Click **Save**.




### Salesforce troubleshooting

  * If "Salesforce administrator token" is not linked "Default User" feature is disabled, the checkbox is disabled and you can't check or clear the box.

  * If "Salesforce administrator token" is linked then "Default User" feature is enabled, you can then check or clear the box.

  * If "Default User" is checked and "Salesforce administrator token" gets unlinked then "Default User" will get unchecked and disabled.

  * If possible, it's best to use a Salesforce administrator account that is not tied to a specific user as individual user accounts are prone to being disabled without understanding the underlying connections.

  * If you run into errors such as "Unable to authenticate Salesforce user" or if you observe that a pop-up window briefly appears and then closes, preventing the linkage from being completed, then you need to disable `Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows` in your connected app under the `API (Enable OAuth Settings)` configuration.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

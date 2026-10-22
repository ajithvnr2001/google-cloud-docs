---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ms-dynamics-crm/
title: Microsoft Dynamics \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:31.175358+00:00
---

# Microsoft Dynamics  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ms-dynamics-crm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Microsoft Dynamics Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to integrate with Microsoft Dynamics. After you integrate, agents can take calls and chats directly from within a Microsoft Dynamics dashboard.

## Microsoft Dynamics integration checklist

The following checklist outlines the steps involved in setting up your Microsoft Dynamics integration.

**Note:** This page and the checklist provided assume you have already identified your environment, or set up a new environment for this portal space.

  1. Install the UJET solution into your environment. The latest version is 1.2.0.0.

  2. Configure the UJET solution IFrameUrl.

  3. Check domain based controls.

  4. Create New Azure app registration

     1. Add a platform configuration.

     2. Configure API permissions

     3. Create new certificates and secrets.

  5. Set up application users for this environment

  6. Set values in the administrator portal to connect to your Microsoft Dynamics instance.

  7. Proceed to optional steps.




## Install the connector

To install the Contact Center AI Platform connector, follow these steps:

  1. Download and unzip the UJET solution. You can find it here: [UJETConnector_1_2_0_0_managed-dynamics.zip](https://s3.us-west-2.amazonaws.com/externals.ujet.co/packages/UJETConnector_1_2_0_0_managed-dynamics.zip).

  2. In Microsoft Dynamics, go to **Service > Solutions**.

  3. Click **Import** and upload the UJET solution.

  4. Locate the **UJETConnector** entry and check it is installed correctly. You can check this from the Connector Settings Manager. For more information, see Configuring the Connector URL.




## Update or install the managed package

The managed package contains the connector. The connector installed to Microsoft Dynamics enables agents to take calls and chats directly in a Microsoft Dynamics dashboard.

### Update or install the Connector in solutions management

  1. In Microsoft Dynamics, use the top right cogwheel to navigate to **Advanced Settings**.

  2. In the **Settings** screen, click the expand_more **Expand more** next to **Settings** to open the drop-down, and from there select **Solutions**.




**Result** : In the **Solutions Management** list, you can see the Connector.

### Update or install the Contact Center AI Platform connector in Microsoft Dynamics

**Prerequisites**

  * You must be assigned as an Admin user with privileges to import connectors in Solutions Management.

  * You must have the managed Connector zip file. For example, `Connector_1_2_0_0_managed.zip.`

  * You must have the **Power Apps** user interface.

  * You must have a sufficient time window for agent adapter downtime. We recommend planning on approximately 10 minutes.




**Import the Connector in Microsoft Dynamics**

  1. In the **Power Apps** header, click the **Import** link. The **Add a Solution** pane appears.

  2. Click **Browse** to select the Connector to be imported.

  3. Click **Import**. The details of the package of the Connector to be imported should appear. If the details appear correctly, proceed to the next step. If not, check that you selected the correct file.

  4. Click **Next**.




Follow the steps to finish importing. There are no specific options required for the upgrading of the Connector.

**Note:** Installation takes 5-10 minutes. The Connector isn't stable during this time.

When the installation is complete, refresh the agent page to show the updated Connector.

**Result** : The connector is installed and ready for use.

## Configuring the Connector URL

After installing package v1_2_0_0, the new application is accessible to the integrator system builder.

  1. In the search bar, find the **UJET Connector Settings Manager** , and then click **Play**. This leads you to the application and to a view that gives you access to the UJET Settings table, which contains the configuration to the iframed adapter.

![The Microsoft Dynamics interface is shown, with the UJET Connector Settings Manager shown in the toolbar.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/configure-connector-url.png)

  2. For new installations, a new entry needs to be added to the settings table. Click **New** to add a new IFrameUrl setting.

![The UJET Connector Settings Manager is shown, with the name and value entered for IFrameURL.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/ujet-connector-settings.png)

  3. A new page opens to add an IFrameUrl. There are two fields present: **Name** and **Value**. Use the following sample values to help with configuration:

     1. Name: IFrameUrl

     2. Value: `https://<tenant_subdomain>.&lt;environment_domain>`

  4. Click **Save**. A new entry appears in your Settings table. The IFrameUrl configuration is now complete.


**Important:** It is very important to use IFrameUrl for the **Name** value. If another value is used, the adapter won't be configured correctly.

## Add domain based access control for the agent adapter

Domain-based access control maintains security while also allowing you to define and control which domains can display the agent adapter.

Domain-based access control lets you define and control which domains can display the Agent Adapter. This is a crucial implementation step. Be sure to add all necessary domains in the developer settings as per the guidelines provided. Failure to do so may result in the adapter breaking.

**Important:** Adding domains in the Developer Settings may cause a temporary disruption in the adapter's functionality. For this reason, Google recommends performing this task during a time when call volume is low or during a scheduled maintenance window.

If you have any questions or need assistance with implementation, contact Support.

### Add your domains in developer settings

**Note:** Once added it can take up to a minute for changes to the list of domains to take effect.

To add domains in developer settings, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to **Agent Adapter - Domain Based Access Control**

  3. Enter each domain on a new line. The format is `*.domain`—for example, `*.mycompany.com`.




#### Specifying a domain

**Note:** If no domains are specified, access is granted to all domains.

The format for specifying a domain for an instance can be any valid domain name, and it can include a wildcard (*****) to match an arbitrary number of subdomains. The wildcard must be placed at the beginning of the domain, and it matches any subdomains. Additionally, the user has the option to specify a protocol and a port using the syntax `<protocol>://<domain>:<port>`.

The port may be a wildcard, but the protocol cannot be a wildcard. If a protocol is specified, it matches only that protocol and all other protocols won't be able to display the adapter. For example, `https://some.example.domain.com` won't match `http://some.example.domain.com` or `mail://some.example.domain.com`.

#### CRM specific domains

Use the following domain naming conventions when entering your CRM domain.

**Important:** If you don't include all of these domains for a specific CRM, the agent adapter immediately breaks.

Salesforce: `*.visualforce.com` `*.force.com` `*.salesforce.com`

Zendesk: `*.zdusercontent.com` `*.zendesk.com`

Microsoft Dynamics: `*.crm.dynamics.com`

Kustomer: `*.kustomerapp.com`

**Reload Frame on the adapter**

After making administrator configuration changes, if the agent adapter is not visible for agents, they must right-click the agent adapter, and then click **Reload Frame**.

## Azure app registration (OAuth client)

### Create a new application registration in Azure

  1. Go to **Azure Active Directory > App registrations > New application registration**. The **Register an application** page appears.

  2. Fill in the required fields:

     * In the **Name** field, enter the URL of your environment without the `https://`. For example— `yourcompany.domain.co.`

     * For the **Supported account types** section, click **Accounts in the Organizational Directory Only**.

  3. Click **Register**. The application is now registered. 




### Authentication settings

#### Add a platform configuration

To add a platform configuration in Microsoft Dynamics, follow these steps:

  1. After creating the registered App, go to **Authentication** and enter your callback URL in the **Redirect URI** field—for example, `https://yourcompany.domain.co/v1/dynamics/oauth_callback`.

  2. Click the checkbox for **ID tokens**.




#### Create new certificates and secrets

To create new certificates and secrets in Microsoft Dynamics, follow these steps:

  1. Go to **Certificates & secrets** to create a new key in the **Add a client secret** panel:

     * In the **Description** field, enter a description such as API KEY.

     * In the **Expires** section, click the longest available time period allowed by your security team.

**Note** : This has to be regenerated after the expired time has been reached.

  2. Click **Add**.




#### Add API permissions

To add API permissions in Microsoft Dynamics, follow these steps:

  1. Go to **Manage > API permissions** and click **Add a permission**.

  2. Click **Dynamics CRM**.

  3. Click **Delegated permissions**.

  4. Check the box for **user_permission**.

  5. While still in **API permissions** , click again **Add a permission**.

  6. Click **Microsoft Graph**.

  7. Click **Application Permissions**.

  8. Add **Application.ReadWrite.All** , **Directory.Read.All** , and **User.Read.All**. permissions.

  9. Confirm all permissions under **Microsoft Graph** are selected, including **User.Read**.

  10. Click **Grant admin consent for [your organization name]** and **confirm** in the dialogue box that appears.

  11. Confirm the status is now Granted for **your organization name**.




![The options for API permissions are shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/api-permissions.png)

### Input your values in the Contact Center AI Platform portal

To input your values in the Contact Center AI Platform portal, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Scroll to **CRM > Agent Platform**.

  3. Click **Microsoft Dynamics** and enter values for the following:

     1. Application ID: application client ID (Microsoft Dynamics) found in the overview page of your app registration.

     2. Key Password: This must be copied after its creation as you won't be able to view it again fully on refresh. For more information, see Authentication settings.

     3. Active Directory Tenant: directory (tenant ID) found in the overview page of your app registration.

     4. Microsoft Dynamics Domain - Enter the URL of your environment. This can be found on the environment overview page.

**Note** : Make sure all of these fields are correct before saving and proceeding.

![The options for the Power Platform administration center are shown, with the Environments tab highlighted.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/ms-dynamics-domain.png)

  4. Click **Save**.




## Set up application users for your environment

To set up application users for your environment in Microsoft Dynamics, follow these steps:

  1. Choose your environment and click **Settings**.

![The settings tab for the Microsoft Dynamics environment is shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/crm-dynamics-settings.png)

  2. Click **Application Users**.

![The application user settings are shown from the Environment tab.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/crm-dynamics-application-users.png)

  3. Click **Setup app user**.

![The window for setting up a new app user in Microsoft Dynamics is shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/crm-dynamics-set-up-user.png)

     1. In the App field, choose an existing app and click **Add**.

     2. Click the **Business Unit** field, and then click a business unit.

     3. Add the following security roles:

     4. **Service Reader**

     5. **Service Writer**

  4. Click **Create**.




## Test custom field mapping

This section uses MyCustomField as a walkthrough example for adding and mapping a custom field.

**Note:** If you already have an existing TestCustomFields solution, skip to step 2.

To set up custom field mapping, follow these steps in Microsoft Dynamics:

  1. Create a new custom field in a solution component:

     1. Go to **Sales > Settings > Solutions**.

     2. At the top of the All Solutions page, click **New**.

     3. Enter **TestCustomFields** as the Display Name.

     4. Click **Save and Close**.

     5. Click your existing solution component

  2. Go to **Components > Entities > Add Existing**.

  3. Click the **Contact** solution component.

  4. Click **OK** to view the Contact solution component details. The solution component System Form dialog appears.

  5. Click the entity assets that you want to include in the solution.

     1. Include entity metadata

     2. Add All Assets




For this example, click **Include entity metadata**.

![An example of the entity assets with the entity metadata is shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/entity-assets.png)

  1. Click **Finish**.

  2. Go to **Components > Entities > Contact > Fields**.

  3. Click **New**.

  4. A new field name populates in the Name field. Copy the field name for later use:

![The custom field naming is shown, with the name field highlighted.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/custom-field-name.png)

  5. Click **Save and Close**.




### Edit form to display the custom field

The following example focuses on the contact solution component that was previously configured in Update or install the connector in solutions management.

To edit the form to display the custom field, follow these steps in Microsoft Dynamics:

  1. Open a contact and click **Form**.

  2. Open the **Field Explorer** and filter by **Custom Fields**.

![alt](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/field-explorer-custom-field.png)

  3. Double-click **MyCustomField**.

  4. Click **Save** , and then click **Publish** to add the new field to the form.

  5. Refresh the browser to check that the form displays in the contact screen.

  6. Confirm that **MyCustomField** is in the form.

  7. Enter the identified value in the **MyCustomField** field.

  8. Click **Save**.




### Set up custom field mapping in the Contact Center AI Platform portal

To set up custom field mapping in the Contact Center AI Platform portal, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to **Custom Field Mapping** and click the box.

  3. Under **CRM field to use in lookup** , click the custom field created earlier (**new_mycustomfield**).




### Populate the account and customer fields in a custom case form

The default action within Microsoft Dynamics is to fill in the customer information exclusively when a case is created. Updating this setting allows the contact field to be populated with the customer information from a case at the same time.

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to **CRM > Account Lookup**.

  3. Click **Contact** under **Object Type**.

  4. Select the **Use Custom Parameter Matching** checkbox.




Switching between object types clears the table unless the fields are saved. This lets the Contact field on the case object and the Customer field with the Account associated with the Contact (if there is one), to be updated simultaneously.

The CRM ticket updates when the checkbox **Use Custom Parameter Matching** is checked and **Parameters Configuration** is valid, otherwise it reverts to default logic to update the CRM. If all parameters are configured correctly, they all update. If any parameters are configured incorrectly, only the correctly configured parameters update.

## Test USER segment DAP

**Note:** A Direct Access Point must be created to complete the following steps. For more information, see [Direct Access Points](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dap).

To test a DAP, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Choose your preferred Social Channel

  3. In the **Settings** panel, go to **Access point** and click the **edit icon** beside the access point to update.

![The options to update the Direct Access Point are shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/DAP-update.png)

  4. In the **CRM Custom User Segment Field** , enter the name of the field in the CRM that contains the user segment information—for example, `new_mycustomfield`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

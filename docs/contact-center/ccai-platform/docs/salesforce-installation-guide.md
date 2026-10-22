---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-installation-guide/
title: Salesforce installation guide \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:36.978883+00:00
---

# Salesforce installation guide  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-installation-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Salesforce installation guide Stay organized with collections  Save and categorize content based on your preferences. 

Salesforce installation guide for Salesforce version 1.44.

Salesforce Professional, Enterprise, Performance, Unlimited, and Developer Editions all integrate with Contact Center AI Platform (CCAI Platform).

**Warning:** The Essentials version of Salesforce is not supported.**Note:** Domain-based access control provides the ability to define and control which domains can display the CCAI Platform agent adapter. This is a prerequisite implementation step. Be sure to add all necessary domains in the CCAI Platform Developer Settings. Failure to do so may result in failure of the agent adapter. Adding domains in the Developer Settings may cause a temporary disruption in the adapter's capability. For this reason, it is recommended to perform this task during a time when call volume is low or during a scheduled maintenance window. For more information, see [Domain-based access control](https://docs.cloud.google.com/contact-center/ccai-platform/docs/domain-access-control).

## Support for Salesforce Classic & Lightning

Installation link: [Salesforce Enterprise 1.44](https://login.salesforce.com/packaging/installPackage.apexp?p0=04tKk0000011Nu5)

### Installation steps

The Agent Adapter installed in Salesforce allows agents to take calls and chats directly in a Salesforce Organization (Org). Versions after 1.17 support both Classic Experience and Lightning Experience.

The installation consists of these steps:

  1. Locate Org ID and Org Name and add to the portal

  2. Install the app in Salesforce

  3. Enter connected app consumer key and secret into the portal

  4. Create a connected app

  5. Place connected app consumer key and secret in the portal

  6. Manage the configuration in Salesforce

  7. Manage the call center




##### Data required to perform installation

Field Name | Where to Find | Where to Enter  
---|---|---  
Organization Id | Salesforce | Developer Settings in Portal  
Organization Name | Salesforce | Developer Settings in Portal  
Connected App Consumer Key | Salesforce | Developer Settings in Portal  
Connected App Consumer Secret | Salesforce | Developer Settings in Portal  
Tenant name | Admin Portal <companyName>.<domain> | Custom Settings in SFDC  
Customer Key | Developer Settings | Custom Settings in SFDC  
Secret | Developer Settings | Custom Settings in SFDC  
Connected App | Salesforce Connected App | Custom Settings in SFDC  
  
### Locate Org ID and Org Name and Add to the Portal

In this section, you will set up an initial connection between the CCAI Platform portal and Salesforce by finding the required org information and adding it into the CCAI Platform portal.

#### Prerequisites

  * Access to the **Company Information** page within Salesforce.

  * User with Admin role assigned in the Portal to access **Developer settings**




#### Installation steps

  1. In **Salesforce** , go to **Setup > Settings > Company Settings > Company Information**.

**Tip:** Use the **Quick Find** search box in Salesforce Settings to quickly navigate to various pages throughout this configuration.
  2. Locate the Salesforce.com **Organization Name** and **Organization ID** in **Company Information**.

  3. Copy both values.

  4. In another browser tab, open the CCAI Platform portal.

  5. Go to **Settings > Developer Settings > CRM > Agent Platform**.

  6. Select **Salesforce**.

  7. Locate the **Salesforce Organization ID** and **Salesforce Organization Name** fields.

  8. Enter the `Salesforce Organization ID` into the **Salesforce Organization ID** field and the `Salesforce Organization Name` into the **Salesforce Organization Name** field.

  9. Click **Save**.




### Install the App in Salesforce

In this step we will install the app in Salesforce.

#### Prerequisite

Salesforce user must have privileges to install packages into an Organization.

  1. [Retrieve the Package Installation link](https://login.salesforce.com/packaging/installPackage.apexp?p0=04tKk0000011Nu5).

  2. Sign in to Salesforce if prompted to do so.

  3. Select **Install for All Users**.

![Install for all users](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/163065366599f9.png)

  4. Select **Install** (or **Upgrade** if your Org used a previous version). This may take a few minutes.

  5. Once the installation is complete, click **Done**.

To verify the package installation in Salesforce, go to **Platform Tools > Apps > Packaging > Installed Packages**.




### Create a custom permission set and apply to all agents

In this section, you will create a custom permission set (with the minimum requirements needed for integration), update it with case and contact permissions, and apply it to all agents who use the CCAI Platform portal.

#### Prerequisites

  * User must be a Salesforce Admin to configure this section.

  * A list of agents who will be using the adapter in Salesforce.




#### Steps

  1. In **Salesforce** , go to **Administration > Users > Permission Sets**.

  2. Locate the **CC_Agent** Permission Set and click the **Clone** link.

  3. Rename the cloned Permission Set and click **Save**. For example **Company_Agent_Clone**.

  4. From the **Permission Sets** screen, click the name of the new cloned Permission Set.

  5. Click **Object Settings** , in the **Apps** section.

  6. Configure the **Object Settings** for **Accounts** , **Cases** , **Contacts** , and **Leads** using this table:

Object | Read | Create | Edit | Delete | View All | Modify All  
---|---|---|---|---|---|---  
Cases | X | X | X |  | X |   
Contacts | X | X | X |  | X |   
Accounts | X | X | X |  | X |   
Leads | X | X | X |  | X |   
  7. To configure these settings, click the **Object Name**. Click **Edit** (at the top).

  8. Use the checkboxes in the **Object Permissions** section to enable each of the required permissions (Read, Create, Edit, and View All).

![object permissions checkbox display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1630653665e872.png)

  9. Click **Save**.

  10. Repeat these steps for each of the four objects (Accounts, Cases, Contacts, and Leads).

  11. Configure the **tasks** object's **Type** field permission.

**Note:** Skip this step if using the CCAI Platform Session object. For more information see [Salesforce: CCAI Platform Session Object Technical Details](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-integration-guide#UUID-5f742c36-cc5a-4b9e-2863-7e68bfc72e03).Object | Field | Read Access | Edit Access  
---|---|---|---  
Tasks | Type | X | X  
  
![Task type configuration](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/16306536663c5d.png)

  12. Once all configurations are done, click **Manage Assignments**.

  13. Click the **Add Assignments** button.

**Tip:** You can add the permission set to a group instead of adding users manually. For more information see the Salesforce documentation on [Permission Sets](https://help.salesforce.com/articleView?id=service_presence_give_access_to_statuses_through_permission_sets.htm&type=5).
  14. Use the checkboxes to select the users, then click **Assign**.

![Checkbox display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1630653666910f.png)




### Create a connected app

Create a connected app in Salesforce, a required step for app version 1.15 and later.

A Connected App is an OAuth application that allows the CCAI Platform portal to communicate with Salesforce.

#### Prerequisites

  * Copy your **Portal** URL. It should follow this structure:

https://<tenant&>.<domain>.




#### Steps

  1. In Salesforce, go to **Setup > Apps > External Client Apps > Settings**.

  2. Click the **New Connected App** button.

  3. Update the **Basic Information** fields with the contents:

**Note:** Make a note of your Connected App Name as you will need it in a later step.
  4. Under **API (Enable OAuth Settings)** , select the **Enable OAuth Settings** checkbox and update the settings using the table:

**Field Name** | **Field Value**  
---|---  
Enable OAuth Settings | Selected (TRUE)  
Callback URL | https://<tenant>.<domain>/v1/salesforce/oauth_callback  
Selected OAuth Scopes | Access the identity URL service (id, profile, email, address, phone) Manage user data using APIs (API) Perform requests at any time (refresh_token, offline_access)  
Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows | Unselected (False)  
Required Secret for web flow | Selected (TRUE)  
Require Secret for Refresh Token flow. | Selected (TRUE)  
  5. Under the **Canvas App Settings** , update the settings with the following:

**Field Name** | **Field Value**  
---|---  
Canvas | Selected (TRUE)  
Canvas App URL | https://<tenant>.<domain>/v1/salesforce/start  
Access Method | Signed Request (POST)  
Locations | Console Lightning Component Open CTI Visualforce Page  
  6. Navigate to the bottom of the page and click **Save**.

  7. Click **Continue** to dismiss the confirmation message and wait for the Connected App to be created.

**Note:** It can take up to 10 minutes for the Connected App to be created. If your app is not displayed in Step 10, wait a few minutes and try again.
  8. Go to **Setup > Apps > Connected Apps > Manage Connected Apps**.

  9. Click the name of the app from the **Connected Apps** screen.

  10. Click **Manage**.

  11. Click the **Edit Policies** button.

  12. Under OAuth policies, select the **Admin approved users are pre-authorized** option from the **Permitted Users** drop-down:

![OAUTH policies display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1630653666e394.png)

  13. Click **Save** at the bottom of the page to return to the **Manage** screen for the Connected App.

  14. Navigate to the **Profiles** section and click **Manage Profiles**.

  15. On the **Application Assignment Profile** screen, select the profile options your company will use, such as the System Administrator or another profile an agent may use.

In this example, we are selecting **Standard User** and **System Administrator** :

![Standard user and system administrator checked](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/16306536696d28.png)

  16. Click **Save** to return to the manage connected app view.

A Connected App has been created.To verify the connected app was created, check if the app is listed in **Settings > Apps > App Manager**.




### Enter Connected App Consumer Key and Secret into Admin Portal

Enter `client_id key` and `Secret` into the Salesforce **Admin Portal**.

#### Prerequisites

  * Finish the steps in the Create a connected app previous section.

  * User must have access to the email address associated with Salesforce user account to receive an identity verification email.

  * Must be a user with the administrator role in the **CCAI Platform portal**.




#### Steps

  1. Go to **Setup > Create > Apps > Connected Apps** and find your Connected App.

  2. Click the arrow to the far right of the row.

  3. Click **View**.

  4. Click **Manage consumer details**.

![Manager consumer details display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1630653669b610.png)

  5. Verify your identity by entering the verification code sent to your email address.

  6. Copy the **Consumer key** and **Consumer secret** values displayed.

![Consumer details display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1630653669e855.png)

  7. In the **CCAI Platform portal** , go to **Settings > Developer Settings** and locate the **Connected App Consumer Key** and **Connected App Secret** fields.

  8. Paste the **Consumer Secret** into the **Connected APP Consumer Secret** field.

  9. Paste the **Consumer Key** from Salesforce into the **Connected APP Consumer Key** field.

  10. Click **Save**.

The Connected App information has been added to the CCAI Platform portal.




### Manage the Configuration in Salesforce

_Configure App version 1.22 and later._

#### Prerequisites

  * App version for Salesforce 1.22 or later is installed for the Salesforce Org.

  * Get your company's Company Key and Company Secret Code in the Admin Portal by going to **Settings > Developer Settings**.

  * Connected App is created (see the Create a connected app section above).




#### Steps

  1. In Salesforce, go to **Setup > Apps > Packaging > Installed Packages**.

  2. Locate the **CC_Agent_App** and click **Configure**.

  3. On the new tab that opens, click **Add New Configuration**.

  4. Complete the fields using the following values:

![Complete the field display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/163065366a3839.png)

**Field Name** | **Field Value** | **Location for Field**  
---|---|---  
Setup Owner | Organization or Profile | If you want to set organizational level settings, select _**Organization**_. If you want to add profile level settings, select _**Profile**_. If you select _**Profile**_ you can choose a profile for the settings to be applied to.  
Organization |  | Your organization name displays here and is read-only.  
Profile |  | Your profile list displays here and you can choose a Profile if you selected Profile for Setup Owner.  
CompanyKey | Company Key | **CCAI Platform portal > Settings > Developer Settings**  
CompanySecret | Company Secret | **CCAI Platform portal > Settings > Developer Settings**  
Tenant | Tenant Name | In CCAI Platform portal: https://<tenant>.<domain> Important: only enter the <tenant> portion of the Portal URL in this field. Note: **This field has a 100 char limit.**  
ConnectedApp | Connected App API name | Match the name in Create a connected app (such as CCaaS_Platform_Connected_App)  
  5. If you select **Profile** from the **Setup Owner** drop-down, you can select a profile that will be applied to this new configuration. If **Organization** was selected from Setup Owner, the **Profile** field is disabled.

  6. Click **Save Configuration** and you are returned to the list screen

  7. Once the configuration is completed, close the browser window.




### Manage the Call Center

Configure a Call Center in Salesforce to give agents access to the adapter.

#### Prerequisites

  * Package has been installed (see section 2\. Install the App in Salesforce above)



#### Steps

  1. In Salesforce go to **Setup > Feature Settings > Service > Call Center > Call Centers**.

  2. Locate and click the Call Center titled **Softphone_v2**.

  3. Click **Manage Call Center Users**.

  4. Click **Add More Users**.

  5. Use the filter fields to search for specific users and then click **Find**. To view all users, click **Find**.

  6. Use the checkboxes in the search results to select the users that will use the Portal.

  7. Click **Add to Call Center**.

To verify the result, go to Call Center and see that the users are listed.




### After Installation

Set up the console for Salesforce Classic or Salesforce Lightning:

Console setup for Salesforce Classic

Console setup for Salesforce Lighting

## Console setup for Salesforce Classic

Configure the Console App to use the adapter in the Salesforce Classic Experience.

### Prerequisites

  * Complete Salesforce installation

  * Organization is configured to use Salesforce Classic experience.




### Steps

  1. In Salesforce, go to **Setup > Build > Create > Apps**.

  2. On the **Apps** screen, locate the **Sample Console** and click **Edit**.

  3. To edit the Sample Console, go to the **Choose Console Components** field and select the **UJET_Chat** component from the Available Items list.

  4. Click **Add** to move the component to the Selected Items list.

  5. Go to the **Assign to Profiles** section and select the checkboxes for the profiles with the permission set that you configured in the previous section.

![Assign to profiles display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/163065366beccf.png)

  6. Click **Save**.

  7. Verify the adapter is shown in the Console as expected:

Use the app selector in the **Sales** menu at the top right corner of the screen to select **Sample Console** :

![App selector sample app](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/163065366c4c52.png)




### Result

Salesforce is set up in Salesforce Classic Console.

## Console setup for Salesforce Lightning

Configure the Console App to use the adapter in the Salesforce Lightning Experience.

### Prerequisites

  * Organization uses the Lightning Experience.

  * Must have System Administrator profile or be a user who can manage Apps.

  * [Domain deployment for user](https://help.salesforce.com/articleView?id=domain_name_testing_and_rollout.htm&type=5) with Salesforce is completed.




### Steps

  1. In Salesforce go to **Setup > Apps > App Manager**.

  2. Locate the **Sales and/or Service Console** app that has **Lightning** in the App Type column.

  3. Click the arrow drop-down at the far right and select **Edit**.

  4. Click **Utility Items** from the App Settings menu on the left.

![Utility items display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/163065366cbaa5.png)

  5. Click **Add Utility Item** and select the **Open CTI Softphone** option.

  6. Configure the **Label** field.

![Configure the Label field](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/163065367202b8.png)

  7. Click **Add Utility Item** again and select **Chat Component** in the Custom- Managed section.

  8. Update the **Label** as needed.

  9. Configure the **Icon** as needed.

  10. Click **Save**.

  11. Repeat Steps 2-10 if installing additional Lightning console apps.




The utility bar has been configured with the components. To confirm that Salesforce is set up with the Lightning Experience, check the utility bar in the console.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

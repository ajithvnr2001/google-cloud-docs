---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started/
title: Get started with Contact Center AI Platform (CCAI Platform) \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:00.061335+00:00
---

# Get started with Contact Center AI Platform (CCAI Platform)  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Get started with Contact Center AI Platform (CCAI Platform) Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create an instance of CCAI Platform.

## Before you begin

To use CCAI Platform, do the following:

  1. **Use a full WebRTC browser**. You need the most up-to-date version of a full WebRTC browser. CCAI Platform supports Chrome, Safari, and Firefox, but we recommend the most recent version of Chrome.

  2. **Allow CCAI Platform notifications, permissions and cookies**. For more information, see [Granting Notification and Microphone Permissions.](https://docs.cloud.google.com/contact-center/ccai-platform/docs/troubleshoot#notification-microphone).

  3. **Confirm proper network configuration**. Firewalls can potentially block incoming support inquiries and other critical capabilities.

  4. **Get quota**. For more information, see Instance size and quota.




## Instance size and quota

The following table shows CCAI Platform instance sizes and the maximum number of concurrent call or chat sessions.

Instance size | Concurrent sessions  
---|---  
Small | 250.**Note** : The minimum size for a small instance is 25 agents.  
Medium | 1600  
Large | 3800  
X-Large | 14,000  
2X-Large | 38,000  
3X-Large | 100,000  
  
## Non-production instances

Google provides non-production instances that you can use for trials, development, or demonstrations. These instances have a maximum of 250 concurrent sessions. You can use these instances at no cost, except for telephony. Telephony costs are billed monthly to the billing account associated with the Contact Center AI Platform project.

Google doesn't permit non-production instances to be used for production traffic. Any production usage on a non-production instance results in the instance either being stopped or converted to a production instance, with usage billed to your account.

The following non-production instance types are available:

  * **Trial Small** : an instance for performing a trial.

  * **Sandbox Small** : an instance for Google partners to perform customer demonstrations and testing.

  * **Dev Small** : an instance for development or user-acceptance testing.

  * **Time-Limited Trial Small** : an instance for performing a trial. A Time-Limited Trial Small instance expires after 90 days. When the instance expires, all configuration settings are lost. If you want to transition your time-limited trial instance to a production instance, contact Google support.




## Billing model

Instances are billed monthly. Billing depending on which of the following charging models is assigned to your instance:

  * **Concurrent agents** : the maximum number of concurrent users with the agent role that are signed in during the month period

  * **Named agents** : the maximum number of users in the instance that have the agent role during the month period

  * **Minutes used** : the number of minutes that users with the agent role are signed in during the month period


**Note:** Telephony charges are charged according to consumption.

## Set up your Google Cloud project for CCAI Platform

To set up your Google Cloud project for CCAI Platform, follow these steps:

  1. In the Google Cloud console, go to the project selector dashboard and select the project where you will create your CCAI Platform instance.

[Project selector dashboard](https://console.cloud.google.com/projectselector2/home/dashboard)

You can either choose an existing project or create a new one. For more information about creating a project, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

  2. [Make sure that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  3. Ask your Google account team to grant quota to your project for CCAI Platform. You can't create an instance without quota. If you don't have a Google account team, you can connect with an approved CCAI Platform Google partner. To find a partner visit the [Google Cloud partner page](https://cloud.google.com/find-a-partner/).

  4. To set access control with Identity and Access Management (IAM), do the following:

     1. In the main Google Cloud console navigation menu, go to **IAM & Admin > IAM**.

[IAM and Admin](https://console.cloud.google.com/iam-admin/iam)

     2. Click edit **Edit principal** next to the identity that you want to assign roles to.

     3. In the **Role** field, find and then select the **Contact Center AI Platform Admin** role.

     4. Click **Add another role**.

     5. In the **Select a role** field, filter and then select the **Service Usage Admin** role.

     6. Click **Save**.




## Create a CCAI Platform instance

To create a CCAI Platform instance, follow these steps:

  1. In the Google Cloud console, go to the project selector dashboard and select the project that contains your instance.

[Project selector dashboard](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. In the navigation menu, click **CCAI Platform**.

[CCAI Platform instances](https://console.cloud.google.com/contact-center-ai-platform)

**Note:** If you haven't enabled the CCAI Platform API for this project, the **Contact Center AI Platform API** page appears. Click **Enable**.

The **CCAI Platform instances** page appears.

  3. Click **Create**. The **Set basic information** pane appears.

If the **Create** button is disabled and you see a message that says there is insufficient quota, you need to have quota granted to proceed. For more information, see Set up your Google Cloud project for CCAI Platform.

If you have confirmed that quota has been granted and the **Create** button is still disabled, ensure that the billing ID of the Google Cloud project matches the billing ID that the quota was assigned to.

  4. To set your basic information, do the following:

     1. In the **Instance name** field, enter a name for your instance.

     2. In the **Region** field, select a region. The region can't be changed after you create your instance. Some Contact Center AI Platform capabilities are available only in certain regions. For more information, see [Google Cloud regions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/localities#regions).

     3. In the **Domain prefix** field enter your domain prefix. The domain prefix is added to the URL for your instance, which can help you identify your instance by looking at the URL. The domain prefix can't be changed after you create your instance.

     4. In the **Instance size** field, enter the size of your instance. The instance sizes that are available depend on the quota you have been granted. If you want to change the size of your instance after creating it, contact Google Cloud support. Changing the size of an instance causes a period of downtime lasting between 30 and 60 minutes.

     5. For **Admin information** , enter the name and email address of the administrator for this instance. When the instance is created, an email is sent to this email address with instructions for creating a password for the administrator account. The name and email address values cannot be changed after you create the instance. For this reason, if you plan to keep this instance, Google recommends entering name and email address values that will be useful to your organization over time.

     6. Click **Continue**. The **Configure deployments** pane appears.

  5. In the **Deployment schedule** field, select one of the following:

     * **Rapid** : Get updates as early as possible.

     * **Regular** : Get updates at least two days after updates are available with rapid deployment.

     * **Critical** : Get updates outside of your peak business hours. Google updates instances set for the critical deployment schedule within one week after all regular deployment schedule instances are updated. We recommend the critical deployment schedule for instances that are in production environments.

If you select **Critical** , you must define your peak hours by creating at least one schedule. To create a schedule, do the following:

       1. Click the **Days** field, select the days to include in this schedule, and then click **OK**.

       2. In the **Start time** field, enter the start time, including AM or PM. Times are in UTC.

       3. In the **End time** field, enter the end time, including AM or PM. Times are in UTC.

A summary of your schedule appears in local time.

       4. Optional: Click keyboard_arrow_up **Arrow up** or keyboard_arrow_down **Arrow down** to move schedules up or down.

       5. Optional: Click delete **Delete** to delete a schedule.

       6. If you need additional schedules, click **Add schedule** and repeat these steps.

For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

  6. Click **Continue**. The **Configure authentication** pane appears.

  7. For **Login method** , select one of the following:

     * **Email/password**. Agents use email addresses and passwords specific to this instance.

     * **SAML**. Agents use single sign-on (SSO) to sign into this instance. Configure this section according to the instructions in [Single sign-on (SSO)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sso).

  8. Click **Continue**. The **Configure private access (optional)** pane appears.

**Important:** If you configure private access ([Preview](https://docs.cloud.google.com/products#product-launch-stages)), you restrict public access to your CCAI Platform instance from the internet (end-users can still contact your contact center as they normally would). To enable access to your instance for agents, managers, and CCAI Platform administrators, you need to set up Private Service Connect. For more information, see [Private Service Connect](https://docs.cloud.google.com/contact-center/ccai-platform/docs/set-up-psc).
  9. Optional: To configure private ingress ([Preview](https://docs.cloud.google.com/products#product-launch-stages)), do the following:

     1. For **Ingress** , click **Add setting**. In the **Component type** field, **Agent** is selected.

     2. Click **Done**.

     3. In the **Allowed project IDs** field, enter one of more project IDs for the projects that are allowed to create a Private Service Connect connection to this instance. For more information, see [Private Service Connect](https://docs.cloud.google.com/contact-center/ccai-platform/docs/set-up-psc).

  10. Optional: To configure private egress ([Preview](https://docs.cloud.google.com/products#product-launch-stages)), do the following:

     1. For **Egress** , click **Add setting**. In the **Component type** field, select the component type for the data that you're configuring private egress for. For more information, see [Components](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ccaip-custom-constraints#components).

     2. In the **Service attachment** field, enter the service attachment for a service that you've published, and then click **Done**. For more information, see [Set up private egress](https://docs.cloud.google.com/contact-center/ccai-platform/docs/private-egress).

     3. Optional: Click **Add setting** and repeat the previous two steps for every additional private egress setting that you need.

  11. Click **Continue**. The **Configure extensions** pane appears.

  12. Optional: To turn on advanced reporting, select the **Advanced reporting** checkbox. The checkbox is inactive if your instance is in a [region](https://docs.cloud.google.com/contact-center/ccai-platform/docs/localities#regions) where advanced reporting is not supported. If you need advanced reporting, you must create an instance in a region that supports it.

  13. Optional: To turn on agent desktop, select the **Agent desktop** checkbox.

  14. Click **Create**. When your new instance is created, it appears on the **CCAI Platform instances** page. This can take up to two hours. If you configured your instance for private ingress, a service attachment is created that you'll need to [set up private ingress](https://docs.cloud.google.com/contact-center/ccai-platform/docs/private-ingress). To get the service attachment, do the following:

     1. On the **CCAIP Platform instances** page, click the name of the instance that you just created. The **CCAI Platform instance detail** page appears.

     2. For **Private access** , save the **Service attachments** value.




## Check the version number of your instance

You can check the version number of your instance and compare it with the version numbers of the updates and patches that Google announces in the [CCAI Platform release notes](https://cloud.google.com/contact-center/ccai-platform/docs/release-notes). In this way you can know which capabilities are available in your instance.

To check the version number of your instance, follow these steps:

  1. In the Google Cloud console, go to the project selector dashboard and select the project that contains your instance.

[Project selector dashboard](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. In the navigation menu, click **CCAI Platform**.

[CCAI Platform instances](https://console.cloud.google.com/contact-center-ai-platform)

**Note:** If you haven't enabled the CCAI Platform API for this project, the **Contact Center AI Platform API** page appears. Click **Enable**.

The **CCAI Platform instances** page appears.

  3. View the **Version** column for the instance for which you want the version.




## Initial setup steps and resources for your CCAI Platform environment

This section shows you how to set up your CCAI Platform environment.

### Enter your support center details

  * Adding support center email and name: [Support Center Details - General Settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/migrate-support-center#enter-basic-information).

  * Set up for timezones, Hours of operation, holiday closures: [Hours of operation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hours-of-operation).




### Customize messages and set up other languages

  * [Configure IVR messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-ivr-messages)

    * Customize the messages played to callers and displayed to consumers.
  * If you are using languages other than English, see [Enable Multiple Languages for IVR, Mobile, and Web](https://docs.cloud.google.com/contact-center/ccai-platform/docs/enable-multiple-languages) to add languages.




### Configure your operation management settings

  * Go through items such as the following:

    * [Timeout on Contact Center AI Platform (CCAI Platform)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-timeout).

    * [Custom and default agent avatars](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-avatar).

    * [Localized Languages in the Agent Adapter and User Location Entry](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-location).

  * Create any custom Agent Statuses necessary for your operation.

  * Establish your Target Metrics like SLA and Target pick up time.

  * Decide how you want your calls routed.




### Add users and teams

  * For an understanding of [User Roles and Permissions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-roles-permissions).

  * Adding Users, assigning Agents and Managers to Teams.

  * [Importing Users](https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-management#bulk_user_management_upload_new_or_updated_users)

  * [Bulk User Management](https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-management)




### Create queues and assign agents to queues

  * [IVR: Add and edit queue menus](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-and-edit-ivr-queue-menus).

  * [Setting up and assigning agents to channels and queues: IVR, mobile, web](https://docs.cloud.google.com/contact-center/ccai-platform/docs/setup-agents-channels) so they can receive calls/chats.




### Configure settings for handling calls

  * Call recording, call timers and displays, and default call routing settings: **Settings** > **Calls** > **Call Details**.

  * Setting outbound numbers.

  * Caller announcements and various deflection settings.




### Configure settings for handling chats

  * Enable chat, create proactive web triggers, establish chat channel settings like chat threshold for agents and timeout settings at **Settings** > **Chat**

  * Create [chat shortcuts](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-shortcuts) for agents to use.




### Get info from the developer settings as needed

The **Settings** > **Developer Settings** area is strictly for developers - you need to supply information from this page to your developers if you are setting up any SDKs or making any custom CRM configurations.

## About the CCAI Platform SDKs

CCAI Platform SDKs let you provide voice and chat support to your customers on your website or inside your app on iOS and Android.

### Web SDK

With the CCAI Platform Web SDK, your customers can get in touch with your support team directly on your website.

  * **Instant web calls:** Provide visitors with an estimated wait time and automatically initiate an outbound call to a site visitor when their place in the support queue is reached

  * **Scheduled calls:** Allow site visitors to schedule a time to talk with your support team

  * **Queue deflection:** Automatically route end users to a message or page on your site

  * **Chat support:** Provide live chat support directly from your website

  * **Proactive triggers** : Display a contact bubble for web calls and chats automatically based on visitor behavior. Proactive triggers can be configured based on:

    * Specific page URL.

    * Time spent on page.

    * Number of visits to a particular page.

  * **Mobile Web Support** : Customers on mobile devices can also access your Web SDK

  * **Direct Access Points** : Decide which queue, language, or channel an end-user should reach when on a particular page or with predefined account details




### iOS SDK

With the CCAI Platform iOS SDK, you can create seamless voice and chat support experiences for users of your iPhone and iPad apps.

  * **VoIP calls:** Allow users to make voice calls using data instead of minutes.

  * **PSTN Fallback calls** : When the end-user doesn't have a strong enough data connection for a VoIP call, CCAI Platform will fallback to a PSTN call while still sending the important custom data packet to your CRM record.

  * **Scheduled calls:** Allow users to schedule a time to talk with your support team; AI-powered algorithms predict and provide 15-minute time slots based on agent availability, ensuring your users never have to wait on hold.

  * **SmartActions:** Instantly verify users with Touch ID and Face ID, and request photos, videos, screenshots and text input.

  * **SMS SmartActions:** Send an SMS to activate SmartActions inside your app.

  * **Call deflections:** Configure call deflections based on volume and business hours, and, if needed, to:

    * Allow the user to schedule a call for another time.

    * Provide an email address.

    * Forward the call to another number directly.

    * Forward the call to voicemail.

  * Provide unique visual queue configuration settings

    * Direct queues to a particular website, like a help center article for a common question.

    * Direct queues to a visual message

  * **Direct Access Points** : Decide which queue, language, or channel an end-user should reach when the SDK is invoked in various parts of your app based on predefined contact details




### Android SDK

With the CCAI Platform Android SDK, you can create seamless voice and chat support experiences for users of your Android apps.

  * **VoIP calls:** Allow users to make voice calls using data instead of minutes.

  * **PSTN Fallback calls** : When the end-user doesn't have a strong enough data connection for a VoIP call, CCAI Platform will fallback to a PSTN call while still sending the important custom data packet to your CRM record.

  * **Scheduled calls:** Allow users to schedule a time to talk with your support team; AI-powered algorithms predict and provide 15-minute time slots based on agent availability, ensuring your users never have to wait on hold.

  * **SmartActions:** Instantly verify users with their fingerprint, face or passcode, and request photos, videos, screenshots and text input.

  * **SMS SmartActions:** Send an SMS to activate SmartActions inside your app.

  * **Call deflections:** Configure call deflections based on volume and business hours and if needed:

    * Allow the user to schedule a call for another time.

    * Provide an email address.

    * Forward the call to another number directly.

    * Forward the call to voicemail.

  * Provide unique visual queue configuration settings:

    * Direct queues to a particular website, like a help center article for a common question.

    * Direct queues to a visual message.

  * Detects calls to your main support number from the device's dialer and converts the call to a Mobile call

  * **Direct Access Points** : Decide which queue, language, or channel an end-user should reach when the SDK is invoked in various parts of your app based on predefined contact details




## Working from home

Contact Center AI Platform (CCAI Platform) is the perfect tool to empower agents to work from home. By following a few guidelines outlined in the following sections, agents will be up and running in no time from the safety of their own homes.

Ideally, agents will be using the same laptops that they used in the office which retain control over allow-listing or deny listing and applications the device uses such as AdBlock, mic permissions, etc. If agents don't have access to a work laptop, it's possible for them to use their personal computers if they follow the best practices outlined in the following sections.

### Network requirements

The following sections outline the specific network requirements to support an optional agent and customer experience.

#### Bandwidth

  * **We recommend that you have the bandwidth for 2 Mbps upload and 2 Mbps download per agent**. At a minimum, you should have at least 1 Mbps of network bandwidth per agent.

  * If agents are sharing an internet connection with roommates or family members, agents need to work to prevent others from streaming or downloading large files during working hours.




#### Firewalls

  * Make sure home firewalls don't block access to the Contact Center AI Platform (CCAI Platform) application.

  * If agents have customized security or firewalls setup with IP allow-listing (as opposed to deny-listing), configuration of the router and possibly your firewall is needed to allow Contact Center AI Platform (CCAI Platform) IP addresses.

  * See [IP address allow listing](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-adapter-ip-allow-list) for a list of URLs and IP addresses.




### Workstation requirements

The following section outlines the requirements for the agent workstation.

#### Programs & physical requirements

  * Agents should use a hard-wired connection as Wi-Fi connectivity cannot guarantee the support of proper voice quality.

  * Running any network or CPU intensive applications on the same computer, like streaming music or large uploads/downloads, will compete with bandwidth for audio from Contact Center AI Platform (CCAI Platform) and is highly discouraged.

  * Agent computers should have a Core i5 hardware processor or higher. The recommended RAM is at least 8 GBs.

  * Make sure the most recent version of Contact Center AI Platform (CCAI Platform) supported browser has been installed and browser notifications have been enabled for Contact Center AI Platform (CCAI Platform). We support Chrome, Safari, and Firefox, but recommend the most recent version of Chrome.

  * Disable any 3rd party browser extensions that may block 3rd party integrations. Examples are: AdBlock, Ghostery, AdBlock Plus, etc.




### Supported browsers

Contact Center AI Platform (CCAI Platform) is supported by the latest version of Google Chrome. Refer to the [Google Chrome update page](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop) for more information.

### Headsets

Contact Center AI Platform (CCAI Platform) customers have been most successful with the following standards for headsets. **Headsets should have a wired connection to the computer.** Wireless headsets suffer from signal congestion, delay, and can run out of battery power, possibly during a call.

#### Recommended headset features

  * Binaural - Audio in both ears cuts down on background noise

  * Noise-canceling microphone

  * Noise-canceling headset

  * USB connection




#### Brands of headsets our customers use

  * Jabra

  * Logitech

  * Plantronics

  * Sennheiser




## What's next

  * [Configure a sample contact center](https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-contact-center)

  * [Private Service Connect](https://docs.cloud.google.com/contact-center/ccai-platform/docs/set-up-psc)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

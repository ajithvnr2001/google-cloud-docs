---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup/
title: Agent Assist for Salesforce setup guide \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:03.166979+00:00
---

# Agent Assist for Salesforce setup guide  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Agent Assist for Salesforce setup guide Stay organized with collections  Save and categorize content based on your preferences. 

Integrate Agent Assist UI modules with Salesforce to provide real-time suggestions for your human agents during customer service chat and voice conversations. The Salesforce UI module configuration creates trusted URLs so that Agent Assist can communicate with Salesforce. The configuration also creates an external client application to authenticate and authorize requests from Salesforce to the UI connector. This configuration is required for both Salesforce chat and voice integrations. Follow these steps to integrate Agent Assist UI modules with Salesforce.

## Step 1: Enable resource sharing

Follow these steps in Salesforce to enable cross-origin resource sharing for authorization. 

  1. Navigate to the menu bar and click **Setup** > **CORS**.
  2. Enable CORS for OAuth endpoints.
  3. Click **Save**.



## Step 2: Add domain to remote site settings

Follow these steps in Salesforce to add your domain to the remote site settings:

  1. On the menu bar, click **Setup** > **Remote Site Settings** > **New Remote Site**.
  2. Enter your Salesforce domain. 
  3. Click **Save**.



## Step 3: Create trusted URLs

Follow these steps in Salesforce to create a trusted URL:

  1. Enter a search for **Agent Assist Settings** in the Salesforce app launcher.
  2. Click the link to go to the configuration dashboard.
  3. Navigate to the **Get Started** tab, and enter your trusted URLs. 
  4. Click **Save**. 



## Step 4: Create an external client application

Follow these steps in Salesforce to create an external client application:

  1. Click **Create External Client App**.
  2. After the process is completed, click **Open** to navigate to the external client app's page.
  3. Click **Settings** > **Edit**.
  4. Expand the **OAuth Settings** section.
  5. Select **Enable OAuth**.
  6. Navigate to **App Settings** , and enter the following callback URL: `https://login.salesforce.com/services/oauth2/callback`
  7. Add **Access the identity URL service** to **OAuth scopes**.
  8. Navigate to **Flow Enablement** , and select **Enable Client Credentials Flow**.
  9. Click **Save** > **Policies**.
  10. Expand the **OAuth Policies** section, and select **Enable Client Credentials Flow**. 
  11. Enter your username for **Run As**.
  12. Click **Save** > **Settings** , and navigate to **OAuth Settings**.
  13. Click **Consumer Key and Consumer Secret**. You should receive an email with a code to unlock these values.
  14. Copy the key and secret for later use.



## Step 5: Configure Agent Assist settings in Salesforce

With Agent Assist settings in Salesforce, you can set up open authorization (OAuth) credentials, create a skillset, and manage user permissions. Follow these steps to access **Agent Assist Settings** in Salesforce:

  1. Click apps **App Launcher**.
  2. In the search field, enter **Agent Assist Settings** , and click the result.



From the Agent Assist **Settings** page, you can track and update each step of your configuration. The instructions that follow all begin from this page in Salesforce.

### OAuth credentials

UI modules require OAuth credentials to authenticate Salesforce to communicate with the Agent Assist UI connector.

Follow these steps to create your OAuth credentials: 

  1. Click **Setup** > **Quick find** and enter **external client app**.
  2. Click **External Client App Manager** > **Agent Assist Settings OAuth App** > **Settings** > **OAuth Settings** > **Consumer Key and Secret** , and copy those details.
  3. Navigate to **GCP OAuth Settings** and click **OAuth Credentials** > **New**.
  4. Enter your OAuth credential's name, key, and secret.
  5. Click **Save**.



You should see your new credential in the list. Click arrow_drop_down_circle **Expand** to edit or delete your credential.

### Skillsets

Skillsets serve as the configuration hub for your Agent Assist conversation profile, UI connector endpoint, and UI module settings. When a customer service conversation begins, the UI module on the record page utilizes a skillset to provide the correct tools for your agent. A skillset also connects agents to a specific conversation profile. By creating diverse skills, you can tailor conversations to agents that match specific roles, such as sales, general technical support, or specialized product tiers. 

#### Create a skillset

Follow these steps to create a skillset:

  1. Click **Skillsets** > **New**.
  2. Enter a **Skillset Name** and a **UI connector endpoint**.
  3. Select your features and click arrow_right **Next**.
  4. Enter the **Conversation Profile path** and **Conversation ID prefix**.
  5. Select an **OAuth Credential** and enter the **Container Height**. The default container height is 710 px.
  6. Click **Save**.



You should see your new skillset with a custom permission in the list.

#### Default skillsets

When you set a skillset as default, it's used in all instances of the UI module for every agent, unless you assign the skillset to a permission set. You can only have one default skillset at a time.

Follow these steps to set your skillset as the default:

  1. Click **Skillsets**.
  2. Navigate to your skillset's name in the list.
  3. Click **Set as Default**.



This activates your skill for all agents. If you've assigned your skillset's custom permission to a permission set, custom permissions take precedence over default skillsets. This means the default skillset is a fallback for agents who are not assigned to a permission set. 

#### Skillset-based routing

To complement skill-based routing, Agent Assist for Salesforce offers a permission-driven approach to ensure the correct skillset is ready when your agent accepts a conversation. When you create a skillset, Salesforce automatically generates a corresponding custom permission. You can assign the custom permission to a permission set. You can assign a permission set to an agent. When an agent visits a record page containing the UI module, Salesforce uses the skillset that corresponds to that agent's permission set.

The skillset table displays a skillset's custom permission. For example, suppose you have sales and support agent conversation profiles in Agent Assist. Follow these steps to ensure the UI module accesses the relevant conversation skills:

  1. In Agent Assist for Salesforce, create two skillsets, one for each conversation profile.
  2. Assign the skillsets to permission sets associated with two corresponding agents.



When the UI module loads during a conversation, it checks which skillset is associated with the agent and loads the corresponding skill.

### Priority

When an agent is assigned multiple skillsets, you can choose the priority for each one. Priority dictates which skillsets take precedence and if an agent gets multiple custom permissions associated with different skillsets. A lower priority number gives a skillset higher precedence. For example, a skillset with a priority of **1** takes precedence over a skillset with a priority of **2**. Follow these steps to set your skillset's priority:

  1. Click **Skillsets**.
  2. Navigate to a skillset in the list and click > **Settings**.
  3. Enter a number for the **Priority**.
  4. Click **Save**.



Repeat these steps for each skillset assigned to the agent. 

### User management

With user management, you can assign read and write permissions for Agent Assist custom Salesforce objects to administrators and read permissions to agents. Follow these steps to assign a permission to someone with limited permissions:

  1. Click **User Management**.
  2. Choose a tab: **Admins** or **Agents**.
  3. Select the person's name and click arrow_right **Right**.
  4. Click **Save**.



## Record pages

In Salesforce, a record page is the specific layout you see when you open an individual record, such as a specific contact, account, or voice call. Customer service conversations use a voice call record page or a messaging session record page. For example, when an agent accepts a chat message or a voice call, Salesforce automatically opens a record page and provides details about the conversation.

### Step 1: Create a record page

Choose one of the following options to create a record page:

  * New voice call record page
  * New messaging session record page
  * Update an existing record page 




### Voice

Follow the Salesforce instructions to [create a new voice call record page](https://help.salesforce.com/s/articleView?id=service.voice_setup_create_vc_page.htm&type=5).

### Chat

Follow the Salesforce instructions to [create a new messaging session record page](https://help.salesforce.com/s/articleView?id=service.livemessage_create_console_app.htm&type=5).

### Update

Follow the Salesforce instructions to [update your existing record page](https://help.salesforce.com/s/articleView?id=platform.lightning_app_builder_customize_lex_pages.htm&type=5).

### Step 2: Add an Agent Assist UI module

Add the Google Agent Assist UI module component to a record page to display a console for call transcripts, agent actions, and suggestions. Set your record page's template to **Header and Two Equal Regions**. This allows the Agent Assist UI module to adequately display transcripts and suggestions.

Follow these steps to add an Agent Assist UI module to your record page:

  1. In the Salesforce Lightning app builder, navigate to **Components (Managed)**.
  2. Move Google Agent Assist UI Module onto the page.
  3. Click **Save**.



#### Change record page templates

Default templates use three columns. The Agent Assist UI module requires additional width to display on a standard monitor. Follow these steps to update your record page's template:

  1. Follow the Salesforce instructions to [open the template](https://help.salesforce.com/s/articleView?id=platform.lightning_app_builder_customize_lex_pages.htm&type=5) in the Lightning App Builder.
  2. Click **Change** > **Header and Two Equal Regions** > **Save**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

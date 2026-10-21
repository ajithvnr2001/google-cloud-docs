---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-sentinel/
title: Collect Microsoft Sentinel logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:21:04.560281+00:00
---

# Collect Microsoft Sentinel logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-sentinel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Sentinel logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure Microsoft Sentinel to send incidents and alerts to Google Security Operations using Logic Apps and webhooks.

Microsoft Sentinel is a cloud-native security information and event management (SIEM) and security orchestration, automation, and response (SOAR) solution. It delivers intelligent security analytics and threat intelligence across the enterprise.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Microsoft Azure** portal with permissions to: 
    * Create Logic Apps
    * Configure Microsoft Sentinel automation rules
    * Manage resource group permissions
    * Create and manage service principals
  * Access to Google Cloud console (for API key creation)



## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Microsoft Sentinel Incidents`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Microsoft Sentinel** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Leave empty (each incident or alert is a single event).
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



### Generate and save secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. Copy and save the secret key securely.

**Note:** The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.

**Caution:** To avoid **HTTP 429 (Too Many Requests)** errors and ingestion delays, don't reuse the same shared key or storage account across multiple feeds.

### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is:
         
         https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import
         

Where `{region}` is the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`), and `{parent}` is the resource path in the format `projects/<PROJECT_ID>/locations/<LOCATION>/instances/<INSTANCE_ID>/logTypes/<LOG_TYPE>`.

  4. Save this URL for the next steps.

  5. Click **Done**.




## Create Google Cloud API key

Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud console.

### Create the API key

  1. Go to the [Google Cloud console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Google SecOps instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps Webhook API Key`).
  2. Under **API restrictions** : 
     * Select **Restrict key**.
     * In the **Select APIs** list, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Google SecOps API, reducing security risk if the key is compromised.



## Configure Logic App for Microsoft Sentinel incidents

This section configures a Logic App to send Microsoft Sentinel incidents to Google SecOps.

### Create Logic App

  1. Sign in to **Azure Portal**.
  2. Click **Create a resource**.
  3. Search for **Logic App**.
  4. Click **Create** to start the creation process.
  5. Specify values for the following input parameters: 
     * **Subscription** : Select the subscription.
     * **Resource group** : Select the resource group.
     * **Name** : Enter a name for the Logic App (for example, `Sentinel-Incidents-to-SecOps`).
     * **Region** : Select the region.
     * **Log Analytics workspace** : Select the Log Analytics workspace.
  6. Click **Review + create**.
  7. Click **Create**.
  8. After the Logic App is created, click **Go to resource**.



### Configure Logic App designer

  1. Click **Development Tools > Logic App Designer**.
  2. Click **Add a trigger**.
  3. Search for **Microsoft Sentinel**.
  4. Select **Microsoft Sentinel incident** as the trigger.
  5. If you haven't already created a connection to Microsoft Sentinel, you'll need to do so now.
  6. Click **Create new** and follow the prompts to authenticate: 
     * Select **Sign in with managed identity** (recommended) or **Sign in** to use your credentials.
  7. Click **Insert a new step**.
  8. Click **Add an action**.
  9. Search for and select **HTTP** as the action.
  10. Specify values for the following input parameters: 
     * **URI** : Paste the feed endpoint URL from the Google SecOps feed.
     * **Method** : Select **POST**.
     * **Headers** : Add the following headers: 
       * **Header name** : `X-goog-api-key`
       * **Value** : Paste the API key created earlier.
       * **Header name** : `X-Webhook-Access-Key`
       * **Value** : Paste the secret key from the feed creation.
  11. Click in the **Body** field.
  12. Click the **Expression** tab in the dynamic content panel.
  13. Enter `@{triggerBody()}` in the expression field and click **OK**.

**Note:** The `@{triggerBody()}` expression sends the complete incident JSON to Google SecOps. This parameter is required - without it, the webhook receives empty requests and no data is ingested.
  14. Click **Save** to save the Logic App.




## Grant Microsoft Sentinel permissions to run Logic App

Two separate permission assignments are required for automation rules to successfully trigger the Logic App.

### Permission 1: Grant Logic App managed identity access to Sentinel workspace

The Logic App's managed identity needs permission to read incidents from the Microsoft Sentinel workspace.

#### Enable managed identity for Logic App

  1. In the **Azure Portal** , go to your Logic App resource (`Sentinel-Incidents-to-SecOps`).
  2. In the left navigation, select **Identity** under **Settings**.
  3. On the **System assigned** tab, set **Status** to **On**.
  4. Click **Save**.
  5. Click **Yes** to confirm.
  6. After enabling, note the **Object (principal) ID** displayed.



#### Grant Microsoft Sentinel Responder role to Logic App

  1. In the **Azure Portal** , navigate to your **Microsoft Sentinel workspace**.
  2. In the left navigation, select **Access control (IAM)** under **Settings**.
  3. Click **\+ Add > Add role assignment**.
  4. In the **Role** tab, search for and select **Microsoft Sentinel Responder** : 
     * **Alternative** : If the playbook only reads incidents, use **Microsoft Sentinel Reader** role.
  5. Click **Next**.
  6. In the **Members** tab, configure the following: 
     1. **Assign access to** : Select **Managed identity**.
     2. Click **\+ Select members**.
     3. In the **Managed identity** list, select **Logic App**.
     4. Select your Logic App (`Sentinel-Incidents-to-SecOps`) from the list.
  7. Click **Select**.
  8. Click **Review + assign**.
  9. Click **Review + assign** again to confirm.



### Permission 2: Grant Microsoft Sentinel automation permissions on resource group

Microsoft Sentinel requires **Microsoft Sentinel Automation Contributor** role on the resource group containing the Logic App. Without this permission, automation rules cannot trigger playbooks.

#### Grant automation permissions via Sentinel UI

  1. In the **Azure Portal** , navigate to your **Microsoft Sentinel workspace**.
  2. Go to **Settings > Automation**.
  3. Click **Manage playbook permissions** at the top of the page.
  4. In the **Manage permissions** pane, configure the following: 
     1. Select the **resource group** containing your Logic App (`Sentinel-Incidents-to-SecOps`).
  5. Click **Apply**.

**Note:** This grants the **Microsoft Sentinel service principal** (Azure Security Insights) the **Microsoft Sentinel Automation Contributor** role on the selected resource group.



#### Verify automation permissions (Optional)

  1. In the **Azure Portal** , navigate to the **resource group** containing your Logic App.
  2. In the left navigation, select **Access control (IAM)**.
  3. Click **Role assignments**.
  4. Search for **Azure Security Insights**.
  5. Verify that **Azure Security Insights** has the **Microsoft Sentinel Automation Contributor** role.

**Note:** If you do not see **Manage playbook permissions** in the Sentinel UI, you can grant permissions manually:
  6. Go to the **resource group** containing your Logic App.

  7. Select **Access control (IAM) > Add role assignment**.

  8. Select **Microsoft Sentinel Automation Contributor** role.

  9. In **Members** , select **User, group, or service principal**.

  10. Click **\+ Select members** and search for **Azure Security Insights**.

  11. Select **Azure Security Insights** and click **Select**.

  12. Click **Review + assign** twice to confirm.




## Configure Logic App for Microsoft Sentinel alerts

This section configures a separate Logic App to send Microsoft Sentinel alerts to Google SecOps.

**Note:** Alert triggers are in **Preview** and can only be triggered manually or by scheduled analytics rules. They cannot be called by automation rules.

### Create Logic App for alerts

  1. Go to **Azure Portal Home Page**.
  2. Click **Create a resource**.
  3. Search for **Logic App**.
  4. Click **Create** to start the creation process.
  5. Specify values for the following input parameters: 
     * **Subscription** : Select the subscription.
     * **Resource group** : Select the resource group.
     * **Name** : Enter a name for the Logic App (for example, `Sentinel-Alerts-to-SecOps`).
     * **Region** : Select the region.
     * **Log Analytics workspace** : Select the Log Analytics workspace.
  6. Click **Review + create**.
  7. Click **Create**.
  8. After the Logic App is created, click **Go to resource**.



### Configure Logic App designer for alerts

  1. Click **Development Tools > Logic App Designer**.
  2. Click **Add a trigger**.
  3. Search for **Microsoft Sentinel**.
  4. Select **Microsoft Sentinel alert** as the trigger.
  5. If you haven't already created a connection to Microsoft Sentinel, you'll need to do so now.
  6. Click **Create new** and follow the prompts to authenticate: 
     * Select **Sign in with managed identity** (recommended) or **Sign in** to use your credentials.
  7. Click **Insert a new step**.
  8. Click **Add an action**.
  9. Search for and select **HTTP** as the action.
  10. Specify values for the following input parameters: 
     * **URI** : Paste the feed endpoint URL from the Google SecOps feed.
     * **Method** : Select **POST**.
     * **Headers** : Add the following headers: 
       * **Header name** : `X-goog-api-key`
       * **Value** : Paste the API key created earlier.
       * **Header name** : `X-Webhook-Access-Key`
       * **Value** : Paste the secret key from the feed creation.
  11. Click in the **Body** field.
  12. Click the **Expression** tab in the dynamic content panel.
  13. Enter `@{triggerBody()}` in the expression field and click **OK**.

**Note:** The `@{triggerBody()}` expression sends the complete alert JSON to Google SecOps. This parameter is required - without it, the webhook receives empty requests and no data is ingested.
  14. Click **Save** to save the Logic App.




## Grant Microsoft Sentinel permissions to run alerts Logic App

Two separate permission assignments are required for the alerts Logic App, identical to the incidents Logic App configuration.

### Permission 1: Grant alerts Logic App managed identity access to Sentinel workspace

The alerts Logic App's managed identity needs permission to read alerts from the Microsoft Sentinel workspace.

#### Enable managed identity for alerts Logic App

  1. In the **Azure Portal** , go to your alerts Logic App resource (`Sentinel-Alerts-to-SecOps`).
  2. In the left navigation, select **Identity** under **Settings**.
  3. On the **System assigned** tab, set **Status** to **On**.
  4. Click **Save**.
  5. Click **Yes** to confirm.
  6. After enabling, note the **Object (principal) ID** displayed.



#### Grant Microsoft Sentinel Responder role to alerts Logic App

  1. In the **Azure Portal** , navigate to your **Microsoft Sentinel workspace**.
  2. In the left navigation, select **Access control (IAM)** under **Settings**.
  3. Click **\+ Add > Add role assignment**.
  4. In the **Role** tab, search for and select **Microsoft Sentinel Responder** : 
     * **Alternative** : If the playbook only reads alerts, use **Microsoft Sentinel Reader** role.
  5. Click **Next**.
  6. In the **Members** tab, configure the following: 
     1. **Assign access to** : Select **Managed identity**.
     2. Click **\+ Select members**.
     3. In the **Managed identity** list, select **Logic App**.
     4. Select your alerts Logic App (`Sentinel-Alerts-to-SecOps`) from the list.
  7. Click **Select**.
  8. Click **Review + assign**.
  9. Click **Review + assign** again to confirm.



### Permission 2: Grant Microsoft Sentinel automation permissions on resource group for alerts

Microsoft Sentinel requires **Microsoft Sentinel Automation Contributor** role on the resource group containing the alerts Logic App.

#### Grant automation permissions via Sentinel UI

  1. In the **Azure Portal** , navigate to your **Microsoft Sentinel workspace**.
  2. Go to **Settings > Automation**.
  3. Click **Manage playbook permissions** at the top of the page.
  4. In the **Manage permissions** pane, configure the following: 
     1. Select the **resource group** containing your alerts Logic App (`Sentinel-Alerts-to-SecOps`). 
        * If this is the same resource group as the incidents Logic App, it may already be selected.
  5. Click **Apply**.

**Note:** If the resource group was already configured for the incidents Logic App, this step grants the same permissions for the alerts Logic App.



#### Verify automation permissions for alerts Logic App (Optional)

  1. In the **Azure Portal** , navigate to the **resource group** containing your alerts Logic App.
  2. In the left navigation, select **Access control (IAM)**.
  3. Click **Role assignments**.
  4. Search for **Azure Security Insights**.
  5. Verify that **Azure Security Insights** has the **Microsoft Sentinel Automation Contributor** role.



## Configure automation rules for Microsoft Sentinel

Automation rules trigger Logic Apps when incidents are created or updated in Microsoft Sentinel.

### Create automation rule for incident creation

  1. Go to your **Microsoft Sentinel Workspace**.
  2. Click **Configuration > Automation**.
  3. Click **Create**.
  4. Select **Automation rule**.
  5. Specify values for the following input parameters: 
     * **Name** : Enter a name for the automation rule (for example, `Send New Incidents to SecOps`).
     * **Trigger** : Select **When incident is created**.
     * **Actions** : Select **Run playbook** from the list.
     * Select the Logic App created for incidents (`Sentinel-Incidents-to-SecOps`).
  6. Click **Apply**.



### Create automation rule for incident updates

  1. Go to your **Microsoft Sentinel Workspace**.
  2. Click **Configuration > Automation**.
  3. Click **Create**.
  4. Select **Automation rule**.
  5. Specify values for the following input parameters: 
     * **Name** : Enter a name for the automation rule (for example, `Send Updated Incidents to SecOps`).
     * **Trigger** : Select **When incident is updated**.
     * **Condition** : Click **Add > Condition (And) > Status > Changed**.
  6. In the **Actions** section, configure the following: 
     1. Select **Run playbook** from the list.
     2. Select the Logic App created for incidents (`Sentinel-Incidents-to-SecOps`).
  7. Click **Apply**.



### Create automation rule for alerts

**Note:** Alert automation rules use the **When alert is created** trigger, which is separate from incident triggers.

  1. Go to your **Microsoft Sentinel Workspace**.
  2. Click **Configuration > Automation**.
  3. Click **Create**.
  4. Select **Automation rule**.
  5. Specify values for the following input parameters: 
     * **Name** : Enter a name for the automation rule (for example, `Send Alerts to SecOps`).
     * **Trigger** : Select **When alert is created**.
     * **Actions** : Select **Run playbook** from the list.
     * Select the Logic App created for alerts (`Sentinel-Alerts-to-SecOps`).
  6. Click **Apply**.



## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-sentinel-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 

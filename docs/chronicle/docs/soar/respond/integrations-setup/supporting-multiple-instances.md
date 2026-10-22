---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances/
title: Support multiple instances \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:23.176630+00:00
---

# Support multiple instances  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Support multiple instances

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

You can configure multiple instances of the same integration within the same environment. This feature gives you greater flexibility and control when you [create and run playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen). For example, you can build a playbook for a customer with two sites, each using separate Active Directories, and then select the appropriate integration instance for each playbook step. 

This functionality is configured in **Response > Integrations Setup** and is supported by the **Choose Instance** field in the playbook step, and the multi-select environment option. 

## View integration options

On the **Integrations** page, two predefined options are listed:

  * **Shared Instances**
  * **Default Environment**



**Shared Instances** acts as a library of configured integrations that you can use across all environments.

The **Shared Instances** section includes predefined Google SecOps integrations that are available by default.

Any environment that you create in **Settings > Organizations > Environments** will appear in the environment list.

You can filter the display of environments or hide empty ones. Enterprise customers typically use the default environment.

## Add and configure an integration instance

  1. Add an environment. On the **Integrations Setup** page, first select or add the environment where you want to configure the integration.
  2. Create a new instance. Click add **Create a new instance**.
  3. Select the integration from the list and enter the required parameters for that specific instance. Note: You must configure an instance before using it in a playbook.
     * To configure a second instance of the same integration in the same environment, repeat the process.
     * To edit or reconfigure an instance later, click settings **Configure Instance** next to the integration.



## Select an environment

The multi-select environment feature is available when creating a new playbook. Go to the **Playbooks** page to see it. Do one of the following: 

  * Select **All Environments** to run the playbook on all environments defined in the system.
  * Select one or more environments for the playbook to run on.



The selection of multiple or all environments restricts the instance type configurable for playbook steps. A more detailed explanation follows.

## Use the instance in a playbook

When adding a step in a playbook that uses an integration, the options in the **Configure Instance** field depend on:

  * Which instances you've created
  * Which environments you've selected for the playbook



### Single environment

If you select a single environment, the **Configure Instance** field lets you choose either:

  * An instance you've configured for that specific action in the selected environment.
  * A shared instance integration, if one is available.



### Multiple environments or all environments

If you select multiple environments—or **All Environments** —the first option in **Configure Instance** is **Dynamic Mode**.

### Dynamic Mode

Dynamic Mode means that when the playbook is attached to a case, Google SecOps attempts to access the integration instance configured for the environment associated with the case.

### Fallback Instance

The **Fallback Instance** field is optional. If **Dynamic Mode** is selected and no instance is configured for a specific environment, you can choose a fallback instance from shared instances. This option is available for playbooks that run across all environments.

If no suitable instance exists and no fallback is configured, the following happens:

  * The action fails—unless it's set to skip if failed.
  * Using **skip if failed** is especially helpful for Managed Security Service Provider (MSSPs) who may want to skip steps when customers don't have a license for a specific tool.



A fallback instance is not used if more than one instance is configured for the case environment. In that situation, the playbook will pause and prompt the analyst to manually choose the appropriate instance.

## Use Case #1: Two Instances in a default Environment

This scenario involves an enterprise network divided into two sites: one in the US and one in the UK. Each site requires a distinct Active Directory configuration. To support this, configure two instances of Active Directory integration within the same environment. This lets the playbook to select the appropriate instance dynamically at runtime. 

### Install an integration

  1. Go to **Content Hub > Response Integrations**. 
  2. Search for the required integration. For this example, use **Active Directory**. 
  3. Click **Install** to add the integration.



### Configure an Instance

  1. Go to **Response > Integrations Setup**. 
  2. In the **Environments** list, select the environment where you want to create an instance. For this example, use **Default Environment**. 
  3. Click  add  **Create a new instance**. 
  4. In the **Add Instance** dialog, select the required integration from the list and click **Save**. In this example, select **Active Directory**. 
  5. Go to the required integration, and click  settings  **Configure Instance**.
  6. Enter the relevant configuration information. For this example, configure the instance for users in the US site.
  7. Click **Save** when finished.
  8. Optional: Click **Test** to verify the configuration works. 
  9. Add another instance of the **Active Directory**. In this example, configure it for users in the UK site. Click **Save** when the configuration is complete. 
  10. You can make changes later if needed. Once configured, the instances are available for use in playbooks. 



### Use the instance in playbooks

  1. Go to **Playbooks** and click  add **Add New Playbook or Block** to create a new playbook. 
  2. Select the relevant folder. For this example, choose **Default Environment**. 
  3. In **Actions** , under **ActiveDirectory** , choose **Enrich entities**.
  4. Drag the action into a step and double-click it to open the configuration panel. 
  5. In the **Choose Instance** field, select the appropriate instance—either the US site or UK site—depending on the playbook's target. 



## Use Case #2: Dynamic Mode in multi environments

In this scenario, as an MSSP, you support multiple customers, each defined in a separate environment. At runtime, the playbook should dynamically determine which environment to use based on where the case originated. 

### Define environments

  1. Go to **Settings > Organization > Environments**. 
  2. Click  add **Add Environment** and define the required environment with the parameters for the environment. 
  3. Create several new environments, one for each customer. 



### Install an integration

  1. Go to **Content Hub > Response Integrations**. 
  2. Search for the required integration. For this example, select and install VirusTotal. 



### Configure instances

  1. Go to **Response > Integrations Setup**, select each customer, and click **Configure**. 
  2. Set up the VirusTotal integration instance according to your requirements. 



### Set up a playbook

When adding the VirusTotal Ping action, select **Dynamic Mode**. This ensures that Google SecOps determines the environment at runtime based on where the case originated and applies the appropriate integration instance.

  1. Go to the **Playbooks** page. 
  2. Create a new playbook, making sure to select the environments you previously created and configured. 
  3. When adding the VirusTotal Ping action, select **Dynamic Mode**. This makes sure that Google SecOps checks which environment the case comes from at runtime and applies that specific instance to it. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

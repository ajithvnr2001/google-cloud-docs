---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/using-the-ide/
title: Use the IDE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:53.930531+00:00
---

# Use the IDE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/using-the-ide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use the IDE

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains the Integrated Development Environment (IDE) production mode. The IDE is a framework for viewing, editing, and testing code. You can view the code of commercial integrations and create custom integrations from scratch or by duplicating commercial integrations code.

IDE is where you manage, import and export custom integrations.

## Open the IDE

To open the IDE, follow these steps:

  * To open the IDE, in the main menu, go to **Response > IDE**. The **IDE** page opens.



On the **IDE** page, you can access the following options:

Option | Description  
---|---  
Integrations  
Types | Choose between **Integrations** or **Types** (connectors, actions, jobs, managers).  
Export  
Import | Export individual or multiple items from an integration. Dependent items are included when exporting individual items, but not when exporting a full package.  
The exported file is a ZIP archive containing a JSON file. When importing, you can add individual items to an existing integration or import a full package. For the legacy (V1 - dataplane disabled) export/import format, the package must include an integrations.def file and the folders: **ActionsDefinitions** , **ActionsScripts** , **Dependencies** , and **Managers**. For the new (V2 - dataplane enabled) export/import format, the package folder must include a metadata.json file and can include the folders: **actions** , **connectors** , **jobs** , and **dependencies**.  
Note that exporting an integration from an environment with the dataplane enabled and importing it into an environment where the dataplane is not enabled is not supported. The other way around (exporting from an environment where the dataplane is not enabled to an environment where the dataplane is enabled) is supported.  
toggle_on | Click the **Hide Inactive/Show All** toggle to **Show** or **Hide** deactivated items (actions, connectors).  
add|  **Add** a new custom integration, connector, action, job, or manager.  
  
## Add a connector

To add a connector, follow these steps:

  1. Click add**Create New Item** and select **Connector**.
  2. Enter a name and the required integration.
  3. Click **Create**.
  4. Add integration details.
  5. Add the required parameters.
  6. Click the **Connector** toggle to enable the connector.
  7. Click **Save** when done, or press `Ctrl + S`.



The following options are available in the **Details** tab:

Option | Description  
---|---  
delete **Delete** | Available only for items in custom integrations.  
play_arrow **Play** | Runs the script's test method. Results appear in the **Testing** tab, and debug output appears in the **Debug Output** section.  
file_json  **Manage JSON sample** | In the JSON sample import/export dialog, ensure **Include JSON Result** is enabled. You can then import or export JSON result samples for actions.  
  
**Details**|  Enter user-supplied input and other parameters, such as integration name.  
history **Version Control** | Version Control \- Select an action/job/connector and click to see the following options: **Save as New Version** : Save the object as a new version with optional comments. **View Version History** : View and restore previous versions. Only available if at least one version has been saved. Click Restore to revert to any of the previous versions anytime. This is only available if you have clicked **Save as New Version** on an action/job/connector/manager previously.  
file_copy Duplicate item | Duplicate an item (job, action, connector, manager). After saving, the duplicate appears in the list without a  lock  **Lock** icon.  
  
## Create a custom integration

  1. Click add**Create New Item** and select **Integration**.
  2. Enter a name and click **Create**.
  3. Select the created integration from the list and provide the following information: 
     * **Description** : appears in Content Hub and is visible to all Google Security Operations users.
     * **SVG icon** : upload an SVG icon that appears with the integration.
     * **Image** : upload a Content Hub image for Google SecOps users.
     * **Libraries** : add Python libraries using pip.
     * **Script dependencies** : Upload `.WHL`, `.PY`, `.TAR`, or `.GZ` files. These scripts add more functionality to your integration.
     * **Parameter** : Add configurable fields with defined types, default values, and required status.
  4. Click **Save** when done.

**Note:** You can add jobs, actions, managers, and connectors to your custom integration and use them to push or collect information according to your needs. Simply create a new action and then choose the custom integration. A best practice is to create a **Ping** action to test the integration in the Content Hub. 

## Create a job

To create a job, follow these steps:

  1. Click add**Create New Item** and select **Job**.
  2. Enter a name and the required integration.
  3. Click **Create**.
  4. Optional: Add parameters for user or script input.
  5. Click **Save** or press `Ctrl + S`.
  6. Click  arrow_right  **Play Item** to run the script.
  7. Go to **Response > Jobs Scheduler**.
  8. Click  add **Create New Job** and select the job that you just created.
  9. In **Response >Jobs Scheduler**, choose the required time to run the job (script) that you created.



## Create a new action to be used in a playbook

To create a new action for a playbook, follow these steps:

  1. Click add**Create New Item** and select **Action**.
  2. Enter a name and the required integration > click **Create**.
  3. Edit the code as needed.
  4. Enable **Include JSON Result** if the action should return a JSON result in a playbook.
  5. Optional: Add parameters to display as input fields.
  6. Enable the action and click **Save**.
  7. In **Polling Configuration** , you can set a timeout and a default return value if the action times out. You can also set a default value to return if the action doesn't complete within the defined timeout period.



The action is now available for use in **Playbook > Actions**.

## Create a custom manager

To create a custom manager, follow these steps:

  1. Click add**Create New Item** and select **Manager**. Enter a name and the required integration.
  2. Click **Create**.
  3. Edit the code as needed.
  4. Click **Save**.



## IDE custom code security

To ensure a secure code execution environment, all custom Python code within the IDE runs in a sandboxed environment. This environment is isolated from the main server and operates with a low-privilege user. Access to the underlying operating system is strictly limited to an allow-list of non-administrative commands and directories required for typical integration and automation tasks. This sandboxing approach allows for robust security while providing the flexibility to execute a wide range of Python code. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

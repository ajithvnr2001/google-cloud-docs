---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/create-ide-actions-gemini/
title: Create actions with Gemini in the IDE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:41:55.258634+00:00
---

# Create actions with Gemini in the IDE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/create-ide-actions-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create actions with Gemini in the IDE

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

**Note:** This feature may not be available to all customers in all regions. Private preview features are not manageable in the Public Preview Manager page in the Google SecOps platform. 

This document describes how to use Gemini to generate custom Python code for response actions in the Google SecOps Integrated Developer Environment (IDE). This capability lets you create new actions by providing a natural language description of your requirements.

**Note:** You can only use this feature to create actions for existing integrations. You can't generate new actions for new integrations. 

## Create an action with Gemini

  1. In the Google SecOps navigation menu, go to **Response > IDE**.
  2. In the IDE, select an integration and open the **Create New Action** menu.
  3. Click **Generate action with Gemini**.
  4. In the **Generate action** dialog, perform the following:
     1. Choose an integration from the **Integration** list.
     2. Enter a detailed prompt in the **Enter prompt** field.
**Note:** For more information about generating the best results with prompts, see Prompting best practices.
  5. Click **Generate with Gemini**.
  6. Review the preview screen, which displays the entered prompt, a description of the proposed action, and details regarding its inputs and outputs.
  7. Click **Proceed**.
  8. In the editor that appears, review the generated code. Depending on the results, choose one of the following options: 
     * Accept: If the code meets your requirements, click **Save**.
     * Modify: Manually edit the code directly in the editor to refine the logic, then click **Save**.
     * Iterate: If the code requires significant changes, return to the prompt field to provide more specific instructions and regenerate the action.
     * Discard: Navigate away from the page or select a different item. A confirmation dialog appears to ensure you want to exit without saving the generated code.
  9. Configure the action's technical specifications, including **Timeout** , **Parameters** , and **JSON Result** settings. For more information, see [Create a new action to be used in a playbook](https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/using-the-ide#create-new-action-for-playbook).
  10. Set the toggle to **Enabled** and click **Save**.



The action is now available for use in **Playbook > Actions**.

## Prompting best practices

To get the most accurate and usable code from Gemini, follow these best practices when writing your prompt:

  * Suggest specific names and parameters: Explicitly suggest the name for the action and the parameters it should include.
  * Focus on single endpoints: For best results, use prompts for synchronous actions that interact with a single API endpoint.
  * Define the JSON structure: Suggest the appropriate structure for the JSON results to ensure the code aligns with your playbook requirements.
  * Keep code in a single module: Request that all code for the action be written in one single module to help with review and implementation.
  * Include documentation and examples: Add links to API documentation, API examples, or specific usage examples within your prompt.
  * Reference existing integration assets: You can reference other scripts from the same integration to guide the generation logic and style.



## Example use case

You can use the following prompt to generate a new action in the **Google Chronicle** response integration that combines multiple existing functions into a single custom action:
    
    
    Create an action that combines the case tag action and case priority action. 
    It should accept the same parameters as each original action and perform the 
    same logic based on those parameters. Ensure the action returns a JSON result 
    of the affected case in the following format:
    
    {
      "case": case_id,
      "case_tag": tag,
      "priority": priority
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

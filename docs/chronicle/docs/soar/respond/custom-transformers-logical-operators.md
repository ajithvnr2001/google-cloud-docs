---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/custom-transformers-logical-operators/
title: Develop custom transformers \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:27.887082+00:00
---

# Develop custom transformers  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/custom-transformers-logical-operators/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Develop custom transformers

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

You can create custom Python-based transformation functions and logical operators directly within the IDE and use them in your playbooks for complex and versatile use cases.

## Extension Packs

An _extension pack_ is a specialized integration type designed to act as a container for custom transformation functions and logical operators. Unlike standard integrations, extension packs don't require instance configuration and can be created directly from the IDE.

### Best practices for extension packs

  * **Consolidation:** Create one main extension pack and add multiple transformation functions or logical operators to it.
  * **Separation:** Create a new extension pack when you need a different set of Python libraries (dependencies) that might conflict with the main pack.

**Important:** Creating extension packs in the IDE requires the **All environments** permission. 

### Create an Extension Pack

To create a new extension pack, follow these steps:

  1. Go to **Response > IDE**.
  2. Click add **Create New Item**.
  3. Select **Extension Pack** from the drop-down.
  4. Provide a unique **Name** for the Extension Pack.
**Note:** The name cannot be changed after creation. 
  5. Click **Save**.



### Upload dependencies

Like standard integrations, extension packs run in a virtual environment where you can manage Python libraries.

To manage your libraries, follow these steps:

  1. Open the **Extension Pack settings** in the IDE.
  2. Add required Python libraries from PyPi or upload them from your computer.



These dependencies are available to all transformers and logical operators contained within this specific extension pack.

### Import and Export

You can manually import and export extension packs directly within the IDE interface.

**Note:** Import and export might not be available for customers who have not yet completed the stage 2 migration. For more information, see the [SOAR migration overview](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp). 

## Custom Transformers

**Custom Transformers** are user-defined Python functions that extend the prebuilt functions in the **Expression Builder**. You can create them directly within the IDE to extract and manipulate data, and they can be used alongside existing built-in functions.

### Create a custom transformer

To define a new custom transformer, follow these steps:

  1. In the **IDE** , locate your target extension pack.
  2. Select the target extension pack to add a new item under the pack.
  3. Select **Custom Transformation Function**.
  4. Give it a name.
**Note:** The name cannot be changed after creation. 
  5. Optional: Add a description. This is displayed when you hover over the custom transformer in the Expression Builder.
  6. Define the script logic using Python. You can use the provided default template as a starting point. 
     * The script must include a `main` function as shown in the **predefined template**.
     * The script must return a result to the expression builder by using the SDK `end` function.
     * The input of the custom transformer can be in different types (for example, string or list). Ensure you convert it to the expected type in your `main` function.
     * You can use only a subset of the SDK methods within the IDE for transformers: 
       * `transformer.extract_param("ParamName")`: To retrieve input values.
       * `transformer.LOGGER`: To write logs for debugging.
       * `transformer.end(result)`: To return the transformed value.
  7. Create parameters: 
     * Each custom transformer function includes a default **Input** parameter. This parameter represents the input data, which is the placeholder the function applies to. You cannot delete this parameter.
     * Additionally, you can add optional parameters to be used within your function.
  8. Documentation (Optional): Define in-product documentation for the Expression Builder: 
     * **Expected Input:** Describe the data type the function expects to receive for this transformer (for example, "String" or "List of strings").
     * **Expected Output:** Describe the data type the function expects to return for this transformer (for example, "boolean").
     * **Usage Example:** Provide an example of how to invoke the function (for example, `if_empty("new_value")`).



You can test your custom transformation function logic directly within the IDE before using it in a playbook. This lets you verify that your Python script handles various input types and parameters correctly and returns the expected results.

#### Timeout

  * **Default Timeout:** 1 minute.
  * **Maximum Timeout:** 3 minutes.

Note: Since the platform waits for the function to complete, you must minimize execution time. Focus on direct data transformations and avoid heavy processing or querying external sources. 

### Use custom transformers in the Expression Builder

Once saved, custom transformers appear in the Expression Builder's function list alongside built-in functions. They are identified by the format: `ExtensionPackName.TransformerName`. Hovering over the function displays the documentation generated from your parameter descriptions.

### Support for all placeholders (JSON and non-JSON)

The Expression Builder supports every placeholder exposed in the Playbook Designer, including non-JSON results.

For non-JSON placeholders:

  * You can manually enter sample data into the Expression Builder to test logic against various input types: string, list (comma-separated values), and JSON.
  * Testing with an input type does not guarantee the placeholder will return that specific type at runtime.
  * Most placeholders resolve as strings, except for specific types that resolve as a string or list based on their quantity (for example, `entity.identifier`). For these, it's recommended to always treat the input as a list.

**Note:** Sample data is transient and won't be saved after you close the Expression Builder or save the expression. You must re-enter sample data if you open the builder again. 

### Error Handling

If a custom transformation function encounters an error during execution, the playbook action that uses that transformer fails. The specific error message generated by the Python script is displayed on the screen within the playbook run view, allowing you to troubleshoot the logic directly.

## Custom Logical Operators

**Custom Logical Operators** let you define your own boolean logic for comparing values.

### Create a custom logical operator

To define a new logical operator, follow these steps:

  1. In the **IDE** , locate your target **Extension Pack**.
  2. Select **Custom Logical Operator**.
  3. Give it a name.
**Note:** The name cannot be changed after creation. 
  4. Optional: Add a description for the logical operators menu in the Playbook Designer.
  5. Define the script logic using Python. You can use the provided predefined template as a starting point. 
     * The script must include a `main` function.
     * The script must return a boolean result to the condition by using the SDK `end` function.
     * You can use only a subset of the SDK methods within the IDE for logical operators:
       * `logical_operator.extract_param("ParamName")`: To retrieve input values.
       * `logical_operator.LOGGER`: To write logs for debugging.
       * `logical_operator.end(result)`: Result is a boolean value (`true` or `false`).



You can test your custom logical operator logic directly within the IDE. This lets you input test values for the arguments and verify that the function returns the correct boolean (True or False) result based on your defined conditions.

#### Parameters

Custom logical operators accept two parameters: **Left Side** (mandatory and not editable) and **Right Side** (optional; can be disabled by the user).

  * **Example 1:** `if [left side] not in [right side]`.
  * **Example 2:** `if [left side] is greater than 80` (no right side).



#### Timeout

  * **Default Timeout:** 1 minute.
  * **Maximum Timeout:** 3 minutes.

**Note:** Since the platform waits for the function to complete, you must minimize execution time. Best practice is to focus on direct data transformations and avoid querying external sources or performing heavy processing. 

### Use in playbooks

Custom logical operators appear in the operator menu within **Playbook Conditions** , **Previous Action Conditions** , and **Entity Selection**.

Custom logical operators are selectable alongside standard operators (for example, "Equals" or "Contains").

### Error Handling

If a custom logical operator function encounters an error during execution, the playbook condition or step using that operator will fail. The error message returned by the Python script is displayed within the playbook run view to assist with troubleshooting.

## Limitations

  * Custom transformation functions and logical operators are not supported in **Triggers** or **Webhooks**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

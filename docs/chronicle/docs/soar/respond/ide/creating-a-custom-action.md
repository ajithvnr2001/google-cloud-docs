---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/creating-a-custom-action/
title: Create custom actions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:54.264483+00:00
---

# Create custom actions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/creating-a-custom-action/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create custom actions

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

In [Build a custom integration](https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/building-a-custom-integration), you created a Ping action for the Armis integration. This document outlines how to create a custom action for the Armis integration that enriches entities. It assumes you have a working knowledge of Python and object-oriented programming. For a prerequisite, refer to the SDK documentation and custom integration procedure, and explore the SDK modules. 

## Create a custom action

To create a custom action, follow these steps:

  1. Go to **Response > IDE**; the **IDE** page appears.
  2. Click add**Create New Item** and select **Action**. Enter a name and select the integration.
  3. Click **Create**. IDE creates a new template with code comments and explanations.



## The Siemplify action object

A Siemplify action requires these steps:

  * An object must be instantiated from the `SiemplifyAction` class.
  * The object must use the class's `end` method to return an output message and a result value.



### Result values

Every action has an **Output Name** that represents the result value returned by the SiemplifyAction's `end` method. By default, this is `is_success`, but you can change it in the Integrated Development Environment (IDE). You can also set a default **Return Value** for when an action fails. For example, if the action times out after five minutes (or fails for any other reason), the `ScriptResult` is set to `Timeout`. 

**Note:** The default return value is crucial for controlling playbook flow. You can use it in a condition to branch the playbook if an action fails or times out. 

#### JSON result value

You can also add a JSON result, which is useful for pivoting on data in playbooks or for manual analysis. To do this, use the `add_result_json` method on the `SiemplifyAction` result property or the `add_entity_json` method to attach a JSON result directly to an entity. 

### Imports and constants

The `SiemplifyAction` class from the `SiemplifyAction` module is always imported. Other common imports include:

  * `output_handler` from `SiemplifyUtils` for debugging.
  * `add_prefix_to_dict_keys` and `convert_dict_to_json_result_dict` for data transformation.
  * `EntityTypes` to determine the type of entity an action will run on.



This action also reuses the `ArmisManager` created in the custom integration procedure and import the standard `json` library. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

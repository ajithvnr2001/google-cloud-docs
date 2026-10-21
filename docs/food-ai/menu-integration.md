---
url: https://docs.cloud.google.com/food-ai/menu-integration/
title: Integrating menu data using the Food Ordering AI Agent API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:48:44.587941+00:00
---

# Integrating menu data using the Food Ordering AI Agent API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/menu-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Guides ](https://docs.cloud.google.com/food-ai/concepts)



Send feedback 

#  Integrating menu data using the Food Ordering AI Agent API Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to structure, transform, and ingest your restaurant menu data into the Food Ordering AI Agent Menu API. By doing so, you enable the AI agent to understand your menu offerings and accurately take orders from customers. 

## Before you begin

Before you can ingest and manage menus using the Food Ordering AI Agent API, first:

  1. Enable the Food Ordering AI Agent API:
         
         gcloud services enable foodorderingaiagent.googleapis.com --project=PROJECT
         

  2. Ensure you have the necessary IAM permissions. Grant the following Identity and Access Management (IAM) role to the user or service account that interacts with the API:

     * **Food Ordering Agent Admin** (`roles/foodorderingaiagent.admin`): This role provides full access to create, read, update, and delete all Food Ordering AI Agent resources, including Brands, Stores, and Menus.

You can grant IAM roles using the Google Cloud console, the `gcloud` command-line tool, or the IAM API. For more information, see [Grant an IAM role](https://docs.cloud.google.com/iam/docs/grant-role-console).

To grant the role using Google Cloud console:

     1. In the Google Cloud console, go to the **IAM** page.
     2. Click **Add**.
     3. Enter the principal (user or service account email).
     4. Select the **Food Ordering AI Agent Admin** role.
     5. Click **Save**.

Without the appropriate permissions, API calls to create or modify Brands, Stores, or Menus are denied. The `Food Ordering Agent Viewer` role is insufficient for the tasks described in this guide, as it only grants read-only access.




## Overview

The Food Ordering AI Agent Menu API is designed to be flexible and accommodate various menu structures, from short lists of standalone items to complex menus with nested modifiers and combination meals. The API is built around a few key concepts:

  * **Menu:** The top-level container for all orderable entities.
  * **Item:** Represents an orderable top-level product from the menu, such as a meal, entree, or any product which can be ordered standalone. `Item`s can reference `ModifierGroup`s.
  * **ModifierGroup:** A collection of `Modifier` options that can be applied to an `Item` or another `Modifier` (allowing nesting). Examples include "Choose Your Side", "Add Toppings", or "Select Drink Flavor."
  * **Modifier:** An individual option within a `ModifierGroup`, such as "Fries", "Extra Cheese", or "Cola." Modifiers can adjust the price and can also have their own nested `ModifierGroup`s.
  * **MenuCategory:** Used to organize `Item`s into sections for display and display understanding (e.g., "Appetizers", "Burgers", "Drinks").



## Key concepts and structure

This section details the core components of the Food Ordering AI Agent Menu API schema and how they are structured. Understanding these concepts is crucial for correctly modeling your menu data.

### Items

Each distinct item on your menu should be defined as an `Item`. Key fields include:

  * `id`: A unique identifier within the menu.
  * `display_name`: The customer-facing name.
  * `base_price`: The base price of the item.
  * `modifier_groups`: References to `ModifierGroup`s that can apply to this item.
  * `category_ids`: References to `MenuCategory` IDs this item belongs to.
  * `availability`: Specifies when the item is available (e.g., by status or daypart). Defaults to `STATUS_AVAILABLE` if not specified.



### Modifiers and ModifierGroups

Modifiers allow for customization of items.

  * `ModifierGroup`s define a set of choices, including constraints like minimum or maximum selections. Must contain at least one `Modifier`.
  * `Modifier`s represent the actual options. They can have a `price_adjustment` and can recursively reference other `ModifierGroup`s for nested customizations (e.g., a "Meal Combo" `Item` might have a "Choose Your Drink" `ModifierGroup`, and the "Soda" `Modifier` within that group could have a "Choose Flavor" `ModifierGroup`).

**Tip:** The agent actively works with customers to satisfy constraints specified in each `ModifierGroup`. For example, if an `Item` (e.g. "Fajitas for two") references a `ModifierGroup` with `min_selection_count` `2` (e.g. "Two drinks"), and a customer orders `Item` without specifying a selection for that `ModifierGroup` (e.g. "I would like the fajitas for two."), the agent works with the customer to satisfy the constraints (e.g. "Which two drinks would you like with that?").

#### Example 1: Toppings

A "Bacon Cheeseburger" `Item` might reference a "Toppings" `ModifierGroup`. This `ModifierGroup` would contain `Modifier`s like "Extra Cheese", "No Onions", etc.

#### Example 2: Combination meals (Combos)

Some menus have complex structures consisting of multiple nested choices, such as combination meals, or "combos". Combos can be modeled as an `Item` with several `ModifierGroup`s representing the components of the combo. For example, a "Burger Combo" `Item`, consisting of a fixed entree bundled with multiple options for side and drink could be modeled with:

  * A `ModifierGroup` for the side (e.g., "Side choices"). 
    * Each side option is modeled as a `Modifier` (e.g., "Fries", "Salad"). 
      * Each drink option may reference nested `ModifierGroup`s (e.g., "Ice options", "Drink size") which in turn references `Modifier`s (e.g. "No Ice", "Large drink", respectively).
  * A `ModifierGroup` for the drink (e.g., "Drinks"). 
    * Each drink option is modeled as a `Modifier`. 
      * Each drink option may reference nested `ModifierGroup`s (e.g., "Ice options", "Drink size") which in turn references `Modifier`s (e.g. "No Ice", "Large drink").
  * A `ModifierGroup` for toppings on the entree. (e.g., "Extra Cheese", "Bacon").



### Availability

The `Availability` message on `Item`s and `Modifier`s lets you specify:

  * `status`: `STATUS_AVAILABLE`, `STATUS_OUT_OF_STOCK`, etc.
  * `daypart_availability`: Links to specific daypart IDs if the item is only available during certain times (e.g., "Breakfast Menu").



### Integration attributes

`Item`, `Modifier`, and `ModifierGroup` messages contain an `integration_attributes` field. This field (`ItemIntegrationAttributes`, `ModifierIntegrationAttributes`, etc.) holds a `google.protobuf.Struct` called `custom_integration_attributes`. You can use this to store arbitrary key-value data, such as:

  * IDs from your Point of Sale (POS) system.
  * SKUs or other internal codes.
  * Any other metadata needed for downstream order processing or POS integration.



This data is passed through opaquely by the AI agent.

### Labels

You can use the `labels` field on the `Menu` resource to attach metadata to menus to help with integration and debugging.

Labels are a convenience feature and have no effect on the AI agent's behavior.

**Tip:** You can use labels to annotate a `Menu` with the associated version identifier, effective timestamp, or a URL from which the menu data was retrieved. This is helpful for tracing back nuances of agent behavior to particular menu source data.

## Creating a Menu

Menus are ingested using the `CreateMenu` RPC call within the `MenuService`.

### Steps

  1. **Transform Your Data:** Convert your existing menu data (from your POS, API, or other source) into the structure defined by the `google.cloud.foodorderingaiagent.v1beta.Menu` message. This involves mapping your items, modifiers, categories, and prices to the corresponding API message types.
  2. **Construct the`CreateMenuRequest`:**
     * Set the `parent` field (e.g., `projects/PROJECT/locations/LOCATION`).
     * Populate the `menu` field with your transformed `Menu` object.
     * Optionally provide a `menu_id`.
  3. **Call the API:** Send the `CreateMenuRequest` to the `MenuService.CreateMenu` endpoint. The API will first sanitize the menu, then validate it, and return the final `Menu` object.
  4. **Handle Menu Updates:** Upon each update to the menu source data (e.g. when a new product is introduced, or when a product becomes unavailable), a new `Menu` should be created reflecting the updated source data, following handling menu updates.



### Guidance for data transformation

The specific logic for transforming your menu data will depend on the format and structure of your source system (e.g., POS API, database schema). Here's a general approach:

  * **Export Data:** Obtain a complete export of your menu data, including all items, modifiers, prices, and relationships.
  * **Map Entities:**
    * Identify the corresponding entities in the Food Ordering AI Agent API schema for each element in your source data. For example, your POS "menu items" will likely map to `Item` objects. "Order options" or "add-ons" will map to `Modifier`s and `ModifierGroup`s.
    * Establish relationships using IDs. For example, link `Item`s to their applicable `ModifierGroup`s using the `modifier_groups` reference field.
  * **Handle Nested Structures:** If your menu has nested modifiers (e.g., choosing a drink flavor for a combo meal's soda), model this by having `Modifier`s reference other `ModifierGroup`s.
  * **Populate Attributes:** Fill in fields like `display_name`, `base_price`, `price_adjustment`, and `availability` based on your source data.
  * **Include POS IDs:** Crucially, store your internal POS or system IDs for each item, modifier, and group within the `custom_integration_attributes` field. This lets you translate the `Order` produced by the agent back to your application's representation of a final order or in-progress cart.
  * **Scripting:** You will likely need to write a script (e.g., in Python, Node.js, Go) to fetch data from your source, perform the transformation, and call the `CreateMenu` method. This script will use the Google Cloud client libraries for authentication and API interaction.



**Conceptual Transformation Workflow:**

This workflow outlines the process of transforming menu data from a source system into the Food Ordering AI Agent API format:

  1. **Extract and Map Categories:**
     * Identify categories or sections in your source data (e.g., "Appetizers", "Entrees").
     * Transform each into a `MenuCategory` object with a unique `id` and `display_name`.
  2. **Extract and Map Items:**
     * Identify sellable items in your source data.
     * Transform each into an `Item` object, populating `id`, `display_name`, `base_price`, and `availability`.
     * Map each `Item` to its categories using the `category_ids` field.
     * Store source system identifiers (like PLU or SKU) in `item.integration_attributes.custom_integration_attributes`.
  3. **Extract and Map Modifiers:**
     * Identify item customizations, options, or add-ons in your source data.
     * Group related options (e.g., "Side Options", "Drink Choices", "Extra Toppings") into `ModifierGroup` objects. Define minimum and maximum selection rules on each `ModifierGroup`.
     * Transform each individual option (e.g., "Fries", "Cola", "Extra Cheese") into `Modifier` objects within the appropriate `ModifierGroup`. Populate `price_adjustment` if applicable.
     * Store source system identifiers in `modifier_group.integration_attributes.custom_integration_attributes` and `modifier.integration_attributes.custom_integration_attributes`.
  4. **Establish Relationships:**
     * For each `Item`, populate its `modifier_groups` field with references to the `id`s of `ModifierGroup`s that apply to it.
     * If a `Modifier` allows for further customization (e.g., choosing a flavor for a "Soda" modifier), populate its `modifier_groups` field to create nested modifiers.
  5. **Assemble and Ingest:**
     * Combine all `MenuCategory`, `Item`, `ModifierGroup`, and `Modifier` objects into the lists within a single `Menu` message.
     * Call the `CreateMenu` RPC with the fully assembled `Menu` message as input.



## Handling menu updates

[Menu](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#menu) is **immutable**. Once a menu is created using the `CreateMenu` RPC call, it cannot be modified. To propagate menu updates into a menu—such as changing item prices, modifying options, or adjusting availability—you must create a new menu resource by calling `CreateMenu` again. Each version of your menu should be ingested as a new `Menu` resource with a unique `menu_id`.

The process for ingesting a new version of a menu is identical to ingesting the menu for the first time, and it undergoes the same sanitization and validation steps. While handling orders, the agent's behavior will always reflect the _most recently created_ `Menu` associated with the `Store` referenced in the session's configuration.

**Tip:** Labels are a helpful way to associate metadata that distinguishes related `Menu`s. Diagnosing operational issues is often easier when each `Menu` is annotated with information identifying the event that triggered its creation and information identifying source of its content.

## Automatic menu sanitization

The CreateMenu API automatically performs several sanitization steps to correct common issues and ensure menu content is represented consistently throughout the API. Validations are applied after these sanitizations to simplify menu integration for clients:

  * **Default availability:** `Item`s and `Modifier`s without an explicit `Availability.Status` are set to `STATUS_AVAILABLE`.
  * **Drop unreferenced entities:** `Modifier`s and `ModifierGroup`s that are not transitively referenced by any `Item` are removed from the menu, as they can't be ordered.
  * **Drop empty modifier groups:** `ModifierGroup`s that contain no `modifier_ids` are dropped, and any references to them are removed.



## Menu validation

After sanitization, the API validates the menu against a strict set of rules to ensure it's well-formed and can be reliably used by the AI agent. If validation fails, the `CreateMenu` call will return an error detailing the issues. Key validations include:

  * **Required fields:** Ensures all required fields like `id`, `display_name`, and `availability.status` are present.
  * **Unique IDs:** All `Item`s, `Modifier`s, and `ModifierGroup`s must have unique IDs within the menu.
  * **Unique display names:**
    * All `Item`s must have unique `display_name`s.
    * Within any given `ModifierGroup`, all contained `Modifier`s must have unique `display_name`s.
  * **Reference integrity:**
    * All `modifier_group_ids` referenced by `Item`s or `Modifier`s must exist in the menu.
    * All `modifier_ids` referenced by `ModifierGroup`s must exist in the menu.
    * Default modifiers specified in `ModifierGroupReference` must exist in the referenced `ModifierGroup`.
    * If a `Modifier` uses `item_id` to reference an `Item`, that `Item` must exist.
  * **Modifier group constraints:**
    * `ModifierGroup`s cannot be empty.
    * Minimum or maximum selection counts within `ModifierGroup`s are checked for logical consistency.
    * `Item` or `Modifier` level `modifier_constraints` are validated against the selection count constraints of referenced `ModifierGroup`s to ensure they are satisfiable.
  * **Nesting depth:** The depth of nested modifiers is limited (e.g., `Item` -> `ModifierGroup` -> `Modifier` -> `ModifierGroup` -> `Modifier`...) to a maximum of 5 levels.
  * **Daypart validation:** If dayparts are used in `Availability`, they must be defined in the associated `Store` resource.
  * **Modifier item references:** `Modifier`s referencing an `Item` using `item_id` cannot have fields like `display_name` or `availability` set, as these are inherited from the referenced `Item`.



A failure on any of these validation rules will prevent the menu from being created or updated. The error message will provide details on which entities are causing the violation.

## API reference

For complete details on all messages and fields, see the [Food Ordering AI Agent API RPC Reference](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta).

## Best practices

  * **Unique IDs:** Ensure all `id` fields within the `Menu` scope (for `Item`, `Modifier`, `ModifierGroup`, `MenuCategory`) are unique.
  * **Clear Names:** Use clear, customer-friendly `display_name`s. Provide distinct `display_name`s for semantically different products to steer the agent to disambiguate appropriately.
  * **Model Combos Effectively:** Model combination meals as an `Item` with `ModifierGroup`s representing sides, drinks, and other choices, as described in combination meals. This ensures the agent can correctly guide customers through combo selections.
  * **Use Integration Attributes:** Store any necessary POS or internal system identifiers in the `custom_integration_attributes` to facilitate seamless order integration.
  * **Manage Availability:** Keep the `Availability` status up-to-date.
  * **Test Thoroughly:** After ingestion, test the agent's understanding of the menu with various order combinations. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

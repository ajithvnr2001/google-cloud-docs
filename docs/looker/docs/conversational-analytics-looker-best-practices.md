---
url: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-best-practices/
title: Best practices for configuring Conversational Analytics in Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:39.930981+00:00
---

# Best practices for configuring Conversational Analytics in Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Best practices for configuring Conversational Analytics in Looker Stay organized with collections  Save and categorize content based on your preferences. 

[Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview) uses [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview) to interpret natural language questions, using your Looker [semantic model (LookML)](https://docs.cloud.google.com/looker/docs/what-is-lookml), data values, and data agent configurations as its source of truth. The quality of its responses is tied to how effectively you prepare these inputs.

This guide provides strategies and best practices for LookML developers and administrators to configure and optimize Conversational Analytics. By following these recommendations for your LookML model, Explores, and data agents, you can increase user adoption and ensure that users get accurate, relevant, and useful answers to their questions. This guide covers best practices as they relate to Conversational Analytics, following a logical flow that starts with developing a strong foundation in a model's LookML, configuring Explores that are based on this model, and building data agents that use these Explores as data sources.

  * LookML best practices for Conversational Analytics
  * Best practices for setting up an Explore for use with Conversational Analytics
  * Best practices for building data agents
  * When to add context to LookML versus agent instructions



## LookML best practices for Conversational Analytics

Conversational Analytics interprets natural language questions by leveraging these primary inputs:

  * **The LookML model** : The agent fetches the schema for the Explores that are connected to it. The schema includes fields ([dimensions](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension), [measures](https://docs.cloud.google.com/looker/docs/reference/param-field-measure)), filter-only fields ([filters](https://docs.cloud.google.com/looker/docs/reference/param-field-filter), [parameters](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter)), and their corresponding [labels](https://docs.cloud.google.com/looker/docs/reference/param-field-label), [descriptions](https://docs.cloud.google.com/looker/docs/reference/param-field-description), and [synonyms](https://docs.cloud.google.com/looker/docs/reference/param-field-synonyms) that are defined in the LookML model that underlies the Looker [Explore](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#explore). For the full list of LookML parameters that Conversational Analytics analyzes, see the [Conversational Analytics overview](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview#how-does-ca-work).
  * **Distinct field values** : The agent can sample data values and perform fuzzy searches to check for specific field values in the underlying database. These methods enable the agent to choose the correct fields, apply the correct filter values, and identify the available categories and entities that users might ask about.



The effectiveness of Conversational Analytics is directly tied to the quality and clarity of these inputs. The following table contains common ways that unclear or ambiguous LookML can negatively affect Conversational Analytics, along with solutions for reducing latency and improving the output and user experience.

LookML quality issue | Solution for clearer Conversational Analytics  
---|---  
**Lack of clarity and naming conflicts:** Fields that lack clear labels, have ambiguous definitions, or share similar names across different views can lead to incorrect field selection. | **Apply clear labels and thorough descriptions:**

  * Use the [label](https://docs.cloud.google.com/looker/docs/reference/param-field-label) parameter to give fields intuitive, business-friendly names.
  * Use the [description](https://docs.cloud.google.com/looker/docs/reference/param-field-description) parameter to provide critical context, natural language definitions, and industry-specific terminology. Conversational Analytics uses descriptions to better identify field meanings and map user terms.

  
**Field bloat:** Exposing too many fields — such as internal IDs, duplicate fields from joins, or intermediate calculations — clutters the options that are available to Conversational Analytics. | **Hide irrelevant fields:** Ensure all primary keys, foreign keys, and technical fields remain [hidden](https://docs.cloud.google.com/looker/docs/reference/param-field-hidden). **(Optional) Extend Explores:** For Explores with many fields, consider creating a dedicated version for Conversational Analytics by [extending an existing Explore](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends).  
**Database load for sampling and search:** Retrieving sample values and suggestions from the database can be slow or incur unnecessary load, especially when users reference specific data values in queries. | **Define suggestions in LookML:** Avoid real-time database queries for field suggestions by hard-coding values or pointing to more efficient dimensions: 

  * Use the [`suggestions`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggestions) parameter to hard-code a list of possible values.
  * Use the [`suggest_explore`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-explore) and [`suggest_dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-dimension) parameters to query an alternative, more efficient dimension for filter suggestions.

  
**Database load for data queries:** Large or inefficient queries can increase latency and database load. | **Optimize data queries:** Adhere to general [best practices for optimizing query performance](https://docs.cloud.google.com/looker/docs/best-practices/how-to-optimize-looker-performance), such as using [aggregate awareness](https://docs.cloud.google.com/looker/docs/aggregate-awareness) and efficient join logic.  
**Incomplete LookML definitions:** Relying on dashboard-level custom fields or table calculations makes critical business logic inaccessible to Conversational Analytics. | **Incorporate custom logic:** Convert important and commonly used [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields) or [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) into LookML dimensions and measures.  
**Messy data:** The following types of inconsistent or poorly structured data make it difficult for Conversational Analytics to interpret queries accurately. 

  * **Value variations:** Inconsistent capitalization or naming conventions (for example, a mix of the values `complete`, `Complete`, and `COMPLETE`) can lead to data duplication or incorrect data relationships in Conversational Analytics.
  * **Inconsistent data types:** Columns that are intended to be numeric and that contain occasional string values force the field type to be `string`, which prevents numerical operations.
  * **Timezone ambiguity:** Lack of standardized time zones in timestamp fields can lead to incorrect filtering or aggregation.

| **Address data quality:** Where possible, flag data quality issues (inconsistent values, types, time zones) that you identify during data curation. Work with data engineering teams to clean up the source data or apply transformations in the ETL/data modeling layer.  
  
### Key LookML takeaways

Keep these takeaways in mind when defining LookML for Explores that will be used as data sources for Conversational Analytics:

  * **Use clear and precise labels:** Choose labels for your data that reflect how your business users actually talk. Avoid technical shorthand like `"amt_usd_curr"` and instead use `"Amount (USD)"`.
  * **Enable seamless mapping:** Use synonyms and descriptions to help the agent map user questions to the correct fields.
  * **Centralize calculations:** Define frequently used calculations directly as LookML dimensions or measures to ensure a single source of truth and reduce latency.
  * **Streamline the context** : Hide technical or internal-only fields in LookML (like foreign keys or raw IDs) to ensure that only fields that are necessary for answering business questions are surfaced to Conversational Analytics. Focusing on only relevant fields reduces noise and improves the accuracy of field selection.
  * **Optimize sample data and fuzzy search queries** : Define hardcoded values in the `suggestions` parameter, or use `suggest_dimension` and `suggest_explore` for more efficient database queries.
  * **Optimize data queries:** Adhere to general [Looker best practices for optimizing query performance](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/run_query), such as using aggregate awareness and efficient join logic.

**Tip:** Conversational Analytics doesn't support custom fields in queries. You can monitor an Explore's commonly used custom fields in [System Activity](https://docs.cloud.google.com/looker/docs/system-activity-pages) and add those fields directly to your models.

For more best practices for writing clean, efficient LookML, see the following documentation:

  * [Best practice: What to do and what not to do with LookML](https://docs.cloud.google.com/looker/docs/best-practices/best-practices-lookml-dos-and-donts)
  * [Best practice: Create a positive experience for Looker users](https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-a-positive-experience-for-looker-users)
  * [Best practice: Writing sustainable, maintainable LookML](https://docs.cloud.google.com/looker/docs/best-practices/how-to-write-sustainable-maintainable-lookml)



## Best practices for setting up an Explore for use with Conversational Analytics

To help Conversational Analytics provide the most helpful answers, consider following these best practices when [defining your Explores](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#explore) to use as data source for Conversational Analytics:

  * In your Explore's underlying LookML, define only the fields that are useful for analysis by end users. 
    * Give each field a clear and concise name and description.
    * Include sample values where relevant. Sample values are especially helpful for string type fields.
  * Consider curating data agent-specific Explores that reuse content. 
    * Use [`extends`](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends) to build off existing LookML and curate the fields that the agent needs. In System Activity, users can see what fields are used in queries generated by agents and decide on fields to exclude.
    * Use field-level [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements) to create descriptions that are purpose-built for agents — "Use the Orders field when users refer to Sales".



## Best practices for building data agents

After establishing a solid foundation with LookML best practices and well-configured Explores, you can build [data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents) to provide customized conversational experiences for specific use cases or user groups. Data agents connect to up to five Explores and use natural language instructions to provide context, define terminology, and set behavioral guidelines.

Following best practices when building agents and writing instructions is crucial for tailoring the agent's responses to meet specific user needs and improve overall accuracy. These best practices include designing specialized agents for specific domains and writing clear, effective instructions.

**Tip:** Write your instructions in YAML or Markdown formatting to provide better organization for the agent.

### Build specialized agents

While it can be tempting to build one global data agent to handle all business questions, agents perform best when they are specialized for a specific domain, such as sales, marketing, or product analytics. An agent that is focused on one or a few closely related Explores can be given more precise instructions, which reduces ambiguity and improves response accuracy.

When designing your agents, avoid building a single agent to handle all unrelated data models. Instead, create focused agents for distinct business areas, connecting only to closely related Explores. For example, instead of one agent for all company data, create a "Revenue Agent" specifically focused on `Orders` and `Transactions` Explores.

### Write effective agent instructions

Agent instructions are your primary tool for customizing a data agent's behavior and infusing it with your organization's unique business logic and terminology. Think of instructions as a way to coach your agent on how to interpret user questions, handle ambiguity, and respond in a way that is most helpful to your users. Well-written instructions are key to generating accurate, relevant, and reliable answers.

Enter your agent instructions in the **Instructions** field when you create your data agent. For more information about creating agents, see the [Create and manage Explore data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents) documentation page.

**Tip:** Ask the [Gemini web app](https://gemini.google.com) to help you write agent instructions.

To write effective instructions, follow these best practices:

  * **Define business context and default behavior** : Coach the agent on your organization's unique logic and terminology. Use instructions to define acronyms (for example, "LY means Last Year"), explain common filtering logic, or set default behaviors for ambiguity (for example, "If no `date_created` is provided, filter to the last 6 months").
  * **Use LookML and filter syntax** : When referring to fields or applying filters in instructions, use LookML syntax (for example, `events.date_created`) and filter syntax (for example, `"last 6 months"`). This ensures that the agent understands which fields or filters to apply. For example: "When a user asks about 'region', use the `account_holder.geo_region` field."
  * **Be concise** : Write clearly and avoid unnecessary words or repetition within the instructions.
  * **Avoid redundancy** : Don't duplicate information that belongs in LookML, like field descriptions or synonyms. To learn more about when to define context in LookML versus agent instructions, see When to add context to LookML versus Conversational Analytics. Also avoid explaining basic concepts that the agent already understands, such as the difference between a dimension and a measure or how to perform basic date filtering.



#### Limitations of agent instructions

Note the following limitations of Conversational Analytics when writing your agent instructions:

  * Conversational Analytics doesn't support generating queries that contain the [`pivots`](https://docs.cloud.google.com/looker/docs/filtering-and-pivoting#pivoting_dimensions) parameter. Although Conversational Analytics can return data for multiple dimensions at once, it can't pivot them into separate columns the way that the Looker Explore UI can. Instead, it returns the data in a "long" or "flattened" format, so data is grouped horizontally rather than vertically.
  * Unlike LookML, which is governed, instructions are often free-form text and can become "stale" as the underlying data model evolves over time. To avoid stale instructions with Explore data agents, use [verified queries](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#define-verified-queries) to define pairs of natural language questions and their corresponding Explore queries.



#### Example agent instructions

Here are some sample instructions for a data agent that is connected to Looker Explores called **Order Items** and **Products** :
    
    
    # Define a persona and provide instructions on how to propose suggestions
    You are a helpful data assistant. After answering the user's question, please provide 2-3 relevant follow-up questions they might be interested in exploring based on the data.
    Anticipate the user's needs. Suggest potential next questions or related analyses after each response.
    Always offer suggestions for deeper dives into the data.
    Your tone should be professional and concise.
    
    # Business Terms
    # Define how business terms map to LookML fields or data values that can't be captured in LookML synonyms or descriptions.
    Terms:
      EOP: End of Period. This is the last day of the period.
      LY: Last Year.
      Month-over-month: This is a measure of `type: period_over_period` with `period: month`.
    
    # Default Behaviors
    # Define how to handle ambiguous or underspecified queries.
    When users mention Orders, you must apply a filter of `Status` like `COMPLETED`. Consider this a **hard-coded requirement**. Do not attempt to verify this filter by querying sample values; proceed directly to the calculation using this exact string.
    Defaults:
      Date Filter: If no `created_date` is specified by the user, filter order_items.created_date to "last 12 months".
      Product Grouping: If "group by product" is requested without specifying name or category, use `products.category`.
    
    # Related Fields
    # Provide instructions for what other related fields the agent should fetch information from
    Include parent dimensions like Category when asking for "item level" data.
    

## When to add context to LookML versus Conversational Analytics

In Conversational Analytics, you can add context to LookML or inside [agent instructions](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#write-agent-instructions). When you're deciding where to add context, apply the following guidance:

  * Context that should apply to all users of an Explore should be added directly to your LookML model, as Looker Explores may be used in multiple places, including both in dashboards and in Conversational Analytics. If context should only apply to certain users, consider using LookML features such as [user attributes](https://docs.cloud.google.com/looker/docs/reference/param-lookml-user-attributes) to create customized experiences.
  * Prioritize LookML for field-specific metadata and hard requirements. Place field-specific metadata, including synonyms and descriptions, directly in LookML rather than agent instructions. Requirements for things like default filter values or hidden fields should ideally be handled in LookML to ensure they are respected.
  * Don't duplicate information that the agent already knows, such as how to create a Looker query, an explanation of dimensions or measures, its accessible Explores, or how to do basic date filtering. Likewise, don't define the same term in both LookML and in the agent instructions.



Agent context should be qualitative and focused on the user, and there can be many agents serving different users from one Explore. LookML is good for defining _what_ a field is, but it can't usually define business strategy or predictive calculations. Examples of context that should be included in agent instructions, but not in LookML, are as follows:

  * Who is the user that is interacting with the agent? What is their role? Are they internal or external to the company? What is their previous analytics experience?
  * What is the goal of the user? What type of decision are they looking to make at the end of the conversation?
  * What are some types of questions that this user will ask?
  * What fields are most relevant for this user? For example, which fields should be accessible to this user, should certain filters always be applied, or should some fields be prioritized for this user?



## Related resources

  * [Recommended setup and rollout strategy for Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-rollout)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

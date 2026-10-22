---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-bq/
title: Define data agent context for BigQuery data sources \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:02.109654+00:00
---

# Define data agent context for BigQuery data sources  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-bq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Define data agent context for BigQuery data sources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to provide authored context for data agents that use BigQuery data sources.

[Authored context](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-system-instructions) is guidance that data agent owners can provide to shape the behavior of a data agent and to refine the API's responses. Effective authored context provides your Conversational Analytics API data agents with useful context for answering questions about your data sources.

While authored context is optional, providing robust context enables the agent to give more accurate and relevant responses. Your data agent incorporates this context during its creation and runtime to ensure that its actions, queries, and responses are accurate, compliant, and business-aware. This context is ingested, indexed, and used to shape the agent's behavior.

## Options for providing authored context

For BigQuery data sources, you can provide authored context through a combination of structured context and system instructions. Whenever possible, provide context through structured context fields. Then use the `system_instruction` parameter for supplemental guidance that isn't covered by the structured fields, such as defining an agent's tone or overall behavior.

After you define the structured fields and system instructions that make up your authored context, you can provide that context to the API in one of the following calls:

  * **Creating a persistent data agent** : Include authored context within the `published_context` object in the request body to configure agent behavior that persists across multiple conversations. For more information, see [Create a data agent](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#create_a_data_agent) (HTTP) or [Set up context for stateful or stateless chat](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk#set_up_context_for_stateful_or_stateless_chat) (Python SDK).
  * **Sending a stateless request** : Provide authored context within the `inline_context` object in a chat request to define the agent's behavior for that specific API call. For more information, see [Create a stateless multi-turn conversation](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#create-a-stateless-multi-turn-conversation) (HTTP) or [Send a stateless chat request with inline context](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk#send_a_stateless_chat_request_with_inline_context) (Python SDK).
  * **Send a query data request** : For database data sources, provide the context set ID of the authored context within the `agent_context_reference` object in the query data request. For more information, see [Define data agent context for database data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-databases#cloud-sql-cloud-sql-for-postgresql).



## Define structured context fields

This section describes how to provide context to a data agent by using structured context fields. You can provide the following information to an agent as structured context:

  * Table-level structured context, including a description, synonyms, and tags for a table
  * Column-level structured context, including a description, synonyms, tags, and sample values for a table's columns
  * Example queries, which let you provide natural language questions and corresponding SQL queries that the agent can use to answer questions and cite in its responses
  * User-defined functions, which let you provide custom BigQuery routines that the agent can use in its SQL queries



### Table-level structured context

Use the `tableReferences` key to provide an agent with details about the specific tables that are available for answering questions. For each table reference, you can use the following structured context fields to define a table's schema:

  * `description`: A summary of the table's content and purpose
  * `synonyms`: A list of alternative terms that can be used to refer to the table
  * `tags`: A list of keywords or tags that are associated with the table



The following examples show how to provide these properties as structured context within direct HTTP requests and with the Python SDK.

### HTTP

In a direct HTTP request, you provide these table-level properties within the `schema` object for the relevant table reference. For a complete example of how to structure the full request payload, see [Connect to BigQuery data](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#connect-to-bigquery-data).
    
    
    "tableReferences": [
      {
        "projectId": "bigquery-public-data",
        "datasetId": "thelook_ecommerce",
        "tableId": "orders",
        "schema": {
            "description": "Data for orders in The Look, a fictitious ecommerce store.",
            "synonyms": ["sales"],
            "tags": ["sale", "order", "sales_order"]
        }
      },
      {
        "projectId": "bigquery-public-data",
        "datasetId": "thelook_ecommerce",
        "tableId": "users",
        "schema": {
            "description": "Data for users in The Look, a fictitious ecommerce store.",
            "synonyms": ["customers"],
            "tags": ["user", "customer", "buyer"]
        }
      }
    ]
    

### Python SDK

When you use the Python SDK, you can define these table-level properties on the `schema` property of a `BigQueryTableReference` object. The following example shows how to create table reference objects that provide context for the `orders` and `users` tables. For a complete example of how to build and use table reference objects, see [Connect to BigQuery data](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk#connect-to-bigquery-data).
    
    
    # Define context for the 'orders' table
    bigquery_table_reference_1 = geminidataanalytics.BigQueryTableReference()
    bigquery_table_reference_1.project_id = "bigquery-public-data"
    bigquery_table_reference_1.dataset_id = "thelook_ecommerce"
    bigquery_table_reference_1.table_id = "orders"
    
    bigquery_table_reference_1.schema = geminidataanalytics.Schema()
    bigquery_table_reference_1.schema.description = "Data for orders in The Look, a fictitious ecommerce store."
    bigquery_table_reference_1.schema.synonyms = ["sales"]
    bigquery_table_reference_1.schema.tags = ["sale", "order", "sales_order"]
    
    # Define context for the 'users' table
    bigquery_table_reference_2 = geminidataanalytics.BigQueryTableReference()
    bigquery_table_reference_2.project_id = "bigquery-public-data"
    bigquery_table_reference_2.dataset_id = "thelook_ecommerce"
    bigquery_table_reference_2.table_id = "users"
    
    bigquery_table_reference_2.schema = geminidataanalytics.Schema()
    bigquery_table_reference_2.schema.description = "Data for users in The Look, a fictitious ecommerce store."
    bigquery_table_reference_2.schema.synonyms = ["customers"]
    bigquery_table_reference_2.schema.tags = ["user", "customer", "buyer"]
    

### Column-level structured context

The `fields` key, which is nested within a table reference's `schema` object, takes a list of `field` objects to describe individual columns. Not all fields need additional context; however, for commonly used fields, the inclusion of additional details can help improve the agent's performance.

For each `field` object, you can use the following structured context fields to define a column's fundamental properties:

  * `description`: A brief description of the column's contents and purpose
  * `synonyms`: A list of alternative terms that can be used to refer to the column
  * `tags`: A list of keywords or tags that are associated with the column



The following examples show how you can provide these properties as structured context for the `status` field within the `orders` table and for the `first_name` field within the `users` table with direct HTTP requests and with the Python SDK.

### HTTP

In a direct HTTP request, you can define these column-level properties by providing a list of `fields` objects within the `schema` object of a table reference.
    
    
    "tableReferences": [
      {
        "projectId": "bigquery-public-data",
        "datasetId": "thelook_ecommerce",
        "tableId": "orders",
        "schema": {
          "fields": [{
              "name": "status",
              "description": "The current status of the order.",
          }]
        }
      },
      {
        "projectId": "bigquery-public-data",
        "datasetId": "thelook_ecommerce",
        "tableId": "users",
        "schema": {
          "fields": [{
              "name": "first_name",
              "description": "The first name of the user.",
              "tags": "person",
          }]
        }
      }
    ]
    

### Python SDK

When you use the Python SDK, you can define these column-level properties by assigning a list of `Field` objects to the `fields` property of a table's `schema` property.
    
    
    # Define column context for the 'orders' table
    bigquery_table_reference_1.schema.fields = [
        geminidataanalytics.Field(
            name="status",
            description="The current status of the order.",
        )
    ]
    
    # Define column context for the 'users' table
    bigquery_table_reference_2.schema.fields = [
        geminidataanalytics.Field(
            name="first_name",
            description="The first name of the user.",
            tags=["person"],
        )
    ]
    

### Example queries

The `example_queries` key takes a list of `example_query` objects that define natural language queries to help the agent provide more accurate and relevant responses. By providing the agent with both a natural language question and its corresponding SQL query, you can guide the agent to provide higher quality and more consistent results.

If a user's question semantically matches a defined example query, the agent might execute that query directly rather than by generating a new one. When an agent executes an existing query, the API response includes a `matched_query` object to indicate that a [verified query](https://docs.cloud.google.com/bigquery/docs/conversational-analytics) was used. The agent might also cite that query in its response.

**Note:** The agent uses semantic matching to determine whether a question is a match. A user's input doesn't need to match your example exactly or contain specific keywords.

#### Parameterized example queries

In addition to static queries, you can define parameterized example queries that let the agent substitute dynamic values into a verified query template. By including parameters in your example queries, you can create flexible templates that cover a broader range of user inquiries than static examples. When a user's question matches a template, the agent executes the corresponding query to provide a verified response.

You can define a parameterized query as follows:

  1. In the `naturalLanguageQuestion` field, use curly braces for placeholders, such as `{state}`.
  2. In the `sqlQuery` field, use the BigQuery named parameter syntax for the same variable, such as `@state`.
  3. In the `parameters` field, define each parameter's name, data type, and description.



#### Examples

The following examples show how to define both static and parameterized example queries for the FAA airports dataset.

### HTTP

In a direct HTTP request, provide a list of `example_query` objects in the `example_queries` field. For each object, provide the `naturalLanguageQuestion` key (the question that a user might ask) and its corresponding `sqlQuery` key. For parameterized queries, you must also provide a `parameters` list that includes the name, data type, and description of each parameter.
    
    
    "example_queries": [
      {
        "naturalLanguageQuestion": "How many airports are there?",
        "sqlQuery": "SELECT COUNT(*) FROM `bigquery-public-data.faa.us_airports`"
      },
      {
        "naturalLanguageQuestion": "How many airports are in {state} with an elevation that is greater than {elevation}?",
        "sqlQuery": "SELECT COUNT(*) FROM `bigquery-public-data.faa.us_airports` WHERE LOWER(state_abbreviation) = @state AND elevation > @elevation",
        "parameters": [
          {
            "name": "state",
            "dataType": "STRING",
            "description": "The state abbreviation in lowercase.",
          },
          {
            "name": "elevation",
            "dataType": "FLOAT64",
            "description": "The elevation in feet.",
          }
        ]
      }
    ]
    

### Python SDK

When using the Python SDK, provide a list of `ExampleQuery` objects. For each object, provide values for the `natural_language_question` parameter (the question that a user might ask) and `sql_query` parameters. For parameterized queries, you must also provide a list of `QueryParameter` objects.
    
    
    example_queries = [
        geminidataanalytics.ExampleQuery(
            natural_language_question="How many airports are there?",
            sql_query="SELECT COUNT(*) FROM `bigquery-public-data.faa.us_airports`"
        ),
        geminidataanalytics.ExampleQuery(
            natural_language_question="How many airports are in {state} with an elevation that is greater than {elevation}?",
            sql_query="SELECT COUNT(*) FROM `bigquery-public-data.faa.us_airports` WHERE LOWER(state_abbreviation) = @state AND elevation > @elevation",
            parameters=[
                geminidataanalytics.QueryParameter(
                    name="state",
                    data_type="STRING",
                    description="The state abbreviation in lowercase.",
                ),
                geminidataanalytics.QueryParameter(
                    name="elevation",
                    data_type="FLOAT64",
                    description="The elevation in feet.",
                ),
            ],
        )
    ]
    

### User-defined functions

You can provide [user-defined functions (UDFs)](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions) for BigQuery in the agent context by using the `user_functions` field. When you provide custom [BigQuery routines](https://docs.cloud.google.com/bigquery/docs/user-defined-functions#authorize_routines), the agent can use them if they're needed to answer a question.

For each UDF, you can provide the following properties:

  * `routineReference`: A reference to the BigQuery routine that includes the project ID, dataset ID, and routine ID. To use a routine in a different region from your API endpoint (for example, if you access a table in the `us-east4` region from the `us` multi-region API endpoint), specify that region in the `boundaryLocationId` field.
  * `description`: A summary of the function's behavior that is used by the agent to determine when the function is appropriate for an answer.



The following examples show how to provide user-defined functions with direct HTTP requests and with the Python SDK.

### HTTP

In a direct HTTP request, provide a `user_functions` object that contains a `bqRoutines` list. Each object in the list must contain a `routineReference` property and a `description` field.
    
    
    "user_functions": {
      "bqRoutines": [
        {
          "routineReference": {
            "projectId": "bigquery-public-data",
            "datasetId": "thelook_ecommerce",
            "routineId": "my_custom_function"
          },
          "description": "Calculates adjusted revenue by using custom logic."
        }
      ]
    }
    

### Python SDK

When you use the Python SDK, you can define these routines by assigning a list of `BigQueryRoutine` objects to the `bq_routines` property of a `UserFunctions` object that is added to your agent's context.
    
    
    # Define a BigQuery routine (UDF)
    bq_routine = geminidataanalytics.BigQueryRoutine()
    bq_routine.routine_reference.project_id = "bigquery-public-data"
    bq_routine.routine_reference.dataset_id = "thelook_ecommerce"
    bq_routine.routine_reference.routine_id = "my_custom_function"
    bq_routine.description = "Calculates adjusted revenue by using custom logic."
    
    # Add the routine to the agent's context
    user_functions = geminidataanalytics.UserFunctions()
    user_functions.bq_routines = [bq_routine]
    
    # Assign to context
    context.user_functions = user_functions
    

## Define additional context in system instructions

You can use the `system_instruction` parameter to provide supplemental guidance for context that isn't supported by structured context fields. By providing this additional guidance, you can help the agent better understand the context of your data and use case.

System instructions consist of a series of key components and objects that provide the data agent with details about the data source and guidance about the agent's role when answering questions. You can provide system instructions to the data agent in the `system_instruction` parameter as a YAML-formatted string.

**Important:** Although the `system_instruction` parameter is optional and the structure is up to your discretion, we recommend that you provide well-structured system instructions to enable the agent to give more accurate and relevant responses.

The following template shows a suggested YAML structure for the string, which you can provide to the `system_instruction` parameter for a BigQuery data source, including available keys and expected data types. While this template provides a suggested structure with important components for defining system instructions, it does not include all possible system instruction formats.
    
    
    - system_instruction: str # A description of the expected behavior of the agent. For example: You are a sales agent.
    - tables: # A list of tables to describe for the agent.
      - table: # Details about a single table that is relevant for the agent.
        - name: str # The name of the table.
        - fields: # Details about columns (fields) within the table.
          - field: # Details about a single column within the current table.
            - name: str # The name of the column.
            - aggregations: list[str] # Commonly used or default aggregations for the column.
      - relationships: # A list of join relationships between tables.
        - relationship: # Details about a single join relationship.
          - name: str # The name of this join relationship.
          - description: str # A description of the relationship.
          - relationship_type: str # The join relationship type: one-to-one, one-to-many, many-to-one, or many-to-many.
          - join_type: str # The join type: inner, outer, left, right, or full.
          - left_table: str # The name of the left table in the join.
          - right_table: str # The name of the right table in the join.
          - relationship_columns: # A list of columns that are used for the join.
            - left_column: str # The join column from the left table.
            - right_column: str # The join column from the right table.
    - glossaries: # A list of definitions for glossary business terms, jargon, and abbreviations.
      - glossary: # The definition for a single glossary item.
        - term: str # The term, phrase, or abbreviation to define.
        - description: str # A description or definition of the term.
        - synonyms: list[str] # Alternative terms for the glossary entry.
    - additional_descriptions: # A list of any other general instructions or content.
      - text: str # Any additional general instructions or context not covered elsewhere.
    

The following sections contain examples of key components of system instructions:

  * `system_instruction`
  * `tables`
  * `relationships`
  * `glossaries`
  * `additional_descriptions`



### `system_instruction`

Use the `system_instruction` key to define the agent's role and persona. This initial instruction sets the tone and style for the API's responses and helps the agent understand its core purpose.

For example, you can define an agent as a sales analyst for a fictitious ecommerce store as follows:
    
    
    -   system_instruction: You are an expert sales analyst for a fictitious
        ecommerce store. You will answer questions about sales, orders, and customer
        data. Your responses should be concise and data-driven.
    

### `tables`

While you define a table's fundamental properties (such as its description and synonyms) as structured context, you can also use the `tables` key within system instructions to provide supplemental business logic. For BigQuery data sources, this includes using the `fields` key to define default `aggregations` for specific columns.

The following sample YAML code block shows how you can use the `tables` key within your system instructions to nest fields that provide supplemental guidance for the table `bigquery-public-data.thelook_ecommerce.orders`:
    
    
    -   tables:
      -   table:
        -   name: bigquery-public-data.thelook_ecommerce.orders
        -   fields:
          -   field:
            -   name: num_of_items
            -   aggregations: 'sum, avg'
    

### `relationships`

The `relationships` key in your system instructions contains a list of join relationships between tables. By defining join relationships, you can help the agent understand how to join data from multiple tables when answering questions.

As an example, you can define an `orders_to_user` relationship between the `bigquery-public-data.thelook_ecommerce.orders` table and the `bigquery-public-data.thelook_ecommerce.users` table as follows:
    
    
    -   relationships:
      -   relationship:
        -   name: orders_to_user
        -   description: >-
            Connects customer order data to user information with the user_id and id fields to allow an aggregated view of sales by customer demographics.
        -   relationship_type: many-to-one
        -   join_type: left
        -   left_table: bigquery-public-data.thelook_ecommerce.orders
        -   right_table: bigquery-public-data.thelook_ecommerce.users
        -   relationship_columns:
          -   left_column: user_id
          -   right_column: id
    

### `glossaries`

The `glossaries` key in your system instructions lists definitions for business terms, jargon, and abbreviations that are relevant to your data and use case. By providing glossary definitions, you can help the agent accurately interpret and answer questions that use specific business language. If an agent uses a glossary term to respond to a question, it might cite that term in its response.

As an example, you can define terms like common business statuses and "OMPF" according to your specific business context as follows:
    
    
    - glossaries:
      - glossary:
        - term: complete
        - description: Represents an order status where the order has been completed.
        - synonyms: 'finish, done, fulfilled'
      - glossary:
        - term: shipped
        - description: Represents an order status where the order has been shipped to the customer.
      - glossary:
        - term: returned
        - description: Represents an order status where the customer has returned the order.
      - glossary:
        - term: OMPF
        - description: Order Management and Product Fulfillment
    

### `additional_descriptions`

Use the `additional_descriptions` key to provide any general instructions or context that doesn't fit into other structured context or system instruction fields. By providing additional descriptions in your system instructions, you can help the agent better understand the context of your data and use case.

As an example, you can use the `additional_descriptions` key to provide information about your organization as follows:
    
    
    -   additional_descriptions:
      -   text: All the sales data pertains to The Look, a fictitious ecommerce store.
      -   text: 'Orders can be of three categories: food, clothes, and electronics.'
    

## Example: Authored context for a sales agent

The following example for a fictitious sales analyst agent demonstrates how to provide authored context by using a combination of structured context and system instructions.

### Example: Structured context

You can provide structured context with details about tables, columns, and example queries to guide the agent, as shown in the following HTTP and Python SDK examples.

### HTTP

The following example shows how to define structured context in an HTTP request:
    
    
    {
      "bq": {
        "tableReferences": [
          {
            "projectId": "bigquery-public-data",
            "datasetId": "thelook_ecommerce",
            "tableId": "orders",
            "schema": {
              "description": "Data for orders in The Look, a fictitious ecommerce store.",
              "synonyms": ["sales"],
              "tags": ["sale", "order", "sales_order"],
              "fields": [
                {
                  "name": "status",
                  "description": "The current status of the order."
                },
                {
                  "name": "num_of_items",
                  "description": "The number of items in the order."
                }
              ]
            }
          },
          {
            "projectId": "bigquery-public-data",
            "datasetId": "thelook_ecommerce",
            "tableId": "users",
            "schema": {
              "description": "Data for users in The Look, a fictitious ecommerce store.",
              "synonyms": ["customers"],
              "tags": ["user", "customer", "buyer"],
              "fields": [
                {
                  "name": "first_name",
                  "description": "The first name of the user.",
                  "tags": ["person"]
                },
                {
                  "name": "last_name",
                  "description": "The last name of the user.",
                  "tags": ["person"]
                },
                {
                  "name": "age_group",
                  "description": "The age demographic group of the user."
                },
                {
                  "name": "email",
                  "description": "The email address of the user.",
                  "tags": ["contact"]
                }
              ]
            }
          }
        ]
      },
      "example_queries": [
        {
          "naturalLanguageQuestion": "How many orders are there?",
          "sqlQuery": "SELECT COUNT(*) FROM `bigquery-public-data.thelook_ecommerce.orders`"
        },
        {
          "naturalLanguageQuestion": "How many orders were shipped?",
          "sqlQuery": "SELECT COUNT(*) FROM `bigquery-public-data.thelook_ecommerce.orders` WHERE status = 'shipped'"
        },
        {
          "naturalLanguageQuestion": "How many unique customers are there?",
          "sqlQuery": "SELECT COUNT(DISTINCT id) FROM `bigquery-public-data.thelook_ecommerce.users`"
        },
        {
          "naturalLanguageQuestion": "How many users in the 25-34 age group have a cymbalgroup email address?",
          "sqlQuery": "SELECT COUNT(DISTINCT id) FROM `bigquery-public-data.thelook_ecommerce.users` WHERE users.age_group = '25-34' AND users.email LIKE '%@cymbalgroup.com'"
        }
      ]
    }
    

### Python SDK

The following example shows how to define structured context with the Python SDK:
    
    
    # Define context for the 'orders' table
    bigquery_table_reference_1 = geminidataanalytics.BigQueryTableReference()
    bigquery_table_reference_1.project_id = "bigquery-public-data"
    bigquery_table_reference_1.dataset_id = "thelook_ecommerce"
    bigquery_table_reference_1.table_id = "orders"
    
    bigquery_table_reference_1.schema = geminidataanalytics.Schema()
    bigquery_table_reference_1.schema.description = "Data for orders in The Look, a fictitious ecommerce store."
    bigquery_table_reference_1.schema.synonyms = ["sales"]
    bigquery_table_reference_1.schema.tags = ["sale", "order", "sales_order"]
    bigquery_table_reference_1.schema.fields = [
        geminidataanalytics.Field(
            name="status",
            description="The current status of the order.",
        ),
        geminidataanalytics.Field(
            name="num_of_items",
            description="The number of items in the order."
        )
    ]
    
    # Define context for the 'users' table
    bigquery_table_reference_2 = geminidataanalytics.BigQueryTableReference()
    bigquery_table_reference_2.project_id = "bigquery-public-data"
    bigquery_table_reference_2.dataset_id = "thelook_ecommerce"
    bigquery_table_reference_2.table_id = "users"
    
    bigquery_table_reference_2.schema = geminidataanalytics.Schema()
    bigquery_table_reference_2.schema.description = "Data for users in The Look, a fictitious ecommerce store."
    bigquery_table_reference_2.schema.synonyms = ["customers"]
    bigquery_table_reference_2.schema.tags = ["user", "customer", "buyer"]
    bigquery_table_reference_2.schema.fields = [
        geminidataanalytics.Field(
            name="first_name",
            description="The first name of the user.",
            tags=["person"],
        ),
        geminidataanalytics.Field(
            name="last_name",
            description="The last name of the user.",
            tags=["person"],
        ),
        geminidataanalytics.Field(
            name="age_group",
            description="The age demographic group of the user.",
        ),
        geminidataanalytics.Field(
            name="email",
            description="The email address of the user.",
            tags=["contact"],
        )
    ]
    
    # Define example queries
    example_queries = [
      geminidataanalytics.ExampleQuery(
          natural_language_question="How many orders are there?",
          sql_query="SELECT COUNT(*) FROM `bigquery-public-data.thelook_ecommerce.orders`",
      ),
      geminidataanalytics.ExampleQuery(
          natural_language_question="How many orders were shipped?",
          sql_query="SELECT COUNT(*) FROM `bigquery-public-data.thelook_ecommerce.orders` WHERE status = 'shipped'",
      ),
      geminidataanalytics.ExampleQuery(
          natural_language_question="How many unique customers are there?",
          sql_query="SELECT COUNT(DISTINCT id) FROM `bigquery-public-data.thelook_ecommerce.users`",
      ),
      geminidataanalytics.ExampleQuery(
          natural_language_question="How many users in the 25-34 age group have a cymbalgroup email address?",
          sql_query="SELECT COUNT(DISTINCT id) FROM `bigquery-public-data.thelook_ecommerce.users` WHERE users.age_group = '25-34' AND users.email LIKE '%@cymbalgroup.com'",
      )
    ]
    

### Example: System instructions

The following system instructions supplement structured context by defining the agent's persona and providing guidance that's not supported by structured fields, such as relationship definitions, glossary terms, additional descriptions, and supplemental `orders` table details. In this example, because the `users` table is fully defined with structured context, it doesn't need to be redefined in the system instructions.
    
    
    -   system_instruction: >-
        You are an expert sales analyst for a fictitious ecommerce store. You will answer questions about sales, orders, and customer data. Your responses should be concise and data-driven.
    -   tables:
        -   table:
            -   name: bigquery-public-data.thelook_ecommerce.orders
            -   fields:
                -   field:
                    -   name: num_of_items
                    -   aggregations: 'sum, avg'
    -   relationships:
        -   relationship:
            -   name: orders_to_user
            -   description: >-
                Connects customer order data to user information with the user_id and id fields.
            - relationship_type: many-to-one
            - join_type: left
            - left_table: bigquery-public-data.thelook_ecommerce.orders
            - right_table: bigquery-public-data.thelook_ecommerce.users
            - relationship_columns:
                - left_column: user_id
                - right_column: id
    - glossaries:
        - glossary:
            - term: complete
            - description: Represents an order status where the order has been completed.
            - synonyms: 'finish, done, fulfilled'
        - glossary:
            - term: OMPF
            - description: Order Management and Product Fulfillment
    - additional_descriptions:
        - text: All the sales data pertains to The Look, a fictitious ecommerce store.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

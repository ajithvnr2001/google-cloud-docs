---
url: https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/context-sets-overview/
title: Context sets overview \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:53:00.660594+00:00
---

# Context sets overview  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/context-sets-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Context sets overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A context set is a collection of database-specific information that enables tools such as QueryData to generate queries with high accuracy. Context sets can include templates, facets, and value searches that help QueryData understand your database schema and the business logic of your applications.

The following databases are supported:

  * AlloyDB for PostgreSQL
  * Cloud SQL for MySQL
  * Cloud SQL for PostgreSQL
  * Spanner
  * Firestore with MongoDB compatibility



## What are context sets

To build effective agentic applications, tools such as QueryData must understand your data organization and business logic. You provide this information in the form of a context set.

You define context in files that contain JSON objects for each context type. You can author these context files with the help of the [context engineering agent](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli). You then upload the context file to a context set that you create in the Google Cloud console. This process enables tools such as QueryData to learn the specific schema of the database and business logic of the application.

The context file looks similar to the following:
    
    
    {
      "templates": [
        {
          "nl_query": "Count prague loan accounts",
          "sql": "db.accounts.countDocuments({ \"district.region\": \"Prague\", \"loans\": { $exists: true, $not: { $size: 0 } }});",
          "intent": "How many accounts associated with loans are located in the Prague region?",
          "manifest": "How many accounts associated with loans are located in a given city?",
          "parameterized": {
            "parameterized_intent": "How many accounts associated with loans are located in $1",
            "parameterized_sql": "db.accounts.countDocuments({ \"district.region\": $1, \"loans\": { $exists: true, $not: { $size: 0 } }});",
          }
        }
      ],
      "facets": [
        {
          "sql_snippet": "\"district.average_salary\": { $gt: 6000, $lt: 10000 }",
          "intent": "Average salary between 6000 and 10000",
          "manifest": "Average salary between a given number and a given number",
          "parameterized": {
             "parameterized_intent": "Average salary between $1 and $2",
             "parameterized_sql_snippet": "\"district.average_salary\": { $gt: $1, $lt: $2 }"
          }
        }
      ],
      "value_searches": [
        {
          "query": "db.airports.aggregate([{ '$match': { 'iata': $value } }, { '$project': { 'value': '$iata', 'columns': 'airports.iata', 'concept_type': 'Airport IATA Code', 'distance': 0, 'context': '', '_id': 0 } }, { '$limit': 1 }])",
          "concept_type": "Airport IATA Code",
          "description": "Exact match (standard MQL) for 3-letter airport codes"
        },
        {
          "query": "db.airports.aggregate([{ '$match': { 'name': { '$regex': $value, '$options': 'i' } } }, { '$project': { 'value': '$name', 'columns': 'airports.name', 'concept_type': 'Airport Name', 'distance': 0, 'context': '', '_id': 0 } }, { '$limit': 1 }])",
          "concept_type": "Airport Name",
          "description": "Regex match for partial airport names"
        },
        {
          "query": "db.products.aggregate([{ '$match': { '$text': { '$search': $value } } }, { '$project': { 'value': '$name', 'columns': 'airports.name', 'concept_type': 'Airport Name', 'distance': { '$meta': 'textScore' }, 'context': '', '_id': 0 } }, { '$sort': { 'distance': -1 } }, { '$limit': 1 }])",
          "concept_type": "Airport Name",
          "description": "Full-text search for airport names"
        }
      ]
    }
    

## Context set file format

A context set file consists of a curated set of templates, facets, and value searches in JSON format that guide tools such as QueryData in translating natural language questions into queries for a specific database. Defining context ensures high-accuracy MongoDB-compatible Query Language (MQL) generation for common query patterns.

To maximize accuracy, ensure that the context set is accurate and comprehensive in its coverage of expected application queries.

Context sets can be created in the `us-central1`, `us-east1`, `europe-west4`, and `asia-southeast1` regions.

### Query templates

Query templates are a curated set of representative natural language questions with corresponding MQL queries. They also include explanations to provide a declarative rationale for the natural language-to-MQL generation.

A query template object looks similar to the following:
    
    
    {
      "templates": [
        {
          "nl_query": "Count prague loan accounts",
          "sql": "db.accounts.countDocuments({ \"district.region\": \"Prague\", \"loans\": { $exists: true, $not: { $size: 0 } }});",
          "intent": "How many accounts associated with loans are located in the Prague region?",
          "manifest": "How many accounts associated with loans are located in a given city?",
          "parameterized": {
            "parameterized_intent": "How many accounts associated with loans are located in $1",
            "parameterized_sql": "db.accounts.countDocuments({ \"district.region\": $1, \"loans\": { $exists: true, $not: { $size: 0 } }});"
          }
        }
      ],
      ...
    }
    

The main components of the query template JSON object are as follows:

  * `nl_query`: An example of a natural language query that tools such as QueryData handle.
  * `sql`: The MQL query for the natural language query. In spite of the name of the `sql` key, this contains MQL.
  * `intent`: The goal or purpose of the natural language query. If not set, this value defaults to the natural language query.
  * `manifest`: A generalized, auto-generated form of the intent.
  * `parameterized_intent`: A templated, auto-generated form of the intent, with entity values replaced by parameters.
  * `parameterized_sql`: A templated, auto-generated form of the MQL query that corresponds to the parameterized intent. In spite of the name of the `parameterized_sql` key, this contains MQL.



### Query facets

Query facets are a curated set of representative natural language conditions with corresponding MQL predicates. Facets manage filtering and conditions, which enables query templates to perform faceted searches.

A query facet object looks similar to the following:
    
    
    {
      ...
      "facets": [
        {
          "sql_snippet": "\"district.average_salary\": { $gt: 6000, $lt: 10000 }",
          "intent": "Average salary between 6000 and 10000",
          "manifest": "Average salary between a given number and a given number",
          "parameterized": {
             "parameterized_intent": "Average salary between $1 and $2",
             "parameterized_sql_snippet": "\"district.average_salary\": { $gt: $1, $lt: $2 }"
          }
        }
      ]
    }
    

The main components of the facet JSON object are as follows:

  * `sql_snippet`: A MQL snippet. In spite of the name of the `sql_snippet` key, this contains MQL. To avoid ambiguity, qualify field names with document names (for example, `doc_name.field_name`). 
  * `intent`: An explanation of the MQL predicate.
  * `manifest`: A generalized, auto-generated form of the intent.
  * `parameterized_intent`: A templated, auto-generated form of the intent, with entity values replaced by parameters.
  * `parameterized_sql_snippet`: A templated, auto-generated form of the sql_snippet that corresponds to the parameterized intent. In spite of the name of the `parameterized_sql_snippet` key, this contains MQL.



### Value search queries

_Value search queries_ are developer-defined queries that use match functions to find values and their context within a database. Value linking uses the results of these queries to identify which tables and columns contain a matching value, understand the value's concept type, and correct misspellings. 

The QueryData API uses value linking to more accurately convert natural language into MQL. By using value search queries, the API can correct misspellings and resolve value types based on database values, thus improving conversion accuracy.

Value linking improves natural language to MQL conversion accuracy. For example, if a user asks, "Are there any flights out of Heathrow?", the database might store the airport name as "London Heathrow". Without value linking, the generated MQL might filter by `{ "name": "Heathrow" }` and return no results. Value search queries guide the agent to map "Heathrow" to the correct database value "London Heathrow" and its schema location (`airports.name`), ensuring that the generated MQL is accurate.

An example value search query is:
    
    
    {
      ...
      "value_searches": [
        {
          "query": "db.airports.aggregate([{ '$match': { 'iata': $value } }, { '$project': { 'value': '$iata', 'columns': 'airports.iata', 'concept_type': 'Airport IATA Code', 'distance': 0, 'context': '', '_id': 0 } }, { '$limit': 1 }])",
          "concept_type": "Airport IATA Code",
          "description": "Exact match (standard MQL) for 3-letter airport codes"
        },
        {
          "query": "db.airports.aggregate([{ '$match': { 'name': { '$regex': $value, '$options': 'i' } } }, { '$project': { 'value': '$name', 'columns': 'airports.name', 'concept_type': 'Airport Name', 'distance': 0, 'context': '', '_id': 0 } }, { '$limit': 1 }])",
          "concept_type": "Airport Name",
          "description": "Regex match for partial airport names"
        },
        {
          "query": "db.products.aggregate([{ '$match': { '$text': { '$search': $value } } }, { '$project': { 'value': '$name', 'columns': 'airports.name', 'concept_type': 'Airport Name', 'distance': { '$meta': 'textScore' }, 'context': '', '_id': 0 } }, { '$sort': { 'distance': -1 } }, { '$limit': 1 }])",
          "concept_type": "Airport Name",
          "description": "Full-text search for airport names"
    
        }
      ]
    }
    

The main components of the value search JSON object are as follows:

  * `query`: A parameterized MQL statement that defines the logic for matching a value phrase against the values stored in a database. The result set typically projects the matched value, the schema location, the concept type, and a normalized distance metric (between 0 and 1).
  * `concept_type`: A semantic label assigned to the value—for example, the `district` or the `loan_status`. This label helps value linking and eventually the tools such as QueryData API to understand the role of the value phrase in the schema. It also helps produce a MQL statement that targets the concept for the value, as well as the table and column where the value phrase appears in.
  * `description`: A description of the search logic.



## Limitations

Context sets have the following limitations:

  * Context sets for databases only supports templates, facets, and value searches.
  * Context sets for databases is only used by the `QueryData` endpoint in the Conversational Analytics API.



## What's next

  * Learn how to [build contexts sets using the context engineering agent](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/build-context-sets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 

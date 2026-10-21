---
url: https://docs.cloud.google.com/bigtable/docs/parameterized-views-overview/
title: Parameterized views overview \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:18.045129+00:00
---

# Parameterized views overview  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/parameterized-views-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Parameterized views overview

In Bigtable, you can use parameterized views to dynamically filter data ranges for [logical views](https://docs.cloud.google.com/bigtable/docs/tables-and-views#logical-views) based on application context. This approach protects your applications from SQL injection and reduces the need for multiple static views.

To handle sensitive information, Bigtable parameterized views use an isolated context that is separate from the SQL query text. Because the database binds these values on the server side, users and AI agents can't manipulate query parameters. The database automatically limits data access to your specific context, regardless of how you write the query.

**Caution:** If untrusted users or LLMs generate the SQL that references a parameterized view, add additional security mitigations for defense-in-depth protection. For example, use [Model Armor](https://cloud.google.com/security/products/model-armor) or predefined query templates through [Agent Development Kit (ADK) function tools](https://adk.dev/tools-custom/function-tools/).

## Benefits of parameterized views

Parameterized views are well suited for managing _data scoping_ at the database level, particularly in applications that process free-form queries translated from natural language. Data scoping is the process of restricting query results to a specific subset of data. These views offer a flexible way to implement the following:

  * **Deep-tier identity propagation** : enforce fine-grained data permissions at the user level, which ensure that users can access only their own data context. For example, an application can ensure that users or tenants retrieve rows that are only within their designated boundary.
  * **Simplified user management** : use a single database role for all database users instead of a separate role for each user.
  * **Parameter isolation** : parameterized views mitigate risks by passing values as isolated context that remains outside of LLM or end-user control. Because these values are kept apart from the query text, a user or an AI agent that generates the query can't manipulate them.
  * **SQL injection mitigation** : when building applications, substituting parameters on the client side within the query text can lead to query manipulation. Parameterized views mitigate this risk by performing parameter binding on the server side after the query structure is parsed. This prevents SQL injection because attacker-controlled values can't change the structure of the query.



For example, consider a health-tracking application that stores patient medical records, including cholesterol levels. If patients query their own data, a malicious or poorly-behaved agent might generate or request a query that attempts to retrieve other patients' records. Using a parameterized view, the application enforces patient isolation at the database level. The view is defined with a `patient_id` view parameter:
    
    
    CREATE VIEW patient_health_pv AS
    (SELECT * FROM patient_health_records WHERE patient_id = CAST(VIEW_PARAMETERS('patient_id') AS BYTES))
    

When the client wants to query a patient's `cholesterol` reading:
    
    
    SELECT readings['value'], readings['date']
    FROM patient_health_pv
    WHERE readings['test_name'] = 'cholesterol'
    

Because the view is queried, Bigtable automatically binds and applies the `patient_id` value from the isolated parameter map. The LLM or end-user has no ability to alter or discard this filter, ensuring robust user-level scoping and eliminating SQL injection vectors.

## How parameterized views work

Parameterized views use a mechanism called _view parameters_ to safely pass application-level context, such as a user ID, to the database. Parameterized views achieve this by passing the view parameter values as a separate, isolated context with the query request. Bigtable can then access this context during query execution, but the query itself can't read or modify the context.

The `VIEW_PARAMETERS()` function is the SQL interface for accessing these parameters within a view definition. For example, to filter data based on the ID of the user who makes the query, you can include the following in your view's `WHERE` clause:
    
    
    CREATE VIEW purchase_history_pv AS
    (SELECT * FROM purchases WHERE user_id = CAST(VIEW_PARAMETERS('user_id') AS BYTES))
    

You can also use `VIEW_PARAMETERS()` to parameterize column qualifiers. This lets the view return specific fields dynamically based on the provided application context.
    
    
    CREATE VIEW specific_test_result_pv AS
    SELECT
      tests[VIEW_PARAMETERS('test_name')] AS reading,
      _timestamp AS reading_time
    FROM patients
    

### Difference from standard query parameters

View parameters operate differently compared to standard query parameters:

  * **Syntax and context** : Standard query parameters are defined using the `@param` syntax and can't be declared inside a view definition, only in a query. View parameters are accessed using the `VIEW_PARAMETERS('key')` function, which can be called in any query or view context.
  * **Fail-closed behavior** : If a view definition that contains a `VIEW_PARAMETERS('key')` reference is queried, but the corresponding value isn't provided in the request's view parameters map, the query immediately fails with a `not found / missing parameter` error. This prevents accidental data exposure if the configuration is misapplied.



## Limitations

The following limitations apply to parameterized views:

  * You can only create parameterized views from logical views. You create a new parameterized logical view using the Google Cloud CLI. You don't modify an existing logical view.
  * View parameters only support values of the string type. If a parameter represents a different data type in your view's SQL definition, you must pass the parameter value as a string and cast it inside the view definition—for example, `CAST(VIEW_PARAMETERS('parameter_name') AS INT64)`.



## What's next

  * [Create and manage parameterized views](https://docs.cloud.google.com/bigtable/docs/create-manage-pvs)
  * [Use parameterized views in agentic applications](https://docs.cloud.google.com/bigtable/docs/use-pvs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

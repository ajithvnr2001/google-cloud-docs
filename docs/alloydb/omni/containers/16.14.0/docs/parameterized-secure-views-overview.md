---
url: https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/parameterized-secure-views-overview/
title: Parameterized secure views overview \u00a0|\u00a0 AlloyDB Omni using containers: 16.14.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:19:00.726440+00:00
---

# Parameterized secure views overview  |  AlloyDB Omni using containers: 16.14.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/parameterized-secure-views-overview/

This page documents AlloyDB Omni version **16.14.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/overview)



Send feedback 

#  Parameterized secure views overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.14.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/parameterized-secure-views-overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/parameterized-secure-views-overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/parameterized-secure-views-overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/parameterized-secure-views-overview)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/parameterized-secure-views-overview)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/parameterized-secure-views-overview)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/parameterized-secure-views-overview)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/parameterized-secure-views-overview)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/parameterized-secure-views-overview)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/parameterized-secure-views-overview)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/parameterized-secure-views-overview)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/parameterized-secure-views-overview)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/parameterized-secure-views-overview)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/parameterized-secure-views-overview)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/parameterized-secure-views-overview)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/parameterized-secure-views-overview)



**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes parameterized secure views in AlloyDB Omni, which provide application data security and row access control using SQL views and help ensure that application users can view only the data that they're supposed to access.

Parameterized secure views are an extension of [PostgreSQL secure views](https://www.postgresql.org/docs/current/tutorial-views.html), which let you use application-specific named view parameters in view definitions. This capability provides an interface that takes a query and values for the named parameters. The interface executes the query with those values, which are used throughout the execution of the query.

The following is an example of a parameterized secure view:
    
    
    CREATE VIEW secure_checked_items WITH (security_barrier) AS
           SELECT bag_id, timestamp, location
           FROM checked_items t
           WHERE customer_id = $@app_end_userid;
    

You can query parameterized secure views using the `execute_parameterized_query` stored procedure, or by running the `EXECUTE .. WITH VIEW PARAMETERS` statement. For more information, see [Manage application data security using AlloyDB Omni parameterized secure views](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/manage-application-data-security-parameterized-secure-views).

## Benefits of parameterized secure views

Parameterized secure views are well suited for managing data security at the database level, especially when you're dealing with ad hoc queries from untrusted sources, such as those translated from natural language. These views offer a flexible way to implement fine-grained access control.

For example, consider an application that tracks customers' checked-in luggage. A customer with user ID 12345 asks, "Where is my bag?" In this scenario, parameterized secure views ensure the following:

The query only returns rows accessible to the user who submitted the query—for example, rows linked to user ID 12345.

### Security risk mitigation

Parameterized secure views help mitigate security risks when end users run untrusted queries—like natural language queries—on your database. These risks include the following:

  * **Malicious prompts** : Users might try to manipulate the underlying model to access all application data.
  * **Broadly-scoped SQL queries** : Large language models (LLMs) might generate SQL queries that expose sensitive data, even from well-intentioned user queries.



By using parameterized secure views, you can restrict the range of rows available to individual application users. This control ensures data security, regardless of how users phrase their queries.

### Data access management

Parameterized secure views address common challenges in managing data access for a large and growing number of users.

  * **Simplified user management** : With parameterized secure views, you can use a single database role to serve all end users, instead of using methods that might require you to create a separate database user or role for each end user. Parameterized secure views help simplify user and connection management for applications where each end user needs access only to their data. For example, in an airline application where customers should only see their own bookings, you can define a single parameterized secure view that is parameterized by the end user identifier. This view allows a single database role –with access to the view, not the underlying table– to serve all users, which simplifies user management and database connections.
  * **Streamlined security enforcement** : Parameterized secure views inherently incorporate access controls. When a view is queried, the defined security parameters are consistently enforced, regardless of the user accessing the view. This approach contrasts with situations where underlying security policies on base tables might not automatically apply to views without extra configuration.



For more information about existing security mechanisms in PostgreSQL, such as Row Level Security (RLS) Policies, see [Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html).

### Security mechanism

Parameterized secure views add an extra layer of security by controlling how queries access the underlying data. They give application developers data security and row access control using the following methods:

  * Views created using the [`WITH (security barrier)`](https://www.postgresql.org/docs/current/rules-privileges.html) option provide row-level security by preventing maliciously chosen functions and operators from being passed values from rows until after the view has done its work. For more information about the `WITH (security barrier)` clause, see [Rules and Privileges](https://www.postgresql.org/docs/current/rules-privileges.html).
  * Parameterization using named view parameters allows a restricted view of the database parameterized by values provided by the application based on application-level security, such as end user authentication.
  * Enforcement of additional restrictions on queries accessing parameterized views is useful for applications that execute untrusted queries from end users—like those generated by an AI natural language-to-SQL generation. This prevents escaping the security envelope provided by parameterized secure views and managing resource usage. For more information, see [Enforced restrictions on queries](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/manage-application-data-security-parameterized-secure-views#restrictions).



## Limitations

  * You must enable the parameterized view flag separately on every instance of AlloyDB Omni. Parameterized view objects created on the primary instance are propagated to read pool instances and cross-region replicas. However, the `parameterized_views.enabled` flag setting isn't applied automatically and must be set manually on each instance. For more information, see [Before you begin](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/manage-application-data-security-parameterized-secure-views#before-you-begin). You can't query parameterized views on a read pool instance or on a cross-region replica before you enable the `parameterized_views.enabled` flag on each instance.



## What's next

  * [Manage application data security using parameterized secure views](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/manage-application-data-security-parameterized-secure-views).
  * [Secure and control access to application data using parameterized secure views](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/secure-app-data-parameterized-secure-views).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 

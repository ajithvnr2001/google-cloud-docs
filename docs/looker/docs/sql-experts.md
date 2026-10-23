---
url: https://docs.cloud.google.com/looker/docs/sql-experts/
title: LookML for SQL experts \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:14.892032+00:00
---

# LookML for SQL experts  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/sql-experts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  LookML for SQL experts Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides a focused introduction to LookML, Looker's modeling language, and is specifically intended for those who are already proficient in SQL.

LookML lets you define SQL logic in a structured and reusable way. From the SQL fragments defined in your LookML, Looker assembles relevant SQL statements. Once you've set up your LookML model and connected Looker to your database, Looker automatically generates the necessary SQL queries to retrieve data from your database.

Because you use LookML to define your SQL, you don't need to repeat SQL logic in multiple places. LookML helps you adhere to the "Don't Repeat Yourself (DRY)" principle, a key concept in programming that promotes code reusability and reduces errors. For example, imagine that you need to decode transaction codes by using a SQL `CASE` statement across multiple queries. Instead of declaring the `CASE` statement in multiple queries, you can define it once in LookML and reuse it throughout your data model.

In this guide, you'll deconstruct SQL queries and reassemble them into reusable LookML elements such as dimensions, measures, views, and Explores.

The following pages explain LookML elements by using concepts familiar to SQL experts:

  * [SQL concepts for views](https://docs.cloud.google.com/looker/docs/sql-experts-view): Define and customize LookML views, which are based on database tables, and map your SQL fields to LookML dimensions and measures.
  * [SQL concepts for joins](https://docs.cloud.google.com/looker/docs/sql-experts-joins): Define and customize joins between views in LookML to mirror SQL join logic, and manage relationships between tables to avoid data duplication.
  * [SQL concepts for derived tables](https://docs.cloud.google.com/looker/docs/sql-experts-derived-tables): Define and customize derived tables in LookML by using either SQL or LookML's built-in syntax to define and reuse complex data logic without repeating yourself.



## Related resources

  * [[Hands-On Lab] Writing LookML as a SQL Expert](https://www.skills.google/focuses/128087?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=52304560)
  * [[Community article] Using Looker's SQL Generator](https://www.googlecloudcommunity.com/gc/Technical-Tips-Tricks/Using-Looker-s-SQL-Generator/ta-p/814623)
  * [How Looker generates SQL](https://docs.cloud.google.com/looker/docs/how-looker-generates-sql)
  * [Looker cookbook: Maximizing code reusability with DRY LookML](https://docs.cloud.google.com/looker/docs/best-practices/dry-lookml-cookbook)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

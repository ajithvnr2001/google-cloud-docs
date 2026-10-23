---
url: https://docs.cloud.google.com/looker/docs/using-time-zone-settings/
title: Using time zone settings \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:13.365154+00:00
---

# Using time zone settings  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/using-time-zone-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Using time zone settings Stay organized with collections  Save and categorize content based on your preferences. 

Looker can make time-based data easier to understand by converting it to different time zones. Users can see query results and create filters with time-based data that is converted to their local time zones. For example, a user in New York viewing data created in California doesn't have to manually subtract three hours to filter or interpret their queries.

Looker converts time-based data when it [generates SQL](https://docs.cloud.google.com/looker/docs/how-looker-generates-sql) during a query for a Look, an Explore, or a dashboard. The underlying data is not affected; rather, the query results are converted using Looker's time zone settings. This also means that queries run using [SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics#running_queries_in_sql_runner) do not convert time-based data.

Several settings within Looker specify how to convert time-based data:

  * **System time zone**
  * **Database Time Zone**
  * **User Specific Time Zones**
  * **Application Time Zone**
  * **Query Time Zone**
  * **`convert_tz` LookML parameter**
  * **`sql` LookML parameter**



## System time zone

The system time zone is the time zone for which the server running Looker is configured. Looker's internal database, which stores the information available in the [System Activity](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores) Explores, stores time-based data in the system time zone.

The system time zone is not configurable through the Looker application. For Looker-hosted instances, the system time zone is always set to UTC. Customer-hosted instances may be in a different system time zone. Changing the system time zone is not trivial and is not recommended.

If you need to adjust timestamps in a System Activity Explore, use [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) to create time-adjusted columns. For example, to convert from UTC to EST, you could create a column with the table calculation `add_hours(-5, ${time})`.

Note that because table calculations are performed after query results are returned, they cannot be used to group or pivot data by specific time components (such as hour of day or day of the week). To adjust System Activity timestamps for visualizations that require pivoting or grouping by time components, use [custom dimensions](https://docs.cloud.google.com/looker/docs/custom-fields#creating_a_custom_dimension_using_a_looker_expression) instead. Custom dimensions are processed before the visualization, which allows for proper grouping. For example, to adjust data from UTC to GMT-3, you would first create a custom dimension for the adjusted time by using the Looker expression `add_hours(-3, ${user_facts.last_ui_login_hour})`. You would then create subsequent custom dimensions to extract the required weekday or hour based on that adjusted time field.

## Database Time Zone

When you [add a connection to a database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db), you set the value for the **Database Time Zone** on the [**Connection Settings**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections#connection_settings) page.

This setting represents the time zone that your database is in, which is typically [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Setting this value to anything other than the time zone that your database is in may lead to unexpected results.

## User Specific Time Zones

The most significant setting for time-based data conversion is the **User Specific Time Zones** option, which is on the [**General Settings**](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings) page in the **Admin** section of Looker.

You can enable or disable **User Specific Time Zones** :

  * When enabled, each Looker user is assigned to a time zone, and that time zone specifies the appearance of their query results.
  * When disabled, users don't have individual time zones assigned to their accounts. Rather, all queries run using the **Query Time Zone** value.



With **User Specific Time Zones** enabled, a user can set their time zone on their [**Account**](https://docs.cloud.google.com/looker/docs/user-account#profile_section) page, or Looker admins can assign time zones to users on the [**Users**](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#timezone) page. If a time zone isn't set for a user, their account defaults to the Looker **Application Time Zone** setting.

Whenever a user creates a query, that query is created in the user's time zone. As a result, when a query returns time-based data, Looker converts the data from the **Database Time Zone** to the user's time zone. When a user uses time-related filter values in a query, Looker converts the filter values to the **Database Time Zone**.

In addition, when you enable this option, Looker displays a **Time Zone** drop-down menu in [Explores](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#the_explore_page) and [Looks](https://docs.cloud.google.com/looker/docs/viewing-looks#choosing_timezones).

![](https://docs.cloud.google.com/static/looker/docs/images/admin-time-zone-dropdown-2308.png)

Options in this drop-down are:

  * **Each Tile's Time Zone (dashboards only):** All queries run in the time zone they were saved with.
  * **Viewer Time Zone** : All queries run in the user's current time zone setting.
  * A list of every individual time zone, which users may manually choose if they like.



All queries default to the time zone the query was created with. In other words, if Alice creates a query with time zone "America/Los Angeles" and sends it to Bob, Bob will see the query with time zone "America/Los Angeles," even if Bob's time zone is set to "America/New York." Similarly, drilling always defaults to whatever time zone the query was created with.

Whenever viewing a query, users can use the drop-down to override the time zone, picking their **Viewer Time Zone** or any different time zone for that query or that dashboard's set of queries.

### Things to consider with User Specific Time Zones

When you enable **User Specific Time Zones** , users in different time zones may see data differently.

For example, the exact hours making up the time period `last month` would differ between time zones, so users may see different data values if they are in different time zones but are both filtering on `last month`.

## Application Time Zone

The **Application Time Zone** setting can be configured on the [**General Settings**](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings) page in the **Admin** section of Looker.

The **Application Time Zone** is the default time zone for [content deliveries](https://docs.cloud.google.com/looker/docs/scheduling). The time zone used for content deliveries does not affect time-based data returned by a query; it affects only the time a data delivery is sent.

If you enable the **User Specific Time Zones** option, the **Application Time Zone** is the default time zone for users that do not have a time zone value set for their accounts.

## Query Time Zone

The **Query Time Zone** option is displayed only if you have disabled **User Specific Time Zones**. In that case, you set the **Query Time Zone** value when you [add a connection to a database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) on the [**Connection Settings**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections#connection_settings) page.

If you disable **User Specific Time Zones,** all queries of time-based data use the **Query Time Zone** and Looker converts all time-based data from the **Database Time Zone** to the **Query Time Zone**.

## `convert_tz` LookML parameter

Looker does time zone conversion by default. To disable time zone conversion for an individual field, you can use the `convert_tz` LookML parameter. For example:
    
    
    dimension_group: created {
      type: time
      timeframes: [time, date]
      convert_tz: no
    }
    

For more information, see the [`convert_tz`](https://docs.cloud.google.com/looker/docs/reference/param-field-convert-tz) parameter documentation page.

## `sql` LookML parameter

You can also manually define time zone conversion using your database dialect's functions within the [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter in a LookML dimension. For example, to manually define time zone conversion in MySQL, you could use the following LookML:
    
    
    dimension_group: created {
     type: time
     timeframes: [time, date]
     sql: CONVERT_TZ(${TABLE}.created_at,'UTC','PST') ;;
    }
    

### MySQL dialect notes

MySQL requires a time zone table before its time zone conversion function will work. This can be run by an admin. You can read more in the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/time-zone-support.html).

### Postgres dialect notes

Looker uses the driver setting to select the target time zone. This may affect how queries are processed in SQL Runner as compared with pgAdmin, because Looker will use the current datetime in the time zone selected.

## Database dialect support for time zone conversion

For Looker to convert time zones in your Looker project, your database dialect must support time zone conversion. The following table shows which dialects support time zone conversion in the latest release of Looker:

Dialect | Supported?  
---|---  
Actian Avalanche|   
Amazon Athena|   
Amazon Aurora MySQL|   
Amazon Redshift|   
Amazon Redshift 2.1+|   
Amazon Redshift Serverless 2.1+|   
Apache Druid|   
Apache Druid 0.13.x - 0.17.x|   
Apache Druid 0.18+|   
Apache Hive 2.3+|   
Apache Hive 3.1.2+|   
Apache Spark 3+|   
ClickHouse|   
ClickHouse 26+|   
Cloudera Impala 3.1+|   
Cloudera Impala 3.1+ with Native Driver|   
Cloudera Impala with Native Driver|   
DataVirtuality|   
Databricks|   
Denodo 7|   
Denodo 8 & 9|   
Dremio|   
Dremio 11+|   
Dremio 26+ with Arrow Flight SQL|   
Exasol|   
Google BigQuery Legacy SQL|   
Google BigQuery Standard SQL|   
Google Cloud AlloyDB for PostgreSQL|   
Google Cloud PostgreSQL|   
Google Cloud SQL|   
Google Spanner|   
Greenplum|   
HyperSQL|   
IBM Netezza|   
MariaDB|   
Microsoft Azure PostgreSQL|   
Microsoft Azure SQL Database|   
Microsoft Azure Synapse Analytics|   
Microsoft SQL Server 2008+|   
Microsoft SQL Server 2012+|   
Microsoft SQL Server 2016|   
Microsoft SQL Server 2017+|   
MongoBI|   
MongoSQL|   
MySQL|   
MySQL 8.0.12+|   
Oracle|   
Oracle ADWC|   
PostgreSQL 9.5+|   
PostgreSQL pre-9.5|   
PrestoDB|   
PrestoSQL|   
SAP HANA|   
SAP HANA 2+|   
SingleStore|   
SingleStore 7+|   
Snowflake|   
Teradata|   
Trino|   
Vector|   
Vertica|   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

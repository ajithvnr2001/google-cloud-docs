---
url: https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types/
title: Dimension, filter, and parameter types \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:40.174128+00:00
---

# Dimension, filter, and parameter types  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  Dimension, filter, and parameter types Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `type` parameter that is part of a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) or [filter](https://docs.cloud.google.com/looker/docs/reference/param-field-filter).
> 
> `type` can also be used as part of a measure, described on the [Measure types](https://docs.cloud.google.com/looker/docs/reference/param-measure-types) documentation page.
> 
> `type` can also be used as part of a dimension group, described on the [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) parameter documentation page.

## Usage
    
    
    view: view_name {
      dimension: field_name {
        type: field_type
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `type` |  Possible Field Types Dimension, Filter, Parameter Default Value `string` Accepts [A dimension, filter, or parameter type](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#type_definitions)  
---|---  
  
This page includes additional details about the various types that can be assigned to a [`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension), [`filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-filter), or [`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter). A dimension, filter, or parameter can only have one type, which defaults to `string` if no type is specified.

Some types have supporting parameters, which are described within the appropriate section.

## Type definitions

D = Dimension 

DG = Dimension group 

F = Filter 

P = Parameter 

Type | Description | Valid Field Types  
---|---|---  
`bin` |  Added 21.14  For fields that group numerical values into several ranges | D  
`custom_calendar` | Used with a [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) to create several duration-based custom calendar dimensions from a single table column. For information about dimension groups, see the [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) parameter documentation page. | DG  
`date` | For fields that contain dates | D F P  
`date_time` | For fields that contain dates and times | D F P  
`distance` | For fields that calculate the distance of the most direct path ("as the crow flies") between two `type: location` dimensions | D  
`duration` | Used with a [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) to create several duration-based dimensions from a single table column. For information about dimension groups, see the [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) parameter documentation page. | DG  
`location` | For fields that are based on a latitude and longitude and will be used in visualizations | D  
`number` | For fields that contain numbers | D F P  
`string` | For fields that contain letters or special characters | D F P  
`tier` | For fields that group numerical values into several ranges | D  
`time` | Used with a [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) to create several time-based dimensions from a single table column. For information about dimension groups, see the [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) parameter documentation page. | DG  
`unquoted` | For [`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter) fields whose values will be inserted directly into SQL, and therefore shouldn't be quoted (as they would with `type: string`) | P  
`yesno` | For fields that show if something is true or false | D F P  
`zipcode` | For fields that contain a zip code and will be used in visualizations | D  
Individual Time and Date Types | A rarely used alternative to `type: time` for creating single, time-based dimensions | D F  
Individual Duration Types | A rarely used alternative to `type: duration` for creating single time-based dimensions that calculate time differences | D  
`int` |  Removed 5.4  Replaced by `type: number` | D  
  
## `bin`

> `type: bin` is an alias for `type: tier`. The two types can be used interchangeably.

`type: bin` is used in conjunction with the `bins` parameter to separate a numeric dimension into a set of number ranges. For example, you might bin an age dimension into different age ranges. You can change how the bins appear in the Looker UI with the `style` parameter.

The usage pattern is:
    
    
    view: view_name {
      dimension: field_name {
        type: bin
        bins: [numeric_value, numeric_value, ... ]
        style: interval
        sql: ${my_field_name} ;;
      }
    }
    

The [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter for `type: bin` dimensions can take any valid SQL expression that results in a number or an integer.

An example using age might look like this:
    
    
    dimension: age_bin {
      type: bin
      bins: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
      style: interval
      sql: ${age} ;;
    }
    

The way that this would appear in the Looker UI is described in the `style` section for the `type: tier` parameter on this page.

The `bin` type is an alias for `type: tier`. The two types can be used interchangeably, and the behavior is the same for both: 

  * The `style` subparameter is used to customize the appearance of bins in the Looker UI.
  * `Dimensions of type: bin` cannot be used in [custom filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom_filters).
  * Using `type: bin` in conjunction with [dimension fill](https://docs.cloud.google.com/looker/docs/creating-visualizations#filling_in_missing_dates_and_values) can result in unexpected tier buckets.



## `distance`

`type: distance` is used to calculate the distance of the most direct path ("as the crow flies") between two `type: location` dimensions.

The [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter for `type: distance` dimensions is excluded. Instead, you supply a reference to a `type: location` dimension in the `start_location_field` and `end_location_field` parameters.

The usage is:
    
    
    view: view_name {
      dimension: field_name {
        type: distance
        start_location_field: field_name_1
        end_location_field: field_name_2
        units: kilometers
      }
    }
    

The unit of distance is determined by the `units` parameter, which can take the following values:

  * `feet`
  * `kilometers`
  * `meters`
  * `miles`
  * `nautical_miles`
  * `yards`



For example, you might calculate the distance traveled by a customer to pickup a rental like this:
    
    
    dimension: distance_to_pickup {
      type: distance
      start_location_field: customer.home_location
      end_location_field: rental.pickup_location
      units: miles
    }
    

The distance calculated will be the most direct path between the two points, not necessarily the distance traveled by road.

Don't use the [`${view_name.field_name}`](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#substitution_operator_\($\)) syntax in the `start_location_field` and `end_location_field` parameters. Instead, use the view name and field name by themselves, like `view_name.field_name`.

## `custom_calendar`

`type: custom_calendar` is used in conjunction with a [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) to create a set of calculated time differences between dimensions and/or SQL expressions that are based on [custom calendars](https://docs.cloud.google.com/looker/docs/custom-calendars).

`type: custom_calendar` works only with a `dimension_group` and will _not_ work with a regular [`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension).

For information about dimension groups with `type: custom_calendar`, see the [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#custom_calendar_type) parameter documentation page.

## `duration`

`type: duration` is used in conjunction with a [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) to create a set of calculated time differences between dimensions and/or SQL expressions.

`type: duration` works only with a `dimension_group` and will _not_ work with a regular [`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension). However, you can specify individual duration-based dimensions, as explained in Individual duration types.

For information about dimension groups with `type: duration`, see the [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#duration_type) parameter documentation page.

## `location`

`type: location` is used in conjunction with the `sql_latitude` and `sql_longitude` parameters to create coordinates that you want to plot on a [Map](https://docs.cloud.google.com/looker/docs/map-options) or [Static Map (Points)](https://docs.cloud.google.com/looker/docs/map-points-options) visualization (use a state or country field for [Static Map (Regions)](https://docs.cloud.google.com/looker/docs/map-regions-options)), or that you want to use in a `type: distance` calculation.

The usage pattern is:
    
    
    view: view_name {
      dimension: field_name {
        type: location
        sql_latitude:${field_name_1} ;;
        sql_longitude:${field_name_2} ;;
      }
    }
    

The [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter for `type: location` dimensions is excluded. Instead, you supply any valid SQL expression that results in a decimal latitude or longitude to the `sql_latitude` and `sql_longitude` parameters. These are usually references to LookML fields that contain latitude or longitude information, but they can be static values if you wanted to have a location of your headquarters, or something along those lines.

For example, you might create a `store_location` dimension like this:
    
    
    dimension: store_location {
      type: location
      sql_latitude: ${store_latitude} ;;
      sql_longitude: ${store_longitude} ;;
    }
    

If you don't want to plot the locations or calculate distances, you can use a simpler field type such as `type: number`. When you view a location in a table, Looker will show the value from your database, as well as automatically generate a link to that location in Google Maps.

**Note:** If the underlying database columns for the fields that are referenced in `sql_latitude` and `sql_longitude` contain non-numeric string values (such as `NA`), Looker's location dimension processing will fail, and the Explore page will display the error `The server encountered an error processing result data`. You can resolve error this by modifying the LookML definitions for those latitude and longitude dimensions to filter out or handle non-numeric values (such as replacing `NA` with `NULL` or a default numeric value like `0.0`). See the following example:
    
    
    dimension: latitude {
    type: string
    sql: CASE WHEN ${TABLE}.latitude = 'NA'
            THEN NULL
              ELSE ${TABLE}.latitude END ;;
    }
    

### Supported database dialects for `location`

For Looker to support `type: location` in your Looker project, your database dialect must also support it. The following table shows which dialects support `type: location` in the latest release of Looker:

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
  
## `number`

`type: number` is used with numbers or integers.

The [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter for `type: number` dimensions can take any valid SQL expression that results in a number or an integer.

`type: number` fields can be formatted by using the [`value_format`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format) or [`value_format_name`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format-name) parameters.

For example, the following LookML creates a field called `profit` based on the `revenue` and `cost` fields, then displays it in a money format ($1,234.56):
    
    
    dimension: profit {
      type: number
      sql: ${revenue} - ${cost} ;;
      value_format_name: usd
    }
    

A dimension can perform arithmetic only on other dimensions, not measures.

When a dimension of `type: number` is used in a filter, the filter doesn't provide suggestions to users, even when the dimension displays ID numbers. Floating-point numbers specifically have limited support in filter suggestion picklists. As a workaround, change the dimension `type` from `number` to `string`. If this does not resolve the issue, explicitly cast the value to a string within the `sql` parameter (for example, `sql: STRING(${TABLE}.column_name) ;;`). If the dimension must remain a `number` for calculations or sorting, create a separate dimension of `type: string` to use for dashboard filters.

## `string`

`type: string` is typically used with fields that contain letters or special characters. It can be used with number fields as well, although Looker has better features for handling numbers if you use `type: number` instead.

The [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter for `type: string` dimensions can take any valid SQL expression.

For example, the following LookML creates the field `full_name` by combining a field called `first_name` and `last_name`:
    
    
    dimension: full_name {
      type: string
      sql: CONCAT(${first_name}, ' ', ${last_name}) ;;
    }
    

In this example `type: string` could be omitted, because `string` is the default value for `type`.

## `tier`

> You can use `type: bin` as an alias for `type: tier`. The two types can be used interchangeably.

`type: tier` is used in conjunction with the `tiers` parameter to separate a numeric dimension into a set of number ranges. For example, you might tier an age dimension into different age ranges. You can change how the tiers appear in the Looker UI with the `style` parameter.

The usage pattern is:
    
    
    view: view_name {
      dimension: field_name {
        type: tier
        tiers: [numeric_value, numeric_value, ... ]
        style: interval
        sql: ${my_field_name} ;;
      }
    }
    

The [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter for `type: tier` dimensions can take any valid SQL expression that results in a number or an integer.

An age example might look like this:
    
    
    dimension: age_tier {
      type: tier
      tiers: [0, 10, 20, 30, 40, 50, 60, 70, 80]
      style: classic # the default value, could be excluded
      sql: ${age} ;;
    }
    

The way that this would appear in the Looker UI is described in the `style` section on this page.

> Dimensions of `type: tier` cannot be used in [custom filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom_filters).

### `style`

The `style` parameter lets you change the way that tiers appear in the Looker UI. Although not shown in the examples in the following sections, if there were negative numbers in the data, there would be a beginning tier that would include all numbers from negative infinity up to but not including 0. There are four possible values:

  * `classic` (the default value)
  * `interval`
  * `integer`
  * `relational`



#### `classic`

`style: classic` is the default, and looks like:

Users Age Tier (Classic) | Users Count  
---|---  
T02 [10,20) | 949  
T03 [20,30) | 2,161  
T04 [30,40) | 2,114  
T05 [40,50) | 2,081  
T06 [50,60) | 2,024  
T07 [60,70) | 1,511  
T08 [70,inf) | 1,450  
  
  * You can interpret this tier notation as follows:
    * **T02 [10,20)** is the range including 10, and up to but not including 20
    * **T09 [80,inf)** is the range including 80, and up to infinity



#### `interval`

`style: interval` is similar to `style: classic`, but it doesn't have the leading **TXX** labels. It looks like:

Users Age Tier (Interval) | Users Count  
---|---  
[10,20) | 949  
[20,30) | 2,161  
[30,40) | 2,114  
[40,50) | 2,081  
[50,60) | 2,024  
[60,70) | 1,511  
[70,inf) | 1,450  
  
#### `integer`

`style: integer` must be used with discrete integer values (such as age). If you try to use non-integers to define the tiers you will receive an error. This style looks like:

Users Age Tier (Integer) | Users Count  
---|---  
10 to 19 | 949  
20 to 29 | 2,161  
30 to 39 | 2,114  
40 to 49 | 2,081  
50 to 59 | 2,024  
60 to 69 | 1,511  
70 or Above | 1,450  
  
#### `relational`

`style: relational` is best used with continuous numbers (such as dollars) and looks like:

Users Age Tier (Relational) | Users Count  
---|---  
>=10 and < 20 | 949  
>=20 and < 30 | 2,161  
>=30 and < 40 | 2,114  
>=40 and < 50 | 2,081  
>=50 and < 60 | 2,024  
>=60 and < 70 | 1,511  
>=70 | 1,450  
  
You can also style tiers with [`value_format`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format). For example:
    
    
    dimension: amount_tier {
      type: tier
      tiers: [0, 10, 20, 30, 40, 50, 60, 70, 80]
      style: integer
      sql: ${amount} ;;
      value_format: "$#,##0"
    }
    

This example would result in tier labels like `$10 to $19`, `$20 to $29`, and the like.

### Things to consider

Using `tier` in conjunction with [dimension fill](https://docs.cloud.google.com/looker/docs/creating-visualizations#filling_in_missing_dates_and_values) can result in unexpected tier buckets.

For example, a dimension of `type: tier`, **Age Tier** , will display tier buckets for **Below 0** and **0 to 9** when dimension fill is enabled, although the data doesn't include age values for those buckets:

Users Age Tier  
---  
Below 0  
0 to 9  
10 to 19  
20 to 29  
30 to 39  
40 to 49  
50 to 59  
60 to 69  
70 to 79  
80 or Above  
  
When dimension fill is disabled for **Age Tier** , the buckets more accurately reflect the age values that are available in the data:

Users Age Tier  
---  
10 to 19  
20 to 29  
30 to 39  
40 to 49  
50 to 59  
60 to 69  
70 to 79  
80 or Above  
  
You can enable or disable dimension fill by hovering over the dimension name in the Explore, clicking the field-level [gear icon](https://docs.cloud.google.com/looker/docs/creating-visualizations#to_use_dimension_fill), and selecting either **Remove Filled in Tier Values** to disable, or **Fill in Missing Tier Values** to enable.

## `time`

`type: time` is used in conjunction with a [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) and the [`timeframes`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframes) parameter to create a set of time-based dimensions. For example, you can create a date, week, and month dimension based on a single timestamp column.

`type: time` works only with a `dimension_group` and will _not_ work with a regular [`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension). However, you can specify individual time-based dimensions, as explained in the Individual time and date types section.

For information about dimension groups, see the [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) parameter documentation page, which also includes information on the [`timeframes`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframes), [`convert_tz`](https://docs.cloud.google.com/looker/docs/reference/param-field-convert-tz), and [`datatype`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#specifying_the_database_datatype) parameters, as well as [common challenges](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#things_to_consider) and caveats to consider when you are using time-based data.

## `unquoted`

`type: unquoted` is used only with [`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter) fields. The `unquoted` type is similar to `type: string`, except that when the value of the `parameter` is inserted into the [`{% parameter %}` liquid variable](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) it won't be quoted. This is useful when inserting values into SQL, such as column or table names, that cannot be quoted in order to work properly.

Inserting unquoted values directly into SQL could create the possibility of unwanted SQL actions. To address this, parameter values of `type: unquoted` are restricted to the characters A through Z and 0 through 9 (no spaces or other special characters).

As an example, the following LookML creates a `parameter` called `table_name` that will produce an unquoted value:
    
    
    parameter: table_name {
      type: unquoted
    }
    

## `yesno`

`type: yesno` creates a field that indicates if something is true or false. The values appear as **Yes** and **No** in the Explore UI.

The [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter for a `type: yesno` dimension takes a valid SQL expression that evaluates to `TRUE` or `FALSE`. If the condition evaluates to `TRUE`, **Yes** is displayed to the user; otherwise, **No** is displayed.

The SQL expression for `type: yesno` dimensions cannot include any aggregations. This means it cannot contain SQL aggregations or any references to LookML measures. If you want to create a `yesno` field that includes a SQL aggregation or that references a LookML measure, use a _measure_ with [`type: yesno`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#yesno), not a dimension.

For example, the following LookML creates a field that indicates whether or not an order has been paid, based on the `status` field:
    
    
    dimension: is_order_paid {
      type: yesno
      sql: ${status} = 'paid' ;;
    }
    

To reference a `type: yesno` field in another field, treat the `type: yesno` field as a boolean (in other words, as if it contains a true or false value already). For example:
    
    
    dimension: is_big_order {
      type: yesno
      sql: ${order_size} = 'big' ;;
    }
    # This is correct
    measure: total_boxes_needed {
      type: number
      sql: SUM(CASE WHEN ${is_big_order} THEN 2 ELSE 1 END) ;;
    }
    # This is NOT correct
    measure: total_boxes_needed {
      type: number
      sql: SUM(CASE WHEN ${is_big_order} = 'Yes' THEN 2 ELSE 1 END) ;;
    }
    

If you use `type: yesno` with time-based data, the dimension returns **yes** if the datetime has a value, and returns **no** if not.

## `zipcode`

`type: zipcode` is used with zip code dimensions that you want to plot on a [Static Map (Points)](https://docs.cloud.google.com/looker/docs/map-points-options) visualization (use a state or country field for [Static Map (Regions)](https://docs.cloud.google.com/looker/docs/map-regions-options)). Any dimension of `type: zipcode` is automatically given the [`map_layer_name`](https://docs.cloud.google.com/looker/docs/reference/param-field-map-layer-name) of `us_zipcode_tabulation_areas`. If you don't want to plot the zip codes, you can use a simpler type such as `type: number`.

The [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter for `type: zipcode` dimensions can take any valid SQL expression that results in a five-digit, US zipcode.

> For the purposes of filtering on a zipcode dimension, some database dialects require that the database field referenced by the zipcode dimension is a varchar or string type field, not an integer type field.

For example:
    
    
    dimension: zip {
      type: zipcode
      sql: ${TABLE}.zipcode ;;
    }
    

## Individual time and date types

Typically, dates are handled as a [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) that uses `type: time`.

It is possible to create one [`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) or [`filter` field](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) for each individual timeframe that you want to include, instead of generating all of them in a single [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group). This is generally avoided, unless you have already pre-calculated time columns in your database or want to change the Looker timeframe naming convention (such as having a field named `created_date_of_purchase` instead of `created_date`).

Many individual time and date based types are listed in Available time-based types.

As an example, for this `dimension_group` definition:
    
    
    dimension_group: created {
      type: time
      timeframes: [week, month, year]
      sql: ${TABLE}.created_at ;;
    }
    

You can use this as a logic equivalent:
    
    
    dimension: created_week {
      type: date_week
      sql: ${TABLE}.created_at ;;
    }
    dimension: created_month {
      type: date_month
      sql: ${TABLE}.created_at ;;
    }
    dimension: created_year {
      type: date_year
      sql: ${TABLE}.created_at ;;
    }
    

### Available time-based types

The following types are used in the `type` parameter of an individual dimension to create time or date based fields. Do _not_ use these types with the `timeframe` parameter, which is documented on the [dimension_group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframe_options) documentation page.

> All individual time and date types require a timestamp as input from your database.

#### Special types

Type | Description | Example Output  
---|---|---  
`date_raw` |  The raw value from your database, without casting or time zone conversion, **won't show up on an Explore page** (typically not needed except in joins or time comparisons)  |  `2014-09-03 17:15:00 +0000`  
  
#### Time types

Type | Description | Example Output  
---|---|---  
`date_time` | Datetime of the underlying field (some SQL dialects show as much precision as your database contains, while others show only to seconds) | `2014-09-03 17:15:00`  
`date_time_of_day` | Time of day | `17:15`  
`date_hour` | Datetime truncated to the nearest hour | `2014-09-03 17`  
`date_hour_of_day` | Integer hour of day of the underlying field | `17`  
`date_hourX` | Splits each day into intervals with the specified number of hours. | See Using `date_hourX`.  
`date_minute` | Datetime truncated to the nearest minute | `2014-09-03 17:15`  
`date_minuteX` | Splits each hour into intervals with the specified number of minutes. | See Using `date_minuteX`.  
`date_second` | Datetime truncated to the nearest second | `2014-09-03 17:15:00`  
`date_millisecond` | Datetime truncated to the nearest millisecond (see the Dialect Support for Milliseconds and Microseconds section for information on dialect support) | `2014-09-03 17:15:00.000`  
`date_millisecondX` | Splits each second into intervals with the specified number of milliseconds (see the Dialect Support for Milliseconds and Microseconds section for information on dialect support). | `2014-09-01 01:00:00.250`  
`date_microsecond` | Datetime truncated to the nearest microsecond (see the Dialect Support for Milliseconds and Microseconds section for information on dialect support) | `2014-09-03 17:15:00.000000`  
  
#### Date types

Type | Description | Example Output  
---|---|---  
`date` | Date of the underlying field | `2017-09-03`  
`date_date` |  Removed 4.6  Replaced by `date` |   
  
#### Week types

Type | Description | Example Output  
---|---|---  
`date_week` | Date of the week starting on a Monday of the underlying datetime | `2017-09-01`  
`date_day_of_week` | Day of week alone | `Wednesday`  
`date_day_of_week_index` | Day of week index (0 = Monday, 6 = Sunday) | `2`  
  
Note that the `date_week`, `date_day_of_week`, and `date_day_of_week_index` types depend on the value of [`week_start_day`](https://docs.cloud.google.com/looker/docs/reference/param-model-week-start-day), which defaults to Monday.

#### Month types

Type | Description | Example Output  
---|---|---  
`date_month` | Year and month of the underlying datetime | `2017-09`  
`date_month_num` | Integer number of the month of the underlying datetime | `9`  
`date_month_name` | Name of the month | `September`  
`date_day_of_month` | Day of month | `3`  
`date_fiscal_month_num` | Integer number of the month of the underlying datetime | `9`  
  
To use `date_fiscal_month_num` type, the [`fiscal_month_offset`](https://docs.cloud.google.com/looker/docs/reference/param-model-fiscal-month-offset) parameter must be set in the model.

#### Quarter types

Type | Description | Example Output  
---|---|---  
`date_quarter` | Year and quarter of the underlying datetime | `2017-Q3`  
`date_quarter_of_year` | Quarter of the year preceded by a "Q" | `Q3`  
`date_fiscal_quarter` | Fiscal year and quarter of the underlying datetime | `2017-Q3`  
`date_fiscal_quarter_of_year` | Fiscal quarter of the year preceded by a "Q" | `Q3`  
  
To use `date_fiscal_quarter` and `date_fiscal_quarter_of_year` types, the [`fiscal_month_offset`](https://docs.cloud.google.com/looker/docs/reference/param-model-fiscal-month-offset) parameter must be set in the model.

#### Year types

Type | Description | Example Output  
---|---|---  
`date_year` | Integer year of the underlying date time | `2017`  
`date_day_of_year` | Day of year | `143`  
`date_week_of_year` | Week of the year as a number | `17`  
`date_fiscal_year` | Integer fiscal year of the underlying datetime | `2017`  
  
To use the `date_fiscal_year` type, the [`fiscal_month_offset`](https://docs.cloud.google.com/looker/docs/reference/param-model-fiscal-month-offset) parameter must be set in the model.

#### Using `date_hourX`

In `date_hourX` the `X` is replaced with 2, 3, 4, 6, 8, or 12.

This will split up each day into intervals with the specified number of hours. For example `date_hour6` will split each day into 6 hour segments, which will appear like:

  * `2014-09-01 00:00:00`
  * `2014-09-01 06:00:00`
  * `2014-09-01 12:00:00`
  * `2014-09-01 18:00:00`



For example, a row with a `time` of `2014-09-01 08:03:17` would have a `date_hour6` of `2014-09-01 06:00:00`.

#### Using `date_minuteX`

In `date_minuteX` the `X` is replaced with 2, 3, 5, 10, 15, or 30.

Using `date_minuteX` will split up each hour into intervals with the specified number of minutes. For example, `date_minute15` will split each hour into 15-minute segments, which will appear as follow:

  * `2014-09-01 01:00:00`
  * `2014-09-01 01:15:00`
  * `2014-09-01 01:30:00`
  * `2014-09-01 01:45:00`



To give an example, a row with a `time` of `2014-09-01 01:17:35` would have a `date_minute15` of `2014-09-01 01:15:00`.

### Time zones and `convert_tz`

In general, time computations (differences, durations, and so on) only work correctly when you operate on time values that are all converted to the same time zone, so it is important to keep time zones in mind when writing LookML.

Looker has various [time zone settings](https://docs.cloud.google.com/looker/docs/using-time-zone-settings) that convert time-based data between different time zones. Looker converts time zones by default. If you don't want Looker to perform a time zone conversion for a particular dimension or dimension group, you can use the `convert_tz` parameter described on the [`convert_tz`](https://docs.cloud.google.com/looker/docs/reference/param-field-convert-tz) parameter documentation page.

### Dialect support for milliseconds and microseconds

Looker supports precision to microseconds; however, some databases support precision only to seconds. If a database encounters a time type more precise than it can support, it will round up to seconds.

In the latest release of Looker, the following dialects support milliseconds:

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
  
In the latest release of Looker, the following dialects support microseconds:

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
  
## Individual duration types

Typically, durations are handled as a [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) that uses `type: duration`.

It is possible to create one [`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) for each individual duration that you want to include, instead of generating all of them in a single [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group). This is generally avoided, unless you want to change the Looker timeframe naming convention (such as having a field named **Number of Days to Delivery** instead of **Duration to Delivery**).

Several individual duration types are listed in Individual duration types.

When you use a duration type for a dimension, you must also include the `sql_start` and `sql_end` parameters to provide the start and end times for calculating the time difference.

The `sql_start` and `sql_end` parameters can take any valid SQL expression that contains data in a timestamp, datetime, date, epoch, or yyyymmdd format. The `sql_start` and `sql_end` fields can be any of the following:

  * A reference to a `raw` timeframe from an existing dimension group of `type: time`.
  * A reference to a dimension of `type: date_raw`.
  * A SQL expression that is a timestamp, such as a reference to a SQL column that is a timestamp.
  * A SQL expression that pulls a time from your database, using the appropriate expression for your dialect.



As an example, for this `dimension_group` definition:
    
    
    dimension_group: to_delivery {
      type: duration
      intervals: [day, hour]
      sql_start: ${created_raw} ;;
      sql_end: ${delivered_raw};;
    }
    

You can use these `dimension` parameters as a logical equivalent:
    
    
    dimension: number_of_days_to_delivery {
      type: duration_day
      sql_start: ${created_raw} ;;
      sql_end: ${delivered_raw};;
    }
    
    dimension: number_of_hours_to_delivery {
      type: duration_hour
      sql_start: ${created_raw} ;;
      sql_end: ${delivered_raw};;
    }
    

In the Explore UI, this would create dimensions called **Number of Days to Delivery** and **Number of Hours to Delivery**.

### Available duration types

The following types are used in the `type` parameter of an individual dimension to create duration based fields. Do _not_ use these types with the `intervals` parameter, which is documented on the [dimension_group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#interval_options) documentation page.

> All individual duration types require a timestamp as input from your database.

Type | Description | Example Output  
---|---|---  
`duration_day` | Calculates a time difference in days | `9 days`  
`duration_hour` | Calculates a time difference in hours | `171 hours`  
`duration_minute` | Calculates a time difference in minutes | `10,305 minutes`  
`duration_month` | Calculates a time difference in months | `3 months`  
`duration_quarter` | Calculates a time difference in quarters of the year | `2 quarters`  
`duration_second` | Calculates a time difference in seconds | `606,770 seconds`  
`duration_week` | Calculates a time difference in weeks | `6 weeks`  
`duration_year` | Calculates a time difference in years | `2 years`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

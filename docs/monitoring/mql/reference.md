---
url: https://docs.cloud.google.com/monitoring/mql/reference/
title: Monitoring Query Language reference \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:34.224146+00:00
---

# Monitoring Query Language reference  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/mql/reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Monitoring Query Language reference Stay organized with collections  Save and categorize content based on your preferences. 

**Announcement:** On July 22, 2025, Google Cloud customer support for MQL ended, and MQL is no longer available in the Google Cloud console when you create charts, dashboards, and alerting policies. Existing MQL charts, dashboards, and alerting policies continue to work, and you can still create them by using the Cloud Monitoring API. For more information, see the [deprecation notice for MQL](https://docs.cloud.google.com/stackdriver/docs/deprecations/mql). 

This is a reference manual for the Cloud Monitoring Monitoring Query Language. It covers the following topics:

  * The data model underlying the time series database that the Monitoring Query Language accesses.

  * The structure and semantics of queries.

  * A description of each of the operations and functions that a query is built from.




## **Data Model**

Cloud Monitoring uses a time series database that contains all the measurements it has ingested about each thing it is monitoring (known as a monitored resource). This describes the logical structure of that database.

The fundamental element is a _time series_ whose data consists of observations of the monitored resource being monitored.

Time series in the database are logically organized into relational _tables_ , each containing time series with a common meaning and structure. The tables are referenced by queries that return data, generate graphs, and compute alerts.

The database also includes _metadata_ , which are slowly changing values associated with a monitored resource and which are set by user configuration or by the service that implements the monitored-resource type.

### **Time series**

A _time series_ is a named sequence of _points_ , each being a measured value and the time to which the value applies. A time series consists of three parts: a type, which specifies the structure of the time series, an identifier, which uniquely names the time series, and a history, which contains the time series data. Each of these three parts are explained in this section.

A **time series type** specifies the structure of the time series identifier and the time series history. It consists of two parts:

  * A **monitored-resource type** (listed [here](https://cloud.google.com/monitoring/api/resources)) that names a particular kind of monitored resource that is monitored, such as a Compute Engine instance (`gce_instance`) or a cloud SQL database (`cloudsql_database`). It has a set of [label descriptors](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor) that uniquely identify an instance of that type of monitored resource.

  * A **metric type** (listed [here](https://cloud.google.com/monitoring/api/metrics)) that describes a particular kind of measurement that can be taken on a monitored resource, for example bytes read from disk by a Compute Engine instance is measured by the metric named `compute.googleapis.com/instance/disk/read_bytes_count`, and the data utilization of a cloud SQL database is measured by the metric named `cloudsql.googleapis.com/database/disk/bytes_used`. The metric type specifies the type of measurement's value, the units of the measurement, and the kind of time series. It may specify label descriptors that distinguish time series measuring different aspects of the same thing. For example `command` indicating what command is counted in the `appengine.googleapis.com/memcache/operation_count` metric.




Note that a monitored resource type and a metric type are described by a `MonitoredResourceDescriptor` and a `MetricDescriptor`, respectively. These describe the types. They each contain a field named `type` which contains the name of that monitored resource or metric type.

A **time series identifier** is the name of the time series, uniquely identifying it among all time series with the same type. It consists of a set of values, one for each of the label descriptors specified in the monitored resource and metric types that make up the time series type.

  * The labels from the monitored-resource type uniquely identify the particular instance of the kind of monitored resource from which the measurements in the time series were taken. For example, the `gce_instance` monitored resource has labels `project_id`, `instance_id`, and `zone` which uniquely identify a particular Google Compute Engine virtual machine.

  * Each label from the metric type identifies which specific kind of measurement for the given metric is represented in the time series. For example `status` indicating the status of the commands counted in the `appengine.googleapis.com/memcache/operation_count` metric might have value `'HIT'` for one time series that counts hits and `'MISS'` for another time series that counts misses.




A **time series history** is a time-ordered sequence of _points_ , each representing a simultaneous measurement of one, or, potentially, several values (for example, CPU load or temperature and humidity) at some time or over some time range. A point has two elements:

  * A point's **extent** in time consists of an **end time** , which is always present, and a **start time** which may or may not be present. If the start time is not present, the point's extent is a single point in time given by the end time. If the start time is given, it must be before the end time and the point's extent is the time interval starting at the start time and ending at the end time.

No two points in a time series can have the same extent. In addition, the extents of the points in a time series are constrained by the time series kind given by the metric type as described below.

  * A point's **value** represents a simultaneous measurement of one, or, potentially, several values (for example, CPU load or temperature and humidity) that applies to the time given by the point's extent. The metric type describes each measurement value, giving it a name and a value type for each. If there are multiple measurement values, they are in a particular order and can be reference by their index in that order.

A typical time series stored in the time series database has a single value in each point. The name of the metric in the time series type is a URI and the name of the single value is the part of the metric name after the last `/`. For example, the metric `appengine.googleapis.com/memcache/operation_count` has a value column named `operation_count`.

A time series that is the output of a query may have multiple points whose type, name, and order are given by the query.

The metric type may also specify _units of measurement_ for the time series value if it is of type _Int_ , _Double_ , or _Distribution_. The units are given using a subset of the [Unified Code for Units of Measure](http://unitsofmeasure.org/ucum.html) (UCUM). For example, `ms` for milliseconds or `By` for bytes. See Units of Measure for the details.




Each value in a point has a particular **value type** , which is specified by the metric type in the time series type. Also each label in the time series identifier has a value type, given by the [label descriptor](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor) in the time series type's monitored resource or metric type. The value types are as follows.

  * **Int** : A 64-bit signed integer.

  * **String** : A UTF-8 encoded Unicode string.

  * **Bool** : A boolean value.

  * **Double** : A 64-bit IEEE floating point value.

  * **Distribution** : A complex value containing a histogram and statistics that provide a summary description of a population (set) of _Double_ values. The parts of this value are as follows:

    * A count of the number of values in the population.
    * The sum of the values in the population.
    * The sum of squared deviation of the values in the population.
    * A bucket specification indicating the boundaries between buckets in the histogram. A bucket contains a count of the values that fall between the lower and upper bound of the bucket.
    * A histogram giving the number of values that fall into each bucket.

These parts are enough to additionally compute the population mean, variance, standard deviation, and estimates of percentiles.




A point value's type may be any of the above. A time series identifier label type may only be _String_ , _Int_ , or _Bool_

In addition to these types, there are two further types that are in the start and end time of a point or are used to describe times and durations in queries.

  * **Date** :  A particular point in time measured as the distance since the Unix epoch. It is a time-zone-independent representation of a point in time. The start and end time of a point are of this type.

  * **Duration** :  A length of time. This time does not have a particular unit of measurement (although resolution is to the microsecond level) but takes on a particular unit (e.g. seconds) when converted to an _Int_ or _Double_.




The set of values for each type (except _Date_ and _Duration_) includes a value called **no-value** which indicates that there is no specific value. This is used in two cases:

  * When no specific value is known, for example when there is an error (such as dividing by 0) that prevents the computation of a value.

  * No-value will be the value of a label in a time series identifier when the label is required by the time series type but no value is known for it. This may happen in cases where no value is known when the metric is collected or if the time series was generated by a query and the computation generating the label value did not produce a value. Note that no-value is a distinct value and thus distinguishes the time series identifier from any other that has an actual value for the given label.




No-value is distinct from an IEEE NaN and from a string value that is the empty string. It is not possible for any value in a point to be no-value.

The **time series kind** describes the meaning of the values of the points in a time series and constrains each point's extents. There are three time series kinds:

  * **Gauge** :  The value of a point in a _Gauge_ time series is a measurement taken at the point's end time. A point in a _Gauge_ stream does not have a start time so its extent is a single point in time. The value of a point may represent one of the following things:

    * A _sample_ taken of some variable (such as the length of a queue or an amount of memory in use).

    * A _state_ quality that is true at the point's time and will remain true until the time of the next point.

    * A _summary_ of some quantity (mean, max, etc.) that applies to the period between the point and the next earlier point in the time series.

  * **Delta** :  For numeric values (_Int_ or _Double_), each point represents the change in some measured value over the point's extent, that is to say between the point's start time, which is present, and end time. For a Distribution's value, it has a population of the numeric values that arose during the point's extent. A _Delta_ time series kind must have a value of type _Int_ , _Double_ , or _Distribution_.

For a _Delta_ time series, the extents of any two points cannot overlap, so each point represents an independent change in the measured value (numeric) or disjoint population of values (_Distribution_). Ideally, the extent of each point starts immediately after the extent of the next earlier point so the time series is a complete description of the range of time it covers.

  * **Cumulative** :  This can be thought of as a _Delta_ time series with overlapping extents. The constraint is that, if two points have overlapping extents, they must have the same start time. Thus each point represents a cumulative increase in some measured value over the last point with a common start time.

_Cumulative_ metrics are a robust way to collect time series from an external source of data:

    * The source is not required to reset counters or accumulators each time a value is collected and can be be easily monitored at multiple periods.

    * Accumulated counts are not lost if some points are missing; the next point has all the counts since the start time, including those from the missing point. Only temporal resolution is lost.

In queries, however, cumulative time series are not often observed. To make operations on time series returned from queries more straightforward, when a cumulative time series is fetched, it is automatically converted into a delta time series by making each point's extent start at the time of the next earlier point and making its value be the change since that next earlier point. This does not change the information present but makes each point independent of the others. (This can be overridden by `fetch_cumulative`.)

For a time series whose points have more than one value, each value has a time series kind which can only be _Gauge_ or _Delta_. If any value has _Delta_ kind, then the overall metric has _Delta_ kind (and thus each point has a start and end time). Otherwise, the metric has _Gauge_ kind (and only end time).




### Tables

All time series with the same time series type (monitored-resource type and metric type) are logically organized into a relational _table_. The table has a _table name_ which consists of the monitored-resource type name followed by the metric type name.

A table has one row for each point in each of the time series included in it. The table has the following kinds of columns:

  * **Time series identifier** columns,  One column for each time series identifier label as specified by the monitored resource and metric types. The name of the column is the name of the label (its [key](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor)) and the type of the column is the value type of the label. If a monitored resource label and a metric label have the same name, the name of the metric label column has `metric.` prepended to it.

A time series is made up of all the rows in a table with the same value for each of the corresponding time series idenfiter columns.

  * **Time** column or columns,  derived from the extent of the points in the time series. There is always one end time column that is accessed by the function `end()` (we don't actually give the column a name). If the metric is of _Delta_ time series kind, then there is a start time column accessed by the function `start()`. (There is also a start time column for metrics with Cumulative time series kind.) Both columns have values of type _Date_.

  * **Value** columns,  one for each value in the value of the points of the time series. Each column has the name and type given of that value and the value columns are in the same order as that given by the metric type. If there is a monitored resource or metric label with the same name as a value name, the value name given by the metric type is prefixed with `value.` to form the column name.




All the points in one time series have the same value in the time series identifier columns and these columns uniquely identify time series. The time series columns plus the end time column make up the table's primary key, uniquely identifying a row and thus a point.

The above describes a _stored table_ consisting of time series that are stored in the database. A query takes _stored tables_ as the initial inputs and performs successive table operations (filtering, aggregating, joining, etc), yielding intermediate _derived_ tables as the output from these table operations.

A derived table has the same structure as a stored table with these differences:

  * The table will still be associated with a monitored-resource type if the transformation that produced it preserved all the monitored resource label columns. Otherwise it is not associated with a monitored-resource type. This is important for metadata (described in the next section).

  * The table is described by a table type rather than by a monitored-resource type and metric type. The table type is the same as a metric type except that the set of labels includes all the columns of the time series identifier. Depending on the actual derivation of the table, the time series identifier columns may have no relation to the columns specified by any actual monitored-resource type or metric type.

  * A derived table does not have a name.




### Metadata

A monitored-resource type can have _metadata_ types, each of which associates a value with every instance of that particular monitored-resource type. Each metadata type has a name and a value type (which is _String_ , _Int_ , or _Bool_).

There are two kinds of metadata:

  * **System metadata** which is created by the service that creates and manages the monitored resource. System metadata has a name of the form `metadata.system_labels.<key>`, where `<key>` identifies a specific kind of metadata.

  * **User metadata** which is present when a service allows the user to attach [labels](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor) to a specific monitored resource. User metadata has a name of the form `metadata.user_labels.<key>`, where `<key>` is the key of the label the user has attached to the entity. For example: `metadata.user_labels.my_key`. The value of user metadata is always of type _String_.




A table (stored or derived) that is associated with a monitored resource can be considered to have additional virtual value columns, one for each metadata type associated with the monitored-resource type. For each row in the table, a metadata column has the value of that metadata at the time of the row's end time column. These additional metadata columns are not actually part of the table, but they can be referenced in query expressions as if they were by giving the name of the metadata in the expressions that operate on a table row.

### Alignment

A time series is _temporally aligned_ (or just _aligned_) if the end time of its points occur only at regular intervals. We say a time series is aligned  with respect to a particular alignment base time and period if every point in the time series has an end time that is some multiple of the alignment period before (or after) the alignment base time. For example, with an alignment base time of 10:03 and an alignment period of 5 minutes, 09:48, 09:53, 09:58, 10:03, 10:08 would all be valid end times for points.

If a table's time series have _Delta_ time series kind then the start time of each point must be earlier than the end time by the duration of the period, making the duration of every point be of equal length. A table with _Cumulative_ start times cannot be aligned because it is not, in general, possible to make the start times of points line up between different time series.

If all the time series that make up a table are aligned with respect to the same alignment time and period, then the table is aligned with respect to that time and period.

When a table is aligned, the points in different time series line up with each other in time. This makes it possible to do operations combining different time series. For example, if we want to get the time series that is the sum of some metric over all of our monitored resources, we need the points in the individual time series to 'line up', that is, have the same alignment. Then the value of points in the resulting time series is the sum of values of the points at the same time in the individual time series.

## Syntax and Semantics

### Lexical Elements

The text of a query is made up of a sequence of _tokens_ which are described in the following [grammar](https://en.wikipedia.org/wiki/Wirth_syntax_notation) with these rules:

  * A token is described by one of the all-capitalized non-terminal symbols in the grammar below.
  * A token other than `base_string` has no white space within it. White space is space, tab, newline, and comments. A comment is any text, not in a `base_string` starting with `#` and ending with a newline.
  * White space between tokens is ignored, other than to separate tokens.
  * Two adjacent tokens must be separated by white space if this grammar would allow them to be recognized as a single token other than `BARE_NAME` (which is only recognized in certain contexts).


    
    
    ID : letter { letter_num_under } .
    QUOTED_COLUMN : ( 'c' | 'C' ) base_string .
    BARE_NAME : ( '/' | letter_num_under ) { letter_num_under | '.' | '/' | '-' } .
    NUMBER : digit { digit } [ fraction | '.' ] [ exponent ] | fraction [exponent] .
    STRING : [ 'r' | 'R' ] base_string .
    DURATION : digit { digit } ( 's' | 'ms' | 'us' | 'm' | 'h' | 'd' | 'w' ) .
    DATE : ( 'd' | 'D' ) base_string .
    
    letter_num_under : letter | digit | '_' .
    base_string : '\'' any-but-quote '\'' | '"' any-but-quote-quote '"' .
    fraction : '.' digit { digit } .
    exponent : ( 'e' | 'E' ) [ '-' | '+' ] digit { digit } .
    
    letter - an ASCII letter
    digit  - an ASCII digit
    any-but-quote - any Unicode character except the ASCII control codes or `'`.
    any-but-quote-quote - any Unicode character except the ASCII control codes or `"'.
    

Identifiers (`ID`) are used to name the builtin table operations and functions that are part of the Monitoring Query Language and to name columns and metadata in expressions. The syntax distinguishes between a place that an `ID` can be a table operation or function name and a place that an `ID` can be a column name, so there are no "reserved" identifiers that can't be used as column names. A `QUOTED_COLUMN` is used to give the name of a column that will not parse as an identifier. Example: `c'total cpu'`

The `NUMBER`, `STRING`, `DURATION`, and `DATE` tokens identify literal values. A `NUMBER` can be followed by a `unit` which gives the units of measure of that literal value as a `STRING`. A `STRING` may contain Unicode characters. If it is not prefixed by `r` or `R`, the normal escape sequences will be recognized. The suffix of a `DURATION` indicates how a time duration is being denominated: seconds, milliseconds, microseconds, minutes, hours, days, or weeks. The `base_string` in a date contains a date in the form `2010/06/23-19:32:15-07:00`, where the first `-` can be a space and the timezone (`-07:00`) can be dropped (as can the seconds, minutes, or hours).

The remaining tokens are punctuation and operator tokens that appear in quotes in the grammar that follows (e.g. `'^'` or `'<='`). These tokens are `^`, `<=`, `<`, `==`, `=` `=~`, `>=`, `>`, `||`, `|`, `_`, `-`, `,`, `;`, `::`, `:`, `!=`, `<>`, `!~`, `!`, `//`, `/`, `.`, `(`, `)`, `[`, `]`, `{`, `}`, `*`, `&&`, `%`, `+`.

### Query Structure

A query is made up of a sequence of table operations (`table_op`), joined together by pipe operators (`|`). Each table operation takes tables as inputs and produces tables as output. The tables output by one table operation are piped into the next table operation which consumes them to produce its own table output.
    
    
    query : table_op { '|' table_op } .
    table_op : basic_table_op | grouped_table_op | shortcut_table_op .
    
    basic_table_op : ID [ arg { ',' arg } ] .
    arg : table_name | expr | map .
    
    grouped_table_op:  '{' query { ';' query } '}' .
    

There are three kinds of table operations (`table_op`):

  * A `basic_table_op` starts with an `ID` that names the kind of operation to be done (as described here). This is followed by arguments (`arg`) which provide details about what the table operation will do. Each kind of `basic_table_op` takes zero, one, or many tables as input and produces one table as output.

  * A `grouped_table_op` consists of an ordered list of queries. Each of the queries produces one table and the result of the `grouped_table_op` is an ordered list of these tables. Each of the queries takes as input the same zero or more input tables that are the input to the `grouped_table_op`.

  * A `shortcut_table_op` is a shortcut notation (described here) for a `basic_table_op`.




The tables output by one `table_op` are passed by the pipe operator (`|`) as input to the next `table_op`. The following are the rules of passing tables that are output by one table operation to the left of a pipe operator (called the producer) to a table operation to the right of the pipe operator (called the consumer):

  * A table operation that takes no table input cannot be a consumer.

  * For a producer that outputs a single table and a consumer that takes a single table, the producer output table is an input to the consumer.

  * For a producer that outputs multiple tables and a consumer that takes a single table, the consumer is applied separately to each input table and the output of the consumer table operation is one table for each input table.

  * For a producer that outputs multiple tables and a consumer that takes multiple tables, all the produced tables are input to the consumer.

  * For a producer that produces a single table and a consumer that is a `grouped_table_op`, the single table is the input to the first table operation of each `query` in the `grouped_table_op`.

  * It is not valid for a `grouped_table_op` to be a consumer for a producer that produces multiple tables.

  * The last `table_op` in each `query` in a `grouped_table_op` must produce only one table.




The table operation's 'arg' elements provide information to the table operation about how it should process its input tables into an output table. An `arg` can be one of three things:

  * A table name (`table_name`), which names a table or is part of the name of a table that is to be fetched from the Cloud Monitoring database.

  * An expression (`expr`), which is a formula for computing a value. This can be a literal value that is known statically or it can be a value computed from the column values of one or more rows from the input table or tables of the table operation.

  * A map (`map`), which describes how to compute the columns in the output table of a table operation. A `map` contains one or more `expr` that compute the values of the columns.




### Table Names

A `table_name` names a monitored-resource type, a metric type, a group, or a table. These are used in table operations that fetch tables from the time-series database for further processing.
    
    
    table_name : name { '::' name } .
    name : string | BARE_NAME | ID .
    

A single `name` refers to a monitored-resource type or a metric type, for example the monitored-resource type `gce_instance` or `aws_dynamodb_table` or the metric type `loadbalancing.googleapis.com/http/backend_latencies`.

A monitored-resource type can also be named using a group name or by a monitored-resource type name followed by `::` and a group name. The former can be used when the group specifies a single monitored-resource type and the latter is used when the group does not.

A stored table is given by a monitored-resource type name followed by `::` and a metric type name. For example `gce_instance :: loadbalancing.googleapis.com/http/backend_latencies`.

### Expressions

An expression (`expr`) is a formula for computing a value. It is used as an argument to a table operation and helps describe the transformation that the table operation will perform on its input table or tables. An `expr` can be a literal expression or it can be a dynamic expression.

If an `expr` is literal, it is composed only of literal values and simple function calls whose arguments are literal values. The value of such an expression is determined before the query is applied to any tables.

If an `expr` is dynamic it can contain references to table columns and is used to compute a value from one or more rows from the input table. There are three kinds of dynamic expressions:

  * _Value_ expression  A value expression produces a value for each input table row that it is applied to. It may contain references to table columns and, when evaluated for one input row, those references evaluate to the corresponding column values in the row.

  * _Aggregating_ expression  An aggregating expression produces a value for a set of input table rows. It can be decomposed into three parts:

    * One or more value expressions that are applied individually to each input row to produce a value for each row. These value expressions are arguments to aggregation functions.

    * One or more aggregation functions which take a collection of input values produced by the value expression(s) and reduce them to a single resulting value.

    * An outer expression over the aggregation functions that take the values that result from the aggregation functions and produce the value of the expression as a whole.

For example in the aggregating expression `sum(if(status >= 500, val(), 0)) / sum(val())` the parts are as follows:

    * The value expressions are `if(status >= 500, val(), 0)` and `val()`. These will be applied to each input row to create two collections of values.

    * The aggregators are the two `sum` function calls, each taking as input the collections of values produced by the value expression that is its argument.

    * The outer expression is the division operator (`/`) which will be applied to the final output of each of the `sum` aggregation functions to produce the value of the overall expression.

  * _Aligning_ expression;  An aligning expression consists of a single call on an aligning function. The aligning function produces an output value from an input time series and is used by the `align` to produce an aligned table.




Each expression is composed of `opnd` elements (defined below) connected by operators. 
    
    
    expr : term { infix_op term } .
    term : { prefix_op } opnd .
    infix_op : '&&' | '||' | '^'
             | '==' | '=' | '!=' | '<>' | '<' | '>' | '<=' | '>=' | '=~' | '!~'
             | '+' | '-'
             | '*' | '/' | '//' | '%' .
    prefix_op : '+' | '-' | '!' .
    

The operators behave in the usual way according to precedence. The following table arranges operators in five groups. All the operators in a group have the same precedence, with higher groups binding more tightly. Operators of the same precedence are applied left to right. Each operator corresponds to a function, given in the table, which is applied to its operands.

operator | function | operation  
---|---|---  
`*`   
`/`   
`//`   
`%` | `mul`   
`div`   
`div`   
`rem` | Multiplication   
Division   
Integer Division   
Integer Remainder  
`+`   
`-` | `add`   
`sub` | Addition   
Subtraction  
`==` `=`   
`!=` `<>`  
`<=`   
`>=`   
`>`   
`<`   
`=~`   
`!~` | `eq`   
`ne`   
`le`   
`ge`   
`gt`   
`lt`   
`re_full_match`   
`! re_full_match` | Equality comparison   
Inequality comparison   
Less than or equal comparison   
Greater than or equal comparison   
Greater than comparison   
Less than comparison   
Regular expression full match   
Regular expression not full match  
`&&` | `and` | Logical and  
`||` | `or` | Logical or  
  
The prefix operators `+`, `-`, and `!` correspond to the unary functions `pos`, `neg`, and `not` respectively and are applied before any infix operator.

Thus `a < b && a + b + c / -d == 5` is equivalent to `(a < b) && (((a + b) + (c / (-d))) == 5)`, which in turn is equivalent to `and(lt(a, b), eq(add(add(a, b), div(c, neg(d))), 5))`.

The operators operate on operands (`opnd`).
    
    
    opnd : literal | column_meta_name | '_' | '(' expr ')' | call_chain .
    
    literal : NUMBER [ unit ] | string | DURATION | DATE .
    unit : STRING
    string : STRING { STRING } .
    
    column_meta_name : id { '.' id } .
    id : ID | QUOTED_COLUMN .
    

Each `opnd` corresponds to a particular way of computing a value.

  * `literal` is the value of the given literal token.

    * A NUMBER literal can be followed by a `unit` which gives the units of measure of the literal value, for example `33 'By'` for 33 bytes.

    * A `string` is made up of one or more `STRING` tokens that are concatenated into one string value. Thus `'a-' 'b'` has the same value as `'a-b'`.

  * `column_meta_name` names a column or a virtual metadata column in the input table and evaluates to the value of that column in the input row the expression is applied to.

  * `_` represents the default value. This can only be given as an actual argument to an optional formal argument.

  * `'(' expr ')'` is a parenthesized expression that is just the value of the `expr`.

  * `call_chain` is one or more chained function calls:



    
    
    call_chain : [ ID arg_list ] { '.' call } .
    arg_list : '(' [ expr { ',' expr } [ ',' ] ] ')' .
    call : ID [ arg_list ] .
    

Each `ID` in a call_chain names a function that is applied to zero or more arguments. The arguments to a function call can come from the value columns of the input table, from the result of an earlier `call` in the call chain, or from the value of `expr` in an `arg_list`.

  * If the call chain starts with an `ID` (and no `.` before it), then the arguments to the called function are given by the `expr` in the following `arg_list`.

For example, `add(error_count, 1)` applies the function `add` to two arguments: the `column_meta_name` `error_count` and the `literal` `1`. This would be equivalent to `error_count + 1`.

  * If a `call_chain` starts with a `'.' call`, then the value columns of the input table are the first argument to the called function. If the `call` has an `arg_list`, then the `arg_list` provides additional arguments.

For example, `.div` applied to a table with value columns `num` and `den` would be equivalent to `div(num, den)` or just `num / den`. The expression `.add(3)` applied to a table with a single value column `count` would be equivalent to `add(count, 3)` or just `count + 3`

  * The function called by a `call` other than the first in a call chain takes as its first argument, the output of the previously called function in the call chain. If the `call` has an `arg_list`, then the `arg_list` provides additional arguments.

For example `.mul(3).div(4)` applied to a table with a single value column `error_count` would be equivalent to `div(.mul(3), 4)` which is equivalent to `div(mul(error_count, 3), 4)` which is equivalent to `error_count * 3 / 4` or `(error_count * 3) / 4`.




Note that the end and start time columns in a table do not have column names. The value of the time columns are accessed using the `end` and `start` functions.

### Maps

A `map` computes values for columns in an output row and gives them names. Depending on where the `map` is used, it will either be a time series identifier `map` that computes the time series identifier columns of the output row or a value `map` that computes the value columns of the output row.
    
    
    map : [ modifier ] '[' [ maplet { ',' maplet } ] ']' .
    modifier : ID .
    maplet : [ column_name ':' ] expr .
    column_name : ID | QUOTED_COLUMN .
    

Each `expr` in the `maplet` computes the value of an output column and the `column_name` gives the name of the column. If no `column_name` is given, one is constructed from the `expr`. If the `expr` is just the name of an input column, the `column_name` is the same. If functions are applied, these are added to the name. For example `sum(error_count / 3)` would get the name `error_count_div_sum`.

The output columns that the `map` computes (time series identifier or value) come from the `maplet`s in the `map` and from the corresponding kind of columns (time series identifier or value) in the input table. How this is done depends on the `modifier`:

  * No `modifier` The corresponding columns of the output row consist of exactly those columns specified by a `maplet` in the `map`. The name of the column either is explicitly given by an `ID` or `QUOTED_COLUMN` or is derived from the form of the `expr`. The value of the column in the output row is the value of the `expr`.

Each `maplet` must have a column name (explicit or derived) that is unique among all the columns in the output table.

For example, applying `[ratio: num/den]` as a value column `map` to a table with value columns `num` and `den` would result in an output table with value column `ratio`, where the `ratio` column value is the ratio of the two input colums.

Applying `[zone]` as a time series identifier `map` to a table with time series identifier columns `project_id`, `zone`, and `instance` would result in a table with just a `zone` time series identifier column whose value is the same as the `zone` input table column.

  * **`add`** All of the columns of the corresponding kind (time series identifier or value) of the input row are included in the output row. In addition, for each `maplet` in the `map`, there is an additional output column whose name and value are given by the `maplet`.

Each `maplet` must have a column name (explicit or derived) that is unique among all the columns in the output table.

For example, applying `add[ratio: num/den]` as a value `map` to a table with value columns `num` and `den` would result in an output table with value columns `num`, `den`, and `ratio`, where the `ratio` column value is the ratio of the other two columns.

  * **`update`** All of the columns of the corresponding kind (time series identifier or value) of the input row whose column name is not the same as that of a `maplet` in the `map` are included in the output row. In addition, for each `maplet` in the `map`, there is an additional output column whose name and value are given by the `maplet`.

Each `maplet` must have a column name (explicit or derived) that is unique among all the columns in the output table. It may name a column of the corresponding kind in the input that it is replacing.

For example, the following is a time series identifier `map`:
        
        update[job: re_extract(job, '[^-]*-(.*)', r'\1'),
                 kind: re_extract(job, '([^-]*)-.*', r'\1')]
        

When used on a table with time series identifier columns `user`, `job`, and `zone` would result in an output table with time series identifier column `user`, `job`, `zone`, and `kind`.

  * **`drop`** Each `maplet` must consist of an `expr` that is just the name of an input column of the corresponding kind. The output columns consist of all the input columns of the corresponding kind except those that are named in an `expr` in the `maplet`.

Each `maplet` must not have a `column_name` and the `expr` must simply name a column of the corresponding kind in the input table.

For example, applying `drop [job, user]` as a time series identifier `map` to a table with time series identifier columns `user`, `job`, and `zone` would result in an output table with time series identifier column `zone`.

  * **`ignore`** Each `maplet` must consist of an `expr` that is just a column name. If the name is the name of an input column of the corresponding kind, that column does not appear in the output columns. If the `maplet` column name does not name an input table column of the corresponding kind, that `maplet` has no effect. Thus, the output columns consist of all the input columns of the corresponding kind except those that are named in the `expr` in the `maplet`.

Each `maplet` must not have a `column_name` and the `expr` must simply be a column name, but it does not have to be the name of a column in the input table. If the `maplet` does not name a column in the input table, it is ignored.

For example, applying `ignore [job, instance]` as a time series identifier `map` to a table with time series identifier columns `user`, `job`, and `zone` would result in an output table with time series identifier columns `user` and `zone`. The column `job` is ignored by the maplet `job`, and the maplet `instance` has no effect.

  * **`rename`** Each `maplet` must have an explicit `column_name` and must have an `expr` that just references a column of the corresponding kind in the input table. The output columns are all the columns of the corresponding kind in the input table but if referenced in a `maplet` with a new name given by the `column_name` in the `maplet`.

The `column_name` in each `maplet` must be unique among the column names of the output table.

For example, applying `rename[numerator : num, denominator : den]` as a value column `map` to an input table with value columns `num`, `den`, and `ratio` would result in an output table with value columns `numerator`, `denominator`, and `ratio`.




### Units of Measure

Every numeric value (_Int_ , _Double_ , and _Distribution_) can have a unit of measure associated with it indicating the unit of measurement used by that value. Units are represented by strings that follow a subset of the [Unified Code for Units of Measure](http://ucum.org/ucum.html) (UCUM). For example a value denoting a number of bytes will have unit 'By' and another, denoting a rate of bytes transferred, unit 'By/s'.

Units attach to the columns of tables produced by table operations and to the value of expressions. They are statically associated with the column or expression in the same way that the type is. Any column or expression with a numeric type can have units associated with it but does not have to.

The units attached to columns in tables come from these sources:

  * Metric descriptors can specify the units for the value of a metric and these are seen in the documentation that describes metrics (for example, [here](https://cloud.google.com/monitoring/api/metrics_gcp)). The value columns of tables produced by `fetch` and `metric` table operations have the units specified by the metric descriptor.

  * Output table columns that are just a copy of the column from the input table have the same units as the input table column. So, for example, the `filter` table operation does not change the units on any columns of its input table and passes them on to the output.

  * The `union` table operation combines multiple tables into one, and all the tables must have the same columns. Each value column in an input table must have either no units attached or units that are equivalent to the units, if any, attached to that column in every other input table. If units are given for a column in any of the input tables, that column has those units in the output table. If none of the input tables have units specified for a column, that column has no units in the output.

  * For table operations that contain an `expr` that computes an output table column value, the units on the output column have the units attached to that `expr` as described below.




The units attached to an `expr` depend on the form of the `expr`:

  * Literal values by themselves do not have units. But numeric (_Int_ or _Double_) literals can be given units by following the value with a string specifying the unit. Thus `3 "By"` is an `expr` with value 3, whose type is _Int_ , and whose unit is bytes (`By`).

  * Column reference expressions get units from the named column in the input table, if it has units.

  * Functions and operators derive the unit of measurement for their output values from the unit of their input values. So, if `amount` has unit `By` and `time` has unit `s`, then `amount / time` has unit `By/s`. Functions that take two numeric arguments typically require both arguments to have units or neither argument to have units. The documentation for each function describes the treatment of units of measurement by that function.

Many functions have a requirement about unit agreement. For example `add` requires both of its operands, if they have units, to have the same unit. These requirements are described in the documentation for each function.

  * The functions `scale` and `cast_units` have functionality specific to units.

The `scale` function will multiply a value with one unit by a scale factor that converts it to a value with a different unit. So for `expr` `ev` with unit "KiBy" (kibi-bytes), `scale(ev, "By")` will result in multiplying `ev` by 1024 and giving the result unit `By`. It is equivalent to `ev * 1024 'By/KiBy'`.

The `cast_units` function returns its argument with a given unit regardless of the argument's original unit, if any. So `cast_units(ev, 'By/s')` results in the value of `ev`, unchanged but with the unit `By/s`.




The subset of UCUM units supported by MQL is given by string values that follow this grammar:
    
    
    digit : '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    exponent : [ '+' | '-' ] { digit }
    simple_unit : [ PREFIX_SYMBOL ] ATOM_SYMBOL
    annotatable : '10^' exponent | simple_unit
    component : annotatable [ annotation ] | '1'
    annotation : “{” ANNOTATION-STRING “}” | annotatable | annotation
    unit : component { '.' component } { '/' component }
    

A `simple_unit` specifies a unit given by an `ATOM_SYMBOL` optionally prefixed by a scaling factor given by a `PREFIX_SYMBOL`

An `ATOM_SYMBOL` gives a basic unit of measure:

text | meaning  
---|---  
s | second  
min | minute (60 seconds)  
h | hour (60 minutes)  
d | day (24 hours)  
wk | week (7 days)  
bit | bit  
By | byte (8 bits)  
% | 10^-2 (dimensionless ratio scaled to %)  
m | meter  
g | gram  
K | kelvin  
C | coulomb  
Hz | hertz (1/s)  
J | joule (kg.m.m/s/s)  
W | watt (kg.m.m/s/s/s) (J/s)  
A | amp (C/s)  
V | volt (kg.m.m/s/s/C) (J/C)  
  
A `PREFIX_SYMBOL` gives a scale factor for the basic unit it precedes:

text | meaning | scale  
---|---|---  
k | kilo | 10^3  
M | mega | 10^6  
G | giga | 10^9  
T | tera | 10^12  
P | peta | 10^15  
E | exa | 10^18  
Z | zetta | 10^21  
Y | yotta | 10^24  
m | milli | 10^-3  
u | micro | 10^-6  
n | nano | 10^-9  
p | pico | 10^-12  
f | femto | 10^-15  
a | atto | 10^-18  
z | zepto | 10^-21  
y | yocto | 10^-24  
Ki | kibi | 2^10  
Mi | mebi | 2^20  
Gi | gibi | 2^30  
Ti | tebi | 2^40  
Pi | pebi | 2^50  
  
A dimensionless unit can be given as `1` or as a power of 10 (`10^ exponent` such as `10^2`). The unit `1` is the unit given to most counter metrics. This also supports the dimensionless ratio scaled to percent `%`. So `10^-2` and `%` are the same units. To put it another way, adding 3 to a percentage is the same as adding .03 to the corresponding ratio. The `exponent` is limited to the range of -128 to 127.

An `annotation` is a comment that may be attached to an `annotatable` (`simple_unit` or power of 10) and does not change the meaning of the unit. An annotation not attached to a unit is treated as if it was attached to the unit `1`. Thus `{queries}/s` is equivalent to `1/s`, with the `1` unit decorated with `{queries}`.

A unit string can be made up of multiple `component` strings, connected by `.` or `/`. The `.` connector indicates multiplication of the units and the `/` connector, division. The multiplication and division are applied left to right. The subset of UCUM units that MQL supports requires all division connectors to come after multiplication connectors. This avoids the problem of writing the units of acceleration as `m/s.s` when `m/s/s` is what is wanted. Note that in UCUM units, `m/s.s` is the same as `m.s/s` or just `m`.

Two unit strings are _equivalent_ if they have the same _dimension_ and _scale_ , regardless of annotations. The dimension and scale are determined in the conventional way:

  * Each `component` is either dimensionless or has a dimension that is some combination of _time_ , _length_ , _data_ , _mass_ , or _charge_. For example both `bit` and `By` have dimension _data_. The dimensions of a unit string are found by converting each annotatable to its dimension, multiplying and dividing these as given by the unit string, and canceling dimensions that appear in the numerator and denominator. Thus `b.h/s` (bit-hour per second) has dimension _data_ times _time_ divided by _time_ , and the _time_ dimension cancels to leave dimension _data_.

  * Each annotatable has a scale relative to the basic units of its dimension. For example `h` (hour) has dimension _time_ with basic unit `s` and a scale factor of 3600 (every hour is 3600 seconds). The scale factor of a unit string is the combination of the scale factors of each `component` combined by multiplication and division.




Numeric literals can be given units by following the value with the string for the desired unit of measurement. So `3 "m/s"` is the value `3` with unit `m/s` and `10.8 "km/h"` represents the same speed as the value `10.8` with unit `km/h`.

A value with one unit can be scaled to have a different unit with the same dimension using the `scale` function. For example, `MiBy` and `By` have the dimension _data_ with scale factor 8*1024 and 8 respectively (relative to the base unit of dimension _data_ , which is `bit`). A value `x` having unit `MiBy` can be scaled to a value having unit `By` by the expression `scale(x, "By")`. This multiplies `x` by 1024 and results in a value with unit `By`. It is equivalent to the expression `x * 1024 "By/MiBy"`, `size * 1024 "By/MiBy"` and the unit of the resulting expression is `MiBy.By/MiBy` or just `By`.

The `scale` function checks that the unit requested has the same dimension as the unit of the value being scaled.

If `size` is a column whose value has unit "KiBy", then the expression `scale(size, "By")` is the same as `size * 1024 "By/KiBy"` and the unit of the resulting expression is `MiBy.By/MiBy` or just `By`.

There are a limited number of cases where MQL will automatically adjust or supply units for a value.

  * For a function _f_ that require two arguments with equivalent units (`add`, `sub`, any of the numeric comparison operators, `if`, and `or_else`), one of the arguments may be a call on the `scale` function without the second unit argument. If the unit of the other argument to _f_ has the same dimension as the unit of the argument to the `scale` function, then the `scale` function's second argument will be automatically set to the units of the other argument to _f_. This causes the units of two arguments to _f_ to be equivalent and _f_ will be able to operate.

For example, The `+` operator requires its arguments to have equivalent units because it makes no sense to add two numbers with different units. If `cache_size` has unit `By` and `heap_size` has unit `MiBy`, then the expression `scale(cache_size) + heap_size` is equivalent to the expression `scale(cache_size, "MiBy") + heap_size`

  * For any comparison function, if one argument is a literal with a unit having the same dimension but different scale than the other argument, the literal is scaled to have the same scale.

For example, if 'cache_size' has unit `By`, the expression `cache_size < 3 "KiBy"` is equivalent to the expression `cache_size < 3072 "By"`. Note that this is not the same as `cache_size < scale(3 "KiBy", "By")` if `cache_size` is type _Int_ , because `scale` will convert its result to type _Double_ which might reduce the precision of the comparison. The integer scaling in this case takes into account proper rounding and handling of overflow for the particular comparison done.

  * For either argument of `mul` or the divisor of `div`, a literal without a unit will be given unit '1'. This takes into account scaling operations that are _not_ intended to change units (for example, asking what if the rate were double what it is). To change units, it is best to use `scale`, which will automatically select the right scale factor for the conversion.




Unit errors are treated as warnings when evaluating a query, so the query will still produce results. When defining an alert, unit errors are are treated as real errors and will prevent the alert from being defined.

It is important to realize that _Duration_ and _Date_ are NOT numeric types and do not have units. The _Duration_ value `60s` is a non-numeric length of time, exactly the same length of time as `1m` or `60000ms`. The expression `60s` == `60000ms` is valid and true.

A numeric value with unit of time is different. The numbers `3 'min'` and `180 's'` are two different numeric values (3 and 180) with different units. Without scaling, it is not valid to compare them.

The `scale` function will convert _Duration_ and _Date_ values to _Double_ values with units. For example `scale(60s, "min")`, `scale(1m, "min")`, and `scale(60000ms, "min")` will all return the double value `1.0` with unit `min`.

### Table Operation Shortcuts

A shortcut is a simplified way of specifying a basic table operation.
    
    
    shortcut_table_op : shortcut { ',' arg } .
    shortcut : table_name | '(' expr ')' | map | DURATION .
    

There are a number of forms of shortcut table operations, each of which designates a kind of basic table operation:

  * A function promotion shortcut looks like a normal table operation, but the table operation starts with an `ID` that names a function instead of a table operation and the `arg` elements that follow (which are all `expr` form) are the arguments to the function.

The function is _promoted_ by providing a table operation that the function becomes an argument for. The value column or columns of the input table become the first arguments to the function, as if it had been preceded by a `.` operator. The specific promotions are as follows:

    * An ordinary function becomes the argument of a `value` table operation, computing the single value column of its output table.

For example, `| add 3` is a shortcut for `value [.add(3)]` and `| div` is a shortcut for `| value [.div]`.

    * An aggregating function becomes the second argument of a `group_by` table operation whose first argument is the empty `map` (`[ ]`). Thus the function computes the single value column of an output table with no time series identifier columns (a table with a single time series).

For example `| min` is a shortcut for `| group_by [], [.min]`.

    * An aligning function becomes the argument to an `align` table operation, thus performing its designated kind of alignment on the time-series of the input table.

For example, `| delta 10m` is a shortcut for the table operation `| align [.delta(10m)]`.

  * A naming shortcut starts with a `table_name` which is used as the argument to `resource`, `metric`, or `fetch` table operation, depending on what kind of thing the `table_name` names.

For example, `| gce_instance` is a shortcut for the table operation `| resource gce_instance` and `| gce_instance :: compute/instance/cpu/usage_time` is shortcut for `| fetch gce_instance :: compute/instance/cpu/usage_time`.

  * A filtering shortcut consists of a parenthesized `expr` which becomes the predicate in a `filter` table operation.

For example, `| (job == 'search')` is a shortcut for `| filter job == 'search'`.

  * A grouping shortcut starts with a `map` which becomes the first argument to a `group_by` table operation. It may be followed by an `arg` that is a `map` that describes the aggregation that computes the value columns of the output table.

For example, `| [zone]` is a shortcut for `| group_by [zone]`.

  * A duration shortcut starts with a `DURATION` with no following `arg`. It becomes a `for` table operation, giving the overall extent in time of the query operation.

For example, `| 10m` is a shortcut for `| for 10m`.




### Table Operation and Function Descriptions

Each Monitoring Query Language table operation and function description starts with a documentation signature indicating the table inputs (for table operations) and the types of arguments that can be given for the table operation or function. This section describes the form of these signatures.

Note that these signatures are NOT part of the Monitoring Query Language itself. They are used to describe the Monitoring Query Language.

A table operation signature optionally starts with a type that describes the input table(s) to the table operations followed by the name of the table operation followed by an argument list describing the valid arguments to the table operation. For example, a signature of the `group_by` table operation:

_Table_ `| group_by` _tsid: RowToTSID_`,` _window: lit-WindowDuration_`,` _value: [ RowSetToVal ]_

This table operation takes a `Table` as input (the most common case), and has 3 potential arguments, described by _tsid: RowToTSID_ , _window: lit-WindowDuration_ , and _value: [ RowSetToVal ]_.

The input table and `|` are optional and if not given the table operation does not take an input table. The input table specification is one of the following:

  * _Table_ The input to the table operation is a single table.
  * _Table++_ The table operation takes two or more tables as input.
  * _Resource_ The table operation takes a collection of tables specified by a monitored-resource type (all tables containing time series whose type includes a particular monitored-resource type).
  * _ResourceOrTable_ Either _Table_ or _Resource_ is allowed as input.



Each argument descriptor in the argument list that follows the name of the table operation has the following parts:

  * It may be preceded by an argument name, e.g. _`tsid:`_ , which gives a name that the argument can be referenced by in descriptions.

  * It may be enclosed in _`[`_ _`]`_ , in which case it is optional and the actual argument can be given as `_` or omitted if the actual argument is positioned after all explicitly given arguments.

  * It may have a _`lit-`_ prefix that indicates the argument value must be a constant value known before we evaluate the query.

  * It always has the name of a value type or a class of types (described below) that describes the allowed type of the actual argument.

  * It may have a suffix giving a time series kind which constrains the time series kind of the input value.




The argument descriptor type name may be one of the actual types described here: _Bool_ , _Int_ , _Double_ , _Distribution_ , _String_ , _Duration_ , or _Date_. In that case the actual argument must be an expression of the same type.

The following indicate that the actual argument must be a `table_name` that names a metric, monitored resource, or table, respectively:

  * _MetricName_
  * _ResourceName_
  * _TableName_



An argument descriptor may name a category that indicates the actual argument may be an expression of one of various types:

  * _Num_ Either an _Int_ or _Double_.
  * _Summable_ Types of values that can be summed: _Int_ , _Double_ , or _Distribution_.
  * _Comparable_ : Types of values that can be compared: _Int_ , _Double_ , _String_ , _Bool_ , _Duration_ , _Date_.
  * _ColumnValue_ : Types that are a valid column values: _Int_ , _Double_ , _String_ , _Bool_ , or _Distribution_.
  * _Windowed(Num)_ A _Num_ , potentially annotated by `within`, `ago`, or `bottom` functions.
  * _WindowDuration_ A _Duration_ , potentially annotated by `window` or `sliding`.
  * _BucketSpecification_ A bucket specification for a _Distribution_.



A table operation may require a `map` argument specifying the output row time series identifier columns or value columns. This is indicated by one of the following:

  * _RowToTSID_ A map describing the time series identifier columns of the output table.
  * _TSIDSel_ A map naming time series identifier columns to be retained. Each `maplet` in the `map` must consist only of an `expr` that names a column (`ID` or `column_name`). For example, `[zone, name]` causes the output columns to consist only of the input time series identifier columns `zone` and `name`, with all other input columns dropped.
  * _RowToVal_ A map describing output table value columns. If a non-map expression is given as an actual argument, it is promoted to be a single-element map with that expression.
  * _RowSetToVal_ A map describing output table value columns by aggregation. If a non-map expression is given as an actual argument, it is promoted to be a single-element map with that expression.
  * _DefaultColumns_ A map describing default value columns for an `outer_join`. If a non-map expression is given as an actual argument, it is promoted to be a single-element map with that expression.



A function signature starts with the name of the function followed by a parenthesized argument list describing the valid arguments to the function followed by a return type describing the value returned by the function. For example, the signature of the `fraction_less_than` function:

`fraction_less_than(`_Summable_`,` _lit-Num_`)` → _Double_

This function takes two arguments described by _Summable_ and _lit-Num_ and returns a value of type _Double_. The argument list has the same elements described above for table operations. The return type can be a specific value type, indicating the returned value will be of that type, or one of the following:

  * _Num_ \- If any of the arguments to the function are _Double_ , then _Double_ , otherwise, _Int_.
  * _ColumnValue_ \- The same type as the first actual argument to the function.
  * _LastArgType_ \- The same type as the last actual argument to the function.
  * _Windowed()_ \- The same type as the _Windowed_ actual argument, annotated with the _Windowed_ type. If the _Windowed_ actual argument was type _Int_ , then the return type is _Windowed(Int)_. (See `within`, `ago`, or `bottom` functions.)



A function argument descriptor or return type may have an indicator controlling the time series kind of the argument or result. These appear as one of the following suffixes to the type:

  * _.Cumulative_ , _.Delta_ , or _.Gauge_ indicate the actual argument must have the given time series kind.
  * _.CumulativeOK_ means that an actual argument can be _Cumulative_.
  * _.FirstArgKind_ means, for return types only, the same time series kind as the first argument to the function.



If an argument has no time series kind suffix, the argument must be _Gauge_ or _Delta_ time series kind. If a return type has no time series kind suffix, it will be _Gauge_.

A function signature may also have one or more of the following notes:

  * _(implicit row input)_ This indicates the function takes the whole row as an implicit input. For example, the `hash_tsid` function produces a hash of the time series identifier columns of its input row, but does not take those column values as explicit arguments.
  * _(temporal only)_ This is used on the signature of aggregation functions to indicate the function signature only applies when doing temporal aggregation. (Other signatures for the function apply otherwise.) Note that this includes the case of both temporal aggregation and spatial aggregation are being done in the same table operation.
  * _(sliding temporal only)_ This is used on the signature of aggregation functions to indicate the function signature only applies when doing sliding temporal aggregation. (Other signatures for the function apply otherwise.) Note that this includes the case of both sliding temporal aggregation and spatial aggregation are being done in the same table operation.



## Table Operations

This section describes each of the basic table operations in the Monitoring Query Language.

  * Fetching
    * `fetch` Produces a table from the database.
    * `metric` Produces the table for a specific metric type from a set of tables.
    * `fetch_cumulative` Produces a table of _Cumulative_ time series from the database.
  * Selection
    * `filter` Filters rows from an input table by a predicate.
    * `top` Selects the top time series by a sort-value expression.
    * `bottom` Selects the bottom time series by a sort-value expression.
    * `top_by` Selects time series by a sort-value expression in different groups.
    * `bottom_by` Selects time series by a sort-value expression in different groups.
    * `pick_bottom_rows` Picks rows by minimal sort-value expression.
    * `pick_top_rows` Picks rows by maximal a sort-value expression.
  * Row Modification
    * `map` Rewrites the time-series identifier and value columns of each row in a table.
    * `value` Rewrites the value columns of each row in a table.
    * `time_shift` Shift time series forward in time.
  * Time Series Alignment
    * `align` Produces an aligned table using an alignment function.
  * Aggregation
    * `group_by` Aggregates rows by mapped time-series identifier and time window.
    * `union_group_by` Aggregates rows from multiple tables.
    * `unaligned_group_by` Aggregates rows by mapped time-series identifier without alignment.
  * Union and Join
    * `join` Natural join of multiple tables.
    * `outer_join` Outer natural join of two tables.
    * `union` Union of multiple tables.
  * Time Horizon and Period
    * `every` Specifies the period for aligned table output.
    * `within` Specifies the time range of the query output.
    * `graph_period` Specifies the preferred output period for drawing time series graphs.
    * `window` Specifies the window for alignment operations.
  * Alerting
    * `condition` Add a boolean condition column to the input table.
    * `absent_for` Create a condition for the absence of input.
  * Miscellaneous
    * `ident` Identity table operation: no change to the input table.
    * `ratio` Computes the ratio of value columns of two aligned input tables.
    * `filter_ratio` Computes the ratio of two filtered sums of the input value column.
    * `filter_ratio_by` Computes a grouped ratio of two filtered sums of the input value column.



### Fetching

The output of a `fetch` table operation is a table retrieved by name from the Cloud Monitoring time series data base.

The `resource` table operation's output is the set of all tables that have the named monitored-resource type in their name. Each `resource` must eventually be followed by a `metric` table operation that selects the single table whose name contains that metric. Prior to the `metric` table operation, there may be `filter` table operations that restrict the rows included in the resulting tables.

#### `fetch` Produces a table from the database.

* * *

Signature: `fetch` _name: lit-TableName_

The `fetch` operation fetches from the time series database the table whose name is the table name given by the _name_ argument. It is an error if the table name contains an unknown monitored-resource type or metric type name.

This table will be empty if no metric of the given type was collected from the monitored resource of the given type.

If the metric is _Cumulative_ , the time series that make up the table are effectively converted to _Delta_ time series, where each point represents the change in value since the next-earlier point.

The `fetch` operation can also fetch the set of all tables that are based on a particular monitored resource by just giving the name of the monitored resource and not giving a metric name. Such a `fetch` operation must be followed by a `metric` operation that selects the specific table containing the data for a specific metric. The only operation that may come between such a `fetch` and the subsequent `metric` is a `filter` operation, that filters based on the monitored resource columns.

This form of `fetch` is useful if we wish to fetch more than one metric for a given monitored resource as in this example:
    
    
      fetch gce_instance | filter zone = 'asia-east1-a' |
      { metric compute.googleapis.com/instance/cpu/utilization ;
        metric compute.googleapis.com/instance/cpu/reserved_cores
      } | join | div
    

This is equivalent to
    
    
      { fetch gce_instance :: compute.googleapis.com/instance/cpu/utilization ;
        fetch gce_instance :: compute.googleapis.com/instance/cpu/reserved_cores
      } | filter zone = 'asia-east1-a' | join | div
    

#### `metric` Produces the table for a specific metric type from a set of tables.

* * *

Signature: _Resource_ `| metric` _name: lit-MetricName_

The table input to a `metric` table operation is a set of tables produced by a `fetch` table operation that did not give a metric name.

The `metric` table operation selects the one table from this set whose metric name is given by the _name_ argument and produces that table as its output.

It is an error if there is no metric definition with the given name. It produces an empty table if there is no input table with data for the given metric name.

The `metric` table operation is useful if we wish to fetch more than one metric for a given monitored resource as in this example:
    
    
      fetch gce_instance | filter zone = 'asia-east1-a' |
      { metric compute.googleapis.com/instance/cpu/utilization ;
        metric compute.googleapis.com/instance/cpu/reserved_cores
      } | join | div
    

This is equivalent to
    
    
      { fetch gce_instance :: compute.googleapis.com/instance/cpu/utilization ;
        fetch gce_instance :: compute.googleapis.com/instance/cpu/reserved_cores
      } | filter zone = 'asia-east1-a' | join | div
    

#### `fetch_cumulative` Produces a table of _Cumulative_ time series from the database.

* * *

Signature: `fetch_cumulative` _name: lit-TableName_

The `fetch_cumulative` table operation is the same as the `fetch` table operation except that _Cumulative_ metrics are not automatically converted to _Delta_ metrics when fetched.

### Selection

The selection table operations select rows from the input table for inclusion in the output table. The type of the output table is exactly the same as that of the input table.

#### `filter` Filters rows from an input table by a predicate.

* * *

Signature: _ResourceOrTable_ `| filter` _predicate: Bool_

The `filter` operation evaluates its _predicate_ argument for each row in a single input table or in the collection of tables named by a `resource` operation. Exactly those rows in the input table or tables for which _predicate_ evaluates to true are retained in the output table or tables.

If the input is a collection of tables, only the monitored resource labels (which are common to all the tables) can be referenced in the predicate.

#### `top` Selects the top time series by a sort-value expression.

* * *

Signature: _Table_ `| top` _number: lit-Int_`,` _sort_value: [ Windowed(Num) ]_

The `top` table operation creates an output table with the _number_ time series from the input table with the highest value computed by the _sort_value_ argument.

The _sort_value_ argument is applied to rows in a time series that fall within a value time window. The default value time window is the same as the query time window. If _sort_value_ is an aggregating expression (e.g. `.min`), it is an aggregation over all the rows whose end timestamp is within the value window. If the expression is a value expression (e.g. `.val(0)/.val(1)`), it is applied to the youngest row, if any, within the value window. If there are no rows within the value window for a time series, or if the _sort_value_ argument does not produce a value for a time series, that time series is not considered for inclusion in the output.

The `within` function can be used in the _sort_value_ argument to modify the value window by giving a starting time, a duration, and/or an ending time for the window.

Examples:

This selects 3 time series with the largest value for the most recent point in the time series:
    
    
      | top 3
    

This selects 7 time series with the largest value for the maximum of all the points in the time series within the query window:
    
    
      | top 7, .max
    

This selects 3 time series with the largest value of the `min` reducer applied to the rows in each time series that fall in a window starting 10 hours ago and lasting for 1 hour:
    
    
      | top 3, .min.within(-10h, 1h)
    

#### `bottom` Selects the bottom time series by a sort-value expression.

* * *

Signature: _Table_ `| bottom` _number: lit-Int_`,` _sort_value: [ Windowed(Num) ]_

The `bottom` table operation creates an output table with the _number_ time series from the input table with the lowest value computed by the _sort_value_ argument.

The _sort_value_ argument is applied to rows in a time series that fall within a value time window. The default value time window is the same as the query time window. If the expression is an aggregating expression (e.g. `.min`), it is an aggregation over all the rows whose end timestamp is within the value window. If the expression is a value expression (e.g. `.val(0)/.val(1)`), it is applied to the most recent row, if any, within the value window. If there are no rows within the value window for a time series, or if the _sort_value_ argument does not produce a value for a time series, that time series is not considered for inclusion in the output.

The `within` function can be used in the _sort_value_ argument to modify the value window by giving a a starting time, a duration, and/or an ending time for the window.

Examples:
    
    
      | bottom 3
    

Select 3 time series with the smallest value for the youngest point in the time series.
    
    
      | bottom 7, .min
    

Select 7 time series with the smallest value for the minimum of all the points in the time series within the query window.
    
    
      | bottom 3, .max.within(10h)
    

This selects 3 time series with the smallest value of the `max` reducer applied to the rows in each time series that fall in a window starting 10 hours ago and lasting until now.

#### `top_by` Selects time series by a sort-value expression in different groups.

* * *

Signature: _Table_ `| top_by` _tsid: TSIDSel_`,` _number: lit-Int_`,` _sort_value: [ Windowed(Num) ]_

The `top_by` table operation groups time series together that have the same time-series identifier computed by the _tsid_ argument. Within each group it selects time series by the same method that `top` does when given the same _number_ and _sort_value_ arguments. For each group, it computes a sort value from the _sort_value_ argument for each time series in a group and selects the _number_ time series with the largest value given by _sort_value_.

The _sort_value_ argument is applied to rows in a time series that fall within a _value time window_. The default value time window is the same as the query time window. If the expression is an aggregating expression (e.g. `.min`), it is an aggregation over all the rows whose end timestamp is within the value window. If the expression is a value expression (e.g. `.val(0)/.val(1)`), it is applied to the most recent row, if any, within the value window. If there are no rows within the value window for a time series, or if the _Windowed(Num)_ argument does not produce a value for a time series, then that time series is not considered for inclusion in the output.

The `within` function can be used in the _sort_value_ argument to modify the value window by giving a starting time, a duration, and/or an ending time for the window.

Examples:

For each group of time series with the same value of the 'zone' column, this selects the three time series with the largest value for the most recent point in the time series:
    
    
      | top_by [zone], 3
    

The following computes the sort value for each time series as the maximum value of all the points in the time series. Then for each group of time series with the same value of the `project_id` label, it selects the two time series with the largest sort value. Note that the time series identifier columns of the selected rows are not changed from the input.
    
    
      | top_by [project_id], 2, .max
    

The following computes the sort value for each time series as the minimum value of all the points in the time series whose end timestamp falls in the one-hour interval starting 10h ago. Then for each group of time series with the same value of the `zone` label, it selects the time series with the largest sort value. As above, the time series identifier columns of the selected rows are not changed from the input.
    
    
      | top_by [zone], 1, .min.within(-10h, 1h)
    

#### `bottom_by` Selects time series by a sort-value expression in different groups.

* * *

Signature: _Table_ `| bottom_by` _tsid: TSIDSel_`,` _number: lit-Int_`,` _sort_value: [ Windowed(Num) ]_

The `bottom_by` table operation groups time series together that have the same time-series identifier computed by the _tsid_ argument. Within each group it selects time series by the same method that `bottom` does when given the same _number_ and _sort_value_ arguments. For each group, it computes the _sort_value_ for each time series in a group and selects _number_ time series with the smallest sort value.

The _sort_value_ argument is applied to rows in a time series that fall within a value time window. The default value time window is the same as the query time window. If the expression is an aggregating expression (e.g. `.min`), it is an aggregation over all the rows whose end timestamp is within the value window. If the expression is a value expression (e.g. `.val(0)/.val(1)`), it is applied to the youngest row, if any, within the value window. If there are no rows within the value window for a time series, or if the _sort_value_ argument does not produce a value for a time series, that time series is not considered for inclusion in the output.

The `within` function can be used in the _sort_value_ argument to modify the value window by giving a starting time, a duration, and/or an ending time for the window.

Examples:
    
    
      | bottom_by [zone], 1
    

For each group of time series with the same value of the 'zone' column, this selects the time series with the smallest value for the youngest point in the time series.
    
    
      | bottom_by [project_id], 2, .max
    

For each group of time series with the same value of the 'project_id' column, this this selects the 2 time series with the smallest value for the maximum of all the points in the time series within the query window.
    
    
      | bottom_by [zone], 1, .min.within(1h)
    

For each group of time series with the same value of the 'zone' column, this selects the time series with the smallest value of the `min` reducer applied to the rows in each time series that fall in a window starting 10 hours ago and lasting for 1 hour.

#### `pick_bottom_rows` Picks rows by minimal sort-value expression.

* * *

Signature: _Table_ `| pick_bottom_rows` _number: lit-Int_`,` _tsid: [ TSIDSel ]_`,` _sort_value: [ Num ]_

The `pick_bottom_rows` table operation groups rows together that have the same time-series identifier computed by the _tsid_ argument and the same end time. A sort value is computed for each row by applying the _sort_value_ argument expression. Within each group of rows, _number_ rows with the smallest sort-value are selected and are added to the output unchanged.

#### `pick_top_rows` Picks rows by maximal a sort-value expression.

* * *

Signature: _Table_ `| pick_top_rows` _number: lit-Int_`,` _tsid: [ TSIDSel ]_`,` _sort_value: [ Num ]_

The `pick_top_rows` table operation groups rows together that have the same time-series identifier computed by the _tsid_ argument and the same end time. A sort value is computed for each row by applying the _sort_value_ argument expression. Within each group of rows, _number_ rows with the largest sort-value are selected and are added to the output unchanged.

### Row Modification

#### `map` Rewrites the time-series identifier and value columns of each row in a table.

* * *

Signature: _Table_ `| map` _tsid: [ RowToTSID ]_`,` _value: [ RowToVal ]_

The `map` table operation applies two transformations to each of the rows of a table, one at a time:

  * If the _tsid_ map argument is given, it is applied to the time-series identifier columns of that row to produce the time-series identifier columns of the corresponding output row. If the _tsid_ map argument is not given (or given as `_`), then the output time-series identifier columns are the same as the input.

  * If the _value_ map argument is given, it is applied to the value columns of the input row to produce the value columns of the output row. If the _RowToVal_ map is not given, then the output value columns are the same as the input.




It is a dynamic error if rows from two different time series in the input have the same time-series identifier columns after applying the _tsid_ map argument. In this case, all the rows derived from one of the two input time series are dropped from the output and an error message will be given.

If the _tsid_ map contains references to value columns or time columns, then it is possible that it will split single input time series into multiple output time series. For this reason, when the _tsid_ map contains references to value columns or time columns, it is only allowed to apply it to tables whose value columns are _Gauge_ or _Delta_ time series kind.

#### `value` Rewrites the value columns of each row in a table.

* * *

Signature: _Table_ `| value` _value: RowToVal_

For each row in the input _Table_ , the _RowToVal_ map is applied to the columns of that row to produce the value columns of the corresponding output row. Each output row has the same time-series identifier and time columns as the input row it was produced from and has the value columns produced by the _RowToVal_ map.

#### `time_shift` Shift time series forward in time.

* * *

Signature: _Table_ `| time_shift` _shift: lit-Duration_

Each row in the input table has the amount given by the _shift_ argument added to its time column or columns. This has the effect of shifting each time series in the table forward in time by the amount given by _shift_.

If the input table is aligned, then the shift amount must be an even multiple of the alignment period, which maintains the input table alignment.

### Time Series Alignment

#### `align` Produces an aligned table using an alignment function.

* * *

Signature: _Table_ `| align` _aligner: [ Aligner ]_

The `align` table operation uses the alignment function given by its _aligner_ argument to output an aligned version of its input table. Each time series in the input table is aligned using the _aligner_ function is applied to produce an time series in the output table.

The alignment base time is the end time of the query window and the alignment period is set by one of the three following things:

  * An `every` table operation that sets the period for this `align` table operation.

  * The aligner function requires that the alignment period be equal to its window width (see the `delta`).

  * An external graphics interface requires a particular alignment period.




The particular method of producing aligned time series is described for the alignment function given by the _aligner_ argument.

### Aggregation

An aggregation table operation divides the rows of the input table into groups. For each group of input rows it computes a common time-series identifier and time columns for the group, aggregate the input rows to create the value output columns, and outputs a single row with the resulting time series identifier, time, and value columns.

There are three kinds of aggregation

  * _Spatial aggregation_.  This form of aggregation computes new time series id columns for each input row and groups all the rows with the same new time series id columns and end time together. This kind of aggregation typically requires aligned input so that rows from different time series will line up in time to be grouped together.

  * _Temporal aggregation_.  This form of aggregation computes a set of valid aligned output times and computes a new end time for each row giving it the oldest aligned end time that is no earlier than the row's original end time. Rows with the same time-series identifier and end time are grouped together.

  * _Sliding temporal aggregation_.  This form of aggregation is similar to temporal aggregation except that a row may be included in more than one group. This computes a set of time windows, each having an later edge at a valid aligned end time and each having the same fixed width. A row is given an end time that is the later edge of each window it falls within and the row is grouped with any other rows having the same time-series identifier and new end time. When the windows overlap, a row may be given more than one new end time and thus may be included in more than one group.




It is possible to combine spatial aggregation with one of the two forms of temporal aggregation in one table operation.

An important distinction between sliding and non-sliding temporal aggregation is that some aggregators (e.g. sum) will produce values with _Delta_ time-series kind for non-sliding temporal aggregation but _Gauge_ kind for sliding temporal aggregation. The reason for this is the time extents for two points in a _Delta_ time series cannot overlap, so the overlapping input windows of sliding temporal aggregation cannot be represented in the time columns of _Delta_ time series output rows.

When a new time-series identifier is computed for a row, the new time series identifier is computed by a map argument. The value columns for the output row are computed by a map argument with an aggregating expression computing each value column.

#### `group_by` Aggregates rows by mapped time-series identifier and time window.

* * *

Signature: _Table_ `| group_by` _tsid: RowToTSID_`,` _aggregator: [ RowSetToVal ]_   
_Table_ `| group_by` _tsid: RowToTSID_`,` _window: lit-WindowDuration_`,` _aggregator: [ RowSetToVal ]_   
_Table_ `| group_by` _window: lit-WindowDuration_`,` _aggregator: [ RowSetToVal ]_

The `group_by` table operation groups rows together by mapping the time series-identifier columns, time columns, or both:

  * If the _tsid_ argument is given and the _window_ argument is not, `group_by` computes the time-series identifier produced by the _tsid_ argument for each row in the input table and groups together all rows with the same produced time-series identifier and end time.

In this case `group_by` requires an aligned table as input so that different time series have points with the same end time. If the input table is not aligned, then an `align` table operation will automatically be inserted to provide alignment.

  * If the _window_ argument is given and the _tsid_ argument is not, a group of rows is produced for each time-series identifier and every aligned period output point. The rows in one group are all the rows with the given time-series identifier whose end time falls in a window between the output time and the time that is _window_ duration earlier.

If the _window_ argument has a `sliding` function call (e.g. `sliding(1h)`), then the window may be different than the alignment period. Otherwise, the _Duration_ argument must be the same as the alignment period. The expression `window()` represents a duration that is the same as the alignment period. If a non-sliding _Duration_ is given explicitly, it forces the period to be the same if no period was given explicitly.

  * If both the _tsid_ and _window_ arguments are given, a new mapped time-series identifier is computed for each row and a group is created for all the rows with the same mapped time-series identifier whose end time falls in a window between the output time and the time that is _window_ duration earlier.




An output row is produced for each group with the common time series identifier of the rows in the group and a timestamp that is the output point time of the group (_window_ was given) or the common end time of the rows in the group (_window_ was not given). The value columns in the group are produced by the _aggregation_ argument. Each aggregating expression is applied to the rows in the set and the result is the output row value column.

Some aggregating expressions (e.g. `sum`) will produce output value columns with _Delta_ or _Gauge_ time-series kind, depending on the kind of aggregation being done. This depends on whether or not sliding or non-sliding temporal aggregation is being done. For this purpose, aggregation is treated as temporal aggregation if it combines both temporal and spatial aggregation.

A `group_by` table operation always produces aligned output tables. If no _window_ argument is given, then the input table must be aligned and the output table will have the same alignment. If the _window_ argument is given, then an output point is only produced at an alignment time point and the output table is aligned.

Note that if the _tsid_ argument includes value or time columns in its expressions, it is possible that time series in the input table will be fractured into multiple time series in the output table. This is because each point or row in a time series can have different value or time columns from any other point in the time series and if that value is copied to a time-series identifier column, then the point will be in a different time series.

#### `union_group_by` Aggregates rows from multiple tables.

* * *

Signature: _Table++_ `| union_group_by` _tsid: RowToTSID_`,` _aggregator: [ RowSetToVal ]_   
_Table++_ `| union_group_by` _tsid: RowToTSID_`,` _window: lit-WindowDuration_`,` _aggregator: [ RowSetToVal ]_   
_Table++_ `| union_group_by` _window: lit-WindowDuration_`,` _aggregator: [ RowSetToVal ]_

The `union_group_by` function aggregates input rows exactly like the `group_by` function except that it takes its input rows from multiple input tables.

All the input tables input to a `union_group_by` must have the same columns (same name, same type, and, for value columns, same time-series kind). If aligned input tables are required by the arguments to 'union_group_by' (no _window_ argument given), then all the input tables must be aligned with the same period.

#### `unaligned_group_by` Aggregates rows by mapped time-series identifier without alignment.

* * *

Signature: _Table_ `| unaligned_group_by` _tsid: TSIDSel_`,` _aggregator: [ RowSetToVal ]_

The `unaligned_group_by` table operation does the same thing as the `group_by` table operation, but does not require its input table to be aligned.

This computes the time-series identifier produced by the _tsid_ map argument for each row in the input table and groups together all rows with the same resulting time-series identifier and end time. All the rows in the group have the same end time and should have the same start time. If any two rows in a group have different start time, issue a dynamic error and arbitrarily choose one of the rows and remove it from the group.

Produces an output row for each group of the above group of rows. The output row has the time-series identifier produced by _tsid_ map argument and the same end time and (if present) start time as the input rows in the group. It has value columns produced by the _aggregation_ map argument applied to all the rows in the group.

The `unaligned_group_by` table operation does not require its input table to be aligned, which may mean that it is unlikely for there to be multiple rows in a group to aggregate. It does require that the rows collected into one output time series (all having the same time-series identifier) do not have end times whose density gives more than one row per second.

### Union and Join

#### `join` Natural join of multiple tables.

* * *

Signature: _Table++_ `| join`

The `join` table operation takes two or more input tables and combines the rows in these table into rows in a single output table by doing a natural inner join on the time-series identifier and end time columns of the input tables.

Besides being aligned, the input tables must all be aligned with the same period and must all be of _Delta_ or _Gauge_ time-series kind. If an input table is not aligned, then an `align` table operation will automatically be inserted to provide alignment.

The output table will have the following elements:

  * One time-series identifier column for every unique time-series identifier column in any of the input tables. Each column will have the same type as the corresponding column in the input tables. If two tables have time-series identifier columns with the same name but different types, that is an error.

  * An end time column. If any of the input tables is _Delta_ time series kind, the output table will also be _Delta_ time-series kind and have a start time column.

  * A value column for each input table value columns. The order is the order of the input tables in the `grouped_table_op` that produced them. It is an error if two different input tables have value columns with the same name.




The join considers every tuple consisting of one row from each input table. For each such tuple that meets the following conditions, an output row is created:

  * For each time-series identifier column name that appears in any of the input tables that column has the same value for each row in the tuple that has that column.

  * Every row in the tuple has the same end time.




Each such output row will have the following column values:

  * Each time-series column will have the value for that column as each row in the tuple that has that column.

  * Each time column will have the same value as the rows in the input tuple.

  * Each value column will have the same value as the row in the tuple that value column came from.




#### `outer_join` Outer natural join of two tables.

* * *

Signature: _Table++_ `| outer_join` _left_default_value: [ DefaultColumns ]_`,` _right_default_value: [ DefaultColumns ]_

The `outer_join` table operation takes two input tables and combines the rows in these table into rows in a single output table by doing a natural outer join on the time-series identifier and end time columns of the input tables.

One or both of the _left_default_value_ and _right_default_value_ arguments must be given. Each corresponds to one input table (the first, "left", table or the second "right" table) and, when given for a table, that table will have rows created if it does not have some row that matches a row in the other table. Each argument specifies the value columns of the created row. If a default argument is given for a table, then the time series identifier columns in that table must be a subset of the time series of those of the other table and it can only have _Delta_ time-series kind if the other table has _Delta_ time-series kind.

Besides being aligned, the input tables must all be aligned with the same period and must all be of _Delta_ or _Gauge_ time-series kind. If an input table is not aligned, then an `align` table operation will automatically be inserted to provide alignment.

As with `join` the output table will have the following elements:

  * One time-series identifier column for every unique time-series identifier column in any of the input tables. Each column will have the same type as the corresponding column in the input tables. If two tables have time-series identifier columns with the same name but different types, that is an error.

  * An end time column. If any of the input tables is _Delta_ time series kind, the output table will also be _Delta_ time-series kind and have a start time column.

  * A value column for each input table value columns. The order is the order of the input tables in the `grouped_table_op` that produced them. It is an error if two different input tables have value columns with the same name.




The join considers every pair consisting of one row from each input table. For each such pair that meets the following conditions, an output row is created:

  * For each time-series identifier column name that appears in either of the input tables that column has the same value for each row in the pair that has that column.

  * Each row in the pair has the same end time.




Each such output row will have the following column values:

  * Each time-series column will have the value for that column as each row in the pair that has that column.

  * Each time column will have the same value as the rows in the input pair.

  * Each value column will have the same value as the row in the pair that value column came from.




In addition to the pairs above, if a row in one table does cannot form a pair with any row in the other table and the other table has its corresponding default columns argument given, then a pair is created with the row that exists from one table table and a default row for the other table. The default row is constructed as follows:

  * Each of its time-series identifier columns and time columns has the same value as the corresponding column in the first table row.

  * The default row's value columns are constructed by the corresponding default column argument. If the table has a single value column, that default column argument can be a single literal expression. If the table has multiple value columns, the default column argument must be a map expression with one value for each value column, in the same order as the value columns in the input table and without a `label:` given.




#### `union` Union of multiple tables.

* * *

Signature: _Table++_ `| union`

The `union` table operation takes two or more input tables and produces a single output table containing rows from all the input tables.

The input tables must have the same columns (same name, same type, and, for value columns, same time-series kind). The produced output table will have the same columns as the input tables.

If any of the input tables are aligned, the output of `union` will be aligned. In this case any input table that is not aligned will have an `align` table operation automatically be inserted to provide alignment. The alignment period of all the input tables must be the same and that is the alignment period of the output.

In none of the input tables to the `union` operation are aligned, the output of the `union` operation will not be aligned.

It is a dynamic error if streams from two or more different tables have the same time-series identifier. In this case, one of the streams with a duplicate time-series identifier is chosen arbitrarily to be included in the output and the remainder are dropped.

### Time Horizon and Period

The period to use when aligning the time series in the table is set by the `every` command.

The query will produce all its results as points whose end time falls within a _query window_. The duration of the query window is set by the `within` table operation, which can specify any of a starting time, ending time, or duration.

#### `every` Specifies the period for aligned table output.

* * *

Signature: _Table_ `| every` _period: lit-Duration_

The `every` table operation requires an input table that is aligned with an input period given by the _period_ argument. This is handled in one of the following ways:

  * If the input table is aligned but does not have a specific required period, the query that is input to the `every` table operation is adjusted to produce output with the alignment period given by the _period_ argument. For example `fetch | align rate(1h) | every 10m` will set the output period of the `rate` aligner to 10 minutes so that points having the average rate over the previous 1h window are output every 10 minutes. For a query like `fetch | group_by | every 10m`, where the group_by causes an implicit `align` table operation to be inserted, the `every 10m` applies to that implicit `align` table operation.

  * It is an error if the input table is aligned with a specific period and that period is different from the one specified by the _period_ argument. For example `fetch | align delta(10m) | every 1h` is an error because the input to the `every` table operation will have a fixed alignment period of 10 minutes according to the rules of the `delta` aligner.

  * If the input table is not aligned, then an `align` operation is inserted with an appropriate aligner function for the input table. The _period_ argument to the `every` function specifies the alignment period for the aligner. For example `fetch | every 10m` will be rewritten to `fetch | align | every 10m` where the `align` will use a suitable aligner for the input table and produce output points every 10 minutes.




#### `within` Specifies the time range of the query output.

* * *

Signature: _Table_ `| within` _first: lit-DateOrDuration_`,` _last: [ lit-DateOrDuration ]_

The `within` table operation specifies the query output window. The end time of every point output by the query containing the `within` table operation will fall within this range. This operation should be appended to the end of the query.

The query output window is specified by giving one or two of three values: the starting time of the window, the ending time of the window, and the duration of the window as the _first_ and _last_ argument.

If either the _first_ or _last_ argument is a positive _Duration_ , then that sets the width of the window. At most one of the arguments can be a positive _Duration_.

If the _first_ argument is given by a _Date_ , then that specifies the starting time of the query window. If the _second_ argument is given by a _Date_ , that specifies the ending time of the query window. If both _first_ and _second_ are a date, the _second_ argument must come after the _first_ in time. For either _first_ or _second_ the value can be given as a _Date_ literal or with a negative _Duration_ literal. In the later case, the time is the specified amount of time earlier than the time the query was issued (now).

If only one argument is given, the _second_ argument (end time) defaults to the time the query was issued (now). In this case, if the _first_ argument is given by a _Date_ value, it must be earlier than the time the query is issued.

For example:
    
    
    | within 1h                   # one hour ending when the query was given
    | within d'2020/08/19 23:20'  # from the date to when the query was given
    | within 1d, d'2020/02/21 10:15'    # one day, ending at the given date
    | within -2d, 1d                    # one day, starting 2 days ago
    | within 1, -2d                     # one day, ending 2 days ago
    | within d'2020/02/21', d'2020/08/19'  # the interval between the two dates 
    

#### `graph_period` Specifies the preferred output period for drawing time series graphs.

* * *

Signature: _Table_ `| graph_period` _period: lit-Duration_

The `graph_period` table operation transforms its input table to make it suitable for presentation as a graph. Its _period_ argument indicates the period between points suitable for the graph.

This operation is automatically inserted in queries that are given to Metrics Explorer if the user does not explicitly add one to the query. In either event, Metrics Explorer sets the value of the _period_ argument to be appropriate for the actual time window of the chart. Explicitly giving adding `graph_period` as part of a query only makes sense if the query is being given to the API.

The `graph_period` operation compares its _period_ argument with the period of the input table and does one of the following:

  * If the period of the input table is less than half the _period_ argument, then the `graph_period` operation acts as a temporal reducer whose window and output period are given by the _period_ argument. Each value column in the input table is aggregated according to its type.

    * For a value column of numeric type, three columns are placed in the output table, each produced by aggregating the input column with the `min`, `mean`, and `max` aggregators. The output column names are the input column name with, respectively, `.min`, `.mean`, and `.max` appended.

    * For a value column of type _Bool_ , three columns are placed in the output table, each produced by aggregating the input column with the `min`, `mean`, and `max` aggregators. The output column names are the input column name with, respectively, `.all_true`, `.mean`, and `.any_true` append.

    * For a column of type _Distribution_ , a single column with the same name is created using `distribution` aggregation to combine the populations of all the distribution input values that fall in each graph period window.

  * If the input table period is more than twice the _period_ argument, then for each point in the input table, copies are made for the time points required by the output period.

  * If the input table period is less than twice the _period_ argument and more than half the _period_ argument, the input table is just copied to the output.




Note that if the input table has more than one value column or has a _String_ value column, its behavior is undefined. Metrics Explorer might only display a single column or give an error if there is no displayable column.

#### `window` Specifies the window for alignment operations.

* * *

Signature: _Table_ `| window` _window: lit-Duration_

The `window` table operation requires an input table that is aligned by an aligner function whose window _Duration_ argument is the same as the _window_ argument given on this `window` table operation. This is handled in one of the following ways:

  * If the input table is not aligned, then an `align` operation is inserted with an appropriate aligner function for the input table. The _Duration_ argument to the aligner function is given by this `window` table operation's _Duration_ argument.

  * If the table is aligned but the table operation that aligned it does not have a specific alignment window, the _window_ argument from this `window` table operation is used as the aligner window argument.

  * It is an error if the input table is aligned and the table operation that aligned specifies a window _Duration_ that is different from the Duration argument of this `window` table operation.




### Alerting

Alerting operations are used to define alert policies. Use these operations only to install alerts, not as part of a query.

Abstractly, these operations provide ways to create queries that result in a table with two value columns: a boolean indicating whether or not the alert should be in a firing state and a value of the same type as the input giving the most recent value of the input.

#### `condition` Add a boolean condition column to the input table.

* * *

Signature: _Table_ `| condition` _predicate: Bool_

The `condition` table operation adds a boolean value column to each input table row to create its output table. The value of this column is the value produced by the _predicate_ argument applied to the row.

This can be used to create an [alerting](https://cloud.google.com/monitoring/alerts) query. The output table has a a boolean column indicating that the alert condition is satisfied. The alerting facility will use this to determine if and when an alert should fire or stop firing.

The `condition` operation requires its input table to be aligned and to be generated by a query with an explicit alignment window. This is supplied by a window argument to an align operation (for example, `| align delta(10m)`), a temporal `group_by` with a sliding window (for example, `| group_by sliding(10m), sum(val())`), or by a `window` table operation. A `window` table operation sets the window for a prior aligning table operation.

Examples:
    
    
      fetch gce_instance :: compute.googleapis.com/instance/cpu/usage_time
      | rate (5m)
      | condition lt(val(), 0.5's{CPU}/min')
    

This query uses the `rate` aligner to compute a trailing 5-minute average, and the resulting units are `s{CPU}/s`. The condition then specifies the limit in terms of the seconds of CPU usage per minute. The result of the `condition` clause is a table with two value columns. The first column is a _Bool_ column that will be true if the input table `usage_time` value column is less than `.5`. The second column is a copy of the `usage_time` value column from the input.
    
    
      fetch gce_instance :: compute.googleapis.com/instance/cpu/usage_time
      | delta 1m
      | group_by 5m, mean(val())
      | condition lt(val(), 0.5 's{CPU}')
    

This query uses the `delta` aligner to ensure that the period for the values is 1 minute. The `group_by` clause computes the average of the values over a 5-minute period. This example uses a non-sliding `delta` clause, which isn't a problem because it's followed by a sliding window `group_by` clause.

#### `absent_for` Create a condition for the absence of input.

* * *

Signature: _Table_ `| absent_for` _duration: lit-Duration_

The `absent_for` table operation generates a table with two value columns, `active` and `signal`. The `active` column is true when there is data missing from the table input and false otherwise. This is useful for creating a condition query to be used to alert on the absence of inputs.

For each input time series, `absent_for` creates an aligned output time series with the same time-series identifier as the input. The alignment period is either given by a following `every` or is the default period.

The _duration_ argument gives a time limit. The `active` column for an output point will be false if there is a point in the input time series that is within this time limit earlier than the time of the output point. If there is no such input point, the `active` column will be true, indicating an absence of input within the time limit.

If the input table has value columns, the `signal` column will contain the value of first value column of the most recent input point (within the limit or not) in the input time series. If the input table has no value columns, the `signal` column in the output point will be an integer giving the number of minutes since the last input point.

For each output point time, the `absent_for` table operation will look back 24 hours before that time for an input point. If there is no input point in the prior 24 hours no point will be output for that time.

Examples:
    
    
      fetch  gce_instance :: compute.googleapis.com/instance/cpu/usage_time
      | absent_for 8h
    

For each `usage_time` time series from a virtual machine (`gce_instance`) the `absent_for` will generate an aligned time series whose output points will have an `active` column that is true if there is an input point within the last 24 hours but no points within the last 8 hours (`8h`). This is a suitable alerting query.
    
    
      fetch  gce_instance :: compute.googleapis.com/instance/cpu/usage_time
      | value [] | absent_for 8h
    
    

This is similar to the previous example, but the `| value []` removes the value columns from the input to the `absent_for` operation, so the `signal` column is set to the time (in minutes) since the last input point.

### Miscellaneous

#### `ident` Identity table operation: no change to the input table.

* * *

Signature: _Table_ `| ident`

The `ident` table operation produces an input table, unchanged.

Example:
    
    
      fetch  gce_instance :: compute.googleapis.com/instance/cpu/usage_time |
        { ident ; group_by [zone] } |
        join | value [zone_fraction: val(0) / val(1)]
    

For each row in the given table, compute the ratio of its value to the total of that value over all instances in the zone it is in.

#### `ratio` Computes the ratio of value columns of two aligned input tables.

* * *

Signature: _Table++_ `| ratio`

The `ratio` table operation takes two aligned input tables, the numerator table input and the denominator table input, respectively. Both table inputs should have exactly one value column of a numeric type.

The time-series identifier columns of the denominator table must be a subset of the time-series identifier columns of the numerator table. If both tables have the same time-series identifier columns (name and type) then a default value of zero will be used for the numerator when calculating ratios. If the numerator has more time-series identifier columns than the denominator, then an output point will only be produced when both numerator and denominator have a value.

#### `filter_ratio` Computes the ratio of two filtered sums of the input value column.

* * *

Signature: _Table_ `| filter_ratio` _numerator_predicate: Bool_`,` _denominator_predicate: [ Bool ]_

The `filter_ratio` table operation takes one input table that has exactly one value column of a numeric type. If the input table is not aligned, then an `align` table operation will automatically be inserted to provide alignment.

The `filter_ratio` operation aggregates all input rows at a given timestamp, computes a numerator and denominator sum, and produces a time series with the ratio of these sums at each timestamp. The _numerator_predicate_ argument controls what goes into the numerator sum and the _denominator_predicate_ controls what goes into the denominator sum. The _denominator_predicate_ is optional and defaults to `true` if not given.

The _numerator_predicate_ and _denominator_predicate_ arguments are evaluated for each row and if true the value column for that row is included in the numerator (_numerator_predicate_) or denominator (_denominator_predicate_) sum.

#### `filter_ratio_by` Computes a grouped ratio of two filtered sums of the input value column.

* * *

Signature: _Table_ `| filter_ratio_by` _tsid: RowToTSID_`,` _numerator_predicate: Bool_`,` _denominator_predicate: [ Bool ]_

The `filter_ratio_by` table operation takes one input table that has exactly one value column of a numeric type. If the input table is not aligned, then an `align` table operation will automatically be inserted to provide alignment.

The `filter_ratio_by` operation groups rows together that have the same time-series identifier computed by the _tsid_ argument. For each group it computes a numerator and denominator sum, and produces a time series with the ratio of these sums at each timestamp. The _numerator_predicate_ argument controls what goes into the numerator sum and the _denominator_predicate_ argument controls what goes into the denominator sum. The second argument is optional and defaults to `true` if not given.

The _numerator_predicate_ and _denominator_predicate_ arguments are evaluated for each row and if true the value column for that row is included in the numerator (_numerator_predicate_) or denominator (_denominator_predicate_) sum.

One times series is computed for each group, with the time-series identifier computed by the _tsid_ argument.

## Functions

This section describes each of the functions that can be used in expressions (`expr`) in the Monitoring Query Language.

  * Input Row Columns
    * `val` A value column's value in the input point (row).
    * `end` The ending time of the input point (row).
    * `start` The starting time of the input point (row).
    * `older` A value from the next-earlier point (row) in a time series.
    * `adjacent_delta` The change in value between an input point and next-earlier point.
    * `adjacent_rate` The rate of change between the input and next-earlier points (rows).
    * `hash_tsid` Return a hash of the time series identifier columns.
  * Logical
    * `not` The logical negation of a boolean value.
    * `and` The logical and of two boolean values.
    * `or` The logical or of two boolean values.
    * `true` The boolean value true.
    * `false` The boolean value false.
    * `has` True if a set argument contains a particular value.
    * `has_value` True if an argument expression computes a value.
    * `if` A value conditionally chosen from two values.
    * `or_else` A value or, if it is not a value, another value.
  * Comparison
    * `eq` Equal.
    * `ne` Not equal.
    * `ge` Greater than or equal.
    * `gt` Greater than.
    * `le` Less than or equal.
    * `lt` Less than.
  * Arithmetic
    * `add` The sum of two numbers.
    * `sub` The difference of two numbers.
    * `mul` The product of two numbers.
    * `div` The ratio of two numbers.
    * `int_div` The quotient from the division of two integers.
    * `abs` Absolute value.
    * `neg` The negative of a number.
    * `pos` Identity for numeric inputs.
    * `rem` The remainder from the division of two integers.
  * Math
    * `sqrt` Square root.
    * `log` Natural logarithm.
    * `exp` e raised to a power.
    * `power` One number to the power of another.
    * `int_round` Nearest integer.
    * `int_floor` Lower bound integer.
    * `int_ceil` Upper bound integer.
  * String
    * `concatenate` String concatenation.
    * `string_to_double` Convert _String_ to _Double_.
    * `string_to_int64` Convert _String_ to _Int_.
    * `ascii_to_lower` Change ASCII upper case letter characters to lower case.
    * `ascii_to_upper` Change ASCII lower case letter characters to upper case.
    * `format` Format _Int64_ , _Double_ , or _String_ as a _String_.
    * `string_to_timestamp` Convert _String_ to _Date_ using date format and optional timezone.
    * `timestamp_to_string` Convert _Timestamp_ to _String_ using date format and optional timezone.
    * `utf8_normalize` Unicode string suitable for case-folding comparison.
  * Regular Expressions
    * `re_full_match` True if a regular expression matches the whole of a string value.
    * `re_partial_match` True if a regular expression matches some part of string value.
    * `re_extract` Extract values matched by a regular expression in another string.
    * `re_replace` Replace the first match of a regular expression in another string.
    * `re_global_replace` Replace all matches of a regular expression in another string.
  * Aggregation
    * `sum` The sum of a group of numeric values.
    * `distribution` A distribution from a group of numeric or distribution values.
    * `count` The count of the number of values in a group of values.
    * `row_count` The number of input rows encountered.
    * `count_true` The number of true values in a group of boolean values.
    * `min` The minimum of a group of numeric values.
    * `max` The maximum of a group of numeric values.
    * `diameter` The maximum minus the minimum of a group of numeric values.
    * `mean` The mean of a group of numeric values.
    * `stddev` The standard deviation of a group of values.
    * `variance` The variance of a group of numeric values.
    * `covariance` The covariance of a group of pairs of values.
    * `median` The median of a group of numeric or distribution values.
    * `percentile` A percentile of a group of numeric or distribution values.
    * `fraction_less_than` The fraction of a group of values less than a fixed value.
    * `fraction_true` The fraction of a group of boolean values that are true.
    * `any_true` The disjunction of a group of boolean values.
    * `all_true` The conjunction of a group of boolean values.
    * `pick_any` The value of any element of a group of values (chosen arbitrarily).
    * `singleton` The value of the element of a group of values with only one element.
    * `unique` The common value of a group of values (which must all be the same).
    * `aggregate` Default aggregate value from a group of values of any type.
    * `weighted_distribution` A distribution from a group of weighted values.
  * Aligning
    * `rate` Compute a rate of change at aligned points in time.
    * `delta` Compute the change in value at aligned points in time.
    * `any_true_aligner` Align a _Bool_ time series by finding any true value in a window.
    * `count_true_aligner` Align a _Bool_ time series by counting the true values in a window.
    * `delta_gauge` Compute the change in value at aligned points in time as a _Gauge_ time series.
    * `fraction_true_aligner` Align a _Bool_ time series with the fraction of true values in a window.
    * `int_mean_aligner` Align by finding the mean of _Int_ values in a window.
    * `interpolate` Compute interpolated values at aligned points in time.
    * `mean_aligner` Align by finding the mean of values in a window.
    * `next_older` Aligned points in time by moving from an earlier to later time.
    * `next_younger` Aligned points in time by moving from a later to earlier time.
  * Manipulating Units
    * `scale` Scale a value to a different unit of measure.
    * `cast_units` Set the unit of measure of a value.
  * Periodic Window
    * `window` Indicates a window that is the same as the alignment period.
    * `sliding` Indicates a window that is sliding (overlapping) rather than disjoint.
    * `requested_period` The external requested output alignment period.
  * Distribution
    * `count_from` The number of values in a distribution value.
    * `sum_from` The sum of the values in a distribution value.
    * `mean_from` The mean of the values in a distribution value.
    * `stddev_from` The standard deviation of the values in a distribution value.
    * `variance_from` The variance of the values in a distribution value.
    * `median_from` The median of the values in a distribution value.
    * `percentile_from` A percentile of the values in a distribution value.
    * `fraction_less_than_from` The fraction of values in a distribution that are less than a fixed value.
    * `bounded_percentile_from` A percentile of the values within a bound in a distribution value.
    * `rebucket` Distribution value converted to a new bucket specification.
  * Bucket Specifier
    * `powers_of` A bucket specification with exponentially increasing bucket boundaries.
    * `fixed_width` A bucket specification with equal-sized buckets.
    * `custom` A bucket specification from a list of bucket boundaries.
    * `num_buckets` Sets the number of buckets in a bucket specification.
    * `bounds` Sets the lower bound of the first bucket and upper bound of the last.
    * `lower` Sets the lower bound of the first bucket in a bucket specification.
  * Miscellaneous
    * `cast_double` Convert _Int_ value to _Double_.
    * `cast_gauge` Cast a _Cumulative_ or _Delta_ time series value to _Gauge_.
    * `within` Specifies the window of the sort value calculation.



### Input Row Columns

The expressions in a query operate on the columns of an input row. A column is normally accessed by giving its name. The functions in this section provide alternative ways to access columns.

The time columns do not have column names and are accessed by the `start` and `end` functions.

The value columns can be accessed by name or by position using the `val` function.

The `older` function gives access to a column in the next-earlier row in a time series.

#### `val` A value column's value in the input point (row).

* * *

Signature: _ImplicitRowInput_ `val(`_[ lit-Int ]_ `)` → _InputType_ _(implicit row input)_

The `val` function provides an alternative to using the column name when accessing the value columns of an input row. Its _Int_ argument (default value 0) indexes the ordered set of value columns (starting with 0 for the first value column) and returns the value of the indexed value column. This is the same value that results from using the value column name.

It is a static error if the `val` function indicates an index that is negative or is the same or larger than or equal to the number of value columns.

#### `end` The ending time of the input point (row).

* * *

Signature: _ImplicitRowInput_ `end(` `)` → _Date.Gauge_ _(implicit row input)_

The `end` function returns the Date value in the end time column of the current input row.

#### `start` The starting time of the input point (row).

* * *

Signature: _ImplicitRowInput_ `start(` `)` → _Date.Gauge_ _(implicit row input)_

The `start` function returns the Date value in the start time column of the current input row. If the row does not have a start time (because it contains only _Gauge_ data), start time returns no-value.

#### `older` A value from the next-earlier point (row) in a time series.

* * *

Signature: `older(`_ColumnValue.CumulativeOK_ `)` → _FirstArgType.FirstArgKind_   
`older(`_Date_ `)` → _Date.FirstArgKind_

The argument to `older` must be a column name or a function that designates a column value (`val`, `end`, `start`). The value returned is the value of that column in the row that is next-earlier to the input row in the same time series. If there is no such earlier row in the same time series, `older` returns no-value.

The column referenced may be a value, time, or time series identifier column. If it is a time series identifier column `older` will return the same value as the argument expression would even if there is no earlier row in the same time series.

#### `adjacent_delta` The change in value between an input point and next-earlier point.

* * *

Signature: _ImplicitRowInput_ `adjacent_delta(` `)` → _InputType_ _(implicit row input)_

The `adjacent_delta` function operates on tables with a single numeric (_Int_ or _Double_) or Distribution value column.

If applied to a _Gauge_ time series, `adjacent_delta` returns the difference between the value of the value column in current input row and the value column in the next-earlier row in the same time series, if any. If there is no next-earlier row in the same time series, `adjacent_delta` returns no-value. The result has _Gauge_ time series kind.

If applied to a _Delta_ time series, `adjacent_delta` returns the value of the value column, which remains a _Delta_ time series kind. Each output point has the same value, start time, and end time as the input point it was generated from.

Although _Cumulative_ time series are rarely used in queries, if applied to a _Cumulative_ time series, `adjacent_delta` returns one of two values:

  * If the input point's start time is before the end time of the next earlier point, `adjacent_delta` returns the value of the input point minus the value of the next-earlier point.

  * If the input point's start time is later than the end time of the next-earlier point, `adjacent_delta` returns the input points value (effective subtracting a value of 0 at the start time).




The resulting time series has a _Delta_ time series kind and each point a start time that is its original start time or the end time of the next earlier input point, whichever is later.

#### `adjacent_rate` The rate of change between the input and next-earlier points (rows).

* * *

Signature: _ImplicitRowInput_ `adjacent_rate(` `)` → _Double.Gauge_ _(implicit row input)_

The `adjacent_rate` function operates on tables with a single numeric (_Int_ or _Double_) or Distribution value column.

If applied to a _Gauge_ or _Cumulative_ time series, `adjacent_rate` returns the rate of change between the value of the value column in current input row and the value column in the next-earlier row in the same time series, if any. This is the difference in values divided by the difference in end time of the two rows. If there is no next-earlier row in the same time series, `adjacent_rate` return no-value. The result has _Gauge_ time series kind.

If applied to a _Delta_ time series, `adjacent_rate` returns the value column of the current input row divided by the difference between the start time and the end time of that row.

#### `hash_tsid` Return a hash of the time series identifier columns.

* * *

Signature: _ImplicitRowInput_ `hash_tsid(`_[ lit-Int ]_ `)` → _Int_ _(implicit row input)_

The `hash_tsid` function returns a hash of the values in the fields of the time series identifier of the current input row. If it is given an argument, that is used as a seed to the hash.

### Logical

#### `not` The logical negation of a boolean value.

* * *

Signature: `not(`_Bool_ `)` → _Bool_

The `not` function takes a boolean value and returns true if that argument is false and returns false if that argument is true. If the input argument is no-value, that is the result.

#### `and` The logical and of two boolean values.

* * *

Signature: `and(`_Bool_`,` _Bool_ `)` → _Bool_

The `and` function returns true if both of its inputs are true, and false otherwise. If either input is no-value, `and` always returns no-value.

#### `or` The logical or of two boolean values.

* * *

Signature: `or(`_Bool_`,` _Bool_ `)` → _Bool_

The `or` function returns true if either of its inputs are true, and false otherwise. If either input is no-value, `or` always returns no-value.

#### `true` The boolean value true.

* * *

Signature: _ImplicitRowInput_ `true(` `)` → _lit-Bool_ _(implicit row input)_

This function returns the literal _Bool_ value `true`.

#### `false` The boolean value false.

* * *

Signature: _ImplicitRowInput_ `false(` `)` → _lit-Bool_ _(implicit row input)_

This function returns the literal _Bool_ value `false`.

#### `has` True if a set argument contains a particular value.

* * *

Signature: `has(`_Set_`,` _lit-ColumnValue_ `)` → _Bool_

The `has` function returns true if its first argument set has the second argument as an element.

#### `has_value` True if an argument expression computes a value.

* * *

Signature: `has_value(`_ColumnValue_ `)` → _Bool_

The `has_value` function returns true if its argument evaluates to a value and returns false if it evaluates to no-value.

#### `if` A value conditionally chosen from two values.

* * *

Signature: `if(`_Bool_`,` _ColumnValue.Delta_`,` _ColumnValue.Delta_ _(same)_ `)` → _LastArgType.Delta_   
`if(`_Bool_`,` _ColumnValue_`,` _ColumnValue_ _(same)_ `)` → _LastArgType_

The `if` function returns its second or third argument, depending on the value (`true` or `false`) of its first argument.

`if` evaluates its first _Bool_ argument. If it is no-value, then no-value is the result. If the first argument is true, then the second argument is returned and if the first argument is false, then the third argument is returned.

Either the second or third argument may be no-value, but the result of `if` will only be no-value if the _Bool_ argument is no-value or if the argument returned is no-value. The argument that is not selected may be no-value without the result being no-value.

If the second and third arguments of `if` are numeric and either argument has units, then both arguments must have units. If the arguments have units, they must either be equivalent or the rules given here must allow one of the arguments to be scaled before applying `if` so the units are equivalent. It is an error if only one argument has units or if both arguments have units that cannot be made equivalent.

The result of the `if` has the unit of its second argument, possibly scaled.

#### `or_else` A value or, if it is not a value, another value.

* * *

Signature: `or_else(`_ColumnValue_`,` _ColumnValue_ _(same)_ `)` → _LastArgType_

The `or_else` function returns the value of its first argument unless it is no-value, in which case the value of its second argument is returned.

The `or_else` function only returns no-value if both its arguments are no-value.

If the arguments of `or_else` are numeric and either argument has units, then both arguments must have units. If the arguments have units, they must either be equivalent or the rules given here must allow one of the arguments to be scaled before applying `or_else` so the units are equivalent. It is an error if only one argument has units or if both arguments have units that cannot be made equivalent.

The result of the `or_else` has the unit of the first argument, possibly scaled.

### Comparison

The comparison operators compare two values of the same type or two numeric (_Int_ or *Double) values and return a _Bool_ value. Unlike most functions, comparison operators never return no-value. If an input is no-value, it is considered to be a specific value that is larger than any other value.

#### `eq` Equal.

* * *

Signature: `eq(`_Num_`,` _Num_ `)` → _Bool_   
`eq(`_Comparable_`,` _Comparable_ _(same)_ `)` → _Bool_

This compares its first _Comparable_ argument to the second _Comparable_ argument and returns `true` if they are the same and `false` if they are not the same. If one argument is _Int_ and the other _Double_ , the _Int_ argument is converted to a _Double_ value before comparing.

If either input is no-value, the comparison is done and a _Bool_ argument is returned, `true` if both values are no-value and `false` otherwise. (This treats no-value as equal to itself.)

For a comparison on numeric arguments, if either argument has units, then both arguments must have units and the units must be equivalent. The result, being type _Bool_ will not have units. If the arguments to `eq` have non-equivalent units that have the same dimension, then one argument may have its unit scaled automatically to make the units of both arguments be equivalent.

If the arguments of `eq` are numeric and either argument has units, then both arguments must have units. If the arguments have units, they must either be equivalent or the rules given here must allow one of the arguments to be scaled before applying `eq` so the units are equivalent. It is an error if only one argument has units or if both arguments have units that cannot be made equivalent.

The result of 'eq', being type _Bool_ , will not have units.

A comparison between the `resource.project_id` column and a literal string has special treatment to deal with the difference between project numbers and project names, as described in [Matching the `resource.project_id` column](https://docs.cloud.google.com/monitoring/mql/query-language#project-id-special-case).

#### `ne` Not equal.

* * *

Signature: `ne(`_Num_`,` _Num_ `)` → _Bool_   
`ne(`_Comparable_`,` _Comparable_ _(same)_ `)` → _Bool_

This compares its first _Comparable_ argument to the second _Comparable_ argument and returns `false` if they are the same and `true` if they are not the same. If one argument is _Int_ and the other _Double_ , the _Int_ argument is converted to a _Double_ value before comparing.

If either input is no-value, the comparison is done and a _Bool_ argument is returned, `false` if both values are no-value and `false` otherwise. (This treats no-value as equal to itself.)

If the arguments of `ne` are numeric and either argument has units, then both arguments must have units. If the arguments have units, they must either be equivalent or the rules given here must allow one of the arguments to be scaled before applying `ne` so the units are equivalent. It is an error if only one argument has units or if both arguments have units that cannot be made equivalent.

The result of 'ne', being type _Bool_ , will not have units.

A comparison between the `resource.project_id` column and a literal string has special treatment to deal with the difference between project numbers and project names, as described in [Matching the `resource.project_id` column](https://docs.cloud.google.com/monitoring/mql/query-language#project-id-special-case).

#### `ge` Greater than or equal.

* * *

Signature: `ge(`_Num_`,` _Num_ `)` → _Bool_   
`ge(`_Comparable_`,` _Comparable_ _(same)_ `)` → _Bool_

This compares its first _Comparable_ argument to the second _Comparable_ argument and returns `true` if the first is greater than or equal to the second and `false` otherwise. If one argument is _Int_ and the other _Double_ , the _Int_ argument is converted to a _Double_ value before comparing.

If either input is no-value, the comparison is done and a _Bool_ argument is returned, `true` if the first value is no-value and `false` otherwise. (This treats no-value as greater than any other value.)

If the arguments of `ge` are numeric, then, if either argument has units, both arguments must have units. If the arguments have units, then the units must be equivalent. If the units are not equivalent but have the same dimension, then one of the arguments **may** be automatically scaled to have the same units as the other as described here. It is an error if only one of the arguments has units or if the arguments have non-equivalent units and no scaling is done.

The result of 'ge', being type _Bool_ , will not have units.

#### `gt` Greater than.

* * *

Signature: `gt(`_Num_`,` _Num_ `)` → _Bool_   
`gt(`_Comparable_`,` _Comparable_ _(same)_ `)` → _Bool_

This compares its first _Comparable_ argument to the second _Comparable_ argument and returns `true` if the first is greater than the second and `false` otherwise. If one argument is _Int_ and the other _Double_ , the _Int_ argument is converted to a _Double_ value before comparing.

If either input is no-value, the comparison is done and a _Bool_ argument is returned, `false` if the second value is no-value and `true` otherwise. (This treats no-value as greater than any other value.)

If the arguments of `gt` are numeric and either argument has units, then both arguments must have units. If the arguments have units, they must either be equivalent or the rules given here must allow one of the arguments to be scaled before applying `gt` so the units are equivalent. It is an error if only one argument has units or if both arguments have units that cannot be made equivalent.

The result of 'gt', being type _Bool_ , will not have units.

#### `le` Less than or equal.

* * *

Signature: `le(`_Num_`,` _Num_ `)` → _Bool_   
`le(`_Comparable_`,` _Comparable_ _(same)_ `)` → _Bool_

This compares its first _Comparable_ argument to the second _Comparable_ argument and returns `true` if the first is less than or equal to the second and `false` otherwise. If one argument is _Int_ and the other _Double_ , the _Int_ argument is converted to a _Double_ value before comparing.

If either input is no-value, the comparison is done and a _Bool_ argument is returned, `true` if the second value is no-value and `false` otherwise. (This treats no-value as greater than any other value.)

If the arguments of `le` are numeric and either argument has units, then both arguments must have units. If the arguments have units, they must either be equivalent or the rules given here must allow one of the arguments to be scaled before applying `le` so the units are equivalent. It is an error if only one argument has units or if both arguments have units that cannot be made equivalent.

The result of 'le', being type _Bool_ , will not have units.

#### `lt` Less than.

* * *

Signature: `lt(`_Num_`,` _Num_ `)` → _Bool_   
`lt(`_Comparable_`,` _Comparable_ _(same)_ `)` → _Bool_

This compares its first _Comparable_ argument to the second _Comparable_ argument and returns `true` if the first is less than the second and `false` otherwise. If one argument is _Int_ and the other _Double_ , the _Int_ argument is converted to a _Double_ value before comparing.

If either input is no-value, the comparison is done and a _Bool_ argument is returned, `false` if the first value is no-value and `true` otherwise. (This treats no-value as greater than any other value.)

If the arguments of `lt` are numeric and either argument has units, then both arguments must have units. If the arguments have units, they must either be equivalent or the rules given here must allow one of the arguments to be scaled before applying `lt` so the units are equivalent. It is an error if only one argument has units or if both arguments have units that cannot be made equivalent.

The result of 'lt', being type _Bool_ , will not have units.

### Arithmetic

Functions implementing the arithmetic operators.

#### `add` The sum of two numbers.

* * *

Signature: `add(`_Num.Delta_`,` _Num.Delta_ `)` → _Num.Delta_   
`add(`_Num_`,` _Num_ `)` → _Num_   
`add(`_Duration_`,` _Duration_ `)` → _Duration_   
`add(`_Date_`,` _Duration_ `)` → _Date_   
`add(`_Duration_`,` _Date_ `)` → _Date_

The `add` function on two _Num_ arguments returns the sum of its arguments, as a _Double_ value if either input is a _Double_ value and as an _Int_ value otherwise. If both inputs are _Delta_ time series kind, then the output is _Delta_ time series kind. Otherwise the output is _Gauge_ time series kind.

The `add` function on two _Duration_ arguments returns the duration that is their sum.

The `add` function on a _Date_ and _Duration_ argument returns the Date that is the _Duration_ later than the _Date_ argument. If the _Duration_ is negative, the result will be earlier than the input _Date_ (goes back in time).

If the arguments of `add` are numeric and either argument has units, then both arguments must have units. If the arguments have units, they must either be equivalent or the rules given here must allow one of the arguments to be scaled before applying `add` so the units are equivalent. It is an error if only one argument has units or if both arguments have units that cannot be made equivalent.

The result of the `add` has the unit of the first argument, possibly scaled.

#### `sub` The difference of two numbers.

* * *

Signature: `sub(`_Num.Delta_`,` _Num.Delta_ `)` → _Num.Delta_   
`sub(`_Num_`,` _Num_ `)` → _Num_   
`sub(`_Duration_`,` _Duration_ `)` → _Duration_   
`sub(`_Date_`,` _Duration_ `)` → _Date_   
`sub(`_Date_`,` _Date_ `)` → _Duration_

The `sub` function on two _Num_ arguments returns the first argument minus the second argument, as a _Double_ value if either input is a _Double_ value and as an _Int_ otherwise. If both inputs are _Delta_ time series kind, then the output is _Delta_ time series kind. Otherwise the output is _Gauge_ time series kind.

The `sub` function two _Duration_ arguments returns the duration that is their numeric difference.

The `sub` function on a _Date_ and _Duration_ argument returns the Date that is the _Duration_ earlier than the _Date_ argument. If the _Duration_ argument is negative, the result is later than the _Date_ argument.

If the arguments of `sub` are numeric and either argument has units, then both arguments must have units. If the arguments have units, they must either be equivalent or the rules given here must allow one of the arguments to be scaled before applying `sub` so the units are equivalent. It is an error if only one argument has units or if both arguments have units that cannot be made equivalent.

The result of the `sub` has the unit of the first argument, possibly scaled.

#### `mul` The product of two numbers.

* * *

Signature: `mul(`_Num.Delta_`,` _lit-Num_ `)` → _Num.Delta_   
`mul(`_lit-Num_`,` _Num.Delta_ `)` → _Num.Delta_   
`mul(`_Num_`,` _Num_ `)` → _Num_   
`mul(`_Duration_`,` _Num_ `)` → _Duration_   
`mul(`_Num_`,` _Duration_ `)` → _Duration_

The `mul` function on two _Num_ arguments returns the product of the two arguments, as a _Double_ value if either input is a _Double_ value and as an _Int_ value otherwise. If one inputs is _Delta_ time series kind and the other input is a literal, then the output is _Delta_ time series kind. Otherwise the output is _Gauge_ time series kind.

The `mul` function on a _Num_ and _Duration_ is the _Duration_ multiplied by the _Num_ as a _Duration_ type.

If either numeric argument has units, then both arguments must have units and the units must be equivalent. The unit of the result, if the arguments have units, will be the product of the units of the two arguments. The one exception is multiplication by a literal: the literal may not have a unit of measure given explicitly, so if the other argument has a unit of measure, the unit `1` will be given to the literal, causing the result to have the units of the other argument.

#### `div` The ratio of two numbers.

* * *

Signature: `div(`_Num.Delta_`,` _lit-Num_ `)` → _Double.Delta_   
`div(`_Num_`,` _Num_ `)` → _Double_   
`div(`_Duration_`,` _Num_ `)` → _Duration_   
`div(`_Duration_`,` _Duration_ `)` → _Double_   
`div(`_Date_`,` _Duration_ `)` → _Double_

The `div` function divides its first _Num_ argument by its second _Num_ argument, returning the ratio as a _Double_ value.

The `div` function does not produce a result if the second argument is 0.

If both arguments are numeric (_Int_ or _Double_) the result is the _Double_ value that is the ratio of the two numbers.

If the first argument is _Duration_ and the second argument is numeric, then the result is a _Duration_ which is the nearest _Duration_ to the ratio of that duration and numeric value. So `60m / 3.0` is `20s` and `100us / 33` is `3us`.

If the second argument to `div` is a _Duration_ value, the result is a _Double_ value with unit "1" representing the dimensionless ratio between the time span represented by the first argument and the time span represented by the second argument. If the first argument is a _Date_ value, the time span is the difference between the data specified by the value and the Unix epoch (`d'1970/01/01-00:00:00+00:00'`).

To convert a _Date_ or _Duration_ to a _Double_ value with a time unit, use the `scale` function.

If both arguments to `div` are numeric and either has units, then both arguments must have units. The unit of the result, if the arguments have units, will be the division of the unit of the first argument by the unit of the second. The one exception is division by a literal if the literal does not have a unit of measure given explicitly. In this case the unit `1` will be given to the literal, causing the result to have the units of the other argument.

#### `int_div` The quotient from the division of two integers.

* * *

Signature: `int_div(`_Int_`,` _Int_ `)` → _Int_   
`int_div(`_Duration_`,` _Int_ `)` → _Duration_   
`int_div(`_Duration_`,` _Duration_ `)` → _Int_   
`int_div(`_Date_`,` _Duration_ `)` → _Int_

The `int_div` function divides its first argument by its second argument, returning the quotient as an _Int_ value. When an argument is a _Date_ or _Duration_ , the value is represented as an integer value that is the _Date_ or _Duration_ in units that represent the full internal precision of such values. If the result is a Date or Duration, the numeric quotient is interpreted as a value with the same units.

In the case of a _Date_ value being divided by a _Duration_ value, the result is the _Int_ value that is the number of that _Duration_ periods since the Unix epoch (`d'1970/01/01-00:00:00+00:00'`). So `d'2020/06/01-01:20:03' / 1s` is the number of seconds since `d'1970/01/01-00:00:00+00:00'` at `d'2020/06/01-01:20:03'`.

The `int_div` function does not produce a result if the second argument is 0.

If both arguments are _Int_ the result is the _Int_ value that is the quotient of the division.

If the first argument is _Duration_ and the second argument is _Int_ , then the result is a _Duration_ which is the nearest _Duration_ to the quotient of that duration and numeric value. So `60m / 7` is `8s` and `100us / 33` is `3us`.

If the second argument to `div` is a _Duration_ value, the result is an _Int_ value with unit "1" representing the dimensionless quotient of the division of the time span represented by the first argument and the time span represented by the second argument. If the first argument is a _Date_ value, the time span is the difference between the data specified by the value and the Unix epoch (`d'1970/01/01-00:00:00+00:00'`).

To convert a _Date_ or _Duration_ to an _Int_ value with a time unit, use the `scale` function and apply the `int_round` function to the result to convert from the floating output of `scale` to an _Int_ value. For example `scale(3d, "1s").int_round()` to convert 2 days to an _Int_ number of seconds.

If both arguments are _Int_ values and either argument has units, then both arguments must have units. The unit of the result, if the arguments have units, will be the division of the unit of the first argument by the unit of the second. The one exception is division by a literal if the literal does not have a unit of measure given explicitly. In this case the unit `1` will be given to the literal, causing the result to have the units of the other argument.

#### `abs` Absolute value.

* * *

Signature: `abs(`_Num_ `)` → _Num_

The `abs` function takes a numeric (_Int_ or *Double) input and returns a value of the same type that has the same magnitude as the input and is non-negative.

The result of `abs` has the same unit of measure.

#### `neg` The negative of a number.

* * *

Signature: `neg(`_Num_ `)` → _Num_   
`neg(`_Duration_ `)` → _Duration_

The `neg` function returns the negative of its argument.

#### `pos` Identity for numeric inputs.

* * *

Signature: `pos(`_Num_ `)` → _Num_   
`pos(`_Duration_ `)` → _Duration_

The `pos` function returns its one argument

#### `rem` The remainder from the division of two integers.

* * *

Signature: `rem(`_Int_`,` _Int_ `)` → _Int_   
`rem(`_Duration_`,` _Duration_ `)` → _Duration_

The `rem` function divides its first argument by its second argument, returning the remainder.

The `rem` function does not produce a result if the second _Num_ argument is 0.

If the two arguments are of type _Int_ , then the result is the _Int_ remainder of the division with the same unit, if any, as the first argument.

If the two arguments are of type _Duration_ , then the result is the is the _Duration_ that is the remainder of the division.

### Math

Some mathematical functions.

#### `sqrt` Square root.

* * *

Signature: `sqrt(`_Num_ `)` → _Double_

The `sqrt` function returns the square root of the _Num_ argument as a _Double_ value.

The `sqrt` does not produce a result if the _Num_ argument is less than 0.

The result of `sqrt` does not have a unit of measure.

#### `log` Natural logarithm.

* * *

Signature: `log(`_Num_ `)` → _Double_

The `log` function returns the natural logarithm of the _Num_ argument as a _Double_ value.

The `log` does not produce a result if the _Num_ argument is less than or equal to 0.

The result of `log` does not have a unit of measure.

#### `exp` e raised to a power.

* * *

Signature: `exp(`_Num_ `)` → _Double_

The `exp` returns e (the base of natural logarithms) raised to the power of the _Num_ argument as a _Double_ value.

The `exp` functions returns the Double value infinity on overflow.

The result of `exp` does not have a unit of measure.

#### `power` One number to the power of another.

* * *

Signature: `power(`_Num_`,` _Num_ `)` → _Double_

This returns the value of the first _Num_ argument, raised to the power of the second _Num_ argument, represented as a _Double_ value. If either argument is an _Int_ , it is converted to a _Double_ before the operation.

The result of `power` does not have a unit of measure.

#### `int_round` Nearest integer.

* * *

Signature: `int_round(`_Double_ `)` → _Int_

The `int_round` function takes a _Double_ value, rounds it to the nearest integer value and returns it as an _Int_ value. If the input is not a value or the result cannot be represent as an _Int_ value, the result is no-value.

The result of `int_round` has the same unit of measure as its input.

#### `int_floor` Lower bound integer.

* * *

Signature: `int_floor(`_Double_ `)` → _Int_

The `int_floor` function takes a _Double_ value, rounds it toward minus infinity to the nearest integer value and returns it as an _Int_ value. If the input is not a value or the result cannot be represent as an _Int_ value, the result is no-value.

The result of `int_floor` has the same unit of measure as its input.

#### `int_ceil` Upper bound integer.

* * *

Signature: `int_ceil(`_Double_ `)` → _Int_

The `int_ceil` function takes a _Double_ value, rounds it toward infinity to the nearest integer value and returns it as an _Int_ value. If the input is no-valueor the result cannot be represent as an _Int_ value, the result is no-value.

The result of `int_ceil` does not have a unit of measure.

### String

Functions processing _String_ values.

#### `concatenate` String concatenation.

* * *

Signature: `concatenate(`_String_`,` _String_ `)` → _String_

The `concatenate` function returns the concatenation of its two _String_ arguments.

#### `string_to_double` Convert _String_ to _Double_.

* * *

Signature: `string_to_double(`_String_ `)` → _Double_

The `string_to_double` function parses its input _String_ argument as a floating point number and returns the result as a _Double_ value. The input string may contain leading whitespace, may contain a leading '+' or '-' prefix, may have a '0X' or '0x' prefix to indicate a hexadecimal value, may contain leading 0s at the beginning of the numerical value, and may have decimal point followed by a valid number. Decimal numbers may be followed by a base 10 exponent, indicated by "E" or "e" and a decimal number; Hexadecimal numbers may be followed by a base 2 exponent, indicated by "P" or "p" followed by a hexadecimal number. Invalidly formatted strings, overflow, and underflow all result in no-value.

The result of `string_to_double` does not have a unit of measure.

#### `string_to_int64` Convert _String_ to _Int_.

* * *

Signature: `string_to_int64(`_String_`,` _[ lit-Int ]_ `)` → _Int_

The `string_to_int64` function takes two arguments: a required _String_ and an optional _Int_. The function parses the _String_ argument as an integer number, using the optional _Int_ argument as a base, and returns the result as an _Int_. The default value of the optional base is 10. Base value 0 indicates that _String_ s with prefix '0x' or '0X' shall be parsed as hexadecimal (e.g. 0x10 = 16), _String_ s with prefix '0' shall be parsed as octal (e.g. '010' = 8), and _String_ s with no prefix shall be parsed as decimal (e.g. '10' = 10). If the string is not a valid integer value or cannot be represented as an _Int_ value, the result is no-value.

The result of `string_to_int64` does not have a unit of measure.

#### `ascii_to_lower` Change ASCII upper case letter characters to lower case.

* * *

Signature: `ascii_to_lower(`_String_ `)` → _String_

The `ascii_to_upper` function takes a _String_ argument and returns a _String_ value that is the same except that each upper-case ASCII letter has been converted to the corresponding lower-case ASCII letter. All other characters are left unchanged.

#### `ascii_to_upper` Change ASCII lower case letter characters to upper case.

* * *

Signature: `ascii_to_upper(`_String_ `)` → _String_

The `ascii_to_upper` function takes a _String_ argument and returns a _String_ value that is the same except that each lower-case ASCII letter has been converted to the corresponding upper-case ASCII letter. All other characters are left unchanged.

#### `format` Format _Int64_ , _Double_ , or _String_ as a _String_.

* * *

Signature: `format(`_Num_`,` _lit-String_ `)` → _String_   
`format(`_String_`,` _lit-String_ `)` → _String_

The `format` function takes two required arguments: an _Int_ , _Double_ or _String_ , and a _String_. The function formats the first argument as a string, using the format specified in the second _String_ argument, and returns the result as a _String_. 

#### `string_to_timestamp` Convert _String_ to _Date_ using date format and optional timezone.

* * *

Signature: `string_to_timestamp(`_String_`,` _lit-String_`,` _[ lit-String ]_ `)` → _Date_

The `string_to_timestamp` function parses its input _String_ argument as a timestamp and returns the result as a _Date_ value.

Second argument is a time_format, which describes the format of the input string. Use strftime()-like formatting.

Third argument is a time zone and it is optional. Must be a string of TZ identifiers from the IANA Time Zone Database. If no time zone specified, UTC will be used. If time zone information is specified in the input timestamp string, this parameter will not be used.

If the string is not a valid date according to a provided format, the result is no-value.

#### `timestamp_to_string` Convert _Timestamp_ to _String_ using date format and optional timezone.

* * *

Signature: `timestamp_to_string(`_Num_`,` _lit-String_`,` _[ lit-String ]_ `)` → _String_   
`timestamp_to_string(`_Date_`,` _lit-String_`,` _[ lit-String ]_ `)` → _String_

The `timestamp_to_string` function converts input _Timestamp_ to its string representation. Input can be an _Integer_ , _Double_ or _Date_. If input is _Integer_ or _Double_ then units are required.

Second argument is a time_format, which describes the format of the output string. Use strftime()-like formatting.

Third argument is a time zone and it is optional. Must be a string of TZ identifiers from the IANA Time Zone Database. If no time zone specified, UTC will be used.

#### `utf8_normalize` Unicode string suitable for case-folding comparison.

* * *

Signature: `utf8_normalize(`_String_ `)` → _String_

The `utf8_normalize` function takes a _String_ argument and returns an _String_ value suitable for case-folding comparison of the input value under the assumption the input is a valid utf8-encoded string.

### Regular Expressions

Functions that do matching, extraction, and modification using [RE2](https://github.com/google/re2/wiki/Syntax) regular expressions.

#### `re_full_match` True if a regular expression matches the whole of a string value.

* * *

Signature: `re_full_match(`_String_`,` _lit-String_ `)` → _Bool_

The `re_full_match` function takes a string input and a literal string regular expression and returns `true` if the whole of the input string is matched by the regular expression. It returns `false` otherwise, even if the input string argument is no-value.

A regular expression match on the `resource.project_id` column has special treatment to deal with the difference between project numbers and project names, as described in [Matching the `resource.project_id` column](https://docs.cloud.google.com/monitoring/mql/query-language#project-id-special-case).

#### `re_partial_match` True if a regular expression matches some part of string value.

* * *

Signature: `re_partial_match(`_String_`,` _lit-String_ `)` → _Bool_

The `re_partial_match` function takes a string input and a literal string regular expression and returns `true` if any part of the input string is matched by the regular expression. It returns `false` otherwise, even if the string argument is no-value.

#### `re_extract` Extract values matched by a regular expression in another string.

* * *

Signature: `re_extract(`_String_`,` _[ lit-String ]_`,` _[ lit-String ]_ `)` → _String_

The `re_extract` function takes an input _String_ argument and two literal _String_ arguments: a regular expression and a replacement string. The result is formed by matching the input string to the regular expression and the substituting capture groups in the expression in the replacement string. The replacement string with the capture groups substituted is the result.

If the regular expression argument is not given, it defaults to "(.*)", thus including the whole first argument string in one capture group.

If the replacement string argument is not given, it defaults to R"\1", thus making the first replacement group be the output string.

If the input string is no-value, if the regular expression did not match, or the substitution of capture groups did not work, no-value is returned.

#### `re_replace` Replace the first match of a regular expression in another string.

* * *

Signature: `re_replace(`_String_`,` _lit-String_`,` _lit-String_ `)` → _String_

The `re_replace` function takes an input _String_ argument and two literal _String_ arguments: a regular expression and a replacement value. If the regular expression matches any part of the input string, the returned value is formed by replacing the first such match in the input string with the replacement string.

If the input string is no-valueor if there is no match, the input string is the returned value.

#### `re_global_replace` Replace all matches of a regular expression in another string.

* * *

Signature: `re_global_replace(`_String_`,` _lit-String_`,` _lit-String_ `)` → _String_

The `re_global_replace` function takes an input _String_ argument and two literal _String_ arguments: a regular expression and a replacement value. The result is formed from the input string by replacing each disjoint match of the regular expression (from left to right) with the replacement string.

If the input string is no-valueor if there is no match, the input string is the returned value.

### Aggregation

An aggregation function combines a set of input values into a final output value. They are used when a number of input rows are grouped together and aggregated into a single output row.

An aggregation function maintains an internal aggregation state. The argument expression to the aggregation function is evaluated once for each of the grouped input rows and the resulting value (if any) is passed to the aggregation function to be accumulated in its internal state. Once this has been done for all rows in the group, the aggregation function produces its output value to be used in creating value columns in the single output row.

For example, `mean(memory_usage)` applied to a set of rows with a `memory_usage` column, evaluates the argument expression, `memory_usage`, for each row, and incorporates the resulting value (if one is produced) in the internal state of the `mean` aggregation function (which might be a sum of values and a count of values). Once all the rows have been processed, the `mean` reducer produces a value from its internal state (the sum divided by the count).

Most aggregation functions that operate on numeric or _Distribution_ values give the unit of measure of their input to the output. The exceptions are:

  * `count` and `row_count` whose output has unit `1`.

  * `variance` whose output is the square of input.

  * `covariance` whose output is the product of the units of the two inputs.

  * `fraction_less_than` and `fraction_true` give unit `10^2.%` to their output.




#### `sum` The sum of a group of numeric values.

* * *

Signature: `sum(`_Num_ `)` → _Num.Delta_ _(temporal only)_   
`sum(`_Distribution_ `)` → _Double.Delta_ _(temporal only)_   
`sum(`_Num_ `)` → _Num.Gauge_ _(sliding temporal only)_   
`sum(`_Distribution_ `)` → _Double.Gauge_ _(sliding temporal only)_   
`sum(`_Num_ `)` → _Num.FirstArgKind_   
`sum(`_Distribution_ `)` → _Double.FirstArgKind_

If the argument expression is numeric (_Int_ or *Double), this returns the sum of the values that are passed to it.

If the argument expression is a _Distribution_ value, this returns the sum of the population values in all the _Distribution_ values that are passed to it.

If, for some input row, the argument expression does not evaluate to a value or evaluates to a non-finite _Double_ value, that input row does not affect the sum.

For numeric (_Int_ or _Double) input, the result is the same type (_ Int* or _Double_) as the input expression. For _Distribution_ input values, the result type is _Double_.

The output has _Delta_ time series kind if non-sliding temporal aggregations is being done or if only spatial aggregation is being done and the input time series kind is also _Delta_.

The unit of measure attached to the result of `sum` is the same as the unit of the input.

#### `distribution` A distribution from a group of numeric or distribution values.

* * *

Signature: `distribution(`_Num_`,` _lit-BucketSpecification_ `)` → _Distribution.Delta_ _(temporal only)_   
`distribution(`_Num_`,` _lit-BucketSpecification_ `)` → _Distribution.Gauge_   
`distribution(`_Distribution_ `)` → _Distribution.Delta_ _(temporal only)_   
`distribution(`_Distribution_ `)` → _Distribution.Gauge_ _(sliding temporal only)_   
`distribution(`_Distribution_ `)` → _Distribution.FirstArgKind_

If the first argument is a _Num_ value, the input values are collected into a distribution result whose bucket specification is given by the _lit-Bucketer_ argument.

If the first argument is a _Distribution_ value, the distributions are merged into a distribution result that includes the population of all the input distributions. The resulting distribution bucket specification is determined from the input distribution bucket specifications. If the bucket specifications are all the same, then that bucket specification is used. If there are different bucket specification, a new merged bucket specification is used. This merged specification is typically no more accurate than least-accurate input bucket specification.

If, for some input row, the first argument expression does not evaluate to a value or evaluates to a non-finite _Double_ , that input row does not affect the percentile.

The unit of measure attached to the result of `distribution` is the same as the unit of the input.

#### `count` The count of the number of values in a group of values.

* * *

Signature: `count(`_ColumnValue_ `)` → _Int.Delta_ _(temporal only)_   
`count(`_ColumnValue_ `)` → _Int.Gauge_

Returns the count of the number of values that have been passed to it. If the argument expression does not evaluate to a value for some input row or evaluates to a non-finite _Double_ value, it is not counted.

The output will have _Delta_ time series kind when non-sliding temporal aggregation is being done.

The unit of measure attached to the result of `count` is `1`.

#### `row_count` The number of input rows encountered.

* * *

Signature: _ImplicitRowSetInput_ `row_count(` `)` → _Int.Delta_ _(temporal only)_   
_ImplicitRowSetInput_ `row_count(` `)` → _Int.Gauge_

The `row_count` aggregation function returns the count of the number of rows that this is aggregating over. Unlike `count`, `row_count` does not take an argument and does not care if a value could be calculated from the row.

The output will have _Delta_ time series kind when non-sliding temporal aggregation is being done.

The unit of measure attached to the result of `count` is `1`.

#### `count_true` The number of true values in a group of boolean values.

* * *

Signature: `count_true(`_Bool_ `)` → _Int.Delta_ _(temporal only)_   
`count_true(`_Bool_ `)` → _Int_

The input boolean values are collected and the result is the number of input values that are true.

If, for some input row, the argument expression does not evaluate to a value, that input row does not affect the result.

The output will have _Delta_ time series kind when non-sliding temporal aggregation is being done.

The unit of measure attached to the result of `count_true` is `1`.

#### `min` The minimum of a group of numeric values.

* * *

Signature: `min(`_Num_ `)` → _Num_

This collects the numeric values that are passed to it and returns the minimum value. If result type is the same as the input type.

If, for some input row, the argument expression does not evaluate to a value, that input row does not affect the result.

The unit of measure attached to the result of `min` is the same as the unit of the input.

#### `max` The maximum of a group of numeric values.

* * *

Signature: `max(`_Num_ `)` → _Num_

This collects the numeric values that are passed to it and returns the maximum value. If result type is the same as the input type.

If, for some input row, the argument expression does not evaluate to a value, that input row does not affect the result.

The unit of measure attached to the result of `max` is the same as the unit of the input.

#### `diameter` The maximum minus the minimum of a group of numeric values.

* * *

Signature: `diameter(`_Num_ `)` → _Num_

This collects the numeric values that are passed to it and returns the difference between the maximum of the values and the minimum of the values. If result type is the same as the input type (_Int_ or _Double_).

If, for some input row, the argument expression does not evaluate to a value, that input row does not affect the result.

The unit of measure attached to the result of `diameter` is the same as the unit of the input.

#### `mean` The mean of a group of numeric values.

* * *

Signature: `mean(`_Summable_ `)` → _Double_

If the argument expression is numeric (_Int_ or *Double), this returns the mean of the values that are passed to it.

If the argument expression is of type _Distribution_ , this returns the mean of all the values in all the distributions.

If, for some input row, the argument expression does not evaluate to a value or evaluates to a non-finite _Double_ value, that input row does not affect the mean.

The unit of measure attached to the result of `mean` is the same as the unit of the input.

#### `stddev` The standard deviation of a group of values.

* * *

Signature: `stddev(`_Summable_ `)` → _Double_

If the argument expression is numeric (_Int_ or *Double), this returns the standard deviation of the values that are passed to it.

If the argument expression is a _Distribution_ value, this returns the standard deviation of all the values in all the distributions.

If, for some input row, the argument expression does not evaluate to a value or evaluates to a non-finite _Double_ value, that input row does not affect the standard deviation.

The unit of measure attached to the result of `stddev` is the same as the unit of the input.

#### `variance` The variance of a group of numeric values.

* * *

Signature: `variance(`_Summable_ `)` → _Double_

If the argument expression is numeric (_Int_ or *Double), this returns the variance of the values that are passed to it.

If the argument expression is of type _Distribution_ , this returns the variance of all the values in all the distributions.

If, for some input row, the argument expression does not evaluate to a value or evaluates to a non-finite _Double_ value, that input row does not affect the variance.

There is no unit of measure attached to the result of `variance` function.

#### `covariance` The covariance of a group of pairs of values.

* * *

Signature: `covariance(`_Num_`,` _Num_ `)` → _Double_

This returns the covariance of the pairs of numeric (_Int_ or *Double) values that are passed to it.

If, for some input row, either argument expression does not evaluate to a value or evaluates to a non-finite _Double_ value, that input row does not affect the covariance.

There is no unit of measure attached to the result of `covariance` function.

#### `median` The median of a group of numeric or distribution values.

* * *

Signature: `median(`_Summable_ `)` → _Double_

If the argument expression is numeric (_Int_ or *Double), this returns an estimate of the median of the population of values that are passed to it. The median is computed by creating a distribution value from the values in the population with bucket boundaries that are 10% apart, which bounds the error in the estimate by that amount.

The bucket specification used to accumlate a _Distribution_ value from numeric input to estimate a median is `powers_of(1.05).num_buckets(500).lower(.01)`. This includes a range of values from `.01` to about `4e+8`. While this handles many use cases, it might be necessary to use the `scale` function to adjust the input, for example from `By` to `MiBy` or 'MBy' if the range of number of bytes is going to be in the gigabyte or terabyte range.

If the argument expression is a _Distribution_ value, this returns an estimate of the median of the merged population of values from all the distributions. The median is computed by merging all the input distributions into one distribution and estimating the median. The accuracy of the median will depend on the bucket boundaries of the input distributions.

If, for some input row, the argument expression does not evaluate to a value or evaluates to a non-finite _Double_ value, that input row does not affect the standard deviation.

The unit of measure attached to the result of `median` is the same as the unit of the input.

#### `percentile` A percentile of a group of numeric or distribution values.

* * *

Signature: `percentile(`_Summable_`,` _lit-Num_ `)` → _Double_

The _lit-Num_ argument gives a percentile (in the range 0 to 100).

If the first argument expression is numeric (_Int_ or _Double_), this returns an estimate of that percentile of the population of values that are passed to it. The percentile is computed by creating a distribution value from the values in the population with bucket boundaries that are 10% apart, which bounds the error in the estimate by that amount.

The bucket specification used to accumlate a _Distribution_ value from numeric input to estimate a percentile is `powers_of(1.05).num_buckets(500).lower(.01)`. This includes a range of values from `.01` to about `4e+8`. While this handles many use cases, it might be necessary to use the `scale` function to adjust the input, for example from `By` to `MiBy` or 'MBy' if the range of number of bytes is going to be in the gigabyte or terabyte range.

If the argument expression is a _Distribution_ value, this returns an estimate of the percentile of the merged population of values from all the distributions. The percentile is computed by merging all the input distributions into one distribution and estimating the percentile. The accuracy of the percentile will depend on the bucket boundaries of the input distributions.

If, for some input row, the first argument expression does not evaluate to a value or evaluates to a non-finite _Double_ , that input row does not affect the percentile.

The unit of measure attached to the result of `percentile` is the same as the unit of the input.

#### `fraction_less_than` The fraction of a group of values less than a fixed value.

* * *

Signature: `fraction_less_than(`_Summable_`,` _lit-Num_ `)` → _Double_

If the first argument is a numeric (_Int_ or *Double) value, this returns the fraction of the collection of values passed to the first argument that are less than the _lit-Num_ argument. In computing this fraction, it ignores non-finite _Double_ values and not-a-value _Int_ and _Double_ values.

If the first argument is a _Distribution_ value, this combines the populations of all the Distributions it is passed and makes an estimate of the fraction of the values in the population of that aggregated distribution that are less than the value of the _lit-Num_ argument.

The unit of measure attached to the result of `fraction_less_than` is `10^2.%`.

#### `fraction_true` The fraction of a group of boolean values that are true.

* * *

Signature: `fraction_true(`_Bool_ `)` → _Double_

The input boolean values are collected and the result is a _Double_ in the range 0 to 1 that is the fraction of input values that are true.

If, for some input row, the argument expression does not evaluate to a value, that input row does not affect the result.

The unit of measure attached to the result of `fraction_true` is `10^2.%`.

#### `any_true` The disjunction of a group of boolean values.

* * *

Signature: `any_true(`_Bool_ `)` → _Bool_

The `any_true` function calculates the value `true` if all of its input values are `true` and returns `false` otherwise.

If, for some input row, the argument expression does not evaluate to a value, that input row does not affect the result.

#### `all_true` The conjunction of a group of boolean values.

* * *

Signature: `all_true(`_Bool_ `)` → _Bool_

The `all_true` function calculates the value `true` if all its input values are `true` and returns `false` otherwise.

If, for some input row, the argument expression does not evaluate to a value, that input row does not affect the result.

#### `pick_any` The value of any element of a group of values (chosen arbitrarily).

* * *

Signature: `pick_any(`_ColumnValue_ `)` → _FirstArgType_

This functions returns one of the values given to it, chosen arbitrarily.

If, for some input row, the argument expression does not evaluate to a value, that input row does not affect the result.

The unit of measure attached to the result of `pick_any` is the same as the unit of the input, if any.

#### `singleton` The value of the element of a group of values with only one element.

* * *

Signature: `singleton(`_ColumnValue_ `)` → _FirstArgType_

This function returns its argument expression value as evaluated on a single row. It is an error if its argument expression is evaluated and produces a value for more than one row, even if it evaluates to a previously produced value.

If, for some input row, the argument expression does not evaluate to a value, that input row does not affect the result.

The unit of measure attached to the result of `singleton` is the same as the unit of the input.

#### `unique` The common value of a group of values (which must all be the same).

* * *

Signature: `unique(`_Comparable_ `)` → _FirstArgType_

The `unique` function returns the value that is the same as every value that was given to it. If there is no such value (this was given at least two different values), then it generates an error and returns one of the values given to it.

If, for some input row, the argument expression does not evaluate to a value, that input row does not affect the result.

The unit of measure attached to the result of `unique` is the same as the unit of the input.

#### `aggregate` Default aggregate value from a group of values of any type.

* * *

Signature: `aggregate(`_Num_ `)` → _Num.Delta_ _(temporal only)_   
`aggregate(`_Distribution_ `)` → _Distribution.Delta_ _(temporal only)_   
`aggregate(`_Num_ `)` → _Num.Gauge_ _(sliding temporal only)_   
`aggregate(`_Distribution_ `)` → _Distribution.Gauge_ _(sliding temporal only)_   
`aggregate(`_Num_ `)` → _Num.FirstArgKind_   
`aggregate(`_Distribution_ `)` → _Distribution.FirstArgKind_   
`aggregate(`_Bool_ `)` → _Bool_   
`aggregate(`_String_ `)` → _String_

The `aggregate` function does an aggregation that depends on the type of the input.

  * For _Int_ and _Double_ input, it is the same as the `sum` aggregator.

  * For _Distribution_ input, it is the same as the `distribution` aggregator.

  * For _Bool_ input, it is the same as the `any_true` aggregator.

  * For _String_ input, it is the same as the `pick_any` aggregator.




#### `weighted_distribution` A distribution from a group of weighted values.

* * *

Signature: `weighted_distribution(`_Num_`,` _Int_`,` _lit-BucketSpecification_ `)` → _Distribution.Delta_ _(temporal only)_   
`weighted_distribution(`_Num_`,` _Int_`,` _lit-BucketSpecification_ `)` → _Distribution.Gauge_

The input values are collected into a distribution result whose bucket specification is given by _lit-Bucketer_ argument. The first argument is the value to be added to the distribution and the second argument is the weight of that value. A value `N` with a weight of `M` is represented by `M` instances of value `N` in the distribution.

If, for some input row, the first or the second argument expression does not evaluate to a value or evaluates to a non-finite _Double_ , that input row does not affect the percentile.

The unit of measure attached to the result of `weighted_distribution` is the same as the unit of the input.

### Aligning

Aligning functions are use by the `align` table operation to produce an aligned table, one whose time series have points with timestamps at regular intervals.

In addition to its explicit _Duration_ argument, an aligner function takes an input time series and a point in time and produces an output point for that particular time.

The `interpolate` alignment function produces a value at a given time by interpolating a value from two adjacent input points whose timestamps straddle the output timestamp.

The `next_older` and `next_younger` alignment functions produce the value from the single point in the input time series whose timestamp is next is just prior to or just after the output timestamp.

The `delta`, `rate`, and `delta_gauge` aligner functions compute their output based on the change in the value of the input time series over the time window between the output point end time and the _Duration_ argument earlier. That change in value is computed as follows:

  * Thus the value of the input time series at any given time can be computed by linear interpolation between the nearest point before and the nearest point after the output time. The change in value over a given window is the difference between the interpolated value at the earlier edge of the window and the later edge.

  * The amount of change in the window is the sum of the value of all points whose extent is entirely within the window and the pro-rata share of the value of the points whose extent partially overlaps the window.

  * For a _Cumulative_ time series, interpolation of a value between two adjacent points with the same start time is done by linear interpolation between the two values. Interpolation between two adjacent points with different start times (so the start time of the later point is between the end times of the two points) is handled this way:

    * If the output time is between the earlier point's end time and the later point's start time, the result is the earlier point's value. (No change between the earlier point and the reset time.)

    * If the output time is between the later points start and end time, then the value is the linear interpolation between zero (at the start time) and the point's value.

For a _Cumulative_ time series, the change in value over a given window is the difference between the interpolated value at the earlier edge of the window and the later edge plus a correction for resets. For each reset time that falls within the window, the value of the point just before that reset time is added to the change value to account for the time series value being reset to 0 at that time.

The aggregating aligner functions, `mean_aligner`, `int_mean_aligner`, apply an aggregation function to the input points that fall in a time window whose width is given by the _Duration_ argument and whose later edge is the timestamp of the output point. The result of that aggregation is the value of the output point.

The unit of measure of the output of an aligning function is usually the same as that of the input. The exceptions are:

    * The output of `rate` has the unit of its input divided by the unit 's'.

    * The output of `count_true_aligner` has unit `1`.

    * The output of `fraction_true_aligner` has unit `10^2.%`




#### `rate` Compute a rate of change at aligned points in time.

* * *

Signature: _ImplicitRowInput_ `rate(`_[ lit-Duration ]_ `)` → _Double.Gauge_ _(implicit row input)_

The `rate` aligner operates on input time series with a single value column of numeric (_Int_ or *Double) type. It always produces an output table with a single value column of _Double_ type and _Gauge_ time series kind .

The `rate` aligner computes the change in value of the time series over its window (as described here) and divides that by the width of the window in seconds. The window extends from the output point time to the _Duration_ parameter time earlier.

The default value for the _Duration_ argument is the alignment period. Unlike the 'delta' aligner function, there is no requirement that the alignment period and window width match.

#### `delta` Compute the change in value at aligned points in time.

* * *

Signature: _ImplicitRowInput_ `delta(`_[ lit-Duration ]_ `)` → _InputType.Delta_ _(implicit row input)_

The `delta` aligner operates on input time series with a single value column of _Summable_ type (_Int_ , _Double_ , or _Distribution_) and the output is a time series whose value column is of the same type but has a _Delta_ time series kind.

The `delta_gauge` aligner computes the change in value of the input time series over the time window between the output time and the _Duration_ argument earlier. The output point's start time is the _Duration_ argument earlier than the output time (the point's end time).

The `delta` aligner has the requirement that its _Duration_ argument is the same as the alignment period it is used to align to. The default value for the _Duration_ argument is that alignment period.

Because alerting policies require that the alignment window be able to be different from the alignment period, use the `delta_gauge` aligner.

#### `any_true_aligner` Align a _Bool_ time series by finding any true value in a window.

* * *

Signature: _ImplicitRowInput_ `any_true_aligner(`_[ lit-Duration ]_ `)` → _Bool.Gauge_ _(implicit row input)_

The `any_true_aligner` function operates on an input table with a single value column of _Bool_ type and produces an output table with a single value column of _Bool_ type and _Gauge_ time series kind.

The _Duration_ argument gives the width of a time window for each output point that ends at the time of that output point. If the _Duration_ argument is not given, it defaults to the alignment period. The value of an output point is `true` if any input point in the window is true and is `false` otherwise.

#### `count_true_aligner` Align a _Bool_ time series by counting the true values in a window.

* * *

Signature: _ImplicitRowInput_ `count_true_aligner(`_[ lit-Duration ]_ `)` → _Int.Gauge_ _(implicit row input)_

The `count_true_aligner` function operates on an input table with a single value column of _Bool_ type and produces an output table with a single value column of _Int_ type and _Gauge_ time series kind.

The _Duration_ argument gives the width of a time window for each output point that ends at the time of that output point. If the _Duration_ argument is not given, it defaults to the alignment period. The value of an output point is the number of input points in the window with value `true`.

#### `delta_gauge` Compute the change in value at aligned points in time as a _Gauge_ time series.

* * *

Signature: _ImplicitRowInput_ `delta_gauge(`_[ lit-Duration ]_ `)` → _InputType.Gauge_ _(implicit row input)_

The `delta_gauge` aligner operates on input time series with a single value column of _Summable_ type (_Int_ , _Double_ , or _Distribution_) and the output is a time series whose value column is of the same type but has a _Gauge_ time series kind.

The `delta_gauge` aligner computes the change in value of the input time series over its window (as described here). The window extends from the output point time to the _Duration_ parameter time earlier.

The default value for the _Duration_ argument is the alignment period. Unlike the 'delta' aligner function, there is no requirement that the alignment period and window width match.

#### `fraction_true_aligner` Align a _Bool_ time series with the fraction of true values in a window.

* * *

Signature: _ImplicitRowInput_ `fraction_true_aligner(`_[ lit-Duration ]_ `)` → _Double.Gauge_ _(implicit row input)_

The `fraction_true_aligner` function operates on an input table with a single value column of _Bool_ type and produces an output table with a single value column of _Double_ type and _Gauge_ time series kind.

The _Duration_ argument gives the width of a time window for each output point that ends at the time of that output point. If the _Duration_ argument is not given, it defaults to the alignment period. The value of an output point is the fraction of all input points in the window that have the value `true`.

#### `int_mean_aligner` Align by finding the mean of _Int_ values in a window.

* * *

Signature: _ImplicitRowInput_ `int_mean_aligner(`_[ lit-Duration ]_ `)` → _Int.Gauge_ _(implicit row input)_

The `int_mean_aligner` function operates on an input table with a single value column of _Int_ type and _Gauge_ or _Delta_ time series kind. It produces an output table with a single value column of _Int_ type and _Gauge_ time series kind.

The _Duration_ argument gives the width of a time window for each output point that ends at the time of that output point. If the _Duration_ argument is not given, it defaults to the alignment period. The value of an output point is the mean of the input table value points that fall within this above window, rounded to the nearest integer value.

#### `interpolate` Compute interpolated values at aligned points in time.

* * *

Signature: _ImplicitRowInput_ `interpolate(`_[ lit-Duration ]_ `)` → _InputType.Gauge_ _(implicit row input)_

The `interpolate` aligner operates on an input table with a single value column of numeric (_Int_ or *Double) type and _Gauge_ time series kind. It produces an output table with a single value column of the same type and time series kind.

If the output time for the `interpolate` aligner function is the same as the end time of a point in the input time series, that is used for the output point. Otherwise, the `interpolate` aligner considers the input points whose end time are are the nearest earlier and later points to the output time. If these points are within the _Duration_ argument of one another, the output value is the linear interpolation between those to points at the output time. If there is no input point earlier than the output time or no input point later than the output time or if the two input points are not within _Duration_ argument of each other, no output value is produced.

The default for the _Duration_ argument is twice the alignment period.

#### `mean_aligner` Align by finding the mean of values in a window.

* * *

Signature: _ImplicitRowInput_ `mean_aligner(`_[ lit-Duration ]_ `)` → _Double.Gauge_ _(implicit row input)_

The `mean_aligner` function operates on an input table with a single value column of numeric type. (_Int_ or _Double_) and _Gauge_ or _Delta_ time series kind. It produces an output table with a single value column of _Double_ type and _Gauge_ time series kind.

The _Duration_ argument gives the width of a time window for each output point that ends at the time of that output point. If the _Duration_ argument is not given, it defaults to the alignment period. The value of an output point is the mean of the input table value points that fall within this above window.

#### `next_older` Aligned points in time by moving from an earlier to later time.

* * *

Signature: _ImplicitRowInput_ `next_older(`_[ lit-Duration ]_ `)` → _InputType.Gauge_ _(implicit row input)_

The `next_older` aligner operates on time series with any number of value columns of any type, but all with _Gauge_ time series kind. It produces an output columns of the same type and time series kind.

The `next_older` aligner creates an output point at by finding the latest input point whose end time is no later than the output time and whose end time is no further away from the output time than the _Duration_ argument. If there is no such input point, no output point is created.

The default for the _Duration_ argument is twice the alignment period.

#### `next_younger` Aligned points in time by moving from a later to earlier time.

* * *

Signature: _ImplicitRowInput_ `next_younger(`_[ lit-Duration ]_ `)` → _InputType.Gauge_ _(implicit row input)_

The `next_younger` aligner operates on time series with any number of value columns of any type, but all with _Gauge_ time series kind. It produces an output columns of the same type and time series kind.

The `next_younger` aligner creates an output point at by finding the earliest input point whose end time is no earlier than the output time and whose end time is no further away from the output time than the _Duration_ argument. If there is no such input point, no output point is created.

The default for the _Duration_ argument is twice the alignment period.

### Manipulating Units

These functions change the units of the expressions they are applied to.

#### `scale` Scale a value to a different unit of measure.

* * *

Signature: `scale(`_value: Num_`,` _unit: [ lit-String ]_ `)` → _Double_   
`scale(`_value: Duration_`,` _unit: [ lit-String ]_ `)` → _Double_   
`scale(`_value: Date_`,` _unit: [ lit-String ]_ `)` → _Double_

The `scale` function returns the `value`, converted to double, if necessary, and possibly scaled so it has the units given by the _unit_ argument.

If the _unit_ argument is not given, then the `scale` function merely converts its _value_ argument to double, without changing its units except in cases where automatic scaling is invoked as described here. In that case, the _unit_ argument is supplied implicitly, and `scale` behaves as it normally does with two arguments.

The _unit_ argument, if given, must be a valid UCUM code string for the unit that the _value_ argument is to be scaled to. In this case, the returned value denotes the same physical quantity as the _value_ argument but expressed in the units given by the _unit_ argument. This is done by multiplying the argument by the appropriate scaling factor.

For example, the expression `scale(3 "min", "s")` will convert the value `3` with units minutes (`min`) to the value `180` with units seconds (`s`). The same amount of time, expressed in different units.

It is an error if the _value_ argument has no unit or if the unit of the _value_ argument does not have the same dimension as the unit code given as the _unit_ argument, if given. If they do not have the same dimension, it is not possible to scale the _value_ argument to have the dimension given by the _unit_ argument.

For example, it is an error to say `scale(3 "km", "m/s")`, which asks to scale 3 kilometers into some number of meters per second, because kilometers has the dimension "distance" and meters per second has the dimension "distance per time" (speed). There is no scale factor that can turn distance into speed. One would need to divide the distance by some value with units of time to make this work. For example `scale(3 "km" / 10 "min", "m/s")` will scale `.3 "km/min"` to `5 "m/s"`.

If the _value_ argument is a _Date_ or _Duration_ argument, then the _unit_ argument must give a unit of time (for example `"s"`, `"h"`, or `"wk"`). The returned value will be a _Double_ value designating the amount of time given by the _value_ in the units given by the _unit_ argument. For a _Date_ value, this will be the length of time since the Unix epoch.

For example, `scale(1m, "s")` will result in a value of `60.0` with units `s`, and `scale(d'1970/01/01-01:00:00+00', "h")` results in a value of `1.0` with units `h' (one hour into the Unix epoch).

#### `cast_units` Set the unit of measure of a value.

* * *

Signature: `cast_units(`_Summable_`,` _lit-String_ `)` → _FirstArgType_

The `cast_units` function returns the unchanged value of the first argument but sets the unit of measure for that value to be that given by the second argument string.

The string must be a value UCUM code string for the desired unit. Any unit the first argument may have had before applying this function is ignored.

### Periodic Window

The periodic window functions are used to annotate a _Duration_ actual argument passed to a _WindowDuration_ argument that specifies a window width used to select input points to a periodic calculation. Such an argument is passed to the `group_by` table operation which outputs aligned time series. The `window` and `sliding` functions constrain the input window width according to the output alignment period.

The `window` function indicates that the alignment period and the window width must be the same, making the input point windows be non-overlapping. Because alerting policies require that the alignment window be able to be different from the alignment period, don't use the `window` function in alerting policies.

The `sliding` function indicates that the alignment period can be smaller than the window width, causing input windows to overlap.

#### `window` Indicates a window that is the same as the alignment period.

* * *

Signature: `window(`_[ lit-Duration ]_ `)` → _lit-WindowDuration_

The `window` function annotates a _Duration_ actual argument passed to a _WindowDuration_ argument that specifies a window width used in a calculation that produces aligned time series. It requires that the window width and the output alignment period both be the same as its _Duration_ argument. If the _Duration_ argument is not given, then it specifies that the window width be the output alignment period, however that is defined.

Because alerting policies require that the alignment window be able to be different from the alignment period, don't use the `window` function in alerting policies.

For example, the table operation `|``group_by``window(5m), .mean` produces output points that are the mean value of inputs points falling within a 5m window of the output end time. The `window` function annotates the `5m` window width to require that the alignment period of the `group_by` be 5 minutes as well. The table operation `| group_by window(), .mean` also requires the window width to be the same as the output alignment period, but does not specify what that must be.

#### `sliding` Indicates a window that is sliding (overlapping) rather than disjoint.

* * *

Signature: `sliding(`_lit-Duration_ `)` → _lit-WindowDuration_

The `sliding` function annotates a _Duration_ actual argument passed to a _WindowDuration_ argument that specifies a window width used in a calculation that produces aligned time series. It requires that the window width be its _Duration_ argument and requires that the alignment period be no larger (but allows it to be smaller).

For example, the table operation `|``group_by``sliding(5m), .mean` produces output points that are the mean value of inputs points falling within a 5m window of the output end time. The `sliding` function annotating the `5m` window width indicates that alignment period of the `group_by` can be any time no larger than 5 minutes. If there is an `| every 1m` table operation indicating 1 minute alignment, then the 4 minutes of each 5 minute window will overlap the window of the next-earlier output point.

#### `requested_period` The external requested output alignment period.

* * *

Signature: `requested_period(` `)` → _lit-Duration_

If a query is given in an environment (such as Metrics Explorer or a dashboard) which specifies the period of the query's output using a widget that is outside of the query itself, `requested_period()` returns the value of the externally requested period.

If no externally requested period is given for the query, this will return the default period of `1m`.

The `requested_period()` function can be used in any context in a query that accepts a literal duration, including the `every` table operation, the window argument of aligner functions, and the window argument of the `group_by` table operation.

Example, using `requested_period()` to specify the output period of a query:
    
    
      fetch  gce_instance :: compute.googleapis.com/instance/cpu/usage_time
      | group_by [], mean(val())
      | every requested_period()
    

Example, using `requested_period()` to specify the output period of a query and an aligner window that is twice the output period, but at least `2m`:
    
    
      fetch  gce_instance :: compute.googleapis.com/instance/cpu/usage_time
      | align rate(if(requested_period() < 1m, 2m, requested_period() * 2))
      | group_by [], mean(val())
      | every requested_period()
    

### Distribution

#### `count_from` The number of values in a distribution value.

* * *

Signature: `count_from(`_Distribution.CumulativeOK_ `)` → _Int.FirstArgKind_

The `count_from` function returns the size of the population of values in its input Distribution value.

The unit of measure attached to the result of `count_from` is `1`.

#### `sum_from` The sum of the values in a distribution value.

* * *

Signature: `sum_from(`_Distribution.CumulativeOK_ `)` → _Double.FirstArgKind_

The `sum_from` function returns the sum of all the values contained in its input Distribution value.

The result of `sum_from` has the same unit of measure as the input.

#### `mean_from` The mean of the values in a distribution value.

* * *

Signature: `mean_from(`_Distribution_ `)` → _Double_

The `mean_from` function returns the arithmetic mean of all the values contained in its input Distribution value.

The result of `mean_from` has the same unit of measure as the input.

#### `stddev_from` The standard deviation of the values in a distribution value.

* * *

Signature: `stddev_from(`_Distribution_ `)` → _Double_

The `stddev_from` function returns the variance of the population the values contained in its input Distribution value.

The result of `stddev_from` has the same unit of measure as the input.

#### `variance_from` The variance of the values in a distribution value.

* * *

Signature: `variance_from(`_Distribution_ `)` → _Double_

The `variance_from` function returns the variance of the population the values contained in its input Distribution value.

The result of the 'variance_from' function has no unit of measure.

#### `median_from` The median of the values in a distribution value.

* * *

Signature: `median_from(`_Distribution_ `)` → _Double_

The `median_from` function returns an estimate of the median of the population the values contained in its input Distribution value.

The result of `median_from` has the same unit of measure as the input.

#### `percentile_from` A percentile of the values in a distribution value.

* * *

Signature: `percentile_from(`_Distribution_`,` _lit-Num_ `)` → _Double_

The `percentile_from` function returns an estimate of the percentile of the population the values contained in its input Distribution value. The _Num_ argument gives the percentile to estimate as a number between 0 and 100.

The result of `percentile_from` has the same unit of measure as the input.

#### `fraction_less_than_from` The fraction of values in a distribution that are less than a fixed value.

* * *

Signature: `fraction_less_than_from(`_Distribution_`,` _lit-Num_ `)` → _Double_

The `fraction_less_than_from` function returns an estimate of the fraction of the population the values contained in its input Distribution value that are less than its _Num_ argument.

The unit of measure attached to the result of `fraction_less_than` is `10^2.%`.

#### `bounded_percentile_from` A percentile of the values within a bound in a distribution value.

* * *

Signature: `bounded_percentile_from(`_Distribution_`,` _lit-Num_`,` _[ lit-Num ]_`,` _[ lit-Num ]_ `)` → _Double_

The `bounded_percentile_from` function operates on a subset of the value contained in the input Distribution. An estimate is made of the population of values that are greater than the second _Num_ parameter, if given, and less than or equal to the third _Num_ parameter, if given. At least one or the other of the second and third _Num_ arguments must be given and, if both are given, the second must be less than the third.

This returns an estimate of the percentile of that estimated population of values. The first _Num_ argument gives the percentile to estimate as a number between 0 and 100.

The result of `bounded_percentile_from` has the same unit of measure as the input.

#### `rebucket` Distribution value converted to a new bucket specification.

* * *

Signature: `rebucket(`_Distribution.Delta_`,` _lit-BucketSpecification_ `)` → _Distribution.Delta_   
`rebucket(`_Distribution_`,` _lit-BucketSpecification_ `)` → _Distribution_

This converts the input Distribution value to a Distribution value whose bucket specification is that given in the second argument _BucketSpecification_.

This distributes the counts from each bucket in the input Distribution to the buckets of the output Distribution under the assumption that the values counted in a bucket are evenly distributed across the range of the bucket. The output Distribution has the same total count as the input Distribution but the counts are distributed differently across the output Distribution buckets. The output Distribution has the same sum, mean, and standard deviation as the input Distribution.

### Bucket Specifier

A Distribution value has a histogram made up of buckets. Each bucket is associated with a range of values and contains a count of the values in the Distribution that fall within that range. Every Distribution has a Bucket Specification that describes the boundaries for the buckets in a Distribution value. The functions in this section generate Bucket Specifications.

#### `powers_of` A bucket specification with exponentially increasing bucket boundaries.

* * *

Signature: `powers_of(`_lit-Num_ `)` → _lit-BucketSpecification_

The `powers_of` function returns a bucket specifications where the upper bound of each bucket is fixed factor (given by the _Num_ argument) times the lower bound. Thus the bucket size is exponentially increasing and the error for computing percentiles is a bounded by a constant factor of the true value.

This does not set the number of buckets or the lower bound of the first bucket, both of which must either be specified (by 'num_buckets' and 'lower') or will take the default values (30 buckets, lower bound of 1.0). If the bucket specification is given by `powers_of`, the lower bound must be greater than 0.

The following example gives a bucket specification with 50 buckets whose size grows exponentially at a rate of 1.1, starting at the value 100. So the bucket boundaries are 100, 110, 121, 133.1, and so on.
    
    
    powers_of(1.1).num_buckets(30).lower(100.0)
    

#### `fixed_width` A bucket specification with equal-sized buckets.

* * *

Signature: `fixed_width(`_lit-Num_ `)` → _lit-BucketSpecification_

The `fixed_width` function returns a bucket specifications where the upper bound of each bucket is fixed amount (given by the _Num_ argument) more than the lower bound. Thus the bucket size is fixed.

This does not set the number of buckets or the lower bound of the first bucket, both of which must either be specified (by 'num_buckets' and 'lower') or will take the default values (30 buckets, lower bound of 1.0).

The following example gives a bucket specification with 100 buckets of size 1, staring at 1. This is a good specification for a distribution of percentage values.
    
    
    fixed_width(1).num_buckets(100)
    

#### `custom` A bucket specification from a list of bucket boundaries.

* * *

Signature: `custom(`_lit-Num_ _..._ `)` → _lit-BucketSpecification_

The `custom` function returns a bucket specification with explicitly given bucket bounds. The function takes multiple numeric arguments which must be given in increasing order. The lower bound of the first bucket is given by the first argument and the upper bound of the last bucket is given by the last argument. Each intermediate argument gives the upper bound of the previous bucket and the upper bound of the next bucket.

This completely determines the bucket specification, giving the number of buckets and the exact bound of each.

The following example gives a bucket specification with 3 buckets. The first has boundary 3 and 27, the second 27 and 105, and the third 105 and 277.
    
    
    custom(3,27,105,277)
    

#### `num_buckets` Sets the number of buckets in a bucket specification.

* * *

Signature: `num_buckets(`_lit-BucketSpecification_`,` _lit-Num_ `)` → _lit-BucketSpecification_

When applied to a bucket specification that does not have the number of buckets determined, the `num_buckets` function returns a bucket specification with a number of buckets given by its _Num_ argument. All the other aspects of the input bucket specification are preserved.

It is an error to apply `num_buckets` to a bucket specification that already has the number of buckets determined.

#### `bounds` Sets the lower bound of the first bucket and upper bound of the last.

* * *

Signature: `bounds(`_lit-BucketSpecification_`,` _lit-Num_`,` _lit-Num_ `)` → _lit-BucketSpecification_

When applied to a bucket specification that does not have the lower bound of the first bucket or the upper bound of the last bucket determined, the `bounds` function returns its argument _BucketSpecification_ with the lower bound of its first bucket given by its first _Num_ argument and the upper bound of its last bucket given by the second _Num_ argument. All the other aspects of the input bucket specification are preserved.

It is an error to apply `bounds` to a bucket specification that already has either the lower bound of the first bucket or upper bound of the last bucket determined.

#### `lower` Sets the lower bound of the first bucket in a bucket specification.

* * *

Signature: `lower(`_lit-BucketSpecification_`,` _lit-Num_ `)` → _lit-BucketSpecification_

When applied to a bucket specification that does not have the lower bound of the first bucket determined, the `lower` function returns its argument _BucketSpecification_ with the lower bound of its first bucket given by its _Num_ argument. All the other aspects of the argument bucket specification are preserved.

It is an error to apply `lower` to a bucket specification that already has the lower bound of the first bucket determined.

### Miscellaneous

#### `cast_double` Convert _Int_ value to _Double_.

* * *

Signature: `cast_double(`_Num.CumulativeOK_ `)` → _Double.FirstArgKind_

The `cast_double` function takes a single _Int_ argument and returns the nearest _Double_ value.

The result of `cast_double` has the same unit of measure as the input.

#### `cast_gauge` Cast a _Cumulative_ or _Delta_ time series value to _Gauge_.

* * *

Signature: `cast_gauge(`_ColumnValue.CumulativeOK_ `)` → _FirstArgType.Gauge_

The `cast_gauge` functions returns the value of its argument but changes the time series kind of the value to _Gauge_.

If this results in an output table without value columns that have _Delta_ time series kind, the output table will have no start time column.

The result of `cast_gauge` has the same unit of measure as the input.

#### `within` Specifies the window of the sort value calculation.

* * *

Signature: `within(`_ColumnValue_`,` _[ lit-DateOrDuration ]_`,` _[ lit-DateOrDuration ]_ `)` → _Windowed.FirstArgKind_

The `within` function decorates the expression bound to the _Windowed(Num)_ sort value argument of the `top` or `bottom` table operation. It specifies the window in which the sort value expression is evaluated by specifying one or two out of three of the values: the oldest (starting) time of the window, the youngest (ending) time of the window, or the duration of the window.

If either of the two arguments of `within` is a positive _Duration_ , then that sets the width of the window. At most one of the arguments can be such a _Duration_.

If the first argument is a _Date_ , then that specifies the starting time. If the second argument is a _Date_ , that specifies the ending time. If both are _Date_ values, the second must be later in time than the first. A _Date_ argument can be given as a _Date_ literal or with a negative _Duration_ literal. In the later case, the time is the specified _Duration_ before the ending time of the outer query window (see the `within` table operation).

If the first argument is not given, it defaults to the starting time of the outer query window. If the second argument is not given, it defaults to the ending time of the outer query window.

For example `.mean().within(1h,-2h)` indicates that the `max` reducer should be applied to all the points in the input time series whose end time is within a window of 1 hour width, ending 2 hours ago. The `mean` aggregator is applied to all input points whose end time is in this window.

For example `max(val()).within(10m)` indicates that the `max` reducer should be applied to all the in the input time series whose end time falls within the time range between the query end time and 10 minutes earlier. The `max` aggregator is applied to all input points whose end time is in this window.

## Index of Table Operations and Functions

An index to all the table operations and functions.

  * `abs` Absolute value.
  * `absent_for` Create a condition for the absence of input.
  * `add` The sum of two numbers.
  * `adjacent_delta` The change in value between an input point and next-earlier point.
  * `adjacent_rate` The rate of change between the input and next-earlier points (rows).
  * `aggregate` Default aggregate value from a group of values of any type.
  * `align` Produces an aligned table using an alignment function.
  * `all_true` The conjunction of a group of boolean values.
  * `and` The logical and of two boolean values.
  * `any_true` The disjunction of a group of boolean values.
  * `any_true_aligner` Align a _Bool_ time series by finding any true value in a window.
  * `ascii_to_lower` Change ASCII upper case letter characters to lower case.
  * `ascii_to_upper` Change ASCII lower case letter characters to upper case.
  * `bottom` Selects the bottom time series by a sort-value expression.
  * `bottom_by` Selects time series by a sort-value expression in different groups.
  * `bounded_percentile_from` A percentile of the values within a bound in a distribution value.
  * `bounds` Sets the lower bound of the first bucket and upper bound of the last.
  * `cast_double` Convert _Int_ value to _Double_.
  * `cast_gauge` Cast a _Cumulative_ or _Delta_ time series value to _Gauge_.
  * `cast_units` Set the unit of measure of a value.
  * `concatenate` String concatenation.
  * `condition` Add a boolean condition column to the input table.
  * `count` The count of the number of values in a group of values.
  * `count_from` The number of values in a distribution value.
  * `count_true` The number of true values in a group of boolean values.
  * `count_true_aligner` Align a _Bool_ time series by counting the true values in a window.
  * `covariance` The covariance of a group of pairs of values.
  * `custom` A bucket specification from a list of bucket boundaries.
  * `delta` Compute the change in value at aligned points in time.
  * `delta_gauge` Compute the change in value at aligned points in time as a _Gauge_ time series.
  * `diameter` The maximum minus the minimum of a group of numeric values.
  * `distribution` A distribution from a group of numeric or distribution values.
  * `div` The ratio of two numbers.
  * `end` The ending time of the input point (row).
  * `eq` Equal.
  * `every` Specifies the period for aligned table output.
  * `exp` e raised to a power.
  * `false` The boolean value false.
  * `fetch` Produces a table from the database.
  * `fetch_cumulative` Produces a table of _Cumulative_ time series from the database.
  * `filter` Filters rows from an input table by a predicate.
  * `filter_ratio` Computes the ratio of two filtered sums of the input value column.
  * `filter_ratio_by` Computes a grouped ratio of two filtered sums of the input value column.
  * `fixed_width` A bucket specification with equal-sized buckets.
  * `format` Format _Int64_ , _Double_ , or _String_ as a _String_.
  * `fraction_less_than` The fraction of a group of values less than a fixed value.
  * `fraction_less_than_from` The fraction of values in a distribution that are less than a fixed value.
  * `fraction_true` The fraction of a group of boolean values that are true.
  * `fraction_true_aligner` Align a _Bool_ time series with the fraction of true values in a window.
  * `ge` Greater than or equal.
  * `graph_period` Specifies the preferred output period for drawing time series graphs.
  * `group_by` Aggregates rows by mapped time-series identifier and time window.
  * `gt` Greater than.
  * `has` True if a set argument contains a particular value.
  * `has_value` True if an argument expression computes a value.
  * `hash_tsid` Return a hash of the time series identifier columns.
  * `ident` Identity table operation: no change to the input table.
  * `if` A value conditionally chosen from two values.
  * `int_ceil` Upper bound integer.
  * `int_div` The quotient from the division of two integers.
  * `int_floor` Lower bound integer.
  * `int_mean_aligner` Align by finding the mean of _Int_ values in a window.
  * `int_round` Nearest integer.
  * `interpolate` Compute interpolated values at aligned points in time.
  * `join` Natural join of multiple tables.
  * `le` Less than or equal.
  * `log` Natural logarithm.
  * `lower` Sets the lower bound of the first bucket in a bucket specification.
  * `lt` Less than.
  * `map` Rewrites the time-series identifier and value columns of each row in a table.
  * `max` The maximum of a group of numeric values.
  * `mean` The mean of a group of numeric values.
  * `mean_aligner` Align by finding the mean of values in a window.
  * `mean_from` The mean of the values in a distribution value.
  * `median` The median of a group of numeric or distribution values.
  * `median_from` The median of the values in a distribution value.
  * `metric` Produces the table for a specific metric type from a set of tables.
  * `min` The minimum of a group of numeric values.
  * `mul` The product of two numbers.
  * `ne` Not equal.
  * `neg` The negative of a number.
  * `next_older` Aligned points in time by moving from an earlier to later time.
  * `next_younger` Aligned points in time by moving from a later to earlier time.
  * `not` The logical negation of a boolean value.
  * `num_buckets` Sets the number of buckets in a bucket specification.
  * `older` A value from the next-earlier point (row) in a time series.
  * `or` The logical or of two boolean values.
  * `or_else` A value or, if it is not a value, another value.
  * `outer_join` Outer natural join of two tables.
  * `percentile` A percentile of a group of numeric or distribution values.
  * `percentile_from` A percentile of the values in a distribution value.
  * `pick_any` The value of any element of a group of values (chosen arbitrarily).
  * `pick_bottom_rows` Picks rows by minimal sort-value expression.
  * `pick_top_rows` Picks rows by maximal a sort-value expression.
  * `pos` Identity for numeric inputs.
  * `power` One number to the power of another.
  * `powers_of` A bucket specification with exponentially increasing bucket boundaries.
  * `rate` Compute a rate of change at aligned points in time.
  * `ratio` Computes the ratio of value columns of two aligned input tables.
  * `re_extract` Extract values matched by a regular expression in another string.
  * `re_full_match` True if a regular expression matches the whole of a string value.
  * `re_global_replace` Replace all matches of a regular expression in another string.
  * `re_partial_match` True if a regular expression matches some part of string value.
  * `re_replace` Replace the first match of a regular expression in another string.
  * `rebucket` Distribution value converted to a new bucket specification.
  * `rem` The remainder from the division of two integers.
  * `requested_period` The external requested output alignment period.
  * `row_count` The number of input rows encountered.
  * `scale` Scale a value to a different unit of measure.
  * `singleton` The value of the element of a group of values with only one element.
  * `sliding` Indicates a window that is sliding (overlapping) rather than disjoint.
  * `sqrt` Square root.
  * `start` The starting time of the input point (row).
  * `stddev` The standard deviation of a group of values.
  * `stddev_from` The standard deviation of the values in a distribution value.
  * `string_to_double` Convert _String_ to _Double_.
  * `string_to_int64` Convert _String_ to _Int_.
  * `string_to_timestamp` Convert _String_ to _Date_ using date format and optional timezone.
  * `sub` The difference of two numbers.
  * `sum` The sum of a group of numeric values.
  * `sum_from` The sum of the values in a distribution value.
  * `time_shift` Shift time series forward in time.
  * `timestamp_to_string` Convert _Timestamp_ to _String_ using date format and optional timezone.
  * `top` Selects the top time series by a sort-value expression.
  * `top_by` Selects time series by a sort-value expression in different groups.
  * `true` The boolean value true.
  * `unaligned_group_by` Aggregates rows by mapped time-series identifier without alignment.
  * `union` Union of multiple tables.
  * `union_group_by` Aggregates rows from multiple tables.
  * `unique` The common value of a group of values (which must all be the same).
  * `utf8_normalize` Unicode string suitable for case-folding comparison.
  * `val` A value column's value in the input point (row).
  * `value` Rewrites the value columns of each row in a table.
  * `variance` The variance of a group of numeric values.
  * `variance_from` The variance of the values in a distribution value.
  * `weighted_distribution` A distribution from a group of weighted values.
  * `window` Specifies the window for alignment operations.
  * `window` Indicates a window that is the same as the alignment period.
  * `within` Specifies the window of the sort value calculation.
  * `within` Specifies the time range of the query output.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.SqlConditionOrBuilder
title: Interface AlertPolicy.Condition.SqlConditionOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:50.779265+00:00
---

# Interface AlertPolicy.Condition.SqlConditionOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.SqlConditionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AlertPolicy.Condition.SqlConditionOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.6  3.3.6  3.2.10 
    
    
    public static interface AlertPolicy.Condition.SqlConditionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBooleanTest()
    
    
    public abstract AlertPolicy.Condition.SqlCondition.BooleanTest getBooleanTest()

Test the boolean value in the indicated column.

` .google.monitoring.v3.AlertPolicy.Condition.SqlCondition.BooleanTest boolean_test = 6; `

**Returns**  
---  
**Type** | **Description**  
`[AlertPolicy.Condition.SqlCondition.BooleanTest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.BooleanTest)` | The booleanTest.  
  
### getBooleanTestOrBuilder()
    
    
    public abstract AlertPolicy.Condition.SqlCondition.BooleanTestOrBuilder getBooleanTestOrBuilder()

Test the boolean value in the indicated column.

` .google.monitoring.v3.AlertPolicy.Condition.SqlCondition.BooleanTest boolean_test = 6; `

**Returns**  
---  
**Type** | **Description**  
`[AlertPolicy.Condition.SqlCondition.BooleanTestOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.BooleanTestOrBuilder)` |   
  
### getDaily()
    
    
    public abstract AlertPolicy.Condition.SqlCondition.Daily getDaily()

Schedule the query to execute every so many days.

`.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Daily daily = 4;`

**Returns**  
---  
**Type** | **Description**  
`[AlertPolicy.Condition.SqlCondition.Daily](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Daily)` | The daily.  
  
### getDailyOrBuilder()
    
    
    public abstract AlertPolicy.Condition.SqlCondition.DailyOrBuilder getDailyOrBuilder()

Schedule the query to execute every so many days.

`.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Daily daily = 4;`

**Returns**  
---  
**Type** | **Description**  
`[AlertPolicy.Condition.SqlCondition.DailyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.DailyOrBuilder)` |   
  
### getEvaluateCase()
    
    
    public abstract AlertPolicy.Condition.SqlCondition.EvaluateCase getEvaluateCase()

**Returns**  
---  
**Type** | **Description**  
`[AlertPolicy.Condition.SqlCondition.EvaluateCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.EvaluateCase)` |   
  
### getHourly()
    
    
    public abstract AlertPolicy.Condition.SqlCondition.Hourly getHourly()

Schedule the query to execute every so many hours.

`.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Hourly hourly = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AlertPolicy.Condition.SqlCondition.Hourly](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Hourly)` | The hourly.  
  
### getHourlyOrBuilder()
    
    
    public abstract AlertPolicy.Condition.SqlCondition.HourlyOrBuilder getHourlyOrBuilder()

Schedule the query to execute every so many hours.

`.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Hourly hourly = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AlertPolicy.Condition.SqlCondition.HourlyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.HourlyOrBuilder)` |   
  
### getMinutes()
    
    
    public abstract AlertPolicy.Condition.SqlCondition.Minutes getMinutes()

Schedule the query to execute every so many minutes.

`.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Minutes minutes = 2;`

**Returns**  
---  
**Type** | **Description**  
`[AlertPolicy.Condition.SqlCondition.Minutes](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Minutes)` | The minutes.  
  
### getMinutesOrBuilder()
    
    
    public abstract AlertPolicy.Condition.SqlCondition.MinutesOrBuilder getMinutesOrBuilder()

Schedule the query to execute every so many minutes.

`.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Minutes minutes = 2;`

**Returns**  
---  
**Type** | **Description**  
`[AlertPolicy.Condition.SqlCondition.MinutesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.MinutesOrBuilder)` |   
  
### getQuery()
    
    
    public abstract String getQuery()

Required. The Log Analytics SQL query to run, as a string. The query must conform to the required shape. Specifically, the query must not try to filter the input by time. A filter will automatically be applied to filter the input so that the query receives all rows received since the last time the query was run.

For example, the following query extracts all log entries containing an HTTP request:

SELECT timestamp, log_name, severity, http_request, resource, labels FROM my-project.global._Default._AllLogs WHERE http_request IS NOT NULL

`string query = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The query.  
  
### getQueryBytes()
    
    
    public abstract ByteString getQueryBytes()

Required. The Log Analytics SQL query to run, as a string. The query must conform to the required shape. Specifically, the query must not try to filter the input by time. A filter will automatically be applied to filter the input so that the query receives all rows received since the last time the query was run.

For example, the following query extracts all log entries containing an HTTP request:

SELECT timestamp, log_name, severity, http_request, resource, labels FROM my-project.global._Default._AllLogs WHERE http_request IS NOT NULL

`string query = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for query.  
  
### getRowCountTest()
    
    
    public abstract AlertPolicy.Condition.SqlCondition.RowCountTest getRowCountTest()

Test the row count against a threshold.

` .google.monitoring.v3.AlertPolicy.Condition.SqlCondition.RowCountTest row_count_test = 5; `

**Returns**  
---  
**Type** | **Description**  
`[AlertPolicy.Condition.SqlCondition.RowCountTest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.RowCountTest)` | The rowCountTest.  
  
### getRowCountTestOrBuilder()
    
    
    public abstract AlertPolicy.Condition.SqlCondition.RowCountTestOrBuilder getRowCountTestOrBuilder()

Test the row count against a threshold.

` .google.monitoring.v3.AlertPolicy.Condition.SqlCondition.RowCountTest row_count_test = 5; `

**Returns**  
---  
**Type** | **Description**  
`[AlertPolicy.Condition.SqlCondition.RowCountTestOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.RowCountTestOrBuilder)` |   
  
### getScheduleCase()
    
    
    public abstract AlertPolicy.Condition.SqlCondition.ScheduleCase getScheduleCase()

**Returns**  
---  
**Type** | **Description**  
`[AlertPolicy.Condition.SqlCondition.ScheduleCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.ScheduleCase)` |   
  
### hasBooleanTest()
    
    
    public abstract boolean hasBooleanTest()

Test the boolean value in the indicated column.

` .google.monitoring.v3.AlertPolicy.Condition.SqlCondition.BooleanTest boolean_test = 6; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the booleanTest field is set.  
  
### hasDaily()
    
    
    public abstract boolean hasDaily()

Schedule the query to execute every so many days.

`.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Daily daily = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the daily field is set.  
  
### hasHourly()
    
    
    public abstract boolean hasHourly()

Schedule the query to execute every so many hours.

`.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Hourly hourly = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the hourly field is set.  
  
### hasMinutes()
    
    
    public abstract boolean hasMinutes()

Schedule the query to execute every so many minutes.

`.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Minutes minutes = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the minutes field is set.  
  
### hasRowCountTest()
    
    
    public abstract boolean hasRowCountTest()

Test the row count against a threshold.

` .google.monitoring.v3.AlertPolicy.Condition.SqlCondition.RowCountTest row_count_test = 5; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rowCountTest field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

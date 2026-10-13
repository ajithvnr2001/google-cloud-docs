---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.FlagOrBuilder
title: Interface FlagOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:02.624261+00:00
---

# Interface FlagOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.FlagOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FlagOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface FlagOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAllowedIntValues(int index)
    
    
    public abstract long getAllowedIntValues(int index)

Use this field if only certain integers are accepted. Can be combined with min_value and max_value to add additional values.

`repeated int64 allowed_int_values = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allowedIntValues at the given index.  
  
### getAllowedIntValuesCount()
    
    
    public abstract int getAllowedIntValuesCount()

Use this field if only certain integers are accepted. Can be combined with min_value and max_value to add additional values.

`repeated int64 allowed_int_values = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of allowedIntValues.  
  
### getAllowedIntValuesList()
    
    
    public abstract List<Long> getAllowedIntValuesList()

Use this field if only certain integers are accepted. Can be combined with min_value and max_value to add additional values.

`repeated int64 allowed_int_values = 10;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` | A list containing the allowedIntValues.  
  
### getAllowedStringValues(int index)
    
    
    public abstract String getAllowedStringValues(int index)

For `STRING` flags, a list of strings that the value can be set to.

`repeated string allowed_string_values = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowedStringValues at the given index.  
  
### getAllowedStringValuesBytes(int index)
    
    
    public abstract ByteString getAllowedStringValuesBytes(int index)

For `STRING` flags, a list of strings that the value can be set to.

`repeated string allowed_string_values = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the allowedStringValues at the given index.  
  
### getAllowedStringValuesCount()
    
    
    public abstract int getAllowedStringValuesCount()

For `STRING` flags, a list of strings that the value can be set to.

`repeated string allowed_string_values = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of allowedStringValues.  
  
### getAllowedStringValuesList()
    
    
    public abstract List<String> getAllowedStringValuesList()

For `STRING` flags, a list of strings that the value can be set to.

`repeated string allowed_string_values = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the allowedStringValues.  
  
### getAppliesTo(int index)
    
    
    public abstract SqlDatabaseVersion getAppliesTo(int index)

The database version this flag applies to. Can be MySQL instances: `MYSQL_8_0`, `MYSQL_8_0_18`, `MYSQL_8_0_26`, `MYSQL_5_7`, or `MYSQL_5_6`. PostgreSQL instances: `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11` or `POSTGRES_12`. SQL Server instances: `SQLSERVER_2017_STANDARD`, `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`, `SQLSERVER_2019_STANDARD`, `SQLSERVER_2019_ENTERPRISE`, `SQLSERVER_2019_EXPRESS`, or `SQLSERVER_2019_WEB`. See [the complete list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion).

`repeated .google.cloud.sql.v1beta4.SqlDatabaseVersion applies_to = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[SqlDatabaseVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlDatabaseVersion)` | The appliesTo at the given index.  
  
### getAppliesToCount()
    
    
    public abstract int getAppliesToCount()

The database version this flag applies to. Can be MySQL instances: `MYSQL_8_0`, `MYSQL_8_0_18`, `MYSQL_8_0_26`, `MYSQL_5_7`, or `MYSQL_5_6`. PostgreSQL instances: `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11` or `POSTGRES_12`. SQL Server instances: `SQLSERVER_2017_STANDARD`, `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`, `SQLSERVER_2019_STANDARD`, `SQLSERVER_2019_ENTERPRISE`, `SQLSERVER_2019_EXPRESS`, or `SQLSERVER_2019_WEB`. See [the complete list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion).

`repeated .google.cloud.sql.v1beta4.SqlDatabaseVersion applies_to = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of appliesTo.  
  
### getAppliesToList()
    
    
    public abstract List<SqlDatabaseVersion> getAppliesToList()

The database version this flag applies to. Can be MySQL instances: `MYSQL_8_0`, `MYSQL_8_0_18`, `MYSQL_8_0_26`, `MYSQL_5_7`, or `MYSQL_5_6`. PostgreSQL instances: `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11` or `POSTGRES_12`. SQL Server instances: `SQLSERVER_2017_STANDARD`, `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`, `SQLSERVER_2019_STANDARD`, `SQLSERVER_2019_ENTERPRISE`, `SQLSERVER_2019_EXPRESS`, or `SQLSERVER_2019_WEB`. See [the complete list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion).

`repeated .google.cloud.sql.v1beta4.SqlDatabaseVersion applies_to = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SqlDatabaseVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlDatabaseVersion)>` | A list containing the appliesTo.  
  
### getAppliesToValue(int index)
    
    
    public abstract int getAppliesToValue(int index)

The database version this flag applies to. Can be MySQL instances: `MYSQL_8_0`, `MYSQL_8_0_18`, `MYSQL_8_0_26`, `MYSQL_5_7`, or `MYSQL_5_6`. PostgreSQL instances: `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11` or `POSTGRES_12`. SQL Server instances: `SQLSERVER_2017_STANDARD`, `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`, `SQLSERVER_2019_STANDARD`, `SQLSERVER_2019_ENTERPRISE`, `SQLSERVER_2019_EXPRESS`, or `SQLSERVER_2019_WEB`. See [the complete list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion).

`repeated .google.cloud.sql.v1beta4.SqlDatabaseVersion applies_to = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of appliesTo at the given index.  
  
### getAppliesToValueList()
    
    
    public abstract List<Integer> getAppliesToValueList()

The database version this flag applies to. Can be MySQL instances: `MYSQL_8_0`, `MYSQL_8_0_18`, `MYSQL_8_0_26`, `MYSQL_5_7`, or `MYSQL_5_6`. PostgreSQL instances: `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11` or `POSTGRES_12`. SQL Server instances: `SQLSERVER_2017_STANDARD`, `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`, `SQLSERVER_2019_STANDARD`, `SQLSERVER_2019_ENTERPRISE`, `SQLSERVER_2019_EXPRESS`, or `SQLSERVER_2019_WEB`. See [the complete list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion).

`repeated .google.cloud.sql.v1beta4.SqlDatabaseVersion applies_to = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for appliesTo.  
  
### getFlagScope()
    
    
    public abstract SqlFlagScope getFlagScope()

Scope of flag.

`.google.cloud.sql.v1beta4.SqlFlagScope flag_scope = 15;`

**Returns**  
---  
**Type** | **Description**  
`[SqlFlagScope](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlFlagScope)` | The flagScope.  
  
### getFlagScopeValue()
    
    
    public abstract int getFlagScopeValue()

Scope of flag.

`.google.cloud.sql.v1beta4.SqlFlagScope flag_scope = 15;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for flagScope.  
  
### getInBeta()
    
    
    public abstract BoolValue getInBeta()

Whether or not the flag is considered in beta.

`.google.protobuf.BoolValue in_beta = 9;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)` | The inBeta.  
  
### getInBetaOrBuilder()
    
    
    public abstract BoolValueOrBuilder getInBetaOrBuilder()

Whether or not the flag is considered in beta.

`.google.protobuf.BoolValue in_beta = 9;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValueOrBuilder.html)` |   
  
### getKind()
    
    
    public abstract String getKind()

This is always `sql#flag`.

`string kind = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public abstract ByteString getKindBytes()

This is always `sql#flag`.

`string kind = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getMaxValue()
    
    
    public abstract Int64Value getMaxValue()

For `INTEGER` flags, the maximum allowed value.

`.google.protobuf.Int64Value max_value = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Int64Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.html)` | The maxValue.  
  
### getMaxValueOrBuilder()
    
    
    public abstract Int64ValueOrBuilder getMaxValueOrBuilder()

For `INTEGER` flags, the maximum allowed value.

`.google.protobuf.Int64Value max_value = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Int64ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64ValueOrBuilder.html)` |   
  
### getMinValue()
    
    
    public abstract Int64Value getMinValue()

For `INTEGER` flags, the minimum allowed value.

`.google.protobuf.Int64Value min_value = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Int64Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.html)` | The minValue.  
  
### getMinValueOrBuilder()
    
    
    public abstract Int64ValueOrBuilder getMinValueOrBuilder()

For `INTEGER` flags, the minimum allowed value.

`.google.protobuf.Int64Value min_value = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Int64ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64ValueOrBuilder.html)` |   
  
### getName()
    
    
    public abstract String getName()

This is the name of the flag. Flag names always use underscores, not hyphens, for example: `max_allowed_packet`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

This is the name of the flag. Flag names always use underscores, not hyphens, for example: `max_allowed_packet`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getRecommendedIntValue()
    
    
    public abstract Int64Value getRecommendedIntValue()

Recommended flag value in integer format for UI display.

`.google.protobuf.Int64Value recommended_int_value = 17;`

**Returns**  
---  
**Type** | **Description**  
`[Int64Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.html)` | The recommendedIntValue.  
  
### getRecommendedIntValueOrBuilder()
    
    
    public abstract Int64ValueOrBuilder getRecommendedIntValueOrBuilder()

Recommended flag value in integer format for UI display.

`.google.protobuf.Int64Value recommended_int_value = 17;`

**Returns**  
---  
**Type** | **Description**  
`[Int64ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64ValueOrBuilder.html)` |   
  
### getRecommendedStringValue()
    
    
    public abstract String getRecommendedStringValue()

Recommended flag value in string format for UI display.

`string recommended_string_value = 16;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The recommendedStringValue.  
  
### getRecommendedStringValueBytes()
    
    
    public abstract ByteString getRecommendedStringValueBytes()

Recommended flag value in string format for UI display.

`string recommended_string_value = 16;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for recommendedStringValue.  
  
### getRecommendedValueCase()
    
    
    public abstract Flag.RecommendedValueCase getRecommendedValueCase()

**Returns**  
---  
**Type** | **Description**  
`[Flag.RecommendedValueCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.Flag.RecommendedValueCase)` |   
  
### getRequiresRestart()
    
    
    public abstract BoolValue getRequiresRestart()

Indicates whether changing this flag will trigger a database restart. Only applicable to Second Generation instances.

`.google.protobuf.BoolValue requires_restart = 7;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)` | The requiresRestart.  
  
### getRequiresRestartOrBuilder()
    
    
    public abstract BoolValueOrBuilder getRequiresRestartOrBuilder()

Indicates whether changing this flag will trigger a database restart. Only applicable to Second Generation instances.

`.google.protobuf.BoolValue requires_restart = 7;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValueOrBuilder.html)` |   
  
### getType()
    
    
    public abstract SqlFlagType getType()

The type of the flag. Flags are typed to being `BOOLEAN`, `STRING`, `INTEGER` or `NONE`. `NONE` is used for flags which do not take a value, such as `skip_grant_tables`.

`.google.cloud.sql.v1beta4.SqlFlagType type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[SqlFlagType](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlFlagType)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

The type of the flag. Flags are typed to being `BOOLEAN`, `STRING`, `INTEGER` or `NONE`. `NONE` is used for flags which do not take a value, such as `skip_grant_tables`.

`.google.cloud.sql.v1beta4.SqlFlagType type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### hasInBeta()
    
    
    public abstract boolean hasInBeta()

Whether or not the flag is considered in beta.

`.google.protobuf.BoolValue in_beta = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the inBeta field is set.  
  
### hasMaxValue()
    
    
    public abstract boolean hasMaxValue()

For `INTEGER` flags, the maximum allowed value.

`.google.protobuf.Int64Value max_value = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maxValue field is set.  
  
### hasMinValue()
    
    
    public abstract boolean hasMinValue()

For `INTEGER` flags, the minimum allowed value.

`.google.protobuf.Int64Value min_value = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the minValue field is set.  
  
### hasRecommendedIntValue()
    
    
    public abstract boolean hasRecommendedIntValue()

Recommended flag value in integer format for UI display.

`.google.protobuf.Int64Value recommended_int_value = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the recommendedIntValue field is set.  
  
### hasRecommendedStringValue()
    
    
    public abstract boolean hasRecommendedStringValue()

Recommended flag value in string format for UI display.

`string recommended_string_value = 16;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the recommendedStringValue field is set.  
  
### hasRequiresRestart()
    
    
    public abstract boolean hasRequiresRestart()

Indicates whether changing this flag will trigger a database restart. Only applicable to Second Generation instances.

`.google.protobuf.BoolValue requires_restart = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the requiresRestart field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

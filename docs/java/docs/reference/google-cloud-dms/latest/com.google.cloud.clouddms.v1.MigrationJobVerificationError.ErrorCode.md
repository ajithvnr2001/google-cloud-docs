---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJobVerificationError.ErrorCode
title: Enum MigrationJobVerificationError.ErrorCode (2.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:41.261864+00:00
---

# Enum MigrationJobVerificationError.ErrorCode (2.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJobVerificationError.ErrorCode

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum MigrationJobVerificationError.ErrorCode (2.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.98.0 (latest)  2.94.0  2.93.0  2.92.0  2.90.0  2.87.0  2.86.0  2.84.0  2.82.0  2.81.0  2.80.0  2.79.0  2.77.0  2.75.0  2.74.0  2.73.0  2.72.0  2.71.0  2.69.0  2.67.0  2.66.0  2.63.0  2.62.0  2.61.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.8  2.1.9 
    
    
    public enum MigrationJobVerificationError.ErrorCode extends Enum<MigrationJobVerificationError.ErrorCode> implements ProtocolMessageEnum

A general error code describing the type of error that occurred.

Protobuf enum `google.cloud.clouddms.v1.MigrationJobVerificationError.ErrorCode`

## Implements

[ProtocolMessageEnum](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolMessageEnum.html)

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`AUTHENTICATION_FAILURE` |  We failed to authenticate to one of the connection profile. `AUTHENTICATION_FAILURE = 2;`  
`AUTHENTICATION_FAILURE_VALUE` |  We failed to authenticate to one of the connection profile. `AUTHENTICATION_FAILURE = 2;`  
`CANT_RESTART_RUNNING_MIGRATION` |  Migration is already running at the time of restart request. `CANT_RESTART_RUNNING_MIGRATION = 21;`  
`CANT_RESTART_RUNNING_MIGRATION_VALUE` |  Migration is already running at the time of restart request. `CANT_RESTART_RUNNING_MIGRATION = 21;`  
`CONNECTION_FAILURE` |  We failed to connect to one of the connection profile. `CONNECTION_FAILURE = 1;`  
`CONNECTION_FAILURE_VALUE` |  We failed to connect to one of the connection profile. `CONNECTION_FAILURE = 1;`  
`CONNECTION_PROFILE_TYPES_INCOMPATIBILITY` |  The types of the source and the destination are incompatible. `CONNECTION_PROFILE_TYPES_INCOMPATIBILITY = 5;`  
`CONNECTION_PROFILE_TYPES_INCOMPATIBILITY_VALUE` |  The types of the source and the destination are incompatible. `CONNECTION_PROFILE_TYPES_INCOMPATIBILITY = 5;`  
`ERROR_CODE_UNSPECIFIED` |  An unknown error occurred `ERROR_CODE_UNSPECIFIED = 0;`  
`ERROR_CODE_UNSPECIFIED_VALUE` |  An unknown error occurred `ERROR_CODE_UNSPECIFIED = 0;`  
`ERROR_RDBMS` |  There was an underlying RDBMS error. `ERROR_RDBMS = 27;`  
`ERROR_RDBMS_VALUE` |  There was an underlying RDBMS error. `ERROR_RDBMS = 27;`  
`EXISTING_CONFLICTING_DATABASES` |  The destination DB contains existing databases that are conflicting with those in the source DB. `EXISTING_CONFLICTING_DATABASES = 29;`  
`EXISTING_CONFLICTING_DATABASES_VALUE` |  The destination DB contains existing databases that are conflicting with those in the source DB. `EXISTING_CONFLICTING_DATABASES = 29;`  
`INSUFFICIENT_MAX_REPLICATION_SLOTS` |  The value of parameter max_replication_slots is not sufficient. `INSUFFICIENT_MAX_REPLICATION_SLOTS = 11;`  
`INSUFFICIENT_MAX_REPLICATION_SLOTS_VALUE` |  The value of parameter max_replication_slots is not sufficient. `INSUFFICIENT_MAX_REPLICATION_SLOTS = 11;`  
`INSUFFICIENT_MAX_WAL_SENDERS` |  The value of parameter max_wal_senders is not sufficient. `INSUFFICIENT_MAX_WAL_SENDERS = 12;`  
`INSUFFICIENT_MAX_WAL_SENDERS_VALUE` |  The value of parameter max_wal_senders is not sufficient. `INSUFFICIENT_MAX_WAL_SENDERS = 12;`  
`INSUFFICIENT_MAX_WORKER_PROCESSES` |  The value of parameter max_worker_processes is not sufficient. `INSUFFICIENT_MAX_WORKER_PROCESSES = 13;`  
`INSUFFICIENT_MAX_WORKER_PROCESSES_VALUE` |  The value of parameter max_worker_processes is not sufficient. `INSUFFICIENT_MAX_WORKER_PROCESSES = 13;`  
`INVALID_CONNECTION_PROFILE_CONFIG` |  One of the involved connection profiles has an invalid configuration. `INVALID_CONNECTION_PROFILE_CONFIG = 3;`  
`INVALID_CONNECTION_PROFILE_CONFIG_VALUE` |  One of the involved connection profiles has an invalid configuration. `INVALID_CONNECTION_PROFILE_CONFIG = 3;`  
`INVALID_RDS_LOGICAL_REPLICATION` |  Invalid RDS logical replication. `INVALID_RDS_LOGICAL_REPLICATION = 16;`  
`INVALID_RDS_LOGICAL_REPLICATION_VALUE` |  Invalid RDS logical replication. `INVALID_RDS_LOGICAL_REPLICATION = 16;`  
`INVALID_SHARED_PRELOAD_LIBRARY` |  The value of parameter shared_preload_libraries does not include pglogical. `INVALID_SHARED_PRELOAD_LIBRARY = 10;`  
`INVALID_SHARED_PRELOAD_LIBRARY_VALUE` |  The value of parameter shared_preload_libraries does not include pglogical. `INVALID_SHARED_PRELOAD_LIBRARY = 10;`  
`INVALID_WAL_LEVEL` |  The value of parameter wal_level is not set to logical. `INVALID_WAL_LEVEL = 9;`  
`INVALID_WAL_LEVEL_VALUE` |  The value of parameter wal_level is not set to logical. `INVALID_WAL_LEVEL = 9;`  
`NO_PGLOGICAL_INSTALLED` |  No pglogical extension installed on databases, applicable for postgres. `NO_PGLOGICAL_INSTALLED = 7;`  
`NO_PGLOGICAL_INSTALLED_VALUE` |  No pglogical extension installed on databases, applicable for postgres. `NO_PGLOGICAL_INSTALLED = 7;`  
`PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE` |  Insufficient privilege to enable the parallelism configuration. `PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE = 30;`  
`PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE_VALUE` |  Insufficient privilege to enable the parallelism configuration. `PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE = 30;`  
`PGLOGICAL_NODE_ALREADY_EXISTS` |  pglogical node already exists on databases, applicable for postgres. `PGLOGICAL_NODE_ALREADY_EXISTS = 8;`  
`PGLOGICAL_NODE_ALREADY_EXISTS_VALUE` |  pglogical node already exists on databases, applicable for postgres. `PGLOGICAL_NODE_ALREADY_EXISTS = 8;`  
`SOURCE_ALREADY_SETUP` |  The source already has a replication setup. `SOURCE_ALREADY_SETUP = 23;`  
`SOURCE_ALREADY_SETUP_VALUE` |  The source already has a replication setup. `SOURCE_ALREADY_SETUP = 23;`  
`SOURCE_SIZE_EXCEEDS_THRESHOLD` |  The source DB size in Bytes exceeds a certain threshold. The migration might require an increase of quota, or might not be supported. `SOURCE_SIZE_EXCEEDS_THRESHOLD = 28;`  
`SOURCE_SIZE_EXCEEDS_THRESHOLD_VALUE` |  The source DB size in Bytes exceeds a certain threshold. The migration might require an increase of quota, or might not be supported. `SOURCE_SIZE_EXCEEDS_THRESHOLD = 28;`  
`TABLES_WITH_LIMITED_SUPPORT` |  The source has tables with limited support. E.g. PostgreSQL tables without primary keys. `TABLES_WITH_LIMITED_SUPPORT = 24;`  
`TABLES_WITH_LIMITED_SUPPORT_VALUE` |  The source has tables with limited support. E.g. PostgreSQL tables without primary keys. `TABLES_WITH_LIMITED_SUPPORT = 24;`  
`UNRECOGNIZED` |   
`UNSUPPORTED_DATABASE_FDW_CONFIG` |  The source uses an unsupported Foreign Data Wrapper configuration. `UNSUPPORTED_DATABASE_FDW_CONFIG = 26;`  
`UNSUPPORTED_DATABASE_FDW_CONFIG_VALUE` |  The source uses an unsupported Foreign Data Wrapper configuration. `UNSUPPORTED_DATABASE_FDW_CONFIG = 26;`  
`UNSUPPORTED_DATABASE_LOCALE` |  The source uses an unsupported locale. `UNSUPPORTED_DATABASE_LOCALE = 25;`  
`UNSUPPORTED_DATABASE_LOCALE_VALUE` |  The source uses an unsupported locale. `UNSUPPORTED_DATABASE_LOCALE = 25;`  
`UNSUPPORTED_DEFINER` |  The definer is not supported. `UNSUPPORTED_DEFINER = 19;`  
`UNSUPPORTED_DEFINER_VALUE` |  The definer is not supported. `UNSUPPORTED_DEFINER = 19;`  
`UNSUPPORTED_EXTENSIONS` |  Extensions installed are either not supported or having unsupported versions. `UNSUPPORTED_EXTENSIONS = 14;`  
`UNSUPPORTED_EXTENSIONS_VALUE` |  Extensions installed are either not supported or having unsupported versions. `UNSUPPORTED_EXTENSIONS = 14;`  
`UNSUPPORTED_GTID_MODE` |  The gtid_mode is not supported, applicable for MySQL. `UNSUPPORTED_GTID_MODE = 17;`  
`UNSUPPORTED_GTID_MODE_VALUE` |  The gtid_mode is not supported, applicable for MySQL. `UNSUPPORTED_GTID_MODE = 17;`  
`UNSUPPORTED_MIGRATION_TYPE` |  Unsupported migration type. `UNSUPPORTED_MIGRATION_TYPE = 15;`  
`UNSUPPORTED_MIGRATION_TYPE_VALUE` |  Unsupported migration type. `UNSUPPORTED_MIGRATION_TYPE = 15;`  
`UNSUPPORTED_TABLE_DEFINITION` |  The table definition is not support due to missing primary key or replica identity. `UNSUPPORTED_TABLE_DEFINITION = 18;`  
`UNSUPPORTED_TABLE_DEFINITION_VALUE` |  The table definition is not support due to missing primary key or replica identity. `UNSUPPORTED_TABLE_DEFINITION = 18;`  
`VERSION_INCOMPATIBILITY` |  The versions of the source and the destination are incompatible. `VERSION_INCOMPATIBILITY = 4;`  
`VERSION_INCOMPATIBILITY_VALUE` |  The versions of the source and the destination are incompatible. `VERSION_INCOMPATIBILITY = 4;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.MigrationJobVerificationError.ErrorCode#com_google_cloud_clouddms_v1_MigrationJobVerificationError_ErrorCode_forNumber_int_) instead._  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

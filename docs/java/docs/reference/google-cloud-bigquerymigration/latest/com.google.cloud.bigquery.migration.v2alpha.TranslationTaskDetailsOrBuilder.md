---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TranslationTaskDetailsOrBuilder
title: Interface TranslationTaskDetailsOrBuilder (0.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:20.852911+00:00
---

# Interface TranslationTaskDetailsOrBuilder (0.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TranslationTaskDetailsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TranslationTaskDetailsOrBuilder (0.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.102.0 (latest)  0.98.0  0.97.0  0.96.0  0.94.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.67.0  0.66.0  0.65.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.4 
    
    
    public interface TranslationTaskDetailsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsSpecialTokenMap(String key)
    
    
    public abstract boolean containsSpecialTokenMap(String key)

The map capturing special tokens to be replaced during translation. The key is special token in string. The value is the token data type. This is used to translate SQL query template which contains special token as place holder. The special token makes a query invalid to parse. This map will be applied to annotate those special token with types to let parser understand how to parse them into proper structure with type information.

` map<string, .google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.TokenType> special_token_map = 6; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBteqOptions()
    
    
    public abstract BteqOptions getBteqOptions()

The BTEQ specific settings for the translation task.

`.google.cloud.bigquery.migration.v2alpha.BteqOptions bteq_options = 11;`

**Returns**  
---  
**Type** | **Description**  
`[BteqOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.BteqOptions)` | The bteqOptions.  
  
### getBteqOptionsOrBuilder()
    
    
    public abstract BteqOptionsOrBuilder getBteqOptionsOrBuilder()

The BTEQ specific settings for the translation task.

`.google.cloud.bigquery.migration.v2alpha.BteqOptions bteq_options = 11;`

**Returns**  
---  
**Type** | **Description**  
`[BteqOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.BteqOptionsOrBuilder)` |   
  
### getFileEncoding()
    
    
    public abstract TranslationTaskDetails.FileEncoding getFileEncoding()

The file encoding type.

` .google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.FileEncoding file_encoding = 4; `

**Returns**  
---  
**Type** | **Description**  
`[TranslationTaskDetails.FileEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.FileEncoding)` | The fileEncoding.  
  
### getFileEncodingValue()
    
    
    public abstract int getFileEncodingValue()

The file encoding type.

` .google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.FileEncoding file_encoding = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for fileEncoding.  
  
### getFilePaths(int index)
    
    
    public abstract TranslationFileMapping getFilePaths(int index)

Cloud Storage files to be processed for translation.

`repeated .google.cloud.bigquery.migration.v2alpha.TranslationFileMapping file_paths = 12; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TranslationFileMapping](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TranslationFileMapping)` |   
  
### getFilePathsCount()
    
    
    public abstract int getFilePathsCount()

Cloud Storage files to be processed for translation.

`repeated .google.cloud.bigquery.migration.v2alpha.TranslationFileMapping file_paths = 12; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFilePathsList()
    
    
    public abstract List<TranslationFileMapping> getFilePathsList()

Cloud Storage files to be processed for translation.

`repeated .google.cloud.bigquery.migration.v2alpha.TranslationFileMapping file_paths = 12; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TranslationFileMapping](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TranslationFileMapping)>` |   
  
### getFilePathsOrBuilder(int index)
    
    
    public abstract TranslationFileMappingOrBuilder getFilePathsOrBuilder(int index)

Cloud Storage files to be processed for translation.

`repeated .google.cloud.bigquery.migration.v2alpha.TranslationFileMapping file_paths = 12; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TranslationFileMappingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TranslationFileMappingOrBuilder)` |   
  
### getFilePathsOrBuilderList()
    
    
    public abstract List<? extends TranslationFileMappingOrBuilder> getFilePathsOrBuilderList()

Cloud Storage files to be processed for translation.

`repeated .google.cloud.bigquery.migration.v2alpha.TranslationFileMapping file_paths = 12; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.bigquery.migration.v2alpha.TranslationFileMappingOrBuilder>` |   
  
### getFilter()
    
    
    public abstract Filter getFilter()

The filter applied to translation details.

`.google.cloud.bigquery.migration.v2alpha.Filter filter = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Filter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.Filter)` | The filter.  
  
### getFilterOrBuilder()
    
    
    public abstract FilterOrBuilder getFilterOrBuilder()

The filter applied to translation details.

`.google.cloud.bigquery.migration.v2alpha.Filter filter = 7;`

**Returns**  
---  
**Type** | **Description**  
`[FilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.FilterOrBuilder)` |   
  
### getIdentifierSettings()
    
    
    public abstract IdentifierSettings getIdentifierSettings()

The settings for SQL identifiers.

`.google.cloud.bigquery.migration.v2alpha.IdentifierSettings identifier_settings = 5; `

**Returns**  
---  
**Type** | **Description**  
`[IdentifierSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.IdentifierSettings)` | The identifierSettings.  
  
### getIdentifierSettingsOrBuilder()
    
    
    public abstract IdentifierSettingsOrBuilder getIdentifierSettingsOrBuilder()

The settings for SQL identifiers.

`.google.cloud.bigquery.migration.v2alpha.IdentifierSettings identifier_settings = 5; `

**Returns**  
---  
**Type** | **Description**  
`[IdentifierSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.IdentifierSettingsOrBuilder)` |   
  
### getInputPath()
    
    
    public abstract String getInputPath()

The Cloud Storage path for translation input files.

`string input_path = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The inputPath.  
  
### getInputPathBytes()
    
    
    public abstract ByteString getInputPathBytes()

The Cloud Storage path for translation input files.

`string input_path = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for inputPath.  
  
### getLanguageOptionsCase()
    
    
    public abstract TranslationTaskDetails.LanguageOptionsCase getLanguageOptionsCase()

**Returns**  
---  
**Type** | **Description**  
`[TranslationTaskDetails.LanguageOptionsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.LanguageOptionsCase)` |   
  
### getOutputPath()
    
    
    public abstract String getOutputPath()

The Cloud Storage path for translation output files.

`string output_path = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The outputPath.  
  
### getOutputPathBytes()
    
    
    public abstract ByteString getOutputPathBytes()

The Cloud Storage path for translation output files.

`string output_path = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for outputPath.  
  
### getSchemaPath()
    
    
    public abstract String getSchemaPath()

The Cloud Storage path to DDL files as table schema to assist semantic translation.

`string schema_path = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The schemaPath.  
  
### getSchemaPathBytes()
    
    
    public abstract ByteString getSchemaPathBytes()

The Cloud Storage path to DDL files as table schema to assist semantic translation.

`string schema_path = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for schemaPath.  
  
### getSpecialTokenMap() (deprecated)
    
    
    public abstract Map<String,TranslationTaskDetails.TokenType> getSpecialTokenMap()

Use [#getSpecialTokenMapMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TranslationTaskDetailsOrBuilder#com_google_cloud_bigquery_migration_v2alpha_TranslationTaskDetailsOrBuilder_getSpecialTokenMapMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[TokenType](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.TokenType)>` |   
  
### getSpecialTokenMapCount()
    
    
    public abstract int getSpecialTokenMapCount()

The map capturing special tokens to be replaced during translation. The key is special token in string. The value is the token data type. This is used to translate SQL query template which contains special token as place holder. The special token makes a query invalid to parse. This map will be applied to annotate those special token with types to let parser understand how to parse them into proper structure with type information.

` map<string, .google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.TokenType> special_token_map = 6; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSpecialTokenMapMap()
    
    
    public abstract Map<String,TranslationTaskDetails.TokenType> getSpecialTokenMapMap()

The map capturing special tokens to be replaced during translation. The key is special token in string. The value is the token data type. This is used to translate SQL query template which contains special token as place holder. The special token makes a query invalid to parse. This map will be applied to annotate those special token with types to let parser understand how to parse them into proper structure with type information.

` map<string, .google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.TokenType> special_token_map = 6; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[TokenType](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.TokenType)>` |   
  
### getSpecialTokenMapOrDefault(String key, TranslationTaskDetails.TokenType defaultValue)
    
    
    public abstract TranslationTaskDetails.TokenType getSpecialTokenMapOrDefault(String key, TranslationTaskDetails.TokenType defaultValue)

The map capturing special tokens to be replaced during translation. The key is special token in string. The value is the token data type. This is used to translate SQL query template which contains special token as place holder. The special token makes a query invalid to parse. This map will be applied to annotate those special token with types to let parser understand how to parse them into proper structure with type information.

` map<string, .google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.TokenType> special_token_map = 6; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[TranslationTaskDetails.TokenType](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.TokenType)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TranslationTaskDetails.TokenType](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.TokenType)` |   
  
### getSpecialTokenMapOrThrow(String key)
    
    
    public abstract TranslationTaskDetails.TokenType getSpecialTokenMapOrThrow(String key)

The map capturing special tokens to be replaced during translation. The key is special token in string. The value is the token data type. This is used to translate SQL query template which contains special token as place holder. The special token makes a query invalid to parse. This map will be applied to annotate those special token with types to let parser understand how to parse them into proper structure with type information.

` map<string, .google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.TokenType> special_token_map = 6; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TranslationTaskDetails.TokenType](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.TokenType)` |   
  
### getSpecialTokenMapValue() (deprecated)
    
    
    public abstract Map<String,Integer> getSpecialTokenMapValue()

Use [#getSpecialTokenMapValueMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TranslationTaskDetailsOrBuilder#com_google_cloud_bigquery_migration_v2alpha_TranslationTaskDetailsOrBuilder_getSpecialTokenMapValueMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),java.lang.Integer>` |   
  
### getSpecialTokenMapValueMap()
    
    
    public abstract Map<String,Integer> getSpecialTokenMapValueMap()

The map capturing special tokens to be replaced during translation. The key is special token in string. The value is the token data type. This is used to translate SQL query template which contains special token as place holder. The special token makes a query invalid to parse. This map will be applied to annotate those special token with types to let parser understand how to parse them into proper structure with type information.

` map<string, .google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.TokenType> special_token_map = 6; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),java.lang.Integer>` |   
  
### getSpecialTokenMapValueOrDefault(String key, int defaultValue)
    
    
    public abstract int getSpecialTokenMapValueOrDefault(String key, int defaultValue)

The map capturing special tokens to be replaced during translation. The key is special token in string. The value is the token data type. This is used to translate SQL query template which contains special token as place holder. The special token makes a query invalid to parse. This map will be applied to annotate those special token with types to let parser understand how to parse them into proper structure with type information.

` map<string, .google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.TokenType> special_token_map = 6; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSpecialTokenMapValueOrThrow(String key)
    
    
    public abstract int getSpecialTokenMapValueOrThrow(String key)

The map capturing special tokens to be replaced during translation. The key is special token in string. The value is the token data type. This is used to translate SQL query template which contains special token as place holder. The special token makes a query invalid to parse. This map will be applied to annotate those special token with types to let parser understand how to parse them into proper structure with type information.

` map<string, .google.cloud.bigquery.migration.v2alpha.TranslationTaskDetails.TokenType> special_token_map = 6; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTeradataOptions()
    
    
    public abstract TeradataOptions getTeradataOptions()

The Teradata SQL specific settings for the translation task.

`.google.cloud.bigquery.migration.v2alpha.TeradataOptions teradata_options = 10;`

**Returns**  
---  
**Type** | **Description**  
`[TeradataOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TeradataOptions)` | The teradataOptions.  
  
### getTeradataOptionsOrBuilder()
    
    
    public abstract TeradataOptionsOrBuilder getTeradataOptionsOrBuilder()

The Teradata SQL specific settings for the translation task.

`.google.cloud.bigquery.migration.v2alpha.TeradataOptions teradata_options = 10;`

**Returns**  
---  
**Type** | **Description**  
`[TeradataOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerymigration/latest/com.google.cloud.bigquery.migration.v2alpha.TeradataOptionsOrBuilder)` |   
  
### getTranslationExceptionTable()
    
    
    public abstract String getTranslationExceptionTable()

Specifies the exact name of the bigquery table ("dataset.table") to be used for surfacing raw translation errors. If the table does not exist, we will create it. If it already exists and the schema is the same, we will re-use. If the table exists and the schema is different, we will throw an error.

`string translation_exception_table = 13;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The translationExceptionTable.  
  
### getTranslationExceptionTableBytes()
    
    
    public abstract ByteString getTranslationExceptionTableBytes()

Specifies the exact name of the bigquery table ("dataset.table") to be used for surfacing raw translation errors. If the table does not exist, we will create it. If it already exists and the schema is the same, we will re-use. If the table exists and the schema is different, we will throw an error.

`string translation_exception_table = 13;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for translationExceptionTable.  
  
### hasBteqOptions()
    
    
    public abstract boolean hasBteqOptions()

The BTEQ specific settings for the translation task.

`.google.cloud.bigquery.migration.v2alpha.BteqOptions bteq_options = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bteqOptions field is set.  
  
### hasFilter()
    
    
    public abstract boolean hasFilter()

The filter applied to translation details.

`.google.cloud.bigquery.migration.v2alpha.Filter filter = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the filter field is set.  
  
### hasIdentifierSettings()
    
    
    public abstract boolean hasIdentifierSettings()

The settings for SQL identifiers.

`.google.cloud.bigquery.migration.v2alpha.IdentifierSettings identifier_settings = 5; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the identifierSettings field is set.  
  
### hasTeradataOptions()
    
    
    public abstract boolean hasTeradataOptions()

The Teradata SQL specific settings for the translation task.

`.google.cloud.bigquery.migration.v2alpha.TeradataOptions teradata_options = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the teradataOptions field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

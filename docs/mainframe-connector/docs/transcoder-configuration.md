---
url: https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration/
title: Transcoder configuration \u00a0|\u00a0 Mainframe Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:35:02.138765+00:00
---

# Transcoder configuration  |  Mainframe Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Reference ](https://docs.cloud.google.com/mainframe-connector/docs/reference)



Send feedback 

#  Transcoder configuration Stay organized with collections  Save and categorize content based on your preferences. 

You can configure the Mainframe Connector transcoder by adding the required configuration in a JSON file. This file is referred to as the transcoder configuration file. You must define the configuration as specified in section Configuration. The `qsam encode` and `qsam decode` commands use the transcoder configuration file to perform data transcoding.

This page describes the various ways in which you can configure the Mainframe Connector transcoder.

## Configuration

The `Configuration` object is the root of the transcoder configuration. It contains all the configuration options for the transcoder.

JSON representation  
---  
      
    
    {
        "defaults": object (DefaultsSection),
        "field_overrides": object (FieldOverride),
        "field_suffixes": object (FieldSuffix),
        "header_records_to_skip": long,
        "record_filter_condition": string,
        "schema_validation_mode": enum (SchemaValidationMode),
        "transformations": object (Transformation)  
    }
      
  
Fields  
---  
`defaults` |  `object (`DefaultsSection`)` Specify default field modifiers for Cobol archetypes.  
`field_overrides` |  `object (`FieldOverride`)` Specify field overrides.  
`field_suffixes` |  `object (`FieldSuffix`)` Specify field suffixes.  
`header_records_to_skip` |  `long` Specify the number of first records to skip.  
`record_filter_condition` |  `string` Specify a filter condition for records. The filter is based on a subset of Common Expression Language (CEL) and supports the following:

  * **Field Access:** Fields can be referenced by name. For nested fields, use dot notation (e.g., `PARENT.CHILD`).
  * **Comparison operators:** ``==`, `!=`, `<`, `<=`, `>`, `>=`.`
  * **Logical operators:** ``&&` (AND), `||` (OR), `!` (NOT).`
  * **List containment:** ``in`` (checks if a value is present in a list).
  * **Arithmetic operators:** ``+`, `-`, `*`, `/`, `%`.`
  * **String and list functions:**
    * `size()`: Returns the length of a string or list.
    * `contains(substring)`: Checks if a string contains a specified substring.
    * `startsWith(prefix)`: Checks if a string starts with a specified prefix.
    * `endsWith(suffix)`: Checks if a string ends with a specified suffix.
  * **Date and Timestamp constants:**
    * `date(string)`: Parses a date in ISO format (YYYY-MM-DD). E.g., `date('2025-01-12')`.
    * `date(string, format)`: Parses a date using a custom format. E.g., `date('12/01/2025', 'dd/MM/yyyy')`.
    * `timestamp(string)`: Parses a timestamp in ISO format. E.g., `timestamp('1999-05-03T02:34:00Z')`.

Comparisons and operations must be performed between variables or constants of the same or compatible data types (e.g., comparing floating-point numbers or using date/timestamp constants for date/timestamp fields). Example: `"record_filter_condition": "(ACCOUNT-GRP.DATE > date('2025-01-12') ) && ((SCORE_A + SCORE_B) > 134) && FLD-STR.startsWith('HE')"`  
`schema_validation_mode` |  `enum (`SchemaValidationMode`)` Specify the schema validation mode.  
`transformations` |  `object (`Transformation`)` Specify field transformations.  
  
## DefaultsSection

The `DefaultsSection` object can be used to specify default modifications by cobol types. These are applied **before** any suffix or override modifications.

JSON representation  
---  
      
    
    {
        "alpha_numeric_display": object (FieldModifier),
        "binary": object (FieldModifier),
        "dbcs": object (FieldModifier),
        "hexadecimal_floating_point": object (FieldModifier),
        "national": object (FieldModifier),
        "numeric_display": object (FieldModifier),
        "packed_decimal": object (FieldModifier),
        "utf8": object (FieldModifier)  
    }
      
  
Fields  
---  
`alpha_numeric_display` |  `object (`FieldModifier`)` Specify defaults for alphanumeric (PIC X) fields.  
`binary` |  `object (`FieldModifier`)` Specify defaults for binary number (COMP) fields.  
`dbcs` |  `object (`FieldModifier`)` Default for dbcs (DISPLAY-1) fields.  
`hexadecimal_floating_point` |  `object (`FieldModifier`)` Default for hexadecimal floating point (COMP-1, COMP-2) fields.  
`national` |  `object (`FieldModifier`)` Specify defaults for national (PIC N) fields.  
`numeric_display` |  `object (`FieldModifier`)` Specify defaults for numeric display (zoned decimal) fields.  
`packed_decimal` |  `object (`FieldModifier`)` Specify defaults for packed decimal (COMP-3) fields.  
`utf8` |  `object (`FieldModifier`)` Specify defaults for UTF-8 (PIC U) fields.  
  
### FieldModifier

A field modifier lets you modify the encoding or decoding of a specific field. Note that not all modifiers can be applied to all fields. See the documentation for the specific modifiers for more information.

JSON representation  
---  
      
    
    {
        "binary": object (Binary),
        "bytes": object (Bytes),
        "chain": object (ModifierChain),
        "decode_as_null": object (DecodeAsNull),
        "encode_null_as": object (EncodeNullAs),
        "filler": object (Filler),
        "format_date": object (FormatDate),
        "format_timestamp": object (FormatTimestamp),
        "hfp": object (HFP),
        "null_if": object (NullIf),
        "null_if_empty": object (NullIfEmpty),
        "null_if_invalid": object (NullIfInvalid),
        "packed_decimal": object (PackedDecimal),
        "string": object (String),
        "varlen": object (VarLen),
        "zoned_decimal": object (ZonedDecimal)  
    }
      
  
Fields  
---  
`binary` |  `object (`Binary`)` Overrides default configuration for binary numeric fields.  
`bytes` |  `object (`Bytes`)` Treats the field as a raw sequence of bytes, ignoring prior type information.  
`chain` |  `object (`ModifierChain`)` Chains multiple modifiers to be applied sequentially.  
`decode_as_null` |  `object (`DecodeAsNull`)` Defines how null values must be decoded.  
`encode_null_as` |  `object (`EncodeNullAs`)` Defines how null values must be encoded.  
`filler` |  `object (`Filler`)` Excludes the field from processing and output.  
`format_date` |  `object (`FormatDate`)` Formats a string field as a date.  
`format_timestamp` |  `object (`FormatTimestamp`)` Formats a string field as a timestamp.  
`hfp` |  `object (`HFP`)` Interprets the field as a Hexadecimal Floating-Point (HFP) number.  
`null_if` |  `object (`NullIf`)` Conditionally sets the field to null based on the value of another field.  
`null_if_empty` |  `object (`NullIfEmpty`)` Sets the field to null if its content is considered empty.  
`null_if_invalid` |  `object (`NullIfInvalid`)` Sets the field to null if a transcoding error occurs, preventing record spillover.  
`packed_decimal` |  `object (`PackedDecimal`)` Overrides default configuration for packed decimal fields.  
`string` |  `object (`String`)` Overrides default configuration for string fields.  
`varlen` |  `object (`VarLen`)` Set the record as a variable length field.  
`zoned_decimal` |  `object (`ZonedDecimal`)` Overrides default configuration for zoned decimal fields.  
  
#### Binary

Ignore any previous modifiers and treat this field as a binary number.

JSON representation  
---  
      
    
    {
        "signedness": enum (BinarySignedness)  
    }
      
  
Fields  
---  
`signedness` |  `enum (`BinarySignedness`)` The signedness of the number.  
  
#### Bytes

Treats the field as a raw sequence of bytes. This modifier overrides any prior type information, causing the field's raw byte data to be preserved as-is without specific character encoding or numeric interpretation. You can be apply this modifier to any field regardless of its original type or size.

Provide an empty JSON object as follows:

JSON representation  
---  
      
    
    {  
    }
      
  
#### DecodeAsNull

Defines how null values are interpreted during the decoding process. As COBOL doesn't natively support nulls, this parameter specifies what values must be treated as null.

JSON representation  
---  
      
    
    {
        "hex_bytes": string,
        "values": string  
    }
      
  
Fields  
---  
`hex_bytes` |  `string` A list of hexadecimal representations of a single byte. When a field contains repetitions any of these bytes, it is treated as null. For example, using `FF` for all highs and `00` for all lows (empty).  
`values` |  `string` A list of string representations. After the initial decoding of the field to its string form, if the field's content matches any of these values, it will be treated as null.  
  
#### EncodeNullAs

Defines how null values are represented during the encoding process.

JSON representation  
---  
      
    
    {
        "hex_byte": string,
        "value": string  
    }
      
  
Fields  
---  
`hex_byte` |  `string` Encode this specific byte sequence (represented as a hexadecimal string) when the source value is null. For example, `FF` for a two-byte field to high-values. You can apply this to any field with a known size. The bytes are repeated to match the underlying field's size.  
`value` |  `string` Encode this specific value when the source value is null. Verify that the string is valid for the field's type.  
  
#### Filler

Specifies that a field will be ignored during processing. The field won't be decoded from the input or encoded to the output and will be excluded from the resulting schema and data table during decoding. You can apply this modifier to any field that has a static known size.

Provide an empty JSON object as follows:

JSON representation  
---  
      
    
    {  
    }
      
  
#### FormatDate

Format a string or numeric field to a date using one of the supported formats. You can only apply this modifier to sized fields. For numeric fields, they are dynamically converted to their string representation (excluding any sign markers) before formatting. It is assumed that date values are positive; negative numeric dates are not supported and will fail to parse. During the decoding process, the formats are tested in order until one of the formats matches the string. During the encoding process, the first format is used and the rest are ignored.

JSON representation  
---  
      
    
    {
        "formats": object (DateTimeFormat)  
    }
      
  
Fields  
---  
`formats` |  `object (`DateTimeFormat`)` List of date formats.  
  
#### DateTimeFormat

Size and pattern to use when converting the field to a date.

JSON representation  
---  
      
    
    {
        "pattern": string,
        "size": int  
    }
      
  
Fields  
---  
`pattern` |  `string` Specify the date formatter pattern. For more information on valid formatter patterns, see [Class DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html).  
`size` |  `int` Specify the size of the field this pattern applies to.  
  
#### FormatTimestamp

Format a string to a timestamp using one of the provided formats. This can only be applied to sized fields. During decode, the formats are tested in order until one of the formats matches the string. During encode, the first format will be used and the rest will be ignored.

JSON representation  
---  
      
    
    {
        "formats": object (DateTimeFormat)  
    }
      
  
Fields  
---  
`formats` |  `object (`DateTimeFormat`)` List of timestamp formats.  
  
#### HFP

Set this field as Hexadecimal Floating-Point.

Provide an empty JSON object as follows:

JSON representation  
---  
      
    
    {  
    }
      
  
#### ModifierChain

Specify a modifier chain to apply multiple modifiers in series. The modifiers are applied in the order they are specified.

JSON representation  
---  
      
    
    {
        "modifiers": object (FieldModifier)  
    }
      
  
Fields  
---  
`modifiers` |  `object (`FieldModifier`)` Specify the list of modifiers to apply.  
  
#### NullIf

Set a field to null if a condition is satisfied. You must specify either `null_value` or `non_null_value` or both. 

To create a null-indicator field, you can use a `FieldSuffix` with a `null_if` field modifier, and set `is_inverse` to `true` as shown in the following examples:

**Example** : Null-indicator

To create a null-indicator field, we can use the `null_if` field modifier like so. 
    
    
     {
      "field_suffixes": [
       {
         "suffix": "NID",
         "is_inverse": true,
         "modifier": {
         "null_if": {
           "null_value": "?",
           "target_field": "$self"
         }
        }
       }
      ]
     }
    

This allows for all fields with the suffix `NID` to effectively be null indicators as shown in the following copybook snippet: 
    
    
     01 REC.
       02 FIELD     PIC X(10).
       02 FIELD-NID PIC X(1).
    

**Example** : Binary null-indicator

To create a `binary` null-indicator field, we can use the `binary` and `null_if` field modifiers like so. 
    
    
     {
      "field_suffixes": [
       {
         "suffix": "NID",
         "modifier": {
           "binary": {}
         }
       },
       {
         "suffix": "NID",
         "is_inverse": true,
         "modifier": {
         "null_if": {
           "null_value": "15",
           "target_field": "$self"
         }
        }
       }
      ]
     }
    

This allows for all fields with the suffix `NID` to effectively be `binary` null indicators using the same copybook from the earlier example. 

**Example** : Bytes null-indicator

To create a `bytes` null-indicator field, we can use the `bytes` and `null_if` field modifiers like so. The values for null and not-null are expressed as `HEX`. 
    
    
     {
      "field_suffixes": [
       {
         "suffix": "NID",
         "modifier": {
           "bytes": {}
         }
       },
       {
         "suffix": "NID",
         "is_inverse": true,
         "modifier": {
         "null_if": {
           "null_value": "FF",
           "target_field": "$self"
         }
        }
       }
      ]
     }
    

This allows for all fields with the suffix `NID` to effectively be a `bytes` null indicator using the same copybook from the earlier example. JSON representation  
---  
      
    
    {
        "non_null_value": string,
        "non_null_values": string,
        "null_value": string,
        "null_values": string,
        "target_field": string  
    }
      
  
Fields  
---  
`non_null_value` |  `string` When specified, if `target_field` is not equal to this value, the field is not decoded or encoded, and the value is set to null.  
`non_null_values` |  `string` When specified, if `target_field` is not equal to any of these values, the field is not decoded or encoded and the value is set to null.  
`null_value` |  `string` When specified, if `target_field` is equal to this value, the field is not decoded or encoded, and the value is set to null.  
`null_values` |  `string` When specified, if `target_field` is equal to any of these values, the field is not decoded or encoded and the value is set to null.  
`target_field` |  `string` Specify the field whose value you want to check. The field must be in scope. To access nested fields, you can use dot notation (e.g., "GROUP.FIELD").  
  
#### NullIfEmpty

Field should be set to null if all the bytes in that field are 0.

Provide an empty JSON object as follows:

JSON representation  
---  
      
    
    {  
    }
      
  
#### NullIfInvalid

Treat the value as null if transcoding fails. You can only apply this modifier to sized fields. By default, when a field fails to decode, the whole record is moved to the spillover (error) dataset and excluded from the output, while the rest of the load completes with the valid records. When you set the `null_if_invalid` modifier, Mainframe Connector keeps the invalid record and sets this field to null. Use it only when you want to retain such rows with a null value—not just to make a load succeed, since the default already skips the bad records. The error is ignored and is not logged in the spillover dataset. During the decoding process, the value of this field will be null for this record. During the encoding process, if the data can't be written, the entire field will be filled with null bytes.

Provide an empty JSON object as follows:

JSON representation  
---  
      
    
    {  
    }
      
  
#### PackedDecimal

Set this field to a PackedDecimal.

JSON representation  
---  
      
    
    {
        "logical_type": enum (DecimalLogicalType),
        "negative_sign_nibble": enum (PackedDecimalNegativeNibble)  
    }
      
  
Fields  
---  
`logical_type` |  `enum (`DecimalLogicalType`)` Override the logical type. By default, Mainframe Connector uses the optimal logical type based on the precision and scale.  
`negative_sign_nibble` |  `enum (`PackedDecimalNegativeNibble`)` Specifies the nibble to use for negative signs. While both x'B' and x'D' are valid negative signs, some mainframe systems or applications may have a convention that requires one over the other.  
  
#### String

Sets the various options related to string decoding and encoding. Can only be applied on a string field.

JSON representation  
---  
      
    
    {
        "encoding": string,
        "pad_char": string,
        "trim_suffix": boolean  
    }
      
  
Fields  
---  
`encoding` |  `string` The encoding with which the field is encoded.  
`pad_char` |  `string` When set padding export strings with `pad_char`. If set, the length of `pad_char` must be 1. pad_char affects only encoding, decoding ignores pad_char.  
`trim_suffix` |  `boolean` When set to true, any whitespace at the end of the string will be trimmed. trim_suffix affects only decoding, encoding ignores trim_suffix. Note that strings that consist only of whitespaces will become empty strings.  
  
#### VarLen

Represents a variable-length field. 

A variable-length field contains three parts:

  1. A group item that contains two subfields.
  2. A field within the group item that contains the length of the transaction data.
  3. A field within the group item that contains the data.



The name of the variable-length field will be the group name.

Provide an empty JSON object as follows:

JSON representation  
---  
      
    
    {  
    }
      
  
#### ZonedDecimal

Sets various options related to the encoding and decoding of zoned decimals. You can only be apply this modifier on a decimal field.

JSON representation  
---  
      
    
    {
        "encoding": enum (ZonedDecimalEncoding),
        "logical_type": enum (DecimalLogicalType)  
    }
      
  
Fields  
---  
`encoding` |  `enum (`ZonedDecimalEncoding`)` The encoding with which the field is encoded.  
`logical_type` |  `enum (`DecimalLogicalType`)` Specify the logical type to use when decoding or encoding the field.  
  
## FieldOverride

Override or modify the decode and encode chain for the specified field.

JSON representation  
---  
      
    
    {
        "field": string,
        "modifier": object (FieldModifier)  
    }
      
  
Fields  
---  
`field` |  `string` Specify the name of the field to apply the modifier to.  
`modifier` |  `object (`FieldModifier`)` Specify the modifier to apply to matching field.  
  
## FieldSuffix

Field suffixes apply to all fields that have a suffix. 

Fields are matched if they end with a hyphen (`-`) or underscore (`_`) followed by the suffix.

Suffixes are case-insensitive.

The `FieldSuffix` modifier is applied _after_ the `FieldOverride` modifier.

For example, the modifier defined for the suffix `NID` will be applied to the field named `FLD-NID` but not for the field `FUNID`.

JSON representation  
---  
      
    
    {
        "is_inverse": boolean,
        "modifier": object (FieldModifier),
        "suffix": string  
    }
      
  
Fields  
---  
`is_inverse` |  `boolean` Specify whether the modifier is an **inverse** field modifier or not. An inverse field modifier applies the modifier on another field that has the same name as the field with the modifier without the modifier. For example, if both `FLD-NID` and `FLD` fields exist in the same record, the modifier will be applied to `FLD`. When using an inverse field modifier, the special identifier `$self` can be used whenever a field name can traditionally be used to refer to the field with the suffix. For example, to create a null-indicator field, you can use the `null_if` field modifier with `is_inverse` set to `true`. Refer to `NullIf` for more information.  
`modifier` |  `object (`FieldModifier`)` Specify the modifier to apply to matching fields.  
`suffix` |  `string` The field with this suffix will have the modifier applied to it.  
  
## Transformation

View transformations are used to modify the relationship between the table and the QSAM file. Transformations are always phrased from the point of view of the data. The concept is similar to view tables in BigQuery.

JSON representation  
---  
      
    
    {
        "exclude": object (Exclude),
        "move": object (Move),
        "rename": object (Rename),
        "split": object (Split),
        "target_table": string,
        "unnest": object (Unnest)  
    }
      
  
Fields  
---  
`exclude` |  `object (`Exclude`)`  
`move` |  `object (`Move`)`  
`rename` |  `object (`Rename`)`  
`split` |  `object (`Split`)`  
`target_table` |  `string` Optional. Specify the target table (view) name to apply the transformation to. By default, transformations apply to the main table (`_main`) or globally where applicable. If you have split views (created by a `split` transformation), you can target a specific split table by name. Note: Split transformations themselves cannot be targeted and will error if `target_table` is set.  
`unnest` |  `object (`Unnest`)`  
  
### Exclude

Exclude a field from the resulting table, but still undergo decoding or encoding. This is useful when the field doesn't need to be transferred to the table, but is required for transcoding. For example, null indicator or length fields can be omitted from the table. 

To bypass transcoding altogether, apply the filler modifier.

JSON representation  
---  
      
    
    {
        "field": string  
    }
      
  
Fields  
---  
`field` |  `string` Specify the field to exclude.  
  
### Move

Move a field in the record.

JSON representation  
---  
      
    
    {
        "field": string,
        "offset": int  
    }
      
  
Fields  
---  
`field` |  `string` Specify the field to move.  
`offset` |  `int` Specify the number of places, forward or backwards, the field needs to be moved to.  
  
### Rename

Rename one or more fields based on a regular expression match. 

For example, to replace all hyphens with underscores, use the following JSON format: `{"find": "\\-", "replace":"_"}`. 

JSON representation  
---  
      
    
    {
        "find": string,
        "replace": string  
    }
      
  
Fields  
---  
`find` |  `string` Specifies a Java regular expression [pattern](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html) to identify the field(s) to rename. The pattern is matched against the full field name. If the pattern matches any part of the field name, the field is considered a match. Examples:

  * `"\\-"` (matches any field containing a hyphen)
  * `"^field_name$"` (matches fields with the exact name `field_name`)
  * `"^field_(.*)$"` (matches any fields starting with `field_` and captures the rest)
  * `"part_of_name"` (matches any field containing `part_of_name`)

  
`replace` |  `string` Specifies the new name for the matched field(s). Capture groups from the `find` regular expression can be used in the `replace` string using backreferences like `$1`, `$2`. This allows for more complex transformations based on parts of the original field name. Examples:

  * `"new_field_name"` (replaces the field with a fixed name)
  * `"new_$1"` (uses the first capture group from `find`)
  * `"${1}_new"` (alternative syntax for capture groups)
  * `"prefix_$1_suffix"` (uses a capture group and adds prefixes/suffixes)

  
  
### Split

JSON representation  
---  
      
    
    {
        "field": string,
        "foreign_key": string,
        "primary_key": string  
    }
      
  
Fields  
---  
`field` |  `string` Specify the field you want to split.  
`foreign_key` |  `string` Specify the name for the field that will be added to the new schema where the primary-key value will be stored. If not specified, the primary-key name is used.  
`primary_key` |  `string` Specify the field name that will be used as a primary key.  
  
### Unnest

Unnest the field.

JSON representation  
---  
      
    
    {
        "field": string,
        "format": string  
    }
      
  
Fields  
---  
`field` |  `string` Specify the field to unnest  
`format` |  `string` Specify the new field format. The `${parent}` will be released with the name of the field being unnested. For unnested structs, `${field}` is replaced with the name of the structs field. For unnested arrays and lists, `${index}` is replaced with the indexes of the array.  
  
## Enums

### BinarySignedness

Enums  
---  
`SIGNED` | The binary number is signed.  
`UNSIGNED` | The binary number is unsigned.  
`UNSPECIFIED` | Try and deduce the signedness from the exiting chain.  
  
### DecimalLogicalType

Logical type to use for a decimal field.

Enums  
---  
`AUTO` | Use the most optimal type based on the scale and precision.  
`BIG_DECIMAL` | Store the value as an unbounded decimal value. This is the slowest option but supports any decimal of any precision at any scale.  
`BIG_INTEGER` | Store the value as an unbounded integer value. This is the slowest option but supports any integer of any precision.  
`DECIMAL64` | Use 64-bits to store the value. This modifier only works for numbers whose precision is less than or equal to 18.  
`LONG` | Use 64-bits to store the value. This modifier only works for numbers whose precision is less than or equal to 18, and the scale is 0.  
  
### PackedDecimalNegativeNibble

Enums  
---  
`NIBBLE_B` | The default is to use x'B'.  
`NIBBLE_D` | Use x'D' for the negative sign nibble.  
  
### SchemaValidationMode

Specify the schema validation mode to use during the copybook compilation. This mode verifies compatibility with a specific target data format.

Enums  
---  
`BIG_QUERY` | Schema validation mode for BigQuery compatibility. This mode extends the default validation to verify that the copybook's schema is compatible with BigQuery's data types.  
`DEFAULT` | Default schema validation mode. This mode verifies that unique field names are in the copybook.  
`MYSQL` | Schema validation mode for MySQL compatibility. This mode extends the default validation to verify that the copybook's schema is compatible with MySQL data types.  
`POSTGRES` | Schema validation mode for PostgreSQL compatibility. This mode extends the default validation to verify that the copybook's schema is compatible with PostgreSQL data types.  
  
### ZonedDecimalEncoding

Specify the encoding to use when decoding or encoding a zoned decimal field.

Enums  
---  
`ASCII` | Use `ASCII` encoding.  
`EBCDIC` | Use `EBCDIC` encoding.  
`UNSPECIFIED` | Keep the encoding that is specified in the modifier chain. If no modifier is specified, `EBCDIC` is used.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

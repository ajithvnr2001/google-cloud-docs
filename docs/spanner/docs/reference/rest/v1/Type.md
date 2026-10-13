---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type/
title: Type \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:22.938608+00:00
---

# Type  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Type Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TypeCode
  * TypeAnnotationCode



`Type` indicates the type of a Cloud Spanner value, as might be stored in a table cell or returned from an SQL query.

JSON representation  
---  
      
    
    {
      "code": enum ([TypeCode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeCode)),
      "arrayElementType": {
        object ([Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type))
      },
      "structType": {
        object ([StructType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/StructType))
      },
      "typeAnnotation": enum ([TypeAnnotationCode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeAnnotationCode)),
      "protoTypeFqn": string
    }  
  
Fields  
---  
`code` |  `enum (`[TypeCode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeCode)`)` Required. The `[TypeCode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeCode)` for this type.  
`arrayElementType` |  `object (`[Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type)`)` If `[code](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#FIELDS.code)` == `[ARRAY](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeCode.ENUM_VALUES.ARRAY)`, then `arrayElementType` is the type of the array elements.  
`structType` |  `object (`[StructType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/StructType)`)` If `[code](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#FIELDS.code)` == `[STRUCT](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeCode.ENUM_VALUES.STRUCT)`, then `structType` provides type information for the struct's fields.  
`typeAnnotation` |  `enum (`[TypeAnnotationCode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeAnnotationCode)`)` The `[TypeAnnotationCode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeAnnotationCode)` that disambiguates SQL type that Spanner will use to represent values of this type during query processing. This is necessary for some type codes because a single `[TypeCode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeCode)` can be mapped to different SQL types depending on the SQL dialect. `[typeAnnotation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#FIELDS.type_annotation)` typically is not needed to process the content of a value (it doesn't affect serialization) and clients can ignore it on the read path.  
`protoTypeFqn` |  `string` If `[code](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#FIELDS.code)` == `[PROTO](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeCode.ENUM_VALUES.PROTO)` or `[code](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#FIELDS.code)` == `[ENUM](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeCode.ENUM_VALUES.ENUM)`, then `protoTypeFqn` is the fully qualified name of the proto type representing the proto/enum definition.  
  
## TypeCode

`TypeCode` is used as part of `[Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type)` to indicate the type of a Cloud Spanner value.

Each legal value of a type can be encoded to or decoded from a JSON value, using the encodings described below. All Cloud Spanner values can be `null`, regardless of type; `null`s are always encoded as a JSON `null`.

Enums  
---  
`TYPE_CODE_UNSPECIFIED` | Not specified.  
`BOOL` | Encoded as JSON `true` or `false`.  
`INT64` | Encoded as `string`, in decimal format.  
`FLOAT64` | Encoded as `number`, or the strings `"NaN"`, `"Infinity"`, or `"-Infinity"`.  
`FLOAT32` | Encoded as `number`, or the strings `"NaN"`, `"Infinity"`, or `"-Infinity"`.  
`TIMESTAMP` | Encoded as `string` in RFC 3339 timestamp format. The time zone must be present, and must be `"Z"`.If the schema has the column option `allow_commit_timestamp=true`, the placeholder string `"spanner.commit_timestamp()"` can be used to instruct the system to insert the commit timestamp associated with the transaction commit.  
`DATE` | Encoded as `string` in RFC 3339 date format.  
`STRING` | Encoded as `string`.  
`BYTES` | Encoded as a base64-encoded `string`, as described in RFC 4648, section 4.  
`ARRAY` | Encoded as `list`, where the list elements are represented according to `[arrayElementType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#FIELDS.array_element_type)`.  
`STRUCT` | Encoded as `list`, where list element `i` is represented according to `[structType.fields[i]](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/StructType#FIELDS.fields)`.  
`NUMERIC` | Encoded as `string`, in decimal format or scientific notation format. Decimal format: `[+-]Digits[.[Digits]]` or `[+-][Digits].Digits`Scientific notation: `[+-]Digits[.[Digits]][ExponentIndicator[+-]Digits]` or `[+-][Digits].Digits[ExponentIndicator[+-]Digits]` (ExponentIndicator is `"e"` or `"E"`)  
`JSON` | Encoded as a JSON-formatted `string` as described in RFC 7159. The following rules are applied when parsing JSON input:

  * Whitespace characters are not preserved.
  * If a JSON object has duplicate keys, only the first key is preserved.
  * Members of a JSON object are not guaranteed to have their order preserved.
  * JSON array elements will have their order preserved.

  
`PROTO` | Encoded as a base64-encoded `string`, as described in RFC 4648, section 4.  
`ENUM` | Encoded as `string`, in decimal format.  
`UUID` | Encoded as `string`, in lower-case hexa-decimal format, as described in RFC 9562, section 4.  
  
## TypeAnnotationCode

`TypeAnnotationCode` is used as a part of `[Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type)` to disambiguate SQL types that should be used for a given Cloud Spanner value. Disambiguation is needed because the same Cloud Spanner type can be mapped to different SQL types depending on SQL dialect. TypeAnnotationCode doesn't affect the way value is serialized.

Enums  
---  
`TYPE_ANNOTATION_CODE_UNSPECIFIED` | Not specified.  
`PG_NUMERIC` | PostgreSQL compatible NUMERIC type. This annotation needs to be applied to `[Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type)` instances having `[NUMERIC](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeCode.ENUM_VALUES.NUMERIC)` type code to specify that values of this type should be treated as PostgreSQL NUMERIC values. Currently this annotation is always needed for `[NUMERIC](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeCode.ENUM_VALUES.NUMERIC)` when a client interacts with PostgreSQL-enabled Spanner databases.  
`PG_JSONB` | PostgreSQL compatible JSONB type. This annotation needs to be applied to `[Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type)` instances having `[JSON](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeCode.ENUM_VALUES.JSON)` type code to specify that values of this type should be treated as PostgreSQL JSONB values. Currently this annotation is always needed for `[JSON](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeCode.ENUM_VALUES.JSON)` when a client interacts with PostgreSQL-enabled Spanner databases.  
`PG_OID` | PostgreSQL compatible OID type. This annotation can be used by a client interacting with PostgreSQL-enabled Spanner database to specify that a value should be treated using the semantics of the OID type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-30 UTC."],[],[]] 

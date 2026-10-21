---
url: https://docs.cloud.google.com/mainframe-connector/docs/qsam-vsam-transcoding/
title: qsam and vsam commands reference \u00a0|\u00a0 Mainframe Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:42:19.413332+00:00
---

# qsam and vsam commands reference  |  Mainframe Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/qsam-vsam-transcoding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Reference ](https://docs.cloud.google.com/mainframe-connector/docs/reference)



Send feedback 

#  qsam and vsam commands reference Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Mainframe Connector transcodes Queued Sequential Access Method (QSAM) flat files to Google Cloud compatible formats, and the other way around using the `qsam` commands. Mainframe Connector also supports transcoding Virtual Storage Access Method (VSAM) files to Google Cloud compatible formats using the `vsam decode` command. The `qsam` and `vsam` commands perform the following transcoding operations:

  * The [`qsam decode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_decode) command decodes QSAM flat files to Google Cloud compatible formats.
  * The [`qsam encode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam-encode) command encodes Google Cloud data to the mainframe.
  * The [`vsam decode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#vsam_decode) command decodes VSAM files to Google Cloud compatible formats.



These operations perform symmetric transformations, that is, they move the same data to and from Google Cloud. You can define the structure of a QSAM or a VSAM file in a copybook file using the COBOL data structure definition. You can also define advanced transformations using the [Mainframe Connector transcoder configuration file](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration). The following diagrams describes these operations in detail.

![Decode mainframe data to Google Cloud](https://docs.cloud.google.com/static/mainframe-connector/docs/images/qsam-decode.png)Decode mainframe data to Google Cloud![Encode mainframe data from Google Cloud](https://docs.cloud.google.com/static/mainframe-connector/docs/images/qsam-encode.png)Encode Google Cloud data to the mainframe

This page provides an overview of the transcoding process using the `qsam decode`, `qsam encode`, and `vsam decode` commands, the physical and logical types of mainframe data, and the Optimized Row Columnar (ORC) and BigQuery type mappings.

## Physical types

Physical types define how field data is laid out on a disk. Physical types are converted to Mainframe Connector logical types which can then be mapped to database types (ORC or BigQuery).

### Alphanumeric fields

Alphanumeric fields are used to process alphanumeric strings. The data is treated as a series of characters and is stored as strings with a specific encoding, for example, Extended Binary Coded Decimal Interchange Code (EBCDIC). The transcoding process doesn't terminate if any errors occur during the encoding or decoding of alphanumeric fields. Instead, a `SUB` character for the encoding is placed at the location where the error occurred, and the transcoding process continues.

Picture symbols | Picture attributes | Logical type  
---|---|---  
A, B, G, N, U, X, 9 | DISPLAY, DISPLAY-1, NATIONAL, UTF-8 | String  
  
**Example**
    
    
    01 REC
      02 STR      PIC X(10)
      02 NATIONAL PIC N(10)
      02 UTF8     PIC U(1) USAGE UTF-8
    

#### Encoding format

Alphanumeric fields are encoded as follows:

  * X fields default to EBCDIC encoding
  * National (N) fields default to Unicode Transformation Format 16-bit (UTF-16 BE) encoding
  * UTF8 fields default to Unicode Transformation Format-8 (UTF-8) encoding



Mainframe Connector supports most single byte character set (SBCS), double byte character set (DBCS) encodings. You can also define your own [custom SBCS](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#customized-charsets) encoding, if needed.

### Binary fields (COMPUTATIONAL)

Binary fields are stored as either signed or unsigned big-endian integers. Mainframe Connector always stores binary fields logically as signed 64-bit integers. Therefore, unsigned long inputs must use only the lower 63 bits, otherwise, the transcoding process fails.

Picture symbols | Picture attributes | Logical type  
---|---|---  
S, 9 | COMP, COMPUTATIONAL | Long (signed 64-bit integer)  
  
**Example**
    
    
    01 REC
      02 INT PIC S9(8) COMP
    

### Hexadecimal floating point fields (COMP-1, COMP-2)

Hexadecimal floating point (HFP) fields are fully supported. Mainframe Connector uses both single and double precision formats for HFP fields.

Picture symbols | Picture attributes | Logical type  
---|---|---  
| COMP-1, COMP-2 | Double (64-bit signed floating point)  
  
**Example**
    
    
    01 REC
      03 HFP-SINGLE COMP-1.
      03 HFP-DOUBLE COMP-2.
    

### Packed decimal fields (COMP-3)

Packed decimal fields are fully supported. During the transcoding process, Mainframe Connector selects the most performant logical type based on the specified precision and scale.

Picture symbols | Picture attributes | Logical type  
---|---|---  
S, 9, V | COMP-3 | Long (signed 64-bit integer), BigInteger, Decimal64, BigDecimal  
  
**Example**
    
    
    01 REC
      02 DEC PIC S9(2)V9(8) COMP-3
    

### Zoned decimal field (DISPLAY)

Zoned decimal fields are fully supported. During the transcoding process, Mainframe Connector selects the most performant logical type based on the specified precision and scale.

Picture symbols | Picture attributes | Logical type  
---|---|---  
S, 9, V | DISPLAY | Long (signed 64-bit integer), BigInteger, Decimal64, BigDecimal  
  
**Example**
    
    
    01 REC
      02 DEC PIC S9(2)V9(8) DISPLAY
    

### Lists (OCCURS)

Lists are ordered collections of elements of the same type. Mainframe Connector supports the following types of lists:

  * Fixed lists
  * Dynamic lists
  * Packed dynamic lists



#### Fixed lists

Fixed lists are used when the exact number of items (item count) that will be a part of the list is known in advance, and this number always remains the same. The items in a fixed list can be of a variable size.

Fixed lists are defined as follows in a copybook:
    
    
           01 REC.
             02 LIST OCCURS 5 TIMES       PIC X(1).
             02 FLD                       PIC X(5).
    

The following image shows the layout of a fixed list with an item count of 5.

![Layout of a fixed list](https://docs.cloud.google.com/static/mainframe-connector/docs/images/fixed-lists.png)Layout of a fixed list

#### Dynamic lists

Dynamic lists are used when the maximum number of items that will be a part of the list is known in advance. However, the actual item count is unknown and is dependent on another field. The items in a dynamic list can be of variable size.

The properties of dynamic lists are as follows:

  * The length field can be converted to an integer without loss of precision.
  * The length field must be in scope.
  * The minimum item count is not enforced during the transcoding process.



Dynamic lists are defined as follows in a copybook:
    
    
    01 REC.
      02 LEN                      PIC S9(2) BINARY.
      02 LIST OCCURS 1 TO 5 TIMES
        DEPENDING ON LEN          PIC X(1).
      02 FLD                      PIC X(5).
    

The following image shows the layout of a dynamic list with a maximum number of items of five.

![Layout of a dynamic list](https://docs.cloud.google.com/static/mainframe-connector/docs/images/dynamic-lists.png)Layout of a dynamic list

#### Packed dynamic lists

Packed dynamic lists are used when the maximum number of items that will be a part of the list is dependent on another field, and the items are packed.

The properties of packed dynamic lists are as follows:

  * The length field can be converted to an integer without loss of precision.
  * The length field must be in scope.
  * The minimum item count is not enforced during the transcoding process.



Packed dynamic lists are defined as follows in a copybook:
    
    
    01 REC.
      02 LEN                       PIC S9(2) BINARY.
      02 LIST OCCURS UNBOUNDED
          DEPENDING ON LEN         PIC X(1).
      02 FLD                       PIC X(5).
    

The following image shows the layout of a packed dynamic list.

![Layout of a packed dynamic list](https://docs.cloud.google.com/static/mainframe-connector/docs/images/packed-dynamic-lists.png)Layout of a packed dynamic list

### Redefinitions (REDEFINES)

[Redefinitions](https://www.ibm.com/docs/en/cobol-linux-x86/1.2?topic=entry-redefines-clause) is a COBOL feature that allows the same data to have multiple decoding possibilities. During the decoding process, redefinitions appear as additional columns in the resulting table, and the data is decoded multiple times.

The properties of redefinitions are as follows:

  * Redefinitions to the same underlying data are not sibling fields and thus are not in scope of each other.
  * Redefined fields are decoded when the underlying field is decoded, not when they are declared. The underlying field also determines the scope of the redefined fields.
  * All redefined fields must have the same size and must have a fixed size. This means that you can't use variable length text fields and packed dynamic lists in redefined fields.



Redefinitions are defined as follows in a copybook:
    
    
    01  Rec.
    05  Field-1   PIC X(100).
    05  Group-1 REDEFINES Field-1.
      10  Field-2 PIC 9(5) comp-3.
      10  Field-3 PIC X(96).
    05  Group-2 REDEFINES Field-1.
      10  Field-4 PIC 9(4) comp-4.
      10  Field-5 PIC X(50).
      10  Field-6 PIC X(46).
    

The following image shows the layout of a redefined field.

![Layout of a redefined field](https://docs.cloud.google.com/static/mainframe-connector/docs/images/redefines.png)Layout of a redefined field

You can use redefinitions in many ways, including the following most common ways:

  * **View the same data in two different ways:** This is the most common way redefines are used. During the encoding process, the order in which the data is filled in is undefined, so you must ensure that the data in BigQuery retains its integrity when exported.

**Example**
        
        01 REC.
          02 FULL-NAME                  PIC X(12).
          02 NAME REDEFINES FULL-NAME.
            05 FIRST-NAME               PIC X(6).
            05 LAST-NAME                PIC X(6).
        

  * **Use tagged union:** Tagged unions are a common way of using redefines when you need only one of the interpretations of the data of any record, depending on a field. You can use null indicators to mark unneeded interpretations as null. This will also prevent them from getting parsed due to null indicators having lazy evaluations. The properties of tagged unions are as follows:

    * The encoding process fails if more than one redefine is defined.
    * Only equality and non-equality checks are implemented.

**Example**
    
    01  REC.
    05  TYPE      PIC X(5).
    05  DATA      PIC X(100).
    05  VARIANT-1 REDEFINES DATA.
      10  Field-2 PIC 9(4) comp-3.
      10  Field-3 PIC X(96).
    05  VARIANT-2 REDEFINES DATA.
      10  Field-4 PIC 9(4) comp-5.
      10  Field-5 PIC X(50).
      10  Field-6 PIC X(46).
    

You can use the following example to implement a tagged union:
    
    {
      "field_override": [
        {
            "field": "VARIANT-1",
            "modifier": {
              "null_if": {
                "target_field": "TYPE",
                "non_null_value": "VAR1"
              }
            }
        },
        {
            "field": "VARIANT-2",
            "modifier": {
              "null_if": {
                "target_field": "TYPE",
                "non_null_value": "VAR2"
              }
            }
        }
      ],
      "transformations": [
        {
          "field": "DATA",
          "transformation": { "exclude": {}}
        }
      ]
    }
    




## Logical Types

To transcode data to and from multiple formats, Mainframe Connector converts all data to an intermediate representation (IR) that is based on logical types. Input and output formats define how data is converted to and from any logical type. The following table lists all the logical types supported by Mainframe Connector.

Logical type | Description  
---|---  
BigDecimal | Represents decimal numbers of any scale and precision.  
BigInteger | Represents integers of any size.  
Bytes | Represents an array of bytes of variable sizes.  
Date | Represents a date independent of a specific time zone.  
Decimal64 | Represents a decimal with a range that can fit in a 64-bit signed integer of any scale.  
Double | Represents a double precision floating point number as described in IEEE Standard for Floating-Point Arithmetic (IEEE 754).  
List | Represents a list of items of a specific type. The list can contain an arbitrary number of items.  
Long | Represents a signed 64-bit number.  
Record | Represents a fixed series of fields of varying types.  
String | Represents a string of unicode characters unrelated to any specific encoding. Any valid unicode code point is representable. However, some characters may not be encodable in all encoding processes. Logical strings are of variable length.  
Timestamp | Represents a timestamp independent of a specific time zone.  
  
## ORC type mapping

The following table provides the mapping between Mainframe Connector logical types to ORC types.

Logical type | ORC type  
---|---  
BigDecimal | decimal  
BigInteger | decimal  
Bytes | binary blob  
Date | date  
Decimal64 | decimal64  
Double | float64  
List | list  
Long | 64-bit integer (bigint)  
Record | struct  
String | UTF-8 encoded string  
Timestamp | timestamp (without local timezone)  
  
## BigQuery type mapping

The following table provides the mapping between Mainframe Connector logical types to BigQuery data types.

Logical type | BigQuery data type | Comments  
---|---|---  
BigDecimal | NUMERIC |   
BigInteger | NUMERIC |   
Bytes | BYTES |   
Date | DATE |   
Decimal64 | NUMERIC |   
Double | FLOAT64 |   
List | ARRAY | Nested lists and lists of maps are not supported.  
Long | INT64 |   
Record | STRUCT | When a union only has one variant, it's converted to a NULLABLE field. Otherwise, a union is converted to a RECORD with a list of NULLABLE fields. NULLABLE fields have suffixes such as `field_0`, `field_1`. Only one of these fields is assigned a value when the data is read.  
String | STRING |   
Timestamp | TIMESTAMP |   
  
## Field scope

A field is considered to be _in scope_ for another field if it is one of the following:

  * A sibling field that is defined before the field requiring it.
  * A field in a parent record that is defined before the field requiring it.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

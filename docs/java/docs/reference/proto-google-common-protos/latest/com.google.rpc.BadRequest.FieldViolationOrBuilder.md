---
url: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.BadRequest.FieldViolationOrBuilder
title: Interface BadRequest.FieldViolationOrBuilder (2.78.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:28.810791+00:00
---

# Interface BadRequest.FieldViolationOrBuilder (2.78.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.BadRequest.FieldViolationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BadRequest.FieldViolationOrBuilder (2.78.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.78.0 (latest)  2.74.0  2.73.0  2.72.0  2.70.0  2.67.0  2.66.0  2.65.1  2.64.1  2.63.2  2.62.0  2.61.3  2.60.0  2.59.2  2.58.0  2.57.0  2.56.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.0  2.46.0  2.45.1  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.1  2.38.0  2.37.1  2.36.0  2.34.0  2.33.0  2.32.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.1  2.22.1  2.21.1  2.15.0  2.14.3  2.13.0  2.12.0  2.11.0  2.10.0  2.9.6  2.8.4  2.7.4 
    
    
    public static interface BadRequest.FieldViolationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDescription()
    
    
    public abstract String getDescription()

A description of why the request element is bad.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

A description of why the request element is bad.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getField()
    
    
    public abstract String getField()

A path that leads to a field in the request body. The value will be a sequence of dot-separated identifiers that identify a protocol buffer field.

Consider the following:

message CreateContactRequest { message EmailAddress { enum Type { TYPE_UNSPECIFIED = 0; HOME = 1; WORK = 2; }

optional string email = 1; repeated EmailType type = 2; }

string full_name = 1; repeated EmailAddress email_addresses = 2; }

In this example, in proto `field` could take one of the following values:

  * `full_name` for a violation in the `full_name` value
  * `email_addresses[0].email` for a violation in the `email` field of the first `email_addresses` message
  * `email_addresses[2].type[1]` for a violation in the second `type` value in the third `email_addresses` message.

In JSON, the same values are represented as:

  * `fullName` for a violation in the `fullName` value

  * `emailAddresses[0].email` for a violation in the `email` field of the first `emailAddresses` message
  * `emailAddresses[2].type[1]` for a violation in the second `type` value in the third `emailAddresses` message.



`string field = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The field.  
  
### getFieldBytes()
    
    
    public abstract ByteString getFieldBytes()

A path that leads to a field in the request body. The value will be a sequence of dot-separated identifiers that identify a protocol buffer field.

Consider the following:

message CreateContactRequest { message EmailAddress { enum Type { TYPE_UNSPECIFIED = 0; HOME = 1; WORK = 2; }

optional string email = 1; repeated EmailType type = 2; }

string full_name = 1; repeated EmailAddress email_addresses = 2; }

In this example, in proto `field` could take one of the following values:

  * `full_name` for a violation in the `full_name` value
  * `email_addresses[0].email` for a violation in the `email` field of the first `email_addresses` message
  * `email_addresses[2].type[1]` for a violation in the second `type` value in the third `email_addresses` message.

In JSON, the same values are represented as:

  * `fullName` for a violation in the `fullName` value

  * `emailAddresses[0].email` for a violation in the `email` field of the first `emailAddresses` message
  * `emailAddresses[2].type[1]` for a violation in the second `type` value in the third `emailAddresses` message.



`string field = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for field.  
  
### getLocalizedMessage()
    
    
    public abstract LocalizedMessage getLocalizedMessage()

Provides a localized error message for field-level errors that is safe to return to the API consumer.

`.google.rpc.LocalizedMessage localized_message = 4;`

**Returns**  
---  
**Type** | **Description**  
`[LocalizedMessage](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.LocalizedMessage)` | The localizedMessage.  
  
### getLocalizedMessageOrBuilder()
    
    
    public abstract LocalizedMessageOrBuilder getLocalizedMessageOrBuilder()

Provides a localized error message for field-level errors that is safe to return to the API consumer.

`.google.rpc.LocalizedMessage localized_message = 4;`

**Returns**  
---  
**Type** | **Description**  
`[LocalizedMessageOrBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.LocalizedMessageOrBuilder)` |   
  
### getReason()
    
    
    public abstract String getReason()

The reason of the field-level error. This is a constant value that identifies the proximate cause of the field-level error. It should uniquely identify the type of the FieldViolation within the scope of the google.rpc.ErrorInfo.domain. This should be at most 63 characters and match a regular expression of `A-Z+[A-Z0-9]`, which represents UPPER_SNAKE_CASE.

`string reason = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The reason.  
  
### getReasonBytes()
    
    
    public abstract ByteString getReasonBytes()

The reason of the field-level error. This is a constant value that identifies the proximate cause of the field-level error. It should uniquely identify the type of the FieldViolation within the scope of the google.rpc.ErrorInfo.domain. This should be at most 63 characters and match a regular expression of `A-Z+[A-Z0-9]`, which represents UPPER_SNAKE_CASE.

`string reason = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for reason.  
  
### hasLocalizedMessage()
    
    
    public abstract boolean hasLocalizedMessage()

Provides a localized error message for field-level errors that is safe to return to the API consumer.

`.google.rpc.LocalizedMessage localized_message = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the localizedMessage field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

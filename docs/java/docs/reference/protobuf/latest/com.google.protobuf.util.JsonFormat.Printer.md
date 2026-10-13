---
url: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Printer
title: Class JsonFormat.Printer (3.19.4) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:40.899234+00:00
---

# Class JsonFormat.Printer (3.19.4)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Printer

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class JsonFormat.Printer (3.19.4) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static class JsonFormat.Printer

A Printer converts protobuf message to JSON format.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > JsonFormat.Printer

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### appendTo(MessageOrBuilder message, Appendable output)
    
    
    public void appendTo(MessageOrBuilder message, Appendable output)

Converts a protobuf message to JSON format.

**Parameters**  
---  
**Name** | **Description**  
`message` | `[MessageOrBuilder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder)`  
  
`output` | `[Appendable](https://docs.oracle.com/javase/8/docs/api/java/lang/Appendable.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | if the message contains Any types that can't be resolved.  
  
### includingDefaultValueFields()
    
    
    public JsonFormat.Printer includingDefaultValueFields()

Creates a new Printer that will also print fields set to their defaults. Empty repeated fields and map fields will be printed as well. The new Printer clones all other configurations from the current Printer.

**Returns**  
---  
**Type** | **Description**  
`[JsonFormat.Printer](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Printer)` |   
  
### includingDefaultValueFields(Set<Descriptors.FieldDescriptor> fieldsToAlwaysOutput)
    
    
    public JsonFormat.Printer includingDefaultValueFields(Set<Descriptors.FieldDescriptor> fieldsToAlwaysOutput)

Creates a new Printer that will also print default-valued fields if their FieldDescriptors are found in the supplied set. Empty repeated fields and map fields will be printed as well, if they match. The new Printer clones all other configurations from the current Printer. Call includingDefaultValueFields() with no args to unconditionally output all fields.

**Parameter**  
---  
**Name** | **Description**  
`fieldsToAlwaysOutput` | `[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[FieldDescriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonFormat.Printer](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Printer)` |   
  
### omittingInsignificantWhitespace()
    
    
    public JsonFormat.Printer omittingInsignificantWhitespace()

Create a new Printer that will omit all insignificant whitespace in the JSON output. This new Printer clones all other configurations from the current Printer. Insignificant whitespace is defined by the JSON spec as whitespace that appear between JSON structural elements:

ws = *( %x20 / ; Space %x09 / ; Horizontal tab %x0A / ; Line feed or New line %x0D ) ; Carriage return

See <https://tools.ietf.org/html/rfc7159> current Printer.

**Returns**  
---  
**Type** | **Description**  
`[JsonFormat.Printer](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Printer)` |   
  
### preservingProtoFieldNames()
    
    
    public JsonFormat.Printer preservingProtoFieldNames()

Creates a new Printer that is configured to use the original proto field names as defined in the .proto file rather than converting them to lowerCamelCase. The new Printer clones all other configurations from the current Printer.

**Returns**  
---  
**Type** | **Description**  
`[JsonFormat.Printer](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Printer)` |   
  
### print(MessageOrBuilder message)
    
    
    public String print(MessageOrBuilder message)

Converts a protobuf message to JSON format. Throws exceptions if there are unknown Any types in the message.

**Parameter**  
---  
**Name** | **Description**  
`message` | `[MessageOrBuilder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException)` |   
  
### printingEnumsAsInts()
    
    
    public JsonFormat.Printer printingEnumsAsInts()

Creates a new Printer that will print enum field values as integers instead of as string. The new Printer clones all other configurations from the current Printer.

**Returns**  
---  
**Type** | **Description**  
`[JsonFormat.Printer](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Printer)` |   
  
### sortingMapKeys()
    
    
    public JsonFormat.Printer sortingMapKeys()

Create a new Printer that will sort the map keys in the JSON output.

Use of this modifier is discouraged, the generated JSON messages are equivalent with and without this option set, but there are some corner use cases that demand a stable output, while order of map keys is otherwise arbitrary.

The generated order is not well-defined and should not be depended on, but it's stable.

This new Printer clones all other configurations from the current Printer.

**Returns**  
---  
**Type** | **Description**  
`[JsonFormat.Printer](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Printer)` |   
  
### usingTypeRegistry(TypeRegistry registry)
    
    
    public JsonFormat.Printer usingTypeRegistry(TypeRegistry registry)

Creates a new Printer using the given registry. The new Printer clones all other configurations from the current Printer.

**Parameter**  
---  
**Name** | **Description**  
`registry` | `[TypeRegistry](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TypeRegistry)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonFormat.Printer](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Printer)` |   
  
### usingTypeRegistry(JsonFormat.TypeRegistry oldRegistry)
    
    
    public JsonFormat.Printer usingTypeRegistry(JsonFormat.TypeRegistry oldRegistry)

Creates a new Printer using the given registry. The new Printer clones all other configurations from the current Printer.

**Parameter**  
---  
**Name** | **Description**  
`oldRegistry` | `[JsonFormat.TypeRegistry](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.TypeRegistry)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonFormat.Printer](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Printer)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 

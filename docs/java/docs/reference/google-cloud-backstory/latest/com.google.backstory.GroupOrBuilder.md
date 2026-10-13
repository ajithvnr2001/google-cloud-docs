---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.GroupOrBuilder
title: Interface GroupOrBuilder (0.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:16.766962+00:00
---

# Interface GroupOrBuilder (0.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.GroupOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GroupOrBuilder (0.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.0 (latest)  0.3.0  0.2.0  0.1.0 
    
    
    public interface GroupOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAttribute()
    
    
    public abstract Attribute getAttribute()

Generic entity metadata attributes of the group.

`.google.backstory.Attribute attribute = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Attribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Attribute)` | The attribute.  
  
### getAttributeOrBuilder()
    
    
    public abstract AttributeOrBuilder getAttributeOrBuilder()

Generic entity metadata attributes of the group.

`.google.backstory.Attribute attribute = 4;`

**Returns**  
---  
**Type** | **Description**  
`[AttributeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.AttributeOrBuilder)` |   
  
### getCreationTime() (deprecated)
    
    
    public abstract Timestamp getCreationTime()

**Deprecated.** _google.backstory.Group.creation_time is deprecated. See backstory/udm.proto;l=4934_

Group creation time. Deprecated: creation_time should be populated in Attribute as generic metadata.

`.google.protobuf.Timestamp creation_time = 100 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The creationTime.  
  
### getCreationTimeOrBuilder() (deprecated)
    
    
    public abstract TimestampOrBuilder getCreationTimeOrBuilder()

Group creation time. Deprecated: creation_time should be populated in Attribute as generic metadata.

`.google.protobuf.Timestamp creation_time = 100 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getEmailAddresses(int index)
    
    
    public abstract String getEmailAddresses(int index)

Email addresses of the group.

`repeated string email_addresses = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The emailAddresses at the given index.  
  
### getEmailAddressesBytes(int index)
    
    
    public abstract ByteString getEmailAddressesBytes(int index)

Email addresses of the group.

`repeated string email_addresses = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the emailAddresses at the given index.  
  
### getEmailAddressesCount()
    
    
    public abstract int getEmailAddressesCount()

Email addresses of the group.

`repeated string email_addresses = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of emailAddresses.  
  
### getEmailAddressesList()
    
    
    public abstract List<String> getEmailAddressesList()

Email addresses of the group.

`repeated string email_addresses = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the emailAddresses.  
  
### getGroupDisplayName()
    
    
    public abstract String getGroupDisplayName()

Group display name. e.g. "Finance".

`string group_display_name = 101;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The groupDisplayName.  
  
### getGroupDisplayNameBytes()
    
    
    public abstract ByteString getGroupDisplayNameBytes()

Group display name. e.g. "Finance".

`string group_display_name = 101;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for groupDisplayName.  
  
### getProductObjectId()
    
    
    public abstract String getProductObjectId()

Product globally unique user object identifier, such as an LDAP Object Identifier.

`string product_object_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The productObjectId.  
  
### getProductObjectIdBytes()
    
    
    public abstract ByteString getProductObjectIdBytes()

Product globally unique user object identifier, such as an LDAP Object Identifier.

`string product_object_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for productObjectId.  
  
### getWindowsSid()
    
    
    public abstract String getWindowsSid()

Microsoft Windows SID of the group.

`string windows_sid = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The windowsSid.  
  
### getWindowsSidBytes()
    
    
    public abstract ByteString getWindowsSidBytes()

Microsoft Windows SID of the group.

`string windows_sid = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for windowsSid.  
  
### hasAttribute()
    
    
    public abstract boolean hasAttribute()

Generic entity metadata attributes of the group.

`.google.backstory.Attribute attribute = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the attribute field is set.  
  
### hasCreationTime() (deprecated)
    
    
    public abstract boolean hasCreationTime()

**Deprecated.** _google.backstory.Group.creation_time is deprecated. See backstory/udm.proto;l=4934_

Group creation time. Deprecated: creation_time should be populated in Attribute as generic metadata.

`.google.protobuf.Timestamp creation_time = 100 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the creationTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber
title: Class PhoneNumber (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:15.392924+00:00
---

# Class PhoneNumber (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class PhoneNumber (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Type.PhoneNumber)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Type.PhoneNumber)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Type.PhoneNumber)


    
    
    public sealed class PhoneNumber : IMessage<PhoneNumber>, IEquatable<PhoneNumber>, IDeepCloneable<PhoneNumber>, IBufferMessage, IMessage

An object representing a phone number, suitable as an API wire format.

This representation:

  * should not be used for locale-specific formatting of a phone number, such as "+1 (650) 253-0000 ext. 123"

  * is not designed for efficient storage

  * may not be suitable for dialing - specialized libraries (see references) should be used to parse the number for that purpose



To do something meaningful with this number, such as format it for various use-cases, convert it to an `i18n.phonenumbers.PhoneNumber` object first.

For instance, in Java this would be:

com.google.type.PhoneNumber wireProto = com.google.type.PhoneNumber.newBuilder().build(); com.google.i18n.phonenumbers.Phonenumber.PhoneNumber phoneNumber = PhoneNumberUtil.getInstance().parse(wireProto.getE164Number(), "ZZ"); if (!wireProto.getExtension().isEmpty()) { phoneNumber.setExtension(wireProto.getExtension()); }

Reference(s):

  * <https://github.com/google/libphonenumber>



## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PhoneNumber

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[PhoneNumber](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PhoneNumber](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[PhoneNumber](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

## Namespace

[Google.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type)

## Assembly

Google.Api.CommonProtos.dll

## Constructors 

### PhoneNumber()
    
    
    public PhoneNumber()

### PhoneNumber(PhoneNumber)
    
    
    public PhoneNumber(PhoneNumber other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PhoneNumber](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber)`  
  
  
## Fields 

### E164NumberFieldNumber
    
    
    public const int E164NumberFieldNumber = 1

Field number for the "e164_number" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ExtensionFieldNumber
    
    
    public const int ExtensionFieldNumber = 3

Field number for the "extension" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ShortCodeFieldNumber
    
    
    public const int ShortCodeFieldNumber = 2

Field number for the "short_code" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Properties 

### Descriptor
    
    
    public static MessageDescriptor Descriptor { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageDescriptor](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.MessageDescriptor.html)` |   
  
### E164Number
    
    
    public string E164Number { get; set; }

The phone number, represented as a leading plus sign ('+'), followed by a phone number that uses a relaxed ITU E.164 format consisting of the country calling code (1 to 3 digits) and the subscriber number, with no additional spaces or formatting, e.g.:

  * correct: "+15552220123"
  * incorrect: "+1 (555) 222-01234 x123".



The ITU E.164 format limits the latter to 12 digits, but in practice not all countries respect that, so we relax that restriction here. National-only numbers are not allowed.

References:

  * <https://www.itu.int/rec/T-REC-E.164-201011-I>
  * <https://en.wikipedia.org/wiki/E.164>.
  * <https://en.wikipedia.org/wiki/List_of_country_calling_codes>



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Extension
    
    
    public string Extension { get; set; }

The phone number's extension. The extension is not standardized in ITU recommendations, except for being defined as a series of numbers with a maximum length of 40 digits. Other than digits, some other dialing characters such as ',' (indicating a wait) or '#' may be stored here.

Note that no regions currently use extensions with short codes, so this field is normally only set in conjunction with an E.164 number. It is held separately from the E.164 number to allow for short code extensions in the future.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasE164Number
    
    
    public bool HasE164Number { get; }

Gets whether the "e164_number" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### KindCase
    
    
    public PhoneNumber.KindOneofCase KindCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[PhoneNumber](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber)[KindOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber.KindOneofCase)` |   
  
### Parser
    
    
    public static MessageParser<PhoneNumber> Parser { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageParser](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.MessageParser-1.html)[PhoneNumber](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber)` |   
  
### ShortCode
    
    
    public PhoneNumber.Types.ShortCode ShortCode { get; set; }

A short code.

Reference(s):

  * <https://en.wikipedia.org/wiki/Short_code>



**Property Value**  
---  
**Type** | **Description**  
`[PhoneNumber](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber.Types)[ShortCode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber.Types.ShortCode)` |   
  
## Methods 

### CalculateSize()
    
    
    public int CalculateSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ClearE164Number()
    
    
    public void ClearE164Number()

Clears the value of the oneof if it's currently set to "e164_number"

### ClearKind()
    
    
    public void ClearKind()

### Clone()
    
    
    public PhoneNumber Clone()

**Returns**  
---  
**Type** | **Description**  
`[PhoneNumber](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber)` |   
  
### Equals(PhoneNumber)
    
    
    public bool Equals(PhoneNumber other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PhoneNumber](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber)`  
  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Equals(object)
    
    
    public override bool Equals(object other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[object](https://learn.microsoft.com/dotnet/api/system.object)`  
  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
**Overrides**

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object\))

### GetHashCode()
    
    
    public override int GetHashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
**Overrides**

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

### MergeFrom(CodedInputStream)
    
    
    public void MergeFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.CodedInputStream.html)`  
  
  
### MergeFrom(PhoneNumber)
    
    
    public void MergeFrom(PhoneNumber other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PhoneNumber](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber)`  
  
  
### ToString()
    
    
    public override string ToString()

**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Overrides**

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

### WriteTo(CodedOutputStream)
    
    
    public void WriteTo(CodedOutputStream output)

**Parameter**  
---  
**Name** | **Description**  
`output` | `[CodedOutputStream](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.CodedOutputStream.html)`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 

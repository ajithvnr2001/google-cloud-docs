---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRules
title: Google Bigtable v2 API - Class ReadModifyWriteRules (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:02.370700+00:00
---

# Google Bigtable v2 API - Class ReadModifyWriteRules (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRules

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class ReadModifyWriteRules (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public static class ReadModifyWriteRules

Reference documentation and code samples for the Google Bigtable v2 API class ReadModifyWriteRules.

Static class with convenience methods for creating various kinds of [ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReadModifyWriteRules

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Methods 

### Append(string, BigtableByteString, BigtableByteString)
    
    
    public static ReadModifyWriteRule Append(string familyName, BigtableByteString columnQualifier, BigtableByteString appendValue)

Rule specifying that `appendValue` be appended to the existing value. If the targeted cell is unset, it will be treated as containing the empty string.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the family to which the read/modify/write should be applied. Must match `[-_.a-zA-Z0-9]+`  
`columnQualifier` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The qualifier of the column to which the read/modify/write should be applied. Can be any byte string, including the empty string.  
`appendValue` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The value to append to the existing cell value.  
**Returns**  
---  
**Type** | **Description**  
`[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)` | The append value rule.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `columnQualifier` can be specified using a string as well and its UTF-8 representations will be used. 

### Increment(string, BigtableByteString, long)
    
    
    public static ReadModifyWriteRule Increment(string familyName, BigtableByteString columnQualifier, long incrementAmount)

Rule specifying that `incrementAmount` be added to the existing value. If the targeted cell is unset, it will be treated as containing a zero. Otherwise, the targeted cell must contain an 8-byte value (interpreted as a 64-bit big-endian signed integer), or the entire request will fail.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the family to which the read/modify/write should be applied. Must match `[-_.a-zA-Z0-9]+`  
`columnQualifier` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The qualifier of the column to which the read/modify/write should be applied. Can be any byte string, including the empty string.  
`incrementAmount` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
The amount to increment the existing cell value.  
**Returns**  
---  
**Type** | **Description**  
`[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)` | The increment amount rule.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `columnQualifier` can be specified using a string as well and its UTF-8 representations will be used. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

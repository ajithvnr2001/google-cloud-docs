---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest.Types.CsvImportOptions
title: AlloyDB v1beta API - Class ImportClusterRequest.Types.CsvImportOptions (1.0.0-beta19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:32.418130+00:00
---

# AlloyDB v1beta API - Class ImportClusterRequest.Types.CsvImportOptions (1.0.0-beta19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest.Types.CsvImportOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1beta API - Class ImportClusterRequest.Types.CsvImportOptions (1.0.0-beta19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta19 (latest)  1.0.0-beta18 
    
    
    public sealed class ImportClusterRequest.Types.CsvImportOptions : IMessage<ImportClusterRequest.Types.CsvImportOptions>, IEquatable<ImportClusterRequest.Types.CsvImportOptions>, IDeepCloneable<ImportClusterRequest.Types.CsvImportOptions>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1beta API class ImportClusterRequest.Types.CsvImportOptions.

Options for importing data in CSV format.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ImportClusterRequest.Types.CsvImportOptions

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ImportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest.Types)[CsvImportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest.Types.CsvImportOptions), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ImportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest.Types)[CsvImportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest.Types.CsvImportOptions), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ImportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest.Types)[CsvImportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest.Types.CsvImportOptions), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta)

## Assembly

Google.Cloud.AlloyDb.V1Beta.dll

## Constructors 

### CsvImportOptions()
    
    
    public CsvImportOptions()

### CsvImportOptions(CsvImportOptions)
    
    
    public CsvImportOptions(ImportClusterRequest.Types.CsvImportOptions other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ImportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest.Types)[CsvImportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest.Types.CsvImportOptions)`  
  
  
## Properties 

### Columns
    
    
    public RepeatedField<string> Columns { get; }

Optional. The columns to which CSV data is imported. If not specified, all columns of the database table are loaded with CSV data.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EscapeCharacter
    
    
    public string EscapeCharacter { get; set; }

Optional. Specifies the character that should appear before a data character that needs to be escaped. The default is same as quote character. The value of this argument has to be a character in Hex ASCII Code.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FieldDelimiter
    
    
    public string FieldDelimiter { get; set; }

Optional. Specifies the character that separates columns within each row (line) of the file. The default is comma. The value of this argument has to be a character in Hex ASCII Code.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### QuoteCharacter
    
    
    public string QuoteCharacter { get; set; }

Optional. Specifies the quoting character to be used when a data value is quoted. The default is double-quote. The value of this argument has to be a character in Hex ASCII Code.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Table
    
    
    public string Table { get; set; }

Required. The database table to import CSV file into.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

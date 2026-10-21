---
url: https://docs.cloud.google.com/mainframe-connector/docs/csv-configuration/
title: CSV configuration \u00a0|\u00a0 Mainframe Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:15:08.133552+00:00
---

# CSV configuration  |  Mainframe Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/csv-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Reference ](https://docs.cloud.google.com/mainframe-connector/docs/reference)



Send feedback 

#  CSV configuration Stay organized with collections  Save and categorize content based on your preferences. 

You can configure the Mainframe Connector transcoder's CSV formatting by adding the required configuration in a JSON file, and specifying this file using the `--input-parameter csv-dialect`=[DataPath](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#datapath) option with the [`qsam encode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_encode) or [`qsam decode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_decode) commands. You must define the CSV configuration as specified in section [CsvConfiguration](https://docs.cloud.google.com/mainframe-connector/docs/csv-configuration#csvconfiguration).

This page describes the various CSV parameters you can configure as input parameters for transcoding. The `CsvConfiguration` object contains all CSV encoder and decoder configuration options.

## CsvConfiguration

The `CsvConfiguration` object lets you configure the CSV decode and encoder configuration.

JSON representation  
---  
      
    
    {
        "binary_data_encoding": enum (BinaryDataEncoding),
        "date_format": string,
        "delimiter": string,
        "header": enum (WriteHeaderMode),
        "line_terminator": string,
        "list_end_delimiter": string,
        "list_start_delimiter": string,
        "null_representation": string,
        "quote": string,
        "quote_escaping": string,
        "quote_mode": enum (QuoteMode),
        "struct_end_delimiter": string,
        "struct_start_delimiter": string,
        "support_list": boolean,
        "support_struct": boolean,
        "timestamp_format": string  
    }
      
  
Fields  
---  
`binary_data_encoding` |  `enum (`BinaryDataEncoding`)` Specify the way in which Mainframe Connector encodes or decodes binary data. Valid values are hexadecimal, base64, or hex. The default value is base64.  
`date_format` |  `string` Specify the format for the date. The default format is `yyyy-mm-dd`.  
`delimiter` |  `string` Specify the character to use to separate fields.  
`header` |  `enum (`WriteHeaderMode`)` Set this to true if you want the first row to contain column names instead of actual data.  
`line_terminator` |  `string` Specify the character to use to separate lines.  
`list_end_delimiter` |  `string` If `support_list` is set to true, this value represents the end character delimiter for lists.  
`list_start_delimiter` |  `string` If `support_list` is set to true, this value represents the start character delimiter for lists.  
`null_representation` |  `string` Specify the string that represents a null character.  
`quote` |  `string` Specify the quote character.  
`quote_escaping` |  `string` Specify the escape character.  
`quote_mode` |  `enum (`QuoteMode`)` Specify the quoting behavior. The default value is `MINIMAL`.  
`struct_end_delimiter` |  `string` If `support_struct` is set to true, this value represents the end character delimiter for structs.  
`struct_start_delimiter` |  `string` If `support_struct` is set to true, this value represents the start character delimiter for structs.  
`support_list` |  `boolean` Set to true if you want Mainframe Connector to support lists in CSV.  
`support_struct` |  `boolean` Set to true if you want Mainframe Connector to support structs in CSV.  
`timestamp_format` |  `string` Specify the format for the timestamp. The default value is `DateTimeFormatter.ISO_INSTANT`.  
  
## Enums

### BinaryDataEncoding

Specify the way in which Mainframe Connector encodes or decodes binary data. Valid values are hexadecimal, base64, or hex. The default value is base64.

Enums  
---  
`BASE64` | Encodes binary data into an ASCII string.  
`HEX` | Encodes binary data into hex (\x format) or escaped octal.  
`HEXADECIMAL` | Encodes binary data into the hexadecimal (0x format) or raw binary.  
  
### QuoteMode

Defines quoting behavior.

Enums  
---  
`ALL` | Quotes all fields.  
`ALL_NON_NULL` | Quotes all non-null fields.  
`MINIMAL` | Quotes fields which contain special characters such as a the field delimiter, and quotes character or any of the characters in the line separator string.  
`NONE` | Never quotes fields. When a delimiter occurs in the data, the printer prefixes it with the escape character. If the escape character is not set, format validation throws an exception.  
`NON_NUMERIC` | Quotes all non-numeric fields.  
  
### WriteHeaderMode

Defines the behavior of writing the CSV header.

Enums  
---  
`ALWAYS` | Always write the CSV header.  
`NO` | Doesn't write the CSV header.  
`YES` | Writes the CSV header only if data is present.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

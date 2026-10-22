---
url: https://docs.cloud.google.com/mainframe-connector/docs/json-configuration/
title: JSON configuration \u00a0|\u00a0 Mainframe Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:12.057995+00:00
---

# JSON configuration  |  Mainframe Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/json-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Reference ](https://docs.cloud.google.com/mainframe-connector/docs/reference)



Send feedback 

#  JSON configuration Stay organized with collections  Save and categorize content based on your preferences. 

You can configure the Mainframe Connector transcoder's JSON formatting by adding the required configuration in a JSON file, and specifying this file using the `--input-parameter json-dialect`=[DataPath](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#datapath) option with the [`qsam encode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_encode) or [`qsam decode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_decode) commands. You must define the JSON configuration as specified in section [JsonConfiguration](https://docs.cloud.google.com/mainframe-connector/docs/json-configuration#jsonconfiguration).

This page describes the various JSON parameters you can configure as input parameters for transcoding. The `JsonConfiguration` object contains all JSON encoder and decoder configuration options.

## JsonConfiguration

The `JsonConfiguration` object lets you configure the JSON decoder and encoder configuration.

JSON representation  
---  
      
    
    {
        "date_format": string,
        "encoding": string,
        "omit_null_fields": boolean,
        "timestamp_format": string  
    }
      
  
Fields  
---  
`date_format` |  `string` Specify the format for the date. The default format is `yyyy-MM-dd`.  
`encoding` |  `string` Specify the character encoding to use for the JSON output. The default is `UTF-8`.  
`omit_null_fields` |  `boolean` Set to `true` if you want `null` fields to be omitted from the JSON output.  
`timestamp_format` |  `string` Specify the format for the timestamp. The default value is `DateTimeFormatter.ISO_INSTANT`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

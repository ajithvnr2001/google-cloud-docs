---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.text.textstyle-class
title: Class protos.google.monitoring.dashboard.v1.Text.TextStyle (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:43:23.656169+00:00
---

# Class protos.google.monitoring.dashboard.v1.Text.TextStyle (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.text.textstyle-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.monitoring.dashboard.v1.Text.TextStyle (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  4.2.0  2.9.2  2.8.0  2.6.1  2.5.1  2.4.2  2.3.4 

Represents a TextStyle.

## Implements

[protos.google.monitoring.dashboard.v1.Text.ITextStyle](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.text.itextstyle)

## Package

[@google-cloud/monitoring-dashboards](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.monitoring.dashboard.v1.Text.ITextStyle);

Constructs a new TextStyle.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITextStyle](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.text.itextstyle)`   
Properties to set  
  
## Properties 

### backgroundColor
    
    
    public backgroundColor: string;

TextStyle backgroundColor.

### fontSize
    
    
    public fontSize: (google.monitoring.dashboard.v1.Text.TextStyle.FontSize|keyof typeof google.monitoring.dashboard.v1.Text.TextStyle.FontSize);

TextStyle fontSize.

### horizontalAlignment
    
    
    public horizontalAlignment: (google.monitoring.dashboard.v1.Text.TextStyle.HorizontalAlignment|keyof typeof google.monitoring.dashboard.v1.Text.TextStyle.HorizontalAlignment);

TextStyle horizontalAlignment.

### padding
    
    
    public padding: (google.monitoring.dashboard.v1.Text.TextStyle.PaddingSize|keyof typeof google.monitoring.dashboard.v1.Text.TextStyle.PaddingSize);

TextStyle padding.

### pointerLocation
    
    
    public pointerLocation: (google.monitoring.dashboard.v1.Text.TextStyle.PointerLocation|keyof typeof google.monitoring.dashboard.v1.Text.TextStyle.PointerLocation);

TextStyle pointerLocation.

### textColor
    
    
    public textColor: string;

TextStyle textColor.

### verticalAlignment
    
    
    public verticalAlignment: (google.monitoring.dashboard.v1.Text.TextStyle.VerticalAlignment|keyof typeof google.monitoring.dashboard.v1.Text.TextStyle.VerticalAlignment);

TextStyle verticalAlignment.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.monitoring.dashboard.v1.Text.ITextStyle): google.monitoring.dashboard.v1.Text.TextStyle;

Creates a new TextStyle instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITextStyle](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.text.itextstyle)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[TextStyle](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.text.textstyle-class)` | TextStyle instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.monitoring.dashboard.v1.Text.TextStyle;

Decodes a TextStyle message from the specified reader or buffer.

**Parameters**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
`length` |  `number`   
Message length if known beforehand  
**Returns**  
---  
**Type** | **Description**  
`[TextStyle](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.text.textstyle-class)` | TextStyle  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.monitoring.dashboard.v1.Text.TextStyle;

Decodes a TextStyle message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[TextStyle](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.text.textstyle-class)` | TextStyle  
  
### encode(message, writer)
    
    
    public static encode(message: google.monitoring.dashboard.v1.Text.ITextStyle, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified TextStyle message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITextStyle](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.text.itextstyle)`   
TextStyle message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.monitoring.dashboard.v1.Text.ITextStyle, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified TextStyle message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITextStyle](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.text.itextstyle)`   
TextStyle message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.monitoring.dashboard.v1.Text.TextStyle;

Creates a TextStyle message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[TextStyle](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.text.textstyle-class)` | TextStyle  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for TextStyle

**Parameter**  
---  
**Name** | **Description**  
`typeUrlPrefix` |  `string`   
your custom typeUrlPrefix(default "type.googleapis.com")  
**Returns**  
---  
**Type** | **Description**  
`string` | The default type url  
  
### toJSON()
    
    
    public toJSON(): { [k: string]: any };

Converts this TextStyle to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.monitoring.dashboard.v1.Text.TextStyle, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a TextStyle message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[TextStyle](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.text.textstyle-class)`   
TextStyle  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a TextStyle message.

**Parameter**  
---  
**Name** | **Description**  
`message` |  `{ [k: string]: any }`   
Plain object to verify  
**Returns**  
---  
**Type** | **Description**  
`(string|null)` | `null` if valid, otherwise the reason why it is not  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 

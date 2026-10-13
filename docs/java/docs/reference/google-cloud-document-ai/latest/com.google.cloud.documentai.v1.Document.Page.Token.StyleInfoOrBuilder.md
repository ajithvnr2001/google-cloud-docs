---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Token.StyleInfoOrBuilder
title: Interface Document.Page.Token.StyleInfoOrBuilder (2.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:20.336879+00:00
---

# Interface Document.Page.Token.StyleInfoOrBuilder (2.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Token.StyleInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Document.Page.Token.StyleInfoOrBuilder (2.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.103.0 (latest)  2.99.0  2.98.0  2.97.0  2.95.0  2.92.0  2.91.0  2.89.0  2.87.0  2.86.0  2.85.0  2.84.0  2.82.0  2.80.0  2.79.0  2.78.0  2.77.0  2.76.0  2.74.0  2.72.0  2.71.0  2.68.0  2.67.0  2.66.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.5  2.6.2  2.5.1  2.4.3  2.3.1  2.2.1  2.1.9 
    
    
    public static interface Document.Page.Token.StyleInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBackgroundColor()
    
    
    public abstract Color getBackgroundColor()

Color of the background.

`.google.type.Color background_color = 15;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Color` | The backgroundColor.  
  
### getBackgroundColorOrBuilder()
    
    
    public abstract ColorOrBuilder getBackgroundColorOrBuilder()

Color of the background.

`.google.type.Color background_color = 15;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.ColorOrBuilder` |   
  
### getBold()
    
    
    public abstract boolean getBold()

Whether the text is bold (equivalent to font_weight is at least `700`).

`bool bold = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The bold.  
  
### getFontSize()
    
    
    public abstract int getFontSize()

Font size in points (`1` point is `¹⁄₇₂` inches).

`int32 font_size = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The fontSize.  
  
### getFontType()
    
    
    public abstract String getFontType()

Name or style of the font.

`string font_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The fontType.  
  
### getFontTypeBytes()
    
    
    public abstract ByteString getFontTypeBytes()

Name or style of the font.

`string font_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for fontType.  
  
### getFontWeight()
    
    
    public abstract int getFontWeight()

TrueType weight on a scale `100` (thin) to `1000` (ultra-heavy). Normal is `400`, bold is `700`.

`int32 font_weight = 12;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The fontWeight.  
  
### getHandwritten()
    
    
    public abstract boolean getHandwritten()

Whether the text is handwritten.

`bool handwritten = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The handwritten.  
  
### getItalic()
    
    
    public abstract boolean getItalic()

Whether the text is italic.

`bool italic = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The italic.  
  
### getLetterSpacing()
    
    
    public abstract double getLetterSpacing()

Letter spacing in points.

`double letter_spacing = 3;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The letterSpacing.  
  
### getPixelFontSize()
    
    
    public abstract double getPixelFontSize()

Font size in pixels, equal to _unrounded font_size_

  * _resolution_ ÷ `72.0`.



`double pixel_font_size = 2;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pixelFontSize.  
  
### getSmallcaps()
    
    
    public abstract boolean getSmallcaps()

Whether the text is in small caps. This feature is not supported yet.

`bool smallcaps = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The smallcaps.  
  
### getStrikeout()
    
    
    public abstract boolean getStrikeout()

Whether the text is strikethrough. This feature is not supported yet.

`bool strikeout = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The strikeout.  
  
### getSubscript()
    
    
    public abstract boolean getSubscript()

Whether the text is a subscript. This feature is not supported yet.

`bool subscript = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The subscript.  
  
### getSuperscript()
    
    
    public abstract boolean getSuperscript()

Whether the text is a superscript. This feature is not supported yet.

`bool superscript = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The superscript.  
  
### getTextColor()
    
    
    public abstract Color getTextColor()

Color of the text.

`.google.type.Color text_color = 14;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Color` | The textColor.  
  
### getTextColorOrBuilder()
    
    
    public abstract ColorOrBuilder getTextColorOrBuilder()

Color of the text.

`.google.type.Color text_color = 14;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.ColorOrBuilder` |   
  
### getUnderlined()
    
    
    public abstract boolean getUnderlined()

Whether the text is underlined.

`bool underlined = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The underlined.  
  
### hasBackgroundColor()
    
    
    public abstract boolean hasBackgroundColor()

Color of the background.

`.google.type.Color background_color = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the backgroundColor field is set.  
  
### hasTextColor()
    
    
    public abstract boolean hasTextColor()

Color of the text.

`.google.type.Color text_color = 14;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the textColor field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

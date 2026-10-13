---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Document.StyleOrBuilder
title: Interface Document.StyleOrBuilder (2.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:13.559359+00:00
---

# Interface Document.StyleOrBuilder (2.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Document.StyleOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Document.StyleOrBuilder (2.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.103.0 (latest)  2.99.0  2.98.0  2.97.0  2.95.0  2.92.0  2.91.0  2.89.0  2.87.0  2.86.0  2.85.0  2.84.0  2.82.0  2.80.0  2.79.0  2.78.0  2.77.0  2.76.0  2.74.0  2.72.0  2.71.0  2.68.0  2.67.0  2.66.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.5  2.6.2  2.5.1  2.4.3  2.3.1  2.2.1  2.1.9 
    
    
    public static interface Document.StyleOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBackgroundColor()
    
    
    public abstract Color getBackgroundColor()

Text background color.

`.google.type.Color background_color = 3;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Color` | The backgroundColor.  
  
### getBackgroundColorOrBuilder()
    
    
    public abstract ColorOrBuilder getBackgroundColorOrBuilder()

Text background color.

`.google.type.Color background_color = 3;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.ColorOrBuilder` |   
  
### getColor()
    
    
    public abstract Color getColor()

Text color.

`.google.type.Color color = 2;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Color` | The color.  
  
### getColorOrBuilder()
    
    
    public abstract ColorOrBuilder getColorOrBuilder()

Text color.

`.google.type.Color color = 2;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.ColorOrBuilder` |   
  
### getFontFamily()
    
    
    public abstract String getFontFamily()

Font family such as `Arial`, `Times New Roman`. <https://www.w3schools.com/cssref/pr_font_font-family.asp>

`string font_family = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The fontFamily.  
  
### getFontFamilyBytes()
    
    
    public abstract ByteString getFontFamilyBytes()

Font family such as `Arial`, `Times New Roman`. <https://www.w3schools.com/cssref/pr_font_font-family.asp>

`string font_family = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for fontFamily.  
  
### getFontSize()
    
    
    public abstract Document.Style.FontSize getFontSize()

Font size.

`.google.cloud.documentai.v1beta3.Document.Style.FontSize font_size = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Document.Style.FontSize](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Document.Style.FontSize)` | The fontSize.  
  
### getFontSizeOrBuilder()
    
    
    public abstract Document.Style.FontSizeOrBuilder getFontSizeOrBuilder()

Font size.

`.google.cloud.documentai.v1beta3.Document.Style.FontSize font_size = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Document.Style.FontSizeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Document.Style.FontSizeOrBuilder)` |   
  
### getFontWeight()
    
    
    public abstract String getFontWeight()

[Font weight](https://www.w3schools.com/cssref/pr_font_weight.asp). Possible values are `normal`, `bold`, `bolder`, and `lighter`.

`string font_weight = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The fontWeight.  
  
### getFontWeightBytes()
    
    
    public abstract ByteString getFontWeightBytes()

[Font weight](https://www.w3schools.com/cssref/pr_font_weight.asp). Possible values are `normal`, `bold`, `bolder`, and `lighter`.

`string font_weight = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for fontWeight.  
  
### getTextAnchor()
    
    
    public abstract Document.TextAnchor getTextAnchor()

Text anchor indexing into the Document.text.

`.google.cloud.documentai.v1beta3.Document.TextAnchor text_anchor = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Document.TextAnchor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Document.TextAnchor)` | The textAnchor.  
  
### getTextAnchorOrBuilder()
    
    
    public abstract Document.TextAnchorOrBuilder getTextAnchorOrBuilder()

Text anchor indexing into the Document.text.

`.google.cloud.documentai.v1beta3.Document.TextAnchor text_anchor = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Document.TextAnchorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Document.TextAnchorOrBuilder)` |   
  
### getTextDecoration()
    
    
    public abstract String getTextDecoration()

[Text decoration](https://www.w3schools.com/cssref/pr_text_text-decoration.asp). Follows CSS standard. <text-decoration-line> <text-decoration-color> <text-decoration-style>

`string text_decoration = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The textDecoration.  
  
### getTextDecorationBytes()
    
    
    public abstract ByteString getTextDecorationBytes()

[Text decoration](https://www.w3schools.com/cssref/pr_text_text-decoration.asp). Follows CSS standard. <text-decoration-line> <text-decoration-color> <text-decoration-style>

`string text_decoration = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for textDecoration.  
  
### getTextStyle()
    
    
    public abstract String getTextStyle()

[Text style](https://www.w3schools.com/cssref/pr_font_font-style.asp). Possible values are `normal`, `italic`, and `oblique`.

`string text_style = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The textStyle.  
  
### getTextStyleBytes()
    
    
    public abstract ByteString getTextStyleBytes()

[Text style](https://www.w3schools.com/cssref/pr_font_font-style.asp). Possible values are `normal`, `italic`, and `oblique`.

`string text_style = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for textStyle.  
  
### hasBackgroundColor()
    
    
    public abstract boolean hasBackgroundColor()

Text background color.

`.google.type.Color background_color = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the backgroundColor field is set.  
  
### hasColor()
    
    
    public abstract boolean hasColor()

Text color.

`.google.type.Color color = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the color field is set.  
  
### hasFontSize()
    
    
    public abstract boolean hasFontSize()

Font size.

`.google.cloud.documentai.v1beta3.Document.Style.FontSize font_size = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fontSize field is set.  
  
### hasTextAnchor()
    
    
    public abstract boolean hasTextAnchor()

Text anchor indexing into the Document.text.

`.google.cloud.documentai.v1beta3.Document.TextAnchor text_anchor = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the textAnchor field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

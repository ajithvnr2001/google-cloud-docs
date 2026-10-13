---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.LayoutOrBuilder
title: Interface Document.Page.LayoutOrBuilder (2.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:01.689311+00:00
---

# Interface Document.Page.LayoutOrBuilder (2.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.LayoutOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Document.Page.LayoutOrBuilder (2.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.103.0 (latest)  2.99.0  2.98.0  2.97.0  2.95.0  2.92.0  2.91.0  2.89.0  2.87.0  2.86.0  2.85.0  2.84.0  2.82.0  2.80.0  2.79.0  2.78.0  2.77.0  2.76.0  2.74.0  2.72.0  2.71.0  2.68.0  2.67.0  2.66.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.5  2.6.2  2.5.1  2.4.3  2.3.1  2.2.1  2.1.9 
    
    
    public static interface Document.Page.LayoutOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBoundingPoly()
    
    
    public abstract BoundingPoly getBoundingPoly()

The bounding polygon for the Layout.

`.google.cloud.documentai.v1.BoundingPoly bounding_poly = 3;`

**Returns**  
---  
**Type** | **Description**  
`[BoundingPoly](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BoundingPoly)` | The boundingPoly.  
  
### getBoundingPolyOrBuilder()
    
    
    public abstract BoundingPolyOrBuilder getBoundingPolyOrBuilder()

The bounding polygon for the Layout.

`.google.cloud.documentai.v1.BoundingPoly bounding_poly = 3;`

**Returns**  
---  
**Type** | **Description**  
`[BoundingPolyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BoundingPolyOrBuilder)` |   
  
### getConfidence()
    
    
    public abstract float getConfidence()

Confidence of the current Layout within context of the object this layout is for. For example, confidence can be for a single token, a table, a visual element, etc. depending on context. Range `[0, 1]`.

`float confidence = 2;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The confidence.  
  
### getOrientation()
    
    
    public abstract Document.Page.Layout.Orientation getOrientation()

Detected orientation for the Layout.

`.google.cloud.documentai.v1.Document.Page.Layout.Orientation orientation = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Document.Page.Layout.Orientation](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Layout.Orientation)` | The orientation.  
  
### getOrientationValue()
    
    
    public abstract int getOrientationValue()

Detected orientation for the Layout.

`.google.cloud.documentai.v1.Document.Page.Layout.Orientation orientation = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for orientation.  
  
### getTextAnchor()
    
    
    public abstract Document.TextAnchor getTextAnchor()

Text anchor indexing into the Document.text.

`.google.cloud.documentai.v1.Document.TextAnchor text_anchor = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Document.TextAnchor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.TextAnchor)` | The textAnchor.  
  
### getTextAnchorOrBuilder()
    
    
    public abstract Document.TextAnchorOrBuilder getTextAnchorOrBuilder()

Text anchor indexing into the Document.text.

`.google.cloud.documentai.v1.Document.TextAnchor text_anchor = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Document.TextAnchorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.TextAnchorOrBuilder)` |   
  
### hasBoundingPoly()
    
    
    public abstract boolean hasBoundingPoly()

The bounding polygon for the Layout.

`.google.cloud.documentai.v1.BoundingPoly bounding_poly = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the boundingPoly field is set.  
  
### hasTextAnchor()
    
    
    public abstract boolean hasTextAnchor()

Text anchor indexing into the Document.text.

`.google.cloud.documentai.v1.Document.TextAnchor text_anchor = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the textAnchor field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

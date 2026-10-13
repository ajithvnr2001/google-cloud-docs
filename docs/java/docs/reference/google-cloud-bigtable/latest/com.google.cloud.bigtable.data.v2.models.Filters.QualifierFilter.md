---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Filters.QualifierFilter
title: Class Filters.QualifierFilter (2.85.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:24.025862+00:00
---

# Class Filters.QualifierFilter (2.85.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Filters.QualifierFilter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Filters.QualifierFilter (2.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.85.0 (latest)  2.81.0  2.80.0  2.79.0  2.78.1  2.77.0  2.74.0  2.73.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.1  2.66.0  2.65.1  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.2  2.56.0  2.54.0  2.52.0  2.51.2  2.49.0  2.46.0  2.45.1  2.44.1  2.43.0  2.42.0  2.40.0  2.39.5  2.37.0  2.35.1  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0 
    
    
    public static final class Filters.QualifierFilter implements Serializable

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Filters.QualifierFilter

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### exactMatch(ByteString value)
    
    
    public Filters.Filter exactMatch(ByteString value)

Matches only cells from columns whose qualifiers equal the value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Filters.Filter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Filters.Filter)` |   
  
### exactMatch(String value)
    
    
    public Filters.Filter exactMatch(String value)

Matches only cells from columns whose qualifiers equal the value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Filters.Filter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Filters.Filter)` |   
  
### rangeWithinFamily(String family)
    
    
    public Filters.QualifierRangeFilter rangeWithinFamily(String family)

Construct a QualifierRangeFilter that can create a ColumnRange oriented Filter.

**Parameter**  
---  
**Name** | **Description**  
`family` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Filters.QualifierRangeFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Filters.QualifierRangeFilter)` | a new QualifierRangeFilter  
  
### regex(ByteString regex)
    
    
    public Filters.Filter regex(ByteString regex)

Matches only cells from columns whose qualifiers satisfy the given [RE2 regex](https://github.com/google/re2/wiki/Syntax). Note that, since column qualifiers can contain arbitrary bytes, the `C` escape sequence must be used if a true wildcard is desired. The `.` character will not match the new line character ` `, which may be present in a binary qualifier.

**Parameter**  
---  
**Name** | **Description**  
`regex` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Filters.Filter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Filters.Filter)` |   
  
### regex(String regex)
    
    
    public Filters.Filter regex(String regex)

Matches only cells from columns whose qualifiers satisfy the given [RE2 regex](https://github.com/google/re2/wiki/Syntax). Note that, since column qualifiers can contain arbitrary bytes, the `C` escape sequence must be used if a true wildcard is desired. The `.` character will not match the new line character ` `, which may be present in a binary qualifier.

**Parameter**  
---  
**Name** | **Description**  
`regex` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Filters.Filter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Filters.Filter)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

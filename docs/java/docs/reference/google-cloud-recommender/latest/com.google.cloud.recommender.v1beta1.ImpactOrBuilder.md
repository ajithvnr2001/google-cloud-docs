---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.ImpactOrBuilder
title: Interface ImpactOrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:34.780337+00:00
---

# Interface ImpactOrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.ImpactOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ImpactOrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.7  2.4.1  2.3.0  2.2.0  2.1.5 
    
    
    public interface ImpactOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCategory()
    
    
    public abstract Impact.Category getCategory()

Category that is being targeted.

`.google.cloud.recommender.v1beta1.Impact.Category category = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Impact.Category](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.Impact.Category)` | The category.  
  
### getCategoryValue()
    
    
    public abstract int getCategoryValue()

Category that is being targeted.

`.google.cloud.recommender.v1beta1.Impact.Category category = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for category.  
  
### getCostProjection()
    
    
    public abstract CostProjection getCostProjection()

Use with CategoryType.COST

`.google.cloud.recommender.v1beta1.CostProjection cost_projection = 100;`

**Returns**  
---  
**Type** | **Description**  
`[CostProjection](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.CostProjection)` | The costProjection.  
  
### getCostProjectionOrBuilder()
    
    
    public abstract CostProjectionOrBuilder getCostProjectionOrBuilder()

Use with CategoryType.COST

`.google.cloud.recommender.v1beta1.CostProjection cost_projection = 100;`

**Returns**  
---  
**Type** | **Description**  
`[CostProjectionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.CostProjectionOrBuilder)` |   
  
### getProjectionCase()
    
    
    public abstract Impact.ProjectionCase getProjectionCase()

**Returns**  
---  
**Type** | **Description**  
`[Impact.ProjectionCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.Impact.ProjectionCase)` |   
  
### getSecurityProjection()
    
    
    public abstract SecurityProjection getSecurityProjection()

Use with CategoryType.SECURITY

`.google.cloud.recommender.v1beta1.SecurityProjection security_projection = 101;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityProjection](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.SecurityProjection)` | The securityProjection.  
  
### getSecurityProjectionOrBuilder()
    
    
    public abstract SecurityProjectionOrBuilder getSecurityProjectionOrBuilder()

Use with CategoryType.SECURITY

`.google.cloud.recommender.v1beta1.SecurityProjection security_projection = 101;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityProjectionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.SecurityProjectionOrBuilder)` |   
  
### getSustainabilityProjection()
    
    
    public abstract SustainabilityProjection getSustainabilityProjection()

Use with CategoryType.SUSTAINABILITY

` .google.cloud.recommender.v1beta1.SustainabilityProjection sustainability_projection = 102; `

**Returns**  
---  
**Type** | **Description**  
`[SustainabilityProjection](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.SustainabilityProjection)` | The sustainabilityProjection.  
  
### getSustainabilityProjectionOrBuilder()
    
    
    public abstract SustainabilityProjectionOrBuilder getSustainabilityProjectionOrBuilder()

Use with CategoryType.SUSTAINABILITY

` .google.cloud.recommender.v1beta1.SustainabilityProjection sustainability_projection = 102; `

**Returns**  
---  
**Type** | **Description**  
`[SustainabilityProjectionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.SustainabilityProjectionOrBuilder)` |   
  
### hasCostProjection()
    
    
    public abstract boolean hasCostProjection()

Use with CategoryType.COST

`.google.cloud.recommender.v1beta1.CostProjection cost_projection = 100;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the costProjection field is set.  
  
### hasSecurityProjection()
    
    
    public abstract boolean hasSecurityProjection()

Use with CategoryType.SECURITY

`.google.cloud.recommender.v1beta1.SecurityProjection security_projection = 101;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the securityProjection field is set.  
  
### hasSustainabilityProjection()
    
    
    public abstract boolean hasSustainabilityProjection()

Use with CategoryType.SUSTAINABILITY

` .google.cloud.recommender.v1beta1.SustainabilityProjection sustainability_projection = 102; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sustainabilityProjection field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

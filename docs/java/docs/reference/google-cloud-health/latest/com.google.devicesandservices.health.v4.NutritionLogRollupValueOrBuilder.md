---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValueOrBuilder
title: Interface NutritionLogRollupValueOrBuilder (0.8.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:16.921347+00:00
---

# Interface NutritionLogRollupValueOrBuilder (0.8.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValueOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface NutritionLogRollupValueOrBuilder (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.0 (latest)  0.4.0  0.3.0  0.2.0 
    
    
    public interface NutritionLogRollupValueOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEnergy()
    
    
    public abstract NutritionLogRollupValue.EnergyQuantityRollup getEnergy()

Energy rollup.

` .google.devicesandservices.health.v4.NutritionLogRollupValue.EnergyQuantityRollup energy = 2; `

**Returns**  
---  
**Type** | **Description**  
`[NutritionLogRollupValue.EnergyQuantityRollup](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue.EnergyQuantityRollup)` | The energy.  
  
### getEnergyFromFat()
    
    
    public abstract NutritionLogRollupValue.EnergyQuantityRollup getEnergyFromFat()

Value Energy from fat rollup.

` .google.devicesandservices.health.v4.NutritionLogRollupValue.EnergyQuantityRollup energy_from_fat = 3; `

**Returns**  
---  
**Type** | **Description**  
`[NutritionLogRollupValue.EnergyQuantityRollup](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue.EnergyQuantityRollup)` | The energyFromFat.  
  
### getEnergyFromFatOrBuilder()
    
    
    public abstract NutritionLogRollupValue.EnergyQuantityRollupOrBuilder getEnergyFromFatOrBuilder()

Value Energy from fat rollup.

` .google.devicesandservices.health.v4.NutritionLogRollupValue.EnergyQuantityRollup energy_from_fat = 3; `

**Returns**  
---  
**Type** | **Description**  
`[NutritionLogRollupValue.EnergyQuantityRollupOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue.EnergyQuantityRollupOrBuilder)` |   
  
### getEnergyOrBuilder()
    
    
    public abstract NutritionLogRollupValue.EnergyQuantityRollupOrBuilder getEnergyOrBuilder()

Energy rollup.

` .google.devicesandservices.health.v4.NutritionLogRollupValue.EnergyQuantityRollup energy = 2; `

**Returns**  
---  
**Type** | **Description**  
`[NutritionLogRollupValue.EnergyQuantityRollupOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue.EnergyQuantityRollupOrBuilder)` |   
  
### getNutrients(int index)
    
    
    public abstract NutritionLogRollupValue.NutrientQuantityRollup getNutrients(int index)

List of the nutrient roll-ups by the nutrient type.

` repeated .google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollup nutrients = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NutritionLogRollupValue.NutrientQuantityRollup](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollup)` |   
  
### getNutrientsCount()
    
    
    public abstract int getNutrientsCount()

List of the nutrient roll-ups by the nutrient type.

` repeated .google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollup nutrients = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNutrientsList()
    
    
    public abstract List<NutritionLogRollupValue.NutrientQuantityRollup> getNutrientsList()

List of the nutrient roll-ups by the nutrient type.

` repeated .google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollup nutrients = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[NutrientQuantityRollup](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollup)>` |   
  
### getNutrientsOrBuilder(int index)
    
    
    public abstract NutritionLogRollupValue.NutrientQuantityRollupOrBuilder getNutrientsOrBuilder(int index)

List of the nutrient roll-ups by the nutrient type.

` repeated .google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollup nutrients = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NutritionLogRollupValue.NutrientQuantityRollupOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollupOrBuilder)` |   
  
### getNutrientsOrBuilderList()
    
    
    public abstract List<? extends NutritionLogRollupValue.NutrientQuantityRollupOrBuilder> getNutrientsOrBuilderList()

List of the nutrient roll-ups by the nutrient type.

` repeated .google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollup nutrients = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.devicesandservices.health.v4.NutritionLogRollupValue.NutrientQuantityRollupOrBuilder>` |   
  
### getTotalCarbohydrate()
    
    
    public abstract NutritionLogRollupValue.WeightQuantityRollup getTotalCarbohydrate()

Total carbohydrate rollup.

` .google.devicesandservices.health.v4.NutritionLogRollupValue.WeightQuantityRollup total_carbohydrate = 4; `

**Returns**  
---  
**Type** | **Description**  
`[NutritionLogRollupValue.WeightQuantityRollup](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue.WeightQuantityRollup)` | The totalCarbohydrate.  
  
### getTotalCarbohydrateOrBuilder()
    
    
    public abstract NutritionLogRollupValue.WeightQuantityRollupOrBuilder getTotalCarbohydrateOrBuilder()

Total carbohydrate rollup.

` .google.devicesandservices.health.v4.NutritionLogRollupValue.WeightQuantityRollup total_carbohydrate = 4; `

**Returns**  
---  
**Type** | **Description**  
`[NutritionLogRollupValue.WeightQuantityRollupOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue.WeightQuantityRollupOrBuilder)` |   
  
### getTotalFat()
    
    
    public abstract NutritionLogRollupValue.WeightQuantityRollup getTotalFat()

Total fat rollup.

` .google.devicesandservices.health.v4.NutritionLogRollupValue.WeightQuantityRollup total_fat = 5; `

**Returns**  
---  
**Type** | **Description**  
`[NutritionLogRollupValue.WeightQuantityRollup](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue.WeightQuantityRollup)` | The totalFat.  
  
### getTotalFatOrBuilder()
    
    
    public abstract NutritionLogRollupValue.WeightQuantityRollupOrBuilder getTotalFatOrBuilder()

Total fat rollup.

` .google.devicesandservices.health.v4.NutritionLogRollupValue.WeightQuantityRollup total_fat = 5; `

**Returns**  
---  
**Type** | **Description**  
`[NutritionLogRollupValue.WeightQuantityRollupOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue.WeightQuantityRollupOrBuilder)` |   
  
### hasEnergy()
    
    
    public abstract boolean hasEnergy()

Energy rollup.

` .google.devicesandservices.health.v4.NutritionLogRollupValue.EnergyQuantityRollup energy = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the energy field is set.  
  
### hasEnergyFromFat()
    
    
    public abstract boolean hasEnergyFromFat()

Value Energy from fat rollup.

` .google.devicesandservices.health.v4.NutritionLogRollupValue.EnergyQuantityRollup energy_from_fat = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the energyFromFat field is set.  
  
### hasTotalCarbohydrate()
    
    
    public abstract boolean hasTotalCarbohydrate()

Total carbohydrate rollup.

` .google.devicesandservices.health.v4.NutritionLogRollupValue.WeightQuantityRollup total_carbohydrate = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the totalCarbohydrate field is set.  
  
### hasTotalFat()
    
    
    public abstract boolean hasTotalFat()

Total fat rollup.

` .google.devicesandservices.health.v4.NutritionLogRollupValue.WeightQuantityRollup total_fat = 5; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the totalFat field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

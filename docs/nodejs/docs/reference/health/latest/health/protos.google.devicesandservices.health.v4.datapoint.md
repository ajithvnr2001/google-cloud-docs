---
url: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datapoint
title: Class protos.google.devicesandservices.health.v4.DataPoint (0.8.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:12.566299+00:00
---

# Class protos.google.devicesandservices.health.v4.DataPoint (0.8.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datapoint

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devicesandservices.health.v4.DataPoint (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a DataPoint.

## Implements

[protos.google.devicesandservices.health.v4.IDataPoint](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idatapoint)

## Package

[@google-cloud/health](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.devicesandservices.health.v4.IDataPoint);

Constructs a new DataPoint.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataPoint](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idatapoint)`   
Properties to set  
  
## Properties 

### activeEnergyBurned
    
    
    public activeEnergyBurned?: (google.devicesandservices.health.v4.IActiveEnergyBurned|null);

DataPoint activeEnergyBurned.

### activeMinutes
    
    
    public activeMinutes?: (google.devicesandservices.health.v4.IActiveMinutes|null);

DataPoint activeMinutes.

### activeZoneMinutes
    
    
    public activeZoneMinutes?: (google.devicesandservices.health.v4.IActiveZoneMinutes|null);

DataPoint activeZoneMinutes.

### activityLevel
    
    
    public activityLevel?: (google.devicesandservices.health.v4.IActivityLevel|null);

DataPoint activityLevel.

### altitude
    
    
    public altitude?: (google.devicesandservices.health.v4.IAltitude|null);

DataPoint altitude.

### basalEnergyBurned
    
    
    public basalEnergyBurned?: (google.devicesandservices.health.v4.IBasalEnergyBurned|null);

DataPoint basalEnergyBurned.

### bloodGlucose
    
    
    public bloodGlucose?: (google.devicesandservices.health.v4.IBloodGlucose|null);

DataPoint bloodGlucose.

### bodyFat
    
    
    public bodyFat?: (google.devicesandservices.health.v4.IBodyFat|null);

DataPoint bodyFat.

### coreBodyTemperature
    
    
    public coreBodyTemperature?: (google.devicesandservices.health.v4.ICoreBodyTemperature|null);

DataPoint coreBodyTemperature.

### dailyHeartRateVariability
    
    
    public dailyHeartRateVariability?: (google.devicesandservices.health.v4.IDailyHeartRateVariability|null);

DataPoint dailyHeartRateVariability.

### dailyHeartRateZones
    
    
    public dailyHeartRateZones?: (google.devicesandservices.health.v4.IDailyHeartRateZones|null);

DataPoint dailyHeartRateZones.

### dailyOxygenSaturation
    
    
    public dailyOxygenSaturation?: (google.devicesandservices.health.v4.IDailyOxygenSaturation|null);

DataPoint dailyOxygenSaturation.

### dailyRespiratoryRate
    
    
    public dailyRespiratoryRate?: (google.devicesandservices.health.v4.IDailyRespiratoryRate|null);

DataPoint dailyRespiratoryRate.

### dailyRestingHeartRate
    
    
    public dailyRestingHeartRate?: (google.devicesandservices.health.v4.IDailyRestingHeartRate|null);

DataPoint dailyRestingHeartRate.

### dailySleepTemperatureDerivations
    
    
    public dailySleepTemperatureDerivations?: (google.devicesandservices.health.v4.IDailySleepTemperatureDerivations|null);

DataPoint dailySleepTemperatureDerivations.

### dailyVo2Max
    
    
    public dailyVo2Max?: (google.devicesandservices.health.v4.IDailyVO2Max|null);

DataPoint dailyVo2Max.

### data
    
    
    public data?: ("steps"|"floors"|"heartRate"|"sleep"|"dailyRestingHeartRate"|"dailyHeartRateVariability"|"exercise"|"weight"|"altitude"|"distance"|"bodyFat"|"activeZoneMinutes"|"heartRateVariability"|"dailySleepTemperatureDerivations"|"sedentaryPeriod"|"runVo2Max"|"oxygenSaturation"|"dailyOxygenSaturation"|"activityLevel"|"vo2Max"|"dailyVo2Max"|"nutritionLog"|"irregularRhythmNotification"|"electrocardiogram"|"dailyHeartRateZones"|"hydrationLog"|"food"|"timeInHeartRateZone"|"activeMinutes"|"respiratoryRateSleepSummary"|"dailyRespiratoryRate"|"swimLengthsData"|"height"|"basalEnergyBurned"|"coreBodyTemperature"|"activeEnergyBurned"|"foodMeasurementUnit"|"bloodGlucose"|"menstrualPeriod"|"ovulationTest"|"symptoms"|"moods");

DataPoint data.

### dataSource
    
    
    public dataSource?: (google.devicesandservices.health.v4.IDataSource|null);

DataPoint dataSource.

### distance
    
    
    public distance?: (google.devicesandservices.health.v4.IDistance|null);

DataPoint distance.

### electrocardiogram
    
    
    public electrocardiogram?: (google.devicesandservices.health.v4.IElectrocardiogram|null);

DataPoint electrocardiogram.

### exercise
    
    
    public exercise?: (google.devicesandservices.health.v4.IExercise|null);

DataPoint exercise.

### floors
    
    
    public floors?: (google.devicesandservices.health.v4.IFloors|null);

DataPoint floors.

### food
    
    
    public food?: (google.devicesandservices.health.v4.IFood|null);

DataPoint food.

### foodMeasurementUnit
    
    
    public foodMeasurementUnit?: (google.devicesandservices.health.v4.IFoodMeasurementUnit|null);

DataPoint foodMeasurementUnit.

### heartRate
    
    
    public heartRate?: (google.devicesandservices.health.v4.IHeartRate|null);

DataPoint heartRate.

### heartRateVariability
    
    
    public heartRateVariability?: (google.devicesandservices.health.v4.IHeartRateVariability|null);

DataPoint heartRateVariability.

### height
    
    
    public height?: (google.devicesandservices.health.v4.IHeight|null);

DataPoint height.

### hydrationLog
    
    
    public hydrationLog?: (google.devicesandservices.health.v4.IHydrationLog|null);

DataPoint hydrationLog.

### irregularRhythmNotification
    
    
    public irregularRhythmNotification?: (google.devicesandservices.health.v4.IIrregularRhythmNotification|null);

DataPoint irregularRhythmNotification.

### menstrualPeriod
    
    
    public menstrualPeriod?: (google.devicesandservices.health.v4.IMenstrualPeriod|null);

DataPoint menstrualPeriod.

### moods
    
    
    public moods?: (google.devicesandservices.health.v4.IMoods|null);

DataPoint moods.

### name
    
    
    public name: string;

DataPoint name.

### nutritionLog
    
    
    public nutritionLog?: (google.devicesandservices.health.v4.INutritionLog|null);

DataPoint nutritionLog.

### ovulationTest
    
    
    public ovulationTest?: (google.devicesandservices.health.v4.IOvulationTest|null);

DataPoint ovulationTest.

### oxygenSaturation
    
    
    public oxygenSaturation?: (google.devicesandservices.health.v4.IOxygenSaturation|null);

DataPoint oxygenSaturation.

### respiratoryRateSleepSummary
    
    
    public respiratoryRateSleepSummary?: (google.devicesandservices.health.v4.IRespiratoryRateSleepSummary|null);

DataPoint respiratoryRateSleepSummary.

### runVo2Max
    
    
    public runVo2Max?: (google.devicesandservices.health.v4.IRunVO2Max|null);

DataPoint runVo2Max.

### sedentaryPeriod
    
    
    public sedentaryPeriod?: (google.devicesandservices.health.v4.ISedentaryPeriod|null);

DataPoint sedentaryPeriod.

### sleep
    
    
    public sleep?: (google.devicesandservices.health.v4.ISleep|null);

DataPoint sleep.

### steps
    
    
    public steps?: (google.devicesandservices.health.v4.ISteps|null);

DataPoint steps.

### swimLengthsData
    
    
    public swimLengthsData?: (google.devicesandservices.health.v4.ISwimLengthsData|null);

DataPoint swimLengthsData.

### symptoms
    
    
    public symptoms?: (google.devicesandservices.health.v4.ISymptoms|null);

DataPoint symptoms.

### timeInHeartRateZone
    
    
    public timeInHeartRateZone?: (google.devicesandservices.health.v4.ITimeInHeartRateZone|null);

DataPoint timeInHeartRateZone.

### vo2Max
    
    
    public vo2Max?: (google.devicesandservices.health.v4.IVO2Max|null);

DataPoint vo2Max.

### weight
    
    
    public weight?: (google.devicesandservices.health.v4.IWeight|null);

DataPoint weight.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.devicesandservices.health.v4.IDataPoint): google.devicesandservices.health.v4.DataPoint;

Creates a new DataPoint instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataPoint](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idatapoint)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DataPoint](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datapoint)` | DataPoint instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.devicesandservices.health.v4.DataPoint;

Decodes a DataPoint message from the specified reader or buffer.

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
`[DataPoint](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datapoint)` | DataPoint  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.devicesandservices.health.v4.DataPoint;

Decodes a DataPoint message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DataPoint](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datapoint)` | DataPoint  
  
### encode(message, writer)
    
    
    public static encode(message: google.devicesandservices.health.v4.IDataPoint, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataPoint message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataPoint](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idatapoint)`   
DataPoint message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.devicesandservices.health.v4.IDataPoint, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataPoint message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataPoint](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idatapoint)`   
DataPoint message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.devicesandservices.health.v4.DataPoint;

Creates a DataPoint message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DataPoint](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datapoint)` | DataPoint  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DataPoint

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

Converts this DataPoint to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.devicesandservices.health.v4.DataPoint, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DataPoint message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DataPoint](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datapoint)`   
DataPoint  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DataPoint message.

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

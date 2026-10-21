---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/access/how-to-query-in-fed-api/
title: Query using Federation API \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:39.644984+00:00
---

# Query using Federation API  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/access/how-to-query-in-fed-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query using Federation API

This guide explains how to query data in Manufacturing Data Engine (MDE) using Federation API for typical use-cases.

Federation provides access to parts of the configuration data, data stored in BigQuery or Bigtable.

To use Federation API to query data in Bigtable make sure you have deployed MDE with the correct "size". For more information, see [the sizes section](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/sizes) and choose a size that deploys the required Dataflow writer job as well as a Bigtable instance. Typically, anything larger than `Pilot` includes the required dependencies.

## Introduction

The Federation API is a typical REST API that return JSON structures. To access the API either use the MDE proxy or expose using Identity-Aware Proxy.

The data available through the API are the following:

Available Data | API root path using tunnel  
---|---  
Get records from BigLake | `/data/v1/bigquery`  
Get records from Bigtable | `/data/v1/bigtable`  
Get metadata instance from Metadata Manager | `/data/v1/metadata`  
Get types and tags from Config Manager | `/data/v1/config`  
  
In some cases attribute name are abbreviated to ensure proper performance when transferring large JSON payloads across the network. It is possible to include a headers section in the response that explains the abbreviations.

General query parameters use across the different parts of the API are:

Query parameter | Description  
---|---  
`includeMetrics` | Metrics related to the queries are included in the response.  
`includeHeader` | A header is included in the response with explanation of abbreviation and response statistics.  
`includeMetadata` | When returning records this specifies whether or not to include metadata fields in the response. This can substantially increase the size of the response are might not be needed.  
`nextPageToken` | If more data is available than returned a nextPageToken is returned that can be provided in the next request to get the next page. For Bigtable nextPageToken is always provided as there is not way to know if there are more records available or not.  
`includeIds` | Include row ids and source message ids.  
  
The following is a sample request with three of the query param included:
    
    
    GET http://localhost:8080/data/v1/bigquery/records/primepaintingrobot-01-airhumidity/default-numeric-records/latest?includeMetrics=true&includeHeader=true&includeMetadata=true
    

A sample response with the three query param included would look similar the following example:
    
    
    {
      "header": {
        "startTime": "1691060884507",
        "endTime": "1691060884507",
        "tagCount": 1,
        "dataRecordCount": 1,
        "dataFields": {
          "d": "duration",
          "dp": "discretePayload",
          "cp": "continuousPayload",
          "its": "ingestTimestamp",
          "cmr": "cloudMetadataRef",
          "sdi": "sourceMessageId",
          "np": "numericPayload",
          "id": "id",
          "v": "value",
          "em": "embeddedMetadata",
          "et": "eventTimestampEnd",
          "mcm": "materializedCloudMetadata",
          "t": "eventTimestamp",
          "st": "eventTimestampStart"
        }
      },
      "tags": [
        {
          "tagName": "primepaintingrobot-01-airhumidity",
          "data": [
            {
              "t": "1691060884507000",
              "np": {
                "v": 80.7
              },
              "em": "{\"datatype\":\"float\",\"description\":\"This is a fake prime painting robot on NodeRed\",\"deviceID\":\"75c18751-7a94-453e-86f5-67be2b0c8fd4\",\"deviceName\":\"primepaintingrobot-01\",\"headers\":{},\"messageClassName\":\"default-numeric-value\",\"metadata\":{\"brand\":\"Philips\",\"measurementUnit\":\"percentage\",\"sensorType\":\"humidity\",\"shift\":\"Shift 4\"},\"registerId\":\"a2635b62-0e89-40ff-b172-13eea37a92c2\",\"success\":true,\"unit\":\"percentage\"}",
              "mcm": "{}",
              "cmr": "{}"
            }
          ],
          "typeName": "default-numeric-records"
        }
      ],
      "metrics": {
        "totalTimeMS": 2766
      }
    }
    

The API supports server-side downsampling. To use this feature, specify a downsampling interval in the format:`sample=Duration,Unit,Aggregation`

For example: `sample=[10,MINUTE,MEAN]`

Allowed parameters:

  * `Duration`: `Int` \- An integer representing the downsampling interval.
  * `Unit`: `{SECOND, MINUTE, HOUR}` \- The time unit for the interval.
  * `Aggregation`: `{MEAN, SUM,MAX, MIN, COUNT}` \- The aggregation function to apply.



Downsampling is available for data from both Bigtable and Bigtable. Available aggregation types also depends on the Archetype.

## Get records from BigQuery

The following is a sample request to get latest record for a number of tags with type combination from BigQuery:
    
    
    GET http://localhost:8080/data/v1/bigquery/records/default-numeric-records?tags=station-a-powerusage,station-b-powerusage&startTimestamp=1691057738790&endTimestamp=1691061338790&pageSize=100
    

A sample response would look similar to the following:
    
    
    {
      "header": {
        "startTime": "1691061786759",
        "endTime": "1691061786759",
        "tagCount": 1,
        "dataRecordCount": 1,
        "dataFields": {
          "d": "duration",
          "dp": "discretePayload",
          "cp": "continuousPayload",
          "its": "ingestTimestamp",
          "cmr": "cloudMetadataRef",
          "sdi": "sourceMessageId",
          "np": "numericPayload",
          "id": "id",
          "v": "value",
          "em": "embeddedMetadata",
          "et": "eventTimestampEnd",
          "mcm": "materializedCloudMetadata",
          "t": "eventTimestamp",
          "st": "eventTimestampStart"
        }
      },
      "tags": [
        {
          "tagName": "primepaintingrobot-01-airhumidity",
          "data": [
            {
              "t": "1691061786759000",
              "np": {
                "v": 81.79
              },
              "em": "{\"datatype\":\"float\",\"description\":\"This is a fake prime painting robot on NodeRed\",\"deviceID\":\"75c18751-7a94-453e-86f5-67be2b0c8fd4\",\"deviceName\":\"primepaintingrobot-01\",\"headers\":{},\"messageClassName\":\"default-numeric-value\",\"metadata\":{\"brand\":\"Philips\",\"measurementUnit\":\"percentage\",\"sensorType\":\"humidity\",\"shift\":\"Shift 4\"},\"registerId\":\"a2635b62-0e89-40ff-b172-13eea37a92c2\",\"success\":true,\"unit\":\"percentage\"}",
              "mcm": "{}",
              "cmr": "{}"
            }
          ],
          "typeName": "default-numeric-records"
        }
      ],
      "metrics": {
        "totalTimeMS": 2371
      }
    }
    

The following is a sample request to retrieve records for specific tags, type combination, and start and end time ranges from BigQuery:
    
    
    GET http://localhost:8080/data/v1/bigquery/records/default-numeric-records?tags=station-a-powerusage,station-b-powerusage&startTimestamp=1691057738790&endTimestamp=1691061338790&pageSize=100
    

A partial sample response would look similar to the following:
    
    
    {
       "tags": [
          {
             "tagName": "station-a-powerusage",
             "data": [
                {
                   "t": "1691061419653000",
                   "np": {
                      "v": 14.174
                   }
                },
                {
                   "t": "1691061418653000",
                   "np": {
                      "v": 17.979
                   }
                },
    

The following sample request gets records for a tags and type combination from BigQuery with downsampling (the minimum value for each five-minute window within the specified time range):
    
    
    GET http://localhost:8080/data/v1/bigquery/records/default-numeric-records?tags=station-a-powerusage,station-b-powerusage&startTimestamp=1691058375905&endTimestamp=1691061975905&pageSize=1000&sample=5,MINUTE,MIN
    

A sample response would look similar to the following:
    
    
    {
      "tags": [
        {
          "tagName": "station-a-powerusage",
          "data": [
            {
              "t": "1691061775669000",
              "agg": {
                "v": 12.019
              }
            },
            {
              "t": "1691061475669000",
              "agg": {
                "v": 12.022
              }
            }
          ]
        },
        {
          "tagName": "station-b-powerusage",
          "data": [
            {
              "t": "1691061775702000",
              "agg": {
                "v": 34.092
              }
            },
            {
              "t": "1691061475702000",
              "agg": {
                "v": 34.201
              }
            }
          ]
        }
      ],
      "nextPageToken": "LTU3NjUwMTA5OS4w"
    }
    

The following sample request gets records for a clustered type based on two clustered values from BigQuery:
    
    
    GET http://localhost:8080/data/v1/bigquery/clusteredrecords/clustered-energy-consumption-numeric-records?clusterColumnValues=DK,AAR&startTimestamp=1691062260871&endTimestamp=1691065860871
    

A partial sample response would look similar to the following:
    
    
    {
        "tags": [
            {
                "tagName": "energymonitor2-line-total-energy",
                "data": [
                    {
                        "t": "1691065853667000",
                        "np": {
                            "v": 15.148
                        }
                    },
    [...]
                  {
                    "tagName": "energymonitor6-line-total-energy",
                    "data": [
                      {
                        "t": "1691065853710000",
                        "np": {
                          "v": 15.015
                        }
                      },
                      {
                        "t": "1691065852710000",
                        "np": {
                          "v": 18.468
                        }
                      },
    [...]
    

The following sample request gets tags for a type:
    
    
    GET http://localhost:8080/data/v1/bigquery/tags/default-numeric-records?startTimestamp=1690942297865&endTimestamp=1691062297865&includeHeader=true
    

A partial sample response would look similar to the following:
    
    
    {
        "header": {
            "tagCount": 56,
            "dataRecordCount": 56,
            "dataFields": {
                "typeName": "typeName",
                "tagName": "tagName",
                "version": "typeVersion"
            }
        },
        "tags": [
            {
                "tagName": "sb01_d_voltage",
                "typeVersion": "1",
                "typeName": "default-numeric-records"
            },
            {
                "tagName": "JGC_001",
                "typeVersion": "1",
                "typeName": "default-numeric-records"
            },
    

## Get records from Bigtable

The following is a sample request to get records for a combination of tags, type, and a time range (start and end time) from Bigtable:
    
    
    GET http://localhost:8080/data/v1/bigtable/records/default-numeric-records?startTimestamp=1687462558476&endTimestamp=1691062558476&tags=clearcoatingrobot-01-airpressure,primepaintingrobot-01-airhumidity
    

A partial sample response would look similar to the following:
    
    
    {
       "tags": [
          {
             "tagName": "clearcoatingrobot-01-airpressure",
             "data": [
                {
                   "t": "1691062557069",
                   "np": {
                      "v": 757.18
                   }
                },
                {
                   "t": "1691062556068",
                   "np": {
                      "v": 763.71
                   }
                },
    

The following is a sample request to get latest record for a combination of a tag and a type combination from Bigtable:
    
    
    GET http://localhost:8080/data/v1/bigtable/records/clearcoatingrobot-01-airpressure/default-numeric-records/latest?includeHeader=true
    

A sample response would look similar to the following:
    
    
    {
      "header": {
        "startTime": "1691062700094",
        "endTime": "1691062700094",
        "tagCount": 1,
        "dataRecordCount": 1,
        "dataFields": {
          "d": "duration",
          "dp": "discretePayload",
          "cp": "continuousPayload",
          "its": "ingestTimestamp",
          "cmr": "cloudMetadataRef",
          "sdi": "sourceMessageId",
          "np": "numericPayload",
          "id": "id",
          "v": "value",
          "em": "embeddedMetadata",
          "et": "eventTimestampEnd",
          "mcm": "materializedCloudMetadata",
          "t": "eventTimestamp",
          "st": "eventTimestampStart"
        }
      },
      "tags": [
        {
          "tagName": "clearcoatingrobot-01-airpressure",
          "data": [
            {
              "t": "1691062700094",
              "np": {
                "v": 764.91
              }
            }
          ],
          "typeName": "default-numeric-records"
        }
      ]
    }
    

## Get metadata instance from metadata manager

The following is a sample request to get metadata instance from metadata manager:
    
    
    GET http://localhost:8080/data/v1/metadata/instances/41e9a32b-e85f-4a9a-a6a2-a3784855e859?includeHeader=true
    

A partial sample response would look similar to the following:
    
    
    {
      "header": {
        "dataFields": {
          "i": "instance",
          "bv": "bucketVersion",
          "bnam": "bucketName",
          "bnum": "bucketNumber",
          "nk": "naturalKey",
          "ct": "createdTimestamp",
          "iid": "instanceId"
        }
      },
      "metadataInstances": [
        {
          "iid": "41e9a32b-e85f-4a9a-a6a2-a3784855e859",
          "bnum": 357,
          "bnam": "source",
          "bv": 1,
          "nk": "mce",
          "i": "{\"source\":\"Manufacturing Connect edge\"}",
          "ct": "1689781556451"
        }
      ]
    }
    

## Get types and tags from Config Manager

The following is a sample request to get tags from Config Manager:
    
    
    GET http://localhost:8080/data/v1/config/tags?includeHeader=true&pageSize=10
    

A partial sample response would look similar to the following:
    
    
    {
      "header": {
        "tagCount": 10,
        "dataFields": {
          "types": "types",
          "createdTimestamp": "createdTimestamp",
          "tagName": "tagName",
          "id": "id"
        }
      },
      "tags": [
        {
          "id": "613db120-fed4-4584-a3b1-9468d7228edb",
          "tagName": "MCe-tag-single-string",
          "types": ["default-discrete-records"],
          "createdTimestamp": "1689781665469"
        },
        {
          "id": "3b42c8c3-3261-4a30-8af8-d2bde1ca72de",
          "tagName": "MCe-tag-array-event-3",
          "types": ["default-discrete-records"],
          "createdTimestamp": "1689781665458"
        },
        {
          "id": "73e198c8-0ffc-4064-bf42-6c60e413c845",
          "tagName": "MCe-tag-array-event-2",
          "types": ["default-discrete-records"],
          "createdTimestamp": "1689781665541"
        },
        {
          "id": "01822a93-f917-4c9c-a1a9-49ba7ee98bff",
          "tagName": "MCe-tag-array-event-0",
          "types": ["default-discrete-records"],
          "createdTimestamp": "1689781665470"
        },
        {
          "id": "7bccbbd2-9e65-4bb5-b0c7-48ab9531712d",
          "tagName": "MCe-tag-array-numeric",
          "types": ["default-complex-numeric-records"],
          "createdTimestamp": "1689781667366"
        },
        {
          "id": "85804705-64a6-494b-a105-c5b8b52ae147",
          "tagName": "stampingmachine-09-vibration",
          "types": ["default-complex-numeric-records"],
          "createdTimestamp": "1689781667445"
        },
        {
          "id": "c33732fb-28b3-43d6-a9ed-8d0c228f1eeb",
          "tagName": "primepaintingrobot-01-viscosity",
          "types": ["default-numeric-records"],
          "createdTimestamp": "1689781669547"
        },
        {
          "id": "50bbb41e-c378-4740-ba9e-0c6f84b44ca7",
          "tagName": "MCe-tag-array-event-1",
          "types": ["default-discrete-records"],
          "createdTimestamp": "1689781665555"
        },
        {
          "id": "39666ff1-738a-4c12-b1d9-370c41ca777f",
          "tagName": "MCe-tag-single-event",
          "types": ["default-discrete-records"],
          "createdTimestamp": "1689781665543"
        },
        {
          "id": "45ea101b-d077-4a91-96d7-aca35b5f20c1",
          "tagName": "stampingmachine-09-vibration-1",
          "types": ["default-numeric-records"],
          "createdTimestamp": "1689781669291"
        }
      ],
      "nextPageToken": "LTE4MDA5NTU0MzAuQUFBQUFhRnhTRlYwREFuRnVQcjBBMGx5K1JDVURPdFBtbmN0RW5lUHRGV2o3OE5M"
    }
    

The following is a sample request to get types from Config Manager:
    
    
    GET http://localhost:8080/data/v1/config/types?includeHeader=true&pageSize=5
    

A sample response would look similar to the following:
    
    
    {
      "header": {
        "typeCount": 5,
        "dataFields": {
          "active": "active",
          "typeName": "typeName",
          "archetypeName": "archetypeName",
          "createdTimestamp": "createdTimestamp",
          "id": "id"
        }
      },
      "types": [
        {
          "typeName": "default-complex-numeric-records",
          "archetypeName": "DISCRETE_DATA_SERIES",
          "createdTimestamp": "1689781557147",
          "id": "4ec777fc-f078-4465-81fd-d70e7a1df329",
          "active": true
        },
        {
          "typeName": "default-continuous-records",
          "archetypeName": "CONTINUOUS_DATA_SERIES",
          "createdTimestamp": "1689781557805",
          "id": "d684637a-b751-49d5-82c2-8941aa4c1ef4",
          "active": true
        },
        {
          "typeName": "default-clustered-numeric-records",
          "archetypeName": "CLUSTERED_NUMERIC_DATA_SERIES",
          "createdTimestamp": "1689781557979",
          "id": "e2dbbab1-ad15-4445-b0db-59bb17b96a54",
          "active": true
        },
        {
          "typeName": "default-numeric-records",
          "archetypeName": "NUMERIC_DATA_SERIES",
          "createdTimestamp": "1689781556887",
          "id": "0f6fc49f-a463-4948-ab65-e4c4f66192b9",
          "active": true
        },
        {
          "typeName": "default-discrete-records",
          "archetypeName": "DISCRETE_DATA_SERIES",
          "createdTimestamp": "1689781557444",
          "id": "94327246-5ec3-4777-9154-a968dd546c90",
          "active": true
        }
      ],
      "nextPageToken": "LTYxMjI4MTg4OC5BQUFBQVVzR25vRVpkMGplSU9FZUc1N2VJY2h0clNqQXhUOUN4QmYxSXZ6UGpjY3U="
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

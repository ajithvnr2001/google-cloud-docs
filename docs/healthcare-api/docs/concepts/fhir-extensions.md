---
url: https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-extensions/
title: FHIR extensions \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:36.763641+00:00
---

# FHIR extensions  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  FHIR extensions Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how the Cloud Healthcare API supports [FHIR extensions](http://hl7.org/fhir/extensibility.html).

## Overview

FHIR allows user-defined extensions on resources and data types. The Cloud Healthcare API supports storing and retrieving these extensions.

## Extension values

An extension element is a key-value pair. The key, stored in the `url` field, indicates the canonical URL of an extension definition that defines the content and meaning of the extension. The `value` field is a choice element that can contain many different FHIR data types.

This mechanism is the same across all FHIR versions, except that earlier versions have fewer available data types. The available data types for extensions can be found in the FHIR standard ([DSTU2](https://hl7.org/fhir/dstu2/extensibility.html), [STU3](https://hl7.org/fhir/stu3/extensibility.html), [R4](http://hl7.org/fhir/extensibility.html)).

The following example shows a `Patient` resource with two extensions, hair color and citizenship, on the root element:
    
    
    {
      "resourceType": "Patient",
      "active": true,
      "gender": "male",
      "extension": [
        {
          "url": "http://example.com/fhir/StructureDefinition/hair-color",
          "valueString": "brown"
        },
        {
          "url": "http://example.com/fhir/StructureDefinition/patient-citizenship",
          "valueCodeableConcept": {
            "coding" : [{
              "system" : "urn:iso:std:iso:3166",
              "code" : "US"
            }]
          }
        }
      ]
    }
    

Complex data types and elements with child fields can also have extensions; for example, this `Patient` contains an extension on the `identifier` field which is a complex data type and an extension on the `communication` field which has other child fields:
    
    
    {
      "resourceType": "Patient",
      "active": true,
      "gender": "male",
      "identifier": [
        "system": "MRN",
        "value": "AB1234",
        "extension": [
          {
            "url": "http://example.com/fhir/StructureDefinition/last-verified",
            "valueDateTime": "2021-01-01T00:00:00Z"
          }
        ]
      ],
      "communication": [
        {
          "language": {
            "coding": [{
              "system": "urn:iso:std:iso:639",
              "code": "EN"
            }]
          },
          "extension": [
            {
              "url": "http://example.com/fhir/StructureDefinition/fluency-level",
              "valueInteger": 7
            }
          ]
        }
      ]
    }
    

Each extension element can only have a single value field. To define an extension that contains an array of values, you must define multiple extension elements with the same `url`.

You can't define extensions on the root element for the following resource types:

  * `Binary`
  * `Bundle`
  * `Parameters`



## Complex extensions

Extensions can contain extensions to define a nested structure. The `url` name of the child extension is relative to the outer extension. Each extension element must have either a value element or a nested child extension, but not both.

The following example shows a `Patient` resource that contains a complex `patient-citizenship` extension with child extensions `code` and `period`:
    
    
    {
      "resourceType": "Patient",
      "extension": [
        {
          "url": "http://hl7.org/fhir/StructureDefinition/patient-citizenship",
          "extension": [
            {
              "url": "code",
              "valueCodeableConcept": {
                "coding": [{
                  "system": "urn:iso:std:iso:3166",
                  "code": "CA"
                }]
               }
            },
            {
              "url": "period",
              "valuePeriod": {
                "start": "2010-01-01"
              }
            }
          ]
          }
      ]
    }
    

## Extensions on primitive types

Primitive data types in FHIR can also have extensions. When represented in JSON format the extensions are represented in an additional JSON property with `_` prepended to the name of the primitive element, as defined in the [FHIR JSON representation](http://hl7.org/fhir/json.html#primitive).

The following example, in JSON format, shows a `Patient` resource with an extension on the `birthDate` field:
    
    
    {
      "resourceType": "Patient",
      "active": true,
      "gender": "male",
      "birthDate": "1970-01-01",
      "_birthDate": {
        "extension": [
          {
            "url": "http://example.com/fhir/StructureDefinition/date-type",
            "valueString": "A"
          }
        ]
      }
    }
    

If the primitive element is repeated, the property with `_` is also handled as an array, with null values used to align extension values with their corresponding primitives.

The following example shows a `Patient` resource with an extension on the second value of `name.given` but no extension on the first value:
    
    
    {
      "resourceType": "Patient",
      "name": {
        "given": [
          "ABC",
          "DEF"
        ],
        "_given": [
          null,
          {
            "extension": [
              {
                "url": "http://hl7.org/fhir/StructureDefinition/display",
                "valueString": "XYZ"
              }
            ]
          }
        ]
      }
    }
    

## Defining an extension with a `StructureDefinition`

For the purposes of interoperability, the name and meaning of an extension can be defined with a `StructureDefinition` resource that can be published or distributed to enable consumers of the data to interpret it. This is optional when using extensions in the Cloud Healthcare API.

The identity of this definition is indicated by the [canonical url](http://hl7.org/fhir/references.html#canonical) in the 'url' field. For any data that is exchanged between organizations, it is recommended to use a URL that data consumers can follow to obtain the `StructureDefinition`. The Cloud Healthcare API does not validate this URL or attempt to resolve it.

The contents of a `StructureDefinition` resource can be complex and are often defined using tools for authoring [FHIR profiles](http://hl7.org/fhir/profiling.html).

## Modifier extensions

[Modifier extensions](http://hl7.org/fhir/extensibility.html#modifierExtension) are similar to extensions, but are stored in the `modifierExtension` field. A modifier extension is additional data that can't be ignored because it could invalidate the interpretation of the element that contains it.

For example, a modifier extension could indicate that the patient does **not** have the specified condition or that a drug must **not** be prescribed.

The Cloud Healthcare API stores and retrieves modifier extensions but does not attempt to interpret their meaning. Applications are advised to take appropriate action when encountering a modifier extension that they do not understand, possibly by displaying a warning or rejecting the resource entirely. Implementers should avoid the use of modifier extensions where possible.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-advanced-search/
title: Advanced FHIR search features \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:13.864444+00:00
---

# Advanced FHIR search features  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-advanced-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Advanced FHIR search features Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to search for FHIR resources using more advanced query functionality available through the [`projects.locations.datasets.fhirStores.fhir.search`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/search) method. This guide assumes that you are already familiar with the contents of [Searching for FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search).

## Sample FHIR bundle

The samples on this page use a provided JSON FHIR bundle to show the results of advanced FHIR search features. Save the [`r4_bundle.json`](https://docs.cloud.google.com/static/healthcare-api/docs/resources/r4_bundle.json) file to your machine to use it in the samples.

### Execute the sample FHIR bundle

To execute the sample FHIR bundle in a FHIR store, see [Executing a bundle](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-bundles#executing_a_bundle). The FHIR store must have the following settings:

  * Set [`enableUpdateCreate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.enable_update_create) to `true`.
  * Set [`version`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.version) to R4.



## String search modifiers

A string search defaults to a prefix match that is case and accent insensitive through folding to the standard Unicode NFC form. Punctuation and extra whitespace is ignored.

The following modifiers are available:

  * `:contains` matches resources with the specified value anywhere in the string, for example `name:contains=eve` matches `Evelyn` and `Severine`.
  * `:exact` matches the entire string including case and accents, for example `name:exact=Eve` doesn't match `eve` or `Evelyn`.



Expand the following section to see an example of using search string modifiers:

#### String search modifiers samples

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



To send your request, choose one of these options:

#### curl

  
The following sample uses the `Patient?name:contains=eve` query. 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?name:contains=eve"

#### PowerShell

  
The following sample uses the `Patient?name:contains=eve` query. 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?name:contains=eve" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/patient2",
          "resource": {
            "active": false,
            "address": [
              {
                "city": "Mountain View",
                "district": "KW",
                "line": [
                  "1800 Amphibious Blvd"
                ],
                "period": {
                  "start": "2000-01-01"
                },
                "text": "1800 Amphibious Blvd",
                "type": "both",
                "use": "home"
              }
            ],
            "birthDate": "1989-03-11",
            "communication": [
              {
                "language": {
                  "coding": [
                    {
                      "code": "FR",
                      "display": "jkl",
                      "system": "123"
                    },
                    {
                      "code": "french",
                      "display": "mno",
                      "system": "456"
                    }
                  ],
                  "text": "pqr"
                }
              }
            ],
            "deceasedBoolean": false,
            "gender": "female",
            "id": "patient2",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "tag": [
                {
                  "code": "tag2",
                  "display": "Tag Two",
                  "system": "tag-system"
                },
                {
                  "code": "tag|tag3",
                  "display": "Tag Three",
                  "system": "other"
                }
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "name": [
              {
                "family": "Lee",
                "given": [
                  "Jane",
                  "Evelyne"
                ],
                "use": "usual"
              }
            ],
            "resourceType": "Patient",
            "telecom": [
              {
                "rank": 1,
                "system": "phone",
                "use": "home",
                "value": "0982344522"
              },
              {
                "rank": 2,
                "system": "email",
                "use": "home",
                "value": "jane@example.com"
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/patient1",
          "resource": {
            "active": false,
            "address": [
              {
                "city": "Mountain View",
                "district": "KW",
                "line": [
                  "1800 Amphibious Blvd"
                ],
                "period": {
                  "start": "1974-12-25"
                },
                "text": "1800 Amphibious Blvd",
                "type": "both",
                "use": "home"
              }
            ],
            "birthDate": "1974-12-25",
            "communication": [
              {
                "language": {
                  "coding": [
                    {
                      "code": "ENG",
                      "display": "def",
                      "system": "123"
                    },
                    {
                      "code": "english",
                      "display": "ghi",
                      "system": "456"
                    }
                  ],
                  "text": "abc"
                }
              }
            ],
            "deceasedBoolean": false,
            "gender": "male",
            "id": "patient1",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "tag": [
                {
                  "code": "tag1",
                  "display": "Tag One",
                  "system": "tag-system"
                },
                {
                  "code": "tag2",
                  "display": "Tag Two",
                  "system": "other-system"
                }
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "name": [
              {
                "family": "Lee",
                "given": [
                  "Alex",
                  "Cleve"
                ],
                "text": "Alex Lee",
                "use": "usual"
              },
              {
                "given": [
                  "Joe"
                ],
                "use": "nickname"
              }
            ],
            "resourceType": "Patient",
            "telecom": [
              {
                "rank": 1,
                "system": "phone",
                "use": "home",
                "value": "0982344522"
              },
              {
                "rank": 2,
                "system": "email",
                "use": "home",
                "value": "alex@example.com"
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?name%3Acontains=eve"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?name%3Acontains=eve"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?name%3Acontains=eve"
        }
      ],
      "resourceType": "Bundle",
      "total": 2,
      "type": "searchset"
    }
    

## Comparators and precision for numbers, dates, and quantities

Values used in a numeric or date search depend on the precision of the parameter value. For example, the number `7.00` has an implicit range of `6.995` inclusive to `7.005` exclusive. The date `2015-08-12` has a range of `2015-08-12T00:00:00` inclusive to `2015-08-13T00:00:00` exclusive.

Precision affects what results are returned for equality comparisons. For example, a value of `7.03` in a resource would match a search for `value=7.0` but would not match a search for `value=7.00`.

All clinically significant floating point values in FHIR are represented by types such as [Decimal](http://hl7.org/fhir/datatypes.html#decimal) and [Quantity](http://hl7.org/fhir/datatypes.html#Quantity) that record the precision of the stored value. As an exception there are a few fields that use simple integers, for example to represent a position in a sequence, and searches on those fields are exact numerical matches.

The following prefixes apply to numeric comparisons against a singleton value. If no prefixes are specified, the default is `eq`.

  * `eq`: equals, the exact stored value is inside the range defined by the precision of the parameter value
  * `ne`: not equals, the opposite of `eq`
  * `gt`: the exact stored value is greater than the exact parameter value
  * `lt`: the exact stored value is less than the exact parameter value
  * `ge`: the exact stored value is greater than or equal to the exact parameter value
  * `le`: the exact stored value is less than or equal to the exact parameter value



Date values have an implicit range based on the level of specificity of the value (one year, one month, one day). Other data types such as [Range](http://hl7.org/fhir/datatypes.html#Range) and [Period](http://hl7.org/fhir/datatypes.html#Period) contain explicit upper and lower bounds. The following prefixes apply to range comparisons. If no prefixes are specified, the default is `eq`.

  * `eq`: equals, the range of the parameter value fully contains the range of the target
  * `ne`: not equals, the opposite of `eq`
  * `gt`: greater than, the range above the parameter value overlaps with the range of the target
  * `lt`: less than, the range below the parameter value overlaps with the range of the target
  * `ge`: greater than or equal to
  * `le`: less than or equal to
  * `sa`: the range of the parameter value starts after the target range
  * `eb`: the range of the parameter value ends before the target range



#### Comparators and precision for numbers, dates, and quantities samples

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



To send your request, choose one of these options:

#### curl

  
The following sample uses the `_lastUpdated=gt2018-01-01` query to search for Patient resources with a `_lastUpdated` value greater than (`gt`) `2018-01-01`. 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?_lastUpdated=gt2018-01-01"

#### PowerShell

  
The following sample uses the `_lastUpdated=gt2018-01-01` query to search for Patient resources with a `_lastUpdated` value greater than (`gt`) `2018-01-01`. 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?_lastUpdated=gt2018-01-01" | Select-Object -Expand Content

The query `_lastUpdated=gt2018-01-01` returns Patient resources updated since 2018-01-01. If you created all of the resources in your FHIR store after that date, then the server returns all of the resources. To see a subset of resources, change the date to a time after some resources were last updated.
    
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/patient3",
          "resource": {
            "active": false,
            "address": [
              {
                "city": "Lisbon",
                "district": "KW",
                "line": [
                  "Avenida da Pastelaria, 1903"
                ],
                "period": {
                  "start": "1980-01-01"
                },
                "text": "Avenida da Pastelaria, 1903",
                "type": "both",
                "use": "home"
              }
            ],
            "birthDate": "1980-01-01",
            "deceasedBoolean": false,
            "id": "patient3",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "tag": [
                {
                  "code": "tag3",
                  "display": "Tag $3",
                  "system": "other|tag"
                },
                {
                  "code": "code,4",
                  "display": "Tag 4",
                  "system": "system"
                }
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "name": [
              {
                "family": "Smith",
                "given": [
                  "Mary"
                ],
                "text": "Smith, Mary",
                "use": "usual"
              }
            ],
            "resourceType": "Patient",
            "telecom": [
              {
                "rank": 1,
                "system": "phone",
                "use": "home",
                "value": "1110891111"
              },
              {
                "rank": 2,
                "system": "email",
                "use": "home",
                "value": "mary@example.com"
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/patient2",
          "resource": {
            "active": false,
            "address": [
              {
                "city": "Mountain View",
                "district": "KW",
                "line": [
                  "1800 Amphibious Blvd"
                ],
                "period": {
                  "start": "2000-01-01"
                },
                "text": "1800 Amphibious Blvd",
                "type": "both",
                "use": "home"
              }
            ],
            "birthDate": "1989-03-11",
            "communication": [
              {
                "language": {
                  "coding": [
                    {
                      "code": "FR",
                      "display": "jkl",
                      "system": "123"
                    },
                    {
                      "code": "french",
                      "display": "mno",
                      "system": "456"
                    }
                  ],
                  "text": "pqr"
                }
              }
            ],
            "deceasedBoolean": false,
            "gender": "female",
            "id": "patient2",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "tag": [
                {
                  "code": "tag2",
                  "display": "Tag Two",
                  "system": "tag-system"
                },
                {
                  "code": "tag|tag3",
                  "display": "Tag Three",
                  "system": "other"
                }
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "name": [
              {
                "family": "Lee",
                "given": [
                  "Jane",
                  "Evelyne"
                ],
                "use": "usual"
              }
            ],
            "resourceType": "Patient",
            "telecom": [
              {
                "rank": 1,
                "system": "phone",
                "use": "home",
                "value": "0982344522"
              },
              {
                "rank": 2,
                "system": "email",
                "use": "home",
                "value": "jane@example.com"
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/8ac08aa9-63d2-4e81-8647-3a138d7f9f5a",
          "resource": {
            "address": [
              {
                "country": "US",
                "line": [
                  "907 Arlo Cliffs",
                  "Suite 984"
                ],
                "postalCode": "XXXXX"
              }
            ],
            "birthDate": "1940-12-01",
            "communication": [
              {
                "language": {
                  "coding": [
                    {
                      "code": "en-US",
                      "display": "English (United States)",
                      "system": "urn:ietf:bcp:47"
                    }
                  ]
                }
              }
            ],
            "deceasedDateTime": "2009-07-26T12:01:23-05:00",
            "extension": [
              {
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
                "valueCodeableConcept": {
                  "coding": [
                    {
                      "code": "2106-3",
                      "display": "White",
                      "system": "http://hl7.org/fhir/v3/Race"
                    }
                  ],
                  "text": "race"
                }
              },
              {
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
                "valueCodeableConcept": {
                  "coding": [
                    {
                      "code": "2186-5",
                      "display": "Nonhispanic",
                      "system": "http://hl7.org/fhir/v3/Ethnicity"
                    }
                  ],
                  "text": "ethnicity"
                }
              },
              {
                "url": "http://hl7.org/fhir/StructureDefinition/birthPlace",
                "valueAddress": {
                  "city": "Tama",
                  "country": "US",
                  "postalCode": "52339",
                  "state": "Iowa"
                }
              },
              {
                "url": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName",
                "valueString": "Farrah Feeney"
              },
              {
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
                "valueCode": "M"
              },
              {
                "url": "http://hl7.org/fhir/StructureDefinition/patient-interpreterRequired",
                "valueBoolean": false
              },
              {
                "url": "http://standardhealthrecord.org/fhir/StructureDefinition/shr-actor-FictionalPerson-extension",
                "valueBoolean": true
              },
              {
                "url": "http://standardhealthrecord.org/fhir/StructureDefinition/shr-demographics-FathersName-extension",
                "valueHumanName": {
                  "text": "Christopher Diaz"
                }
              },
              {
                "url": "http://standardhealthrecord.org/fhir/StructureDefinition/shr-demographics-SocialSecurityNumber-extension",
                "valueString": "999-16-9041"
              }
            ],
            "gender": "male",
            "generalPractitioner": [
              {
                "reference": "Organization/9fb51c89-1453-406c-8357-578311b43a91"
              }
            ],
            "id": "8ac08aa9-63d2-4e81-8647-3a138d7f9f5a",
            "identifier": [
              {
                "system": "https://github.com/synthetichealth/synthea",
                "value": "c1ee4b49-3194-4b39-91ed-4d1393a780c6"
              },
              {
                "system": "http://hl7.org/fhir/sid/us-ssn",
                "type": {
                  "coding": [
                    {
                      "code": "SB",
                      "system": "http://hl7.org/fhir/identifier-type"
                    }
                  ]
                },
                "value": "999169041"
              },
              {
                "system": "urn:oid:2.16.840.1.113883.4.3.25",
                "type": {
                  "coding": [
                    {
                      "code": "DL",
                      "system": "http://hl7.org/fhir/v2/0203"
                    }
                  ]
                },
                "value": "S99992205"
              },
              {
                "system": "http://standardhealthrecord.org/fhir/StructureDefinition/passportNumber",
                "type": {
                  "coding": [
                    {
                      "code": "PPN",
                      "system": "http://hl7.org/fhir/v2/0203"
                    }
                  ]
                },
                "value": "X12551631X"
              },
              {
                "system": "http://hospital.smarthealthit.org",
                "type": {
                  "coding": [
                    {
                      "code": "MR",
                      "system": "http://hl7.org/fhir/v2/0203"
                    }
                  ]
                },
                "value": "c1ee4b49-3194-4b39-91ed-4d1393a780c6"
              }
            ],
            "maritalStatus": {
              "coding": [
                {
                  "code": "S",
                  "system": "http://hl7.org/fhir/v3/MaritalStatus"
                }
              ],
              "text": "S"
            },
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-demographics-PersonOfRecord"
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "multipleBirthBoolean": false,
            "name": [
              {
                "family": "Diaz",
                "given": [
                  "Christopher"
                ],
                "prefix": [
                  "Mr."
                ],
                "use": "official"
              }
            ],
            "resourceType": "Patient",
            "telecom": [
              {
                "system": "phone",
                "use": "home",
                "value": "434-100-2918 x800"
              }
            ],
            "text": {
              "div": "
    
    Generated by [Synthea](https://github.com/synthetichealth/synthea). Version identifier: 2dd4c1c37e2743d14e5073c7b5e42899a3e51531
    
    ",
              "status": "generated"
            }
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/patient1",
          "resource": {
            "active": false,
            "address": [
              {
                "city": "Mountain View",
                "district": "KW",
                "line": [
                  "1800 Amphibious Blvd"
                ],
                "period": {
                  "start": "1974-12-25"
                },
                "text": "1800 Amphibious Blvd",
                "type": "both",
                "use": "home"
              }
            ],
            "birthDate": "1974-12-25",
            "communication": [
              {
                "language": {
                  "coding": [
                    {
                      "code": "ENG",
                      "display": "def",
                      "system": "123"
                    },
                    {
                      "code": "english",
                      "display": "ghi",
                      "system": "456"
                    }
                  ],
                  "text": "abc"
                }
              }
            ],
            "deceasedBoolean": false,
            "gender": "male",
            "id": "patient1",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "tag": [
                {
                  "code": "tag1",
                  "display": "Tag One",
                  "system": "tag-system"
                },
                {
                  "code": "tag2",
                  "display": "Tag Two",
                  "system": "other-system"
                }
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "name": [
              {
                "family": "Lee",
                "given": [
                  "Alex",
                  "Cleve"
                ],
                "text": "Alex Lee",
                "use": "usual"
              },
              {
                "given": [
                  "Joe"
                ],
                "use": "nickname"
              }
            ],
            "resourceType": "Patient",
            "telecom": [
              {
                "rank": 1,
                "system": "phone",
                "use": "home",
                "value": "0982344522"
              },
              {
                "rank": 2,
                "system": "email",
                "use": "home",
                "value": "alex@example.com"
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_lastUpdated=gt2018-01-01"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_lastUpdated=gt2018-01-01"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_lastUpdated=gt2018-01-01"
        }
      ],
      "resourceType": "Bundle",
      "total": 4,
      "type": "searchset"
    }
    

## Token search

Token search parameters apply to cases where a value is not an arbitrary string, but rather an entity in a naming system. String matching on a token parameter is exact.

Most token searches apply to complex data types that contain a `system` that is a URI indicating the naming system that the `code` value is taken from. These searches support the following value syntaxes:

  * `[parameter]=[code]` matches the `code` value regardless of the `system`
  * `[parameter]=[system]|[code]` must match both the `system` and `code` specified
  * `[parameter]=|[code]` matches `code` when the `system` value is empty
  * `[parameter]=[system]|` matches any `code` with the given `system` value



There are several modifiers that trigger alternate token search functionality:

  * `:not` negates the matching conditions of a token search
  * `:text` does a string search (not exact match) on the `text` or `display` field associated with the code, instead of the code value itself
  * `:above` takes a parameter only of the form `[system]|[code]` and matches resources where the code in the resource subsumes the query parameter. To use this modifier the specified `system` must exist in the FHIR store as a `CodeSystem` resource.
  * `:below` is like `:above` but matches if the code in the resource is subsumed by the query parameter.
  * `:in` takes a single parameter using the reference parameter syntax, for example `code:in=ValueSet/1234`. The reference must refer to a `ValueSet` resource within the same FHIR store. The modifier matches any code that is in the referenced `ValueSet`.
  * `:not-in` negates the conditions of `:in`



Token searches also apply to boolean and URI fields and certain string fields where only exact match is allowed. In these cases, the only parameter format is `[parameter]=[value]`.

#### Token search samples

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



To send your request, choose one of these options:

#### curl

  
The following sample uses the `Patient?_tag=tag-system|tag2` query to search for Patient resources with a specified `system` and `code`. 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?_tag=tag-system|tag2"

#### PowerShell

  
The following sample uses the `Patient?_tag=tag-system|tag2` query to search for Patient resources with a specified `system` and `code`. 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?_tag=tag-system|tag2" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/patient2",
          "resource": {
            "active": false,
            "address": [
              {
                "city": "Mountain View",
                "district": "KW",
                "line": [
                  "1800 Amphibious Blvd"
                ],
                "period": {
                  "start": "2000-01-01"
                },
                "text": "1800 Amphibious Blvd",
                "type": "both",
                "use": "home"
              }
            ],
            "birthDate": "1989-03-11",
            "communication": [
              {
                "language": {
                  "coding": [
                    {
                      "code": "FR",
                      "display": "jkl",
                      "system": "123"
                    },
                    {
                      "code": "french",
                      "display": "mno",
                      "system": "456"
                    }
                  ],
                  "text": "pqr"
                }
              }
            ],
            "deceasedBoolean": false,
            "gender": "female",
            "id": "patient2",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "tag": [
                {
                  "code": "tag2",
                  "display": "Tag Two",
                  "system": "tag-system"
                },
                {
                  "code": "tag|tag3",
                  "display": "Tag Three",
                  "system": "other"
                }
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "name": [
              {
                "family": "Lee",
                "given": [
                  "Jane",
                  "Evelyne"
                ],
                "use": "usual"
              }
            ],
            "resourceType": "Patient",
            "telecom": [
              {
                "rank": 1,
                "system": "phone",
                "use": "home",
                "value": "0982344522"
              },
              {
                "rank": 2,
                "system": "email",
                "use": "home",
                "value": "jane@example.com"
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_tag=tag-system%7Ctag2"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_tag=tag-system%7Ctag2"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_tag=tag-system%7Ctag2"
        }
      ],
      "resourceType": "Bundle",
      "total": 1,
      "type": "searchset"
    }
    

## Searching for missing values

The search modifier `:missing` can be used on any search parameter to match based on the presence or absence of any value in the specified field. For example, `Patient?gender=unknown` matches resources that explicitly contain the `unknown` enum value for gender, but as this field is not required there may be other resources that do not populate the field at all. Such resources can be matched by `Patient?gender:missing=true`. The converse, `Patient?gender:missing=false` matches any resource that explicitly populates this field.

**Warning:** The `:missing` modifier is less scalable than a search for a specific value. Use caution when performing a search over a large FHIR store using `:missing` unless other query parameters narrow the results to a small set.

#### Missing values samples

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



To send your request, choose one of these options:

#### curl

  
The following sample uses the `gender:missing=false` query: 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?gender:missing=false"

#### PowerShell

  
The following sample uses the `gender:missing=false` query: 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?gender:missing=false" | Select-Object -Expand Content

One Patient resource with the ID `patient3` is missing a `gender` value: 
    
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/mydataset/fhirStores/FHIR_STORE_ID/fhir/Patient/patient3",
          "resource": {
            "active": false,
            "address": [
              {
                "city": "Lisbon",
                "district": "KW",
                "line": [
                  "Avenida da Pastelaria, 1903"
                ],
                "period": {
                  "start": "1980-01-01"
                },
                "text": "Avenida da Pastelaria, 1903",
                "type": "both",
                "use": "home"
              }
            ],
            "birthDate": "1980-01-01",
            "deceasedBoolean": false,
            "id": "patient3",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "tag": [
                {
                  "code": "tag3",
                  "display": "Tag $3",
                  "system": "other|tag"
                },
                {
                  "code": "code,4",
                  "display": "Tag 4",
                  "system": "system"
                }
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "name": [
              {
                "family": "Smith",
                "given": [
                  "Mary"
                ],
                "text": "Smith, Mary",
                "use": "usual"
              }
            ],
            "resourceType": "Patient",
            "telecom": [
              {
                "rank": 1,
                "system": "phone",
                "use": "home",
                "value": "1110891111"
              },
              {
                "rank": 2,
                "system": "email",
                "use": "home",
                "value": "mary@example.com"
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/mydataset/fhirStores/FHIR_STORE_ID/fhir/Patient/?gender%3Amissing=true"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/mydataset/fhirStores/FHIR_STORE_ID/fhir/Patient/?gender%3Amissing=true"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/mydataset/fhirStores/FHIR_STORE_ID/fhir/Patient/?gender%3Amissing=true"
        }
      ],
      "resourceType": "Bundle",
      "total": 1,
      "type": "searchset"
    }
    

## Text search

The use of the `_content` search parameter without specifying a FHIR resource type is deprecated. When you use `_content` to make a search, you must specify the FHIR resource type in one of the following ways:

In the HTTP path after `/fhir/`:
    
    
    https://healthcare.googleapis.com/v1/.../fhirStores/my-fhir-store/fhir/**Patient**?_content=Smith%20|%20Mountain%20View
    

In the HTTP path using the `_type` parameter:
    
    
    https://healthcare.googleapis.com/v1/.../fhirStores/my-fhir-store/fhir?**_type=Patient** &_content=Smith%20|%20Mountain%20View
    

If you don't provide a FHIR resource type, the results from the search query depend on whether you enabled [`defaultSearchHandlingStrict`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.default_search_handling_strict) on the FHIR store:

  * `defaultSearchHandlingStrict` enabled: The search query returns an error.
  * `defaultSearchHandlingStrict` disabled: The search query ignores the information in the `_content` parameter.



The special search parameter `_content` performs a text match on string-based fields (excluding number, date, or enum fields) if the field is the target of any search parameter on the resource. By default, `_content` matches resources that contain all of the words in the query, with support for additional operators:

  * `|` is the OR operator, for example `abc | def | ghi xyz` will match a resource that contains `xyz` and one or more of `abc` `def` `ghi`.
  * `-` is the NOT operator, for example `abc -def` will match a resource that contains `abc` but does not contain `def`.



The matching is based on complete words and does not match substrings or non-alphanumeric characters. The order of the words does not matter. Matching words can be spread across multiple fields in the resource.

The parameter `_text` performs the same type of match only on the [Narrative](http://hl7.org/fhir/narrative.html) field, which is intended to contain a human-readable summary of the resource contents. The Cloud Healthcare API does not automatically generate this summary, but supports the `_text` search parameter if this data was populated by the client when creating or updating the resource.

**Warning:** `_text` and `_contains` don't support `:contains` or `:exact` modifiers. `_content` does not support the `:missing` modifier.

#### Text search samples

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



To send your request, choose one of these options:

#### curl

  
The following sample uses the `_content=Smith%20|%20Mountain%20View` query: 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?_content=Smith%20|%20Mountain%20View"

#### PowerShell

  
The following sample uses the `_content=Smith%20|%20Mountain%20View` query: 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?_content=Smith%20|%20Mountain%20View" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/patient1",
          "resource": {
            "active": false,
            "address": [
              {
                "city": "Mountain View",
                "district": "KW",
                "line": [
                  "1800 Amphibious Blvd"
                ],
                "period": {
                  "start": "1974-12-25"
                },
                "text": "1800 Amphibious Blvd",
                "type": "both",
                "use": "home"
              }
            ],
            "birthDate": "1974-12-25",
            "communication": [
              {
                "language": {
                  "coding": [
                    {
                      "code": "ENG",
                      "display": "def",
                      "system": "123"
                    },
                    {
                      "code": "english",
                      "display": "ghi",
                      "system": "456"
                    }
                  ],
                  "text": "abc"
                }
              }
            ],
            "deceasedBoolean": false,
            "gender": "male",
            "id": "patient1",
            "meta": {
              "lastUpdated": "2021-10-21T16:41:47.211939+00:00",
              "tag": [
                {
                  "code": "tag1",
                  "display": "Tag One",
                  "system": "tag-system"
                },
                {
                  "code": "tag2",
                  "display": "Tag Two",
                  "system": "other-system"
                }
              ],
              "versionId": "MTYzNDgzNDUwNzIxMTkzOTAwMA"
            },
            "name": [
              {
                "family": "Lee",
                "given": [
                  "Alex",
                  "Cleve"
                ],
                "text": "Alex Lee",
                "use": "usual"
              },
              {
                "given": [
                  "Joe"
                ],
                "use": "nickname"
              }
            ],
            "resourceType": "Patient",
            "telecom": [
              {
                "rank": 1,
                "system": "phone",
                "use": "home",
                "value": "0982344522"
              },
              {
                "rank": 2,
                "system": "email",
                "use": "home",
                "value": "alex@example.com"
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/patient2",
          "resource": {
            "active": false,
            "address": [
              {
                "city": "Mountain View",
                "district": "KW",
                "line": [
                  "1800 Amphibious Blvd"
                ],
                "period": {
                  "start": "2000-01-01"
                },
                "text": "1800 Amphibious Blvd",
                "type": "both",
                "use": "home"
              }
            ],
            "birthDate": "1989-03-11",
            "communication": [
              {
                "language": {
                  "coding": [
                    {
                      "code": "FR",
                      "display": "jkl",
                      "system": "123"
                    },
                    {
                      "code": "french",
                      "display": "mno",
                      "system": "456"
                    }
                  ],
                  "text": "pqr"
                }
              }
            ],
            "deceasedBoolean": false,
            "gender": "female",
            "id": "patient2",
            "meta": {
              "lastUpdated": "2021-10-21T16:41:47.211939+00:00",
              "tag": [
                {
                  "code": "tag2",
                  "display": "Tag Two",
                  "system": "tag-system"
                },
                {
                  "code": "tag|tag3",
                  "display": "Tag Three",
                  "system": "other"
                }
              ],
              "versionId": "MTYzNDgzNDUwNzIxMTkzOTAwMA"
            },
            "name": [
              {
                "family": "Lee",
                "given": [
                  "Jane",
                  "Evelyne"
                ],
                "use": "usual"
              }
            ],
            "resourceType": "Patient",
            "telecom": [
              {
                "rank": 1,
                "system": "phone",
                "use": "home",
                "value": "0982344522"
              },
              {
                "rank": 2,
                "system": "email",
                "use": "home",
                "value": "jane@example.com"
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_content=Smith%7CMountain+View"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_content=Smith%7CMountain+View"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_content=Smith%7CMountain+View"
        }
      ],
      "resourceType": "Bundle",
      "total": 2,
      "type": "searchset"
    }
    

## Composite search parameters

When searching using multiple query parameters, there are cases where individual search parameters combined with AND would match unintended results. Composite search parameters are a special type of search parameter that address this issue.

For example, the `Observation` resource may contain multiple values in the `component` field, each of which contains a pair of `code` and `value`. A search for `Observation?component-code=8867-4&component-value-quantity=lt50` would match a resource that had one component containing a `code` of 8867-4 and a _different_ component containing a `value` less than 50. This search cannot be used to restrict to a match of these two values within the same component.

Composite search parameters define a new parameter that combines two other search parameters and defines a level of nesting within which they must both match. In the query, the two values are joined by `$`. For example, `Observation` has a composite parameter `component-code-value-quantity` that can restrict the previous example to a single component by searching for `Observation?component-code-value-quantity=8867-4$lt50`. These parameters are defined by the FHIR specification and do not exist for all combinations of search parameters.

Composite search parameters do not allow modifiers.

As with all search parameters, information on which composite parameters are supported by the Cloud Healthcare API can be found in the [capability statement](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/capabilities) or [FHIR Conformance Statement](https://docs.cloud.google.com/healthcare-api/docs/fhir).

#### Composite search samples

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



To send your request, choose one of these options:

#### curl

  
The following sample uses the `Observation?component-code-value-quantity=8480-6$lt150` query. 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?component-code-value-quantity=8480-6\$lt150"

#### PowerShell

  
The following sample uses the `Observation?component-code-value-quantity=8480-6$lt150` query. 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?component-code-value-quantity=8480-6\$lt150" | Select-Object -Expand Content

The response contains the Observation with a `component-code=8480-6` and a `component-value-quantity` of 133, which meets the criteria for `lt150`. 
    
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/a35bf421-1f00-4897-a94d-4d47c3bb306b",
          "resource": {
            "category": [
              {
                "coding": [
                  {
                    "code": "vital-signs",
                    "system": "http://hl7.org/fhir/observation-category"
                  }
                ]
              }
            ],
            "code": {
              "coding": [
                {
                  "code": "55284-4",
                  "display": "Blood Pressure",
                  "system": "http://loinc.org"
                }
              ]
            },
            "component": [
              {
                "code": {
                  "coding": [
                    {
                      "code": "8480-6",
                      "display": "Systolic Blood Pressure",
                      "system": "http://loinc.org"
                    }
                  ],
                  "text": "Systolic Blood Pressure"
                },
                "valueQuantity": {
                  "code": "mmHg",
                  "system": "http://unitsofmeasure.org",
                  "unit": "mmHg",
                  "value": 133
                }
              },
              {
                "code": {
                  "coding": [
                    {
                      "code": "8462-4",
                      "display": "Diastolic Blood Pressure",
                      "system": "http://loinc.org"
                    }
                  ],
                  "text": "Diastolic Blood Pressure"
                },
                "valueQuantity": {
                  "code": "mmHg",
                  "system": "http://unitsofmeasure.org",
                  "unit": "mmHg",
                  "value": 84
                }
              }
            ],
            "effectiveDateTime": "2008-03-07T17:47:02-05:00",
            "encounter": {
              "reference": "Encounter/0e9d631c-4407-45e5-bfbe-689806caaf7b"
            },
            "id": "a35bf421-1f00-4897-a94d-4d47c3bb306b",
            "issued": "2008-03-07T17:47:02-05:00",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-observation-Observation",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-BloodPressure"
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/8ac08aa9-63d2-4e81-8647-3a138d7f9f5a"
            }
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/?component-code-value-quantity=8480-6%24lt150"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/?component-code-value-quantity=8480-6%24lt150"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/?component-code-value-quantity=8480-6%24lt150"
        }
      ],
      "resourceType": "Bundle",
      "total": 1,
      "type": "searchset"
    }
    

## Chained search

A chained search allows a search to traverse references within the context of a query. The basic syntax for a chained search is:

`[reference parameter]:[resource type].[inner search parameter]=[inner value]`

If the reference parameter only refers to one resource type, the `:[resource type]` may be omitted, resulting in:

`[reference parameter].[inner search parameter]=[inner value]`

For example, `Observation` has a reference search parameter `subject` that may point to a `Group`, `Device`, `Patient`, or `Location`. To find `Observations` that have a `subject` which is a `Patient` having a name beginning with "Joe", you can search `Observation?subject:Patient.name=Joe`.

If the query has multiple chained parameters, each chain is evaluated separately. For example, `Patient?general-practitioner.name=Joe&general-practitioner.address-country=Canada` would match a `Patient` that had two `general-practitioner` references, one named "Joe" and the other having an address in Canada. There is no syntax to group these clauses together to match only Joe from Canada.

Chained searches can be recursive with other chains or reverse chains, for example `Observation?subject:Patient.organization.name=Acme` would match an `Observation` that refers to a `subject` that refers to an `organization` that has a `name` of `Acme`.

**Warning:** The Cloud Healthcare API has limited support for chained searches. The inner query must match no more than 100 results or the search returns an error. For recursive chained searches, each level of the recursion must match no more than 100 results or the search will return an error. This functionality is suitable for queries where the inner query is highly selective, for example `Observation?subject:Patient.identifier=MRN|123456` is likely to select a small number of `Patient` records and succeed, but `Observation?subject:Patient.gender=male` is not selective enough and is likely to be rejected. For queries that need generalized and scalable SQL join functionality, consider [Exporting FHIR resources to BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery).

#### Chained search samples

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



To send your request, choose one of these options:

#### curl

  
The following sample uses the `Observation?subject:Patient.name=Christopher` query to return all Observations that have a `subject` which is a `Patient` that has a name beginning with `Christopher`. 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?subject:Patient.name=Christopher"

#### PowerShell

  
The following sample uses the `Observation?subject:Patient.name=Christopher` query to return all Observations that have a `subject` which is a `Patient` that has a name beginning with `Christopher`. 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?subject:Patient.name=Christopher" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/85652a63-09ba-4a5b-ac5b-b690c6972eb5",
          "resource": {
            "category": [
              {
                "coding": [
                  {
                    "code": "laboratory",
                    "system": "http://hl7.org/fhir/observation-category"
                  }
                ]
              }
            ],
            "code": {
              "coding": [
                {
                  "code": "2093-3",
                  "display": "Total Cholesterol",
                  "system": "http://loinc.org"
                }
              ],
              "text": "Total Cholesterol"
            },
            "effectiveDateTime": "2008-03-07T17:47:02-05:00",
            "encounter": {
              "reference": "Encounter/0e9d631c-4407-45e5-bfbe-689806caaf7b"
            },
            "id": "85652a63-09ba-4a5b-ac5b-b690c6972eb5",
            "issued": "2008-03-07T17:47:02-05:00",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-observation-Observation"
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/8ac08aa9-63d2-4e81-8647-3a138d7f9f5a"
            },
            "valueQuantity": {
              "code": "mg/dL",
              "system": "http://unitsofmeasure.org",
              "unit": "mg/dL",
              "value": 191
            }
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/e7aea507-61af-4290-9323-0b3daed0b7a9",
          "resource": {
            "category": [
              {
                "coding": [
                  {
                    "code": "laboratory",
                    "system": "http://hl7.org/fhir/observation-category"
                  }
                ]
              }
            ],
            "code": {
              "coding": [
                {
                  "code": "2571-8",
                  "display": "Triglycerides",
                  "system": "http://loinc.org"
                }
              ],
              "text": "Triglycerides"
            },
            "effectiveDateTime": "2008-03-07T17:47:02-05:00",
            "encounter": {
              "reference": "Encounter/0e9d631c-4407-45e5-bfbe-689806caaf7b"
            },
            "id": "e7aea507-61af-4290-9323-0b3daed0b7a9",
            "issued": "2008-03-07T17:47:02-05:00",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-observation-Observation"
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/8ac08aa9-63d2-4e81-8647-3a138d7f9f5a"
            },
            "valueQuantity": {
              "code": "mg/dL",
              "system": "http://unitsofmeasure.org",
              "unit": "mg/dL",
              "value": 143
            }
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/a35bf421-1f00-4897-a94d-4d47c3bb306b",
          "resource": {
            "category": [
              {
                "coding": [
                  {
                    "code": "vital-signs",
                    "system": "http://hl7.org/fhir/observation-category"
                  }
                ]
              }
            ],
            "code": {
              "coding": [
                {
                  "code": "55284-4",
                  "display": "Blood Pressure",
                  "system": "http://loinc.org"
                }
              ]
            },
            "component": [
              {
                "code": {
                  "coding": [
                    {
                      "code": "8480-6",
                      "display": "Systolic Blood Pressure",
                      "system": "http://loinc.org"
                    }
                  ],
                  "text": "Systolic Blood Pressure"
                },
                "valueQuantity": {
                  "code": "mmHg",
                  "system": "http://unitsofmeasure.org",
                  "unit": "mmHg",
                  "value": 133
                }
              },
              {
                "code": {
                  "coding": [
                    {
                      "code": "8462-4",
                      "display": "Diastolic Blood Pressure",
                      "system": "http://loinc.org"
                    }
                  ],
                  "text": "Diastolic Blood Pressure"
                },
                "valueQuantity": {
                  "code": "mmHg",
                  "system": "http://unitsofmeasure.org",
                  "unit": "mmHg",
                  "value": 84
                }
              }
            ],
            "effectiveDateTime": "2008-03-07T17:47:02-05:00",
            "encounter": {
              "reference": "Encounter/0e9d631c-4407-45e5-bfbe-689806caaf7b"
            },
            "id": "a35bf421-1f00-4897-a94d-4d47c3bb306b",
            "issued": "2008-03-07T17:47:02-05:00",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-observation-Observation",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-BloodPressure"
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/8ac08aa9-63d2-4e81-8647-3a138d7f9f5a"
            }
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/14df9701-2dd4-4538-8fac-776c40dec22d",
          "resource": {
            "category": [
              {
                "coding": [
                  {
                    "code": "vital-signs",
                    "system": "http://hl7.org/fhir/observation-category"
                  }
                ]
              }
            ],
            "code": {
              "coding": [
                {
                  "code": "8302-2",
                  "display": "Body Height",
                  "system": "http://loinc.org"
                }
              ],
              "text": "Body Height"
            },
            "effectiveDateTime": "2008-03-07T17:47:02-05:00",
            "encounter": {
              "reference": "Encounter/0e9d631c-4407-45e5-bfbe-689806caaf7b"
            },
            "id": "14df9701-2dd4-4538-8fac-776c40dec22d",
            "issued": "2008-03-07T17:47:02-05:00",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-observation-Observation",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-VitalSign",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-BodyHeight"
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/8ac08aa9-63d2-4e81-8647-3a138d7f9f5a"
            },
            "valueQuantity": {
              "code": "cm",
              "system": "http://unitsofmeasure.org",
              "unit": "centimeters",
              "value": 177.72961711703704
            }
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/1e2fdce6-4c79-4ef8-a5a9-2326cddbc8b3",
          "resource": {
            "category": [
              {
                "coding": [
                  {
                    "code": "vital-signs",
                    "system": "http://hl7.org/fhir/observation-category"
                  }
                ]
              }
            ],
            "code": {
              "coding": [
                {
                  "code": "39156-5",
                  "display": "Body Mass Index",
                  "system": "http://loinc.org"
                }
              ],
              "text": "Body Mass Index"
            },
            "effectiveDateTime": "2008-03-07T17:47:02-05:00",
            "encounter": {
              "reference": "Encounter/0e9d631c-4407-45e5-bfbe-689806caaf7b"
            },
            "id": "1e2fdce6-4c79-4ef8-a5a9-2326cddbc8b3",
            "issued": "2008-03-07T17:47:02-05:00",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-observation-Observation",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-VitalSign",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-BodyMassIndex"
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/8ac08aa9-63d2-4e81-8647-3a138d7f9f5a"
            },
            "valueQuantity": {
              "code": "kg/m2",
              "system": "http://unitsofmeasure.org",
              "unit": "kg/m2",
              "value": 38.34566163709526
            }
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/58357362-6f18-438a-8479-3289ebab1617",
          "resource": {
            "category": [
              {
                "coding": [
                  {
                    "code": "laboratory",
                    "system": "http://hl7.org/fhir/observation-category"
                  }
                ]
              }
            ],
            "code": {
              "coding": [
                {
                  "code": "18262-6",
                  "display": "Low Density Lipoprotein Cholesterol",
                  "system": "http://loinc.org"
                }
              ],
              "text": "Low Density Lipoprotein Cholesterol"
            },
            "effectiveDateTime": "2008-03-07T17:47:02-05:00",
            "encounter": {
              "reference": "Encounter/0e9d631c-4407-45e5-bfbe-689806caaf7b"
            },
            "id": "58357362-6f18-438a-8479-3289ebab1617",
            "issued": "2008-03-07T17:47:02-05:00",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-observation-Observation"
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/8ac08aa9-63d2-4e81-8647-3a138d7f9f5a"
            },
            "valueQuantity": {
              "code": "mg/dL",
              "system": "http://unitsofmeasure.org",
              "unit": "mg/dL",
              "value": 102
            }
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/c6f1b042-a0fc-4bbc-9cd5-7a8a924c00e7",
          "resource": {
            "category": [
              {
                "coding": [
                  {
                    "code": "laboratory",
                    "system": "http://hl7.org/fhir/observation-category"
                  }
                ]
              }
            ],
            "code": {
              "coding": [
                {
                  "code": "2085-9",
                  "display": "High Density Lipoprotein Cholesterol",
                  "system": "http://loinc.org"
                }
              ],
              "text": "High Density Lipoprotein Cholesterol"
            },
            "effectiveDateTime": "2008-03-07T17:47:02-05:00",
            "encounter": {
              "reference": "Encounter/0e9d631c-4407-45e5-bfbe-689806caaf7b"
            },
            "id": "c6f1b042-a0fc-4bbc-9cd5-7a8a924c00e7",
            "issued": "2008-03-07T17:47:02-05:00",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-observation-Observation"
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/8ac08aa9-63d2-4e81-8647-3a138d7f9f5a"
            },
            "valueQuantity": {
              "code": "mg/dL",
              "system": "http://unitsofmeasure.org",
              "unit": "mg/dL",
              "value": 60
            }
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/ac57b908-2804-4d67-a7ad-1e4a4c3225a1",
          "resource": {
            "category": [
              {
                "coding": [
                  {
                    "code": "vital-signs",
                    "system": "http://hl7.org/fhir/observation-category"
                  }
                ]
              }
            ],
            "code": {
              "coding": [
                {
                  "code": "29463-7",
                  "display": "Body Weight",
                  "system": "http://loinc.org"
                }
              ],
              "text": "Body Weight"
            },
            "effectiveDateTime": "2008-03-07T17:47:02-05:00",
            "encounter": {
              "reference": "Encounter/0e9d631c-4407-45e5-bfbe-689806caaf7b"
            },
            "id": "ac57b908-2804-4d67-a7ad-1e4a4c3225a1",
            "issued": "2008-03-07T17:47:02-05:00",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-observation-Observation",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-VitalSign",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-BodyWeight"
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/8ac08aa9-63d2-4e81-8647-3a138d7f9f5a"
            },
            "valueQuantity": {
              "code": "kg",
              "system": "http://unitsofmeasure.org",
              "unit": "kg",
              "value": 121.12557348891558
            }
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/?subject%3APatient.name=Christopher"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/?subject%3APatient.name=Christopher"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/?subject%3APatient.name=Christopher"
        }
      ],
      "resourceType": "Bundle",
      "total": 8,
      "type": "searchset"
    }
    

## Reverse chained search

A reverse chained search matches resources based on criteria on other resources that refer to them. The syntax for a reverse chained search is:

`_has:[resource type]:[reference parameter]:[search parameter]=[value]`

For example, the `Appointment` resource has a search parameter `patient` referring to a `Patient` resource. To find all `Patient` resources that are referenced by an `Appointment` resource with a date of `2020-04-01`, use `Patient?_has:Appointment:patient:date=eq2020-04-01`.

Reverse chains can be recursive with other chains or reverse chains, for example `Practitioner?_has:Encounter:practitioner:_has:Claim:encounter:created=eq2020-04-01` would match a `Practitioner` P if there is an `Encounter` E and a `Claim` C such that C has a created date of `2020-04-01`, C refers to E through its `encounter` reference, and E refers to P through its `practitioner` reference.

**Warning:** The Cloud Healthcare API has limited support for reverse chained searches. The inner query must match no more than 100 results or the search will return an error. For recursive reverse chained searches, each level of the recursion must match no more than 100 results. For queries that need generalized and scalable SQL join functionality, consider [Exporting FHIR resources to BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery).

#### Reverse chained search samples

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



To send your request, choose one of these options:

#### curl

  
The following sample uses the `Patient?_has:Procedure:patient:date=eq2008-03-07` query. 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?_has:Procedure:patient:date=eq2008-03-07"

#### PowerShell

  
The following sample uses the `Patient?_has:Procedure:patient:date=eq2008-03-07` query. 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?_has:Procedure:patient:date=eq2008-03-07" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/8ac08aa9-63d2-4e81-8647-3a138d7f9f5a",
          "resource": {
            "address": [
              {
                "country": "US",
                "line": [
                  "907 Arlo Cliffs",
                  "Suite 984"
                ],
                "postalCode": "XXXXX"
              }
            ],
            "birthDate": "1940-12-01",
            "communication": [
              {
                "language": {
                  "coding": [
                    {
                      "code": "en-US",
                      "display": "English (United States)",
                      "system": "urn:ietf:bcp:47"
                    }
                  ]
                }
              }
            ],
            "deceasedDateTime": "2009-07-26T12:01:23-05:00",
            "extension": [
              {
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
                "valueCodeableConcept": {
                  "coding": [
                    {
                      "code": "2106-3",
                      "display": "White",
                      "system": "http://hl7.org/fhir/v3/Race"
                    }
                  ],
                  "text": "race"
                }
              },
              {
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
                "valueCodeableConcept": {
                  "coding": [
                    {
                      "code": "2186-5",
                      "display": "Nonhispanic",
                      "system": "http://hl7.org/fhir/v3/Ethnicity"
                    }
                  ],
                  "text": "ethnicity"
                }
              },
              {
                "url": "http://hl7.org/fhir/StructureDefinition/birthPlace",
                "valueAddress": {
                  "city": "Tama",
                  "country": "US",
                  "postalCode": "52339",
                  "state": "Iowa"
                }
              },
              {
                "url": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName",
                "valueString": "Farrah Feeney"
              },
              {
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
                "valueCode": "M"
              },
              {
                "url": "http://hl7.org/fhir/StructureDefinition/patient-interpreterRequired",
                "valueBoolean": false
              },
              {
                "url": "http://standardhealthrecord.org/fhir/StructureDefinition/shr-actor-FictionalPerson-extension",
                "valueBoolean": true
              },
              {
                "url": "http://standardhealthrecord.org/fhir/StructureDefinition/shr-demographics-FathersName-extension",
                "valueHumanName": {
                  "text": "Christopher Diaz"
                }
              },
              {
                "url": "http://standardhealthrecord.org/fhir/StructureDefinition/shr-demographics-SocialSecurityNumber-extension",
                "valueString": "999-16-9041"
              }
            ],
            "gender": "male",
            "generalPractitioner": [
              {
                "reference": "Organization/9fb51c89-1453-406c-8357-578311b43a91"
              }
            ],
            "id": "8ac08aa9-63d2-4e81-8647-3a138d7f9f5a",
            "identifier": [
              {
                "system": "https://github.com/synthetichealth/synthea",
                "value": "c1ee4b49-3194-4b39-91ed-4d1393a780c6"
              },
              {
                "system": "http://hl7.org/fhir/sid/us-ssn",
                "type": {
                  "coding": [
                    {
                      "code": "SB",
                      "system": "http://hl7.org/fhir/identifier-type"
                    }
                  ]
                },
                "value": "999169041"
              },
              {
                "system": "urn:oid:2.16.840.1.113883.4.3.25",
                "type": {
                  "coding": [
                    {
                      "code": "DL",
                      "system": "http://hl7.org/fhir/v2/0203"
                    }
                  ]
                },
                "value": "S99992205"
              },
              {
                "system": "http://standardhealthrecord.org/fhir/StructureDefinition/passportNumber",
                "type": {
                  "coding": [
                    {
                      "code": "PPN",
                      "system": "http://hl7.org/fhir/v2/0203"
                    }
                  ]
                },
                "value": "X12551631X"
              },
              {
                "system": "http://hospital.smarthealthit.org",
                "type": {
                  "coding": [
                    {
                      "code": "MR",
                      "system": "http://hl7.org/fhir/v2/0203"
                    }
                  ]
                },
                "value": "c1ee4b49-3194-4b39-91ed-4d1393a780c6"
              }
            ],
            "maritalStatus": {
              "coding": [
                {
                  "code": "S",
                  "system": "http://hl7.org/fhir/v3/MaritalStatus"
                }
              ],
              "text": "S"
            },
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-demographics-PersonOfRecord"
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "multipleBirthBoolean": false,
            "name": [
              {
                "family": "Diaz",
                "given": [
                  "Christopher"
                ],
                "prefix": [
                  "Mr."
                ],
                "use": "official"
              }
            ],
            "resourceType": "Patient",
            "telecom": [
              {
                "system": "phone",
                "use": "home",
                "value": "434-100-2918 x800"
              }
            ],
            "text": {
              "div": "
    
    Generated by [Synthea](https://github.com/synthetichealth/synthea). Version identifier: 2dd4c1c37e2743d14e5073c7b5e42899a3e51531
    
    ",
              "status": "generated"
            }
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_has%3AProcedure%3Apatient%3Adate=eq2008-03-07"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_has%3AProcedure%3Apatient%3Adate=eq2008-03-07"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_has%3AProcedure%3Apatient%3Adate=eq2008-03-07"
        }
      ],
      "resourceType": "Bundle",
      "total": 1,
      "type": "searchset"
    }
    

## Including additional resources in search results

The `_include` and `_revinclude` parameters request that the search results include additional resources ("included resources") related to the resources directly matching the query ("primary results"). Using these parameters is more efficient than making a series of requests to retrieve these additional resources separately. In the `searchset` bundle returned from the search, resources added by these parameters will be flagged with `entry.search.mode = include` to distinguish them from primary results which will have `entry.search.mode = match`.

Forward inclusion with `_include` adds resources and resource versions referenced by the primary results, and reverse inclusion with `_revinclude` adds resources that reference the primary results. The reference to follow is specified by the name of a search parameter, and only reference fields that are available as search parameters can be used in this way.

The parameter formats to `_include` and `_revinclude` are the same, taking two or three values delimited by `:`. The first value is the resource type that the reference is coming from, the second value is the search parameter name, and the optional third value limits the resource type to a single type in cases where the reference can point to more than one type.

For example:

  * `MedicationRequest?_include=MedicationRequest:subject` searches over `MedicationRequest` resources, and for each resource returned also returns the target of the `subject` reference which might be a `Group` or `Patient` as defined in the FHIR specification.
  * `MedicationRequest?_include=MedicationRequest:subject:Patient` is similar but only returns `subject` references to `Patient` resources.
  * `MedicationRequest?_revinclude=Provenance:target` searches over `MedicationRequest` resources, and for each resource returned also returns any `Provenance` resources where the `target` reference on `Provenance` refers to the matching resource.



#### `_include` search samples

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



To send your request, choose one of these options:

#### curl

  
The following sample uses the `Observation?code=http://loinc.org|2571-8&_include=*` query. 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?code=http://loinc.org|2571-8&_include=*"

#### PowerShell

  
The following sample uses the `Observation?code=http://loinc.org|2571-8&_include=*` query. 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?code=http://loinc.org|2571-8&_include=*" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/8ac08aa9-63d2-4e81-8647-3a138d7f9f5a",
          "resource": {
            "address": [
              {
                "country": "US",
                "line": [
                  "907 Arlo Cliffs",
                  "Suite 984"
                ],
                "postalCode": "XXXXX"
              }
            ],
            "birthDate": "1940-12-01",
            "communication": [
              {
                "language": {
                  "coding": [
                    {
                      "code": "en-US",
                      "display": "English (United States)",
                      "system": "urn:ietf:bcp:47"
                    }
                  ]
                }
              }
            ],
            "deceasedDateTime": "2009-07-26T12:01:23-05:00",
            "extension": [
              {
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
                "valueCodeableConcept": {
                  "coding": [
                    {
                      "code": "2106-3",
                      "display": "White",
                      "system": "http://hl7.org/fhir/v3/Race"
                    }
                  ],
                  "text": "race"
                }
              },
              {
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
                "valueCodeableConcept": {
                  "coding": [
                    {
                      "code": "2186-5",
                      "display": "Nonhispanic",
                      "system": "http://hl7.org/fhir/v3/Ethnicity"
                    }
                  ],
                  "text": "ethnicity"
                }
              },
              {
                "url": "http://hl7.org/fhir/StructureDefinition/birthPlace",
                "valueAddress": {
                  "city": "Tama",
                  "country": "US",
                  "postalCode": "52339",
                  "state": "Iowa"
                }
              },
              {
                "url": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName",
                "valueString": "Farrah Feeney"
              },
              {
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
                "valueCode": "M"
              },
              {
                "url": "http://hl7.org/fhir/StructureDefinition/patient-interpreterRequired",
                "valueBoolean": false
              },
              {
                "url": "http://standardhealthrecord.org/fhir/StructureDefinition/shr-actor-FictionalPerson-extension",
                "valueBoolean": true
              },
              {
                "url": "http://standardhealthrecord.org/fhir/StructureDefinition/shr-demographics-FathersName-extension",
                "valueHumanName": {
                  "text": "Christopher Diaz"
                }
              },
              {
                "url": "http://standardhealthrecord.org/fhir/StructureDefinition/shr-demographics-SocialSecurityNumber-extension",
                "valueString": "999-16-9041"
              }
            ],
            "gender": "male",
            "generalPractitioner": [
              {
                "reference": "Organization/9fb51c89-1453-406c-8357-578311b43a91"
              }
            ],
            "id": "8ac08aa9-63d2-4e81-8647-3a138d7f9f5a",
            "identifier": [
              {
                "system": "https://github.com/synthetichealth/synthea",
                "value": "c1ee4b49-3194-4b39-91ed-4d1393a780c6"
              },
              {
                "system": "http://hl7.org/fhir/sid/us-ssn",
                "type": {
                  "coding": [
                    {
                      "code": "SB",
                      "system": "http://hl7.org/fhir/identifier-type"
                    }
                  ]
                },
                "value": "999169041"
              },
              {
                "system": "urn:oid:2.16.840.1.113883.4.3.25",
                "type": {
                  "coding": [
                    {
                      "code": "DL",
                      "system": "http://hl7.org/fhir/v2/0203"
                    }
                  ]
                },
                "value": "S99992205"
              },
              {
                "system": "http://standardhealthrecord.org/fhir/StructureDefinition/passportNumber",
                "type": {
                  "coding": [
                    {
                      "code": "PPN",
                      "system": "http://hl7.org/fhir/v2/0203"
                    }
                  ]
                },
                "value": "X12551631X"
              },
              {
                "system": "http://hospital.smarthealthit.org",
                "type": {
                  "coding": [
                    {
                      "code": "MR",
                      "system": "http://hl7.org/fhir/v2/0203"
                    }
                  ]
                },
                "value": "c1ee4b49-3194-4b39-91ed-4d1393a780c6"
              }
            ],
            "maritalStatus": {
              "coding": [
                {
                  "code": "S",
                  "system": "http://hl7.org/fhir/v3/MaritalStatus"
                }
              ],
              "text": "S"
            },
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-demographics-PersonOfRecord"
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "multipleBirthBoolean": false,
            "name": [
              {
                "family": "Diaz",
                "given": [
                  "Christopher"
                ],
                "prefix": [
                  "Mr."
                ],
                "use": "official"
              }
            ],
            "resourceType": "Patient",
            "telecom": [
              {
                "system": "phone",
                "use": "home",
                "value": "434-100-2918 x800"
              }
            ],
            "text": {
              "div": "
    
    Generated by [Synthea](https://github.com/synthetichealth/synthea). Version identifier: 2dd4c1c37e2743d14e5073c7b5e42899a3e51531
    
    ",
              "status": "generated"
            }
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_has%3AProcedure%3Apatient%3Adate=eq2008-03-07"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_has%3AProcedure%3Apatient%3Adate=eq2008-03-07"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_has%3AProcedure%3Apatient%3Adate=eq2008-03-07"
        }
      ],
      "resourceType": "Bundle",
      "total": 1,
      "type": "searchset"
    }
    

The modifier `:iterate` causes an `_include` to be evaluated iteratively. This modifier can follow an extra layer of references from included results, or follow recursive structures such as `Observation:derived-from` referring to another `Observation`.

The depth of recursion is limited to two levels: the top level and two sublevels. For example, suppose you have the following sequence of references:

  * A Patient resource that references a PractitionerRole resource through the [`Patient.generalPractitioner`](https://www.hl7.org/fhir/patient-definitions.html#Patient.generalPractitioner) field.
  * The PractitionerRole resource references a Practitioner resource through the [`PractitionerRole.practitioner`](https://build.fhir.org/practitionerrole-definitions.html#PractitionerRole.practitioner) field.
  * The Practitioner resource references an Organization resource through the [`Practitioner.qualification.issuer`](https://build.fhir.org/practitioner-definitions.html#Practitioner.qualification.issuer) field.



The following example shows the sequence of references. The Organization resource at level 3 isn't included in the search results because it exceeds the maximum two-level limit.
    
    
    Patient (Level 0)
      - Patient.generalPractitioner -> PractitionerRole (Level 1)
        - PractitionerRole.practitioner -> Practitioner (Level 2)
          - Practitioner.organization -> Organization (Level 3)
    

The following additional examples describe the behavior of the `:iterate` modifier:

  * `Observation?_include:iterate=Observation:derived-from:Observation` searches over `Observation` resources and recursively follows the derived-from reference from matching `Observation` resources, and then from included resources.
  * `MedicationRequest?_revinclude=Provenance:target&_include:iterate=Provenance:agent` will search over `MedicationRequest` resources, include `Provenance` resources with a `target` that is in this result set, and then also include resources referenced through the `agent` parameter of those `Provenance` resources.



A wildcard, `*`, indicates that all references available as search parameters should be included. You can use the `*` wildcard as the first and only argument in the `_include`, or in place of the search parameter name from the standard `_include`, where the optional third value limits the resource type to a single type as in the original behavior.

For example:

  * `Observation?_include=*` searches over `Observation` resources, and for each resource also returns all referenced resources.
  * `Observation?_include=Observation:*` is equivalent to the preceding.
  * `MedicationRequest?_include=MedicationRequest:*:Patient` returns all references to `Patient` resources for each `MedicationRequest` resource.



The server deduplicates resources so that each page of results only includes one copy of the resource, even if the resource appears in multiple references. The same included resource appears on each page of results if a primary result relates to it.

### Manage the number of included resources

Note the following about additional resources included using the `_include` and `_revinclude` parameters:

  * Included resources don't count toward the page size. They aren't counted in `Bundle.total`, and they might cause the number of returned resources to be larger than a specified `_count` parameter.

  * Because included resources don't count toward the page size, use caution with `_include` and `_revinclude` parameters that might produce many results. Large result sizes can lead to timeouts or errors. Consider using a smaller `_count` value to limit the number of primary results if you expect many included results. Avoid following a one-to-many relationship where the many side of the relationship isn't bounded.

  * An individual `_revinclude` parameter adds at most 100 additional resources. For use cases where there might be more than 100 resources referring to the primary results, do one of the following:

    * Use a separate search query request using page size and pagination parameters to retrieve more results.
    * Start the search with the included resources:

Suppose an Encounter resource with ID `1234` has hundreds of Observation resources. Searching for these Observation resources using `_revinclude` (starting with the Encounter) returns a response that exceeds the limit of 100 additional resources:
          
          fhir/Encounter?_id=123&_revinclude=Observation:encounter
          

Instead, search for Observation resources and include the related Encounter using `_include`:
          
          fhir/Observation?encounter=123&_include=Observation:encounter
          

This approach filters Observation resources to only those related to the Encounter and retrieves the Encounter resource only once.




## Limiting fields returned in search results

The `_elements` parameter allows the client to request that only a subset of fields is returned for each search result to reduce the size of the response by omitting unnecessary data. The parameter accepts a comma-separated list of base element names in the resource, for example `Patient?_elements=identifier,contact,link`. Only these fields and their children will be included in the returned resources. Resources in the response that have been altered by this parameter will contain a `meta.tag` value of `SUBSETTED` to indicate that they are incomplete.

#### `_elements` search samples

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



To send your request, choose one of these options:

#### curl

  
The following sample uses the `Patient?_elements=identifier,contact,link` query. 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?_elements=identifier,contact,link"

#### PowerShell

  
The following sample uses the `Patient?_elements=identifier,contact,link` query. 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?_elements=identifier,contact,link" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/patient3",
          "resource": {
            "id": "patient3",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "tag": [
                {
                  "code": "SUBSETTED",
                  "system": "http://hl7.org/fhir/v3/ObservationValue"
                }
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "resourceType": "Patient"
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/patient2",
          "resource": {
            "id": "patient2",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "tag": [
                {
                  "code": "SUBSETTED",
                  "system": "http://hl7.org/fhir/v3/ObservationValue"
                }
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "resourceType": "Patient"
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/8ac08aa9-63d2-4e81-8647-3a138d7f9f5a",
          "resource": {
            "id": "8ac08aa9-63d2-4e81-8647-3a138d7f9f5a",
            "identifier": [
              {
                "system": "https://github.com/synthetichealth/synthea",
                "value": "c1ee4b49-3194-4b39-91ed-4d1393a780c6"
              },
              {
                "system": "http://hl7.org/fhir/sid/us-ssn",
                "type": {
                  "coding": [
                    {
                      "code": "SB",
                      "system": "http://hl7.org/fhir/identifier-type"
                    }
                  ]
                },
                "value": "999169041"
              },
              {
                "system": "urn:oid:2.16.840.1.113883.4.3.25",
                "type": {
                  "coding": [
                    {
                      "code": "DL",
                      "system": "http://hl7.org/fhir/v2/0203"
                    }
                  ]
                },
                "value": "S99992205"
              },
              {
                "system": "http://standardhealthrecord.org/fhir/StructureDefinition/passportNumber",
                "type": {
                  "coding": [
                    {
                      "code": "PPN",
                      "system": "http://hl7.org/fhir/v2/0203"
                    }
                  ]
                },
                "value": "X12551631X"
              },
              {
                "system": "http://hospital.smarthealthit.org",
                "type": {
                  "coding": [
                    {
                      "code": "MR",
                      "system": "http://hl7.org/fhir/v2/0203"
                    }
                  ]
                },
                "value": "c1ee4b49-3194-4b39-91ed-4d1393a780c6"
              }
            ],
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "tag": [
                {
                  "code": "SUBSETTED",
                  "system": "http://hl7.org/fhir/v3/ObservationValue"
                }
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "resourceType": "Patient"
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/patient1",
          "resource": {
            "id": "patient1",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "tag": [
                {
                  "code": "SUBSETTED",
                  "system": "http://hl7.org/fhir/v3/ObservationValue"
                }
              ],
              "versionId": "MTYzMTgyMTExMDIyMDk5ODAwMA"
            },
            "resourceType": "Patient"
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_elements=identifier%2Ccontact%2Clink"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_elements=identifier%2Ccontact%2Clink"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?_elements=identifier%2Ccontact%2Clink"
        }
      ],
      "resourceType": "Bundle",
      "total": 4,
      "type": "searchset"
    }
    

The Cloud Healthcare API has limited support for the `_summary` parameter, which provides pre-defined subsets of resource fields similar to `_elements`:

  * `_summary=text` returns only the `text`, `id`, and `meta` top-level fields
  * `_summary=data` removes the `text` field and returns all other fields



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

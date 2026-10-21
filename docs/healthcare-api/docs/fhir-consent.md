---
url: https://docs.cloud.google.com/healthcare-api/docs/fhir-consent/
title: Control access to FHIR resources in the Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:15.718117+00:00
---

# Control access to FHIR resources in the Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/fhir-consent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Control access to FHIR resources in the Cloud Healthcare API Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use [FHIR Consent resources](https://www.hl7.org/fhir/R4/consent.html) to determine data access of FHIR stores in the Cloud Healthcare API.

## Configure a FHIR access control enabled store

To configure a FHIR store with consent enforcement, complete the following steps:

  1. Create a FHIR store if you don't already have one.

  2. Set the following FHIR store's [`ConsentConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#ConsentConfig) parameters to enable consent enforcement:

     * `version`: Specifies which consent enforcement version is being used for the FHIR store. This value can only be set once by either [`CreateFhirStore`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/create) or [`UpdateFhirStore`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/patch). After it's set, you must call [`ApplyConsents`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/applyConsents) or [`ApplyAdminConsents`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/applyAdminConsents) to change the version.

     * `access_enforced`: If set to `true`, when accessing FHIR resources, the consent headers provided will be verified against consent directives given by consumers.

**Note:** The enforcement model is not in effect until `ApplyConsents` or `ApplyAdminConsents` is run, which is described in the following section.
     * [`consent_header_handling`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#ConsentHeaderHandling): If set to `PERMIT_EMPTY_SCOPE` (default), the server allows requests without (or empty) `X-Consent-Scope` header. If set to `REQUIRED_ON_READ` and `access_enforced` = `true`, the server rejects all requests without (or empty) `X-Consent-Scope` header.




#### Set up a new FHIR store with `ConsentConfig`
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json" \
        --data "{
          'version': 'R4',
          'enableUpdateCreate': true,
          'consentConfig': {
            'version': 'V1',
            'accessEnforced': true
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores?fhirStoreId=FHIR_STORE_ID"

You should receive a JSON response similar to the following: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      "version": "R4",
      "enableUpdateCreate": true,
      "consentConfig": {
        "version": "V1"
      }
    }
    

If you have an existing store already, use `UpdateFhirStore` to set the [`ConsentConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#consentconfig) with the consent enforcement `version` as [`V1`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#ConsentEnforcementVersion) and set `accessEnforced` to `true`.
    
    
    curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json" \
        --data "{
          'consentConfig': {
            'version': 'V1',
            'accessEnforced': true
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?update_mask=consentConfig"

## Define Policies Using Consent Resource

Policies are represented through [Consent resource](http://hl7.org/fhir/R4/consent.html). The resource fields' purpose and use are described in the [Data Model Docs](https://docs.cloud.google.com/healthcare-api/docs/fhir-access-control-technical).

Here is an example of all resources that can be created for this particular example.

#### Create FHIR resources

The following sample shows how to execute a [FHIR bundle](/healthcare-api/docs/how-tos/fhir-bundles) to populate the following resources: 

  * A Practitioner resource with name Jeffrey Brown
  * A Patient resource with name Darcy Smith
  * An Observation resource showing hemoglobin measurement of Darcy ([LOINC](https://loinc.org/)`718-7`) that was collected by the Happy Hospital
  * An Observation resource showing glucose measurement of Darcy ([LOINC](https://loinc.org/)`15074-8`).
  * A Consent from Darcy to permit Jeffrey Brown using application `App/123` to access her data collected by the Happy Hospital
  * A Consent from Darcy to permit Jeffrey Brown to access any of her data for emergency treatment ([`ETREAT`](http://hl7.org/fhir/R4/v3/ActReason/cs.html#v3-ActReason-ETREAT))
  * A Consent from the Happy Hospital to permit Jeffrey Brown to access all data when doing biomedical research ([`BIORCH`](http://hl7.org/fhir/R4/v3/ActReason/cs.html#v3-ActReason-BIORCH)) with application `App/golden`


    
    
    cat > bundle.json << 'EOF'
    {
      "resourceType": "Bundle",
      "type": "transaction",
      "entry": [
        {
          "request": {"method": "PUT", "url": "Practitioner/12942879-f89f-41ae-aa80-0b911b649833"},
          "resource": {
            "active": true,
            "birthDate": "1970-05-23",
            "gender": "male",
            "id": "12942879-f89f-41ae-aa80-0b911b649833",
            "name": [{
                "family": "Brown",
                "given": ["Jeffrey"],
                "use": "official"
            }],
            "resourceType": "Practitioner"
          }
        },
        {
          "request": {"method": "PUT", "url": "Patient/3c6aa096-c054-4c22-b2b4-1e4a4d203de2"},
          "resource": {
            "active": true,
            "birthDate": "1990-01-01",
            "gender": "female",
            "id": "3c6aa096-c054-4c22-b2b4-1e4a4d203de2",
            "name": [{
                "family": "Smith",
                "given": ["Darcy"],
                "use": "official"
            }],
            "meta": {
              "tag": [{
                "system": "http://terminology.hl7.org/CodeSystem/common-tags",
                "code": "employee"
              }]
            },
            "resourceType": "Patient"
          }
        },
        {
          "request": {"method": "PUT", "url": "Observation/7473784b-46a8-470c-b9a6-fe38a01025aa"},
          "resource": {
            "id": "7473784b-46a8-470c-b9a6-fe38a01025aa",
            "meta": {"source": "http://example.com/HappyHospital"},
            "code": {
              "coding": [{
                "code": "718-7",
                "system": "http://loinc.org",
                "display": "Hemoglobin [Mass/volume] in Blood"
              }]
            },
            "effectivePeriod": {"start": "2021-12-10T05:30:10+01:00"},
            "issued": "2021-12-10T13:30:10+01:00",
            "resourceType": "Observation",
            "status": "final",
            "subject": {"reference": "Patient/3c6aa096-c054-4c22-b2b4-1e4a4d203de2"},
            "valueQuantity": {
              "code": "g/dL",
              "system": "http://unitsofmeasure.org",
              "unit": "g/dl",
              "value": 7.2
            }
          }
        },
        {
          "request": {"method": "PUT", "url": "Observation/68583624-9921-4158-8754-2a306c689abd"},
          "resource": {
            "id": "68583624-9921-4158-8754-2a306c689abd",
            "code": {
              "coding": [{
                "code": "15074-8",
                "system": "http://loinc.org",
                "display": "Glucose [Moles/volume] in Blood"
              }]
            },
            "effectivePeriod": {"start": "2021-12-01T05:30:10+01:00"},
            "issued": "2021-12-01T13:30:10+01:00",
            "resourceType": "Observation",
            "status": "final",
            "subject": {"reference": "Patient/3c6aa096-c054-4c22-b2b4-1e4a4d203de2"},
            "valueQuantity": {
              "code": "mmol/L",
              "system": "http://unitsofmeasure.org",
              "unit": "mmol/l",
              "value": 6.3
            }
          }
        },
        {
          "request": {"method": "PUT", "url": "Consent/10998b60-a252-405f-aa47-0702554ddc8e"},
          "resource": {
            "category": [{
              "coding": [{
                "code": "59284-0",
                "system": "http://terminology.hl7.org/CodeSystem/consentcategorycodes"
              }]
            }],
            "id": "10998b60-a252-405f-aa47-0702554ddc8e",
            "patient": {"reference": "Patient/3c6aa096-c054-4c22-b2b4-1e4a4d203de2"},
            "policyRule": {
              "coding": [{
                "code": "OPTIN",
                "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode"
              }]
            },
            "provision": {
              "actor": [
                {
                  "reference": {"reference": "Practitioner/12942879-f89f-41ae-aa80-0b911b649833"},
                  "role": {
                    "coding": [{
                      "code": "GRANTEE",
                      "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
                    }]
                  }
                }
              ],
              "extension": [
                {
                  "url": "https://g.co/fhir/medicalrecords/Environment",
                  "valueCodeableConcept": {
                    "coding": [{
                      "code": "123",
                      "system": "App"
                    }]
                  }
                },
                {
                  "url": "https://g.co/fhir/medicalrecords/DataSource",
                  "valueUri": "http://example.com/HappyHospital"
                }
              ],
              "type": "permit"
            },
            "resourceType": "Consent",
            "scope": {
              "coding": [{
                "code": "patient-privacy",
                "system": "http://terminology.hl7.org/CodeSystem/consentscope"
              }]
            },
            "status": "active"
          }
        },
        {
          "request": {"method": "PUT", "url": "Consent/73c54e8d-2789-403b-9dee-13085c5d5e34"},
          "resource": {
            "category": [{
              "coding": [{
                "code": "59284-0",
                "system": "http://terminology.hl7.org/CodeSystem/consentcategorycodes"
              }]
            }],
            "id": "73c54e8d-2789-403b-9dee-13085c5d5e34",
            "patient": {"reference": "Patient/3c6aa096-c054-4c22-b2b4-1e4a4d203de2"},
            "policyRule": {
              "coding": [{
                "code": "OPTIN",
                "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode"
              }]
            },
            "provision": {
              "actor": [
                {
                  "reference": {"reference": "Practitioner/12942879-f89f-41ae-aa80-0b911b649833"},
                  "role": {
                    "coding": [{
                      "code": "GRANTEE",
                      "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
                    }]
                  }
                }
              ],
              "purpose": [{
                "code": "ETREAT",
                "system": "http://terminology.hl7.org/CodeSystem/v3-ActReason"
              }],
              "type": "permit"
            },
            "resourceType": "Consent",
            "scope": {
              "coding": [{
                "code": "patient-privacy",
                "system": "http://terminology.hl7.org/CodeSystem/consentscope"
              }]
            },
            "status": "active"
          }
        },
        {
          "request": {"method": "PUT", "url": "Consent/5c8e3f8a-9fd5-480d-a08e-f29b89feccde"},
          "resource": {
            "category": [{
              "coding": [{
                "code": "57017-6",
                "system": "http://loinc.org"
              }]
            }],
            "id": "5c8e3f8a-9fd5-480d-a08e-f29b89feccde",
            "patient": {},
            "extension": [{
              "url": "https://g.co/fhir/medicalrecords/ConsentAdminPolicy"
            }],
            "policyRule": {
              "coding": [{
                "code": "OPTIN",
                "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode"
              }]
            },
            "provision": {
              "actor": [
                {
                  "reference": {"reference": "Practitioner/12942879-f89f-41ae-aa80-0b911b649833"},
                  "role": {
                    "coding": [{
                      "code": "GRANTEE",
                      "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
                    }]
                  }
                }
              ],
              "purpose": [{
                "code": "BIORCH",
                "system": "http://terminology.hl7.org/CodeSystem/v3-ActReason"
              }],
              "extension": [
                {
                  "url": "https://g.co/fhir/medicalrecords/Environment",
                  "valueCodeableConcept": {
                    "coding": [{
                      "code": "golden",
                      "system": "App"
                    }]
                  }
                }
              ],
              "type": "permit"
            },
            "resourceType": "Consent",
            "scope": {},
            "status": "active"
          }
        }
      ]
    }
    EOF
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/fhir+json; charset=utf-8" \
        --data @bundle.json \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir"

You should receive a JSON response similar to the following: 
    
    
    {
      "entry": [
        {
          "response": {
            "etag": "W/\"VERSION_ID\"",
            "lastModified": "2022-09-01T17:31:40.423469+00:00",
            "location": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Practitioner/12942879-f89f-41ae-aa80-0b911b649833/_history/VERSION_ID",
            "status": "201 Created"
          }
        },
        {
          "response": {
            "etag": "W/\"VERSION_ID\"",
            "lastModified": "2022-09-01T17:31:40.423469+00:00",
            "location": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/3c6aa096-c054-4c22-b2b4-1e4a4d203de2/_history/VERSION_ID",
            "status": "201 Created"
          }
        },
        {
          "response": {
            "etag": "W/\"VERSION_ID\"",
            "lastModified": "2022-09-01T17:31:40.423469+00:00",
            "location": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/7473784b-46a8-470c-b9a6-fe38a01025aa/_history/VERSION_ID",
            "status": "201 Created"
          }
        },
        {
          "response": {
            "etag": "W/\"VERSION_ID\"",
            "lastModified": "2022-09-01T17:31:40.423469+00:00",
            "location": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/68583624-9921-4158-8754-2a306c689abd/_history/VERSION_ID",
            "status": "201 Created"
          }
        },
        {
          "response": {
            "etag": "W/\"VERSION_ID\"",
            "lastModified": "2022-09-01T17:31:40.423469+00:00",
            "location": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Consent/10998b60-a252-405f-aa47-0702554ddc8e/_history/VERSION_ID",
            "status": "201 Created"
          }
        },
        {
          "response": {
            "etag": "W/\"VERSION_ID\"",
            "lastModified": "2022-09-01T17:31:40.423469+00:00",
            "location": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Consent/73c54e8d-2789-403b-9dee-13085c5d5e34/_history/VERSION_ID",
            "status": "201 Created"
          }
        },
        {
          "response": {
            "etag": "W/\"VERSION_ID\"",
            "lastModified": "2022-09-01T17:31:40.423469+00:00",
            "location": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Consent/5c8e3f8a-9fd5-480d-a08e-f29b89feccde/_history/VERSION_ID",
            "status": "201 Created"
          }
        }
      ],
      "resourceType": "Bundle",
      "type": "transaction-response"
    }
    

Following are more examples of R4 [Consent resource](http://hl7.org/fhir/R4/consent.html) that demonstrates how complex policies can be represented.

**Note:** Some of the links in these examples are not resolvable and used for illustrative purposes only.

#### Sample patient consent directive
    
    
    {
      "resourceType": "Consent",
      "id": "patient-consent-example",
      "patient": {
        "reference": "Patient/f001"
      },
      "category": [
        {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "59284-0"
            }
          ]
        }
      ],
      "scope": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/consentscope",
            "code": "patient-privacy"
          }
        ]
      },
      "policyRule": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
            "code": "OPTIN"
          }
        ]
      },
      "status": "active",
      "provision": {
        "type": "permit",
        "actor": [
          {
            "reference": {
              "reference": "Practitioner/f002"
            },
            "role": {
              "coding": [
                {
                  "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
                  "code": "GRANTEE"
                }
              ]
            }
          }
        ],
        "purpose": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActReason",
            "code": "TREAT"
          }
        ],
        "class": [
          {
            "system": "http://hl7.org/fhir/resource-types",
            "code": "Encounter"
          }
        ],
        "data": [
          {
            "meaning": "instance",
            "reference": {
              "reference": "Encounter/e001"
            }
          }
        ],
        "extension": [
          {
            "url": "https://g.co/fhir/medicalrecords/Environment",
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "iso3166-1",
                  "code": "CA"
                }
              ]
            }
          },
          {
            "url": "https://g.co/fhir/medicalrecords/DataTag",
            "valueCoding": {
              "system": "http://terminology.hl7.org/CodeSystem/common-tags",
              "code": "actionable"
            }
          },
          {
            "url": "https://g.co/fhir/medicalrecords/DataTag",
            "extension": [
              {
                "url": "https://g.co/fhir/medicalrecords/DataTag",
                "valueCoding": {
                  "system": "http://example.com/custom-tags",
                  "code": "archived"
                }
              },
              {
                "url": "https://g.co/fhir/medicalrecords/DataTag",
                "valueCoding": {
                  "system": "http://example.com/custom-tags",
                  "code": "insensitive"
                }
              }
            ]
          },
          {
            "url": "https://g.co/fhir/medicalrecords/DataSource",
            "valueUri": "http://somesystem.example.org/foo"
          }
        ],
        "securityLabel": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/v3-Confidentiality",
            "code": "R"
          },
          {
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
            "code": "PSY"
          }
        ]
      }
    }

The preceding example represents a patient Consent resource in which a patient `f001` gives permission to a practitioner `f002` with the purpose of providing regular treatment represented by `TREAT`. The practitioner is from the geolocation `iso3166-1/CA`. This Consent resource permits the practitioner to access the patient data if the data satisfies **all** of the following conditions. 

  * It is an `Encounter` type with the ID `Encounter/e001`.
  * It comes from the source `http://somesystem.example.org/foo`.
  * It satisfies at least one of the following conditions on tag (resources can be tagged by setting [Meta.tag](https://hl7.org/fhir/R4/resource-definitions.html#Meta.tag)s' `system` and `code` field):
    * Has the tag (`system` = `http://terminology.hl7.org/CodeSystem/common-tags` and `code` = `actionable`)
    * Has both tags (`system` = `http://example.com/custom-tags` and `code` = `archived`) **and** (`system` = `http://example.com/custom-tags` and `code` = `insensitive`)
  * It has at least one of the following security labels
    * `system` = `http://terminology.hl7.org/CodeSystem/v3-Confidentiality` and `code` is one of `R`, `N`, `M`, `L`, `U`.
    * `system` = `http://terminology.hl7.org/CodeSystem/v3-ActCode` and `code` = `PSY`.



#### Sample admin policy directive
    
    
    {
      "resourceType": "Consent",
      "id": "admin-policy-example",
      "patient": {},
      "extension": [{
        "url": "https://g.co/fhir/medicalrecords/ConsentAdminPolicy"
      }],
      "category": [
        {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "57017-6"
            }
          ]
        }
      ],
      "scope": {},
      "policyRule": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
            "code": "OPTIN"
          }
        ]
      },
      "status": "active",
      "provision": {
        "type": "permit",
        "actor": [
          {
            "reference": {
              "reference": "Practitioner/f002"
            },
            "role": {
              "coding": [
                {
                  "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
                  "code": "GRANTEE"
                }
              ]
            }
          }
        ],
        "purpose": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActReason",
            "code": "TREAT"
          }
        ],
        "class": [
          {
            "system": "http://hl7.org/fhir/resource-types",
            "code": "Encounter"
          }
        ],
        "data": [
          {
            "meaning": "instance",
            "reference": {
              "reference": "Encounter/e001"
            }
          }
        ],
        "extension": [
          {
            "url": "https://g.co/fhir/medicalrecords/Environment",
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "iso3166-1",
                  "code": "CA"
                }
              ]
            }
          },
          {
            "url": "https://g.co/fhir/medicalrecords/DataTag",
            "valueCoding": {
              "system": "http://terminology.hl7.org/CodeSystem/common-tags",
              "code": "actionable"
            }
          },
          {
            "url": "https://g.co/fhir/medicalrecords/DataTag",
            "extension": [
              {
                "url": "https://g.co/fhir/medicalrecords/DataTag",
                "valueCoding": {
                  "system": "http://example.com/custom-tags",
                  "code": "archived"
                }
              },
              {
                "url": "https://g.co/fhir/medicalrecords/DataTag",
                "valueCoding": {
                  "system": "http://example.com/custom-tags",
                  "code": "insensitive"
                }
              }
            ]
          },
          {
            "url": "https://g.co/fhir/medicalrecords/DataSource",
            "valueUri": "http://somesystem.example.org/foo"
          }
        ],
        "securityLabel": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/v3-Confidentiality",
            "code": "R"
          },
          {
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
            "code": "PSY"
          }
        ]
      }
    }

The preceding example represents an admin policy Consent resource gives permission to a practitioner `f002` with the purpose of providing regular treatment represented by `TREAT`. The practitioner is from the geolocation `iso3166-1/CA`. This Consent resource permits the practitioner to access the patient data if the data satisfies **all** of the following conditions: 

  * It is an `Encounter` type with the ID `Encounter/e001`.
  * It comes from the source `http://somesystem.example.org/foo`.
  * It satisfies at least one of the following conditions on tag:
    * Has the tag (`system` = `http://terminology.hl7.org/CodeSystem/common-tags` and `code` = `actionable`)
    * Has both tags (`system` = `http://example.com/custom-tags` and `code` = `archived`) **and** (`system` = `http://example.com/custom-tags` and `code` = `insensitive`)
  * It has at least one of the following security labels
    * `system` = `http://terminology.hl7.org/CodeSystem/v3-Confidentiality` and `code` is one of `R`, `N`, `M`, `L`, `U`.
    * `system` = `http://terminology.hl7.org/CodeSystem/v3-ActCode` and `code` = `PSY`.



#### Sample admin cascading policy directive
    
    
    {
      "resourceType": "Consent",
      "id": "admin-cascading-policy-example",
      "patient": {},
      "extension": [
        { "url": "https://g.co/fhir/medicalrecords/ConsentAdminPolicy" },
        { "url": "https://g.co/fhir/medicalrecords/CascadingPolicy" }
      ],
      "category": [
        {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "57017-6"
            }
          ]
        }
      ],
      "scope": {},
      "policyRule": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
            "code": "OPTIN"
          }
        ]
      },
      "status": "active",
      "provision": {
        "type": "permit",
        "actor": [
          {
            "reference": {
              "reference": "Practitioner/f002"
            },
            "role": {
              "coding": [
                {
                  "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
                  "code": "GRANTEE"
                }
              ]
            }
          }
        ],
        "purpose": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActReason",
            "code": "TREAT"
          }
        ],
        "class": [
          {
            "system": "http://hl7.org/fhir/resource-types",
            "code": "Patient"
          }
        ],
        "extension": [
          {
            "url": "https://g.co/fhir/medicalrecords/Environment",
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "iso3166-1",
                  "code": "CA"
                }
              ]
            }
          },
          {
            "url": "https://g.co/fhir/medicalrecords/DataTag",
            "valueCoding": {
              "system": "http://terminology.hl7.org/CodeSystem/common-tags",
              "code": "employee"
            }
          }
        ]
      }
    }

The preceding example represents an admin cascading policy Consent resource giving permission to a practitioner `f002` with the purpose of providing regular treatment represented by `TREAT`. The practitioner is from the geolocation `iso3166-1/CA`. This Consent resource permits the practitioner to access the compartment data of patients with tag `employee`. All [resource criteria](https://docs.cloud.google.com/healthcare-api/docs/fhir-access-control-technical#resource-criteria) only applies to the compartment base resources, meaning the Patient resource, as it controls which resources to cascade from. 

## Enforce patient consents or admin policies

#### Enforce the patient's consents by `ApplyConsents`
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json" \
        --data "{'validateOnly': false}" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:applyConsents"

You should receive a JSON response similar to the following: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. To track the status of the operation, you can use the [Operation `get` method](/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get): 
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

When the operation finishes, the server returns a response with the status of the operation in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.fhir.FhirStoreService.ApplyConsents",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter": {
          "success": "2",
          "secondarySuccess": "5"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.fhir.ApplyConsentsResponse",
        "consentApplySuccess": "2",
        "affectedResources": "5"
      }
    }
    

This response indicated that the server successfully processed 2 consents and updated the consensual access of 5 resources (1 Patient, 2 Consents, 2 Observations). 

#### Enforce the admin policy by `ApplyAdminConsents`
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json" \
        --data "{
          'validateOnly': false,
          'newConsentsList': {
            'names': ['projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Consent/5c8e3f8a-9fd5-480d-a08e-f29b89feccde/_history/VERSION_ID']
          }
        }" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:applyAdminConsents"

You should receive a JSON response similar to the following: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. To track the status of the operation, you can use the [Operation `get` method](/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get): 
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

When the operation finishes, the server returns a response with the status of the operation in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.fhir.FhirStoreService.ApplyAdminConsents",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter": {
          "success": "1",
          "secondarySuccess": "7"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.fhir.ApplyAdminConsentsResponse",
        "consentApplySuccess": "1",
        "affectedResources": "7"
      }
    }
    

This response indicated that the server successfully processed 1 admin policy and updated the consensual access of 7 resources (1 Practitioner, 1 Patient, 2 Observations, 2 patient Consents and 1 admin policy). 

Enforcement on consents stored within a FHIR store won't come into effect until `ApplyConsents` (for patient consents) or `ApplyAdminConsents` (for admin policies and admin cascading policies) is called and completes successfully. If you add, modify, or remove consents after you have run `ApplyConsents` or `ApplyAdminConsents`, you must run it again for those consents to be included in the enforcement model.

FHIR resources are indexed asynchronously, so there might be a slight delay between the time when `ApplyConsents` or `ApplyAdminConsents` completes and when the enforcement model is reflected in search results. This delay is only expected for search requests.

If this is the first time you're setting up consent enforcement on the FHIR store, wait for the `ApplyConsents` or `ApplyAdminConsents` long-running operation to complete before making consent-aware requests.

To call `ApplyConsents` on a subset of patients, you can use the following filters:

  * [`PatientScope`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/applyConsents#PatientScope): to run `ApplyConsents` on a list of patient IDs with up to 10,000 patients

  * [`TimeRange`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/applyConsents#TimeRange): to run `ApplyConsent` on a list of Patient resource IDs whose Consent resources are updated during a certain time range




To call `ApplyAdminConsents`: you need to provide the full list of **all** policies that you want to apply (not an incremental list). As a result, an empty list will void enforcement from all admin policies from the store. Each policy must be a resource version name if the [FHIR store](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores) is versioning, and a resource name otherwise.

You can use [`operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to retrieve the [`ProgressCounter`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/OperationMetadata#ProgressCounter) of the operation. Upon completion there is an [ApplyConsentsResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/ApplyConsentsResponse) which is included in the [`Operation.response`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations#Operation). The counters in the `ProgressCounter` and `ApplyConsentsResponse` or `ApplyAdminConsentsResponse` are described in the following table.

`ProgressCounter` | `ApplyConsentsResponse` or `ApplyAdminConsentsResponse` | Description  
---|---|---  
`success` | `consentApplySuccess` | The number of Consent resources that the operation successfully processed.  
`failure` | `consentApplyFailure` | The number of Consent resources that are unsupported or invalid. You can either [view error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging) or when [`validateOnly`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/applyConsents#request-body) is `false`, check consent enforcement status using [`CheckConsentEnforcementStatus`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Consent-enforcement-status) or [`CheckPatientConsentEnforcementStatus`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Patient-consent-enforcement-status) to retrieve error details.  
`secondarySuccess` | `affectedResources` | When `validateOnly` is `false`, it represents the number of FHIR resources that were successfully re-indexed because of the effect of the consent change.  
`secondaryFailure` | `failedResources` | When `validateOnly` is `false`, it represents the number of FHIR resources that may have consent change but failed to reindex. This may affect search with consent context but not other methods. To see the error details, you can [view error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging).  
  
When FHIR Consent resources are processed, you can use the following APIs to check the status of enforcement for a single consent or all consents from a patient:

  * [`CheckConsentEnforcementStatus`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Consent-enforcement-status): returns a `Parameters` ([STU3](http://hl7.org/fhir/STU3/parameters.html), [R4](http://hl7.org/fhir/R4/parameters.html)) resource that lists the following parameters:

    * `id`: represents the resource ID of the Consent resource

    * `lastUpdated`: represents the time when the consent was last enforced

    * `versionId`: represents the version ID used for consent enforcement

    * `consent-enforcement-status`: represents the status of consent enforcement

  * [`CheckPatientConsentEnforcementStatus`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Patient-consent-enforcement-status): returns a `Bundle` ([STU3](http://hl7.org/fhir/STU3/bundle.html), [R4](http://hl7.org/fhir/R4/bundle.html)) of the `Parameters` ([STU3](http://hl7.org/fhir/STU3/parameters.html), [R4](http://hl7.org/fhir/R4/parameters.html)) resource consisting of enforcement status of all the consents from a single patient




For admin policy, `CheckConsentEnforcementStatus` can only be used for checking the enforcement status of a single Consent admin policy. Alternatively, you can use [`fhirStores.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/get) to see all the active admin policies applied to the store.

### Consent Enforcement Status

The `consent-enforcement-status` can have any of the following values:

  * `OFF`: represents the default enforcement status of a new Consent resource in which the Consent resource has never been processed.

  * `ENFORCEABLE`: the state in which the Consent resource has been processed successfully.

  * `INACTIVE`: an inactive state in which the Consent resource is ignored.

  * `UNSUPPORTED`: the state of a Consent resource that may conform to FHIR specifications, but is unenforceable. This is due to limited implementation of the FHIR consent enforcement with the current level of feature support.

  * `ENFORCEMENT_LIMIT_EXCEEDED`: the state when the FHIR consent resource format and the level of support for the resource are error-free, however one or more of the following conditions are true:

    * The Patient has a large set of Consent resources.

    * The size of the consent directives across all active consents is greater than the maximum allowed size of the consent directives for a FHIR server to enforce them.




## Search with Consent context

The Cloud Healthcare API supports searches for FHIR resources in a given FHIR store with `actor`, `purpose`, and `environment` as query parameters. The response contains only those resources that are consented.

#### Search FHIR resources with consent scope

  1. Practitioner Jeffrey Brown (identified by `Practitioner/12942879-f89f-41ae-aa80-0b911b649833`) using a trusted application `App/123` searches all Observations with `status=final`.
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Consent-Scope: actor/Practitioner/12942879-f89f-41ae-aa80-0b911b649833 env/App/123" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?status=final"

You should receive a JSON response similar to the following: 
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/7473784b-46a8-470c-b9a6-fe38a01025aa",
          "resource": {
            "code": {
              "coding": [
                {
                  "code": "718-7",
                  "display": "Hemoglobin [Mass/volume] in Blood",
                  "system": "http://loinc.org"
                }
              ]
            },
            "effectivePeriod": {
              "start": "2021-12-10T05:30:10+01:00"
            },
            "id": "7473784b-46a8-470c-b9a6-fe38a01025aa",
            "issued": "2021-12-10T13:30:10+01:00",
            "meta": {
              "lastUpdated": "2022-09-01T17:31:40.423469+00:00",
              "source": "http://example.com/HappyHospital",
              "versionId": "VERSION_ID"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/3c6aa096-c054-4c22-b2b4-1e4a4d203de2"
            },
            "valueQuantity": {
              "code": "g/dL",
              "system": "http://unitsofmeasure.org",
              "unit": "g/dl",
              "value": 7.2
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
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/?status=final"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/?status=final"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/?status=final"
        }
      ],
      "resourceType": "Bundle",
      "total": 1,
      "type": "searchset"
    }
    

  2. Practitioner Jeffrey Brown (identified by `Practitioner/12942879-f89f-41ae-aa80-0b911b649833`) using application `App/123` searches all Observations from Patient Darcy.
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Consent-Scope: actor/Practitioner/12942879-f89f-41ae-aa80-0b911b649833 env/App/123" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?subject:Patient.name=Darcy"

You should receive a JSON response similar to the following: 
    
    {
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/?subject%3APatient.name=Darcy"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/?subject%3APatient.name=Darcy"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/?subject%3APatient.name=Darcy"
        }
      ],
      "resourceType": "Bundle",
      "total": 0,
      "type": "searchset"
    }
    

The preceding query is a chained search. Because the consent scenario `actor/Practitioner/12942879-f89f-41ae-aa80-0b911b649833 env/App/123` is denied access for the Patient Darcy resource (identified by `Patient/3c6aa096-c054-4c22-b2b4-1e4a4d203de2`), the FHIR server returns no Observation from the Patient as if the Patient does not exist. 

  3. Practitioner Jeffrey Brown (identified by `Practitioner/12942879-f89f-41ae-aa80-0b911b649833`) using application `App/123` searches all Observations from Patient Darcy for emergency treatment purposes.
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Consent-Scope: actor/Practitioner/12942879-f89f-41ae-aa80-0b911b649833 purp/v3/ETREAT env/App/123" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?subject:Patient.name=Darcy"

You should receive a JSON response similar to the following: 
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/68583624-9921-4158-8754-2a306c689abd",
          "resource": {
            "code": {
              "coding": [
                {
                  "code": "15074-8",
                  "display": "Glucose [Moles/volume] in Blood",
                  "system": "http://loinc.org"
                }
              ]
            },
            "effectivePeriod": {
              "start": "2021-12-01T05:30:10+01:00"
            },
            "id": "68583624-9921-4158-8754-2a306c689abd",
            "issued": "2021-12-01T13:30:10+01:00",
            "meta": {
              "lastUpdated": "2022-09-01T17:31:40.423469+00:00",
              "versionId": "VERSION_ID"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/3c6aa096-c054-4c22-b2b4-1e4a4d203de2"
            },
            "valueQuantity": {
              "code": "mmol/L",
              "system": "http://unitsofmeasure.org",
              "unit": "mmol/l",
              "value": 6.3
            }
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/7473784b-46a8-470c-b9a6-fe38a01025aa",
          "resource": {
            "code": {
              "coding": [
                {
                  "code": "718-7",
                  "display": "Hemoglobin [Mass/volume] in Blood",
                  "system": "http://loinc.org"
                }
              ]
            },
            "effectivePeriod": {
              "start": "2021-12-10T05:30:10+01:00"
            },
            "id": "7473784b-46a8-470c-b9a6-fe38a01025aa",
            "issued": "2021-12-10T13:30:10+01:00",
            "meta": {
              "lastUpdated": "2022-09-01T17:31:40.423469+00:00",
              "source": "http://example.com/HappyHospital",
              "versionId": "VERSION_ID"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/3c6aa096-c054-4c22-b2b4-1e4a4d203de2"
            },
            "valueQuantity": {
              "code": "g/dL",
              "system": "http://unitsofmeasure.org",
              "unit": "g/dl",
              "value": 7.2
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
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/?subject:Patient.name=Darcy"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/?subject:Patient.name=Darcy"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/?subject:Patient.name=Darcy"
        }
      ],
      "resourceType": "Bundle",
      "total": 2,
      "type": "searchset"
    }
    

  4. Practitioner Jeffrey Brown (identified by `Practitioner/12942879-f89f-41ae-aa80-0b911b649833`) searches Observations with `status=final` for two purposes, treatment **and** research
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Consent-Scope: actor/Practitioner/12942879-f89f-41ae-aa80-0b911b649833 purp/v3/TREAT purp/v3/HRESCH" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?status=final"

You should receive a JSON response similar to the following: 
    
    {
      "issue": [
        {
          "code": "security",
          "details": {
            "text": "permission_denied"
          },
          "diagnostics": "the maximum number of allowed consent purpose scopes is 1, got 2",
          "severity": "error"
        }
      ],
      "resourceType": "OperationOutcome"
    }
    

In this case, Practitioner Jeffrey Brown should remove an unnecessary purpose from the `X-Consent-Scope` in the request. 

**Note**  
  
Removing consent scopes may increase or decrease the number of records returned depending on matching `permit` or `deny` consent directives. Therefore, the consent scopes should always reflect the access scenario in question, and dropping consent scopes that should be included for the access scenario should be done with care to make sure the consent enforcement reflects data usage agreements.
  5. A hospital IT administrator uses `bypass` to search for all Practitioners at the hospital.
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Consent-Scope: bypass actor/Admin/ef0592c9-6724-467e-878d-f879e537cd15 env/net/HappyNet" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Practitioner?"

Because `bypass` is provided, the consent checks were skipped. You should receive a JSON response similar to the following: 
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Practitioner/12942879-f89f-41ae-aa80-0b911b649833",
          "resource": {
            "active": true,
            "birthDate": "1970-05-23",
            "gender": "male",
            "id": "12942879-f89f-41ae-aa80-0b911b649833",
            "meta": {
              "lastUpdated": "2022-09-01T17:31:40.423469+00:00",
              "versionId": "VERSION_ID"
            },
            "name": [
              {
                "family": "Brown",
                "given": [
                  "Jeffrey"
                ],
                "use": "official"
              }
            ],
            "resourceType": "Practitioner"
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Practitioner/?"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Practitioner/?"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Practitioner/?"
        }
      ],
      "resourceType": "Bundle",
      "total": 1,
      "type": "searchset"
    }
    




## Get resource with Consent context

The Cloud Healthcare API supports get FHIR resource in a given FHIR store with `actor`, `purpose`, and `environment` as query parameters. The response contains only those resources that are consented.

#### Get FHIR resources with consent scope

  1. Practitioner Jeffrey Brown (identified by `Practitioner/12942879-f89f-41ae-aa80-0b911b649833`) using application `App/123` reads the hemoglobin measurement of the Patient (in this example, `Observation/7473784b-46a8-470c-b9a6-fe38a01025aa`).
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Consent-Scope: actor/Practitioner/12942879-f89f-41ae-aa80-0b911b649833 env/App/123" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/7473784b-46a8-470c-b9a6-fe38a01025aa"

Because the requestor was given consent, the response is the content of the Observation resource. 
    
    {
      "code": {
        "coding": [
          {
            "code": "718-7",
            "display": "Hemoglobin [Mass/volume] in Blood",
            "system": "http://loinc.org"
          }
        ]
      },
      "effectivePeriod": {
        "start": "2021-12-10T05:30:10+01:00"
      },
      "id": "7473784b-46a8-470c-b9a6-fe38a01025aa",
      "issued": "2021-12-10T13:30:10+01:00",
      "meta": {
        "lastUpdated": "2022-09-01T17:31:40.423469+00:00",
        "source": "http://example.com/HappyHospital",
        "versionId": "VERSION_ID"
      },
      "resourceType": "Observation",
      "status": "final",
      "subject": {
        "reference": "Patient/3c6aa096-c054-4c22-b2b4-1e4a4d203de2"
      },
      "valueQuantity": {
        "code": "g/dL",
        "system": "http://unitsofmeasure.org",
        "unit": "g/dl",
        "value": 7.2
      }
    }
    

  2. Practitioner Jeffrey Brown (identified by `Practitioner/12942879-f89f-41ae-aa80-0b911b649833`) using unknown application `App/unknown` reads the hemoglobin measurement of the Patient (in this example, `Observation/7473784b-46a8-470c-b9a6-fe38a01025aa`).
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Consent-Scope: actor/Practitioner/12942879-f89f-41ae-aa80-0b911b649833 env/App/unknown" \
      "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/7473784b-46a8-470c-b9a6-fe38a01025aa"

Because the boundary access of the requestor (`App/unknown`) is not permitted by the Patient's consent, the request is denied. 
    
    {
      "issue": [
        {
          "code": "security",
          "details": {
            "text": "permission_denied"
          },
          "diagnostics": "Consent access denied or the resource being accessed does not exist",
          "severity": "error"
        }
      ],
      "resourceType": "OperationOutcome"
    }
    

  3. Practitioner Jeffrey Brown (identified by `Practitioner/12942879-f89f-41ae-aa80-0b911b649833`) doing biomedical research using application `App/golden` reads the Darcy's birthDate (in this example, `Patient/3c6aa096-c054-4c22-b2b4-1e4a4d203de2`).
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Consent-Scope: actor/Practitioner/12942879-f89f-41ae-aa80-0b911b649833 purp/v3/BIORCH env/App/golden" \
      "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/3c6aa096-c054-4c22-b2b4-1e4a4d203de2"

Because the requestor was given consent, the response is the content of the Patient resource. 
    
    {
      "active": true,
      "birthDate": "1990-01-01",
      "gender": "female",
      "id": "3c6aa096-c054-4c22-b2b4-1e4a4d203de2",
      "meta": {
        "lastUpdated": "2022-09-01T17:31:40.423469+00:00",
        "versionId": "VERSION_ID",
        "tag": [{
          "system": "http://terminology.hl7.org/CodeSystem/common-tags",
          "code": "employee"
        }]
      },
      "name": [
        {
          "family": "Smith",
          "given": [
            "Darcy"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient"
    }
    

  4. Practitioner Jeffrey Brown (identified by `Practitioner/12942879-f89f-41ae-aa80-0b911b649833`) requests emergency unauthorized access to a patient's record, using the "break-the-glass" protocol. (in this example, `Observation/7473784b-46a8-470c-b9a6-fe38a01025aa`).
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Consent-Scope: btg actor/Practitioner/12942879-f89f-41ae-aa80-0b911b649833" \
      "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/7473784b-46a8-470c-b9a6-fe38a01025aa"

Because the consent's authorization method is `btg`, the server skips consent checks. The response is the content of the Observation resource. 
    
    {
      "code": {
        "coding": [
          {
            "code": "718-7",
            "display": "Hemoglobin [Mass/volume] in Blood",
            "system": "http://loinc.org"
          }
        ]
      },
      "effectivePeriod": {
        "start": "2021-12-10T05:30:10+01:00"
      },
      "id": "7473784b-46a8-470c-b9a6-fe38a01025aa",
      "issued": "2021-12-10T13:30:10+01:00",
      "meta": {
        "lastUpdated": "2022-09-01T17:31:40.423469+00:00",
        "source": "http://example.com/HappyHospital",
        "versionId": "VERSION_ID"
      },
      "resourceType": "Observation",
      "status": "final",
      "subject": {
        "reference": "Patient/3c6aa096-c054-4c22-b2b4-1e4a4d203de2"
      },
      "valueQuantity": {
        "code": "g/dL",
        "system": "http://unitsofmeasure.org",
        "unit": "g/dl",
        "value": 7.2
      }
    }
    




## Configure consent header

The following sections describe the supported consent enforcement methods in the Cloud Healthcare API and how resource access is enforced when you make a consent-aware request.

When making a request, your authorization server is responsible for generating access tokens with the relevant consent scope.

**Note:** See Constraints and limitations section for supported methods.

### Set HTTP header

**Note:** This section is only applicable if you're not using [SMART on FHIR](http://www.hl7.org/fhir/smart-app-launch/). To access the [Google Cloud SMART on FHIR](https://github.com/GoogleCloudPlatform/smart-on-fhir) GitHub repository, see [Configure SMART on FHIR in the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/smart-on-fhir#configure-smart).

Consent scopes are passed to the Cloud Healthcare API using the `X-Consent-Scope` HTTP header. The Cloud Healthcare API uses this header to enforce consent-based access control on data in FHIR stores.

A FHIR request can support limited number of consent entry scopes. Up to three entries of `actor`, one of `purp`, and one of `env` can be included in a given FHIR request.

For special scopes, a FHIR request can support one of `btg`, or `bypass`.

### Set HTTP headers for trusted applications

This section is only required if you're using a customer-controlled authorization server. In this instance, you must also use a SMARTproxy or similar proxy.

Some trusted applications may make calls directly to the Cloud Healthcare API with the consent scopes in the specified HTTP header. This enables direct consent enforcement without the need for a SMARTproxy or another proxy to convert between external authorization servers and Google Cloud.

For example, your application might be registered for a subset of scopes, such as an application `environment` scope, or the application might present a selection widget to set some scope entries such as the accessor's `purpose`.

A trusted user or a trusted application could also use [the `btg` or the `bypass` scope entries](https://docs.cloud.google.com/healthcare-api/docs/fhir-access-control-technical#request-scope), which are subject to post-audit reviews.

### Configure your authorization server for consent scopes

The Cloud Healthcare API provides built-in support for FHIR Consent enforcement based on the input consent scopes. FHIR store administrators are responsible for creating and configuring an authorization server outside of the Cloud Healthcare API that grants consent scopes.

### Sample access token

The following sample shows an access token encoded in base64:
    
    
    eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJpc3MiOiJjb25zZW50LnRva2VuLm9yZyIsImlhdCI6MTYxMjg4NDA4NSwiZXhwIjoxNjQ0NDIwMDg1LCJhdWQiOiJ3d3cuZXhhbXBsZS5jb20iLCJzdWIiOiJkb2N0b3IuZ2FicmllbGFAZXhhbXBsZS5jb20iLCJzY29wZSI6Im9pZGMgYWN0b3IvUHJhY3RpdGlvbmVyLzEyMyBhY3Rvci9Hcm91cC85OTkgcHVycC92My9UUkVBVCBlbnYvQXBwL2FiYyJ9.fC7ljkVUUx8fwUOrJuONcrqA-WKC-k_Bclzlgds0Cq6H_gEe3nUjPlSOCTQsIdYB
    

After decoding the access token, you can see that it contains the following payload:
    
    
    {
      "iss": "consent.token.org",
      "iat": 1612884085,
      "exp": 1644420085,
      "aud": "www.example.com",
      "sub": "doctor.gabriela@example.com",
      "scope": "oidc actor/Practitioner/123 actor/Group/999 purp/v3/TREAT env/App/abc"
    }
    

### Configure SMARTProxy

**Note:** This section is only applicable if you're using [SMARTProxy](https://docs.cloud.google.com/healthcare-api/docs/smart-on-fhir#configure-smart).

SMARTProxy is an open source proxy from Google that provides the following features:

  * Allows the Cloud Healthcare API FHIR server to accept and validate consent-aware access tokens.

  * Allows the FHIR implementation in the Cloud Healthcare API to include consent-aware access tokens as part of the Cloud Healthcare API management and permission model.

  * Supports token features for SMART on FHIR support as well.

**Note:** This requires a separate approval process.



When you make a request to retrieve data from the Cloud Healthcare API through SMARTProxy, the following occurs:

  1. SMARTProxy accepts a request from a client containing a consent-aware token.

  2. SMARTProxy validates the consent-aware token through a JWT authorization server that you own.

  3. SMARTProxy reads the scopes from the consent-aware token and passes them to the Cloud Healthcare API through the HTTP header.

  4. The Cloud Healthcare API receives the headers and validates them to enforce consent directives on the request. The Cloud Healthcare API then returns a response through the SMARTProxy to the client.




#### Configure a Google Cloud service account

A proxy can only have a single Google Cloud service account. If multiple clients use the same proxy, then the clients will use the same service account. Use caution when sharing a service account with multiple clients for the following reasons:

  * To read the FHIR data in the Cloud Healthcare API, the service account can be configured to have broad read and write permissions. For more information on permissions, see [Controlling access to Cloud Healthcare API resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/controlling-access). See General best practices for setting up proxy.

  * The Cloud Audit Logs

[principal email address](https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog#AuthenticationInfo.FIELDS.principal_email) is tied to the service account.




For example, if you call the Cloud Healthcare API directly using your Google Account for authentication, then Cloud Audit Logs logs your email address as the principal email address. When you use a proxy to call the Cloud Healthcare API, the proxy uses its own service account and the principal email address is the service account's email address and the original account is not defined.

## Audit logs

Audit logs are generated when there is an access request or when the resources' access enforcement changes.

### Access audit logs

If audit logs are [enabled](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) on the FHIR store, then a `consentMode` metadata field is included in the audit logs available in Cloud Logging. The `consentMode` may have one of the following values:

  * `off`: the FHIR store configuration has `consentConfig.accessEnforced` set to `false` and does not allow consent-aware requests.

  * `emptyScope`: the FHIR store has `consentConfig.accessEnforced` set to `true` but a consent scope header was not included. As a result, consents were not enforced.

  * `enforced`: the FHIR store has `consentConfig.accessEnforced` set to `true` and the consent scope header was present. As a result, consents were evaluated and enforced on the request.

  * `btg`: the FHIR request had `btg` provided in the consent scope header. As a result, consent checks were skipped. This request is intended to be used for emergencies and subject to post-audit review only.

  * `bypass`: the FHIR request had only `bypass` provided in the consent scope header. As a result, consent checks were skipped. This request is intended to be used by a trusted workflow (such as an administrator or a trusted application instead of end-users) so that this audit log is different from the `btg`, which is used for data governance checks.




Optionally, you may set [`access_determination_log_config`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#AccessDeterminationLogConfig) to `VERBOSE` to record more information about why a request is granted or denied.

### Access enforcement change audit logs

When the compartment base resource changes (for example, removing a patient's `employee` tag): The access control on the changed resource and its compartment may change due to Admin Cascading Policy. It will trigger reindexing on all of its compartment resources. The reindex progress for each compartment base resource update can be tracked in Cloud Logging with the filter `jsonPayload.@type="type.googleapis.com/google.cloud.healthcare.logging.FhirConsentCascadeLogEntry"`.

#### Sample cascade reindex progress log
    
    
    {
      "insertId": "tz2gtza8",
      "jsonPayload": {
        "@type": "type.googleapis.com/google.cloud.healthcare.logging.FhirConsentCascadeLogEntry",
        "state": "STATE_FINISHED",
        "affectedResources": "2",
        "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "compartmentBaseResourceName": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_RESOURCE_ID/_history/PATIENT_RESOURCE_VERSION"
      },
      "resource": {
        "type": "healthcare_fhir_store",
        "labels": {
          "location": "LOCATION",
          "dataset_id": "DATASET_ID",
          "fhir_store_id": "FHIR_STORE_ID",
          "project_id": "PROJECT_ID"
        }
      },
      "timestamp": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
      "severity": "INFO",
      "logName": "projects/PROJECT_ID/logs/healthcare.googleapis.com%2Fconsent_cascading_fhir",
      "receiveTimestamp": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ"
    }
    

`jsonPayload.state` is the state of the reindex operation, `jsonPayload.affectedResources` is the number of reindexed compartment resources, and `jsonPayload.lastUpdated` is the timestamp of patient resource update. If the operation just started, then `jsonPayload.state="STATE_STARTED"`, and `jsonPayload.affectedResources` won't be present. 

## Constraints and limitations

This section shows the constraints and limits for FHIR [R4](http://hl7.org/fhir/R4/index.html), but the same constraints and limits apply to FHIR [STU3](http://hl7.org/fhir/STU3/).

Type | Constraints and limits  
---|---  
Single Consent resource | 

  * Only a single [`Consent.provision`](https://hl7.org/fhir/R4/consent-definitions.html#Consent.provision) is supported, multiple provisions or nested provision are unsupported.
  * At least 1 [`Consent.provision.actor`](http://hl7.org/fhir/consent-definitions.html#Consent.provision.actor), at most 25:
    * `Consent.provision.actor.role` must be `http://terminology.hl7.org/CodeSystem/v3-RoleCode`.
    * `Consent.provision.actor.code` must be `GRANTEE` or `HPOWATT`.
  * At most 1 [`Consent.provision.purpose`](http://hl7.org/fhir/R4/consent-definitions.html#Consent.provision.purpose):
    * `Consent.provision.purpose.system` must be `http://terminology.hl7.org/CodeSystem/v3-ActReason`.
    * `Consent.provision.purpose.code` is non-empty and at most 13 characters.
  * At most 1 `environment`:
    * `Consent.provision.extension.url` must be `https://g.co/fhir/medicalrecords/Environment`.
    * Length of system and code combined must be less than 15 characters.
  * If filtering by resource type, `Consent.provision.class.system` must be `http://hl7.org/fhir/resource-types`.
  * If filtering by data source, `Consent.provision.extension.url` must be `https://g.co/fhir/medicalrecords/DataSource`.
  * If filtering by data tag, `Consent.provision.extension.url` must be `https://g.co/fhir/medicalrecords/DataTag`.
    * Data tag may be a complex extension, nested up to one level, to describe a policy that matches resources with all of the specified tags (interpreted conjunctively).
    * At most 5 nested tags are supported.
  * At most 100 values for all repeated attributes unless described differently in this row.

  
Enforcement model | 

  * Each patient may have up to 200 [`active`](https://www.hl7.org/fhir/R4/valueset-consent-state-codes.html) Consent resources enforced at a time.
  * Each store may have up to 200 [`active`](https://www.hl7.org/fhir/R4/valueset-consent-state-codes.html) admin policies enforced at a time.
  * A special compact format for the set of all [Consent Directives](https://docs.cloud.google.com/healthcare-api/docs/fhir-access-control-technical#consent-directive) across all active consents for a given Patient must not exceed a set threshold of size; typically there is enough capacity to encode thousands of consent directives, unless very long resource strings are particularly plentiful. For example:
    * Hundreds of Consents on unique data source and data tags, each of which is very long consumes a lot of space.
    * A single Patient with 3000 unique `Consent.provision.data.reference` resource identifier entries across many active Consents each specifying a unique `Consent.provision.actor` uses space more aggressively than provisions that don't specify any data reference constraint or otherwise contain many of the same actor reference strings.
  * Each resource may have up to 1000 consent directives from all Consents that are applicable to it.

  
`X-Consent-Scope` | 

  * Minimum one and maximum three `actor` entries.
  * Maximum one `purp` entry:
    * Each `purp` entry must be of the format `system/code` (`v3` is the registered system for `http://terminology.hl7.org/CodeSystem/v3-ActReason`).
    * Length of the code must be less than 13.
  * Maximum one `env` entry:
    * Each `env` entry must be of the format `system/code`.
    * Length of system and code combined must be less than 15.
  * `btg` requires minimum one `actor` entry.
  * `bypass` requires minimum one `actor` entry and one `env` entry.

  
Supported methods | 

  * The Cloud Healthcare API supports consent enforcement for the following methods:
    * [`fhir.read`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/read)
    * [`fhir.vread`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/vread)
    * [`fhir.history`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/history)
    * [`fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle) with `GET` operations
    * [`fhir.search`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/search) and [`fhir.search-type`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/search-type)
    * [`fhir.Observation-lastn`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Observation-lastn)
    * [`fhir.Patient-everything`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Patient-everything)
    * [`fhir.Encounter-everything`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Encounter-everything)
    * [`fhir.Consent-enforement-status`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Consent-enforcement-status)
    * [`fhir.Patient-consent-enforement-status`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Patient-consent-enforcement-status)
  * Write methods such as `POST`, `PUT`, `PATCH`, and `DELETE` are not supported for individual resources or a bundle of resources.
  * All [`projects.locations.datasets.fhirStores`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores) methods are unsupported.

  
Performance | 

  * `ApplyConsents` and `ApplyAdminConsents` scale similarly or better than `ImportResources`.
    * If you require higher throughput, contact your [support representative](https://docs.cloud.google.com/support/docs#contacting_technical_support).
  * Regarding consent-aware requests:
    * Our consent model has been optimized for enforcement performance of CRUD operations, including search at scale across many resources and many patients.
    * A read of individual resources may have a marginal impact on request latency, however search performance varies based on the base query and the number of [consent scopes](https://docs.cloud.google.com/healthcare-api/docs/fhir-access-control-technical#consent-scope) that leads to more [accessor criteria](https://docs.cloud.google.com/healthcare-api/docs/fhir-access-control-technical#accessor-criteria) being active during a search.
    * We recommend running your own performance tests over a variety of representative FHIR request parameters to determine performance characteristics for your use cases based on characteristics of your data, such as how many resources of a given search resource type are in the FHIR store.
    * Our solution keeps ingestion and updates of all resources, including consent resources, light-weight such that throughput during ingestion and other forms of write traffic may proceed with minimum impact.

  
  
## Best practices

The following sections describe best practices when using FHIR Access Control.

### General best practices

  * Don't [import](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export) FHIR resources and call `ApplyConsents` or `ApplyAdminConsents` in parallel. We recommend you to first import FHIR resources and then call `ApplyConsents` or `ApplyAdminConsents`. However, if the resources to be imported don't include any Patient or Consent resources, then the [enforcement model](https://docs.cloud.google.com/healthcare-api/docs/fhir-access-control-technical#consent_enforcement_model) won't be affected and processing consents or admin policies is not necessary.

  * Don't [create custom searches](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-custom-search) and call `ApplyConsents` in parallel. We recommend you to do them one after the other.

  * If your workflows require calling multiple `ApplyConsents` on disjoint `PatientScope`, they can be called in parallel.

  * `ApplyAdminConsents` can run in parallel with any number of `ApplyConsents`, but not with another `ApplyAdminConsents`.

  * When setting up the proxy, restrict the IAM service account with read-only permissions to avoid writing one patient's data to another patient's records.

  * Don't use the consent proxy when creating or updating records.

  * Validate all write requests to prevent unexpected modification of cross-patient data.

  * When cascading consents are enforced, compartment base resources must be [imported](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export) first, followed by the remaining compartment resources. Alternatively, all compartment resources can be wrapped within a single bundle and ingested using[`fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle).




### Delete Patient resource

When deleting a Patient resource, if you also want to remove the consent enforcement for that patient (especially when `FhirStore.disableReferentialIntegrity` is true), we recommend you to follow this order of operations:

  1. Delete all Consent resources belonging to the Patient resource.

  2. Call `ApplyConsents` with the `PatientScope` filter.




### Set up an existing store for consent access

To set up an existing store for consent access, complete these steps:

  1. Use `UpdateFhirStore` to set the [`ConsentConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#consentconfig) with the consent enforcement `version` as [`V1`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#ConsentEnforcementVersion) and set `accessEnforced` to `true`.
         
         curl -X PATCH \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json" \
             --data "{
               'consentConfig': {
                 'version': 'V1',
                 'accessEnforced': true
               }
             }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?update_mask=consentConfig"

  2. Process patient consents or admin policies

     1. `ApplyConsents` for patient consents
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json" \
        --data "{'validateOnly': false}" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:applyConsents"

     1. `ApplyAdminConsents` for admin policies and admin cascading policies.
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json" \
        --data "{
          'newConsentsList': {
              'names': [
              'projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Consent/RESOURCE_ID_1/_history/VERSION_ID_1',
              ...
              'projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Consent/RESOURCE_ID_N/_history/VERSION_ID_N'
              ]
          },
          'validateOnly': false
        }" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:applyAdminConsents"




### How often to run ApplyConsents or ApplyAdminConsents

  * When the `ConsentConfig` field is unset: The `ConsentConfig` field is unset both when a FHIR store is first created and when the `ConsentConfig` field is cleared. Once the `ConsentConfig` field is unset, you must repeat the set up the store for consent access before making consent-aware requests to avoid evaluating out of date consent enforcement policies.

  * When the [enforcement model](https://docs.cloud.google.com/healthcare-api/docs/fhir-access-control-technical#consent_enforcement_model) changes: When a Consent resource is created, updated, or deleted, the enforcement model changes. In such cases, you must call `ApplyConsents` or `ApplyAdminConsents` for these changes to take effect.

    * If you can keep track of the Patients with Consent changes, we recommend you to use `PatientScope` filter to avoid re-processing the entire store. This filter is useful to immediately refresh enforcement of a small set of Patients.

    * You can also run `ApplyConsents` periodically using the `TimeRange` filter. This filter is useful when immediate refreshment is not critical. For example, the following request refreshes enforcement for consent changes between UTC 0AM 2022-09-20 and UTC 0AM 2022-09-21.
          
          curl -X POST \
            -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
            -H "Content-Type: application/json" \
            --data "{
               'validateOnly': false,
               'timeRange': {
                 'start': '2022-09-20T00:00:00Z',
                 'end': '2022-09-21T00:00:00Z',
               }
              }" \
            "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:applyConsents"




## Use FHIR consent view

The FHIR Consent Viewer displays access control policies. It provides a table containing consent scopes to represent FHIR Access Control rules.

Before you can use the FHIR Consent Viewer, ensure the following:

  * The FHIR store [`disableResourceVersioning`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.disable_resource_versioning) setting must be `false`. This setting can't be changed after the FHIR store is created. To create a new FHIR store, see [Create a FHIR store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir#creating_a_fhir_store).

  * The FHIR store is configured for consent enforcement.




To view the **FHIR Consent Viewer** , complete the following steps:

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) roles:

**Permissions**

  * `healthcare.fhirStores.get`
  * `healthcare.fhirResources.get`



**Roles**

  * Healthcare FHIR Store Viewer (`roles/healthcare.fhirStoreViewer`) 
  * Healthcare FHIR Resource Reader (`roles/healthcare.fhirResourceReader`) 



You can ask your administrator to grant you these Identity and Access Management roles. For instructions on granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) or [Control access to Cloud Healthcare API resources](https://docs.cloud.google.com/healthcare-api/docs/controlling-access#using_cloud_iam_with_datasets). You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

**Note** : If you created a Google Cloud project for this guide, then, as the project creator, you're automatically granted the Owner (`roles/owner`) IAM role, which has the permissions. You don't need to be granted any additional IAM roles. 

### Console

  1. In the Google Cloud console, go to the **Browser** page.

[Go to Browser](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the FHIR store whose enforced consent policies you want to view.

  3. In the **Data stores** page, in the **Data stores** list, select the FHIR store whose enforced consent policies you want to view.

  4. In the **Data store details** page, click the **Consent** tab. The consent scopes are displayed.




## What's next

  * [Understand enforced policies](https://docs.cloud.google.com/healthcare-api/docs/fhir-access-explain-data-access)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

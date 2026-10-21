---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-custom-parser-examples/
title: Custom schema parser examples \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:12:20.068150+00:00
---

# Custom schema parser examples  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-custom-parser-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Custom schema parser examples Stay organized with collections  Save and categorize content based on your preferences. 

This page contains examples of use cases, ranging from simple to complex, that show when and how to configure a custom schema parser on an HL7v2 store. Each use case contains an HL7v2 message that the custom schema parser is based on.

## Custom segment terminator and custom field

The samples in this section use a sample message that is nonstandard in the following ways:

  * The sample message's segment delimiters are newlines (`\n`) rather than the standard carriage returns (`\r`).
  * The sample message has a software (`SFT`) segment with an additional sub-field: a custom field that specifies the URL `https://example.com/healthcare-api/`.


    
    
    MSH|^~\&|My EHR|My Test Facility||My EHR Facility|20150926140551||ORU^R01^ORU_R01|My-LOI_5.0_1.1-NG|T|2.5.1|||AL|AL|||||\n
    SFT|Google^D|v1|Healthcare API|1||20190601|https://example.com/healthcare-api/\n
    PID|1||PATID5421^^^My MPI^MR||Zhang^Sally^Brian^^^^L||19840611|F||2106-3^White^HL70005|123 Main Street^^Mountain Springs^CO^80439^^H||^PRN^PH^^^203^2290210|||||||||N^Not Hispanic or Latino^HL70189\n
    ORC|RE|833582639|3266238193||CM||||20101234567890\n
    OBR|1|833582639|3266238193|us-0005^Vital Signs^WinPath^^||20101234567890|20101234567890|||||||20101234567890||||||||20101234567890|||F||1\n
    OBX|1|NM|tt-0005-07^MDC_PULS_RATE_NON_INV^MDC^^||52.31|MDC_DIM_BEAT_PER_MIN|50-200||||F|||20101234567890||\n
    OBX|2|NM|tt-0005-12^PAIN LEVEL^L^^||1.71|/10|1-10||||F|||20101234567890||\n
    OBX|3|NM|tt-0005-09^MDC_TEMP^MDC^^||36.22|MDC_DIM_DEGC|36-38||||F|||20101234567890||\n
    

### Update an HL7v2 store with the custom segment terminator

You must specify the [segment terminator](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages#setting_the_segment_terminator) if your messages use a nonstandard terminator like the sample message provided in Custom segment terminator and custom field. The sample message uses the nonstandard `\n` as its segment terminator.

The following samples show how to configure `segmentTerminator` in [`ParserConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserConfig) when you [create an HL7v2 store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2#creating_an_hl7v2_store). The segment terminator is set to `Cg==`, which is the base-64 encoding of `\n`.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the HL7v2 store's parent dataset
  * HL7V2_STORE_ID: the HL7v2 store ID



Request JSON body: 
    
    
    {
      "parserConfig": {
        "segmentTerminator": "Cg==""
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "parserConfig": {
        "segmentTerminator": "Cg==""
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "parserConfig": {
        "segmentTerminator": "Cg==""
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID",
      "parserConfig": {
        "segmentTerminator": "Cg=="
      }
    }
    

### Update an HL7v2 store with the custom schema

You can update an HL7v2 store with a custom schema defined in JSON format. After configuring a custom schema that includes the additional field in the `SFT` segment, you can ingest the sample message. For information about specifying a custom field, see [`SchemaPackage`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#SchemaPackage).

The configuration specified in this sample has the following behavior:

  * Rewrites the `SFT` segment definition to have the URL field as field `7`.
  * The `version` filter determines which incoming messages the custom schema applies to based on a field in the message segment header (`MSH`). If you don't supply a `version` filter, the schema is applied to all HL7v2 messages in the HL7v2 store. In this sample, the custom `SFT` segment applies when the sending application field contains `My EHR`.
  * The field for the additional field is named `7` for consistency with the rest of the specification. You could also name it `URL` to be more descriptive.



To update the store with the custom schema, use the [`projects.locations.datasets.hl7V2Stores.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/patch) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the HL7v2 store's parent dataset
  * HL7V2_STORE_ID: the HL7v2 store ID



Request JSON body: 
    
    
    {
      "parserConfig": {
        "schema": {
          "schematizedParsingType": "HARD_FAIL",
          "types": [
            {
              "version": [
                {
                  "mshField": "3.1",
                  "value": "My EHR"
                }
              ],
              "type": [
                {
                  "name": "SFT",
                  "fields": [
                    {
                      "name": "1",
                      "type": "XON",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "2",
                      "type": "ST",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "3",
                      "type": "ST",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "4",
                      "type": "ST",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "5",
                      "type": "TX",
                      "maxOccurs": 1
                    },
                    {
                      "name": "6",
                      "type": "DTM",
                      "maxOccurs": 1
                    },
                    {
                      "name": "7",
                      "type": "ST",
                      "maxOccurs": 1
                    }
                  ]
                }
              ]
            }
          ]
        },
        "version": "V3"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "parserConfig": {
        "schema": {
          "schematizedParsingType": "HARD_FAIL",
          "types": [
            {
              "version": [
                {
                  "mshField": "3.1",
                  "value": "My EHR"
                }
              ],
              "type": [
                {
                  "name": "SFT",
                  "fields": [
                    {
                      "name": "1",
                      "type": "XON",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "2",
                      "type": "ST",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "3",
                      "type": "ST",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "4",
                      "type": "ST",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "5",
                      "type": "TX",
                      "maxOccurs": 1
                    },
                    {
                      "name": "6",
                      "type": "DTM",
                      "maxOccurs": 1
                    },
                    {
                      "name": "7",
                      "type": "ST",
                      "maxOccurs": 1
                    }
                  ]
                }
              ]
            }
          ]
        },
        "version": "V3"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID?updateMask=parser_config.schema"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "parserConfig": {
        "schema": {
          "schematizedParsingType": "HARD_FAIL",
          "types": [
            {
              "version": [
                {
                  "mshField": "3.1",
                  "value": "My EHR"
                }
              ],
              "type": [
                {
                  "name": "SFT",
                  "fields": [
                    {
                      "name": "1",
                      "type": "XON",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "2",
                      "type": "ST",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "3",
                      "type": "ST",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "4",
                      "type": "ST",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "5",
                      "type": "TX",
                      "maxOccurs": 1
                    },
                    {
                      "name": "6",
                      "type": "DTM",
                      "maxOccurs": 1
                    },
                    {
                      "name": "7",
                      "type": "ST",
                      "maxOccurs": 1
                    }
                  ]
                }
              ]
            }
          ]
        },
        "version": "V3"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID?updateMask=parser_config.schema" | Select-Object -Expand Content

The sample uses the recommended [`V3`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserVersion.ENUM_VALUES.V3) version of the parser. 

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID",
      "parserConfig": {
        "segmentTerminator": "Cg==",
        "schema": {
          "schematizedParsingType": "HARD_FAIL",
          "types": [
            {
              "version": [
                {
                  "mshField": "3.1",
                  "value": "My EHR"
                }
              ],
              "type": [
                {
                  "name": "SFT",
                  "fields": [
                    {
                      "name": "1",
                      "type": "XON",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "2",
                      "type": "ST",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "3",
                      "type": "ST",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "4",
                      "type": "ST",
                      "minOccurs": 1,
                      "maxOccurs": 1
                    },
                    {
                      "name": "5",
                      "type": "TX",
                      "maxOccurs": 1
                    },
                    {
                      "name": "6",
                      "type": "DTM",
                      "maxOccurs": 1
                    },
                    {
                      "name": "7",
                      "type": "ST",
                      "maxOccurs": 1
                    }
                  ]
                }
              ]
            }
          ]
        }
      }
    }
    

### Ingest and parse the HL7v2 message using the custom schema

The following samples show how to ingest a base-64 encoded version of the HL7v2 message from Custom segment terminator and custom field. To ingest the HL7v2 message, you use the [`projects.locations.datasets.hl7V2Stores.messages.ingest`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/ingest) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the HL7v2 store's parent dataset
  * HL7V2_STORE_ID: the HL7v2 store ID



Request JSON body: 
    
    
    {
      "message": {
        "data": "TVNIfF5+XCZ8TXkgRUhSfE15IFRlc3QgRmFjaWxpdHl8fE15IEVIUiBGYWNpbGl0eXwyMDE1MDkyNjE0MDU1MXx8T1JVXlIwMV5PUlVfUjAxfE15LUxPSV81LjBfMS4xLU5HfFR8Mi41LjF8fHxBTHxBTHx8fHx8ClNGVHxHb29nbGVeRHx2MXxIZWFsdGhjYXJlIEFQSXwxfHwyMDE5MDYwMXxodHRwczovL2V4YW1wbGUuY29tL2hlYWx0aGNhcmUvClBJRHwxfDQwOTAzMzEzMjBeXl5TSU1VTEFUT1IgTVJOXk1STnw0MDkwMzMxMzIwXl5eU0lNVUxBVE9SIE1STl5NUk5+Mjg4ODUyNzE1NF5eXk5IU05CUl5OSFNOTUJSfHxEYXZpc15DaGVsc2VhXl5eTWlzc15eQ1VSUkVOVHx8MjAwOTEwMTcwMDAwMDB8Rnx8fDE4MSBUcmFuc21pc3Npb24gUm9hZF5eTG9uZG9uXl5LRzIyIDlIWF5HQlJeSE9NRXx8MDIwIDgxMjIgOTk0N15IT01FfHx8fHx8fHx8SF5Bc2lhbiBvciBBc2lhbiBCcml0aXNoIC0gSW5kaWFuXl5efHx8fHx8fHwKUFYxfDF8SXxPdGhlcldhcmReTWFpblJvb21eQmVkIDFeU2ltdWxhdGVkIEhvc3BpdGFsXl5CRUReTWFpbiBCdWlsZGluZ140fDI4Ynx8fEMwMDNeQ3VkZHleS2V2aW5eXl5Ecl5eXkRSTkJSXlBSU05MXl5eT1JHRFJ8fHxVUk98fHx8fHx8fHwxMjUxMzI0NzIzMjIzODk0ODc4M15eXl52aXNpdGlkfHx8fHx8fHx8fHx8fHx8fHx8fHx8fEFSUklWRUR8fHwyMDIwMDUwNjE3MDgyMnx8Ck9SQ3xSRXw4MzM1ODI2Mzl8MzI2NjIzODE5M3x8Q018fHx8MjAyMDA1MDYxNzA4MjIKT0JSfDF8ODMzNTgyNjM5fDMyNjYyMzgxOTN8dXMtMDAwNV5WaXRhbCBTaWduc15XaW5QYXRoXl58fDIwMjAwNTA2MTcwODIyfDIwMjAwNTA2MTcwODIyfHx8fHx8fDIwMjAwNTA2MTcwODIyfHx8fHx8fHwyMDIwMDUwNjE3MDgyMnx8fEZ8fDEKT0JYfDF8VFh8dHQtMDAwNS0xMV5PeHlnZW5EZXZeV2VsY2hBbGx5bl5efHxWZW50dXJpfHx8fHx8Rnx8fDIwMjAwNTA2MTcwODIyfHwK"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "message": {
        "data": "TVNIfF5+XCZ8TXkgRUhSfE15IFRlc3QgRmFjaWxpdHl8fE15IEVIUiBGYWNpbGl0eXwyMDE1MDkyNjE0MDU1MXx8T1JVXlIwMV5PUlVfUjAxfE15LUxPSV81LjBfMS4xLU5HfFR8Mi41LjF8fHxBTHxBTHx8fHx8ClNGVHxHb29nbGVeRHx2MXxIZWFsdGhjYXJlIEFQSXwxfHwyMDE5MDYwMXxodHRwczovL2V4YW1wbGUuY29tL2hlYWx0aGNhcmUvClBJRHwxfDQwOTAzMzEzMjBeXl5TSU1VTEFUT1IgTVJOXk1STnw0MDkwMzMxMzIwXl5eU0lNVUxBVE9SIE1STl5NUk5+Mjg4ODUyNzE1NF5eXk5IU05CUl5OSFNOTUJSfHxEYXZpc15DaGVsc2VhXl5eTWlzc15eQ1VSUkVOVHx8MjAwOTEwMTcwMDAwMDB8Rnx8fDE4MSBUcmFuc21pc3Npb24gUm9hZF5eTG9uZG9uXl5LRzIyIDlIWF5HQlJeSE9NRXx8MDIwIDgxMjIgOTk0N15IT01FfHx8fHx8fHx8SF5Bc2lhbiBvciBBc2lhbiBCcml0aXNoIC0gSW5kaWFuXl5efHx8fHx8fHwKUFYxfDF8SXxPdGhlcldhcmReTWFpblJvb21eQmVkIDFeU2ltdWxhdGVkIEhvc3BpdGFsXl5CRUReTWFpbiBCdWlsZGluZ140fDI4Ynx8fEMwMDNeQ3VkZHleS2V2aW5eXl5Ecl5eXkRSTkJSXlBSU05MXl5eT1JHRFJ8fHxVUk98fHx8fHx8fHwxMjUxMzI0NzIzMjIzODk0ODc4M15eXl52aXNpdGlkfHx8fHx8fHx8fHx8fHx8fHx8fHx8fEFSUklWRUR8fHwyMDIwMDUwNjE3MDgyMnx8Ck9SQ3xSRXw4MzM1ODI2Mzl8MzI2NjIzODE5M3x8Q018fHx8MjAyMDA1MDYxNzA4MjIKT0JSfDF8ODMzNTgyNjM5fDMyNjYyMzgxOTN8dXMtMDAwNV5WaXRhbCBTaWduc15XaW5QYXRoXl58fDIwMjAwNTA2MTcwODIyfDIwMjAwNTA2MTcwODIyfHx8fHx8fDIwMjAwNTA2MTcwODIyfHx8fHx8fHwyMDIwMDUwNjE3MDgyMnx8fEZ8fDEKT0JYfDF8VFh8dHQtMDAwNS0xMV5PeHlnZW5EZXZeV2VsY2hBbGx5bl5efHxWZW50dXJpfHx8fHx8Rnx8fDIwMjAwNTA2MTcwODIyfHwK"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages:ingest"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "message": {
        "data": "TVNIfF5+XCZ8TXkgRUhSfE15IFRlc3QgRmFjaWxpdHl8fE15IEVIUiBGYWNpbGl0eXwyMDE1MDkyNjE0MDU1MXx8T1JVXlIwMV5PUlVfUjAxfE15LUxPSV81LjBfMS4xLU5HfFR8Mi41LjF8fHxBTHxBTHx8fHx8ClNGVHxHb29nbGVeRHx2MXxIZWFsdGhjYXJlIEFQSXwxfHwyMDE5MDYwMXxodHRwczovL2V4YW1wbGUuY29tL2hlYWx0aGNhcmUvClBJRHwxfDQwOTAzMzEzMjBeXl5TSU1VTEFUT1IgTVJOXk1STnw0MDkwMzMxMzIwXl5eU0lNVUxBVE9SIE1STl5NUk5+Mjg4ODUyNzE1NF5eXk5IU05CUl5OSFNOTUJSfHxEYXZpc15DaGVsc2VhXl5eTWlzc15eQ1VSUkVOVHx8MjAwOTEwMTcwMDAwMDB8Rnx8fDE4MSBUcmFuc21pc3Npb24gUm9hZF5eTG9uZG9uXl5LRzIyIDlIWF5HQlJeSE9NRXx8MDIwIDgxMjIgOTk0N15IT01FfHx8fHx8fHx8SF5Bc2lhbiBvciBBc2lhbiBCcml0aXNoIC0gSW5kaWFuXl5efHx8fHx8fHwKUFYxfDF8SXxPdGhlcldhcmReTWFpblJvb21eQmVkIDFeU2ltdWxhdGVkIEhvc3BpdGFsXl5CRUReTWFpbiBCdWlsZGluZ140fDI4Ynx8fEMwMDNeQ3VkZHleS2V2aW5eXl5Ecl5eXkRSTkJSXlBSU05MXl5eT1JHRFJ8fHxVUk98fHx8fHx8fHwxMjUxMzI0NzIzMjIzODk0ODc4M15eXl52aXNpdGlkfHx8fHx8fHx8fHx8fHx8fHx8fHx8fEFSUklWRUR8fHwyMDIwMDUwNjE3MDgyMnx8Ck9SQ3xSRXw4MzM1ODI2Mzl8MzI2NjIzODE5M3x8Q018fHx8MjAyMDA1MDYxNzA4MjIKT0JSfDF8ODMzNTgyNjM5fDMyNjYyMzgxOTN8dXMtMDAwNV5WaXRhbCBTaWduc15XaW5QYXRoXl58fDIwMjAwNTA2MTcwODIyfDIwMjAwNTA2MTcwODIyfHx8fHx8fDIwMjAwNTA2MTcwODIyfHx8fHx8fHwyMDIwMDUwNjE3MDgyMnx8fEZ8fDEKT0JYfDF8VFh8dHQtMDAwNS0xMV5PeHlnZW5EZXZeV2VsY2hBbGx5bl5efHxWZW50dXJpfHx8fHx8Rnx8fDIwMjAwNTA2MTcwODIyfHwK"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages:ingest" | Select-Object -Expand Content

Because the schema of the HL7v2 message matches the schema of the HL7v2 store, the response contains a JSON string with the custom URL in the `ORU_R01.SFT.7` field. 

#### Response
    
    
    {
      "hl7Ack": "TVNIfF5+XCZ8fE15IEVIUiBGYWNpbGl0eXxNeSBFSFJ8TXkgVGVzdCBGYWNpbGl0eXwyMDIwMDUwNjIxNDY1MXx8QUNLfDcwY2IxMjJhLTUxYzctNGFkYy04NzFkLWZlMzJjZTgxYzI5OHxUfDIuNS4xDU1TQXxBQXxNeS1MT0lfNS4wXzEuMS1ORw==",
      "message": {
        "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/HL7V2_MESSAGE_ID",
        "data": "TVNIfF5+XCZ8TXkgRUhSfE15IFRlc3QgRmFjaWxpdHl8fE15IEVIUiBGYWNpbGl0eXwyMDE1MDkyNjE0MDU1MXx8T1JVXlIwMV5PUlVfUjAxfE15LUxPSV81LjBfMS4xLU5HfFR8Mi41LjF8fHxBTHxBTHx8fHx8ClNGVHxHb29nbGVeRHx2MXxIZWFsdGhjYXJlIEFQSXwxfHwyMDE5MDYwMXxodHRwczovL2V4YW1wbGUuY29tL2hlYWx0aGNhcmUvClBJRHwxfHxQQVRJRDU0MjFeXl5NeSBNUEleTVJ8fFpoYW5nXlNhbGx5XkJyaWFuXl5eXkx8fDE5ODQwNjExfEZ8fDIxMDYtM15XaGl0ZV5ITDcwMDA1fDEyMyBNYWluIFN0cmVldF5eTW91bnRhaW4gU3ByaW5nc15DT144MDQzOV5eSHx8XlBSTl5QSF5eXjIwM14yMjkwMjEwfHx8fHx8fHx8Tl5Ob3QgSGlzcGFuaWMgb3IgTGF0aW5vXkhMNzAxODkKT1JDfFJFfDgzMzU4MjYzOXwzMjY2MjM4MTkzfHxDTXx8fHwyMDIwMDUwNjE3MDgyMgpPQlJ8MXw4MzM1ODI2Mzl8MzI2NjIzODE5M3x1cy0wMDA1XlZpdGFsIFNpZ25zXldpblBhdGheXnx8MjAyMDA1MDYxNzA4MjJ8MjAyMDA1MDYxNzA4MjJ8fHx8fHx8MjAyMDA1MDYxNzA4MjJ8fHx8fHx8fDIwMjAwNTA2MTcwODIyfHx8Rnx8MQpPQlh8MXxOTXx0dC0wMDA1LTA3Xk1EQ19QVUxTX1JBVEVfTk9OX0lOVl5NRENeXnx8NTIuMzF8TURDX0RJTV9CRUFUX1BFUl9NSU58NTAtMjAwfHx8fEZ8fHwyMDIwMDUwNjE3MDgyMnx8Ck9CWHwyfE5NfHR0LTAwMDUtMTJeUEFJTiBMRVZFTF5MXl58fDEuNzF8LzEwfDEtMTB8fHx8Rnx8fDIwMjAwNTA2MTcwODIyfHwKT0JYfDN8Tk18dHQtMDAwNS0wOV5NRENfVEVNUF5NRENeXnx8MzYuMjJ8TURDX0RJTV9ERUdDfDM2LTM4fHx8fEZ8fHwyMDIwMDUwNjE3MDgyMnx8Cg==",
        "sendFacility": "My Test Facility",
        "sendTime": "2015-09-26T14:05:51Z",
        "messageType": "ORU",
        "createTime": "CREATE_TIME",
        "patientIds": [
          {
            "value": "PATID5421",
            "type": "MR"
          }
        ],
        "schematizedData": {
          "data": {
            \"ORU_R01\": {
              \"DSC\": null,
              \"MSH\": {
                \"0\": \"MSH\",
                \"1\": \"|\",
                \"2\": \"^~\\\\\\u0026\",
                \"3\": {
                  \"1\": \"My EHR\"
                },
                \"4\": {
                  \"1\": \"My Test Facility\"
                },
                \"5\": null,
                \"6\": {
                  \"1\": \"My EHR Facility\"
                },
                \"7\": \"20150926140551\",
                \"8\": null,
                \"9\": {
                  \"1\": \"ORU\",
                  \"2\": \"R01\",
                  \"3\": \"ORU_R01\"
                },
                \"10\": \"My-LOI_5.0_1.1-NG\",
                \"11\": {
                  \"1\": \"T\"
                },
                \"12\": {
                  \"1\": \"2.5.1\"
                },
                \"13\": null,
                \"14\": null,
                \"15\": \"AL\",
                \"16\": \"AL\",
                \"17\": null,
                \"18\": null,
                \"19\": null,
                \"20\": null,
                \"21\": null
              },
              \"PATIENT_RESULT\": [
                {
                  \"ORDER_OBSERVATION\": [
                    {
                      \"COMMON_ORDER\": {
                        \"ORC\": {
                          \"0\": \"ORC\",
                          \"1\": \"RE\",
                          \"2\": {
                            \"1\": \"833582639\"
                          },
                          \"3\": {
                            \"1\": \"3266238193\"
                          },
                          \"4\": null,
                          \"5\": \"CM\",
                          \"6\": null,
                          \"7\": null,
                          \"8\": null,
                          \"9\": \"CREATE_TIME\"
                        },
                        \"ORDER_DOCUMENT\": null,
                        \"PRT\": null
                      },
                      \"CTD\": null,
                      \"CTI\": null,
                      \"FT1\": null,
                      \"NTE\": null,
                      \"OBR\": {
                        \"0\": \"OBR\",
                        \"1\": \"1\",
                        \"2\": {
                          \"1\": \"833582639\"
                        },
                        \"3\": {
                          \"1\": \"3266238193\"
                        },
                        \"4\": {
                          \"1\": \"us-0005\",
                          \"2\": \"Vital Signs\",
                          \"3\": \"WinPath\",
                          \"4\": null,
                          \"5\": null
                        },
                        \"5\": null,
                        \"6\": \"CREATE_TIME\",
                        \"7\": \"CREATE_TIME\",
                        \"8\": null,
                        \"9\": null,
                        \"10\": null,
                        \"11\": null,
                        \"12\": null,
                        \"13\": null,
                        \"14\": \"CREATE_TIME\",
                        \"15\": null,
                        \"16\": null,
                        \"17\": null,
                        \"18\": null,
                        \"19\": null,
                        \"20\": null,
                        \"21\": null,
                        \"22\": \"CREATE_TIME\",
                        \"23\": null,
                        \"24\": null,
                        \"25\": \"F\",
                        \"26\": null,
                        \"27\": [
                          {
                            \"1\": {
                              \"1\": \"1\"
                            }
                          }
                        ]
                      },
                      \"OBSERVATION\": [
                        {
                          \"NTE\": null,
                          \"OBX\": {
                            \"0\": \"OBX\",
                            \"1\": \"1\",
                            \"2\": \"NM\",
                            \"3\": {
                              \"1\": \"tt-0005-07\",
                              \"2\": \"MDC_PULS_RATE_NON_INV\",
                              \"3\": \"MDC\",
                              \"4\": null,
                              \"5\": null
                            },
                            \"4\": null,
                            \"5\": [
                              {
                                \"1\": {
                                  \"1\": \"52.31\"
                                }
                              }
                            ],
                            \"6\": {
                              \"1\": \"MDC_DIM_BEAT_PER_MIN\"
                            },
                            \"7\": \"50-200\",
                            \"8\": null,
                            \"9\": null,
                            \"10\": null,
                            \"11\": \"F\",
                            \"12\": null,
                            \"13\": null,
                            \"14\": \"CREATE_TIME\",
                            \"15\": null,
                            \"16\": null
                          },
                          \"PRT\": null
                        },
                        {
                          \"NTE\": null,
                          \"OBX\": {
                            \"0\": \"OBX\",
                            \"1\": \"2\",
                            \"2\": \"NM\",
                            \"3\": {
                              \"1\": \"tt-0005-12\",
                              \"2\": \"PAIN LEVEL\",
                              \"3\": \"L\",
                              \"4\": null,
                              \"5\": null
                            },
                            \"4\": null,
                            \"5\": [
                              {
                                \"1\": {
                                  \"1\": \"1.71\"
                                }
                              }
                            ],
                            \"6\": {
                              \"1\": \"/10\"
                            },
                            \"7\": \"1-10\",
                            \"8\": null,
                            \"9\": null,
                            \"10\": null,
                            \"11\": \"F\",
                            \"12\": null,
                            \"13\": null,
                            \"14\": \"CREATE_TIME\",
                            \"15\": null,
                            \"16\": null
                          },
                          \"PRT\": null
                        },
                        {
                          \"NTE\": null,
                          \"OBX\": {
                            \"0\": \"OBX\",
                            \"1\": \"3\",
                            \"2\": \"NM\",
                            \"3\": {
                              \"1\": \"tt-0005-09\",
                              \"2\": \"MDC_TEMP\",
                              \"3\": \"MDC\",
                              \"4\": null,
                              \"5\": null
                            },
                            \"4\": null,
                            \"5\": [
                              {
                                \"1\": {
                                  \"1\": \"36.22\"
                                }
                              }
                            ],
                            \"6\": {
                              \"1\": \"MDC_DIM_DEGC\"
                            },
                            \"7\": \"36-38\",
                            \"8\": null,
                            \"9\": null,
                            \"10\": null,
                            \"11\": \"F\",
                            \"12\": null,
                            \"13\": null,
                            \"14\": \"CREATE_TIME\",
                            \"15\": null,
                            \"16\": null
                          },
                          \"PRT\": null
                        }
                      ],
                      \"PRT\": null,
                      \"SPECIMEN\": null,
                      \"TIMING_QTY\": null
                    }
                  ],
                  \"PATIENT\": {
                    \"ARV\": null,
                    \"NK1\": null,
                    \"NTE\": null,
                    \"PATIENT_OBSERVATION\": null,
                    \"PD1\": null,
                    \"PID\": {
                      \"0\": \"PID\",
                      \"1\": \"1\",
                      \"2\": null,
                      \"3\": [
                        {
                          \"1\": \"PATID5421\",
                          \"2\": null,
                          \"3\": null,
                          \"4\": {
                            \"1\": \"My MPI\"
                          },
                          \"5\": \"MR\"
                        }
                      ],
                      \"4\": null,
                      \"5\": [
                        {
                          \"1\": {
                            \"1\": \"Zhang\"
                          },
                          \"2\": \"Sally\",
                          \"3\": \"Brian\",
                          \"4\": null,
                          \"5\": null,
                          \"6\": null,
                          \"7\": \"L\"
                        }
                      ],
                      \"6\": null,
                      \"7\": \"19840611\",
                      \"8\": {
                        \"1\": \"F\"
                      },
                      \"9\": null,
                      \"10\": [
                        {
                          \"1\": \"2106-3\",
                          \"2\": \"White\",
                          \"3\": \"HL70005\"
                        }
                      ],
                      \"11\": [
                        {
                          \"1\": {
                            \"1\": \"123 Main Street\"
                          },
                          \"2\": null,
                          \"3\": \"Mountain Springs\",
                          \"4\": \"CO\",
                          \"5\": \"80439\",
                          \"6\": null,
                          \"7\": \"H\"
                        }
                      ],
                      \"12\": null,
                      \"13\": [
                        {
                          \"1\": null,
                          \"2\": \"PRN\",
                          \"3\": \"PH\",
                          \"4\": null,
                          \"5\": null,
                          \"6\": \"203\",
                          \"7\": \"2290210\"
                        }
                      ],
                      \"14\": null,
                      \"15\": null,
                      \"16\": null,
                      \"17\": null,
                      \"18\": null,
                      \"19\": null,
                      \"20\": null,
                      \"21\": null,
                      \"22\": [
                        {
                          \"1\": \"N\",
                          \"2\": \"Not Hispanic or Latino\",
                          \"3\": \"HL70189\"
                        }
                      ]
                    },
                    \"PRT\": null,
                    \"VISIT\": null
                  }
                }
              ],
              \"SFT\": [
                {
                  \"0\": \"SFT\",
                  \"1\": {
                    \"1\": \"Google\",
                    \"2\": {
                      \"1\": \"D\"
                    }
                  },
                  \"2\": \"v1\",
                  \"3\": \"Healthcare API\",
                  \"4\": \"1\",
                  \"5\": {
                    \"1\": {
                      \"1\": \"\"
                    }
                  },
                  \"6\": \"20190601\",
                  \"7\": \"https://example.com/healthcare-api/\"
                }
              ],
              \"UAC\": null
            }
          }"
        }
      }
    }
    

## Parser heuristics using a custom segment

The following sample shows how the HL7v2 parser uses heuristics to parse a message with minor configuration on the HL7v2 store.

The sample uses the following HL7v2 message:
    
    
    MSH|^~\&$|||||||ADT^A01|||2.1
    EVN|\P\\L\\H\\N\
    PID|1
    ZCD|1
    

The HL7v2 message is non-standard because the `ZCD` segment is not defined in the HL7v2 standard.

### Create an HL7v2 store with the custom schema

To create an HL7v2 store with the custom schema, use the [`projects.locations.datasets.hl7V2Stores.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/create) method.

Note that the configuration only uses the following three fields and no `schemas` or `types` array:

  * `"unexpectedSegmentHandling": "PARSE"`
  * `"ignoreMinOccurs": "true"`
  * `"schematizedParsingType": "HARD_FAIL"`



Without specifying anything else about the message definition or its types, the HL7v2 parser determines that the message is an `ADT_A01` message and parses the `MSH`, `EVN`, and `PID` segments, and the custom `ZCD` segment.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the HL7v2 store's parent dataset
  * HL7V2_STORE_ID: the HL7v2 store ID



Request JSON body: 
    
    
    {
      "parserConfig": {
        "schema": {
          "unexpectedSegmentHandling": "PARSE",
          "ignoreMinOccurs": "true",
          "schematizedParsingType": "HARD_FAIL"
        }
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "parserConfig": {
        "schema": {
          "unexpectedSegmentHandling": "PARSE",
          "ignoreMinOccurs": "true",
          "schematizedParsingType": "HARD_FAIL"
        }
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores?hl7V2StoreId=HL7V2_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "parserConfig": {
        "schema": {
          "unexpectedSegmentHandling": "PARSE",
          "ignoreMinOccurs": "true",
          "schematizedParsingType": "HARD_FAIL"
        }
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores?hl7V2StoreId=HL7V2_STORE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID",
      "parserConfig": {
        "schema": {
          "schematizedParsingType": "HARD_FAIL",
          "ignoreMinOccurs": true,
          "unexpectedSegmentHandling": "PARSE"
        }
      }
    }
    

### Ingest and parse the HL7v2 message using the custom schema

Ingest the base 64-encoded version of the HL7v2 message.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the HL7v2 store's parent dataset
  * HL7V2_STORE_ID: the HL7v2 store ID



Request JSON body: 
    
    
    {
      "message": {
        "data": "TVNIfF5+XCYkfHx8fHx8fEFEVF5BMDF8fHwyLjENRVZOfFxQXExcSFxOXA1QSUR8MQ1aQ0R8MQ=="
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "message": {
        "data": "TVNIfF5+XCYkfHx8fHx8fEFEVF5BMDF8fHwyLjENRVZOfFxQXExcSFxOXA1QSUR8MQ1aQ0R8MQ=="
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages:ingest"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "message": {
        "data": "TVNIfF5+XCYkfHx8fHx8fEFEVF5BMDF8fHwyLjENRVZOfFxQXExcSFxOXA1QSUR8MQ1aQ0R8MQ=="
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages:ingest" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "hl7Ack": "TVNIfF5+XCZ8fHx8fDIwMjIwMzE0MjExMTM1fHxBQ0t8Mjk1MmMxNDctZjczNS00MzczLWFmOTktNDgzNDRlODIwODJkfHwyLjENTVNBfEFB",
      "message": {
        "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/HL7V2_MESSAGE_ID",
        "data": "TVNIfF5+XCYkfHx8fHx8fEFEVF5BMDF8fHwyLjENRVZOfFxQXExcSFxOXA1QSUR8MQ1aQ0R8MQ==",
        "messageType": "ADT",
        "createTime": "CREATE_TIME",
        "schematizedData": {
          "data": "{\"ADT_A01\":{\"ACC\":null,\"AL1\":null,\"ARV_1\":null,\"ARV_2\":null,\"DB1\":null,\"DG1\":null,\"DRG\":null,\"EVN\":[{\"0\":\"EVN\",\"1\":\"LN\\\\\"}],\"GT1\":null,\"INSURANCE\":null,\"MSH\":{\"0\":\"MSH\",\"1\":\"|\",\"10\":null,\"11\":null,\"12\":{\"1\":\"2.1\"},\"2\":\"^~\\\\\\u0026$\",\"3\":null,\"4\":null,\"5\":null,\"6\":null,\"7\":null,\"8\":null,\"9\":{\"1\":\"ADT\",\"2\":\"A01\"}},\"NK1\":null,\"OBX\":null,\"PD1\":null,\"PDA\":null,\"PID\":[{\"0\":\"PID\",\"1\":\"1\"}],\"PROCEDURE\":null,\"PV1\":null,\"PV2\":null,\"ROL_1\":null,\"ROL_2\":null,\"SFT\":null,\"UAC\":null,\"UB1\":null,\"UB2\":null,\"ZCD\":[{\"0\":[{\"1\":{\"1\":\"ZCD\"}}],\"1\":[{\"1\":{\"1\":\"1\"}}]}]}}"
        }
      }
    }
    

## Parser using an HL7v2 message with missing fields

The following sample shows how to use type and group definitions to parse this HL7v2 message:
    
    
    MSH|^~\&|||||20100101000000||ORM^O01^O01|23701|1|2.3||
    PID|11|SMITH
    PV1|11
    PID|22|JOHN
    PV1|22
    ORC|3
    OBX|4
    NTE|5
    NTE|6
    OBX|7
    NTE|8
    

The HL7v2 message is non-standard because it only uses a few fields (in some cases a single field) in all segments except `MSH`. For example, the HL7v2 standard requires the `PID` segment to contain fields such as the patient's primary language, address, and date of birth, but the `PID` segments in the sample message only contain an ID for the patient and the patient's first or last name.

The HL7v2 message follows the HL7 syntax, but is otherwise nearly entirely customized.

### Create an HL7v2 store with the custom schema

Before creating an HL7v2 store with the custom schema, read through the following properties of the `ParserConfig` object which is used in the schema:

`schemas` array:

  * The `mshField` is set to the 12th field (separated by a pipe `|` character) of the first segment in the message. The value of the field is `2.3`. As a result, the `schema` you supply to the HL7v2 store will apply to any HL7v2 message corresponding to the `mshField` and `value`.
  * The message type, `ORM`, is specified with a `members` array containing the following information: 
    * The segment type for the `ORM` message is the message segment header, or `MSH`
    * A group named "Patient" which has a `maxOccurs` of 2. 
      * Another `members` group nested under the "Patient" group that contains the type of segment that matches to the "Patient" group. That segment type is `PID`.
      * Another group named "Patient Visit". Like "Patient", there is a segment matching "Patient Visit". That segment type is `PV1`.
    * A group named "Order" which has no maximum or minimum of occurrences. 
      * Another `members` group nested under the "Order" group that contains the type of segment that matches to the "Order" group. That segment type is `ORC`.
      * Another group named "Observation", which has its own `members` array. 
        * The `members` array contains two segments that map to "Observation": `OBX` and `NTE`. `OBX` has a `maxOccurs` of `1`.



`types` array:

  * Like the `schemas` array, `mshField` is set to the 12th field (separated by a pipe `|` character) of the first segment in the message. The value of the field is `2.3`. As a result, the `types` you supply to the HL7v2 store will apply to any HL7v2 message corresponding to the `mshField` and `value`.
  * The `ST` and `SI` data types are declared as `STRING` primitives. Because only `ST` and `SI` are declared, you can tell that the message has no custom types.
  * The `Patient` group has a `maxOccurs` of `2` and a segment type of `PID`, so two types are declared in the fields `PID`. Both types are `SI`.
  * The remaining segment types are listed with their relevant fields and types. All of the remaining segments have a single occurrence and use the `SI` type.



Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the HL7v2 store's parent dataset
  * HL7V2_STORE_ID: the HL7v2 store ID



Request JSON body: 
    
    
    {
      "parserConfig": {
        "schema": {
          "schematizedParsingType": "HARD_FAIL",
          "unexpectedSegmentHandling": "PARSE",
          "schemas": [
            {
              "version": [
                {
                  "mshField": "12",
                  "value": "2.3"
                }
              ],
              "messageSchemaConfigs": {
                "ORM_O01": {
                  "name": "ORM_O01",
                  "members": [
                    {
                      "segment": {
                        "type": "MSH"
                      }
                    },
                    {
                      "group": {
                        "name": "Patient",
                        "maxOccurs": 2,
                        "members": [
                          {
                            "segment": {
                              "type": "PID"
                            }
                          },
                          {
                            "group": {
                              "name": "Patient Visit",
                              "members": [
                                {
                                  "segment": {
                                    "type": "PV1"
                                  }
                                }
                              ]
                            }
                          }
                        ]
                      }
                    },
                    {
                      "group": {
                        "name": "Order",
                        "members": [
                          {
                            "segment": {
                              "type": "ORC"
                            }
                          },
                          {
                            "group": {
                              "name": "Observation",
                              "members": [
                                {
                                  "segment": {
                                    "type": "OBX",
                                    "maxOccurs": 1
                                  }
                                },
                                {
                                  "segment": {
                                    "type": "NTE"
                                  }
                                }
                              ]
                            }
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            }
          ],
          "types": [
            {
              "version": [
                {
                  "mshField": "12",
                  "value": "2.3"
                }
              ],
              "type": [
                {
                  "name": "ST",
                  "primitive": "STRING"
                },
                {
                  "name": "SI",
                  "primitive": "STRING"
                },
                {
                  "name": "PID",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    },
                    {
                      "name": "2",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "PV1",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "ORC",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "OBX",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "NTE",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                }
              ]
            }
          ],
        },
        "version": "V3"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "parserConfig": {
        "schema": {
          "schematizedParsingType": "HARD_FAIL",
          "unexpectedSegmentHandling": "PARSE",
          "schemas": [
            {
              "version": [
                {
                  "mshField": "12",
                  "value": "2.3"
                }
              ],
              "messageSchemaConfigs": {
                "ORM_O01": {
                  "name": "ORM_O01",
                  "members": [
                    {
                      "segment": {
                        "type": "MSH"
                      }
                    },
                    {
                      "group": {
                        "name": "Patient",
                        "maxOccurs": 2,
                        "members": [
                          {
                            "segment": {
                              "type": "PID"
                            }
                          },
                          {
                            "group": {
                              "name": "Patient Visit",
                              "members": [
                                {
                                  "segment": {
                                    "type": "PV1"
                                  }
                                }
                              ]
                            }
                          }
                        ]
                      }
                    },
                    {
                      "group": {
                        "name": "Order",
                        "members": [
                          {
                            "segment": {
                              "type": "ORC"
                            }
                          },
                          {
                            "group": {
                              "name": "Observation",
                              "members": [
                                {
                                  "segment": {
                                    "type": "OBX",
                                    "maxOccurs": 1
                                  }
                                },
                                {
                                  "segment": {
                                    "type": "NTE"
                                  }
                                }
                              ]
                            }
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            }
          ],
          "types": [
            {
              "version": [
                {
                  "mshField": "12",
                  "value": "2.3"
                }
              ],
              "type": [
                {
                  "name": "ST",
                  "primitive": "STRING"
                },
                {
                  "name": "SI",
                  "primitive": "STRING"
                },
                {
                  "name": "PID",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    },
                    {
                      "name": "2",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "PV1",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "ORC",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "OBX",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "NTE",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                }
              ]
            }
          ],
        },
        "version": "V3"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores?hl7V2StoreId=HL7V2_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "parserConfig": {
        "schema": {
          "schematizedParsingType": "HARD_FAIL",
          "unexpectedSegmentHandling": "PARSE",
          "schemas": [
            {
              "version": [
                {
                  "mshField": "12",
                  "value": "2.3"
                }
              ],
              "messageSchemaConfigs": {
                "ORM_O01": {
                  "name": "ORM_O01",
                  "members": [
                    {
                      "segment": {
                        "type": "MSH"
                      }
                    },
                    {
                      "group": {
                        "name": "Patient",
                        "maxOccurs": 2,
                        "members": [
                          {
                            "segment": {
                              "type": "PID"
                            }
                          },
                          {
                            "group": {
                              "name": "Patient Visit",
                              "members": [
                                {
                                  "segment": {
                                    "type": "PV1"
                                  }
                                }
                              ]
                            }
                          }
                        ]
                      }
                    },
                    {
                      "group": {
                        "name": "Order",
                        "members": [
                          {
                            "segment": {
                              "type": "ORC"
                            }
                          },
                          {
                            "group": {
                              "name": "Observation",
                              "members": [
                                {
                                  "segment": {
                                    "type": "OBX",
                                    "maxOccurs": 1
                                  }
                                },
                                {
                                  "segment": {
                                    "type": "NTE"
                                  }
                                }
                              ]
                            }
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            }
          ],
          "types": [
            {
              "version": [
                {
                  "mshField": "12",
                  "value": "2.3"
                }
              ],
              "type": [
                {
                  "name": "ST",
                  "primitive": "STRING"
                },
                {
                  "name": "SI",
                  "primitive": "STRING"
                },
                {
                  "name": "PID",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    },
                    {
                      "name": "2",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "PV1",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "ORC",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "OBX",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "NTE",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                }
              ]
            }
          ],
        },
        "version": "V3"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores?hl7V2StoreId=HL7V2_STORE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID",
      "parserConfig": {
        "schema": {
          "schematizedParsingType": "HARD_FAIL",
          "schemas": [
            {
              "version": [
                {
                  "mshField": "12",
                  "value": "2.3"
                }
              ],
              "messageSchemaConfigs": {
                "ORM_O01": {
                  "name": "ORM_O01",
                  "members": [
                    {
                      "segment": {
                        "type": "MSH"
                      }
                    },
                    {
                      "group": {
                        "name": "Patient",
                        "maxOccurs": 2,
                        "members": [
                          {
                            "segment": {
                              "type": "PID"
                            }
                          },
                          {
                            "group": {
                              "name": "Patient Visit",
                              "members": [
                                {
                                  "segment": {
                                    "type": "PV1"
                                  }
                                }
                              ]
                            }
                          }
                        ]
                      }
                    },
                    {
                      "group": {
                        "name": "Order",
                        "members": [
                          {
                            "segment": {
                              "type": "ORC"
                            }
                          },
                          {
                            "group": {
                              "name": "Observation",
                              "members": [
                                {
                                  "segment": {
                                    "type": "OBX",
                                    "maxOccurs": 1
                                  }
                                },
                                {
                                  "segment": {
                                    "type": "NTE"
                                  }
                                }
                              ]
                            }
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            }
          ],
          "types": [
            {
              "version": [
                {
                  "mshField": "12",
                  "value": "2.3"
                }
              ],
              "type": [
                {
                  "name": "ST",
                  "primitive": "STRING"
                },
                {
                  "name": "SI",
                  "primitive": "STRING"
                },
                {
                  "name": "PID",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    },
                    {
                      "name": "2",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "PV1",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "ORC",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "OBX",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                },
                {
                  "name": "NTE",
                  "fields": [
                    {
                      "name": "1",
                      "type": "SI"
                    }
                  ]
                }
              ]
            }
          ],
          "unexpectedSegmentHandling": "PARSE"
        },
        "version": "V3"
      }
    }
    

### Ingest and parse the HL7v2 message using the custom schema

Ingest a base64-encoded version of the HL7v2 message.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the HL7v2 store's parent dataset
  * HL7V2_STORE_ID: the HL7v2 store ID



Request JSON body: 
    
    
    {
      "message": {
        "data": "TVNIfF5+XCZ8fHx8fDIwMTAwMTAxMDAwMDAwfHxPUk1eTzAxXk8wMXwyMzcwMXwxfDIuM3x8DVBJRHwxMXxTTUlUSA1QVjF8MTENUElEfDIyfEpPSE4NUFYxfDIyDU9SQ3wzDU9CWHw0DU5URXw1DU5URXw2DU9CWHw3DU5URXw4"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "message": {
        "data": "TVNIfF5+XCZ8fHx8fDIwMTAwMTAxMDAwMDAwfHxPUk1eTzAxXk8wMXwyMzcwMXwxfDIuM3x8DVBJRHwxMXxTTUlUSA1QVjF8MTENUElEfDIyfEpPSE4NUFYxfDIyDU9SQ3wzDU9CWHw0DU5URXw1DU5URXw2DU9CWHw3DU5URXw4"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages:ingest"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "message": {
        "data": "TVNIfF5+XCZ8fHx8fDIwMTAwMTAxMDAwMDAwfHxPUk1eTzAxXk8wMXwyMzcwMXwxfDIuM3x8DVBJRHwxMXxTTUlUSA1QVjF8MTENUElEfDIyfEpPSE4NUFYxfDIyDU9SQ3wzDU9CWHw0DU5URXw1DU5URXw2DU9CWHw3DU5URXw4"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages:ingest" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "hl7Ack": "TVNIfF5+XCZ8fHx8fDIwMjIwMzE0MjE1NzU3fHxBQ0t8NGU4NjIyMDMtZTA3OC00YjhlLWExOWYtNzA3ZjhkNTk5OTY2fDF8Mi4zDU1TQXxBQXwyMzcwMQ==",
      "message": {
        "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/HL7V2_MESSAGE_ID",
        "data": "TVNIfF5+XCZ8fHx8fDIwMTAwMTAxMDAwMDAwfHxPUk1eTzAxXk8wMXwyMzcwMXwxfDIuM3x8DVBJRHwxMXxTTUlUSA1QVjF8MTENUElEfDIyfEpPSE4NUFYxfDIyDU9SQ3wzDU9CWHw0DU5URXw1DU5URXw2DU9CWHw3DU5URXw4",
        "sendTime": "2010-01-01T00:00:00Z",
        "messageType": "ORM",
        "createTime": "CREATE_TIME",
        "schematizedData": {
          "data": {
            "ORM_O01": [
              {
                "MSH": [
                  {
                    "0": "MSH",
                    "1": "|",
                    "2": "^~\\\\\\u0026",
                    "3": null,
                    "4": null,
                    "5": null,
                    "6": null,
                    "7": "20100101000000",
                    "8": null,
                    "9": {
                      "1": "ORM",
                      "2": "O01",
                      "3": "O01"
                    },
                    "10": "23701",
                    "11": {
                      "1": "1"
                    },
                    "12": {
                      "1": "2.3"
                    },
                    "13": null,
                    "14": null
                  }
                ],
                "Order": [
                  {
                    "ORC": [
                      {
                        "0": "ORC",
                        "1": [
                          "3"
                        ]
                      }
                    ],
                    "Observation": [
                      {
                        "NTE": [
                          {
                            "0": "NTE",
                            "1": [
                              "5"
                            ]
                          },
                          {
                            "0": "NTE",
                            "1": [
                              "6"
                            ]
                          }
                        ],
                        "OBX": {
                          "0": "OBX",
                          "1": [
                            "4"
                          ]
                        }
                      },
                      {
                        "NTE": [
                          {
                            "0": "NTE",
                            "1": [
                              "8"
                            ]
                          }
                        ],
                        "OBX": {
                          "0": "OBX",
                          "1": [
                            "7"
                          ]
                        }
                      }
                    ]
                  }
                ],
                "Patient": [
                  {
                    "PID": [
                      {
                        "0": "PID",
                        "1": [
                          "11"
                        ],
                        "2": [
                          "SMITH"
                        ]
                      }
                    ],
                    "Patient Visit": [
                      {
                        "PV1": [
                          {
                            "0": "PV1",
                            "1": [
                              "11"
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "PID": [
                      {
                        "0": "PID",
                        "1": [
                          "22"
                        ],
                        "2": [
                          "JOHN"
                        ]
                      }
                    ],
                    "Patient Visit": [
                      {
                        "PV1": [
                          {
                            "0": "PV1",
                            "1": [
                              "22"
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        }
      }
    }
    

For a more readable version of the `data` field in the response, expand the following section:

#### Expand
    
    
    {
      "data": {
        "ORM_O01": [
          {
            "MSH": [
              {
                "0": "MSH",
                "1": "|",
                "2": "^~\\\\\\u0026",
                "3": null,
                "4": null,
                "5": null,
                "6": null,
                "7": "20100101000000",
                "8": null,
                "9": {
                  "1": "ORM",
                  "2": "O01",
                  "3": "O01"
                },
                "10": "23701",
                "11": {
                  "1": "1"
                },
                "12": {
                  "1": "2.3"
                },
                "13": null,
                "14": null
              }
            ],
            "Order": [
              {
                "ORC": [
                  {
                    "0": "ORC",
                    "1": [
                      "3"
                    ]
                  }
                ],
                "Observation": [
                  {
                    "NTE": [
                      {
                        "0": "NTE",
                        "1": [
                          "5"
                        ]
                      },
                      {
                        "0": "NTE",
                        "1": [
                          "6"
                        ]
                      }
                    ],
                    "OBX": {
                      "0": "OBX",
                      "1": [
                        "4"
                      ]
                    }
                  },
                  {
                    "NTE": [
                      {
                        "0": "NTE",
                        "1": [
                          "8"
                        ]
                      }
                    ],
                    "OBX": {
                      "0": "OBX",
                      "1": [
                        "7"
                      ]
                    }
                  }
                ]
              }
            ],
            "Patient": [
              {
                "PID": [
                  {
                    "0": "PID",
                    "1": [
                      "11"
                    ],
                    "2": [
                      "SMITH"
                    ]
                  }
                ],
                "Patient Visit": [
                  {
                    "PV1": [
                      {
                        "0": "PV1",
                        "1": [
                          "11"
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "PID": [
                  {
                    "0": "PID",
                    "1": [
                      "22"
                    ],
                    "2": [
                      "JOHN"
                    ]
                  }
                ],
                "Patient Visit": [
                  {
                    "PV1": [
                      {
                        "0": "PV1",
                        "1": [
                          "22"
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

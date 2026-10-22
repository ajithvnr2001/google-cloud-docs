---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-default-parser/
title: Enable schematized parsing for HL7v2 messages \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:28.995979+00:00
---

# Enable schematized parsing for HL7v2 messages  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-default-parser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Enable schematized parsing for HL7v2 messages Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to enable schematized parsing on an HL7v2 store to parse HL7v2 messages that align with the HL7v2 standard. Enabling schematized parsing without setting a schema configuration is referred to as using the _default schema_. The primary use case for enabling schematized parsing is to preserve grouping when ingesting or creating HL7v2 messages.

Default schematized parsing can only be used with messages that conform to the HL7v2 standard. To parse messages that deviate from the HL7v2 standard, you must [use a custom schema](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-custom-parser). The default parser is based on version 2.8.2 of the HL7v2 standard.

## Sample HL7v2 message

The samples in this page use the following HL7v2 message. The sample message conforms to the HL7v2 standard.
    
    
    MSH|^~\&|My EHR|My Test Facility||My EHR Facility|20150926140551||ORU^R01^ORU_R01|My-LOI_5.0_1.1-NG|T|2.5.1|||AL|AL|||||\r
    PID|1||PATID5421^^^My MPI^MR||Zhang^Sally^Brian^^^^L||19840611|F||2106-3^White^HL70005|123 Main Street^^Mountain Springs^CO^80439^^H||^PRN^PH^^^203^2290210|||||||||N^Not Hispanic or Latino^HL70189\r
    ORC|RE|833582639|3266238193||CM||||2010-01-01T19:53:38.408547Z\r
    OBR|1|833582639|3266238193|us-0005^Vital Signs^WinPath^^||2010-01-01T19:53:38.408547Z|2010-01-01T19:53:38.408547Z|||||||2010-01-01T19:53:38.408547Z||||||||2010-01-01T19:53:38.408547Z|||F||1\r
    OBX|1|NM|tt-0005-07^MDC_PULS_RATE_NON_INV^MDC^^||52.31|MDC_DIM_BEAT_PER_MIN|50-200||||F|||2010-01-01T19:53:38.408547Z||\r
    OBX|2|NM|tt-0005-12^PAIN LEVEL^L^^||1.71|/10|1-10||||F|||2010-01-01T19:53:38.408547Z||\r
    OBX|3|NM|tt-0005-09^MDC_TEMP^MDC^^||36.22|MDC_DIM_DEGC|36-38||||F|||2010-01-01T19:53:38.408547Z||\r
    

## Use the default schema to preserve grouping

When you [create or ingest an HL7v2 message](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages#overview_of_creating_and_ingesting_hl7v2_messages), the Cloud Healthcare API parses the message so that all segments in the message are returned in a [`ParsedData`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#ParsedData) object as a flat hierarchy. As a result, grouping information in the message is lost. To preserve grouping, you can enable default schematized parsing when creating or patching an HL7v2 store by passing in the [`ParserConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserConfig) object.

After passing in `ParserConfig`, the segments in the message are returned in a [`SchematizedData`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#SchematizedData) object that preserves grouping.

For example, compare the parsed versions of an `MSH` segment in an HL7v2 message between the `ParsedData` version (without setting `ParserConfig`) and with the `SchematizedData` version (with setting `ParserConfig`):

`ParsedData`| `SchematizedData`  
---|---  
      
    
    {
      "parsedData": {
        "segments": [
          {
            "segmentId": "MSH",
            "fields": {
              "0": "MSH",
              "1": "^~\\&",
              "2": "My EHR",
              "3": "My Test Facility",
              "5": "My EHR Facility",
              "6": "20150926140551",
              "9": "My-LOI_5.0_1.1-NG",
              "10": "T",
              "11": "2.5.1",
              "14": "AL",
              "15": "AL",
              "8.3": "ORU_R01",
              "8.2": "R01",
              "8.1": "ORU"
            }
          },
      ...
      }
    }

| 
    
    
    {
      "schematizedData": {
        "data": "{
          "ORU_R01": {
            "DSC": null,
            "MSH": {
              "0": "MSH",
              "1": "|",
              "2": "^~\\\\\\u0026",
              "3": {
                "1": "My EHR"
              },
              "4": {
                "1": "My Test Facility"
              },
              "5": null,
              "6": {
                "1": "My EHR Facility"
              },
              "7": "20150926140551",
              "8": null,
              "9": {
                "1": "ORU",
                "2": "R01",
                "3": "ORU_R01"
              },
              "10": "My-LOI_5.0_1.1-NG",
              "11": {
                "1": "T"
              },
              "12": {
                "1": "2.5.1"
              },
              "13": null,
              "14": null,
              "15": "AL",
              "16": "AL",
              "17": null,
              "18": null,
              "19": null,
              "20": null,
              "21": null
            },
        ...
      }
    }  
  
## Update an HL7v2 store with the default schema

To update an existing HL7v2 store and enable default schematized parsing, use the [`projects.locations.datasets.hl7V2Stores.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/patch) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the HL7v2 store's parent dataset
  * HL7V2_STORE_ID: the HL7v2 store ID
  * FAILURE_MODE: the failure mode for schematized parsing, one of `HARD_FAIL` or `SOFT_FAIL`. See [`SchematizedParsingType`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#schematizedparsingtype) for more information.



Request JSON body: 
    
    
    {
      "parserConfig": {
        "schema": {
          "schematizedParsingType": "FAILURE_MODE"
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
          "schematizedParsingType": "FAILURE_MODE"
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
          "schematizedParsingType": "FAILURE_MODE"
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
        "schema": {
          "schematizedParsingType": "FAILURE_MODE"
        }
        "version": "V3"
      }
    }
    

## Ingest and parse the sample HL7v2 message with the default schema

After creating or updating the HL7v2 store with default schematized parsing, you can ingest an HL7v2 message into the store.

The following samples show how to ingest the sample message shown in Sample HL7v2 message converted to base64. The encoded message is supplied as a value to the `data` field inside of the `message` object.

To ingest the message, use the [`projects.locations.datasets.hl7V2Stores.messages.ingest`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/ingest) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the HL7v2 store's parent dataset
  * HL7V2_STORE_ID: the HL7v2 store ID



Request JSON body: 
    
    
    {
      "message": {
        "data": "TVNIfF5+XCZ8TXkgRUhSfE15IFRlc3QgRmFjaWxpdHl8fE15IEVIUiBGYWNpbGl0eXwyMDE1MDkyNjE0MDU1MXx8T1JVXlIwMV5PUlVfUjAxfE15LUxPSV81LjBfMS4xLU5HfFR8Mi41LjF8fHxBTHxBTHx8fHx8DVBJRHwxfHxQQVRJRDU0MjFeXl5NeSBNUEleTVJ8fFpoYW5nXlNhbGx5XkJyaWFuXl5eXkx8fDE5ODQwNjExfEZ8fDIxMDYtM15XaGl0ZV5ITDcwMDA1fDEyMyBNYWluIFN0cmVldF5eTW91bnRhaW4gU3ByaW5nc15DT144MDQzOV5eSHx8XlBSTl5QSF5eXjIwM14yMjkwMjEwfHx8fHx8fHx8Tl5Ob3QgSGlzcGFuaWMgb3IgTGF0aW5vXkhMNzAxODkNT1JDfFJFfDgzMzU4MjYzOXwzMjY2MjM4MTkzfHxDTXx8fHwyMDIwMDUwNjE3MDgyMg1PQlJ8MXw4MzM1ODI2Mzl8MzI2NjIzODE5M3x1cy0wMDA1XlZpdGFsIFNpZ25zXldpblBhdGheXnx8MjAyMDA1MDYxNzA4MjJ8MjAyMDA1MDYxNzA4MjJ8fHx8fHx8MjAyMDA1MDYxNzA4MjJ8fHx8fHx8fDIwMjAwNTA2MTcwODIyfHx8Rnx8MQ1PQlh8MXxOTXx0dC0wMDA1LTA3Xk1EQ19QVUxTX1JBVEVfTk9OX0lOVl5NRENeXnx8NTIuMzF8TURDX0RJTV9CRUFUX1BFUl9NSU58NTAtMjAwfHx8fEZ8fHwyMDIwMDUwNjE3MDgyMnx8DU9CWHwyfE5NfHR0LTAwMDUtMTJeUEFJTiBMRVZFTF5MXl58fDEuNzF8LzEwfDEtMTB8fHx8Rnx8fDIwMjAwNTA2MTcwODIyfHwNT0JYfDN8Tk18dHQtMDAwNS0wOV5NRENfVEVNUF5NRENeXnx8MzYuMjJ8TURDX0RJTV9ERUdDfDM2LTM4fHx8fEZ8fHwyMDIwMDUwNjE3MDgyMnx8DQ=="
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "message": {
        "data": "TVNIfF5+XCZ8TXkgRUhSfE15IFRlc3QgRmFjaWxpdHl8fE15IEVIUiBGYWNpbGl0eXwyMDE1MDkyNjE0MDU1MXx8T1JVXlIwMV5PUlVfUjAxfE15LUxPSV81LjBfMS4xLU5HfFR8Mi41LjF8fHxBTHxBTHx8fHx8DVBJRHwxfHxQQVRJRDU0MjFeXl5NeSBNUEleTVJ8fFpoYW5nXlNhbGx5XkJyaWFuXl5eXkx8fDE5ODQwNjExfEZ8fDIxMDYtM15XaGl0ZV5ITDcwMDA1fDEyMyBNYWluIFN0cmVldF5eTW91bnRhaW4gU3ByaW5nc15DT144MDQzOV5eSHx8XlBSTl5QSF5eXjIwM14yMjkwMjEwfHx8fHx8fHx8Tl5Ob3QgSGlzcGFuaWMgb3IgTGF0aW5vXkhMNzAxODkNT1JDfFJFfDgzMzU4MjYzOXwzMjY2MjM4MTkzfHxDTXx8fHwyMDIwMDUwNjE3MDgyMg1PQlJ8MXw4MzM1ODI2Mzl8MzI2NjIzODE5M3x1cy0wMDA1XlZpdGFsIFNpZ25zXldpblBhdGheXnx8MjAyMDA1MDYxNzA4MjJ8MjAyMDA1MDYxNzA4MjJ8fHx8fHx8MjAyMDA1MDYxNzA4MjJ8fHx8fHx8fDIwMjAwNTA2MTcwODIyfHx8Rnx8MQ1PQlh8MXxOTXx0dC0wMDA1LTA3Xk1EQ19QVUxTX1JBVEVfTk9OX0lOVl5NRENeXnx8NTIuMzF8TURDX0RJTV9CRUFUX1BFUl9NSU58NTAtMjAwfHx8fEZ8fHwyMDIwMDUwNjE3MDgyMnx8DU9CWHwyfE5NfHR0LTAwMDUtMTJeUEFJTiBMRVZFTF5MXl58fDEuNzF8LzEwfDEtMTB8fHx8Rnx8fDIwMjAwNTA2MTcwODIyfHwNT0JYfDN8Tk18dHQtMDAwNS0wOV5NRENfVEVNUF5NRENeXnx8MzYuMjJ8TURDX0RJTV9ERUdDfDM2LTM4fHx8fEZ8fHwyMDIwMDUwNjE3MDgyMnx8DQ=="
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
        "data": "TVNIfF5+XCZ8TXkgRUhSfE15IFRlc3QgRmFjaWxpdHl8fE15IEVIUiBGYWNpbGl0eXwyMDE1MDkyNjE0MDU1MXx8T1JVXlIwMV5PUlVfUjAxfE15LUxPSV81LjBfMS4xLU5HfFR8Mi41LjF8fHxBTHxBTHx8fHx8DVBJRHwxfHxQQVRJRDU0MjFeXl5NeSBNUEleTVJ8fFpoYW5nXlNhbGx5XkJyaWFuXl5eXkx8fDE5ODQwNjExfEZ8fDIxMDYtM15XaGl0ZV5ITDcwMDA1fDEyMyBNYWluIFN0cmVldF5eTW91bnRhaW4gU3ByaW5nc15DT144MDQzOV5eSHx8XlBSTl5QSF5eXjIwM14yMjkwMjEwfHx8fHx8fHx8Tl5Ob3QgSGlzcGFuaWMgb3IgTGF0aW5vXkhMNzAxODkNT1JDfFJFfDgzMzU4MjYzOXwzMjY2MjM4MTkzfHxDTXx8fHwyMDIwMDUwNjE3MDgyMg1PQlJ8MXw4MzM1ODI2Mzl8MzI2NjIzODE5M3x1cy0wMDA1XlZpdGFsIFNpZ25zXldpblBhdGheXnx8MjAyMDA1MDYxNzA4MjJ8MjAyMDA1MDYxNzA4MjJ8fHx8fHx8MjAyMDA1MDYxNzA4MjJ8fHx8fHx8fDIwMjAwNTA2MTcwODIyfHx8Rnx8MQ1PQlh8MXxOTXx0dC0wMDA1LTA3Xk1EQ19QVUxTX1JBVEVfTk9OX0lOVl5NRENeXnx8NTIuMzF8TURDX0RJTV9CRUFUX1BFUl9NSU58NTAtMjAwfHx8fEZ8fHwyMDIwMDUwNjE3MDgyMnx8DU9CWHwyfE5NfHR0LTAwMDUtMTJeUEFJTiBMRVZFTF5MXl58fDEuNzF8LzEwfDEtMTB8fHx8Rnx8fDIwMjAwNTA2MTcwODIyfHwNT0JYfDN8Tk18dHQtMDAwNS0wOV5NRENfVEVNUF5NRENeXnx8MzYuMjJ8TURDX0RJTV9ERUdDfDM2LTM4fHx8fEZ8fHwyMDIwMDUwNjE3MDgyMnx8DQ=="
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
      "hl7Ack": "TVNIfF5+XCZ8fE15IEVIUiBGYWNpbGl0eXxNeSBFSFJ8TXkgVGVzdCBGYWNpbGl0eXwyMDIwMDUwNjIxNDY1MXx8QUNLfDcwY2IxMjJhLTUxYzctNGFkYy04NzFkLWZlMzJjZTgxYzI5OHxUfDIuNS4xDU1TQXxBQXxNeS1MT0lfNS4wXzEuMS1ORw==",
      "message": {
        "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/HL7V2_STORE_ID",
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
          "data": "{
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
                          \"9\": \"20200506170822\"
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
                        \"6\": \"20200506170822\",
                        \"7\": \"20200506170822\",
                        \"8\": null,
                        \"9\": null,
                        \"10\": null,
                        \"11\": null,
                        \"12\": null,
                        \"13\": null,
                        \"14\": \"20200506170822\",
                        \"15\": null,
                        \"16\": null,
                        \"17\": null,
                        \"18\": null,
                        \"19\": null,
                        \"20\": null,
                        \"21\": null,
                        \"22\": \"20200506170822\",
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
                            \"14\": \"20200506170822\",
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
                            \"14\": \"20200506170822\",
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
                            \"14\": \"20200506170822\",
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
              \"SFT\": null,
              \"UAC\": null
            }
          }"
        }
      }
    }
    

## What's next

[Use a custom schema to parse HL7v2 messages](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-custom-parser) that don't conform to the HL7v2 standard.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

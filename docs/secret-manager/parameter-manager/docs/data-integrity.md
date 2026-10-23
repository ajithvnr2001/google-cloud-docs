---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/data-integrity/
title: Data integrity assurance \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:57:42.717870+00:00
---

# Data integrity assurance  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/data-integrity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Data integrity assurance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use checksums to maintain and verify the integrity of your parameter's data when [adding](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-version) and [accessing](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/render-parameter-version) parameter versions.

Think of a checksum as a unique fingerprint for your data. It's a short code generated from the parameter data using the CRC32C algorithm. If even a single bit in your parameter data changes, the checksum also changes. This lets Parameter Manager detect any accidental modifications or corruption.

Parameter Manager uses checksums in the following ways:

  1. When you add a parameter version: 
     * Parameter Manager calculates the CRC32C checksum of your parameter data.
     * This checksum is stored along with the parameter data.
  2. When you access a parameter version: 
     * Parameter Manager returns the parameter data along with its checksum.
     * You can use this checksum to verify that the data you received is exactly the same as the data stored in Parameter Manager.



To ensure that the checksum is compatible with the [ParameterVersionPayload](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rpc/google.cloud.parametermanager.v1#parameterversionpayload) structure, the checksum of the parameter data must be calculated using the CRC32C algorithm and encoded as a decimal integer. The [ParameterVersion](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rpc/google.cloud.parametermanager.v1#parameterversion) response includes a field indicating whether the server has successfully received and validated this checksum.

The following example shows how checksums work in Parameter Manager:

With parameter data stored in a data file, calculate the checksum, using [gcloud storage hash](https://docs.cloud.google.com/sdk/gcloud/reference/storage/hash). Checksum must be converted to decimal format; it is encoded as int64 in ParameterVersionPayload proto.

### API

These examples use [curl](https://curl.haxx.se/) to demonstrate using the API. You can generate [access tokens](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials) with `gcloud auth print-access-token`. On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 

With parameter data stored in a data file, calculate the checksum, using [gcloud storage hash](https://docs.cloud.google.com/sdk/gcloud/reference/storage/hash). Checksum must be converted to decimal format; it is encoded as int64 in ParameterVersionPayload proto. 
    
    
    $ gcloud storage hash "/path/to/file.yaml" --hex
    

Base64-encode the parameter data and save it as a shell variable.
    
    
    $ PARAMETER_DATA=$(echo "port: 8080" | base64)
    

With parameter data passed on the command line, calculate the checksum as follows: 
    
    
    $ gcloud storage hash --hex cat <(echo "${PARAMETER_DATA}")
    

**Global parameters**

Invoke the API using curl.
    
    
    $ curl "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions?parameter_version_id=PARAMETER_VERSION_ID" \
        --request "POST" \
        --header "authorization: Bearer $(gcloud auth print-access-token)" \
        --header "content-type: application/json" \
        --data "{\"payload\": {\"data\": \"${PARAMETER_DATA}\", \"data_crc32c\": $CHECKSUM}}"
    

  


**Regional parameters**

Invoke the API using curl.
    
    
    $ curl "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions?parameter_version_id=PARAMETER_VERSION_ID" \
        --request "POST" \
        --header "authorization: Bearer $(gcloud auth print-access-token)" \
        --header "content-type: application/json" \
        --data "{\"payload\": {\"data\": \"${PARAMETER_DATA}\", \"data_crc32c\": $CHECKSUM}}"
    

When the parameter version is accessed, the returned [ParameterVersionPayload](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rpc/google.cloud.parametermanager.v1#parameterversionpayload) contains the data along with its checksum. Following is a sample response:
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions/VERSION_ID",
      "payload": {
        "data": "cG9ydDogODA4MAo=",
        "dataCrc32c": "**1739307059** "
      },
      "checksumSource": "USER_SPECIFIED"
    }

In the console, when you [add a parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-version), the checksum is automatically calculated when you enter a value for the parameter.

Parameter versions encrypted with customer-managed encryption keys (CMEK) and created before August 24, 2026 don't have checksums stored.

## What's next

  * Learn how to [add a parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-version).
  * Learn how to [access and render parameter versions](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/render-parameter-version).
  * Learn how to [reference secrets in parameters](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter).
  * Learn how to [enable CMEK for Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/cmek).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

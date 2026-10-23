---
url: https://docs.cloud.google.com/spectrum-access-system/docs/samples/
title: API code samples \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:46.904569+00:00
---

# API code samples  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/samples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  API code samples Stay organized with collections  Save and categorize content based on your preferences. 

This page contains code samples for the Google Spectrum Access System (SAS) Portal API.

## Before you begin

For the following examples, ensure that you complete the following prerequisites:

  * [Obtain a token with your service account](https://docs.cloud.google.com/spectrum-access-system/docs/authorization-and-authentication) `TOKEN=$(gcloud auth print-access-token)`.
  * Set `${CLIENT_PROJECT}` to the project ID of the Google Cloud project.



## List current customers

  1. Return all of the customers that the caller has access to:
         
         curl -X GET -H "X-Goog-User-Project: ${CLIENT_PROJECT}" \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer ${TOKEN}" \"https://sasportal.googleapis.com/v1alpha1/customers"
         

  2. Save the customer name that is returned as a variable:
         
         CUSTOMER_NAME=customers/...
         




## Create a new device configuration

  1. Set the `${FCCID}` and `${SN}` of the device that you want to create:
         
         FCCID=f1
         SN=sn1
         

  2. Create the device configuration:
         
         curl -X POST -H "X-Goog-User-Project: ${CLIENT_PROJECT}" \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer ${TOKEN}" \ "https://sasportal.googleapis.com/v1alpha1/${CUSTOMER_NAME}/devices" \
          -d "{ \"fcc_id\": \"$FCCID\", \"serial_number\": \"$SN\", \"preloaded_config\": { \"call_sign\": \"cs1\", \"category\": \"DEVICE_CATEGORY_A\"}}"
         

The command returns a newly created device configuration.

  3. Save the device name as a variable:
         
         DEVICE_NAME=customers/.../devices/...
         




## List current devices
    
    
    curl -X GET -H "X-Goog-User-Project: ${CLIENT_PROJECT}" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer $TOKEN" \ "https://sasportal.googleapis.com/v1alpha1/${CUSTOMER_NAME}/devices"
    

## Retrieve devices by name
    
    
    curl -X GET -H "X-Goog-User-Project: ${CLIENT_PROJECT}" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer $TOKEN" \
     "https://sasportal.googleapis.com/v1alpha1/${DEVICE_NAME}"
    

## Update an existing device
    
    
    curl -X PATCH -H "X-Goog-User-Project: ${CLIENT_PROJECT}" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer $TOKEN" \
     "https://sasportal.googleapis.com/v1alpha1/${DEVICE_NAME}" \
    

## Validate your Certified Professional Installer (CPI) identity and certification

  1. Generate the secret string:
         
         curl -X POST -H "X-Goog-User-Project: ${CLIENT_PROJECT}" \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $TOKEN" \ "https://sasportal.googleapis.com/v1alpha1/installer:generateSecret" \
          -d "{}"
         

The output is similar to the following:
         
         {
           "secret": "<generated secret>"
          }
         

  2. Use the [JSON Web Token format](https://docs.cloud.google.com/spectrum-access-system/docs/json-web-token-format) to encode the secret string into a JWT.

  3. Set the following:

     1. `${SECRET}` to the secret string
     2. `${ENCODED_SECRET}` to the JWT string
     3. `${CPI_ID}` to the ID of the CPI
  4. Validate the identity and certification of the CPI:
         
         curl -X POST -H "X-Goog-User-Project: ${CLIENT_PROJECT}" \
           -H "Content-Type: application/json" \
           -H "Authorization: Bearer $TOKEN" \ "https://sasportal.googleapis.com/v1alpha1/installer:validate" \
           -d "{ \"installer_id\": \"${CPI_ID}\", \"secret\": \"${SECRET}\", \"encoded_secret\": \"${ENCODED_SECRET}\" }"
         




Now the CPI can install a Citizens Broadband Radio Service Device (CBSD) that has all the required parameters.

## Multistep CBSD registration

You can perform multistep CBSD registration with device parameters previously signed by a CPI or with a CPI account.

### Device parameters previously signed by a CPI

This sample shows how to create an inactive device configuration with CBSD installation parameters previously encoded by a CPI. As a result, the non-CPI users can also create the configuration.

  1. Use the CPI's private key to encode the CBSD parameters. We recommend that you use the [JSON Web Token format](https://docs.cloud.google.com/spectrum-access-system/docs/json-web-token-format).
  2. Set `${ENCODED_DEVICE}` to the JWT string and `${CPI_ID}` to the ID of the CPI.
  3. Create the inactive device configuration:
         
         curl -X POST -H "X-Goog-User-Project: ${CLIENT_PROJECT}" \
           -H "Content-Type: application/json" \
           -H "Authorization: Bearer ${TOKEN}" \ "https://sasportal.googleapis.com/v1alpha1/${CUSTOMER_NAME}/devices:createSigned" \
           -d "{ \"installer_id\": \"${CPI_ID}\", \"encoded_device\": \"${ENCODED_DEVICE}\", \"parent\": \"${CUSTOMER_NAME}\" }"
         




The CBSD must then send a registration request to SAS to complete its registration.

### CPI account

The CPI's identity must be validated _before_ you [validate](https://docs.cloud.google.com/spectrum-access-system/docs/validate-cpi-identity) a device configuration. When that is done, use the following command to create an inactive device configuration:
    
    
      curl -X POST -H "X-Goog-User-Project: ${CLIENT_PROJECT}" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $TOKEN" \ "https://sasportal.googleapis.com/v1alpha1/${DEVICE_NAME}:signDevice" \
        -d "${DEVICE}"
    

Replace `${DEVICE}` with the JSON representation of the CBSD registration parameters. For more information about the format, see [REST Resource: customers.devices](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices).

The CBSD must then send a registration request to SAS to complete its registration.

## What's next

  * To get an overview of the SAS Portal API, see [Google SAS Portal API overview](https://docs.cloud.google.com/spectrum-access-system/docs/overview-api).
  * For information about each API, see [Customers API](https://docs.cloud.google.com/spectrum-access-system/docs/customers-api) and [Device Manager API](https://docs.cloud.google.com/spectrum-access-system/docs/device-manager-api).
  * For reference documentation, see [APIs and reference](https://docs.cloud.google.com/spectrum-access-system/docs/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

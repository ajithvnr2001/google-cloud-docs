---
url: https://docs.cloud.google.com/compute/shielded-vm/docs/retrieving-endorsement-key/
title: Retrieving endorsement keys \u00a0|\u00a0 Shielded VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:05:06.814412+00:00
---

# Retrieving endorsement keys  |  Shielded VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/shielded-vm/docs/retrieving-endorsement-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Shielded VM ](https://docs.cloud.google.com/compute/shielded-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm)



Send feedback 

#  Retrieving endorsement keys Stay organized with collections  Save and categorize content based on your preferences. 

This topic describes how to retrieve the endorsement key (EKPub) from a Shielded VMinstance.

You can retrieve the endorsement key for both the encryption key and the signing key. You can use the encryption key to encrypt data so that only the vTPM can read it, or the signing key to verify signatures that the vTPM makes. You can also use the key to ascertain the identity of a VM instance before sending sensitive information to it.

You must have the `getShieldedInstanceIdentity` permission to retrieve endorsement keys.

## Retrieving endorsement keys using the Google Cloud CLI

Use the `gcloud compute instances get-shielded-identity` command to retrieve the public portion of the endorsement key from a Shielded VM instance.
    
    
        gcloud compute instances get-shielded-identity [INSTANCE_NAME]
    

The results returned look similar to the following:
    
    
    encryptionKey:
      ekPub: |
        -----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4ucWqhLjIkcEJyqc8KJM
        12345678abcdefghijklmnopqrstuvwxyz12345678abcdefghijklmnopqrstu
        oBSrm0swIu3x4LWR/Ebl5KA0EKe9YFGaS9Pguun1m6X8Ld2zAqmoIwnxDiOqxQEU
        mx2wxkjf0bbjxG5ZI1i3t/c/QzeaE2WWTlKdgnUDyxSloDBq63yywtoIrp1nbDLj
        X8qdBymixu8jXXp1iGwmEUltnEnx779JKTpKgKTEednri+NcfRmXHrnPCxfiPudQ
        4wIDAQAB
        -----END PUBLIC KEY-----
    kind: compute#shieldedInstanceIdentity
    signingKey:
      ekPub: |
        -----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzQvcD+2LAnsXAgdsVYAc
        12345678abcdefghijklmnopqrstuvwxyz12345678abcdefghijklmnopqrstu
        V/7WHasUuGlkbqiDOuDWgb15FAn35PU64HGey67McZTUT9EvrkT/ryXi4kZgBtoM
        lQIDAQAB
        -----END PUBLIC KEY-----
    

## Retrieving endorsement keys using the Compute Engine API

You can use the Compute Engine API to view endorsement key information. For more information on how to use the API, see the [How-to guides](https://docs.cloud.google.com/compute/docs/api/how-tos/how-tos).
    
    
    GET /compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]/getShieldedInstanceIdentity
    
    {
      "signingKey": {
        "ekPub": [PEM-formatted key]
      },
      "encryptionKey": {
        "ekPub": [PEM-formatted key]
      },
      "kind": "compute#shieldedInstanceIdentity"
    }
    

## What's next

  * Learn about [modifying options on a Shielded VM instance](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm).
  * Learn about one approach to [automating responses to integrity monitoring events](https://docs.cloud.google.com/compute/shielded-vm/docs/automating-responses-integrity-failures).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

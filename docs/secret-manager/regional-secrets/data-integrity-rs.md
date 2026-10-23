---
url: https://docs.cloud.google.com/secret-manager/regional-secrets/data-integrity-rs/
title: Data integrity assurance \u00a0|\u00a0 Secret Manager Regional Service Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:47.981678+00:00
---

# Data integrity assurance  |  Secret Manager Regional Service Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/regional-secrets/data-integrity-rs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Regional service ](https://docs.cloud.google.com/secret-manager/regional-secrets)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/regional-secrets/regional-secrets-overview)



Send feedback 

#  Data integrity assurance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use checksums to maintain and verify the integrity of your secret's data when [adding](https://docs.cloud.google.com/secret-manager/regional-secrets/add-secret-version-rs) and [accessing](https://docs.cloud.google.com/secret-manager/regional-secrets/access-secret-version-rs) secret versions.

Think of a checksum as a unique fingerprint for your data. It's a short code generated from the secret data using the CRC32C algorithm. If even a single bit in your secret data changes, the checksum also changes. This lets Secret Manager detect any accidental modifications or corruption.

Secret Manager uses checksums in the following ways:

  1. When you add a secret version:

     * Secret Manager calculates the CRC32C checksum of your secret data.

     * This checksum is stored along with the secret data.

  2. When you access a secret version:

     * Secret Manager returns the secret data along with its checksum.

     * You can use this checksum to verify that the data you received is exactly the same as the data stored in Secret Manager.




To ensure that the checksum is compatible with the [SecretPayload](https://docs.cloud.google.com/secret-manager/docs/reference/rpc/google.cloud.secretmanager.v1#secretpayload) structure, the checksum of the secret data must be calculated using the CRC32C algorithm and encoded as a decimal integer. The [SecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions#SecretVersion.FIELDS) response includes a field indicating whether the server has successfully received and validated this checksum.

The following example shows how checksums work in Secret Manager:

### API

These examples use [curl](https://curl.haxx.se/) to demonstrate using the API. You can generate [access tokens](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials) with `gcloud auth print-access-token`. On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 

With secret data stored in a data file, calculate the checksum, using [gcloud storage hash](https://docs.cloud.google.com/sdk/gcloud/reference/storage/hash). Checksum must be converted to decimal format; it is encoded as int64 in SecretPayload proto. 
    
    
    $ gcloud storage hash "/path/to/file.txt" --hex
    

Base64-encode the secret data and save it as a shell variable.
    
    
    $ SECRET_DATA=$(echo "seCr3t" | base64)
    

With secret data passed on the command line, calculate the checksum as follows: 
    
    
    $ gcloud storage hash --hex cat <(echo ${SECRET_DATA})
    

Invoke the API using curl.
    
    
    $ curl "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/secret-id:addVersion" \
        --request "POST" \
        --header "authorization: Bearer $(gcloud auth print-access-token)" \
        --header "content-type: application/json" \
        --data "{\"payload\": {\"data\": \"${SECRET_DATA}\", \"data_crc32c\": $CHECKSUM}}"
    

When the secret version is accessed, the returned [SecretPayload](https://docs.cloud.google.com/secret-manager/docs/reference/rpc/google.cloud.secretmanager.v1#secretpayload) contains the data along with its checksum. Following is a sample response:
    
    
    {
      "name": "projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID",
      "payload": {
        "data": "YQo=",
        "dataCrc32c": "**163439259** "
      }
    }

In the console, when you [add a secret version](https://docs.cloud.google.com/secret-manager/regional-secrets/add-secret-version-rs), the checksum is automatically calculated when you enter a value for the secret.

Secret versions encrypted with customer-managed encryption keys (CMEK) and created before July 16, 2021 do not have checksums stored.

## What's next

  * [Set up notifications on a regional secret](https://docs.cloud.google.com/secret-manager/regional-secrets/notifications-regional-secrets)
  * [Analyze regional secrets with Cloud Asset Inventory](https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

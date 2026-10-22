---
url: https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/troubleshoot-omni-tde/
title: Troubleshoot Transparent Data Encryption (TDE) \u00a0|\u00a0 AlloyDB Omni using containers: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:45.862068+00:00
---

# Troubleshoot Transparent Data Encryption (TDE)  |  AlloyDB Omni using containers: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/troubleshoot-omni-tde/

This page documents AlloyDB Omni version **18.3.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/overview)



Send feedback 

#  Troubleshoot Transparent Data Encryption (TDE) Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/troubleshoot-omni-tde)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/troubleshoot-omni-tde)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/troubleshoot-omni-tde)



This page describes how to troubleshoot [transparent data encryption (TDE)](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/transparent-data-encryption-omni) issues in AlloyDB Omni.

## Retrieve troubleshooting logs

To troubleshoot TDE issues, you can collect logs depending on your deployment type.

Collect the container logs and filter for TDE-related messages:
    
    
    docker logs CONTAINER_NAME | grep "TDE"

The logs might contain entries like the following:

  * `TDE: TdeContext initialization failed`
  * `TDE: Vault server unreachable`
  * `TDE: Certificate expired`



## Error scenarios

This section describes common TDE error scenarios and provides suggested fixes.

### JWT errors

If you see HashiCorp Vault authentication or initialization failures in the collected logs, they are often related to JSON Web Token (JWT) issues.

#### Description

You might see errors like the following:

Error | Description | Reason  
---|---|---  
`TDE: Failed to register Key Store with URL: VAULT_URL, error code: 3, error message: JWT cannot be empty` | JWT not found or empty | The JWT token is missing or empty.  
`TDE: Failed to register Key Store with URL: VAULT_URL, error code: 3, error message: Invalid JWT format. Expected JWS compact serialization (three dot-separated segments: header, payload, and signature) with base64url encoded values.` | Malformed JWT format | The JWT token is not in the correct JWS compact serialization format.  
`TDE: Failed to register Key Store with URL: VAULT_URL, error code: 3, error message: Vault request failed with HTTP code: 400, Vault errors: ["error validating token: invalid expiration time (exp) claim: token is expired"]` | Expired JWT | The JWT token has expired.  
`TDE: Failed to register Key Store with URL: VAULT_URL, error code: 3, error message: Vault request failed with HTTP code: 400, Vault errors: ["error validating token: error verifying token signature: failed to verify id token signature"]` | Invalid JWT signature | The Vault server couldn't verify the signature of the JWT token.  
`TDE: Failed to register Key Store with URL: VAULT_URL, error code: 9, error message: Failed to get Vault configuration parameter 'VAULT_JWT'` | Permission issue | AlloyDB Omni lacks permission to read the JWT token file, or the `VAULT_JWT` environment variable is not set.  
  
#### Recommended fix

To resolve JWT issues:

  1. Retrieve the active JWT:

Run the following command to print the `VAULT_JWT` environment variable from the container:
         
         docker exec -it CONTAINER_NAME sh -c 'echo $VAULT_JWT'

  2. Examine JWT structure: make sure that the token is valid and conforms to the JWT compact serialization format.

  3. Verify token state: make sure that the token is active and has not expired.




### KMS URL errors

If the database fails to initialize or boot, it might be due to a misconfigured Key Management Service (KMS) Key Encryption Key (KEK) URL.

#### Description

You might see errors like the following:

Error | Description | Reason  
---|---|---  
`TDE: Failed to register Key Store with URL: KMS_URL, error code: 12, error message: Unsupported key store type` | Unsupported key store type | Occurs when the KEK URL protocol is not `vault`. For example, using `http://` or `https://` instead of `vault://`, or omitting the scheme entirely.  
`TDE: Failed to register Key Store with URL: KMS_URL, error code: 3, error message: Invalid Vault address format. Expected hostname or hostname:port` | Invalid Vault address format | Occurs when the Vault address part of the URL is incorrectly formatted. For example, if it includes the protocol scheme again, such as `vault://https://vault.example.com:8200/...`.  
`TDE: Failed to read KEK, error code: 3, error message: Invalid key path format. Must start with '/', not end with '/', and contain only valid characters` | Invalid key path format | Occurs when the path part of the Vault URL is malformed. The path must start with a forward slash `/` and must not end with a trailing slash.  
`TDE: Failed to register Key Store with URL: KMS_URL, error code: 13, error message: curl_easy_perform() failed: Could not resolve hostname` | Hostname resolution failure | Occurs when the Vault hostname in the KEK URL can't be resolved. This can happen if the URL is malformed (for example, `vault://https:`) or if there is a DNS configuration issue.  
  
#### Recommended fix

  * Verify KEK URL scheme: make sure that the URL starts with `vault://`. Don't use `https://` as the prefix. 
    * Correct: `vault://vault.example.com:8200/v1/secret/data/key`
    * Incorrect: `https://vault.example.com:8200/v1/secret/data/key`
  * Check address format: make sure that the host and port are correctly specified immediately after the `vault://` prefix.
  * Verify path formatting: make sure that the path starts with `/` and doesn't have a trailing slash (for example, use `/v1/secret/data/key`, not `/v1/secret/data/key/`).
  * Verify host resolution: make sure that the Vault hostname specified in the URL is correct and that it can be resolved from within the database container.



### KEK not base64-encoded

If the KEK stored in HashiCorp Vault is not correctly base64-encoded, AlloyDB Omni fails to decode it upon retrieval. This prevents it from unwrapping the local Data Encryption Keys (DEKs) and causes a boot failure.

#### Description

You might see errors like the following in the database diagnostic logs (`postgresql.log`):

Error | Description | Reason  
---|---|---  
`TDE: Failed to read KEK, error code: 13, error message: Error decoding base64 key string` | Error decoding base64 key string | Occurs when the key manager attempts to decode the retrieved secret from Vault using Base64, but the string is not valid Base64.  
  
#### Recommended fix

  * Retrieve KEK value: retrieve and inspect the KEK value directly from HashiCorp Vault.
  * Update value in Vault: make sure that the KEK stored in Vault is base64-encoded. If it is stored as raw binary or plain text, update the value in Vault with its base64-encoded equivalent. 
    1. Convert the raw key to Base64: 
           
           echo -n "RAW_KEY" | base64

    2. Update the secret in HashiCorp Vault to the generated base64-encoded string.



### KEK version missing in Vault

The KEK version missing in Vault error occurs when AlloyDB Omni attempts to unwrap local DEKs using a specific historical version of the KEK, but that version is deleted, destroyed, or missing in HashiCorp Vault. This is most common during backup restore operations or standby replica initialization.

#### Description

You might see errors like the following in the database diagnostic logs (`postgresql.log`):

Error | Description | Reason  
---|---|---  
`TDE: Failed to read KEK, error code: 5, error message: Vault request failed with HTTP code: 404, Response body: {... "destroyed":true, "version":4 ...}` | Key version destroyed | The requested KEK version is permanently destroyed in Vault.  
  
#### Recommended fix

  * Verify KEK version in Vault: make sure that the requested KEK version is present and active (not deleted or destroyed) in HashiCorp Vault.
  * Restore missing KEK version: restore or undelete the requested KEK version in Vault if it has been deleted but not destroyed.
  * Handle destroyed keys: if the requested key version is permanently destroyed in Vault, the data or backup encrypted under that version is permanently unrecoverable.



### Bad or missing TLS or SSL certificates

The bad or missing TLS or SSL certificate error occurs when AlloyDB Omni can't establish a secure TLS connection to HashiCorp Vault because certificates are missing, expired, untrusted, or misconfigured.

#### Description

You might see errors like the following in the database diagnostic logs (`postgresql.log`):

Error | Description | Reason  
---|---|---  
`TDE: Failed to read KEK, error code: 13, error message: curl_easy_perform() failed: SSL peer certificate or SSH remote key was not OK`  
Or  
`TDE: Failed to read KEK, error code: 13, error message: curl_easy_perform() failed: Peer certificate cannot be authenticated with given CA certificates` | Vault server certificate verification failed | The Vault server's certificate can't be verified using the provided CA certificate.  
`TDE: Failed to register Key Store with URL: VAULT_URL, error code: 13, error message: curl_easy_perform() failed: Problem with the local SSL certificate` | Local SSL certificate problem | Occurs if a client certificate is required and has issues.  
  
#### Recommended fix

To resolve TLS verification issues, make sure that the correct certificates are supplied, mounted, and readable by the `postgres` user.

Docker expects certificates to be supplied using a mounted host volume.

  1. Confirm that `VAULT_CERT_PATH` is set and points to the correct directory inside the container:
         
         docker inspect CONTAINER_NAME | grep VAULT_CERT_PATH

  2. Check that the certificate files exist and are readable by the database user (uid 999):
         
         docker exec -it CONTAINER_NAME ls -la PATH_TO_CERTS_DIRECTORY

Make sure that `ca.crt`, `tls.crt` and `tls.key` are present and have read permissions for the database user.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 

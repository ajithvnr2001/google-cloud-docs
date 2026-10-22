---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/troubleshoot-omni-tde/
title: Troubleshoot transparent data encryption \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:38:52.664168+00:00
---

# Troubleshoot transparent data encryption  |  AlloyDB Omni using the container orchestrator: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/troubleshoot-omni-tde/

This page documents AlloyDB Omni version **18.4.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/overview)



Send feedback 

#  Troubleshoot transparent data encryption Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/troubleshoot-omni-tde)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/troubleshoot-omni-tde)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/troubleshoot-omni-tde)

This page describes how to troubleshoot [transparent data encryption (TDE)](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/transparent-data-encryption-omni) issues in AlloyDB Omni. 

## Retrieve troubleshooting logs

To troubleshoot TDE issues, you can collect logs depending on your deployment type.

Collect diagnostics from the following three sources:

  1. **Cluster configuration and events:**

Use the `describe` database cluster command to check for high-level errors or status messages:
         
         kubectl describe dbcluster CLUSTER_NAME -n NAMESPACE

  2. **Pod logs:**

Get the logs for the database pod:
         
         kubectl logs POD_NAME -n NAMESPACE

  3. **Internal database logs:**

Inspect the PostgreSQL diagnostic log file inside the pod, filtering for TDE-related messages:
         
         kubectl exec -it POD_NAME -c database -n NAMESPACE -- cat /obs/diagnostic/postgresql.log | grep "TDE"




Replace the following:

  * `CLUSTER_NAME`: the name of your `DBCluster` resource.
  * `NAMESPACE`: the Kubernetes namespace where your `DBCluster` is deployed.
  * `POD_NAME`: the name of your database pod.



The logs might contain entries like the following:

  * `TDE: TdeContext initialization failed`
  * `TDE: Vault server unreachable`
  * `TDE: CipherTrust request failed`
  * `TDE: Certificate expired`



## Error scenarios

This section describes common TDE error scenarios and provides suggested fixes.

### JWT errors (HashiCorp Vault)

If you see HashiCorp Vault authentication or initialization failures in the collected logs, they are often related to JSON Web Token (JWT) issues.

#### Description

You might see errors like the following:

Error | Description | Reason  
---|---|---  
`TDE: Failed to register Key Store with URL: VAULT_URL, error code: 3, error message: JWT cannot be empty` | JWT not found or empty | The JWT token is missing or empty.  
`TDE: Failed to register Key Store with URL: VAULT_URL, error code: 3, error message: Invalid JWT format. Expected JWS compact serialization (three dot-separated segments: header, payload, and signature) with base64url encoded values.` | Malformed JWT format | The JWT token isn't in the correct JWS compact serialization format.  
`TDE: Failed to register Key Store with URL: VAULT_URL, error code: 3, error message: Vault request failed with HTTP code: 400, Vault errors: ["error validating token: invalid expiration time (exp) claim: token is expired"]` | Expired JWT | The JWT token has expired.  
`TDE: Failed to register Key Store with URL: VAULT_URL, error code: 3, error message: Vault request failed with HTTP code: 400, Vault errors: ["error validating token: error verifying token signature: failed to verify id token signature"]` | Invalid JWT signature | The Vault server couldn't verify the signature of the JWT token.  
`TDE: Failed to register Key Store with URL: VAULT_URL, error code: 9, error message: Failed to get Vault configuration parameter 'VAULT_JWT'` | Permission issue | AlloyDB Omni lacks permission to read the JWT token file, or the `VAULT_JWT` environment variable isn't set.  
  
#### Recommended fix

To resolve JWT issues:

  1. Retrieve the active JWT:

Run the following command to retrieve the JWT token from the pod:
         
         kubectl exec -it POD_NAME -c database -n NAMESPACE -- cat /var/run/secrets/vault/token

Replace `POD_NAME` with the name of your database pod and `NAMESPACE` with the namespace where your cluster is deployed.

  2. Examine JWT structure: Make sure that the token is valid and conforms to the JWT compact serialization format.

  3. Verify token state: Make sure that the token is active and has not expired.




### CipherTrust credential errors (Thales CipherTrust Manager)

If you see Thales CipherTrust Manager authentication or initialization failures in the collected logs, they are typically caused by missing or invalid user credentials (`username` and `password`).

#### Description

You might see errors like the following:

Error | Description | Reason  
---|---|---  
`TDE: Failed to register Key Store with URL: CIPHERTRUST_URL, error code: 3, error message: CipherTrust user cannot be empty` | Missing username | The `CIPHERTRUST_USER` environment variable or the `username` key in the Kubernetes Secret is empty.  
`TDE: Failed to register Key Store with URL: CIPHERTRUST_URL, error code: 3, error message: CipherTrust password cannot be empty` | Missing password | The `CIPHERTRUST_PASSWORD` environment variable or the `password` key in the Kubernetes Secret is empty.  
`TDE: Failed to register Key Store with URL: CIPHERTRUST_URL, error code: 9, error message: Failed to get CipherTrust configuration parameter 'CIPHERTRUST_USER'`  
Or  
`TDE: Failed to register Key Store with URL: CIPHERTRUST_URL, error code: 9, error message: Failed to get CipherTrust configuration parameter 'CIPHERTRUST_PASSWORD'` | Environment variable not set | The `CIPHERTRUST_USER` or `CIPHERTRUST_PASSWORD` environment variable is missing.  
`TDE: Failed to register Key Store with URL: CIPHERTRUST_URL, error code: 16, error message: CipherTrust request failed with HTTP code: 401` | Invalid credentials | The `username` or `password` was rejected by the Thales CipherTrust Manager authentication endpoint (`/api/v1/auth/tokens`).  
  
#### Recommended fix

  1. Extract the referenced `TdeConfig` name from your database cluster:
         
         kubectl get dbcluster CLUSTER_NAME -n NAMESPACE -o jsonpath='{.spec.primarySpec.features.transparentDataEncryption.tdeConfigRef.name}'

  2. Extract the referenced `credentialsSecretRef` name from your `TdeConfig` resource:
         
         kubectl get tdeconfig TDE_CONFIG_NAME -n NAMESPACE -o jsonpath='{.spec.kmsProvider.ciphertrust.credentialsSecretRef.name}'

  3. Verify that the Secret exists in the same namespace and contains non-empty `username` and `password` keys:
         
         kubectl describe secret CREDENTIALS_SECRET_NAME -n NAMESPACE




Replace the following:

  * `<var>CLUSTER_NAME</var>`: the name of your `DBCluster` resource.
  * `<var>NAMESPACE</var>`: the Kubernetes namespace where your `DBCluster` is deployed.
  * `<var>TDE_CONFIG_NAME</var>`: the name of your `TdeConfig` custom resource.
  * `<var>CREDENTIALS_SECRET_NAME</var>`: the name of the Kubernetes Secret containing your CipherTrust Manager credentials.



### KMS URL errors

If the database fails to initialize or boot, it might be due to a misconfigured Key Management Service (KMS) Key Encryption Key (KEK) URL.

#### Description

You might see errors like the following:

Error | Description | Reason  
---|---|---  
`TDE: Failed to register Key Store with URL: KMS_URL, error code: 12, error message: Unsupported key store type` | Unsupported key store type | Occurs when the KEK URL protocol isn't `vault` or `ciphertrust`. For example, using `http://` or `https://` instead of `vault://` or `ciphertrust://`, or omitting the scheme entirely.  
`TDE: Failed to register Key Store with URL: KMS_URL, error code: 3, error message: Invalid Vault address format. Expected hostname or hostname:port`  
Or  
`TDE: Failed to register Key Store with URL: KMS_URL, error code: 3, error message: Invalid CipherTrust address format. Expected hostname or hostname:port` | Invalid KMS address format | Occurs when the KMS address part of the URL is incorrectly formatted. For example, if it includes the protocol scheme again, such as `vault://https://vault.example.com:8200/...` or `ciphertrust://https://ciphertrust.example.com:443/...`.  
`TDE: Failed to read KEK, error code: 3, error message: Invalid key path format. Must start with '/', not end with '/', and contain only valid characters` | Invalid key path format | Occurs when the path part of the KMS URL is malformed. The path must start with a forward slash `/` and must not end with a trailing slash.  
`TDE: Failed to register Key Store with URL: KMS_URL, error code: 13, error message: curl_easy_perform() failed: Could not resolve hostname` | Hostname resolution failure | Occurs when the KMS hostname in the KEK URL can't be resolved. This can happen if the URL is malformed or if there is a DNS configuration issue.  
  
#### Recommended fix

  * Verify KEK URL scheme: Make sure that the URL starts with `vault://` (for HashiCorp Vault) or `ciphertrust://` (for Thales CipherTrust Manager). Don't use `https://` as the prefix. 
    * Correct (Vault): `vault://vault.example.com:8200/v1/secret/data/key`
    * Correct (CipherTrust): `ciphertrust://ciphertrust.example.com:443/api/v1/vault/secrets/key`
    * Incorrect: `https://vault.example.com:8200/v1/secret/data/key`
  * Check address format: Make sure that the host and port are correctly specified immediately after the `vault://` or `ciphertrust://` prefix.
  * Verify path formatting: Make sure that the path starts with `/` and doesn't have a trailing slash (for example, use `/v1/secret/data/key` for HashiCorp Vault or `/api/v1/vault/secrets/key` for Thales CipherTrust Manager, without a trailing `/`).
  * Verify host resolution: Make sure that the KMS hostname specified in the URL is correct and that it can be resolved from within the database pod.



### KEK not base64-encoded

If the KEK stored in your external KMS isn't correctly base64-encoded, AlloyDB Omni fails to decode it upon retrieval. This prevents it from unwrapping the local Data Encryption Keys (DEKs) and causes a boot failure.

#### Description

You might see errors like the following in the database diagnostic logs (`postgresql.log`):

Error | Description | Reason  
---|---|---  
`TDE: Failed to read KEK, error code: 13, error message: Error decoding base64 key string` | Error decoding base64 key string | Occurs when the key manager attempts to decode the retrieved secret from the KMS using Base64, but the string isn't valid Base64.  
  
#### Recommended fix

  * Retrieve KEK value: Retrieve and inspect the KEK value directly from your KMS (HashiCorp Vault or Thales CipherTrust Manager).
  * Update value in KMS: Make sure that the KEK stored in your KMS is base64-encoded. If it is stored as raw binary or plain text, update the value in the KMS with its base64-encoded equivalent. 
    1. Convert the raw key to Base64: 
           
           echo -n "RAW_KEY" | base64

Replace `<var>RAW_KEY</var>` with your unencoded key value.
    2. Update the secret in your KMS to the generated base64-encoded string.



### KEK version missing in KMS

The KEK version missing error occurs when AlloyDB Omni attempts to unwrap local DEKs using a specific historical version of the KEK, but that version is deleted, destroyed, or missing in the external KMS. This is most common during backup restore operations or standby replica initialization.

#### Description

You might see errors like the following in the database diagnostic logs (`postgresql.log`):

Error | Description | Reason  
---|---|---  
`TDE: Failed to read KEK, error code: 5, error message: Vault request failed with HTTP code: 404, Response body: {... "destroyed":true, "version":4 ...}`  
Or  
`TDE: Failed to read KEK, error code: 5, error message: CipherTrust request failed with HTTP code: 404, CipherTrust error: "NCERRResourceNotFound: ..."` | Key version missing or destroyed | The requested KEK version is missing, deleted, or permanently destroyed in the KMS.  
  
#### Recommended fix

  * Verify KEK version in KMS: Make sure that the requested KEK version is present and active (not deleted or destroyed) in your KMS.
  * Restore missing KEK version: Restore or undelete the requested KEK version in your KMS if it has been deleted but not destroyed.
  * Handle destroyed keys: If the requested key version is permanently destroyed in your KMS, the data or backup encrypted under that version is permanently unrecoverable.



### Bad or missing TLS or SSL certificates

The bad or missing TLS or SSL certificate error occurs when AlloyDB Omni can't establish a secure TLS connection to your external KMS (HashiCorp Vault or Thales CipherTrust Manager) because certificates are missing, expired, untrusted, or misconfigured.

#### Description

You might see errors like the following in the database diagnostic logs (`postgresql.log`):

Error | Description | Reason  
---|---|---  
`TDE: Failed to read KEK, error code: 13, error message: curl_easy_perform() failed: SSL peer certificate or SSH remote key was not OK`  
Or  
`TDE: Failed to read KEK, error code: 13, error message: curl_easy_perform() failed: Peer certificate cannot be authenticated with given CA certificates` | KMS server certificate verification failed | The KMS server's certificate can't be verified using the provided CA certificate.  
`TDE: Failed to register Key Store with URL: KMS_URL, error code: 13, error message: curl_easy_perform() failed: Problem with the local SSL certificate` | Local SSL certificate problem | Occurs if a client certificate is required and has issues.  
  
#### Recommended fix

To resolve TLS verification issues, make sure that the correct certificates are supplied, mounted, and readable by the `postgres` user.

Kubernetes expects certificates to be supplied as a Secret mounted into the database pod at `/tde-tls`. To locate and inspect the certificate secret:

  1. Extract the referenced `TdeConfig` name directly from your database cluster:
         
         kubectl get dbcluster CLUSTER_NAME -n NAMESPACE -o jsonpath='{.spec.primarySpec.features.transparentDataEncryption.tdeConfigRef.name}'

  2. Extract the secret name directly from the `TdeConfig` resource:
         
         kubectl get tdeconfig TDE_CONFIG_NAME -n NAMESPACE -o jsonpath='{.spec.tls.certSecret.name}'

  3. Verify that the secret exists and contains the required keys:
         
         kubectl describe secret CERT_SECRET_NAME -n NAMESPACE

  4. Confirm that the secret is correctly mounted and that the files are readable by the `postgres` user:
         
         kubectl exec -it POD_NAME -c database -n NAMESPACE -- ls -la /tde-tls




Replace the following:

  * `CLUSTER_NAME`: the name of your `DBCluster` resource.
  * `NAMESPACE`: the Kubernetes namespace where your `DBCluster` is deployed.
  * `TDE_CONFIG_NAME`: the name of your `TdeConfig` custom resource.
  * `CERT_SECRET_NAME`: the name of the Kubernetes Secret containing your TLS certificates.
  * `POD_NAME`: the name of your database pod.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 

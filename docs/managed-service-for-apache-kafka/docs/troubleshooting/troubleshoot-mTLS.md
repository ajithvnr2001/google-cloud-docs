---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/troubleshooting/troubleshoot-mTLS/
title: Troubleshoot mTLS issues \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:41.802110+00:00
---

# Troubleshoot mTLS issues  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/troubleshooting/troubleshoot-mTLS/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Troubleshoot mTLS issues Stay organized with collections  Save and categorize content based on your preferences. 

This section provides troubleshooting guidance for common issues encountered when configuring and using mTLS with Managed Service for Apache Kafka.

## Errors when updating a cluster

You might encounter the following errors when running a `gcloud managed-kafka clusters update` or `gcloud managed-kafka clusters create` command.

### Invalid SSL principal mapping rule

You receive an error message similar to one of the following:
    
    
    INVALID_ARGUMENT: The request was invalid: invalid SSL principal mapping
    rule: \"RULE:INVALID-RULE\". The rule must be of the format DEFAULT or
    RULE:pattern/replacement/[LU]
    
    
    
    INVALID_ARGUMENT: The request was invalid: invalid SSL principal mapping
    rules: \"RULE:\\nRULE:,DEFAULT\" contains a newline
    

The error messages occur because the value provided for the `ssl-principal-mapping-rules` flag is incorrectly formatted or contains invalid characters.

Correct the rule to match the required format and verify that the rule string does not contain any newline characters. For more information about the `ssl-principal-mapping-rules` flag, see [Principal mapping](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls#principal-mapping).

### Invalid CA pool configuration

You receive an error message similar to one of the following:
    
    
    INVALID_ARGUMENT: The request was invalid:
    ca_pool: project/managed-kafka-test/locations/us-central1/test-ca-pool
    doesn't match the expected format: projects/{project}/locations/{location}/caPools/{caPool}
    
    
    
    INVALID_ARGUMENT: The request was invalid: maximum of 10 CA pools can be specified
    
    
    
    INVALID_ARGUMENT: The request was invalid: duplicate CA pool:
    projects/managed-kafka-test/locations/us-central1/caPools/test-ca-pool.
    All CA pools must be unique
    

The error messages occur because the list of CA pools provided for the `mtls-ca-pools` flag is invalid. Check the list of CA pools and verify the following:

  * All CA pool names use the full resource format: `projects/PROJECT_ID/locations/LOCATION/caPools/CA_POOL_ID`.

  * There are no duplicate CA pools in the list.

  * The total number of CA pools does not exceed 10.




### Cluster does not support mTLS

You receive an error message similar to the following:
    
    
    FAILED_PRECONDITION: Invalid resource state for \"tls_config\": mTLS is not
    supported for this cluster because it was created before the mTLS feature
    was added. Please create a new cluster to use mTLS.
    

The error message occurs because you are attempting to enable mTLS on a cluster that was created before the feature was available. As the error message suggests, you must create a new cluster to use mTLS. You cannot enable mTLS on an existing, ineligible cluster that was created before June 24, 2025.

## Client connection failures

If a client application cannot connect to the mTLS endpoint of the cluster, check for the following common configuration issues:

  * **Incorrect bootstrap address** : verify that you are using the correct bootstrap address. You must use the mTLS bootstrap address, which ends in `9192` not `9092`.

  * **Invalid or incorrect client certificate** : verify that the client certificate is valid, has not expired, and was issued from a CA that resides in one of the CA pools configured on the cluster.

  * **Incorrect client keystore configuration** : confirm that the client application's configuration correctly points to its keystore and truststore files and that the passwords are correct.

  * **Incorrect Kafka ACLs** : verify that you have created the necessary Kafka ACLs for the authenticated principal. Remember that the principal is the certificate's subject name (or mapped alias), prefixed with `User:`. For example, if the subject name is `test-user`, the principal is `User:test-user`.




## Errors in Cloud Logging

The following errors might appear in the cluster's logs, which you can view in Logging. For more information about Logging, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

### Trust store size exceeds maximum

You see a log entry similar to the following:
    
    
    Trust store size X bytes exceeds the maximum allowed size of 1000 KiB
    and cannot be updated.
    

The error message occurs because the total size of all CA certificates in the configured CA pools is larger than the 1000 KiB limit.

Review the certificates in your CA pools to reduce the total size. This might involve removing large or unnecessary certificates or optimizing the CA chains.

### Failed to fetch certificates from CA pool

You see a log entry similar to the following:
    
    
    Managed Service for Apache Kafka failed to fetch certificates from
    CA pool <ca-pool-name>. Error: <error>.
    

The error message occurs the Managed Service for Apache Kafka service agent was unable to retrieve the certificates from the specified CA pool. The error portion of the message provides more detail. A common reason for this failure is missing IAM permissions.

Verify that the Managed Service for Apache Kafka service agent has the **CA Pool Reader** (`roles/privateca.poolReader`) role on the project that contains the CA pool. This is especially important in cross-project setups. For more information about required permissions to configure mTLS, see [Required roles and permissions](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls#roles-permissions-for-mtls).

_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

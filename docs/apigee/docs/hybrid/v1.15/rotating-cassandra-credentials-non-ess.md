---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/rotating-cassandra-credentials-non-ess/
title: Rotating Cassandra credentials in Kubernetes secrets \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:14:40.504921+00:00
---

# Rotating Cassandra credentials in Kubernetes secrets  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/rotating-cassandra-credentials-non-ess/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Rotating Cassandra credentials in Kubernetes secrets Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.15 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.15 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/rotating-cassandra-credentials-non-ess.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/rotating-cassandra-credentials-non-ess.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/rotating-cassandra-credentials-non-ess.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/rotating-cassandra-credentials-non-ess.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/rotating-cassandra-credentials-non-ess.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/rotating-cassandra-credentials-non-ess.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/rotating-cassandra-credentials-non-ess.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/rotating-cassandra-credentials-non-ess.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/rotating-cassandra-credentials-non-ess.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/rotating-cassandra-credentials-non-ess.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/rotating-cassandra-credentials-non-ess.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/rotating-cassandra-credentials-non-ess.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/rotating-cassandra-credentials-non-ess.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/rotating-cassandra-credentials-non-ess.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/rotating-cassandra-credentials-non-ess.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/rotating-cassandra-credentials-non-ess.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/rotating-cassandra-credentials-non-ess.html)



##  Rotating Cassandra secrets in Kubernetes secrets 

This procedure describes rotating Cassandra credentials in Kubernetes secrets in your cluster. For rotating credentials within Hashicorp Vault, see [Rotating Cassandra credentials in Hashicorp Vault](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/rotating-cassandra-credentials-in-vault). 

This procedure will enable you to rotate the Cassandra credentials used for production Apigee Hybrid services without causing downtime by automating and triggering three tasks: 

  * Rotation of user credentials
  * Rollback of the rotation
  * Cleanup of old and new credentials



## Rotate Cassandra secrets in Kubernetes secrets

There are six Cassandra credential pairs (username+password) that can be rotated:

  * Default*
  * Admin
  * DDL
  * DML
  * JMX
  * Jolokia

*** Note:** You can only rotate the password for the default Cassandra user. The username cannot be changed.

### Prepare for credential rotation

To perform these steps, you must have permission to run `kubectl apply -f` within the cluster. 

  1. Backup the Cassandra database. This backup is to ensure recovery is possible to pre-rotated credentials. See [Cassandra backup overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/cassandra-backup-overview). 
  2. Make sure the cluster is in a healthy state, that all Apigee resources are running and no state changes are pending. 



### Single region credential rotation

  1. Create a new Kubernetes secret in your Apigee namespace which holds the Cassandra user credentials you want to rotate, following [Setting usernames and passwords in a Kubernetes secret](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/cassandra-tls#setting-usernames-and-passwords-in-a-kubernetes-secret). 
  2. Perform the rotation precheck. 
     1. Create a new SecretRotation custom resource using the following template: 
            
            # rotation-k8s-secrets.yaml
            
            apiVersion: apigee.cloud.google.com/v1alpha1
            kind: SecretRotation
            metadata:
              name: ROTATION_NAME
              namespace: APIGEE_NAMESPACE
            spec:
              organizationId: APIGEE_ORG
              rotationId: ROTATION_ID
              timeoutMinutes: TIMEOUT_MINUTES # optional. 480 recommended.
              precheck: true
              cassandra:
                oldSecretRef: OLD_SECRET_REF
                newSecretRef: NEW_SECRET_REF
                jobType: ROTATE
            

Where:

        * ROTATION_NAME: A name for the rotation job, for example: `sr-1-precheck`.
        * APIGEE_NAMESPACE: your Apigee namespace.
        * APIGEE_ORG: Your Apigee organization ID.
        * ROTATION_ID: A custom identifier, for example: `rot-1-precheck`.
        * TIMEOUT_MINUTES: Optional. Overrides the default (480m == 8hr). <=0 means infinite timeout.
        * PRECHECK : Triggers dry-run execution. When set to true, the rotation process goes through all the steps except actually applying the new credentials.
        * OLD_SECRET_REF: The secret name currently being used by the `apigeedatastore`. You can find this using the following command: 
              
              kubectl -n APIGEE_NAMESPACE get apigeedatastore default -o jsonpath='{.spec.credentialRef}'
              

        * NEW_SECRET_REF: The secret name created in the previous step.
     2. Trigger the rotation precheck job by applying the rotation YAML file: 
            
            kubectl -n APIGEE_NAMESPACE apply -f ROTATION_YAML_FILE
            

  3. Check the job status and wait for it to complete. 
         
         kubectl -n APIGEE_NAMESPACE describe sr ROTATION_NAME
         

When the job is finished, the output will contain: 
         
         Status:
           Message:  rotation complete
           State:    complete

**Tip:** You can also view the logs while the job is running with the following command:
         
         kubectl -n APIGEE_NAMESPACE logs sr-ROTATION_ID-rotate-job-HASH
         



* When the rotation precheck job completes, perform the rotation: 

  1. Make the following changes in the rotation YAML file: 
     * Change the `metadata.name` to a name indicating this is not a precheck, for example: `sr-1`.
     * Set `spec.precheck` to `false`.
     * Change `spec.rotationId` to a new identifier, for example: `rot-1`.
  2. Apply the file again to perform the rotation. 
         
         kubectl -n APIGEE_NAMESPACE apply -f ROTATION_YAML_FILE
         



* Once the rotation job completes, validate that traffic is still flowing correctly.
* After validating your traffic, perform the cleanup of the old secrets. **Caution:** Once you trigger the cleanup job, you will not be able to perform a rollback to revert the rotation process and leave the cluster in its original state. See Rolling back a rotation.

  1. Make the following changes in the rotation YAML file: 
     * Change the `metadata.name` to a name indicating this is a cleanup job, for example: `sr-1-cleanup`.
     * Set `spec.cassandra.jobType` to `CLEANUP`.
     * Ensure `spec.precheck` is set to `false`.
  2. Apply the file again to perform the cleanup. 
         
         kubectl -n APIGEE_NAMESPACE apply -f ROTATION_YAML_FILE
         

  3. Check the job status and wait for it to complete. 
         
         kubectl -n APIGEE_NAMESPACE describe sr ROTATION_NAME
         

When the cleanup job is completed, the rotation process is complete.



* Update your overrides file and set `cassandra.auth.secret` to the new secret name (`newSecretRef`). 
    
    
    cassandra:
      auth:
        secret: NEW_SECRET_REF

* Take a backup of the Cassandra database. This backup is to ensure recovery is possible to post-rotated credentials. 
* Delete the old Cassandra credential secret. 

### Multi-region credential rotation

  1. in each region, create a new Kubernetes secret in the your Apigee namespace which holds the Cassandra user credentials you want to rotate, following [Setting usernames and passwords in a Kubernetes secret](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/cassandra-tls#setting-usernames-and-passwords-in-a-kubernetes-secret). 

The credentials must be the same in each region.

  2. Perform the rotation precheck. 
     1. Create a new SecretRotation custom resource using the following template: 
            
            # rotation-k8s-secrets.yaml
            
            apiVersion: apigee.cloud.google.com/v1alpha1
            kind: SecretRotation
            metadata:
              name: ROTATION_NAME
              namespace: APIGEE_NAMESPACE
            spec:
              organizationId: APIGEE_ORG
              rotationId: ROTATION_ID
              timeoutMinutes: TIMEOUT_MINUTES # optional. 480 recommended.
              precheck: true
              cassandra:
                oldSecretRef: OLD_SECRET_REF
                newSecretRef: NEW_SECRET_REF
                jobType: ROTATE
            

Where:

        * ROTATION_NAME: A name for the rotation job, for example: `sr-1-precheck`.
        * APIGEE_NAMESPACE: your Apigee namespace.
        * APIGEE_ORG: Your Apigee organization ID.
        * ROTATION_ID: A custom identifier, for example: `rot-1-precheck`.
        * TIMEOUT_MINUTES: Optional. Overrides the default (480m == 8hr). <=0 means infinite timeout.
        * PRECHECK : Triggers dry-run execution. When set to true, the rotation process goes through all the steps except actually applying the new credentials.
        * OLD_SECRET_REF: The secret name currently being used by the `apigeedatastore`. You can find this using the following command: 
              
              kubectl -n APIGEE_NAMESPACE get apigeedatastore default -o jsonpath='{.spec.credentialRef}'
              

        * NEW_SECRET_REF: The secret name created in the previous step.
     2. In the first region, trigger the rotation precheck job by applying the rotation YAML file: 
            
            kubectl -n APIGEE_NAMESPACE apply -f ROTATION_YAML_FILE
            

  3. Check the job status and wait for it to complete. 
         
         kubectl -n APIGEE_NAMESPACE describe sr ROTATION_NAME
         

When the job is finished, the output will contain: 
         
         Status:
           Message:  rotation complete
           State:    complete

**Tip:** You can also view the logs while the job is running with the following command:
         
         kubectl -n APIGEE_NAMESPACE logs sr-ROTATION_ID-rotate-job-HASH
         



* When the rotation precheck job completes, perform the rotation in the same region: 

  1. Make the following changes in the rotation YAML file: 
     * Change the `metadata.name` to a name indicating this is not a precheck, for example: `sr-1`.
     * Set `spec.precheck` to `false`.
     * Change `spec.rotationId` to a new identifier, for example: `rot-1`.
  2. Apply the file again to perform the rotation. 
         
         kubectl -n APIGEE_NAMESPACE apply -f ROTATION_YAML_FILE
         



* Once the rotation job completes, validate that traffic is still flowing correctly.
* Repeat the rotation steps for the remaining regions.
* After validating your traffic, perform the cleanup of the old secrets. You only need to perform the cleanup in a single region. It does not matter which region you choose. **Caution:** Once you trigger the cleanup job, you will not be able to perform a rollback to revert the rotation process and leave the cluster in its original state. See Rolling back a rotation.

  1. Make the following changes in the rotation YAML file: 
     * Change the `metadata.name` to a name indicating this is a cleanup job, for example: `sr-1-cleanup`.
     * Set `spec.cassandra.jobType` to `CLEANUP`.
     * Ensure `spec.precheck` is set to `false`.
  2. Apply the file again to perform the cleanup. 
         
         kubectl -n APIGEE_NAMESPACE apply -f ROTATION_YAML_FILE
         

  3. Check the job status and wait for it to complete. 
         
         kubectl -n APIGEE_NAMESPACE describe sr ROTATION_NAME
         

When the cleanup job is completed, the rotation process is complete.



* Update your overrides file and set `cassandra.auth.secret` to the new secret name (`newSecretRef`). 
    
    
    cassandra:
      auth:
        secret: NEW_SECRET_REF

* Take a backup of the Cassandra database. This backup is to ensure recovery is possible to post-rotated credentials. 
* Delete the old Cassandra credential secret. 

## Rolling back a rotation

**Note:** You can only roll back a rotation before the cleanup job has been triggered.

Perform the following steps in each region.

  1. Create a new SecretRotation custom resource using the following template: 
         
         # rollback-k8s-secrets.yaml
         
         apiVersion: apigee.cloud.google.com/v1alpha1
         kind: SecretRotation
         metadata:
           name: ROLLBACK_NAME
           namespace: APIGEE_NAMESPACE
         spec:
           organizationId: APIGEE_ORG
           rotationId: ROTATION_ID # match the current rotation.
           timeoutMinutes: TIMEOUT_MINUTES # optional.
           precheck: **false**
           cassandra:
             oldSecretRef: OLD_SECRET_REF # Must match the previous oldSecretRef.
             newSecretRef: NEW_SECRET_REF # Must match the previous newSecretRef.
             jobType: **ROLLBACK**
         

Where:

     * ROLLBACK_NAME: A name for the rollback job, for example: `sr-1-rollback`.
     * APIGEE_NAMESPACE: your Apigee namespace.
     * APIGEE_ORG: Your Apigee organization ID.
     * ROTATION_ID: The id of the current rotation that you are rolling back, for example: `rot-1`.
     * TIMEOUT_MINUTES: Optional. Overrides the default (480m == 8hr). <=0 means infinite timeout.
     * OLD_SECRET_REF: This must match the secret name for `oldSecretRef:` in the rotation YAML file you used in Single region rotation or Multi-region rotation procedure.
     * NEW_SECRET_REF: this must match the secret name for `newSecretRef:` in the rotation YAML file you used in Single region rotation or Multi-region rotation procedure.
  2. Apply the rollback: 
         
         kubectl -n APIGEE_NAMESPACE apply -f ROLLBACK_YAML_FILE
         

  3. Check the job status and wait for it to complete. 
         
         kubectl -n APIGEE_NAMESPACE describe sr ROTATION_NAME
         

  4. When the rollback(s) complete, verify that traffic is still flowing correctly. 
  5. When the traffic is flowing correctly, repeat the rollback process in each remaining region.
  6. Once you have completed the rollback and verified that traffic is still flowing correctly, start the cleanup process. You only need to perform the cleanup in a single region. It does not matter which region you choose. 

Make the following changes in the rotation YAML file:

     * Change `metadata.name` to a name indicating this is a cleanup job, for example: `sr-1-cleanup-rollback`.
     * Change `spec.cassandra.jobType` to `CLEANUP_ROLLBACK`.
  7. Apply the file to trigger the cleanup job: 
         
         kubectl -n APIGEE_NAMESPACE apply -f ROTATION_YAML_FILE
         

  8. Check the job status and wait for it to complete. 
         
         kubectl -n APIGEE_NAMESPACE describe sr ROTATION_NAME
         

When the cleanup job is completed, the rollback process is complete.

  9. Update your overrides file and set `cassandra.auth.secret` to the old secret name (`oldSecretRef`). 
         
         cassandra:
           auth:
             secret: OLD_SECRET_REF




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

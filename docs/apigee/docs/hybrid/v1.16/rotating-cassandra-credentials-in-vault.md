---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/rotating-cassandra-credentials-in-vault/
title: Rotating Cassandra credentials in Hashicorp Vault \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:25:12.147218+00:00
---

# Rotating Cassandra credentials in Hashicorp Vault  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/rotating-cassandra-credentials-in-vault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Rotating Cassandra credentials in Hashicorp Vault Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/rotating-cassandra-credentials-in-vault.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/rotating-cassandra-credentials-in-vault.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/rotating-cassandra-credentials-in-vault.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/rotating-cassandra-credentials-in-vault.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/rotating-cassandra-credentials-in-vault.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/rotating-cassandra-credentials-in-vault.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/rotating-cassandra-credentials-in-vault.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/rotating-cassandra-credentials-in-vault.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/rotating-cassandra-credentials-in-vault.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/rotating-cassandra-credentials-in-vault.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/rotating-cassandra-credentials-in-vault.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/rotating-cassandra-credentials-in-vault.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/rotating-cassandra-credentials-in-vault.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/rotating-cassandra-credentials-in-vault.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/rotating-cassandra-credentials-in-vault.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/rotating-cassandra-credentials-in-vault.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/rotating-cassandra-credentials-in-vault.html)



##  Overview 

This procedure describes rotating Cassandra credentials within Hashicorp Vault. For rotating credentials in Kubernetes secrets in your cluster, see [Rotating Cassandra credentials in Kubernetes secrets](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/rotating-cassandra-credentials-non-ess). 

This feature allows platform administrators to:

  * Rotate Cassandra credentials in Hashicorp Vault.
  * Roll back to the previous Cassandra credentials in Vault in case of any issues during password rotation.
  * Rotate the Cassandra password for one region at a time, so that you can ensure minimal impact on service availability and maintain control over the rotation process.
  * Track the start, progress, and completion of the rotation for a single region.



This feature is available in Apigee Hybrid 1.13.1 and later. 

**Note:** Before using this feature, you must have Vault storage of Cassandra credentials set up. Follow the instructions in [Storing Cassandra secrets in Hashicorp Vault](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-cassandra-secrets-in-vault)

##  Before you begin 

Before setting up credential rotation: 

  * Backup your Cassandra database. This backup is to ensure recovery is possible to pre-rotated credentials. 
  * Ensure the cluster is in a healthy state (i.e. all Apigee resources are running, no state changes are pending). 

**Note:** You must have permission to run `kubectl apply -f` within the cluster to set up credential rotation.

## Single region setup

  1. Create a new `SecretProviderClass` Kubernetes resource in your Apigee namespace for the new Cassandra credentials. See [Storing Cassandra secrets in Hashicorp Vault](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-cassandra-secrets-in-vault#create-secretproviderclass-object) for a template to use. This allows a Vault role to access secrets within the Kubernetes namespaces. 
  2. Create a new `SecretRotation` custom resource using the following template: 
         
         # rotation.yaml
         
         apiVersion: apigee.cloud.google.com/v1alpha1
         kind: SecretRotation
         metadata:
           name: ROTATION_PROCESS_NAME
           namespace: APIGEE_NAMESPACE
         spec:
           organizationId: ORG_NAME
           rotationId: ROTATION_ID
           timeoutMinutes: 480 # optional. overrides the default (480m == 8hr).
                               # less than or equal to 0 means infinite timeout.
           precheck: true
           cassandra:
             oldSecretProviderClass: OLD_SPC_NAME
             newSecretProviderClass: NEW_SPC_NAME
             jobType: ROTATE
         

     * ROTATION_PROCESS_NAME: A unique name for the rotation job. You will need to set `metadata.name` to a unique value for the rotation precheck job and again for the rotation job. For example `sr-1-precheck` followed by `sr-1`.
     * ROTATION_ID: Set `spec.rotationId` to a custom identifier, for example `rotation-1-precheck`.
     * NEW_SPC_NAME: Set `spec.cassandra.newSecretProviderClass` to the new secret provider class name you created in the previous step.
     * OLD_SPC_NAME: Set `spec.cassandra.oldSecretProviderClass` to the SPC name currently being used by the `ApigeeDatastore`.
  3. Trigger the rotation precheck job by applying the `rotation.yaml` file. 
         
         kubectl -n APIGEE_NAMESPACE apply -f rotation.yaml

  4. Check the job status to verify when the precheck job is complete. 
         
         kubectl -n APIGEE_NAMESPACE get job sr-(rotationId)-(rotate|rollback|cleanup)-job

**Tip:** You can also view the logs while the job is running. 
         
         kubectl -n APIGEE_NAMESPACE logs sr-(rotationId)-(rotate|rollback|cleanup)-job-(hash)

  5. Once the rotation precheck job completes, change the value of `metadata.name` and set `spec.precheck` to `false`. Apply the file again to perform the rotation. 
         
         kubectl -n APIGEE_NAMESPACE apply -f rotation.yaml

  6. After the rotation job completes and you have validated traffic is still flowing correctly, clean up the process with the following two steps: 
     1. Update the value of `metadata.name` and set `spec.cassandra.jobType` to `CLEANUP`. 
     2. Trigger the cleanup job by applying the file. 
            
            kubectl -n APIGEE_NAMESPACE apply -f rotation.yaml

**Note:** Up until this step, you can trigger a rollback job to revert the rotation process and leave the cluster in its original state.

When the cleanup job is completed, the rotation process is complete.

  7. Update your overrides file and set `cassandra.auth.secretProviderClass` to the new secret provider class (`newSecretProviderClass`). 
         
         cassandra:
           auth:
             secretProviderClass: NEW_SPC_NAME

  8. Backup your Cassandra database. This backup is to ensure recovery is possible to post-rotated credentials. 
  9. Delete the old Cassandra credentials, role, and policy from Vault. 



## Multi-region setup

The multi-region setup procedures are divided into two sections: setup for the first region and setup for the remaining regions.

  1. Complete the following steps in the first region before starting the subsequent regions. 
     1. Create a new `SecretProviderClass` Kubernetes resource in the `APIGEE_NAMESPACE` namespace for the new Cassandra credentials. See [Storing Cassandra secrets in Hashicorp Vault](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-cassandra-secrets-in-vault#create-secretproviderclass-object) for a template to use. This allows a Vault role to access secrets within the Kubernetes namespaces. 
     2. Create a new `SecretRotation` custom resource using the following template: 
            
            # rotation.yaml
            
            apiVersion: apigee.cloud.google.com/v1alpha1
            kind: SecretRotation
            metadata:
              name: ROTATION_PROCESS_NAME
              namespace: APIGEE_NAMESPACE
            spec:
              organizationId: ORG_NAME
              rotationId: ROTATION_ID
              timeoutMinutes: -1 # this value is required and should not be changed.
              precheck: true
              cassandra:
                oldSecretProviderClass: OLD_SPC_NAME
                newSecretProviderClass: NEW_SPC_NAME
                jobType: ROTATE
            

        * ROTATION_PROCESS_NAME: A unique name for the rotation job. You will need to set `metadata.name` to a unique value for the rotation precheck job and again for the rotation job. For example `sr-1-precheck` followed by `sr-1`.
        * ROTATION_ID: Set `spec.rotationId` to a custom identifier, for example `rotation-1-precheck`.
        * NEW_SPC_NAME: Set `spec.cassandra.newSecretProviderClass` to the new secret provider class name you created in the previous step.
        * OLD_SPC_NAME: Set `spec.cassandra.oldSecretProviderClass` to the SPC name currently being used by the `ApigeeDatastore`.
     3. Trigger the rotation precheck job by applying the `rotation.yaml` file. 
            
            kubectl -n APIGEE_NAMESPACE apply -f rotation.yaml

     4. Check the job status to verify when the precheck job is complete. 
            
            kubectl -n APIGEE_NAMESPACE get job sr-(rotationId)-(rotate|rollback|cleanup)-job

**Tip:** You can also view the logs while the job is running. 
            
            kubectl -n APIGEE_NAMESPACE logs sr-(rotationId)-(rotate|rollback|cleanup)-job-(hash)

     5. Once the rotation precheck job completes: 
        * Change the value of `metadata.name`, for example from `sr-1-precheck` to `sr-1`.
        * Set `spec.precheck` to `false` to turn off the precheck and perform the rotation.
        * Set `spec.rotationId` to a new identifier, for example `rotation-1`.
     6. Apply the file again to perform the rotation. 
            
            kubectl -n APIGEE_NAMESPACE apply -f rotation.yaml

     7. Check the state of the `SecretRotation` and wait until it is `complete`. 
            
            kubectl -n APIGEE_NAMESPACE get sr SR_NAME

  2. In each subsequent region, complete the following steps: 
     1. Create a new `SecretProviderClass` Kubernetes resource in your Apigee namespace for the new Cassandra credentials. See [Storing Cassandra secrets in Hashicorp Vault](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-cassandra-secrets-in-vault#create-secretproviderclass-object) for a template to use. This should be the same definition as step 1a. 
     2. Update your `overrides.yaml` and set `cassandra.auth.secretProviderClass` to the match the value of `spec.cassandra.newSecretProviderClass` in the `rotation.yaml` file. 
            
            cassandra:
              auth:
                secretProviderClass: NEW_SPC_NAME

     3. Apply the operator chart: 
            
            helm upgrade operator apigee-operator/ \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f OVERRIDES_FILE

     4. A new `ReplicaSet` will be created. Check that the new controller-manager pods are using the new SPC: 
            
            export POD=NEW_CONTROLLER_MANAGER_POD_NAME
            kubectl -n APIGEE_NAMESPACE get pods $POD -o jsonpath='{.spec.volumes[?(@.name=="apigee-external-secrets")].csi.volumeAttributes.secretProviderClass}'
            

The result should match the value you set for `spec.cassandra.newSecretProviderClass` in `rotation.yaml`, for example: 
            
            kubectl -n apigee get pods $POD -o jsonpath='{.spec.volumes[?(@.name=="apigee-external-secrets")].csi.volumeAttributes.secretProviderClass}'
            
            my-new-spc

     5. Apply the datastore chart: 
            
            helm upgrade datastore apigee-datastore/ \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f OVERRIDES_FILE

**Note:** Applying the datastore chart will also trigger releases for the organization and environments. 
     6. The datastore will go into a releasing state. Wait until the datastore has finished releasing and is in the running state. 
            
            kubectl -n APIGEE_NAMESPACE get apigeedatastore DATASTORE_NAME

DATASTORE_NAME is `default` in most installations.

     7. Check that the new datastore pods are using the new SPC: 
            
            export POD=NEW_DATASTORE_POD_NAME
            kubectl -n APIGEE_NAMESPACE get pods $POD -o jsonpath='{.spec.volumes[?(@.name=="apigee-external-secrets")].csi.volumeAttributes.secretProviderClass}'
            

The result should match the value you set for `spec.cassandra.newSecretProviderClass` in `rotation.yaml`, for example: 
            
            kubectl -n apigee get pods $POD -o jsonpath='{.spec.volumes[?(@.name=="apigee-external-secrets")].csi.volumeAttributes.secretProviderClass}'
            
            my-new-spc

     8. Wait until the organization and environments are done releasing and have returned to the running state. 
            
            kubectl -n APIGEE_NAMESPACE get apigeeorg ORG_NAME
            kubectl -n APIGEE_NAMESPACE get apigeeenv ENV_NAME

     9. Check that the new MART, runtime, and synchronizer pods are using the new SPC: 
            
            export POD=NEW_MART_POD_NAME
            kubectl -n APIGEE_NAMESPACE get pods $POD -o jsonpath='{.spec.volumes[?(@.name=="apigee-external-secrets")].csi.volumeAttributes.secretProviderClass}'
            export POD=NEW_RUNTIME_POD_NAME
            kubectl -n APIGEE_NAMESPACE get pods $POD -o jsonpath='{.spec.volumes[?(@.name=="apigee-external-secrets")].csi.volumeAttributes.secretProviderClass}'
            export POD=NEW_SYNCHRONIZER_POD_NAME
            kubectl -n APIGEE_NAMESPACE get pods $POD -o jsonpath='{.spec.volumes[?(@.name=="apigee-external-secrets")].csi.volumeAttributes.secretProviderClass}'
            

The result should match the value you set for `spec.cassandra.newSecretProviderClass` in `rotation.yaml`, for example: 
            
            kubectl -n apigee get pods $POD -o jsonpath='{.spec.volumes[?(@.name=="apigee-external-secrets")].csi.volumeAttributes.secretProviderClass}'
            
            my-new-spc

  3. After completing the steps in every region and validate traffic is still flowing correctly, clean up the process in the first region with the following two steps: 
     1. In the first region, update the value of `metadata.name` and set `spec.cassandra.jobType` to `CLEANUP`. 
     2. Trigger the cleanup job by applying the file. 
            
            kubectl -n APIGEE_NAMESPACE apply -f rotation.yaml

     3. Check the job status and watch the job logs to verify when the cleanup job is complete.

When the cleanup job is completed, the rotation process is complete.

  4. Update your overrides file and set `cassandra.auth.secretProviderClass` to the new secret provider class (`newSecretProviderClass`). 
         
         cassandra:
           auth:
             secretProviderClass: NEW_SPC_NAME

  5. Backup your Cassandra database. This backup is to ensure recovery is possible to post-rotated credentials. 
  6. Delete the old Cassandra credentials, role, and policy from Vault. 



## Rolling back a rotation

**Note:** You can only roll back a rotation before the cleanup job has been triggered.

For multi-region, perform the rollback in each region.

  1. Create a new SecretRotation custom resource using the following template: 
         
         # rollback-rotation.yaml
         
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
             oldSecretProviderClass: OLD_SPC_NAME # Must match the previous oldSecretProviderClass.
             newSecretProviderClass: NEW_SPC_NAME # Must match the previous newSecretProviderClass.
             jobType: **ROLLBACK**
         

Where:

     * ROLLBACK_NAME: A name for the rollback job, for example: `sr-1-rollback`.
     * APIGEE_NAMESPACE: your Apigee namespace.
     * APIGEE_ORG: Your Apigee organization ID.
     * ROTATION_ID: The id of the current rotation that you are rolling back, for example: `rot-1`.
     * TIMEOUT_MINUTES: Optional. Overrides the default (480m == 8hr). <=0 means infinite timeout.
     * OLD_SPC_NAME: This must match the secret name for `oldSecretProviderClass:` in the rotation YAML file you used in Single region setup or Multi-region setup procedure.
     * NEW_SPC_NAME: this must match the secret name for `newSecretProviderClass:` in the rotation YAML file you used in Single region setup or Multi-region setup procedure.
  2. Apply the rollback: 
         
         kubectl -n APIGEE_NAMESPACE apply -f ROLLBACK_YAML_FILE
         

  3. Check the job status and wait for it to complete. 
         
         kubectl -n APIGEE_NAMESPACE describe sr ROTATION_NAME
         

  4. When the rollback(s) complete, verify that traffic is still flowing correctly. 
  5. For multi-region installations, when the traffic is flowing correctly, repeat the rollback process in each region.
  6. Once you have completed the rollback and verified that traffic is still flowing correctly in all regions, start the cleanup process. 

Make the following changes in the rotation YAML file:

     * Change `metadata.name` to a name indicating this is a cleanup job, for example: `sr-1-cleanup-rollback`.
     * Change `spec.cassandra.jobType` to `CLEANUP_ROLLBACK`.
  7. Apply the file to trigger the cleanup job: 
         
         kubectl -n APIGEE_NAMESPACE apply -f ROTATION_YAML_FILE
         

  8. Check the job status and wait for it to complete. 
         
         kubectl -n APIGEE_NAMESPACE describe sr ROTATION_NAME
         

When the cleanup job is completed, the rollback process is complete.

  9. Update your overrides file and set `cassandra.auth.secretProviderClass` to the old secret provider class (`oldSecretProviderClass`). 
         
         cassandra:
           auth:
             secretProviderClass: OLD_SPC_NAME




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
